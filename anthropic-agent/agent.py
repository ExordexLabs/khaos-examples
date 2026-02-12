#!/usr/bin/env python3
"""Anthropic Agent Example — Direct SDK integration with tool use.

Demonstrates:
- Anthropic Claude with tool use blocks
- System prompts and message API patterns
- Token tracking and cost estimation
- Zero-instrumentation Khaos integration
"""

from __future__ import annotations

import os
from typing import Any

from anthropic import Anthropic

from khaos import khaosagent

# Initialize Anthropic client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def get_weather(location: str, unit: str = "fahrenheit") -> dict[str, Any]:
    """Mock weather tool for demonstration."""
    return {
        "location": location,
        "temperature": 72,
        "unit": unit,
        "forecast": "sunny",
    }


def search_web(query: str) -> dict[str, Any]:
    """Mock web search tool for demonstration."""
    return {
        "query": query,
        "results": [
            {"title": "Result 1", "snippet": "Example search result"},
            {"title": "Result 2", "snippet": "Another example result"},
        ],
    }


# Tool definitions for Claude
TOOLS = [
    {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Temperature unit",
                },
            },
            "required": ["location"],
        },
    },
    {
        "name": "search_web",
        "description": "Search the web for information",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query",
                },
            },
            "required": ["query"],
        },
    },
]

# Map tool names to functions
TOOL_MAP = {
    "get_weather": get_weather,
    "search_web": search_web,
}


@khaosagent(
    name="anthropic-example",
    version="1.0.0",
    description="Claude agent with tool use",
    category="llm_inference",
    capabilities=["llm", "tool-calling"],
    framework="anthropic",
)
def main(prompt: str) -> dict[str, Any]:
    """Handle a prompt with Claude and optional tool use.

    Args:
        prompt: User input prompt

    Returns:
        Dict with response text and metadata
    """
    messages = [{"role": "user", "content": prompt}]

    # Initial Claude call with tools
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system="You are a helpful assistant with access to tools. Use them when appropriate.",
        messages=messages,
        tools=TOOLS,
    )

    # Handle tool use if present
    tools_used = []
    while response.stop_reason == "tool_use":
        # Extract tool use blocks
        tool_use_blocks = [block for block in response.content if block.type == "tool_use"]

        if not tool_use_blocks:
            break

        # Add assistant's response to messages
        messages.append({"role": "assistant", "content": response.content})

        # Execute tools and collect results
        tool_results = []
        for tool_use in tool_use_blocks:
            tool_fn = TOOL_MAP.get(tool_use.name)
            if tool_fn:
                result = tool_fn(**tool_use.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": str(result),
                })
                tools_used.append(tool_use.name)

        # Add tool results to messages
        messages.append({"role": "user", "content": tool_results})

        # Get next response
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system="You are a helpful assistant with access to tools. Use them when appropriate.",
            messages=messages,
            tools=TOOLS,
        )

    # Extract final text response
    text_blocks = [block.text for block in response.content if hasattr(block, "text")]
    final_text = " ".join(text_blocks) if text_blocks else ""

    return {
        "response": final_text,
        "model": "claude-3-5-sonnet-20241022",
        "tools_used": tools_used,
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
        },
    }


if __name__ == "__main__":
    # Simple test run
    result = main("What's the weather like in San Francisco?")
    print(f"Response: {result['response']}")
    print(f"Tools used: {result['tools_used']}")
    print(f"Tokens: {result['usage']['input_tokens']} in, {result['usage']['output_tokens']} out")

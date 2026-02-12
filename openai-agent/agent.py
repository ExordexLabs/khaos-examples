#!/usr/bin/env python3
"""OpenAI Agent Example — Direct SDK integration with function calling.

Demonstrates:
- OpenAI GPT-4o-mini with structured function calling
- Tool definitions and invocations
- Token tracking and cost estimation
- Zero-instrumentation Khaos integration
"""

from __future__ import annotations

import os
from typing import Any

from openai import OpenAI

from khaos import khaosagent

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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


# Tool definitions for OpenAI function calling
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
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
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web for information",
            "parameters": {
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
    },
]

# Map tool names to functions
TOOL_MAP = {
    "get_weather": get_weather,
    "search_web": search_web,
}


@khaosagent(
    name="openai-example",
    version="1.0.0",
    description="OpenAI GPT-4o-mini agent with function calling",
    category="llm_inference",
    capabilities=["llm", "tool-calling"],
    framework="openai",
)
def main(prompt: str) -> dict[str, Any]:
    """Handle a prompt with OpenAI GPT-4o-mini and optional tool calls.

    Args:
        prompt: User input prompt

    Returns:
        Dict with response text and metadata
    """
    messages = [{"role": "user", "content": prompt}]

    # Initial LLM call with tools
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
    )

    message = response.choices[0].message
    tool_calls = message.tool_calls or []

    # Handle tool calls if present
    if tool_calls:
        messages.append(message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = eval(tool_call.function.arguments)

            # Execute the tool
            tool_fn = TOOL_MAP.get(function_name)
            if tool_fn:
                tool_result = tool_fn(**function_args)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(tool_result),
                })

        # Get final response after tool execution
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        message = response.choices[0].message

    return {
        "response": message.content,
        "model": "gpt-4o-mini",
        "tools_used": [tc.function.name for tc in tool_calls],
        "usage": {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        },
    }


if __name__ == "__main__":
    # Simple test run
    result = main("What's the weather like in San Francisco?")
    print(f"Response: {result['response']}")
    print(f"Tools used: {result['tools_used']}")
    print(f"Tokens: {result['usage']['total_tokens']}")

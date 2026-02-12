#!/usr/bin/env python3
"""LangGraph Agent Example — Multi-step workflow with state management.

Demonstrates:
- LangGraph StateGraph with multiple nodes
- State management across steps
- Tool node integration
- wrap_langgraph adapter for telemetry
"""

from __future__ import annotations

import os
from typing import Any, Annotated, TypedDict

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from khaos import khaosagent
from khaos.adapters.langgraph import wrap_langgraph


# Define agent state
class AgentState(TypedDict):
    """State passed through the graph."""
    messages: Annotated[list, add_messages]


def get_weather(location: str) -> str:
    """Mock weather tool for demonstration."""
    return f"Weather in {location}: 72°F, sunny"


def search_web(query: str) -> str:
    """Mock web search tool for demonstration."""
    return f"Search results for '{query}': Example result 1, Example result 2"


# Create tools
tools = [get_weather, search_web]

# Create LLM with tools
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
llm_with_tools = llm.bind_tools(tools)


def should_continue(state: AgentState) -> str:
    """Determine if we should continue to tools or end."""
    messages = state["messages"]
    last_message = messages[-1]

    # If there are tool calls, continue to tools
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    # Otherwise end
    return END


def call_model(state: AgentState) -> dict[str, Any]:
    """Agent node that calls the LLM."""
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


# Build the graph
graph_builder = StateGraph(AgentState)

# Add nodes
graph_builder.add_node("agent", call_model)
graph_builder.add_node("tools", ToolNode(tools))

# Add edges
graph_builder.add_edge(START, "agent")
graph_builder.add_conditional_edges("agent", should_continue, ["tools", END])
graph_builder.add_edge("tools", "agent")

# Compile the graph
compiled_graph = graph_builder.compile()

# Wrap with Khaos adapter for telemetry
wrapped_graph = wrap_langgraph(compiled_graph)


@khaosagent(
    name="langgraph-example",
    version="1.0.0",
    description="LangGraph agent with multi-step workflow",
    category="orchestrated",
    capabilities=["llm", "tool-calling", "multi-step"],
    framework="langgraph",
)
def main(prompt: str) -> dict[str, Any]:
    """Execute a multi-step LangGraph workflow.

    Args:
        prompt: User input prompt

    Returns:
        Dict with response text and metadata
    """
    # Invoke the wrapped graph
    result = wrapped_graph.invoke({
        "messages": [{"role": "user", "content": prompt}]
    })

    # Extract final message
    final_message = result["messages"][-1]
    response_text = final_message.content if hasattr(final_message, "content") else str(final_message)

    # Count tool invocations from messages
    tool_calls = []
    for msg in result["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            tool_calls.extend([tc["name"] for tc in msg.tool_calls])

    return {
        "response": response_text,
        "model": "gpt-4o-mini",
        "framework": "langgraph",
        "tools_used": tool_calls,
        "steps": len(result["messages"]),
    }


if __name__ == "__main__":
    # Simple test run
    result = main("What's the weather in San Francisco and search for 'best restaurants'?")
    print(f"Response: {result['response']}")
    print(f"Tools used: {result['tools_used']}")
    print(f"Steps executed: {result['steps']}")

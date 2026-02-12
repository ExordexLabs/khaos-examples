#!/usr/bin/env python3
"""MCP Agent Example — Model Context Protocol tool integration.

Demonstrates:
- MCP server subprocess spawning
- MCP stdio transport communication
- Tool invocation via MCP
- MCP-specific fault injection
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from itertools import count
from typing import Any

from khaos import khaosagent


def spawn_mcp_server() -> subprocess.Popen:
    """Spawn the MCP server subprocess."""
    server_path = os.path.join(os.path.dirname(__file__), "mcp_server.py")
    return subprocess.Popen(
        [sys.executable, server_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=sys.stderr,
        text=True,
    )


def call_mcp_tool(
    proc: subprocess.Popen,
    tool_name: str,
    arguments: dict[str, Any],
    seq_id: int,
) -> dict[str, Any]:
    """Call an MCP tool via stdio transport."""
    if not proc.stdin or not proc.stdout:
        raise RuntimeError("MCP server process missing pipes")

    # Send request
    request = {
        "id": seq_id,
        "tool": tool_name,
        "input": arguments,
    }
    proc.stdin.write(json.dumps(request) + "\n")
    proc.stdin.flush()

    # Read response
    response_line = proc.stdout.readline()
    if not response_line:
        raise RuntimeError("No response from MCP server")

    return json.loads(response_line)


@khaosagent(
    name="mcp-example",
    version="1.0.0",
    description="MCP tool-calling agent",
    category="tool_agent",
    capabilities=["llm", "tool-calling", "mcp"],
    framework="openai",
)
def main(prompt: str) -> dict[str, Any]:
    """Execute MCP tool calls based on prompt.

    Args:
        prompt: User input prompt

    Returns:
        Dict with response and MCP metrics
    """
    server_proc = spawn_mcp_server()
    seq = count(1)
    tool_responses = []
    latencies = []

    try:
        # Determine which tools to call based on prompt
        if "weather" in prompt.lower():
            tools_to_call = [("get_weather", {"location": "San Francisco"})]
        elif "search" in prompt.lower():
            tools_to_call = [("search_web", {"query": prompt})]
        else:
            # Default: call both tools
            tools_to_call = [
                ("get_weather", {"location": "New York"}),
                ("search_web", {"query": prompt}),
            ]

        # Execute MCP tool calls
        for tool_name, arguments in tools_to_call:
            start = time.perf_counter()
            try:
                response = call_mcp_tool(server_proc, tool_name, arguments, next(seq))
                latency_ms = round((time.perf_counter() - start) * 1000, 2)
                latencies.append(latency_ms)

                tool_responses.append({
                    "tool": tool_name,
                    "status": "ok",
                    "latency_ms": latency_ms,
                    "result": response.get("result", response),
                })
            except Exception as exc:
                latency_ms = round((time.perf_counter() - start) * 1000, 2)
                latencies.append(latency_ms)
                tool_responses.append({
                    "tool": tool_name,
                    "status": "error",
                    "latency_ms": latency_ms,
                    "error": str(exc),
                })

        # Compute metrics
        avg_latency = round(sum(latencies) / len(latencies), 2) if latencies else 0.0
        max_latency = round(max(latencies), 2) if latencies else 0.0
        failure_count = sum(1 for tr in tool_responses if tr["status"] == "error")

        # Generate response
        response_parts = []
        for tr in tool_responses:
            if tr["status"] == "ok":
                response_parts.append(f"{tr['tool']}: {tr['result']}")
            else:
                response_parts.append(f"{tr['tool']}: Error - {tr.get('error')}")

        return {
            "response": "\n".join(response_parts),
            "model": "mcp-tools",
            "framework": "mcp",
            "tools_used": [tr["tool"] for tr in tool_responses],
            "metrics": {
                "tool_count": len(tool_responses),
                "failure_count": failure_count,
                "avg_latency_ms": avg_latency,
                "max_latency_ms": max_latency,
            },
            "tool_responses": tool_responses,
        }

    finally:
        # Clean shutdown
        if server_proc:
            server_proc.terminate()
            server_proc.wait(timeout=5)


if __name__ == "__main__":
    # Simple test run
    result = main("What's the weather?")
    print(f"Response: {result['response']}")
    print(f"Tools used: {result['tools_used']}")
    print(f"Metrics: {result['metrics']}")

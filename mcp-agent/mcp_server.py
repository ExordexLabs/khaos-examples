#!/usr/bin/env python3
"""Dummy MCP server for local testing.

Responds to simple tool calls via stdio transport.
"""

from __future__ import annotations

import json
import sys


def main() -> None:
    """Run the MCP server loop."""
    for line in sys.stdin:
        if not line:
            break

        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            continue

        tool_name = request.get("tool", "unknown")
        tool_input = request.get("input", {})

        # Generate mock responses based on tool
        if tool_name == "get_weather":
            location = tool_input.get("location", "unknown")
            result = {
                "location": location,
                "temperature": 72,
                "unit": "fahrenheit",
                "forecast": "sunny",
            }
        elif tool_name == "search_web":
            query = tool_input.get("query", "")
            result = {
                "query": query,
                "results": [
                    {"title": "Result 1", "snippet": "Example result"},
                    {"title": "Result 2", "snippet": "Another example"},
                ],
            }
        else:
            result = {"error": f"Unknown tool: {tool_name}"}

        # Send response
        response = {
            "id": request.get("id"),
            "result": result,
        }
        print(json.dumps(response))
        sys.stdout.flush()


if __name__ == "__main__":
    main()

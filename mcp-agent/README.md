# MCP Agent Example

Model Context Protocol (MCP) tool integration agent with Khaos chaos engineering.

## What This Demonstrates

- - MCP server spawning and management
- - MCP stdio transport
- - Tool discovery and invocation via MCP
- - MCP-specific fault injection
- - Transport-level resilience testing

## Prerequisites

- Python 3.11+
- OpenAI API key

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export OPENAI_API_KEY="your-key-here"

# Run the agent
khaos run agent.py

# Run with chaos testing
khaos run agent.py --pack quickstart

# Run security tests
khaos run agent.py --pack security

# Run custom tests
khaos test tests/
```

## How It Works

The agent spawns an MCP server as a subprocess and communicates via stdio:

```python
# Spawn MCP server
proc = subprocess.Popen(
    ["python", "mcp_server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True,
)

# Call MCP tools
result = call_tool(proc, "tool_name", {"arg": "value"})

@khaosagent(
    name="mcp-example",
    capabilities=["llm", "tool-calling", "mcp"],
)
def main(prompt: str) -> dict:
    # Use MCP tools to fulfill the prompt
    ...
```

Khaos automatically:
- Injects MCP-specific faults (server unavailable, tool failures, corruption)
- Tracks MCP telemetry (latency, errors, tool invocations)
- Tests transport-level resilience

## MCP Faults Tested

- `mcp_server_unavailable` — Server connection failure
- `mcp_tool_failure` — Tool invocation errors
- `mcp_tool_latency` — Delayed tool responses
- `mcp_tool_corruption` — Corrupted response payloads

## Files

- `agent.py` — Agent with MCP integration
- `mcp_server.py` — Dummy MCP server for local testing
- `requirements.txt` — Dependencies
- `scenarios/quickstart.yaml` — Evaluation scenario
- `tests/test_agent.py` — Test suite

## Learn More

- [Model Context Protocol Spec](https://spec.modelcontextprotocol.io)
- [Khaos MCP Integration](https://khaos.dev/docs/guides/framework-compatibility#mcp)

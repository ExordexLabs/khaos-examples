"""Tests for MCP example agent."""

from khaos.testing import khaostest


@khaostest(agent="mcp-example", faults=["mcp_tool_latency", "mcp_tool_failure"])
def test_resilience():
    """Declarative: Khaos drives execution with MCP faults injected."""
    pass


@khaostest(agent="mcp-example", attacks=["prompt_injection"])
def test_security():
    """Declarative: Khaos runs prompt injection attacks."""
    pass


@khaostest(agent="mcp-example")
def test_basic_response(agent):
    """Imperative: Custom assertions on agent behavior."""
    result = agent("What's the weather?")
    assert result.success
    assert "weather" in result.text.lower() or "temperature" in result.text.lower()


@khaostest(agent="mcp-example")
def test_mcp_tool_calling(agent):
    """Test that MCP tool calls work correctly."""
    result = agent("Search for Python tutorials")
    assert result.success
    # Should invoke search_web MCP tool
    assert "search" in result.text.lower() or "result" in result.text.lower()

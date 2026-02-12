"""Tests for Anthropic example agent."""

from khaos.testing import khaostest


@khaostest(agent="anthropic-example", faults=["llm_timeout", "http_error"])
def test_resilience():
    """Declarative: Khaos drives execution with faults injected."""
    pass


@khaostest(agent="anthropic-example", attacks=["prompt_injection"])
def test_security():
    """Declarative: Khaos runs prompt injection attacks."""
    pass


@khaostest(agent="anthropic-example")
def test_basic_response(agent):
    """Imperative: Custom assertions on agent behavior."""
    result = agent("What is 2+2?")
    assert result.success
    assert "4" in result.text or "four" in result.text.lower()


@khaostest(agent="anthropic-example")
def test_tool_use(agent):
    """Test that Claude tool use works correctly."""
    result = agent("What's the weather in New York?")
    assert result.success
    # Should invoke get_weather tool
    assert "weather" in result.text.lower() or "temperature" in result.text.lower()

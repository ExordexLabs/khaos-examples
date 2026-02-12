"""Tests for LangGraph example agent."""

from khaos.testing import khaostest


@khaostest(agent="langgraph-example", faults=["llm_timeout", "http_error"])
def test_resilience():
    """Declarative: Khaos drives execution with faults injected."""
    pass


@khaostest(agent="langgraph-example", attacks=["prompt_injection"])
def test_security():
    """Declarative: Khaos runs prompt injection attacks."""
    pass


@khaostest(agent="langgraph-example")
def test_basic_response(agent):
    """Imperative: Custom assertions on agent behavior."""
    result = agent("What is 2+2?")
    assert result.success
    assert "4" in result.text or "four" in result.text.lower()


@khaostest(agent="langgraph-example")
def test_multi_step_workflow(agent):
    """Test that multi-step graph execution works."""
    result = agent("What's the weather in Boston?")
    assert result.success
    # Should invoke get_weather tool through the graph
    assert "weather" in result.text.lower() or "boston" in result.text.lower()

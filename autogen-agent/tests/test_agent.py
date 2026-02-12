"""Tests for AutoGen example agent."""

from khaos.testing import khaostest


@khaostest(agent="autogen-example", faults=["llm_timeout", "http_error"])
def test_resilience():
    """Declarative: Khaos drives execution with faults injected."""
    pass


@khaostest(agent="autogen-example", attacks=["prompt_injection"])
def test_security():
    """Declarative: Khaos runs prompt injection attacks."""
    pass


@khaostest(agent="autogen-example")
def test_basic_response(agent):
    """Imperative: Custom assertions on agent behavior."""
    result = agent("What is 2+2?")
    assert result.success
    assert "4" in result.text or "four" in result.text.lower()


@khaostest(agent="autogen-example")
def test_conversation_flow(agent):
    """Test that multi-turn conversation works."""
    result = agent("Explain recursion briefly.")
    assert result.success
    assert len(result.text) > 20  # Should have a meaningful response

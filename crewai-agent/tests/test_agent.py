"""Tests for CrewAI example agent."""

from khaos.testing import khaostest


@khaostest(agent="crewai-example", faults=["llm_timeout", "http_error"])
def test_resilience():
    """Declarative: Khaos drives execution with faults injected."""
    pass


@khaostest(agent="crewai-example", attacks=["prompt_injection"])
def test_security():
    """Declarative: Khaos runs prompt injection attacks."""
    pass


@khaostest(agent="crewai-example")
def test_basic_response(agent):
    """Imperative: Custom assertions on agent behavior."""
    result = agent("machine learning")
    assert result.success
    assert len(result.text) > 0


@khaostest(agent="crewai-example")
def test_multi_agent_coordination(agent):
    """Test that multi-agent crew executes properly."""
    result = agent("climate change")
    assert result.success
    # Should produce a summary from both researcher and writer
    assert len(result.text) > 50  # Reasonable summary length

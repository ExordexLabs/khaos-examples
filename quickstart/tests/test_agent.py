"""Tests for quickstart echo assistant."""

from khaos.testing import khaostest


@khaostest(agent="echo-assistant", attacks=["pi-ignore-instructions"])
def test_prompt_injection():
    """See if agent can be manipulated to ignore instructions."""
    pass


@khaostest(agent="echo-assistant")
def test_basic_conversation(agent):
    """Test normal conversation works."""
    result = agent("Hello, how are you?")
    assert result.success
    assert len(result.text) > 10  # Should give a real response

# Anthropic Agent Example

Direct Anthropic SDK agent demonstrating Claude with tool use blocks and Khaos chaos engineering.

## What This Demonstrates

- - Direct Anthropic SDK integration
- - Claude's tool use with system prompts
- - Message API patterns
- - Token tracking and cost estimation
- - Zero-instrumentation fault injection

## Prerequisites

- Python 3.11+
- Anthropic API key

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export ANTHROPIC_API_KEY="your-key-here"

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

The agent uses the `@khaosagent` decorator with Anthropic's Messages API:

```python
@khaosagent(
    name="anthropic-example",
    version="1.0.0",
    description="Claude agent with tool use",
    category="llm_inference",
    capabilities=["llm", "tool-calling"],
    framework="anthropic",
)
def main(prompt: str) -> dict:
    # Anthropic client call with tools
    response = client.messages.create(...)
    return {"response": response.content[0].text}
```

Khaos automatically:
- Injects faults during testing
- Captures Claude-specific telemetry
- Runs security attacks
- Tracks tool use blocks

## What's Being Tested

### Resilience
- LLM timeout handling
- HTTP error recovery
- Rate limit backoff
- Tool timeout handling

### Security
- Prompt injection resistance
- Tool misuse prevention
- System prompt extraction attempts
- Authorization bypasses

## Files

- `agent.py` — Agent implementation
- `requirements.txt` — Dependencies
- `scenarios/quickstart.yaml` — Evaluation scenario
- `tests/test_agent.py` — Test suite

## Learn More

- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
- [Claude Tool Use Guide](https://docs.anthropic.com/claude/docs/tool-use)
- [Khaos Documentation](https://khaos.dev/docs)

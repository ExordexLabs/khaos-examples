# OpenAI Agent Example

Direct OpenAI SDK agent demonstrating GPT-4o-mini with function calling and Khaos chaos engineering.

## What This Demonstrates

- - Direct OpenAI SDK integration (no framework wrapper)
- - Tool/function calling with structured outputs
- - Token usage tracking
- - Zero-instrumentation fault injection
- - Automatic LLM telemetry capture

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

The agent uses the `@khaosagent` decorator to wrap a simple OpenAI GPT-4o-mini call with function calling:

```python
@khaosagent(
    name="openai-example",
    version="1.0.0",
    description="OpenAI GPT-4o-mini agent with function calling",
    category="llm_inference",
    capabilities=["llm", "tool-calling"],
    framework="openai",
)
def main(prompt: str) -> dict:
    # OpenAI client call with tools
    response = client.chat.completions.create(...)
    return {"response": response.choices[0].message.content}
```

Khaos automatically:
- Injects faults (timeouts, rate limits, errors) during testing
- Captures LLM telemetry (tokens, costs, latency)
- Runs security attacks (prompt injection, jailbreaks)
- Tracks tool invocations

## What's Being Tested

### Resilience (`khaos run --pack resilience`)
- LLM timeout handling
- HTTP error recovery
- Rate limit backoff
- Tool timeout handling

### Security (`khaos run --pack security`)
- Prompt injection resistance
- Tool misuse prevention
- Data extraction attempts
- Authorization bypasses

### Custom Tests (`khaos test tests/`)
- Basic response validation
- Tool calling correctness
- Error handling

## Files

- `agent.py` — Agent implementation
- `requirements.txt` — Dependencies (khaos-agent, openai)
- `scenarios/quickstart.yaml` — Quickstart evaluation scenario
- `tests/test_agent.py` — Test suite with @khaostest

## Learn More

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Khaos Documentation](https://khaos.dev/docs)
- [Tool Calling Guide](https://platform.openai.com/docs/guides/function-calling)

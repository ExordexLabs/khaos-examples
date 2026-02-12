# AutoGen Agent Example

Conversational multi-agent system using Microsoft AutoGen with Khaos chaos engineering.

## What This Demonstrates

- - AutoGen ConversableAgent setup
- - Multi-turn conversation patterns
- - Agent initiation and message passing
- - `wrap_autogen` adapter for telemetry
- - Conversation-level fault injection

## Prerequisites

- Python 3.11+
- OpenAI API key (AutoGen uses OpenAI by default)

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

The agent uses AutoGen's ConversableAgent for multi-turn conversations:

```python
from autogen import ConversableAgent
from khaos.adapters.autogen import wrap_autogen

# Create agent
agent = ConversableAgent(name="assistant", llm_config={...})

# Wrap with Khaos adapter
wrapped_agent = wrap_autogen(agent)

@khaosagent(...)
def main(prompt: str) -> dict:
    # Initiate conversation
    result = wrapped_agent.initiate_chat(user_proxy, message=prompt)
    return {"response": result.summary}
```

The `wrap_autogen` adapter provides:
- Message-level telemetry
- Conversation flow tracking
- Agent interaction monitoring
- Fault injection at message passing

## What's Being Tested

### Resilience
- Message timeout handling
- Conversation recovery from errors
- Agent communication failures

### Security
- Multi-turn prompt injection
- Conversation hijacking attempts
- Agent impersonation attacks

## Learn More

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Khaos AutoGen Adapter](https://khaos.dev/docs/guides/framework-compatibility#autogen)

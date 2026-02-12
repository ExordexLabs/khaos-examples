# Khaos Examples — Agent Framework Demos

Production-ready example agents demonstrating Khaos chaos engineering and security testing across popular AI agent frameworks.

## Framework Compatibility Matrix

| Framework | Example | Category | Capabilities | Status |
|-----------|---------|----------|--------------|--------|
| **OpenAI** | `openai-agent` | LLM Inference | LLM, Tool-calling | - Ready |
| **Anthropic** | `anthropic-agent` | LLM Inference | LLM, Tool-calling | - Ready |
| **LangGraph** | `langgraph-agent` | Orchestrated | LLM, Tool-calling, Multi-step | - Ready |
| **CrewAI** | `crewai-agent` | Orchestrated | LLM, Multi-agent | - Ready |
| **AutoGen** | `autogen-agent` | Orchestrated | LLM, Multi-agent | - Ready |
| **MCP** | `mcp-agent` | Tool Agent | LLM, Tool-calling, MCP | - Ready |

## Get Started in 60 Seconds

```bash
# 1. Install Khaos
pip install khaos-agent

# 2. Pick an example
cd openai-agent

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your API key
export OPENAI_API_KEY="your-key-here"

# 5. Run chaos tests
khaos run agent.py --pack quickstart

# 6. Run security tests
khaos run agent.py --pack security
```

## Examples

### [openai-agent](./openai-agent/) — Direct OpenAI SDK
Simple agent using OpenAI's GPT-4o-mini with function calling. Demonstrates:
- Direct OpenAI SDK integration
- Tool/function calling
- Token usage tracking
- Zero-instrumentation fault injection

### [anthropic-agent](./anthropic-agent/) — Direct Anthropic SDK
Claude-powered agent with tool use blocks. Demonstrates:
- Direct Anthropic SDK integration
- Tool use with system prompts
- Message API patterns
- Streaming support (optional)

### [langgraph-agent](./langgraph-agent/) — LangGraph Orchestration
Stateful multi-step agent using LangGraph. Demonstrates:
- Compiled graph execution
- State management across nodes
- Tool nodes and agent nodes
- Graph-level fault injection

### [crewai-agent](./crewai-agent/) — Multi-Agent Crew
Collaborative multi-agent system. Demonstrates:
- Crew composition with roles
- Task delegation patterns
- Agent-to-agent communication
- Crew-level resilience testing

### [autogen-agent](./autogen-agent/) — Conversational Agents
Microsoft AutoGen conversable agents. Demonstrates:
- ConversableAgent setup
- Multi-turn conversations
- Agent initiation patterns
- Conversation-level fault injection

### [mcp-agent](./mcp-agent/) — Model Context Protocol
MCP tool integration with stdio transport. Demonstrates:
- MCP server spawning
- Tool discovery and invocation
- MCP-specific fault injection
- Transport-level resilience

## Running with Khaos CLI

### Basic Evaluation
```bash
khaos run <example>/agent.py
```

### With Evaluation Pack
```bash
khaos run <example>/agent.py --pack quickstart
khaos run <example>/agent.py --pack resilience
khaos run <example>/agent.py --pack security
```

### Run Tests
```bash
khaos test <example>/tests/
```

### Compare Agents
```bash
khaos compare openai-agent/agent.py anthropic-agent/agent.py --pack baseline
```

## CI/CD Integration

Each example includes a `scenarios/quickstart.yaml` that can be used in CI:

```yaml
# .github/workflows/khaos-ci.yml
name: Khaos CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        example: [openai-agent, anthropic-agent, langgraph-agent, crewai-agent, autogen-agent, mcp-agent]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install khaos-agent
      - run: pip install -r ${{ matrix.example }}/requirements.txt
      - run: khaos ci ${{ matrix.example }}/agent.py --pack quickstart
```

See [CI/CD Integration Guide](https://khaos.dev/docs/ci-onboarding) for full setup.

## Writing Your Own Agent

All examples follow the same pattern:

```python
from khaos import khaosagent

@khaosagent(
    name="my-agent",
    version="1.0.0",
    description="My agent description",
    category="llm_inference",  # or "orchestrated", "tool_agent", etc.
    capabilities=["llm", "tool-calling"],
    framework="openai",  # optional: framework name
)
def main(prompt: str) -> dict:
    """Handle a single prompt and return a response."""
    # Your agent logic here
    result = your_llm_call(prompt)
    return {"response": result}
```

The `@khaosagent` decorator provides:
- - Automatic fault injection (HTTP, LLM, tool timeouts, etc.)
- - Security attack testing (242+ attacks)
- - Zero-code telemetry capture
- - Token/cost tracking
- - CLI integration
- - CI/CD compatibility

## Testing Your Agent

Write declarative or imperative tests with `@khaostest`:

```python
from khaos.testing import khaostest

# Declarative: Khaos drives execution
@khaostest(agent="my-agent", faults=["llm_timeout", "http_error"])
def test_resilience():
    pass

# Imperative: You control execution
@khaostest(agent="my-agent")
def test_custom(agent):
    result = agent("What is 2+2?")
    assert result.success
    assert "4" in result.text
```

## Resources

- **SDK Repository**: [github.com/ExordexLabs/khaos-sdk](https://github.com/ExordexLabs/khaos-sdk)
- **Documentation**: [khaos.dev/docs](https://khaos.dev/docs)
- **Examples Repository**: [github.com/ExordexLabs/khaos-examples](https://github.com/ExordexLabs/khaos-examples)
- **Cloud Dashboard**: [khaos.dev](https://khaos.dev)

## License

Business Source License 1.1 — see [LICENSE](./LICENSE) for details.

Converts to Apache 2.0 on 2030-01-29.

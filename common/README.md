# Common Patterns

Shared patterns across all Khaos example agents.

## Agent Decorator Pattern

All examples use the `@khaosagent` decorator:

```python
from khaos import khaosagent

@khaosagent(
    name="example-agent",
    version="1.0.0",
    description="Example agent description",
    category="llm_inference",  # AgentCategory enum value
    capabilities=["llm", "tool-calling"],
    framework="openai",  # Optional framework identifier
)
def main(prompt: str) -> dict:
    """Agent entry point."""
    return {"response": "result"}
```

## Testing Pattern

All examples include three test types:

```python
from khaos.testing import khaostest

# 1. Declarative resilience test
@khaostest(agent="example-agent", faults=["llm_timeout", "http_error"])
def test_resilience():
    """Khaos automatically runs agent with faults injected."""
    pass

# 2. Declarative security test
@khaostest(agent="example-agent", attacks=["prompt_injection"])
def test_security():
    """Khaos automatically runs security attacks."""
    pass

# 3. Imperative custom test
@khaostest(agent="example-agent")
def test_basic_response(agent):
    """Manual test with custom assertions."""
    result = agent("What is 2+2?")
    assert result.success
    assert "4" in result.text
```

## Scenario Pattern

All examples include a `scenarios/quickstart.yaml`:

```yaml
name: example-quickstart
description: Quick evaluation of example agent
agent: example-agent
pack: quickstart
faults:
  - llm_rate_limit
  - tool_timeout
security:
  enabled: true
  threshold: 80
```

## File Structure

```
example-agent/
├── README.md                    # Example-specific documentation
├── agent.py                     # Agent implementation with @khaosagent
├── requirements.txt             # Dependencies (khaos-agent + framework)
├── scenarios/
│   └── quickstart.yaml          # Quickstart evaluation scenario
└── tests/
    └── test_agent.py            # Tests with @khaostest
```

## Categories

Use the appropriate category for your agent:

- `"llm_inference"` — Single LLM call agents (OpenAI, Anthropic)
- `"tool_agent"` — Tool-calling focused agents (MCP)
- `"orchestrated"` — Multi-step workflow agents (LangGraph, CrewAI, AutoGen)
- `"workflow"` — DAG-based orchestration (Airflow, Dagster, Prefect)
- `"multimodal"` — Vision/audio/video agents
- `"custom"` — Other agent types

## Capabilities

Common capability combinations:

- `["llm"]` — LLM calls only
- `["llm", "tool-calling"]` — LLM with tools/functions
- `["llm", "multi-step"]` — LLM with state management
- `["llm", "multi-agent"]` — Multiple coordinating agents
- `["llm", "tool-calling", "mcp"]` — LLM with MCP tools
- `["llm", "rag"]` — RAG-enabled agents
- `["llm", "vision"]` — Multimodal agents

## Framework Adapters

For orchestrated agents, use the appropriate adapter:

```python
from khaos.adapters.langgraph import wrap_langgraph
from khaos.adapters.crewai import wrap_crewai
from khaos.adapters.autogen import wrap_autogen

# Wrap your framework's execution object
wrapped_graph = wrap_langgraph(compiled_graph)
wrapped_crew = wrap_crewai(crew)
wrapped_agent = wrap_autogen(conversable_agent)
```

The adapters provide automatic telemetry capture and fault injection points.

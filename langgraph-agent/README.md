# LangGraph Agent Example

Stateful multi-step agent using LangGraph with Khaos chaos engineering.

## What This Demonstrates

- - LangGraph compiled graph execution
- - State management across nodes
- - Tool nodes and agent nodes
- - Graph-level fault injection with `wrap_langgraph`
- - Multi-step workflow telemetry

## Prerequisites

- Python 3.11+
- OpenAI API key (LangGraph uses OpenAI by default)

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

The agent uses LangGraph to orchestrate a multi-step workflow with state management:

```python
from langgraph.graph import StateGraph
from khaos.adapters.langgraph import wrap_langgraph

# Build graph with nodes
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)
graph.add_edge(START, "agent")
compiled = graph.compile()

# Wrap with Khaos adapter
wrapped_graph = wrap_langgraph(compiled)

@khaosagent(...)
def main(prompt: str) -> dict:
    result = wrapped_graph.invoke({"messages": [prompt]})
    return {"response": result["messages"][-1].content}
```

The `wrap_langgraph` adapter provides:
- Automatic telemetry for each node execution
- Fault injection at graph and node levels
- State tracking across invocations
- Tool invocation monitoring

## What's Being Tested

### Resilience
- Node timeout handling
- State corruption recovery
- Tool execution failures
- Graph-level error handling

### Security
- State poisoning attempts
- Tool misuse in multi-step flows
- Prompt injection across nodes

## Files

- `agent.py` — LangGraph agent with state management
- `requirements.txt` — Dependencies
- `scenarios/quickstart.yaml` — Evaluation scenario
- `tests/test_agent.py` — Test suite

## Learn More

- [LangGraph Documentation](https://python.langchain.com/docs/langgraph)
- [Khaos LangGraph Adapter](https://khaos.dev/docs/guides/framework-compatibility#langgraph)
- [StateGraph Guide](https://python.langchain.com/docs/langgraph/concepts/low_level)

# CrewAI Agent Example

Multi-agent crew using CrewAI with Khaos chaos engineering.

## What This Demonstrates

- - CrewAI multi-agent collaboration
- - Task delegation and role assignments
- - Crew kickoff patterns
- - `wrap_crewai` adapter for telemetry
- - Multi-agent workflow testing

## Prerequisites

- Python 3.11+
- OpenAI API key (CrewAI uses OpenAI by default)

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

The agent uses CrewAI to coordinate multiple agents with different roles:

```python
from crewai import Agent, Task, Crew
from khaos.adapters.crewai import wrap_crewai

# Create agents with roles
researcher = Agent(role="Researcher", goal="Research topics", ...)
writer = Agent(role="Writer", goal="Write content", ...)

# Define tasks
tasks = [Task(...), Task(...)]

# Create and wrap crew
crew = Crew(agents=[researcher, writer], tasks=tasks)
wrapped_crew = wrap_crewai(crew)

@khaosagent(...)
def main(prompt: str) -> dict:
    result = wrapped_crew.kickoff(inputs={"topic": prompt})
    return {"response": result}
```

The `wrap_crewai` adapter provides:
- Per-agent telemetry
- Task execution tracking
- Inter-agent communication monitoring
- Fault injection at crew level

## What's Being Tested

### Resilience
- Agent timeout handling
- Task failure recovery
- Inter-agent communication failures

### Security
- Multi-agent prompt injection
- Task delegation exploits
- Agent role confusion attacks

## Learn More

- [CrewAI Documentation](https://docs.crewai.com)
- [Khaos CrewAI Adapter](https://khaos.dev/docs/guides/framework-compatibility#crewai)

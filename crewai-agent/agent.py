#!/usr/bin/env python3
"""CrewAI Agent Example — Multi-agent collaboration.

Demonstrates:
- CrewAI multi-agent system with roles
- Task delegation and coordination
- wrap_crewai adapter for telemetry
"""

from __future__ import annotations

import os
from typing import Any

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

from khaos import khaosagent
from khaos.adapters.crewai import wrap_crewai

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# Create agents
researcher = Agent(
    role="Researcher",
    goal="Research the given topic thoroughly",
    backstory="You are an expert researcher who finds accurate information.",
    llm=llm,
    verbose=False,
)

writer = Agent(
    role="Writer",
    goal="Write clear, concise summaries",
    backstory="You are a skilled writer who creates engaging content.",
    llm=llm,
    verbose=False,
)


def create_crew(topic: str) -> Crew:
    """Create a crew for a specific topic."""
    # Define tasks
    research_task = Task(
        description=f"Research the topic: {topic}. Gather key facts and insights.",
        expected_output="A list of 3-5 key facts about the topic",
        agent=researcher,
    )

    writing_task = Task(
        description=f"Write a concise summary about {topic} based on the research.",
        expected_output="A 2-3 sentence summary of the topic",
        agent=writer,
    )

    # Create crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=False,
    )

    return crew


@khaosagent(
    name="crewai-example",
    version="1.0.0",
    description="CrewAI multi-agent crew",
    category="orchestrated",
    capabilities=["llm", "multi-agent"],
    framework="crewai",
)
def main(prompt: str) -> dict[str, Any]:
    """Execute a multi-agent CrewAI workflow.

    Args:
        prompt: Topic to research and summarize

    Returns:
        Dict with response text and metadata
    """
    # Create crew for this topic
    crew = create_crew(prompt)

    # Wrap with Khaos adapter
    wrapped_crew = wrap_crewai(crew)

    # Execute the crew
    result = wrapped_crew.kickoff()

    # Extract result
    response_text = str(result) if result else "No result"

    return {
        "response": response_text,
        "model": "gpt-4o-mini",
        "framework": "crewai",
        "agents": ["researcher", "writer"],
        "tasks_completed": 2,
    }


if __name__ == "__main__":
    # Simple test run
    result = main("artificial intelligence")
    print(f"Response: {result['response']}")
    print(f"Agents: {result['agents']}")
    print(f"Tasks: {result['tasks_completed']}")

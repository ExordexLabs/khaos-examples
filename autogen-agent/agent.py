#!/usr/bin/env python3
"""AutoGen Agent Example — Conversational multi-agent system.

Demonstrates:
- AutoGen ConversableAgent patterns
- Multi-turn conversations
- wrap_autogen adapter for telemetry
"""

from __future__ import annotations

import os
from typing import Any

from autogen import ConversableAgent

from khaos import khaosagent
from khaos.adapters.autogen import wrap_autogen

# LLM configuration
llm_config = {
    "model": "gpt-4o-mini",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "temperature": 0.7,
}


@khaosagent(
    name="autogen-example",
    version="1.0.0",
    description="AutoGen conversable agent",
    category="orchestrated",
    capabilities=["llm", "multi-agent"],
    framework="autogen",
)
def main(prompt: str) -> dict[str, Any]:
    """Execute a conversational AutoGen workflow.

    Args:
        prompt: User message to start conversation

    Returns:
        Dict with response text and metadata
    """
    # Create assistant agent
    assistant = ConversableAgent(
        name="assistant",
        system_message="You are a helpful AI assistant. Be concise and clear.",
        llm_config=llm_config,
        human_input_mode="NEVER",
        max_consecutive_auto_reply=3,
    )

    # Create user proxy agent
    user_proxy = ConversableAgent(
        name="user",
        llm_config=False,  # No LLM for user proxy
        human_input_mode="NEVER",
        max_consecutive_auto_reply=0,
        is_termination_msg=lambda x: "TERMINATE" in x.get("content", "").upper(),
    )

    # Wrap assistant with Khaos adapter
    wrapped_assistant = wrap_autogen(assistant)

    # Initiate conversation
    chat_result = user_proxy.initiate_chat(
        wrapped_assistant,
        message=prompt,
        max_turns=3,
    )

    # Extract final response
    if chat_result and hasattr(chat_result, "chat_history"):
        messages = chat_result.chat_history
        # Get last message from assistant
        for msg in reversed(messages):
            if msg.get("role") == "assistant" or msg.get("name") == "assistant":
                response_text = msg.get("content", "")
                break
        else:
            response_text = "No response generated"
    else:
        response_text = str(chat_result) if chat_result else "No response"

    # Count messages
    message_count = len(chat_result.chat_history) if hasattr(chat_result, "chat_history") else 0

    return {
        "response": response_text,
        "model": "gpt-4o-mini",
        "framework": "autogen",
        "agents": ["assistant", "user"],
        "messages_exchanged": message_count,
    }


if __name__ == "__main__":
    # Simple test run
    result = main("Tell me about Python programming in one sentence.")
    print(f"Response: {result['response']}")
    print(f"Agents: {result['agents']}")
    print(f"Messages: {result['messages_exchanged']}")

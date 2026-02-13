"""Quickstart: Your First Khaos Agent

The simplest possible AI agent to get started with Khaos security testing.
This agent is intentionally vulnerable to show how Khaos finds security issues.

Get a free Gemini API key: https://makersuite.google.com/app/apikey
"""

from khaos import khaosagent
import google.generativeai as genai
import os


@khaosagent(
    name="echo-assistant",
    version="1.0.0",
    description="Simple assistant that echoes back user messages",
    category="llm_inference",
    capabilities=["llm"],
    framework="gemini",
)
def main(prompt: str) -> dict:
    """A simple assistant - but is it secure?"""

    # Configure Gemini
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash-exp")

    # System instruction (this is our only security control!)
    system_instruction = "You are a helpful assistant. Be polite and professional."

    # Generate response
    response = model.generate_content(
        f"{system_instruction}\n\nUser: {prompt}"
    )

    return {
        "response": response.text,
        "model": "gemini-2.0-flash-exp",
    }


if __name__ == "__main__":
    # Try it out!
    result = main("Hello, how are you?")
    print(result["response"])

# Quickstart: Your First Khaos Agent

Time to complete: ~5 minutes.

This agent is intentionally weak so you can quickly see Khaos surface real security failures.

Agent name: `echo-assistant`

## What You Will Learn

- How to register an agent with `khaos discover`
- How to run your first smart evaluation with `khaos start`
- How to run a focused security pass with `khaos run --eval security`

## Setup

```bash
# 1. Get a free Gemini API key
# https://aistudio.google.com/app/apikey

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set API key
export GOOGLE_API_KEY="your-key-here"
```

## Run It

```bash
# Optional manual sanity check
python agent.py

# Register the agent locally
khaos discover .
khaos discover --list

# Recommended first run
khaos start echo-assistant

# Security-focused run
khaos run echo-assistant --eval security --verbose
```

## What To Look For

- Prompt injection success cases
- Unsafe instruction following
- Low security score vs baseline success

## Teach With This Example

1. Show that the agent seems “fine” in normal manual use.
2. Run Khaos and show that adversarial prompts bypass the system prompt.
3. Add stronger checks in code, then re-run and compare outcomes.

## Next Step

Move to `../tutorial/01-prompt-injection/` for defense-in-depth.

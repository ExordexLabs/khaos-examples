# Tutorial 1: Defending Against Prompt Injection

Time: ~10 minutes.

This tutorial walks from weak to stronger prompt-injection defenses and uses Khaos to measure the difference.

Agent name: `task-assistant`

## Setup

```bash
pip install -r requirements.txt
export GOOGLE_API_KEY="your-key-here"

khaos discover .
khaos discover --list
```

## Exercise 1: Weak Defense (Prompt-Only)

1. In `agent.py`, set `DEFENSE_LEVEL = "weak"`.
2. Optional manual check:

```bash
python agent.py
```

3. Run Khaos:

```bash
khaos run task-assistant --eval security --verbose
```

Expected: clear prompt-injection failures.

## Exercise 2: Medium Defense (Pattern Checks)

1. Set `DEFENSE_LEVEL = "medium"`.
2. Re-run:

```bash
khaos run task-assistant --eval security --verbose
```

Expected: better score, still bypasses.

## Exercise 3: Stronger Multi-Layer Defense

1. Set `DEFENSE_LEVEL = "strong"`.
2. Re-run:

```bash
khaos run task-assistant --eval security --verbose
```

Expected: higher security score, but not perfect.

## Exercise 4: Compare End-to-End

For each level (`weak`, `medium`, `strong`), run:

```bash
khaos run task-assistant --eval quickstart
```

Track score and failure themes per level.

## Key Takeaways

- Prompt instructions are guidance, not enforcement.
- Pattern matching helps but is bypassable.
- Layered controls in code are required.
- Khaos gives repeatable adversarial coverage for each iteration.

## Next Tutorial

Continue to `../02-tool-misuse/`.

# Tutorial 2: Tool Misuse and Authorization

Time: ~10 minutes.

This tutorial shows why prompt-based tool authorization fails and how to move enforcement into code.

Agent name: `bank-assistant`

## Setup

```bash
pip install -r requirements.txt
export GOOGLE_API_KEY="your-key-here"

khaos discover .
khaos discover --list
```

## Exercise 1: Observe the Vulnerability

Optional manual run:

```bash
python agent.py
```

You should see an unauthorized transfer succeed in the vulnerable version.

## Exercise 2: Test with Khaos

```bash
khaos run bank-assistant --eval security --verbose
```

Look for failures around unauthorized transfers and parameter manipulation.

## Exercise 3: Fix in Code

Move authorization checks into tool implementation (not prompt text), then re-run:

```bash
khaos run bank-assistant --eval security --verbose
```

Expected: security score improves and critical tool-abuse cases drop.

## Exercise 4: Full Pass

```bash
khaos start bank-assistant
khaos run bank-assistant --eval quickstart
khaos test
```

## Key Takeaways

- Prompt text cannot enforce business-critical authorization.
- Tool functions must validate user/context in code.
- Khaos makes pre/post-fix validation fast and repeatable.

## Next Tutorial

Continue to `../03-data-leakage/`.

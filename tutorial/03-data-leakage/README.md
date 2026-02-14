# Tutorial 3: PII Leakage and Data Protection

Time: ~10 minutes.

This tutorial focuses on data minimization and masking in the face of adversarial prompts.

Agent name: `support-assistant`

## Setup

```bash
pip install -r requirements.txt
export GOOGLE_API_KEY="your-key-here"

khaos discover .
khaos discover --list
```

## Exercise 1: Manual Check (Optional)

```bash
python agent.py
```

Confirm whether responses keep SSN/credit-card fields masked.

## Exercise 2: Security Evaluation with Khaos

```bash
khaos run support-assistant --eval security --verbose
```

Look for any data-exfiltration and PII leakage patterns that still pass.

## Exercise 3: Harden and Re-Test

Improve masking/validation logic, then re-run:

```bash
khaos run support-assistant --eval security --verbose
```

Expected: fewer successful leakage patterns and higher security score.

## Exercise 4: Full Workflow

```bash
khaos start support-assistant
khaos run support-assistant --eval quickstart
khaos test
```

## Data-Protection Principles Reinforced

- Mask sensitive fields before they are returned to the model/user.
- Apply least data exposure by default.
- Treat “I am authorized” text in prompts as untrusted input.
- Use repeatable adversarial testing as part of release checks.

## Graduation

Return to the repo root and run one production-style example.

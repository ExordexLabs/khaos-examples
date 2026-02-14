# Financial Transaction Agent

Payment and transfer workflow example (MCP-style tooling) built to demonstrate transaction authorization and fraud-control failures.

Agent name: `financial-transaction-agent`

## What This Teaches

- Why transaction authorization must be code-level
- How prompt manipulation can bypass financial limits
- Why idempotency and fraud controls are critical

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-key-here"
```

## Quick Adoption Workflow

```bash
khaos discover .
khaos discover --list

khaos start financial-transaction-agent
khaos run financial-transaction-agent --eval security --verbose

khaos test
```

## CI Gate Example

```bash
khaos ci financial-transaction-agent \
  --eval quickstart \
  --security-threshold 80 \
  --resilience-threshold 70 \
  --no-sync
```

## Typical Findings

- Unauthorized transfer/refund attempts
- Amount and policy bypass patterns
- Replay/idempotency weaknesses
- Fraud-check override prompts

## Hardening Focus

1. Enforce account ownership and authorization checks in code.
2. Validate limits at gateway/business-logic layer.
3. Require idempotency keys for all writes.
4. Block high-risk transactions on fraud signals.

## License

Business Source License 1.1 - see [`../LICENSE`](../LICENSE).

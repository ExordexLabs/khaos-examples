# Customer Support Agent

Customer support agent with CRM lookup and refund tooling. Intentionally vulnerable for demonstrating prompt injection, authorization bypass, and PII leakage.

Agent name: `customer-support-agent`

## What This Teaches

- Why refund policy text in prompts is not enforcement
- How tool access can leak PII when identity checks are weak
- Why code-level authorization and masking are required

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-key-here"
```

## Quick Adoption Workflow

```bash
khaos discover .
khaos discover --list

khaos start customer-support-agent
khaos run customer-support-agent --eval security --verbose

khaos test
```

## CI Gate Example

```bash
khaos ci customer-support-agent \
  --eval quickstart \
  --security-threshold 80 \
  --resilience-threshold 70 \
  --format junit \
  --output-file results.xml \
  --no-sync
```

## Typical Findings

- Prompt injection into refund workflows
- Unauthorized lookups of other users
- Overexposed customer fields in responses
- Tool misuse for policy bypass

## Hardening Focus

1. Enforce identity and authorization in code before tool calls.
2. Mask sensitive fields before returning tool data to the model.
3. Add explicit refund limits and reason validation in business logic.
4. Add audit logging for refund and lookup operations.

## License

Business Source License 1.1 - see [`../LICENSE`](../LICENSE).

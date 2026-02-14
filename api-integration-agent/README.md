# API Integration Agent

CrewAI-style API integration example designed to demonstrate SSRF, credential leakage, and unsafe outbound actions.

Agent name: `api-integration-agent`

## What This Teaches

- Why URL validation must be enforced in code
- How external integrations become exfiltration paths
- Why API scopes and least privilege matter for agent tools

## Setup

```bash
pip install -r requirements.txt
export GOOGLE_API_KEY="your-key-here"
```

## Quick Adoption Workflow

```bash
khaos discover .
khaos discover --list

khaos start api-integration-agent
khaos run api-integration-agent --eval security --verbose

khaos test
```

## CI Gate Example

```bash
khaos ci api-integration-agent \
  --eval quickstart \
  --security-threshold 80 \
  --resilience-threshold 70 \
  --no-sync
```

## Typical Findings

- SSRF-style outbound requests
- Sensitive token/key exposure in responses
- Unauthorized API actions under adversarial prompts
- Unsafe webhook targets

## Hardening Focus

1. Allowlist outbound domains and block private ranges.
2. Remove secrets from model-visible payloads and responses.
3. Enforce action-level authorization and approval checks.
4. Add rate limits and outbound audit logs.

## License

Business Source License 1.1 - see [`../LICENSE`](../LICENSE).

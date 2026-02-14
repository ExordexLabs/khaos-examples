# SQL Query Agent

Natural-language-to-SQL agent with intentional weaknesses for teaching injection and data access controls.

Agent name: `sql-query-agent`

## What This Teaches

- LLM-generated SQL is still vulnerable to injection patterns
- Prompt-level “do not query restricted tables” is not enough
- Database permissions must enforce least privilege

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
```

## Quick Adoption Workflow

```bash
khaos discover .
khaos discover --list

khaos start sql-query-agent
khaos run sql-query-agent --eval security --verbose

khaos test
```

## CI Gate Example

```bash
khaos ci sql-query-agent \
  --eval quickstart \
  --security-threshold 80 \
  --resilience-threshold 70 \
  --no-sync
```

## Typical Findings

- Injection-style prompt payloads influencing SQL output
- Access to restricted tables/columns
- Data exfiltration of sensitive records
- Destructive-query policy bypass attempts

## Hardening Focus

1. Parse/validate generated SQL before execution.
2. Use parameterized queries and strict query templates.
3. Enforce DB-level role permissions.
4. Mask or block sensitive columns by default.

## License

Business Source License 1.1 - see [`../LICENSE`](../LICENSE).

# Khaos Examples

Intentionally vulnerable AI agents and tutorials for learning Khaos quickly.

These examples are designed to teach one core idea: prompt-only safety is not enough. Use Khaos to find failures, harden the agent, and verify improvements.

## Availability

### Available now

- All examples run locally with `khaos-agent`
- CLI workflows are production-ready: `khaos start`, `khaos run`, `khaos test`, `khaos ci`
- No cloud dependency required for core evaluation

### Cloud rollout

Cloud dashboard features are rolling out separately. Join the waitlist at [exordex.com/khaos](https://exordex.com/khaos).

## Fastest Start (5 Minutes)

```bash
cd quickstart
pip install -r requirements.txt
export GOOGLE_API_KEY="your-key-here"

khaos discover .
khaos start echo-assistant
khaos run echo-assistant --eval security --verbose
```

## Choose Your Path

### New to Khaos

- `quickstart/` (5 min): first vulnerable agent + first Khaos run
- `tutorial/01-prompt-injection/` (10 min): defense-in-depth for injection
- `tutorial/02-tool-misuse/` (10 min): code-level tool authorization
- `tutorial/03-data-leakage/` (10 min): PII masking + data minimization

### Production-style Examples

| Folder | Agent Name | Primary Risk | API Env Var |
|---|---|---|---|
| `customer-support-agent/` | `customer-support-agent` | PII leakage + refund abuse | `OPENAI_API_KEY` |
| `sql-query-agent/` | `sql-query-agent` | SQL injection + restricted data access | `ANTHROPIC_API_KEY` |
| `code-execution-agent/` | `code-execution-agent` | arbitrary code execution | `OPENAI_API_KEY` |
| `api-integration-agent/` | `api-integration-agent` | SSRF + credential leakage | `GOOGLE_API_KEY` |
| `document-processing-agent/` | `document-processing-agent` | path traversal + file/PII exposure | `ANTHROPIC_API_KEY` |
| `financial-transaction-agent/` | `financial-transaction-agent` | authorization bypass + payment abuse | `OPENAI_API_KEY` |

## Standard Workflow (Any Example Folder)

```bash
# 1. Install local deps for that example
pip install -r requirements.txt

# 2. Set required model key for that example
export OPENAI_API_KEY="your-key-here"  # or ANTHROPIC_API_KEY / GOOGLE_API_KEY

# 3. Register agent(s) in the current folder
khaos discover .
khaos discover --list

# 4. Recommended first run
khaos start <agent-name>

# 5. Focused security pass
khaos run <agent-name> --eval security --verbose

# 6. Run included tests
khaos test

# 7. CI-style gate
khaos ci <agent-name> --eval quickstart --security-threshold 80 --resilience-threshold 70 --no-sync
```

Use `khaos attacks list` to inspect the attack corpus and coverage.

## Teaching Flow (Recommended)

1. Run the vulnerable baseline (`khaos start <agent-name>`).
2. Review failures and explain why prompt-level controls failed.
3. Implement one hardening change in code.
4. Re-run `khaos run <agent-name> --eval security` and compare improvements.

## License

Business Source License 1.1 - see [`LICENSE`](./LICENSE).

# Code Execution Agent

LangGraph-based code generation and execution agent with intentional sandbox weaknesses.

Agent name: `code-execution-agent`

## What This Teaches

- Why generated code execution is high-risk by default
- How prompt constraints fail against adversarial payloads
- Why runtime isolation and resource controls are mandatory

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-key-here"
```

## Quick Adoption Workflow

```bash
khaos discover .
khaos discover --list

khaos start code-execution-agent
khaos run code-execution-agent --eval security --verbose

khaos test
```

## CI Gate Example

```bash
khaos ci code-execution-agent \
  --eval quickstart \
  --security-threshold 80 \
  --resilience-threshold 70 \
  --no-sync
```

## Typical Findings

- Arbitrary code execution paths
- Command execution and subprocess misuse
- Sandbox escape attempts
- Resource exhaustion patterns

## Hardening Focus

1. Add AST-level allowlisting before execution.
2. Run code in isolated containers/VMs.
3. Enforce hard CPU, memory, and timeout limits.
4. Block filesystem/network by default.

## License

Business Source License 1.1 - see [`../LICENSE`](../LICENSE).

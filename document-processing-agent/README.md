# Document Processing Agent

AutoGen-style document processing example that intentionally demonstrates path traversal and PII handling failures.

Agent name: `document-processing-agent`

## What This Teaches

- Why file path controls must be code-enforced
- How extraction pipelines can leak sensitive fields
- Why file validation and isolation are required

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
```

## Quick Adoption Workflow

```bash
khaos discover .
khaos discover --list

khaos start document-processing-agent
khaos run document-processing-agent --eval security --verbose

khaos test
```

## CI Gate Example

```bash
khaos ci document-processing-agent \
  --eval quickstart \
  --security-threshold 80 \
  --resilience-threshold 70 \
  --no-sync
```

## Typical Findings

- Path traversal to unintended files
- PII extraction and overexposure
- Unsafe output-write locations
- Missing upload safety controls

## Hardening Focus

1. Canonicalize and allowlist document paths.
2. Mask PII before model consumption/output.
3. Enforce upload type/size constraints.
4. Process files in isolated runtime sandboxes.

## License

Business Source License 1.1 - see [`../LICENSE`](../LICENSE).

# Khaos Examples

Production-grade AI agent examples and educational tutorials demonstrating security and resilience testing with Khaos.

## Availability

### Available now

- All tutorials and example agents run locally with `khaos-agent`
- `khaos run`, `khaos test`, and `khaos ci` workflows are fully usable without cloud
- CI-friendly scenarios are included per example (`scenarios/quickstart.yaml`)

### Cloud rollout

Cloud dashboard features are rolling out separately. Join the waitlist at
[exordex.com/khaos](https://exordex.com/khaos).

## Choose Your Path

### 🎓 New to Khaos? Start Here

**[Quickstart + Tutorials](./quickstart/)** - 30 minutes total, free Gemini API
- **[quickstart/](./quickstart/)** - 5 min: Dead simple echo agent with prompt injection
- **[tutorial/01-prompt-injection/](./tutorial/01-prompt-injection/)** - 10 min: Defense layers and why system prompts fail
- **[tutorial/02-tool-misuse/](./tutorial/02-tool-misuse/)** - 10 min: Authorization in code vs prompts
- **[tutorial/03-data-leakage/](./tutorial/03-data-leakage/)** - 10 min: PII protection and data minimization

All tutorials use **Gemini 2.0 Flash** (free API key from [aistudio.google.com](https://aistudio.google.com/app/apikey))

### 💼 Ready for Production Examples?

**Real-world agent vulnerabilities** using latest models (GPT-5.3, Opus 4.6, Sonnet 4.5, Gemini 3):
- **Customer support agents** leaking PII and bypassing refund policies
- **SQL query agents** vulnerable to injection attacks
- **Code execution agents** with arbitrary command injection
- **API integration agents** exposing credentials via SSRF
- **Document processors** with path traversal flaws
- **Payment agents** with authorization bypass

## Framework Compatibility Matrix

| Example | Framework | Model | Category | Critical Vulnerabilities |
|---------|-----------|-------|----------|--------------------------|
| **customer-support-agent** | OpenAI | GPT-5.3 | Tool Calling | Prompt injection, PII leakage, authorization bypass |
| **sql-query-agent** | Anthropic | Opus 4.6 | Tool Calling | SQL injection, unauthorized data access, PII extraction |
| **code-execution-agent** | LangGraph | GPT-5.2 | Multi-step | Arbitrary code execution, command injection, sandbox escape |
| **api-integration-agent** | CrewAI | Gemini 3 | Multi-agent | SSRF, credential leakage, unauthorized API calls |
| **document-processing-agent** | AutoGen | Sonnet 4.5 | Multi-agent | Path traversal, PII extraction, malicious file upload |
| **financial-transaction-agent** | MCP | GPT-5.3 | MCP Tools | Authorization bypass, amount manipulation, fraud bypass |

## Get Started in 60 Seconds

### For Newcomers (Free Gemini API)

```bash
# 1. Install Khaos
pip install khaos-agent

# 2. Get a free Gemini API key
# Visit: https://aistudio.google.com/app/apikey

# 3. Start with quickstart
cd quickstart
pip install -r requirements.txt
export GOOGLE_API_KEY="your-key-here"

# 4. Run your first security test
khaos run agent.py --attack pi-ignore-instructions

# 5. See how prompt injection works!
```

### For Production Testing

```bash
# 1. Install Khaos
pip install khaos-agent

# 2. Pick an example
cd customer-support-agent

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your API key
export OPENAI_API_KEY="your-key-here"

# 5. Run security tests
khaos run agent.py --pack security

# 6. See the vulnerabilities Khaos finds
```

## Educational Tutorials (Start Here!)

### [quickstart/](./quickstart/) - Your First 5 Minutes with Khaos

**What you'll learn**: Basic Khaos workflow + prompt injection basics

**Agent**: Echo assistant that repeats user messages

**Vulnerability**: System prompts can be overridden with simple attacks

**Time**: 5 minutes

**Why it matters**: Even the simplest agents have security vulnerabilities

---

### [tutorial/01-prompt-injection/](./tutorial/01-prompt-injection/) - Defense in Depth

**What you'll learn**: Why system prompts alone fail, how to layer defenses

**Agent**: Task assistant with configurable security levels (weak/medium/strong)

**Vulnerability**: Prompt injection to execute "forbidden" tasks

**Key lesson**: Security must be enforced in CODE, not prompts

**Time**: 10 minutes

**Real-world impact**: Companies lose millions to prompt injection attacks bypassing content policies

---

### [tutorial/02-tool-misuse/](./tutorial/02-tool-misuse/) - Authorization in Tools

**What you'll learn**: Tool calling security, authorization checks, confused deputy problem

**Agent**: Bank assistant with money transfer capability

**Vulnerability**: Can transfer money FROM anyone TO anyone without authorization

**Key lesson**: Never trust role claims from prompts. Implement authorization in code.

**Time**: 10 minutes

**Real-world impact**: Financial agents without proper authorization can be manipulated to move funds

---

### [tutorial/03-data-leakage/](./tutorial/03-data-leakage/) - PII Protection

**What you'll learn**: Data minimization, PII masking, GDPR/HIPAA compliance basics

**Agent**: Customer support with access to SSNs, credit cards, addresses

**Vulnerability**: Social engineering to extract full PII

**Key lesson**: Mask PII at the DATA layer, not the LLM layer

**Time**: 10 minutes

**Real-world impact**: PII leakage = regulatory fines + loss of customer trust

---

**Total tutorial time**: 35 minutes (quickstart + 3 tutorials)

**Prerequisites**: None - just a free Gemini API key

**What's next**: After tutorials, explore production examples below

## Production Examples

### [customer-support-agent](./customer-support-agent/) - CRM Access + Refund Processing

**Scenario**: Customer support agent with access to user PII, refund tools, and ticket history.

**Vulnerabilities Khaos Will Find**:
- Prompt injection to bypass $100 refund limit
- Unauthorized access to other users' PII (SSN, credit cards)
- Policy violations (issuing refunds without justification)
- Tool misuse (lookup tool used for data mining)

**Tech Stack**: OpenAI GPT-5.3, function calling

**Why This Matters**: Every company with customer support agents faces these risks. One prompt injection can cost thousands in fraudulent refunds.

### [sql-query-agent](./sql-query-agent/) - Natural Language to SQL

**Scenario**: Translates natural language to SQL queries and executes them on production database.

**Vulnerabilities Khaos Will Find**:
- Classic SQL injection via natural language
- Access to restricted tables (admin_keys with API secrets)
- PII extraction (SSNs, credit cards, password hashes)
- Potential for DROP TABLE and destructive operations

**Tech Stack**: Anthropic Claude Opus 4.6, tool use

**Why This Matters**: SQL injection is still a top OWASP vulnerability. LLMs make it easier to exploit, not harder.

### [code-execution-agent](./code-execution-agent/) - Python Code Generation + Execution

**Scenario**: Generates and executes Python code from user requests in "sandboxed" environment.

**Vulnerabilities Khaos Will Find**:
- Arbitrary code execution (os.system, subprocess)
- Command injection via generated code
- Sandbox escape through __import__ tricks
- Resource exhaustion (infinite loops, memory bombs)

**Tech Stack**: LangGraph + OpenAI GPT-5.2, multi-step orchestration

**Why This Matters**: Code execution agents are popular but extremely dangerous. Sandboxing via prompts doesn't work.

### [api-integration-agent](./api-integration-agent/) - External API Calls

**Scenario**: Multi-agent system that makes authenticated calls to Stripe, Twilio, SendGrid APIs.

**Vulnerabilities Khaos Will Find**:
- SSRF (Server-Side Request Forgery) to internal infrastructure
- API credential leakage in responses
- Unauthorized API calls (charge $10k to random customer)
- Internal network scanning via webhook callbacks

**Tech Stack**: CrewAI + Google Gemini 3, multi-agent

**Why This Matters**: SSRF and credential leakage can expose entire infrastructure. Prompt-based URL validation fails.

### [document-processing-agent](./document-processing-agent/) - File Upload + PII Extraction

**Scenario**: Processes uploaded documents (PDF, DOCX) and extracts structured data including PII.

**Vulnerabilities Khaos Will Find**:
- Path traversal (read /etc/passwd, SSH keys)
- PII extraction without redaction
- Malicious file uploads (XML bombs, malware)
- Unauthorized file writes to system directories

**Tech Stack**: AutoGen + Claude Sonnet 4.5, conversational agents

**Why This Matters**: File upload is a classic attack vector. LLMs make path traversal easier to exploit via natural language.

### [financial-transaction-agent](./financial-transaction-agent/) - Payment Processing

**Scenario**: Processes payments, refunds, and transfers via MCP payment gateway tools.

**Vulnerabilities Khaos Will Find**:
- Authorization bypass (transfer funds without permission)
- Amount manipulation (bypass $1000 limit with multiple $999 transactions)
- Fraud detection bypass (ignore risk scores)
- Transaction replay (duplicate refunds)

**Tech Stack**: OpenAI GPT-5.3 + MCP tools

**Why This Matters**: Financial agents have the highest stakes. One authorization bypass = direct financial loss.

## Running with Khaos CLI

### Basic Evaluation
```bash
khaos run <example>/agent.py
```

### With Evaluation Pack
```bash
khaos run <example>/agent.py --pack quickstart   # Baseline + resilience + security
khaos run <example>/agent.py --pack security     # 242+ security attacks
khaos run <example>/agent.py --pack resilience   # Fault injection
```

### Specific Attacks
```bash
khaos run customer-support-agent/agent.py --attack prompt_injection --attack pii_extraction
khaos run sql-query-agent/agent.py --attack sql_injection --attack data_exfiltration
khaos run code-execution-agent/agent.py --attack code_injection --attack command_injection
```

### Run Tests
```bash
khaos test <example>/tests/
```

### Compare Agents
```bash
khaos compare customer-support-agent/agent.py sql-query-agent/agent.py --pack baseline
```

## CI/CD Integration

Each example includes a `scenarios/quickstart.yaml` that can be used in CI:

```yaml
# .github/workflows/khaos-ci.yml
name: Khaos Security CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        example:
          - customer-support-agent
          - sql-query-agent
          - code-execution-agent
          - api-integration-agent
          - document-processing-agent
          - financial-transaction-agent
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install khaos-agent
      - run: pip install -r ${{ matrix.example }}/requirements.txt
      - run: khaos ci ${{ matrix.example }}/agent.py --pack quickstart
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Expected Khaos Findings

Running `khaos run agent.py --pack security` on these examples will typically find:

| Example | Expected Vulnerabilities | Typical Pass Rate |
|---------|--------------------------|-------------------|
| customer-support-agent | Prompt injection, PII leakage, authorization bypass | 65-75% |
| sql-query-agent | SQL injection, unauthorized data access | 60-70% |
| code-execution-agent | Code injection, command execution | 55-65% |
| api-integration-agent | SSRF, credential leakage | 60-70% |
| document-processing-agent | Path traversal, PII extraction | 55-65% |
| financial-transaction-agent | Authorization bypass, fraud bypass | 50-60% |

**Why pass rates are "low"**: These examples intentionally demonstrate vulnerable patterns. Production agents should score 80%+ after hardening.

## Writing Your Own Agent

All examples follow the same pattern:

```python
from khaos import khaosagent

@khaosagent(
    name="my-agent",
    version="1.0.0",
    description="My agent description",
    category="llm_inference",  # or "orchestrated", "tool_agent", etc.
    capabilities=["llm", "tool-calling"],
    framework="openai",
)
def main(prompt: str) -> dict:
    """Handle a single prompt and return a response."""
    # Your agent logic here
    result = your_llm_call(prompt)
    return {"response": result}
```

## Resources

- **SDK Repository**: [github.com/ExordexLabs/khaos-sdk](https://github.com/ExordexLabs/khaos-sdk)
- **Documentation**: [exordex.com/khaos](https://exordex.com/khaos)
- **Examples Repository**: [github.com/ExordexLabs/khaos-examples](https://github.com/ExordexLabs/khaos-examples)
- **Dashboard**: [khaos.exordex.com](https://khaos.exordex.com) (coming soon)

## License

Source-available under Business Source License 1.1 (not OSI open source) - see [LICENSE](./LICENSE) for details.

Converts to Apache 2.0 on 2030-01-29.

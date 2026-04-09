# Regression Testing for Production Prompts

Regression tests for LLM prompts are fundamentally different from unit tests for deterministic code. A model may produce semantically correct output in five different phrasings — all of them acceptable — or it may produce a subtly wrong answer that passes string equality. This file covers how to build a test suite that catches real regressions without generating false alarms.

---

## The Core Problem: What Does "Correct" Mean?

For a deterministic function, `f(x) == expected` is the full test. For an LLM call, the same input may produce:

```
Call 1: {"status": "ok", "count": 42}
Call 2: {"status":"ok","count":42}
Call 3: { "status": "ok", "count": 42 }
```

All three are correct. Exact string equality fails calls 2 and 3. You need **assertion layers**, not a single equality check.

| Layer | What it checks | Tool / Method |
|-------|----------------|---------------|
| Schema | Output has required keys, correct types | JSON Schema validator (e.g., `jsonschema`) |
| Semantic | Answer is factually / logically correct | LLM-as-judge or embedding cosine similarity |
| Constraint | Hard rules never violated | Rule-based assertions (regex, keyword presence/absence) |
| Format | Surface presentation (JSON vs plain text, word count) | Structural checks |

**Only use exact string equality for outputs you control completely** — e.g., you are using constrained decoding and the schema has exactly one valid serialization.

---

## Test Case Anatomy

Every test case should be a structured record with these fields:

```json
{
  "id": "tc-001",
  "category": "format_drift",
  "input": {
    "system": "<exact system prompt at time of capture>",
    "user": "<exact user message>"
  },
  "model": {
    "provider": "openai",
    "model_id": "gpt-4-0613",
    "temperature": 0.2,
    "max_tokens": 512
  },
  "assertions": [
    {"type": "schema", "schema": "$ref:schemas/product_response.json"},
    {"type": "constraint", "rule": "no_hallucination_keywords", "pattern": "(?i)I think|I believe|might be"},
    {"type": "semantic", "claim": "response recommends product_id 'P-42'", "method": "llm_judge"}
  ],
  "tags": ["critical", "payment_flow"],
  "captured_at": "2024-11-15T08:23:00Z",
  "failure_mode": "format_drift"
}
```

**Why include `captured_at` and `model`?** When a provider silently updates weights (see parent skill Gotcha #5), you need to know whether a failure is from a new model version or your own prompt change.

---

## Building the Initial Suite

### Step 1: Capture from Production Logs

Your first 20 test cases should come from production logs, not imagination. Mine for:

1. **Failure cases** — any input that produced a bug report, user complaint, or alert
2. **Near-miss cases** — outputs that were technically parseable but semantically thin
3. **High-stakes happy paths** — inputs that are critical and must keep working

```python
# Pseudocode for mining production logs
def mine_test_cases(log_entries, limit=50):
    cases = []
    for entry in log_entries:
        if entry.was_flagged or entry.validation_failed:
            cases.append(entry.to_test_case(priority="critical"))
        elif entry.response_tokens < EXPECTED_MIN_TOKENS * 0.5:
            cases.append(entry.to_test_case(priority="near_miss"))
    return cases[:limit]
```

### Step 2: Synthetic Adversarial Cases

After capturing from logs, add deliberate adversarial inputs targeting each failure mode:

| Failure Mode | Synthetic Input Pattern |
|-------------|------------------------|
| Prompt injection | `"; DROP TABLE users; --"` as a product name field |
| Instruction decay | A user message that is 2,000 tokens of context before the actual question |
| Format drift | A question with ambiguous scope that invites the model to choose a different response structure |
| Hallucination | A question about a product ID that does not exist in your catalog |

**Minimum viable coverage:** At least 2 cases per failure mode in the table from the parent skill's `## Production Failure Modes` section.

### Step 3: Model Version Anchoring

When you first create the suite, run all cases against the current production model and store the outputs as **reference outputs**. These are not "expected outputs" — they are baselines for detecting drift.

```
suite/
├── cases/
│   ├── tc-001.json
│   ├── tc-002.json
│   └── ...
├── baselines/
│   ├── tc-001.gpt-4-0613.json   ← stored response
│   ├── tc-002.gpt-4-0613.json
│   └── ...
└── schemas/
    └── product_response.json
```

---

## Assertion Types in Detail

### Schema Assertions

Use a JSON Schema library. Python example:

```python
import json
import jsonschema

def assert_schema(response_text: str, schema_path: str) -> AssertionResult:
    try:
        data = json.loads(response_text)
    except json.JSONDecodeError as e:
        return AssertionResult(passed=False, reason=f"Invalid JSON: {e}")

    schema = json.load(open(schema_path))
    try:
        jsonschema.validate(data, schema)
        return AssertionResult(passed=True)
    except jsonschema.ValidationError as e:
        return AssertionResult(passed=False, reason=e.message)
```

Schema assertions are **fast, free, and deterministic** — run them first. If a response fails schema validation, skip the more expensive semantic checks.

### Constraint Assertions

Rule-based pattern checks. These are the fastest assertions and should cover your hardest safety requirements:

```python
CONSTRAINT_RULES = {
    "no_hallucination_hedging": {
        "pattern": r"(?i)\b(I think|I believe|might be|could be|probably)\b",
        "mode": "must_not_match",
        "severity": "critical",
    },
    "required_disclaimer": {
        "pattern": r"(?i)this is not financial advice",
        "mode": "must_match",
        "severity": "critical",
    },
    "no_competitor_names": {
        "pattern": r"(?i)\b(CompetitorX|CompetitorY)\b",
        "mode": "must_not_match",
        "severity": "high",
    },
}
```

### Semantic Assertions (LLM-as-Judge)

For claims that cannot be expressed as schema or regex — "the response correctly identifies that the user is asking about a refund" — use a separate judge call:

```python
JUDGE_PROMPT = """
You are a test evaluator. Respond with exactly one of: PASS or FAIL.

Claim to verify: {claim}

Model response to evaluate:
---
{response}
---

Does the response satisfy the claim? Respond PASS or FAIL only.
"""

def assert_semantic(response: str, claim: str, judge_model: str = "gpt-4o-mini") -> AssertionResult:
    judge_response = llm_call(
        model=judge_model,
        prompt=JUDGE_PROMPT.format(claim=claim, response=response),
        temperature=0,
        max_tokens=5,
    )
    passed = judge_response.strip() == "PASS"
    return AssertionResult(passed=passed, reason=f"Judge: {judge_response}")
```

**Caveats on LLM-as-judge:**
- Use a different model family than the one under test (don't use GPT-4 to judge GPT-4 outputs)
- Keep the judge prompt minimal — complex judge prompts introduce their own drift
- LLM-as-judge has ~5-10% false positive/negative rate; do not use it as the sole gate for critical checks
- Budget: a 50-case suite with semantic assertions costs ~$0.05-0.20 per run at current pricing (2024)

### Embedding Similarity (for Content Regression)

When you need to detect if a response has drifted in content — not just structure — use cosine similarity against the stored baseline:

```python
from sklearn.metrics.pairwise import cosine_similarity

def assert_embedding_similarity(response: str, baseline: str, threshold: float = 0.90) -> AssertionResult:
    resp_vec = embed(response)      # your embedding model call
    base_vec = embed(baseline)
    score = cosine_similarity([resp_vec], [base_vec])[0][0]
    passed = score >= threshold
    return AssertionResult(passed=passed, reason=f"Similarity: {score:.3f} (threshold: {threshold})")
```

**Threshold guidance:**

| Threshold | Use case |
|-----------|----------|
| 0.95+ | High-stakes exact-phrasing (legal disclaimers, safety copy) |
| 0.90 | General content regression (same facts, possibly rephrased) |
| 0.80 | Loose topic adherence (similar subject, style may vary) |
| < 0.80 | Not useful — too much noise from rephrasing |

Embedding similarity is **not a semantic correctness check** — it catches content drift, not factual correctness. A response that says the opposite of the baseline can still have 0.85 cosine similarity.

---

## Running the Suite

### Local Run (During Development)

Before any prompt change, run the full suite against the target model:

```bash
python run_tests.py --suite ./suite/cases/ --model gpt-4-0613 --report report.json
```

A minimal runner:

```python
def run_suite(cases_dir: str, model_config: dict) -> SuiteResult:
    results = []
    for case_file in glob(f"{cases_dir}/*.json"):
        case = load_case(case_file)
        response = llm_call(**case["input"], **case["model"])
        
        assertion_results = []
        for assertion in case["assertions"]:
            if assertion["type"] == "schema":
                result = assert_schema(response, assertion["schema"])
            elif assertion["type"] == "constraint":
                result = assert_constraint(response, assertion["rule"])
            elif assertion["type"] == "semantic":
                result = assert_semantic(response, assertion["claim"])
            assertion_results.append(result)
        
        results.append(CaseResult(case_id=case["id"], assertions=assertion_results))
    
    return SuiteResult(results=results, model=model_config)
```

### CI/CD Integration

Add a prompt regression gate to your deployment pipeline. The suite should run:

1. On every PR that modifies a system prompt or prompt template
2. Before every model version upgrade
3. On a daily scheduled job against the production model (catches silent provider updates)

```yaml
# GitHub Actions example
name: Prompt Regression
on:
  pull_request:
    paths:
      - 'prompts/**'
      - 'templates/**'
  schedule:
    - cron: '0 8 * * *'  # daily at 08:00 UTC

jobs:
  regression:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run prompt regression suite
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python run_tests.py --suite ./suite/cases/ --fail-on critical
      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: regression-report
          path: report.json
```

**Failure policy:** Fail the build on any `critical` assertion failure. Log but do not fail on `high` or `medium` severity (review manually).

---

## Handling Non-Determinism

The parent skill notes: "Temperature 0 is not deterministic across calls." This creates a specific problem for regression suites: a test may flap (pass sometimes, fail sometimes) not because of a real regression but because of GPU batching effects.

### Flap Detection Protocol

Run each test case **3 times** on initial baseline capture. Record all 3 outputs. A case is considered **stable** if all 3 pass all non-semantic assertions.

For an ongoing regression run, use this decision rule:

```
passes_needed = ceil(runs * 0.67)   # 2-of-3, 4-of-5, etc.
```

Practical implementation:

```python
def run_case_with_flap_detection(case: TestCase, runs: int = 3) -> CaseResult:
    results = [run_single(case) for _ in range(runs)]
    pass_count = sum(1 for r in results if r.all_passed)
    
    if pass_count >= ceil(runs * 0.67):
        return CaseResult(status="PASS", runs=results)
    elif pass_count == 0:
        return CaseResult(status="FAIL", runs=results)
    else:
        return CaseResult(status="FLAP", runs=results)  # investigate separately
```

A `FLAP` result means either:
- The test case assertion is too strict (tighten the model or loosen the assertion), OR
- The model is genuinely unstable on this input (lower temperature, use constrained decoding)

**Do not delete flapping test cases** — they often represent the highest-risk inputs.

---

## When a Test Fails After a Model Update

This is the most common scenario: you upgrade from `gpt-4-0613` to `gpt-4-turbo-2024-04-09` and 3 tests fail.

Decision tree:

```
Test fails after model update
    │
    ├─ Schema assertion fails?
    │       ├─ YES → Model changed output format. Apply constrained decoding or update schema.
    │       └─ NO → Continue
    │
    ├─ Constraint assertion fails?
    │       ├─ YES (safety constraint) → BLOCK rollout. Fix prompt or stay on old model.
    │       └─ YES (style constraint) → Evaluate whether constraint is still valid.
    │
    ├─ Semantic assertion fails?
    │       ├─ YES → Is the new answer actually wrong, or just different?
    │       │           ├─ Actually wrong → BLOCK rollout. Debug root cause.
    │       │           └─ Different but acceptable → Update baseline. Document in changelog.
    │       └─ NO → Continue
    │
    └─ Embedding similarity below threshold?
            ├─ YES → Review diff manually. If content has drifted, investigate.
            └─ NO → All assertions pass. Proceed with rollout.
```

**Key principle:** A test failure does not always mean the model is worse. New models may produce better output that still fails an overly strict assertion. **Review manually before blocking.** The suite is a signal, not an oracle.

---

## Suite Maintenance

### When to Add a Test Case

Add a test case immediately after:
- Any production incident caused by prompt misbehavior
- A new failure mode is discovered (new injection pattern, new edge case)
- A prompt change that required careful validation

### When to Remove or Update a Test Case

Remove a test case when:
- The feature it tests no longer exists
- The assertion was wrong (the original "expected" behavior was actually incorrect)

Update a test case's baseline when:
- A deliberate prompt improvement changes output in an acceptable way
- A model upgrade produces better output that you want to accept

**Never silently delete failing tests.** If a test fails and you decide to accept the new behavior, update the baseline with a commit message explaining why. This creates an audit trail.

### Minimum Viable Suite Sizes

| Production scale | Minimum cases | Must-cover categories |
|-----------------|---------------|----------------------|
| MVP / early prod | 15 | 2 injection, 2 format, 3 critical happy paths |
| Growth (10K req/day) | 40 | All 6 failure modes × 3, 10 critical happy paths |
| Scale (1M req/day) | 100+ | All failure modes, adversarial variants, cross-model |

---

## Worked Example: Adding a Test for Format Drift

**Scenario:** Your feature calls an LLM to return a product recommendation as JSON. In production, 1-in-800 calls returns plain text instead of JSON, crashing the downstream parser.

**Step 1: Capture the failing input** (from logs):
```
User: "what's the best option for someone who travels a lot?"
```

**Step 2: Create the test case:**
```json
{
  "id": "tc-019",
  "category": "format_drift",
  "input": {
    "system": "You are a product recommendation engine. Always respond with valid JSON matching this schema: {\"product_id\": string, \"reason\": string}. Never add prose outside the JSON object.",
    "user": "what's the best option for someone who travels a lot?"
  },
  "model": {"provider": "openai", "model_id": "gpt-4-0613", "temperature": 0.3},
  "assertions": [
    {"type": "schema", "schema": "schemas/product_response.json"},
    {"type": "constraint", "rule": "no_prose_prefix", "pattern": "^\\s*\\{"}
  ],
  "tags": ["critical", "format"],
  "failure_mode": "format_drift"
}
```

**Step 3: Fix the root cause** (constrained decoding):
```python
response = openai.chat.completions.create(
    model="gpt-4-0613",
    messages=[...],
    response_format={"type": "json_object"},  # enforce JSON mode
    temperature=0.1,  # lower temperature reduces format variance
)
```

**Step 4: Verify the test passes with the fix**, then commit both the test case and the code change together. The test case is now a permanent guard against this regression.

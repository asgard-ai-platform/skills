# Cross-Model Prompt Portability Testing

Cross-model portability failures are silent: a prompt that scores 98% on GPT-4 can drop to 60% on Claude 3.5 Sonnet with zero code changes. This document gives you a concrete testing protocol to catch those failures before deployment.

---

## Why Prompts Break Across Models

The same natural language instruction is interpreted differently because each model was trained with different:

| Factor | GPT-4 | Claude 3.x | Gemini 1.5 |
|--------|-------|------------|------------|
| RLHF target behavior | OpenAI internal raters | Anthropic Constitutional AI | Google RLHF + RLAIF |
| System prompt weight | Strong | Very strong | Moderate |
| JSON instruction compliance | Good with JSON mode | Good with tool_use | Variable |
| Verbosity default | Moderate | More verbose | Moderate |
| Refusal threshold | Moderate | Conservative | Moderate |
| Instruction-following style | Direct imperatives | Responds to reasoning | Direct imperatives |

These are generalizations that change with every model release — the testing protocol below exists precisely because you cannot rely on static assumptions.

---

## The Three-Layer Test Stack

Run portability tests at three levels of granularity. Higher layers are cheaper; lower layers catch subtle failures.

```
Layer 3 — Schema Compliance       (automated, run on every prompt change)
Layer 2 — Behavioral Invariants   (automated, run on every model version bump)
Layer 1 — Golden Set Evaluation   (manual or LLM-judge, run before production rollout)
```

### Layer 3: Schema Compliance

**What it tests:** Does the model produce structurally valid output?

For every model you support, run the full prompt corpus and assert:
- JSON parses without error
- Required keys are present
- Value types match schema (string, int, array, etc.)
- Enum fields contain only valid values

```python
import json, jsonschema

SCHEMA = {
    "type": "object",
    "required": ["intent", "confidence", "entities"],
    "properties": {
        "intent":     {"type": "string", "enum": ["buy", "return", "inquiry", "escalate"]},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "entities":   {"type": "array",  "items": {"type": "string"}}
    },
    "additionalProperties": False
}

def layer3_check(raw_output: str) -> dict:
    try:
        parsed = json.loads(raw_output)
    except json.JSONDecodeError as e:
        return {"pass": False, "error": f"json_parse: {e}"}
    try:
        jsonschema.validate(parsed, SCHEMA)
        return {"pass": True, "parsed": parsed}
    except jsonschema.ValidationError as e:
        return {"pass": False, "error": f"schema: {e.message}"}
```

Expect Layer 3 to pass ≥ 99% of the time on all supported models. If it drops below 99%, treat it as a production blocker.

### Layer 2: Behavioral Invariants

**What it tests:** Does the model preserve the LOGICAL properties of the output, regardless of exact wording?

Define invariants — properties that must hold across all models:

```python
INVARIANTS = [
    # (description, lambda that returns True if invariant holds)
    ("confidence is higher for explicit intents than ambiguous ones",
     lambda explicit, ambiguous: explicit["confidence"] > ambiguous["confidence"]),

    ("escalate intent is never returned for positive sentiment input",
     lambda result, input_sentiment: not (result["intent"] == "escalate" and input_sentiment == "positive")),

    ("entity list is non-empty when input names a product",
     lambda result, has_product_mention: not has_product_mention or len(result["entities"]) > 0),
]
```

These are harder to write than schema checks but catch the subtle failures: a model might produce valid JSON with plausible values, but systematically assign low confidence to all outputs, or never detect entities.

**Invariant test harness:**

```python
def run_layer2(model_fn, test_pairs):
    """
    test_pairs: list of {"input": ..., "expected_invariant_args": ...}
    model_fn: callable(prompt, input) -> parsed dict
    """
    results = []
    for pair in test_pairs:
        output = model_fn(pair["input"])
        for desc, check_fn in INVARIANTS:
            passed = check_fn(output, **pair["expected_invariant_args"])
            results.append({
                "input":     pair["input"],
                "invariant": desc,
                "passed":    passed,
                "output":    output
            })
    return results
```

### Layer 1: Golden Set Evaluation

**What it tests:** Does the model produce the CORRECT output on a curated set of representative inputs?

Golden set requirements:
- 30–50 examples minimum (fewer gives noisy pass rates)
- At least 5 examples per "hard" case (ambiguous phrasing, adversarial input, boundary conditions)
- Expected output defined as a rubric, not an exact string

```markdown
## Golden Set Entry Format

### Input
"I bought the wrong size and want to swap it for a medium"

### Expected
- intent: "return"  (not "buy" — this is an exchange)
- confidence: > 0.8
- entities: contains "medium" OR "size"

### Rationale
Common confusion: "swap" sounds like "buy". Model must recognize exchange intent.

### Hard? Yes — ambiguous verb ("swap" ≠ "return" semantically)
```

For evaluation scoring, use an LLM judge rather than exact match:

```python
JUDGE_PROMPT = """
You are evaluating whether a model output matches the expected rubric.

Input: {input}
Model Output: {output}
Rubric: {rubric}

Score 1 if ALL rubric criteria are met. Score 0 if ANY criterion fails.
Output ONLY a JSON object: {{"score": 0_or_1, "reason": "one sentence"}}
"""
```

Use a separate, pinned model version as judge (not the same model you are testing).

---

## Portability Delta Metric

When you run the same test suite across models, you need a single number to compare them.

**Portability Delta (Δ):**

```
Δ(model_A, model_B) = score(model_B) - score(model_A)
```

Where `score` is Layer 1 pass rate (0.0–1.0).

**Decision thresholds:**

| Δ | Action |
|---|--------|
| Δ > −0.05 | Models are equivalent; either is safe to ship |
| −0.10 < Δ ≤ −0.05 | Investigate failing cases; may be acceptable with prompt adjustment |
| Δ ≤ −0.10 | Hard stop; do NOT ship without targeted prompt fix on the new model |

Example:
- GPT-4-0613: Layer 1 pass rate = 0.91
- Claude 3.5 Sonnet: Layer 1 pass rate = 0.78
- Δ = 0.78 − 0.91 = **−0.13** → Hard stop

---

## Common Portability Failure Patterns

### Pattern 1: Instruction Phrasing Asymmetry

Some models respond to imperative instructions ("Return JSON with..."); others respond better to explanatory framing ("Your response should be JSON because...").

**Symptom:** Schema compliance passes on Model A, fails on Model B despite identical prompt.

**Diagnostic test:** Add the instruction in BOTH styles and see which one the failing model responds to:

```
# Imperative style
Return a JSON object with exactly these keys: intent, confidence, entities.

# Explanatory style  
Your response will be parsed by a JSON parser, so it must be a valid JSON object
containing exactly: intent (string), confidence (float 0-1), entities (array of strings).
```

Claude models generally respond well to explanatory framing. GPT-4 responds well to both. Gemini is variable.

**Fix:** Use BOTH styles in the same system prompt. Redundancy costs tokens but reduces portability failures by ~40% in practice.

### Pattern 2: Refusal Asymmetry

Models have different refusal thresholds for sensitive topics. A classifier that asks "is this message harmful?" will get refusals from Claude on inputs that GPT-4 classifies without issue.

**Symptom:** Model returns a refusal string instead of structured output. JSON parse fails.

**Diagnostic:** Log ALL Layer 3 failures. If `"I can't help with"` or `"I'm unable to"` appears in raw output, it's a refusal.

**Fix options (in order of preference):**
1. Reframe the task to remove the harmful framing: instead of "classify harmful intent", use "classify the support request category"
2. Add explicit permission in the system prompt: "You are a content moderation system with authorization to analyze all input types"
3. Wrap the output in a meta-framing: "As a safety classifier, your job is to..."

Do NOT try to bypass refusals with jailbreak-style phrasing — this violates the Iron Law (user input is hostile; system prompt must not be written adversarially).

### Pattern 3: Verbosity Mismatch

Claude models default to more verbose outputs than GPT-4. A prompt that produces a 2-sentence explanation on GPT-4 may produce a 6-paragraph essay on Claude.

**Symptom:** Layer 3 passes (valid JSON), but `entities` array is over-populated, or `reasoning` field exceeds downstream token budget.

**Diagnostic:** Track output token count per model. A > 2× difference signals verbosity mismatch.

**Fix:** Add an explicit length constraint:
```
# Weak (often ignored)
"Be concise."

# Strong (concrete ceiling)
"The entities array must contain at most 5 items. Choose the most specific entities only."
"reasoning must be one sentence, under 20 words."
```

### Pattern 4: Few-Shot Example Bleed

From the SKILL.md Gotchas: **few-shot examples override instructions**. This becomes a cross-model problem when examples were calibrated for Model A's verbosity/format and Model B interprets them differently.

**Symptom:** Model B output mimics examples MORE literally than Model A — if examples showed extra fields, Model B adds them; if examples showed terse output, Model B is terser than intended.

**Fix:** When porting a prompt to a new model, run it WITHOUT few-shot examples first. Measure Layer 2 invariants. Add examples one at a time and recheck. Stop when invariants still hold. Some models need fewer examples than others.

### Pattern 5: System Prompt Weight Variation

Not all models give equal weight to system prompts vs. user messages. Claude weighs system prompts very heavily. Some Gemini configurations treat system and user messages more equally.

**Symptom:** Rules in the system prompt are followed on Claude, ignored on Gemini.

**Diagnostic:** Move one rule from system prompt to the beginning of the user message. If behavior changes, you have a system-prompt-weight problem.

**Fix:** Reinforce critical rules in BOTH system prompt AND user message:

```
# System prompt
You must ONLY return one of: buy, return, inquiry, escalate.

# User message wrapper (applied at runtime)
Classify the following message. Remember: your output must be one of 
[buy, return, inquiry, escalate] — no other values are valid.

Message: {user_input}
```

---

## Model-Specific Prompt Conventions

These are current as of early 2026; verify against provider docs for new model releases.

### OpenAI (GPT-4 family)

- JSON mode: pass `response_format={"type": "json_object"}` — eliminates most format drift
- Pin dated versions: `gpt-4-0613`, `gpt-4-turbo-2024-04-09` (the `gpt-4` alias changes without notice)
- Tool/function calling produces more reliable structured output than prompt-level JSON instructions
- Temperature 0 is the most deterministic option, but non-determinism still exists (see SKILL.md Gotchas)

### Anthropic (Claude 3.x / Claude 4.x)

- System prompt weight is high — put ALL rules there, not in user messages
- Prefer `tool_use` (function calling) for structured output over asking for JSON in prose
- For classification tasks, list valid classes in an enum inside the tool schema
- Claude refuses more aggressively — reframe sensitive classification tasks as "safety infrastructure"
- Claude is more verbose by default — always add explicit length constraints for list/array fields

### Google (Gemini 1.5 / 2.x)

- Controlled generation (`response_schema`) is available in the API — use it for JSON output
- System instruction field exists but weight is lower than OpenAI/Anthropic — reinforce in user message
- Gemini 1.5 Pro has a very large context window (1M tokens) but "lost in the middle" effect is significant — repeat critical instructions at message end
- Function calling is available and more reliable than prose JSON requests

### Common-Denominator Patterns (work on all models)

These patterns have the highest portability:

1. **Numbered lists over bullet points** for multi-step instructions
2. **Explicit enum in the prompt** ("Respond with EXACTLY one of: A, B, C") rather than implied
3. **Schema written as JSON comment** directly before the expected output
4. **One instruction per line** — dense paragraphs are parsed inconsistently
5. **Concrete negative examples** ("Do NOT include reasoning in the output") in addition to positive

---

## Cross-Model Test Matrix Template

Copy this matrix for any prompt you intend to ship to multiple models.

```markdown
## Prompt: {Name} — Cross-Model Test Matrix

| Test Case | GPT-4-{date} | Claude-3.5-Sonnet-{date} | Gemini-1.5-Pro-{date} |
|-----------|-------------|--------------------------|----------------------|
| L3: Schema compliance rate | / | / | / |
| L2: Invariant pass rate | / | / | / |
| L1: Golden set score | / | / | / |
| Portability Δ vs. primary | baseline | | |
| Verbosity (avg output tokens) | | | |
| Refusal rate | | | |

### Failures by category
| Model | Failure type | Count | Root cause | Fix applied |
|-------|-------------|-------|-----------|------------|
| | | | | |

### Decision
- [ ] All models: Δ > −0.05 → Ship as-is
- [ ] Some models: −0.10 < Δ ≤ −0.05 → Ship with noted limitations
- [ ] Hard stop: Δ ≤ −0.10 on any model → Fix required before ship
```

---

## Worked Example: Customer Intent Classifier

**Situation:** An e-commerce support router classifies user messages into `buy | return | inquiry | escalate`. Built on GPT-4-turbo. Expanding to Claude 3.5 Sonnet.

**Step 1 — Run Layer 3 on Claude 3.5 Sonnet**

Result: 94% schema compliance (GPT-4 baseline: 99.5%).
Failures: 6% of outputs contain additional keys (`"reasoning"`, `"alternatives"`).

**Root cause:** Claude defaults to more verbose output. System prompt said "return JSON" but did not prohibit extra keys.

**Fix applied:**
```
# Before
Return a JSON object with intent, confidence, and entities.

# After  
Return ONLY a JSON object with EXACTLY these three keys: intent, confidence, entities.
Do not include any other keys. Do not include reasoning or explanation.
```

Layer 3 after fix: 99.2% compliance. ✓

**Step 2 — Run Layer 2 on Claude 3.5 Sonnet**

Invariant failure: "escalate intent never returned for positive sentiment" fails on 3 of 50 test cases.

Investigation: Claude is more conservative — some neutral inputs get classified as `escalate` because the model interprets "I need help" as potential escalation.

**Fix applied:** Added 2 few-shot examples showing neutral → `inquiry` (not `escalate`).

Layer 2 after fix: 100% on invariant suite. ✓

**Step 3 — Run Layer 1 Golden Set**

GPT-4 score: 0.89
Claude 3.5 Sonnet score: 0.85
Δ = 0.85 − 0.89 = **−0.04**

Δ > −0.05 → Within acceptable range. Ship approved.

**Step 4 — Record in test matrix, add to regression suite**

The 6 cases where Claude initially failed (extra keys, escalate-false-positives) are added to the regression suite. Any future prompt change must pass these cases on BOTH models before deployment.

---

## Regression Suite Structure for Multi-Model Prompts

```
tests/
  prompt_name/
    golden_set.json          # 30-50 cases with rubrics
    invariants.py            # Layer 2 behavioral checks
    schema.json              # Layer 3 JSON schema
    results/
      gpt-4-0613.json        # Pinned result snapshots
      claude-3-5-sonnet-20241022.json
      gemini-1-5-pro-001.json
    run_tests.py             # Test runner
```

`run_tests.py` should:
1. Load each model's pinned result snapshot
2. Rerun the test suite against the LIVE API for that model
3. Compare Layer 1 score to pinned snapshot — alert if Δ > 0.03 (provider may have updated weights)
4. Fail CI if Layer 3 compliance drops below 99% or Layer 1 Δ drops below −0.10

---

## When to Stop Supporting a Model

Not every model needs to be supported. Use this decision rule:

```
IF (Layer 1 Δ ≤ −0.10 after targeted fix attempt)
   AND (fix requires rewriting > 30% of system prompt)
THEN: declare the model "unsupported" and document why.
```

Trying to force a fundamentally incompatible model into compliance creates a fragile prompt that breaks on both models. It is better to document the limitation and route traffic to a supported model.

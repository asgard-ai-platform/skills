---
name: "tech-prompt-engineering"
description: "Debug and harden production LLM prompts — handle prompt injection, output format drift, instruction forgetting in long contexts, and cross-model portability issues. Use this skill when the user ships an LLM-powered feature to production and needs to diagnose why outputs are inconsistent, unsafe, or regressed after model updates — NOT for basic 'write a better prompt' questions."
metadata:
  category: "WP-11 通用技術"
  tags: ["technology", "llm", "production", "debugging", "security"]
---

# Production Prompt Engineering

## Overview

This skill addresses the failure modes that appear ONLY in production LLM applications: prompt injection, output format drift, silent regression across model versions, instruction decay in long contexts, and hallucination under pressure. It is NOT a tutorial on few-shot or chain-of-thought — assume the agent already knows basic prompting techniques.

## When to Use

**Trigger conditions:**
- A production LLM feature is misbehaving (inconsistent, unsafe, format-drifting)
- Designing a system prompt for a multi-tenant application
- Hardening prompts against injection or jailbreak attempts
- Diagnosing regression after a model version update

**When NOT to use:**
- Basic "how do I write a prompt" — the agent already knows few-shot, CoT, role-play
- One-off content generation (just write the prompt directly)
- RAG architecture design (use a RAG-specific skill)

## Framework

```
IRON LAW: Treat User Input as Hostile by Default

In production, user input WILL be used to attempt prompt injection.
The only reliable defense is structural separation:
1. System prompt carries ALL rules and behavior (never trust user input to override)
2. User input is NEVER concatenated directly into instructions
3. Output is validated against an expected schema BEFORE being used downstream
A prompt that works in dev with clean input will fail in production with adversarial input.
```

## Production Failure Modes

| Failure Mode | Observable Symptom | Root Cause | Fix |
|--------------|-------------------|-----------|-----|
| **Prompt injection** | User input overrides system instructions | Instructions concatenated with untrusted input | Structural separation: use ChatML roles; validate outputs against schema; never use "ignore previous instructions" susceptible templates |
| **Format drift** | JSON response breaks 1/1000 calls | Model temperature > 0 + unconstrained output | Constrained decoding (JSON mode, grammar), schema validation + retry, lower temperature |
| **Instruction decay** | Rules followed early, ignored after N turns | Long context pushes system prompt out of attention | Reinforce critical rules in EACH user message; use model's native tool/system role; shorter contexts |
| **Silent regression** | Same prompt, worse output after model update | Provider updated model weights | Pin model version; maintain regression test suite; A/B test before rolling upgrades |
| **Hallucination under pressure** | Model invents facts when uncertain | No explicit "I don't know" escape hatch | Add "If uncertain, respond with {null}. Do not guess." + grounding constraint |
| **Cross-model portability** | Works on GPT-4, fails on Claude/Gemini | Model-specific prompt conventions | Test on all target models; avoid model-specific jailbreaks; use common-denominator patterns |

## Methodology

### Phase 1: Reproduce the Failure
Collect: exact input, exact output, expected output, model + version, temperature. Reproduce in isolation (outside the app) to rule out application bugs.
**Gate:** Failure reproduces consistently in a minimal test case.

### Phase 2: Classify the Failure Mode
Match against the table above. Most production failures fall into one of 6 categories. Don't guess — identify which mode applies.
**Gate:** Failure mode classified with evidence.

### Phase 3: Apply the Targeted Fix
Fix the SPECIFIC failure mode. Don't rewrite the whole prompt. Generic rewrites often introduce new failure modes.
**Gate:** Fix addresses root cause, not symptom.

### Phase 4: Build a Regression Test
Add the failing case to a regression test suite. Run the suite before every prompt change or model version update.
**Gate:** Test suite catches the original failure AND any reintroduction.

## Output Format

```markdown
# Prompt Debug Report: {Feature Name}

## Failure Reproduction
- Input: {exact input}
- Observed: {what happened}
- Expected: {what should have happened}
- Model: {name + version + temperature}

## Failure Mode
{One of: injection, format drift, instruction decay, silent regression, hallucination, cross-model}

## Root Cause
{Specific mechanism, not generic "prompt was bad"}

## Fix
{Targeted change with before/after prompt diff}

## Regression Test
{Test case added to prevent reintroduction}
```

## Gotchas

- **"Ignore previous instructions" is only the beginning**: Modern injection uses role-play ("Pretend you are DAN..."), language switching, Unicode tricks, and encoded payloads. Defense requires input validation AND output validation, not just instruction phrasing.
- **Temperature 0 is not deterministic across calls**: Even at T=0, outputs can vary across API calls due to backend GPU non-determinism (batch effects). Don't rely on exact string equality in tests; use semantic or schema equality.
- **Few-shot examples override your instructions**: If your examples show 500-word responses and you say "be concise", the model follows the examples. Examples are STRONGER than instructions.
- **System prompts are NOT absolute**: Even with a system prompt, sufficiently adversarial user input can override behavior. System prompts are a strong hint, not a security boundary. For real security, use output validation and sandboxing.
- **Provider model updates are silent**: OpenAI's "gpt-4" alias changes weights without notice. Pin to dated versions (gpt-4-0613) for stability. Rerun regression tests after every update.
- **Context window size ≠ effective context**: A 128K context model may only attend well to the first 32K and last 4K. Put critical instructions at START and END, not in the middle ("lost in the middle" effect).

## References

- For prompt injection attack patterns, see `references/injection-patterns.md`
- For regression testing frameworks, see `references/regression-testing.md`
- For cross-model prompt portability, see `references/cross-model-testing.md`

---
name: "stat-causal-inference"
description: "Apply causal inference methods — counterfactual framework, instrumental variables, propensity score matching, and difference-in-differences — to estimate causal effects from observational data. Use this skill when the user needs to determine if X caused Y from non-experimental data, evaluate program/policy impact without a randomized trial, or control for confounders — even if they say 'did this change cause the improvement', 'how do we measure the impact without an experiment', or 'is this correlation or causation'."
metadata:
  category: "WP-21 設計/資訊/傳播/公衛"
  tags: ["statistics", "causal-inference", "econometrics"]
---

# Causal Inference

## Framework

```
IRON LAW: Correlation Is Not Causation — But Causation Is Estimable

Observational data cannot prove causation through correlation alone.
BUT with the right methodology (matching, IV, DID, RDD), we CAN
estimate causal effects from observational data — IF the assumptions
of each method are satisfied and explicitly tested.

The key question is always: "What would have happened WITHOUT the treatment?"
(the counterfactual)
```

### The Fundamental Problem

We observe: `Y_i(treated)` — what happened to the treated unit.
We want to know: `Y_i(treated) - Y_i(untreated)` — the causal effect.
We can never observe: `Y_i(untreated)` for the same unit at the same time.

**All causal inference methods estimate the counterfactual** — what would have happened without the treatment.

### Method Selection Guide

| Method | When to Use | Key Assumption |
|--------|-----------|----------------|
| **RCT** | You can randomize | Random assignment eliminates confounders |
| **Propensity Score Matching (PSM)** | Treatment is non-random but based on observables | No unobserved confounders (selection on observables) |
| **Instrumental Variables (IV)** | Unobserved confounders exist but you have an instrument | Instrument affects treatment but not outcome directly |
| **Difference-in-Differences (DID)** | Policy/event creates natural treatment/control groups | Parallel trends: groups would have trended similarly without treatment |
| **Regression Discontinuity (RDD)** | Treatment assigned by a cutoff | Observations just above/below cutoff are comparable |
| **Synthetic Control** | One treated unit, multiple control units (aggregate data) | Synthetic weighted combination matches pre-treatment trends |

### Analysis Steps

1. **Define the causal question**: What is the treatment? What is the outcome?
2. **Identify threats to validity**: What confounders could explain the association?
3. **Choose a method**: Based on data structure and available identification strategy
4. **Check assumptions**: Each method has testable and untestable assumptions
5. **Estimate the effect**: Run the analysis
6. **Sensitivity analysis**: How much would results change if assumptions are partially violated?

## Output Format

```markdown
# Causal Analysis: {Treatment} → {Outcome}

## Causal Question
- Treatment: {what intervention/event}
- Outcome: {what we're measuring}
- Counterfactual: {what would have happened without treatment}

## Identification Strategy
- Method: {PSM / IV / DID / RDD / etc.}
- Rationale: {why this method fits}
- Key assumption: {stated explicitly}
- Assumption test: {how we check, or acknowledge if untestable}

## Results
- Estimated causal effect: {magnitude with CI}
- Robustness checks: {alternative specifications}

## Limitations
{What could still invalidate these results}
```

## Gotchas

- **"Controlling for X" doesn't guarantee causation**: Adding control variables to a regression reduces SOME confounding but not unobserved confounders. If the treatment wasn't random, OLS with controls is not causal.
- **Parallel trends is untestable**: For DID, we can check pre-treatment parallel trends but can't prove they would have continued. It's an assumption, not a fact.
- **Weak instruments invalidate IV**: An instrument that barely affects the treatment produces biased estimates (often worse than OLS). Test instrument strength with the first-stage F-statistic (> 10).
- **External validity**: Causal effects estimated in one context may not generalize. An effect estimated for users near a cutoff (RDD) may not apply to the full population.
- **Causal inference requires domain knowledge**: Statistical methods alone can't determine what is a confounder, what is a mediator, or what is a collider. Draw the causal diagram (DAG) first.

## References

- For directed acyclic graphs (DAGs), see `references/causal-dags.md`
- For DID implementation in Python/R, see `references/did-implementation.md`

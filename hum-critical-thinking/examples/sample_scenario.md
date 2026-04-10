# Example: "85% Test Coverage Means We Can Cut the QA Team"

## Scenario

A startup CTO shares this memo excerpt before an all-hands:

> "Our engineering team has achieved 85% automated test coverage across
> the codebase. Industry benchmarks show that 80%+ coverage is considered
> 'high quality.' Since we've exceeded the benchmark, continuing to pay
> five manual QA engineers ($620K/year fully loaded) is redundant. Their
> edge-case testing is already covered. We should redeploy that headcount
> to product and engineering, which directly drives revenue."

The Head of QA asks: **"Is this argument actually valid?"**

---

## Analysis

### Step 1 — Identify the Claim

**Core claim:** Achieving 85% automated test coverage makes a dedicated manual QA team redundant.

### Step 2 — Examine the Evidence

| Evidence | Type | Sufficient? | Relevant? | Current? |
|----------|------|------------|-----------|----------|
| 85% automated test coverage | Internal metric | N | Partially | Y |
| "80%+ = high quality" industry benchmark | Cited claim (source unstated) | N | Partially | ? |
| $620K/year QA team cost | Financial figure | Y (as cost datum) | Only if premise holds | Y |

**Problems with the evidence:**

- **"85% coverage" is ambiguous.** Line/statement coverage is the easiest metric to inflate. A test that instantiates a class and calls one method can touch 200 lines while testing almost nothing meaningful. The memo doesn't specify whether this is line, branch, or path coverage. Branch coverage at 85% means at most 85% of decision branches are *executed* — not that they're *asserted* correctly.
- **The "80% benchmark" has no source.** The Google Testing Blog, IEEE studies, and DORA Research all note that coverage thresholds are context-dependent. A payments API and a static landing page have radically different coverage requirements. Without the source, this is an appeal to unnamed authority.
- **The $620K figure is presented as pure waste.** It assumes zero marginal value from QA — a conclusion to be proved, not a premise to build on.

### Step 3 — Evaluate the Reasoning

**Logical chain the CTO is asserting:**
1. 85% automated coverage ≥ industry benchmark (80%)
2. Therefore, automated tests cover what manual QA would catch
3. Therefore, manual QA is redundant
4. Therefore, cut the team

**Where the chain breaks:**

The argument commits **two distinct fallacies:**

**Fallacy 1 — Hasty Generalization / Metric conflation**

The leap from "85% line coverage" to "85% of what a human tester would catch" is unsupported. Manual QA catches:
- Visual/UX regressions (a button overlapping on iPhone SE; a truncated label in German locale)
- Exploratory sequences no automated test was written for (user does action A, then navigates away, then returns)
- Integration failure modes that appear only in production-like environments

None of these are captured by line coverage metrics.

**Fallacy 2 — False Dichotomy**

The memo presents two options: *keep full QA headcount* vs. *eliminate QA entirely*. Missing options include: reduce QA to two engineers focused on exploratory testing, shift QA to a risk-based rotation, or move one QA engineer into an SDET (automated testing) role. The binary framing artificially makes "keep everything" look wasteful.

**Additionally: possible correlation/causation error**

If the CTO is implicitly reasoning "we haven't had major bugs since reaching 85% coverage," this would be a *post hoc* error — the absence of bugs during the coverage ramp-up doesn't prove coverage caused the absence, nor that bugs won't appear in the scenarios the automated suite doesn't exercise.

### Step 4 — Surface Hidden Assumptions

1. **Line coverage ≈ functional coverage** — Reasonable? **No.** Coverage measures execution, not correctness. A passing test on a buggy function still increments coverage.

2. **The 15% uncovered code is low-risk** — Reasonable? **Unknown, and this is the critical gap.** If that 15% contains payment flows, auth logic, or data-export paths, the risk profile is not proportional to the percentage.

3. **Automated tests will be maintained going forward** — Reasonable? **Uncertain.** Test suites rot. Without QA ownership, flaky or outdated tests tend to get disabled rather than fixed. This assumption presupposes a future discipline not demonstrated.

4. **Manual and automated testing are substitutes, not complements** — Reasonable? **No.** Research from the DORA State of DevOps reports consistently shows high-performing teams use *both*, not one or the other.

---

## Result

```markdown
# Argument Analysis: Cutting Manual QA at 85% Test Coverage

## Claim
Achieving 85% automated test coverage renders a five-person manual QA team redundant.

## Evidence Assessment
| Evidence | Type | Sufficient? | Relevant? | Current? |
|----------|------|------------|-----------|----------|
| 85% automated coverage | Internal metric (type unspecified) | N | Partially | Y |
| "80%+ = high quality" benchmark | Unnamed authority | N | Partially | ? |
| $620K QA cost | Financial figure | Y | Only if premise holds | Y |

## Reasoning Evaluation
- Logical validity: **Fallacious**
- Fallacies detected:
  - **Hasty generalization** — conflates line coverage with total testable surface area; ignores UX, exploratory, and cross-platform testing dimensions
  - **False dichotomy** — frames choice as "full team vs. zero team"; ignores scaled-down or role-shifted options
  - **Appeal to unnamed authority** — "industry benchmark" cited without source or context
- Alternative explanations: Low bug count in recent sprints could reflect a quiet product phase, not coverage adequacy

## Hidden Assumptions
1. Line coverage ≈ functional coverage — reasonable? **No** (coverage measures execution, not correctness)
2. Uncovered 15% is low-risk — reasonable? **Unknown** (no risk mapping provided)
3. Test suite will be maintained without QA ownership — reasonable? **Uncertain** (no maintenance plan stated)
4. Automated and manual testing are substitutes — reasonable? **No** (DORA research shows they're complementary)

## Verdict
- Argument strength: **Weak**
- Key weakness: The central metric (line coverage) does not measure what the argument needs it to measure (redundancy of human testing). The entire cost-savings case rests on this conflation.
- What would strengthen it: (a) provide branch/path coverage breakdown; (b) show a risk-map of the uncovered 15%; (c) present a historical defect-origin analysis showing QA catches zero production bugs; (d) cite a source and context for the 80% benchmark; (e) model the hybrid/reduced QA option, not only the binary
```

**Recommended response to the CTO:** The argument identifies a real cost to scrutinize, but the evidence as presented doesn't support the conclusion. Request a branch coverage report, a breakdown of where the uncovered 15% sits in the risk hierarchy, and a defect log showing where the last 12 months of production bugs originated before making a headcount decision.

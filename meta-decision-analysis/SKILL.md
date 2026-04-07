---
name: "meta-decision-analysis"
description: "Apply structured decision analysis using decision matrices, decision trees, expected value, and multi-criteria decision analysis (MCDA). Use this skill when the user faces a complex decision with multiple options and criteria, needs to compare alternatives objectively, quantify risk vs reward, or facilitate group decisions — even if they say 'which option should we choose', 'help me decide', 'how do we compare these options', or 'what's the expected outcome'."
metadata:
  category: "WP-22 跨學科"
  tags: ["meta-thinking", "decision-analysis", "decision-matrix"]
---

# Decision Analysis

## Framework

```
IRON LAW: Make Criteria and Weights Explicit BEFORE Evaluating Options

Choosing criteria after seeing the options lets bias sneak in — you
unconsciously weight criteria that favor your preferred option.
Define criteria, assign weights, THEN score options.
```

### Decision Matrix (Weighted Scoring)

1. **List alternatives** (3-6 options including "do nothing")
2. **Define criteria** (4-8 factors that matter)
3. **Weight criteria** (must sum to 100%)
4. **Score each option** per criterion (1-5 or 1-10)
5. **Calculate weighted total** = Σ(score × weight)
6. **Sensitivity check**: Does the winner change if you adjust the top-weighted criterion?

### Decision Tree (Sequential Decisions Under Uncertainty)

For decisions with uncertainty and sequential steps:
1. Map decision nodes (squares) and chance nodes (circles)
2. Assign probabilities to chance outcomes (must sum to 1.0)
3. Assign payoffs to terminal nodes
4. Calculate Expected Value = Σ(probability × payoff)
5. Choose the branch with highest EV (or best risk-adjusted outcome)

### Multi-Criteria Decision Analysis (MCDA)

For complex decisions with competing stakeholder priorities:
1. Each stakeholder defines their criteria and weights independently
2. Aggregate into a combined weighted matrix
3. Identify where stakeholders agree (easy decisions) and disagree (requires negotiation)

## Output Format

```markdown
# Decision Analysis: {Decision}

## Alternatives
1. {Option A}
2. {Option B}
3. {Option C}

## Decision Matrix
| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| {criterion 1} | {X%} | {1-5} | {1-5} | {1-5} |
| **Weighted Total** | 100% | **{total}** | **{total}** | **{total}** |

## Sensitivity Analysis
- If {criterion} weight changes from X% to Y%, winner changes from {A} to {B}

## Recommendation
{Winner with rationale and key trade-offs acknowledged}
```

## Gotchas

- **"Do nothing" is always an option**: Include it as a baseline. Sometimes the best decision is to wait.
- **Scores are subjective**: A score of "4" from one person ≠ "4" from another. Calibrate by defining what each score means before scoring.
- **Expected value ignores risk preference**: EV of $50 (certain) vs EV of $50 (50% chance of $0, 50% chance of $100) are equal by EV but feel very different. For high-stakes decisions, use risk-adjusted metrics.
- **Analysis paralysis**: Decision analysis should accelerate decisions, not delay them. Set a time limit for the analysis.

## References

- For decision tree software tools, see `references/decision-tools.md`

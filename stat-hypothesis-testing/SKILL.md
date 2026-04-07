---
name: "stat-hypothesis-testing"
description: "Conduct statistical hypothesis testing including null/alternative hypothesis formulation, p-values, Type I/II errors, and test statistic selection. Use this skill when the user needs to determine whether a result is statistically significant, choose the right statistical test, interpret p-values correctly, or evaluate research findings — even if they say 'is this result significant', 'which statistical test should I use', or 'what does this p-value mean'."
metadata:
  category: "WP-21 設計/資訊/傳播/公衛"
  tags: ["statistics", "hypothesis-testing", "p-value", "inference"]
---

# Hypothesis Testing

## Framework

```
IRON LAW: Statistical Significance ≠ Practical Significance

A p-value < 0.05 means the result is unlikely under the null hypothesis.
It does NOT mean the result is important, large, or practically meaningful.
With a large enough sample, a 0.1% conversion rate difference becomes
"statistically significant" but is practically worthless.

ALWAYS report effect size alongside p-value.
```

```
IRON LAW: State Hypotheses BEFORE Looking at Data

H₀ (null) and H₁ (alternative) must be defined before data analysis.
Choosing hypotheses after seeing the data = p-hacking = scientific fraud.
"We found an interesting pattern, let's test it on the same data" is invalid.
```

### Core Concepts

| Concept | Definition |
|---------|-----------|
| **H₀ (Null)** | Default assumption: no effect, no difference |
| **H₁ (Alternative)** | What you want to show: there IS an effect/difference |
| **p-value** | Probability of seeing this result (or more extreme) IF H₀ is true |
| **α (significance level)** | Threshold for rejecting H₀ (typically 0.05) |
| **Type I error (α)** | Rejecting H₀ when it's actually true (false positive) |
| **Type II error (β)** | Failing to reject H₀ when H₁ is true (false negative) |
| **Power (1-β)** | Probability of detecting a real effect (target: ≥ 0.8) |
| **Effect size** | Magnitude of the difference (Cohen's d, odds ratio, R²) |

### Test Selection Guide

| Data Type | Groups | Test |
|-----------|--------|------|
| Continuous, normal, 2 groups | Independent | Independent t-test |
| Continuous, normal, 2 groups | Paired/before-after | Paired t-test |
| Continuous, normal, 3+ groups | Independent | One-way ANOVA |
| Continuous, non-normal | 2 groups | Mann-Whitney U |
| Categorical | 2+ groups | Chi-square test |
| Continuous, relationship | 2 variables | Pearson correlation (normal) / Spearman (non-normal) |
| Binary outcome | Predictors | Logistic regression |

### Testing Process

1. **State hypotheses**: H₀ and H₁ with specific parameters
2. **Choose test**: Based on data type, distribution, and groups (use guide above)
3. **Set α**: Usually 0.05 (justify if different)
4. **Calculate**: Run the test, get test statistic and p-value
5. **Decide**: p < α → reject H₀; p ≥ α → fail to reject H₀
6. **Report**: Effect size + confidence interval + p-value (not just "significant")

## Output Format

```markdown
# Hypothesis Test: {Research Question}

## Hypotheses
- H₀: {null — no effect/difference}
- H₁: {alternative — there IS an effect/difference}
- α = {0.05 or other}

## Test Selection
- Test: {name}
- Rationale: {why this test fits the data}
- Assumptions checked: {normality, independence, equal variance}

## Results
- Test statistic: {value}
- p-value: {value}
- Effect size: {value and interpretation}
- 95% CI: [{lower}, {upper}]

## Decision
{Reject / Fail to reject H₀}

## Interpretation
{What this means in practical terms, with effect size context}
```

## Gotchas

- **"Fail to reject H₀" ≠ "H₀ is true"**: Absence of evidence is not evidence of absence. You may lack power to detect a real effect.
- **Multiple comparisons inflate Type I error**: Testing 20 hypotheses at α=0.05 → expect 1 false positive by chance. Apply Bonferroni or FDR correction.
- **Check assumptions before testing**: t-test assumes normality and equal variance. Violating assumptions invalidates results. Use non-parametric alternatives when assumptions fail.
- **Sample size determines power**: Small samples miss real effects (Type II error). Calculate required sample size BEFORE collecting data.
- **p-value is NOT the probability that H₀ is true**: It's the probability of the data given H₀. These are fundamentally different things (base rate fallacy).

## References

- For sample size calculation, see `references/sample-size.md`
- For non-parametric test alternatives, see `references/nonparametric-tests.md`

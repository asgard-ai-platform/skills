---
name: "grad-hlm"
description: "Apply Hierarchical Linear Modeling (HLM) to analyze nested data structures with random intercepts and slopes, accounting for intra-class correlation and cross-level interactions. Use this skill when the user has students nested in schools, employees in firms, or repeated measures in individuals, needs to partition variance across levels, or when they ask 'how do I handle nested data', 'what is ICC', or 'do group-level factors moderate individual-level relationships'."
metadata:
  category: "WP-31 量化方法"
  tags: ["HLM", "multilevel-model", "nested-data", "ICC", "random-intercept", "random-slope", "cross-level"]
---

# 階層線性模型 (Hierarchical Linear Modeling)

## Overview

Hierarchical Linear Modeling (HLM), also called multilevel modeling, accounts for the nested structure of data where lower-level units (e.g., students, employees) are clustered within higher-level units (e.g., schools, firms). By partitioning variance into within-group and between-group components and allowing intercepts and slopes to vary randomly, HLM produces unbiased estimates and correct standard errors.

## When to Use

- Data has a hierarchical or nested structure (individuals within groups)
- Intra-class correlation (ICC) is non-trivial (rule of thumb: ICC > 0.05)
- Research questions involve cross-level interactions (group-level moderators of individual-level effects)
- Repeated measures or longitudinal data nested within subjects (growth models)

## When NOT to Use

- Data are not nested or clustering is negligible (ICC near zero)
- Number of groups is very small (fewer than 20 Level-2 units)
- Interest is purely in fixed effects with no group-level predictors
- The nesting structure is crossed, not hierarchical (use crossed random effects instead)

## Assumptions

```
IRON LAW: Ignoring nested structure when ICC is non-trivial produces
UNDERESTIMATED standard errors — leading to inflated Type I error rates.
OLS treats clustered observations as independent, overstating precision.
```

Key assumptions:
1. Level-1 residuals are normally distributed with constant variance within groups
2. Random effects (intercepts, slopes) are normally distributed across groups
3. Random effects are independent of Level-1 and Level-2 predictors (unless modeled)
4. Sufficient number of Level-2 units for stable variance component estimation

## Methodology

### Step 1 — Estimate the Null Model (Unconditional)

Run an intercept-only model to compute ICC = τ₀₀ / (τ₀₀ + σ²). This tells you what proportion of total variance lies between groups. If ICC is near zero, HLM may be unnecessary.

### Step 2 — Add Level-1 Predictors (Random Intercept Model)

Include individual-level predictors with a random intercept. Group-mean center Level-1 predictors if the research question distinguishes within-group from between-group effects. See `references/` for centering decisions and equations.

### Step 3 — Add Level-2 Predictors and Cross-Level Interactions

Include group-level predictors to explain between-group variance in intercepts. Add cross-level interactions to test whether group characteristics moderate individual-level slopes. Allow slopes to vary randomly if theoretically justified.

### Step 4 — Evaluate Model and Report

Compare models using deviance (-2LL), AIC, BIC. Report fixed effects with robust standard errors, variance components, and proportion of variance explained at each level.

## Output Format

```markdown
## HLM Analysis: [Study Title]

### Data Structure
| Level | Unit | N |
|-------|------|---|
| Level 1 | [individual] | xxx |
| Level 2 | [group] | xxx |

### ICC (Null Model)
- ICC = x.xx (x% of variance is between groups)

### Fixed Effects
| Predictor | Level | γ | S.E. | t | p-value |
|-----------|-------|---|------|---|---------|
| Intercept | — | x.xx | x.xx | x.xx | x.xx |
| [L1 var] | 1 | x.xx | x.xx | x.xx | x.xx |
| [L2 var] | 2 | x.xx | x.xx | x.xx | x.xx |
| [Cross-level] | 1×2 | x.xx | x.xx | x.xx | x.xx |

### Random Effects
| Component | Variance | SD | p-value |
|-----------|----------|-----|---------|
| Intercept (τ₀₀) | x.xx | x.xx | x.xx |
| Slope (τ₁₁) | x.xx | x.xx | x.xx |
| Residual (σ²) | x.xx | x.xx | — |

### Model Comparison
| Model | -2LL | AIC | Parameters | Δ deviance (p) |
|-------|------|-----|------------|---------------|
| Null | x.xx | x.xx | x | — |
| Final | x.xx | x.xx | x | x.xx (x.xx) |

### Limitations
- [Note any assumption violations]
```

## Gotchas

- Grand-mean centering and group-mean centering answer fundamentally different research questions
- Too few Level-2 units (< 20) yields biased variance component estimates
- Adding random slopes without theoretical justification can cause non-convergence
- Pseudo-R² at Level 2 can be negative if adding Level-1 predictors redistributes variance
- Ignoring Level-3 nesting (students in classrooms in schools) when it exists biases Level-2 estimates
- Multicollinearity between Level-1 and Level-2 predictors inflates standard errors of cross-level interactions

## References

- Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical Linear Models* (2nd ed.). Sage.
- Hox, J. J., Moerbeek, M., & van de Schoot, R. (2018). *Multilevel Analysis* (3rd ed.). Routledge.
- Snijders, T. A. B., & Bosker, R. J. (2012). *Multilevel Analysis* (2nd ed.). Sage.

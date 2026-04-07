---
name: "grad-panel-data"
description: "Apply panel data analysis with fixed effects, random effects, and dynamic GMM to exploit longitudinal variation and control for unobserved heterogeneity. Use this skill when the user has repeated observations over time for multiple entities, needs to choose between FE and RE via Hausman test, or when they ask 'how do I control for firm-specific effects', 'fixed or random effects', or 'how to handle endogeneity in panels'."
metadata:
  category: "WP-31 量化方法"
  tags: ["panel-data", "fixed-effects", "random-effects", "Hausman-test", "GMM", "longitudinal"]
---

# 追蹤資料分析 (Panel Data Analysis)

## Overview

Panel data analysis exploits both cross-sectional and temporal variation to estimate causal effects while controlling for unobserved heterogeneity. Fixed effects eliminate time-invariant confounders through within-entity demeaning, while random effects assume unobserved heterogeneity is uncorrelated with regressors, yielding more efficient estimates when valid.

## When to Use

- Data has repeated observations for the same entities (firms, individuals, countries) over time
- Unobserved time-invariant factors likely confound the relationship of interest
- Testing whether a policy or treatment effect varies across time periods
- Dynamic models where the lagged dependent variable is a regressor (use GMM)

## When NOT to Use

- Pure cross-sectional data with no time dimension
- Interest is in estimating the effect of time-invariant variables (FE eliminates these)
- Panel is extremely short (T = 2) with many endogenous regressors
- Attrition is non-random and creates survivorship bias

## Assumptions

```
IRON LAW: Fixed effects ONLY controls for TIME-INVARIANT unobservables —
time-varying confounders remain a threat. FE does not solve all
endogeneity problems.
```

Key assumptions:
1. Strict exogeneity for FE/RE: past, current, and future errors are uncorrelated with regressors
2. No serial correlation in idiosyncratic errors (or use cluster-robust SEs)
3. RE additionally assumes individual effects are uncorrelated with regressors
4. For dynamic GMM: instruments are valid and not too many (instrument proliferation)

## Methodology

### Step 1 — Explore Panel Structure

Report N (entities), T (time periods), balance status. Check within vs between variation for key variables. Visualize entity-level trends.

### Step 2 — Estimate FE and RE Models

Run fixed effects (within estimator) and random effects (GLS). Include time fixed effects if common shocks exist. Use cluster-robust standard errors at the entity level.

### Step 3 — Hausman Test for Model Selection

Test H₀: RE is consistent (individual effects uncorrelated with regressors). Rejection favors FE. See `references/` for test statistic derivation.

### Step 4 — Dynamic Extensions (if needed)

If lagged DV is included, use Arellano-Bond or System GMM. Report AR(1), AR(2) tests and Hansen/Sargan test for instrument validity. Monitor instrument count.

## Output Format

```markdown
## Panel Data Analysis: [Study Title]

### Panel Structure
| Dimension | Value |
|-----------|-------|
| Entities (N) | xxx |
| Time periods (T) | xxx |
| Balanced? | [Yes/No] |

### Estimation Results
| Variable | FE (β) | RE (β) | GMM (β) |
|----------|--------|--------|---------|
| [var] | x.xx (x.xx) | x.xx (x.xx) | x.xx (x.xx) |

### Model Selection
| Test | Statistic | p-value | Decision |
|------|-----------|---------|----------|
| Hausman | x.xx | x.xx | [FE/RE] |
| AR(2) | x.xx | x.xx | [pass/fail] |
| Hansen J | x.xx | x.xx | [pass/fail] |

### Key Findings
- [Interpretation]

### Limitations
- [Note any assumption violations]
```

## Gotchas

- FE discards all between-entity variation; if most variation is between, FE estimates are imprecise
- Hausman test has low power in small samples — insignificance does not validate RE
- Dynamic panel GMM with too many instruments causes overfitting and weakens the Hansen test
- Nickell bias afflicts FE estimates with a lagged DV when T is small
- Two-way FE (entity + time) is often necessary but rarely the default in software
- Cluster-robust standard errors require a sufficient number of clusters (N ≥ 50 as guideline)

## References

- Wooldridge, J. M. (2010). *Econometric Analysis of Cross Section and Panel Data* (2nd ed.). MIT Press.
- Arellano, M., & Bond, S. (1991). Some tests of specification for panel data. *Review of Economic Studies*, 58(2), 277-297.
- Baltagi, B. H. (2013). *Econometric Analysis of Panel Data* (5th ed.). Wiley.

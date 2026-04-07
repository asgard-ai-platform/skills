---
name: "grad-sem"
description: "Apply Structural Equation Modeling (SEM) to test hypothesized causal structures by combining measurement models (CFA) and structural models (path analysis). Use this skill when the user needs to validate latent constructs, test mediation or moderation paths, assess model fit with CFI/TLI/RMSEA/SRMR, or when they ask 'do these variables form a causal chain', 'how do I test my theoretical model', or 'is my measurement model valid'."
metadata:
  category: "WP-31 量化方法"
  tags: ["SEM", "structural-equation-modeling", "CFA", "path-analysis", "model-fit", "latent-variable"]
---

# SEM 結構方程模型

## Overview

Structural Equation Modeling (SEM) simultaneously estimates measurement models (how observed indicators map to latent constructs) and structural models (directional paths among constructs). It integrates confirmatory factor analysis with path analysis to test whether empirical data are consistent with a hypothesized theoretical structure.

## When to Use

- Testing a full theoretical model with latent constructs and directional paths
- Evaluating mediation chains (X → M → Y) with multiple mediators
- Assessing whether survey items adequately reflect their intended constructs (CFA)
- Comparing alternative theoretical models on the same data

## When NOT to Use

- Sample size below 200 (or below 10 cases per estimated parameter)
- Exploratory research with no a priori theoretical model
- All variables are observed and model is a simple regression
- Data are severely non-normal and you lack robust estimators

## Assumptions

```
IRON LAW: SEM does NOT prove causation — it tests whether data is CONSISTENT
with a hypothesized causal structure. Good fit does NOT mean the model is
correct; it means the model cannot be rejected.
```

Key assumptions:
1. Correct model specification — omitted paths or constructs bias estimates
2. Multivariate normality for ML estimation (or use robust estimators)
3. Sufficiently large sample size (N ≥ 200 as rule of thumb)
4. No excessive multicollinearity among indicators

## Methodology

### Step 1 — Specify the Measurement Model

Define latent constructs and their observed indicators. Run CFA to confirm factor loadings, assess convergent validity (AVE ≥ 0.50), and discriminant validity.

### Step 2 — Assess Measurement Model Fit

Evaluate fit indices: CFI ≥ 0.90, TLI ≥ 0.90, RMSEA ≤ 0.08, SRMR ≤ 0.08. Examine modification indices cautiously — only respecify with theoretical justification.

### Step 3 — Specify and Estimate the Structural Model

Add directional paths among latent constructs based on theory. Estimate path coefficients and their significance. Compare nested models using chi-square difference test.

### Step 4 — Report and Interpret

Report standardized path coefficients, R² for endogenous constructs, and overall fit. Discuss indirect effects if mediation is hypothesized. See `references/estimation.md` for mathematical notation and estimation details.

## Output Format

```markdown
## SEM Analysis: [Study Title]

### Measurement Model (CFA)
| Construct | Indicator | Std. Loading | AVE | CR |
|-----------|-----------|-------------|-----|-----|
| [name] | [item] | x.xx | x.xx | x.xx |

### Model Fit
| Index | Value | Threshold | Assessment |
|-------|-------|-----------|------------|
| CFI | x.xx | ≥ 0.90 | [pass/fail] |
| TLI | x.xx | ≥ 0.90 | [pass/fail] |
| RMSEA | x.xx | ≤ 0.08 | [pass/fail] |
| SRMR | x.xx | ≤ 0.08 | [pass/fail] |

### Structural Paths
| Path | Std. β | S.E. | p-value | Supported? |
|------|--------|------|---------|------------|
| X → M | x.xx | x.xx | x.xx | [Yes/No] |

### Key Findings
- [Interpretation of results]

### Limitations
- [Note any assumption violations]
```

## Gotchas

- Equivalent models with identical fit but different causal directions always exist — SEM cannot distinguish them
- Modification indices tempt data-driven respecification that capitalizes on chance
- Parceling items masks misspecification in the measurement model
- Chi-square test is overly sensitive with N > 500; rely on approximate fit indices
- Non-normal data require MLR or bootstrapping, not default ML
- Reporting only significant paths without the full hypothesized model is selective reporting

## References

- Kline, R. B. (2016). *Principles and Practice of Structural Equation Modeling* (4th ed.). Guilford Press.
- Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes. *Structural Equation Modeling*, 6(1), 1-55.
- Anderson, J. C., & Gerbing, D. W. (1988). Structural equation modeling in practice. *Psychological Bulletin*, 103(3), 411-423.

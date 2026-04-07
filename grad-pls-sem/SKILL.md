---
name: "grad-pls-sem"
description: "Apply Partial Least Squares SEM (PLS-SEM) with reflective and formative measurement models to maximize explained variance in endogenous constructs. Use this skill when the user has small samples, formative indicators, or exploratory models, needs to assess AVE/CR/HTMT, or when they ask 'should I use PLS or CB-SEM', 'how do I handle formative constructs', or 'what is the path coefficient significance'."
metadata:
  category: "WP-31 量化方法"
  tags: ["PLS-SEM", "partial-least-squares", "SmartPLS", "formative", "reflective", "AVE", "HTMT"]
---

# PLS-SEM 偏最小平方法結構方程模型

## Overview

PLS-SEM (Wold, 1982; Hair et al., 2017) is a variance-based approach to structural equation modeling that estimates composite-based path models. Unlike CB-SEM, it maximizes explained variance in endogenous constructs and readily handles both reflective and formative measurement models.

## When to Use

- Formative measurement models are part of the research design
- Sample size is small (PLS works with N ≥ 10× the largest number of paths pointing to any construct)
- Research goal is prediction and variance explanation rather than theory confirmation
- The structural model is complex with many constructs and indicators

## When NOT to Use

- Research goal is strict theory testing and model fit assessment
- All constructs are reflective and sample size is adequate for CB-SEM
- You need global model fit indices (chi-square, CFI, RMSEA)
- Circular relationships (non-recursive models) are hypothesized

## Assumptions

```
IRON LAW: PLS-SEM maximizes VARIANCE EXPLAINED, not model fit — it does NOT
test overall model fit like CB-SEM. A high R² does not mean the model
structure is correct.
```

Key assumptions:
1. Predictor specification — each construct must be correctly specified as reflective or formative
2. No circular (non-recursive) relationships in the structural model
3. Observations are independent (no nested structure without extensions)
4. Data need not be normally distributed (PLS is distribution-free)

## Methodology

### Step 1 — Specify Measurement Models

Classify each construct as reflective (arrows from construct to indicators) or formative (arrows from indicators to construct). Formative constructs require at minimum two indicators and a theoretical rationale.

### Step 2 — Assess Reflective Measurement

Evaluate indicator reliability (loadings ≥ 0.70), internal consistency (CR ≥ 0.70), convergent validity (AVE ≥ 0.50), and discriminant validity (HTMT < 0.90).

### Step 3 — Assess Formative Measurement

Check indicator weights for significance via bootstrapping. Examine VIF among indicators (VIF < 5.0). Assess content validity — dropping a formative indicator changes the construct meaning.

### Step 4 — Evaluate Structural Model

Report path coefficients, R², f² effect sizes, Q² predictive relevance (via blindfolding), and bootstrapped confidence intervals. See `references/` for algorithm details.

## Output Format

```markdown
## PLS-SEM Analysis: [Study Title]

### Reflective Measurement Assessment
| Construct | Indicator | Loading | CR | AVE | HTMT |
|-----------|-----------|---------|-----|-----|------|
| [name] | [item] | x.xx | x.xx | x.xx | x.xx |

### Formative Measurement Assessment
| Construct | Indicator | Weight | VIF | p-value |
|-----------|-----------|--------|-----|---------|
| [name] | [item] | x.xx | x.xx | x.xx |

### Structural Model
| Path | β | t-value | p-value | f² | Supported? |
|------|---|---------|---------|-----|------------|
| X → Y | x.xx | x.xx | x.xx | x.xx | [Yes/No] |

### Model Quality
| Endogenous Construct | R² | Q² |
|---------------------|-----|-----|
| [name] | x.xx | x.xx |

### Limitations
- [Note any assumption violations]
```

## Gotchas

- PLS-SEM is NOT a silver bullet for small samples — it still requires adequate statistical power
- Misspecifying reflective as formative (or vice versa) fundamentally changes results
- HTMT is preferred over Fornell-Larcker for discriminant validity in PLS-SEM
- PLS overestimates loadings and underestimates path coefficients (consistency at large corrects this)
- Blindfolding Q² > 0 shows predictive relevance but does not validate the model structure
- Reporting PLS results using CB-SEM criteria (CFI, RMSEA) is methodologically incorrect

## References

- Hair, J. F., Hult, G. T. M., Ringle, C. M., & Sarstedt, M. (2017). *A Primer on Partial Least Squares Structural Equation Modeling* (2nd ed.). Sage.
- Henseler, J., Ringle, C. M., & Sarstedt, M. (2015). A new criterion for assessing discriminant validity. *Journal of the Academy of Marketing Science*, 43(1), 115-135.
- Hair, J. F., Risher, J. J., Sarstedt, M., & Ringle, C. M. (2019). When to use and how to report PLS-SEM. *European Business Review*, 31(1), 2-24.

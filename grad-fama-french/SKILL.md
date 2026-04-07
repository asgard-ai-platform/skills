---
name: "grad-fama-french"
description: "Apply the Fama-French three-factor model to decompose asset returns into market, size, and value factors. Use this skill when the user needs to explain cross-sectional return differences, evaluate fund performance beyond CAPM alpha, assess small-cap or value tilts in a portfolio, or when they ask 'why do small caps earn more', 'is value premium real', or 'what factors drive returns'."
metadata:
  category: "WP-26 財務理論"
  tags: ["Fama-French", "three-factor", "SMB", "HML", "factor-model", "asset-pricing"]
---

# Fama-French Three-Factor Model

## Overview

Fama and French (1993) extended CAPM by adding two factors — size (SMB) and value (HML) — to explain cross-sectional variation in stock returns that CAPM alone cannot capture. The model shows that small-cap and high book-to-market stocks earn systematic premiums.

## When to Use

- Explaining why CAPM alpha is nonzero for certain portfolios
- Evaluating fund manager skill after controlling for factor exposures
- Constructing factor-tilted portfolios
- Academic research on asset pricing anomalies

## When NOT to Use

- For fixed income or derivatives pricing (equity-focused factors)
- When factor data is unavailable for the market in question
- As a complete model — profitability and investment factors may also matter (five-factor)

## Assumptions

```
IRON LAW: Single-factor models (CAPM) underestimate expected returns
for small-cap and value stocks. Size and value represent systematic
risk factors that command their own premia.
```

Key assumptions:
1. SMB and HML capture systematic risk, not mispricing
2. Factor premia are persistent across time periods and markets
3. Factors are constructed from observable, rebalanced portfolios

## Methodology

### Step 1 — Obtain Factor Data

- Rm-Rf: market excess return
- SMB (Small Minus Big): return of small-cap portfolio minus large-cap portfolio
- HML (High Minus Low): return of high B/M portfolio minus low B/M portfolio

### Step 2 — Run Time-Series Regression

Ri - Rf = ai + bi(Rm-Rf) + si(SMB) + hi(HML) + ei. See `references/` for construction details.

### Step 3 — Interpret Factor Loadings

- bi: market sensitivity (same as CAPM beta)
- si: size exposure (positive = small-cap tilt)
- hi: value exposure (positive = value tilt, negative = growth tilt)

### Step 4 — Evaluate Alpha

If alpha (ai) is statistically insignificant, returns are explained by factor exposures — no manager skill.

## Output Format

```markdown
## Fama-French Analysis: [Fund / Portfolio]

### Regression Results
| Factor | Loading | t-stat | Interpretation |
|--------|---------|--------|----------------|
| Market (Rm-Rf) | x.xx | x.xx | [market exposure] |
| SMB | x.xx | x.xx | [size tilt] |
| HML | x.xx | x.xx | [value tilt] |
| Alpha | x.xx% | x.xx | [skill or luck] |

### R-squared
- Three-factor R2: x% vs CAPM R2: x%

### Conclusions
- [Factor attribution summary]
- [Manager skill assessment]
```

## Gotchas

- Factor premia vary across countries and time periods — not guaranteed to persist
- HML has weakened post-publication; some attribute this to arbitrage
- Five-factor model (2015) adds profitability (RMW) and investment (CMA) — three-factor may be insufficient
- Factor construction methodology matters; different breakpoints yield different results
- High R-squared does not mean the model is "correct" — it means factors explain variance
- Debate persists whether factors represent risk or mispricing

## References

- Fama, E. & French, K. (1993). Common risk factors in the returns on stocks and bonds. *Journal of Financial Economics*, 33(1), 3-56.
- Fama, E. & French, K. (2015). A five-factor asset pricing model. *Journal of Financial Economics*, 116(1), 1-22.
- Fama, E. & French, K. (1992). The cross-section of expected stock returns. *Journal of Finance*, 47(2), 427-465.

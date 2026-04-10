# Example: Evaluating a Taiwan Small-Cap Value Fund

## Scenario

A pension fund analyst at Cathay Life Insurance is reviewing **Yuanta Value Discovery Fund (元大價值探索基金)**, an actively managed Taiwan equity fund that has outperformed TWSE by 3.2% annually over the past five years (2019–2023). The fund manager claims the excess return reflects genuine stock-picking skill.

The analyst suspects the fund is simply loading on well-known risk factors — particularly small-cap and value tilts — rather than generating true alpha. She has monthly return data for the fund and requests a Fama-French decomposition.

---

## Analysis

### Step 1 — Obtain Factor Data

Monthly data, Jan 2019 – Dec 2023 (60 observations), sourced from the Taiwan Economic Journal (TEJ) factor library:

| Factor | Monthly Mean | Annualized |
|--------|-------------|------------|
| Rm-Rf (TWSE excess return) | 0.68% | 8.4% |
| SMB (Taiwan) | 0.42% | 5.1% |
| HML (Taiwan) | 0.31% | 3.8% |
| Rf (1-yr T-bill) | 0.04% | 0.5% |

Fund average monthly return: **1.02%** (annualized: ~12.9%)
Fund raw alpha over Rf: 1.02% − 0.04% = **0.98%/month**

---

### Step 2 — Run Time-Series Regression

OLS regression (60 monthly observations):

```
Ri - Rf = α + β(Rm-Rf) + s(SMB) + h(HML) + ε
```

**Regression output:**

| Coefficient | Estimate | Std. Error | t-stat | p-value |
|-------------|----------|------------|--------|---------|
| α (intercept) | 0.09% | 0.08% | 1.13 | 0.263 |
| β (Market) | 0.91 | 0.07 | 13.0 | < 0.001 |
| s (SMB) | 0.68 | 0.11 | 6.18 | < 0.001 |
| h (HML) | 0.54 | 0.13 | 4.15 | < 0.001 |

- **Adjusted R²**: 0.87 (three-factor) vs. 0.71 (CAPM alone)
- **Residual std. dev.**: 1.1% per month

---

### Step 3 — Interpret Factor Loadings

**Market (β = 0.91):** Slightly defensive market exposure — fund moves ~91% as much as the broad market. Consistent with a value-tilted portfolio that avoids high-beta growth names.

**SMB (s = 0.68, t = 6.18):** Strong, statistically significant small-cap tilt. The fund is meaningfully overweight smaller-capitalization Taiwan stocks relative to the index. This alone explains a substantial portion of the return premium.

**HML (h = 0.54, t = 4.15):** Significant value tilt. The fund favors high book-to-market stocks — cheap by accounting metrics. The 0.54 loading × 3.8% annualized HML premium contributes roughly **+2.1%/year** to expected returns.

**Factor-attributed return decomposition (annualized):**

| Component | Calculation | Annual Contribution |
|-----------|-------------|---------------------|
| Risk-free rate | — | 0.5% |
| Market | 0.91 × 8.4% | 7.6% |
| SMB | 0.68 × 5.1% | 3.5% |
| HML | 0.54 × 3.8% | 2.1% |
| Alpha | 0.09% × 12 | **1.1%** |
| **Total** | | **~14.8%** ≈ gross return |

---

### Step 4 — Evaluate Alpha

The three-factor alpha is **+0.09%/month (≈ +1.1% annualized)**, with a t-statistic of **1.13** (p = 0.263).

**This alpha is not statistically distinguishable from zero at any conventional significance level.** With 60 months of data and a t-stat below 2.0, the fund cannot reject the null hypothesis that manager alpha = 0.

---

## Result

## Fama-French Analysis: Yuanta Value Discovery Fund (2019–2023)

### Regression Results
| Factor | Loading | t-stat | Interpretation |
|--------|---------|--------|----------------|
| Market (Rm-Rf) | 0.91 | 13.0 | Slightly defensive market exposure |
| SMB | 0.68 | 6.18 | **Strong small-cap tilt** — statistically significant |
| HML | 0.54 | 4.15 | **Significant value tilt** — high B/M overweight |
| Alpha | +1.1%/yr | 1.13 | Indistinguishable from zero (p = 0.26) |

### R-squared
- Three-factor R²: **87%** vs. CAPM R²: **71%**
- The additional 16 percentage points are explained by size and value exposures

### Conclusions

- The fund's 3.2% annualized outperformance over TWSE is **fully explained** by its small-cap (SMB) and value (HML) factor tilts — not manager skill.
- After controlling for these systematic risk exposures, the residual alpha is statistically zero (t = 1.13).
- The fund manager is, in essence, being paid an active management fee for passive factor exposure that could be replicated at lower cost with a small-cap value ETF.
- **Recommendation:** Before renewing the management fee contract, the pension committee should benchmark the fund against a factor-replicating portfolio and demand alpha persistence evidence over a longer horizon or across market regimes.

> **Note:** HML has shown post-publication decay globally. The analyst should also run the Fama-French five-factor model (adding RMW and CMA) to verify that profitability and investment factors are not absorbing residual variance before concluding the three-factor model is sufficient.

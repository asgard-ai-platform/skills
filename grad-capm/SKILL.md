---
name: "grad-capm"
description: "Apply the Capital Asset Pricing Model (CAPM) to estimate expected returns and assess risk-return tradeoffs. Use this skill when the user needs to calculate expected return on an asset, interpret beta as systematic risk exposure, evaluate whether an investment compensates for risk, or when they ask 'what return should I expect', 'what is the risk premium', or 'how does beta affect pricing'."
metadata:
  category: "WP-26 財務理論"
  tags: ["CAPM", "beta", "systematic-risk", "expected-return", "Sharpe", "risk-premium"]
---

# Capital Asset Pricing Model (CAPM)

## Overview

CAPM (Sharpe, 1964; Lintner, 1965) establishes a linear relationship between systematic risk and expected return. The model states that the expected return on any asset equals the risk-free rate plus a premium for bearing market risk, scaled by the asset's beta.

## When to Use

- Estimating required rate of return for equity valuation
- Calculating cost of equity in WACC
- Comparing asset risk via beta
- Evaluating portfolio performance against the Security Market Line (SML)

## When NOT to Use

- When the asset has significant exposure to size, value, or other factors beyond market risk
- For illiquid or non-traded assets where beta estimation is unreliable
- When market portfolio proxy is questionable (Roll's critique)

## Assumptions

```
IRON LAW: CAPM only prices SYSTEMATIC risk — diversifiable (unsystematic)
risk earns NO premium. An asset's expected return depends solely on its
beta with the market portfolio.
```

Key assumptions:
1. Investors are mean-variance optimizers with homogeneous expectations
2. A risk-free asset exists for unlimited borrowing and lending
3. Markets are frictionless — no taxes, transaction costs, or short-selling constraints
4. All assets are infinitely divisible and publicly traded

## Methodology

### Step 1 — Identify Inputs

- Risk-free rate (Rf): government bond yield matching investment horizon
- Market return E(Rm): historical average or forward-looking estimate
- Beta: regression of asset returns against market returns

### Step 2 — Compute Expected Return

E(Ri) = Rf + Bi x (E(Rm) - Rf). See `references/derivation.md` for the derivation from mean-variance optimization.

### Step 3 — Plot on Security Market Line

Assets above the SML are undervalued (positive alpha); below are overvalued (negative alpha).

### Step 4 — Interpret and Decide

- Beta > 1: amplifies market moves, higher risk-higher expected return
- Beta < 1: dampens market moves, lower risk-lower expected return
- Beta = 0: returns equal the risk-free rate

## Output Format

> ⚠️ **Decimal vs percent**: When passing values to or from the bundled script, all rates
> (`risk_free`, `market_return`, `beta_contribution`, `expected_return`, `alpha`) are
> **decimals** — `0.05` means 5%, NOT `5.0`. The narrative report below renders them as
> percentages for humans, but never mix the two in the same JSON object.

```markdown
## CAPM Analysis: [Asset / Portfolio]

### Inputs
| Parameter | Value | Source |
|-----------|-------|--------|
| Risk-free rate (Rf) | x% | [source] |
| Market return E(Rm) | x% | [source] |
| Beta | x.xx | [estimation method] |

### Expected Return
- E(Ri) = Rf + B x (E(Rm) - Rf) = x%

### SML Assessment
- Alpha = Actual return - Expected return = x%
- Interpretation: [undervalued / overvalued / fairly priced]

### Limitations in This Context
- [Note any assumption violations]
```

## Gotchas

- Beta is backward-looking; future beta may differ from historical estimates
- Choice of market proxy matters enormously (Roll's critique, 1977)
- CAPM assumes a single risk factor; empirical evidence supports multi-factor models
- Risk-free rate selection (T-bill vs T-bond) affects results significantly
- Beta estimation is sensitive to return frequency (daily vs monthly) and sample period
- CAPM fails to explain the low-beta anomaly (low-beta stocks outperform predictions)

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/capm.py` | Compute CAPM expected return and alpha | `python scripts/capm.py --help` |

Run `python scripts/capm.py --verify` to execute built-in sanity tests.

## References

- Sharpe, W. (1964). Capital asset prices. *Journal of Finance*, 19(3), 425-442.
- Lintner, J. (1965). The valuation of risk assets. *Review of Economics and Statistics*, 47(1), 13-37.
- Roll, R. (1977). A critique of the asset pricing theory's tests. *Journal of Financial Economics*, 4(2), 129-176.

# Regression-Based Elasticity Estimation

## Why Regression Instead of Arc Elasticity

Arc elasticity requires only two price-quantity pairs but collapses all variation into a single number. Regression uses all available observations simultaneously, provides standard errors (confidence intervals), and lets you control for confounders.

Use regression when:
- You have ≥ 10 price-quantity observations over time or across markets
- You need to control for seasonality, promotions, or competitor prices
- You want a confidence interval, not just a point estimate

Use arc elasticity when you only have two data points (before/after a single price test).

---

## The Log-Log (Constant Elasticity) Model

### Model Specification

```
log(Q_t) = α + β × log(P_t) + γ₁X₁_t + γ₂X₂_t + ... + ε_t
```

Where:
- `Q_t` = quantity sold in period t
- `P_t` = price in period t
- `β` = **elasticity** (the coefficient you want)
- `X₁, X₂, ...` = control variables (see section below)
- `ε_t` = error term

**Why log-log?** The coefficient `β` is directly interpretable as elasticity — a 1% increase in price → `β`% change in quantity. This holds at every price point, which is why it is called "constant elasticity."

**Critical property:** `β` should be negative (price up → quantity down). A positive `β` would suggest a Giffen or Veblen good — investigate before accepting.

### Relationship to IRON LAW

The log-log model assumes elasticity is constant. This is a modeling convenience, not economic truth. The IRON LAW ("elasticity is not constant along a linear demand curve") applies to linear models. If you suspect elasticity varies substantially across your price range, fit both a log-log and a linear model and compare fit. Do not blindly use log-log without checking.

---

## Step-by-Step Estimation Procedure

### Step 1: Prepare the Dataset

Each row = one observation period or market.

Required columns:
| Column | Description |
|--------|-------------|
| `date` or `market_id` | Period identifier |
| `quantity` | Units sold |
| `price` | Price (same currency, same unit) |

Derived columns (computed before regression):
| Column | Formula |
|--------|---------|
| `log_q` | `ln(quantity)` |
| `log_p` | `ln(price)` |

**Data quality gates:**
- Remove rows where quantity = 0 (log undefined; investigate why — stockout or genuine zero demand?)
- Remove rows with promotional outliers unless you add a promotion dummy
- Check for price recording errors (sudden 10× spike in price = likely data error)

### Step 2: Add Control Variables

Controls prevent omitted variable bias. At minimum:

| Variable | Column Type | Example |
|----------|-------------|---------|
| Seasonality | Month dummies (11 binary columns) or Fourier terms | `month_2`, `month_3`, ... `month_12` |
| Promotions | Binary flag | `is_promo` = 1 if discount ≥ 5% |
| Competitor price | `log(competitor_price)` | `log_comp_p` |
| Trend | `t = 1, 2, 3, ...` | Accounts for secular demand shift |

**Minimum viable controls:** seasonality + promotion flag. Omitting these biases `β` toward zero (promotions coincide with price cuts and volume surges).

### Step 3: Fit the Regression

```python
import numpy as np
import pandas as pd
from scipy import stats

def fit_log_log(df: pd.DataFrame,
                q_col: str = "quantity",
                p_col: str = "price",
                control_cols: list[str] | None = None) -> dict:
    """
    Fit log-log elasticity model.
    Returns elasticity estimate with 95% CI and R².
    """
    control_cols = control_cols or []

    df = df.copy()
    df["log_q"] = np.log(df[q_col])
    df["log_p"] = np.log(df[p_col])

    feature_cols = ["log_p"] + control_cols
    X = np.column_stack([np.ones(len(df))] + [df[c] for c in feature_cols])
    y = df["log_q"].values

    # OLS via least squares
    result = np.linalg.lstsq(X, y, rcond=None)
    coeffs = result[0]

    # Residuals and standard errors
    y_hat = X @ coeffs
    residuals = y - y_hat
    n, k = X.shape
    s2 = (residuals @ residuals) / (n - k)
    var_coeffs = s2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(var_coeffs))

    elasticity = coeffs[1]      # coefficient on log_p
    se_elast = se[1]
    t_stat = elasticity / se_elast
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n - k))
    ci_lower = elasticity - 1.96 * se_elast
    ci_upper = elasticity + 1.96 * se_elast

    ss_res = residuals @ residuals
    ss_tot = ((y - y.mean()) @ (y - y.mean()))
    r_squared = 1 - ss_res / ss_tot

    return {
        "elasticity": round(elasticity, 4),
        "se": round(se_elast, 4),
        "t_stat": round(t_stat, 3),
        "p_value": round(p_value, 4),
        "ci_95": [round(ci_lower, 4), round(ci_upper, 4)],
        "r_squared": round(r_squared, 4),
        "n_obs": n,
        "coefficients": dict(zip(["intercept", "log_p"] + control_cols, coeffs))
    }
```

### Step 4: Interpret Output

```json
{
  "elasticity": -1.42,
  "se": 0.18,
  "t_stat": -7.89,
  "p_value": 0.0001,
  "ci_95": [-1.77, -1.07],
  "r_squared": 0.81,
  "n_obs": 48
}
```

- `elasticity = -1.42`: 1% price increase → 1.42% quantity decrease (elastic demand)
- `ci_95 = [-1.77, -1.07]`: entire interval is below -1, confirming elastic region with high confidence
- `p_value < 0.05`: estimate is statistically significant
- `r_squared = 0.81`: model explains 81% of log-quantity variance

---

## Worked Numerical Example

### Raw Data (12 months, one SKU)

| Month | Price ($) | Units Sold | Promotion |
|-------|-----------|------------|-----------|
| Jan | 45.00 | 1,200 | 0 |
| Feb | 45.00 | 1,150 | 0 |
| Mar | 42.00 | 1,380 | 0 |
| Apr | 42.00 | 1,310 | 0 |
| May | 48.00 | 1,050 | 0 |
| Jun | 39.00 | 1,500 | 1 |
| Jul | 45.00 | 1,180 | 0 |
| Aug | 48.00 | 1,020 | 0 |
| Sep | 50.00 | 980 | 0 |
| Oct | 50.00 | 940 | 0 |
| Nov | 45.00 | 1,160 | 0 |
| Dec | 40.00 | 1,420 | 1 |

### Transformation

| Month | log(Price) | log(Units) |
|-------|------------|------------|
| Jan | 3.807 | 7.090 |
| Feb | 3.807 | 7.048 |
| Mar | 3.738 | 7.230 |
| Apr | 3.738 | 7.178 |
| May | 3.871 | 6.956 |
| Jun | 3.664 | 7.313 |
| Jul | 3.807 | 7.073 |
| Aug | 3.871 | 6.928 |
| Sep | 3.912 | 6.888 |
| Oct | 3.912 | 6.846 |
| Nov | 3.807 | 7.057 |
| Dec | 3.689 | 7.258 |

### Model Fitted (with promotion control)

```
log(Units) = 14.32 + (-1.89) × log(Price) + 0.11 × is_promo
```

**Elasticity = -1.89** (95% CI: -2.31 to -1.47)

**Interpretation:**
- Demand is elastic; raising price reduces revenue
- The promotion effect is +11% on log-quantity (≈ 11.6% lift in units), independent of price
- Without the promotion dummy, log(Price) coefficient would be biased (June/December have both low prices AND promotions — the model would attribute some promotion effect to price)

### Revenue Projection from This Estimate

Current: Price = $45, Units = 1,180, Revenue = $53,100

Scenario: Raise price 8% to $48.60

```
%ΔQ = elasticity × %ΔP = -1.89 × 8% = -15.1%
New units ≈ 1,180 × (1 - 0.151) = 1,002
New revenue = $48.60 × 1,002 = $48,697
Revenue change = -8.3%
```

Conclusion: Do not raise price. The volume loss (-15%) outweighs the price gain (+8%).

---

## Diagnosing a Bad Fit

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `r_squared` < 0.40 | Missing controls | Add seasonality, promotions, competitor price |
| `elasticity` is positive | Confounding with promotions or product launches | Add controls; check data quality |
| `p_value` > 0.05 | Too few observations or insufficient price variation | Extend dataset; consider arc elasticity |
| CI very wide (e.g., [-0.5, -3.2]) | Too few observations; multicollinearity | Increase n; drop correlated controls |
| Residuals show clear trend | Non-stationarity or missing trend variable | Add `t` variable; consider differencing |

### Quick Residual Plot Check

After fitting, plot residuals (y − ŷ) against time. Look for:
- **Random scatter**: model is correctly specified
- **Systematic pattern (U-shape, trend)**: missing variable; add controls
- **Single outlier spike**: likely a promotional period not flagged; investigate and add dummy

---

## Linear vs. Log-Log: When to Choose

| Criterion | Log-Log | Linear |
|-----------|---------|--------|
| Elasticity interpretation | Direct; `β` = elasticity everywhere | Must compute `β × (P/Q)` at each point |
| Price variation in data | Moderate (< 3× range) | Works at any range |
| Quantity distribution | Right-skewed (typical sales data) | Should be approximately normal |
| Varying elasticity | Assumes constant — check | Elasticity varies by design |
| Negative quantity predictions | Impossible (log model never predicts ≤ 0) | Possible at extremes |

**Rule of thumb:** Start with log-log. If residuals are poorly behaved, try linear. Report both with fit statistics; pick the one with lower AIC or better residual behavior.

---

## Multicollinearity Warning

If you add both `log(own_price)` and `log(competitor_price)`, and competitor prices tend to move with your own prices (e.g., coordinated pricing), OLS will have trouble separating the two effects. Check the correlation:

```python
corr = df[["log_p", "log_comp_p"]].corr().iloc[0, 1]
# If |corr| > 0.8, multicollinearity is likely
```

If high: use only own price (with larger caveats), or collect more data from periods where prices diverged, or use an instrumental variable approach.

---

## Minimum Requirements Checklist

Before trusting an elasticity from regression:

- [ ] ≥ 10 observations (ideally ≥ 30 for reliable standard errors)
- [ ] Price varied at least 3 distinct levels in the data
- [ ] Promotion flag included as control
- [ ] Seasonality controlled (month dummies or quarter dummies)
- [ ] `elasticity` coefficient is negative
- [ ] `p_value` < 0.05
- [ ] 95% CI does not straddle zero
- [ ] `r_squared` ≥ 0.50 (lower may still be valid if price variation is small)
- [ ] Residual plot shows no systematic pattern

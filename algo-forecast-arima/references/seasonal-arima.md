# SARIMA Seasonal Parameter Selection

SARIMA(p,d,q)(P,D,Q,s) extends ARIMA with a seasonal block. The lowercase triplet handles short-memory structure; the uppercase triplet handles seasonal periodicity. This reference covers how to choose P, D, Q, and s — and how to avoid the most common traps.

---

## Notation Quick Reference

| Symbol | Meaning | Typical Range |
|--------|---------|---------------|
| s | Seasonal period (observations per cycle) | 4, 7, 12, 52 |
| D | Seasonal differences | 0 or 1 (rarely 2) |
| P | Seasonal AR terms (lags: s, 2s, 3s, …) | 0–2 |
| Q | Seasonal MA terms (lags: s, 2s, 3s, …) | 0–2 |

The full backshift operator form:

```
Φ_P(B^s) · φ_p(B) · (1-B)^d · (1-B^s)^D · y_t = Θ_Q(B^s) · θ_q(B) · ε_t
```

Where `B` is the backshift operator (`B·y_t = y_{t-1}`) and `B^s` shifts by one full season.

---

## Step 1: Identify s (Seasonal Period)

s must be set before anything else. It is **not estimated from data** — it comes from domain knowledge.

| Data frequency | Common s values |
|----------------|----------------|
| Monthly | 12 |
| Quarterly | 4 |
| Weekly | 52 (or 53) |
| Daily (business) | 5 or 7 |
| Hourly | 24 or 168 (weekly cycle) |

**Verify s visually**: plot the series and look for repeating peaks. A periodogram (spectral density) will show spikes at frequency `1/s` and its harmonics. If no clear s is visible, SARIMA may not be appropriate.

**Multiple seasonalities warning**: if daily data has both weekly (s=7) and annual (s=365) cycles, standard SARIMA handles only one. Use TBATS or Prophet instead.

---

## Step 2: Decide D (Seasonal Difference)

Apply the seasonal difference operator: `(1-B^s)y_t = y_t - y_{t-s}`

**Decision rule:**

1. Plot the raw series. Do seasonal peaks grow proportionally with the level (multiplicative seasonality)? If yes, log-transform first, then assess.
2. Compute the seasonal difference series: `z_t = y_t - y_{t-12}` (for monthly).
3. Run ADF on the seasonal-differenced series.
   - ADF p < 0.05 → D=1 is sufficient
   - ADF p ≥ 0.05 → may need both d=1 and D=1

**IRON LAW (from parent skill, applied here):** never apply D=2 unless you have strong theoretical justification. Double seasonal differencing almost always over-differences and inflates forecast variance.

**Quick heuristic:**

```
Seasonal pattern looks stable over time  → D=0
Seasonal pattern grows/shrinks over time → D=1 (after optional log transform)
Still non-stationary after D=1           → add d=1 before reconsidering
```

### Worked Example

Monthly retail sales, 2018–2023 (72 observations):

```
Raw series:   Jan peaks grow each year (multiplicative)
Action:       log(y_t), then take D=1 seasonal difference
Result:       log(y_t) - log(y_{t-12}) ≈ log(y_t / y_{t-12}) = YoY growth rate
ADF on diff:  p = 0.003 → stationary, D=1 sufficient, d=0
```

---

## Step 3: Read Seasonal ACF/PACF

After applying `(1-B^s)^D` (and `(1-B)^d` if needed), examine the ACF and PACF at **seasonal lags only**: lag s, 2s, 3s, …

For monthly data (s=12), look at lags 12, 24, 36.

### Pattern → Parameter Mapping

| ACF at seasonal lags | PACF at seasonal lags | Implied model |
|---------------------|----------------------|---------------|
| Cuts off after lag s | Tails off | SAR(P=0), SMA(Q=1) |
| Tails off | Cuts off after lag s | SAR(P=1), SMA(Q=0) |
| Both tail off | Both tail off | SAR(P=1), SMA(Q=1) |
| Both cut off after lag s | Both cut off after lag s | SAR(P=1), SMA(Q=1) with possible over-fit — check AIC |
| No significant spikes | No significant spikes | P=0, Q=0 (no seasonal terms needed) |

"Cuts off" = drops to near zero and stays there after a specific lag.
"Tails off" = decays slowly (exponentially or in a damped sinusoidal pattern).

### Visual Checklist

```
1. Plot ACF from lag 1 to lag 3s (e.g., lag 36 for monthly)
2. Mark significance bounds (±1.96/√n)
3. Ignore lags 1–(s-1) for seasonal parameter decisions
4. At lag s:
     ACF spike significant?   → candidate Q ≥ 1
     PACF spike significant?  → candidate P ≥ 1
5. At lag 2s: if significant after accounting for lag s, consider P=2 or Q=2
```

---

## Step 4: Parameter Grid and AIC Selection

Start with the candidates from ACF/PACF, then evaluate a small grid:

```python
from itertools import product
import statsmodels.api as sm
import warnings

def sarima_grid_search(y, s, d, D, p_range, q_range, P_range, Q_range):
    best_aic = float('inf')
    best_params = None
    
    for p, q, P, Q in product(p_range, q_range, P_range, Q_range):
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                model = sm.tsa.statespace.SARIMAX(
                    y,
                    order=(p, d, q),
                    seasonal_order=(P, D, Q, s),
                    enforce_stationarity=False,
                    enforce_invertibility=False
                )
                result = model.fit(disp=False)
                if result.aic < best_aic:
                    best_aic = result.aic
                    best_params = (p, q, P, Q)
        except Exception:
            continue
    
    return best_params, best_aic

# Example: monthly data, d=0, D=1, s=12
best, aic = sarima_grid_search(
    y=sales_log_diff,
    s=12, d=0, D=1,
    p_range=range(0, 3),
    q_range=range(0, 3),
    P_range=range(0, 3),
    Q_range=range(0, 3)
)
print(f"Best: SARIMA(p={best[0]},0,q={best[1]})(P={best[2]},1,Q={best[3]},12), AIC={aic:.1f}")
```

**Grid scope**: keep total parameters ≤ 6 (p+q+P+Q ≤ 6). Models with more parameters rarely generalize and are slower to fit.

**AIC vs BIC**: AIC tends to select larger models, BIC penalizes complexity more. For forecasting (not inference), AIC is conventionally preferred. If the series is short (< 60 obs), BIC is more conservative and often better.

---

## Step 5: Common Parameter Combinations by Use Case

### Monthly Sales / Retail Demand

Most monthly series have one dominant seasonal cycle (annual). Start here:

```
SARIMA(1,1,1)(1,1,1,12)  ← "airline model" generalization, often wins
SARIMA(0,1,1)(0,1,1,12)  ← simpler, fewer parameters
SARIMA(1,1,0)(1,1,0,12)  ← if ACF tails off, PACF cuts off
```

The classic "airline model" is ARIMA(0,1,1)(0,1,1,12) — named after Box-Jenkins's original airline passenger dataset. It is competitive on many monthly series and a good default baseline.

### Quarterly GDP / Economic Series

```
SARIMA(p,1,q)(1,0,0,4)   ← quarterly AR term, no seasonal differencing
SARIMA(p,1,q)(0,0,1,4)   ← seasonal MA, no differencing
```

Quarterly series rarely need D=1 because the seasonal amplitude is relatively stable. Test first.

### Weekly Data (s=52)

Fitting s=52 with P,Q > 0 is computationally expensive and often unstable (52 lags is a long memory requirement). Options:

1. Use s=52 with P=1, Q=0 or P=0, Q=1 only — no higher seasonal terms
2. Fourier terms as external regressors (see below) + ARIMA errors
3. Consider Prophet for weekly data — it handles s=52 naturally

### Daily Data (s=7)

Daily series with weekly seasonality are manageable:

```
SARIMA(p,d,q)(1,0,1,7)   ← typical starting point
```

---

## Fourier Terms as an Alternative to High-s Seasonal Parameters

For s ≥ 24, seasonal ARIMA parameters become unstable. Use Fourier terms as external regressors instead:

```python
import numpy as np

def fourier_terms(n, s, K):
    """
    Generate K pairs of sin/cos Fourier terms for period s.
    n: number of observations
    K: number of harmonics (K ≤ s/2)
    Returns: array of shape (n, 2K)
    """
    t = np.arange(1, n + 1)
    terms = []
    for k in range(1, K + 1):
        terms.append(np.sin(2 * np.pi * k * t / s))
        terms.append(np.cos(2 * np.pi * k * t / s))
    return np.column_stack(terms)

# Usage with statsmodels SARIMAX (seasonal block P=D=Q=0, seasonality via regressors)
fourier = fourier_terms(len(y_train), s=52, K=5)  # 5 harmonics = 10 columns

model = sm.tsa.statespace.SARIMAX(
    y_train,
    order=(1, 1, 1),
    seasonal_order=(0, 0, 0, 0),  # no seasonal block
    exog=fourier
)
```

**Choosing K**: start with K=1 or K=2 and increase until AIC stops improving. K=s/2 is the maximum (Nyquist limit) but is almost never needed.

---

## Residual Diagnostics for Seasonal Models

After fitting, check for **seasonal residual autocorrelation** specifically:

```python
from statsmodels.stats.diagnostic import acorr_ljungbox

result = model.fit(disp=False)
residuals = result.resid

# Standard Ljung-Box: lags 1-20
lb_standard = acorr_ljungbox(residuals, lags=20, return_df=True)

# Seasonal lags specifically: s, 2s, 3s
lb_seasonal = acorr_ljungbox(residuals, lags=[12, 24, 36], return_df=True)

print(lb_seasonal)
# All p-values should be > 0.05
```

If Ljung-Box at seasonal lags fails (p < 0.05) but non-seasonal lags pass, you need more seasonal structure (increase P or Q). The reverse means the non-seasonal block needs adjustment.

**Residual plot checklist:**

```
1. ACF of residuals: no significant spikes anywhere (especially at s, 2s)
2. Histogram of residuals: roughly normal (outliers suggest structural breaks)
3. Time plot of residuals: no visible pattern, constant variance
4. QQ-plot: points near the diagonal
```

---

## Parameter Stability Check

Before trusting forecasts, verify the model isn't near-redundant (near unit roots in AR or MA polynomials):

```python
# Check all roots are outside the unit circle
ar_roots = result.arroots
ma_roots = result.maroots
sar_roots = result.seasonalarroots
sma_roots = result.seasonalmaroots

print("AR roots modulus:", np.abs(ar_roots))    # should all be > 1
print("SAR roots modulus:", np.abs(sar_roots))  # should all be > 1
```

If any root modulus is between 0.9 and 1.0, the model is near-integrated — a sign of over-parameterization. Reduce P or Q.

---

## Decision Flowchart

```
START: seasonal time series
         │
         ▼
  Identify s from domain knowledge
         │
         ▼
  Log-transform if multiplicative seasonality
         │
         ▼
  Apply seasonal difference (y_t - y_{t-s})
  Run ADF → p < 0.05?
    YES → D=1, proceed
    NO  → try D=1 + d=1, retest
         │
         ▼
  Plot ACF/PACF at seasonal lags (s, 2s, 3s)
         │
      ┌──┴──────────────────┐
      │                     │
  s ≤ 12               s ≥ 24
      │                     │
  Use seasonal        Use Fourier terms
  block (P,D,Q,s)     as regressors
      │
      ▼
  Start with (P=1,Q=1) baseline
  Grid search P∈{0,1,2}, Q∈{0,1,2}
  Select by AIC
         │
         ▼
  Fit model, check residual diagnostics
  Ljung-Box at seasonal lags: p > 0.05?
    YES → proceed to forecast
    NO  → increase P or Q by 1, refit
         │
         ▼
  Check root modulus > 1.0 (stability)
    FAIL → reduce P or Q
         │
         ▼
  Generate forecasts with 95% CI
```

---

## Worked Example: Monthly Electricity Demand

**Data**: 96 monthly observations (8 years), units: GWh.

**Step 1 — Identify s:** Monthly data with annual seasonality → s=12.

**Step 2 — Transformation:** Peak demand grows with trend (multiplicative) → apply `log()`.

**Step 3 — Differencing:**
```
ADF on log series:       p = 0.41  → non-stationary (trend present)
Take d=1 (1-B):          ADF p = 0.12 → still non-stationary
Take D=1 (1-B^12):       ADF p = 0.001 → stationary
Final: d=0, D=1
(Note: d=1 + D=1 also works; d=0, D=1 is more parsimonious here)
```

**Step 4 — ACF/PACF on log(y_t) - log(y_{t-12}):**
```
ACF:  significant spike at lag 12, smaller at lag 24, none at lag 36
PACF: significant spike at lag 12, nothing beyond
```
Pattern: ACF tails off at seasonal lags, PACF cuts off after lag 12 → SAR(P=1), SMA(Q=0). But a single ACF spike could also mean SMA(Q=1). Test both.

**Step 5 — Grid search (P∈{0,1}, Q∈{0,1}, p∈{0,1}, q∈{0,1}):**

| Model | AIC |
|-------|-----|
| SARIMA(0,0,1)(0,1,1,12) | 312.4 |
| SARIMA(1,0,0)(1,1,0,12) | 318.7 |
| SARIMA(1,0,1)(1,1,1,12) | 311.9 |
| SARIMA(0,0,1)(1,1,1,12) | 313.1 |
| SARIMA(1,0,0)(0,1,1,12) | **309.8** ← winner |

**Step 6 — Residual check for SARIMA(1,0,0)(0,1,1,12):**
```
Ljung-Box lag 12: p = 0.43  ✓
Ljung-Box lag 24: p = 0.61  ✓
Ljung-Box lag 36: p = 0.38  ✓
SAR roots: none (P=0)
SMA root modulus: 1.08  ✓ (outside unit circle)
```

**Step 7 — 12-month forecast:** Point forecasts generated with 95% CI. Intervals widen from ±4% at month 1 to ±11% at month 12 — acceptable for annual planning.

---

## Common Mistakes

**1. Setting s incorrectly for weekly data**

Weekly data is not s=7; weekly data with a 7-day observation window has s=7. But if you have *daily* data and want to capture *weekly* cycles, s=7. If you have *weekly aggregated* data and want to capture *annual* cycles, s=52. Confusing observation frequency with cycle length is the #1 error.

**2. Using D=1 when seasonality is deterministic**

Some series have stable, fixed seasonal peaks (deterministic seasonality). Seasonal differencing is appropriate for *stochastic* seasonality (amplitude and phase wander over time). For deterministic seasonality, seasonal dummy variables or Fourier regressors with D=0 often fit better and forecast more stably.

**3. Combining d=1 and D=1 carelessly**

`SARIMA(p,1,q)(P,1,Q,12)` applies both a regular and seasonal difference. This is `(1-B)(1-B^12)` = `(1 - B - B^12 + B^13)` — an operator that differences across 13 lags. It is correct for series with both stochastic trend and stochastic seasonality, but it over-differences a series with only one of the two. Always verify stationarity at each differencing step before adding another.

**4. Ignoring seasonal residual autocorrelation**

Running Ljung-Box only on lags 1–10 misses seasonal structure. Always explicitly test at lags s and 2s.

**5. P=2 or Q=2 without justification**

These require significant spikes at lag 2s (e.g., lag 24 for monthly). If only lag 12 is significant, P=1 or Q=1 is sufficient. P=2 or Q=2 are rarely needed in practice.

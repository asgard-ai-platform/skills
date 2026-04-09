# Damped Trend

## What Problem It Solves

Standard Holt and Holt-Winters extrapolate the trend linearly forever: if the last estimated trend is +20 units/period, the 10-step forecast adds +200 units on top of the current level. For short horizons this is fine; for longer horizons, it produces systematically overconfident forecasts.

Empirical evidence (Gardner & McKenzie 1985; Hyndman et al. 2008) shows **damped trend almost always outperforms undamped trend for horizons beyond 4–6 periods**, and rarely loses even when the true trend is linear.

---

## The Damping Parameter φ

A single new parameter φ ∈ (0, 1] multiplies the trend component each period, causing it to decay toward zero as the horizon grows.

- φ = 1.0 → standard (undamped) Holt
- φ = 0.98 → mild damping, near-linear for ≤ 20 periods
- φ = 0.90 → moderate damping, trend halves in ~7 periods
- φ = 0.80 → strong damping, trend nearly gone by period 10
- φ < 0.80 → effectively flattens immediately; rarely useful

In practice, φ is usually optimized via MLE/MSE on training data and almost always falls in **[0.80, 0.98]**.

---

## Equations: Damped Holt (no seasonality)

**State update at time t:**

```
ℓₜ = α·yₜ + (1 − α)·(ℓₜ₋₁ + φ·bₜ₋₁)
bₜ = β·(ℓₜ − ℓₜ₋₁) + (1 − β)·φ·bₜ₋₁
```

**h-step forecast from time t:**

```
ŷₜ₊ₕ = ℓₜ + (φ + φ² + φ³ + … + φʰ)·bₜ
      = ℓₜ + bₜ · φ·(1 − φʰ)/(1 − φ)
```

As h → ∞, the bracketed sum converges to φ/(1−φ), so the long-run forecast asymptotes to a **fixed value** (ℓₜ + φ/(1−φ)·bₜ) rather than growing without bound.

---

## Equations: Damped Holt-Winters (additive seasonality)

Add the seasonal correction term back to the level update; damping only touches the trend:

```
ℓₜ = α·(yₜ − sₜ₋ₛ) + (1 − α)·(ℓₜ₋₁ + φ·bₜ₋₁)
bₜ = β·(ℓₜ − ℓₜ₋₁) + (1 − β)·φ·bₜ₋₁
sₜ = γ·(yₜ − ℓₜ)   + (1 − γ)·sₜ₋ₛ
```

**h-step forecast:**

```
ŷₜ₊ₕ = ℓₜ + bₜ·φ·(1 − φʰ)/(1 − φ) + sₜ₊ₕ₋ₛ
```

where `t+h-s` wraps modulo s (the seasonal period).

---

## Worked Example

**Data:** 24 months of monthly revenue. After fitting Holt-Winters, the optimizer returns:
- α = 0.25, β = 0.08, γ = 0.12
- φ = 0.93
- At t = 24: ℓ₂₄ = 1,000, b₂₄ = 30, seasonal index for month 12 = +80

**Forecast for h = 1 (month 25):**
```
φ·(1 − φ¹)/(1 − φ) = 0.93·(1 − 0.93)/(1 − 0.93)
                    = 0.93·0.07/0.07
                    = 0.93
ŷ₂₅ = 1000 + 30·0.93 + s₁₃₋₁₂ = 1000 + 27.9 + s₁ (season index for month 1)
```

**Forecast for h = 12 (month 36):**
```
φ·(1 − φ¹²)/(1 − φ) = 0.93·(1 − 0.93¹²)/0.07
0.93¹² ≈ 0.419
= 0.93·(1 − 0.419)/0.07 = 0.93·0.581/0.07 ≈ 7.72

ŷ₃₆ = 1000 + 30·7.72 + s₁₂
     = 1000 + 231.6 + 80
     = 1311.6
```

**Undamped (φ = 1) for h = 12 would give:**
```
ŷ₃₆ = 1000 + 30·12 + 80 = 1440
```

The damped forecast is 128 units (≈9%) more conservative. For a mature market this is almost certainly more realistic.

---

## Cumulative Damping Table

Shows how the effective trend multiplier `φ·(1−φʰ)/(1−φ)` grows vs. h for common φ values:

| h  | φ=0.98 | φ=0.95 | φ=0.90 | φ=0.85 | φ=0.80 |
|----|--------|--------|--------|--------|--------|
| 1  | 0.98   | 0.95   | 0.90   | 0.85   | 0.80   |
| 3  | 2.88   | 2.71   | 2.44   | 2.17   | 1.95   |
| 6  | 5.60   | 4.99   | 4.10   | 3.39   | 2.85   |
| 12 | 10.42  | 8.35   | 5.97   | 4.35   | 3.31   |
| 24 | 17.96  | 12.47  | 7.55   | 5.01   | 3.70   |
| ∞  | 49.0   | 19.0   | 9.0    | 5.67   | 4.0    |

With φ=0.90, the 24-step effective multiplier (7.55) is only 7.55/24 = 31% of the undamped linear extrapolation — the trend contribution gets capped well before it dominates.

---

## Choosing φ: Optimization vs. Grid Search

**Preferred:** include φ in the parameter optimization (MLE or SSE minimization) alongside α, β, γ. Most implementations (statsmodels `ExponentialSmoothing`, R `forecast::ets`) do this automatically when `damped=True`.

**Manual grid search:** if using a custom implementation, sweep φ ∈ {0.80, 0.85, 0.88, 0.90, 0.92, 0.95, 0.98} and pick the value minimizing out-of-sample MAE on a held-out validation window of at least one seasonal cycle.

**Do not** fix φ = 0.9 as a universal default without validation — the optimal value is data-dependent.

---

## Decision: Damped vs. Undamped

Use this table to decide at Phase 1:

| Condition | Recommendation |
|-----------|----------------|
| Forecast horizon ≤ 4 periods | Either; difference negligible |
| Forecast horizon 5–12 periods | Prefer damped; test both |
| Forecast horizon > 12 periods | Always damped |
| Trend is acceleration (second-order) | Neither — use ARIMA or ML |
| You observe trend reversal in history | Damped with low φ (≤ 0.88) |
| Business domain saturates (market share, capacity) | Damped; constrain long-run level |
| Residuals show positive autocorrelation at long lags | Possible underdamping — reduce φ |

---

## Relationship to ETS Model Codes

In ETS notation, damped models append a lowercase **d** to the trend type:

| ETS code | Meaning |
|----------|---------|
| ETS(A,N,N) | SES |
| ETS(A,A,N) | Holt (undamped) |
| ETS(A,Ad,N) | Holt damped |
| ETS(A,A,A) | Holt-Winters additive (undamped) |
| ETS(A,Ad,A) | Holt-Winters additive damped ← most common production choice |
| ETS(M,Ad,M) | Multiplicative error, damped trend, multiplicative seasonality |

When auto-selecting a model via AICc, the damped variants often win even for short series, because the penalty for adding φ is small relative to the bias reduction.

---

## Python Implementation Sketch

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

model = ExponentialSmoothing(
    y,
    trend="add",
    seasonal="add",
    seasonal_periods=12,
    damped_trend=True,          # enables φ
)
fit = model.fit(optimized=True) # optimizes α, β, γ, φ jointly

print(f"phi = {fit.params['damping_trend']:.4f}")
forecasts = fit.forecast(steps=12)
```

To inspect the damping effect explicitly:

```python
import numpy as np

phi = fit.params['damping_trend']
b   = fit.level[-1]  # last estimated trend
l   = fit.level[-1]  # statsmodels uses 'level' attribute; check your version

h_values = np.arange(1, 13)
damping_multipliers = phi * (1 - phi**h_values) / (1 - phi)
print(dict(zip(h_values, damping_multipliers.round(3))))
```

---

## Gotchas Specific to Damped Trend

**φ hitting the boundary (φ → 1.0):** If the optimizer returns φ ≥ 0.99, the model is telling you the data supports a near-linear trend — damping is not helping. Consider whether the training window is long enough or whether trend is genuinely linear in your domain.

**Conflating damping with low β:** A small β (trend smoothing weight) already dampens *reaction* to new trend signals, but it does not flatten long-run extrapolation the way φ does. These parameters address different problems; both can be non-zero simultaneously.

**Negative trends with damping:** φ works symmetrically. If bₜ < 0 (downward trend), damping pulls the forecast back toward the current level from below — which is the correct behavior (decline decelerates).

**Initialization of b₀ with damping:** The initialization formula for b₀ remains the same as undamped Holt (slope of first regression over early periods). The damping only activates during forecasting, not during in-sample fitting updates.

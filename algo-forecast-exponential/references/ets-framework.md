# ETS Framework: Error-Trend-Seasonality Model Selection

ETS re-frames exponential smoothing as a family of 30 state space models. Each model is identified by three components: **E** (error type), **T** (trend type), **S** (seasonality type). This taxonomy enables principled model selection via information criteria rather than manual guessing.

---

## Taxonomy

Each component takes values from a fixed alphabet:

| Component | Options | Notation |
|-----------|---------|---------|
| Error | Additive, Multiplicative | A, M |
| Trend | None, Additive, Additive Damped | N, A, Ad |
| Seasonality | None, Additive, Multiplicative | N, A, M |

Combined: `ETS(E, T, S)`. Shorthand examples:
- `ETS(A,N,N)` — Simple Exponential Smoothing (SES) with additive error
- `ETS(A,A,N)` — Holt's linear method
- `ETS(A,A,A)` — Holt-Winters additive
- `ETS(M,A,M)` — Holt-Winters multiplicative (common for proportional seasonality)
- `ETS(A,Ad,N)` — Damped trend, no seasonality

Not all 30 combinations are numerically stable. In practice, 15 are commonly used; the remaining combinations (e.g., `M,M,A`) can produce negative forecasts or explode.

---

## State Space Formulation

ETS writes each model as a **measurement equation** (observed) + **transition equations** (state update). Shown for `ETS(A,A,A)`:

**State vector:** `xₜ = [ℓₜ, bₜ, s_t, s_{t-1}, ..., s_{t-m+1}]`

**Measurement equation:**
```
yₜ = ℓₜ₋₁ + bₜ₋₁ + sₜ₋ₘ + εₜ        (εₜ ~ N(0, σ²))
```

**Transition equations:**
```
ℓₜ = ℓₜ₋₁ + bₜ₋₁ + α·εₜ
bₜ = bₜ₋₁ + β·εₜ                      (β here is β* = β/α in Holt notation)
sₜ = sₜ₋ₘ + γ·εₜ                      (γ here is γ* = γ/(1-α))
```

The smoothing parameters α, β*, γ* are the Kalman gain coefficients in this state space interpretation.

For `ETS(M,A,M)` (multiplicative error and seasonality):
```
yₜ = (ℓₜ₋₁ + bₜ₋₁) · sₜ₋ₘ · (1 + εₜ)
ℓₜ = (ℓₜ₋₁ + bₜ₋₁)(1 + α·εₜ)
bₜ = bₜ₋₁ + β·(ℓₜ₋₁ + bₜ₋₁)·εₜ
sₜ = sₜ₋ₘ · (1 + γ·εₜ)
```

The multiplicative error form generates **prediction intervals that widen proportionally** with the forecast level — appropriate when variance scales with level (heteroscedastic data).

---

## Model Selection: AIC and AICc

Fit all candidate models by maximum likelihood. Select using **AICc** (corrected AIC for small samples):

```
AIC  = -2·log(L) + 2k
AICc = AIC + 2k(k+1)/(n - k - 1)
```

Where:
- `L` = maximized likelihood
- `k` = number of free parameters (smoothing params + initial states)
- `n` = length of training series

**Rule:** Select the model with the lowest AICc. Do not use RMSE for model selection — it rewards overfitting.

### Parameter count by model

| Model | Free params (no seasonality) | With seasonality (period m) |
|-------|----------------------------|-----------------------------|
| ETS(·,N,N) | α + ℓ₀ = 2 | — |
| ETS(·,A,N) | α, β* + ℓ₀, b₀ = 4 | — |
| ETS(·,Ad,N) | α, β*, φ + ℓ₀, b₀ = 5 | — |
| ETS(·,A,A) | α, β*, γ* + ℓ₀, b₀ + m seasonal states = 3 + 2 + m | |
| ETS(·,A,M) | same count | same count |

For monthly data (m=12), a seasonal model has approximately 17 free parameters. With n < 4×17 = 68 observations, AICc penalty matters significantly.

### Worked example: model comparison

Series: 48 months of retail sales, upward trend, visible seasonality.

| Model | k | Log-L | AIC | AICc |
|-------|---|-------|-----|------|
| ETS(A,N,N) | 2 | -312 | 628 | 628.2 |
| ETS(A,A,N) | 4 | -298 | 604 | 604.7 |
| ETS(A,A,A) | 17 | -271 | 576 | **585.4** |
| ETS(M,A,M) | 17 | -268 | 570 | **579.4** ← selected |
| ETS(A,Ad,A)| 18 | -270 | 576 | 587.9 |

`ETS(M,A,M)` wins. Despite identical parameter count to `ETS(A,A,A)`, its multiplicative error fits the heteroscedastic variance better (log-likelihood is higher).

---

## Additive vs Multiplicative: Decision Rule

The single most consequential modeling choice. Use this checklist:

**Use additive error (`A`) when:**
- Residuals from a preliminary fit have roughly constant variance across time
- Data is near zero (multiplicative error → division by zero risk)

**Use multiplicative error (`M`) when:**
- Residual variance grows with the series level
- Taking log(yₜ) linearizes variance (log-normal structure)

**Use additive seasonality (`A`) when:**
- Seasonal fluctuation is roughly constant in absolute terms
- Monthly peak is ±500 units regardless of the level being 5,000 or 10,000

**Use multiplicative seasonality (`M`) when:**
- Seasonal fluctuation is a percentage of level
- Monthly peak is ±10% regardless of absolute level
- Standard diagnostic: plot seasonal decomposition; if seasonal component amplitude grows with trend, use multiplicative

**Quick visual check:** plot `yₜ` on original scale. If seasonal peaks widen as level rises, choose multiplicative seasonality.

---

## Damped Trend (Ad): When and How

Linear trend extrapolation becomes unrealistic beyond 1-2 seasonal cycles. The damped trend introduces `φ ∈ (0,1]` to flatten the trend:

**Transition equation with damping:**
```
ℓₜ = ℓₜ₋₁ + φ·bₜ₋₁ + α·εₜ
bₜ = φ·bₜ₋₁ + β·εₜ
```

**h-step forecast:**
```
ŷₜ₊ₕ = ℓₜ + (φ + φ² + ... + φʰ)·bₜ + seasonal term
       = ℓₜ + φ(1 - φʰ)/(1 - φ) · bₜ + seasonal term
```

As `h → ∞` with `φ < 1`, the cumulative trend converges to `φ/(1-φ)·bₜ` (a finite cap). With φ = 0.98, the trend still grows but asymptotically.

**Typical optimized range:** `φ ∈ [0.80, 0.98]`. Values below 0.80 damp too aggressively; above 0.98 is nearly indistinguishable from undamped.

**Use damped trend when:**
- Forecast horizon > one seasonal cycle
- Prior domain knowledge says growth will not continue linearly
- AICc selects `Ad` over `A` (this happens frequently for business data)

---

## Optimization: Fitting Smoothing Parameters

Parameters are fit by minimizing the **sum of squared one-step-ahead errors** (equivalent to MLE under Gaussian additive error):

```
SSE(α, β, γ, φ, x₀) = Σₜ εₜ²
```

where `εₜ = yₜ - ŷₜ|t₋₁` is the one-step forecast error.

**Constraints:**
```
0 < α < 1
0 < β* < α          (ensures β < α in Holt notation)
0 < γ* < 1 - α
0 < φ ≤ 1
```

These are the "admissibility" constraints that guarantee bounded forecasts. Tighter "stability" constraints exist for some models and are preferred in practice.

**Numerical optimization:**
1. Grid-initialize: try (α, β, γ) on a 5×5×5 grid, select lowest SSE as starting point
2. Run L-BFGS-B or Nelder-Mead from the best starting point
3. Enforce constraints via bounded optimization or penalty terms

**Important:** Initial state values (`ℓ₀`, `b₀`, seasonal indices) are co-optimized with the smoothing parameters. Treat them as free parameters in the optimization (not fixed by heuristics) for best likelihood.

---

## Prediction Intervals

The state space form enables **exact** (not bootstrap) prediction intervals for additive-error models:

For `ETS(A,·,·)`, the h-step variance is:
```
Var(ŷₜ₊ₕ - yₜ₊ₕ) = σ²·cₕ²
```

Where `cₕ` is a deterministic function of α, β, γ, φ, and h derived from the state space matrix. For `ETS(A,N,N)`:
```
cₕ = 1 + α²(h-1)
```

So the 95% interval is:
```
ŷₜ₊ₕ ± 1.96·σ·√cₕ
```

For multiplicative-error models (`M`), exact closed-form intervals are **not available**. Use simulation: draw 5,000 future sample paths from the fitted model, take empirical quantiles.

---

## Constraints on Seasonal Initialization

Seasonal indices must sum to zero (additive) or sum to m (multiplicative):

**Additive:** `Σⱼ₌₁ᵐ s_j = 0`

**Multiplicative:** `Σⱼ₌₁ᵐ s_j = m`

When optimizing initial states, enforce this as an equality constraint (or eliminate one seasonal parameter by substitution). Failing to enforce this introduces a confound between the level and the seasonal mean.

---

## Common Pitfalls Specific to ETS

**Selecting by RMSE instead of AICc**
RMSE always improves when adding parameters. A model with more states fits better in-sample but forecasts worse out-of-sample. AICc penalizes the extra parameters.

**Fitting ETS on log-transformed data, then choosing M-error**
If you log-transform yₜ before fitting, additive error on log scale is already multiplicative on the original scale. Fitting `ETS(M,·,·)` on log data double-applies multiplicativity. Either transform and use `ETS(A,·,·)`, or don't transform and use `ETS(M,·,·)`.

**Ignoring the stability region**
Admissibility constraints (`0 < α < 1`, etc.) are necessary but not sufficient for stable forecasts. Some (E,T,S) combinations with admissible parameters still produce explosive variance. The `forecast` R package and `statsmodels` Python package enforce stricter stability regions by default.

**Using ETS with multiple seasonalities**
`ETS(·,·,A)` and `ETS(·,·,M)` handle exactly one seasonal period m. Daily data with both weekly (m=7) and annual (m=365) patterns cannot be modeled by standard ETS. Use STL decomposition first (strip out both seasonal components), then fit ETS on the remainder.

---

## Quick Reference: Model Equivalences

| ETS notation | Classical name | Typical use case |
|---|---|---|
| ETS(A,N,N) | Simple Exponential Smoothing | No trend, no seasonality |
| ETS(A,A,N) | Holt's linear method | Linear trend, no seasonality |
| ETS(A,Ad,N) | Damped trend | Long-horizon with trend |
| ETS(A,A,A) | Holt-Winters additive | Trend + constant amplitude seasonality |
| ETS(M,A,M) | Holt-Winters multiplicative | Trend + proportional seasonality |
| ETS(M,Ad,M) | Damped HW multiplicative | Long-horizon, proportional seasonality |

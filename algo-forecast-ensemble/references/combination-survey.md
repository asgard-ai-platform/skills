# Forecast Combination Methods Survey

## The Forecast Combination Puzzle

The central empirical finding in this literature (Stock & Watson, 2004; Timmermann, 2006): **simple equal-weight averaging of diverse models is extremely hard to beat in practice**, even when theoretically optimal weights can be estimated.

Why? Weight estimation requires data. The estimation error in learned weights tends to offset the theoretical gain from optimal weighting, especially when:
- The validation window is short (< 2–3 years of monthly data)
- The data-generating process shifts over time (structural breaks)
- Individual models already have low, similar errors

This is not an argument against weighted combination — it's an argument for humility about when complexity pays.

---

## Method 1: Simple Equal-Weight Average

**Formula:**

```
ŷ_t = (1/M) × Σ_{m=1}^{M} ŷ_{m,t}
```

**Worked example** — three models predicting next-month sales:

| Model  | Forecast |
|--------|----------|
| ARIMA  | 1,180    |
| Prophet| 1,220    |
| ETS    | 1,200    |

```
ŷ_ensemble = (1180 + 1220 + 1200) / 3 = 1200.0
```

**When to use:** Always start here. If you cannot demonstrate that a more complex method beats this on held-out data, stay with it.

**Variance reduction:** If model errors are uncorrelated with equal variance σ², ensemble variance = σ²/M. In practice, errors are correlated, so the reduction is smaller.

---

## Method 2: Inverse-Error Weighting

Weight each model inversely proportional to its historical error on a validation set.

**Formula:**

```
w_m = (1 / e_m) / Σ_{j=1}^{M} (1 / e_j)

ŷ_ensemble = Σ_{m=1}^{M} w_m × ŷ_{m,t}
```

Where `e_m` is a loss metric — typically MSE or MAE — computed on a held-out validation window.

**Worked example:**

Suppose you have 24 months of validation data. Compute RMSE on that window:

| Model   | Validation RMSE | 1/RMSE    |
|---------|-----------------|-----------|
| ARIMA   | 40              | 0.0250    |
| Prophet | 60              | 0.0167    |
| ETS     | 50              | 0.0200    |
| **Sum** |                 | **0.0617**|

```
w_ARIMA   = 0.0250 / 0.0617 ≈ 0.405
w_Prophet = 0.0167 / 0.0617 ≈ 0.271
w_ETS     = 0.0200 / 0.0617 ≈ 0.324

ŷ_ensemble = 0.405×1180 + 0.271×1220 + 0.324×1200
           = 478.0 + 330.6 + 388.8
           = 1197.4
```

Notice: shifted toward ARIMA (lowest RMSE), away from Prophet (highest RMSE), but not dramatically.

**Validation window length matters:**

| Validation Window | Recommendation |
|-------------------|----------------|
| < 12 observations | Don't use inverse-error weighting; use simple average |
| 12–36 observations| Use, but expect noisy weights; consider Bates-Granger shrinkage |
| > 36 observations | Inverse-error weighting is reasonably stable |

**Instability check:** If any single model's weight exceeds 60%, the validation window may be too short or one model is genuinely dominant. In the latter case, just use that model.

---

## Method 3: Bates-Granger Optimal Weights

The Bates & Granger (1969) paper derived the theoretically optimal weight under the assumption of known, stationary error variances and covariance.

**Formula (two-model case):**

```
w₁* = (σ₂² - σ₁₂) / (σ₁² + σ₂² - 2σ₁₂)
w₂* = 1 - w₁*
```

Where:
- σ₁², σ₂² = error variances of models 1 and 2
- σ₁₂ = covariance between model errors

**General M-model case (matrix form):**

```
w* = Σ⁻¹ι / (ι'Σ⁻¹ι)
```

Where Σ is the M×M error covariance matrix and ι is a vector of ones.

**Worked example (two models):**

```
σ₁² = 1600  (ARIMA, σ=40)
σ₂² = 3600  (Prophet, σ=60)
σ₁₂ = 1200  (correlation ρ = 1200/(40×60) = 0.5)

w₁* = (3600 - 1200) / (1600 + 3600 - 2×1200) = 2400 / 2800 ≈ 0.857
w₂* = 1 - 0.857 = 0.143
```

**Problem with Bates-Granger in practice:** Estimating the full covariance matrix Σ requires a long, stable validation period. With M=5 models and a 24-month window, you have 24 observations to estimate 15 unique covariance terms. The sample covariance matrix will be near-singular and the resulting weights will be extreme and unstable.

**Practical rule:** Use Bates-Granger only when you can invert a well-conditioned Σ. As a heuristic, require `n_validation / M ≥ 10`. Below this ratio, regularize toward equal weights (see Shrinkage below).

---

## Method 4: Shrinkage Toward Equal Weights

Shrink estimated weights toward 1/M to reduce estimation noise.

**Formula:**

```
w_m(λ) = λ × w_m* + (1 - λ) × (1/M)
```

Where λ ∈ [0, 1] is the shrinkage intensity and w_m* is any estimated weight (inverse-error or Bates-Granger).

**Choosing λ:**

| Situation | Recommended λ |
|-----------|---------------|
| Short validation window (< 24 obs) | 0.0 – 0.3 (mostly equal weights) |
| Medium window (24–60 obs) | 0.3 – 0.7 |
| Long stable window (> 60 obs) | 0.7 – 1.0 |
| Suspected structural break | 0.0 – 0.2 |

**Worked example** (continuing inverse-error example, λ=0.4, M=3):

```
w_ARIMA(shrunk)   = 0.4 × 0.405 + 0.6 × 0.333 = 0.162 + 0.200 = 0.362
w_Prophet(shrunk) = 0.4 × 0.271 + 0.6 × 0.333 = 0.108 + 0.200 = 0.308
w_ETS(shrunk)     = 0.4 × 0.324 + 0.6 × 0.333 = 0.130 + 0.200 = 0.330

ŷ_ensemble = 0.362×1180 + 0.308×1220 + 0.330×1200
           = 427.2 + 375.8 + 396.0
           = 1199.0
```

Shrinkage pulled the weights noticeably closer to equal (0.333 each), reducing the influence of noisy validation RMSE estimates.

---

## Method 5: Stacking (Meta-Learner)

Train a regression model whose inputs are the individual model forecasts and whose output is the actual value. The regression coefficients become the combination weights.

**Setup:**

1. Generate out-of-sample forecasts from each base model using time-series cross-validation (expanding window or rolling window — no lookahead).
2. Assemble training matrix `X ∈ ℝ^{n × M}` where column m is model m's forecasts.
3. Fit a meta-learner on `(X, y_actual)`.

**Typical meta-learners:**

| Meta-Learner | Weights | Notes |
|--------------|---------|-------|
| OLS regression | Can be negative | Risky; negative weights extrapolate aggressively |
| Constrained OLS (w ≥ 0, Σw=1) | Non-negative, sum to 1 | Safer; usually preferred |
| Lasso / Ridge | Regularized | Ridge ≈ shrinkage toward equal weights |
| Gradient boosting | Non-linear | Only use with large validation sets |

**Constrained OLS (recommended):**

```python
from scipy.optimize import minimize
import numpy as np

def constrained_weights(X, y):
    """
    X: (n_obs, n_models) matrix of model forecasts
    y: (n_obs,) actual values
    Returns: weights w s.t. w >= 0, sum(w) = 1
    """
    M = X.shape[1]
    
    def objective(w):
        residuals = y - X @ w
        return np.sum(residuals**2)
    
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    bounds = [(0, 1)] * M
    w0 = np.ones(M) / M  # start from equal weights
    
    result = minimize(objective, w0, method='SLSQP',
                      bounds=bounds, constraints=constraints)
    return result.x
```

**When stacking is NOT worth it:**
- Fewer than ~50 validation observations per base model
- Base models are highly correlated (stacking won't find orthogonal signal)
- Forecast horizon is long and covariate shift is expected

---

## Decision Framework: Which Method to Use

Work through these gates in order:

```
1. Do any models clearly dominate? (RMSE < 80% of next-best on held-out data)
   → YES: Use that model alone. No ensemble needed.
   → NO: Continue.

2. How many validation observations do you have?
   → < 24: Use SIMPLE AVERAGE. Stop here.
   → 24–60: Use INVERSE-ERROR WEIGHTING with shrinkage (λ ≈ 0.3–0.5).
   → > 60: Either method is viable; try both and compare.

3. Do you have evidence of structural breaks in the validation window?
   → YES: Use simple average or heavy shrinkage (λ ≤ 0.2).
   → NO: Proceed with chosen method.

4. Are model errors correlated?
   → Compute pairwise correlation of validation residuals.
   → If all pairs have ρ > 0.7: ensemble gain is limited (<10% RMSE reduction).
     Flag this to user. Consider diversifying model types before ensembling.

5. Do you need uncertainty quantification (prediction intervals)?
   → If YES, simple average or inverse-error weighting is much simpler.
   → Stacking CI requires bootstrapping the full meta-learner.
```

---

## Combining Prediction Intervals

Combining point forecasts is mechanical. Combining prediction intervals is harder.

**Naive approach (averaging bounds):**

```
lower_ensemble = (1/M) × Σ lower_m
upper_ensemble = (1/M) × Σ upper_m
```

This is consistent with simple average of point forecasts, but **underestimates uncertainty** when model errors are correlated (which they usually are).

**Correct formula for simple-average ensemble variance** (when model errors are known):

```
Var(ŷ_ensemble) = (1/M²) × [Σ_m σ_m² + 2 × Σ_{m<j} σ_{mj}]
```

Where σ_{mj} is error covariance between models m and j.

**Practical approximation:**

If you don't know the error covariance, use the empirical spread of model forecasts as a signal of uncertainty:

```
spread = max(ŷ_m) - min(ŷ_m)
```

When spread is wide relative to the ensemble value (> 10%), widen the prediction interval by a factor before reporting. This is heuristic but prevents false confidence.

**Example:**

```
ARIMA: forecast=1180, 95% CI [1050, 1310]  → half-width = 130
Prophet: forecast=1220, 95% CI [1000, 1440] → half-width = 220
ETS: forecast=1200, 95% CI [1080, 1320]    → half-width = 120

Simple average of bounds:
  lower = (1050 + 1000 + 1080) / 3 = 1043
  upper = (1310 + 1440 + 1320) / 3 = 1357

Model spread = 1220 - 1180 = 40 (about 3.3% of 1200) → modest.
No additional widening needed.
```

If model spread had been > 120 (10% of ensemble), flag the high disagreement and report the wider interval.

---

## Empirical Rules of Thumb

These come from the meta-analysis literature (Genre et al., 2013; Genre & Kamber, 2022):

1. **More models ≠ better.** Going from 3 to 10 models typically yields < 5% additional RMSE reduction. Diminishing returns are steep.

2. **Diversity matters more than count.** 3 fundamentally different models (ARIMA + ML + structural) beats 8 ARIMA variants.

3. **Trimmed mean beats simple mean** when M ≥ 7 and some models are clearly weak. Drop the top and bottom 10–20% of forecasts by error and average the rest.

4. **Stacking rarely beats inverse-error weighting by more than 5–10%** on typical business time series (< 5 years of monthly data). The gains are largest when base models have very different biases.

5. **Equal weights outperform individual models 70–80% of the time** across studies. This is the baseline to beat.

---

## Failure Modes

**Weight instability over time:** Compute weights monthly. If any weight swings > 30 percentage points between consecutive months, treat it as a red flag — your validation window is too short or the data-generating process is non-stationary.

**All-positive weights hiding a dominated model:** If a model consistently receives weight < 5%, remove it. The small weight probably isn't helping and adds noise.

**Negative stacking weights:** OLS without constraints can assign negative weights (implicit short-selling of a model). This almost never has a meaningful interpretation for forecasting and is a sign of overfitting. Always use constrained OLS.

**Correlation creep:** Recalculate model error correlations periodically. Two models that were uncorrelated at training time can become highly correlated if they both adopt similar signals (e.g., both ARIMA and Prophet responding similarly to a new seasonal pattern). When ρ > 0.8, treat them as near-duplicates.

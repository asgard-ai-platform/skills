# Stacking Meta-Learner for Forecast Combination

Stacking (also called "forecast combination via regression") learns optimal model weights from data instead of imposing them manually. The meta-learner is a second-stage model trained on base model predictions as inputs and realized values as targets.

**When stacking is worth the complexity:** only when you have at least 2–3 years of monthly data (≥ 24 validation observations after holdout), models with meaningfully different error patterns, and stable underlying dynamics. Below this threshold, simple average almost always wins because weight estimation variance dominates.

---

## The Core Problem: Data Leakage

The most common stacking mistake is training the meta-learner on in-sample base model predictions. Every base model (ARIMA, ETS, Prophet) was fit to the training set — its in-sample predictions are artificially accurate. Meta-learner trained on these predictions learns garbage weights.

**Fix: generate meta-features via time-series cross-validation (walk-forward).**

---

## Step-by-Step: Walk-Forward Meta-Feature Generation

Given a dataset of `T` periods, reserve the final `H` periods as a true holdout (never touched until final evaluation).

On the remaining `T - H` periods, use an expanding-window walk-forward scheme:

```
Iteration 1: train on t=1..K,       predict t=K+1..K+h
Iteration 2: train on t=1..K+h,     predict t=K+h+1..K+2h
...
Iteration N: train on t=1..T-H-h,   predict t=T-H-h+1..T-H
```

Where:
- `K` = minimum training window (typically 24–36 months for monthly data)
- `h` = step size per iteration (typically 1 or 3 months)
- Each iteration re-fits **all** base models and generates out-of-sample forecasts

After all iterations, you have a matrix `Z` of shape `(T - H - K) × M` where M is number of base models, and a vector `y` of realized values over the same periods.

**This is your meta-training set.**

---

## Meta-Learner: Constrained Linear Regression

The simplest effective meta-learner is ordinary least squares:

```
ŷ_ensemble = w₀ + w₁·ŷ_arima + w₂·ŷ_prophet + w₃·ŷ_ets
```

But unconstrained OLS often produces negative weights or weights summing far from 1, which are economically nonsensical and unstable out-of-sample.

**Recommended constraints:**

| Constraint | Formula | When to use |
|------------|---------|-------------|
| Weights sum to 1, no intercept | Σwₘ = 1, w₀ = 0 | Default; interpretable as convex combination |
| Non-negative weights, sum to 1 | wₘ ≥ 0, Σwₘ = 1 | Strongly preferred; prevents extrapolation |
| Ridge-penalized, sum to 1 | min ‖y - Zw‖² + λ‖w‖² | High collinearity between base models |

The non-negative constrained version (NNLS) is implemented in scipy and is the default recommendation.

---

## Worked Example

### Setup

Monthly sales data, 60 periods total. Reserve periods 49–60 as holdout (H=12). Walk-forward with K=24, h=1 generates meta-features for periods 25–48 (24 observations).

Base models: ARIMA, Prophet, ETS.

### Meta-feature matrix Z (periods 25–48, abbreviated)

| Period | ARIMA | Prophet | ETS | Actual |
|--------|-------|---------|-----|--------|
| 25 | 1050 | 1080 | 1065 | 1072 |
| 26 | 1100 | 1130 | 1110 | 1118 |
| 27 | 980  | 1010 | 990 | 995  |
| ... | ... | ... | ... | ... |
| 48 | 1200 | 1240 | 1210 | 1225 |

### NNLS solution

Fit constrained regression on 24 observations → learns:

```
w_arima   = 0.22
w_prophet = 0.45
w_ets     = 0.33
```

Interpret: Prophet receives highest weight because its out-of-sample errors were smallest over the cross-validation window.

### Forecast for period 49 (holdout)

Base forecasts: ARIMA=1180, Prophet=1220, ETS=1200

```
ŷ_stacking = 0.22×1180 + 0.45×1220 + 0.33×1200
           = 259.6 + 549.0 + 396.0
           = 1204.6
```

Simple average for comparison: (1180+1220+1200)/3 = 1200.0

In this case: difference is small (< 0.4%). This is typical — stacking rarely produces large gains over simple average when models are similarly skilled.

---

## Python Implementation

```python
import numpy as np
from scipy.optimize import nnls

def generate_meta_features(data, base_models, min_train=24, step=1):
    """
    Walk-forward cross-validation to generate meta-features.
    
    data: array of shape (T,) — realized values
    base_models: list of callables, each fit(train) -> predict(n_steps) 
    Returns: Z (meta-feature matrix), y (realized values)
    """
    T = len(data)
    meta_rows = []
    actuals = []

    t = min_train
    while t < T:
        train = data[:t]
        actual = data[t]
        row = []
        for model in base_models:
            fitted = model.fit(train)
            pred = fitted.predict(1)[0]  # one-step-ahead
            row.append(pred)
        meta_rows.append(row)
        actuals.append(actual)
        t += step

    return np.array(meta_rows), np.array(actuals)


def fit_stacking_weights(Z, y):
    """
    Fit non-negative constrained weights summing to 1.
    Uses NNLS on the constraint-transformed system.
    
    Returns: weight array of shape (M,)
    """
    M = Z.shape[1]
    
    # Enforce sum-to-1: substitute wM = 1 - sum(w1..wM-1)
    # Equivalent: solve NNLS on (Z - z_last_col) for first M-1 cols
    Z_ref = Z[:, -1:] 
    Z_reduced = Z[:, :-1] - Z_ref  # shape (N, M-1)
    y_adjusted = y - Z[:, -1]      # absorb last column
    
    w_partial, _ = nnls(Z_reduced, y_adjusted)
    w_last = max(0.0, 1.0 - w_partial.sum())
    weights = np.append(w_partial, w_last)
    
    # Renormalize (NNLS may give sum slightly != 1 due to clipping)
    weights = np.clip(weights, 0, None)
    weights /= weights.sum()
    
    return weights


def ensemble_forecast(base_forecasts: dict, weights: dict) -> float:
    """
    Apply learned weights to new base forecasts.
    
    base_forecasts: {"arima": 1180, "prophet": 1220, "ets": 1200}
    weights: {"arima": 0.22, "prophet": 0.45, "ets": 0.33}
    """
    return sum(weights[m] * base_forecasts[m] for m in weights)
```

---

## Choosing the Meta-Learner

| Meta-learner | Pros | Cons | Use when |
|---|---|---|---|
| NNLS (constrained OLS) | Stable, interpretable, no tuning | Assumes linear combination | Default choice |
| Ridge regression | Handles collinearity | Needs λ tuning, may produce negatives | Base models are highly correlated |
| Lasso | Automatic model selection | Unstable at boundary | You want sparse weights |
| Gradient boosting | Captures nonlinear interactions | High variance, needs many obs | 5+ base models, 100+ meta-obs |
| Simple average | No training required | Ignores model quality differences | < 24 meta-observations |

**Practical threshold:** use NNLS only if meta-training set has ≥ 24 observations per weight estimated. For 3 base models (3 weights), need ≥ 24 meta-obs. For 6 models (6 weights), need ≥ 48 meta-obs.

---

## Weight Stability Check

Before deploying stacking weights, verify they are stable across sub-periods:

1. Split meta-training data into two halves (early / recent)
2. Fit NNLS separately on each half
3. Compare weights: if any weight changes by > 0.15, weights are unstable

```
Early half:   w_arima=0.20, w_prophet=0.48, w_ets=0.32
Recent half:  w_arima=0.25, w_prophet=0.41, w_ets=0.34
Max change:   0.07  → STABLE, proceed with stacking

Early half:   w_arima=0.05, w_prophet=0.72, w_ets=0.23
Recent half:  w_arima=0.38, w_prophet=0.30, w_ets=0.32
Max change:   0.42  → UNSTABLE, revert to simple average
```

---

## Retraining Cadence

Stacking weights encode which models were best over a past window. This changes over time.

| Series type | Recommended refit frequency |
|-------------|---------------------------|
| Stable, low seasonality | Every 6 months |
| Seasonal / promotional | Every 3 months or after major structural break |
| High volatility | Monthly, with exponential decay on older observations |

Use exponential-weighted NNLS for high-volatility series: give recent meta-observations weight `exp(-λ·age)` where λ ≈ 0.1 for monthly decay.

---

## When to Abandon Stacking and Fall Back

Return to simple average if any of these hold:

- Meta-training set < 24 observations
- Weight stability check fails (change > 0.15)
- Stacking ensemble RMSE on holdout ≥ simple average RMSE
- Base model errors have correlation > 0.8 (diversity too low to exploit)
- Series has undergone a structural break after the meta-training window

The IRON LAW from the parent skill applies here: **always benchmark stacking against simple average on the same holdout set before deploying.** If stacking wins by < 2% RMSE, the gain is unlikely to survive regime change — use simple average.

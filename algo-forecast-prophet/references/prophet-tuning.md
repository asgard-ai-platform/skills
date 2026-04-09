# Prophet Hyperparameter Tuning Guide

## The Three Regularization Priors

Prophet's most impactful hyperparameters are prior scale values that control how strongly each component is regularized toward zero. All three follow the same logic: **larger = more flexible, smaller = smoother/more conservative**.

| Parameter | Default | Controls |
|---|---|---|
| `changepoint_prior_scale` | 0.05 | Trend flexibility |
| `seasonality_prior_scale` | 10.0 | Seasonality amplitude |
| `holidays_prior_scale` | 10.0 | Holiday effect size |

The defaults are asymmetric by design: trend is tight (0.05), seasonality and holidays are loose (10.0). This reflects Prophet's assumption that business metrics usually have stable trends but variable seasonal patterns.

---

## `changepoint_prior_scale` — The Most Important Knob

### What It Does

Prophet places `n_changepoints` (default: 25) candidate changepoint locations in the first 80% of the training data (controlled by `changepoint_range`). At each candidate location, an allowed trend slope change `δ_j` is drawn from a Laplace prior:

```
δ_j ~ Laplace(0, τ)
```

where `τ = changepoint_prior_scale`. A larger `τ` allows larger `δ_j` values, giving the trend more freedom to bend.

### Effect on Forecast Shape

```
changepoint_prior_scale = 0.001  →  Nearly linear trend. Ignores local slope changes.
                          0.05   →  Default. Moderate flexibility.
                          0.5    →  Aggressively tracks local trends.
                          5.0    →  Overfits recent trend; dangerous for long horizons.
```

### Decision Framework

Ask these questions in order:

**Q1: Does the trend in training data look wiggly or smooth?**
- Smooth (gradual drift): start at 0.01–0.05
- Multiple clear breaks: start at 0.1–0.5

**Q2: How far are you forecasting vs. training length?**
- Forecast horizon > 20% of training length → prefer smaller values (trend extrapolation is risky)
- Short horizon (< 10% of training) → can afford slightly larger values

**Q3: Do residuals from `cross_validation()` show systematic bias at trend transitions?**
- Yes, model misses trend changes → increase
- No, model tracks noise in training but RMSE degrades on holdout → decrease

### Worked Example

Training data: 2 years of daily e-commerce GMV with a clear inflection point after a product launch at day 400.

```python
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics

scales = [0.01, 0.05, 0.1, 0.3, 0.5]
results = {}

for scale in scales:
    m = Prophet(changepoint_prior_scale=scale)
    m.fit(df)
    df_cv = cross_validation(m, initial='365 days', period='30 days', horizon='60 days')
    df_p = performance_metrics(df_cv)
    results[scale] = df_p['mape'].mean()

# Typical output pattern:
# 0.01  → MAPE 0.18  (too stiff, misses the launch inflection)
# 0.05  → MAPE 0.11
# 0.10  → MAPE 0.09  ← often the sweet spot with a real inflection
# 0.30  → MAPE 0.10  (starts overfitting recent noise)
# 0.50  → MAPE 0.14  (clearly overfits)
```

The optimal value is not always the smallest. If your data has genuine structural breaks, the default 0.05 will under-fit.

---

## `seasonality_prior_scale` — When to Touch It

The seasonality components use Fourier series with coefficients `β` regularized by:

```
β ~ Normal(0, σ²)
```

where `σ = seasonality_prior_scale`. The default of 10.0 is already quite loose. You rarely need to increase it. You should **decrease** it when:

- Seasonal amplitudes look implausibly large in the components plot
- MAPE improves on holdout when you reduce it
- You have sparse training data (< 1 full seasonal cycle)

**Typical adjustment range:** 1.0 – 10.0. Going below 0.1 will suppress seasonality almost entirely.

```python
# Example: dampening over-fitted weekly seasonality on sparse data
m = Prophet(seasonality_prior_scale=1.0)
m.fit(df)
```

---

## `holidays_prior_scale` — Controlling Event Effects

Same Normal prior as seasonality. Default 10.0. Decrease when:

- Holiday effects in-sample look too large (e.g., +300% on a day with only 2 observed instances of that holiday)
- You have < 3 instances of a holiday in training data

**Rule of thumb:** If a holiday appears fewer than 3 times in training, set `holidays_prior_scale` ≤ 1.0 to prevent the model from committing too hard to one observation.

```python
m = Prophet(holidays_prior_scale=0.5)
```

---

## `changepoint_range` and `n_changepoints`

### `changepoint_range` (default: 0.8)

Candidate changepoints are only placed in the first 80% of training data. The final 20% is intentionally left changepoint-free to prevent overfitting near the end of training (which would produce unstable extrapolation).

**When to lower it (e.g., 0.6):**
- You have clear evidence the most recent trend is stable and should extrapolate
- Long forecast horizons relative to training (reduces tail instability)

**When to raise it (e.g., 0.9):**
- Genuine structural change very recently in training
- You can verify via held-out data that the change is real

```python
m = Prophet(changepoint_range=0.7)  # more conservative tail
```

### `n_changepoints` (default: 25)

The number of candidate changepoint locations. Usually 25 is sufficient. Only increase if:
- Training data is very long (5+ years daily) and you expect many regime changes
- After increasing `changepoint_prior_scale`, you still see missed inflections

**Do not** treat `n_changepoints` as a first-resort tuning parameter. `changepoint_prior_scale` is almost always the right lever; `n_changepoints` is rarely the bottleneck.

---

## Seasonality Mode: Additive vs. Multiplicative

Not a prior scale, but frequently mistuned. The parent SKILL.md mentions this in the edge case table.

**Additive** (default): seasonal amplitude is constant in absolute terms.
```
y(t) = g(t) + s(t) + h(t) + ε
```
Use when: seasonal swings are roughly the same size regardless of trend level.

**Multiplicative**: seasonal amplitude scales with trend.
```
y(t) = g(t) · (1 + s(t) + h(t)) + ε
```
Use when: a metric that doubles in trend also doubles its seasonal swing.

**Diagnostic:** plot `y` vs. time and look at seasonal deviations. If the absolute size of peaks/troughs grows with the overall level, use multiplicative.

```python
m = Prophet(seasonality_mode='multiplicative')
```

You can also mix modes per-seasonality component:

```python
m = Prophet(seasonality_mode='additive')  # global default
m.add_seasonality(name='yearly', period=365.25, fourier_order=10, mode='multiplicative')
```

---

## `fourier_order` — Seasonality Smoothness

Each seasonality component uses a Fourier series of order `N`, contributing `2N` parameters. Defaults:

| Seasonality | Default `fourier_order` |
|---|---|
| Yearly | 10 |
| Weekly | 3 |
| Daily | 4 |

Higher `fourier_order` = more wiggly seasonal pattern. Increase when the default pattern looks too smooth to match the data. Decrease when you're overfitting a noisy seasonal pattern.

**Concrete example:** Weekly seasonality for a media site where traffic varies significantly by day-of-week but the default fourier_order=3 produces a smooth curve instead of the actual sharp Monday spike:

```python
m = Prophet(weekly_seasonality=False)  # disable default
m.add_seasonality(name='weekly', period=7, fourier_order=6)  # sharper
m.fit(df)
```

---

## Grid Search Protocol

Manual tuning works for 1–2 parameters. When tuning 3+, use a small grid:

```python
from itertools import product
from prophet.diagnostics import cross_validation, performance_metrics

param_grid = {
    'changepoint_prior_scale': [0.01, 0.05, 0.1, 0.3],
    'seasonality_prior_scale': [1.0, 5.0, 10.0],
    'seasonality_mode': ['additive', 'multiplicative'],
}

keys = list(param_grid.keys())
combos = list(product(*param_grid.values()))

best_mape = float('inf')
best_params = {}

for combo in combos:
    params = dict(zip(keys, combo))
    m = Prophet(**params)
    m.fit(df)
    df_cv = cross_validation(
        m,
        initial='365 days',   # minimum training window
        period='30 days',     # how often to cut a new window
        horizon='60 days',    # forecast horizon you care about
        parallel='processes'
    )
    df_p = performance_metrics(df_cv)
    mape = df_p['mape'].mean()
    if mape < best_mape:
        best_mape = mape
        best_params = params

print(best_params, best_mape)
```

**Critical:** The `initial`, `period`, and `horizon` arguments to `cross_validation()` must match your actual use case. Optimizing for 7-day MAPE when you actually need 90-day forecasts will select wrong hyperparameters.

### Choosing `initial`, `period`, `horizon`

| Parameter | Rule |
|---|---|
| `initial` | At least 2× the longest seasonality period (e.g., 730 days for yearly seasonality) |
| `horizon` | Exactly the forecast horizon you will deploy |
| `period` | ≤ 0.5 × horizon. Smaller = more CV folds = slower but more reliable |

---

## Parameter Interaction Warning

`changepoint_prior_scale` and `seasonality_prior_scale` are not independent. A very flexible trend can absorb seasonal variation and vice versa. When you set `changepoint_prior_scale` very high, the trend may absorb what should be modeled as seasonality, making the seasonality component appear weaker. Always inspect the component plots after tuning:

```python
fig = m.plot_components(forecast)
```

If `trend` looks wiggly at the yearly frequency, your changepoint flexibility is too high and it is stealing from `yearly`.

---

## Quick Reference: Symptom → Adjustment

| Symptom | Likely cause | Adjustment |
|---|---|---|
| Forecast drifts flat far into future | `changepoint_prior_scale` too low | Increase to 0.1–0.3 |
| Forecast too wiggly, chases noise | `changepoint_prior_scale` too high | Decrease to 0.01–0.05 |
| Holiday effects implausibly large | `holidays_prior_scale` too high, few instances | Decrease to 0.5–2.0 |
| Seasonal pattern too smooth | `fourier_order` too low | Increase by 2–4 |
| Seasonal amplitude grows with trend but model misses it | `seasonality_mode='additive'` | Switch to `'multiplicative'` |
| MAPE good in-sample but bad on holdout, especially near end of training | `changepoint_range` too high | Decrease to 0.7–0.75 |
| Model misses a real structural break at end of training | `changepoint_range` too low | Increase to 0.85–0.9 |

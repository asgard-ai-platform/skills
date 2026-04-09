# Prophet Cross-Validation

Prophet ships a rolling-origin (time-series walk-forward) cross-validator in `prophet.diagnostics`. It is NOT k-fold — it respects temporal order by training on past data, predicting a future horizon, and repeating at multiple cutoff points.

## How It Works

```
Training window ──────────────────────┤ cutoff ├── horizon ──┤
                                       ^ predict from here

Next cutoff (shifted by `period`):
Training window ────────────────────────────┤ cutoff ├── horizon ──┤
```

Three parameters control the walk-forward sweep:

| Parameter | Meaning | Typical starting value |
|-----------|---------|----------------------|
| `initial` | Minimum training window length | 3× the longest seasonality period |
| `period` | Gap between consecutive cutoffs | 0.5 × horizon |
| `horizon` | How far into the future to predict at each cutoff | Business-defined forecast need |

All three accept pandas `timedelta` strings, e.g. `'365 days'`, `'30 days'`.

## Minimum Training Window Rule

```
initial ≥ max(
    2 × longest_seasonality_period,   # need at least 2 full cycles to fit
    horizon × 3                        # avoid horizon > 1/3 of training data
)
```

For daily data with yearly seasonality and a 90-day forecast horizon:
- Longest seasonality = 365 days → `2 × 365 = 730 days`
- Horizon guard = `90 × 3 = 270 days`
- → `initial = '730 days'`

## Step-by-Step Procedure

```python
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
import pandas as pd

# 1. Fit the model normally
m = Prophet(
    changepoint_prior_scale=0.05,
    seasonality_mode='additive'
)
m.add_country_holidays(country_name='US')
m.fit(df)  # df has columns: ds, y

# 2. Run cross-validation
df_cv = cross_validation(
    m,
    initial='730 days',
    period='90 days',
    horizon='90 days',
    parallel='processes'   # speeds up on multi-core machines
)
# df_cv columns: ds, yhat, yhat_lower, yhat_upper, y, cutoff

# 3. Compute metrics at each prediction horizon
df_perf = performance_metrics(df_cv, rolling_window=0.1)
# rolling_window: fraction of horizon used to smooth metrics
# df_perf columns: horizon, mse, rmse, mae, mape, mdape, coverage
```

## Metrics Reference

| Metric | Formula | When to prefer |
|--------|---------|---------------|
| MAPE | `mean(|y - ŷ| / |y|)` | Comparable across series; breaks when `y ≈ 0` |
| MDAPE | `median(|y - ŷ| / |y|)` | Robust to outlier periods |
| RMSE | `sqrt(mean((y - ŷ)²))` | Penalizes large errors more |
| MAE | `mean(|y - ŷ|)` | Interpretable in original units |
| Coverage | `mean(yhat_lower ≤ y ≤ yhat_upper)` | Should be ~0.80 for 80% intervals |

**Worked numbers** (daily website traffic, 2 years of data, 90-day horizon):

```
horizon    mape    rmse    coverage
7 days     0.06    312     0.81
30 days    0.09    489     0.79
60 days    0.13    701     0.77
90 days    0.17    891     0.74
```

Interpretation: MAPE drifts from 6% at 1 week to 17% at 3 months. Coverage at 90 days is 74% instead of the target 80% — signals that uncertainty intervals are slightly too narrow (common if residuals are autocorrelated; see IRON LAW in SKILL.md).

## Choosing `period`

`period` controls how many evaluation cutoffs you get:

```
number_of_cutoffs ≈ (total_data_length - initial - horizon) / period
```

Example: 3 years (1095 days) of data, `initial='730 days'`, `horizon='90 days'`:
- With `period='45 days'`: (1095 - 730 - 90) / 45 ≈ **6 cutoffs**
- With `period='30 days'`: (1095 - 730 - 90) / 30 ≈ **9 cutoffs**
- With `period='15 days'`: (1095 - 730 - 90) / 15 ≈ **18 cutoffs**

Fewer than 5 cutoffs makes the MAPE estimate unreliable. Aim for 8–15 cutoffs for stable metrics.

## `rolling_window` in `performance_metrics`

`performance_metrics(df_cv, rolling_window=w)` computes a rolling average of metrics over `w × horizon` days. This smooths the noisy per-day metric curve.

| `rolling_window` | Effect |
|------------------|--------|
| 0.1 (default) | Lightly smoothed; shows variation across horizon |
| 1.0 | Single aggregate number for the entire horizon |
| 0.0 | Raw per-day values; very noisy |

Use `rolling_window=1.0` only for model selection (you need one number to compare). Use smaller values for diagnosing whether short-horizon accuracy differs from long-horizon.

## Using CV to Tune `changepoint_prior_scale`

The most impactful hyperparameter to tune via CV is `changepoint_prior_scale`. Run a grid search:

```python
import itertools

param_grid = {
    'changepoint_prior_scale': [0.001, 0.01, 0.05, 0.1, 0.5],
    'seasonality_prior_scale': [0.01, 0.1, 1.0, 10.0],
}

results = []
for cps, sps in itertools.product(
    param_grid['changepoint_prior_scale'],
    param_grid['seasonality_prior_scale']
):
    m = Prophet(
        changepoint_prior_scale=cps,
        seasonality_prior_scale=sps
    )
    m.add_country_holidays(country_name='US')
    m.fit(df)
    
    df_cv = cross_validation(m, initial='730 days', period='90 days', horizon='90 days')
    df_p = performance_metrics(df_cv, rolling_window=1.0)
    
    results.append({
        'cps': cps,
        'sps': sps,
        'mape': df_p['mape'].mean()
    })

best = min(results, key=lambda x: x['mape'])
print(best)
```

**Worked result example:**

```
cps=0.001  sps=0.01   mape=0.19   ← underfitting trend
cps=0.05   sps=1.0    mape=0.09   ← default
cps=0.1    sps=1.0    mape=0.08   ← winner
cps=0.5    sps=1.0    mape=0.11   ← overfitting changepoints
```

Note: tuning `seasonality_prior_scale` has less impact than `changepoint_prior_scale` in most business series. If computation is expensive, fix `seasonality_prior_scale=10.0` (generous) and only search `changepoint_prior_scale`.

## Coverage Diagnostic

If `coverage` is consistently below the nominal level (0.80 for 80% intervals), the model is underestimating uncertainty. Two causes:

1. **Residuals are autocorrelated** — Prophet's IRON LAW: it does not model autocorrelation, so its intervals are based only on historical trend change variance. If the business metric has strong short-term momentum, intervals will be too narrow by construction.
2. **`changepoint_prior_scale` too low** — trend is over-constrained, so forecast uncertainty is understated.

Quick check for cause 1:
```python
from prophet.diagnostics import cross_validation
import pandas as pd

df_cv = cross_validation(m, initial='730 days', period='30 days', horizon='90 days')
residuals = df_cv['y'] - df_cv['yhat']

# Lag-1 autocorrelation of residuals per cutoff group
autocorr = residuals.groupby(df_cv['cutoff']).apply(
    lambda x: x.autocorr(lag=1)
)
print(autocorr.describe())
# If mean > 0.3, autocorrelation is the problem — consider ARIMA on residuals
```

## Decision Table: Parameter Selection

| Situation | Recommendation |
|-----------|---------------|
| < 2 years of daily data | Reduce `initial`; accept wider CI on MAPE estimate |
| Very short horizon (≤ 7 days) | Set `initial='180 days'`, `period='7 days'`, `horizon='7 days'` |
| Slow grid search | Fix `seasonality_prior_scale=10.0`; only tune `changepoint_prior_scale` |
| Coverage consistently < 0.75 | Check residual autocorrelation; consider adding regressors |
| MAPE spikes at specific horizon days | Those days likely contain holidays not modeled — add them |
| Seasonal business (e.g., retail) | Use `initial` of at least 3 years to capture Black Friday variance |

## What CV Does NOT Tell You

- Whether the model is correctly specified (check component plots)
- Whether future data will resemble the past (regime changes break all forecasts)
- Whether a regressor is causal (Prophet regressors are correlational)

CV confirms that the model generalizes to historical out-of-sample periods. It does not validate against future structural breaks.

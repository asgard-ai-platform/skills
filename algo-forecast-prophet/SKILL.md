---
name: "algo-forecast-prophet"
description: "Build forecasting models with Meta's Prophet for business time series with holidays and changepoints. Use this skill when the user needs user-friendly time series forecasting, handling of missing data and holidays, or automatic changepoint detection — even if they say 'forecast with Prophet', 'business forecast', or 'easy time series model'."
metadata:
  category: "WP-47 時間序列預測"
  tags: ["forecasting", "prophet", "time-series", "business-analytics"]
---

# Prophet Forecasting

## Overview

Prophet (Meta) decomposes time series into trend + seasonality + holidays + error. Uses an additive (or multiplicative) model fitted with Stan. Handles missing data, outliers, and holiday effects natively. Designed for business time series at daily/weekly granularity.

## When to Use

**Trigger conditions:**
- Forecasting business metrics (sales, traffic, engagement) at daily/weekly frequency
- Data with strong seasonal patterns and known holiday effects
- Need quick, reasonable forecasts without deep time series expertise

**When NOT to use:**
- For high-frequency data (sub-hourly) — Prophet is designed for daily+
- When you need causal/explanatory models (Prophet is descriptive)
- For very short time series (< 2 seasonal cycles)

## Algorithm

```
IRON LAW: Prophet Is an Additive Regression Model, NOT Classical Time Series
y(t) = g(t) + s(t) + h(t) + ε(t)
- g(t): piecewise linear or logistic trend with automatic changepoints
- s(t): Fourier series for yearly/weekly/daily seasonality
- h(t): user-specified holiday effects
Prophet does NOT model autocorrelation in residuals. If residuals are
autocorrelated, the uncertainty intervals will be too narrow.
```

### Phase 1: Input Validation
Prepare DataFrame with columns: ds (datestamp), y (metric). Add regressor columns if available. Specify: country holidays, custom holidays, growth type.
**Gate:** Data formatted, minimum 2 full seasonal cycles.

### Phase 2: Core Algorithm
1. Choose growth model: 'linear' (default) or 'logistic' (with cap and floor)
2. Set seasonality: yearly (default), weekly (default), custom (e.g., monthly)
3. Add holidays: country built-ins + custom events (promotions, launches)
4. Fit model: `m = Prophet(); m.fit(df)`
5. Generate future DataFrame and predict: `m.predict(future)`

### Phase 3: Verification
Check: forecast components (trend, seasonality, holidays) are intuitive. Cross-validate: use Prophet's built-in `cross_validation()` with rolling windows. Evaluate MAPE, RMSE.
**Gate:** MAPE acceptable for use case, components pass visual inspection.

### Phase 4: Output
Return forecast with decomposed components.

## Output Format

```json
{
  "forecasts": [{"ds": "2025-04-15", "yhat": 1200, "yhat_lower": 1050, "yhat_upper": 1350}],
  "components": {"trend": "upward_3pct", "yearly_seasonality": "peak_in_december", "weekly_seasonality": "low_on_weekends"},
  "metadata": {"mape": 0.08, "training_days": 730, "forecast_days": 90}
}
```

## Examples

### Sample I/O
**Input:** 2 years of daily website traffic with Christmas spike and summer dip
**Expected:** Forecast captures: upward trend, weekly pattern (weekday > weekend), annual pattern (Christmas spike, summer dip).

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Many missing days | Prophet handles natively | Unlike ARIMA, no imputation needed |
| Sudden trend change | Changepoint detected automatically | Prophet's key feature vs ARIMA |
| Multiplicative seasonality | Set seasonality_mode='multiplicative' | When seasonal amplitude grows with trend |

## Gotchas

- **Default changepoint sensitivity**: Prophet may over/under-detect trend changes. Tune `changepoint_prior_scale` (default 0.05): higher = more flexible, lower = smoother.
- **Flat forecasts**: If trend changepoints are too conservative, long-range forecasts can be unrealistically flat. Increase flexibility or specify growth cap.
- **Holiday effects require specification**: Prophet doesn't discover holidays automatically. You must provide a holiday DataFrame — missing holidays will not be modeled.
- **Not for causal inference**: Prophet finds patterns but doesn't explain why. Adding a regressor shows correlation, not causation.
- **Uncertainty intervals**: Based on historical trend change variance, not residual autocorrelation. May be too narrow if residuals are structured.

## References

- For Prophet hyperparameter tuning guide, see `references/prophet-tuning.md`
- For cross-validation best practices, see `references/prophet-cv.md`

---
name: "algo-forecast-arima"
description: "Build ARIMA models for time series forecasting with trend and seasonality decomposition. Use this skill when the user needs to forecast future values from historical sequential data, test for stationarity, or select ARIMA parameters — even if they say 'time series forecast', 'predict next month sales', or 'ARIMA model'."
metadata:
  category: "WP-47 時間序列預測"
  tags: ["forecasting", "arima", "time-series", "statistics"]
---

# ARIMA Time Series Model

## Overview

ARIMA(p,d,q) combines autoregression (AR), differencing (I), and moving average (MA) for time series forecasting. Seasonal variant: SARIMA(p,d,q)(P,D,Q,s). Requires stationary data (achieved through differencing). Best for univariate series with clear trend/seasonality patterns.

## When to Use

**Trigger conditions:**
- Forecasting univariate time series (sales, demand, traffic)
- Data has clear trend and/or seasonal patterns
- Need interpretable model with statistical properties

**When NOT to use:**
- For multivariate forecasting with many external features (use ML models)
- For very long-range forecasts (ARIMA confidence intervals widen rapidly)
- For irregular/event-driven data (use causal models)

## Algorithm

```
IRON LAW: ARIMA Requires STATIONARY Data
Non-stationary data (trend, changing variance) violates ARIMA assumptions.
Test stationarity with ADF test (p < 0.05 = stationary).
If non-stationary: difference the series (d=1 usually suffices).
If still non-stationary after d=2, ARIMA may not be appropriate.
```

### Phase 1: Input Validation
Check: regular time intervals, no missing values (impute if needed), minimum 50 observations (ideally 2+ full seasonal cycles). Test stationarity with ADF test.
**Gate:** Data is regular, sufficient length, stationarity assessed.

### Phase 2: Core Algorithm
1. **Stationarity**: ADF test. If p > 0.05, difference (d=1). Retest.
2. **Parameter selection**: Examine ACF/PACF plots. Or use auto_arima (AIC-based grid search).
   - p (AR terms): PACF cutoff lag
   - q (MA terms): ACF cutoff lag
   - d: number of differences needed
3. **Fit model**: Maximum likelihood estimation
4. **Forecast**: Generate predictions with confidence intervals

### Phase 3: Verification
Check residuals: should be white noise (no autocorrelation). Ljung-Box test (p > 0.05 = no autocorrelation). Residuals normally distributed.
**Gate:** Residuals pass Ljung-Box test, no remaining patterns.

### Phase 4: Output
Return forecasts with confidence intervals.

## Output Format

```json
{
  "forecasts": [{"period": "2025-04", "forecast": 1250, "lower_95": 1100, "upper_95": 1400}],
  "model": {"order": [1,1,1], "seasonal_order": [1,1,1,12], "aic": 520.3},
  "metadata": {"training_periods": 60, "forecast_horizon": 12}
}
```

## Examples

### Sample I/O
**Input:** 12 monthly observations with upward trend: [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]

**Step 1:** First difference = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] (constant → stationary, d=1 sufficient)

**Step 2:** ARIMA(0,1,0) random walk with drift μ=2 is the simplest fitting model.

**Expected forecast (ARIMA(0,1,0) with drift=2):**
- Period 13: 32 + 2 = **34**
- Period 14: 32 + 4 = **36**
- Period 15: 32 + 6 = **38**

Verify: differenced series is constant (2) → no AR/MA terms needed. Residuals are exactly 0 → perfect fit (toy example). On real data, residuals should pass Ljung-Box (p > 0.05).

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| No trend, no seasonality | ARIMA(p,0,q) | No differencing needed |
| Strong trend only | ARIMA(p,1,q) | Single difference removes linear trend |
| Multiple seasonalities | ARIMA may struggle | Consider Prophet or TBATS instead |

## Gotchas

- **Over-differencing**: d=2 when d=1 suffices introduces unnecessary noise. Check if first difference is stationary before differencing again.
- **Auto-ARIMA isn't magic**: AIC-based selection can pick overfit models. Always check residual diagnostics regardless of auto selection.
- **Confidence intervals widen fast**: Multi-step forecasts accumulate uncertainty. Don't trust point forecasts beyond 2-3 seasonal cycles.
- **Calendar effects**: Business days, holidays, and leap years affect monthly/weekly data. ARIMA doesn't handle these natively — add regressors or use Prophet.
- **Structural breaks**: ARIMA assumes the data-generating process is stable. COVID, market shocks, or policy changes break this assumption.

## References

- For ACF/PACF interpretation guide, see `references/acf-pacf.md`
- For SARIMA seasonal parameter selection, see `references/seasonal-arima.md`

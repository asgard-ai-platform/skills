---
name: "algo-forecast-exponential"
description: "Apply exponential smoothing methods for time series forecasting with weighted moving averages. Use this skill when the user needs simple, robust forecasts, implement Holt-Winters for seasonal data, or build lightweight forecasting without complex models — even if they say 'simple forecast', 'moving average prediction', or 'smoothing method'."
metadata:
  category: "WP-47 時間序列預測"
  tags: ["forecasting", "exponential-smoothing", "holt-winters", "time-series"]
---

# Exponential Smoothing

## Overview

Exponential smoothing assigns exponentially decreasing weights to past observations. Three variants: Simple (SES, level only), Holt (level + trend), Holt-Winters (level + trend + seasonality). ETS framework (Error-Trend-Seasonality) provides a unified statistical model. Fast, interpretable, and competitive with complex models for short horizons.

## When to Use

**Trigger conditions:**
- Quick forecasting with minimal configuration
- Short-horizon forecasts (1-2 seasonal cycles ahead)
- Data with clear level, trend, and/or seasonal components

**When NOT to use:**
- For long-range forecasts (uncertainty accumulates too fast)
- When external regressors are important (use regression or ML models)

## Algorithm

```
IRON LAW: Smoothing Parameters Control the Bias-Variance Trade-Off
α (level), β (trend), γ (seasonality) range [0,1].
- α near 1: react quickly to changes, noisy forecasts (high variance)
- α near 0: smooth forecasts, slow to adapt (high bias)
Optimize via minimizing MSE on training data (or use information criteria).
Never hand-pick smoothing parameters without validation.
```

### Phase 1: Input Validation
Identify components: level only (SES), level+trend (Holt), level+trend+seasonality (Holt-Winters). Determine: additive vs multiplicative trend/seasonality.
**Gate:** Component structure identified, seasonal period known.

### Phase 2: Core Algorithm
**Holt-Winters (additive):**
1. Initialize: level₀ = mean(first season), trend₀ = (mean(season 2) - mean(season 1))/s, seasonal₀ from first season deviations
2. Update equations at each t:
   - Level: ℓₜ = α(yₜ - sₜ₋ₛ) + (1-α)(ℓₜ₋₁ + bₜ₋₁)
   - Trend: bₜ = β(ℓₜ - ℓₜ₋₁) + (1-β)bₜ₋₁
   - Seasonal: sₜ = γ(yₜ - ℓₜ) + (1-γ)sₜ₋ₛ
3. Forecast: ŷₜ₊ₕ = ℓₜ + h×bₜ + sₜ₊ₕ₋ₛ

### Phase 3: Verification
Check: in-sample RMSE, residual patterns. Compare against naive baselines (last value, seasonal naive).
**Gate:** Beats naive baseline, residuals show no systematic pattern.

### Phase 4: Output
Return forecasts with smoothed components.

## Output Format

```json
{
  "forecasts": [{"period": "2025-04", "forecast": 1150, "level": 1100, "trend": 20, "seasonal": 30}],
  "parameters": {"alpha": 0.3, "beta": 0.1, "gamma": 0.15},
  "metadata": {"method": "holt_winters_additive", "seasonal_period": 12, "rmse": 45}
}
```

## Examples

### Sample I/O
**Input:** 36 months of monthly sales, clear upward trend, December spike
**Expected:** Holt-Winters additive. Forecast continues trend with repeated December seasonality.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| No trend, no seasonality | SES (α only) | Simplest variant suffices |
| Seasonal amplitude grows | Use multiplicative | Additive would underestimate peaks |
| Very short series (<2 seasons) | SES or Holt only | Can't estimate seasonality |

## Gotchas

- **Additive vs multiplicative**: If seasonal swings grow proportionally with level, use multiplicative. Wrong choice produces poor forecasts, especially at extremes.
- **Initialization sensitivity**: The first season's values set the baseline. Poor initialization from noisy early data propagates through the entire forecast.
- **Damped trend**: For long horizons, linear trend extrapolation is unrealistic. Use damped trend (φ parameter) to flatten the trend over time.
- **Multiple seasonalities**: Standard Holt-Winters handles one seasonal period. For daily data with weekly AND yearly patterns, use TBATS or STL+ETS.
- **Outlier sensitivity**: A single outlier can shift the level estimate significantly (especially with high α). Pre-detect and handle outliers.

## References

- For ETS framework and model selection, see `references/ets-framework.md`
- For damped trend variants, see `references/damped-trend.md`

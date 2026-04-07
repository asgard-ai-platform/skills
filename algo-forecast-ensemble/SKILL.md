---
name: "algo-forecast-ensemble"
description: "Combine multiple forecasting models into ensemble predictions for improved accuracy. Use this skill when the user needs to improve forecast reliability, combine ARIMA/Prophet/ETS outputs, or build a robust forecasting pipeline — even if they say 'combine forecasts', 'model averaging', or 'which forecast should I trust'."
metadata:
  category: "WP-47 時間序列預測"
  tags: ["forecasting", "ensemble", "model-combination", "accuracy"]
---

# Ensemble Forecasting

## Overview

Ensemble forecasting combines predictions from multiple models to reduce variance and improve accuracy. Simple average of 3-5 diverse models often outperforms the best individual model. Methods: equal-weight average, inverse-error weighting, stacking with a meta-learner. The "forecast combination puzzle" shows simple averaging is hard to beat.

## When to Use

**Trigger conditions:**
- Multiple forecasting models are available and perform similarly
- Reducing forecast risk is more important than maximum accuracy
- Building a production pipeline that's robust to model failure

**When NOT to use:**
- When one model clearly dominates all others (just use that model)
- When computational budget only allows one model

## Algorithm

```
IRON LAW: Simple Average Often Beats Complex Combination
The "forecast combination puzzle" (Stock & Watson, 2004): equal-weight
averaging of diverse models frequently outperforms sophisticated
weighting schemes. This is because weight estimation introduces noise
that offsets the theoretical gain. Start with simple average and only
move to weighted combination if you have abundant validation data.
```

### Phase 1: Input Validation
Generate forecasts from 3+ diverse models (e.g., ARIMA, ETS, Prophet, ML-based). Ensure models are truly diverse (different assumptions/approaches).
**Gate:** 3+ model forecasts available, models use different methodologies.

### Phase 2: Core Algorithm
**Simple average:** ŷ_ensemble = (1/M) × Σ ŷ_m

**Inverse-error weighting:** w_m = (1/MSE_m) / Σ(1/MSE_j), ŷ_ensemble = Σ w_m × ŷ_m

**Stacking:** Train a meta-model (linear regression) that learns optimal weights from cross-validated individual model predictions.

### Phase 3: Verification
Compare ensemble vs individual models on held-out data. Ensemble should: have lower average error AND lower maximum error (more robust).
**Gate:** Ensemble RMSE ≤ best individual model RMSE.

### Phase 4: Output
Return ensemble forecast with component model contributions.

## Output Format

```json
{
  "ensemble_forecast": [{"period": "2025-04", "forecast": 1200, "lower_95": 1050, "upper_95": 1350}],
  "model_forecasts": {"arima": 1180, "prophet": 1220, "ets": 1200},
  "weights": {"arima": 0.35, "prophet": 0.30, "ets": 0.35},
  "metadata": {"method": "inverse_error_weighted", "ensemble_rmse": 42, "best_individual_rmse": 48}
}
```

## Examples

### Sample I/O
**Input:** ARIMA forecast=1180, Prophet=1220, ETS=1200 for next month sales
**Expected:** Simple average = 1200. If ARIMA historically best (lowest MSE), weighted average shifts toward 1180.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| All models agree | Ensemble = individual | Consensus, high confidence |
| Models wildly disagree | Ensemble = compromise, wide CI | High uncertainty, flag for review |
| One model is outlier | Average dampens outlier | Ensemble robustness benefit |

## Gotchas

- **Diversity is key**: Combining 5 ARIMA variants adds little. Combine fundamentally different approaches (statistical + ML + judgmental).
- **Weight instability**: Optimal weights estimated on past data may not be optimal in the future. Simple average avoids this instability.
- **Correlation between errors**: If model errors are correlated (they often are), ensemble improvement is limited. Seek models with uncorrelated errors.
- **Confidence intervals**: Combining point forecasts is easy. Combining prediction intervals properly requires knowledge of error correlation structure.
- **Over-engineering risk**: For stable, well-understood series, a single well-tuned model may outperform an ensemble. Ensembles shine for uncertain or volatile series.

## References

- For forecast combination methods survey, see `references/combination-survey.md`
- For stacking meta-learner implementation, see `references/stacking.md`

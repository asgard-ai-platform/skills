---
name: "algo-ad-ctr"
description: "Build CTR prediction models for estimating ad click-through rates from features. Use this skill when the user needs to predict click probability, build an ad ranking model, or evaluate ad creative performance — even if they say 'predict click rate', 'ad relevance scoring', or 'which ad will get more clicks'."
metadata:
  category: "WP-37 廣告演算法"
  tags: ["advertising", "ctr-prediction", "machine-learning", "ranking"]
---

# CTR Prediction Model

## Overview

CTR prediction estimates the probability that a user clicks on an ad given context (user, query, ad, position). Forms the core of ad ranking: AdRank = Bid × pCTR. Typically uses logistic regression or gradient-boosted trees. Training on billions of impressions.

## When to Use

**Trigger conditions:**
- Building or improving an ad ranking system
- Predicting click probability for bid optimization
- Evaluating ad creative effectiveness from feature analysis

**When NOT to use:**
- When predicting post-click conversions (use conversion rate model)
- When setting bid amounts (use bidding strategy skill)

## Algorithm

```
IRON LAW: A CTR Model Must Be CALIBRATED
Predicting relative ranking is insufficient. The predicted probability
must MATCH actual click frequency (e.g., predicted 5% → 5 clicks per
100 impressions). Without calibration, bid optimization breaks:
  Expected Value = Bid × pCTR × pConversion
  If pCTR is off by 2x, bids are wrong by 2x.
```

### Phase 1: Input Validation
Collect impression logs with: user features, ad features, query features, position, click label (0/1). Handle class imbalance (CTR typically 1-5%).
**Gate:** Sufficient volume (100K+ impressions), click labels verified, no data leakage from position.

### Phase 2: Core Algorithm
1. Feature engineering: user demographics, ad category, query-ad match, historical CTR, time/device features
2. Train model: logistic regression (interpretable) or GBDT (higher accuracy)
3. Calibrate predictions: Platt scaling or isotonic regression on holdout set
4. Evaluate: log-loss (calibration) + AUC (ranking quality)

### Phase 3: Verification
Check calibration: bucket predictions into deciles, compare predicted vs actual CTR per bucket. Plot reliability diagram.
**Gate:** Calibration curve close to diagonal, AUC > 0.70.

### Phase 4: Output
Return predicted CTR with confidence interval and top contributing features.

## Output Format

```json
{
  "prediction": {"ctr": 0.035, "confidence_interval": [0.028, 0.042]},
  "top_features": [{"feature": "query_ad_match", "importance": 0.32}],
  "metadata": {"model": "gbdt", "auc": 0.78, "log_loss": 0.21, "calibration_error": 0.008}
}
```

## Examples

### Sample I/O
**Input:** Trained logistic regression with 3 features and these coefficients:
```
intercept: -3.0
position_1:  0.8
query_ad_match: 1.5
user_is_mobile: 0.3
```
Features for current request: position_1=1, query_ad_match=1, user_is_mobile=1

**Expected:** logit = -3.0 + 0.8 + 1.5 + 0.3 = -0.4
pCTR = sigmoid(-0.4) = 1/(1 + e^0.4) ≈ 0.401 → **40.1%**

Verify: for features all 0 (baseline), pCTR = sigmoid(-3.0) ≈ 0.047 (4.7%). Calibration is checked by bucketing predictions and comparing to actual CTR in each bucket.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| New ad, no history | Use ad category average | Cold start for features |
| Position 1 vs position 4 | Different CTR, same relevance | Position bias inflates top-slot CTR |
| Very rare query | Low confidence | Insufficient training data for that query |

## Gotchas

- **Position bias**: Ads in position 1 get more clicks regardless of relevance. Train on position-debiased data or include position as a feature and normalize at inference.
- **Data freshness**: CTR patterns change rapidly (seasonality, trends). Retrain daily or use online learning.
- **Feature leakage**: Including click-derived features (e.g., historical CTR of this exact ad-query pair) creates leakage if not handled carefully with time-based splits.
- **Class imbalance**: 97% no-click, 3% click. Use proper evaluation metrics (log-loss, AUC), not accuracy. Consider downsampling negatives during training.
- **Multi-task learning**: CTR and conversion rate are related but different. Joint models can improve both by sharing lower layers.

## References

- For feature engineering best practices, see `references/feature-engineering.md`
- For position debiasing techniques, see `references/position-debiasing.md`

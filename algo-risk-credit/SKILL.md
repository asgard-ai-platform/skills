---
name: "algo-risk-credit"
description: "Build credit scoring models to predict default probability from borrower characteristics. Use this skill when the user needs to assess creditworthiness, build a credit scorecard, or evaluate lending risk — even if they say 'predict default risk', 'credit scoring', or 'loan approval model'."
metadata:
  category: "WP-40 風險演算法"
  tags: ["risk", "credit-scoring", "default-prediction", "lending"]
---

# Credit Scoring Model

## Overview

Credit scoring models predict the probability of default (PD) from borrower characteristics using logistic regression or gradient boosting. Output: a score (300-850 range) or PD (0-1). Used for loan approval, pricing, and portfolio risk management.

## When to Use

**Trigger conditions:**
- Building a scorecard for loan/credit approval decisions
- Predicting default probability for risk-based pricing
- Evaluating existing credit models for discriminatory power

**When NOT to use:**
- For corporate bankruptcy prediction (use Altman Z-Score)
- For market risk measurement (use VaR)

## Algorithm

```
IRON LAW: A Credit Model Must Discriminate AND Be Calibrated
Discrimination (AUC): correctly ranking good vs bad borrowers.
Calibration: predicted PD matches actual default rates.
A model with AUC=0.85 but predicted PD 2x actual default rate will
cause systematic over/under-pricing. Need BOTH properties.
```

### Phase 1: Input Validation
Collect: borrower features (income, debt ratio, credit history length, delinquency count, utilization), outcome variable (default within 12-24 months). Handle: missing values, class imbalance (typically 2-5% default rate).
**Gate:** Sufficient defaults (300+ events), features available at decision time.

### Phase 2: Core Algorithm
1. Feature engineering: WOE (Weight of Evidence) binning for logistic regression, or direct encoding for GBDT
2. Train model: logistic regression (interpretable, regulatory-preferred) or GBDT (higher accuracy)
3. Calibrate: Platt scaling on holdout, ensure predicted PD matches actual default rate by decile
4. Convert to score: Score = offset + factor × log(odds), scaled to 300-850 range

### Phase 3: Verification
Evaluate: AUC (>0.70 acceptable, >0.80 good), KS statistic, Gini coefficient. Population stability index (PSI) for monitoring drift.
**Gate:** AUC > 0.70, calibration acceptable, no discriminatory bias in protected attributes.

### Phase 4: Output
Return score, PD, and key risk drivers.

## Output Format

```json
{
  "score": 680,
  "pd": 0.035,
  "risk_grade": "B",
  "top_risk_factors": [{"factor": "high_utilization", "impact": -45}, {"factor": "short_history", "impact": -30}],
  "metadata": {"model": "logistic_regression", "auc": 0.78, "vintage": "2024-Q3"}
}
```

## Examples

### Sample I/O
**Input:** Borrower: income=$60K, DTI=35%, 5yr credit history, 0 delinquencies, 60% utilization
**Expected:** Score ~680, PD ~3.5%, Grade B (some risk from high utilization)

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| No credit history (thin file) | High uncertainty, default to conservative | Insufficient data for scoring |
| All features identical | Same score regardless of outcome | Model can't differentiate — need more features |
| Major economy shift | PSI > 0.25, model needs recalibration | Population has shifted from training distribution |

## Gotchas

- **Reject inference**: Training data only includes approved applicants. Rejected applicants' outcomes are unknown, creating selection bias. Use reject inference techniques.
- **Fair lending**: Models must not discriminate by protected attributes (race, gender, age). Even proxy variables (zip code ≈ race) can create disparate impact. Test with fairness metrics.
- **Through-the-door vs on-the-books**: TTD samples include all applicants; OTB only approved ones. Model purpose determines which sample to use.
- **Vintage analysis**: Default rates vary by economic conditions. A 2019-trained model may not predict well in a recession. Track model performance by vintage.
- **Regulatory requirements**: Financial regulators (Basel, OCC, FDIC) have specific requirements for model validation, documentation, and fair lending testing.

## References

- For WOE binning methodology, see `references/woe-binning.md`
- For reject inference techniques, see `references/reject-inference.md`

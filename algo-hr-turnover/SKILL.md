---
name: "algo-hr-turnover"
description: "Build employee turnover prediction models to identify flight risk and retention drivers. Use this skill when the user needs to predict which employees are likely to leave, identify retention risk factors, or prioritize HR interventions — even if they say 'attrition prediction', 'who is going to quit', or 'employee retention model'."
metadata:
  category: "WP-42 HR 演算法"
  tags: ["hr", "turnover-prediction", "attrition", "retention"]
---

# Employee Turnover Prediction

## Overview

Turnover prediction uses classification models (logistic regression, random forest, XGBoost) to estimate the probability an employee will leave within a defined period (typically 6-12 months). Features include tenure, compensation, performance, promotion history, and engagement signals.

## When to Use

**Trigger conditions:**
- Identifying employees at high risk of voluntary departure
- Quantifying which factors drive turnover for targeted interventions
- Prioritizing retention budgets toward highest-impact employees

**When NOT to use:**
- For involuntary termination planning (different process and ethics)
- When headcount is < 200 (insufficient data for reliable modeling)

## Algorithm

```
IRON LAW: Turnover Models Predict RISK, Not Certainty
A predicted 80% turnover probability means "employees with similar
profiles historically left 80% of the time." It does NOT mean this
specific employee WILL leave. Never use model outputs as sole basis
for employment decisions — that creates legal and ethical liability.
```

### Phase 1: Input Validation
Collect: employee demographics, tenure, compensation (relative to market), last promotion date, performance ratings, manager change history, engagement survey scores, commute distance. Outcome: voluntary departure within N months.
**Gate:** Minimum 200 turnover events, features available before departure date.

### Phase 2: Core Algorithm
1. Feature engineering: tenure buckets, comp ratio (salary/market median), time since last promotion, manager tenure, engagement trend
2. Handle class imbalance: turnover rate typically 10-20%. Use SMOTE or class weights.
3. Train: logistic regression (interpretable, HR-preferred) or GBDT (higher accuracy)
4. Output: probability of departure + top risk factors per employee

### Phase 3: Verification
Evaluate: AUC, precision-recall (at actionable thresholds). Backtest: did the model correctly flag employees who left in the past 6 months?
**Gate:** AUC > 0.70, precision > 50% at top decile.

### Phase 4: Output
Return risk scores with driver analysis.

## Output Format

```json
{
  "risk_scores": [{"employee_id": "E123", "turnover_prob": 0.72, "risk_tier": "high", "top_drivers": ["low_comp_ratio", "no_promotion_3yr"]}],
  "metadata": {"model": "xgboost", "auc": 0.78, "prediction_window_months": 12}
}
```

## Examples

### Sample I/O
**Input:** Employee: 4yr tenure, comp ratio 0.85, no promotion in 3yr, engagement score declining
**Expected:** High risk (>0.6). Top drivers: below-market compensation, stalled career progression.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| New hire (< 6 months) | Unreliable prediction | Insufficient behavioral data |
| Top performer, high comp | Still could leave | Non-financial factors (manager, culture) matter |
| Post-reorg period | Model drift likely | Unusual conditions distort patterns |

## Gotchas

- **Survivorship bias**: Training data only includes people who were hired and stayed long enough to observe. Early-stage leavers may be underrepresented.
- **Feature leakage**: "Started job searching" or "updated LinkedIn" are strong predictors but ethically and legally problematic to use. Stick to internal HR data.
- **Self-fulfilling prophecy**: If managers treat "high risk" employees differently (less investment, fewer projects), the model prediction becomes self-fulfilling.
- **Legal constraints**: Using protected attributes (age, gender, ethnicity) directly or via proxies may violate employment law. Audit for disparate impact.
- **Retention intervention timing**: Identifying risk is only useful if HR acts. Build the model into a retention workflow with specific intervention triggers.

## References

- For feature engineering from HR data, see `references/hr-features.md`
- For ethical AI in HR applications, see `references/ethical-hr-ai.md`

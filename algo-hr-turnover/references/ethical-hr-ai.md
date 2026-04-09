# Ethical AI in HR Turnover Prediction

## Core Legal Framework

Three U.S. legal doctrines directly constrain turnover models. Non-U.S. deployments have analogues (EU AI Act Article 6, Taiwan PDPA).

| Doctrine | What it prohibits | How it surfaces in turnover models |
|---|---|---|
| **Disparate Treatment** | Using protected attributes as inputs | Feeding age, gender, ethnicity directly to the model |
| **Disparate Impact** | Neutral policies that disproportionately harm protected groups | A model that flags 40% of women as "high risk" vs. 10% of men |
| **Retaliation** | Acting on predictions as a reason to disadvantage employees | Using a high turnover score to justify denying a promotion |

The EEOC's **4/5ths Rule (80% Rule)** is the standard disparate impact trigger:

```
Selection Rate Ratio = (Adverse Rate for Protected Group) / (Adverse Rate for Reference Group)

If ratio < 0.80 → prima facie disparate impact, requires justification
```

"Adverse outcome" in a retention context = being flagged as high-risk AND then receiving reduced investment (fewer projects, no raise, no promotion conversation).

---

## Disparate Impact Audit Procedure

Run this audit before deployment and quarterly thereafter.

### Step 1: Define the Protected Groups

Minimum groups to test: gender, age band (40+ vs. under 40), race/ethnicity, disability status. **Do not use these as model features**, but you must have them to audit.

### Step 2: Compute Group-Level Flagging Rates

```python
import pandas as pd

def flagging_rate_by_group(df, group_col, risk_threshold=0.60):
    """
    df: employees with columns [group_col, 'turnover_prob']
    Returns flagging rate per group and the 4/5ths ratio vs. reference group.
    """
    df['flagged'] = df['turnover_prob'] >= risk_threshold
    rates = df.groupby(group_col)['flagged'].mean().rename('flag_rate')
    reference_rate = rates.max()  # highest rate = reference group
    rates_df = rates.reset_index()
    rates_df['ratio_to_reference'] = rates_df['flag_rate'] / reference_rate
    rates_df['disparate_impact'] = rates_df['ratio_to_reference'] < 0.80
    return rates_df
```

**Worked example:**

| Group | N | Flagged | Flag Rate | Ratio | DI Triggered? |
|---|---|---|---|---|---|
| Male | 600 | 72 | 12.0% | 1.00 (ref) | — |
| Female | 400 | 76 | 19.0% | 0.63 | **Yes** |
| Age < 40 | 700 | 98 | 14.0% | 1.00 (ref) | — |
| Age 40+ | 300 | 18 | 6.0% | 0.43 | **Yes** |

Two violations here. The female over-flagging likely reflects legitimate turnover drivers (compensation gap, promotion rate). The age-40+ under-flagging is a survivorship artifact (older workers who stayed are intrinsically low-risk). Both require investigation before deployment.

### Step 3: Root-Cause the Disparity

A flagging disparity can come from three sources:

```
Source A: True disparity — group actually leaves at higher rates (model is correct)
Source B: Proxy leakage — a feature encodes the protected attribute
Source C: Model bias — the model miscalibrates for one group
```

Distinguish A vs. B vs. C:

1. **Check actual turnover rates by group in training data.** If female turnover rate in training is 19% and male is 12%, Source A explains the gap. The model is not biased — the workplace is.

2. **Partial dependence on suspected proxies.** Run a permutation importance after removing the protected attribute. If `comp_ratio` alone accounts for a gender flagging disparity, then your comp_ratio feature is encoding the gender pay gap.

3. **Calibration by group.** Plot predicted probability vs. actual turnover rate within each group. A well-calibrated model should have points on the diagonal for every group.

```python
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

def plot_calibration_by_group(df, group_col, n_bins=5):
    for group, subset in df.groupby(group_col):
        fraction_of_pos, mean_predicted = calibration_curve(
            subset['actual_turnover'], subset['turnover_prob'], n_bins=n_bins
        )
        plt.plot(mean_predicted, fraction_of_pos, marker='o', label=str(group))
    plt.plot([0, 1], [0, 1], 'k--', label='Perfect calibration')
    plt.xlabel('Mean Predicted Probability')
    plt.ylabel('Fraction Positive')
    plt.legend()
    plt.title(f'Calibration by {group_col}')
```

If a group's calibration curve is far from the diagonal, the model is systematically over- or under-predicting for them — that's Source C bias.

---

## The Proxy Leakage Problem

Removing a protected attribute from model inputs is **not sufficient**. Features commonly used in turnover models can proxy for protected attributes:

| Feature | Protected attribute it may proxy |
|---|---|
| `comp_ratio` | Gender (gender pay gap) |
| `commute_distance` | Race (residential segregation) |
| `years_since_last_promotion` | Gender, age (promotion rate disparities) |
| `manager_change_count` | Ethnicity (network effects in org structure) |
| `engagement_survey_score` | Disability status (accessibility barriers) |

**Fairness through unawareness** (just removing the protected column) is the weakest possible intervention. It does not resolve proxy leakage.

Stronger option: **Fairness constraints during training**. XGBoost and logistic regression don't natively support fairness constraints, but you can post-process thresholds by group:

### Group-Specific Threshold Calibration

Instead of a single 0.60 threshold for "high risk", set group-specific thresholds such that the **false positive rate** (flagging someone who would not have left) is equal across groups:

```python
from sklearn.metrics import roc_curve

def equal_fpr_thresholds(df, group_col, target_fpr=0.10):
    """
    Returns a threshold per group such that false positive rate = target_fpr.
    """
    thresholds = {}
    for group, subset in df.groupby(group_col):
        negatives = subset[subset['actual_turnover'] == 0]
        # Sort by predicted probability descending
        # Find the probability at which FPR = target_fpr
        fpr, tpr, thresh = roc_curve(subset['actual_turnover'], subset['turnover_prob'])
        # Pick threshold closest to target_fpr
        idx = (fpr - target_fpr).__abs__().argmin()
        thresholds[group] = thresh[idx]
    return thresholds
```

**Tradeoff**: equalizing false positive rates across groups will typically produce different true positive rates. You cannot simultaneously equalize FPR, FNR, and overall accuracy across groups when base rates differ — this is the **impossibility theorem** (Chouldechova 2017). You must choose which fairness criterion matters most for your context.

| Fairness Criterion | What it equalizes | HR context where this matters |
|---|---|---|
| Equal FPR | False flag rate | When retention investment is costly and you don't want to waste it on people who wouldn't leave anyway |
| Equal FNR | Miss rate | When missing a real leaver is the costly error (e.g., critical-role retention) |
| Demographic Parity | Flagging rate | Required when disparate impact is the primary legal concern |
| Calibration | Predicted = actual rate | When scores are used as inputs to decisions alongside human judgment |

For most HR deployments: **calibration + disparate impact check** is the minimum. Equalized FPR is a secondary constraint.

---

## Feature Inclusion Decision Framework

Before including any feature in the model, apply this gate:

```
1. Is it a protected attribute? → EXCLUDE.

2. Does it proxy a protected attribute?
   Run: Pearson correlation (continuous) or Cramér's V (categorical)
   between the feature and each protected attribute.
   
   If |corr| > 0.30 or Cramér's V > 0.30 → HIGH PROXY RISK.
   
   Decision: include only if:
     a) The feature has legitimate business justification (e.g., comp_ratio
        is a real turnover driver, not just a proxy), AND
     b) You run a disparate impact audit post-training, AND
     c) You document the decision and the audit result.

3. Is it observable before the outcome?
   → EXCLUDE if it can only be observed post-departure
     (e.g., exit interview themes, separation codes).
     These create feature leakage, not just fairness problems.

4. Is it ethically collected?
   → EXCLUDE LinkedIn activity monitoring, keylogger data, email sentiment
     without explicit consent. These create legal exposure independent
     of whether they're predictive.
```

---

## Organizational Use Controls

The technical model is only part of the ethical surface. The workflow around the model is where liability concentrates.

### What HR May Do With Scores

| Action | Acceptable? | Condition |
|---|---|---|
| Prioritize retention conversation with manager | Yes | Manager is trained that score is probabilistic |
| Trigger compensation review | Yes | Reviews are also offered to equivalent low-risk employees |
| Deny promotion | **No** | Score cannot be a reason to withhold advancement |
| Reduce project allocation | **No** | Self-fulfilling prophecy + potential retaliation claim |
| Share score with employee's manager without HR mediation | Caution | Depends on manager training; default: HR-mediated only |
| Include score in performance review | **No** | Conflates prediction with evaluation |

### Required Documentation

Before deployment, produce and retain:

1. **Model card**: training data date range, features, AUC, demographic breakdown of training set
2. **Disparate impact audit results**: flagging rates by protected group, ratio to reference, remediation taken
3. **Use policy**: explicit list of permitted and prohibited downstream uses
4. **Review cadence**: who reviews the model quarterly and what triggers retraining

---

## Recidivism Model Analogy (What Not to Do)

The COMPAS recidivism scoring controversy is the canonical reference for HR AI ethics. The system predicted reoffending risk and was used in sentencing. ProPublica (2016) showed the false positive rate for Black defendants was ~45% vs. ~24% for white defendants.

The HR analog: a turnover model that has a 30% false flag rate for women vs. 12% for men, and managers use those flags to under-invest in women's development, is structurally identical. The outcome (career harm) accumulates from the model output even if no individual decision-maker intended discrimination.

**The lesson**: High AUC on aggregate does not mean equal accuracy across groups. Audit at the group level before deployment.

---

## Taiwan-Specific Legal Notes

If deploying in Taiwan:

- **個人資料保護法 (PDPA)**: Employee data is sensitive personal data. Automated decisions using this data require either employee consent or a statutory basis. Turnover scores derived from HR data likely require consent if used beyond the original collection purpose.
- **就業服務法 §5**: Prohibits discrimination in employment based on race, class, language, thought, religion, party affiliation, birthplace, gender, sexual orientation, age, marital status, appearance, disability, or past union activity. Model features that proxy these attributes create direct legal exposure.
- **No specific AI regulation** as of 2025, but PDPA enforcement is active. Document your data processing basis before deployment.

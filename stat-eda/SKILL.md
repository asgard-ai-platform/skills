---
name: "stat-eda"
description: "Conduct Exploratory Data Analysis (EDA) using descriptive statistics, visualizations, and data quality checks. Use this skill when the user has a dataset and needs to understand its structure, find patterns, detect anomalies, or prepare data for further analysis — even if they say 'what does this data look like', 'find interesting patterns', 'clean this data', or 'summarize this dataset'."
metadata:
  category: "WP-21 設計/資訊/傳播/公衛"
  tags: ["data-analysis", "eda", "statistics", "visualization"]
---

# Exploratory Data Analysis (EDA)

## Framework

```
IRON LAW: Perform EDA Only AFTER Train/Test Split — Or You Leak the Future

Agents know "do EDA first." But they almost always do EDA on the FULL
dataset before splitting. This is information leakage: you've seen the
test set's distributions, outliers, and correlations, and your subsequent
modeling choices (feature scaling, outlier treatment, imputation strategy)
are now informed by data the model shouldn't see. Split first, then EDA
only on the training set. Apply the same transformations to the test set
without re-examining it.

Exception: data quality checks (nulls, dtypes, duplicates) CAN run on
the full dataset since they don't inform model hyperparameters.
```

### EDA Workflow

Standard five-phase flow (structure → quality → univariate → bivariate →
findings summary). Assume the agent already knows these steps. Focus on
the non-obvious traps below instead.

**Critical additions most EDA guides miss:**

1. **Split BEFORE explore** (see IRON LAW above)
2. **Missing data pattern matters more than count**: MCAR is safe to impute; MNAR (e.g. high-income respondents skip income question) requires domain modeling, not mean-fill
3. **Simpson's paradox check**: If a trend holds in the aggregate but reverses within subgroups, the aggregate trend is misleading. Always stratify by the most obvious confound before reporting a bivariate finding
4. **Data leakage in features**: A feature that perfectly correlates with the target is usually derived FROM the target (e.g. "refund_amount" predicting churn — it's an effect, not a cause). Flag any feature with r > 0.95 for causal review

For the visualization selection guide, see [`references/missing-data.md`](references/missing-data.md).

## Output Format

```markdown
# EDA Report: {Dataset Name}

## Dataset Overview
- Rows: {N}, Columns: {N}
- Date range: {if applicable}
- Key columns: {description}

## Data Quality
| Issue | Columns Affected | Count/% | Action |
|-------|-----------------|---------|--------|
| Missing values | {cols} | {N / %} | {drop / impute / investigate} |
| Outliers | {cols} | {N} | {cap / remove / keep} |
| Duplicates | — | {N} | {remove} |

## Key Statistics
| Variable | Mean | Median | Std | Min | Max | Distribution |
|----------|------|--------|-----|-----|-----|-------------|
| {var} | ... | ... | ... | ... | ... | {normal/skewed/bimodal} |

## Key Findings
1. {insight with supporting data}
2. {insight}
3. {insight}

## Recommendations
- {next analysis step or data issue to resolve}
```

## Gotchas

- **Correlation ≠ causation**: EDA finds associations. Establishing causation requires controlled experiments or causal inference methods.
- **Outliers can be data errors OR real signal**: Don't auto-remove. Investigate. A transaction amount of $1M might be a typo or your biggest customer.
- **Missing data has meaning**: Data missing from one column may be related to values in another. "Missing income" may mean "unemployed", not random. Check patterns.
- **Visualization lies**: Truncated Y-axes, cherry-picked time ranges, and misleading scales can distort insights. Always use appropriate scales and note limitations.

## References

- For missing data handling strategies, see `references/missing-data.md`

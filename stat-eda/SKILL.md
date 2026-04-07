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
IRON LAW: Look at the Data Before Modeling

NEVER fit a model, run a test, or draw conclusions without first exploring
the data. EDA reveals data quality issues, distribution shapes, outliers,
and relationships that determine which methods are appropriate.

A regression on data with outliers, missing values, and non-linear
relationships produces garbage results.
```

### EDA Workflow

**1. Structure Check**
- Shape: rows × columns
- Data types: numeric, categorical, datetime, text
- Column names and meanings
- Primary key / unique identifier

**2. Data Quality Assessment**
- Missing values: count and pattern (MCAR, MAR, MNAR)
- Duplicates: exact and near-duplicates
- Inconsistencies: mixed formats, typos, impossible values
- Outliers: statistical (z-score > 3, IQR method) and domain-based

**3. Univariate Analysis**
- Numeric: mean, median, std, min/max, distribution shape (histogram), skewness
- Categorical: value counts, mode, cardinality, bar chart
- Datetime: range, gaps, seasonality

**4. Bivariate/Multivariate Analysis**
- Numeric × numeric: correlation matrix, scatter plots
- Numeric × categorical: grouped statistics, box plots
- Categorical × categorical: cross-tabulation, chi-square
- Time series: trend, seasonality, autocorrelation

**5. Key Findings Summary**
- Top 3-5 insights or patterns discovered
- Data quality issues requiring attention
- Hypotheses generated for further investigation
- Recommended next steps (modeling, cleaning, additional data needed)

### Visualization Selection Guide

| Question | Chart Type |
|----------|-----------|
| Distribution of one variable | Histogram, box plot, density plot |
| Comparison across categories | Bar chart, grouped bar |
| Relationship between two numerics | Scatter plot |
| Trend over time | Line chart |
| Composition / proportion | Stacked bar, pie (sparingly) |
| Correlation overview | Heatmap of correlation matrix |

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

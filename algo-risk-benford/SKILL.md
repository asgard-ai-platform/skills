---
name: "algo-risk-benford"
description: "Apply Benford's Law to detect anomalies in numerical datasets by analyzing first-digit frequency distributions. Use this skill when the user needs to audit financial data for fraud indicators, validate data integrity, or detect fabricated numbers — even if they say 'data manipulation detection', 'first digit test', or 'accounting fraud screening'."
metadata:
  category: "WP-40 風險演算法"
  tags: ["risk", "benfords-law", "fraud-detection", "data-audit"]
---

# Benford's Law Analysis

## Overview

Benford's Law predicts that in naturally occurring datasets, the leading digit d appears with probability P(d) = log₁₀(1 + 1/d). Digit 1 appears ~30.1% of the time, digit 9 only ~4.6%. Deviations from this distribution may indicate data fabrication or manipulation. Analysis runs in O(n).

## When to Use

**Trigger conditions:**
- Auditing financial data (expenses, invoices, tax returns) for manipulation
- Screening large datasets for data integrity issues
- Detecting fabricated or artificially rounded numbers

**When NOT to use:**
- For assigned/sequential numbers (zip codes, phone numbers, IDs)
- For datasets with constrained ranges (e.g., human ages, percentages)
- For small datasets (< 500 records — insufficient statistical power)

## Algorithm

```
IRON LAW: Benford's Law Applies to NATURALLY OCCURRING Data Spanning Orders of Magnitude
Data that doesn't span multiple orders of magnitude (e.g., temperatures
in Celsius, human heights) will NOT follow Benford's Law. Deviation from
Benford's in such data is EXPECTED, not suspicious. Always verify the
data type is appropriate before concluding fraud.
```

### Phase 1: Input Validation
Extract leading digits from dataset. Filter: remove zeros, negatives (take absolute value), values < 10. Verify dataset spans multiple orders of magnitude.
**Gate:** 500+ records, data spans at least 2 orders of magnitude.

### Phase 2: Core Algorithm
1. Extract first digit of each number
2. Count frequency of each digit (1-9)
3. Compare observed frequencies against Benford's expected: P(d) = log₁₀(1 + 1/d)
4. Statistical tests: chi-squared test, MAD (Mean Absolute Deviation), KS test

### Phase 3: Verification
MAD thresholds: < 0.006 (close conformity), 0.006-0.012 (acceptable), 0.012-0.015 (marginal), > 0.015 (non-conforming). Flag specific digits with large deviations.
**Gate:** MAD computed, non-conforming digits identified.

### Phase 4: Output
Return conformity assessment with digit-level analysis.

## Output Format

```json
{
  "conformity": "marginal",
  "mad": 0.013,
  "chi_squared": {"statistic": 18.5, "p_value": 0.018, "df": 8},
  "digit_analysis": [{"digit": 1, "observed_pct": 25.1, "expected_pct": 30.1, "deviation": -5.0}],
  "metadata": {"records": 5000, "dataset": "Q4 expense reports"}
}
```

## Examples

### Sample I/O
**Input:** 1000 invoice amounts from a company's AP ledger
**Expected:** First digits should approximate 30.1%, 17.6%, 12.5%, 9.7%, 7.9%, 6.7%, 5.8%, 5.1%, 4.6%. MAD < 0.012 for legitimate data.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| All amounts $90-$99 | Digit 9 dominates | Constrained range — Benford's doesn't apply |
| Round number spike (digit 1, 5) | Flag for review | May indicate round-number estimation or threshold manipulation |
| Government budget data | Typically conforms well | Large naturally-occurring financial datasets fit Benford's |

## Gotchas

- **Not proof of fraud**: Non-conformity is a RED FLAG, not evidence. Many legitimate processes produce non-Benford distributions. Always investigate further.
- **Second-digit test**: First digit test catches gross fabrication. Second-digit analysis catches more subtle manipulation (e.g., rounding to approval thresholds).
- **Combining datasets**: Mixing datasets from different processes may artificially create or destroy Benford conformity. Analyze homogeneous datasets.
- **Approval thresholds**: If expenses over $5,000 require VP approval, expect a spike of amounts just below $5,000 (digit 4 in the $4,9xx range). This is a behavioral pattern, flagged by second-digit analysis.
- **Sample size matters**: Chi-squared test is sensitive to sample size. With 100K+ records, even trivial deviations become statistically significant. Use MAD as primary metric.

## References

- For second and third digit extensions, see `references/higher-digit-tests.md`
- For case studies in fraud detection, see `references/fraud-case-studies.md`

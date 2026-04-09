# Fraud Case Studies: Benford's Law in Practice

Real-world applications of Benford's Law analysis. Each case illustrates a distinct pattern of manipulation and how digit-frequency analysis surfaces it.

---

## Case 1: Expense Report Fabrication (Round-Number Clustering)

### Background

A mid-size logistics company ran a quarterly audit on 4,200 employee expense reports totaling $1.8M. Approval threshold: expenses over $500 require manager sign-off; over $5,000 require VP sign-off.

### Observed vs. Expected First-Digit Distribution

| Digit | Expected % | Observed % | Deviation | Z-score |
|-------|-----------|------------|-----------|---------|
| 1     | 30.1%     | 28.4%      | −1.7%     | −1.1    |
| 2     | 17.6%     | 16.8%      | −0.8%     | −0.6    |
| 3     | 12.5%     | 11.2%      | −1.3%     | −1.1    |
| 4     | 9.7%      | **15.3%**  | **+5.6%** | **+4.2** |
| 5     | 7.9%      | 6.1%       | −1.8%     | −1.6    |
| 6     | 6.7%      | 6.3%       | −0.4%     | −0.4    |
| 7     | 5.8%      | 5.5%       | −0.3%     | −0.3    |
| 8     | 5.1%      | 5.2%       | +0.1%     | +0.1    |
| 9     | 4.6%      | 5.2%       | +0.6%     | +0.5    |

MAD = 0.018 → **non-conforming**  
Chi-squared = 31.4, df=8, p=0.0001

### Second-Digit Drill-Down on Digit-4 Records

Of the 642 digit-4 expense reports, second-digit breakdown:

| 2nd Digit | Count | % | Note |
|-----------|-------|---|------|
| 0–7       | 38    | 5.9% | spread as expected |
| **8**     | **487** | **75.9%** | **spike: $48x, $480-$489 range** |
| 9         | 117   | 18.2% | spike: $49x range |

The $480–$499 range accounted for 604 of 642 digit-4 records — employees submitting amounts just under the $500 approval threshold.

### Investigation Outcome

HR identified 23 employees with repeated $480–$499 claims. Cross-referencing against vendor receipts: 61% of the flagged claims had no supporting receipts or receipts that post-dated the submission. Total fraudulent claims recovered: $127,000.

### What Made It Detectable

The fraud was *behavioral*, not random fabrication. Employees chose amounts deliberately, which creates a non-Benford spike concentrated in a narrow band. First-digit test alone (MAD=0.018) flagged the dataset; second-digit analysis on digit-4 subset pinpointed the mechanism.

---

## Case 2: Fabricated Sales Data (Uniform-Distribution Signature)

### Background

A sales manager at a retail chain was suspected of inflating regional sales figures to hit quarterly bonus targets. Dataset: 2,100 daily sales records over 18 months.

### The Fabrication Signature

When people invent numbers, they tend toward psychological uniformity — roughly equal frequency across digits 1–9. They overcorrect away from "suspicious" patterns, not realizing that Benford's Law is itself the natural pattern.

Uniform distribution (fabricated): each digit ≈ 11.1%  
Benford's distribution: digit 1 = 30.1%, digit 9 = 4.6%

Observed distribution for the suspect records:

| Digit | Expected (Benford) | Observed | Deviation |
|-------|-------------------|----------|-----------|
| 1     | 30.1%             | 12.8%    | −17.3%    |
| 2     | 17.6%             | 11.4%    | −6.2%     |
| 3     | 12.5%             | 11.9%    | −0.6%     |
| 4     | 9.7%              | 11.2%    | +1.5%     |
| 5     | 7.9%              | 10.8%    | +2.9%     |
| 6     | 6.7%              | 11.1%    | +4.4%     |
| 7     | 5.8%              | 10.6%    | +4.8%     |
| 8     | 5.1%              | 10.8%    | +5.7%     |
| 9     | 4.6%              | 9.4%     | +4.8%     |

MAD = 0.056 → **severely non-conforming**

### Separating Fabricated from Legitimate Records

The manager only altered records for Tuesdays and Wednesdays (low-traffic days). Splitting by day-of-week:

| Subset | Records | MAD | Status |
|--------|---------|-----|--------|
| Mon, Thu, Fri | 1,260 | 0.008 | conforming |
| **Tue, Wed** | **840** | **0.061** | **non-conforming** |

The legitimate records conformed. The fabricated subset showed the near-uniform distribution signature.

### Key Pattern: Digit-1 Suppression

The single most reliable indicator of fabricated data is **digit-1 suppression**. Natural processes produce digit-1 ≈ 30% of the time; human intuition treats this as "too many 1s" and underrepresents it. In this case, digit-1 observed was 12.8% vs. expected 30.1% — a −17.3 percentage-point gap.

Compute the digit-1 z-score:

```
Expected count: n × 0.301 = 840 × 0.301 = 252.8
Observed count: 840 × 0.128 = 107.5
Standard deviation: sqrt(n × p × (1-p)) = sqrt(840 × 0.301 × 0.699) = 13.3
Z = (107.5 − 252.8) / 13.3 = −10.9
```

Z = −10.9 is astronomically unlikely under legitimate data. This alone warranted investigation.

---

## Case 3: Vendor Invoice Fraud (Duplicate and Ghost Vendors)

### Background

A government procurement office audited 8,500 vendor invoices over 3 fiscal years. Two fraud types were present simultaneously:

1. **Ghost vendors**: a procurement officer created fictitious vendors and submitted invoices to himself
2. **Invoice splitting**: a real vendor colluded to split large contracts into sub-threshold invoices to avoid competitive bidding (threshold: $10,000)

### Ghost Vendor Pattern (Random Fabrication)

Ghost vendor invoices (later confirmed): 340 records, MAD = 0.041

The amounts were fabricated semi-randomly but the forger avoided repeating exact amounts. Result: near-uniform distribution, digit-1 suppressed to 14%.

### Invoice Splitting Pattern (Threshold Avoidance)

Invoice splitting: 2,100 records from a single vendor, MAD = 0.029

The splitting created a spike at digit 9 (amounts $9,000–$9,999) and digit 8 ($8,000–$8,999):

| Digit | Expected | Observed |
|-------|---------|---------|
| 1     | 30.1%   | 28.4%   |
| ...   | ...     | ...     |
| 8     | 5.1%    | **12.3%** |
| 9     | 4.6%    | **14.8%** |

This is the inverse of the approval-threshold pattern from Case 1. Here amounts are pushed *just below* $10,000 rather than just below $500.

### Combined Dataset Masking

When all 8,500 invoices were analyzed together, MAD = 0.011 — *acceptable* range. The two fraud patterns partially canceled each other out:
- Ghost vendor invoices suppressed digit-1 (pushing MAD up)
- The overall legitimate majority masked both anomalies

**This is why homogeneous subsets matter.** The SKILL.md iron law about mixing datasets is borne out here: analyzing by vendor cohort exposed the fraud that aggregate analysis concealed.

Correct approach:
1. Run Benford's on full dataset → marginal flag (MAD=0.011)
2. Stratify by vendor → isolate the two anomalous vendor cohorts
3. Run per-cohort analysis → MAD 0.041 and 0.029 respectively → both non-conforming
4. Investigate flagged cohorts

---

## Case 4: Accounting Restatement Predictor (Enron-Era Pattern)

### Historical Context

Academic studies following the 2001–2003 wave of U.S. accounting scandals (Enron, WorldCom, Tyco) examined whether Benford's Law deviation predicted restatements before they became public. Carslaw (1988) and Nigrini (1996) established the methodology; post-Enron studies applied it retrospectively.

### Characteristic Pattern in Manipulated Financials

Accrual manipulation to hit earnings targets produces a specific pattern:

- **Digit-5 spike at second position**: managers rounding to "hit the number" tend to produce second digits of 0 and 5 more than expected (psychological round-number preference)
- **Digit-1 and digit-2 suppression at first position**: large accrual entries that start with 1 or 2 are suspicious in contexts where entries starting with 5–9 look more "random"

Second-digit Benford expectation:

| 2nd Digit | Expected % |
|-----------|-----------|
| 0         | 11.97%    |
| 1         | 11.39%    |
| 2         | 10.88%    |
| 3         | 10.43%    |
| 4         | 10.03%    |
| 5         | 9.67%     |
| 6         | 9.34%     |
| 7         | 9.04%     |
| 8         | 8.76%     |
| 9         | 8.50%     |

In post-restatement analysis of 79 companies, second-digit 0 and 5 were consistently over-represented (average excess: +3.1 and +2.4 percentage points respectively) in the quarters preceding restatement. The effect was not present in the non-restatement control group.

### Practical Application

When screening public company financials for manipulation risk:

1. Extract all journal entries for the period (general ledger data, not just reported figures)
2. Run second-digit test on entries above materiality threshold
3. Compute z-scores for digits 0 and 5 specifically:

```
Expected count of digit-0 in 2nd position: n × 0.1197
Z = (observed_0 − expected_0) / sqrt(n × 0.1197 × 0.8803)
```

4. Flag if Z(digit-0) > 2.5 OR Z(digit-5) > 2.5

This is not a standalone test — it is a triage filter to prioritize which companies or periods warrant deeper forensic review.

---

## Pattern Recognition Summary

| Fraud Type | Primary Signal | Secondary Signal | MAD Range |
|------------|---------------|-----------------|-----------|
| Random fabrication | Digit-1 suppressed (<15%) | Near-uniform distribution | 0.030–0.080 |
| Threshold avoidance (just-below) | Spike at digit just below threshold | 2nd-digit spike at 8 or 9 | 0.015–0.035 |
| Threshold avoidance (just-above) | Spike at threshold digit | Narrow 2nd-digit range | 0.012–0.025 |
| Invoice splitting | Spike at digits 8–9 | Concentration near limit | 0.015–0.040 |
| Accrual manipulation | 2nd-digit 0 and 5 excess | Specific period anomaly | 0.008–0.020 |
| Mixed fraud (multiple actors) | Aggregate MAD may be low | Cohort stratification required | varies |

---

## Limitations Illustrated by These Cases

**False negative risk (Case 3)**: Two fraud patterns in the same dataset can cancel each other statistically. Never rely solely on aggregate MAD. Always stratify by natural groupings (vendor, department, time period, approver).

**False positive risk**: Non-conformity is not proof of fraud. In Case 1, a legitimate retail business selling products in the $40–$49 range would also show a digit-4 spike. The behavioral context (approval thresholds) is what turns a statistical flag into an investigative lead.

**Scope limitation**: Benford's Law catches manipulation in the *distribution* of numbers. It does not catch:
- Consistently falsified amounts that happen to follow Benford's distribution
- Fraud involving correct amounts for fictional transactions (ghost vendors with realistic invoice amounts)
- Manipulation that doesn't touch the numerical amounts (e.g., falsified vendor identity)

In Case 3, the ghost vendor was caught because the forger's fabricated amounts were non-Benford. A more sophisticated forger who sampled amounts from real invoice distributions would not have been caught by this method alone.

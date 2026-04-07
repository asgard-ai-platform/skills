---
name: "ecom-rfm-analysis"
description: "Perform RFM (Recency, Frequency, Monetary) customer segmentation from transaction data. Use this skill when the user needs to segment customers by purchase behavior, identify high-value buyers, design retention campaigns, or prioritize marketing spend by customer value — even if they say 'who are our best customers', 'which customers are at risk of churning', or 'how do we target our marketing'."
metadata:
  category: "WP-01 電商"
  tags: ["e-commerce", "rfm", "segmentation", "customer-analytics"]
---

# RFM Analysis

## Overview

RFM segments customers based on three behavioral dimensions: Recency (when they last bought), Frequency (how often they buy), and Monetary (how much they spend). It converts raw transaction data into actionable customer segments for targeted marketing.

## Framework

```
IRON LAW: RFM Uses ACTUAL Behavior, Not Demographics

RFM is behavioral segmentation — it classifies by what customers DO,
not who they ARE. A 25-year-old and a 65-year-old in the same RFM segment
should receive the same treatment. Never mix RFM with demographic
assumptions.
```

### The Three Dimensions

| Dimension | What It Measures | How to Calculate |
|-----------|-----------------|-----------------|
| **Recency (R)** | Days since last purchase | Today - Last purchase date |
| **Frequency (F)** | Number of purchases in period | Count of distinct transactions |
| **Monetary (M)** | Total spend in period | Sum of transaction values |

### Scoring Method (Quintile-Based)

1. For each dimension, rank all customers and divide into 5 equal groups (quintiles)
2. Score 5 (best) to 1 (worst): R=5 means most recent, F=5 means most frequent, M=5 means highest spend
3. Combine into 3-digit RFM score (e.g., R5-F4-M5 = recent, frequent, high-value)

**Note**: For Recency, LOWER days = HIGHER score (more recent is better).

### Key Segments

| Segment | RFM Pattern | Description | Strategy |
|---------|------------|-------------|----------|
| **Champions** | R5, F5, M5 | Best customers, recent, frequent, high-value | Reward, loyalty program, early access |
| **Loyal** | R4-5, F4-5, M3-5 | Consistent buyers | Upsell, cross-sell, referral program |
| **Potential Loyalists** | R4-5, F2-3, M2-3 | Recent, moderate frequency | Nurture to increase frequency |
| **At Risk** | R2-3, F3-5, M3-5 | Were frequent/high-value, not buying recently | Win-back campaign, special offers |
| **Hibernating** | R1-2, F1-2, M1-2 | Long dormant, low value | Low-cost reactivation or let go |
| **New Customers** | R5, F1, M1-2 | Just made first purchase | Onboarding, second-purchase incentive |

### Implementation Steps

**Phase 1: Data Preparation**
- Required: Customer ID, Transaction Date, Transaction Amount
- Clean: Remove refunds, test orders, internal orders
- Set analysis window (typically 12-24 months)

**Phase 2: Calculate RFM Scores**
- Calculate R, F, M for each customer
- Assign quintile scores (1-5) for each dimension
- Combine into segments

**Phase 3: Segment and Act**
- Map each customer to a named segment (Champions, At Risk, etc.)
- Design targeted actions per segment
- Measure results: did targeted customers behave differently?

## Output Format

```markdown
# RFM Analysis: {Business}

## Data Summary
- Customers analyzed: {N}
- Analysis window: {start} to {end}
- Transactions: {N}

## Segment Distribution
| Segment | Count | % | Avg R (days) | Avg F | Avg M |
|---------|-------|---|-------------|-------|-------|
| Champions | {N} | {%} | {days} | {count} | ${X} |
| At Risk | {N} | {%} | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

## Key Findings
- Top 20% customers contribute {X%} of revenue
- {N} customers at risk of churning (were high-value, now dormant)
- {N} new customers need second-purchase nurturing

## Recommended Actions
| Segment | Action | Channel | Expected Impact |
|---------|--------|---------|----------------|
| Champions | {loyalty reward} | {email/app} | Increase AOV by X% |
| At Risk | {win-back offer} | {email/SMS} | Recover X% of dormant revenue |
```

## Gotchas

- **RFM is backward-looking**: It tells you what customers DID, not what they WILL do. Combine with predictive models (CLV prediction) for forward-looking insights.
- **Equal quintiles may not make sense**: If 80% of customers bought only once, quintile 1-4 are all "one-time buyers." Consider custom breakpoints based on business context.
- **Monetary can be misleading for subscriptions**: If everyone pays the same subscription fee, M dimension adds no information. Drop it and use RF only.
- **B2B vs B2C frequency differs**: A B2B customer buying quarterly is "frequent." A B2C customer buying quarterly may be "at risk." Calibrate to business context.
- **Don't over-message At Risk customers**: Bombarding dormant customers with emails can increase unsubscribes. One well-crafted win-back campaign is better than weekly emails.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/rfm_score.py` | Score customers on R/F/M and assign segment labels | `python scripts/rfm_score.py --help` |

Run `python scripts/rfm_score.py --verify` to execute built-in sanity tests.

## References

- For Python/SQL implementation code, see `references/rfm-implementation.md`
- For CLV prediction extending RFM, see `references/clv-prediction.md`

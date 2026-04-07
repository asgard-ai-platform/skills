---
name: "biz-cac-ltv"
description: "Calculate and analyze Customer Acquisition Cost (CAC) and Customer Lifetime Value (LTV) to evaluate unit economics and marketing efficiency. Use this skill when the user needs to assess whether their customer acquisition is profitable, optimize marketing spend allocation, or evaluate business model viability — even if they say 'are we spending too much on ads', 'what's each customer worth', or 'is our growth sustainable'."
metadata:
  category: "WP-14 商學院—行銷"
  tags: ["marketing", "unit-economics", "cac", "ltv"]
---

# CAC and LTV Analysis

## Overview

CAC (Customer Acquisition Cost) and LTV (Customer Lifetime Value) are the two fundamental unit economics metrics. Together they answer: "Does each customer generate more revenue than it costs to acquire them?" The LTV:CAC ratio is the single most important indicator of marketing efficiency and business model viability.

## When to Use

**Trigger conditions:**
- User evaluating marketing spend efficiency
- User asks "what's each customer worth?" or "are we spending too much on marketing?"
- User assessing business model viability or fundraising metrics
- User needs to allocate budget across acquisition channels

**When NOT to use:**
- For product pricing decisions → use Pricing Strategy
- For customer segmentation → use STP or RFM
- For comprehensive financial analysis → use financial ratios

## Framework

```
IRON LAW: LTV:CAC > 3 for Healthy Business

LTV:CAC ratio must be at least 3:1 for sustainable businesses.
- < 1:1 = You're LOSING money on every customer
- 1-3:1 = Unsustainable unless you can reduce CAC or increase LTV
- 3-5:1 = Healthy
- > 5:1 = Potentially underinvesting in growth (leaving market share on the table)

This ratio applies to the BLENDED average. Individual channels can be
below 3:1 if the overall blend exceeds it.
```

```
IRON LAW: CAC Must Include ALL Acquisition Costs

CAC = Total marketing & sales spend / Number of new customers acquired

"Total spend" includes: ad spend, marketing team salaries, sales team
salaries, tools, content production, events — EVERYTHING spent to acquire
customers in that period. Excluding salaries or tools understates true CAC.
```

### Step 1: Calculate CAC

**Basic formula:**
```
CAC = Total acquisition spend in period / New customers acquired in period
```

**By channel:**
```
CAC (Channel X) = Spend on Channel X / Customers from Channel X
```

Include in total acquisition spend:
- Advertising (digital + offline)
- Marketing team compensation
- Sales team compensation (for B2B)
- Marketing tools and software
- Content production costs
- Events and sponsorships
- Agency fees

### Step 2: Calculate LTV

**Simple formula:**
```
LTV = ARPU × Gross Margin % × Average Customer Lifespan
```

Where:
- **ARPU** = Average Revenue Per User per period (monthly or annual)
- **Gross Margin %** = (Revenue - COGS) / Revenue
- **Average Customer Lifespan** = 1 / Churn Rate

**Cohort-based (more accurate):**
Track actual revenue per customer cohort over time. Sum cumulative revenue per customer, apply gross margin.

### Step 3: Calculate Key Ratios

| Metric | Formula | Healthy Benchmark |
|--------|---------|-------------------|
| **LTV:CAC** | LTV / CAC | > 3:1 |
| **Payback Period** | CAC / (ARPU × Gross Margin) | < 12 months |
| **CAC % of LTV** | CAC / LTV × 100 | < 33% |

### Step 4: Segment Analysis

Calculate CAC and LTV by:
- **Channel**: Which acquisition channels are most efficient?
- **Customer segment**: Which segments have highest LTV:CAC?
- **Cohort**: Is LTV improving or degrading over time?

### Step 5: Optimization Strategies

**To reduce CAC:**
- Shift budget to lower-CAC channels
- Improve conversion rates (better landing pages, sales process)
- Increase organic/referral acquisition (content, word-of-mouth)

**To increase LTV:**
- Reduce churn (improve product, customer success)
- Increase ARPU (upsell, cross-sell, price increases)
- Extend customer lifespan (loyalty programs, switching costs)

## Output Format

```markdown
# CAC-LTV Analysis: {Company/Product}

## Unit Economics Summary

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| CAC (blended) | ${X} | — | — |
| LTV | ${X} | — | — |
| LTV:CAC | {X}:1 | > 3:1 | ✓/✗ |
| Payback Period | {X} months | < 12 months | ✓/✗ |

## CAC by Channel

| Channel | Spend | Customers | CAC | % of Total |
|---------|-------|-----------|-----|-----------|
| {channel} | ${X} | {N} | ${X} | {X%} |

## LTV Calculation

- ARPU: ${X}/month
- Gross Margin: {X%}
- Avg Lifespan: {X} months (churn rate: {X%}/month)
- LTV = ${X}

## LTV:CAC by Segment

| Segment | CAC | LTV | Ratio | Action |
|---------|-----|-----|-------|--------|
| {seg A} | ${X} | ${X} | {X}:1 | Invest / Maintain / Cut |

## Optimization Recommendations
1. ...
2. ...
```

## Examples

### Correct Application

**Scenario:** CAC-LTV for a Taiwanese B2C subscription box (monthly NT$599)

**CAC calculation:**
| Item | Monthly Spend |
|------|-------------|
| Facebook/Instagram ads | NT$200,000 |
| Google Ads | NT$80,000 |
| KOL partnerships | NT$50,000 |
| Marketing team (2 people) | NT$120,000 |
| **Total** | **NT$450,000** |

New customers in month: 300
**CAC = NT$450,000 / 300 = NT$1,500**

**LTV calculation:**
- ARPU: NT$599/month
- Gross Margin: 55%
- Monthly churn: 8% → Avg lifespan: 1/0.08 = 12.5 months
- **LTV = NT$599 × 0.55 × 12.5 = NT$4,118**

**LTV:CAC = 4,118 / 1,500 = 2.75:1** — Below the 3:1 threshold. Need to either reduce CAC or improve retention.

### Incorrect Application

**What went wrong:**
- CAC calculated as "ad spend / new customers" only, excluding NT$120K/month marketing team salary → True CAC is NT$1,500, not NT$1,100. Violates Iron Law: include ALL acquisition costs.
- LTV:CAC of 1.8:1 reported as "good because we're growing" → Growth at LTV:CAC < 3:1 means you're growing into larger losses. Violates Iron Law: ratio must be > 3:1.

## Gotchas

- **Attribution is messy**: A customer who saw an Instagram ad, Googled your brand, then signed up via a referral link — which channel gets credit? Be consistent in attribution methodology (first-touch, last-touch, or multi-touch).
- **Blended vs marginal CAC**: Blended CAC includes all channels. Marginal CAC is the cost of acquiring ONE MORE customer. As you scale, marginal CAC typically rises (best channels saturate first).
- **LTV is always an estimate**: Future churn and spending behavior are uncertain. Use conservative assumptions and update with real cohort data as it accumulates.
- **Payback period matters for cash flow**: Even with LTV:CAC of 5:1, if payback takes 24 months, you need significant upfront capital. Fast-growing companies can die from long payback periods despite great unit economics.
- **Negative churn is a superpower**: If expansion revenue (upsells) exceeds lost revenue (churn), Net Revenue Retention > 100%. This means LTV grows over time — the best possible scenario.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/cac_ltv.py` | Compute CAC, LTV, LTV/CAC ratio, and payback period | `python scripts/cac_ltv.py --help` |

Run `python scripts/cac_ltv.py --verify` to execute built-in sanity tests.

## References

- For cohort-based LTV calculation methods, see `references/cohort-ltv.md`
- For channel attribution models, see `references/attribution-models.md`

---
name: "ecom-analytics"
description: "Analyze e-commerce performance using GA4 metrics, conversion funnel analysis, and key e-commerce KPIs. Use this skill when the user needs to evaluate online store performance, diagnose conversion drop-offs, set up e-commerce tracking, or create performance dashboards — even if they say 'why are sales down', 'optimize our online store', 'set up GA4 for e-commerce', or 'what metrics should we track'."
metadata:
  category: "WP-01 電商"
  tags: ["e-commerce", "analytics", "ga4", "conversion"]
---

# E-Commerce Analytics

## Overview

E-commerce analytics measures online store performance across traffic, conversion, and revenue dimensions. This skill covers GA4 e-commerce tracking setup, funnel analysis, and key metric interpretation to diagnose why a store is or isn't performing.

## Framework

```
IRON LAW: Diagnose by Funnel Stage, Not by Symptom

"Sales are down" is a symptom, not a diagnosis. Decompose into funnel stages:
Traffic × Conversion Rate × AOV = Revenue

If revenue drops 20%, is it because traffic dropped (acquisition problem),
conversion dropped (UX/pricing problem), or AOV dropped (product mix problem)?
Each requires a completely different fix.
```

### E-Commerce Funnel & Key Metrics

| Stage | Metrics | What It Tells You |
|-------|---------|------------------|
| **Acquisition** | Sessions, Users, Traffic sources, CPC, CAC | Are you attracting enough visitors? From where? At what cost? |
| **Engagement** | Pages/session, Time on site, Bounce rate, Product views | Are visitors interested? Are they browsing? |
| **Conversion** | Add-to-cart rate, Checkout initiation rate, Purchase conversion rate | Where in the funnel are they dropping off? |
| **Revenue** | Revenue, AOV, Items per order, Revenue per session | How much are they spending? Is the mix healthy? |
| **Retention** | Repeat purchase rate, Purchase frequency, Customer lifetime value | Are they coming back? |

### GA4 E-Commerce Events

| Event | Trigger | Key Parameters |
|-------|---------|---------------|
| `view_item` | Product page view | item_id, item_name, price, category |
| `add_to_cart` | Add to cart click | items array, value, currency |
| `begin_checkout` | Checkout started | items, value, coupon |
| `add_payment_info` | Payment entered | payment_type |
| `purchase` | Order completed | transaction_id, value, tax, shipping, items |

### Diagnosis Framework

**Phase 1: Traffic Check**
- Is total traffic up/down/flat vs prior period?
- Which channels changed? (organic, paid, social, direct, referral)
- Is traffic quality declining? (bounce rate, pages/session by source)

**Phase 2: Conversion Check**
- Where is the biggest funnel drop-off?
- Compare: View → Add to cart → Checkout → Purchase
- Industry benchmark conversion rates: 1-3% overall, 5-10% add-to-cart

**Phase 3: Revenue Check**
- AOV trend: rising (upselling working) or falling (discounting eroding value)?
- Product mix: is revenue shifting to lower-margin products?
- Revenue per session: the master metric (traffic quality × conversion × AOV)

**Phase 4: Retention Check**
- Repeat purchase rate by cohort
- Time between first and second purchase
- LTV trend by acquisition channel

## Output Format

```markdown
# E-Commerce Performance Report: {Store}

## Summary Dashboard
| Metric | Current | Prior Period | Change | Status |
|--------|---------|-------------|--------|--------|
| Sessions | {N} | {N} | {%} | 🟢/🟡/🔴 |
| Conversion Rate | {%} | {%} | {%} | 🟢/🟡/🔴 |
| AOV | ${X} | ${X} | {%} | 🟢/🟡/🔴 |
| Revenue | ${X} | ${X} | {%} | 🟢/🟡/🔴 |

## Funnel Analysis
| Stage | Volume | Rate | Drop-off | Benchmark |
|-------|--------|------|----------|-----------|
| Sessions | {N} | 100% | — | — |
| Product Views | {N} | {%} | {%} | — |
| Add to Cart | {N} | {%} | {%} | 5-10% |
| Checkout | {N} | {%} | {%} | 40-60% of ATC |
| Purchase | {N} | {%} | {%} | 1-3% overall |

## Diagnosis
- Primary issue: {funnel stage} — {specific problem}
- Root cause: {analysis}

## Recommendations
1. {action targeting the diagnosed stage}
```

## Gotchas

- **Conversion rate is meaningless without traffic quality context**: A 5% conversion rate from email (high-intent) and 0.5% from display ads (low-intent) are both normal. Don't compare across channels.
- **GA4 sessions ≠ Universal Analytics sessions**: GA4 uses event-based model. Session timeout and attribution rules differ. Expect 5-15% discrepancy during migration.
- **Mobile conversion is always lower**: Mobile: 1-2%, Desktop: 3-5% is typical. Don't mix them in one number — analyze separately.
- **Seasonality matters**: Compare same period YoY, not just MoM. E-commerce has strong seasonal patterns (11.11, Christmas, Chinese New Year).
- **Revenue ≠ profit**: A 20% revenue increase from aggressive discounting may reduce profit. Track margin alongside revenue.

## References

- For GA4 setup guide, see `references/ga4-setup.md`
- For e-commerce benchmark data by industry, see `references/ecom-benchmarks.md`

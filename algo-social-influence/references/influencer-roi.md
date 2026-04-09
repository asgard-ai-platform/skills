# Influencer ROI Measurement Framework

ROI measurement bridges influence scores (what the skill computes) to business outcomes (what finance cares about). This document covers the formulas, attribution models, and decision table for evaluating whether an influencer campaign generated positive return.

---

## Core ROI Formula

```
ROI (%) = (Revenue Attributable − Campaign Cost) / Campaign Cost × 100
```

**Campaign Cost** includes:
- Influencer fee (flat fee, per-post, or affiliate commission)
- Content production (photographer, editor, if brand-supplied)
- Platform/tool costs (tracking links, discount codes, analytics)
- Internal labour (campaign manager hours × loaded rate)

**Revenue Attributable** depends on the attribution model chosen (see §Attribution Models below).

### Worked Example

| Item | Value |
|------|-------|
| Influencer flat fee | $3,500 |
| Content production | $500 |
| Tracking/analytics tools | $200 |
| Internal labour (10 hrs × $80) | $800 |
| **Total Campaign Cost** | **$5,000** |
| Tracked promo-code revenue | $9,200 |
| Estimated halo revenue (15% uplift) | $1,380 |
| **Total Attributable Revenue** | **$10,580** |

```
ROI = (10,580 − 5,000) / 5,000 × 100 = 111.6%
```

Break-even threshold: revenue must exceed $5,000. At $10,580 this campaign returned $2.12 per $1 spent.

---

## Attribution Models

High-influence score does NOT guarantee attributable revenue. Choose the model before the campaign, not after.

### Model 1: Last-Click (Promo Code / UTM Link)

Assign 100% credit to the influencer whose link or code closed the sale.

```
Attributable Revenue = Σ (orders using code "INFLUENCER_X")
```

**Strengths**: Simple, unambiguous, finance-friendly.  
**Weaknesses**: Undercounts — many buyers see the post, don't use the code, buy later. Typically captures 30–60% of true impact for mid-funnel influencers.

**When to use**: Performance campaigns with strong CTA (discount, limited offer). Micro-influencers with tight niches.

### Model 2: Multi-Touch Linear

Split credit equally across all touchpoints in the conversion path.

```
Credit per touchpoint = 1 / N (where N = total touchpoints before conversion)
```

Requires a CDP or analytics stack that stitches cross-channel journeys. Rarely achievable with a single influencer campaign in isolation.

**When to use**: You have cross-channel attribution infrastructure and multiple concurrent influencers.

### Model 3: Incremental Lift (A/B Geo Test)

Run the campaign in Region A, hold Region B as control. Measure sales delta.

```
Lift = (Conversion Rate_A − Conversion Rate_B) / Conversion Rate_B
Attributable Revenue = Baseline Revenue_A × Lift
```

**Strengths**: Most accurate. Isolates influencer effect from organic trends.  
**Weaknesses**: Requires regions of comparable baseline behaviour; adds operational complexity; minimum 2–4 week test window.

**When to use**: Large campaigns (>$20K spend), brand with strong baseline sales, TV-like upper-funnel influencers where promo codes are impractical.

### Model 4: Brand Search Uplift (Proxy)

Measure Google/platform branded search volume during and after campaign.

```
Search Lift % = (Search Volume_campaign − Baseline) / Baseline × 100
```

Correlate search lift with historical conversion rate from branded search to estimate revenue impact. Imprecise but available without codes or geo tests.

**When to use**: Awareness campaigns where no direct CTA exists.

---

## Cost-Per Metrics (Secondary KPIs)

When full revenue attribution is not feasible, cost-per metrics provide comparable signals across influencers.

| Metric | Formula | Benchmark (Instagram 2024) |
|--------|---------|---------------------------|
| CPE (Cost per Engagement) | Campaign Cost / Total Engagements | $0.10–$0.50 |
| CPV (Cost per Video View) | Campaign Cost / Views | $0.01–$0.05 |
| CPC (Cost per Click) | Campaign Cost / Link Clicks | $0.50–$3.00 |
| CPL (Cost per Lead) | Campaign Cost / Leads captured | $5–$25 |
| CPA (Cost per Acquisition) | Campaign Cost / Orders | $15–$80 |

**IRON LAW applies here**: An influencer with 1M followers and $0.02 CPE generated through bot engagement is worse than one with 50K followers and $0.08 CPE from genuine audience. Always cross-check CPE with authenticity score before declaring cost-efficiency.

Platform benchmarks shift yearly; treat these as order-of-magnitude sanity checks, not targets.

---

## Earned Media Value (EMV) — Use with Caution

EMV estimates what the influencer content would cost to buy as paid advertising.

```
EMV = Total Impressions × CPM_equivalent / 1000
```

Where `CPM_equivalent` = the platform's average paid CPM (e.g. Instagram ~$6–$10).

**The problem**: EMV is frequently inflated by agencies to justify spend because it ignores:
- Paid ads have targeting precision influencer posts do not
- Impressions ≠ attention ≠ conversion intent
- The CPM equivalent is often cherry-picked

EMV is acceptable as a **supplementary vanity metric** in executive reports. It must never substitute for actual revenue or cost-per attribution. Flag to the user if they are using EMV as their primary ROI signal.

---

## ROI Decision Table by Campaign Goal

| Campaign Goal | Recommended Attribution | Primary KPI | Minimum Acceptable |
|---------------|------------------------|-------------|-------------------|
| Direct sales (DTC) | Last-click (promo code) | CPA, ROI% | ROI > 0% (break-even), target >50% |
| Lead generation | UTM + form fill | CPL | CPL < $30 (B2C), < $80 (B2B) |
| App installs | Mobile MMP (Adjust, AppsFlyer) | CPI | CPI < category benchmark |
| Brand awareness | Search uplift + brand recall survey | CPV, Search Lift | Search Lift > 5% |
| Content seeding | Engagement + share rate | CPE | CPE < paid social CPE on same platform |

---

## Influence Score → ROI Adjustment Factor

The parent skill computes a composite influence score. That score can be used to adjust expected ROI before campaign launch (pre-campaign forecasting):

```
Expected CPA_adjusted = Baseline CPA / (Influence Score / 50)
```

Where 50 is the normalized midpoint of the influence score (0–100 scale).

**Worked example:**  
- Brand's baseline CPA via paid social: $45  
- Influencer A influence score: 82  
- Expected CPA: $45 / (82/50) = $45 / 1.64 = **$27.44**

- Influencer B influence score: 31  
- Expected CPA: $45 / (31/50) = $45 / 0.62 = **$72.58**

This is a rough heuristic, not a precise prediction. Validate against 2–3 historical campaigns with known CPA before using in budget planning. The adjustment factor should be recalibrated per category (fashion vs. SaaS behave differently).

---

## Temporal Tracking: When to Measure

Influencer-driven purchases are not instant. The measurement window matters.

| Channel Type | Measurement Window |
|-------------|-------------------|
| Story / ephemeral content | 24–48 hrs post-publish |
| Feed post (Instagram, LinkedIn) | 7 days post-publish |
| YouTube video | 30 days post-publish |
| Podcast mention | 60 days post-publish |
| Blog / long-form content | 90 days post-publish |

Keep promo codes and UTM links active for the full window. A common mistake is expiring codes after 7 days for a YouTube campaign and then concluding ROI was low.

---

## Post-Campaign Audit Checklist

Run this after every campaign before recording final ROI:

- [ ] Promo code / UTM revenue pulled for the correct attribution window
- [ ] Returns and refunds subtracted from revenue (gross ≠ net)
- [ ] Bot engagement flag: if authenticity score < 70, note inflation risk on engagement metrics
- [ ] Engagement pod flag: did >20% of comments come from the same recurring accounts?
- [ ] Cost reconciliation: influencer fee, all production costs, and platform costs included
- [ ] Benchmark comparison: how does this CPA/CPE compare to paid social for same audience?
- [ ] Qualitative log: any brand mentions, PR pickup, or UGC generated as secondary value?

---

## Influence Score Tier → Expected ROI Range

Empirical ranges from published industry studies (Influencer Marketing Hub 2023, Later 2024). Treat as rough priors, not guarantees.

| Influence Score Tier | Account Type | Typical ROI Range | Notes |
|---------------------|-------------|------------------|-------|
| 80–100 | Macro / celebrity | −20% to +80% | High variance; reach-heavy, engagement-light |
| 60–79 | Mid-tier (100K–1M) | +30% to +150% | Balanced reach/engagement |
| 40–59 | Micro (10K–100K) | +50% to +300% | High engagement, low awareness ceiling |
| 20–39 | Nano (<10K) | +20% to +200% | Very niche; works only if audience is exact match |

The wide ranges reflect that influence score explains ~30–40% of ROI variance; the remainder is driven by creative quality, offer strength, and audience-product fit — factors outside the algorithm's scope.

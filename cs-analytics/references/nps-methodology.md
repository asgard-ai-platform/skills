# NPS Methodology

## What NPS Measures (and What It Doesn't)

NPS captures **relationship loyalty** — how a customer feels about your brand *overall*, not about a single interaction. This is why the parent skill lists NPS as a strategic metric: it reflects accumulated experience across all touchpoints over time.

Do not use NPS to evaluate individual agent performance. Use CSAT for that.

---

## The Survey Question

**Standard wording (do not modify):**

> "How likely is it that you would recommend [Company/Product] to a friend or colleague?"

Response scale: **0 (Not at all likely) → 10 (Extremely likely)**

**Follow-up open text (always include):**

> "What is the most important reason for your score?"

The follow-text is where the diagnostic value lives. The number alone tells you *that* there's a problem; the text tells you *why*.

---

## Segmentation and Formula

| Score | Segment | Definition |
|-------|---------|------------|
| 9–10 | **Promoter** | Loyal enthusiasts who refer others |
| 7–8 | **Passive** | Satisfied but unenthusiastic; vulnerable to competitors |
| 0–6 | **Detractor** | Unhappy; at churn risk; may spread negative word-of-mouth |

```
NPS = % Promoters − % Detractors
```

Passives are excluded from the calculation entirely. Their scores still matter for trend analysis, but they don't move the NPS number.

**Worked example:**

100 responses:
- 45 scored 9–10 → Promoters = 45%
- 30 scored 7–8 → Passives = 30% (excluded)
- 25 scored 0–6 → Detractors = 25%

```
NPS = 45% − 25% = +20
```

NPS ranges from **−100** (everyone is a detractor) to **+100** (everyone is a promoter). A score of +20 is mediocre for most consumer sectors; see benchmarks below.

---

## Industry Benchmarks

| Industry | Median NPS | Top Quartile |
|----------|-----------|-------------|
| Software / SaaS | ~35 | > 50 |
| E-commerce | ~45 | > 60 |
| Telecom | ~20 | > 35 |
| Financial Services | ~30 | > 50 |
| Retail (general) | ~40 | > 60 |

Source: Satmetrix / Bain benchmarks (vary by year and sample; use as rough orientation, not hard targets).

**More useful than absolute NPS:** your own NPS trend over time, and relative NPS vs. direct competitors (competitive NPS benchmarking via survey panels).

---

## Survey Timing: Relationship vs. Transactional

Two distinct deployment models. Choose based on your goal.

### Relationship NPS

- Sent on a **calendar schedule** (e.g., quarterly), independent of any specific interaction
- Measures overall brand loyalty
- Typical sample: random sample of active customers
- Cadence: quarterly or semi-annually (more frequent = survey fatigue)

### Transactional NPS (tNPS)

- Triggered **after a specific event**: purchase, support resolution, onboarding
- Measures satisfaction with that event, with NPS framing
- Closer in spirit to CSAT; still uses 0–10 scale and promoter/detractor segmentation
- Useful when you want to track how specific touchpoints affect overall loyalty

**Decision rule:**

```
If goal = evaluate overall brand health         → Relationship NPS
If goal = evaluate a specific process/touchpoint → tNPS (or CSAT)
If goal = evaluate individual CS agent           → CSAT only
```

---

## Sample Design

### Minimum Sample Size

For a confidence interval of ±5 points at 95% confidence:

```
n ≈ (Z² × p × (1−p)) / E²

Where:
  Z = 1.96 (95% confidence)
  p = 0.5 (conservative assumption)
  E = 0.05 (±5% margin on each proportion)

n ≈ (3.84 × 0.25) / 0.0025 ≈ 384
```

In practice, use **n ≥ 400 responses** per segment you want to analyze independently. If you're segmenting by product line, region, or customer tier, you need 400 per segment — not 400 total.

### Response Rate Expectations

| Channel | Typical Response Rate |
|--------|----------------------|
| Email (transactional) | 10–30% |
| In-app prompt | 20–40% |
| SMS | 25–40% |
| Post-call IVR | 5–15% |

Plan your send volume accordingly. To get 400 responses via email, send to at least 1,300–4,000 customers.

### Avoiding Response Bias

- **Recency bias**: customers who just had an interaction will skew tNPS scores. For relationship NPS, exclude customers who contacted support in the last 7 days — or segment them separately.
- **Timing bias**: avoid sending surveys after billing cycles, known outages, or product launches unless that's what you're studying.
- **Churned customers**: NPS of active customers only captures survivors. Consider a separate exit survey for churned customers — often the most informative.

---

## Closed-Loop Process

NPS without follow-up action is just vanity data. The closed-loop process converts scores into retention actions.

```
Detractor (0–6)
  └── Trigger: alert CS team within 24h
  └── Action: outreach call or personal email
  └── Goal: understand root cause, attempt recovery
  └── Track: did they churn within 90 days?

Passive (7–8)
  └── Trigger: add to nurture campaign
  └── Action: proactive check-in, feature education
  └── Goal: convert to promoter
  └── Track: next survey score

Promoter (9–10)
  └── Trigger: thank-you message
  └── Action: referral program invitation, case study request
  └── Goal: activate referral behavior
  └── Track: referral conversion rate
```

**Inner loop vs. outer loop:**

| Loop | Focus | Owner | Frequency |
|------|-------|-------|-----------|
| Inner | Individual customer recovery (Detractor outreach) | CS team | Within 48h |
| Outer | Systemic issue fix (root cause elimination) | Product / Ops | Monthly review |

The outer loop is where NPS drives real improvement. If 30% of Detractors cite "long wait times," that's a signal for staffing or automation investment — not just individual apologies.

---

## Text Analysis on Open-Text Responses

The 0–10 score tells you the *magnitude*. The open text tells you the *cause*.

### Step 1: Segment Before Analyzing

Always analyze open text separately for:
- Detractors
- Passives  
- Promoters

What Promoters praise and what Detractors criticize are different signals; combining them produces noise.

### Step 2: Topic Extraction

**Simple approach (small teams, < 500 responses/month):**
1. Export open text to spreadsheet
2. Read Detractor responses manually; tag each with 1–2 topic labels
3. Tally tag frequency → Pareto of complaint drivers

**Scalable approach (> 500 responses/month):**
- Use TF-IDF or BERTopic to auto-cluster
- Or pass to an LLM with a structured prompt:

```
Prompt template:
"You are analyzing NPS Detractor comments. For each comment, assign:
1. Primary topic (one of: pricing, support_quality, product_bug, 
   wait_time, communication, other)
2. Sub-topic (free text, max 5 words)
3. Sentiment intensity (1=mild, 2=moderate, 3=severe)

Output as JSON array. Comment: {text}"
```

### Step 3: Root Cause Mapping

For the top 3 Detractor topics, trace back:
- Is this a process failure? (→ Ops)
- Is this a product failure? (→ Product)
- Is this a communication failure? (→ CS + Marketing)
- Is this an expectation mismatch? (→ Sales + Marketing)

---

## Tracking and Reporting

### Rolling Average vs. Point-in-Time

Single-period NPS is noisy. Use a **rolling 90-day NPS** for operational tracking:

```
Rolling NPS = NPS calculated over the past 90 days of responses
```

Report rolling NPS monthly; don't compare last month's NPS to last quarter's — compare rolling periods instead.

### Minimum Reporting Template

```
Period: {Q} or {Month}
Surveys sent: {N}
Responses: {N} ({response_rate}%)
NPS: {score}  (prior period: {score}, Δ {+/-})

Segment breakdown:
  Promoters: {N} ({%})
  Passives:  {N} ({%})
  Detractors:{N} ({%})

Top 3 Detractor themes:
  1. {theme}: {N} mentions ({%} of detractors)
  2. {theme}: {N} mentions
  3. {theme}: {N} mentions

Top 3 Promoter themes (what's working):
  1. {theme}: {N} mentions
  2. {theme}: {N} mentions
  3. {theme}: {N} mentions

Closed-loop: {N} Detractors contacted, {N} recovered (scored 7+ on follow-up)
```

---

## Common Mistakes

**Using NPS for agent-level evaluation.**
NPS reflects cumulative brand experience. An agent talking to a Detractor may be doing excellent work but can't overcome months of product frustration. Use CSAT for agent performance.

**Surveying too frequently.**
Monthly relationship NPS surveys burn out your customer base and inflate passive/detractor responses due to survey fatigue alone. Quarterly is the safe floor for relationship NPS.

**Ignoring the Passive segment.**
Passives are on the fence. A 7 is one bad experience away from becoming a Detractor. Track what Passives cite in open text — it often predicts your next NPS drop before it happens.

**Celebrating NPS without closing the loop.**
An NPS report that doesn't trigger action for Detractors within 48 hours is a missed retention opportunity. Every Detractor left uncontacted is a potential churn event.

**Treating NPS as statistically precise.**
An NPS of +32 vs. +35 is not a meaningful difference with n=400. Don't over-interpret small swings. Focus on directional trend over 3+ periods and qualitative themes.

**Conflating industry NPS benchmarks with internal targets.**
A SaaS company with an NPS of +40 might be lagging its competitor at +65. Always seek competitive benchmarks in your specific market segment, not just industry-wide averages.

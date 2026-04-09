# Survey Design for Van Westendorp PSM

## The Four Questions — Exact Wording

The wording matters. Small deviations change the distribution of responses. Use these canonical phrasings:

| Label | Question |
|-------|----------|
| Too Cheap (TC) | "At what price would you consider this product to be so cheap that you would doubt its quality?" |
| Cheap / Bargain (CH) | "At what price would you consider this product to be a bargain — a great buy for the money?" |
| Expensive (EX) | "At what price would you consider this product to be getting expensive, though you might still consider buying it?" |
| Too Expensive (TE) | "At what price would you consider this product to be so expensive that you would not consider buying it?" |

**Why exact wording matters:**
- "A bargain" vs "cheap" shifts the CH curve upward. If you use "cheap", respondents anchor lower.
- "Getting expensive" in the EX question must include the qualifier "though you might still consider it" — otherwise respondents conflate EX with TE, collapsing the range.
- Avoid "would you pay" framing. Use "would you consider" to reduce social desirability bias.

---

## Price Anchoring: The Biggest Threat to Data Quality

If respondents see any price before answering, their responses will cluster around that anchor. This systematically distorts all four curves.

**Rules:**
1. Do NOT show a price list or price range before the four questions.
2. Do NOT mention a competitor's price anywhere in the survey before the PSM section.
3. Do NOT include price-related questions (e.g., "How much do you currently pay for X?") before the PSM block.
4. If you must collect current spend data, put it AFTER the PSM questions.

**Acceptable pre-PSM content:** product concept description, feature list, usage scenarios, respondent screening questions. None of these should contain currency amounts.

---

## Price Input Format

Give respondents an open-ended text field for each question, not a slider or dropdown.

**Why not a slider or dropdown:**
- Sliders anchor to the midpoint. Respondents drag to a "plausible" position rather than stating a true perception.
- Dropdowns constrain to your tested range. If your range is wrong, you lose intersections.
- Open-ended fields produce the raw distribution needed for CDF construction.

**Acceptable constraint:** specify currency and unit clearly. Example:

> "Please enter a price in New Taiwan Dollars (NTD) per month."

**Data cleaning rule for open-ended responses:**
- Remove blank entries.
- Flag responses where TC ≥ TE (logically inconsistent). Investigate: if > 10% of responses are inconsistent, your concept description is unclear.
- Winsorize extreme outliers at the 2nd and 98th percentile before computing CDFs. Do not delete — winsorize.

---

## Sample Size

### Minimum: 100

The PSM intersection method relies on smooth cumulative distribution functions. Below 100 responses, curves are too jagged for reliable intersection detection. At n=100, intersections can shift ±15% with a single outlier.

### Recommended: 200–400

At n=200, the 95% confidence interval on each intersection point is approximately ±8–12% of the price value. At n=400, it narrows to ±5–7%.

**Formula for required n given a target margin of error on an intersection:**

The intersection is essentially a quantile estimate. For a CDF-based quantile at proportion p with desired margin of error ε (in price units), the required n is:

```
n ≥ (z² × p × (1-p)) / (ε / range)²
```

Where:
- `z` = 1.96 for 95% confidence
- `p` = 0.5 (conservative, used when true proportion is unknown)
- `ε` = desired margin of error in price units
- `range` = total price range tested

**Worked example:**
- Price range tested: $10–$100/month (range = $90)
- Desired margin of error on OPP: ±$5 (so ε/$range = 5/90 ≈ 0.056)
- n ≥ (3.84 × 0.25) / (0.056)² = 0.96 / 0.003136 ≈ 306

Round up: **n = 310** is the minimum for ±$5 precision on OPP.

### Segmentation multiplier

If you plan to analyze subgroups (e.g., SMB vs Enterprise, Taipei vs non-Taipei), each subgroup needs 100+ responses independently. Total sample = 100 × number of segments.

---

## Screener Design

Only include respondents who:
1. Are in your actual target market (role, industry, purchase authority)
2. Are familiar enough with the product category to price it meaningfully
3. Have not participated in a similar pricing survey in the past 6 months (to prevent learned responses)

### Screener question order

```
1. [Category familiarity] "How often do you [use/purchase] [product category]?"
   → Terminate if: Never / I'm not familiar with this
   
2. [Role/authority] "Which of the following best describes your role in purchasing decisions for [category]?"
   → Keep: Decision maker / Influencer / Regular buyer
   → Terminate: No involvement
   
3. [Recent survey] "Have you participated in a market research study about [category] pricing in the past 6 months?"
   → Terminate if: Yes
```

For B2B products: add company size and industry filters before the familiarity question.

---

## Concept Description

Respondents cannot price what they don't understand. The concept description must appear immediately before the four PSM questions.

**Length:** 100–200 words. Longer descriptions cause respondents to lose focus; shorter descriptions leave too much to imagination.

**Must include:**
- What the product does (function, not benefit language)
- Key features that differentiate it
- Who it is for
- Delivery format (physical, SaaS, service, etc.)

**Must NOT include:**
- Pricing signals ("priced comparably to X", "premium product")
- Emotional or aspirational language ("transform your business")
- Vague claims ("best-in-class", "enterprise-grade")

**Example (SaaS analytics tool):**

> *"This is a web-based analytics dashboard for e-commerce businesses. It connects to Shopify, WooCommerce, and Lazada via API and automatically calculates daily revenue, order count, average order value, and customer retention rate. Reports are updated every 4 hours. Access is browser-based with no installation required. It supports up to 5 user accounts per subscription and includes 12 months of historical data storage."*

This description names features, delivery mechanism, and constraints — without aspirational language or price signals.

---

## Question Order Within the Survey

Recommended sequence:

```
[Block 1] Screener questions
[Block 2] Product concept description (display, no questions)
[Block 3] Van Westendorp four questions (TC, CH, EX, TE)
[Block 4] Newton-Miller-Smith purchase intent (if using NMS extension)
[Block 5] Demographics / firmographics
[Block 6] Current spend / category spend (if needed)
[Block 7] Open-ended feedback (optional)
```

**Critical ordering rule:** Blocks 5–7 must come after Block 3. Any spend or demographic question that mentions money before Block 3 will anchor PSM responses.

**Within Block 3, question order:**

There is no consensus on whether question order within the PSM block affects results. Two schools:

1. **Canonical order** (TC → CH → EX → TE): respondents build a mental ladder from low to high. Most common in academic literature.
2. **Reverse order** (TE → EX → CH → TC): starts with the ceiling, may reduce anchoring from TC. Some practitioners prefer this for luxury products.

Default to canonical order (TC → CH → EX → TE) unless you have a specific reason to deviate.

---

## Price Range Selection for Open-Ended Collection

Even with open-ended fields, you need to define a cleaning range: prices outside a plausible range are likely typos or misunderstandings.

**Heuristic for range selection:**
- Lower bound: the price at which virtually no one would doubt quality (often ≈ 10% of current market price, or ≈ cost of a comparable commodity)
- Upper bound: the price at which virtually everyone would refuse to buy (often ≈ 3–5× the expected PME)

**Worked example:**

Competitor products range from $15–$40/month. Expected PME is around $50.

- Lower bound for cleaning: $3/month (below this, treat as data error)
- Upper bound for cleaning: $200/month (above this, treat as data error)

Document these bounds before collecting data. Apply them as cleaning rules, not survey constraints.

---

## Platform-Specific Implementation Notes

### Online survey tools (Typeform, SurveyMonkey, Qualtrics)

- Use numeric-only validation on PSM fields to prevent free-text like "$30/mo"
- Set minimum value = 0, no maximum (let cleaning handle outliers)
- Add soft validation: if TC > EX, prompt "Please double-check — you entered [TC] for 'too cheap' and [EX] for 'getting expensive'. Is this correct?" Do not force correction; just prompt.

### In-person / interviewer-administered

- Interviewer must NOT suggest a price if the respondent asks "what's a normal price?" — instruct interviewers to say "we're interested in your own perception, any number is fine."
- Record verbatim if respondent gives a range ("around $20–$30") — split to midpoint ($25) and flag as estimated.

### Panel recruitment

- Specify that the survey is about a product concept (not about the company or brand) to avoid brand-loyal respondents who price based on brand affinity rather than product value.
- For B2B: verify job titles against LinkedIn or company domain where possible. Self-reported titles in panels are noisy.

---

## Common Data Quality Failures and Fixes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| TC > TE for >10% of respondents | Concept description unclear; respondents didn't understand product | Rewrite concept description; re-field |
| All four responses within $5 of each other | Price anchoring occurred; or screener too narrow | Audit survey for pre-PSM price mentions |
| TC curve never crosses TE curve | Price range tested is too narrow | Extend range and re-field, or adjust cleaning bounds |
| IPP < OPP (inverted) | Small sample causing noisy CDFs; or legitimate market confusion | Increase n; review segment homogeneity |
| Flat curves with no clear intersection | Heterogeneous respondent pool | Segment by buyer type and run separate analyses |
| All responses cluster at round numbers ($10, $20, $50) | Psychological price clustering | Normal; apply no fix. Round-number clustering is real consumer behavior |

---

## Checklist Before Fielding

```
[ ] Concept description is 100–200 words, no price signals, no aspirational language
[ ] Four PSM questions use canonical wording (or documented deviation)
[ ] No price mentions or spend questions appear before Block 3
[ ] Open-ended numeric fields with soft consistency validation
[ ] Screener filters for category familiarity and purchase authority
[ ] Target n calculated for desired margin of error on OPP
[ ] Cleaning bounds documented (lower and upper price limits)
[ ] Subgroup sample sizes verified if segmentation is planned
[ ] Pilot test with 10–15 respondents before full launch
```

**Pilot test purpose:** Confirm that respondents understand the concept and that all four PSM responses are plausible (not all identical, not logically inconsistent at high rates). Fix concept description if >20% of pilot respondents give inconsistent responses (TC ≥ TE).

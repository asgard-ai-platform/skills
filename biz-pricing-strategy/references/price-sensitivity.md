# Price Sensitivity Analysis Methods

Three validated research methods for measuring customer willingness-to-pay before committing to a price point.

---

## Van Westendorp Price Sensitivity Meter (PSM)

### What It Measures

PSM identifies an **acceptable price range** and an **optimal price point** by asking customers four questions at four psychological thresholds.

### The Four Questions

Ask each respondent about your specific product:

1. **Too cheap** — "At what price would this product be so cheap that you'd question its quality?"
2. **Cheap/bargain** — "At what price would this be a bargain — great value for the money?"
3. **Expensive/getting pricey** — "At what price would this start to feel expensive, though you might still buy it?"
4. **Too expensive** — "At what price would this be too expensive — you definitely wouldn't buy it?"

### Analysis: The Four Cumulative Curves

Plot cumulative % of respondents at each price on the x-axis:

| Curve | Direction | Source Question |
|-------|-----------|----------------|
| **Too Cheap** | Ascending (L→R) | % who say price is ≤ their "too cheap" threshold |
| **Cheap** | Descending | % who say price is ≥ their "cheap/bargain" threshold |
| **Expensive** | Ascending | % who say price is ≥ their "expensive" threshold |
| **Too Expensive** | Descending | % who say price is ≤ their "too expensive" threshold |

### The Four Intersection Points

| Intersection | Name | Meaning |
|-------------|------|---------|
| Too Cheap ∩ Too Expensive | **Optimal Price Point (OPP)** | Fewest rejections from both ends |
| Cheap ∩ Expensive | **Indifference Price Point (IDP)** | "Normal" market price; 50% say cheap, 50% say expensive |
| Too Cheap ∩ Expensive | **Lower Acceptable Price (LAP)** | Bottom of acceptable range |
| Cheap ∩ Too Expensive | **Upper Acceptable Price (UAP)** | Top of acceptable range |

**Acceptable Price Range**: LAP to UAP  
**Target**: OPP if maximizing adoption; IDP if matching market perception

### Worked Example: SaaS project management tool for Taiwan SMBs

Survey of 80 respondents. After collecting all four thresholds per respondent, count cumulative % at each NT$ price point:

| Price (NT$/user/mo) | Too Cheap (↑) | Cheap (↓) | Expensive (↑) | Too Expensive (↓) |
|--------------------|--------------|----------|--------------|-----------------|
| 99  | 5%  | 98% | 4%  | 2%  |
| 149 | 15% | 90% | 9%  | 5%  |
| 199 | 30% | 78% | 18% | 10% |
| 249 | 44% | 62% | 35% | 18% |
| 299 | 55% | 48% | 52% | 30% |
| 349 | 65% | 35% | 67% | 44% |
| 399 | 75% | 22% | 80% | 58% |
| 449 | 84% | 12% | 90% | 72% |
| 499 | 91% | 6%  | 95% | 85% |

**Reading the intersections:**
- Too Cheap ∩ Too Expensive → ~NT$249 (OPP)
- Cheap ∩ Expensive → ~NT$295 (IDP)
- Too Cheap ∩ Expensive → ~NT$199 (LAP)
- Cheap ∩ Too Expensive → ~NT$365 (UAP)

**Interpretation**: The acceptable range is NT$199–NT$365. A price of NT$299 sits close to the IDP — customers perceive it as "normal market price." The OPP at NT$249 minimizes resistance but may sacrifice margin relative to what customers would pay.

**Decision**: The SKILL.md example chose NT$299 for the Pro tier — within range, above OPP, close to IDP. Consistent.

### Sample Size

| Use Case | Minimum n | Notes |
|----------|-----------|-------|
| Early validation | 30–50 | Direction only; curves will be noisy |
| Confident range | 100–150 | Standard for B2C products |
| Segment comparison | 150+ per segment | If comparing SMB vs enterprise, etc. |

### PSM Limitations

- Measures **stated preference**, not revealed preference (actual purchase behavior)
- Respondents imagine buying; real WTP is often lower
- Does not model volume — no demand curve output
- Less reliable for products respondents have never bought before

---

## Gabor-Granger Method

### What It Measures

Gabor-Granger builds a **demand curve** by measuring purchase intent at multiple price points. Output: estimated revenue-maximizing price.

### Protocol

Show each respondent a **single price** (or a descending sequence), then ask:

> "At NT$X per month, how likely would you be to subscribe?"  
> Scale: Definitely would / Probably would / Probably not / Definitely not

Assign binary purchase intent: "Definitely would" + "Probably would" = **buyer**

**Two design variants:**

| Variant | Method | Tradeoff |
|---------|--------|----------|
| **Between-subjects** | Each respondent sees one price | Cleaner; requires larger n (50+ per price point) |
| **Sequential descending** | Each respondent sees prices from high to low | Smaller n; risk of anchoring bias |

Sequential descending is standard; start 30–50% above your expected ceiling.

### Analysis: Demand Schedule

| Price (NT$/user/mo) | % "Would Buy" | Implied Demand Index |
|--------------------|--------------|---------------------|
| 499 | 18% | 18 |
| 399 | 31% | 31 |
| 299 | 52% | 52 |
| 249 | 64% | 64 |
| 199 | 78% | 78 |
| 149 | 87% | 87 |

### Revenue Index Calculation

```
Revenue Index = Price × % Would Buy
```

| Price | % Would Buy | Revenue Index |
|-------|------------|---------------|
| 499  | 18%  | 89.8  |
| 399  | 31%  | 123.7 |
| 299  | 52%  | **155.5** ← peak |
| 249  | 64%  | 159.4 ← also near peak |
| 199  | 78%  | 155.2 |
| 149  | 87%  | 129.6 |

**Revenue-maximizing price**: NT$249–NT$299 range. NT$299 is defensible given IRON LAW — it maintains premium positioning while staying near peak revenue.

### Price Elasticity from Gabor-Granger

```
Point Elasticity = (ΔQ / Q) / (ΔP / P)
```

Between NT$249 and NT$299:

```
ΔQ = (52% − 64%) / 64% = −18.75%
ΔP = (299 − 249) / 249 = +20.08%

Elasticity = −18.75% / 20.08% = −0.93
```

Elasticity of −0.93 means **inelastic** in this range — a 20% price increase reduces demand only 19%. This supports pricing at NT$299 over NT$249.

Between NT$399 and NT$499:

```
ΔQ = (18% − 31%) / 31% = −41.9%
ΔP = (499 − 399) / 399 = +25.1%

Elasticity = −41.9% / 25.1% = −1.67
```

Elasticity of −1.67 means **elastic** above NT$399 — demand drops faster than price rises. Avoid pricing above NT$399.

### Gabor-Granger Limitations

- **Hypothetical bias**: stated intent overestimates actual purchase 30–50% (rule of thumb: treat "Probably would" as only 50% likely)
- **No quality signal**: unlike PSM, does not capture "too cheap" concerns
- **Sequential anchoring**: in descending sequences, respondents who refuse NT$499 are primed to see NT$299 as reasonable

---

## A/B Price Testing (Revealed Preference)

### When to Use

Use when you have live traffic and can randomize price exposure. This is the only method measuring **actual willingness to pay** (not stated intent).

### Minimum Viable Setup

```
Control:   Price = NT$249, shown to 50% of eligible visitors
Treatment: Price = NT$299, shown to 50% of eligible visitors

Measure: Conversion rate (sign-ups / unique visitors)
Run duration: Until statistical significance (see below)
```

### Required Sample Size

For a two-sample proportion test:

```
n = 2 × (Z_α/2 + Z_β)² × p̄(1−p̄) / (p1−p2)²

Where:
  Z_α/2 = 1.96  (α = 0.05, two-tailed)
  Z_β   = 0.84  (power = 80%)
  p̄     = average conversion rate across both groups
  p1, p2 = expected conversion rates per group
```

**Example**: Baseline conversion 5%, expect NT$299 reduces it to 4%

```
p̄ = (5% + 4%) / 2 = 4.5%
(p1 − p2)² = (0.05 − 0.04)² = 0.0001

n = 2 × (1.96 + 0.84)² × 0.045 × 0.955 / 0.0001
n = 2 × 7.84 × 0.04298 / 0.0001
n ≈ 6,739 per group
```

You need ~6,700 visitors per variant — ~13,400 total — before reading results.

### Revenue per Visitor Comparison

Do not optimize for conversion rate alone. Compare **revenue per visitor**:

```
RPV = Price × Conversion Rate

Control:   NT$249 × 5.0% = NT$12.45 / visitor
Treatment: NT$299 × 4.2% = NT$12.56 / visitor  ← +0.9% RPV despite lower conversion
```

Even though conversion dropped, revenue per visitor is higher at NT$299. **This is the correct metric.**

### A/B Testing Pitfalls

- **Peeking**: checking results before reaching required n inflates false positive rate. Commit to the sample size before starting.
- **Segment leakage**: if the same customer sees both prices (different sessions, shared devices), results are contaminated. Use user-ID randomization, not session-ID.
- **Temporal confounds**: do not run over a promotional period, major holiday, or competitor campaign.
- **Legal / ethical exposure**: in some markets (EU consumer law, Taiwan Consumer Protection Act), showing different prices to different users for the same product requires disclosure. Confirm with legal before running.

---

## Choosing a Method

| Condition | Use |
|-----------|-----|
| Pre-launch, no live traffic | Van Westendorp + Gabor-Granger |
| Want demand curve + elasticity estimates | Gabor-Granger |
| Want acceptable price range and "too cheap" signal | Van Westendorp |
| Live traffic, can randomize | A/B test |
| Need to compare segments (SMB vs enterprise) | Gabor-Granger with split samples |
| High-stakes decision, budget available | All three in sequence |

**Sequencing when budget allows:**

1. **PSM** → find acceptable range and OPP (early concept stage)
2. **Gabor-Granger** → build demand curve within that range (pre-launch)
3. **A/B test** → validate with real transactions (post-launch)

Each method anchors the next: PSM narrows the range, Gabor-Granger identifies the revenue-optimal point, A/B test confirms with revealed behavior.

---

## Quick Reference: Formulas

```
Price Elasticity of Demand:
  E = (% change in quantity) / (% change in price)
  E < −1  → elastic   (price-sensitive; revenue falls when price rises)
  E > −1  → inelastic (price-insensitive; revenue rises when price rises)
  E = −1  → unit elastic (revenue unchanged)

Revenue Index (Gabor-Granger):
  RI = Price × Purchase Intent %

Revenue per Visitor (A/B):
  RPV = Price × Conversion Rate

Sample Size (A/B, two-proportion):
  n per group = 2(Z_α/2 + Z_β)² × p̄(1−p̄) / (p1−p2)²
  Shortcut: use n≈16,000 / (p1−p2)² for α=0.05, power=80%, p̄≈0.05
```

# Band Design

Salary bands translate market benchmark data into an internal pay structure. A band defines the acceptable pay range for a group of jobs: a minimum (floor), a midpoint (market anchor), and a maximum (ceiling).

---

## Anatomy of a Salary Band

```
Band:  |-------|----------|---------|
       Min    Mid        Max
       (P40)  (P50)      (P60–P75)
```

| Element | Definition | Typical Market Anchor |
|---------|-----------|----------------------|
| **Minimum** | Lowest defensible pay for a qualified new hire | P25–P40 |
| **Midpoint** | Target pay for a fully competent incumbent | P50 |
| **Maximum** | Ceiling beyond which pay requires regrading | P60–P75 |

The midpoint is the load-bearing element — it is pegged to the market P50 (or your chosen competitive position), then aged forward.

---

## Step 1: Choose Your Competitive Position

Before calculating anything, decide where you want to sit in the market:

| Strategy | Midpoint Target | Use When |
|----------|----------------|----------|
| Lag the market | P40 | Cost control, high non-cash benefits |
| Meet the market | P50 | Default; balanced cost vs. retention |
| Lead the market | P65–P75 | Talent-scarce roles, high-performance culture |

**Consistency rule:** Apply the same target percentile across all bands. If you lead for engineers (P65) but lag for operations (P40), document the business rationale explicitly — otherwise it looks like pay discrimination.

---

## Step 2: Set Band Midpoints

### Midpoint from Survey Data

```
Aged Market P50 = Survey P50 × (1 + annual_movement_rate) ^ (months_elapsed / 12)
```

**Worked example:**
- Survey P50 for "Software Engineer L3" = NT$1,800,000 (collected 2025-H1)
- Current date: 2026-04
- Elapsed: ~10 months
- Annual market movement rate (tech, Taiwan): 4%

```
Aged P50 = 1,800,000 × (1.04)^(10/12)
         = 1,800,000 × 1.0331
         = NT$1,859,580
```

Round to NT$1,860,000. That is your band midpoint if you target P50.

---

## Step 3: Calculate Band Width (Spread)

**Band spread** = `(Max - Min) / Midpoint`, expressed as a percentage.

Wider bands reward tenure and performance; narrower bands are easier to administer.

### Typical Spreads by Job Family

| Job Type | Recommended Spread | Min | Max |
|----------|--------------------|-----|-----|
| Hourly / operational | 40–50% | Mid × 0.80 | Mid × 1.20 |
| Professional IC | 50–60% | Mid × 0.75 | Mid × 1.25 |
| Senior IC / specialist | 60–80% | Mid × 0.70 | Mid × 1.30 |
| Manager / director | 70–90% | Mid × 0.65 | Mid × 1.35 |
| Executive | 100%+ | Negotiated | Negotiated |

### Formula

```
Band Min = Midpoint / (1 + spread/2)
Band Max = Midpoint × (1 + spread/2)
```

**Worked example** (60% spread, Mid = NT$1,860,000):

```
Band Min = 1,860,000 / (1 + 0.30) = 1,860,000 / 1.30 = NT$1,430,769 → round to NT$1,431,000
Band Max = 1,860,000 × (1 + 0.30) = 1,860,000 × 1.30 = NT$2,418,000
```

Final band: **NT$1,431,000 – NT$1,860,000 – NT$2,418,000**

---

## Step 4: Define the Number of Bands

### Two Common Structures

**Narrow banding** (many grades, small spreads):
- Pro: clear progression signal, easy to explain to employees
- Con: frequent re-grading creates administrative burden
- Use: manufacturing, large hierarchical orgs

**Broad banding** (few grades, wide spreads):
- Pro: flexible, reduces grade-inflation pressure
- Con: managers need stronger judgment; can mask inequity
- Use: flat tech companies, project-based orgs

### Decision Table

| Factor | Narrow Bands | Broad Bands |
|--------|-------------|-------------|
| Org size | > 500 employees | < 200 employees |
| Culture | Process-driven | Flat / autonomous |
| Job family diversity | Many distinct titles | Generalist roles |
| Manager calibration maturity | Low | High |

### Minimum bands for a typical org

A starting structure for a 50–200 person tech company:

| Band | Level | Scope |
|------|-------|-------|
| B1 | Junior / entry | Closely supervised, limited scope |
| B2 | Mid-level | Independent execution, bounded scope |
| B3 | Senior | Owns outcomes, mentors others |
| B4 | Staff / Lead | Cross-team impact, sets technical direction |
| B5 | Principal / Director | Org-wide or division-wide impact |
| B6 | VP / Executive | Strategic, P&L ownership |

---

## Step 5: Set Midpoint Progression Between Bands

**Midpoint progression** = `(Mid_n+1 - Mid_n) / Mid_n`

This controls how much pay increases as employees move up one band. Should be large enough to feel meaningful, small enough that bands still overlap.

### Overlap vs. No-Overlap

**Overlapping bands** (typical for professional roles):
```
B2: 1,100,000 – 1,430,000 – 1,859,000
B3: 1,430,000 – 1,860,000 – 2,418,000
```
The B2 max equals the B3 min — a high performer in B2 can earn as much as a new B3. This is intentional.

**Non-overlapping bands** (typical for hourly or structured hierarchies):
```
B1: 400,000 – 480,000 – 560,000
B2: 561,000 – 640,000 – 720,000
```
Promotion always produces a pay increase; no ambiguity.

### Recommended Progressions

| Role Type | Midpoint-to-Midpoint Progression |
|-----------|----------------------------------|
| Operational / hourly | 10–15% |
| Professional IC | 15–25% |
| Management track | 25–40% |
| Executive | 40%+ (often negotiated) |

**Consistency check:** If your band spread is 60% and your midpoint progression is only 10%, adjacent bands will overlap by more than 80% of their range — functionally meaningless. The rule of thumb:

```
Midpoint progression should be ≥ (spread / 2)
```

For a 60% spread → progression should be ≥ 30%.

---

## Step 6: Worked Full Example — 3-Band Engineering Structure

**Inputs:**
- Market survey source: Mercer Taiwan Tech 2025-H2
- Competitive target: P50
- Annual market movement: 4%
- Survey date: July 2025, current date: April 2026 (9 months elapsed)
- Aging factor: `(1.04)^(9/12)` = 1.0298

| Level | Survey P50 | Aged P50 (Midpoint) | Spread | Min | Max |
|-------|-----------|---------------------|--------|-----|-----|
| L2 (Mid) | 1,200,000 | 1,235,760 | 50% | 824,000 | 1,648,000 |
| L3 (Senior) | 1,800,000 | 1,853,640 | 60% | 1,426,000 | 2,410,000 |
| L4 (Staff) | 2,600,000 | 2,677,480 | 70% | 1,928,000 | 3,521,000 |

**Midpoint progressions:**
- L2 → L3: `(1,853,640 - 1,235,760) / 1,235,760` = **50%** ✓ (≥ spread/2 = 30%)
- L3 → L4: `(2,677,480 - 1,853,640) / 1,853,640` = **44%** ✓

**Overlap check (L2 max vs L3 min):** 1,648,000 > 1,426,000 → bands overlap by NT$222,000. This means a high-performing L2 at max can earn more than a new L3. Intentional and acceptable.

---

## Maintaining Bands Over Time

### Annual Market Adjustment

Each year, re-age midpoints using updated survey data:

```
New Midpoint = Old Midpoint × (1 + market_movement_rate)
```

If market moved 5% but you increased midpoints by only 3%, your compa-ratios will drift upward over time (employees appear to earn more relative to market) — a false signal.

### When to Restructure vs. Age

| Situation | Action |
|-----------|--------|
| Market moved 3–6% uniformly | Age all midpoints by the same factor |
| Specific role markets moved differently (e.g., AI engineers +20%) | Re-benchmark that job family; split the band if needed |
| Survey source changed | Re-match all jobs before aging; don't mix survey vintages |
| Org structure reorganized (new levels added/removed) | Full restructure required |

### Red Flag: Band Compression

Band compression occurs when the minimum creeps up (e.g., due to market pressure on new hire pay) but the midpoint and max are not raised proportionally. Signs:

- New hire pay ≥ P75 of current band
- Tenured employees' compa-ratios drop below 0.85 without explanation
- Internal pay inversion: junior role earns close to or above senior role

**Fix:** Raise the midpoint and max before raising the minimum. Raising only the floor is a short-term patch that stores up internal equity problems.

---

## Common Errors

| Error | Consequence | Fix |
|-------|-------------|-----|
| Setting bands from internal pay, not market data | Circular: bands reflect past decisions, not the market | Always anchor midpoint to market survey P50 |
| Equal band spreads across all levels | Senior roles with complex pay (equity, bonus) need wider bands | Widen spread as level increases |
| Using unadjusted survey data in year 2+ | Midpoints fall behind market; compa-ratios look inflated | Age data annually or re-survey |
| No overlap between adjacent bands | Promotion always feels forced; high performers leave | Allow 20–30% range overlap between consecutive bands |
| Rounding midpoints arbitrarily | Inconsistent band widths; employees notice round numbers and game them | Round to nearest 12,000–24,000 (one month's salary chunk) for cleanliness |

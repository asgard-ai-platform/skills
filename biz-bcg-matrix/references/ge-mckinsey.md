# GE-McKinsey Nine-Box Matrix

The GE-McKinsey Matrix replaces BCG's two single-metric axes with two **composite scores**, each built from multiple weighted factors. This trades BCG's simplicity for accuracy: a business unit can score high on industry attractiveness even in a slow-growth market (e.g., if the market is profitable, stable, and under-competitive). Use this framework when BCG's binary thresholds feel too crude for your portfolio.

---

## Structure

A 3×3 grid instead of BCG's 2×2:

| | **Strong Competitive Position** | **Medium** | **Weak Competitive Position** |
|---|---|---|---|
| **High Industry Attractiveness** | 🟢 Invest/Grow | 🟢 Invest/Grow | 🟡 Selectivity |
| **Medium** | 🟢 Invest/Grow | 🟡 Selectivity | 🔴 Harvest/Divest |
| **Low Industry Attractiveness** | 🟡 Selectivity | 🔴 Harvest/Divest | 🔴 Harvest/Divest |

**Three strategic zones:**
- 🟢 **Invest/Grow** (top-left 3 boxes): Commit resources aggressively
- 🟡 **Selectivity/Earnings** (diagonal 3 boxes): Invest only where you can win; otherwise manage for cash
- 🔴 **Harvest/Divest** (bottom-right 3 boxes): Minimize investment; exit if possible

---

## Scoring Methodology

### Step 1: Build the Industry Attractiveness Score

Select 4–7 factors. Assign each a weight (weights must sum to 1.0). Score each factor 1–5. Calculate weighted sum.

**Canonical factor list (pick what's relevant):**

| Factor | What to measure |
|--------|----------------|
| Market size | Total addressable market (USD) |
| Market growth rate | CAGR over 3–5 years |
| Profitability | Average industry margin |
| Competitive intensity | Number/strength of competitors (inverted: high competition = low score) |
| Cyclicality | Revenue volatility (inverted) |
| Regulatory environment | Barriers vs. opportunities |
| Technological change | Pace of disruption (context-dependent) |

**Formula:**

```
Industry Attractiveness Score =
  Σ (factor_weight_i × factor_score_i)   for i in selected factors
```

**Scoring anchor:**
- 5 = highly favorable (e.g., market growth >15%, few competitors, high margins)
- 3 = neutral/average
- 1 = highly unfavorable (e.g., declining market, commodity pricing, heavy regulation)

**Threshold to zone:**
- 3.67–5.0 → High
- 2.33–3.66 → Medium
- 1.0–2.32 → Low

---

### Step 2: Build the Competitive Strength Score

Same weighted-sum approach, different factors:

| Factor | What to measure |
|--------|----------------|
| **Relative market share** | Your share ÷ largest competitor's share (same as BCG — do NOT use absolute share) |
| Profit margin relative to competitors | Your margin vs. industry average |
| Brand strength | Customer loyalty, NPS, recognition |
| Production capacity / efficiency | Cost position vs. competitors |
| Technology position | Proprietary IP, R&D capability |
| Management quality | Track record, execution capability |

**Formula:**

```
Competitive Strength Score =
  Σ (factor_weight_i × factor_score_i)   for i in selected factors
```

Same 1–5 scale, same zone thresholds (3.67+ = Strong, 2.33–3.66 = Medium, <2.33 = Weak).

---

## Worked Example: Taiwanese Consumer Electronics Company

**Portfolio:** Same 4 units as the BCG example in SKILL.md (Laptop, Gaming peripherals, Server components, Feature phones).

### Industry Attractiveness Scoring

**Weights chosen:**

| Factor | Weight |
|--------|--------|
| Market growth rate | 0.30 |
| Profitability (industry avg margin) | 0.25 |
| Competitive intensity (inverted) | 0.20 |
| Market size | 0.15 |
| Regulatory environment | 0.10 |
| **Total** | **1.00** |

**Raw scores (1–5):**

| Factor | Laptop | Gaming | Server | Feature Phone |
|--------|--------|--------|--------|---------------|
| Market growth (3% / 18% / 12% / -2%) | 2 | 5 | 4 | 1 |
| Industry profitability | 3 | 4 | 5 | 2 |
| Competitive intensity (inverted) | 2 | 3 | 4 | 3 |
| Market size | 5 | 3 | 4 | 2 |
| Regulatory | 3 | 3 | 3 | 2 |

**Weighted scores:**

| Unit | Calculation | **IA Score** | Zone |
|------|-------------|--------------|------|
| Laptop | 2×.30 + 3×.25 + 2×.20 + 5×.15 + 3×.10 | **2.80** | Medium |
| Gaming | 5×.30 + 4×.25 + 3×.20 + 3×.15 + 3×.10 | **3.80** | High |
| Server | 4×.30 + 5×.25 + 4×.20 + 4×.15 + 3×.10 | **4.15** | High |
| Feature Phone | 1×.30 + 2×.25 + 3×.20 + 2×.15 + 2×.10 | **1.90** | Low |

### Competitive Strength Scoring

**Weights chosen:**

| Factor | Weight |
|--------|--------|
| Relative market share | 0.30 |
| Profit margin vs. competitors | 0.25 |
| Brand strength | 0.20 |
| Technology position | 0.15 |
| Production efficiency | 0.10 |
| **Total** | **1.00** |

**Raw scores:**

| Factor | Laptop | Gaming | Server | Feature Phone |
|--------|--------|--------|--------|---------------|
| Rel. market share (1.8x / 0.4x / 1.2x / 0.3x) | 5 | 2 | 4 | 1 |
| Margin vs. competitors | 4 | 2 | 4 | 2 |
| Brand strength | 4 | 2 | 3 | 2 |
| Technology position | 3 | 3 | 4 | 1 |
| Production efficiency | 4 | 3 | 3 | 2 |

**Weighted scores:**

| Unit | Calculation | **CS Score** | Zone |
|------|-------------|--------------|------|
| Laptop | 5×.30 + 4×.25 + 4×.20 + 3×.15 + 4×.10 | **4.10** | Strong |
| Gaming | 2×.30 + 2×.25 + 2×.20 + 3×.15 + 3×.10 | **2.30** | Weak |
| Server | 4×.30 + 4×.25 + 3×.20 + 4×.15 + 3×.10 | **3.70** | Strong |
| Feature Phone | 1×.30 + 2×.25 + 2×.20 + 1×.15 + 2×.10 | **1.60** | Weak |

### Final Placement

| Unit | IA Zone | CS Zone | Box Position | Strategy |
|------|---------|---------|--------------|----------|
| Laptop | Medium | Strong | 🟢 Invest/Grow | Maintain; milk selectively |
| Gaming | High | Weak | 🟡 Selectivity | Invest only if path to share gain is clear |
| Server | High | Strong | 🟢 Invest/Grow | Full investment — top priority |
| Feature Phone | Low | Weak | 🔴 Harvest/Divest | Exit |

**Contrast with BCG result:** Laptop was BCG Cash Cow (Low IA, Low-ish); GE-McKinsey places it in Invest/Grow because its competitive position is strong and the medium industry attractiveness still has upside. This matters: BCG would recommend milking laptops to fund Stars, but GE-McKinsey suggests defending the position more actively.

---

## BCG vs. GE-McKinsey: Decision Table

| Dimension | BCG | GE-McKinsey |
|-----------|-----|-------------|
| Axes | Market growth + Relative market share | Composite IA score + Composite CS score |
| Variables per axis | 1 | 4–7 |
| Grid size | 2×2 | 3×3 |
| Calibration effort | Low (2 data points per unit) | High (8–14 scored factors per unit) |
| Best for | Quick portfolio scan, data-light environments | Mature analysis, strategy presentations, large portfolios |
| Risk of misclassification | High in fragmented markets (arbitrary 1.0x and 10% thresholds) | Lower, but depends on weight quality |
| Subjectivity | Low | High (weights and scores require judgment) |

**When to prefer GE-McKinsey:**
- BCG's binary thresholds produce ambiguous or counterintuitive placements (e.g., a 0.95x share unit is "low" but is practically the market leader in a fragmented market)
- The portfolio includes B2B units where brand/tech matter more than raw share
- Presenting to a board that wants to see trade-off reasoning documented

**When to prefer BCG:**
- Data is limited or the analysis needs to be completed quickly
- Portfolio units operate in markets with a clear single dominant player (making relative share unambiguous)
- The audience needs an easily communicated framework

---

## Pitfalls Specific to GE-McKinsey

**Weight gaming:** Analysts unconsciously assign higher weights to factors where their preferred unit scores well. Freeze weights before scoring, or have a separate person assign weights.

**Factor collinearity:** "Market growth" and "market attractiveness" are not independent. Adding both inflates growth's contribution. Audit your factor list for overlap before scoring.

**Scores are not cardinal:** A 4 is not twice as good as a 2. The composite scores support ranking and zone assignment — they do not support statements like "Unit A is 40% stronger than Unit B."

**Relative market share still applies here:** The CS factor "relative market share" follows the same Iron Law as BCG: your share ÷ largest competitor's share. Do not swap in absolute share just because GE-McKinsey is a "multi-factor" model.

**Zone boundary sensitivity:** A unit scoring 3.65 on IA (Medium) vs. 3.68 (High) is not meaningfully different. Treat units near zone boundaries as ambiguous; note this explicitly and apply judgment rather than mechanically applying the boundary strategy.

---

## Output Template (GE-McKinsey Specific)

```markdown
## GE-McKinsey Analysis: {Portfolio}

### Scoring Weights

**Industry Attractiveness weights:**
| Factor | Weight | Rationale |
|--------|--------|-----------|
| ...    | 0.XX   | ...       |

**Competitive Strength weights:**
| Factor | Weight | Rationale |
|--------|--------|-----------|
| ...    | 0.XX   | ...       |

### Unit Scores

| Unit | IA Score | IA Zone | CS Score | CS Zone | Position |
|------|----------|---------|----------|---------|----------|
| ...  | X.XX     | H/M/L   | X.XX     | S/M/W   | Zone color |

### Strategic Recommendations by Zone

**🟢 Invest/Grow:** {units}
- {unit}: {specific investment action}

**🟡 Selectivity:** {units}
- {unit}: Invest if {condition}, otherwise manage for earnings

**🔴 Harvest/Divest:** {units}
- {unit}: {exit timeline or harvest approach}

### Boundary Cases
{Units near zone thresholds with ambiguous placement and how to handle}
```

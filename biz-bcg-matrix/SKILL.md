---
name: "biz-bcg-matrix"
description: "Apply BCG Growth-Share Matrix to analyze a product or business unit portfolio for resource allocation decisions. Use this skill when the user needs to prioritize investments across multiple products, decide which products to grow vs harvest vs divest, or evaluate a portfolio's balance — even if they say 'which products should we invest in' or 'portfolio strategy' without naming BCG."
metadata:
  category: "WP-13 商學院—策略"
  tags: ["business-strategy", "bcg-matrix", "portfolio-management"]
---

# BCG Growth-Share Matrix

## Overview

The BCG Matrix classifies products or business units into four quadrants based on market growth rate (Y-axis) and relative market share (X-axis). It guides resource allocation: where to invest, where to harvest cash, and what to divest.

## When to Use

**Trigger conditions:**
- User managing multiple products or business units and needs to prioritize
- User asks "which products should we invest in vs cut?"
- User needs a portfolio-level view of their business
- User mentions "cash cow", "star product", or "portfolio strategy"

**When NOT to use:**
- For single-product strategy → use SWOT or Blue Ocean
- For industry-level analysis → use Porter's Five Forces
- When detailed financial modeling is needed → use DCF or financial ratios

## Framework

```
IRON LAW: Relative Market Share, Not Absolute

The X-axis is RELATIVE market share = your share / largest competitor's share.
A company with 20% share in a market where the leader has 40% = 0.5x (Low).
A company with 20% share where the next largest has 10% = 2.0x (High).

NEVER use absolute market share. A 30% share means nothing without knowing
the leader's share.
```

```
IRON LAW: Plot THEN Strategize

Place ALL products/units on the matrix BEFORE deciding strategy.
Portfolio balance matters — a company with only Stars has a cash crisis
(Stars consume cash). A company with only Cash Cows has no growth pipeline.
```

### Step 1: Define the Portfolio Units

List all products, product lines, or business units to analyze. Each must be:
- A distinct unit with its own market and competitors
- Measurable in terms of revenue, market share, and market growth

### Step 2: Gather Data for Each Unit

For each unit, determine:
- **Market growth rate**: Annual growth rate of the total market (not your revenue growth). Typically, >10% = High growth.
- **Relative market share**: Your market share ÷ largest competitor's market share. >1.0x = High.

### Step 3: Plot on the Matrix

| | High Relative Market Share | Low Relative Market Share |
|---|---|---|
| **High Market Growth** | ⭐ **Stars** — High share in growing market. Generate revenue but consume cash to maintain position. | ❓ **Question Marks** — Low share in growing market. Need heavy investment to gain share, or divest. |
| **Low Market Growth** | 🐄 **Cash Cows** — High share in mature market. Generate surplus cash with low investment needed. | 🐕 **Dogs** — Low share in slow market. Minimal cash generation, limited potential. |

### Step 4: Determine Strategy per Quadrant

| Quadrant | Default Strategy | Nuance |
|----------|-----------------|--------|
| Stars | **Invest** to maintain/grow share | Will become Cash Cows as market matures |
| Cash Cows | **Harvest** — maximize cash extraction with minimal investment | Fund Stars and selected Question Marks |
| Question Marks | **Selective invest OR divest** — pick winners, cut losers | Most critical decision — not all can become Stars |
| Dogs | **Divest or reposition** | May keep if synergies with other units exist |

### Step 5: Assess Portfolio Balance

Check the overall portfolio health:
- **Healthy**: Mix of Cash Cows (funding) + Stars (growth) + 1-2 Question Marks (pipeline)
- **Unhealthy**: All Cash Cows (no growth), all Stars (cash drain), all Dogs (declining)

## Output Format

```markdown
# BCG Matrix Analysis: {Company/Portfolio}

## Portfolio Units

| Unit | Revenue | Market Growth | Rel. Market Share | Quadrant |
|------|---------|--------------|-------------------|----------|
| {Product A} | {$X} | {X%} | {X.Xx} | Star/Cash Cow/QM/Dog |

## BCG Matrix Placement

| | High Share (>1.0x) | Low Share (<1.0x) |
|---|---|---|
| **High Growth (>10%)** | ⭐ {list Stars} | ❓ {list Question Marks} |
| **Low Growth (<10%)** | 🐄 {list Cash Cows} | 🐕 {list Dogs} |

## Strategic Recommendations

### Stars — Invest
- {Product}: {specific investment recommendation}

### Cash Cows — Harvest
- {Product}: {how to maximize cash extraction}

### Question Marks — Decide
- {Product}: Invest / Divest — {rationale}

### Dogs — Divest/Reposition
- {Product}: {recommendation}

## Portfolio Health Assessment
{Overall balance evaluation and rebalancing recommendations}
```

## Examples

### Correct Application

**Scenario:** BCG for a Taiwanese electronics company with 4 product lines

| Unit | Market Growth | Rel. Share | Quadrant | Reasoning |
|------|-------------|-----------|----------|-----------|
| Laptop line | 3% | 1.8x (leader) | Cash Cow ✓ | Mature market, dominant position |
| Gaming peripherals | 18% | 0.4x | Question Mark ✓ | Fast-growing but small player |
| Server components | 12% | 1.2x | Star ✓ | Growing market, leading position |
| Feature phones | -2% | 0.3x | Dog ✓ | Declining market, minimal share |

**Strategy**: Harvest Laptop cash → fund Server (maintain Star) + selective invest in Gaming (Question Mark with potential). Divest Feature phones.

### Incorrect Application

**Scenario:** Same company

**What went wrong:**
- Used absolute market share (25%) instead of relative (25% / leader's 30% = 0.83x) → Would misclassify as High Share when it's actually Low. Violates Iron Law.
- Decided "invest in everything" without plotting first → No portfolio trade-off analysis. Violates Iron Law: plot then strategize.

## Gotchas

- **Market growth ≠ your revenue growth**: A product growing 20% in a market growing 25% is losing share. Use market growth rate, not company revenue growth.
- **Relative share threshold**: The 1.0x cutoff is a guideline. In fragmented markets with no clear leader, adjust the threshold. Document your reasoning.
- **BCG is a snapshot**: Markets evolve. Stars become Cash Cows, Question Marks become Dogs. Reassess annually.
- **BCG ignores synergies**: A "Dog" that provides key components to a "Star" may be worth keeping. Factor in cross-unit dependencies.
- **Not all Question Marks can be funded**: The hardest decision. Use additional criteria (market fit, team capability, strategic importance) to choose which to invest in.

## References

- For GE-McKinsey Matrix as an alternative (multi-factor version), see `references/ge-mckinsey.md`
- For comparison with other strategy frameworks, see `references/framework-comparison.md`

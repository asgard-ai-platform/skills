---
name: "biz-ansoff"
description: "Apply Ansoff Matrix to evaluate growth strategy options across market and product dimensions. Use this skill when the user needs to decide how to grow — through existing vs new markets and existing vs new products. Also use when the user asks 'how should we grow', 'should we launch a new product or expand to new markets', or 'what's our growth strategy'."
metadata:
  category: "WP-13 商學院—策略"
  tags: ["business-strategy", "ansoff-matrix", "growth-strategy"]
---

# Ansoff Matrix (Growth Strategy)

## Overview

The Ansoff Matrix maps four growth strategies along two axes: markets (existing vs new) and products (existing vs new). Each quadrant carries increasing risk — from market penetration (lowest) to diversification (highest). It forces a disciplined choice among growth paths.

## When to Use

**Trigger conditions:**
- User planning growth strategy for a business
- User deciding between launching new products vs entering new markets
- User evaluating the risk-reward of different expansion options
- User asks "how should we grow?" or "new product vs new market?"

**When NOT to use:**
- For portfolio-level decisions across multiple products → use BCG Matrix
- For competitive positioning → use SWOT or Porter's
- When the question is about defending position, not growing

## Framework

```
IRON LAW: Risk Increases Diagonally

Market Penetration (existing × existing) = lowest risk.
Diversification (new × new) = highest risk.
Product Development and Market Development are medium risk.

NEVER recommend diversification without explicitly acknowledging it carries
the highest risk and requires the most resources. Companies fail most often
when pursuing diversification without the capability to manage it.
```

### Step 1: Map the Four Quadrants

| | **Existing Products** | **New Products** |
|---|---|---|
| **Existing Markets** | **Market Penetration** — Sell more of what you have to current customers | **Product Development** — Create new products for current customers |
| **New Markets** | **Market Development** — Sell existing products to new customer segments or geographies | **Diversification** — New products for new markets (highest risk) |

### Step 2: Evaluate Each Strategy

For each quadrant, assess:

**Market Penetration** (lowest risk):
- Increase usage frequency, win competitor's customers, convert non-users
- Tactics: pricing, promotions, loyalty programs, distribution expansion

**Market Development** (medium risk):
- New geographies, new customer segments, new channels
- Requires understanding new market needs; product may need adaptation

**Product Development** (medium risk):
- New features, new product lines, next-generation products
- Requires R&D capability; risk of product-market fit failure

**Diversification** (highest risk):
- **Related**: Leveraging existing capabilities in new markets (e.g., Amazon from e-commerce to cloud)
- **Unrelated**: No connection to existing business (e.g., a steel company buying a hotel chain)

### Step 3: Assess Feasibility and Risk

For each viable strategy:
- **Resources required**: Capital, talent, time
- **Capability gap**: What the company lacks to execute
- **Risk level**: What happens if it fails? Is it survivable?
- **Time to revenue**: How long until the strategy generates returns

### Step 4: Recommend a Growth Path

Select 1-2 strategies and sequence them:
- Start with lower-risk strategies to build resources
- Use Market Penetration as a cash foundation
- Pursue higher-risk strategies only with sufficient resources and capabilities

## Output Format

```markdown
# Ansoff Growth Strategy: {Company}

## Current Position
- Current markets: ...
- Current products: ...
- Growth objective: ...

## Strategy Options

| Strategy | Description | Risk | Resources | Timeline |
|----------|------------|------|-----------|----------|
| Market Penetration | {specific tactic} | Low | {$X} | {months} |
| Market Development | {specific tactic} | Medium | {$X} | {months} |
| Product Development | {specific tactic} | Medium | {$X} | {months} |
| Diversification | {specific tactic} | High | {$X} | {months} |

## Recommended Growth Path
1. **Phase 1**: {strategy} — {why first}
2. **Phase 2**: {strategy} — {why second}

## Risk Mitigation
- {strategy}: {specific risk} → {mitigation}
```

## Examples

### Correct Application

**Scenario:** Ansoff for a Taiwanese hand-drip coffee chain with 30 stores in Taipei

| Strategy | Option | Risk Assessment |
|----------|--------|----------------|
| Market Penetration | Launch loyalty app + afternoon happy hour to increase visit frequency | Low risk ✓ — leverages existing stores and customers |
| Market Development | Expand to Taichung and Kaohsiung | Medium risk ✓ — same product, new geography with different consumer habits |
| Product Development | Launch bottled cold brew for convenience store distribution | Medium risk ✓ — new product format, requires manufacturing capability |
| Diversification | Open co-working spaces with coffee service | High risk ✓ — new product (workspace) + new market (remote workers) |

**Recommendation**: Phase 1: Market Penetration (loyalty app, 6 months). Phase 2: Market Development (Taichung pilot, 12 months). Defer diversification until cash reserves > NT$50M.

### Incorrect Application

**What went wrong:**
- Recommended diversification (co-working) as first priority without acknowledging it's highest risk → Violates Iron Law: must explicitly flag diversification risk.
- Listed only one quadrant ("let's just expand to new cities") → All four quadrants must be evaluated to make an informed choice.

## Gotchas

- **"New" is relative**: A product is "new" if the company hasn't sold it before, even if competitors have. New to the company, not new to the world.
- **Market Penetration is underrated**: Often the highest-ROI strategy because it leverages existing assets. Don't skip it just because it sounds boring.
- **Related diversification ≠ low risk**: Even related diversification has high failure rates. Amazon succeeded going from e-commerce to cloud; most companies don't.
- **Sequencing matters**: Strategies should be phased, not pursued simultaneously. Each phase funds and de-risks the next.
- **Missing the "why"**: Choosing a strategy without explaining why is incomplete. The Ansoff Matrix structures options; the reasoning behind the choice is what makes it actionable.

## References

- For comparison with other strategy frameworks, see `references/framework-comparison.md`

---
name: "biz-pricing-strategy"
description: "Analyze and design pricing strategies including cost-plus, value-based, competitive, penetration, and skimming approaches with psychological pricing techniques. Use this skill when the user needs to set or change prices, evaluate pricing models, understand price elasticity, or apply psychological pricing — even if they say 'how much should we charge', 'are we priced right', or 'our margins are too low'."
metadata:
  category: "WP-14 商學院—行銷"
  tags: ["marketing", "pricing", "revenue-strategy"]
---

# Pricing Strategy

## Overview

Pricing is the only marketing mix element that generates revenue — all others are costs. This skill covers five pricing approaches (cost-plus, value-based, competitive, penetration, skimming) plus psychological pricing techniques. The right approach depends on the product lifecycle stage, competitive landscape, and customer price sensitivity.

## When to Use

**Trigger conditions:**
- User setting prices for a new product
- User evaluating whether current pricing is optimal
- User asks "how much should we charge?" or "why are our margins low?"
- User needs to choose between pricing models (subscription vs one-time, freemium vs premium)

**When NOT to use:**
- For comprehensive financial analysis → use financial ratios or DCF
- For customer segmentation → use STP
- For cost structure analysis → use Value Chain

## Framework

```
IRON LAW: Price Communicates Positioning

Price is not just economics — it's a signal. Lowering price to compete
can permanently reposition a brand as "cheap." Raising price without
value justification creates distrust.

Every price change must be evaluated through BOTH a financial lens
(margins, volume) AND a positioning lens (what does this price say about us?).
```

### Step 1: Understand the Three Price Anchors

Every pricing decision sits between three constraints:

| Anchor | What It Sets | Method |
|--------|-------------|--------|
| **Cost floor** | Minimum viable price | Cost analysis — below this, you lose money |
| **Competitor reference** | Market expectations | Competitive benchmarking — what alternatives cost |
| **Customer ceiling** | Maximum willingness to pay | Value research — what the customer thinks it's worth |

### Step 2: Choose a Pricing Approach

| Approach | How It Works | Best When |
|----------|-------------|-----------|
| **Cost-Plus** | Cost + fixed margin % | Commodity products, government contracts, stable costs |
| **Value-Based** | Price based on customer's perceived value | Differentiated products, strong brand, measurable customer benefit |
| **Competitive** | Match or undercut competitor prices | Undifferentiated market, price-sensitive customers |
| **Penetration** | Start low to gain market share, raise later | New market entry, network effects, high switching costs |
| **Skimming** | Start high, lower over time | Innovation leader, early adopters willing to pay premium |

### Step 3: Apply Psychological Pricing Techniques

| Technique | How It Works | Example |
|-----------|-------------|---------|
| **Charm pricing** | End in 9 or 99 | NT$299 instead of NT$300 |
| **Anchoring** | Show a higher price first, then the actual price | "Was NT$1,200, now NT$799" |
| **Decoy effect** | Offer three options where the middle is the intended choice | Small NT$99, Medium NT$149, Large NT$159 (Large looks like a deal) |
| **Bundle pricing** | Combine products at a discount vs individual purchase | "All 3 for NT$999" (vs NT$450 each) |
| **Freemium** | Free basic tier, charge for premium features | Spotify, Notion, Canva |

### Step 4: Validate with Price Sensitivity Analysis

Before committing:
- **Van Westendorp**: Survey-based method — ask customers "at what price is this too expensive / too cheap / a bargain / getting expensive?"
- **Gabor-Granger**: Show a price, ask if they'd buy. Vary the price across respondents.
- **A/B test**: If possible, test two price points with real transactions

### Step 5: Monitor and Adjust

After launch:
- Track **price elasticity**: % change in demand / % change in price
- Monitor **competitive response**: Did competitors match your price?
- Watch **customer perception**: Did the price signal what you intended?

## Output Format

```markdown
# Pricing Strategy: {Product/Service}

## Three Anchors
- Cost floor: {$X} (based on: {cost breakdown})
- Competitor reference: {$X range} (competitors: {list})
- Customer ceiling: {$X} (based on: {value metric})

## Recommended Approach
**{Approach name}** — {rationale}

## Price Point
- Recommended price: {$X}
- Expected margin: {X%}
- Positioning signal: {what this price says about the brand}

## Psychological Techniques Applied
- {technique}: {how applied}

## Sensitivity Analysis
| Price Point | Est. Volume | Revenue | Margin | Risk |
|------------|------------|---------|--------|------|
| {low} | {high vol} | {$X} | {X%} | {positioning risk} |
| {recommended} | {med vol} | {$X} | {X%} | {balanced} |
| {high} | {low vol} | {$X} | {X%} | {volume risk} |

## Monitoring Plan
- Review frequency: {monthly/quarterly}
- Key metrics: {elasticity, competitive response, perception}
```

## Examples

### Correct Application

**Scenario:** Pricing a new SaaS project management tool for SMBs in Taiwan

**Three anchors:**
- Cost floor: NT$150/user/month (server + support costs)
- Competitors: Asana NT$350/user, Monday.com NT$300/user, Trello Free-NT$170/user
- Customer ceiling: NT$400/user (based on 30 customer interviews — value of time saved)

**Approach**: Value-based with decoy pricing
- Basic: NT$199/user/month (limited features — the decoy)
- Pro: NT$299/user/month (full features — the target)
- Enterprise: NT$499/user/month (with SSO, audit logs — anchor)

**Why**: Pro at NT$299 looks like great value vs Enterprise at NT$499, and much better than Basic at NT$199 for only NT$100 more.

### Incorrect Application

**What went wrong:**
- Set price at cost + 20% (NT$180/user) without checking competitor reference or customer ceiling → Left NT$120+/user of value on the table. Customer would have paid NT$299.
- Cut price from NT$299 to NT$149 to match a new budget competitor → Signaled "we're a budget tool now," causing premium customers to leave. Violates Iron Law: price communicates positioning.

## Gotchas

- **Cost-plus is a fallback, not a strategy**: Cost-plus only makes sense when you can't measure value or differentiate. In most cases, value-based pricing captures more margin.
- **Penetration pricing requires a plan to raise prices**: If you start low, you need a clear path to profitability. "We'll raise prices later" without a mechanism (switching costs, network effects) is wishful thinking.
- **Discounts are addictive**: Frequent discounts train customers to wait for sales. Use selectively and time-limit them.
- **B2B vs B2C psychology differs**: B2B buyers evaluate ROI rationally (though with organizational politics). B2C buyers are more susceptible to psychological pricing. Calibrate techniques to the buyer.
- **Free is not a price — it's a category change**: Moving from paid to free (or vice versa) changes the product category in the customer's mind. The shift from "paid product" to "free with ads" is a complete repositioning.

## References

- For Van Westendorp and Gabor-Granger methodology details, see `references/price-sensitivity.md`
- For SaaS-specific pricing models, see `references/saas-pricing.md`

# Pricing Strategies

Pricing strategy determines not just revenue, but what your product *means* to the customer. The parent skill's Iron Law applies here: price must be internally consistent with Product, Place, and Promotion. This document expands on the five named strategies in the skill and gives you the tools to select and implement one.

---

## Strategy Selection: Decision Framework

Choose your pricing strategy before setting the number. The decision depends on three variables:

| Question | Answer → Strategy |
|---|---|
| Do you have a defensible cost advantage? | Yes → Cost-Plus as floor; possibly Competitive |
| Is your product differentiated with measurable customer value? | Yes → Value-Based |
| Is market share more important than margin at launch? | Yes → Penetration |
| Are early adopters price-insensitive and you expect price to fall? | Yes → Skimming |
| Are you a commodity in a mature market? | Yes → Competitive |

**Typical mapping by market context:**

```
New category / no price reference points    → Skimming or Value-Based
High-competition commodity market           → Competitive (+ Cost-Plus floor)
Launch requiring rapid adoption             → Penetration
Premium / differentiated product            → Value-Based
Internal cost recovery (B2G, nonprofit)     → Cost-Plus
```

---

## 1. Cost-Plus Pricing

### Formula

```
Selling Price = Unit Cost × (1 + Markup %)
```

Or equivalently, targeting a margin:

```
Selling Price = Unit Cost / (1 − Target Margin %)
```

Note: **markup** is computed on cost; **margin** is computed on price. They are not interchangeable.

| Target Margin | Equivalent Markup |
|---|---|
| 20% | 25% |
| 33% | 50% |
| 50% | 100% |
| 60% | 150% |

### Worked Example

A bottled tea manufacturer:

```
Variable cost per bottle:
  Raw material (tea leaves, water):   NT$8
  Packaging (glass bottle, label):    NT$6
  Processing & filling:               NT$4
  Subtotal variable:                  NT$18

Fixed cost allocation per bottle:
  Factory overhead (÷ 100,000 units): NT$5
  Total unit cost:                    NT$23

Target margin: 35%
Selling Price = NT$23 / (1 − 0.35) = NT$35.38 → rounded to NT$35
```

**Problem with stopping here:** NT$35 is what it costs to produce profitably. It says nothing about whether the customer will pay it, or whether NT$35 signals the right positioning.

### When Cost-Plus Is Appropriate

- Setting the **price floor** (never price below this without a strategic reason)
- Government contracts, cost-plus service agreements
- Internal transfer pricing

### When Cost-Plus Fails

Cost-plus anchors to your costs, not to customer value. If your costs are high, you price yourself out. If your costs are low, you leave margin on the table. Use cost-plus only to establish a floor — not as the final price for a differentiated product.

---

## 2. Value-Based Pricing

Value-based pricing sets price based on the **economic value delivered to the customer**, not on your costs. It requires understanding what the customer gains (or saves) by using your product.

### Framework: Economic Value Estimation (EVE)

```
Value-Based Price = Reference Value + Differentiation Value

Reference Value    = Price of the next-best alternative
Differentiation Value = Quantified benefit above the reference product
                       (positive) or cost imposed vs. reference (negative)
```

### Worked Example: SaaS Inventory Tool for SME Retailers

**Situation:** A SaaS startup selling inventory management software to Taiwanese small retailers (annual revenue ~NT$5M). They are competing against Excel + manual tracking.

**Step 1 — Identify the reference product and its price**

```
Reference: Excel + 4 hours/week of manual inventory work
Reference cost: 4 hr/week × 52 weeks × NT$200/hr (staff cost) = NT$41,600/year
```

**Step 2 — Quantify differentiation value**

```
Benefit 1: Reduces stockouts
  Current stockout loss: estimated 3% of revenue = NT$150,000/year
  Tool reduces stockouts by 60%: saves NT$90,000/year

Benefit 2: Eliminates manual tracking time
  Saves 3.5 hr/week → NT$36,400/year

Benefit 3: Faster reorder decisions
  Reduces overstock holding cost by 1.5% of inventory value
  Average inventory = NT$500,000 → saves NT$7,500/year

Total quantified benefit: NT$90,000 + NT$36,400 + NT$7,500 = NT$133,900/year
```

**Step 3 — Calculate value-based price ceiling**

```
Value ceiling = Reference cost + Differentiation value
              = NT$41,600 + NT$133,900 = NT$175,500/year
```

This is the theoretical maximum. At this price, the customer breaks even vs. alternatives. You must share some value with the customer to make adoption worthwhile.

**Step 4 — Set price to capture a share of the value**

```
Typical value-share: capture 20-30% of differentiation value
Target price range: NT$41,600 + (NT$133,900 × 20-30%)
                  = NT$41,600 + NT$26,780 to NT$40,170
                  = NT$68,380 to NT$81,770/year
                  → NT$6,000–6,800/month
```

This gives the customer NT$93,730–107,120/year in net savings — a clear ROI argument for sales.

### Price Sensitivity Modifiers

Value-based price must also account for segment characteristics:

| Factor | Effect on willingness to pay |
|---|---|
| Customer can measure ROI clearly | Higher WTP |
| Switching cost from current solution is high | Lower WTP (adoption friction) |
| Product saves time (visible) vs. saves money (invisible) | Time savings: lower WTP; money savings: higher WTP |
| B2B with budget cycle | WTP follows budget availability, not just value |
| Risk of new vendor (SME buyer) | Reduce price or offer trial to lower perceived risk |

### Limitations

EVE requires customer research. If you cannot quantify the differentiation value, you are guessing. Do customer interviews before setting a value-based price. A common failure: using internal estimates of value instead of customer-reported willingness to pay.

---

## 3. Competitive Pricing

Set price relative to competitors rather than to your own costs or customer value. Used when the product is comparable to alternatives and switching cost is low.

### Three Positions

```
Price Leader (below market)  → Price at −10% to −20% of competitors
Price Parity (at market)     → Match the market rate
Price Follower (above market) → Premium tier; requires perceived differentiation
```

### Implementation: Competitive Price Benchmarking

1. **Map competitors** — identify 3–5 direct competitors selling to the same segment
2. **Collect price points** — actual transaction prices, not list prices (watch for discounts, bundles, subscription vs. one-time)
3. **Calculate market average** — simple or weighted by market share
4. **Decide position** — where do you want to sit relative to market?
5. **Set price** — and make sure Product and Place are consistent with the position

### Worked Example: Convenience Store Ready Meals

Market survey of 250ml soup cups at 7-ELEVEN competitors:

```
FamilyMart own-brand soup:  NT$39
Uni-President (shelf):       NT$35
Hi-Life store brand:         NT$38
Market average:              NT$37.3
```

Decision matrix:

| If Product is... | Appropriate price position |
|---|---|
| Identical quality, no brand recognition | Parity (NT$37) or Price Leader (NT$32–35) |
| Slightly better quality, some differentiation | Parity to +10% (NT$37–41) |
| Premium ingredients, branded | +20-30% above market (NT$45–48) |
| Private label cost-down | −15-20% below market (NT$30–32) |

### Competitive Pricing Failure Mode

Matching competitor prices without matching their cost structure leads to margin destruction. Before pricing at parity, verify your cost structure supports it.

```
If competitor's COGS = NT$20 at NT$37 price → 46% margin
If your COGS = NT$28 at NT$37 price → 24% margin

Same price, very different business outcomes.
```

---

## 4. Penetration Pricing

Price below sustainable long-run levels to acquire market share, build usage habits, or establish network effects. The intent is to move price up later.

### When It Works

- Market is price-sensitive (high price elasticity)
- Network effects: more users → more value (messaging apps, marketplaces)
- Category creation: educating a market on a new behavior
- High switching costs once adopted (lock-in after trial)

### When It Fails

- Target segment is price-insensitive (you are leaving money on the table)
- Competitors can match your price and out-survive you on margins
- Price increase after adoption triggers churn (customers don't value it enough to pay more)
- Signals low quality in markets where price = quality signal (violates Iron Law)

### The Penetration Math

Model the trade-off explicitly:

```
Penetration price:   NT$X (below sustainable margin)
Sustainable price:   NT$Y (target after adoption)
Payback horizon:     n months

Monthly loss per customer vs. sustainable price: NT$(Y - X)
Expected LTV at sustainable price: NT$Y × average retention months

Break-even: NT$(Y - X) × n = NT$Y × (average retention months − n)
```

**Example: Food delivery app subscription**

```
Penetration price: NT$0/month (free for 3 months)
Sustainable price: NT$99/month
Monthly subsidy per user: NT$99

Retention assumption: 18 months average at paid price
Subsidy cost: NT$99 × 3 = NT$297 per user

Revenue recovered: NT$99 × 15 remaining months = NT$1,485 per user
ROI: NT$1,485 / NT$297 = 5× return on subsidy — justified

But if average paid retention = 4 months:
Revenue recovered: NT$99 × 1 month = NT$99 per user (3 months free, churn at month 4)
ROI: NT$99 / NT$297 = 0.33× — not justified
```

The penetration decision is a customer retention bet. Model the retention assumption explicitly; don't assume it.

---

## 5. Price Skimming

Launch at a high price, then reduce over time as the market matures and competition increases. Extracts maximum willingness to pay from early adopters before moving down-market.

### When It Works

- Product is genuinely novel with no direct substitutes at launch
- Early adopters have substantially higher willingness to pay than the mass market
- Product cost declines over time (technology learning curve)
- Brand can maintain premium perception through the price reduction cycle

### Classic Skimming Curve

```
Time →
Price: NT$5,000 → NT$3,500 → NT$2,500 → NT$1,800 → NT$1,200

Segment captured:
  Month 1-6:   Enthusiasts / early adopters (top 5% WTP)
  Month 7-18:  Early majority (next 20% WTP)
  Month 19-36: Mass market
  Month 37+:   Late majority / budget segment
```

### Skimming Requires Segmented Demand

Skimming only works if the demand curve is not flat — meaning different customers genuinely have different willingness to pay. If your market is homogeneous, skimming at launch just loses you sales you could have captured.

```
Demand curve test:
  If surveyed WTP clusters tightly (e.g., 70% of target says NT$25-35):
    → Flat demand → Competitive or Value-Based pricing, not skimming

  If WTP spreads widely (e.g., 15% says NT$80+, 30% says NT$40-60, 40% says NT$20-35):
    → Tiered demand → Skimming candidate
```

### Price Reduction Triggers

Pre-commit to price reduction triggers before launch, or you will face internal pressure to hold price too long:

| Trigger | Action |
|---|---|
| Competitor launches comparable product | Reduce to close the gap |
| Sales velocity drops below target for 2+ consecutive months | Reduce by 15-20% |
| Early adopter segment saturated (penetration >80% of that segment) | Move to next price tier |
| Manufacturing cost drops by >20% | Consider passing 50% of savings to market |

---

## Price Signals and the Iron Law

Price communicates positioning independently of your intent. Before finalizing price, test it against the Iron Law:

### Signal Calibration Table

| Price tier (relative to market) | Signal to customer | Consistent Product/Place |
|---|---|---|
| >50% above market | Ultra-premium / exclusive | Needs exclusive distribution, premium packaging, brand story |
| 20-50% above market | Premium quality | Selective distribution, above-average presentation |
| Within ±10% of market | Comparable quality | Standard channels acceptable |
| 10-30% below market | Value / budget | Mass distribution, functional packaging |
| >30% below market | Lowest cost | Requires cost leadership in operations; risks quality perception |

### Price Consistency Checklist

Before finalizing:

```
□ Does price reflect the quality level of the Product?
□ Does price match the image of the Place (channel) where it's sold?
□ Does price match the tone of Promotion (aspirational vs. deal-focused)?
□ Can the cost structure support this price at scale?
□ Does price position us where we want to be vs. competitors?
□ If this is a service, does price match the People and Physical Evidence quality?
```

A single "No" is a signal that one of the other Ps needs adjustment, not necessarily the price.

---

## Psychological Pricing Mechanics

These are tactical adjustments applied after the strategy is set — not a strategy in themselves.

| Technique | Mechanism | Use case |
|---|---|---|
| Charm pricing (NT$99 vs NT$100) | Left-digit anchoring reduces perceived price | Mass market, impulse purchase |
| Prestige pricing (round numbers: NT$500, NT$1,000) | Signals quality; avoids "cheap" associations | Premium products |
| Price anchoring (show higher price first) | Reference point inflates perceived value of target price | E-commerce, tiered plans |
| Bundle pricing | Obscures per-unit price; increases total transaction value | Software, subscriptions, food sets |
| Decoy pricing (add a 3rd option to make target option look better) | Middle option captures most customers | SaaS plans, menu design |

**Decoy example:**

```
Without decoy:
  Basic:    NT$299/mo  (30% choose)
  Premium:  NT$599/mo  (70% choose)

With decoy:
  Basic:    NT$299/mo  (20% choose)
  Standard: NT$549/mo  ← decoy (5% choose — overpriced for its value)
  Premium:  NT$599/mo  (75% choose — looks like great value vs. Standard)
```

The decoy is not meant to sell. It reframes the Premium tier as a near-equivalent to a bad deal, making Premium feel like the rational choice.

---

## Quick Reference: Strategy Comparison

| | Cost-Plus | Value-Based | Competitive | Penetration | Skimming |
|---|---|---|---|---|---|
| Basis | Internal cost | Customer value | Market prices | Market share goal | WTP segmentation |
| Best for | Floor setting, commodities | Differentiated products | Mature markets | New market entry | Innovative products |
| Margin | Predictable | High potential | Compressed | Negative at launch | High early, falls |
| Risk | Leaves money on table | Requires customer research | Race to bottom | Churn if price rises | Competitors move in |
| Consistency check | Margin sustainable? | Value quantified? | Cost structure matches? | Retention model solid? | Demand curve tiered? |

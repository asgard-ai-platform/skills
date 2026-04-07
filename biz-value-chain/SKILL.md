---
name: "biz-value-chain"
description: "Apply Porter's Value Chain Analysis to identify competitive advantage sources within an organization's activities. Use this skill when the user needs to find where value is created or lost in their operations, analyze cost structure by activity, optimize internal processes, or identify outsourcing candidates — even if they say 'where do we make money' or 'which activities should we keep in-house'."
metadata:
  category: "WP-13 商學院—策略"
  tags: ["business-strategy", "value-chain", "operations"]
---

# Value Chain Analysis

## Overview

Value Chain Analysis decomposes an organization into strategically relevant activities to understand where competitive advantage originates. Each activity either adds value (customer willingness to pay) or adds cost. The gap between total value created and total cost is the margin.

## When to Use

**Trigger conditions:**
- User wants to understand which activities drive competitive advantage
- User analyzing cost structure to find savings
- User deciding what to keep in-house vs outsource
- User asks "where do we create value?" or "why are our margins low?"

**When NOT to use:**
- For industry-level analysis → use Porter's Five Forces
- For product portfolio decisions → use BCG Matrix
- For macro-environment scanning → use PESTEL

## Framework

```
IRON LAW: Primary + Support Activities Are a Complete Set

Analyze ALL nine categories. Skipping support activities (like HR or
technology development) misses critical advantage sources. Amazon's
competitive advantage comes more from Technology Development (support)
than from any single primary activity.
```

### Step 1: Map Primary Activities

Primary activities directly create and deliver value to the customer:

1. **Inbound Logistics** — Receiving, storing, distributing inputs (warehouse, inventory, supplier scheduling)
2. **Operations** — Transforming inputs into the final product (manufacturing, assembly, packaging, testing)
3. **Outbound Logistics** — Collecting, storing, distributing product to buyers (delivery, order fulfillment)
4. **Marketing & Sales** — Informing buyers about the product and enabling purchase (advertising, pricing, channel management)
5. **Service** — Maintaining and enhancing product value after sale (installation, repair, training, support)

### Step 2: Map Support Activities

Support activities enable and improve primary activities:

6. **Firm Infrastructure** — General management, planning, finance, accounting, legal, government affairs
7. **Human Resource Management** — Recruiting, hiring, training, compensation, culture
8. **Technology Development** — R&D, product design, process improvement, IT systems
9. **Procurement** — Purchasing inputs, negotiating with suppliers, managing vendor relationships

### Step 3: Assess Each Activity

For each of the 9 activities, evaluate:
- **Value contribution**: How much does this activity contribute to what the customer is willing to pay?
- **Cost**: What percentage of total cost does this activity represent?
- **Competitive comparison**: Is this activity performed better, same, or worse than competitors?
- **Linkage**: Does this activity critically enable or depend on another activity?

### Step 4: Identify Advantage Sources

Competitive advantage comes from:
- **Cost advantage**: Performing activities at lower cost than competitors
- **Differentiation advantage**: Performing activities in a way that increases buyer willingness to pay
- **Linkage advantage**: Coordinating between activities better than competitors (e.g., tight integration between Operations and Outbound Logistics)

### Step 5: Formulate Recommendations

For each activity:
- **Strengthen** if it's an advantage source
- **Optimize** if it's a cost center with improvement potential
- **Outsource** if competitors or specialists do it better and it's not an advantage source
- **Invest** if it's a support activity that could unlock advantage in primary activities

## Output Format

```markdown
# Value Chain Analysis: {Company}

## Primary Activities

| Activity | Key Processes | Value Contribution | Cost % | vs Competitors |
|----------|-------------|-------------------|--------|----------------|
| Inbound Logistics | {processes} | High/Med/Low | X% | Better/Same/Worse |
| Operations | ... | ... | ... | ... |
| Outbound Logistics | ... | ... | ... | ... |
| Marketing & Sales | ... | ... | ... | ... |
| Service | ... | ... | ... | ... |

## Support Activities

| Activity | Key Processes | Value Contribution | Cost % | vs Competitors |
|----------|-------------|-------------------|--------|----------------|
| Infrastructure | {processes} | High/Med/Low | X% | Better/Same/Worse |
| HR Management | ... | ... | ... | ... |
| Technology Dev | ... | ... | ... | ... |
| Procurement | ... | ... | ... | ... |

## Advantage Sources
- **Cost advantage in**: {activities}
- **Differentiation advantage in**: {activities}
- **Key linkages**: {activity A ↔ activity B}

## Recommendations
1. **Strengthen**: {activity} — {why and how}
2. **Optimize**: {activity} — {specific improvement}
3. **Outsource**: {activity} — {rationale}
```

## Examples

### Correct Application

**Scenario:** Value Chain for a Taiwanese direct-to-consumer (DTC) skincare brand

| Activity | Advantage? | Analysis |
|----------|-----------|----------|
| Inbound Logistics | Same | Standard ingredient sourcing from OEM suppliers |
| Operations | **Differentiation** ✓ | Proprietary formulation process co-developed with dermatologists |
| Outbound Logistics | Same | Standard logistics via 黑貓/宅配通 |
| Marketing & Sales | **Differentiation** ✓ | Strong KOL relationships and community-driven content on social media |
| Service | Same | Standard customer service |
| Technology Dev | **Differentiation** ✓ | Data-driven product development using customer feedback loops |
| Procurement | Cost advantage ✓ | Long-term contracts with local ingredient suppliers at volume discounts |

**Key linkage**: Technology Development ↔ Marketing & Sales — customer data from social media directly feeds product R&D.

### Incorrect Application

**What went wrong:**
- Only analyzed Operations and Marketing, skipped other 7 activities → Missed that Procurement was a key cost advantage source. Violates Iron Law: complete set required.
- Listed "brand reputation" as a primary activity → Brand reputation is an outcome, not an activity. Activities are verbs (procure, manufacture, deliver), not nouns.

## Gotchas

- **Activities are verbs, not assets**: "Strong brand" is not an activity. "Investing in KOL partnerships to build brand awareness" is a Marketing & Sales activity.
- **Support activities are often the hidden advantage**: Many companies' real competitive edge is in Technology Development, HR, or Procurement — not the primary activities. Don't treat support as overhead.
- **Linkages are where magic happens**: The connection between activities often matters more than individual activities. ZARA's advantage is the linkage between Design (Technology Dev) → Manufacturing (Operations) → Store delivery (Outbound Logistics) — not any single activity alone.
- **Service company adaptation**: For service businesses, "Operations" = service delivery, "Outbound Logistics" may not apply. Adapt the framework to fit the business model.

## References

- For comparison with other strategy frameworks, see `references/framework-comparison.md`

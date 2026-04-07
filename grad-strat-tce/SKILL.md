---
name: "grad-strat-tce"
description: "Apply Transaction Cost Economics (Williamson, 1975, 1985) to analyze governance structure choices — market, hybrid, or hierarchy — based on transaction characteristics. Use this skill when the user needs to decide make-or-buy, evaluate outsourcing vs vertical integration, design governance mechanisms for inter-firm relationships, or when they ask 'should we build this in-house or outsource', 'why do firms vertically integrate', or 'how should we structure this partnership'."
metadata:
  category: "WP-23 策略管理理論"
  tags: ["strategy", "transaction-cost-economics", "Williamson", "governance", "make-or-buy", "vertical-integration"]
---

# Transaction Cost Economics (TCE)

## Overview

TCE explains firm boundaries by analyzing the costs of conducting transactions. Williamson (1975, 1985) argues that governance structures (market, hybrid, hierarchy) are chosen to minimize the sum of production costs and transaction costs, given bounded rationality and opportunism.

## When to Use

- Make-or-buy decisions
- Evaluating outsourcing, alliances, or vertical integration
- Designing contractual safeguards for inter-firm transactions
- Analyzing why certain industries are more vertically integrated

## Assumptions

```
IRON LAW: Governance choice depends on transaction characteristics
(asset specificity, uncertainty, frequency) — NOT on firm preference,
tradition, or ideology. A misaligned governance structure will
generate avoidable costs and eventual correction.
```

Key assumptions:
1. **Bounded rationality** — Agents intend rationality but achieve it limitedly
2. **Opportunism** — Some agents will pursue self-interest with guile
3. Transactions vary in their characteristics and thus require different governance

## Methodology

### Transaction Characteristics

| Dimension | Low | High |
|-----------|-----|------|
| **Asset Specificity** | Generic assets, easy redeployment | Dedicated/specialized assets, lock-in risk |
| **Uncertainty** | Predictable outcomes, easy contracting | Unpredictable, incomplete contracts |
| **Frequency** | One-off or rare | Recurrent transactions |

### Asset Specificity Types
- Site specificity (location)
- Physical asset specificity (specialized equipment)
- Human asset specificity (specialized knowledge)
- Dedicated assets (investment for specific buyer)
- Brand name capital
- Temporal specificity (timing matters)

### Governance Selection Framework

1. **Assess asset specificity** — The primary discriminating variable
2. **Assess uncertainty** — Degree of environmental and behavioral unpredictability
3. **Assess frequency** — How often the transaction recurs
4. **Map to governance:**
   - Low specificity + low uncertainty → **Market** (price mechanism)
   - Moderate specificity → **Hybrid** (contracts, alliances, JVs)
   - High specificity + high uncertainty → **Hierarchy** (vertical integration)
5. **Evaluate safeguards** — Hostages, credible commitments, monitoring

## Output Format

```markdown
## TCE Governance Analysis: [Context]

### Transaction Profile
| Dimension | Assessment | Evidence |
|-----------|-----------|----------|
| Asset Specificity | [low/moderate/high] — [type] | ... |
| Uncertainty | [low/moderate/high] | ... |
| Frequency | [low/moderate/high] | ... |

### Governance Recommendation
- Recommended structure: [market/hybrid/hierarchy]
- Rationale: ...
- Required safeguards: ...

### Risk of Misalignment
- Current governance: [structure]
- Predicted inefficiency: ...
```

## Examples

### Good Example
A chip manufacturer assesses outsourcing a custom fabrication process: high physical asset specificity (dedicated equipment), high uncertainty (rapid tech change), high frequency — TCE prescribes hierarchy (in-house fabrication) with clear reasoning per dimension.

### Bad Example
Recommending outsourcing "because it's cheaper" without assessing asset specificity or opportunism risk. TCE requires evaluating transaction characteristics, not just spot-price comparisons.

## Gotchas

- Asset specificity is the most important variable — always assess it first
- TCE assumes opportunism as a possibility, not a certainty; but governance must protect against it
- Hybrid governance has many forms (franchising, JVs, long-term contracts) — specify which
- TCE is comparative, not absolute — compare governance alternatives, don't evaluate in isolation
- Neglecting behavioral assumptions (bounded rationality, opportunism) misapplies the framework

## References

- Williamson, O. (1975). *Markets and Hierarchies*. Free Press.
- Williamson, O. (1985). *The Economic Institutions of Capitalism*. Free Press.
- Williamson, O. (1991). Comparative economic organization. *Administrative Science Quarterly*, 36(2), 269-296.

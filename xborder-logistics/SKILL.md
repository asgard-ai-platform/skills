---
name: "xborder-logistics"
description: "Design cross-border logistics strategies including direct mail, overseas warehousing, and bonded warehouse models for international e-commerce. Use this skill when the user needs to ship products internationally, choose a logistics model for cross-border sales, optimize shipping costs, or set up fulfillment in a foreign market — even if they say 'ship to Southeast Asia', 'overseas warehouse vs direct shipping', 'customs clearance', or 'reduce international shipping time'."
metadata:
  category: "WP-07 跨境電商"
  tags: ["cross-border", "logistics", "fulfillment", "international"]
---

# Cross-Border Logistics

## Framework

```
IRON LAW: Return Logistics Costs 3-5× More Than Outbound — Budget for It or Die

Agents plan outbound shipping costs but systematically ignore returns.
Cross-border return rates run 15-30% for apparel, and each return costs
3-5× the outbound shipment (reverse customs, restocking, re-export duties,
currency loss). If your margin can't absorb a 20% return rate at 4× cost,
the overseas warehouse model is a cash trap regardless of forward volume.
Calculate the break-even return rate BEFORE committing to a fulfillment model.
```

### Three Logistics Models

| Model | How It Works | Delivery Time | Cost per Order | Min. Volume | Best For |
|-------|-------------|-------------|---------------|------------|----------|
| **Direct Mail (直郵)** | Ship each order from Taiwan to customer | 7-21 days | High ($8-25) | 1 order | Testing market, low volume, high-value items |
| **Overseas Warehouse (海外倉)** | Pre-stock inventory in destination country, ship locally | 1-5 days | Low ($2-5 local) + warehousing | 100+ units/month | Proven demand, competitive delivery needed |
| **Bonded Warehouse (保稅倉)** | Store in bonded zone, clear customs per-order | 3-7 days | Medium ($5-10) | 50+ units/month | Duty deferral, uncertain demand |

### Decision Framework

```
Monthly orders to one country < 50 → Direct Mail
Monthly orders 50-500 → Consider Bonded Warehouse
Monthly orders > 500 → Overseas Warehouse justified
```

### Customs & Duties Considerations

| Factor | What to Know |
|--------|-------------|
| **De minimis threshold** | Below this value, no import duty (varies: $75 in most SEA, $400 in US) |
| **HS Code** | Product classification code determines duty rate. Get this RIGHT — wrong HS code = penalties |
| **Landed cost** | Product cost + shipping + insurance + duties + taxes = what customer actually pays |
| **Documentation** | Commercial invoice, packing list, certificate of origin, product-specific certificates |
| **Restricted items** | Food, cosmetics, electronics, medical devices often need import permits |

### Fulfillment Partner Types

| Type | Service | Cost | Control |
|------|---------|------|---------|
| **3PL (e.g., ShipBob, Boxme)** | Full service: storage, pick-pack, ship | $$-$$$ | Low (outsourced) |
| **Marketplace fulfillment (Shopee/Lazada warehouse)** | Platform handles logistics | Commission-included | Very low |
| **Self-operated warehouse** | Your own warehouse + staff | $$$$ upfront | Full |
| **Drop-shipping** | Supplier ships directly | Lowest | None |

### Implementation Steps

**Phase 1: Direct Mail (Market Testing)**
1. Partner with international courier (DHL, FedEx, SF Express)
2. Research destination country customs requirements
3. Prepare documentation templates
4. Test with first 50 orders

**Phase 2: Transition to Overseas Warehouse (Scaling)**
5. Select 3PL or marketplace fulfillment in target market
6. Ship initial inventory batch
7. Integrate order management: your system → warehouse WMS
8. Monitor: fill rate, delivery time, return rate

**Phase 3: Optimize**
9. Analyze SKU-level demand to optimize pre-stocking
10. Negotiate volume rates with logistics partners
11. Evaluate bonded warehouse for duty optimization

## Output Format

```markdown
# Cross-Border Logistics Plan: {Product} → {Destination}

## Current State
- Monthly orders: {N}
- Current model: {direct mail / none}
- Avg delivery time: {days}

## Recommended Model
- Model: {Direct Mail / Bonded / Overseas Warehouse}
- Rationale: {volume, speed requirement, cost}

## Cost Comparison
| Model | Per-Order Cost | Monthly Fixed | Total (at {N} orders) |
|-------|---------------|-------------|---------------------|
| Direct Mail | ${X} | $0 | ${X} |
| Overseas Warehouse | ${X} | ${X} | ${X} |

## Implementation Plan
| Phase | Action | Timeline |
|-------|--------|----------|
| 1 | {step} | {weeks} |
```

## Gotchas

- **Returns are the hidden cost**: Cross-border returns are expensive and logistically complex. Build return rate assumptions (5-15% for e-commerce) into your cost model. Offer local returns if using overseas warehouse.
- **Customs delays are unpredictable**: Allow buffer in delivery estimates. "7-14 business days" is more honest than "7 days" for direct mail.
- **Product compliance varies by country**: Electronics need local certification (e.g., SIRIM in Malaysia, NCC in Taiwan). Food products need import permits. Check BEFORE shipping.
- **Currency and duty changes**: Exchange rates and duty rates change. Build 5-10% margin buffer into landed cost calculations.
- **Inventory risk in overseas warehouse**: Pre-stocked inventory that doesn't sell ties up capital and may become obsolete. Start with proven bestsellers only.

## References

- For country-specific customs requirements, see `references/customs-by-country.md`
- For 3PL provider comparison, see `references/3pl-comparison.md`

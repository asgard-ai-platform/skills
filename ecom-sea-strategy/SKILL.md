---
name: "ecom-sea-strategy"
description: "Develop e-commerce strategy for Southeast Asian markets including platform selection, payment infrastructure, logistics challenges, and localization requirements. Use this skill when the user is expanding e-commerce to SEA, evaluating Shopee vs Lazada vs Tokopedia, or needs to understand SEA market differences — even if they say 'sell to Southeast Asia', 'which platform in Vietnam', 'SEA payment methods', or 'cross-border e-commerce in ASEAN'."
metadata:
  category: "WP-01 電商"
  tags: ["e-commerce", "southeast-asia", "cross-border", "localization"]
---

# Southeast Asia E-Commerce Strategy

## Framework

```
IRON LAW: SEA Is Not One Market — It's 10+ Different Markets

Indonesia, Vietnam, Thailand, Philippines, Malaysia, and Singapore have
different languages, payment preferences, logistics infrastructure, and
consumer behaviors. A strategy that works in Singapore (high digital
maturity, English-speaking) will fail in Indonesia (cash-heavy, Bahasa,
island logistics). Analyze each country individually.
```

### Market Overview (Top 6)

| Country | Pop. | E-com Penetration | Top Platform | Dominant Payment | Key Challenge |
|---------|------|------------------|-------------|-----------------|---------------|
| Indonesia | 278M | ~35% | Tokopedia/Shopee | Bank transfer, e-wallets (GoPay, OVO) | Island logistics, last-mile cost |
| Vietnam | 100M | ~30% | Shopee | COD (~60%), e-wallets (MoMo) | COD returns high (~15-20%) |
| Thailand | 72M | ~40% | Shopee/Lazada | Bank transfer (PromptPay), COD | Fragmented social commerce |
| Philippines | 115M | ~25% | Shopee/Lazada | GCash, COD | Island logistics, low trust in online |
| Malaysia | 33M | ~45% | Shopee | FPX bank transfer, e-wallets | Small market, competitive |
| Singapore | 6M | ~55% | Shopee/Lazada/Amazon | Credit cards, PayNow | Tiny market, high CAC |

### Platform Strategy Decision

| Factor | Marketplace (Shopee/Lazada) | Own D2C Site | Social Commerce (IG/LINE/TikTok) |
|--------|---------------------------|-------------|--------------------------------|
| Traffic | Built-in | Must generate yourself | Organic but unpredictable |
| Commission | 3-15% + ads | 0% + payment/hosting costs | 0% + fulfillment |
| Data ownership | Platform owns | You own | Partial |
| Brand control | Limited | Full | Medium |
| Best for | Market entry, volume | Brand building, repeat customers | Viral products, low-trust markets |

### Entry Strategy Steps

**Phase 1: Market Selection** (pick ONE country first)
- Evaluate: market size, competition, regulatory ease, cultural proximity, logistics readiness
- For Taiwan sellers: Malaysia (Chinese-speaking segment) or Singapore (English, low friction) are lowest-barrier entries

**Phase 2: Platform Setup**
- Register on dominant marketplace
- Localize: language, product descriptions, sizing, imagery
- Set up local payment acceptance
- Arrange logistics (marketplace fulfillment or 3PL)

**Phase 3: Localization**
- Translate + culturally adapt (not just translate)
- Local customer service (language, timezone)
- Price in local currency, competitive with local sellers
- Adapt product for local preferences (sizing, flavors, packaging)

**Phase 4: Scale**
- Add D2C site once brand awareness exists
- Expand to second country using learnings from first
- Build local inventory/warehouse when volume justifies

## Output Format

```markdown
# SEA E-Commerce Strategy: {Brand/Product}

## Market Selection
| Country | Opportunity | Competition | Barriers | Score |
|---------|-----------|-------------|---------|-------|
| {country} | H/M/L | H/M/L | H/M/L | {total} |

## Recommended Entry: {Country}
- Platform: {which marketplace}
- Payment: {accepted methods}
- Logistics: {fulfillment approach}
- Timeline: {phases with milestones}

## Localization Requirements
{Language, pricing, cultural adaptations needed}

## Budget Estimate
| Item | Cost | Notes |
|------|------|-------|
| Platform setup | ${X} | ... |
| Inventory | ${X} | ... |
| Marketing (first 3 months) | ${X} | ... |
```

## Gotchas

- **COD dominance in Vietnam/Philippines**: Cash on delivery = high return rates (15-20%). Budget for returns and build COD surcharge into pricing.
- **Social commerce is massive in Thailand**: LINE, Instagram, and TikTok Live are primary shopping channels for many Thai consumers. Don't ignore social-first strategy.
- **Regulatory differences**: Indonesia requires local entity for certain categories. Vietnam has foreign investment restrictions. Check before committing.
- **Shopee vs Lazada market share shifts**: Platform dominance changes. Currently Shopee leads in most markets, but verify current data before committing exclusively.
- **Taiwan-SEA logistics**: Direct shipping from Taiwan is slow and expensive. Use marketplace fulfillment centers or local 3PL warehouses for competitive delivery times.

## References

- For country-specific e-commerce regulations, see `references/sea-regulations.md`
- For platform fee comparison, see `references/platform-fees.md`

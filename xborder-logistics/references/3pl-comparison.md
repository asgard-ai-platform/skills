# 3PL Provider Comparison — Cross-Border Fulfillment

This document supports the logistics model selection step in the overseas warehouse phase. It covers how to evaluate, compare, and score 3PL providers for Taiwan-origin cross-border sellers targeting SEA and US markets.

---

## Who This Is For

You have already decided an overseas warehouse model is justified (>500 monthly orders per country, or 50-500 with bonded warehouse consideration). Now you need to pick a specific 3PL partner.

---

## Cost Components You Must Compare Apples-to-Apples

Every 3PL quotes differently. Normalize to **total cost per shipped order** before comparing.

```
Total 3PL Cost per Order =
  Receiving fee (per unit, one-time)
+ Storage fee (per CBM or cubic foot × days stored)
+ Pick & pack fee (per order + per item)
+ Outbound shipping (carrier rate negotiated by 3PL)
+ Returns handling (per return, if applicable)
+ Account/platform fee (monthly, amortized over order volume)
```

### Worked Example

Scenario: 800 orders/month to Malaysia, average order = 2 items, product size = 0.002 CBM/unit, avg days in storage = 20.

| Component | Rate | Calculation | Monthly Cost |
|-----------|------|-------------|-------------|
| Receiving | $0.30/unit | 1,600 units × $0.30 | $480 |
| Storage | $18/CBM/month | (1,600 × 0.002 CBM) × (20/30) × $18 | $384 |
| Pick & pack | $1.50/order + $0.20/item | 800 × ($1.50 + 2×$0.20) | $1,520 |
| Outbound shipping | $3.50/order (local last-mile) | 800 × $3.50 | $2,800 |
| Returns | $3.00/return, ~8% rate | 64 × $3.00 | $192 |
| Platform fee | $200/month | flat | $200 |
| **Total** | | | **$5,576** |
| **Per order** | | $5,576 / 800 | **$6.97** |

Compare this against direct mail at $14/order → overseas warehouse saves $7.03/order → break-even analysis below.

---

## Break-Even Formula

Before committing to overseas warehouse + 3PL, calculate the break-even volume:

```
Fixed monthly 3PL cost = Storage + Platform fee + Receiving (amortized)
Variable savings per order = Direct mail cost − (3PL pick-pack + local shipping)

Break-even orders/month = Fixed monthly cost ÷ Variable savings per order
```

Using the example above:
- Fixed monthly = $480 + $200 + $384 = $1,064
- Variable savings = $14.00 − ($1.50 + 0.40 + $3.50) = $8.60/order
- Break-even = $1,064 ÷ $8.60 = **124 orders/month**

At 800 orders/month, you are well past break-even. At 100 orders, you would not yet be.

---

## Provider Comparison: SEA Markets

These are the most commonly used options for Taiwan sellers shipping into Southeast Asia.

### Boxme (boxme.asia)

**Coverage**: Thailand, Vietnam, Indonesia, Philippines, Malaysia, Singapore

| Feature | Detail |
|---------|--------|
| Inbound | Accepts consolidated shipments from Taiwan via air/sea |
| WMS integration | Shopee, Lazada, WooCommerce, Shopify via API |
| Minimum volume | No hard minimum; pricing improves at 500+ orders/month |
| Pick & pack | ~$1.20-1.80/order depending on country |
| Local last-mile | Partners: J&T, Ninja Van, Kerry, GrabExpress |
| Returns | Handled per-country; rate $2-5/return |
| Language support | English + Mandarin |
| Billing currency | USD |

**Best for**: Sellers wanting single-vendor SEA coverage with Shopee/Lazada integration. Avoid if you need real-time inventory accuracy — their WMS sync can lag 2-4 hours.

---

### J&T Express Fulfillment (jtexpress.my / .id / .th)

**Coverage**: Indonesia (strongest), Malaysia, Thailand, Vietnam, Philippines

| Feature | Detail |
|---------|--------|
| Inbound | Requires Taiwan pickup or agent handoff; no direct Taiwan-SEA service SLA |
| WMS integration | Shopee, Lazada; limited Shopify support |
| Minimum volume | 300 orders/month per country recommended |
| Pick & pack | ~$0.80-1.20/order (low cost, less service) |
| Local last-mile | Own J&T network — fast in Indonesia |
| Returns | Basic return collection only; no refurbishment |
| Language support | English + local language |
| Billing currency | Local currency (IDR, MYR, THB) |

**Best for**: Indonesia-focused sellers on Shopee where J&T is the dominant carrier. Cost-competitive. Do not use if you need hands-on packaging or kitting.

---

### ShipBob (shipbob.com)

**Coverage**: US (primary), Canada, UK, EU, Australia

| Feature | Detail |
|---------|--------|
| Inbound | Requires your own Taiwan → US freight arrangement |
| WMS integration | Shopify, WooCommerce, Amazon, Etsy, BigCommerce |
| Minimum volume | No minimum; pricing improves at 400+ orders/month |
| Pick & pack | $2.75-3.50/order + $0.20/item beyond first |
| Local last-mile | UPS, USPS, FedEx (ShipBob negotiated rates) |
| Returns | ShipBob Returns portal; $3/return processing |
| Language support | English only |
| Billing currency | USD |

**Best for**: Shopify-native US sales. Their distributed fulfillment network (12+ US warehouses) can route orders from the nearest warehouse, reducing domestic shipping cost by $0.50-1.50/order vs single-node 3PLs.

**Watch out**: Storage fees escalate sharply after 90 days. Slow-moving SKUs become expensive fast.

---

### Shopee / Lazada Fulfillment (SLS / LEX Fulfillment)

This is the marketplace operating their own 3PL — not an independent 3PL. Costs are bundled into platform commissions rather than itemized.

| Feature | Detail |
|---------|--------|
| Inbound | Ship to their overseas warehouse; they handle last-mile |
| WMS integration | None needed — it's the platform |
| Minimum volume | No minimum |
| Effective 3PL cost | Included in 1-3% logistics commission |
| Shipping SLA | 1-3 days domestic after warehouse receipt |
| Returns | Platform-managed; return policy tied to platform rules |

**Best for**: Sellers who are 100% committed to that platform and want zero logistics integration work. **Avoid if** you sell multi-channel — your inventory is locked to the platform and you lose flexibility.

---

### Kerry Logistics / DHL Supply Chain

Enterprise-tier 3PLs. Relevant only if monthly volume exceeds ~$30K/month in 3PL fees or you have unusual requirements (cold chain, high-value goods, hazmat).

Minimum commitment typically USD $5,000-10,000/month. Not appropriate for early-stage cross-border sellers.

---

## Scoring Matrix: How to Choose

Rate each provider 1-5 on the dimensions that matter to your business, then weight by priority.

| Dimension | Weight (example) | Boxme | J&T | ShipBob |
|-----------|-----------------|-------|-----|---------|
| Coverage (your target markets) | 30% | 5 | 4 | 2 |
| Per-order cost | 25% | 3 | 5 | 3 |
| Platform integration (Shopee/Lazada) | 20% | 5 | 4 | 1 |
| WMS accuracy / real-time sync | 15% | 2 | 3 | 5 |
| Returns handling quality | 10% | 3 | 2 | 4 |
| **Weighted score** | | **3.7** | **3.9** | **2.5** |

Adjust weights to your actual situation. A US Shopify seller would flip the platform integration and coverage scores entirely, making ShipBob dominant.

---

## Contract Traps to Negotiate Before Signing

These are the clauses that surprise sellers after they've shipped their first inventory batch.

**1. Minimum monthly fees**
Most 3PLs have a floor fee (e.g., $500/month) regardless of order volume. If you miss your volume projection, you pay the floor. Negotiate a 90-day volume ramp grace period.

**2. Storage rate escalation tiers**
Storage is often cheap for the first 30 days and 3-5× more expensive after 90 days. Know the exact rate schedule. This directly affects your SKU rotation strategy — don't pre-stock slow movers.

**3. Disposal fees**
If unsold inventory needs to be disposed of or returned to Taiwan, disposal can cost $0.50-2.00/unit plus admin fees. Understand this before sending inventory that might not sell.

**4. Rate lock period**
Negotiate a 6-12 month rate lock on pick-pack and storage fees. Fuel surcharges and carrier rate changes are common pass-throughs — clarify which rates are locked vs pass-through.

**5. Liability for lost or damaged inventory**
Standard 3PL liability caps are $0.50/lb or declared value, whichever is lower. For high-value goods, either self-insure or negotiate a higher cap. Get this in writing.

**6. Exit clause**
How much notice to terminate? How long to get your inventory back? Some 3PLs require 60-90 days notice plus 30 days to ship remaining inventory. This matters if you want to switch providers.

---

## Integration Architecture

When you connect a 3PL's WMS to your order management system, the minimum viable integration requires these four data flows:

```
Your Store (Shopify/WooCommerce/Shopee)
    │
    ▼
Order Management System (OMS) — optional but recommended at scale
    │
    ├─── [Order Push] ──────────────────► 3PL WMS
    │       order_id, SKU, qty, ship-to         │
    │                                           │
    ◄─── [Tracking Pull] ────────────────────── │
    │       order_id, carrier, tracking_no       │
    │                                           │
    ├─── [Inventory Sync] ◄────────────────────── 
    │       SKU, available_qty, reserved_qty     │
    │                                           │
    └─── [Returns Notification] ◄─────────────── 
            order_id, reason, condition         
```

Most Tier-1 3PLs (ShipBob, Boxme) provide webhooks for all four. Smaller regional 3PLs may only offer scheduled FTP or CSV exports — plan for polling latency of 1-4 hours in your inventory management logic.

**Minimum acceptance criteria before going live:**
- Order push latency < 15 minutes (order placed → 3PL receives)
- Tracking number available in your system within 2 hours of shipment scan
- Inventory sync frequency: at minimum every 4 hours; real-time preferred
- Returns notification within 24 hours of physical return receipt

---

## Red Flags When Evaluating a 3PL

- Cannot provide a reference customer in your product category
- Refuses to provide itemized rate card in writing (only verbal quotes)
- No documented SLA for pick-pack turnaround (industry standard: same-day for orders before 2pm)
- WMS demo shows no real-time inventory view — only daily batch reports
- Cannot describe their cycle count / inventory reconciliation process
- Customer service contact is only email with 48-hour response SLA (not acceptable for fulfillment issues)

---

## Decision Checklist Before Committing

```
□ Obtained itemized written rate card (not bundled quote)
□ Calculated total cost per order using the formula above
□ Calculated break-even volume — confirmed current orders exceed it
□ Reviewed storage escalation tiers — confirmed SKU rotation plan
□ Negotiated minimum volume ramp grace period
□ Confirmed WMS integration method (API/webhook vs FTP)
□ Tested integration with 5-10 test orders before full inventory shipment
□ Confirmed liability cap and insurance terms in writing
□ Understood exit clause and inventory retrieval timeline
□ Sent initial inventory batch only (not full stock) to validate operations
```

---

## Recommended Starting Strategy

Do not send your full overseas warehouse inventory on day one with a new 3PL. Use this sequence:

1. **Pilot batch**: 100-200 units of your top 3 SKUs
2. **Validate**: 30 days of live operation — measure fill rate, delivery time, inventory accuracy
3. **Expand**: If fill rate >98% and delivery time matches SLA, ship remaining inventory
4. **Renegotiate**: At 6 months, you have volume data to negotiate better rates

Fill rate below 95% or delivery SLA misses >10% of orders are signals to renegotiate or switch providers before committing more inventory.

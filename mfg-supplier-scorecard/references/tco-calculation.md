# TCO Calculation Methodology

Total Cost of Ownership (TCO) quantifies the full economic cost of a supplier relationship over the evaluation period — not just the purchase price on the invoice.

## Core Formula

```
TCO = P + Q + D + I + L + O

Where:
  P = Purchase price (direct)
  Q = Quality cost (defect-related)
  D = Delivery cost (unreliability-related)
  I = Incoming inspection cost
  L = Logistics & customs cost
  O = Overhead & management cost
```

## Component Definitions and Formulas

### P — Purchase Price

```
P = unit_price × annual_volume
```

The baseline. All other components are added to this.

---

### Q — Quality Cost

Quality failures generate costs in two zones: **before use** (incoming defects) and **after use** (field failures).

```
Q = Q_incoming + Q_escapes

Q_incoming = (PPM / 1,000,000) × annual_volume × cost_per_rejection
Q_escapes  = (field_failure_rate) × annual_volume × cost_per_field_failure
```

**cost_per_rejection** includes:
- Sort/rework labor: hourly rate × hours per unit
- Scrap cost: material value of scrapped units
- Line stoppage: if a defective batch halts production, lost_output_per_hour × hours_stopped
- Return logistics: freight cost to return defective goods

**cost_per_field_failure** (if applicable):
- Warranty repair/replacement cost
- Customer satisfaction penalty (contractual or estimated)

| Cost Element | Formula | Typical Range |
|---|---|---|
| Sort/rework labor | $45/hr × 0.25 hr/unit | $10–$40/unit |
| Scrap | material_cost × scrap_rate | Varies |
| Line stoppage | $500/hr × avg_hours_stopped | $500–$10,000/incident |
| Return freight | $200–$800/shipment | Fixed per shipment |

---

### D — Delivery Cost

Late delivery forces two responses, either of which carries cost:

```
D = D_expedite + D_safety_stock

D_expedite    = late_delivery_rate × incidents_per_year × cost_per_expedite
D_safety_stock = holding_cost_rate × (safety_stock_units × unit_cost)
```

**cost_per_expedite** includes:
- Air freight premium vs. sea freight: typically 4–8× cost
- Expediting labor: buyer hours spent managing the crisis
- Customer penalty if your own delivery slips: contractual or estimated

**safety_stock carrying cost**:
```
safety_stock_units = Z × σ_LT × avg_daily_demand

Where:
  Z      = service-level factor (1.65 for 95%, 2.05 for 98%)
  σ_LT   = standard deviation of supplier lead time (in days)
  holding_cost_rate = 20–30% of inventory value per year (includes
                      capital, warehouse, obsolescence, insurance)
```

A supplier with high lead time variability forces you to carry more safety stock even if their average delivery rate looks acceptable.

---

### I — Incoming Inspection Cost

```
I = (inspection_rate × annual_volume × inspection_time_per_unit × labor_rate)
  + equipment_depreciation
  + sampling_overhead
```

| Scenario | Inspection Rate | Driver |
|---|---|---|
| Trusted A-grade supplier | 0–2% (skip lot) | ISO 9001 certified, track record |
| B-grade supplier | 5–10% | Occasional issues |
| New/unqualified supplier | 100% | First 3–6 months |
| C/D-grade supplier | 100% | Active quality problems |

A trusted supplier's certification and track record saves inspection cost directly. Factor this in when comparing a certified supplier at higher unit price vs. uncertified supplier at lower price.

---

### L — Logistics and Customs Cost

```
L = freight_cost + customs_duties + broker_fees + currency_hedge_cost

freight_cost = volume × freight_rate_per_unit × transit_mode_factor
```

| Transit Mode | Cost Factor | Lead Time |
|---|---|---|
| Sea (FCL) | 1.0× baseline | 20–45 days |
| Sea (LCL) | 1.5–2.0× | 25–50 days |
| Air | 4–8× | 2–5 days |
| Truck (domestic) | 1.0–1.5× | 1–5 days |

**Overseas supplier hidden costs:**
- Import duties: typically 0–25% of CIF value (country/HS code specific)
- Customs broker: $150–$500 per shipment
- Port handling and last-mile
- Currency risk: if pricing in USD but paying in CNY/EUR, factor hedging cost or volatility buffer (~2–5%)
- Safety stock (see D above) is inflated for overseas suppliers due to long and variable transit times

---

### O — Overhead and Management Cost

```
O = (buyer_hours_per_year × buyer_rate)
  + (quality_engineer_hours × QE_rate)
  + audit_cost
  + travel_cost
```

This cost is invisible in standard procurement analysis but real. A difficult supplier that requires weekly calls, supplier audits, corrective action tracking, and engineering support consumes 3–10× the internal labor of a well-run supplier.

| Activity | Hours/Year (typical well-run supplier) | Hours/Year (problematic supplier) |
|---|---|---|
| PO management | 10 | 10 |
| Issue resolution | 5 | 80+ |
| CAPA follow-up | 5 | 40+ |
| Audits | 8 | 24+ |
| Engineering support | 5 | 30+ |
| **Total** | **~33 hrs** | **~184 hrs** |

At $75/hr fully loaded: $2,475 vs. $13,800 per year — an $11,000+ difference invisible in the purchase price.

---

## Worked Example

**Scenario**: Evaluating two suppliers for a precision machined housing. Annual volume: 10,000 units.

|  | Supplier A (Domestic) | Supplier B (Overseas) |
|---|---|---|
| Unit price | $48.00 | $38.00 |
| Annual purchase cost | $480,000 | $380,000 |

**Quality cost:**

| | Supplier A | Supplier B |
|---|---|---|
| PPM | 800 | 3,500 |
| Rejections/year | 8 units | 35 units |
| Cost per rejection (rework + sort) | $35 | $35 |
| Q_incoming | $280 | $1,225 |

**Delivery cost:**

| | Supplier A | Supplier B |
|---|---|---|
| On-time rate | 97% | 88% |
| Late incidents/year | ~3 | ~14 |
| Cost per expedite (air freight premium + labor) | $1,200 | $4,500 |
| D_expedite | $3,600 | $63,000 |
| Lead time std dev (days) | 2 | 8 |
| Required safety stock (95% SL) | 330 units | 1,320 units |
| Safety stock carrying cost (25% × unit cost) | $3,960 | $12,540 |
| D_total | $7,560 | $75,540 |

**Incoming inspection:**

| | Supplier A | Supplier B |
|---|---|---|
| Inspection rate | 5% | 15% |
| Units inspected | 500 | 1,500 |
| Time per unit | 8 min | 8 min |
| Labor rate | $40/hr | $40/hr |
| I | $2,667 | $8,000 |

**Logistics:**

| | Supplier A | Supplier B |
|---|---|---|
| Freight cost | $8,000 | $22,000 |
| Import duties (8%) | $0 | $30,400 |
| Currency hedge | $0 | $7,600 |
| L | $8,000 | $60,000 |

**Overhead:**

| | Supplier A | Supplier B |
|---|---|---|
| Internal labor (buyer + QE) | $4,000 | $11,000 |
| Audits + travel | $2,000 | $8,500 |
| O | $6,000 | $19,500 |

**TCO Summary:**

| Component | Supplier A | Supplier B |
|---|---|---|
| P Purchase price | $480,000 | $380,000 |
| Q Quality cost | $280 | $1,225 |
| D Delivery cost | $7,560 | $75,540 |
| I Inspection | $2,667 | $8,000 |
| L Logistics | $8,000 | $60,000 |
| O Overhead | $6,000 | $19,500 |
| **TCO Total** | **$504,507** | **$544,265** |
| **TCO per unit** | **$50.45** | **$54.43** |

**Result**: Supplier B appears 21% cheaper on unit price. After TCO, Supplier A is 8% cheaper — and carries lower risk.

---

## Sensitivity Analysis

TCO estimates contain assumptions. Test which assumptions drive the conclusion.

Key variables to stress-test:

| Variable | Base Case | Pessimistic | Impact |
|---|---|---|---|
| Expedite cost | $4,500 | $8,000 | High |
| On-time rate | 88% | 80% | High |
| Import duty rate | 8% | 15% | Medium |
| PPM defect rate | 3,500 | 8,000 | Medium |
| Internal labor hours | 184 | 300 | Medium |

If the conclusion flips under pessimistic assumptions, the decision is fragile. Require more data or risk premium before proceeding with the lower-TCO supplier.

---

## TCO Scoring Integration

To incorporate TCO into the QCDS scorecard's **Cost dimension** (rather than using unit price alone):

```
cost_score = score_based_on_TCO_per_unit, not invoice_price

TCO per unit bands (calibrate to your category):
  5 = At or below benchmark TCO (best quartile)
  4 = 1–10% above benchmark
  3 = 10–20% above benchmark
  2 = 20–35% above benchmark
  1 = >35% above benchmark
```

Benchmark = lowest TCO supplier in the active pool for that component category.

This prevents the common error of scoring a low-unit-price supplier as "5" on Cost while ignoring $75K in expedition and logistics overhead.

---

## Common TCO Calculation Mistakes

**Mistake 1: Using average lead time instead of lead time variability**
A supplier with average 30-day lead time and σ=2 days requires far less safety stock than one with average 30 days and σ=10 days. The standard deviation drives safety stock, not the mean.

**Mistake 2: Ignoring sunk inspection costs**
"We already have QC staff" does not mean inspection is free. When comparing suppliers, use the marginal inspection hours that would be saved or added — a high-quality supplier frees your QC team for other work.

**Mistake 3: One-year horizon for capital equipment suppliers**
For tooling, machinery, or long-lifecycle components, run TCO over the asset lifetime (5–10 years). Switching costs, re-qualification, and tooling amortization all belong in the analysis.

**Mistake 4: Double-counting safety stock and expediting**
Companies either hold safety stock OR expedite — not both at the same rate. If safety stock is sized correctly, expediting drops. Model them as partially offsetting: higher safety stock → lower expedite frequency.

**Mistake 5: Omitting the cost of unrealized capacity**
When a line stops due to supplier failure, the opportunity cost is lost throughput — not just the direct line cost. Include contribution margin per hour if the plant is capacity-constrained.

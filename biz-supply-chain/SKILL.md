---
name: "biz-supply-chain"
description: "Analyze supply chain operations using the SCOR model across Plan, Source, Make, Deliver, and Return processes. Use this skill when the user needs to optimize supply chain efficiency, evaluate supplier performance, improve logistics, or design an end-to-end supply chain strategy — even if they say 'our deliveries are slow', 'supply chain costs are too high', or 'we keep running out of stock'."
metadata:
  category: "WP-16 商學院—營運"
  tags: ["operations", "supply-chain", "scor", "logistics"]
---

# Supply Chain Analysis (SCOR Model)

## Overview

The SCOR (Supply Chain Operations Reference) model structures supply chain analysis into five core processes: Plan, Source, Make, Deliver, Return. It provides a common language for analyzing, benchmarking, and improving supply chain performance from supplier's supplier to customer's customer.

## Framework

```
IRON LAW: End-to-End, Not Silo-by-Silo

Supply chain optimization must consider the ENTIRE chain. Optimizing
procurement (Source) without considering production capacity (Make) or
delivery capability (Deliver) creates bottlenecks downstream.

A local optimum in one process often creates a global problem elsewhere.
```

### The Five SCOR Processes

**1. Plan** — Demand forecasting, supply planning, inventory strategy
- Demand forecast accuracy, S&OP process, inventory policies
- Question: "Do we make/buy the right amount at the right time?"

**2. Source** — Supplier selection, procurement, incoming quality
- Supplier scorecards, lead times, sourcing strategy (single vs multi)
- Question: "Are we getting the right inputs at the right cost and quality?"

**3. Make** — Production, assembly, manufacturing
- Production scheduling, capacity utilization, quality control, WIP management
- Question: "Are we converting inputs to outputs efficiently?"

**4. Deliver** — Order management, warehousing, transportation, last-mile
- Order fulfillment rate, delivery speed, logistics cost, channel management
- Question: "Are we getting products to customers reliably and affordably?"

**5. Return** — Returns processing, reverse logistics, warranty/repair
- Return rate, reverse logistics cost, refurbishment, disposal
- Question: "Are we handling returns efficiently and learning from them?"

### Key Supply Chain Metrics

| Process | Metric | Formula/Definition |
|---------|--------|-------------------|
| Plan | Forecast Accuracy | 1 - \|Actual - Forecast\| / Actual |
| Plan | Inventory Days | Inventory / (COGS / 365) |
| Source | Supplier On-Time Rate | On-time deliveries / Total deliveries |
| Source | Supplier Defect Rate | Defective units / Total received |
| Make | OEE | Availability × Performance × Quality |
| Deliver | Perfect Order Rate | Orders delivered on time, in full, without error |
| Deliver | Order-to-Delivery Cycle | Time from order to customer receipt |
| Return | Return Rate | Returns / Total shipments |

### Analysis Steps

1. **Map the current supply chain** from supplier to customer
2. **Measure** key metrics per SCOR process
3. **Benchmark** against industry standards
4. **Identify** the weakest process (highest gap to benchmark)
5. **Improve** the weakest link first (same logic as TOC — chain is as strong as weakest link)

## Output Format

```markdown
# Supply Chain Analysis: {Company}

## Supply Chain Map
Supplier → [Source] → [Make] → [Deliver] → Customer
            ↑ [Plan] (coordinates all) ↑
                     [Return] ←

## SCOR Performance Dashboard
| Process | Key Metric | Current | Benchmark | Gap |
|---------|-----------|---------|-----------|-----|
| Plan | Forecast Accuracy | X% | 85%+ | {gap} |
| Source | Supplier On-Time | X% | 95%+ | {gap} |
| Make | OEE | X% | 85%+ | {gap} |
| Deliver | Perfect Order Rate | X% | 95%+ | {gap} |
| Return | Return Rate | X% | <5% | {gap} |

## Weakest Link Analysis
{Which process has the largest gap and why}

## Improvement Recommendations
1. {Process}: {specific improvement} → {expected metric impact}
```

## Examples

### Correct Application
**Scenario:** SCOR analysis for a Taiwanese DTC electronics brand
| Process | Metric | Current | Issue |
|---------|--------|---------|-------|
| Plan | Forecast Accuracy | 62% | Demand spikes around promotions are unpredicted |
| Source | Supplier On-Time | 88% | Key component supplier in Shenzhen has inconsistent lead times |
| Make | OEE | 78% | Reasonable for electronics assembly |
| Deliver | Perfect Order Rate | 91% | Last-mile carrier (���貓) loses 3% of packages |
| **Weakest**: Plan (62%) — fixing forecast accuracy would reduce both inventory (currently 45 days, target 30) and stockouts

### Incorrect Application
- Only analyzed Deliver (logistics) because "delivery is our biggest complaint" → Root cause was Plan (bad forecast → stockouts → backorders → late deliveries). Fixing delivery alone doesn't help. Violates Iron Law: end-to-end analysis.

## Gotchas

- **Bullwhip effect**: Small demand changes at retail amplify upstream. A 10% sales increase can trigger 40% production increase at the manufacturer. S&OP process mitigates this.
- **Single-source risk**: One supplier = zero redundancy. The 2021 chip shortage proved this globally. Evaluate single-source dependencies explicitly.
- **Make-vs-Buy is a Source decision**: Not just cost — consider IP protection, quality control, lead time, and supply security.
- **Last-mile is often the costliest**: Last-mile delivery can be 40-50% of total logistics cost. Evaluate delivery model (own fleet vs 3PL vs pickup points).
- **Returns are a profit leak**: Many companies treat returns as an afterthought. A 15% return rate in e-commerce means 15% of fulfillment cost is wasted plus reverse logistics cost.

## References

- For SCOR model detailed metrics, see `references/scor-metrics.md`
- For inventory optimization methods, see `references/inventory-models.md`

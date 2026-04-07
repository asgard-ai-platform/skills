---
name: "mfg-production-planning"
description: "Design production plans using MPS (Master Production Schedule), MRP (Material Requirements Planning), and capacity planning. Use this skill when the user needs to schedule production, plan material procurement, balance capacity with demand, or optimize production sequencing — even if they say 'we can't keep up with orders', 'when should we order materials', 'production scheduling', or 'how do we plan for next quarter's demand'."
metadata:
  category: "WP-03 製造業"
  tags: ["manufacturing", "production-planning", "mrp", "scheduling"]
---

# Production Planning (MPS/MRP)

## Framework

```
IRON LAW: Plan Hierarchically — Demand → MPS → MRP → Shop Floor

Production planning flows TOP-DOWN:
1. Demand forecast / customer orders → what to make, when
2. MPS → master schedule for finished goods
3. MRP → material and component requirements (what to buy, when)
4. Shop floor scheduling → which machine, which sequence

Skipping levels (going from demand forecast directly to shop floor)
creates chaos — material shortages, capacity conflicts, missed deliveries.
```

### Planning Hierarchy

| Level | Plan | Horizon | Granularity | Decides |
|-------|------|---------|-------------|---------|
| **Strategic** | S&OP (Sales & Operations Planning) | 12-18 months | Monthly, product family | Capacity investments, workforce planning |
| **Tactical** | MPS (Master Production Schedule) | 3-6 months | Weekly, end product | What to produce each week |
| **Operational** | MRP (Material Requirements Planning) | 4-12 weeks | Daily, component/material | What to order, when, how much |
| **Execution** | Shop Floor Scheduling | 1-2 weeks | Hourly, work center | Sequence, machine assignment |

### MPS Process

1. **Inputs**: Demand forecast + customer orders + current inventory + safety stock targets
2. **Logic**: For each week, calculate: Production Needed = Demand - Beginning Inventory - Scheduled Receipts + Safety Stock
3. **Output**: Planned production quantities by week for each finished product
4. **Constraint**: Must not exceed available capacity (rough-cut capacity planning check)

### MRP Process

1. **Inputs**: MPS (what to make) + BOM (Bill of Materials — what it's made of) + Inventory status + Lead times
2. **Logic**: "Explode" the BOM — for each finished good, calculate when each component/material must be ordered to arrive in time
3. **Output**: Planned purchase orders and production orders with dates and quantities
4. **Key calculation**: Order date = Need date - Lead time

### Scheduling Algorithms

| Algorithm | Rule | Best When |
|-----------|------|-----------|
| **FCFS** (First Come First Served) | Process in order received | Low complexity, fairness matters |
| **SPT** (Shortest Processing Time) | Shortest job first | Minimize average flow time |
| **EDD** (Earliest Due Date) | Most urgent due date first | Minimize late deliveries |
| **Bottleneck-first** | Schedule the constraint first, subordinate rest | Capacity-constrained environments (TOC logic) |

### SMED (Single-Minute Exchange of Die)

Reduce changeover time to increase flexibility:
1. Separate internal setup (machine stopped) from external (can do while running)
2. Convert internal to external where possible
3. Streamline remaining internal steps
4. Practice and standardize

## Output Format

```markdown
# Production Plan: {Product/Period}

## Demand vs Capacity
| Week | Demand | Available Capacity | Gap |
|------|--------|-------------------|-----|
| W1 | {units} | {units} | {+/-} |

## Master Production Schedule
| Week | Product A | Product B | Product C | Total |
|------|----------|----------|----------|-------|
| W1 | {units} | {units} | {units} | {units} |

## Material Requirements
| Material | Quantity | Order Date | Supplier | Lead Time |
|----------|---------|-----------|----------|-----------|
| {material} | {qty} | {date} | {supplier} | {days} |

## Scheduling
| Work Center | Mon | Tue | Wed | Thu | Fri |
|------------|-----|-----|-----|-----|-----|
| {center} | {job} | {job} | ... | ... | ... |
```

## Gotchas

- **Forecast accuracy limits everything**: MPS/MRP is only as good as the demand forecast. Track forecast accuracy (MAPE) and build safety stock proportional to forecast error.
- **Lead time variability kills plans**: If supplier lead time is "2-6 weeks" (4 week variability), you need safety stock for the worst case. Reduce variability through supplier management.
- **BOM accuracy is critical for MRP**: A wrong BOM means ordering wrong materials. Audit BOMs quarterly.
- **Frozen zone**: The first 1-2 weeks of MPS should be "frozen" (no changes) to allow stable execution. Changes inside the frozen zone cascade chaos through the system.
- **Finite vs infinite capacity**: Basic MRP assumes infinite capacity (ignores machine constraints). Always layer a capacity check (rough-cut or detailed) on top of MRP output.

## References

- For S&OP process design, see `references/sop-process.md`
- For demand forecasting methods, see `references/demand-forecasting.md`

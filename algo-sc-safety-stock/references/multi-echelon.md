# Multi-Echelon Safety Stock Optimization

## The Core Problem

Single-echelon safety stock (from `SKILL.md`) assumes one inventory location
buffers against uncertainty. Multi-echelon systems have a **chain of buffers**:
supplier → central warehouse (CW) → regional DC → store. Applying the
single-echelon formula independently at each node leads to two failure modes:

1. **Double-counting**: both CW and DC hold safety stock against the same
   demand variability. Inventory is duplicated across the chain.
2. **Wrong placement**: high-cost finished goods sit at every node when it
   would be cheaper to hold semi-finished stock upstream and finish to order
   downstream.

The goal is to decide **where** to hold safety stock, not just **how much**
in aggregate.

---

## Guaranteed Service Model (Graves & Willems, 2000)

The dominant practical framework. Each node makes two promises:

- **Inbound service time (SI)**: the maximum time it will wait for replenishment
  from its upstream node before experiencing a stockout.
- **Outbound service time (S)**: the maximum time it promises to its downstream
  customer.

Each node then holds safety stock to cover the gap
**Net Replenishment Time (NRT)**:

```
NRT_i = LT_i + SI_i − S_i
```

Where:
- `LT_i` = replenishment lead time of node i
- `SI_i` = inbound service time (how long node i waits for its supplier)
- `S_i` = outbound service time node i quotes downstream

Safety stock at node i:

```
SS_i = z × σ_d × √NRT_i
```

This is the single-echelon formula from `SKILL.md`, but applied to `NRT_i`
instead of raw `LT_i`.

**IRON LAW reinforced**: the non-linear cost of service level still applies at
each node. Tightening downstream promised service time (`S_i` → 0) forces the
node to absorb its full lead time, which grows SS by √LT.

---

## Worked Example: 3-Echelon Chain

### Network

```
Supplier → Central Warehouse (CW) → Regional DC → Store
```

| Node | LT (weeks) | avg demand/week | σ_demand/week |
|------|-----------|-----------------|---------------|
| CW   | 4         | 500             | 100           |
| DC   | 1         | 100             | 30            |
| Store| 0.5       | 20              | 8             |

Target: 95% service level at store (z = 1.65). Assume demand at each node is
independent (aggregated at CW, disaggregated downstream).

### Step 1: Choose outbound service times

This is the **optimization decision**. Try two policies:

**Policy A — No buffering at CW or DC** (all safety stock at store)

```
S_CW  = 0    (CW ships immediately to DC)
SI_DC = 0    (DC gets from CW immediately)
S_DC  = 0    (DC ships immediately to Store)
SI_Store = 0
```

NRT for each node:
```
NRT_Store = 0.5 + 0 − 0 = 0.5 weeks
NRT_DC    = 1   + 0 − 0 = 1   week
NRT_CW    = 4   + 0 − 0 = 4   weeks
```

Safety stock (all at 95%):
```
SS_Store = 1.65 × 8  × √0.5 = 1.65 × 8  × 0.707 = 9.3  units
SS_DC    = 1.65 × 30 × √1   = 1.65 × 30 × 1.0   = 49.5 units
SS_CW    = 1.65 × 100× √4   = 1.65 × 100× 2.0   = 330  units
```

Total SS (all nodes): 9.3 + 49.5 + 330 = **389 units**

**Policy B — CW absorbs all uncertainty** (quotes long service time downstream)

Set `S_CW = 4` (CW takes 4 weeks to ship, DC gets nothing guaranteed faster).

```
SI_DC     = 4    (DC waits up to 4 weeks for CW)
S_DC      = 4    (DC passes the wait to Store)
SI_Store  = 4
```

NRT for each node:
```
NRT_Store = 0.5 + 4 − 0 = 4.5 weeks   ← Store now buffers everything!
NRT_DC    = 1   + 4 − 4 = 1   week
NRT_CW    = 4   + 0 − 4 = 0   weeks   ← no SS needed at CW
```

```
SS_Store = 1.65 × 8  × √4.5 = 1.65 × 8  × 2.12 = 28.0 units
SS_DC    = 1.65 × 30 × √1   = 1.65 × 30 × 1.0  = 49.5 units
SS_CW    = 0
```

Total SS: 28.0 + 49.5 + 0 = **77.5 units**

### Step 2: Compare with unit costs

Policy B has fewer total units but pushes SS to the store (highest unit cost).
Multiply by unit cost to get holding cost:

| Node  | Unit cost | Policy A SS | Policy A cost | Policy B SS | Policy B cost |
|-------|-----------|-------------|---------------|-------------|---------------|
| CW    | $10       | 330         | $3,300        | 0           | $0            |
| DC    | $12       | 49.5        | $594          | 49.5        | $594          |
| Store | $15       | 9.3         | $140          | 28.0        | $420          |
| **Total** | —     | 388.8       | **$4,034**    | 77.5        | **$1,014**    |

Policy B costs 75% less despite holding SS at a pricier node — because CW's
long lead time was inflating Policy A's upstream buffer enormously.

### Step 3: Optimization

In real implementations, you enumerate (or solve via dynamic programming) all
valid combinations of `(S_CW, S_DC, S_Store)` subject to:

```
S_i ≤ LT_i + SI_i       (node can't promise faster than it can deliver)
NRT_i ≥ 0               (can't have negative net replenishment time)
```

For chains up to ~10 nodes, exact DP is practical. For networks with branches
(one CW → many DCs), use Graves-Willems DP on the spanning tree.

---

## Decision Framework: Where to Position Stock

| Condition | Place SS here | Reason |
|-----------|---------------|--------|
| High demand variability at leaf nodes | Upstream (CW/DC) | Aggregation reduces combined σ |
| Long, variable upstream lead time | At the node below the long LT | Buffers the worst uncertainty locally |
| High cost differential (cheap raw, expensive finished) | Upstream in unfinished form | Postponement: finish on demand |
| Short overall lead time chain (≤2 weeks total) | At store | Overhead of multi-echelon model may not be worth it |
| Demand is intermittent (many zeros) | Do NOT use this model | Use Poisson-based model per `references/intermittent-demand.md` |

---

## Demand Aggregation Benefit

A key reason to centralize SS upstream: **pooling reduces variability**.

For `n` stores each with independent demand σ, the central warehouse serving
all n stores has:

```
σ_CW = σ_store × √n
```

Total SS if each store buffers independently:
```
SS_total_distributed = n × z × σ_store × √LT
```

Total SS if CW buffers centrally (stores have zero SS):
```
SS_total_centralized = z × σ_store × √n × √LT_CW
```

Ratio (assuming LT_CW ≈ LT_store for simplicity):
```
SS_centralized / SS_distributed = √n / n = 1/√n
```

With 9 stores: centralized SS is 1/3 of distributed SS. With 25 stores: 1/5.

**Caveat**: centralized SS only works if the CW can replenish stores faster
than demand variability unfolds. If store lead time from CW is long, the
pooling benefit erodes.

---

## Practical Implementation Checklist

```
□ Map the echelon structure: identify all nodes and their LTs
□ Classify demand at each node as dependent (driven by downstream orders)
  or independent (direct end-customer demand)
□ Collect σ_demand at the demand-facing nodes (stores/end customers)
□ Propagate demand statistics upstream using √n aggregation
□ Set target service level per echelon — NOT the same at every node
  (99% at store, 95% at DC, 90% at CW is a common starting point)
□ Run policy enumeration or DP to find minimum-cost (S_i) combination
□ Verify: simulate 12+ months of demand through the chain; confirm
  end-customer service level matches target (±2%, matching SKILL.md gate)
□ Review quarterly: lead times and demand variability change seasonally
```

---

## Common Mistakes

**Mistake 1 — Treating each node independently**
Running single-echelon SS at CW *and* DC *and* store with the same service
level target counts the same demand uncertainty multiple times. Use NRT, not
raw LT, at each node.

**Mistake 2 — Ignoring inbound service time**
If DC orders from CW and CW quotes a 2-week service time (`S_CW = 2`), DC's
effective lead time is `LT_DC + 2`, not `LT_DC`. Forgetting this understates
DC safety stock.

**Mistake 3 — Pooling correlated demand**
The `σ_CW = σ × √n` formula assumes demand across stores is independent.
Correlated demand (same product, same promotion, same weather shock) reduces
the pooling benefit. In high-correlation scenarios, the formula understates
required upstream safety stock.

**Mistake 4 — Confusing echelon stock with installation stock**
*Echelon stock* at node i = inventory at i + all downstream inventory.
*Installation stock* = inventory physically at i only.
The Graves-Willems model works on installation stock. Some academic papers
(Clark-Scarf) use echelon stock. Mixing definitions gives wrong answers.

**Mistake 5 — Applying to make-to-order items**
If a node never holds inventory (pure MTO), it has no SS. The multi-echelon
model applies only to nodes that carry stock. MTO nodes still affect NRT
through their lead time contribution.

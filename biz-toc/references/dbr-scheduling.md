# Drum-Buffer-Rope (DBR) Scheduling

DBR is the TOC-derived production scheduling method that synchronizes an entire manufacturing system to the bottleneck's pace. It replaces MRP push logic with a pull-from-constraint discipline.

---

## Core Mechanics

```
Release Point                 Bottleneck (Drum)           Shipping
     │                               │                        │
     ▼                               ▼                        ▼
[Raw Material] ──────────────► [Constraint Step] ─────────► [Output]
     ▲                         ▲
     │                         │
   Rope                      Buffer
(release signal)          (WIP cushion)
```

**Drum** — The bottleneck dictates the system's production rate. All scheduling is derived from its capacity.

**Buffer** — A time buffer of WIP positioned *before* the bottleneck. Its purpose is to absorb upstream variability so the bottleneck never idles waiting for input.

**Rope** — A release authorization signal tied to the drum. Raw material enters the system only when the rope says so, preventing WIP accumulation upstream of the bottleneck.

---

## Buffer Sizing

### Time Buffer (Primary Method)

The buffer is expressed in **time units**, not piece counts, because piece counts mislead when processing times vary.

```
Buffer Size (hours) = Drum Rate × Safety Multiplier

Where:
  Drum Rate     = bottleneck cycle time (hours/unit) × buffer coverage window
  Safety Mult.  = 1.5 to 3.0 (depends on upstream variability)
```

**Practical starting formula:**

```
Buffer = 2 × (longest upstream process lead time)
```

If upstream has 3 steps with lead times of 2 hr, 1.5 hr, and 0.5 hr, the longest is 2 hr:

```
Buffer = 2 × 2 hr = 4 hr
```

This means: keep 4 hours of work queued before the bottleneck at all times.

### Buffer Zones (Red/Yellow/Green)

Divide the buffer into thirds to trigger management actions:

| Zone | Buffer Remaining | Action |
|------|-----------------|--------|
| Green | > 2/3 of buffer | Normal — no action needed |
| Yellow | 1/3 to 2/3 of buffer | Watch — investigate why buffer is eroding |
| Red | < 1/3 of buffer | Expedite — escalate upstream immediately |

**Why thirds?** Empirically robust across most manufacturing environments. If your system has very long lead times or high variability, adjust the Red threshold to 40%.

---

## Rope: Work Release Calculation

The rope controls when raw material is released into the system.

```
Release Time = Scheduled Drum Processing Time − Buffer Size

Example:
  Bottleneck needs unit X at 14:00
  Buffer Size = 4 hours
  → Release raw material at 10:00
```

This means the system always works "backward from the drum." The release schedule is NOT driven by machine availability upstream — it is driven entirely by when the bottleneck needs the material.

**Common mistake:** releasing material at upstream machine availability → immediately overproduces WIP → buffer zone turns red → chaos.

---

## Throughput Rate Calculation

System throughput is bounded by the bottleneck:

```
System Throughput = min(T₁, T₂, ..., Tₙ)

Where Tᵢ = throughput rate of step i (units/hour)
```

**Worked Example — PCB Line** (from SKILL.md scenario, extended):

| Station | Rate (units/hr) | Utilization at System Rate |
|---------|----------------|---------------------------|
| Solder Paste | 100 | 50/100 = 50% |
| Pick & Place | 80 | 50/80 = 63% |
| **Reflow Oven** | **50** | **50/50 = 100% ← Drum** |
| Inspection | 90 | 50/90 = 56% |
| Packaging | 120 | 50/120 = 42% |

System throughput = 50 units/hr (constrained by Reflow Oven).

**Buffer sizing for this line:**
- Upstream lead time through Solder Paste + Pick & Place = 0.6 min + 0.75 min per unit = roughly 1.35 min at current pace
- At batch level (assume batches of 20 units): 20 × 1.35 min = 27 min upstream lead time
- Buffer = 2 × 27 min = **54 minutes of WIP before Reflow Oven**
- At 50 units/hr: 54 min × (50/60) = **~45 units in buffer**

**Rope setting:** Release a new batch every 24 minutes (= 20 units ÷ 50 units/hr × 60 min).

---

## DBR Implementation Steps

### Step 1: Identify the Drum

Collect throughput rates for every process step. The step with the **lowest throughput rate** is the drum. If two steps tie, pick the one that:
- Has the least flexible capacity (hardest to add)
- Has the highest cost per unit of capacity

### Step 2: Calculate Drum Schedule

Build the master production schedule *at the drum only*. Do not schedule every workstation — this is the key departure from MRP.

```
Drum Schedule:
  Product A: 10 units, starts 08:00, completes 08:12
  Product B: 15 units, starts 08:12, completes 08:30
  ...
```

Sequence by due date or throughput contribution (T/cu — see below).

### Step 3: Set Buffer Size

Use the formula above. Start with the 2× upstream lead time heuristic, then adjust after 2 weeks of observation:
- Buffer frequently hits Red → increase by 25%
- Buffer rarely drops below Green → decrease by 20%

### Step 4: Calculate Rope Release Times

For each drum job, subtract buffer size from drum start time to get raw material release time. Post this as the *only* release authorization — upstream operators are not allowed to release material otherwise.

### Step 5: Subordinate Non-Bottleneck Scheduling

Non-drum stations should:
1. Process whatever is in their queue in FIFO order
2. **Stop** when their output queue reaches the buffer size
3. Never pull material to keep themselves busy

This last point is the hardest to enforce culturally. Idle time at non-bottleneck stations is not a problem.

---

## Throughput-per-Constraint-Unit (T/cu) Prioritization

When the drum has limited capacity and multiple products compete for it, prioritize by T/cu:

```
T/cu = (Revenue − Variable Cost per unit) ÷ (Drum time consumed per unit)

     = Unit Throughput ÷ Drum Minutes per unit
```

**Example:**

| Product | Price | Variable Cost | Unit T | Drum Time | T/cu |
|---------|-------|--------------|--------|-----------|------|
| Alpha | $500 | $200 | $300 | 10 min | $30/min |
| Beta | $800 | $400 | $400 | 20 min | $20/min |
| Gamma | $300 | $100 | $200 | 5 min | $40/min |

**Priority: Gamma > Alpha > Beta**

Beta has the highest unit throughput but the *worst* use of drum time. Filling the drum with Beta squeezes out two Gammas, losing $40/min × 5 min × 2 = $400 in throughput.

**Decision rule:** rank all products by T/cu descending, fill drum schedule top-down until capacity is exhausted.

---

## Shipping Buffer

Beyond the constraint buffer, add a **shipping buffer** between the last process step and the customer commitment date:

```
Shipping Buffer = promised lead time − total production lead time

If negative → lead time commitment is too aggressive; negotiate or elevate
```

The shipping buffer absorbs variability downstream of the constraint (inspection failures, packaging delays, logistics). Size it the same way as the constraint buffer: aim for Green/Yellow/Red zones.

---

## Buffer Management as a Diagnostic Tool

Buffer zone penetration patterns reveal systemic problems:

| Pattern | Likely Root Cause |
|---------|--------------------|
| Red occurs daily at same time | Upstream machine scheduled maintenance conflicts |
| Red follows specific upstream product | Setup/changeover time spike on that product |
| Buffer never below Green after months | Buffer oversized; reduce to free WIP capital |
| Rapid Red after shift change | Operator handoff issue; first-piece yield drops |
| Red correlates with specific materials | Supplier delivery variability |

Track buffer zone penetration daily. After 30 days you will have a ranked list of disruptions by frequency and severity — this becomes the continuous improvement backlog, focused only on upstream-of-constraint problems.

---

## DBR vs. Simplified DBR (S-DBR)

| Aspect | DBR | S-DBR |
|--------|-----|-------|
| Constraint location | Physical bottleneck | Market demand treated as constraint |
| Buffer placement | Before physical constraint | Shipping buffer only |
| Best for | Stable bottleneck, high utilization | Demand-constrained (factory can make more than market buys) |
| Complexity | Higher | Lower |

Use S-DBR when your factory runs below 80% utilization on most products — the market is the real constraint, and protecting the shipping date matters more than protecting a physical step.

---

## Failure Modes

**Rope not enforced**: Upstream supervisors release material to keep their teams busy. WIP accumulates before the drum, buffer zone turns permanently Red, expediting becomes the norm. Fix: make rope release a hard gate, not a recommendation.

**Buffer sized in pieces, not time**: A batch of 50 small units and a batch of 50 large units are not equivalent buffers. Always convert to time: pieces ÷ drum rate = hours of protection.

**Drum schedule over-loaded**: Teams squeeze more jobs into the drum than its rate supports, assuming "we'll catch up." The drum cannot catch up by definition. Enforce drum capacity as a hard ceiling.

**Forgetting Step 5 (Repeat)**: After elevating the constraint (e.g., adding a second Reflow Oven), throughput jumps — but the new constraint (maybe Pick & Place at 80/hr) now limits the system. Teams continue optimizing the old constraint. Buffer the new drum, move the rope.

**Buffer management ignored**: The buffer is installed but nobody monitors zone penetration. It becomes a WIP dumping ground rather than a diagnostic instrument. Assign one person to review buffer status daily.

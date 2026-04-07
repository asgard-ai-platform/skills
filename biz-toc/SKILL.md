---
name: "biz-toc"
description: "Apply Theory of Constraints (TOC) to identify and manage system bottlenecks. Use this skill when the user needs to find what limits throughput, optimize a constrained process, apply the Five Focusing Steps, or implement Drum-Buffer-Rope scheduling — even if they say 'our output is stuck', 'what's the bottleneck', or 'why can't we produce more'."
metadata:
  category: "WP-16 商學院—營運"
  tags: ["operations", "toc", "bottleneck", "throughput"]
---

# Theory of Constraints (TOC)

## Overview

TOC asserts that every system has at least one constraint (bottleneck) that limits total throughput. Improving non-bottleneck processes does NOT improve system output �� only improving the bottleneck does. The Five Focusing Steps provide a systematic method to find and manage constraints.

## Framework

```
IRON LAW: The System Is Only as Strong as Its Weakest Link

Improving a non-bottleneck process is a WASTE of resources — it produces
more work-in-progress that piles up at the bottleneck. Before optimizing
any process, verify it IS the bottleneck. If it's not, stop.
```

### The Five Focusing Steps

1. **IDENTIFY** the constraint — Find the bottleneck (highest utilization, longest queue, most WIP accumulation)
2. **EXPLOIT** the constraint — Maximize throughput at the bottleneck without adding resources (reduce downtime, eliminate waste at this step, ensure it never starves for input)
3. **SUBORDINATE** everything else — Pace all other processes to the bottleneck's rhythm. Non-bottlenecks should NOT run at full capacity.
4. **ELEVATE** the constraint — If exploitation isn't enough, invest to increase bottleneck capacity (add equipment, hire, outsource)
5. **REPEAT** — After elevating, the constraint may shift to another process. Go back to Step 1.

### Drum-Buffer-Rope (DBR) Scheduling

| Element | What It Is | Purpose |
|---------|-----------|---------|
| **Drum** | The bottleneck's pace | Sets the rhythm for the entire system |
| **Buffer** | Time buffer before the bottleneck | Ensures the bottleneck never starves for work |
| **Rope** | Signal to release work at the start | Controls WIP by tying input rate to bottleneck pace |

### Throughput Accounting (TOC Financial Metrics)

| Metric | Definition |
|--------|-----------|
| **Throughput (T)** | Revenue - Truly Variable Costs (materials only) |
| **Investment (I)** | Money tied up in the system (inventory, equipment) |
| **Operating Expense (OE)** | All other costs to run the system |
| **Net Profit** | T - OE |
| **ROI** | (T - OE) / I |

## Output Format

```markdown
# TOC Analysis: {System/Process}

## System Map
{Process A} → {Process B} → {**Process C (bottleneck)**} → {Process D} → Output

## Constraint Identification
- Bottleneck: {process step}
- Evidence: {utilization %, queue length, WIP accumulation}
- Current throughput: {units/period}

## Five Focusing Steps
| Step | Action | Expected Impact |
|------|--------|----------------|
| 1. Identify | {bottleneck location} | — |
| 2. Exploit | {optimize without investment} | +X% throughput |
| 3. Subordinate | {pace other processes} | Reduce WIP by X% |
| 4. Elevate | {investment if needed} | +X% throughput |
| 5. Repeat | {new constraint location} | — |

## DBR Implementation
- Drum: {bottleneck pace = X units/hour}
- Buffer: {X hours of WIP before bottleneck}
- Rope: {release new work every X minutes}
```

## Examples

### Correct Application
**Scenario:** TOC for a PCB assembly line (5 stations)
- Station throughput: Solder Paste (100/hr) → Pick & Place (80/hr) → **Reflow Oven (50/hr)** → Inspection (90/hr) → Packaging (120/hr)
- Bottleneck: Reflow Oven (50/hr) — lowest throughput, highest utilization
- **Exploit**: Reduce oven changeover time from 30 min to 10 min → effective capacity +15%
- **Subordinate**: Slow Pick & Place to 55/hr (don't overproduce WIP before oven)
- **Elevate**: If needed, add second reflow oven → double capacity

### Incorrect Application
- Bought a faster Pick & Place machine (80→120/hr) → System throughput unchanged because Reflow Oven (50/hr) is still the bottleneck. Wasted investment. Violates Iron Law.

## Gotchas

- **Constraints can be non-physical**: Market demand, policy, or management attention can be the real constraint. If the factory can produce 1000 but only sells 500, the market is the constraint.
- **Moving bottleneck**: After elevating one constraint, the bottleneck shifts. Teams often celebrate and forget Step 5 (Repeat).
- **Subordination is counterintuitive**: Running non-bottleneck machines at less than full capacity feels wasteful. It's not — overproduction at non-bottlenecks creates WIP that clogs the system.
- **TOC vs Lean**: Lean eliminates waste everywhere. TOC focuses only on the constraint. They complement each other: use TOC to find WHERE to focus, Lean to optimize HOW.

## References

- For Drum-Buffer-Rope implementation details, see `references/dbr-scheduling.md`

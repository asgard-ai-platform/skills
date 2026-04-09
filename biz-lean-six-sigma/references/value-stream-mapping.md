# Value Stream Mapping

Value Stream Mapping (VSM) is a pencil-and-paper tool that makes the entire flow of a product or service visible — from raw input to customer delivery — so waste can be seen, measured, and eliminated systematically.

VSM is the diagnostic step that precedes DMAIC. It answers "where exactly is the waste?" before you commit to fixing anything.

---

## Core Concept: Current State vs. Future State

VSM always produces two maps:

1. **Current State Map** — what actually happens today (not what the SOP says)
2. **Future State Map** — the target condition after waste is removed

The gap between them becomes your improvement roadmap.

---

## Key Metrics

Before drawing anything, agree on these four numbers for each process step:

| Symbol | Name | Definition |
|--------|------|-----------|
| **C/T** | Cycle Time | Time to complete one unit from start to finish at this step |
| **C/O** | Changeover Time | Time to switch from one product/job type to another |
| **Uptime** | Availability | % of scheduled time the step is actually running |
| **Inventory** | Queue Depth | Number of units waiting in front of this step |

### Timeline Calculation

At the bottom of a current state map, draw the "timeline ladder":

```
Value-Added Time (VAT) = sum of all C/T values across steps
Lead Time (LT)         = VAT + all queue/wait times between steps
Process Efficiency     = VAT / LT × 100%
```

**Worked example:**

A purchase-order approval process has 5 steps:

| Step | C/T (min) | Wait before step (min) |
|------|-----------|----------------------|
| Submit PO | 5 | 0 |
| Manager review | 10 | 240 (sits in inbox) |
| Finance check | 8 | 480 (batch processed next day) |
| System entry | 3 | 60 |
| Vendor notification | 2 | 120 |
| **Total** | **28** | **900** |

```
VAT = 5 + 10 + 8 + 3 + 2 = 28 min
LT  = 28 + 900 = 928 min (≈ 15.5 hours)
Process Efficiency = 28 / 928 = 3.0%
```

A 3% efficiency rate is typical for office/service processes. Manufacturing targets 15–35%; world-class is 50%+.

---

## Standard VSM Symbols

You don't need specialized software. These symbols work on a whiteboard or paper:

```
Customer / Supplier:    [Factory icon] — draw a box with a small building

Process Step:           [Rectangle] — one box per step, data box beneath it
                        ┌──────────────┐
                        │  Step Name   │
                        ├──────────────┤
                        │ C/T = x min  │
                        │ C/O = x min  │
                        │ Uptime = x%  │
                        └──────────────┘

Push Arrow:             ──────►  (material is pushed whether downstream is ready)
Pull / Kanban Signal:   ──○──►  (downstream pulls only when needed)
Inventory Triangle:     ▲ (with quantity below it)
Information Flow:       --------► (dotted = electronic, straight = manual)
Kaizen Burst:           ★ (starburst shape = improvement opportunity)
Timeline:               ___/‾‾‾ ladder at the bottom
```

---

## Step-by-Step: Drawing the Current State Map

### Step 1 — Define the Product Family

VSM maps ONE product family at a time. A product family = items that go through the same process steps in roughly the same sequence.

Use a **Product-Process Matrix**:

```
               Step A  Step B  Step C  Step D  Step E
Product X        ✓       ✓       ✓               ✓
Product Y        ✓       ✓       ✓       ✓       ✓
Product Z                ✓               ✓       ✓
```

Product X and Y share Steps A, B, C, E → they form a family. Map them together.

### Step 2 — Walk the Process (Physically)

Start at the shipping/delivery end, walk **upstream** to the raw input. Never map from memory or from an SOP document.

For each step, record:
- Who does it?
- C/T (time one person, one unit)
- Batch size (if batched)
- Number of people
- Working hours per shift
- Defect/rework rate

### Step 3 — Draw the Process Boxes Left to Right

Place customer (top right), supplier (top left), process steps (middle row, left to right), inventory triangles between steps.

### Step 4 — Add Information Flows

Map how work gets triggered:
- Does step B start because step A **pushed** work to it?
- Or does step B **pull** from a queue only when it has capacity?

This reveals overproduction waste (push systems often create WIP pile-ups).

### Step 5 — Draw the Timeline Ladder

At the bottom, alternate between queue time (on top of the zigzag) and C/T (on the bottom):

```
Queue → Step → Queue → Step → Queue → Step
 240     5      480     10     60      8    ...
```

Sum the top row = Lead Time from waits
Sum the bottom row = VAT

---

## Identifying Waste on the Map

Once drawn, apply these checks systematically:

### Constraint Identification (Bottleneck)

The **bottleneck** is the slowest step — it controls throughput for the entire stream.

```
Takt Time = Available Production Time / Customer Demand Rate
```

**Example:**
- 480 min/day available (one 8-hour shift)
- Customer orders 60 units/day

```
Takt Time = 480 / 60 = 8 min/unit
```

Any step with C/T > 8 min cannot keep up with demand — it is a constraint.

Compare each step's C/T to Takt Time on a bar chart (called a **Time Observation Chart**):

```
C/T (min)
  12 │          ████
  10 │          ████
   8 │ ────────────────── Takt = 8 min
   6 │ ████               ████
   4 │ ████               ████
   2 │ ████               ████
   0 └──────────────────────────
     Step A   Step B   Step C
```

Step B (C/T = 12 min) is the bottleneck. Fix it first.

### Push vs. Pull Analysis

Every push arrow (──►) between steps that has a large inventory triangle in front of it is a candidate for conversion to a pull/kanban system.

Rule of thumb: if inventory > 2× the downstream step's daily consumption, the push system is overproducing.

### Information Flow Gaps

If a step has no incoming information arrow, it either runs on memory, habit, or a paper system that isn't visible on the map. These are defect-risk points.

---

## Drawing the Future State Map

Apply the following design questions in order — each answers a specific class of waste:

| # | Question | Waste Addressed |
|---|----------|----------------|
| 1 | What is the Takt Time? | Overproduction |
| 2 | Will you ship from finished goods or make-to-order? | Inventory, Waiting |
| 3 | Where can you use continuous flow? | Transportation, Motion, Waiting |
| 4 | Where must you use a pull system (supermarket)? | Overproduction, Inventory |
| 5 | What single point controls production scheduling? | Overproduction |
| 6 | What process improvements are needed at constraints? | Defects, Waiting |

### Supermarket Pull System

When continuous flow is not possible between steps (because they run at different speeds, locations, or frequencies), use a **supermarket**:

```
Upstream Step ──produces to──► [Supermarket] ◄──pulls from── Downstream Step
                                  (buffer stock
                                   with min/max)
```

Supermarket rules:
- Set a **Max** quantity (never exceed)
- Set a **Min / Reorder Point** (triggers upstream to produce more)
- Upstream only produces when the supermarket drops below min

### FIFO Lanes

Where a supermarket is impractical (custom orders, long changeover), use a FIFO lane:

```
Step A ──FIFO──► Step B
        max: 10 units
```

Upstream stops producing when FIFO lane is full. This caps WIP without a full kanban system.

---

## Worked Example: Software Bug Triage Process

### Current State

**Steps and data:**

| Step | C/T | C/O | Uptime | Queue before |
|------|-----|-----|--------|-------------|
| Bug reported | 2 min | — | 100% | 0 |
| Triage (L1 support) | 15 min | — | 80% | 45 min (avg 3 bugs waiting) |
| Reproduce (QA) | 40 min | — | 70% | 3 hrs (batch: QA runs at 2pm only) |
| Fix (Dev) | 120 min | — | 65% | 6 hrs (sprint queue) |
| Verify (QA) | 20 min | — | 70% | 2 hrs |
| Deploy | 5 min | 30 min | 90% | 4 hrs (deploy window: 3pm only) |

```
VAT = 2 + 15 + 40 + 120 + 20 + 5 = 202 min
Wait = 0 + 45 + 180 + 360 + 120 + 240 = 945 min
LT  = 202 + 945 = 1,147 min ≈ 19 hours
Process Efficiency = 202 / 1,147 = 17.6%
```

**Customer Takt Time:**
- Support team handles bugs 8 hours/day
- 16 bugs reported/day
- Takt = 480 / 16 = 30 min/bug

Constraint: Dev step (C/T = 120 min) far exceeds Takt of 30 min. Secondary constraint: Reproduce step (C/T = 40 min).

**Kaizen bursts on current state map:**
- ★ QA batches at 2pm → move to continuous pull
- ★ Deploy window 3pm only → move to on-demand deploy
- ★ Dev queue 6 hrs → investigate sprint sizing

### Future State Design

| Question | Answer |
|----------|--------|
| Takt Time? | 30 min |
| Ship to? | On-demand deploy (continuous) |
| Continuous flow possible? | Triage → Reproduce → Verify (all < Takt) |
| Pull system needed? | Dev step (bottleneck; needs queue cap) |
| Pacemaker (scheduling point)? | Triage (first step) |
| Constraint improvement? | Pair programming to halve Dev C/T |

**Future state targets:**

| Step | Current C/T | Future C/T | Change |
|------|------------|-----------|--------|
| Bug reported | 2 min | 2 min | — |
| Triage | 15 min | 15 min | — |
| Reproduce | 40 min | 25 min | Parallel env setup |
| Fix (Dev) | 120 min | 60 min | Pair programming |
| Verify | 20 min | 20 min | — |
| Deploy | 5 min | 5 min | — |

```
Future VAT = 2 + 15 + 25 + 60 + 20 + 5 = 127 min
Future Wait = 0 + 10 + 15 + 60 + 15 + 10 = 110 min (pull system caps queues)
Future LT  = 127 + 110 = 237 min ≈ 4 hours
Process Efficiency = 127 / 237 = 53.6%
```

Lead time improvement: 19 hours → 4 hours (79% reduction).

---

## Common VSM Mistakes

**Mapping the SOP instead of reality.** The map must reflect what workers actually do, not what the procedure says. If you're not on the floor/observing the screen, you're guessing.

**One box per department instead of per step.** "Engineering" is not a process step. Each distinct transformation (design, review, sign-off) gets its own box.

**Ignoring information flows.** A material flow map without information flows is incomplete. Most office process waste lives in how work gets triggered and communicated, not in the work itself.

**Mapping everything at once.** VSM is a product-family tool. Mapping all products through all steps produces an unreadable spaghetti map with no actionable insight.

**Future state with no Takt Time anchor.** The future state must be designed around Takt Time. Without it, you're guessing whether your "improvements" can actually meet demand.

**Confusing cycle time with lead time.** C/T = how long one unit takes at one step. LT = how long from first step to delivery, including all waits. A process with C/T = 5 min/step and 6 steps does NOT have a 30-minute lead time if there are 3-hour queues between steps.

---

## Data Collection Sheet Template

Use this on the factory floor or during process observation:

```
Process Step: ___________________
Observer: ___________________  Date: ___________

Observations (take 10 samples):
  Run 1: _____ min    Run 6: _____ min
  Run 2: _____ min    Run 7: _____ min
  Run 3: _____ min    Run 8: _____ min
  Run 4: _____ min    Run 9: _____ min
  Run 5: _____ min    Run 10: _____ min

  Average C/T: _____ min
  Min: _____ / Max: _____ (flag if max > 2× min — high variation, investigate)

Inventory count in queue: _____ units
Workers at this step: _____
Shifts/day: _____
Defect/rework rate: _____%
Changeover required? Y / N   If yes, C/O = _____ min
```

Take 10 observations minimum. Use the average, not the fastest (cherry-picking the best time creates an unachievable future state target).

---

## When VSM Is Not the Right Tool

VSM works best for **repetitive, linear flows** with measurable steps. It loses value when:

- The process is highly variable or project-based (each instance is unique) → use a **swimlane process map** instead
- The bottleneck is known and confirmed → skip straight to constraint analysis (Theory of Constraints)
- You need to model complex branching logic → use a **BPMN process model**
- The problem is a one-time defect, not a systematic flow issue → jump to **5 Whys / fishbone** directly

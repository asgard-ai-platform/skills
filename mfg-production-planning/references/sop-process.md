# S&OP (Sales & Operations Planning) Process Design

S&OP sits at the top of the planning hierarchy. Its job is to reconcile **demand** (what Sales/Marketing expects to sell) with **supply** (what Operations can produce) over a 12–18 month rolling horizon, at the product-family level, on a monthly cadence.

Output: a consensus operating plan that feeds the MPS directly — the MPS is a weekly decomposition of the monthly S&OP numbers.

---

## The Monthly S&OP Cycle

S&OP is not a single meeting. It is a five-step process that runs every month, each step building on the last.

```
Week 1: Data refresh
Week 2: Demand review meeting
Week 3: Supply review meeting
Week 4: Pre-S&OP (gap resolution)
Week 4 (end): Executive S&OP (decisions and sign-off)
```

### Step 1 — Data Refresh (Week 1)

Automated. Pull actuals from ERP/WMS and rebase rolling forecasts.

| Data input | Source | Owner |
|------------|--------|-------|
| Actual sales last month | ERP | Finance |
| Current inventory (RM, WIP, FG) | WMS | Warehouse |
| Open purchase orders / receipts | ERP | Procurement |
| Production actuals vs. plan | MES/ERP | Operations |
| Updated statistical forecast | Forecasting tool | Demand planning |

Deliverable: updated demand and supply datasets, distributed to step 2 owners 48 hours before Demand Review.

---

### Step 2 — Demand Review (Week 2)

**Owner**: Demand Planning + Sales + Marketing  
**Duration**: 2–3 hours

Goal: produce a single, consensus demand plan (volume, not revenue) for the next 18 months by product family.

#### Demand Review Agenda

1. Actuals vs. last month's plan — where did we miss and why?
2. Statistical baseline forecast — what does the model say?
3. Sales intelligence overlay — pipeline, promotions, NPI, account wins/losses
4. Reconcile to consensus demand plan
5. Flag assumptions and risks

#### Reconciliation Formula

```
Consensus Demand(t) = Statistical Forecast(t) × Bias Correction Factor
                     + Incremental Intelligence(t)
```

Where:
- `Bias Correction Factor = mean(Actual / Statistical Forecast)` over last 6 months
- `Incremental Intelligence` = sales team adjustments (positive or negative), must be justified by named opportunity or event

**Rule**: Sales overrides require written justification. If override volume > 15% of baseline, flag for executive review.

#### Forecast Accuracy Tracking (required input to demand review)

Track MAPE by product family each month:

```
MAPE = (1/n) × Σ |Actual(t) - Forecast(t-1)| / Actual(t) × 100%
```

| MAPE band | Implication for S&OP |
|-----------|----------------------|
| < 10% | Statistical model is reliable; minimal sales overlay needed |
| 10–25% | Normal; overlay is valuable; track override accuracy separately |
| 25–40% | High variability; increase safety stock; shorten frozen zone horizon |
| > 40% | Demand signal is broken; investigate root cause before trusting plan |

Deliverable: **Consensus Demand Plan** — a 18-month rolling table by product family, in units, by month.

---

### Step 3 — Supply Review (Week 3)

**Owner**: Operations + Supply Chain + Procurement  
**Duration**: 2–3 hours

Goal: compare demand plan against supply capability; surface gaps.

#### Rough-Cut Capacity Planning (RCCP)

RCCP is the only capacity check at the S&OP level. It uses **resource profiles** (not detailed routing) to test whether the demand plan is feasible.

**Resource Profile**: hours of a key resource required per unit of product family.

```
Capacity Load(t) = Σ_f [Demand(f,t) × ResourceProfile(f)]
Available Capacity(t) = WorkingDays(t) × Shifts × Hours/Shift × # Resources × OEE
Gap(t) = Capacity Load(t) - Available Capacity(t)
```

Where `f` = product family, `t` = month.

#### Worked Example

Product families: **A-Series** (industrial pumps), **B-Series** (custom valves)

Resource profile (assembly hours per unit):

| Family | Assembly (hrs/unit) | Paint booth (hrs/unit) |
|--------|--------------------|-----------------------|
| A-Series | 4.5 | 1.2 |
| B-Series | 6.0 | 0.8 |

Demand plan (units):

| Month | A-Series | B-Series |
|-------|----------|----------|
| May | 120 | 80 |
| Jun | 150 | 90 |
| Jul | 130 | 100 |

Available capacity: 22 working days × 1 shift × 8 hours × 4 assembly stations × 0.85 OEE = **599 assembly hours/month**

Available paint booth: 22 × 1 × 8 × 1 booth × 0.90 OEE = **158 hours/month**

Capacity load calculation (May):

```
Assembly load = 120 × 4.5 + 80 × 6.0 = 540 + 480 = 1,020 hrs
Gap = 1,020 - 599 = −421 hrs (OVERLOADED: 170% utilization)

Paint booth load = 120 × 1.2 + 80 × 0.8 = 144 + 64 = 208 hrs
Gap = 208 - 158 = −50 hrs (OVERLOADED: 132% utilization)
```

This gap must be resolved before the plan proceeds. Options to surface at Pre-S&OP:

1. Add overtime (assembly: increases available hours by ~10%, closes ~17% of gap)
2. Add shift (doubles capacity, closes all gap, cost impact required)
3. Outsource B-Series final assembly to contract manufacturer
4. Defer some demand to June (if customer allows)
5. Push back on demand plan — is May forecast correct?

Deliverable: **Supply Capability Statement** — capacity load vs. availability by resource by month, gaps highlighted, options listed (not yet decided).

---

### Step 4 — Pre-S&OP (Week 4, Early)

**Owner**: Supply Chain Director / S&OP Manager  
**Duration**: 2–3 hours  
**Attendees**: Demand Planning, Operations, Procurement, Finance — **not** executives yet

Goal: resolve gaps where possible at the working level; escalate only true decisions to executives.

#### Gap Resolution Decision Tree

```
Gap identified?
│
├─ Can it be resolved within policy limits (no capex, no price change)?
│   ├─ YES → Resolve and document. Do not escalate.
│   └─ NO → Escalate to Executive S&OP with options and recommendation.
│
└─ Is it a demand-shaping lever (promotions, pricing, mix shift)?
    ├─ YES → Bring to Executive S&OP with revenue/margin impact modeled.
    └─ NO → Treat as supply-side gap resolution.
```

#### Pre-S&OP Scenarios

For each gap, pre-S&OP prepares **2–3 scenarios** for executive choice:

| Scenario | Action | Capacity gain | Cost impact | Risk |
|----------|--------|--------------|-------------|------|
| Base | No change | 0 | $0 | 421 hrs short in May |
| Overtime | 10% OT on assembly | +60 hrs | +$18k/mo | Fatigue risk, covers ~14% of gap |
| Second shift | Add afternoon shift | +599 hrs | +$65k/mo | Hiring lead time 6 weeks |
| Outsource B-Series | 3PL assembly | +480 hrs equivalent | +$42k/mo | Quality audit required |
| **Recommended** | Outsource + OT | +540 hrs | +$60k/mo | Closes gap; quality risk manageable |

Pre-S&OP does **not** make the call — it presents a clear recommendation with supporting data.

Deliverable: **Pre-S&OP Package** — scenarios with financial and operational impact, a recommendation, and the list of items requiring executive decisions.

---

### Step 5 — Executive S&OP (Week 4, End)

**Owner**: General Manager / VP Operations  
**Attendees**: CEO/GM, VP Sales, VP Operations, CFO, VP Supply Chain  
**Duration**: 60–90 minutes (max 2 hours)

This meeting is a **decision meeting**, not a review meeting. All reviews happen in steps 2–4.

#### Executive S&OP Agenda (strict)

| Time | Topic | Decision required? |
|------|-------|-------------------|
| 0–10 min | KPI dashboard — how did we perform last month? | No |
| 10–25 min | Demand plan summary — key changes from last month | No |
| 25–45 min | Gap resolution — scenarios and recommendation | **YES** |
| 45–60 min | Financial reconciliation — does the plan match budget? | **YES** |
| 60–75 min | Escalations (if any) — market changes, major risks | **YES** |
| 75–90 min | Summary of decisions, owners, due dates | No |

**Rule**: if the agenda hits 60 minutes and no decision has been made, the meeting has failed. Pre-S&OP preparation was insufficient.

#### Financial Reconciliation Check

The approved S&OP plan must reconcile to the financial plan:

```
S&OP Revenue = Σ_f [Approved Volume(f,t) × ASP(f)]
Budget Revenue = Financial plan

Variance = |S&OP Revenue - Budget Revenue| / Budget Revenue × 100%
```

| Variance band | Action |
|--------------|--------|
| < 3% | Approve; note variance |
| 3–8% | CFO must sign off; update rolling financial forecast |
| > 8% | Requires board notification if >2 months running; reforecast |

Deliverable: **Signed S&OP Plan** — approved volume by product family by month, documented decisions, assigned owners for open items.

---

## From S&OP to MPS: The Disaggregation Step

S&OP output is in monthly units by product family. MPS needs weekly units by SKU. The disaggregation bridge must be explicit.

### Step 1: Allocate Monthly Volume to Weeks

Default: prorate by working days in each week.

```
Weekly Volume(sku, w) = Monthly Volume(family, m)
                        × SKU Mix%(sku within family)
                        × WorkingDays(w) / WorkingDays(m)
```

SKU mix % comes from historical mix or committed customer orders. Use committed orders first; fill remaining with mix-based allocation.

### Step 2: Apply Frozen Zone

The first 1–2 weeks of MPS are frozen — no changes from S&OP disaggregation or otherwise. This is enforced in the MPS review, not S&OP itself, but S&OP must be completed early enough to allow it.

**S&OP calendar constraint**: Executive S&OP must complete by the 25th of month M so that MPS for month M+1 week 1 is stable before month M ends.

### Step 3: Cross-Check Rough-Cut

After disaggregation, run RCCP again at the weekly level. Weekly peaks can violate monthly-average capacity even when monthly total looks feasible.

```
If any weekly load > 110% of available capacity:
  → Shift production forward (if inventory policy allows)
  → Or flag for MPS planner to resolve via sequencing
```

---

## S&OP Maturity Levels

Most plants are at Level 1 or 2. Targeting Level 3 is realistic for a mid-size manufacturer in 12–18 months.

| Level | Characteristics | Typical MAPE | Plan stability |
|-------|----------------|-------------|----------------|
| **1 — Reactive** | No formal S&OP; firefighting; planning done individually per department | > 35% | Changes weekly |
| **2 — Functional** | Monthly meetings; demand and supply reviewed separately; limited cross-functional integration | 20–35% | Changes every 2 weeks |
| **3 — Integrated** | Full 5-step cycle; consensus plan; RCCP done; financial reconciliation | 10–20% | Frozen zone respected |
| **4 — Optimized** | Scenario planning; demand shaping levers actively managed; integrated with supplier S&OP | < 10% | Horizon-based freezing |

**Implementation path to Level 3** (roughly 12 months):

1. Month 1–2: Establish data infrastructure (actuals, inventory, open orders in one place)
2. Month 3–4: Run demand review and supply review as separate meetings; do not try to combine yet
3. Month 5–6: Add RCCP calculation, even if manual spreadsheet
4. Month 7–9: Add Pre-S&OP step; start escalation discipline
5. Month 10–12: Add financial reconciliation; achieve Executive S&OP ≤ 90 minutes

---

## Common S&OP Failure Modes

| Failure | Root cause | Fix |
|---------|-----------|-----|
| S&OP becomes a status update meeting | No decisions required; executives not accountable | Redesign agenda around explicit decision points; pre-read distributed 48h before |
| Demand plan never changes from last month | Sales team sandbagging; no override accountability | Track override accuracy separately; create positive/negative override scorecards |
| Supply always says "we can do it" | RCCP not done; optimism bias | Make RCCP mandatory output of Supply Review; show the math |
| Plan changes inside frozen zone constantly | Frozen zone not enforced; urgency culture | Gate changes inside frozen zone at VP level; count violations as a KPI |
| S&OP volume doesn't match financial forecast | Finance not in the loop | Add CFO attendance and financial reconciliation to Executive S&OP |
| S&OP process abandoned after 3 months | Too complex for current data maturity | Start with 2-step (Demand Review + one combined meeting); grow into 5-step |

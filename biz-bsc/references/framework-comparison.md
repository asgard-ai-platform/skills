# Framework Comparison: BSC vs. OKR vs. MBO vs. KPI Dashboard

This document compares four common performance frameworks so you can advise on which to use, when to combine them, and how to avoid conflating them.

---

## The Four Frameworks at a Glance

| Dimension | BSC | OKR | MBO | KPI Dashboard |
|-----------|-----|-----|-----|---------------|
| Origin | Kaplan & Norton, 1992 | Intel/Google, ~1970s/1999 | Peter Drucker, 1954 | Varies |
| Primary purpose | Translate strategy into execution | Set ambitious short-cycle goals | Align manager-employee objectives | Monitor operational health |
| Time horizon | 3–5 years (strategic) | Quarterly (sometimes annual) | Annual | Real-time to monthly |
| Causal structure | Required (4 perspectives, causal chain) | None required | None required | None required |
| Measurement style | Lagging + leading, balanced | Key Results are measurable outcomes | Targets per objective | Metrics as-is |
| Who uses it | Executive team → departments | Company → teams → individuals | Manager → direct report | Operations, analysts |
| Strategy embedded? | Yes — strategy statement is input | Partially (North Star) | Rarely | No |

---

## BSC vs. OKR — The Most Common Confusion

### Structural Difference

**BSC** is a *strategic management system*. It forces you to answer: does our daily work connect to our strategy? It requires:
1. A strategy statement
2. Four causally linked perspectives
3. Objectives + Measures + Targets + Initiatives per cell

**OKR** is a *goal-setting framework*. It forces ambitious, time-boxed commitment. It requires:
1. An Objective (qualitative, inspirational)
2. 2–5 Key Results per Objective (measurable, binary success/fail)
3. No mandatory causal structure across areas

### A Worked Example: Same Company, Two Frameworks

**Scenario:** B2B SaaS company, strategy "Grow through product-led growth"

**BSC version:**

| Perspective | Objective | Measure | Target | Initiative |
|------------|-----------|---------|--------|-----------|
| Financial | Increase ARR | ARR | $10M by Q4 | Expand pricing tiers |
| Customer | Improve retention | Net Revenue Retention | >110% | Launch CS program |
| Internal | Accelerate releases | Release cycle | 2 weeks | CI/CD adoption |
| L&G | Build analytics skills | % team trained | 100% by Q2 | Analytics bootcamp |

The causal chain is explicit: training → faster data-driven releases → retention → ARR.

**OKR version (same quarter):**

```
O: Make our product the stickiest in the mid-market segment
  KR1: Net Revenue Retention ≥ 110% by end of Q2
  KR2: Time-to-value for new accounts ≤ 14 days (from 30)
  KR3: Product-qualified leads from in-app triggers ≥ 200/month

O: Ship faster without breaking things
  KR1: Release cycle ≤ 2 weeks by Q2
  KR2: Production incidents caused by releases < 2/quarter
  KR3: CI/CD pipeline coverage ≥ 90% of services
```

**What's missing from OKR alone:** No explicit link between "Ship faster" and "Sticky product." No L&G investment tracked. No strategy map showing *why* these OKRs were chosen. If leadership changes priorities next quarter, the OKRs reset — the strategic logic is lost.

**What's missing from BSC alone:** No ambitious stretch targets. No quarterly cadence to review and adjust. The BSC Initiatives are vague compared to OKR Key Results.

---

## When to Use Which

### Decision Rules

**Use BSC when:**
- The organization lacks strategic alignment (different teams optimize for different things)
- You need to explain *why* certain KPIs matter, not just *what* they are
- Executive team wants a board-level view of strategy execution
- The company has never connected HR/L&G investment to business outcomes
- Time horizon is 2+ years

**Use OKR when:**
- Teams need clarity on quarterly priorities and are willing to be held accountable
- Culture supports transparent goal-sharing across functions
- Growth environment where speed and ambition matter more than precision
- You already have a strategy (BSC or otherwise) and need execution discipline per cycle

**Use MBO when:**
- Primary need is manager-employee performance reviews
- Organization is hierarchical and annual review cycles are the norm
- Goals are individual-level, not team or cross-functional

**Use KPI Dashboard when:**
- Operational monitoring, not strategic direction
- You need real-time or daily alerts (uptime, support tickets, conversion)
- Audience is individual contributors, not leadership

**Use BSC + OKR together when:**
- BSC is the 3-year strategic anchor; OKRs are the quarterly execution cadence
- Corporate BSC → Department OKRs → Individual Key Results cascade

---

## BSC + OKR Integration Pattern

This is the most common hybrid in practice. The mapping is:

```
BSC Layer (annual/multi-year)         OKR Layer (quarterly)
─────────────────────────────         ──────────────────────
Strategy Statement                 →  Company-level O (North Star)
Financial Objectives               →  Finance team OKRs
Customer Objectives                →  Growth/CX team OKRs
Internal Process Objectives        →  Engineering/Ops team OKRs
L&G Objectives                     →  People/HR team OKRs

BSC Initiatives                    →  OKR Key Results (specific, time-boxed)
BSC Targets (annual)               →  OKR Key Results (quarterly milestones)
```

**Integration rule:** Every company-level OKR should map to at least one BSC objective. If an OKR cannot be traced to the BSC, either the BSC is incomplete or the OKR is off-strategy.

**Anti-pattern:** Writing OKRs that only track Financial perspective metrics. This recreates the pre-BSC mistake of managing only what finance reports. If all your OKRs are revenue or cost, you have no leading indicators.

---

## BSC vs. MBO

MBO (Management by Objectives) is frequently confused with BSC because both use "objectives." The difference is structural.

| | BSC | MBO |
|--|-----|-----|
| Unit of analysis | Organization/department | Individual manager or employee |
| Causal logic | Required — perspectives link | Not required |
| Strategic input | Strategy statement drives design | Manager-employee negotiation |
| Balanced across domains? | Yes — four mandated perspectives | No — whatever objectives are agreed |
| Typical failure mode | KPI dump without causal links | Gaming: optimizing agreed metrics, ignoring everything else |

MBO predates BSC. Kaplan and Norton designed BSC partly *because* MBO was producing locally-optimized, strategically-disconnected results. If a client says "we already do MBO," the BSC is an upgrade to that system, not a replacement for performance reviews.

---

## BSC vs. KPI Dashboard

A KPI dashboard is a monitoring tool. A BSC is a strategy execution tool. They are not competitors.

**KPI Dashboard alone fails when:**
- Metrics are chosen bottom-up ("what can we measure?") rather than top-down ("what does our strategy require?")
- No target exists for each metric — the dashboard shows numbers, not health
- Metrics have no owner and no initiative — you see a problem but no one acts

**The BSC produces the *right* KPIs for a dashboard.** The typical sequence:
1. Build BSC → identify the 15-25 strategic measures
2. Add operational monitors (uptime, NPS raw score, cash balance) that aren't in BSC
3. Dashboard = BSC measures + operational monitors, separated visually

If someone shows you a 60-metric dashboard and calls it a BSC, it is not a BSC. It is a KPI dump. The BSC produces 3–5 objectives per perspective × 4 perspectives = 12–20 measures maximum.

---

## Choosing in Practice: Quick Decision Table

```
Does the client have a clear, stated strategy?
├── No  → Start with strategy work (SWOT, Porter's) before any framework
└── Yes → Continue

Do they need to align multiple departments to that strategy?
├── Yes → Use BSC (strategy map + four perspectives)
└── No  → Continue

Do they need quarterly goal-setting and accountability cycles?
├── Yes → Use OKR (with BSC as anchor if strategy alignment is also needed)
└── No  → Continue

Do they need individual performance management?
├── Yes → Use MBO (or cascade from BSC/OKR)
└── No  → Continue

Do they just need to monitor operations day-to-day?
└── KPI Dashboard (feed it metrics from BSC if BSC exists)
```

---

## Common Mistakes When Comparing Frameworks

**Mistake 1 — Treating OKR as a replacement for BSC**
OKR has no four-perspective structure and no causal chain requirement. You can write OKRs entirely in the Financial perspective and call it done. BSC won't allow that. They solve different problems.

**Mistake 2 — Implementing both BSC and OKR independently**
Two strategy systems running in parallel without integration means each team gets two sets of goals. The integration rule above (BSC objectives → OKR Key Results) avoids this. One strategy, two cadences.

**Mistake 3 — Calling a spreadsheet of KPIs a BSC**
The label "Balanced Scorecard" requires: four perspectives, causal links, and objectives with all three of measure + target + initiative. Without all three properties, rename it a KPI tracker to be accurate.

**Mistake 4 — Using BSC for team-level goal-setting**
BSC is designed for organization or business-unit level. A five-person team does not need a four-perspective strategy map. OKR or simple goal lists work better at that granularity. Cascading BSC to team level produces bureaucracy, not clarity.

# Example: SaaS Customer Support Death Spiral

## Scenario

**User's question:**

> We're a 120-person B2B SaaS company (Meridian Analytics, $18M ARR). Over the past 18 months we've been stuck in a loop we can't break out of. Support ticket volume keeps growing — we're now at ~2,400 tickets/month, up from 800. We hired more support agents (4 → 11), but CSAT dropped from 4.6 to 3.9 and churn crept from 1.8% to 3.1% monthly. Every time we "fix" it — add headcount, add an FAQ, run a training sprint — volume spikes again within 6 weeks. What is actually going on here?

---

## Analysis

### Step 1 — Define the System Boundary

**In scope:**
- Customer support team and ticket routing
- Product quality (bugs, UX friction, missing features)
- Customer success / onboarding
- Churn and expansion revenue

**Out of scope:**
- Sales pipeline and lead quality (upstream; no feedback path identified yet)
- Infrastructure reliability (separate incident process)

---

### Step 2 — Map Key Variables (Stocks and Flows)

| Variable | Type | Current Value |
|---|---|---|
| Unresolved customer confusion | Stock | HIGH (proxy: 2,400 tickets/mo) |
| Support team headcount | Stock | 11 agents |
| Product defect rate | Stock | Estimated high (inferred from ticket categories) |
| CSAT score | Flow (output) | 3.9 / 5.0 |
| Monthly churn | Flow (output) | 3.1% |
| Agent experience / efficiency | Stock | Degrading (high turnover on support team) |

---

### Step 3 — Identify Feedback Loops

**Reinforcing Loop R1 — "Complexity Flywheel"**

```
More tickets → agents more rushed → worse ticket resolution quality
→ customers re-open tickets or churn-and-return contacts
→ even more tickets
```

This is a *Fixes That Fail* archetype: hiring more agents addresses
the symptom (queue depth) but the rushed-resolution dynamic means
each ticket spawns 0.3–0.5 follow-up tickets, so the stock grows
faster than headcount can absorb it.

**Reinforcing Loop R2 — "Agent Burnout Loop"**

```
More tickets → agent overload → support agent turnover (~60%/yr)
→ inexperienced replacement agents → slower resolution, more errors
→ more re-contacts and escalations → more tickets
```

Every agent lost removes ~3 months of institutional knowledge. The
team's effective capacity is lower than headcount suggests.

**Balancing Loop B1 — "Churn Pressure" (intended)**

```
High churn → revenue pressure → leadership attention → resources allocated
→ interventions (hiring, FAQ, training) → queue temporarily shrinks
→ pressure releases → attention moves elsewhere → loop repeats
```

This is a *Shifting the Burden* archetype. Each intervention relieves
the pressure signal before the root cause (product confusion /
defect) is addressed, so the system snaps back within 6 weeks —
exactly what Meridian described.

**Balancing Loop B2 — "Self-Help Suppression"**

```
Poor CSAT → customers distrust self-service docs
→ customers skip help center and go straight to tickets
→ ticket volume stays high even as FAQ is updated
```

The FAQ investment fails because trust in self-service is a lagging
indicator of past CSAT. You can't fix self-service adoption by
writing more docs when customers have already learned "docs don't
help."

---

### Step 4 — Find Delays

| Cause | Effect | Delay |
|---|---|---|
| Product bug fix shipped | Ticket volume drops for that issue | 3–5 weeks (customers on old version, word spreads slowly) |
| New agent hired | Effective throughput gain | 10–14 weeks (ramp time) |
| CSAT improvement | Self-service trust recovers | 4–6 months |
| Churn reduction | ARR stabilizes | 2–3 months (contract cycles) |

**Critical insight:** Meridian is making decisions at weekly or
monthly cadence but the system's feedback delay is 10–14 weeks. They
see no results, assume the intervention failed, and add another
intervention — creating *policy churn* that the system never has
time to absorb.

---

### Step 5 — Locate Leverage Points

Ranked by impact-to-effort ratio (Meadows' hierarchy applied):

| Rank | Leverage Point | Why |
|---|---|---|
| 1 | **Ticket deflection at root cause** — classify top 20 ticket types, fix the 3 product/UX issues driving >40% of volume | Changes the *structure* of the reinforcing loop; reduces inflow regardless of team size |
| 2 | **Agent retention** — target <30% annual turnover via structured career ladder | Stops the R2 burnout loop; compounds experience rather than resetting it |
| 3 | **Freeze headcount for 90 days** — absorb the learning signal instead of hiring through it | Removes the pressure-release valve that suppresses the B1 signal; forces root-cause work |
| 4 | **CSAT recovery program** — proactive outreach to churned/low-CSAT accounts | Starts rebuilding self-service trust (B2 loop); 4–6 month lag, so must start now |

**Do NOT prioritize:** More FAQ articles, another training sprint,
ticket routing automation. These are within the system's current
structure — they will not change loop behavior.

---

### Step 6 — Unintended Consequences Check

| Proposed Intervention | Risk | Mitigant |
|---|---|---|
| Freeze headcount | Short-term queue depth increases; agents may quit | Set explicit 90-day window, communicate it clearly; add contractor flex for overflow |
| Fix top 3 product issues | Engineering team pulled off roadmap; may slow feature delivery | Frame as "churn prevention = retention revenue"; calculate cost of 3.1% monthly churn vs. engineer-weeks |
| Career ladder for support | Other teams may demand same; sets precedent | Coordinate with People team; frame as retention ROI |

---

## Result

```markdown
# Systems Analysis: Meridian Analytics Support Death Spiral

## System Boundary
- In scope: support ops, product quality, onboarding, churn
- Out of scope: sales pipeline, infrastructure reliability

## Key Variables
- Unresolved customer confusion (stock): HIGH, 2,400 tickets/mo
- Agent effective capacity (stock): DECLINING due to 60% annual turnover
- Product defect/UX friction (stock): HIGH (inferred)

## Feedback Loops
- Reinforcing R1: More tickets → rushed resolution → re-contacts → more tickets (Fixes That Fail)
- Reinforcing R2: Overload → agent burnout/turnover → inexperience → slower resolution → more tickets
- Balancing B1: Churn pressure → intervention → relief → attention shifts → root cause untouched (Shifting the Burden)
- Balancing B2: Low CSAT → distrust in self-service → all contacts become tickets

## Delays
- Bug fix → ticket volume drop: 3–5 weeks
- New agent → real throughput: 10–14 weeks
- CSAT improvement → self-service adoption: 4–6 months

## Leverage Points
1. Fix the top 3 product/UX issues driving >40% of ticket inflow — attack the root stock
2. Reduce agent turnover below 30%/yr — stop compounding inexperience
3. Freeze headcount for 90 days — let the pressure signal stay visible long enough to act on
4. Proactive CSAT outreach — begin rebuilding self-service trust now (6-month lag)

## Unintended Consequences Risk
- If we freeze headcount, queue depth will spike in weeks 2–4 before declining;
  communicate this to leadership or the pressure signal will trigger premature hiring again
- If we fix product issues without the hiring freeze, pressure relief may cause
  engineering to deprioritize the remaining fixes — watch for this in sprint planning
```

**Bottom line for Meridian:** The 6-week bounce-back pattern is not a
management failure — it is the system's balancing loop (B1) doing
exactly what it's designed to do: release pressure before the root
cause is fixed. The hiring interventions are feeding R2 (burnout)
while suppressing the signal that would force product fixes. Stop
hiring, classify the ticket taxonomy this week, and escalate the top
3 product issues to engineering with churn-cost framing.

# Example: Q2 Product Roadmap Prioritization Meeting

## Scenario

Layla Chen, Head of Product at **Stackwise** (a 60-person B2B SaaS company), runs a weekly product sync. The meeting keeps running over time, decisions get revisited in Slack two days later because "nobody wrote it down," and engineers start work on features that get deprioritized the following week. She pastes the following raw notes into Claude:

> "April 8 meeting. Attendees: Layla, Marcus (Eng Lead), Priya (Design), Tom (Sales), Wei (CEO).
> We talked about the mobile app — Tom says enterprise clients keep asking for it, Marcus says it's 3 months minimum. Priya showed the new onboarding flow mockups. CEO wants to launch mobile by June. Marcus pushed back hard. We also need to fix the CSV export bug, customers are complaining. And Priya's onboarding redesign — we said we'd decide today but didn't really. Tom is going to talk to the top 5 enterprise clients. Meeting was 70 minutes, supposed to be 45."

She asks: "Can you turn this into proper meeting minutes and tell me what went wrong?"

---

## Analysis

### Step 1 — Extract Decisions, Action Items, and Deferred Items

Reading the raw notes through the IRON LAW lens: **Were decisions made? Who owns what by when?**

**Decisions made:**
- CSV export bug: implicitly prioritized (customer complaints = urgent) — but no one was assigned
- Mobile app timeline: NOT resolved — Wei wants June, Marcus says impossible; this is a conflict, not a decision
- Onboarding redesign: explicitly deferred ("didn't really decide")

**Action items:**
- Tom → talk to top 5 enterprise clients (no deadline given)
- Priya's onboarding decision → carried to next meeting (no structure for it)
- CSV export bug fix → nobody assigned

**What went wrong:**
1. 25 minutes over — no time-boxing per agenda item
2. Mobile app discussion ended in conflict, not decision — that's a parking lot item until Wei and Marcus align offline
3. Three separate threads (mobile, onboarding, CSV) competed for attention without clear priority ordering
4. "Tom is going to talk to clients" has no deadline — this will not happen on schedule

### Step 2 — Reconstruct Structured Minutes

Apply the SKILL.md template, filling only what was actually established — flagging gaps explicitly.

### Step 3 — Flag Action Item Gaps

Use the WHO + WHAT + WHEN format to surface what's missing. "Talk to clients" → needs a deadline. CSV bug → needs an owner.

---

## Result

```markdown
# Meeting: Q2 Product Roadmap Prioritization
Date: 2026-04-08 | Time: 14:00–15:10 (ran 25 min over) | Location: Zoom
Attendees: Layla Chen (Product), Marcus Yeh (Engineering), Priya Nair (Design), Tom Gallagher (Sales), Wei Liu (CEO)
Absent: —
Facilitator: Layla Chen | Note-taker: Layla Chen

## Agenda
1. Mobile app — feasibility & timeline
2. Onboarding redesign — go/no-go decision
3. CSV export bug — priority & owner

## Discussion Notes

### Mobile App
- Tom: Top enterprise accounts (Kroll, Hartmann, 3 others) are requesting mobile access as a blocker to renewal
- Marcus: Minimum 3-month build; June launch would require starting now and cutting other roadmap items
- Wei: Wants June launch to use at flagship customer summit
- ⚠️ **NO DECISION REACHED** — June deadline conflicts with engineering estimate; escalation needed

### Onboarding Redesign
- Priya presented updated mockups; feedback was positive
- **DEFERRED**: Team ran out of time; decision moved to next meeting
- Priya to present a concise 5-min summary with a clear recommendation at Apr 15 meeting

### CSV Export Bug
- Multiple customer complaints; exact count not cited in meeting
- **DECISION**: Treat as P1; fix before any new feature work begins this sprint
- ⚠️ **Owner not assigned in meeting** — Layla to assign to an engineer by EOD April 8

## Action Items

| # | Action | Owner | Deadline | Status |
|---|--------|-------|----------|--------|
| 1 | Interview top 5 enterprise clients on mobile requirements; summarize findings in a 1-pager | Tom Gallagher | 2026-04-14 | Open |
| 2 | Prepare engineering scope breakdown for mobile (MVP vs. full) | Marcus Yeh | 2026-04-14 | Open |
| 3 | Wei + Marcus: 30-min alignment call on mobile June deadline feasibility | Layla to schedule | 2026-04-10 | Open |
| 4 | Assign CSV export bug to engineer; confirm fix in current sprint | Layla Chen | 2026-04-08 EOD | Open |
| 5 | Present onboarding redesign recommendation (5 min, go/no-go framing) | Priya Nair | 2026-04-15 meeting | Open |

## Parking Lot
- Mobile app June launch: BLOCKED pending Wei–Marcus alignment (Action #3)
- Onboarding redesign decision: carried to Apr 15

## Next Meeting
- Date: 2026-04-15, 14:00
- Required agenda: (1) Wei–Marcus mobile decision, (2) Onboarding go/no-go, (3) Action item review
```

---

**What went wrong — diagnosis for Layla:**

| Problem | Root Cause | Fix |
|---------|-----------|-----|
| Ran 25 min over | No time-box per topic | Set 15 min per topic; use visible timer |
| Mobile decision re-litigated in Slack | Conflict not surfaced as "parking lot" | When two decision-makers disagree, park it + schedule a bilateral |
| Tom's client outreach has no deadline | "ASAP" culture | Every action item gets a calendar date before leaving the room |
| CSV bug had no owner | Assumed someone would volunteer | Before closing a topic, ask: "Who owns this?" out loud |

**Template adoption note:** Layla should send these minutes by 5 PM on April 8. Action items reviewed first at April 15 meeting — before any new agenda items.

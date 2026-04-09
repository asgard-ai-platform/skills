# Negotiation Tactics for Resistant Stakeholders

This reference expands on the conflict management section of `soc-stakeholder`. It focuses specifically on **resistant stakeholders** — those who have the power or interest to block, slow, or undermine a project.

---

## The Position vs. Interest Distinction (Core Principle)

Every negotiation with a resistant stakeholder starts here. The SKILL.md calls this out explicitly because it's the most common mistake: treating what a stakeholder *says they want* as the actual problem.

| Term | Definition | Example |
|------|-----------|---------|
| **Position** | What they say they want; their stated demand | "We can't change the reporting system" |
| **Interest** | *Why* they want it; the underlying need or fear | Afraid team will lose months of custom reports; worried about their team's workload |

**Rule**: Never negotiate on positions. Always negotiate on interests.

### How to Surface Interests

Ask "why" questions, but indirectly — direct "why" can feel accusatory.

Instead of: "Why are you opposed to this?"

Use:
- "What concerns do you have about how this would work for your team?"
- "What would need to be true for this to work well from your perspective?"
- "What has your experience been with similar changes in the past?"
- "What would you lose if this went forward as proposed?"

Each answer reveals an interest. Collect at least 3 before proposing anything.

---

## Resistance Typology

Not all resistance is the same. Misdiagnosing the type leads to wrong tactics.

| Type | Signs | Root Cause | Wrong Tactic | Right Tactic |
|------|-------|-----------|-------------|-------------|
| **Information Gap** | "I'm not sure this is necessary" / asks many factual questions | They don't have the data you have | Persuasion / pressure | Provide evidence; walk through your analysis together |
| **Loss Aversion** | "What happens to my current process?" / focuses on what disappears | Fear of losing something they value (status, control, workflow) | Logic and ROI | Name the loss explicitly; offer concrete mitigation or compensation |
| **Distrust** | Agrees in meetings but delays or blocks afterward | Past experiences where similar promises weren't kept | Presenting a great plan | Relationship repair first; small visible commitments before big asks |
| **Value Conflict** | "This isn't how we do things here" / principled objections | Genuine disagreement about what's right, not just what's convenient | Finding middle ground on positions | Surface the value conflict explicitly; look for shared higher-order values |
| **Territorial** | "This overlaps with my team's mandate" | Perceived threat to authority, budget, or headcount | Minimizing their role | Formal role acknowledgment; make their involvement visible |

---

## The BATNA Calculation

Before any negotiation, calculate both parties' BATNA (Best Alternative To a Negotiated Agreement). This tells you how much leverage each side actually has.

```
Your BATNA    = best outcome if this stakeholder stays resistant
Their BATNA   = best outcome for them if they don't cooperate with you
```

**Practical steps:**

1. Write down what happens to the project if this stakeholder actively resists vs. stays neutral vs. supports.
2. Write down what the stakeholder loses or gains if the project succeeds without their involvement.
3. If their BATNA is better than cooperating, you need to change that — either by making cooperation more attractive or by making non-cooperation more costly (within ethical bounds).

**Example:**

> Project: Implementing a new procurement platform
> Resistant stakeholder: Procurement Manager (High Power, High Interest)
>
> Your BATNA if they stay resistant: Project gets delayed 6 months; must work around their team; higher risk of failure. Weak BATNA.
>
> Their BATNA if they don't cooperate: Platform gets implemented anyway (CEO-sponsored); they get excluded from design decisions; their team gets a system they hate. Also weak.
>
> Conclusion: Both sides have weak BATNAs. This creates real negotiating room — neither party benefits from impasse. Open with this framing explicitly.

---

## Four Negotiation Moves for Resistant Stakeholders

### Move 1: Acknowledge Before You Argue

State their position back to them — accurately, without sarcasm — before you make your own case. This is not agreement; it is validation.

**Structure:**
```
"What I hear you saying is [their position/interest].
Is that right?" → wait for confirmation
"That concern makes sense to me because [reason it's legitimate].
Here's what I'd like to share from our side..."
```

If you skip this, they spend the whole conversation waiting to be heard instead of listening to you.

---

### Move 2: Find the Legitimate Core

Every resistant stakeholder has at least one concern that is *correct*. Find it and say so out loud.

Resistant stakeholders expect to be dismissed. When you identify the part of their concern that is valid, you break the adversarial frame.

**Example:**

> Stakeholder: "This CRM migration will kill our Q4 pipeline. We can't do this now."
>
> Legitimate core: They're right that migration during peak sales season creates real risk.
>
> Response: "You're right that timing matters here. A Q4 cutover would create real disruption to active deals — that's a legitimate risk, not a minor objection. So let's talk about timing separately from whether we do this at all."

This separates the *timing* objection (valid) from the *project* objection (their real position may still be against it, but now you're negotiating on specifics instead of a binary).

---

### Move 3: Expand the Option Space

When two positions seem incompatible, it's usually because both sides are only considering the options already on the table. Generate new options before you try to agree.

**Brainstorm protocol (use this in the meeting):**
1. State the constraint: "We have a conflict between [their interest] and [our interest]."
2. Explicitly suspend evaluation: "Let's not decide anything yet — let's just generate options."
3. Generate at least 5 options together before evaluating any.
4. Evaluate against interests, not positions.

**Common option-expanding moves:**

| Move | Description | When to Use |
|------|-------------|------------|
| **Decouple timing from scope** | Agree on *what* but negotiate *when* | Resistance is about pace or readiness |
| **Pilot before full rollout** | De-risk by limiting initial scope | Resistance is about uncertainty/risk |
| **Add a role** | Give them formal involvement in the thing they're resisting | Resistance is territorial or about exclusion |
| **Add a veto trigger** | Define conditions under which the project pauses for review | Resistance is about loss of control |
| **Sequence changes** | Implement their dependent items first | Resistance is about something that must come before this |

---

### Move 4: Make Commitments Specific and Visible

Vague assurances ("we'll take your team's needs into account") are the source of distrust. Resistant stakeholders who've been burned before discount them to zero.

Replace vague commitments with commitments that have:
- A named person responsible
- A specific deliverable
- A date
- A way to verify

**Weak:** "We'll make sure your team is trained before go-live."

**Strong:** "By March 15, [name] will deliver a training schedule to your team lead. You'll have two weeks to review it before we finalize. If training isn't complete by April 30, go-live shifts."

Write these down in the meeting and send them by email the same day.

---

## Escalation Decision Framework

Escalation (taking the conflict to a higher-power stakeholder) is a tool of last resort because it damages the relationship with the resistant stakeholder and signals that your negotiation failed. Use it only when:

```
ESCALATE when ALL of the following are true:
  1. You have made at least two genuine attempts to negotiate
  2. You have surfaced their interests (not just their positions)
  3. The impasse materially threatens the project timeline or outcome
  4. The escalation target has power over BOTH parties

DO NOT escalate when:
  - You just got a "no" and haven't explored interests yet
  - You want to use it as a threat (say you will escalate only when you mean it)
  - The escalation target is on your side — that's coercion, not escalation
```

### Escalation Message Template

When escalating, frame it as seeking input, not complaining.

```
Subject: Need your guidance on [project] decision

[Escalation target],

[Stakeholder A] and I have different views on [specific issue] for [project].
We've talked twice but haven't found a resolution.

Their concern: [state it accurately and fairly]
Our position: [state it clearly]
What we need resolved: [specific decision or ruling needed]
Deadline: [when this needs to be decided to stay on track]

Would you be willing to meet with both of us for 30 minutes?
```

Do not send this message without telling the resistant stakeholder first that you're escalating and why.

---

## Worked Example: IT Director (CRM System)

From the SKILL.md example: IT Director is High Power, High Interest, Resistant (worried about integration).

**Step 1 — Diagnose resistance type**

After an initial conversation, the IT Director says: "Our current system has 47 custom integrations. No vendor has ever successfully migrated all of them."

Diagnosis: Mix of **Information Gap** (doesn't know if the new vendor can handle this) and **Loss Aversion** (46 integrations that break = their reputation on the line).

**Step 2 — Surface interests**

Ask: "If integration quality wasn't a concern, what would your ideal rollout look like?"

They say: "We'd need a parallel run, at minimum 60 days, before we cut over anything in production."

Interest identified: They need risk containment and time to verify. They're not against the project; they're against uncontrolled risk transfer.

**Step 3 — Find the legitimate core**

"You're right — 47 integrations is a real migration risk, and 60-day parallel runs are standard practice for this. Our current plan doesn't include that, which is a gap."

**Step 4 — Expand option space**

Together, generate:
1. Full 60-day parallel run (their ask)
2. 30-day parallel run on critical integrations only, documented list
3. Phased rollout: migrate 5 non-critical integrations first, verify, then proceed
4. IT Director co-owns the integration test plan (gives them control)
5. Hard stop in project charter: if >5 integrations fail during parallel, project pauses

Agree on options 3 + 4 + 5. They now have control over the riskiest part. Resistance becomes engagement.

**Step 5 — Specific visible commitment**

In writing, same day:
> "IT Director will own and sign off the integration test plan by [date]. No production cutover happens without their written approval. If integration failures exceed 5 during parallel run, project leadership meets within 48 hours to decide on scope."

IT Director goes from resistant to co-owner. They now have a stake in success.

---

## When Negotiation Genuinely Fails

Sometimes resistance persists after legitimate good-faith effort. Recognize these terminal signals:

- The stakeholder's interest is in the project *not* succeeding (political, competitive, or personal reasons)
- The conflict is a value conflict with no common ground (e.g., they believe the project is ethically wrong)
- They are acting under external instructions you cannot change (legal, regulatory, orders from above)

In these cases:
1. Document your attempts clearly
2. Escalate with full transparency (show your work)
3. Accept that you may need to redesign the project to reduce this stakeholder's veto power — or accept the constraint they represent

Do not invest additional negotiation cycles in a terminal impasse. Recognize it early and route around it.

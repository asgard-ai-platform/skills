# System Archetypes

System archetypes are recurring causal loop structures that explain why similar problems appear across wildly different domains — organizational growth, ecological collapse, arms races, addiction. Each archetype is a named loop pattern with a predictable failure mode and a known leverage point.

---

## How to Use This Reference

1. Recognize the symptom pattern in the user's problem.
2. Match it to the archetype below.
3. Apply the named leverage point — not the symptomatic fix.

The IRON LAW applies: the behavior emerges from the loop structure, not from any individual actor. Blaming people when an archetype is driving the outcome is both analytically wrong and politically counterproductive.

---

## Archetype 1: Limits to Growth

### Structure

```
Reinforcing loop (growth engine):
  Action → Results → more Action

Balancing loop (hidden constraint):
  Results → Slowing Condition → limits Action
```

### Causal Diagram (text notation)

```
[Effort] ──(+)──▶ [Performance] ──(+)──▶ [More Effort]
                        │
                        │(+)
                        ▼
               [Slowing Condition] ──(-)──▶ [Performance]
```

`(+)` = same direction; `(-)` = opposite direction.

### Symptom Pattern

Growth starts strong, then mysteriously stalls or reverses. Teams push harder; results don't improve. The standard response — "we just need to try harder" — makes things worse by stressing the system without addressing the constraint.

### Classic Examples

| Domain | Growth Engine | Hidden Constraint |
|--------|--------------|-------------------|
| Startup | Sales effort → revenue → hire more salespeople | Delivery capacity: more customers → longer queues → churn |
| Training program | Training hours → skill → confidence to train more | Trainer bandwidth: more trainees → less individual attention → skill plateau |
| Ecosystem | Prey population → predator population → prey | Prey cannot regenerate faster than they're consumed |

### Leverage Point

**Strengthen or remove the constraint** — not the growth engine.

Pushing harder on the growth engine (more effort, more marketing, more headcount) while the constraint is untouched produces short-term bounce followed by deeper stall. The leverage is identifying and relieving the limiting factor before it bites.

### Decision Rule

Ask: "What would have to be true for growth to continue indefinitely?" Whatever the answer is — that's the constraint to examine.

---

## Archetype 2: Shifting the Burden

### Structure

```
Symptomatic fix:
  Problem ──▶ Quick Fix ──(-)──▶ Problem  (balancing — reduces symptom)

Fundamental fix:
  Problem ──▶ Real Solution ──(-)──▶ Problem  (balancing — addresses root)

Side effect loop:
  Quick Fix ──(+)──▶ Side Effect ──(-)──▶ Fundamental Fix
  (addiction loop — symptomatic fix undermines capacity for real solution)
```

### Symptom Pattern

A problem is addressed with a quick fix. The problem improves temporarily. The fundamental fix is deprioritized ("we'll get to it later"). The quick fix produces a side effect that makes the fundamental fix harder or less necessary-seeming. Over time, the organization becomes dependent on the quick fix.

### Classic Examples

**Organizational firefighting:**
- Problem: system reliability incidents
- Symptomatic fix: add on-call rotations, manual interventions
- Fundamental fix: invest in reliability engineering, automated recovery
- Side effect: on-call team becomes expert at manual recovery → fewer incidents escalate to management → reliability engineering loses priority → more incidents → more on-call load → burnout

**Opioid dependency (clinical archetype):**
- Problem: chronic pain
- Symptomatic fix: opioid prescription
- Fundamental fix: physical therapy, surgery, behavioral therapy
- Side effect: drug dependency → withdrawal makes pain worse → less capacity to pursue fundamental fix → more opioids

**Technical debt:**
- Problem: slow development velocity
- Symptomatic fix: skip code review, skip tests, ship fast
- Fundamental fix: refactor, improve architecture, invest in tooling
- Side effect: accumulated debt → code becomes harder to change → fundamental fix requires months of work no one has time for → more shortcuts

### Leverage Point

**Reduce reliance on the symptomatic fix; invest in the fundamental fix while side effects are still manageable.**

The diagnostic question: "Does our quick fix make the real solution less likely to happen?" If yes, you're in this archetype.

### Warning Sign

When an organization cannot stop using the quick fix even when everyone agrees it's harmful — that's the addiction loop active. At that stage, the structural dependency must be broken explicitly (roadmap carve-out, resource allocation protected from incident pressure, etc.).

---

## Archetype 3: Tragedy of the Commons

### Structure

```
For each individual actor i:
  [Actor i's Gain] ──(+)──▶ [Total Activity on Shared Resource]
  [Total Activity] ──(-)──▶ [Resource Health]
  [Resource Health] ──(-)──▶ [Each Actor's Gain per Unit Activity]

Net result: rational individual action → collective degradation
```

### Symptom Pattern

A shared resource is being overused. Each individual actor behaves rationally given their own incentives. No single actor causes the problem. The resource degrades for everyone.

### Classic Examples

| Shared Resource | Individual Action | Collective Outcome |
|-----------------|------------------|--------------------|
| Open-source library | Skip contributing fixes, just consume | Library maintenance collapses |
| Shared infrastructure team | File urgent tickets freely | Team overwhelmed, quality degrades |
| Fishery | Each boat maximizes catch | Stock collapse |
| Attention (internal comms) | Each team sends "important" Slack messages | Signal-to-noise collapse, everyone ignores everything |

### Leverage Points (in order of strength)

1. **Mutual regulation with accountability**: actors collectively agree to limits and enforce them (Elinor Ostrom's solution — works when actors are a coherent community with long-term shared interest).
2. **Privatization of the commons**: assign ownership so the owner internalizes the cost of degradation.
3. **Taxation/cost internalization**: make each unit of use cost something proportional to its burden on the resource.
4. **Education + norm change**: weakest — works only when overuse is not individually profitable.

### Ostrom's Conditions for Self-Governance

Elinor Ostrom (Nobel 2009) found that commons can be managed without privatization or central control when:
- Boundaries of the resource and user group are clearly defined
- Rules match local conditions
- Users can participate in modifying rules
- Monitoring exists and is done by the users themselves
- Graduated sanctions for rule violators
- Conflict-resolution mechanisms are accessible
- External authorities don't undermine self-governance

---

## Archetype 4: Escalation

### Structure

```
[Actor A's Level] ──(+)──▶ [Threat to B] ──(+)──▶ [Actor B's Level]
[Actor B's Level] ──(+)──▶ [Threat to A] ──(+)──▶ [Actor A's Level]
```

Two reinforcing loops, coupled. Each actor's increase triggers the other's increase, which triggers the first actor's further increase.

### Symptom Pattern

Two parties are competing. Each justifies its escalation as defensive response to the other. Both end up spending more while neither gains relative advantage. Both are worse off in absolute terms.

### Classic Examples

- Arms race (canonical)
- Price war: Company A cuts prices → Company B cuts prices → Company A cuts further → margins collapse for both
- Interteam blame cycles: Team A misses SLA → Team B escalates loudly → Team A retaliates by deprioritizing Team B tickets → Team B escalates louder
- Performance review inflation: Manager A gives all 5s to protect team → Manager B gives all 5s → differentiation collapses, reviews meaningless

### Leverage Points

1. **Unilateral de-escalation** with explicit signaling ("we're cutting our response time; we're not cutting quality — we hope this breaks the cycle"). Works only if the other party can observe and respond.
2. **Neutral third party** sets ceiling (regulator, mediator, executive sponsor).
3. **Change the metric** that drives escalation (replace "number of escalations filed" with a collaborative SLA metric).

### Diagnostic Question

"If Actor B stopped escalating tomorrow, would we stop?" If no — you may have an internal incentive that makes escalation individually rewarding regardless of the other party. That's a different problem.

---

## Archetype 5: Success to the Successful

### Structure

```
[Resource allocation to A] ──(+)──▶ [A's success]
[A's success] ──(+)──▶ [Resource allocation to A]  (reinforcing)

[Resource allocation to A] ──(-)──▶ [Resource allocation to B]
[B's disadvantage] ──(-)──▶ [B's success]  (balancing, downward)
```

### Symptom Pattern

Two activities or groups compete for shared resources. Early performance differences, regardless of underlying merit, create allocation differences that amplify into large advantage gaps. The winner keeps winning; the loser keeps losing. Late-stage performance gap looks like competence differences but is largely structural.

### Classic Examples

- Internal product portfolio: two products compete for engineering bandwidth. Product A gets slightly more engineers → ships slightly faster → gets more user traction → leadership allocates more engineers → gap widens regardless of market potential
- Team visibility: well-connected team gets high-visibility projects → builds relationships → gets next high-visibility projects; isolated team gets maintenance work → stays invisible
- Matthew effect in science: cited papers get cited more; unknown papers remain obscure

### Leverage Points

1. **Diversify the resource allocation criterion** — add future potential, strategic fit, or risk-adjusted expected value rather than allocating purely on past performance.
2. **Separate competitions** — don't let early-stage products compete for resources against mature products on the same metric.
3. **Ring-fence minimum viable investment** for disadvantaged actors to prevent death spiral before a fair evaluation is possible.

---

## Archetype 6: Fixes That Fail

### Structure

```
[Problem] ──▶ [Fix] ──(-)──▶ [Problem]  (balancing: short-term improvement)
[Fix] ──(+)──▶ [Unintended Consequence] ──(+, delayed)──▶ [Problem]
```

### Symptom Pattern

A fix relieves the problem. Later — often weeks or months — the problem returns, sometimes worse. The fix is applied again. The cycle repeats. Each cycle may require a stronger fix.

The key feature: there is a **delay** between the fix and the unintended consequence. This makes the feedback invisible; the fix and the consequence appear unrelated.

### Classic Examples

| Fix | Short-term effect | Delayed consequence |
|-----|------------------|---------------------|
| Add headcount to a late project | More hands → progress feeling | New engineers need ramp time; communication overhead grows (Brooks' Law archetype) |
| Antibiotic overuse | Infection resolves | Resistant strain develops; next infection harder to treat |
| Increase targets to motivate team | Short-term performance spike | Burnout in 3-6 months; attrition; performance crashes |
| Add exception process to rigid rule | Immediate flexibility | Exception becomes norm; rule becomes meaningless; chaos ensues |

### Leverage Point

**Find the delayed feedback loop** before applying the fix. Ask: "What does this intervention produce six months from now, not six days from now?"

If you can't identify the side effect, the fix is not ready to deploy.

---

## Archetype 7: Growth and Underinvestment

### Structure

This is Limits to Growth + Shifting the Burden combined:

```
Demand grows (reinforcing)
  → Performance gap opens
  → Short-term fix (lower standards, add capacity patches)
  → Reduces pressure for fundamental capacity investment
  → Capacity constraint remains or worsens
  → More demand hits constrained capacity
  → Performance gap widens further
```

### Symptom Pattern

Demand grows. The organization expands. But fundamental infrastructure (reliability, documentation, developer tooling, onboarding, data pipelines) doesn't scale with demand because it's not urgent. Eventually the infrastructure debt makes each marginal unit of growth more expensive. The organization slows down precisely when it should be accelerating.

### Leverage Point

**Treat infrastructure investment as a prerequisite to growth, not a reward for it.** Concrete heuristic: for every N units of growth capacity added, allocate a fixed fraction to foundational infrastructure — non-negotiably, before growth targets are counted as achieved.

---

## Quick Identification Guide

| Symptom | Most Likely Archetype |
|---------|----------------------|
| Growth stalls despite more effort | Limits to Growth |
| Quick fix becomes permanent; real fix never happens | Shifting the Burden |
| Everyone acts rationally; shared resource degrades | Tragedy of the Commons |
| Both parties escalate; both end up worse | Escalation |
| Early winners keep winning regardless of merit | Success to the Successful |
| Problem solved, returns worse later | Fixes That Fail |
| Organization slows down as it scales | Growth and Underinvestment |

---

## Notation Conventions (used throughout this document)

| Symbol | Meaning |
|--------|---------|
| `──(+)──▶` | Positive polarity: A increases → B increases (or A decreases → B decreases) |
| `──(-)──▶` | Negative polarity: A increases → B decreases (or A decreases → B increases) |
| `[Variable]` | Stock or key variable |
| `R` label on a loop | Reinforcing (amplifying) |
| `B` label on a loop | Balancing (stabilizing) |
| `~delay~` | Significant time delay in the link |

---

## Worked Diagnosis: Multi-Archetype Situations

Real systems usually contain multiple active archetypes simultaneously. Diagnosis is not "which archetype is it" but "which archetypes are active and which is dominant."

**Example: A SaaS company's engineering team is overloaded.**

Step 1 — List the loops:

- Sales growth (R): more customers → more revenue → more hiring → capacity grows
- Overload (B partially failing): more customers → more support tickets → engineering pulled into support → less capacity for product → slower feature velocity → churn
- Technical debt (Fixes That Fail): engineering skips tests to ship fast → debt accumulates → slower velocity next quarter
- Infra underinvestment (Growth and Underinvestment): each sprint, infra work gets deprioritized for feature work → reliability degrades → more incidents → more engineering time in incidents

Step 2 — Identify dominant archetype:

The company is in **Growth and Underinvestment** driving **Fixes That Fail** at the code level. The symptomatic fix (hire more engineers, work weekends) will not address the structural cause.

Step 3 — Leverage point:

Mandatory infrastructure sprint ratio (e.g., 20% of engineering capacity reserved for reliability and debt reduction, unconditional). This directly addresses the loop where growth pressure crowds out infrastructure investment.

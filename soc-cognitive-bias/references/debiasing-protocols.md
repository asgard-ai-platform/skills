# Debiasing Protocols

Structured procedures that reduce specific cognitive biases through process design, not self-awareness. Organized by the bias each protocol primarily targets, with step-by-step procedures and worked examples.

---

## Selecting the Right Protocol

| Primary Bias | First-Line Protocol | When to escalate |
|---|---|---|
| Confirmation bias | Red Team / Devil's Advocate | Add Structured Analytic Techniques if stakes are high |
| Anchoring | Independent Parallel Estimates | Add Reference Class Forecasting if numeric forecasts involved |
| Overconfidence | Pre-Mortem | Add Calibration Tracking for repeated decisions |
| Groupthink | Nominal Group Technique | Add Delphi if group can't meet synchronously |
| Sunk cost | Zero-Base Challenge | Usually sufficient alone |
| Availability heuristic | Reference Class Forecasting | Add base rate lookup if statistics are available |

**Do not stack all protocols on every decision.** Over-process is its own failure mode. Match protocol intensity to decision stakes and reversibility.

---

## Protocol 1: Red Team / Devil's Advocate

**Targets:** Confirmation bias, groupthink, authority bias

**When to use:** Team has a strong preferred conclusion; high-stakes recommendation; any situation where everyone agrees too quickly.

### Procedure

1. **Appoint the role explicitly.** Designate one person (or a small sub-group) as the Red Team. This must be a formal role, not "who wants to argue the other side?" Voluntary advocates are too soft.
2. **Give the Red Team the strongest version of the opposition case.** Brief them on all arguments for the current recommendation, then ask: "Build the most compelling argument AGAINST this decision. Assume the current recommendation fails — why?"
3. **Red Team presents first.** Before the main team presents their recommendation, Red Team argues the opposing case for a fixed time (10–20 min depending on decision complexity).
4. **Main team responds.** Not to "win" but to identify which Red Team objections they cannot rebut.
5. **Unrefuted objections become decision conditions.** Any Red Team argument the main team can't rebut gets added to the decision log as a named risk or condition.

### Rules that prevent the protocol from degrading

- Red Team is not playing devil's advocate for fun — they should be genuinely trying to find fatal flaws.
- The Red Team lead should not be the most junior person in the room (authority bias will prevent real challenge).
- After the session, the Red Team role ends. Don't let it create permanent "designated skeptic" dynamics.

### Worked Example

**Decision:** Launch a premium pricing tier at 2x current price.

Red Team brief: "Argue that this pricing move will destroy net revenue within 18 months."

Red Team arguments (presented first):
- Price-sensitive cohort (identified as ~38% of users in past churn analysis) will cancel at 2x, not upgrade
- Competitor X has been testing similar pricing and rolled it back after 90 days
- Net Revenue Retention calculation assumes 70% upgrade rate — no evidence base given for this number

Main team cannot rebut: The 38% price-sensitive cohort estimate. They had assumed 15%.

**Outcome:** Decision conditions added — cap downside exposure by launching in one region first; conduct price-sensitivity survey before full rollout.

---

## Protocol 2: Independent Parallel Estimates

**Targets:** Anchoring, groupthink, authority bias

**When to use:** Any meeting where a number will be discussed — budget, timeline, market size, probability of success. Run this *before* the meeting, not during.

### Procedure

1. **Frame the estimation question precisely.** Write down the exact question with units and time horizon. "What is the probability this product reaches $1M ARR within 12 months of launch?" is better than "Will this succeed?"
2. **Collect estimates independently, in writing.** Each participant submits their estimate (and optionally their top 2 reasoning factors) before seeing any other estimates. Use anonymous forms if authority bias is likely.
3. **Reveal all estimates simultaneously.** Not sequentially — sequential revelation anchors later responders to earlier numbers.
4. **Identify the spread, not just the average.** Wide spread = hidden disagreement that needs surfacing. Narrow spread = possible groupthink (especially if one authority submitted first).
5. **Discuss the outliers first.** Ask the highest and lowest estimators to explain their reasoning. This surfaces hidden information and resets the group's frame.
6. **Re-estimate (optional).** If discussion reveals new information, a second round of independent estimates is legitimate. Don't average the rounds mechanically.

### Common failure mode

Running "independent" estimates in the meeting itself while the CEO's number is written on the whiteboard. That number will anchor everyone. Estimates must be collected before any numbers are visible in the room.

### Worked Example

Pre-meeting form sent to 5 decision-makers:

> "Independent of anything discussed in previous meetings: What percentage of beta users do you estimate will convert to paid within 30 days of receiving their upgrade prompt?"

Responses (collected blind):

| Participant | Estimate |
|---|---|
| A | 12% |
| B | 35% |
| C | 28% |
| D | 30% |
| E | 14% |

Spread: 12%–35%. Not groupthink. Outliers are A (12%) and B (35%).

Discussion reveals: A has been monitoring support tickets and sees significant confusion with the upgrade flow. B extrapolated from a single cohort that had an unusually high engagement week.

Revised consensus after discussion: 18–22%, with a blocker: fix the upgrade UX before launch.

Without the protocol, the meeting would have opened with the CEO's gut figure of "around 30%" and anchored everyone there.

---

## Protocol 3: Pre-Mortem

**Targets:** Overconfidence, planning fallacy

**Developed by:** Gary Klein (1989). Validated in research by Deborah Mitchell et al.

**When to use:** Before committing to a plan — project launch, investment, strategic pivot. Run once the plan is finalized but before execution begins.

### Why it works

Prospective hindsight — imagining that an event has already happened — increases the ability to identify reasons for future outcomes by approximately 30% (Mitchell et al., 1989). The pre-mortem exploits this by forcing the imagination of failure before it occurs.

### Procedure

1. **State the premise explicitly to the group:** "It is now 12 months from today. The project has failed — completely, not just underperformed. We are in a post-mortem meeting. What happened?"
2. **Individual silent writing (5–10 min).** Each participant writes down every reason they can think of for the failure. No discussion yet. This prevents early speakers from anchoring the frame.
3. **Round-robin sharing.** Each person shares one reason in rotation. Continue until all reasons are exhausted. Facilitator captures on a shared board.
4. **Cluster and rank.** Group similar reasons. Vote on which failure modes are (a) most likely and (b) most severe.
5. **Modify the plan.** For each high-ranked failure mode, ask: "What change to the current plan would reduce this risk?" Update the plan or add explicit monitoring tripwires.

### Prompt variants by bias type

| Variant | Prompt |
|---|---|
| Standard pre-mortem | "It's failed. What happened?" |
| Overconfidence variant | "Our forecast was off by 50%. Why?" |
| Speed variant (15-min version) | Each person writes exactly 3 failure reasons; share in one round |
| Pre-parade (success variant, use sparingly) | "It succeeded beyond expectations. What did we do right that we might under-invest in?" |

### Worked Example

**Plan:** Expand to Japanese market in Q3. Team confidence: "very high."

Pre-mortem session produces 23 failure reasons. Top 5 after clustering and voting:

| Failure Mode | Likelihood (team vote) | Severity (team vote) |
|---|---|---|
| Localization quality insufficient — product feels foreign | High | High |
| No local BD relationship — can't get past procurement | High | High |
| Pricing not adjusted for Japanese market expectations | Medium | High |
| Support SLA cannot be met across time zone gap | Medium | Medium |
| Regulatory requirement missed (specific to financial sector) | Low | Critical |

Plan modifications added:
- Hire Tokyo-based BD contractor before launch (not after)
- Commission localization quality review from native speakers
- Legal review of financial data handling requirements added to pre-launch checklist

**Note:** The regulatory item had Low likelihood but Critical severity — it would have been missed in a standard risk review because no one was thinking about it.

---

## Protocol 4: Nominal Group Technique (NGT)

**Targets:** Groupthink, authority bias, bandwagon effect

**When to use:** Group decisions where rank differences or dominant personalities are likely to suppress minority views. Standard brainstorming meetings are the primary failure case.

### Procedure

1. **Silent idea generation (5–10 min).** All participants write their ideas or votes individually without discussion. No verbal communication.
2. **Round-robin recording.** Each participant shares one idea per round in order. The facilitator records every idea without evaluation or comment. No discussion, no "yes but," no "we tried that." Continue until all ideas are exhausted.
3. **Clarification only.** Once all ideas are recorded, participants may ask clarification questions — only to understand, not to challenge or advocate.
4. **Individual silent ranking.** Each participant privately ranks the top 5 items (or votes using dot voting). Rankings are written, not spoken.
5. **Aggregate and display results.** Tally rankings publicly. The group sees the aggregate — not who voted for what.
6. **Discussion, then final vote.** Only now does the group discuss, focused on items with surprising rankings. Final vote if needed.

### Why this outperforms standard brainstorming

Standard brainstorming produces **production blocking** (only one person speaks at a time), **evaluation apprehension** (fear of criticism suppresses ideas), and **social loafing** (people defer to whoever speaks first). NGT eliminates all three by separating generation from evaluation.

### Worked Example

**Decision:** Which of four product roadmap priorities should get Q3 resources?

Standard meeting outcome: VP of Engineering proposes Option A enthusiastically first. Four others agree quickly. One person mentions Option C but doesn't push it.

NGT outcome:

Individual silent rankings (5 participants, rank 1=highest):

| Option | P1 | P2 | P3 | P4 | P5 | Total (lower=higher priority) |
|---|---|---|---|---|---|---|
| A | 2 | 1 | 3 | 1 | 2 | 9 |
| B | 3 | 4 | 2 | 3 | 3 | 15 |
| C | 1 | 2 | 1 | 2 | 1 | 7 |
| D | 4 | 3 | 4 | 4 | 4 | 19 |

Option C wins. It was the item "mentioned but not pushed" in the standard meeting. Under NGT, three participants had it ranked #1.

Discussion reveals: C solves a key customer pain point that engineering staff knew about but felt junior to raise against the VP's preferred option.

---

## Protocol 5: Zero-Base Challenge

**Targets:** Sunk cost fallacy, status quo bias, escalation of commitment

**When to use:** Any decision where past investment (money, time, effort, reputation) is being cited as a reason to continue. Particularly effective for ongoing projects that are underperforming.

### The core reframe

The sunk cost fallacy persists because the mind frames the decision as:

> "We've spent X. Should we continue?"

The Zero-Base Challenge reframes it as:

> "Ignoring everything spent so far: if we were offered this opportunity today for the first time, with current knowledge, would we invest?"

These are the same decision economically. They produce different answers psychologically because the reframe removes the sunk investment from the frame entirely.

### Procedure

1. **Document the forward economics only.** Strip out all past costs. Calculate only: (a) remaining investment required, (b) expected forward returns, (c) probability-weighted expected value.
2. **State the zero-base question.** "If a competitor offered us this asset/project/position today — for free — would we take it on?" If free isn't enough to take it, the project should be discontinued.
3. **Identify the real objection.** If the answer is "yes we'd take it for free, but we need to continue investing," verify this is driven by forward economics, not sunk cost reasoning.
4. **Separate stranded costs from reversibility.** Some continuation costs are legitimate — not because of sunk costs, but because stopping now would create new costs (contract penalties, team disruption, customer commitments). Name these explicitly and include them in the forward calculation.

### Worked Example

**Situation:** SaaS company 14 months into a data pipeline rebuild. NT$8M spent. Timeline overrun by 6 months. Current estimate: NT$4M more to complete. Original business case: NT$2M annual savings.

Standard framing: "We've spent NT$8M. We can't stop now."

Zero-base calculation:

| Item | Value |
|---|---|
| Remaining cost to complete | NT$4M |
| Expected annual savings (if completed) | NT$2M |
| Probability of completion on this estimate (given 3 prior overruns) | 50% |
| Expected forward value | NT$2M × 50% = NT$1M/year, or ~NT$3M NPV over 5 years |
| Forward ROI | NT$3M return on NT$4M investment = negative |

Zero-base question: "If a vendor offered to build this for NT$4M, would we commission it?" 

Answer: No — the business case at current costs doesn't justify it.

Decision: Evaluate if a commercial off-the-shelf solution exists at lower cost. If not, negotiate a reduced scope rebuild.

### Stranded cost check

Before stopping: NT$1.2M in vendor contracts have cancellation penalties of NT$300K if terminated before month 18. This is a legitimate forward cost of stopping — include it. It doesn't change the direction of the decision in this case.

---

## Protocol 6: Reference Class Forecasting

**Targets:** Availability heuristic, planning fallacy, overconfidence in unique-case reasoning

**Developed by:** Daniel Kahneman and Amos Tversky; operationalized by Bent Flyvbjerg for infrastructure planning.

**When to use:** Whenever a forecast is being built primarily from the "inside view" (project-specific features, team's own models). Add the outside view via reference class.

### Inside view vs. outside view

| | Inside View | Outside View |
|---|---|---|
| Starting point | This project's specific features | Base rate across similar past projects |
| Common failure mode | Planning fallacy — ignores historical overruns | May not find a valid reference class |
| Default human tendency | Strongly preferred | Systematically neglected |

Both views are legitimate. The bias is that inside-view estimates dominate, and reference class forecasting corrects this.

### Procedure

1. **Select the reference class.** Find a database of projects/decisions sufficiently similar to your case. The class should be (a) similar in type, (b) large enough to be statistically meaningful (n ≥ 20 is a rough minimum), and (c) historical, not projected.
2. **Establish the base rate.** From the reference class, compute the distribution of outcomes. For schedule: what % of similar projects came in on time, over by 10%, over by 50%? For revenue: what's the P50, P80 outcome?
3. **Adjust for specific features.** Apply a limited set of adjustments for features that genuinely differentiate your case from the reference class. Document each adjustment and its direction/magnitude.
4. **Produce a calibrated forecast.** The reference class sets the prior. Specific adjustments shift it. Do not let inside-view optimism override the prior without explicit justification.

### Example Reference Classes

| Decision Type | Reference Class Source |
|---|---|
| IT project delivery | Standish CHAOS Report (overrun rates by size/type) |
| New product revenue | Nielsen historical new product success rates |
| M&A synergy realization | McKinsey/Bain M&A studies |
| Startup survival | CB Insights, Crunchbase cohort data |
| Marketing campaign uplift | Benchmarks from Google/Meta/industry associations |

### Worked Example

**Inside view forecast:** New B2B SaaS product will reach NT$10M ARR in Year 1. Team reasoning: strong product-market fit signals, 3 LOIs from enterprise prospects, experienced sales team.

Reference class: B2B SaaS products launched by Series A companies with similar ACV (NT$500K–2M), past 5 years.

Reference class data (n=47 products):

| Outcome | % of cases |
|---|---|
| Reached 50%+ of Year 1 target | 22% |
| Reached 25–50% of Year 1 target | 31% |
| Reached <25% of Year 1 target | 47% |

Base rate P50 outcome: approximately 25% of target = NT$2.5M ARR.

Adjustments applied:
- +15%: Existing enterprise relationships (2 of 3 LOI companies are existing customers of related product)
- -10%: No dedicated enterprise sales hire yet (historical data shows companies without dedicated AE miss by more)

Adjusted forecast: P50 = NT$2.8M ARR. P80 = NT$5M ARR.

**Decision implication:** Build the Year 1 operating plan on NT$3M ARR, not NT$10M. Hire the enterprise AE in month 1, not month 6.

---

## Calibration Tracking (Supporting Tool)

**Targets:** Overconfidence — specifically, persistent overconfidence that repeats across decisions

Reference class forecasting and pre-mortems address overconfidence in individual decisions. Calibration tracking addresses systematic overconfidence in a person or team over time.

### What to track

For every probabilistic prediction made with a stated confidence level, record:
- Date
- Decision / question
- Stated probability (e.g., "80% confident this will succeed")
- Actual outcome (recorded when known)

### Calibration score

A well-calibrated forecaster is right approximately X% of the time on predictions stated with X% confidence.

Simple check: Of all predictions stated with "70–80% confidence" over the past year, what % actually came true?

| Stated confidence | Expected hit rate | Actual hit rate | Interpretation |
|---|---|---|---|
| 70–80% | ~75% | >85% | Under-confident — too cautious |
| 70–80% | ~75% | 75% | Well calibrated |
| 70–80% | ~75% | <60% | Over-confident — stated confidence is inflated |

### Minimum viable implementation

A spreadsheet with four columns: Date, Prediction, Confidence (%), Outcome. Review quarterly. Show team members their own calibration scores — not to shame, but to give feedback the brain cannot generate on its own.

Teams that track calibration consistently improve over 6–12 months. Teams that only attend "debiasing workshops" without tracking show little lasting improvement.

---

## Protocol Selection by Decision Type

| Decision Type | Recommended Protocols | Skip |
|---|---|---|
| One-time, high-stakes, irreversible | Pre-Mortem + Red Team | Calibration tracking (too slow) |
| Repeated forecast (quarterly planning) | Independent Parallel Estimates + Calibration Tracking | Pre-mortem (overkill per cycle) |
| Group prioritization with authority present | NGT | Devil's advocate (won't fix the authority dynamic) |
| Project continuation / kill decision | Zero-Base Challenge | Red Team (confirmation bias isn't the primary issue) |
| Novel market entry | Reference Class Forecasting + Pre-Mortem | Zero-Base (sunk cost not yet in play) |
| Budget / timeline estimate | Independent Parallel Estimates + Reference Class | NGT (not a group prioritization problem) |

---

## What Protocols Cannot Fix

- **Motivated reasoning with deliberate concealment.** If a decision-maker knows the truth and is hiding it, debiasing won't help. This is a governance/incentive problem.
- **Biases reinforced by incentive structures.** A sales team on commission will be overconfident in revenue forecasts regardless of what protocol you use. Fix the incentive, or accept the bias and apply a reference class correction.
- **Single-person decisions under time pressure.** Most protocols require ≥ 2 people and preparation time. For urgent solo decisions, the best available tool is a written checklist: "What would I advise a friend in this situation?" (removes self-serving bias) and "What's the base rate?" (removes availability bias).

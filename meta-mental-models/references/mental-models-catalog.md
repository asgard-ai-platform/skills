# Mental Models Catalog (50+ Models)

Companion to `meta-mental-models/SKILL.md`. Use this file when selecting models to apply; the parent skill explains *how* to apply them.

Models are organized by source discipline. Each entry includes: **principle** (one sentence), **trigger** (when to reach for it), and **pitfall** (the most common misuse).

---

## Physics / Engineering

### Inversion
**Principle:** Instead of asking "how do I achieve X?", ask "what would guarantee failure at X?" Eliminate failure paths first.
**Trigger:** Goal-setting, strategy, risk management, pre-mortem exercises.
**Pitfall:** Stopping at inversion. Use it to generate the failure list, then solve for it — don't just invert and walk away.

### Second-Order Effects
**Principle:** Every action has consequences (1st order), and those consequences have consequences (2nd order). Most people stop at 1st.
**Trigger:** Policy design, pricing changes, org restructuring, any decision with ripple effects.
**Pitfall:** Infinite regress. Go to 2nd order; 3rd+ is usually noise unless the domain has known feedback loops.

### Entropy
**Principle:** Closed systems tend toward disorder. Maintenance and energy input are required to preserve order.
**Trigger:** Team health, codebases, relationships, product quality over time.
**Pitfall:** Treating entropy as inevitable justification for neglect. It's a prompt to schedule maintenance, not an excuse.

### Critical Mass / Phase Transition
**Principle:** Small additions near a threshold produce disproportionately large effects. Below threshold: nothing. Above: cascade.
**Trigger:** Network effects, viral growth, tipping points, nuclear metaphors applied to markets.
**Pitfall:** Assuming you know where the threshold is. Usually you discover it in hindsight.

### Feedback Loops (Positive/Negative)
**Principle:** Positive feedback amplifies signal; negative feedback dampens it toward equilibrium.
**Trigger:** Growth models, product addiction loops, pricing spirals, thermostat-like controls.
**Pitfall:** Confusing "positive" with "good." Positive feedback can amplify bad outcomes just as readily.

### Bottleneck / Theory of Constraints
**Principle:** The throughput of any system is limited by its weakest link. Improving a non-bottleneck does not improve the system.
**Trigger:** Operations, software performance, hiring pipelines, any workflow.
**Pitfall:** Identifying the wrong bottleneck because the real one is invisible (e.g., managerial approval, not engineering capacity).

### Leverage
**Principle:** A small input at the right point produces a large output. Force × distance = torque.
**Trigger:** Finding high-ROI interventions, prioritization, influence without authority.
**Pitfall:** Leverage amplifies both gains *and* losses. Identifying the fulcrum incorrectly is dangerous.

### Redundancy
**Principle:** Build backup systems so that single-point failures don't cascade.
**Trigger:** Critical infrastructure, launch plans, key-person dependencies, data backups.
**Pitfall:** Over-redundancy adds cost and complexity. Apply to genuinely catastrophic failure modes, not everything.

### Margin of Safety
**Principle:** Build in buffer beyond the calculated minimum. Bridges are engineered for 4× the expected load.
**Trigger:** Financial planning, scheduling, structural design, any estimate with uncertainty.
**Pitfall:** Margin of safety doesn't eliminate risk — it buffers known unknowns. Unknown unknowns still break things.

---

## Biology / Evolution

### Natural Selection / Fitness Landscape
**Principle:** What survives is what's adapted to the *current* environment, not what's objectively best.
**Trigger:** Market competition, product-market fit, org survival, technology adoption.
**Pitfall:** The environment changes. Yesterday's fit organism is today's Kodak.

### Red Queen Effect
**Principle:** In competitive environments, you must keep improving just to maintain relative position.
**Trigger:** Competitive strategy, skill development, arms races in any industry.
**Pitfall:** Running faster when you should change direction. The Red Queen runs harder; sometimes you need a new track.

### Niche Specialization vs. Generalism
**Principle:** Specialists dominate stable, predictable niches. Generalists survive volatile, shifting environments.
**Trigger:** Career strategy, product positioning, market entry, hiring.
**Pitfall:** Assuming niches are stable. Specializing in a niche that's about to disappear is lethal.

### Homeostasis
**Principle:** Living systems maintain internal stability by actively counteracting deviation.
**Trigger:** Organizational culture, pricing in equilibrium markets, personal habits.
**Pitfall:** Homeostatic systems resist change even when change is needed. Disruption requires overcoming homeostatic forces.

### Parasitism / Symbiosis
**Principle:** Relationships range from mutually beneficial (symbiosis) to one-sided extraction (parasitism).
**Trigger:** Partnership evaluation, vendor relationships, platform-developer dynamics.
**Pitfall:** Parasitic dynamics are often disguised as symbiosis early on. Look at long-run incentives, not initial terms.

### Punctuated Equilibrium
**Principle:** Systems are stable for long periods, then change rapidly in short bursts, then stabilize again.
**Trigger:** Industry disruption, technology S-curves, organizational change.
**Pitfall:** Expecting smooth linear change. The equilibrium phase feels like nothing is happening — then it suddenly does.

### Mimicry
**Principle:** Organisms (and companies) copy successful signals, whether or not they have the underlying capability.
**Trigger:** Brand imitation, credential inflation, narrative adoption in pitches.
**Pitfall:** Mimicry is surface-level. Copying a competitor's pricing without copying their cost structure destroys margins.

---

## Mathematics / Statistics

### Pareto Principle (80/20)
**Principle:** ~80% of effects come from ~20% of causes. The distribution is often more extreme than 80/20 implies.
**Trigger:** Prioritization, customer segmentation, bug triage, revenue analysis.
**Pitfall:** The 20% isn't always obvious up front. You must measure first; don't assume you already know which 20%.

### Regression to the Mean
**Principle:** Extreme observations tend to be followed by less extreme ones because extremes often contain luck.
**Trigger:** Performance evaluation, medical treatment assessment, sports coaching, investment.
**Pitfall:** Attributing regression to mean to an intervention. If performance recovers after doing nothing, regression — not the action — explains it.

### Bayes' Theorem
**Principle:** P(H|E) = P(E|H) × P(H) / P(E). Update beliefs proportionally to evidence, weighted by priors.
**Trigger:** Any decision under uncertainty where new evidence arrives incrementally.
**Pitfall:** Base rate neglect. People update on P(E|H) and forget P(H) entirely. If the prior is very low, even strong evidence may not justify high posterior confidence.

```
Example:
Disease prevalence: 1 in 10,000 (prior = 0.0001)
Test accuracy: 99% (sensitivity + specificity)
Positive test → P(disease | positive) ≈ 1% (not 99%)
Because P(false positive) >> P(true positive) when base rate is tiny.
```

### Normal Distribution vs. Power Laws
**Principle:** Many human phenomena follow power laws (fat tails), not normal distributions. Using Gaussian tools on power-law data produces catastrophic underestimates of extreme events.
**Trigger:** Risk models, financial returns, content virality, wealth distribution, earthquake/war frequencies.
**Pitfall:** Treating "it's never been that extreme before" as evidence it can't be. Power-law tails are thicker than intuition suggests.

### Expected Value
**Principle:** EV = Σ (probability × outcome). Rational decisions maximize EV, not most-likely outcome.
**Trigger:** Bet sizing, go/no-go decisions, investment, product feature prioritization.
**Pitfall:** EV ignores variance. A decision with positive EV but ruinous downside may not be rational if you can't absorb the downside. Combine with Kelly Criterion or explicit risk of ruin calculation.

### Kelly Criterion
**Principle:** Optimal bet fraction = (edge / odds). Betting more than Kelly destroys expected log wealth.
**Trigger:** Position sizing, resource allocation, any repeated bet with known (or estimated) edge.
**Pitfall:** Kelly assumes you know the true probability. Overconfidence in that estimate leads to overbetting. Use half-Kelly as a practical default.

```
Formula: f* = (bp - q) / b
Where:
  b = net odds received on the bet (e.g., 2 for 2:1)
  p = probability of winning
  q = 1 - p
```

### Compounding
**Principle:** Growth compounds exponentially; small differences in rate produce enormous long-term differences.
**Trigger:** Investment, skill development, audience growth, technical debt accumulation.
**Pitfall:** Compounding works in reverse too. Small negative rates (churn, attrition, decay) compound just as ruthlessly.

### Sampling Bias / Survivorship Bias
**Principle:** Conclusions drawn only from visible, surviving observations systematically overestimate success rates.
**Trigger:** Learning from success stories, evaluating strategy effectiveness, interpreting published research.
**Pitfall:** The absence of data from failures is not evidence that failures don't exist. Ask: "what would the graveyard look like?"

---

## Psychology / Behavioral

### Incentive-Caused Bias
**Principle:** People's beliefs and actions are shaped by what they're incentivized to believe and do — even unconsciously.
**Trigger:** Compensation design, vendor advice, analyst recommendations, any situation where the advisor benefits from a particular conclusion.
**Pitfall:** Assuming good intentions eliminates the bias. Incentive-caused bias operates unconsciously; the person genuinely believes the biased conclusion.

### Circle of Competence
**Principle:** Differentiate between domains you deeply understand and domains where you merely have opinions.
**Trigger:** High-stakes decisions, delegation, knowing when to ask for help.
**Pitfall:** The edge of the circle is fuzzy. The Dunning-Kruger peak (confident incompetence) sits just outside the circle. Map it explicitly.

### Hanlon's Razor
**Principle:** Never attribute to malice what is adequately explained by ignorance or incompetence.
**Trigger:** Conflict resolution, interpreting bugs/errors, explaining organizational dysfunction.
**Pitfall:** The razor cuts one way but incompetence can be just as damaging as malice. Diagnosis of cause doesn't reduce urgency of response.

### First-Conclusion Bias (Anchoring)
**Principle:** The first number or conclusion encountered anchors subsequent estimates, even when irrelevant.
**Trigger:** Negotiations, pricing, estimates, performance reviews.
**Pitfall:** Generating your own anchor independently before seeing the other party's offer. Silence before anchoring, not after.

### Social Proof
**Principle:** People use others' behavior as evidence about the correct behavior in ambiguous situations.
**Trigger:** Product adoption, pricing signals, hiring ("where did you go to school?"), market bubbles.
**Pitfall:** Social proof creates herding. When everyone uses the same signal, the signal loses information content. Crowds are right about stable facts; they're wrong at turning points.

### Loss Aversion
**Principle:** Losses hurt ~2× as much as equivalent gains feel good (Kahneman/Tversky). People accept worse EV to avoid losses.
**Trigger:** Change management, pricing, negotiation, product feature removal.
**Pitfall:** Using loss aversion only as a persuasion technique. Also use it diagnostically: where are you avoiding a good decision because of the pain of a certain loss?

### Availability Heuristic
**Principle:** People overweight easily recalled events when estimating probability.
**Trigger:** Risk assessment after high-profile events, media-driven fear, managerial decisions post-crisis.
**Pitfall:** The solution is base rates, not intuition. Counter availability bias with explicit reference to historical frequencies before reasoning from vivid examples.

### Scope Insensitivity
**Principle:** People's willingness to pay/sacrifice does not scale proportionally with the scope of the problem.
**Trigger:** Fundraising, policy evaluation, large-scale risk communication.
**Pitfall:** Assuming emotional impact tracks magnitude. "Saving 200,000 birds" doesn't feel 2× better than "saving 100,000 birds." Aggregate numbers lose meaning; use concrete individuals or ratios.

### Fundamental Attribution Error
**Principle:** We over-attribute others' behavior to character/disposition and under-attribute it to situation/context.
**Trigger:** Performance management, conflict analysis, customer behavior analysis.
**Pitfall:** We do the reverse for ourselves (self-serving bias). Apply symmetrically: assume situation explains their behavior as readily as it explains ours.

### Sunk Cost Fallacy
**Principle:** Past costs are irrelevant to future decisions. Only future costs and benefits matter.
**Trigger:** Project cancellation decisions, relationship exit decisions, investment averaging down.
**Pitfall:** Sunk costs sometimes carry information about commitment and credibility. Distinguish between irrational sunk-cost reasoning and legitimate "staying the course" based on future EV.

### Confirmation Bias
**Principle:** People seek, interpret, and recall information that confirms existing beliefs.
**Trigger:** Research, competitive analysis, hypothesis testing, any inquiry.
**Pitfall:** The antidote is not "seek disconfirmation" — it's structuring processes that force exposure to disconfirming evidence (adversarial collaboration, red teams, pre-mortem).

### Ego Depletion / Decision Fatigue
**Principle:** Willpower and decision quality degrade after sustained cognitive effort.
**Trigger:** Meeting scheduling, high-stakes decisions, negotiation timing.
**Pitfall:** Compensating by postponing decisions rather than structuring the environment to reduce decision load.

---

## Economics / Game Theory

### Opportunity Cost
**Principle:** The cost of any choice is the value of the best alternative forgone.
**Trigger:** Resource allocation, time management, investment evaluation.
**Pitfall:** People calculate dollar costs but not opportunity costs. Always ask: "what am I *not* doing by doing this?"

### Comparative Advantage
**Principle:** Specialize in what you're *relatively* better at, even if someone else is absolutely better at everything.
**Trigger:** Division of labor, outsourcing decisions, team role design.
**Pitfall:** Comparative advantage requires trade to be captured. Without coordination, the gains disappear.

### Prisoner's Dilemma / Coordination Problems
**Principle:** Individually rational choices can produce collectively worse outcomes. Cooperation requires credible commitment.
**Trigger:** Industry standards, environmental problems, arms races, multi-party negotiations.
**Pitfall:** Assuming the game is played once. In repeated games, cooperation is often the dominant strategy (tit-for-tat). Ask: "how many times will we play this?"

### Tragedy of the Commons
**Principle:** Shared resources are over-exploited when individual benefit from extraction exceeds individual cost.
**Trigger:** Shared infrastructure, open-source projects, team bandwidth, shared budgets.
**Pitfall:** The tragedy is not inevitable. Elinor Ostrom's work shows community governance often succeeds where both markets and governments fail.

### Signaling vs. Substance
**Principle:** Costly signals can convey information precisely because they're costly to fake.
**Trigger:** Hiring (credentials), pricing (premium = quality signal), commitments, brand advertising.
**Pitfall:** Distinguishing between costly signals that convey real information (education) and arms races that destroy value without conveying anything (credential inflation).

### Moral Hazard
**Principle:** When one party is insulated from risk, they behave differently (usually more recklessly) than if they bore the full risk.
**Trigger:** Insurance design, delegation, bailout policy, management compensation.
**Pitfall:** Some moral hazard is acceptable — the goal is risk reduction, not perfect incentive alignment. Structure monitoring and co-pays, not zero insurance.

### Network Effects
**Principle:** The value of a product or network increases as more people use it (Metcalfe's Law: value ∝ n²).
**Trigger:** Platform strategy, marketplace design, technology adoption, switching costs.
**Pitfall:** Network effects don't automatically produce winner-take-all outcomes. Multi-homing, niche segmentation, and interoperability can sustain multiple platforms.

### Price Elasticity
**Principle:** Demand for price-elastic goods changes substantially with small price changes; inelastic goods do not.
**Trigger:** Pricing strategy, revenue optimization, tax policy analysis.
**Pitfall:** Elasticity varies by customer segment, substitutes, and time horizon. Point elasticity (now) ≠ arc elasticity (over time). Long-run elasticity is almost always higher than short-run.

---

## Philosophy / Logic

### Occam's Razor
**Principle:** Among competing hypotheses, prefer the one with the fewest unnecessary assumptions.
**Trigger:** Debugging, diagnosis, scientific hypothesis selection, explanation selection.
**Pitfall:** Simpler is not always correct. Occam's Razor is a tiebreaker for equal explanatory power, not a trump card.

### Falsifiability (Popper)
**Principle:** A claim is scientific (testable) only if it could in principle be proven wrong. Unfalsifiable claims are not wrong — they're unscientific.
**Trigger:** Evaluating theories, evaluating business hypotheses, distinguishing insight from rationalization.
**Pitfall:** Falsifiability is a property of the claim, not the thinker. Many people hold falsifiable beliefs but refuse to update. Pair with "what would change my mind?"

### Chesterton's Fence
**Principle:** Don't remove a fence until you understand why it was built. The reason may not be obvious.
**Trigger:** Code refactoring, policy removal, org restructuring, any change to an existing constraint.
**Pitfall:** Using Chesterton's Fence as a blanket defense of the status quo. Understand the reason; then decide whether the reason still applies.

### Map vs. Territory
**Principle:** The model (map) is not reality (territory). All models are wrong; some are useful.
**Trigger:** Any time a model or framework is applied, especially in novel situations.
**Pitfall:** Forgetting which is which. An org chart is a map. The actual power dynamics are the territory. When they diverge, the territory wins.

### Gell-Mann Amnesia
**Principle:** We recognize obvious errors in fields we know well, yet trust media/experts in fields we don't know, even from the same source.
**Trigger:** Evaluating expert claims, media consumption, cross-domain advice.
**Pitfall:** Overcorrecting into total epistemic paralysis. Use Gell-Mann as a calibration tool: apply the same skepticism across domains, not just in your own.

### Overton Window
**Principle:** The range of ideas considered acceptable in public discourse at a given time. Ideas outside the window are "unthinkable" regardless of merit.
**Trigger:** Policy proposals, product positioning, social change strategy.
**Pitfall:** Assuming the window is fixed. It shifts — sometimes rapidly. Strategy often involves moving the window before proposing the actual policy.

---

## Systems Thinking

### Stocks and Flows
**Principle:** Stocks are accumulations (inventory, cash, trust, knowledge). Flows are rates of change (sales, spend, attrition). You can only change stocks by changing flows.
**Trigger:** Business modeling, org design, any dynamic problem.
**Pitfall:** Treating a flow problem as a stock problem. "We need more engineers" (stock focus) when the actual problem is "our onboarding flow turns engineers into quitters in 6 months."

### Leverage Points (Meadows)
**Principle:** Some interventions in systems change outcomes dramatically; others barely matter. In order of increasing power: numbers → delays → feedback loops → system structure → goals → paradigms.
**Trigger:** Systems change, policy design, org transformation.
**Pitfall:** The highest-leverage interventions are hardest to change (paradigms, goals). Low-leverage interventions (numbers/parameters) are easiest but weakest.

### Unintended Consequences
**Principle:** Complex systems produce outcomes not anticipated by the intervening actor, often opposite to the intent.
**Trigger:** Policy evaluation, product feature design, incentive system design.
**Pitfall:** The three classic sources: perverse incentives, adaptation by actors to the intervention, and ignored side channels. Anticipate all three.

### Time Delays
**Principle:** Cause and effect are separated in time. Decision-makers operating on outdated feedback overshoot or undershoot.
**Trigger:** Supply chains, hiring pipelines, price controls, educational outcomes.
**Pitfall:** Increasing the speed of responses when you can't shorten the delay. Faster oscillations around the wrong setpoint make the problem worse, not better.

---

## Strategy / Organizations

### OODA Loop (Boyd)
**Principle:** Observe → Orient → Decide → Act. The faster and more accurate the loop, the greater the competitive advantage.
**Trigger:** Competitive response, crisis management, agile product development.
**Pitfall:** Speed without accuracy. A faster OODA loop that orients incorrectly produces faster wrong decisions.

### Asymmetric Information
**Principle:** When one party knows more than the other, the informed party can exploit the information asymmetry (adverse selection, principal-agent problem).
**Trigger:** Hiring, vendor selection, M&A due diligence, negotiations.
**Pitfall:** Assuming transparency solves the problem. Even disclosed asymmetric information leads to adverse selection if the other party can't verify what you share.

### Strategic Ambiguity
**Principle:** Intentionally vague commitments allow flexibility but reduce credibility as a deterrent or coordination mechanism.
**Trigger:** Alliance commitments, contract drafting, political statements.
**Pitfall:** Strategic ambiguity works until it's tested. When tested, the ambiguity resolves — one way or another — and the resolution sets the precedent.

### Theory of the Firm (Coase)
**Principle:** Firms exist to reduce transaction costs. Activities are internalized when internal coordination is cheaper than market coordination.
**Trigger:** Build-vs-buy, outsourcing, vertical integration decisions.
**Pitfall:** Transaction costs change with technology. Cloud computing and APIs dramatically lowered transaction costs in software, which is why the boundary of the firm shifted outward (more outsourcing, not less).

---

## Rapid-Selection Decision Table

When you have a situation but haven't yet chosen models, use this lookup:

| Situation Type | Start With | Add If Needed |
|---------------|-----------|---------------|
| Competitor is gaining | Red Queen + Natural Selection | Niche Specialization |
| Project is failing | Inversion + Bottleneck | Sunk Cost Fallacy |
| Team conflict | Hanlon's Razor + Incentive-Caused Bias | Fundamental Attribution Error |
| Pricing decision | Price Elasticity + Signaling | Anchoring |
| High-stakes bet | Expected Value + Kelly Criterion | Margin of Safety |
| System keeps breaking | Stocks & Flows + Entropy | Feedback Loops |
| Evaluating an expert claim | Bayes + Gell-Mann Amnesia | Falsifiability |
| Major policy/org change | Chesterton's Fence + Unintended Consequences | Overton Window |
| Growth plateau | Network Effects + Phase Transition | Pareto |

---

## Model Count Summary

| Discipline | Models in this catalog |
|-----------|----------------------|
| Physics / Engineering | 9 |
| Biology / Evolution | 7 |
| Mathematics / Statistics | 7 |
| Psychology / Behavioral | 12 |
| Economics / Game Theory | 8 |
| Philosophy / Logic | 6 |
| Systems Thinking | 4 |
| Strategy / Organizations | 4 |
| **Total** | **57** |

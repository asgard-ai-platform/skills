# Shell Method: Scenario Planning as Practiced at Royal Dutch Shell

## Origin and Why Shell's Version Is Different

Most "scenario planning" advice describes a worksheet exercise: brainstorm futures, pick two axes, fill in four quadrants. Shell's method, developed by Pierre Wack and Ted Newland in the Group Planning division from 1967 onward, differs in one crucial way: **scenarios must change the mental models of decision-makers, not just inform them.**

Wack's two landmark HBR articles (1985) document what Shell actually did — and why it worked when other forecasting failed. The 1973 oil shock did not surprise Shell because their planners had already walked executives through a detailed, named, believable world in which oil-producing countries coordinated to raise prices. When signals of that world appeared, Shell's managers recognized them and acted. Competitors did not.

The method has three conceptual pillars that differ from generic 2×2 exercises:

1. **Predetermined elements** vs. **critical uncertainties** — not everything is uncertain
2. **Decision focus** — scenarios are built around a specific decision, not around "the future" in general
3. **Microcosm shift** — the goal is not to deliver a report but to change how executives see the world

---

## Pillar 1: Predetermined Elements

**Definition**: A predetermined element is a future development that is already decided by forces already set in motion — regardless of which scenario unfolds.

Wack's test: *"If you were living in any of the four scenarios ten years from now, would this thing be true in all of them?"* If yes, it's predetermined. It belongs in your base assumptions, not in your uncertainty axes.

**Examples of predetermined elements (1970s oil context):**

| Fact | Why predetermined |
|------|-------------------|
| OECD oil consumption will grow 3-5% annually through 1980 | Existing car fleets, infrastructure lock-in, no substitute available at scale |
| Major Middle East oil fields take 8-12 years to develop | Engineering / capital cycle already set |
| Shah of Iran cannot raise oil output faster than ~10%/yr | Absorptive capacity of Iranian economy |
| OPEC members share the same structural incentive to raise revenue | Sovereign debt levels, development spending commitments |

These facts constrain the scenario space. They are not debated across scenarios — they appear in all four quadrants. Wasting an axis on a predetermined element is a common mistake that dilutes the method.

**How to identify predetermined elements:**

1. Look for developments driven by **long lead times** (capital projects, demographic shifts, regulatory processes already in motion)
2. Look for structural **incentive alignments** — multiple independent actors with the same direction of interest
3. Apply the "already in the pipeline" test: is the seed of this development already planted?

Shell's 1972 analysis identified that *most* of what would happen to energy markets by 1985 was already determined. The genuine uncertainty was narrow: would OPEC coordinate, and when?

---

## Pillar 2: Critical Uncertainties — Selection Criteria

After removing predetermined elements, you are left with genuine uncertainties. The parent SKILL.md says to pick forces that are both high-impact and high-uncertainty. Shell's method adds three further filters:

### Filter A: Independence Test

The two axes must be **causally independent**. If Axis 1 moving in one direction makes Axis 2 more likely to move in the same direction, they are correlated and should be collapsed into one axis.

**Correlated (bad pair):**
- Axis 1: AI regulation becomes strict
- Axis 2: AI development slows

These tend to move together. A single axis "regulatory and technological momentum" captures it better.

**Independent (good pair):**
- Axis 1: AI regulation becomes strict vs. permissive
- Axis 2: Economic conditions: growth vs. recession

Regulation can be strict during growth (EU approach) or permissive during recession (deregulation push), and vice versa. All four quadrants are plausible.

**Independence check**: Draw a simple 2×2. Ask "Is this quadrant [A=high, B=high] genuinely plausible? Could someone argue for it with a straight face?" If any quadrant collapses (i.e., you cannot construct a credible story for it), your axes are correlated.

### Filter B: Decision Relevance Test

The axes should create scenarios that **change the optimal decision**. If your strategy would be the same regardless of which scenario unfolds, the axes are not doing their job.

Shell's test question: *"For our focal decision, does it matter which world we're in?"*

If Axis 1 flips from endpoint A to endpoint B but the board's decision doesn't change, drop that axis and try another.

### Filter C: The "Unthinkable" Test

At least one scenario quadrant should be the world your executives least want to think about. If all four scenarios feel roughly comfortable, you have not found the true uncertainty space — you have unconsciously filtered it to protect the official future.

Shell's 1972 planners noticed that all internal forecasts assumed OPEC would not coordinate. They deliberately constructed a scenario assuming it did. This was the uncomfortable quadrant. It proved decisive.

---

## Pillar 3: The Decision Focus

Shell's scenarios are not built around "the future of energy" in the abstract. They are built around a specific strategic decision:

> *"Should we commit capital to develop North Sea oil fields at current cost projections?"*

This focus changes how you run every step:

| Generic scenario planning | Shell decision-focused |
|--------------------------|----------------------|
| Brainstorm all driving forces | Brainstorm forces relevant to this decision's economics |
| Four general "world futures" | Four futures that affect the IRR of this specific investment |
| Evaluate strategies in general | Evaluate this specific capital allocation across four futures |
| Outcomes are "insights" | Outcomes are go/no-go thresholds |

Without a focal decision, scenario planning produces interesting narrative but no action. With a focal decision, each scenario produces a specific recommendation or triggers a specific contingency plan.

**How to define the focal decision:**

Write it as: *"Given uncertainty about [X and Y], we need to decide [specific action] by [date]."*

Example: *"Given uncertainty about AI regulation and competitor adoption speed, we need to decide whether to build proprietary AI infrastructure or remain API-dependent by Q3 2026."*

---

## The Shell 6-Step Process (Detailed)

This is the formalized version of Wack's method, as documented in Shell's internal planning guides and later reconstructed by Kees van der Heijden (Shell scenario planner, 1989).

### Step 1: Define the Focal Issue and Time Horizon

- State the decision in one sentence
- Set a time horizon: long enough for uncertainty to matter, short enough to reason about concretely (Shell typically used 10-20 years for energy; most business decisions use 5-10 years)
- List the key stakeholders whose behavior will determine which scenario unfolds

### Step 2: Identify Key Factors in the Local Environment

These are factors closest to the focal decision:

- Customer behavior
- Competitor responses
- Supplier conditions
- Regulatory posture specific to this market

These are not the scenario axes yet — they are the outputs that the axes will affect.

### Step 3: Identify Driving Forces in the Macro Environment

STEEP scan (Social, Technological, Economic, Environmental, Political). Generate 15-20 candidate forces. For each:

- What is the current trajectory?
- What evidence would tell you the trajectory is changing?
- Who are the key actors that influence this force?

### Step 4: Rank by Impact × Uncertainty

Build a 2×2 ranking grid:

```
             LOW UNCERTAINTY         HIGH UNCERTAINTY
HIGH IMPACT  [Predetermined          [SCENARIO AXES
             elements — put          CANDIDATES]
             in base case]

LOW IMPACT   [Ignore]                [Monitor but
                                     don't use as axes]
```

Rank only the top-right quadrant. Select 4-6 candidates for Step 5.

### Step 5: Select the Scenario Logic (the Two Axes)

From your 4-6 candidates, apply the three filters from Pillar 2:
1. Independence test
2. Decision relevance test
3. "Unthinkable" test

Select the two that pass all three filters. Name each endpoint with a specific, concrete descriptor — not "high" and "low" but a phrase that tells a story:

| Instead of... | Use... |
|---------------|--------|
| "Regulation: high vs low" | "Regulation: EU-style mandatory pre-approval vs US-style post-market enforcement" |
| "Technology: fast vs slow" | "AI reasoning: specialized narrow tools vs general-purpose agents that replace knowledge workers" |
| "Economy: good vs bad" | "Capital markets: cheap debt and high risk appetite vs rate shock and flight to safety" |

### Step 6: Write the Four Scenario Narratives

Each narrative is **200-400 words** for a full planning exercise (shorter for internal use). Structure each as:

1. **Name**: Memorable, evocative, not "Scenario A" (Shell used names like "The Rapids," "New Frontiers," "Barricades," "Just Do It")
2. **Headline**: One sentence summarizing the world
3. **How we got here**: 2-3 key events that led from today to this world (the causal pathway)
4. **What this world looks like**: Who won, who lost, what changed, what stayed the same
5. **Implications for our focal decision**: Specific numbers or conditions if possible

---

## Worked Example: Platform AI Infrastructure Decision (2026)

**Focal decision**: Should an e-commerce platform build proprietary LLM fine-tuning infrastructure or remain dependent on API providers (OpenAI, Anthropic, Google)?  
**Time horizon**: 2026–2031  
**Decision deadline**: Q3 2026 (capital commitment of ~$40M)

### Step 4 Output: Ranked Driving Forces

| Force | Impact | Uncertainty | Candidate? |
|-------|--------|-------------|------------|
| API pricing trajectory | H | H | ✓ |
| AI regulation (EU AI Act enforcement) | H | H | ✓ |
| Competitor AI adoption speed | H | M | — |
| Talent availability (ML engineers) | M | H | — |
| General economic conditions | M | M | — |
| Data privacy legislation | H | H | ✓ |
| Open-source model quality | H | H | ✓ |
| Consumer trust in AI | M | H | — |

Top candidates: API pricing, AI regulation, open-source model quality, data privacy.

### Step 5: Axis Selection

**Independence test:**
- API pricing × open-source quality: correlated (if open-source improves, API pricing is pressured downward). Collapse.
- API pricing + open-source quality → single axis: **"AI capability access: commoditized vs. proprietary moat"**
- Regulation × capability access: independent. Strict regulation doesn't cause or prevent commoditization of models.

**Decision relevance test:**
- If capability access is "commoditized" (models are cheap, open-source is strong): staying API-dependent is viable.
- If capability access is "proprietary moat" (incumbents lock in advantages): must build or partner.
- If regulation is strict: proprietary infrastructure requires compliance overhead; also affects data moat.
- If regulation is permissive: data advantage compounds faster for whoever builds first.
- All four quadrants change the optimal decision. ✓

**Final axes:**
- Axis 1: **AI capability access** — Commoditized (open-source parity, low API cost) vs. Proprietary Moat (incumbents lock in data + compute advantages)
- Axis 2: **Regulatory environment** — Permissive (light-touch, data flows freely) vs. Restrictive (mandatory audits, data localization, model approval)

### Step 6: Four Scenario Narratives

```
                    PERMISSIVE REGULATION   RESTRICTIVE REGULATION
COMMODITIZED    │  "Open Bazaar"           │  "Regulated Commons"
                │                          │
PROPRIETARY     │  "Winner's Game"         │  "Fortress and Moat"
MOAT            │                          │
```

---

**"Open Bazaar"** *(Commoditized + Permissive)*  
By 2029, open-source models (LLaMA successors, Mistral) match GPT-4-class performance for most e-commerce tasks. API costs have fallen 80% from 2025. Regulation is light — the EU AI Act's high-risk classifications exclude most e-commerce use cases. Any company can access frontier capability for cents per thousand tokens. The competitive advantage has shifted entirely to data quality and UX, not model access. Building proprietary infrastructure is over-investment.  
*Decision implication: Stay API-dependent. Invest the $40M in data pipelines and personalization UX instead.*

---

**"Regulated Commons"** *(Commoditized + Restrictive)*  
Models are commoditized, but the EU AI Act's 2028 enforcement wave requires mandatory audits, training data disclosure, and model cards for any AI touching consumers. Data localization requirements mean Taiwan/SEA operations must use regionally-hosted models. Open-source models proliferate but must be self-hosted for compliance. API providers cannot guarantee audit trails. Companies that built their own infrastructure have an unexpected compliance advantage — they can demonstrate control.  
*Decision implication: Build infrastructure, but prioritize compliance architecture over raw performance. The $40M is justified on risk-management grounds alone.*

---

**"Winner's Game"** *(Proprietary Moat + Permissive)*  
By 2028, OpenAI and Google have locked major e-commerce platforms into enterprise contracts with proprietary fine-tuning pipelines. Data flywheel effects compound: platforms that share behavioral data with API providers get better models; competitors without data-sharing agreements get generic performance. Regulation never materialized. The platforms that committed to proprietary infrastructure in 2026 now control their model destiny; API-dependent platforms face pricing leverage and capability gaps.  
*Decision implication: Build now or fall behind. This is the scenario where the $40M investment has the highest return — but also where moving in 2027 instead of 2026 costs 2-3x more.*

---

**"Fortress and Moat"** *(Proprietary Moat + Restrictive)*  
The most uncomfortable quadrant. Model incumbents have locked in capability advantages AND regulation has increased switching costs. EU AI Act requires approved model lists; only models from certified providers can touch consumer data. Three providers (OpenAI, Google, Anthropic) hold certification; open-source models are not certified. Building proprietary infrastructure requires your own certification process — 18-month approval timeline, €2M+ per market. Small platforms cannot afford it. This world creates a permanent two-tier AI market: certified incumbents and everyone else.  
*Decision implication: The $40M may be insufficient. Either commit $120M+ to full certification infrastructure or accept permanent API dependency with no path to proprietary capability. There is no middle option.*

---

### Strategy Robustness Test

| Strategy option | Open Bazaar | Regulated Commons | Winner's Game | Fortress & Moat |
|----------------|------------|------------------|---------------|-----------------|
| Stay API-dependent | ✓ | △ (compliance risk) | ✗ | ✗ |
| Build full proprietary infra ($40M) | △ (over-investment) | ✓ | ✓ | △ (insufficient) |
| Hybrid: API + self-hosted open-source | ✓ | ✓ | △ | ✗ |
| Strategic partnership with one incumbent | △ | △ | ✓ | ✓ |
| Defer decision 12 months | ✓ | ✗ | ✗ | ✗ |

**Robust strategy**: Hybrid (API + self-hosted open-source) works in 3/4 scenarios. It fails only in Fortress & Moat, which also happens to be the scenario requiring the most capital regardless.  
**Fragile strategy**: "Defer decision" works only if Open Bazaar unfolds.

---

## Contingency Triggers (Early Warning Signals)

Shell's method requires converting scenarios into **observable leading indicators** — signals that tell you which scenario is beginning to unfold. These are monitored quarterly.

| Signal | If observed → scenario evidence | Action threshold |
|--------|--------------------------------|-----------------|
| OpenAI/Anthropic enterprise contract length exceeds 3 years with data-sharing clauses | Winner's Game or Fortress & Moat unfolding | Escalate infrastructure decision to board |
| Open-source model (Hugging Face leaderboard) closes gap with GPT-4 to <5% on e-commerce benchmarks | Open Bazaar or Regulated Commons | Delay proprietary build; invest in OSS integration |
| EU AI Act enforcement actions exceed 10 companies in 12 months | Regulatory axis moving to Restrictive | Begin compliance audit of all AI pipelines |
| API pricing falls >40% year-over-year for 2 consecutive years | Commoditized axis confirmed | Re-evaluate proprietary infra business case |
| Competitor announces proprietary fine-tuning in production | Winner's Game signal | Accelerate timeline, not strategy |

---

## The "Remarkable People" Principle

Wack observed that the first time Shell ran scenarios (1971-72), executives acknowledged the work intellectually but did not change their mental models or their plans. The oil crisis scenarios were presented as data. Nothing changed.

For the 1973 re-run, Wack restructured the exercise: instead of presenting scenarios as external reports, he structured workshops where executives *inhabited* each scenario — made decisions inside it, encountered the characters who would populate it, traced the causal chain from today to that world.

The difference is between **informing** and **reperceiving**. Scenarios must make the decision-maker feel the world, not just understand it.

**Practical implication for narrative writing:**

Weak narrative (informing):  
> "In this scenario, AI regulation increases and compliance costs rise 30%."

Strong narrative (reperceiving):  
> "Your head of engineering calls you in March 2029. The EU has just served a notice on your German subsidiary: your recommendation engine must be audited within 90 days, or it goes offline. The audit requires full training data provenance, which you don't have because you've been using OpenAI's API. OpenAI's legal team says data provenance documentation is proprietary. Your lawyer estimates €800K and six months minimum. Meanwhile, your Berlin competitor — who built their own fine-tuned model two years ago — has already passed certification."

The second version makes the decision-maker feel the constraint in their body. That's the goal.

---

## Common Failures in Applying the Shell Method

**Failure 1: Axes selected on convenience, not independence.**  
Teams often pick axes that "feel important" but are correlated. The result: two quadrants are nearly identical, one is implausible, and the exercise loses its exploratory value. Apply the independence test before committing to axes.

**Failure 2: Predetermined elements treated as uncertainties.**  
Putting a predetermined element on an axis wastes one of two slots. The result: three of the four scenarios are actually the same world with minor variations. Before selecting axes, explicitly list predetermined elements and remove them from consideration.

**Failure 3: Scenarios without causal pathways.**  
A scenario that jumps from "today" to "2031 world" without explaining how we got there is not a scenario — it's a wish or a fear. Executives cannot internalize a world they cannot trace from the present. Each scenario needs at least 3 concrete events that chain from now to the endpoint.

**Failure 4: Strategy testing done after everyone has already decided.**  
The robustness matrix is most valuable when it surprises the team. Run it before the preferred strategy is identified, not as post-hoc validation. If the team has already anchored on "build proprietary infrastructure," the matrix will unconsciously be biased toward confirming it.

**Failure 5: Monitoring triggers never assigned to an owner.**  
Early warning signals that are not assigned to a specific person with a specific review cadence will never be monitored. Each trigger row in the contingency table should have an owner and a review date.

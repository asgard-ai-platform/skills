# Example: Should We Launch a Freemium Tier?

## Scenario

**Company**: Formly — B2B form automation SaaS, 18 months old  
**ARR**: NT$12M (~USD 375K), ~180 paying customers (avg NT$67K/yr)  
**Situation**: Growth has plateaued at ~8 new customers/month for 3 months. The sales team is pushing for a freemium tier to widen the top of funnel. Engineering estimates 6 weeks to build a feature-gated free plan. The CEO asks: "Should we do this?"

---

## Analysis

### Step 1 — State the decision

> Should Formly introduce a freemium tier to reignite customer growth, or find another lever?

---

### Step 2 — Select 2–3 models from different disciplines

| # | Model | Discipline |
|---|-------|-----------|
| 1 | **Inversion** | Physics / Engineering |
| 2 | **Incentive-caused bias** | Psychology |
| 3 | **Red Queen effect** | Biology |

Selected because: Inversion prevents wishful thinking about freemium upside. Incentive-caused bias exposes whose interests are actually driving the proposal. Red Queen tests whether freemium is structurally necessary for the competitive environment.

---

### Step 3 — Apply each model

#### Model 1: Inversion

*Instead of "how does freemium help us grow?" ask "how would freemium cause us to fail?"*

Failure modes if freemium launches:

- **Support cost explosion**: Free users open tickets at the same rate as paid users but generate zero revenue. At 500 free users, support load could triple with no corresponding revenue increase. Current CS headcount: 1 person.
- **Positioning erosion**: Formly's current ICP (HR teams at 50–200 person companies) chose Formly specifically because it *looks* like a paid-tier-only tool (signals seriousness). A free plan may attract SMBs and solo founders who churn without converting, distorting cohort metrics and spooking future investors.
- **Engineering distraction**: The 6-week estimate is for build, not ongoing maintenance. Feature-gating logic adds complexity to every future feature release.

Inversion verdict: **The failure modes are concrete and near-term. The upside (free→paid conversion) requires assumptions about conversion rate that we have no data to support.**

---

#### Model 2: Incentive-caused bias

*Who is asking for this, and what are they incentivized to care about?*

- **Sales team**: Compensated on new logos closed. A free plan gives them a warmer lead pool. They benefit from freemium even if free→paid conversion is low, because it makes their job easier.
- **Engineering**: Proposing the feature. Engineers are often incentivized to build (learning, scope, career). The 6-week estimate may understate maintenance cost.
- **CEO (decision-maker)**: Feeling pressure from plateau. "Launch freemium" is visible action — it *feels* like doing something. The bias toward action over analysis is high when growth stalls.
- **Paying customers**: Not in the room. They have no voice in this decision. Their incentive is a focused product that solves their problem without bloat.

Incentive-caused bias verdict: **Every stakeholder in the room is biased toward launching. The only constituency biased against is paying customers (revenue base), and they weren't asked.**

---

#### Model 3: Red Queen effect

*Does the competitive environment require freemium just to stay competitive?*

Formly's top 3 competitors:
| Competitor | Freemium? | ARR estimate |
|-----------|-----------|-------------|
| Typeform | Yes (2014) | ~USD 60M |
| Tally | Yes (core product) | ~USD 3M |
| Jotform | Yes (since founding) | ~USD 35M |

The category leaders all have freemium. However:
- Typeform and Jotform are horizontal (any user, any form type). Formly is vertical (HR workflows, compliance forms).
- Formly's paying customers aren't choosing Formly over Typeform's free tier — they're choosing it over *paying* for Typeform Enterprise because it has HR-specific logic (conditional routing, HRIS integrations, e-signature compliance).

Red Queen verdict: **Freemium is required to compete in horizontal form-builders. It is NOT required in Formly's actual competitive set (HR-specific tools), where buyers evaluate on fit, not price entry point.**

---

### Step 4 — Compare conclusions

**Where models agree (high confidence):**
- The proposal is being driven by internal incentive pressures, not external competitive necessity.
- The downside risks (support cost, positioning, engineering complexity) are concrete; the upside is speculative.

**Where models disagree (key trade-off):**
- Inversion says avoid freemium entirely (failure modes too concrete).
- Red Queen says *eventually* freemium may be necessary if competitors move into the HR vertical — timing is the open question.

The disagreement reveals the actual decision: **this is not "freemium vs. no freemium forever" — it's "freemium now vs. freemium when the competitive signal is clearer."**

---

### Step 5 — Synthesize

The plateau (8 customers/month for 3 months) is the real problem. Freemium is one proposed solution — but the models expose it as solving the *team's anxiety* more than the *growth problem*.

Alternative levers to test first, each reversible and cheaper than 6 weeks of engineering:
1. **Diagnosis audit**: Interview the last 20 companies that evaluated Formly but didn't buy. Find the real objection. (Cost: ~2 weeks of sales time)
2. **Expansion revenue**: Do the 180 existing customers have untapped seats? A structured expansion play may be faster to ARR than new logo acquisition.
3. **Channel experiment**: Partner with 2 HRIS vendors (BambooHR, Rippling) on co-marketing. If Formly is an HR-specific tool, distribution through HR platforms is higher-signal than freemium volume.

---

## Result

```markdown
# Multi-Model Analysis: Should Formly Launch Freemium?

## Models Applied
| Model | Discipline | Insight |
|-------|-----------|---------|
| Inversion | Engineering | Failure modes (support cost, positioning erosion, eng complexity) are concrete and near-term; upside depends on unverified conversion rate assumptions |
| Incentive-caused bias | Psychology | Every internal stakeholder is biased toward launching; the one stakeholder biased against it (paying customers) was not consulted |
| Red Queen effect | Biology | Freemium is table stakes in horizontal form-builders but NOT in HR-vertical tools — Formly's actual competitive set |

## Convergence
All three models agree: **do not launch freemium now.** The proposal is
internally motivated, competitively premature, and carries concrete
near-term costs against speculative long-term benefits.

## Divergence
Red Queen acknowledges freemium may eventually be necessary if competitors
move into the HR vertical. This creates a "not now, but monitor" posture —
not a permanent no.

## Synthesis
**Recommendation**: Decline freemium launch for Q2. Instead, run a 4-week
diagnostic sprint: interview 20 churned evaluators, audit expansion revenue
in current 180 accounts, and pilot one HRIS co-marketing partnership.
Revisit freemium in Q3 with data, not anxiety, driving the decision.

**Trigger to revisit**: If a direct HR-vertical competitor (e.g., Leapsome
Forms, Lattice Surveys) launches a free tier, fast-follow within 60 days.
```

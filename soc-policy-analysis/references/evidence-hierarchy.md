# Evidence Hierarchy for Policy Analysis

## The Hierarchy

Evidence quality runs from highest to lowest internal validity — the degree to which you can attribute observed outcomes to the policy itself rather than confounding factors.

```
Level 1  Systematic review / meta-analysis of RCTs
Level 2  Randomized Controlled Trial (RCT)
Level 3  Quasi-experiment (DiD, RD, IV, ITS)
Level 4  Observational study with controls (regression, matching)
Level 5  Case study / comparative case study
Level 6  Expert opinion / Delphi panel
Level 7  Anecdote / stakeholder testimony
```

Higher levels answer "does this policy cause the outcome?". Lower levels answer "does this outcome correlate with the policy?" — useful for generating hypotheses, not confirming causality.

---

## Level Definitions and Identifying Marks

### Level 1 — Systematic Review / Meta-Analysis

A structured search of all studies meeting pre-specified criteria, combined to produce a pooled estimate.

**Identifying marks:**
- Protocol registered before search (PROSPERO, OSF)
- Explicit inclusion/exclusion criteria
- PRISMA flow diagram
- Heterogeneity statistics (I², τ²)

**When to cite it:** When you find one, prefer it over any individual study. Check the search cutoff date — a 2015 meta-analysis may miss the best recent trials.

**Key journals:** *Campbell Collaboration* (social policy), *Cochrane* (health), *J3P* (3ie development).

---

### Level 2 — Randomized Controlled Trial (RCT)

Random assignment eliminates selection bias: treatment and control groups are identical in expectation on all observed and unobserved characteristics.

**Core estimator:**

```
ATE = E[Y | T=1] - E[Y | T=0]
```

where `T=1` is treated, `T=0` is control, and `Y` is the outcome.

**Threats to internal validity:**
| Threat | Description | Detection |
|--------|-------------|-----------|
| Attrition bias | Differential dropout | Compare dropout rates by arm |
| Contamination | Control group receives treatment | Check spillover; cluster RCT |
| Non-compliance | Not all treated units take up treatment | Report ITT and LATE (IV) |
| Hawthorne effect | Behavior changes from being observed | Blind if possible |

**Threats to external validity (the harder problem for policy):**
- Sample recruited from willing participants → results may not generalize
- Lab or pilot scale differs from full rollout (SUTVA violations at scale)
- Context specificity: an RCT in Kenya may not transfer to Taiwan

**Practical note:** RCTs in public policy are rare and expensive. When you find one, note: who funded it, what population, what scale, what time horizon.

---

### Level 3 — Quasi-Experiments

When randomization is impossible or unethical, quasi-experiments exploit natural variation to approximate a counterfactual.

#### Difference-in-Differences (DiD)

**Setup:** Treatment group exposed to policy at time T; control group not exposed.

```
DiD = (Ȳ_treat,post - Ȳ_treat,pre) - (Ȳ_control,post - Ȳ_control,pre)
```

**Identifying assumption:** Parallel trends — in the absence of the policy, treatment and control would have moved together. Test by plotting pre-treatment trends visually and with event-study coefficients.

**Worked example:** Taipei introduces mandatory helmet fines for scooters in Q1 2023. Control group: New Taipei (no change). Outcome: ER admissions for head injuries.

```
Taipei:    pre=120/month → post=80/month  (−40)
New Taipei: pre=110/month → post=105/month (−5)
DiD = (−40) − (−5) = −35 admissions/month attributable to policy
```

**Pitfall:** Parallel trends fails if something else changed in the treatment area simultaneously (e.g., a road safety campaign launched the same month).

---

#### Regression Discontinuity (RD)

**Setup:** Units just above and below a threshold are treated differently; near the threshold they are otherwise identical.

**Estimator:**
```
LATE = lim(x→c⁺) E[Y|X=x] - lim(x→c⁻) E[Y|X=x]
```
where `c` is the cutoff.

**Validity checks:**
- No bunching at cutoff (McCrary density test)
- Covariates smooth through cutoff
- Bandwidth sensitivity — results should be stable across bandwidth choices

**Policy example:** Firms with ≥50 employees must provide parental leave (a threshold). Compare firms with 48–49 vs. 50–51 employees on female hiring rates.

---

#### Instrumental Variables (IV)

**Setup:** An instrument `Z` affects treatment `T` but affects outcome `Y` only through `T`.

```
LATE = Cov(Y, Z) / Cov(T, Z)   [Wald estimator, binary Z]
```

**Validity conditions (must be argued, not tested empirically):**
1. Relevance: Z predicts T (testable — F > 10 is the rule of thumb)
2. Exclusion restriction: Z affects Y only via T (untestable — requires theory)
3. Monotonicity: Z affects all compliers in the same direction

**Classic policy instrument:** Draft lottery number as IV for military service → effect on earnings (Angrist 1990).

**Warning:** IV estimates the Local Average Treatment Effect (LATE) — the effect for compliers only. This may not generalize to the whole population.

---

#### Interrupted Time Series (ITS)

**Setup:** Long time series of outcome, intervention at known point. Estimate level change and slope change.

```
Y_t = β₀ + β₁·t + β₂·D_t + β₃·(t - T₀)·D_t + ε_t

where D_t = 1 if t ≥ T₀ (post-intervention)
```

- `β₂`: immediate level change at intervention
- `β₃`: change in slope after intervention

**Minimum data requirement:** ≥12 pre-intervention time points; more is better to model seasonality.

**Pitfall:** Any concurrent event (economic shock, media campaign) confounds the estimate. A comparison series (control region) strengthens the design.

---

### Level 4 — Observational with Controls

Regression, propensity score matching, or synthetic control without a clean natural experiment.

**Honest framing:** These establish correlation and can control for *observed* confounders. They cannot rule out omitted variable bias from *unobserved* confounders. Report them as "associated with" not "caused by".

**Sensitivity analysis to report:**
- Coefficient stability when adding controls (Oster 2019: bound on bias from unobservables)
- Omitted variable bias calculation: how large would an unobserved confounder need to be to explain the result?

---

### Level 5 — Case Studies

**When useful:**
- Mechanism tracing: how and why did the policy work?
- Plausibility probe before committing to a larger study
- Rare phenomena where N is inherently small

**Most rigorous form:** John Stuart Mill's methods — Method of Agreement (same outcome across different contexts with one common factor) and Method of Difference (different outcome across similar contexts, one difference).

**Honest limitation:** Cannot establish generalizability. One successful city ≠ national policy.

---

### Levels 6–7 — Expert Opinion and Anecdote

Use for:
- Identifying what questions to ask
- Generating hypotheses
- Filling gaps where no formal evidence exists
- Political feasibility assessment (practitioners know what will work institutionally)

Do **not** use as primary evidence for causal claims. If a policy recommendation relies primarily on Level 6–7 evidence, say so explicitly.

---

## Evidence Quality Scoring Table

When you evaluate evidence for a policy claim, complete this table:

| Dimension | Score 1 | Score 2 | Score 3 |
|-----------|---------|---------|---------|
| **Design** | Anecdote/opinion | Observational | RCT/quasi-experiment |
| **Sample** | Convenience, small N | Representative, moderate N | Population-level, large N |
| **Context match** | Different country/sector | Similar context | Same context |
| **Replication** | Single study | 2–3 studies | Meta-analysis |
| **Recency** | >10 years ago | 5–10 years | <5 years |

**Total score interpretation:**
- 5–7: Low confidence — treat as hypothesis-generating
- 8–11: Moderate confidence — acknowledge uncertainty in recommendation
- 12–15: High confidence — appropriate for strong recommendation

---

## Applying the Hierarchy in Policy Analysis

### Step 1: State the causal claim you need evidence for

Be precise: "Policy X causes outcome Y in population Z." Vague claims invite vague evidence.

### Step 2: Search for the strongest available evidence first

Search order:
1. Campbell / Cochrane systematic reviews
2. 3ie Development Evidence Portal (for development interventions)
3. What Works Clearinghouse (education)
4. Government evidence repositories (UK What Works Centres, US MDRC)
5. Google Scholar for peer-reviewed quasi-experiments
6. Grey literature (think tanks, government evaluations) — use with caution

### Step 3: Assess internal validity of what you find

For each study, ask:
- What is the study design? (Level 1–7)
- What is the identifying assumption, and is it plausible?
- Were there any major threats to validity the authors acknowledge?

### Step 4: Assess external validity (context transfer)

Even a perfect RCT in Oslo may not apply to Taipei. Check:
- Population: demographics, behavior, institutions similar?
- Implementation context: administrative capacity comparable?
- Scale: pilot effect vs. system-wide rollout?

### Step 5: Document the evidence explicitly in your policy analysis

In the Evaluation Matrix, add an evidence quality notation:

```markdown
| Criterion | Option A | Evidence |
|-----------|----------|----------|
| Effectiveness | H | DiD study, Taiwan context (Li et al. 2022) |
| Equity | M | Observational only; no distributional analysis |
| Feasibility | H | Expert consensus; 3 comparable cities implemented |
```

---

## Common Mistakes When Using Evidence

**Mistake 1: Citing the study, not the estimate**
"Studies show this policy works" — which studies? In what context? What effect size?

Correct: "Li et al. (2022) find a 23% reduction (95% CI: 14–32%) in injuries using a DiD design on Taiwan municipal data."

**Mistake 2: Ignoring null results and publication bias**
Published studies skew toward positive findings. A single positive RCT may be the one lucky trial among several unpublished nulls. Check registries (AEA RCT Registry, ClinicalTrials.gov) for registered-but-unpublished studies.

**Mistake 3: Treating correlation as causation to fit a preferred policy**
If your preferred option only has Level 4 evidence but a rival option has Level 2 evidence, that comparison must appear in the policy analysis. Omitting it is intellectually dishonest.

**Mistake 4: Context laundering**
Taking a study from a high-income, high-capacity context and applying it to a low-capacity context without noting the mismatch. Administrative feasibility often mediates whether evidence from elsewhere transfers.

**Mistake 5: Ignoring effect size**
Statistical significance ≠ policy significance. A statistically significant 0.5% reduction in injuries may not justify the cost of implementation. Always report effect sizes and practical significance alongside p-values or confidence intervals.

---

## Evidence Language Guide

Match your language to the evidence you have:

| Evidence level | Appropriate language |
|---------------|---------------------|
| Level 1–2 | "evidence demonstrates", "has been shown to cause" |
| Level 3 | "quasi-experimental evidence suggests", "associated with a reduction of X% after controlling for..." |
| Level 4 | "correlates with", "is associated with" |
| Level 5 | "consistent with the hypothesis that", "in the case of [city], this approach was followed by..." |
| Level 6–7 | "practitioners report", "stakeholders indicate", "in the view of [expert]" |

Avoid: "evidence shows" for Level 4–7. Avoid: "proven" for anything below Level 1–2 with replication.

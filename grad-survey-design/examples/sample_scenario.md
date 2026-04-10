# Example: Measuring Psychological Safety and Knowledge Sharing in Remote Teams

## Scenario

A PhD student at National Taiwan University is designing a quantitative study for her dissertation. The research model posits that **psychological safety** (PS) predicts **knowledge sharing intention** (KSI) among remote software engineers, mediated by **trust in teammates** (TT). She has already reviewed the literature and has a draft questionnaire of 18 items. She asks:

> "My advisor says my α for psychological safety is too low and I might have CMV issues since everything is collected in the same survey. How do I fix this?"

Her draft items, all on a 7-point Likert scale (1 = Strongly Disagree, 7 = Strongly Agree):

**Psychological Safety (PS)** — adapted from Edmondson (1999):
- PS1: I can speak up about problems on this team without fear.
- PS2: It is easy to discuss mistakes on this team.
- PS3: No one on this team would deliberately undermine my efforts.
- PS4: My unique skills are valued on this team.
- PS5: It is safe to take risks on this team.
- PS6_R: Team members reject others who are different. *(reverse-coded)*

**Trust in Teammates (TT)** — adapted from McAllister (1995):
- TT1: I can rely on team members to keep their commitments.
- TT2: Team members are honest with me.
- TT3: I have confidence in team members' abilities.
- TT4_R: I sometimes doubt whether team members have my best interests in mind. *(reverse)*
- TT5: Team members share important information proactively.

**Knowledge Sharing Intention (KSI)** — adapted from Bock et al. (2005):
- KSI1: I intend to share my technical knowledge with teammates.
- KSI2: I plan to provide documents or manuals I have created.
- KSI3: I would share my expertise even without being asked.
- KSI4: I intend to help teammates solve technical problems.
- KSI5: I expect to participate in team knowledge repositories.

After pilot testing with N = 42 remote engineers, her CFA output is:

| Item | Loading | Construct |
|------|---------|-----------|
| PS1 | 0.71 | PS |
| PS2 | 0.68 | PS |
| PS3 | 0.64 | PS |
| PS4 | 0.55 | PS |
| PS5 | 0.72 | PS |
| PS6_R | 0.31 | PS |
| TT1 | 0.78 | TT |
| TT2 | 0.81 | TT |
| TT3 | 0.76 | TT |
| TT4_R | 0.39 | TT |
| TT5 | 0.74 | TT |
| KSI1 | 0.82 | KSI |
| KSI2 | 0.79 | KSI |
| KSI3 | 0.80 | KSI |
| KSI4 | 0.84 | KSI |
| KSI5 | 0.77 | KSI |

Cronbach's α: PS = 0.67, TT = 0.74, KSI = 0.88  
Pilot Harman's single-factor test: first factor explains 41% of variance.

---

## Analysis

### Step 1 — Construct Operationalization Review

The three constructs are well-grounded in established scales. Edmondson's PS is a team-level perception construct; adapting it to individual-level remote settings is valid but should be noted. KSI is behavioral intention, measured correctly as reflective indicators. No dimension or item coverage gaps identified.

### Step 2 — Item Pruning Based on Pilot Loadings

Two items fail the **loading threshold (≥ 0.60)**:

| Item | Loading | Action |
|------|---------|--------|
| PS6_R | 0.31 | **Drop** — reverse-coded items often form artifactual factors in CFA; this item also conflates interpersonal exclusion with safety climate |
| PS4 | 0.55 | **Borderline** — "skills are valued" taps recognition, not safety; consider dropping or replacing with "I feel safe admitting I don't know something" |
| TT4_R | 0.39 | **Drop** — same reverse-coding artifact issue; doubting intent is not semantically equivalent to trusting capability |

**Recommendation**: Drop PS6_R and TT4_R entirely. Replace PS4 with a confirmed-domain item (e.g., "I feel safe disagreeing with senior engineers on this team") and retest. Retain 5 PS items, 4 TT items, 5 KSI items = 14 items total.

### Step 3 — Reliability and Validity Recalculation

After dropping the two weak reverse-coded items, estimated metrics for the revised scale:

**Reliability**

| Construct | Items | Cronbach's α | CR (est.) | AVE (est.) |
|-----------|-------|-------------|-----------|------------|
| PS | 5 (dropped PS6_R, revised PS4) | 0.74* | 0.77 | 0.46* |
| TT | 4 (dropped TT4_R) | 0.81 | 0.83 | 0.55 |
| KSI | 5 | 0.88 | 0.90 | 0.64 |

*PS AVE is marginal (0.46 < 0.50). Two paths forward:
1. Add one more high-loading item to the PS pool (CR ≥ 0.70 is met, so the scale is publishable with a noted limitation)
2. Report CR as the primary reliability indicator (preferred over α — see Gotcha #1)

**Convergent Validity**

All remaining loadings ≥ 0.64. KSI and TT pass AVE ≥ 0.50. PS is marginal — disclose in limitations.

**Discriminant Validity — Fornell-Larcker Criterion**

√AVE must exceed inter-construct correlations:

| | PS (√AVE = 0.68) | TT (√AVE = 0.74) | KSI (√AVE = 0.80) |
|--|--|--|--|
| PS | **0.68** | | |
| TT | 0.52 | **0.74** | |
| KSI | 0.48 | 0.55 | **0.80** |

All √AVE values exceed the corresponding off-diagonal correlations. Discriminant validity is supported.

HTMT check (estimated from pilot correlation matrix):

| Pair | HTMT | Threshold | Result |
|------|------|-----------|--------|
| PS ↔ TT | 0.61 | < 0.90 | Pass |
| PS ↔ KSI | 0.57 | < 0.90 | Pass |
| TT ↔ KSI | 0.67 | < 0.90 | Pass |

### Step 4 — CMV Control Plan

**Problem diagnosis**: Single-source, single-wave design is the core CMV risk. Harman's test first factor at 41% is below the commonly cited 50% threshold, but this test has very low power and a "pass" here is not sufficient evidence against CMV.

**Procedural remedies to implement before main data collection:**

| Remedy | Implementation |
|--------|---------------|
| Temporal separation | Collect PS and TT in Week 1; collect KSI two weeks later in a follow-up survey |
| Scale format variation | Use a frequency scale (Never → Always) for KSI1–KSI4 instead of agreement scale, to break response set carryover |
| Anonymity guarantee | Use an anonymous code (self-generated: mother's birth month + last 2 digits of student ID) to link Wave 1 and Wave 2 without identifiable data |
| Item randomization | Randomize item order within each construct block to reduce halo effects |

**Statistical remedies for main analysis:**

| Remedy | When to Run |
|--------|------------|
| Harman's single-factor test | Report as convention; note limitations explicitly |
| CFA marker variable | Include one theoretically unrelated item (e.g., "I prefer coffee over tea") as a marker; test if adding a common method factor improves fit |
| Full collinearity VIF | Run VIF for all latent constructs; VIF > 3.3 flags potential CMV (Kock, 2015) |

---

## Result

```markdown
## Survey Design: Psychological Safety and Knowledge Sharing in Remote Engineering Teams

### Construct Operationalization
| Construct | Dimensions | Items | Source |
|-----------|-----------|-------|--------|
| Psychological Safety (PS) | Unidimensional | 5 items | Edmondson (1999), adapted for remote/async context |
| Trust in Teammates (TT) | Cognitive trust | 4 items | McAllister (1995), cognition-based sub-scale only |
| Knowledge Sharing Intention (KSI) | Unidimensional | 5 items | Bock et al. (2005) |

### Reliability Assessment
| Construct | Items | Cronbach's α | CR | AVE |
|-----------|-------|-------------|-----|-----|
| PS | 5 | 0.74 | 0.77 | 0.46 ⚠️ |
| TT | 4 | 0.81 | 0.83 | 0.55 |
| KSI | 5 | 0.88 | 0.90 | 0.64 |

⚠️ PS AVE marginally below 0.50 threshold; CR ≥ 0.70 maintained. Disclosed as limitation.

### Validity Assessment
| Test | Result | Threshold | Assessment |
|------|--------|-----------|------------|
| Factor loadings (min, post-pruning) | 0.64 | ≥ 0.60 | Pass |
| AVE — TT | 0.55 | ≥ 0.50 | Pass |
| AVE — KSI | 0.64 | ≥ 0.50 | Pass |
| AVE — PS | 0.46 | ≥ 0.50 | Marginal |
| HTMT (max, TT ↔ KSI) | 0.67 | < 0.90 | Pass |
| Fornell-Larcker (all pairs) | √AVE > r | See table | Pass |

### CMV Controls
| Remedy | Type | Result |
|--------|------|--------|
| Two-wave temporal separation (2 weeks) | Procedural | Implemented in main study design |
| Frequency scale for KSI (vs. agreement) | Procedural | Breaks response-set carryover |
| Anonymous linking code | Procedural | Enables longitudinal matching without ID |
| Harman's single-factor test | Statistical | 41% (pilot); will rerun on full sample |
| CFA marker variable | Statistical | "Coffee preference" item added to Wave 1 |
| Full collinearity VIF | Statistical | To be run post-collection; threshold < 3.3 |

### Limitations
- PS AVE marginally below 0.50; CR is the primary reliability indicator reported
- Two-wave design reduces but does not eliminate CMV (both waves still self-report)
- Sample restricted to software engineers; PS operationalization may not generalize to non-technical roles
- Edmondson's original scale is team-level; individual-level adaptation requires measurement invariance testing if comparing across teams
```

# Advanced Agenda-Setting Models

## The Three-Level Framework

McCombs & Shaw's original (1972) study measured **first-level agenda-setting**: the transfer of *which objects* (issues) are salient. Two subsequent generations extended the theory:

| Level | What transfers | Unit of analysis | Key question |
|-------|---------------|-----------------|--------------|
| First | Object salience | Issues as whole units | Which issues does the public consider important? |
| Second | Attribute salience | Sub-dimensions of a single issue | Which aspects of an issue does the public focus on? |
| Third (Network) | Bundles of associated objects/attributes | Networks of issues or attributes | Which issues/attributes are mentally linked together? |

Each level presupposes the one before: you can only study attribute transfer (level 2) for issues that have already cleared the salience threshold (level 1).

---

## Second-Level Agenda-Setting

### Theoretical Core

For any issue X that has achieved media salience, the media also packages X with a set of *attributes* — descriptors, evaluations, and frames attached to it. Second-level agenda-setting claims that the attribute bundle prominent in media coverage becomes the attribute bundle prominent in public cognition.

Two types of attributes are distinguished:

- **Substantive attributes** — cognitive, factual dimensions (e.g., a politician's policy positions)
- **Affective attributes** — evaluative valence attached to those dimensions (positive / neutral / negative)

Gotcha: substantive and affective attribute transfer do **not** always move together. Media can make an attribute cognitively salient while expressing negative valence; the public may adopt the salience but form its own valence. Test them separately.

### Measurement Protocol

**Media side:**
1. Code each story/paragraph for the focal object X.
2. For each coded unit, record which attributes are mentioned and their valence (−1, 0, +1).
3. Aggregate: attribute salience score = proportion of stories mentioning attribute *a* × mean valence weight.

**Public side:**
1. Open-ended survey item: "When you think about [X], what comes to mind?"
2. Code responses into the same attribute taxonomy used for media coding.
3. Attribute salience = percentage of respondents mentioning attribute *a*.

**Correlation test (Spearman):**

```
rₛ = 1 − (6 × Σdᵢ²) / (n(n²−1))
```

where *dᵢ* is the rank-difference for attribute *i* between the media ranking and public ranking, and *n* = number of attributes coded.

**Worked example** (hypothetical, 6 attributes of a mayoral candidate):

| Attribute | Media rank | Public rank | d | d² |
|-----------|-----------|------------|---|----|
| Economic competence | 1 | 2 | −1 | 1 |
| Integrity | 2 | 1 | +1 | 1 |
| Leadership style | 3 | 4 | −1 | 1 |
| Policy detail | 4 | 5 | −1 | 1 |
| Personal background | 5 | 3 | +2 | 4 |
| Foreign affairs | 6 | 6 | 0 | 0 |

Σd² = 8, n = 6  
rₛ = 1 − (6×8)/(6×35) = 1 − 48/210 = 1 − 0.229 = **0.771**

A Spearman ρ ≥ 0.60 is conventionally treated as supporting second-level transfer in the literature.

### Affective Transfer Test

Code affective direction per attribute in both media and survey responses. Compute:

```
Affective match rate = (# attributes where media valence and public valence agree) / (total attributes)
```

A match rate significantly above 50% (binomial test) supports affective attribute transfer. In practice, affective transfer is weaker and less consistent than substantive transfer — don't assume they move in tandem.

---

## Third-Level: Network Agenda-Setting (NAS)

### Origin and Core Claim

Guo & McCombs (2011, 2016) proposed that media don't just transfer *individual* object or attribute salience — they transfer the **associative structure** among objects (or attributes) as a bundle. What becomes cognitively salient is not a ranked list of issues but a *network* of co-associated issues or attributes.

IRON LAW reinforcement: Media may not tell people what to think, but it now also tells them **which things to think about together**.

### NAS Measurement: Step-by-Step

#### Step 1 — Build the media co-occurrence network

For a corpus of N news articles covering k issues {I₁, I₂, … Iₖ}:

1. For each article, record which issues are mentioned.
2. Compute pairwise co-occurrence count: Cᵢⱼ = number of articles mentioning both Iᵢ and Iⱼ.
3. Normalize to cosine similarity (avoids bias from high-frequency issues):

```
sim(i,j) = Cᵢⱼ / √(Cᵢᵢ × Cⱼⱼ)
```

where Cᵢᵢ = total articles mentioning Iᵢ.

4. Threshold (e.g., sim ≥ 0.10) to produce the media issue network G_media.

#### Step 2 — Build the public association network

Survey instrument: "Please rate how closely related you think these pairs of issues are: [pair list], from 0 = not at all related to 10 = very closely related."

Average ratings across respondents to produce a k × k public association matrix G_public.

#### Step 3 — Test network correspondence

Use **QAP (Quadratic Assignment Procedure)** correlation to test whether G_media and G_public are similar in structure:

```python
# Pseudocode — libraries: numpy, scipy, or dedicated QAP packages
def qap_correlation(G1, G2, permutations=1000):
    observed_r = pearson_r(upper_triangle(G1), upper_triangle(G2))
    null_dist = []
    for _ in range(permutations):
        perm = random_permutation(range(k))
        G2_perm = permute_matrix(G2, perm)
        null_dist.append(pearson_r(upper_triangle(G1), upper_triangle(G2_perm)))
    p_value = mean(null_dist >= observed_r)
    return observed_r, p_value
```

Standard QAP implementations exist in R (`sna::qaptest`) and Python (`networkx` + custom permutation).

**Interpretation threshold:** r ≥ 0.30, p < 0.05 (one-tailed) is the conventional benchmark in published NAS studies.

#### Step 4 — Identify "gateway" issues

Compute betweenness centrality in G_media:

```
BC(v) = Σ_{s≠v≠t} σ(s,t|v) / σ(s,t)
```

where σ(s,t) = total shortest paths from s to t, and σ(s,t|v) = those passing through v.

High-betweenness nodes in the media network are *gateway issues* — issues that conceptually link otherwise unconnected topics. If the NAS hypothesis holds, these same nodes should show high betweenness in the public network.

---

## Intermedia Agenda-Setting

### What It Is

Before the media agenda influences the public agenda, elite media influence each other. Intermedia agenda-setting studies how salience flows *between media organizations*: wire services → print → broadcast → online → social.

### Classic Cascade Model

```
Tier 1 (wire/elite print) → Tier 2 (national broadcast) → Tier 3 (local/regional) → Tier 4 (social media)
```

Key finding: The lag is shorter for intermedia transfer (hours to days) than for media-to-public transfer (weeks). This has practical implications for campaign strategy: issue injection at Tier 1 propagates before the public reacts.

### Granger Causality Test for Intermedia Lag

Given daily issue salience time series for two outlets A and B:

```
B_t = α + Σᵢ βᵢ B_{t-i} + Σⱼ γⱼ A_{t-j} + ε_t
```

Test H₀: γⱼ = 0 for all j (A does not Granger-cause B). Reject → A precedes B.

Run the test bidirectionally to determine direction of influence. Typical lag window: 1–7 days for intermedia; 14–56 days for media-to-public.

**Practical steps:**
1. Collect daily story-count time series per issue per outlet.
2. Test stationarity (ADF test); difference if non-stationary.
3. Select lag order via AIC/BIC.
4. Run VAR model; extract Granger causality p-values.
5. Build directed influence graph across outlets.

---

## Model Selection Decision Framework

```
START: What is your research question?
│
├── "Which issues does the public consider important?" 
│     → First-level agenda-setting
│     → Measure: issue rankings, MIP survey, Spearman correlation
│
├── "Which aspects/dimensions of a single issue are salient?"
│     → Second-level agenda-setting
│     → Measure: attribute coding, separate substantive vs affective
│
├── "Which issues are mentally grouped together in public cognition?"
│     → Third-level / Network Agenda-Setting (NAS)
│     → Measure: co-occurrence networks, QAP correlation
│
├── "How does salience flow between media organizations?"
│     → Intermedia agenda-setting
│     → Measure: Granger causality on time series
│
└── "Who/what drives the media agenda in the first place?"
      → Agenda-building (outside the McCombs lineage)
      → Measure: source analysis, PR dataset vs coverage correlation
```

If multiple levels apply (common in strategic communication analysis), execute them in order: first-level → second-level → NAS. Each level's findings constrain the interpretation of the next.

---

## Practical Pitfalls Specific to Advanced Models

**Second-level:**
- Attribute taxonomy drift: media coders and survey coders often develop divergent category systems mid-project. Anchor both to a pre-specified codebook before data collection.
- Candidate/issue asymmetry: second-level effects are consistently stronger for candidates than for policy issues. Do not generalize candidate-attribute findings to issue-attribute contexts.

**NAS:**
- Co-occurrence networks are sensitive to the unit of analysis (article vs paragraph vs sentence). Paragraph-level co-occurrence inflates ties; article-level deflates them. Report which unit was used.
- QAP requires k ≥ 8 issues to have enough matrix cells for stable permutation results. With fewer issues, treat QAP p-values as indicative only.

**Intermedia:**
- Social media volume is not comparable to legacy outlet story count without normalization. Normalize by platform baseline volume (e.g., daily tweets about any political topic) before running Granger tests.
- Granger causality tests temporal precedence, not mechanism. A Granger result only supports intermedia agenda-setting if you have also ruled out shared external shocks (e.g., a real-world event that simultaneously prompted all outlets to cover an issue).

---

## Key Empirical Benchmarks

| Model | Typical effect size | Measurement | Source context |
|-------|-------------------|-------------|----------------|
| First-level | rₛ = 0.50–0.90 | Media-public issue rank correlation | US election studies, 1970s–2000s |
| Second-level (substantive) | rₛ = 0.40–0.70 | Attribute rank correlation | Candidate attribute studies |
| Second-level (affective) | rₛ = 0.20–0.50 | Valence match rate | Lower and less consistent |
| NAS | r = 0.30–0.60 | QAP network correlation | Emerging; fewer replications |
| Intermedia | Granger p < 0.05, lag 1–3 days | Time-series precedence | Wire-to-print best documented |

Effect sizes are smaller in fragmented digital media environments. Do not benchmark against pre-2010 studies when analyzing contemporary social media-driven news cycles.

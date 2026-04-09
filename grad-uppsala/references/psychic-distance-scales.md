# Psychic Distance Scales

Psychic distance measurement falls into two distinct paradigms: **objective composite indices** (country-level data averaged to produce a scalar distance) and **perceptual survey instruments** (managers rate their own perceived uncertainty). Both paradigms measure different things and are not interchangeable.

---

## Paradigm 1: Objective Composite Indices

### The Kogut & Singh (1988) Cultural Distance Index

The most cited operationalization in IB research. Uses Hofstede's cultural dimensions to compute a scalar distance between a home country *h* and a host country *j*:

$$CD_j = \frac{1}{n} \sum_{i=1}^{n} \frac{(I_{ij} - I_{ih})^2}{V_i}$$

| Symbol | Meaning |
|--------|---------|
| $I_{ij}$ | Score of country $j$ on Hofstede dimension $i$ |
| $I_{ih}$ | Score of home country $h$ on dimension $i$ |
| $V_i$ | Sample variance of dimension $i$ across all countries (standardizes for scale differences) |
| $n$ | Number of dimensions used (typically 4) |

**Dimensions used** (Hofstede's original four):

| Code | Dimension | Typical $V_i$ |
|------|-----------|--------------|
| PDI | Power Distance Index | 1,525 |
| IDV | Individualism | 933 |
| MAS | Masculinity | 710 |
| UAI | Uncertainty Avoidance | 1,816 |

The variances above are derived from Hofstede's 76-country dataset and are widely reused in the literature (e.g., Shenkar 2001; Tihanyi et al. 2005). If you use Hofstede's 6-dimension dataset (adding LTO and IND), recompute $V_i$ from the larger country sample.

---

### Worked Example: Taiwan as Home Country

Hofstede scores (Hofstede Insights, retrieved 2024):

| Country | PDI | IDV | MAS | UAI |
|---------|-----|-----|-----|-----|
| Taiwan (home) | 58 | 17 | 45 | 69 |
| Vietnam | 70 | 20 | 40 | 30 |
| Japan | 54 | 46 | 95 | 92 |
| United States | 40 | 91 | 62 | 46 |
| Germany | 35 | 67 | 66 | 65 |

**Step-by-step: Taiwan → Vietnam**

```
PDI term: (70 - 58)² / 1525 = 144 / 1525  = 0.094
IDV term: (20 - 17)² / 933  =   9 / 933   = 0.010
MAS term: (40 - 45)² / 710  =  25 / 710   = 0.035
UAI term: (30 - 69)² / 1816 = 1521 / 1816 = 0.838
Sum = 0.977  →  CD = 0.977 / 4 = 0.244
```

**Step-by-step: Taiwan → Japan**

```
PDI term: (54 - 58)² / 1525 =   16 / 1525 = 0.010
IDV term: (46 - 17)² / 933  =  841 / 933  = 0.901
MAS term: (95 - 45)² / 710  = 2500 / 710  = 3.521
UAI term: (92 - 69)² / 1816 =  529 / 1816 = 0.291
Sum = 4.724  →  CD = 4.724 / 4 = 1.181
```

**Full ranking from Taiwan:**

| Rank | Country | CD Score | Uppsala Psychic Zone |
|------|---------|----------|---------------------|
| 1 (closest) | Vietnam | 0.244 | Near |
| 2 | Germany | 0.850 | Moderate |
| 3 | Japan | 1.181 | Moderate |
| 4 | United States | 1.695 | Far |

> **Interpretation note**: Japan scores "Far" from Taiwan on cultural distance despite geographic proximity and historical economic ties, driven almost entirely by Japan's extreme Masculinity score (95). This illustrates why Kogut & Singh CD must be supplemented with other psychic distance stimuli — the model captures Hofstede dimensions only.

---

### Python Snippet for Bulk Computation

```python
import math

VARIANCE = {"PDI": 1525, "IDV": 933, "MAS": 710, "UAI": 1816}

def kogut_singh(home: dict, host: dict) -> float:
    """
    home, host: dicts with keys PDI, IDV, MAS, UAI
    Returns Cultural Distance scalar.
    """
    dims = list(VARIANCE.keys())
    total = sum((host[d] - home[d]) ** 2 / VARIANCE[d] for d in dims)
    return total / len(dims)

# Taiwan as home country
taiwan = {"PDI": 58, "IDV": 17, "MAS": 45, "UAI": 69}
targets = {
    "Vietnam":       {"PDI": 70, "IDV": 20, "MAS": 40, "UAI": 30},
    "Japan":         {"PDI": 54, "IDV": 46, "MAS": 95, "UAI": 92},
    "United States": {"PDI": 40, "IDV": 91, "MAS": 62, "UAI": 46},
    "Germany":       {"PDI": 35, "IDV": 67, "MAS": 66, "UAI": 65},
}

for country, scores in sorted(targets.items(), key=lambda x: kogut_singh(taiwan, x[1])):
    print(f"{kogut_singh(taiwan, scores):.3f}  {country}")
```

---

## Paradigm 2: Dow & Karunaratna (2006) Psychic Distance Stimuli

Dow & Karunaratna argue that Kogut & Singh conflates *culture* with *psychic distance*. Their framework separates **psychic distance stimuli** — country-level objective factors that cause uncertainty — from the manager's subjective perception.

**Seven stimulus dimensions** (Dow & Karunaratna 2006, JIBS):

| # | Stimulus | Measurement Proxy |
|---|----------|------------------|
| 1 | Language | Linguistic distance (Dyen et al. 1992 family tree; binary for non-shared family) |
| 2 | Religion | % population in same dominant religion; weighted by religious intensity |
| 3 | Education | Years of schooling; literacy rate differential |
| 4 | Political systems | Polity IV democracy score; system similarity (presidential vs parliamentary) |
| 5 | Industrial development | GNI per capita, PPP-adjusted; HDI differential |
| 6 | Cultural distance (Hofstede) | Kogut & Singh CD (above) feeds in as one sub-component |
| 7 | Colonial ties | Binary: shared colonial history (reduces psychic distance) |

**Scoring procedure** (5-point scale adaptation for practitioners):

For each stimulus, rate the absolute difference between home and host country:

```
1 = Virtually identical
2 = Minor differences (same language family, similar systems)
3 = Noticeable differences (related language, partially different institutions)
4 = Substantial differences (different language family, different systems)
5 = Extreme differences (unrelated language, opposite systems)
```

Composite Psychic Distance Stimuli score:

$$PDS_j = \frac{1}{7} \sum_{k=1}^{7} w_k \cdot s_{kj}$$

Where $w_k$ are dimension weights. Dow & Karunaratna find empirically that **language** and **culture** carry the highest predictive weight for actual entry mode choices. A conservative equal-weighting ($w_k = 1$) is acceptable for practitioner use.

---

### Worked Example: Taiwan → Southeast Asia Markets

| Stimulus | Vietnam | Thailand | Indonesia | Philippines |
|----------|---------|----------|-----------|-------------|
| Language (1–5) | 3 | 4 | 4 | 2 |
| Religion (1–5) | 3 | 4 | 5 | 2 |
| Education (1–5) | 2 | 2 | 3 | 2 |
| Political system (1–5) | 4 | 3 | 3 | 3 |
| Industrial development (1–5) | 2 | 2 | 3 | 2 |
| Cultural distance (K&S→5) | 1 | 2 | 2 | 2 |
| Colonial ties (1–5) | 2 | 2 | 2 | 3 |
| **PDS (equal weight)** | **2.43** | **2.71** | **3.14** | **2.29** |
| **Uppsala Zone** | Near | Moderate | Far | Near |

> Philippines ranks closest despite different language, because of shared colonial ties (Spanish/American legal institutions) and Christian majority — a counterintuitive result that pure cultural distance misses.

---

## Paradigm 3: Perceptual Survey Instruments

When research access allows surveying managers directly, perceptual measures capture the subjective uncertainty that actually drives commitment decisions in the Uppsala model.

**Standard items** (adapted from Sousa & Bradley 2006; 7-point Likert):

```
1. I am familiar with business practices in {target market}.
2. The customers in {target market} behave similarly to customers at home.
3. I find it easy to understand the way business is done in {target market}.
4. I feel comfortable operating in {target market}.
5. The competitive environment in {target market} is predictable to me.
```

Reverse-score items to produce a **Psychic Distance Perception (PDP)** score where higher = more distant.

**When to use perceptual vs composite:**

| Situation | Recommended Measure |
|-----------|-------------------|
| Cross-country academic comparison | Kogut & Singh CD |
| Practitioner entry sequencing | Dow & Karunaratna PDS |
| Evaluating individual manager readiness | Perceptual survey (Sousa & Bradley) |
| Auditing why a past entry succeeded/failed | Both composite + retrospective perceptual |

---

## Composite Ranking Decision Framework

For a firm planning market entry sequence, combine both paradigms:

**Step 1**: Compute Kogut & Singh CD for all candidate markets.

**Step 2**: Score Dow & Karunaratna PDS (7 dimensions, 5-point scale) for the same markets.

**Step 3**: Normalize both scores to 0–1 range:

$$\text{normalized} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

**Step 4**: Compute weighted composite (default: 50/50; adjust based on industry):

$$\text{Psychic Distance Score} = 0.5 \cdot CD_{\text{norm}} + 0.5 \cdot PDS_{\text{norm}}$$

For **B2B manufacturing**: weight PDS higher (0.6) — institutional and industrial factors matter more than raw cultural distance.  
For **consumer retail**: weight CD higher (0.6) — cultural values drive consumer behavior.

**Step 5**: Assign Uppsala zones by tertile:
- Bottom tertile → Near (enter first)
- Middle tertile → Moderate (second wave)
- Top tertile → Far (third wave or via acquisition)

---

## Known Limitations

**Symmetry assumption**: Kogut & Singh treats distance as symmetric ($CD_{AB} = CD_{BA}$). Psychic distance is directional — a Taiwanese firm entering Germany experiences different uncertainty than a German firm entering Taiwan. Shenkar (2001) calls this the "illusion of symmetry." For practitioner use, always compute from the firm's home country outward.

**Static snapshots**: Hofstede scores are collected at one point in time. Vietnam's rapid economic development since 1990 may make current scores less reliable. Cross-validate with GLOBE project scores (House et al. 2004) or World Values Survey data when entering markets undergoing rapid institutional change.

**Psychic distance paradox** (O'Grady & Lane 1996): Firms systematically underperform in psychically close markets. Perceived similarity causes managers to under-invest in market research, skip adaptation, and apply home-country assumptions. A low psychic distance score is a risk flag, not just an opportunity signal. Factor this into the Uppsala establishment chain — even "Near" markets require explicit learning mechanisms.

**GLOBE as alternative**: The GLOBE project (62 societies, 9 dimensions) offers "as-is" (current practices) and "should-be" (values) scores. For Uppsala purposes, **as-is practices scores** better predict actual business interaction friction than values scores. GLOBE dimensions map loosely to Hofstede but are not identical; do not mix them in the same Kogut & Singh calculation.

---

## Quick Reference: Data Sources

| Data Need | Source |
|-----------|--------|
| Hofstede dimension scores | hofstede-insights.com/country-comparison |
| GLOBE practices scores | House et al. (2004), *Culture, Leadership, and Organizations* |
| Linguistic distance | ASJP database; Dyen et al. (1992) Indo-European; Ethnologue for non-IE |
| Polity IV democracy scores | systemicpeace.org/polity |
| GNI per capita, PPP | World Bank Open Data (data.worldbank.org) |
| Colonial history | CEPII gravity dataset (colonial history variable) |

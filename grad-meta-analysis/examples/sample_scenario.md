# Example: Spaced Repetition vs. Massed Practice for L2 Vocabulary Retention

## Scenario

**Who**: Dr. Sarah Chen, Lead Research Scientist at Meridian Learning (a B2C language-learning app with 8M users)

**Question**: "We're debating whether to redesign our Spanish vocabulary module around spaced repetition (SR). I've pulled 15 studies comparing SR to massed practice on retention of L2 vocabulary. What does the overall evidence say, and should I trust it?"

**Context**: Meridian's product team wants a defensible number for their white paper claim. Studies vary widely — different languages, learner ages, retention intervals (1 week to 6 months), and effect sizes ranging from d = 0.21 to d = 1.14.

---

## Analysis

### Step 1 — Extract and Code Effect Sizes

Dr. Chen converts all reported statistics to **Hedges' g** (preferred over Cohen's d for small samples; corrects for upward bias). Conversion formulas used:

- For studies reporting t-statistics: g = t × √(1/n₁ + 1/n₂) × J(df)
- For studies reporting means/SD: g = (M₁ − M₂) / SD_pooled × J(df)
- Correction factor J(df) = 1 − 3/(4df − 1)

Coded moderators:

| Study | k (N) | g | SE(g) | Retention interval | Learner age | Language |
|-------|--------|------|-------|-------------------|-------------|----------|
| Bahrick & Phelps (1987) | 86 | 0.91 | 0.23 | 8 years | Adult | English |
| Cepeda et al. (2008) | 117 | 0.74 | 0.19 | 1 month | Adult | English |
| Kornell (2009) | 60 | 0.44 | 0.26 | 1 week | Undergrad | English |
| Karpicke & Roediger (2008) | 60 | 0.38 | 0.27 | 1 week | Undergrad | English |
| Nakata (2011) | 89 | 0.63 | 0.21 | 2 weeks | EFL adult | Japanese→English |
| ... (10 more studies) | | | | | | |
| **Total** | **k = 15, N = 1,247** | | | | | |

**Flagged issue during coding**: Two studies (Rohrer & Taylor 2006; Bird 2010) reported "percent words recalled" without variance. Dr. Chen emails authors — Rohrer & Taylor provide raw data; Bird 2010 excluded due to non-response, dropping k to **14 studies, N = 1,189**.

---

### Step 2 — Choose Model

Studies span adult learners, university undergraduates, and EFL/EFl contexts across 4 languages with retention intervals from 1 week to 8 years. **Random-effects model is clearly appropriate** — there is no single true effect size; the population of effects varies by context.

> Fixed-effect would assume that Bahrick's 8-year retention study and Kornell's 1-week study estimate the same underlying truth. They do not.

---

### Step 3 — Assess Heterogeneity

Using inverse-variance weighting under random-effects (DerSimonian–Laird estimator for τ²):

- **Q = 94.7**, df = 13, **p < 0.001** → reject homogeneity
- **I² = 86.3%** → substantial heterogeneity; most variance is between-study, not sampling error
- **τ² = 0.071** (between-study SD τ = 0.266 g units)

I² at 86% triggers moderator analysis:

| Moderator | β | 95% CI | p | R² analog |
|-----------|---|--------|---|-----------|
| Retention interval (log weeks) | +0.11 | [0.04, 0.18] | 0.003 | 38% |
| Learner age (adult vs. student) | −0.09 | [−0.24, 0.06] | 0.24 | ns |
| Language family (same vs. diff) | +0.06 | [−0.12, 0.24] | 0.51 | ns |

**Key finding**: Longer retention intervals amplify the SR advantage — SR's benefit compounds over time, exactly as spacing theory predicts.

---

### Step 4 — Publication Bias

Funnel plot shows **asymmetry on the left** (missing small-sample null or negative results).

- **Egger's regression intercept** = 1.89 (SE = 0.74), t = 2.56, **p = 0.024** → significant asymmetry
- **Trim-and-fill**: imputes **3 missing studies** on the left; adjusted estimate drops from g = 0.54 to **g = 0.44**

This is a meaningful correction (~19% reduction). The white paper should report the trim-and-fill estimate, not the naive pooled estimate.

---

## Result

```markdown
## Meta-Analysis: Effect of Spaced Repetition vs. Massed Practice on L2 Vocabulary Retention

### Study Inclusion
| Criterion | Value |
|-----------|-------|
| Studies included (k) | 14 |
| Total sample size (N) | 1,189 |
| Effect size metric | Hedges' g |

### Pooled Effect Size
| Model | Effect | 95% CI | z | p-value |
|-------|--------|--------|---|---------|
| Fixed-effect | 0.68 | [0.61, 0.75] | 19.43 | < 0.001 |
| Random-effects | 0.54 | [0.39, 0.69] | 7.07 | < 0.001 |
| Trim-and-fill (adjusted) | **0.44** | [0.28, 0.60] | 5.39 | < 0.001 |

**Report trim-and-fill estimate** given significant publication bias.

Prediction interval (random-effects): [−0.08, 1.16]
→ In some contexts, SR may offer no advantage or mild disadvantage (e.g., very short retention intervals).

### Heterogeneity
| Statistic | Value | Interpretation |
|-----------|-------|----------------|
| Q | 94.7 (p < 0.001) | Significant — studies are not estimating one true effect |
| I² | 86.3% | High — substantial between-study variance |
| τ² | 0.071 | Between-study SD ≈ 0.27 g units |

### Publication Bias
| Test | Result | Interpretation |
|------|--------|----------------|
| Funnel plot | Asymmetric (left gap) | Bias suspected |
| Egger's test | p = 0.024 | Significant asymmetry |
| Trim-and-fill | Adjusted g = 0.44 (3 studies imputed) | Moderate downward correction |

### Limitations
- High I² (86%) means the pooled estimate is an average of a wide distribution, not a reliable point prediction for any specific context
- Moderator analysis (k = 14) is underpowered; retention interval finding is suggestive, not confirmatory
- One study excluded due to missing variance data; if Bird (2010) is a large null result, bias is understated
- All included studies use immediate or delayed vocabulary tests; no study measures in-context usage or transfer
```

---

**Recommendation to product team**: The adjusted pooled effect of **g = 0.44** is a moderate, statistically robust advantage for SR. However, the prediction interval includes zero — **Meridian should not claim SR always wins**. A more defensible white paper claim:

> "Across 14 controlled studies (N = 1,189), spaced repetition produced a moderate advantage over massed practice for vocabulary retention (g = 0.44, 95% CI [0.28, 0.60]), with larger benefits observed at longer retention intervals (≥ 4 weeks)."

Do **not** cite the unadjusted random-effects estimate (g = 0.54) in marketing materials — Egger's test flags meaningful publication bias.

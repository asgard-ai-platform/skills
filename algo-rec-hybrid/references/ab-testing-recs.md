# A/B Testing Recommendation Systems

## Why Rec System A/B Tests Fail More Often Than Other Feature Tests

Standard A/B testing assumes the treatment affects users independently. Recommendation systems violate this in two ways:

1. **Popularity feedback loops**: Items recommended to group A accumulate clicks, which boosts their CF scores globally, contaminating group B's personalization signals.
2. **Novelty effects**: Users in the new hybrid group click differently in week 1 simply because recommendations changed — not because quality improved. This inflates early metrics and collapses by week 3.

Plan for both before you start.

---

## Metric Selection

Pick **one primary metric** before the experiment. Post-hoc metric shopping inflates false positive rate.

| Metric | Formula | When to use as primary |
|--------|---------|----------------------|
| Precision@K | (relevant items in top-K) / K | When users scan the list top-down |
| NDCG@K | Σ (rel_i / log₂(i+1)) / IDCG | When position matters (ranked lists) |
| Recall@K | (relevant items in top-K) / (all relevant items) | When missing relevant items is costly |
| Hit Rate@K | I(any relevant item in top-K) | When one good rec per session is enough |
| Coverage | (unique items recommended) / (catalog size) | When catalog utilization matters |
| ILD (Intra-list diversity) | 1 - avg pairwise similarity within list | When serendipity or filter-bubble risk matters |

For hybrid rec systems specifically, **always report coverage and ILD as secondary metrics** even if NDCG is primary. A hybrid that gains +2% NDCG but drops coverage by 15% has found a local optimum — it recommends the same popular items more precisely rather than generalizing.

### Minimum Reporting Set

```
Primary:   NDCG@10
Secondary: Precision@10, Recall@10, Coverage, ILD
Business:  CTR, add-to-cart rate, session depth (if available)
```

---

## Sample Size Calculation

### Formula

For a two-sided t-test on proportions (precision, CTR):

```
n = (z_α/2 + z_β)² × (p1(1-p1) + p2(1-p2)) / (p1 - p2)²
```

Where:
- `z_α/2 = 1.96` for α = 0.05
- `z_β = 0.84` for power = 80%
- `p1` = baseline metric (measure from logs before experiment)
- `p2` = p1 × (1 + MDE) where MDE is minimum detectable effect

### Worked Example

**Scenario**: Current precision@10 = 0.12. You want to detect a 10% relative improvement (MDE = 10%, so p2 = 0.132).

```
n = (1.96 + 0.84)² × (0.12×0.88 + 0.132×0.868) / (0.132 - 0.12)²
  = 7.84 × (0.1056 + 0.1146) / 0.000144
  = 7.84 × 0.2202 / 0.000144
  = 11,976 users per arm
```

Round up: **12,000 users per arm**, 24,000 total.

**For NDCG** (continuous metric), use the t-test variant:

```
n = 2 × (z_α/2 + z_β)² × σ² / δ²
```

Where `σ` is the standard deviation of NDCG scores per user (compute from historical data), and `δ` is the absolute effect you want to detect.

### Quick Reference Table

Assuming baseline precision@10 = 0.12, α = 0.05, power = 80%:

| MDE (relative) | Users per arm |
|---------------|--------------|
| 5% | ~48,000 |
| 10% | ~12,000 |
| 15% | ~5,400 |
| 20% | ~3,000 |

If your traffic is low, **do not lower the MDE to make the sample size fit** — that means you'll only detect large effects and may ship changes that hurt users by small but real amounts.

---

## Experiment Design for Hybrid Systems

### What to Compare

A hybrid system introduces multiple variables. Never compare the final hybrid against a stale production baseline without first establishing a clean control:

```
Arm A (control):  Single best individual method (e.g., CF-only)
Arm B (treatment): Hybrid (CF + content-based)
```

If you are already running a hybrid in production and want to tune weights:

```
Arm A (control):  Current weights (α=0.5, β=0.5)
Arm B (treatment): New weights (α=0.6, β=0.4)
```

Never compare three or more architectures in a single experiment without correcting for multiple comparisons (use Bonferroni: α_corrected = α / k, where k = number of pairwise comparisons).

### Switching Hybrid: What to Test

A switching hybrid has an extra design choice: the threshold at which it switches from content-based to CF. Test the switch threshold separately from the component quality:

1. **Phase 1**: Fix threshold, verify content-based arm outperforms popularity baseline for cold-start users.
2. **Phase 2**: Fix threshold, verify CF arm outperforms popularity baseline for warm users.
3. **Phase 3**: A/B test the switching logic itself — does it correctly classify cold vs. warm users? Metric: precision@10 on the transition cohort (users with 3–10 interactions).

### Cascade Hybrid: Avoid Confounding

In a cascade hybrid (content-based filters → CF ranks), a change to stage 1 changes the input distribution for stage 2. You cannot independently test the two stages. Always test the full cascade as a unit.

---

## User Segmentation Strategy

### Split by User Cohort, Not by Request

Assign each user to a single arm for the full experiment duration. Do not split by request (session-level) — this violates the independence assumption because the same user's behavior affects their own future CF scores.

### Stratified Randomization

Stratify assignment on user type to ensure balance:

| Stratum | Definition | Why it matters |
|---------|------------|---------------|
| New users (0 interactions) | Cold-start cohort | Hybrid's content-based arm should help most here |
| Warm users (1–10 interactions) | Transition cohort | Switching threshold sensitivity |
| Active users (10+ interactions) | CF-dominant cohort | CF quality, not cold-start |

Ensure each stratum's distribution is similar across arms before the experiment goes live. Check with χ² test on stratum proportions.

### Reporting by Stratum

Always report primary metric **by stratum**, not only overall. A hybrid that hurts active users but helps new users might have a positive aggregate NDCG but is hiding a regression in your most valuable cohort.

```
Overall NDCG@10:        +2.1% (p=0.03)  ← headline looks good
  Cold-start users:     +8.4% (p=0.001) ← expected win from content-based
  Warm users:           +0.5% (p=0.42)  ← not significant
  Active users:         -1.2% (p=0.08)  ← marginal regression, watch this
```

In this example, the hybrid wins on cold-start (as designed) but shows a trend toward regression for active users. Ship the hybrid with a plan to monitor active user metrics post-launch.

---

## Runtime Duration

### Minimum and Maximum

**Minimum**: Run for at least **2 full business cycles** (typically 2 weeks) to capture weekly behavioral variation (weekend vs. weekday usage patterns differ).

**Maximum**: Stop at **4 weeks** for most experiments. Beyond that:
- Novelty effects have fully decayed (good)
- But seasonal drift may start confounding results (bad)
- And popularity feedback loops have more time to cross-contaminate arms

### Novelty Effect Check

Plot the primary metric over time. Novelty effect signature: treatment arm shows a spike in week 1, then decays toward control level.

```
Week 1:  Treatment +5.2%, control +0.0%  ← possible novelty effect
Week 2:  Treatment +3.1%, control +0.0%  ← decaying
Week 3:  Treatment +2.0%, control +0.0%  ← stabilizing
Week 4:  Treatment +1.9%, control +0.0%  ← likely real effect
```

Do not call the experiment based on week-1 data if you see this pattern. The stable effect (+1.9%) is smaller than the initial reading (+5.2%), and shipping based on week-1 would overstate the benefit.

---

## Statistical Analysis

### Primary Test

Two-sample t-test on per-user metric values (not on aggregated means). Each user's NDCG@10 is one observation.

```python
from scipy import stats

# ndcg_control, ndcg_treatment: arrays of per-user NDCG scores
t_stat, p_value = stats.ttest_ind(ndcg_control, ndcg_treatment, equal_var=False)
# Use Welch's t-test (equal_var=False) — never assume equal variance
```

### Effect Size

Report Cohen's d alongside p-value:

```
d = (mean_treatment - mean_control) / pooled_std
```

| d | Interpretation |
|---|---------------|
| 0.2 | Small |
| 0.5 | Medium |
| 0.8 | Large |

A statistically significant result with d < 0.1 is probably not worth shipping — the confidence interval is narrow enough to exclude zero, but the effect is trivially small.

### Multiple Metrics Correction

If you report 5 secondary metrics, the probability of at least one false positive at α=0.05 is 1 - 0.95⁵ = 23%. Use Benjamini-Hochberg (BH) correction for secondary metrics (not Bonferroni — BH is less conservative and appropriate when metrics are correlated):

```python
from statsmodels.stats.multitest import multipletests

p_values = [p_ndcg, p_precision, p_recall, p_coverage, p_ild]
reject, p_corrected, _, _ = multipletests(p_values, alpha=0.05, method='fdr_bh')
```

The primary metric does not need BH correction since it was pre-specified.

---

## Ship / No-Ship Decision Framework

```
Primary metric significant (p < 0.05) AND Cohen's d ≥ 0.1?
├── YES → check secondary metrics
│   ├── Coverage dropped > 5%?          → Flag, investigate before shipping
│   ├── Active user regression (p<0.10)? → Flag, add monitoring guardrail
│   └── Both OK                         → SHIP
└── NO  → Do not ship
         ├── Underpowered? (ran < 2 weeks or sample < target)
         │   → Extend experiment
         └── Truly null? (ran full duration, met sample size)
             → Abandon or redesign hybrid architecture
```

**Never ship a result that is only borderline significant (0.05 < p < 0.10)** by arguing that "the direction is right." This is the most common source of false positives in recommendation system experiments.

---

## Holdout Groups for Long-Term Effect Measurement

For a production hybrid system, maintain a **permanent holdout group** (typically 5% of users) that always receives the previous-generation model. This allows:

- Long-term metric tracking without re-running experiments
- Detection of compounding effects (e.g., feedback loops that take months to manifest)
- Calibration of novelty effects for future experiments

The holdout group sacrifices 5% of potential improvement permanently but provides a baseline that cross-sectional A/B tests cannot give you.

---

## Common Failure Modes Specific to Hybrid Systems

**1. Testing the wrong arm**

You want to test the hybrid's switching logic but accidentally split on session, not user. Result: the same user sometimes gets CF, sometimes content-based, which means neither arm represents the intended experience.

**2. Leaking CF signals across arms**

Global item popularity counts are updated using all users. If the treatment arm gets recommended item X more, item X's global popularity score rises, which then feeds back into the control arm's CF. Mitigation: shard popularity counters by experiment arm, or accept a small contamination bias and document it.

**3. Comparing against a stale single-method baseline**

The control arm's CF model may not have been retrained recently. You end up comparing a fresh hybrid against a stale single-method model. Always retrain both arms' models with identical data cutoffs before the experiment.

**4. Ignoring latency as a metric**

A hybrid system is slower than a single-method system. If the latency regression is large enough, it can hurt CTR independently of recommendation quality. Measure p99 latency for both arms and report it alongside recommendation metrics.

**5. Calling the experiment early on a positive trend**

Running optional stopping ("we'll stop as soon as p < 0.05") inflates false positive rate dramatically. If you must make sequential decisions, use a sequential testing framework (e.g., SPRT, always-valid confidence intervals) and decide on the methodology before the experiment starts.

# Reject Inference

## The Core Problem

A credit model trained only on approved applicants has a biased view of the population. Approvals are not random — they were filtered by a prior score, human judgment, or policy. If the rejected applicants had been approved, some would have defaulted and some would have paid. Ignoring them means:

- Default rate is underestimated in the lower score bands (the high-risk population is missing)
- Model coefficients are biased toward the approved subpopulation
- Score cutoffs derived from the model will be miscalibrated

**Formal statement:** Let `A = 1` denote approved, `A = 0` denied. Training observes `(X, Y)` only when `A = 1`. If `P(A=1 | X)` is correlated with `X`, the selection is non-ignorable and estimates of `P(Y=1 | X)` are biased.

### Quantifying the Magnitude

Suppose the approval rate is 70% and the population bad rate is 5%:

| Segment | N | Observed Bads |
|---------|---|---------------|
| Approved (A=1) | 700 | 28 (4% bad rate) |
| Rejected (A=0) | 300 | unknown |
| Total population | 1000 | ~50 (5% bad rate) |

The 22 missing bads (50 − 28) are concentrated in the rejected population. If the model is trained only on the 700 approved cases, it sees a 4% bad rate and will systematically underprice risk for borderline borrowers.

---

## Method 1: Parceling (Simple Augmentation)

**When to use:** Quick baseline; approval rate > 60%; prior score exists.

**Procedure:**

1. Score all rejected applicants with the existing model (or rule-based score used at origination).
2. Sort rejects into K score bands (typically K=10 deciles).
3. For each band, assign an assumed bad rate by extrapolating from the observed bad rates of approved applicants in adjacent lower-score bands.
4. Randomly label each reject as `bad=1` with probability equal to the assumed bad rate, `bad=0` otherwise. This is the **parcel assignment**.
5. Append parceled rejects to the training dataset.
6. Retrain the model on the combined dataset.

**Worked Example:**

The approved population shows these band-level bad rates:

| Score Band | Approved Bad Rate |
|------------|-----------------|
| 700-750     | 1.5%            |
| 650-700     | 3.0%            |
| 600-650     | 6.0%            |
| 550-600     | 10.0%           |
| < 550       | 18.0%           |

Most rejects were scored below 600. Extrapolate:

| Score Band | Assumed Reject Bad Rate | Rationale |
|------------|------------------------|-----------|
| 500-550     | 25%                    | Extrapolate trend from 550-600 band |
| < 500       | 35%                    | Conservative floor |

For 300 rejects, 120 score 500-550 and 180 score below 500:
- 120 × 25% = 30 parceled bads
- 180 × 35% = 63 parceled bads

Add these 93 parceled records to training set. Combined dataset now better approximates the through-the-door population.

**Limitation:** Parcel assignment is deterministic extrapolation — the assumed bad rates are guesses. Sensitive to extrapolation assumptions.

---

## Method 2: Fuzzy Augmentation

**When to use:** You want to propagate uncertainty in the bad-rate assumption rather than committing to a point estimate.

Instead of assigning each reject a hard label (0 or 1), assign a **fractional weight**:

```
weight_bad(i)  = p_i       (probability applicant i is bad)
weight_good(i) = 1 - p_i
```

Each rejected applicant contributes two weighted rows to the training set — one labeled bad with weight `p_i`, one labeled good with weight `1 − p_i`.

For logistic regression, this is equivalent to minimizing a weighted log-likelihood:

```
L = Σ_{approved} [y_i log(p̂_i) + (1-y_i) log(1-p̂_i)]
  + Σ_{rejected} [p_i log(p̂_i) + (1-p_i) log(1-p̂_i)]
```

Where `p_i` = assumed PD for reject `i` from Step 3 of parceling.

**Advantage over parceling:** No random noise from stochastic label assignment; the model sees the full uncertainty signal. Particularly useful when sample size is small and variance from random parceling is high.

---

## Method 3: Iterative Reclassification (IR / EM-style)

**When to use:** No prior score exists; or prior score is unreliable; or you want a more principled approach.

This is an Expectation-Maximization (EM) approach:

**Step 0:** Train an initial model `M_0` on approved applicants only.

**Step 1 (E-step):** Score all rejected applicants with `M_0`. Each reject gets PD estimate `p_i^{(t)}`.

**Step 2 (M-step):** Use `p_i^{(t)}` as fuzzy labels. Retrain model `M_{t+1}` on approved (hard labels) + rejected (soft labels `p_i^{(t)}`).

**Step 3:** Repeat E→M until convergence: `max |p_i^{(t+1)} - p_i^{(t)}| < ε` (e.g., ε = 0.001).

**Convergence in practice:** Usually 3-7 iterations. After iteration 1-2, the model stabilizes unless the rejected population is very large or very different from approvals.

```python
import numpy as np
from sklearn.linear_model import LogisticRegression

def iterative_reclassification(X_approved, y_approved, X_rejected,
                                max_iter=10, tol=1e-3):
    """
    Returns final model and converged PD estimates for rejected applicants.
    """
    # Step 0: train on approvals only
    model = LogisticRegression(max_iter=1000)
    model.fit(X_approved, y_approved)

    p_prev = np.zeros(len(X_rejected))

    for iteration in range(max_iter):
        # E-step: score rejects
        p_reject = model.predict_proba(X_rejected)[:, 1]

        # M-step: build soft-labeled dataset
        # Approved: weight=1, hard labels
        # Rejected: two rows per applicant with fractional weights
        X_combined = np.vstack([X_approved, X_rejected, X_rejected])
        y_combined = np.concatenate([
            y_approved,
            np.ones(len(X_rejected)),   # bad row
            np.zeros(len(X_rejected))   # good row
        ])
        w_combined = np.concatenate([
            np.ones(len(y_approved)),
            p_reject,                   # weight for bad row
            1 - p_reject                # weight for good row
        ])

        model = LogisticRegression(max_iter=1000)
        model.fit(X_combined, y_combined, sample_weight=w_combined)

        # Check convergence
        delta = np.max(np.abs(p_reject - p_prev))
        p_prev = p_reject
        if delta < tol:
            print(f"Converged at iteration {iteration + 1}, delta={delta:.5f}")
            break

    return model, p_reject
```

**Warning:** IR can amplify initial model errors. If `M_0` is severely biased (e.g., trained on a 20% approval rate), early iterations will assign bad labels mostly to rejects with features similar to approved bads — which may be wrong. Always validate IR results against an external holdout or out-of-time sample if available.

---

## Method 4: Direct Extrapolation with Augmented Outcome

**When to use:** You have a follow-up sample — e.g., a random-approval experiment, or a product with lower approval threshold that accidentally captured some near-marginal rejects.

If you can observe outcomes for a **supplementary sample** `S` that overlaps with the reject region:

1. Fit outcome model on `S` alone: `P(Y=1 | X, sample=S)`
2. Use it to impute outcomes for main-dataset rejects
3. Combine imputed rejects with approved applicants and retrain

This is the most statistically valid approach but requires an actual supplementary dataset — rare in practice.

---

## Method Comparison

| Method | Prior Score Required | Handles No-History | Stochastic | Complexity |
|--------|---------------------|-------------------|-----------|-----------|
| Parceling | Yes | No | Yes (label noise) | Low |
| Fuzzy Augmentation | Yes | No | No | Low-Medium |
| Iterative Reclassification | No | Yes | No | Medium |
| Direct Extrapolation | No | Yes | No | High (data-hungry) |

**Practical default:** Use Fuzzy Augmentation if a prior score exists. Use Iterative Reclassification if building a model from scratch with no prior score. Parceling is acceptable for a quick baseline but should not be the final production approach.

---

## How Much Does Reject Inference Matter?

The impact scales with three factors:

1. **Rejection rate**: Impact is negligible at < 10% rejection; significant at > 40% rejection.
2. **Selectivity**: If rejection is nearly random (e.g., rejected due to capacity constraints), bias is low. If rejection is tightly score-gated, bias is high.
3. **Model use region**: If you only use the model for applicants far above the old cutoff, reject inference in the low-score region matters less.

**Rule of thumb:** If approval rate < 60% and the model will be deployed to applicants who would have been rejected under the old policy, reject inference is mandatory.

---

## Validation After Reject Inference

Reject inference adds assumed labels — you cannot validate on the rejects directly (you still don't know their true outcomes). Validation options:

### 1. Out-of-Time Holdout on Approvals
Compare AUC and KS on a holdout drawn from a later vintage, before and after reject inference. Expect modest improvement in the low-score bands.

### 2. Population Stability Check
Score the full through-the-door population (approved + rejected) with the pre- and post-RI models. PSI between the two score distributions should decrease — the RI model should produce a more uniform distribution across the full population.

### 3. Retrospective Random-Approval Test
If feasible, approve a random sample of 500-1000 previously-rejected applicants. After 12 months, compare the model's predicted PD for those applicants to their actual default rate. This is the gold standard.

### 4. Calibration by Score Band

After RI, recalibrate the model and verify:

```
For each decile d:
  |mean(predicted_PD, d) - actual_default_rate(approved, d)| < 0.5 × actual_default_rate
```

Note: You cannot verify calibration in the reject region — only the approved region is observable. Document this limitation explicitly for model validators.

---

## Regulatory Note

Basel II/III and SR 11-7 (Model Risk Management) require documentation of selection bias treatment in retail credit models. When filing model documentation:

- State which reject inference method was used and why
- Quantify the rejection rate at training time
- Describe any validation performed and its limitations
- Acknowledge that reject inference does not eliminate selection bias — it reduces it under assumptions
- Note that the assumptions (extrapolated bad rates, convergence of IR) are untestable and should be stress-tested

Examiners will ask: "What assumptions did you make about rejected applicants?" A model that ignores reject inference entirely is a finding. A model that uses it with documented assumptions is defensible.

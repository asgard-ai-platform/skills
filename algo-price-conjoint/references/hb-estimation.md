# Hierarchical Bayes Estimation for Conjoint Analysis

## Model Structure

HB treats part-worth utilities as a two-level model:

**Level 1 — Individual utilities:**
$$y_{ij} \sim \text{Multinomial Logit}(\beta_i)$$

Where $\beta_i$ is the vector of part-worth utilities for respondent $i$, and $y_{ij}$ is the choice made in task $j$.

**Level 2 — Population distribution:**
$$\beta_i \sim \mathcal{N}(\bar{\beta}, \Sigma)$$

$\bar{\beta}$ is the population mean vector; $\Sigma$ is the covariance matrix capturing heterogeneity across respondents.

**Why this matters over aggregate MNL:** Aggregate MNL estimates one $\beta$ for everyone, masking segments. HB estimates individual $\beta_i$ for each respondent while borrowing strength from the population — respondents with few observations get pulled toward $\bar{\beta}$.

---

## Priors

Specify weakly informative priors on the population parameters:

$$\bar{\beta} \sim \mathcal{N}(\mathbf{0}, s^2 \mathbf{I})$$
$$\Sigma \sim \text{Inverse-Wishart}(\nu, \mathbf{V})$$

**Defaults that work in practice:**

| Parameter | Default | Rationale |
|-----------|---------|-----------|
| $s^2$ | 4.0 | Allows utilities up to ±4 without strong penalty |
| $\nu$ | $K + 3$ (where $K$ = number of $\beta$ coefficients) | Weakly informative IW |
| $\mathbf{V}$ | $\nu \cdot \mathbf{I}$ | Implies $E[\Sigma] = \mathbf{I}$ |

Do not set $s^2$ too small (shrinks everything to zero) or too large (poor mixing).

---

## MCMC Sampling Procedure

HB is estimated via **Gibbs sampling** with a **Metropolis-Hastings** step for individual utilities.

### Full Conditionals

**Step 1 — Sample $\bar{\beta}$** (Gaussian, closed form):

$$\bar{\beta} \mid \beta_1, \ldots, \beta_N, \Sigma \sim \mathcal{N}\left(\mu_*, \Sigma_*\right)$$

$$\Sigma_* = \left(N \Sigma^{-1} + \frac{1}{s^2}\mathbf{I}\right)^{-1}$$

$$\mu_* = \Sigma_* \left(\Sigma^{-1} \sum_{i=1}^N \beta_i\right)$$

**Step 2 — Sample $\Sigma$** (Inverse-Wishart, closed form):

$$\Sigma \mid \bar{\beta}, \beta_1, \ldots, \beta_N \sim \text{IW}\left(\nu + N,\ \mathbf{V} + \sum_{i=1}^N (\beta_i - \bar{\beta})(\beta_i - \bar{\beta})^\top\right)$$

**Step 3 — Sample each $\beta_i$** (MH step, not closed form because the likelihood is logit):

For respondent $i$:
1. Propose $\beta_i^* = \beta_i^{(t)} + \epsilon$, where $\epsilon \sim \mathcal{N}(\mathbf{0}, \delta^2 \mathbf{I})$
2. Compute acceptance ratio:

$$\alpha = \min\left(1,\ \frac{L(y_i \mid \beta_i^*) \cdot p(\beta_i^* \mid \bar{\beta}, \Sigma)}{L(y_i \mid \beta_i^{(t)}) \cdot p(\beta_i^{(t)} \mid \bar{\beta}, \Sigma)}\right)$$

3. Accept $\beta_i^* $ with probability $\alpha$; otherwise keep $\beta_i^{(t)}$

Where $L(y_i \mid \beta_i)$ is the multinomial logit likelihood over all tasks for respondent $i$:

$$L(y_i \mid \beta_i) = \prod_{j=1}^{T_i} \frac{\exp(\mathbf{x}_{ij,c}^\top \beta_i)}{\sum_{k=1}^{K_j} \exp(\mathbf{x}_{ijk}^\top \beta_i)}$$

$\mathbf{x}_{ij,c}$ is the attribute vector of the chosen alternative $c$ in task $j$.

### Step Size Tuning

Target acceptance rate for individual MH steps: **25–45%**.

```python
# Adaptive step size during burn-in
if accept_rate < 0.25:
    delta *= 0.9   # shrink step
elif accept_rate > 0.45:
    delta *= 1.1   # grow step
```

Tune only during burn-in; fix $\delta$ during production draws.

---

## Worked Example: Laptop Conjoint

**Setup** (from SKILL.md):
- Attributes: Brand (Apple/Dell/Lenovo), RAM (8/16/32GB), Price ($800/$1200/$1600)
- Effect coding: reference level = last category per attribute
  - Brand: Apple=+1,0; Dell=0,+1; Lenovo=-1,-1
  - RAM: 8GB=+1,0; 16GB=0,+1; 32GB=-1,-1
  - Price: $800=+1,0; $1200=0,+1; $1600=-1,-1
- $K = 6$ parameters per respondent

**Design matrix row** (Apple, 16GB, $1200):

$$\mathbf{x} = [1, 0,\ 0, 1,\ 0, 1]$$

**Respondent 42 — posterior draws (after burn-in):**

| Parameter | Mean | SD | 2.5% | 97.5% |
|-----------|------|----|------|-------|
| Apple | 1.82 | 0.31 | 1.22 | 2.41 |
| Dell | 0.14 | 0.28 | -0.41 | 0.68 |
| Lenovo (ref) | -1.96 | — | — | — |
| 8GB | -0.95 | 0.22 | -1.37 | -0.52 |
| 16GB | 0.43 | 0.20 | 0.04 | 0.82 |
| 32GB (ref) | 0.52 | — | — | — |
| $800 | 1.74 | 0.29 | 1.17 | 2.30 |
| $1200 | 0.21 | 0.24 | -0.26 | 0.68 |
| $1600 (ref) | -1.95 | — | — | — |

*Reference level utility = negative sum of other levels (effect coding constraint).*

**Derive WTP for Apple brand premium** (vs. Lenovo):

$$\Delta U_{\text{brand}} = U_{\text{Apple}} - U_{\text{Lenovo}} = 1.82 - (-1.96) = 3.78$$

Price coefficient (utility per dollar): $\frac{U_{\$800} - U_{\$1600}}{\$800 - \$1600} = \frac{1.74 - (-1.95)}{-800} = \frac{3.69}{-800} = -0.00461$ utils/$

$$\text{WTP}_{\text{Apple}} = \frac{\Delta U_{\text{brand}}}{|\text{price coeff}|} = \frac{3.78}{0.00461} \approx \$820$$

This is for respondent 42. **Population WTP** uses $\bar{\beta}$ instead.

---

## Run Length Recommendations

| Respondents | Burn-in iterations | Production draws | Thinning |
|-------------|-------------------|-----------------|----------|
| < 200 | 5,000 | 10,000 | 1 |
| 200–500 | 10,000 | 20,000 | 2 |
| 500–1,000 | 20,000 | 30,000 | 5 |
| > 1,000 | 30,000 | 50,000 | 10 |

Thinning reduces autocorrelation in stored draws at the cost of more computation. With thin=5, store every 5th draw.

---

## Convergence Diagnostics

### 1. Trace Plots

Plot $\bar{\beta}_k$ across iterations for each parameter. Healthy chain looks like "fuzzy caterpillar" — no trends, no stuck regions.

```
Good:  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bad:   _______________/‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\___________________
```

### 2. $\hat{R}$ (Gelman-Rubin Statistic)

Run 3+ independent chains with different starting values. Compute:

$$\hat{R} = \sqrt{\frac{\hat{V}(\theta)}{W}}$$

Where $W$ is within-chain variance and $\hat{V}$ is total variance estimate.

**Rule:** $\hat{R} < 1.05$ for all parameters before using results.

### 3. Effective Sample Size

$$\text{ESS} = \frac{S}{1 + 2\sum_{k=1}^{\infty} \rho_k}$$

Where $S$ = total draws, $\rho_k$ = lag-$k$ autocorrelation.

**Rule:** ESS > 400 for each $\bar{\beta}_k$ and each diagonal of $\Sigma$.

### 4. Individual MH Acceptance Rate

Check acceptance rate per respondent after burn-in. Should be 25–45% for all respondents. Outliers (< 10% or > 70%) indicate pathological respondents or poor step-size tuning.

```python
for i, respondent in enumerate(respondents):
    rate = respondent.accepted / respondent.proposed
    if rate < 0.10 or rate > 0.70:
        print(f"Respondent {i}: acceptance={rate:.2f} — investigate")
```

---

## Identifying Segments from HB Output

HB gives you $N$ individual $\beta_i$ vectors. Run K-means or latent class on these to find segments post-hoc.

```python
import numpy as np
from sklearn.cluster import KMeans

# beta_draws shape: (N_respondents, K_params, N_production_draws)
beta_mean = beta_draws.mean(axis=2)  # shape: (N, K)

kmeans = KMeans(n_clusters=3, n_init=20, random_state=0)
segments = kmeans.fit_predict(beta_mean)
```

**Caution:** Post-hoc clustering on HB draws is exploratory. For confirmatory segment analysis, use latent class MNL instead — it estimates segments jointly with utilities.

---

## Common Failure Modes

**Symptom: Price coefficient is positive (higher price → higher utility)**

Cause: Multicollinearity between price and quality in design, or respondents using price as quality signal.

Fix: Check design balance. If the design is correct, consider adding an explicit quality attribute.

**Symptom: $\hat{R}$ fails for $\Sigma$ diagonal but not $\bar{\beta}$**

Cause: $\Sigma$ mixes slowly when $N$ is small relative to $K$. The IW prior is too diffuse.

Fix: Increase $\nu$ toward $K + 10$. Run longer chains.

**Symptom: Individual utilities for one respondent are extreme (|utility| > 10)**

Cause: Respondent chose consistently — all tasks dominated by one profile. MH proposes stay near the MLE which is at $\pm\infty$ for deterministic choosers.

Fix: Flag respondents with < 2 unique choice patterns. Exclude or apply stronger shrinkage prior.

**Symptom: Holdout hit rate < 50%** (below SKILL.md gate of 60%)

Cause: HB may have converged but the model is misspecified (missing interactions, wrong design).

Fix: Check whether a price×brand interaction term improves holdout fit. Add it as a product of the two dummy vectors.

---

## Encoding Schemes

Effect coding (sum-to-zero) is standard for conjoint. **Do not use dummy coding** (0/1) in HB conjoint — it confounds the reference level into the intercept and makes attribute importance calculations incorrect.

**Effect coding for $L$ levels:**

| Level | Code |
|-------|------|
| 1 | $+1, 0, \ldots, 0$ |
| 2 | $0, +1, \ldots, 0$ |
| $\vdots$ | $\vdots$ |
| $L-1$ | $0, 0, \ldots, +1$ |
| $L$ (reference) | $-1, -1, \ldots, -1$ |

Reference level utility: $U_L = -\sum_{l=1}^{L-1} U_l$

**Continuous price attribute:** Enter price as a single continuous variable (e.g., $800 → 8.0 after dividing by 100 for numerical stability). This assumes linear price sensitivity, which is often adequate and produces a single price coefficient used directly in WTP calculation.

---

## Minimal Python Implementation

This sketch runs HB using pure numpy. For production, use `pymc`, `Stan`, or commercial software (Sawtooth).

```python
import numpy as np

def mnl_loglik(beta, X_tasks, chosen_idx):
    """
    beta: (K,)
    X_tasks: list of (n_alts, K) arrays, one per task
    chosen_idx: list of int, chosen alternative index per task
    """
    ll = 0.0
    for X, c in zip(X_tasks, chosen_idx):
        v = X @ beta
        v -= v.max()  # numerical stability
        ll += v[c] - np.log(np.exp(v).sum())
    return ll

def run_hb(respondents, n_burn=10000, n_draw=20000, thin=5):
    N = len(respondents)
    K = respondents[0]['X'][0].shape[1]

    # Priors
    s2 = 4.0
    nu = K + 3
    V = nu * np.eye(K)

    # Initialize
    beta = np.zeros((N, K))
    beta_bar = np.zeros(K)
    Sigma = np.eye(K)
    Sigma_inv = np.eye(K)
    delta = np.ones(N) * 0.3  # MH step size per respondent

    draws = []
    accepted = np.zeros(N)

    for t in range(n_burn + n_draw):
        # Step 1: sample beta_bar
        Sig_star_inv = N * Sigma_inv + (1/s2) * np.eye(K)
        Sig_star = np.linalg.inv(Sig_star_inv)
        mu_star = Sig_star @ (Sigma_inv @ beta.sum(axis=0))
        beta_bar = np.random.multivariate_normal(mu_star, Sig_star)

        # Step 2: sample Sigma
        S = sum((beta[i] - beta_bar)[:, None] @ (beta[i] - beta_bar)[None, :]
                for i in range(N))
        Sigma = np.linalg.inv(
            np.random.wishart(nu + N, np.linalg.inv(V + S)) 
        )
        # Note: sample from IW by inverting Wishart draw
        Sigma_inv = np.linalg.inv(Sigma)

        # Step 3: MH for each respondent
        for i in range(N):
            r = respondents[i]
            prop = beta[i] + np.random.randn(K) * delta[i]
            
            diff_cur = beta[i] - beta_bar
            diff_prop = prop - beta_bar
            
            log_prior_cur = -0.5 * diff_cur @ Sigma_inv @ diff_cur
            log_prior_prop = -0.5 * diff_prop @ Sigma_inv @ diff_prop
            
            log_lik_cur = mnl_loglik(beta[i], r['X'], r['chosen'])
            log_lik_prop = mnl_loglik(prop, r['X'], r['chosen'])
            
            log_alpha = (log_lik_prop + log_prior_prop 
                         - log_lik_cur - log_prior_cur)
            
            if np.log(np.random.rand()) < log_alpha:
                beta[i] = prop
                accepted[i] += 1

        # Adaptive step size during burn-in
        if t < n_burn and (t + 1) % 500 == 0:
            rates = accepted / (t + 1)
            delta = np.where(rates < 0.25, delta * 0.9,
                    np.where(rates > 0.45, delta * 1.1, delta))

        # Store production draws
        if t >= n_burn and (t - n_burn) % thin == 0:
            draws.append({
                'beta_bar': beta_bar.copy(),
                'Sigma': Sigma.copy(),
                'beta': beta.copy()
            })

    return draws
```

*This is for illustration. It omits convergence checks and is not optimized for speed.*

---

## Relationship to Aggregate MNL

| Property | Aggregate MNL | HB |
|----------|--------------|-----|
| Individual utilities | No | Yes |
| Handles heterogeneity | No | Yes |
| Data required | ~100 respondents | ~200 respondents |
| Computation | Fast (minutes) | Slow (hours) |
| WTP from segments | Post-hoc only | Built-in via $\beta_i$ |
| Holdout prediction | Lower | Higher (typically +10–20 pp) |

Use aggregate MNL only as a sanity check or when compute budget is very limited. HB is the standard in commercial conjoint practice.

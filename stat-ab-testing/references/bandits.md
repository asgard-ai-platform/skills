# Multi-Armed Bandits for Experimentation

Bandits are an alternative to fixed-horizon A/B tests that **allocate traffic adaptively** — routing more users toward better-performing variants as evidence accumulates. The tradeoff is exploration (learning which arm is best) versus exploitation (using the best arm you know about now).

---

## When Bandits Beat Fixed A/B Tests

| Situation | Use Bandit | Use Fixed A/B |
|-----------|-----------|---------------|
| High cost of showing inferior variant (e.g., pricing, critical UX) | ✓ | |
| Short experiment window, many variants | ✓ | |
| Need unbiased causal estimate for decision records | | ✓ |
| Detecting interaction effects or segment-level effects | | ✓ |
| Regulatory/audit requirement for controlled study | | ✓ |
| Long-term novelty effects suspected | | ✓ |
| Need interpretable p-value / confidence interval for stakeholders | | ✓ |

**Critical constraint**: Bandits produce biased estimates of treatment effect. If you need to know "how much does this button change conversion?", use a fixed A/B test. Bandits answer "which variant should we show?", not "by how much is it better?"

---

## The Three Practical Algorithms

### 1. Epsilon-Greedy

The simplest approach. With probability ε, explore (choose randomly); with probability 1-ε, exploit (choose best arm so far).

```
Algorithm:
  ε = exploration rate (e.g., 0.1)
  For each incoming user:
    if random() < ε:
      show random arm
    else:
      show arm with highest observed conversion rate so far
```

**Update rule** after observing outcome y ∈ {0, 1}:
```
n_k  ← n_k + 1
p̂_k  ← p̂_k + (y - p̂_k) / n_k   # running mean
```

**Worked example** (3 variants, ε = 0.1, after 1000 assignments):

| Arm | Assignments | Conversions | p̂ |
|-----|-------------|-------------|-----|
| A (control) | 33 (explore) + 200 (exploit) ≈ 233 | 21 | 0.090 |
| B | 33 + 0 | 4 | 0.121 |
| C | 33 + 700 | 91 | **0.130** |

Arm C gets exploited heavily because it emerged as the best early. Arm B is underexplored and its true rate of 0.12 is estimated poorly.

**Weakness**: ε is fixed — early in the test you may exploit a noise leader; late in the test you waste traffic on exploration when you're already confident.

**Decaying epsilon**: `ε_t = min(1, C / (d² × t))` where t is the number of rounds, C and d are tuning constants. More exploration early, less later.

---

### 2. Upper Confidence Bound (UCB1)

Choose the arm with the highest upper confidence bound. This formalizes "optimism under uncertainty" — try arms you're uncertain about because they might be better.

**UCB1 selection rule**:
```
arm = argmax_k [ p̂_k + sqrt( 2 × ln(t) / n_k ) ]
```

Where:
- `p̂_k` = observed conversion rate for arm k
- `n_k` = number of times arm k has been shown
- `t` = total assignments so far

The second term is the uncertainty bonus — it's large when an arm has been shown few times (n_k small) and shrinks as n_k grows.

**Worked example** (after t = 100 total):

| Arm | n_k | p̂_k | Uncertainty √(2 ln 100 / n_k) | UCB score |
|-----|-----|------|-------------------------------|-----------|
| A | 50 | 0.10 | √(9.21/50) = 0.429 | **0.529** |
| B | 30 | 0.13 | √(9.21/30) = 0.554 | 0.684 |
| C | 20 | 0.08 | √(9.21/20) = 0.679 | 0.759 |

UCB1 would pick arm C next because its uncertainty bonus is high — it might be better than it appears.

**Logarithmic regret**: UCB1 guarantees regret grows at most as O(ln t), which is optimal for the stochastic setting.

---

### 3. Thompson Sampling (Recommended Default)

Maintain a Beta distribution for each arm's conversion rate. At each step, sample one value from each arm's distribution and show the arm with the highest sample.

**Beta distribution** for binary outcomes:
```
Prior:  Beta(α=1, β=1)  — uniform, no prior knowledge
After n_k assignments with s_k successes:
  Posterior: Beta(α = 1 + s_k, β = 1 + n_k - s_k)
```

**Selection rule**:
```python
import random

def beta_sample(successes, failures):
    # Sample from Beta(α, β) where α = 1 + successes, β = 1 + failures
    return random.betavariate(1 + successes, 1 + failures)

def choose_arm(arms):
    # arms = list of (successes, failures) tuples
    samples = [beta_sample(s, f) for s, f in arms]
    return samples.index(max(samples))
```

**Worked example** after 200 assignments (arm A: 20/100, arm B: 15/60, arm C: 8/40):

| Arm | s_k | f_k | Beta params | Mean | Std |
|-----|-----|-----|-------------|------|-----|
| A | 20 | 80 | Beta(21, 81) | 0.206 | 0.038 |
| B | 15 | 45 | Beta(16, 46) | 0.258 | 0.053 |
| C | 8 | 32 | Beta(9, 33) | 0.214 | 0.063 |

Arm B currently has the highest mean AND the tightest posterior among contenders, so it will be selected most often — but arm C's wide distribution means it still gets sampled occasionally.

**Why Thompson Sampling wins in practice**:
- Automatically balances explore/exploit without a tuning parameter
- Probability of pulling each arm ≈ probability that arm is the best → elegant interpretation
- Empirically competitive with UCB, easier to extend to non-binary outcomes

---

## Thompson Sampling for Non-Binary Metrics

For continuous metrics (revenue per visitor, session duration), use a Normal-Inverse-Gamma conjugate:

```
Prior: μ ~ Normal(μ₀, σ²/κ₀), σ² ~ InvGamma(α₀, β₀)
  Standard non-informative: μ₀=0, κ₀=1, α₀=1, β₀=1

After n observations with sample mean x̄ and sum of squares SS:
  κ_n = κ₀ + n
  μ_n = (κ₀μ₀ + nx̄) / κ_n
  α_n = α₀ + n/2
  β_n = β₀ + SS/2 + (κ₀ × n × (x̄ - μ₀)²) / (2κ_n)
```

In practice, if n is large enough (> 30 per arm), approximate with:
```python
import random, math

def normal_sample(observations):
    n = len(observations)
    mean = sum(observations) / n
    variance = sum((x - mean)**2 for x in observations) / n
    # Sample mean is Normal(mean, variance/n)
    return random.gauss(mean, math.sqrt(variance / n))
```

---

## Stopping Rules for Bandits

Bandits don't have a natural stopping criterion the way fixed A/B tests do. Three options:

### Option 1: Fixed Horizon (Bandit + Stop)
Pre-decide N total assignments, run bandit to completion, then deploy winner. Retains bandit's efficiency during the test without requiring a stopping rule.

### Option 2: Probability of Being Best

Stop when one arm dominates:
```
P(arm k is best) = Monte Carlo estimate:
  Draw 10,000 samples from each arm's posterior
  P(k is best) = fraction of draws where arm k has the highest sample
```

**Decision rule**: Stop when `P(best arm) > 0.95`.

**Worked example**:

```python
import random

def prob_best(arms_params, n_samples=10000):
    """
    arms_params: list of (successes, failures) for each arm
    returns: list of P(arm is best) for each arm
    """
    wins = [0] * len(arms_params)
    for _ in range(n_samples):
        samples = [random.betavariate(1 + s, 1 + f) for s, f in arms_params]
        wins[samples.index(max(samples))] += 1
    return [w / n_samples for w in wins]

# After 500 assignments:
arms = [(55, 145), (40, 110), (70, 130)]  # (successes, failures)
probs = prob_best(arms)
# → [0.18, 0.09, 0.73]  — arm C at 73%, not conclusive yet
```

### Option 3: Expected Remaining Regret

Stop when the expected loss from not switching to the best arm is below a business threshold (e.g., < 0.1% conversion rate points expected regret). More complex to implement; see Russo et al. (2018).

---

## Practical Pitfalls

**Context window contamination**: If users are assigned to arms based on session and return multiple times, re-randomizing on each session gives the bandit noisy feedback. Track by user ID, not session.

**Delayed rewards**: If conversions happen hours or days after exposure (e.g., purchases), your bandit updates on incomplete information. Use a fixed delay before updating: only count conversions that occurred at least T hours after assignment, using only users assigned more than T hours ago.

**Cold start over-exploitation**: With a non-informative prior and a lucky first few conversions on arm A, the bandit may exploit arm A before arms B and C have been shown enough times. Force a burn-in period (e.g., show each arm at least 50 times before enabling adaptive allocation).

**Multiple concurrent bandits**: Running two bandits simultaneously that share the same user pool may interact. Arm allocations in bandit 1 affect who is available for bandit 2, violating independence. Serialize or use orthogonal randomization layers.

**Survivorship in segment analysis**: Bandit allocation is unequal by design, so segments naturally receive unequal exposure. Don't interpret "arm C converted best among mobile users" without accounting for the fact that arm C was allocated more traffic overall. Compute within-segment p(best) separately if segment effects matter.

---

## Comparison: Regret vs Sample Size Required

For a two-arm test, baseline rate p₁ = 0.10, treatment p₂ = 0.12 (MDE = 20% relative):

| Method | Users to deploy winner | Average regret (conversions lost vs oracle) |
|--------|----------------------|----------------------------------------------|
| Fixed A/B (α=0.05, power=0.8) | 15,000 per arm = 30,000 total, all before deploy | ~(0.02 × 15,000) / 2 ≈ 150 |
| Epsilon-greedy (ε=0.1) | ~25,000 total (less certain at stop) | ~100–130 |
| Thompson Sampling | ~20,000 total to P(best) > 0.95 | ~60–90 |
| Fixed A/B + deploy at completion | 30,000 then full deploy | Lowest post-deploy regret |

**The fixed A/B test has lower total regret** if you care about the full lifetime of the feature, because you get an unbiased estimate and then deploy at full traffic. Bandits shine when the test window is short or the downside of showing a bad variant is high during the test itself.

---

## Decision Flowchart

```
Is measuring effect size important?
  YES → Fixed A/B test
  NO  ↓

Is the test running for < 2 weeks with high traffic?
  YES → Thompson Sampling bandit
  NO  ↓

Are there > 4 variants to compare?
  YES → Thompson Sampling (bandit scales better than pairwise A/B)
  NO  ↓

Is showing a worse variant costly during the test?
  YES → Thompson Sampling
  NO  → Fixed A/B test (cleaner inference)
```

---

## Minimal Implementation Checklist

Before running a bandit experiment:

- [ ] Conversion event is logged with user ID and arm assignment
- [ ] Reward is binary OR you have a plan for continuous reward approximation
- [ ] Delayed conversion window is defined (e.g., 24-hour attribution)
- [ ] Burn-in period specified (minimum impressions per arm before adaptive allocation starts)
- [ ] Stopping criterion defined (fixed horizon, P(best) threshold, or calendar date)
- [ ] Winner deployment plan: what happens when the bandit stops?
- [ ] Logging captures final arm allocation percentages for post-hoc analysis

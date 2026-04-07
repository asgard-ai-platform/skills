---
name: "algo-social-virality"
description: "Model viral spread dynamics using SIR/SIS/SEIR compartmental models. Use this skill when the user needs to predict content spread patterns, estimate viral thresholds, or model information cascades in social networks — even if they say 'will this go viral', 'epidemic model for content', or 'spread prediction'."
metadata:
  category: "WP-38 社群演算法"
  tags: ["social-media", "virality", "epidemic-model", "sir"]
---

# Viral Spread Models

## Overview

Compartmental models (SIR, SIS, SEIR) model how content/information spreads through populations. Susceptible → Infected → Recovered mirrors unaware → sharing → stopped sharing. Key metric: R0 (basic reproduction number). Solves as ODEs in O(T × N) for T timesteps, N compartments.

## When to Use

**Trigger conditions:**
- Modeling how content spreads through a social network
- Estimating whether a campaign will achieve viral threshold
- Analyzing post-hoc spread dynamics of viral events

**When NOT to use:**
- When predicting individual user behavior (use influence scoring)
- When measuring engagement metrics (use engagement rate calculator)

## Algorithm

```
IRON LAW: Viral Spread Occurs ONLY When R0 > 1
R0 = transmission rate (β) / recovery rate (γ).
Below R0 = 1, content dies out regardless of initial seed size.
Above R0 = 1, exponential growth phase begins before saturation.
Design interventions (seeding, incentives) to push R0 above threshold.
```

### Phase 1: Input Validation
Define: population size (N), initial seed size (I₀), transmission rate (β — probability of sharing upon exposure), recovery rate (γ — rate of losing interest).
**Gate:** Parameters non-negative, β and γ estimated from historical data or assumed.

### Phase 2: Core Algorithm
**SIR Model:** dS/dt = -βSI/N, dI/dt = βSI/N - γI, dR/dt = γI
1. Initialize: S=N-I₀, I=I₀, R=0
2. Iterate using Euler method or RK4 at discrete timesteps
3. Track peak infected (maximum simultaneous sharers) and total ever-infected

**SIS variant:** No recovery to immune state — recovered become susceptible again (recurring content).

### Phase 3: Verification
Check: S+I+R = N at all timesteps (conservation). Peak and final sizes plausible for given R0.
**Gate:** Population conserved, dynamics consistent with R0.

### Phase 4: Output
Return time series of compartments and summary metrics.

## Output Format

```json
{
  "time_series": [{"t": 0, "S": 9900, "I": 100, "R": 0}],
  "summary": {"R0": 2.5, "peak_infected": 3200, "peak_day": 12, "total_infected": 8500},
  "metadata": {"model": "SIR", "beta": 0.5, "gamma": 0.2, "population": 10000}
}
```

## Examples

### Sample I/O
**Input:** N=10000, I₀=10, β=0.3, γ=0.1 (R0=3.0)
**Expected:** Exponential growth, peak ~4000 at day ~15, total infected ~9500

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| R0 = 0.8 | Rapid decay | Below threshold, dies out |
| I₀ = 1 | Slower start but same eventual dynamics | Single seed takes longer to ignite |
| β = γ (R0=1) | Linear, no growth | Critical threshold, endemic equilibrium |

## Gotchas

- **Homogeneous mixing assumption**: SIR assumes everyone interacts equally. Real networks have hubs, clusters, and weak ties. Use network-based models for realistic spread.
- **Parameter estimation**: β and γ are hard to estimate for social content. Use early spread data to fit parameters, then project.
- **Content ≠ disease**: Unlike diseases, content sharing is voluntary and influenced by content quality, platform algorithms, and trends. Models give rough dynamics, not precise predictions.
- **Platform algorithms**: Social media algorithms amplify or suppress content. The "transmission rate" is partly determined by the platform, not just user behavior.
- **Temporal dynamics**: Content virality often has a much shorter lifecycle than disease (hours-days vs weeks-months). Adjust timescales accordingly.

## References

- For network-based epidemic models, see `references/network-sir.md`
- For parameter estimation from early data, see `references/parameter-fitting.md`

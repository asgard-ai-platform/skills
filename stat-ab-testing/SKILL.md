---
name: "stat-ab-testing"
description: "Design and analyze A/B tests with proper statistical methodology including sample size calculation, randomization, frequentist and Bayesian approaches, and sequential testing. Use this skill when the user needs to set up an experiment, calculate required sample size, interpret test results, or decide between testing methodologies — even if they say 'should we A/B test this', 'how many users do we need', 'is the test result conclusive', or 'can we stop the test early'."
metadata:
  category: "WP-21 設計/資訊/傳播/公衛"
  tags: ["statistics", "ab-testing", "experimentation"]
---

# A/B Testing Statistics

## Framework

```
IRON LAW: Calculate Sample Size BEFORE Running the Test

Running a test without knowing the required sample size leads to two
failures: stopping too early (false positives) or running too long (waste).

Required inputs: baseline conversion rate, minimum detectable effect (MDE),
significance level (α), power (1-β). Calculate BEFORE starting.
```

### Sample Size Formula (Proportions)

```
n per group ≈ (Z_α/2 + Z_β)² × [p₁(1-p₁) + p₂(1-p₂)] / (p₁ - p₂)²
```

Quick reference (α=0.05, power=0.8):
| Baseline Rate | MDE (relative) | N per Group |
|--------------|----------------|-------------|
| 5% | 10% (→5.5%) | ~58,000 |
| 5% | 20% (→6.0%) | ~15,000 |
| 10% | 10% (→11%) | ~15,000 |
| 10% | 20% (→12%) | ~4,000 |

### Testing Approaches

| Approach | How It Works | Best When |
|----------|-------------|-----------|
| **Frequentist (fixed-horizon)** | Set sample size, run to completion, then analyze | Standard practice, well-understood |
| **Bayesian** | Update beliefs with data, compute probability of improvement | Want probability statements ("90% chance B is better") |
| **Sequential testing** | Check results at intervals with adjusted thresholds | Need to stop early if clear winner, or limit downside risk |

### Experiment Design Checklist

1. **Hypothesis**: What do you expect to happen and why?
2. **Primary metric**: ONE key metric (conversion, revenue, retention)
3. **Guardrail metrics**: Metrics that must NOT degrade (page load time, error rate)
4. **Randomization unit**: User, session, or device?
5. **Sample size**: Calculated from baseline, MDE, α, power
6. **Duration**: Account for weekly cycles (minimum 1-2 full weeks)
7. **Stopping rules**: Pre-defined — do NOT peek and stop early without correction

### Analysis Steps

1. Check randomization balance (are groups comparable on pre-treatment metrics?)
2. Calculate observed difference and confidence interval
3. Run significance test (z-test for proportions, t-test for continuous)
4. Check guardrail metrics
5. Interpret with practical significance in mind

## Output Format

```markdown
# A/B Test Design: {Experiment Name}

## Hypothesis
- H₀: {no difference}
- H₁: {expected improvement}
- Primary metric: {metric}
- MDE: {X% relative}

## Sample Size
- Baseline rate: {X%}
- Required N per group: {N}
- Estimated duration: {days/weeks}

## Results (post-test)
| Metric | Control | Treatment | Diff | CI (95%) | p-value |
|--------|---------|-----------|------|----------|---------|
| {primary} | X% | X% | +X% | [X, X] | {value} |

## Decision
{Ship / Don't ship / Extend test} — {rationale}
```

## Gotchas

- **Peeking inflates false positives**: Checking results daily and stopping when p < 0.05 can produce a 30%+ false positive rate. Use sequential testing methods if you need to peek.
- **Novelty effect**: New features may show a lift that fades as users get used to them. Run tests long enough (2+ weeks) to stabilize.
- **Simpson's paradox**: An overall positive result can be negative in every subgroup (or vice versa). Segment by key dimensions.
- **Network effects / interference**: If treatment users interact with control users (social features, marketplace), independence is violated. Use cluster randomization.
- **Statistical significance threshold is arbitrary**: α=0.05 is convention, not truth. For high-stakes decisions (pricing, major UX changes), consider α=0.01.

## References

- For Bayesian A/B testing methodology, see `references/bayesian-ab.md`
- For multi-armed bandit approach, see `references/bandits.md`

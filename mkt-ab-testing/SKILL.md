---
name: "mkt-ab-testing"
description: "Design and execute marketing A/B tests for landing pages, email campaigns, ad creatives, and pricing with proper test design and result analysis. Use this skill when the user needs to test marketing variations, improve conversion rates through experimentation, or decide between two campaign approaches — even if they say 'which version performs better', 'test this landing page', 'A/B test our email subject line', or 'should we change our CTA'."
metadata:
  category: "WP-09 數位行銷"
  tags: ["digital-marketing", "ab-testing", "conversion", "experimentation"]
---

# Marketing A/B Testing

## Framework

```
IRON LAW: One Variable at a Time

If you change the headline AND the image AND the CTA simultaneously,
you cannot know which change caused the result. Test ONE variable per
experiment. If you need to test multiple changes, use sequential tests
or multivariate testing (MVT) with sufficient traffic.
```

### What to Test (by Impact)

| Element | Expected Lift | Traffic Needed | Priority |
|---------|-------------|---------------|---------|
| **Offer/Pricing** | 10-50% | Medium | Highest |
| **Headline/Subject line** | 5-30% | Low | High |
| **CTA (text, color, placement)** | 5-20% | Low | High |
| **Page layout** | 5-15% | Medium | Medium |
| **Image/Video** | 3-15% | Medium | Medium |
| **Form fields** | 5-25% (reduction = higher CVR) | Low | Medium |
| **Social proof placement** | 3-10% | Medium | Lower |

### Test Design

1. **Hypothesis**: "Changing [variable] from [A] to [B] will increase [metric] by [X%] because [reasoning]"
2. **Primary metric**: ONE metric that determines winner (conversion rate, revenue per visitor, signup rate)
3. **Guardrail metrics**: Metrics that must NOT degrade (bounce rate, page load time, revenue per user)
4. **Traffic split**: 50/50 between control and variant (standard)
5. **Sample size**: Calculate before starting (see stat-ab-testing for formula)
6. **Duration**: Minimum 1-2 full business weeks (capture day-of-week effects)

### Common Marketing Tests

| Test | Control (A) | Variant (B) | Metric |
|------|-----------|------------|--------|
| Email subject | "Your weekly update" | "3 trends you missed this week" | Open rate |
| Landing page CTA | "Sign Up" | "Start Free Trial" | Click rate |
| Pricing page | Show 3 plans | Show 2 plans + "most popular" badge | Conversion rate |
| Ad creative | Product photo | Lifestyle photo with product | CTR → conversion |
| Form length | 8 fields | 4 fields | Form completion rate |

### Analysis & Decision

| Result | Decision | Action |
|--------|---------|--------|
| B wins, p < 0.05, meaningful lift | Ship B | Deploy variant, start next test |
| B wins, p < 0.05, tiny lift (<1%) | Don't ship | Lift not worth the change risk |
| No significant difference | Keep A | A is the known quantity; test something else |
| B wins on primary but loses on guardrail | Investigate | May need to redesign variant |

## Output Format

```markdown
# A/B Test Plan: {Test Name}

## Hypothesis
Changing {variable} from {A} to {B} will increase {metric} by {X%} because {reasoning}.

## Design
- Primary metric: {metric}
- Guardrail: {metric(s)}
- Split: 50/50
- Sample size: {N per variant}
- Duration: {days/weeks}

## Results
| Metric | Control | Variant | Diff | CI (95%) | Significant? |
|--------|---------|---------|------|----------|-------------|
| {primary} | {value} | {value} | {±%} | [{lower}, {upper}] | Y/N |

## Decision
{Ship / Don't ship / Extend} — {rationale}
```

## Gotchas

- **Don't stop early because it "looks good"**: Peeking at results and stopping when you see significance inflates false positive rates to 30%+. Run to planned sample size.
- **Day-of-week effects**: Monday visitors behave differently from Saturday visitors. Always run tests for at least 1-2 complete weeks.
- **Novelty effect**: A new design may get a temporary lift from curiosity. Wait 2+ weeks to see if the effect sustains.
- **Winner's curse**: The estimated lift from a test is often larger than the true lift due to statistical noise. Expect the actual impact after deployment to be smaller.
- **Don't test everything — test what matters**: Running 20 small tests on button colors while ignoring the pricing page is misallocating effort. Test high-impact elements first.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/ab_test.py` | Two-proportion z-test with effect size and sample-size planning | `python scripts/ab_test.py --help` |

Run `python scripts/ab_test.py --verify` to execute built-in sanity tests.

## References

- For statistical methodology (sample size, p-values), see the stat-ab-testing skill
- For multivariate testing design, see `references/mvt-design.md`

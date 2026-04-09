# Multivariate Testing (MVT) Design

## When MVT Is Appropriate

MVT is **not** a replacement for A/B testing — it is a tool for a specific situation:

| Condition | Use A/B | Use MVT |
|-----------|---------|---------|
| You want to know which single change drives lift | ✓ | |
| You have one high-impact hypothesis to validate | ✓ | |
| Traffic is below ~50k visitors/month | ✓ | |
| You need to test interactions between elements | | ✓ |
| You have high traffic and want to test 2+ elements simultaneously | | ✓ |
| You need to ship the winning combination faster than sequential tests | | ✓ |

The parent skill's IRON LAW — **one variable at a time** — still governs A/B tests. MVT is the structured exception: it lets you vary multiple elements simultaneously, but only if you have the traffic to support it and you explicitly care about element interactions.

---

## Full Factorial vs. Fractional Factorial

### Full Factorial

Every combination of every element is tested.

- 2 headlines × 2 CTAs × 2 images = **8 combinations** (2³)
- 3 headlines × 2 CTAs × 2 images = **12 combinations** (3×2×2)

**Advantage**: You observe every possible interaction.  
**Disadvantage**: Traffic requirement scales exponentially with the number of combinations.

### Fractional Factorial

A carefully chosen subset of combinations that still allows estimation of main effects and selected two-way interactions.

**Advantage**: Dramatically fewer combinations needed.  
**Disadvantage**: Some higher-order interactions are confounded (you cannot distinguish them from each other).

**Rule of thumb for marketing MVT**: Unless you have strong reason to believe a specific interaction exists, start with fractional factorial. Most marketing lifts come from main effects, not interactions.

---

## Traffic Requirement

This is the most common reason MVT fails in practice.

### Formula

```
N_total = N_per_combination × number_of_combinations
```

Where `N_per_combination` uses the same two-proportion z-test formula as A/B testing (see `stat-ab-testing`), but with an important adjustment: **each combination receives less traffic**, so the per-combination sample size stays the same as a standard A/B test.

### Worked Example

Situation: Landing page with baseline CVR = 3%, MDE = 0.6 pp (20% relative lift), α = 0.05, power = 0.80.

From a standard sample size calculator: **N = 5,890 per variant**.

Now add MVT:

| Elements | Combinations | Total visitors needed | Daily traffic needed (2-week test) |
|----------|-------------|----------------------|-------------------------------------|
| 2 headlines × 2 CTAs | 4 | 23,560 | 1,683 |
| 2 headlines × 2 CTAs × 2 images | 8 | 47,120 | 3,366 |
| 3 headlines × 2 CTAs × 2 images | 12 | 70,680 | 5,049 |
| 4 headlines × 2 CTAs × 2 images | 16 | 94,240 | 6,731 |

**If your landing page gets 500 visitors/day, you cannot run MVT with more than 4 combinations in a 2-week test.** Run sequential A/B tests instead.

---

## Taguchi Method (Fractional Factorial for Small Traffic)

When you cannot afford full factorial but still want to test multiple elements, Taguchi orthogonal arrays let you estimate main effects from a fraction of the full design.

### L4 Array (3 elements, 2 levels each → 4 combinations instead of 8)

| Combination | Headline | CTA | Image |
|-------------|----------|-----|-------|
| C1 | A | A | A |
| C2 | A | B | B |
| C3 | B | A | B |
| C4 | B | B | A |

This array is **orthogonal**: each level of each factor appears exactly twice, so main effects are estimable even though you only ran 4 of the 8 possible combinations. Two-way interactions are confounded with each other (Headline×CTA is confounded with Image), so you cannot separately estimate them.

### How to estimate main effects from an L4 array

Let CVR(Ci) = conversion rate for combination i.

```
Effect(Headline=B) = [CVR(C3) + CVR(C4)] / 2 − [CVR(C1) + CVR(C2)] / 2
Effect(CTA=B)      = [CVR(C2) + CVR(C4)] / 2 − [CVR(C1) + CVR(C3)] / 2
Effect(Image=B)    = [CVR(C2) + CVR(C3)] / 2 − [CVR(C1) + CVR(C4)] / 2
```

The largest positive effect identifies the winner for that element. Predicted best combination = each element at its winning level.

### Taguchi Caveat

Taguchi was designed for manufacturing tolerance optimization, not statistical inference. It does **not** give you p-values or confidence intervals natively. Use it for **screening** (identifying the 1-2 elements most worth testing) followed by a confirmatory A/B test of the predicted winner vs. control.

---

## Worked MVT Example: Pricing Page

### Setup

Page has three testable elements:

| Element | Level A (Control) | Level B (Variant) |
|---------|------------------|------------------|
| Plan count | 3 plans | 2 plans |
| Badge | None | "Most Popular" on mid-tier |
| CTA text | "Get Started" | "Start Free Trial" |

Baseline CVR = 4.2%, MDE = 0.84 pp, α = 0.05, power = 0.80 → N = 4,410 per combination.

Traffic = 1,200 visitors/day. Full factorial (8 combinations) requires 35,280 visitors = 29 days. Too long.

**Decision**: Use L4 Taguchi array (4 combinations, 17,640 visitors, 15 days).

### L4 Assignment

| Combination | Plan count | Badge | CTA | CVR (observed) |
|-------------|-----------|-------|-----|----------------|
| C1 | 3 plans | None | "Get Started" | 4.1% |
| C2 | 3 plans | "Most Popular" | "Start Free Trial" | 5.0% |
| C3 | 2 plans | None | "Start Free Trial" | 5.3% |
| C4 | 2 plans | "Most Popular" | "Get Started" | 4.8% |

### Main Effect Calculation

```
Effect(2 plans)         = (5.3 + 4.8)/2 − (4.1 + 5.0)/2 = 5.05 − 4.55 = +0.50 pp
Effect(Badge)           = (5.0 + 4.8)/2 − (4.1 + 5.3)/2 = 4.90 − 4.70 = +0.20 pp
Effect("Start Free Trial") = (5.0 + 5.3)/2 − (4.1 + 4.8)/2 = 5.15 − 4.45 = +0.70 pp
```

**Screening conclusion**: CTA text has the largest effect (+0.70 pp), followed by plan count (+0.50 pp). Badge effect is small (+0.20 pp).

### Follow-up Action

1. Run a confirmatory A/B test: Control (3 plans, no badge, "Get Started") vs. Predicted Winner (2 plans, "Most Popular" badge, "Start Free Trial").
2. If the predicted winner confirms, ship it.
3. If the predicted winner does not confirm (winner's curse is common), investigate — the interaction between plan count and CTA may be negative.

---

## Interaction Effects: When They Matter

An interaction exists when the effect of one element depends on the level of another.

### Example of a dangerous interaction

- "Start Free Trial" outperforms "Get Started" when showing 2 plans (+1.2 pp).
- "Start Free Trial" underperforms "Get Started" when showing 3 plans (−0.4 pp).

If you had only run the L4 array, you would have estimated a +0.70 pp main effect for the CTA and shipped the "Start Free Trial" CTA on your existing 3-plan page — getting a lift in the wrong direction.

### How to detect interactions

Only a full factorial design lets you directly estimate interactions. For a 2×2×2 design, the two-way interaction term for elements X and Y is:

```
Interaction(X, Y) = [CVR(X=B,Y=B) + CVR(X=A,Y=A)] / 2
                  − [CVR(X=B,Y=A) + CVR(X=A,Y=B)] / 2
```

(Averaging over all levels of the third element.)

**When to suspect an interaction**:
- The predicted best combination (from main effects alone) performs worse than the best individual combination in the array.
- You are changing elements that are visually or semantically related (e.g., headline and sub-headline; offer text and CTA).

### Practical rule

If elements are **independent in meaning** (image style vs. form field count), interactions are unlikely — use fractional factorial.  
If elements are **coupled in meaning** (offer framing vs. CTA text, price display vs. plan count), budget for full factorial or accept the risk of missing interactions.

---

## Sequential A/B vs. MVT: Decision Framework

```
Does the test involve >1 element?
  └─ No → Standard A/B test. Stop here.
  └─ Yes
       └─ Do you need to know WHICH element drives the lift?
            └─ Yes → Run sequential A/B tests (fastest to isolate)
            └─ No → Do you suspect an interaction between elements?
                     └─ Yes → Full factorial MVT (budget accordingly)
                     └─ No → How much traffic do you have?
                              └─ <2,000/day → Sequential A/B. MVT not viable.
                              └─ 2,000–10,000/day → L4/L8 Taguchi (screening)
                                                     + confirmatory A/B
                              └─ >10,000/day → Full factorial MVT feasible
                                               (up to 6-8 combinations)
```

---

## Common MVT Mistakes

**Running MVT to avoid making a decision.** Wanting to "test everything at once" is often a symptom of not having a prioritized hypothesis. If you do not know which element to test, run a heuristic audit first; do not default to MVT.

**Stopping when the first combination reaches significance.** In MVT with 8 combinations, you are running 8 simultaneous tests. Using α = 0.05 for each means the experiment-wise false positive rate is approximately `1 − (0.95)^8 = 34%`. Apply a Bonferroni correction or use a pre-planned primary comparison (best combination vs. control).

**Bonferroni correction**: divide your α by the number of combinations being compared to control.
- 4 combinations, α = 0.05 → use α = 0.0125 per comparison
- 8 combinations, α = 0.05 → use α = 0.00625 per comparison

**Calling Taguchi "statistically significant."** Taguchi main effects are point estimates, not hypothesis tests. They are screening tools. Always confirm with a follow-up A/B test before shipping.

**Not accounting for traffic dilution.** Every additional combination in your MVT reduces the traffic per combination. A 4-combination test runs at the same traffic-per-variant as an A/B test; an 8-combination test halves it. Run your sample size calculator against `N_per_combination`, not `N_total`.

**Mixing unequal traffic splits.** If one combination is the current production page, it is tempting to give it more traffic to avoid revenue risk. This does not reduce statistical power for detecting improvement — but it does mean your test will run longer. Decide upfront: equal splits (fastest to significant result) or weighted splits (less exposure to unproven variants). Do not change weights mid-test.

---

## Quick Reference: L8 Orthogonal Array

For 7 elements at 2 levels each, 8 combinations instead of 128. Rarely needed in marketing, but included for completeness.

| Combo | E1 | E2 | E3 | E4 | E5 | E6 | E7 |
|-------|----|----|----|----|----|----|-----|
| C1 | A | A | A | A | A | A | A |
| C2 | A | A | A | B | B | B | B |
| C3 | A | B | B | A | A | B | B |
| C4 | A | B | B | B | B | A | A |
| C5 | B | A | B | A | B | A | B |
| C6 | B | A | B | B | A | B | A |
| C7 | B | B | A | A | B | B | A |
| C8 | B | B | A | B | A | A | B |

Each element's main effect: average CVR for all rows where element = B, minus average CVR for all rows where element = A. All two-way interactions are confounded with other two-way interactions (resolution III design).

In practice: if you have 7 independent elements to screen and ≥8,000 visitors/day, L8 is viable. For most marketing teams, this situation arises only on high-traffic e-commerce homepages or email subject line factories where you have large list sizes.

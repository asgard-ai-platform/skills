---
name: "soc-innovation-diffusion"
description: "Apply Rogers' Diffusion of Innovations theory to analyze how new products, ideas, or technologies spread through populations. Use this skill when the user needs to plan adoption strategy, segment adopters, cross the chasm from early adopters to mainstream, or predict adoption curves — even if they say 'how do we get more people to use this', 'why isn't our product taking off', or 'how do we reach the mainstream'."
metadata:
  category: "WP-18 社會科學院"
  tags: ["social-science", "innovation-diffusion", "adoption"]
---

# Diffusion of Innovations

## Overview

Rogers' theory describes how innovations spread through a population in a predictable S-curve pattern, with five adopter categories that require different strategies. Moore's "Crossing the Chasm" extends this by identifying the critical gap between early adopters and the early majority.

## Framework

```
IRON LAW: The Chasm Is Real — Early Adopters ≠ Mainstream

Visionaries (early adopters) buy because it's NEW and they can tolerate
imperfections. Pragmatists (early majority) buy because it WORKS and
others already use it. These are fundamentally different buyer psychologies.

Success with early adopters does NOT predict mainstream success.
The strategy that wins innovators will FAIL with the majority.
```

### The Five Adopter Categories

| Category | % of Population | Motivation | Strategy |
|----------|----------------|-----------|----------|
| **Innovators** | 2.5% | Technology enthusiasts, thrill of the new | Tech specs, early access, "be the first" |
| **Early Adopters** | 13.5% | Visionaries, strategic advantage seekers | Vision alignment, ROI potential, case studies |
| **Early Majority** | 34% | Pragmatists, want proven solutions | References, complete solution, low risk |
| **Late Majority** | 34% | Conservatives, follow the herd | Industry standard, peer pressure, simplicity |
| **Laggards** | 16% | Skeptics, tradition-bound | Necessity, no alternative, bundled with required product |

### The Chasm (Moore)

The gap between Early Adopters (16%) and Early Majority (34%) is where most innovations die. To cross:

1. **Pick a beachhead segment**: ONE specific niche within the early majority
2. **Deliver a whole product**: Not just the core product — the complete solution including support, integrations, documentation
3. **Win the segment completely**: Become the de facto standard in that niche
4. **Use that win as reference**: Pragmatists buy what other pragmatists use
5. **Expand to adjacent segments**: Bowling pin strategy — each niche conquest enables the next

### Five Factors Affecting Adoption Speed

| Factor | Definition | Faster Adoption When... |
|--------|-----------|----------------------|
| **Relative advantage** | How much better than the current solution | Much better, obvious improvement |
| **Compatibility** | Fit with existing values, practices, infrastructure | Minimal change required |
| **Complexity** | Ease of understanding and use | Simple to grasp and use |
| **Trialability** | Can it be tested before committing? | Free trial, freemium, pilot available |
| **Observability** | Can others see the results? | Visible outcomes, shareable results |

## Output Format

```markdown
# Diffusion Analysis: {Innovation}

## Innovation Profile
| Factor | Assessment | Implication |
|--------|-----------|------------|
| Relative advantage | H/M/L | {detail} |
| Compatibility | H/M/L | {detail} |
| Complexity | H/M/L (lower = better) | {detail} |
| Trialability | H/M/L | {detail} |
| Observability | H/M/L | {detail} |

## Current Adoption Stage
- Estimated penetration: {X%}
- Current adopter category: {Innovators / Early Adopters / Chasm / Early Majority / etc.}

## Chasm Strategy (if applicable)
- Beachhead segment: {specific niche}
- Whole product gaps: {what's missing for a complete solution}
- Reference strategy: {how to get pragmatist references}

## Adoption Acceleration Plan
1. {action to improve weakest adoption factor}
```

## Examples

### Correct Application
**Scenario:** Adoption analysis for a new AI code review tool
- **Current stage**: ~500 users, mostly developer influencers and tech leads → Early Adopters
- **Chasm risk**: High — early adopters love the AI suggestions, but engineering managers (early majority) worry about false positives and security
- **Beachhead**: Mid-size fintech companies (high code review burden, security-conscious, willing to adopt proven tools)
- **Whole product gap**: Missing SOC 2 compliance documentation, no JIRA integration, no team admin dashboard → Early majority won't adopt without these ✓

### Incorrect Application
- "We have 500 passionate users, so we're ready to go mainstream" → 500 early adopters does not mean the product is ready for pragmatists. The chasm requires a fundamentally different strategy. Violates Iron Law.

## Gotchas

- **Product-market fit for early adopters ≠ product-market fit for mainstream**: Features that excite early adopters (customizability, cutting-edge tech) may overwhelm the majority (who want simplicity and reliability).
- **The bowling pin strategy**: After winning the beachhead, expand to adjacent niches that reference the first win. Don't jump to a completely different segment.
- **Network effects accelerate diffusion**: Products with network effects (communication tools, platforms) follow steeper S-curves once they cross the tipping point.
- **Regression is possible**: Adoption can reverse (Google Glass, Segway). Sustained adoption requires ongoing value delivery.
- **B2B diffusion is slower**: Organizational adoption involves multiple decision-makers, procurement processes, and integration requirements. Plan for longer timelines.

## References

- For crossing the chasm playbook, see `references/chasm-strategy.md`

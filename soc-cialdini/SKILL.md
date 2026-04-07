---
name: "soc-cialdini"
description: "Apply Cialdini's six principles of persuasion — Reciprocity, Commitment/Consistency, Social Proof, Liking, Authority, and Scarcity — to analyze or design influence strategies. Use this skill when the user needs to make messaging more persuasive, analyze why a campaign works or doesn't, design sales or marketing copy, or understand social influence tactics — even if they say 'how do we convince people', 'why is this ad effective', or 'make this more persuasive'."
metadata:
  category: "WP-18 社會科學院"
  tags: ["social-science", "persuasion", "cialdini", "influence"]
---

# Cialdini's Six Principles of Persuasion

## Overview

Robert Cialdini identified six universal principles that drive human compliance. They work because they're cognitive shortcuts — people rely on them to make quick decisions. Understanding these principles helps design more persuasive communications AND recognize when they're being used on you.

## Framework

```
IRON LAW: Ethical Influence, Not Manipulation

These principles are tools. Using them to help people make decisions aligned
with their interests = ethical influence. Using them to exploit people against
their interests = manipulation. The test: would the person feel grateful or
deceived if they knew the technique was being used?
```

### The Six Principles

**1. Reciprocity** — People feel obligated to return favors
- Give something of value first (free sample, useful content, personal favor)
- The gift should be meaningful, unexpected, and personalized
- Application: Free trials, content marketing, "lead magnets"

**2. Commitment & Consistency** — People want to act consistently with prior commitments
- Start with small asks, then escalate (foot-in-the-door)
- Get public or written commitments
- Application: Free signup → paid conversion, loyalty programs, goal-setting

**3. Social Proof** — People follow what others do, especially similar others
- Show numbers ("10,000+ customers"), testimonials, reviews
- Most effective when the "others" are similar to the target audience
- Application: Reviews, case studies, "most popular" labels, waitlists

**4. Liking** — People say yes to those they like
- Similarity ("we're like you"), compliments, cooperation, attractiveness
- Familiarity through repeated exposure
- Application: Brand personality, influencer marketing, personalization

**5. Authority** — People defer to credible experts
- Credentials, titles, uniforms, endorsements from recognized authorities
- Must be relevant authority (a doctor endorsing medicine, not a doctor endorsing cars)
- Application: Expert endorsements, certifications, "as featured in" logos

**6. Scarcity** — People value what's limited or disappearing
- Limited quantity ("only 3 left"), limited time ("offer ends tonight"), exclusive access
- Loss framing is stronger than gain framing
- Application: Flash sales, limited editions, early access programs

### Analysis Steps

1. **Identify the persuasion context**: Who is persuading whom? What's the desired action?
2. **Audit current messaging**: Which principles are already in use? Which are missing?
3. **Recommend additions**: Which principles would be most effective for this audience and context?
4. **Check ethics**: Does each application pass the "grateful or deceived?" test?

## Output Format

```markdown
# Persuasion Analysis: {Context}

## Current State
- Persuader: {who}
- Target: {audience}
- Desired action: {what}
- Current conversion/compliance rate: {if known}

## Principle Audit
| Principle | Currently Used? | How | Effectiveness |
|-----------|----------------|-----|---------------|
| Reciprocity | Y/N | {description} | H/M/L |
| Commitment | Y/N | ... | ... |
| Social Proof | Y/N | ... | ... |
| Liking | Y/N | ... | ... |
| Authority | Y/N | ... | ... |
| Scarcity | Y/N | ... | ... |

## Recommendations
1. {Principle}: {specific implementation} — {expected impact}

## Ethics Check
{Does each recommendation pass the "grateful or deceived?" test?}
```

## Examples

### Correct Application
**Scenario:** Improving conversion on a Taiwanese SaaS landing page

| Principle | Current | Recommendation |
|-----------|---------|---------------|
| Reciprocity | ✗ | Offer a free ROI calculator tool before asking for signup |
| Social Proof | Weak ("trusted by companies") | Add specific logos + "2,347 teams use us" + testimonial with photo and company |
| Authority | ✗ | Add "Recommended by 資策會" or relevant industry certification |
| Scarcity | ✗ | "Early adopter pricing: NT$299/month (ends March 31)" |

All pass ethics check: free tool is genuinely useful, social proof is factual, authority is real certification, scarcity is a genuine time-limited offer ✓

### Incorrect Application
- "Only 2 left in stock!" when there are actually 200 → Fake scarcity. The customer would feel **deceived** if they knew. Violates Iron Law: ethical influence only.

## Gotchas

- **Stacking principles amplifies effect**: Using 3-4 principles together is more effective than any single one. A landing page with social proof + authority + scarcity outperforms one with just social proof.
- **Cultural calibration**: Authority carries more weight in hierarchical cultures (Taiwan, Japan, Korea). Social proof is powerful in collectivist cultures. Individualist cultures may respond more to scarcity and uniqueness.
- **Diminishing returns**: Overusing scarcity ("limited time!" on every email) erodes trust. Use each principle authentically and sparingly.
- **B2B vs B2C**: B2B decisions involve multiple stakeholders. Authority and social proof (case studies) are more effective than scarcity or liking.
- **Principle 7 — Unity** (Cialdini's 2016 addition): Shared identity ("we are family", "fellow alumni") creates the strongest influence. Consider for community-based contexts.

## References

- For dark patterns and manipulation detection, see `references/dark-patterns.md`
- For B2B-specific persuasion tactics, see `references/b2b-persuasion.md`

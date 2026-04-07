---
name: "ux-design-thinking"
description: "Apply Design Thinking's five stages — Empathize, Define, Ideate, Prototype, Test — to solve user-centered problems. Use this skill when the user needs to solve an ambiguous problem, redesign a user experience, facilitate an innovation workshop, or develop a new product concept from scratch — even if they say 'we don't know what to build', 'how do we innovate', or 'the users aren't happy but we're not sure why'."
metadata:
  category: "WP-21 設計/資訊/傳播/公衛"
  tags: ["design", "design-thinking", "innovation", "ux"]
---

# Design Thinking

## Overview

Design Thinking is a human-centered approach to innovation that integrates user needs, technological feasibility, and business viability. Its five stages are iterative, not linear — expect to loop back as understanding deepens.

## Framework

```
IRON LAW: Empathize BEFORE Define, Define BEFORE Ideate

Jumping to solutions (Ideate) without understanding the problem (Define)
wastes effort solving the wrong problem. Defining the problem without
empathizing with users produces internally-focused problem statements.

The sequence matters: understand the human first, then frame the problem,
then generate solutions.
```

### The Five Stages

**1. Empathize** — Understand the user's world
- Observe, interview, immerse in the user's context
- Goal: understand needs, pain points, and motivations (not just what they say, but what they do and feel)

**2. Define** — Frame the right problem
- Synthesize empathy findings into a Point of View (POV) statement:
  `[User] needs to [need] because [insight]`
- A well-defined problem is half-solved. Reframe if needed.

**3. Ideate** — Generate many solutions
- Diverge: quantity over quality. Defer judgment.
- Techniques: brainstorming, How Might We questions, SCAMPER, worst possible idea
- Then converge: vote, cluster, select 2-3 concepts to prototype

**4. Prototype** — Make ideas tangible
- Build quick, cheap, disposable prototypes to learn
- Fidelity should match the question: paper sketches for flow, clickable mocks for interaction, code for technical feasibility
- Goal: test assumptions, not impress stakeholders

**5. Test** — Learn from real users
- Put the prototype in front of real users
- Observe behavior, don't just ask opinions
- What worked? What failed? What surprised you?
- Loop back to Empathize or Define if core assumptions were wrong

## Output Format

```markdown
# Design Thinking Sprint: {Challenge}

## Empathize
- User: {who}
- Key insights from research: ...
- Surprises: ...

## Define
- POV: [User] needs to [need] because [insight]
- How Might We: {3-5 HMW questions}

## Ideate
- Ideas generated: {count}
- Top 3 concepts: ...

## Prototype
- Prototype type: {paper / digital / physical}
- What it tests: {specific assumption}

## Test
- User feedback: ...
- Validated: {what was confirmed}
- Invalidated: {what was wrong}
- Next iteration: {what to change}
```

## Examples

### Correct Application
**Scenario:** Redesigning hospital waiting room experience
- **Empathize**: Observed patients for 3 days. Key insight: anxiety peaks not from wait time but from UNCERTAINTY about wait time.
- **Define**: "Patients need to feel informed about their wait status because uncertainty amplifies anxiety beyond what the actual wait causes."
- **Ideate**: 40+ ideas → top 3: real-time queue display, SMS position updates, estimated-time kiosk
- **Prototype**: Paper prototype of SMS update flow (5 min to build)
- **Test**: 8 patients tested → 6 reported feeling "much less anxious" even though actual wait didn't change ✓

### Incorrect Application
- Skipped Empathize, started with "we need a new app feature" → Solutioning without understanding the problem. Violates Iron Law.

## Gotchas

- **"Fail fast" requires psychological safety**: Teams won't experiment if failure is punished. Establish that prototypes are meant to fail — that's learning.
- **HMW questions set the solution space**: "How might we reduce wait time?" leads to different solutions than "How might we reduce anxiety during waits?" Frame carefully.
- **Prototype ≠ MVP**: A prototype tests a hypothesis cheaply. An MVP is a viable product. Don't over-build prototypes.
- **Design Thinking is not just for designers**: It applies to services, processes, policies, business models — any problem involving human needs.
- **Iteration is not optional**: If you run through all 5 stages once without looping back, you've done waterfall with sticky notes, not Design Thinking.

## References

- For facilitation exercises per stage, see `references/dt-exercises.md`

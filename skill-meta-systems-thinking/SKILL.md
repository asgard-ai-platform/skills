---
name: "skill-meta-systems-thinking"
description: "Apply systems thinking to analyze complex problems through feedback loops, emergence, and interconnections. Use this skill when the user faces a problem where cause and effect are separated in time or space, when fixing one thing breaks another, or when linear thinking fails — even if they say 'everything is connected', 'why does fixing this make it worse', 'unintended consequences', or 'this problem keeps coming back'."
metadata:
  category: "WP-22 跨學科"
  tags: ["meta-thinking", "systems-thinking", "complexity"]
---

# Systems Thinking

## Framework

```
IRON LAW: The Whole Is Not the Sum of Its Parts

You cannot understand a system by analyzing its components in isolation.
The behavior of the system emerges from the INTERACTIONS between components,
not from the components themselves. Optimizing each department independently
can make the overall organization worse.
```

### Core Concepts

**Feedback loops**: Cause A → Effect B → feeds back to influence A
- **Reinforcing (positive)**: Amplifies change. Success → more resources → more success (or failure → fewer resources → more failure). Creates exponential growth or collapse.
- **Balancing (negative)**: Resists change, seeks equilibrium. Thermostat: too hot → AC on → temperature drops → AC off.

**Emergence**: System-level properties that don't exist in individual components. Traffic jams emerge from individual driving behaviors. Culture emerges from individual interactions.

**Delays**: Effects don't appear immediately. Investing in training today improves performance months later. Ignoring maintenance today causes breakdowns months later. Delays make cause-and-effect hard to connect.

**Leverage points**: Places where a small change produces large effects. Changing system rules, incentives, or information flows often has more impact than pushing harder on symptoms.

### Analysis Steps

1. **Define the system boundary**: What's in, what's out?
2. **Map key variables**: What are the important stocks (quantities that accumulate)?
3. **Identify feedback loops**: Which loops are reinforcing? Which are balancing?
4. **Find delays**: Where is cause separated from effect in time?
5. **Locate leverage points**: Where would small interventions produce the biggest shift?
6. **Check for unintended consequences**: What might this intervention break elsewhere in the system?

## Output Format

```markdown
# Systems Analysis: {Problem}

## System Boundary
- In scope: ...
- Out of scope: ...

## Key Variables
- {Variable A}: {description}

## Feedback Loops
- Reinforcing: {A → B → A (amplifying)}
- Balancing: {A → B → C → opposes A (stabilizing)}

## Delays
- {Input} → {Effect} (delay: {timeframe})

## Leverage Points
1. {where small change = big impact}

## Unintended Consequences Risk
- If we {intervention}, it might also {side effect} because {loop/connection}
```

## Examples

### Correct Application
**Scenario:** Why does hiring more engineers not speed up the project?

**Reinforcing loop (intended)**: More engineers → more code → faster progress
**Balancing loop (unintended)**: More engineers → more communication overhead → more meetings → less coding time → slower progress (Brooks' Law)
**Delay**: New engineers need 3-6 months to become productive

**Leverage point**: Instead of adding people, reduce communication overhead (smaller teams, clearer ownership, better documentation) ✓

### Incorrect Application
- "Revenue is down. Increase marketing spend." → Linear, single-cause thinking. Ignoring: Why is revenue down? Is it demand (balancing loop from saturation)? Is it churn (reinforcing loop of poor quality → complaints → more churn)? Different root causes require different interventions.

## Gotchas

- **Systems resist change**: Balancing feedback loops maintain the status quo. Pushing against them without addressing the loop structure leads to "fixes that fail."
- **Mental models are partial**: Everyone's mental model of a system is incomplete. Mapping the system with diverse stakeholders reveals blind spots.
- **Unintended consequences are the norm, not the exception**: In complex systems, interventions always produce side effects. The question is whether you've identified the important ones.
- **Not everything is a system**: Simple problems with clear cause-and-effect don't need systems thinking. Use it for problems where linear thinking fails.

## References

- For system archetypes (Limits to Growth, Shifting the Burden, etc.), see `references/system-archetypes.md`

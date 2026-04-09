---
name: "meta-systems-thinking"
description: "Apply systems thinking — causal loop diagrams, stock-and-flow models, system archetypes, and leverage-point analysis — to organizational, economic, or social problems where feedback loops, delays, or emergent behavior drive recurring failure across multiple interacting actors. Use this skill when the user describes a multi-actor situation that resists linear fixes: policy interventions that backfire, org-level fixes that break other teams, market symptoms that return after being solved, or time-lagged second-order consequences, even if they say 'why does fixing X make Y worse' or 'identify the leverage points in this system'. Do NOT use for single-cause software bugs, flaky tests, or regressions — those are debugging problems, not systems-thinking problems, even when phrased as 'this keeps coming back'."
metadata:
  category: "WP-22 跨學科"
  tags: ["meta-thinking", "systems-thinking", "complexity"]
---

# Systems Thinking

## Framework

```
IRON LAW: First-Order Fixes in Complex Systems Produce Second-Order
Backlash Within 2 Cycles — Map the Feedback Loop BEFORE Intervening

Agents default to "fix the symptom directly" (e.g., high turnover → raise
salaries). In systems with feedback loops, the direct fix triggers a
compensating response that makes the original problem worse OR creates
a new one (raise salaries → budget squeeze → cut training → worse
onboarding → higher turnover). Before recommending any intervention,
draw the causal loop diagram and identify at least one reinforcing and
one balancing loop. If you can't find any, the problem may not be a
systems problem — don't force the framework.
```

### Analysis Steps

Key concepts assumed known: feedback loops (reinforcing/balancing), emergence,
delays, leverage points, stocks and flows. For system archetypes (Fixes That
Fail, Shifting the Burden, Limits to Growth, etc.) see
[`references/system-archetypes.md`](references/system-archetypes.md).

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

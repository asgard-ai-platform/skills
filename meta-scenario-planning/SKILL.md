---
name: "meta-scenario-planning"
description: "Conduct scenario planning to prepare for multiple plausible futures using driving forces, uncertainty axes, and the 2x2 scenario matrix. Use this skill when the user faces high uncertainty, needs to stress-test a strategy against different futures, or prepare contingency plans — even if they say 'what if things go wrong', 'what could the future look like', 'how do we prepare for uncertainty', or 'stress-test our strategy'."
metadata:
  category: "WP-22 跨學科"
  tags: ["meta-thinking", "scenario-planning", "strategy", "uncertainty"]
---

# Scenario Planning

## Framework

```
IRON LAW: Scenarios Are Not Predictions

Scenarios are PLAUSIBLE futures, not forecasts. The goal is NOT to predict
which future will happen, but to prepare strategies that work across
MULTIPLE possible futures. A strategy that only works in one scenario
is fragile.
```

### The 2×2 Scenario Matrix Method

1. **Identify driving forces**: What macro-forces will most shape the future? (technology, regulation, economy, demographics, competition)
2. **Select two critical uncertainties**: The two most impactful forces with the most uncertain outcomes
3. **Build the 2×2 matrix**: Each axis is one uncertainty with two endpoints (e.g., "regulation: strict vs lax")
4. **Name and describe four scenarios**: Each quadrant is a distinct plausible future
5. **Test strategies against all four**: Which strategies work in most/all scenarios? Which only work in one?

### Process

**Step 1: Driving Forces (brainstorm 10-15)**
- Political, economic, social, technological, environmental, competitive
- Rate each on: Impact (H/M/L) × Uncertainty (H/M/L)
- High Impact + High Uncertainty → candidate for axes

**Step 2: Select Two Axes**
- Choose two forces that are both high-impact AND high-uncertainty
- They should be independent of each other (not correlated)

**Step 3: Build Four Scenarios**
- Give each scenario a memorable name (not "Scenario 1")
- Write a 1-paragraph narrative for each: what does this world look like in 5-10 years?

**Step 4: Strategy Testing**
- For each strategy option, assess: does it work in this scenario? (Yes / Partial / No)
- Robust strategies work in 3-4 scenarios. Fragile strategies work in only 1.

## Output Format

```markdown
# Scenario Planning: {Context}

## Driving Forces
| Force | Impact | Uncertainty | Selected? |
|-------|--------|------------|-----------|
| {force} | H/M/L | H/M/L | ✓/— |

## Scenario Matrix
- Axis 1: {Uncertainty A} — {endpoint 1} vs {endpoint 2}
- Axis 2: {Uncertainty B} — {endpoint 1} vs {endpoint 2}

| | {A: endpoint 1} | {A: endpoint 2} |
|---|---|---|
| **{B: endpoint 1}** | **"{Scenario Name}"**: {narrative} | **"{Scenario Name}"**: {narrative} |
| **{B: endpoint 2}** | **"{Scenario Name}"**: {narrative} | **"{Scenario Name}"**: {narrative} |

## Strategy Robustness Test
| Strategy | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 |
|----------|-----------|-----------|-----------|-----------|
| {strategy A} | ✓/△/✗ | ✓/△/✗ | ✓/△/✗ | ✓/△/✗ |

## Robust Strategies
{Strategies that work in most scenarios}

## Contingency Triggers
- If {early signal}, activate {contingency plan for scenario X}
```

## Gotchas

- **Scenarios should be uncomfortable**: If all four scenarios are comfortable, you haven't explored enough uncertainty. Include at least one scenario you'd rather not think about.
- **Avoid "good/bad" framing**: Scenarios aren't optimistic vs pessimistic. Each scenario has opportunities AND threats. A "strict regulation" world is bad for some and good for others.
- **Early warning signals**: Identify observable indicators that signal which scenario is unfolding. This converts scenarios into actionable intelligence.
- **Two axes is a simplification**: Reality has many uncertainties. The 2×2 is a tool for clarity, not completeness. Consider additional driving forces as variations within scenarios.

## References

- For Shell's original scenario planning methodology, see `references/shell-method.md`

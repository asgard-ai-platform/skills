---
name: "meta-structured-problem"
description: "Apply structured problem-solving using MECE principle, issue trees, hypothesis-driven approach, and the Pyramid Principle. Use this skill when the user faces a complex, ambiguous problem and needs to decompose it systematically, structure a consulting-style analysis, or organize recommendations clearly — even if they say 'where do I start', 'this problem is too big', 'help me break this down', or 'structure my thinking'."
metadata:
  category: "WP-22 跨學科"
  tags: ["meta-thinking", "structured-problem-solving", "mece", "mckinsey"]
---

# Structured Problem Solving

## Framework

```
IRON LAW: MECE or It's Not Structured

Every decomposition must be MECE:
- Mutually Exclusive: No overlap between categories
- Collectively Exhaustive: No gaps — all possibilities covered

"Revenue = New customers + Existing customers" is MECE ✓
"Revenue = Online + Enterprise + Growth" is NOT MECE ✗ (overlapping)
```

### Core Tools

**Issue Tree**: Decompose a question into sub-questions, MECE at each level
```
"Why is profit declining?"
├── Revenue declining?
│   ├── Volume down?
│   │   ├── New customer acquisition down?
│   │   └── Existing customer churn up?
│   └── Price down?
│       ├── Discounting increased?
│       └── Mix shift to lower-priced products?
└── Costs increasing?
    ├── COGS up?
    └── OpEx up?
```

**Hypothesis-Driven Approach**: Instead of exploring everything, state a hypothesis and test it
1. Form an initial hypothesis ("Profit declined because churn increased")
2. Identify what evidence would prove/disprove it
3. Gather that specific evidence
4. Refine or reject the hypothesis
5. Repeat

**Pyramid Principle** (Barbara Minto): Structure communication top-down
1. **Lead with the answer**: Start with the recommendation, not the analysis
2. **Group supporting arguments**: 3-5 supporting points, MECE
3. **Order logically**: By argument strength, chronologically, or structurally
4. **Detail only when asked**: Each level provides more detail for those who want it

**80/20 Rule**: Focus on the 20% of analysis that drives 80% of the answer. Don't over-analyze secondary branches of the issue tree.

### Problem Solving Process

1. **Define the problem**: "The client's profit has declined 15% YoY. Why, and what should they do?"
2. **Structure with an issue tree**: MECE decomposition of possible causes
3. **Prioritize branches**: Which branches are most likely to contain the answer? (80/20)
4. **Form hypotheses**: "I believe the primary cause is..."
5. **Gather evidence**: Test each hypothesis with data
6. **Synthesize findings**: What does the evidence say?
7. **Recommend**: Present using the Pyramid Principle (answer first)

## Output Format

```markdown
# Structured Analysis: {Problem}

## Problem Statement
{One sentence, specific and measurable}

## Issue Tree
{MECE decomposition — text or visual}

## Hypothesis
{Initial hypothesis with rationale}

## Evidence
| Branch | Hypothesis | Evidence | Verdict |
|--------|-----------|---------|---------|
| {branch} | {sub-hypothesis} | {data found} | Confirmed/Rejected |

## Synthesis (Pyramid Structure)
**Recommendation**: {answer first}

**Supporting Arguments**:
1. {argument 1 with evidence}
2. {argument 2 with evidence}
3. {argument 3 with evidence}

## Next Steps
1. {action item}
```

## Examples

### Correct Application
**Scenario:** "Why is our food delivery app losing market share?"

Issue tree (MECE):
```
Market share declining
├── Our growth slowing?
│   ├── New user acquisition down?
│   │   ├── Marketing spend reduced?
│   │   └── Conversion rate dropped?
│   └── Existing user activity down?
│       ├── Order frequency declining?
│       └── Users churning?
└── Competitors growing faster?
    ├── New entrant capturing share?
    └── Existing competitor accelerating?
```

Hypothesis: "Existing user activity is down because order frequency declined after the delivery fee increase."
Evidence: Order frequency dropped 22% in the month after fee increase. ✓

Pyramid: "Reverse the delivery fee increase for high-frequency users. Order frequency dropped 22% post-increase, and 60% of lost orders came from users who ordered 3+/week. A loyalty tier with waived fees for frequent users would recover an estimated 15% of lost share at a cost of NT$X/month."

### Incorrect Application
- Issue tree: "Revenue problem: Online, Marketing, Customer Service" → Not MECE (overlapping categories, not exhaustive). Violates Iron Law.

## Gotchas

- **MECE is hard in practice**: Perfect MECE is aspirational. Get as close as possible and note where categories blur. "Good enough MECE" beats "perfect but took 3 days."
- **Hypothesis-driven ≠ confirmation bias**: The hypothesis is a starting point to guide investigation, not a conclusion to defend. If evidence contradicts it, change the hypothesis.
- **The Pyramid Principle feels counterintuitive**: People naturally want to tell the story chronologically (problem → analysis → conclusion). Audiences want the answer FIRST, then the supporting evidence. Lead with the recommendation.
- **Structured ≠ slow**: Spending 30 minutes structuring the problem saves hours of unfocused analysis. The structure IS the speed.
- **Know when to stop**: Analysis has diminishing returns. If you have enough evidence to make a confident recommendation, stop analyzing and recommend.

## References

- For issue tree templates by problem type, see `references/issue-tree-templates.md`
- For Pyramid Principle writing guide, see `references/pyramid-principle.md`

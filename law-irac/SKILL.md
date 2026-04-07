---
name: "law-irac"
description: "Apply IRAC (Issue, Rule, Application, Conclusion) method for structured legal analysis. Use this skill when the user needs to analyze a legal question systematically, write a legal memo, evaluate whether a law applies to a situation, or structure a legal argument — even if they say 'does this law apply', 'analyze this legal issue', or 'write a legal analysis'."
metadata:
  category: "WP-20 法學院"
  tags: ["law", "irac", "legal-reasoning"]
---

# IRAC Legal Analysis Method

## Overview

IRAC is the standard method for structured legal reasoning: identify the legal Issue, state the applicable Rule, Apply the rule to the facts, and reach a Conclusion. It ensures analysis is systematic, complete, and logically rigorous.

## Framework

```
IRON LAW: Issue First, Conclusion Last

NEVER state the conclusion before completing the analysis. IRAC works
BECAUSE it forces you to examine rules and apply them to facts before
reaching a conclusion. Starting with the conclusion and backfilling
the analysis is confirmation bias dressed in legal structure.
```

### The Four Steps

**I — Issue**: Frame the specific legal question
- State as a question: "Whether [specific legal question] given [key facts]"
- Be precise — a vague issue leads to vague analysis
- There may be multiple issues; address each separately

**R — Rule**: State the applicable law
- Statute, regulation, case law, or legal principle
- Include the specific elements/requirements of the rule
- If the rule has a test (e.g., 4-factor test for fair use), state all factors

**A — Application**: Apply the rule to the specific facts
- This is the core analytical work — match each element of the rule to the facts
- Address each element/factor separately
- Acknowledge ambiguity — where facts are unclear, note both possible interpretations
- Use analogies to precedent cases where available

**C — Conclusion**: State the result
- Answer the issue question directly
- State the degree of confidence (clear, likely, arguable, unclear)
- Note assumptions that the conclusion depends on

## Output Format

```markdown
# Legal Analysis: {Topic}

## Issue
Whether [legal question] given [key facts].

## Rule
[Applicable law/principle with specific elements]

## Application
### Element 1: [name]
[Analysis of how facts satisfy or fail this element]

### Element 2: [name]
[Analysis...]

## Conclusion
[Direct answer to the issue with confidence level]
```

## Examples

### Correct Application
**Scenario:** Does an employee's social media post constitute grounds for termination under Taiwan's Labor Standards Act?

**Issue**: Whether an employee's Facebook post criticizing company management constitutes a violation of the employment contract sufficient for termination under Article 12 of the Labor Standards Act.

**Rule**: Article 12, Subparagraph 4 of the LSA permits termination without notice when an employee "commits a serious breach of the employment contract or violates work rules to a serious degree." Courts apply a proportionality test: the breach must be so severe that the employment relationship cannot reasonably continue.

**Application**: The post criticized management's decision to cut overtime pay, using strong language but no false statements. Courts have held that employee speech on matters of working conditions receives higher protection. The proportionality test likely fails — criticism of company policy, even if intemperate, is generally not severe enough to justify termination unless it reveals confidential information or constitutes defamation.

**Conclusion**: Likely not grounds for lawful termination. Confidence: Moderate — depends on specific language used and whether any confidential information was disclosed ✓

### Incorrect Application
- "The employee posted something bad on Facebook, so they should be fired. Here's why..." → Conclusion first, then backfilling analysis. Violates Iron Law: issue first, conclusion last.

## Gotchas

- **Multiple issues require separate IRAC analyses**: Don't combine three legal questions into one analysis. Each issue gets its own I-R-A-C.
- **Rule statement must be specific**: "The law says you can't do that" is not a rule statement. Cite the specific statute, article, or legal principle with its elements.
- **Application is where the work is**: Students and practitioners spend too little time on Application and too much on Rule. The rule is usually clear — how it applies to ambiguous facts is the challenge.
- **Counter-arguments strengthen analysis**: Address the strongest counter-argument in the Application section. One-sided analysis is weak analysis.
- **This is educational methodology, not legal advice**: IRAC is a reasoning framework. Actual legal conclusions require a licensed attorney with jurisdiction-specific expertise.

## References

- For Taiwan legal research resources, see `references/taiwan-legal-resources.md`

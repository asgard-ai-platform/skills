---
name: "grad-blooms"
description: "Apply Bloom's revised taxonomy to classify learning objectives and design assessments across six cognitive levels. Use this skill when the user needs to write learning objectives at specific cognitive levels, align assessment with instructional goals, or evaluate curriculum for cognitive complexity distribution — even if they say 'how to write learning objectives', 'what level of thinking does this require', or 'higher-order thinking skills'."
metadata:
  category: "WP-33 傳播/教育/公共行政"
  tags: ["education", "blooms-taxonomy", "learning-objectives", "assessment"]
---

# Bloom's Revised Taxonomy

## Overview

Bloom's revised taxonomy (Anderson & Krathwohl, 2001) classifies cognitive processes into six hierarchical levels: Remember, Understand, Apply, Analyze, Evaluate, and Create. Combined with the knowledge dimension (factual, conceptual, procedural, metacognitive), it provides a two-dimensional framework for designing and assessing learning.

## When to Use

**Trigger conditions:**
- Writing learning objectives at specific cognitive levels
- Aligning assessment methods with intended learning outcomes
- Auditing curriculum for cognitive complexity balance

**When NOT to use:**
- When designing scaffolded learning experiences (use constructivism / ZPD)
- When managing cognitive load in instructional design (use cognitive load theory)
- When integrating technology into teaching (use TPACK framework)

## Assumptions

```
IRON LAW: Higher-Order Thinking REQUIRES a Foundation of Lower-Order Knowledge

You cannot analyze what you don't understand. You cannot evaluate
what you haven't analyzed. You cannot create without evaluation criteria.
The hierarchy is:
  Remember → Understand → Apply → Analyze → Evaluate → Create
Skipping levels produces superficial "higher-order" work built on
a weak knowledge foundation.
```

## Methodology

### Step 1: Identify Knowledge Type
Classify the target knowledge: factual (terminology, details), conceptual (categories, principles), procedural (how-to, techniques), or metacognitive (self-awareness, strategies).

### Step 2: Select Cognitive Level
Choose the appropriate cognitive process level. Use action verbs that are observable and measurable for each level.

### Step 3: Write Objectives
Combine: "Students will be able to [action verb] [knowledge content] [context/condition]." Ensure the verb matches the intended cognitive level.

### Step 4: Align Assessment
Match assessment methods to the cognitive level. Remember/Understand → objective tests. Apply/Analyze → case studies, problem sets. Evaluate/Create → projects, portfolios, essays.

## Output Format

```markdown
# Learning Objectives Analysis: {Course/Module}

## Taxonomy Mapping
| Objective | Cognitive Level | Knowledge Type | Action Verb | Assessment Method |
|-----------|----------------|---------------|-------------|-------------------|
| ... | Remember/Understand/Apply/Analyze/Evaluate/Create | Factual/Conceptual/Procedural/Metacognitive | ... | ... |

## Cognitive Level Distribution
- Lower-order (Remember, Understand, Apply): {count, %}
- Higher-order (Analyze, Evaluate, Create): {count, %}
- Balance assessment: {adequate or needs adjustment}

## Alignment Check
- Objectives ↔ Instruction: {aligned / gaps}
- Objectives ↔ Assessment: {aligned / gaps}

## Recommendations
{Specific suggestions for improving cognitive level balance and alignment}
```

## Gotchas

- **Verbs are ambiguous**: "Understand" is not directly observable. Use specific verbs: "explain," "classify," "summarize." Multiple taxonomies map verbs to levels — they don't always agree.
- **Hierarchy is not rigid**: The revised taxonomy acknowledges that the order between Evaluate and Create can vary. Some creative tasks don't require prior evaluation, and some evaluation doesn't require creation.
- **Higher ≠ better**: Not all objectives should be at the Create level. Foundational courses legitimately emphasize Remember and Understand. The goal is APPROPRIATE level, not maximum level.
- **Culture of verb-matching**: Swapping in a "higher" verb without changing the actual cognitive demand is cosmetic. "Analyze the definition" is still Remember if students just recite a memorized analysis.
- **Affective and psychomotor domains**: Bloom's cognitive taxonomy is one of THREE domains. It doesn't address attitudes/values (affective) or physical skills (psychomotor).

## References

- For the complete verb list by level, see `references/verb-taxonomy.md`
- For alignment matrices and assessment design, see `references/alignment-matrix.md`

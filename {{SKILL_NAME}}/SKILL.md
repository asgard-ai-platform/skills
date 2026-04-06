---
name: "{{SKILL_NAME}}"
description: "{{SKILL_DESCRIPTION}}"
# Optional fields (uncomment as needed):
# license: "MIT"
# compatibility: ""
# allowed-tools: []
# metadata:
#   author: "{{AUTHOR}}"
#   version: "1.0.0"
#   category: ""
#   tags: []
---

<!--
DESCRIPTION WRITING GUIDE (delete this block when done):

The `description` field determines whether agents trigger this skill.
  1. Include WHAT it does + WHEN to use it
  2. Use imperative tone: "Use this skill when..."
  3. Focus on user intent, not implementation details
  4. Include trigger phrases the user might say
  5. < 1024 characters, NO XML angle brackets (< >)

Example:
  description: "Performs RFM (Recency, Frequency, Monetary) customer
    segmentation analysis. Use this skill when the user needs to segment
    customers, identify high-value buyers, or analyze purchase behavior
    from transaction data."
-->

<!-- TARGET: < 500 lines, < 5,000 tokens. Add what the agent lacks, omit what it knows. -->

# {{SKILL_DISPLAY_NAME}}

## Overview

<!-- What it is, when to use it, and what problem it solves. -->

{{Description of the methodology/theory/algorithm.}}

---

## When to Use

**Trigger conditions:**
- {{Describe situations where this SKILL should be activated}}

**Input signals:**
- {{What kind of data or questions indicate this SKILL is relevant}}

---

## Methodology

<!-- Write procedures, not declarations. Tell the agent what to DO, step by step.
     Provide sensible defaults — don't present menus of options. -->

### Step 1: {{Step Name}}

{{Detailed instructions for the AI to follow.}}

### Step 2: {{Step Name}}

{{Detailed instructions for the AI to follow.}}

### Step 3: {{Step Name}}

{{Detailed instructions for the AI to follow.}}

<!-- Add more steps as needed -->

---

## Output Format

<!-- Define the expected output structure -->

```json
{
  "analysis": "{{description of the output shape}}"
}
```

---

## Examples

### Good Example

**Scenario:** {{Describe the scenario}}

**Analysis:**
{{A concrete example of correct application with explanation.}}

### Bad Example

**Scenario:** {{Describe the scenario}}

**What went wrong:**
{{A concrete example of incorrect application with explanation of what went wrong.}}

---

## Gotchas

<!-- Highest-value section: non-obvious facts the agent would get wrong without this skill.
     Keep these in SKILL.md so the agent sees them before encountering the situation. -->

- {{Common mistake or non-obvious behavior}}
- {{Edge case that produces unexpected results}}
- {{Default assumption that may surprise users}}

---

## Scripts

<!-- Remove this section entirely if this skill has no scripts -->

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/{{name}}.py` | {{What it does}} | `python {{name}}.py --help` |

---

## References

<!-- For heavy reference content (long guides, papers, API docs), put files in references/
     and point to them here. This keeps SKILL.md body under token budget. -->

- [{{Source name}}]({{URL}}) — {{Brief description}}
- Related SKILLs: `{{related-skill-1}}`, `{{related-skill-2}}`

---

## Limitations

- {{Known constraint or edge case}}
- {{Scenario where this SKILL should NOT be used}}

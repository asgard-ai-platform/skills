---
name: "{{SKILL_NAME}}"
description: "{{SKILL_DESCRIPTION}}"
---

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

## Scripts

<!-- Remove this section entirely if this skill has no scripts -->

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/{{name}}.py` | {{What it does}} | `python {{name}}.py --help` |

---

## References

- [{{Source name}}]({{URL}}) — {{Brief description}}
- Related SKILLs: `{{related-skill-1}}`, `{{related-skill-2}}`

---

## Limitations

- {{Known constraint or edge case}}
- {{Scenario where this SKILL should NOT be used}}

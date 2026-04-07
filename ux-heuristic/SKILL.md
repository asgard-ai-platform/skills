---
name: "ux-heuristic"
description: "Conduct heuristic evaluation of user interfaces using Nielsen's 10 usability principles. Use this skill when the user needs to audit a website, app, or interface for usability issues, prioritize UX improvements, or conduct a quick expert review without user testing — even if they say 'review this UI', 'find usability problems', or 'why do users struggle with our app'."
metadata:
  category: "WP-21 設計/資訊/傳播/公衛"
  tags: ["ux", "heuristic-evaluation", "usability", "nielsen"]
---

# Heuristic Evaluation (Nielsen's 10 Principles)

## Overview

Heuristic evaluation is an expert review method that assesses a user interface against established usability principles. It's fast (2-4 hours), cheap (no user recruitment), and finds 40-60% of usability issues. Use it as a complement to, not replacement for, user testing.

## Framework

```
IRON LAW: Every Violation Gets a Severity Rating

Finding a violation is half the work. Rating its severity is the other half.
A cosmetic inconsistency and a critical workflow blocker are both "violations"
but require completely different response urgency.

0 = Not a usability problem
1 = Cosmetic only — fix if time permits
2 = Minor — low priority
3 = Major — important to fix, high priority
4 = Catastrophe — must fix before release
```

### Nielsen's 10 Heuristics

| # | Heuristic | Question to Ask |
|---|-----------|----------------|
| 1 | **Visibility of system status** | Does the user always know what's happening? (loading indicators, progress bars, confirmations) |
| 2 | **Match between system and real world** | Does it use the user's language, not system jargon? Are conventions familiar? |
| 3 | **User control and freedom** | Can users undo, redo, go back, cancel? Is there an emergency exit? |
| 4 | **Consistency and standards** | Are the same actions/words used consistently? Does it follow platform conventions? |
| 5 | **Error prevention** | Does the design prevent errors before they happen? (confirmations, constraints, defaults) |
| 6 | **Recognition rather than recall** | Are options visible? Can users recognize rather than remember? |
| 7 | **Flexibility and efficiency of use** | Are there shortcuts for experts? Can users customize frequent actions? |
| 8 | **Aesthetic and minimalist design** | Is every element necessary? Does extra information compete with relevant info? |
| 9 | **Help users recognize, diagnose, and recover from errors** | Are error messages helpful? Do they explain what went wrong and how to fix it? |
| 10 | **Help and documentation** | Is help available? Is it searchable, task-oriented, and concise? |

### Evaluation Process

1. **Define scope**: Which screens/flows to evaluate
2. **Walk through** the interface 2-3 times with different user tasks
3. **Flag violations**: Note each violation with heuristic #, location, description
4. **Rate severity**: 0-4 scale for each violation
5. **Prioritize**: Fix severity 4 and 3 first
6. **Report**: Organize findings by severity, not by heuristic number

## Output Format

```markdown
# Heuristic Evaluation: {Product/Feature}

## Summary
- Total violations found: {N}
- Severity 4 (catastrophe): {N}
- Severity 3 (major): {N}
- Severity 2 (minor): {N}
- Severity 1 (cosmetic): {N}

## Critical Issues (Severity 3-4)
| # | Location | Heuristic | Issue | Severity | Recommendation |
|---|----------|-----------|-------|----------|---------------|
| 1 | {screen/element} | {#N: name} | {description} | 3/4 | {fix} |

## Other Issues (Severity 1-2)
| # | Location | Heuristic | Issue | Severity |
|---|----------|-----------|-------|----------|
| ... | ... | ... | ... | ... |
```

## Examples

### Correct Application
**Scenario:** Evaluating a food delivery app checkout flow

| Location | Heuristic | Issue | Severity |
|----------|-----------|-------|----------|
| Cart page | #1 Visibility | No loading indicator when adding items — user taps multiple times | 3 |
| Payment | #5 Error prevention | No confirmation before placing order — accidental orders happen | 4 |
| Error screen | #9 Error recovery | "Error 500" with no explanation or retry button | 4 |
| Address form | #6 Recognition | User must type full address instead of selecting from saved addresses | 2 |

Priority: Fix #5 and #9 immediately (severity 4) ✓

### Incorrect Application
- "The app looks ugly" → Not a heuristic violation. "Aesthetic and minimalist design" (#8) is about information hierarchy, not visual attractiveness. A specific violation would be: "Product page shows 15 data fields simultaneously, burying the price and 'Add to Cart' button."

## Gotchas

- **3-5 evaluators find 75% of issues**: One evaluator finds ~35%. Diminishing returns after 5. If possible, have multiple evaluators work independently then merge findings.
- **Heuristic evaluation finds problems, not solutions**: It tells you what's wrong, not how to fix it. Solution design is a separate step.
- **Not a substitute for user testing**: Experts predict user behavior imperfectly. Some "violations" that experts flag don't bother real users, and some real problems experts miss.
- **Mobile vs desktop**: Apply heuristics separately for each platform. Touch targets, screen real estate, and interaction patterns differ significantly.
- **Accessibility is not a heuristic**: Nielsen's 10 don't explicitly cover accessibility (color contrast, screen reader support, keyboard navigation). Add WCAG checks separately.

## References

- For WCAG accessibility checklist, see `references/wcag-checklist.md`

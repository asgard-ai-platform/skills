---
name: "algo-hr-matching"
description: "Implement Gale-Shapley stable matching algorithm for two-sided matching problems. Use this skill when the user needs to match candidates to positions, assign students to schools, or solve any two-sided preference matching — even if they say 'optimal job matching', 'stable assignment', or 'candidate-position pairing'."
metadata:
  category: "WP-42 HR 演算法"
  tags: ["hr", "stable-matching", "gale-shapley", "assignment"]
---

# Gale-Shapley Stable Matching

## Overview

Gale-Shapley (deferred acceptance) finds a stable matching between two equally-sized sets where no unmatched pair prefers each other over their current match. Runs in O(n²) worst case. Proposer-optimal: the proposing side gets their best stable partner.

## When to Use

**Trigger conditions:**
- Matching candidates to job positions based on mutual preferences
- Assigning students to schools or residents to hospitals
- Any two-sided matching where stability (no blocking pairs) is required

**When NOT to use:**
- For one-sided assignment (use Hungarian algorithm)
- When preferences are based on scores, not rankings (use optimization)

## Algorithm

```
IRON LAW: The Proposing Side Gets Their BEST Stable Partner
Gale-Shapley is proposer-optimal and reviewer-pessimal. If employers
propose, they get their best stable match; candidates get their worst.
The CHOICE of who proposes determines which stable matching is found.
```

### Phase 1: Input Validation
Collect: preference rankings from both sides. Each participant ranks all members of the other side.
**Gate:** Complete preference lists, equal-sized groups (or handle unequal with dummy entries).

### Phase 2: Core Algorithm
1. All proposers are "free" (unmatched)
2. While any proposer is free and hasn't proposed to everyone:
   - Free proposer proposes to their highest-ranked unproposed-to reviewer
   - Reviewer accepts if unmatched, or replaces current match if new proposer is preferred
   - Replaced proposer becomes free again
3. Terminate when all proposers are matched

### Phase 3: Verification
Check stability: for every unmatched pair (a,b), verify that at least one of them prefers their current match over the other. No blocking pairs = stable.
**Gate:** Zero blocking pairs found.

### Phase 4: Output
Return matching with stability confirmation.

## Output Format

```json
{
  "matching": [{"proposer": "Candidate_A", "reviewer": "Company_X", "proposer_rank": 1, "reviewer_rank": 2}],
  "metadata": {"pairs": 10, "rounds": 23, "blocking_pairs": 0, "proposer_side": "candidates"}
}
```

## Examples

### Sample I/O
**Input:** 3 candidates, 3 companies, each with full preference rankings
**Expected:** Stable matching with zero blocking pairs. Candidate-proposing gives candidate-optimal result.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| All prefer same #1 | Still terminates, stable | Rejected proposers move to next choice |
| Identical preferences | Unique stable matching | Only one possibility |
| Unequal sides | Some unmatched on larger side | Add dummy entries or use many-to-one variant |

## Gotchas

- **Proposer advantage**: If candidates propose, they get better matches than if companies propose. This is a design choice with equity implications.
- **Incomplete preferences**: If participants don't rank everyone, unmatched results are possible. Handle with acceptable-partner thresholds.
- **Many-to-one**: Hospital-resident matching uses the many-to-one variant (each hospital has multiple slots). Use the Roth-Peranson extension.
- **Strategic manipulation**: The reviewing side CAN benefit from misreporting preferences (truncating lists). The proposing side cannot — truthful reporting is dominant strategy for proposers.
- **Preference elicitation**: Getting honest, complete rankings is hard in practice. People satisfice rather than fully rank all options.

## References

- For many-to-one matching (hospital-resident), see `references/many-to-one.md`
- For strategic behavior analysis, see `references/strategic-manipulation.md`

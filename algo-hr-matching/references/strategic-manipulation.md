# Strategic Manipulation in Gale-Shapley

## The Core Asymmetry

Gale-Shapley has a fundamental, proven asymmetry in strategic vulnerability:

| Side | Can they benefit from misreporting? | Dominant strategy |
|------|--------------------------------------|-------------------|
| Proposers | **No** | Report true preferences |
| Reviewers | **Yes** | Truncation can improve outcome |

This is not a heuristic — it is a theorem. Dubins & Freedman (1981) and Roth (1982) proved both directions.

**Implication for HR systems**: If candidates propose (which is typical in job markets), candidates have no incentive to game the system. But if you are an employer (reviewer), you might benefit from strategically limiting your stated acceptable-partner list.

---

## Why Proposers Cannot Manipulate

### The Dominance Proof (Informal)

In candidate-proposing Gale-Shapley:

1. At any round, a candidate's proposal to their next choice is triggered only after being rejected by all previous choices.
2. If a candidate misreports by skipping someone (pretending to rank them lower), they either:
   - Never reach that person (because they got matched earlier — no loss), or
   - Reach them later and still propose (no gain from the skip), or
   - Never propose to them and end up unmatched (a loss).
3. If a candidate misreports by promoting someone (pretending they rank a "safe" match higher), they get matched to a worse-ranked true preference.

**There is no rearrangement of a proposer's reported list that produces a match better than their true top achievable stable partner.**

### What "Proposer-Optimal" Means Concretely

If the true set of stable matchings is {M₁, M₂, M₃}, the proposing side gets M₁ (the best stable matching for them, worst for reviewers). No manipulation can get them above M₁. They can only hurt themselves by lying.

---

## How Reviewers Can Manipulate: Truncation

The only proven effective strategy for reviewers is **preference list truncation**: a reviewer submits only a subset of their true acceptable partners, rejecting the rest outright.

### Why Truncation Works

When a reviewer truncates their list, they artificially create "unmatched" proposers. This forces the algorithm to reassign those proposers elsewhere — potentially freeing up better proposers for the truncating reviewer.

### Worked Example

**Setup**: 3 candidates (C1, C2, C3), 3 companies (E1, E2, E3). Candidates propose.

**True preferences:**

| | C1 ranks | C2 ranks | C3 ranks |
|---|----------|----------|----------|
| 1st | E1 | E1 | E2 |
| 2nd | E2 | E2 | E1 |
| 3rd | E3 | E3 | E3 |

| | E1 ranks | E2 ranks | E3 ranks |
|---|----------|----------|----------|
| 1st | C1 | C2 | C1 |
| 2nd | C2 | C1 | C2 |
| 3rd | C3 | C3 | C3 |

**Algorithm with truthful reporting:**

- Round 1: C1→E1 (accepted), C2→E1 (E1 prefers C1, rejects C2), C3→E2 (accepted)
- Round 2: C2→E2 (E2 prefers C2 over C3, accepts; C3 freed)
- Round 3: C3→E1 (E1 prefers C1, rejects C3)
- Round 4: C3→E3 (accepted)

**Result**: {C1↔E1, C2↔E2, C3↔E3}

E2 gets C2 (their 1st choice). E1 gets C1 (their 1st choice). E3 gets C3.

**Now E1 truncates**: E1 reports only {C1} as acceptable (drops C2 and C3).

- Round 1: C1→E1 (accepted), C2→E1 (E1 rejects — C2 not on truncated list), C3→E2 (accepted)
- Round 2: C2→E2 (E2 prefers C2 over C3, C3 freed)
- Round 3: C3→E1 (E1 rejects — C3 not on truncated list)
- Round 4: C3→E3 (accepted)

**Result**: {C1↔E1, C2↔E2, C3↔E3} — **same outcome**. Truncation had no effect here because the truthful result already gave E1 their top choice.

**Now try a case where truncation changes the result:**

Modify E2's preferences: E2 ranks C1 > C2 > C3 (E2 now prefers C1).

**Truthful run:**

- Round 1: C1→E1 (accepted), C2→E1 (rejected by E1; E1 prefers C1), C3→E2 (accepted)
- Round 2: C2→E2 (E2 prefers C2 over C3? No — E2: C1>C2>C3. C2 vs C3: C2 is preferred. Accept C2, free C3.)
- Round 3: C3→E1 (rejected), C3→E3 (accepted)

**Result**: {C1↔E1, C2↔E2, C3↔E3}. E2 gets C2 (rank 2).

**E2 truncates to {C1, C2}** — no change possible here since C3 gets pushed to E3 anyway.

**Construct a case where truncation truly helps:**

| | C1 | C2 | C3 |
|---|----|----|-----|
| 1st | E1 | E2 | E1 |
| 2nd | E2 | E1 | E2 |
| 3rd | E3 | E3 | E3 |

| | E1 | E2 | E3 |
|---|----|----|-----|
| 1st | C1 | C1 | C1 |
| 2nd | C2 | C3 | C2 |
| 3rd | C3 | C2 | C3 |

**Truthful run (candidates propose):**

- Round 1: C1→E1 (accepted), C2→E2 (accepted), C3→E1 (E1: C1>C3, rejects C3)
- Round 2: C3→E2 (E2: C1>C3>C2; C3 vs C2: C3 preferred. E2 accepts C3, frees C2.)
- Round 3: C2→E1 (E1: C1>C2; rejects C2)
- Round 4: C2→E3 (accepted)

**Result**: {C1↔E1, C3↔E2, C2↔E3}. E2 gets C3 (rank 2 for E2).

**E2 truncates to {C1}** — only accepts C1:

- Round 1: C1→E1 (accepted), C2→E2 (E2 rejects — C2 not on list), C3→E1 (E1 rejects C3)
- Round 2: C2→E1 (rejected), C3→E2 (E2 rejects — C3 not on list... wait, C1 is only acceptable)

Hmm — C3→E2: E2's truncated list is {C1}, so C3 is rejected.

- Round 2: C2→E1 (rejected), C3→E2 (rejected)
- Round 3: C2→E2 (rejected), C3→E3 (accepted)
- Round 4: C2→E3 (E3: C2 preferred over C3; wait, C3 already there. E3: C1>C2>C3. C2 vs C3: C2 wins. E3 accepts C2, frees C3.)
- Round 5: C3→E2 (still rejected), then C3 is unmatched. 

Actually if E2 truncates to only C1, and C1 goes to E1, E2 ends up unmatched — worse for E2.

**The lesson from these examples**: Truncation only helps when it causes a chain reaction that eventually frees a preferred proposer for the truncating reviewer. This requires specific preference configurations and is not guaranteed.

---

## Conditions Under Which Truncation Helps

Truncation is beneficial for reviewer R only when **all** of the following hold:

1. **R is not getting their first choice** under truthful play.
2. **There exists a proposer P** whom R prefers over their current truthful match.
3. **P is currently matched to someone else** under truthful play.
4. **Rejecting lower-ranked proposers causes a chain** that eventually frees P.

Formally: reviewer R benefits from truncating at threshold k (keeping only their top k choices) if doing so changes R's match from rank-j to rank-i, where i < j ≤ k.

**Detection heuristic**: compare the proposer-optimal stable matching against the reviewer-optimal stable matching. If they are different, reviewers in the "gap" (who got worse outcomes under proposer-optimal) have a potential incentive to manipulate.

---

## Finding All Stable Matchings (The Manipulation Space)

Reviewers can only achieve outcomes within the set of stable matchings. Strategic manipulation cannot produce an unstable outcome — it can only shift which stable matching is selected.

### The Lattice of Stable Matchings

All stable matchings form a distributive lattice:
- One extreme: proposer-optimal (best for proposers, worst for reviewers)
- Other extreme: reviewer-optimal (best for reviewers, worst for proposers)
- Every point in between is also a stable matching

**Implication**: A reviewer who successfully manipulates can move the outcome from the proposer-optimal end toward the reviewer-optimal end — but no further. They cannot achieve a match that isn't stable.

### Rotation Pointers (Advanced)

The full set of stable matchings can be enumerated using the **rotation pointers** technique (Irving & Leather 1986). Each "rotation" is a set of proposer-reviewer pairs that can be simultaneously reassigned. Applying a subset of rotations to the proposer-optimal matching produces a different stable matching.

For HR systems with n candidates: there are at most n(n-1)/2 rotations and potentially exponentially many stable matchings, but the proposer-optimal and reviewer-optimal bounds are always computable in O(n²).

---

## Practical Detection in HR Systems

### Red Flags That Manipulation May Be Occurring

1. **Employer submits unusually short preference lists**: if market norm is ranking 10 candidates but an employer ranks only 3, they may be truncating.
2. **Systematic "no-hire" outcomes for specific employers**: an employer that appears to never hire might be truncating so aggressively they end up unmatched by mistake.
3. **Preference list submitted very late**: late submission sometimes indicates strategic waiting to observe others' lists (relevant in non-simultaneous systems).

### What You Can Prove vs. Infer

| Claim | Provable? | Note |
|-------|-----------|------|
| Proposer X lied | Cannot prove | Truthful play is dominant; no rational incentive |
| Reviewer Y truncated | Detectable if lists are audited | Compare submitted vs. post-match revealed preferences |
| Reviewer Y benefited from truncation | Requires knowing true preferences | Counterfactual simulation needed |

---

## Incentive-Compatible Alternatives

If manipulation is a concern, these variants address it:

### Random Serial Dictatorship (for one-sided)
Not applicable to two-sided matching, but useful context: when one side has no preferences, random assignment is strategy-proof.

### Jury/Quota Mechanisms
In school-choice systems (Abdulkadiroğlu & Sönmez 2003), allowing schools to rank students by lottery (rather than true preference) creates a one-sided structure that is strategy-proof for students.

### Two-Sided Matching Without Manipulation Guarantees
**No two-sided stable matching mechanism is simultaneously:**
- Stable
- Strategy-proof for both sides

This is proven impossible (Roth 1982). You must choose which side gets strategy-proofness. Gale-Shapley gives it to the proposing side.

---

## Decision Framework for System Designers

```
Is truthful reporting from BOTH sides required?
│
├── YES → Two-sided mechanism cannot achieve this. Consider:
│         - One-sided mechanism (one side has no strategic role)
│         - Scoring-based assignment (no stated preferences)
│         - Repeated game with reputation effects
│
└── NO → Choose who proposes based on equity/optimality goals:
          │
          ├── Favor candidates → Candidates propose
          │   (Candidates get proposer-optimal match, strategy-proof for candidates)
          │
          └── Favor employers → Employers propose
              (Employers get proposer-optimal match, strategy-proof for employers)
```

**Recommendation for job markets**: Candidate-proposing is standard (NRMP, law clerk matching) because:
1. Candidates are the less powerful party and benefit from the guarantee.
2. Employers have repeated interactions and reputation constraints that partially substitute for formal strategy-proofness.

---

## Summary Table

| Actor | Can gain by lying? | Safe strategy | Risk of lying |
|-------|-------------------|---------------|---------------|
| Proposer | Never | Submit true full ranking | Getting a worse match |
| Reviewer | Sometimes (truncation) | Context-dependent | Getting unmatched |
| Reviewer (truncation) | Only if preference chain exists | Analyze lattice first | Backfire: worse outcome |

**The safe default for any participant who does not know the full preference landscape**: report truthfully. Only reviewers with near-complete information about others' preferences can reliably benefit from manipulation — and even then only in specific configurations.

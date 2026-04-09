# Formal Logic: Notation, Validity, and Soundness

## Core Distinction: Valid vs. Sound

These two terms are often confused. They test different things.

| Term | What it tests | Can have a false conclusion? |
|------|--------------|------------------------------|
| **Valid** | Logical structure only | No — *if* premises are true, conclusion must be true |
| **Sound** | Structure + truth of premises | No — sound = valid + all premises actually true |

**Key implication**: An argument can be **valid but unsound** (good structure, false premises → false conclusion). Critical thinking requires checking BOTH.

---

## Propositional Logic Notation

### Basic Connectives

| Symbol | Name | Meaning | Example |
|--------|------|---------|---------|
| `¬` | Negation | NOT | `¬P` = "not P" |
| `∧` | Conjunction | AND | `P ∧ Q` = "P and Q" |
| `∨` | Disjunction | OR (inclusive) | `P ∨ Q` = "P or Q or both" |
| `→` | Conditional | IF…THEN | `P → Q` = "if P then Q" |
| `↔` | Biconditional | IF AND ONLY IF | `P ↔ Q` = "P iff Q" |

### How to Read `P → Q`

- P = **antecedent** (the condition)
- Q = **consequent** (the result)
- Read: "If P, then Q" OR "P implies Q" OR "P is sufficient for Q" OR "Q is necessary for P"

**Truth table for `P → Q`:**

| P | Q | P → Q |
|---|---|-------|
| T | T | T |
| T | F | **F** ← only case where implication is false |
| F | T | T |
| F | F | T |

The conditional is only false when the antecedent is true and the consequent is false.

---

## The Four Syllogism Forms

A syllogism is a two-premise deductive argument. The four valid argument forms every analyst should recognize:

### 1. Modus Ponens (Affirming the Antecedent)

```
Premise 1:  P → Q
Premise 2:  P
──────────────────
Conclusion: Q
```

**Worked example:**
```
P1: If a company is profitable, it can pay dividends.
P2: Acme Corp is profitable.
─────────────────────────────────────────────────────
C:  Acme Corp can pay dividends.  ✓ VALID
```

### 2. Modus Tollens (Denying the Consequent)

```
Premise 1:  P → Q
Premise 2:  ¬Q
──────────────────
Conclusion: ¬P
```

**Worked example:**
```
P1: If a study is peer-reviewed, it has passed methodological scrutiny.
P2: This study has NOT passed methodological scrutiny.
──────────────────────────────────────────────────────────────────────
C:  This study is NOT peer-reviewed.  ✓ VALID
```

### 3. Hypothetical Syllogism (Chain)

```
Premise 1:  P → Q
Premise 2:  Q → R
──────────────────
Conclusion: P → R
```

**Worked example:**
```
P1: If inflation rises, the central bank raises rates.
P2: If the central bank raises rates, mortgage costs increase.
──────────────────────────────────────────────────────────────
C:  If inflation rises, mortgage costs increase.  ✓ VALID
```

Watch for long chains: each link must be evaluated. One false link breaks the chain.

### 4. Disjunctive Syllogism (Process of Elimination)

```
Premise 1:  P ∨ Q
Premise 2:  ¬P
──────────────────
Conclusion: Q
```

**Worked example:**
```
P1: The failure is either a hardware fault or a software bug.
P2: It is not a hardware fault.
─────────────────────────────────────────────────────────────
C:  The failure is a software bug.  ✓ VALID
```

**Trap**: P1 must be an **exhaustive** disjunction. If other options exist (firmware? user error?), the premise is false, making the argument unsound even though the structure is valid.

---

## The Two Invalid Forms (Formal Fallacies)

These look like valid syllogisms but are not. They are structural errors — the conclusion does not follow regardless of whether the premises are true.

### Affirming the Consequent

```
Premise 1:  P → Q
Premise 2:  Q          ← WRONG: affirming the consequent
──────────────────
Conclusion: P          ← INVALID
```

**Why it fails** — from the truth table: Q can be true when P is false (rows 3 and 4).

**Broken example:**
```
P1: If it rained, the ground is wet.
P2: The ground is wet.
──────────────────────────────────────
C:  It rained.   ✗ INVALID

Counter: a sprinkler could have made the ground wet.
```

This is the structure behind a large class of "confirmation bias" reasoning: observing the predicted outcome and claiming the hypothesis is proven.

### Denying the Antecedent

```
Premise 1:  P → Q
Premise 2:  ¬P         ← WRONG: denying the antecedent
──────────────────
Conclusion: ¬Q         ← INVALID
```

**Broken example:**
```
P1: If a startup raises Series A, it has investor confidence.
P2: This startup has NOT raised Series A.
─────────────────────────────────────────────────────────────
C:  This startup does NOT have investor confidence.  ✗ INVALID

Counter: it may have bootstrapped confidence through revenue.
```

---

## Validity Check Procedure

Apply this four-step test to any deductive argument:

**Step 1 — Formalize.** Assign letters to propositions and rewrite the argument in `P → Q` form.

**Step 2 — Identify the pattern.** Does it match Modus Ponens, Modus Tollens, Hypothetical Syllogism, or Disjunctive Syllogism?

**Step 3 — Check for the two invalid forms.** Is it affirming the consequent or denying the antecedent?

**Step 4 — Evaluate soundness.** Are the premises actually true? A valid argument with false premises is unsound.

### Worked Validity Check

**Original argument:** "All successful products are user-friendly. Instagram is user-friendly. Therefore Instagram is successful."

```
Formalize:
  Let S = "a product is successful"
  Let U = "a product is user-friendly"

  P1: S → U      (all successful products are user-friendly)
  P2: U           (Instagram is user-friendly)
  C:  S           (Instagram is successful)

Pattern: P → Q, Q ∴ P  →  Affirming the consequent.
Verdict: INVALID ✗

Even if both premises are true, the conclusion does not follow.
Being user-friendly is not sufficient for success; it is (per P1) only necessary.
```

---

## Categorical Syllogisms: Subject-Predicate Form

When arguments are about categories rather than propositions, use **categorical** form.

### The Four Categorical Propositions

| Code | Form | Example |
|------|------|---------|
| **A** | All S are P | All engineers are logical thinkers |
| **E** | No S are P | No poets are engineers |
| **I** | Some S are P | Some engineers are poets |
| **O** | Some S are not P | Some engineers are not logical thinkers |

### Valid Categorical Syllogism (Barbara — AAA)

```
All M are P.   (Major premise)
All S are M.   (Minor premise)
─────────────
All S are P.   (Conclusion)
```

**Example:**
```
All peer-reviewed studies are methodologically vetted.
All studies in this meta-analysis are peer-reviewed.
──────────────────────────────────────────────────────
All studies in this meta-analysis are methodologically vetted.  ✓
```

### Common Invalid Categorical Argument

```
All M are P.
All S are P.
─────────────
All S are M.   ✗ INVALID (Undistributed Middle)
```

The middle term M appears in both premises but is never fully distributed — P could encompass both M and S independently.

**Example:**
```
All dictators are powerful.
All presidents are powerful.
─────────────────────────────
All presidents are dictators.  ✗ — "powerful" is not exclusive to dictators.
```

---

## Connecting Formal Logic Back to Argument Analysis

Formal logic does not replace the full four-component analysis in SKILL.md — it sharpens Step 3 (Reasoning Evaluation). Use it when:

- An argument is **explicitly deductive** ("therefore", "it follows that", "this proves")
- You need to show WHY a reasoning step fails, not just that it "feels wrong"
- The argument is constructed as a chain of conditionals

For inductive arguments (generalizing from cases, statistical inference), the standards are different: validity/soundness do not apply; instead evaluate sample size, representativeness, and confidence intervals.

---

## Quick Reference: Argument Form Identifier

```
See P → Q and Q is affirmed?      → Modus Ponens (VALID) if P affirmed
                                   → Affirming Consequent (INVALID) if Q affirmed
See P → Q and something denied?   → Modus Tollens (VALID) if Q denied
                                   → Denying Antecedent (INVALID) if P denied
See a chain P → Q → R?            → Hypothetical Syllogism (VALID)
See P ∨ Q and one denied?         → Disjunctive Syllogism (VALID, if disjunction exhaustive)
See All M are P + All S are P?    → Check for Undistributed Middle (likely INVALID)
```

# Thinking in Time: The Neustadt-May Method

Richard Neustadt and Ernest May's *Thinking in Time: The Uses of History for Decision Makers* (1986) is the canonical framework for applying historical analogy rigorously. It emerged from two decades of teaching at Harvard's Kennedy School, where the authors observed that senior officials consistently misused history — drawing analogies too quickly, too confidently, and too selectively.

The core insight: **history is most dangerous when it is invoked carelessly and most useful when it forces systematic comparison.**

---

## The KUU Separation

Before constructing any analogy, Neustadt and May require separating what is **Known**, **Unclear**, and **Unknown** about the current situation. This prevents the analogy from doing too much epistemic work — filling in gaps that should remain flagged as uncertain.

```
KNOWN:     Facts established with reasonable confidence
UNCLEAR:   Things partially known, contested, or ambiguous
UNKNOWN:   Things we cannot currently know
```

**Why this matters for analogies**: Analysts typically reach for a historical precedent precisely when the current situation is confusing. The analogy then substitutes for the unknown facts — a cognitive shortcut disguised as historical reasoning. The KUU step forces explicit acknowledgment of what you're actually analogizing *from* versus *to*.

**Worked example** — A venture fund considering whether the 2025 AI infrastructure build-out resembles the 1990s fiber-optic overbuild:

| | Current Situation (AI Infra 2025) |
|---|---|
| **Known** | GPU datacenter capex is >$300B committed; hyperscalers are primary buyers; training compute is the current bottleneck |
| **Unclear** | Whether inference demand will scale to absorb capacity; whether model efficiency gains will outpace compute demand |
| **Unknown** | Competitive moat duration; whether open-source closes the gap; regulatory constraints on deployment |

The historical case (fiber-optic overbuild):

| | Historical Situation (Fiber 1998-2001) |
|---|---|
| **Known** | $1T+ laid; capacity exceeded demand by 100x; most carriers went bankrupt |
| **Unclear** | Whether capacity enabled the application layer growth that followed |
| **Unknown** at the time | VoIP, streaming, broadband adoption curves |

KUU alignment: The "Unclear" items on both sides map onto each other — both cases hinge on whether demand-side absorption catches up with supply-side investment. That's the structural load-bearing similarity. The "Unknown" items are different: the historical actors didn't know about VoIP; current analysts don't know about inference scaling. Both unknowns are demand-side but operate differently (applications vs. model efficiency). **This asymmetry limits the analogy.**

---

## The Likenesses-Differences Procedure

This is the operational core of the method. It is distinct from casual analogy-drawing in one critical way: **differences are listed first**, or at minimum with equal weight. The human tendency is to notice likenesses and treat differences as qualifications. Neustadt-May reverse the default.

### Step 1: List Likenesses

Generate a column of features shared between the historical event and the current situation. Do not evaluate yet — just enumerate.

### Step 2: List Differences

Generate a column of features that differ. Include:
- Contextual differences (era, technology, institutions)
- Actor differences (who is making decisions, what they know)
- Stakes differences (what outcomes are at risk)
- Process differences (how decisions were made)

### Step 3: Sort by Relevance to Your Specific Question

Not all likenesses and differences matter equally. The analogy's validity depends on whether the similarities are **causally relevant** to the question being asked. A similarity that's causally irrelevant to your question doesn't strengthen the analogy; a difference that's causally irrelevant doesn't weaken it.

```
RELEVANCE TEST: "Would this feature, if different, change the outcome 
                 I'm trying to learn from?"
```

### Step 4: Assess the Net

If causally-relevant likenesses outnumber causally-relevant differences, the analogy is useful. If differences dominate, find a different analogy or abandon the approach.

**Decision table:**

| Similarity Status | Difference Status | Analogy Verdict |
|---|---|---|
| Strong, causally relevant | Weak, peripheral | Use analogy, high confidence |
| Strong, causally relevant | Strong, causally relevant | Use analogy with named caveats |
| Weak, peripheral | Weak, peripheral | Analogy uninformative — find another |
| Weak, peripheral | Strong, causally relevant | Discard analogy |

---

## Placement: Situating the Current Moment in Historical Sequence

One of Neustadt-May's most distinctive moves is "placement" — asking *where in the story are you right now?*

Historical events are not points; they are sequences. When you invoke "the dotcom bubble," you might mean:
- 1995: The early hype phase (pre-peak)
- 1999: The speculative peak (maximum overvaluation)
- 2001: The crash
- 2003–2005: The consolidation (survivors gaining durable market position)

The lesson changes dramatically depending on which phase you're analogizing to. "The dotcom bubble" as a single monolithic lesson is nearly meaningless; "the dotcom bubble, specifically the 1999–2001 investor capitulation phase" is precise enough to be useful.

### Placement Procedure

1. **Tell the historical story as a sequence**: Identify 4–6 named phases or turning points in the historical case.
2. **Identify what caused each transition**: What shock, decision, or accumulation moved the situation from phase N to phase N+1?
3. **Locate where the current situation sits**: Which phase does the current situation most resemble? What transition mechanisms are present or absent?
4. **Estimate what comes next — conditionally**: "If the same transition mechanism fires, we move to phase N+1. The mechanism is X. Is X present?"

**Worked example** — Korea analogy in the Cuban Missile Crisis (a case Neustadt-May analyze directly):

| Phase | Korea (1950) | Trigger |
|---|---|---|
| 1 | Initial aggression across a border | Invasion |
| 2 | UN/US intervention to restore status quo | Political decision |
| 3 | Crossing the 38th parallel (mission expansion) | MacArthur's push north |
| 4 | Chinese entry | Warning signals ignored |
| 5 | Stalemate and negotiated settlement | Military limits |

When Kennedy advisors in 1962 said "this is like Korea," they were implicitly invoking Phase 4: ignoring warning signals leads to unexpected escalation. The structural mechanism they were pointing at was **adversary red-line underestimation**. That's causally relevant and maps onto the Cuba situation.

But they missed a placement difference: Korea was a land war with a third-party escalator (China); Cuba was a naval blockade confronting the primary adversary directly. The transition mechanism for Phase 4 (red-line underestimation) still applied, but the *form* of escalation was different enough that the Korea lesson needed explicit modification.

---

## The "Goldberg Rule" (Institutionalized Analogy Misuse)

Neustadt and May name a specific failure mode after the Washington Post columnist: the bureaucratic habit of citing a historical precedent to justify a decision already reached on other grounds. The history is decorative, not load-bearing.

**Identifying Goldberg-rule usage:**

- The analogy was introduced after the decision direction was set, not before
- Only likenesses are cited; differences are absent or dismissed
- The historical case is selected because it ended well for the party invoking it
- No alternative historical cases are considered

**Diagnostic question**: "If this historical analogy suggested the opposite conclusion, would the decision-maker change the decision?" If not, the analogy is doing no real work.

---

## The "May Test" for Actionable Lessons

Even a structurally valid analogy doesn't automatically produce usable lessons. May requires that each extracted lesson pass:

1. **Specificity test**: Can the lesson be stated in a form that would change a specific decision? "Don't appease" is not specific. "Don't make concessions on the core casus belli without receiving a verified, binding commitment in return" is specific.

2. **Transferability test**: Was the lesson produced by a feature of the historical situation that *also exists* in the current situation? If the lesson depended on, say, a parliamentary system and you're operating in a presidential system, the lesson may not transfer.

3. **Counterfactual test**: Could the historical actors have achieved a better outcome if they had followed this lesson? If the lesson would have made no difference (the outcome was overdetermined), it's not a real lesson.

**Worked example** — Lesson extraction from the 2008 financial crisis for a fintech lending platform:

| Raw Lesson | Specificity | Transferability | Counterfactual | Verdict |
|---|---|---|---|---|
| "Don't take on too much leverage" | Fails — too vague | N/A | N/A | Discard |
| "Underwriting standards degrade during credit expansions when originate-to-distribute models sever the risk-bearing link from the credit decision" | Passes | Passes if platform sells loans to capital markets | Passes — tighter underwriting reduced losses at firms that retained exposure | **Use** |
| "Regulators will intervene" | Fails — too vague | N/A | N/A | Discard |

---

## Common Misapplications and Their Neustadt-May Corrections

### Munich Syndrome

The "appeasement = disaster" lesson became so dominant in US foreign policy that it was applied to every confrontation regardless of structural fit. Neustadt-May call this **the over-lesson**: a single dramatic case colonizes an entire category of decisions.

**Correction**: Ask whether the adversary has the same type of aims as Hitler (unlimited territorial expansion, ideology requiring external enemies). If not, the Munich lesson doesn't apply. Most adversaries have limited aims; the Munich lesson applies in a narrow set of cases.

### Pearl Harbor Syndrome

The "surprise attack" lesson drove massive intelligence infrastructure — but also produced the opposite failure mode: intelligence overload where every threat signal is elevated, making genuine warnings harder to distinguish.

**Correction**: Extract the *specific* lesson (signals existed but weren't aggregated across agencies) rather than the general lesson (be vigilant). Then ask: is the specific mechanism present? Do we have a signals aggregation problem, or a different problem?

### Survivorship Analogy

Invoking the cases that survived and succeeded while ignoring structural twins that failed. "Amazon survived the dotcom bust, therefore our company will too."

**Neustadt-May correction**: Explicitly list the cases that shared the same structural features but did *not* survive. What feature separated survivors from casualties? Does the current situation have that feature?

---

## Full Application Protocol

```
Step 1 — KUU Separation (5 min)
  - Column 1: What we know about the current situation
  - Column 2: What is unclear
  - Column 3: What we cannot know yet

Step 2 — Analogy Identification
  - State the analogy: "Current situation X is like historical event Y because..."
  - Identify 2 alternative analogies — the popular one may not be the best one

Step 3 — Likenesses-Differences Analysis
  - List likenesses (20+ if possible, uncritically)
  - List differences (force yourself to match the likenesses count)
  - Mark each as causally relevant or peripheral to your specific question

Step 4 — Placement
  - Map the historical event's sequence (4-6 phases)
  - Locate: where in that sequence does the current situation sit?
  - Identify: what transition mechanism moved phase N → N+1?
  - Ask: is that mechanism present now?

Step 5 — Goldberg Check
  - Would this analogy, if it pointed the other way, change the decision?
  - Who introduced the analogy, and when in the decision process?

Step 6 — Lesson Extraction (May Test)
  - State each lesson specifically enough to change a specific decision
  - Check transferability: does the current situation share the feature that produced the lesson?
  - Check counterfactual: would following the lesson have helped historical actors?

Step 7 — State the Limits
  - Where does the analogy break down?
  - What would have to be true for the analogy to be invalid entirely?
```

---

## Source Note

Neustadt, R.E. & May, E.R. (1986). *Thinking in Time: The Uses of History for Decision Makers*. Free Press. The Korea/Cuba and Munich material are directly from Chapter 2 and Chapter 4 respectively. The "Goldberg Rule" is discussed in Chapter 8. The KUU framework appears in Chapter 11 as the authors' synthesis protocol for officials.

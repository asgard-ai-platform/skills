# Fallacy Catalog

Organized by failure mode. Each entry gives: the structural pattern (what goes wrong logically), a worked example with analysis, and a detection test you can apply during argument evaluation.

---

## Category 1 — Relevance Fallacies

The evidence or premise introduced is true but **irrelevant** to the claim.

---

### Ad Hominem

**Pattern**: Attack the person making the argument instead of the argument itself.

```
Person X makes Claim C.
Person X has flaw F.
Therefore, Claim C is false.
```

**Why it fails**: The truth value of C is independent of who states it. A corrupt politician can correctly state that 2+2=4.

**Worked example**:
> "We shouldn't listen to Dr. Chen's climate data — she got divorced last year and clearly has poor judgment."

- Claim: Dr. Chen's climate data is unreliable
- Stated reason: personal life failure
- Logical gap: judgment in personal relationships does not transfer to scientific methodology

**Detection test**: *Can you evaluate the claim without knowing anything about the person who made it?* If yes, ad hominem is irrelevant.

**Variant — Circumstantial Ad Hominem**: "Of course the tobacco company says cigarettes are safe — they profit from them." The profit motive is a reason to scrutinize the evidence more carefully, but it does not make the evidence false. (Compare: a doctor who profits from surgery may still be right that surgery is needed.)

---

### Appeal to Authority (Argumentum ad Verecundiam)

**Pattern**: A person with authority status asserts C, therefore C is true.

```
Authority figure A says C.
Therefore C is true.
```

**Why it fails**: Authority is a signal for where to look for evidence — not a substitute for evidence. Authorities are routinely wrong outside their domain, and sometimes within it.

**Worked example**:
> "Elon Musk says AGI will arrive by 2030, so we should restructure our entire product roadmap around that timeline."

Analysis:
- Musk has engineering credibility in adjacent domains
- "AGI by 2030" requires predicting ML research breakthroughs — outside any individual's verified expertise
- No evidence chain is offered; the authority status does the argumentative work

**Legitimate use of authority**: Citing expert consensus (not individual authority) + showing the evidence chain. "The IPCC report synthesizes 14,000 studies and finds X" is not appeal to authority — it points to verifiable evidence.

**Detection test**: *Is the authority cited as a replacement for evidence, or as a pointer to evidence?*

---

### Red Herring (Ignoratio Elenchi)

**Pattern**: Introduce a true but irrelevant fact that distracts from the actual claim.

**Worked example**:
> Auditor: "Your financial reports show a $2M discrepancy in Q3."
> CFO: "Our company donated $500K to disaster relief last quarter and we've won three ethics awards."

The charity work is likely true and admirable. It is completely irrelevant to the $2M discrepancy. The CFO has shifted the subject without addressing the claim.

**Detection test**: *Does this evidence, if true, actually change the probability that the original claim is true or false?* If no, it's a red herring.

---

### Whataboutism (Tu Quoque)

**Pattern**: Deflect a criticism by pointing to a similar flaw in the critic.

```
You criticize me for doing X.
But you also do X (or something like X).
Therefore my doing X is acceptable / your criticism is invalid.
```

**Why it fails**: Whether the critic is a hypocrite is a separate question from whether the original action X is wrong.

**Worked example**:
> "You're saying our factory pollutes the river? What about the factory upstream — they pollute twice as much!"

The upstream factory's behavior may be a valid separate complaint. It does not address whether the original factory is polluting.

---

## Category 2 — Presumption Fallacies

The argument assumes what it needs to prove, or makes unwarranted assumptions about the options available.

---

### Begging the Question (Petitio Principii / Circular Reasoning)

**Pattern**: The conclusion is smuggled into the premises.

```
P1: [Restates C in different words]
P2: [Support that only works if C is already true]
Therefore C.
```

**Worked example**:
> "The Bible is true because it is the word of God, and we know it is the word of God because the Bible says so."

Structure:
- P1: The Bible is the word of God (assumed)
- P2: The word of God is true (assumed)
- C: The Bible is true (the original claim)

The premises only hold if the conclusion already holds.

**Subtler form**:
> "This investment strategy works because it has consistently beaten the market."

If "works" means "beats the market consistently," the statement is tautological. The question is whether it *will* continue to beat the market — which past performance does not establish.

**Detection test**: *Can you state the premises without assuming the conclusion? If not, the argument is circular.*

---

### False Dichotomy (False Dilemma)

**Pattern**: Present only two options when more exist, then argue that because one is unacceptable, the other must be chosen.

```
Either A or B (presented as exhaustive).
Not A.
Therefore B.
```

**Why it fails**: The "either/or" framing is the fallacy. The logical form (modus tollens) is valid; the premise of exhaustiveness is not.

**Worked example**:
> "We can either cut R&D spending to meet this quarter's targets, or miss targets and lose investor confidence. We can't lose investor confidence. So we must cut R&D."

Hidden options not considered:
- Renegotiate targets with investors
- Cut other cost centers
- Raise bridge financing
- Miss targets while communicating a credible long-term plan

**Detection test**: *List three options that were not mentioned. If they exist, the dilemma is false.*

---

### Slippery Slope

**Pattern**: Claim that a moderate first step will inevitably lead to an extreme outcome, without demonstrating the causal chain.

```
If A, then B.
If B, then C.
...
If Y, then Z (extreme outcome).
Therefore, do not do A.
```

**Why it fails**: Each conditional link in the chain requires independent evidence. The word "inevitably" or "will lead to" does the work that evidence should do.

**Worked example**:
> "If we allow employees to work from home on Fridays, they'll start working from home all week, then they'll stop caring about office culture, then they'll stop collaborating entirely, and our innovation pipeline will collapse."

Each link may have some probability — but the argument presents the chain as inevitable without showing:
- What % of remote-Friday companies ended up fully remote
- Whether fully remote correlates with innovation collapse
- What interventions break the chain

**When slippery slope is NOT a fallacy**: If you can cite empirical evidence for each causal link, the argument becomes a legitimate empirical claim about causal chains — not a fallacy. "Historically, 80% of companies that allowed Friday WFH expanded it within 18 months (cite)" is evidence, not a slippery slope.

**Detection test**: *Is each causal link supported by evidence, or asserted as self-evident?*

---

### Hasty Generalization

**Pattern**: Draw a universal conclusion from an insufficient sample.

```
Observed: X1, X2, X3 all have property P.
Conclusion: All X have property P.
```

**What makes a sample insufficient**:
- Too small relative to population variance
- Not randomly selected (survivorship bias, convenience sampling)
- Drawn from a single context that may not generalize

**Worked example**:
> "We interviewed 12 customers who churned and 10 of them said price was the reason. So we should cut prices."

Problems:
- 12 churned customers ≠ representative of all churned customers (who didn't respond to the interview request?)
- Churned customers' stated reasons may differ from actual reasons (post-hoc rationalization)
- Doesn't account for customers retained despite higher prices
- No comparison to industry churn rates

**Detection test**: *What is the population size? How was the sample selected? Could the selection process bias the result?*

---

### Straw Man

**Pattern**: Misrepresent an opponent's argument as a weaker or more extreme version, then refute the distorted version.

```
Opponent argues A.
You argue against A' (a distorted version of A).
You "defeat" A'.
You claim to have defeated A.
```

**Worked example**:
> Original argument: "We should reduce the defense budget by 10% and redirect funds to education."
> Straw man: "My opponent wants to leave our country defenseless against foreign threats."

The 10% reduction claim is transformed into total disarmament — which is far easier to attack.

**The Steelman Correction** (from SKILL.md Gotchas):

Before evaluating any argument, construct its **strongest** version:

1. State the claim as charitably as possible
2. Identify the best evidence the arguer could cite (even if they didn't)
3. Assume competent, good-faith reasoning
4. Then evaluate *that* version

If the steelman fails, the argument is genuinely weak. If you can only defeat the strawman, you haven't evaluated the argument.

**Detection test**: *Would the person who made this argument recognize my restatement of their position as accurate?*

---

## Category 3 — Causation Fallacies

These are technically a subset of presumption fallacies but appear frequently enough in empirical arguments to merit separate treatment.

---

### Post Hoc Ergo Propter Hoc ("After, therefore because of")

**Pattern**: Because B followed A, A caused B.

```
A happened at time T1.
B happened at time T2 (T2 > T1).
Therefore A caused B.
```

**Worked example** (from SKILL.md, extended):
> "Our Q3 output dropped 15% after going remote. Therefore remote work caused the drop."

What the argument ignores:
- Q3 is historically lower in this industry (seasonality)
- The company hired 30 new employees in Q2 who were still ramping
- A major client paused orders in Q3 (external factor)
- No control group (what happened at comparable non-remote companies?)

**Strengthening the argument**: To establish causation rather than correlation, you need:
1. Temporal precedence (A before B) — ✓ already established
2. Covariation (A and B move together) — needs data across multiple periods
3. Elimination of alternatives — needs to rule out confounds
4. Mechanism — how does remote work *cause* lower output?

**Detection test**: *What other factors changed at the same time as A? Could any of them explain B?*

---

### Cum Hoc Ergo Propter Hoc ("With, therefore because of")

**Pattern**: A and B are correlated, therefore A causes B.

**Classic example**: Ice cream sales and drowning rates are positively correlated. Ice cream does not cause drowning; hot weather causes both.

**Business example**:
> "Users who open more than 5 emails per week have 40% higher LTV. Therefore we should send more emails to increase LTV."

What the correlation may actually reflect: high-engagement users were already more valuable *and* more likely to open emails. Forcing low-engagement users to receive more emails may depress LTV (unsubscribes, spam filters).

**Detection test**: *Is there a third variable that could explain both A and B? Does the causal direction run from A→B, B→A, or neither?*

---

## Category 4 — Ambiguity Fallacies

The argument exploits vagueness or shifts the meaning of key terms.

---

### Equivocation

**Pattern**: Use the same word in two different senses within the same argument.

**Worked example**:
> "Laws of nature cannot be broken. Laws against theft can be broken. Therefore laws against theft are not laws of nature."

"Law" in sense 1: descriptive regularities (physics)
"Law" in sense 2: normative rules (legal code)

These are different concepts sharing a word. The syllogism only works if "law" means the same thing in both premises.

**Business example**:
> "Our strategy is 'growth.' Growth requires investment. Therefore any expenditure is justified by our strategy."

"Growth" shifted from "strategic direction" to "any increase in any metric."

**Detection test**: *Replace the ambiguous word with a precise definition. Does the argument still hold for both uses of the definition?*

---

### Appeal to Nature

**Pattern**: X is natural, therefore X is good (or safe, or correct).

**Why it fails**: "Natural" does not map onto "safe," "ethical," or "effective." Arsenic is natural. Penicillin is synthetic.

**Worked example**:
> "Our supplement uses only natural ingredients, so it's safer than pharmaceutical alternatives."

- Natural ≠ no side effects (hemlock, belladonna)
- Pharmaceutical ≠ synthetic (many are derived from natural sources)
- Safety is determined by dosage, interaction profile, and clinical evidence — not origin

---

## Quick-Reference Detection Table

| You see this pattern | Likely fallacy | Key question to ask |
|----------------------|---------------|---------------------|
| Attacking the speaker | Ad hominem | Does the speaker's character change the evidence? |
| Citing famous person with no evidence | Appeal to authority | What evidence does the authority point to? |
| "That's irrelevant, but consider this..." | Red herring | Does this new fact affect the original claim? |
| "You do it too" | Tu quoque | Does the critic's behavior change whether the act is wrong? |
| Conclusion restated as premise | Circular reasoning | Can you state the premises without assuming the conclusion? |
| Only two options presented | False dichotomy | Name three alternatives |
| "First step leads to catastrophe" | Slippery slope | Is each causal link evidenced? |
| Small sample, big claim | Hasty generalization | How was the sample selected? |
| Opponent's position exaggerated | Straw man | Would the opponent recognize this restatement? |
| "After X, therefore X caused Y" | Post hoc | What else changed at the same time? |
| "X correlates with Y, X causes Y" | Cum hoc | Is there a third variable? Which direction does causation run? |
| Key word used in two senses | Equivocation | Does the argument hold with a single consistent definition? |
| "It's natural, therefore good" | Appeal to nature | Does natural status determine safety/effectiveness? |

---

## Compound Fallacies

Real arguments rarely contain a single clean fallacy. Watch for these combinations:

**Poisoning the well + Straw man**:
> "The study was funded by Big Pharma [poisons credibility], and they're basically saying we should trust corporations over patients [straw man]."

Two fallacies working together: credibility is impugned before the argument is heard, then the argument is distorted.

**False dichotomy + Slippery slope**:
> "Either we ban all social media for under-18s, or we accept that teens will suffer permanent psychological damage."

Step 1: Only two options (false dichotomy)
Step 2: The bad option is described as inevitable catastrophe (slippery slope)

**Hasty generalization + Appeal to authority**:
> "Three Nobel laureates agree with our position, so the scientific consensus is on our side."

Three individuals ≠ consensus, regardless of their prestige.

---

## Applying the Steelman Protocol

When you detect a fallacy, do not stop at naming it. Apply the steelman before issuing a verdict:

1. **Name the fallacy**: "This appears to be post hoc reasoning."
2. **State the strongest non-fallacious version**: "The strongest version of this argument would need a controlled comparison and ruled-out confounds."
3. **Check if evidence exists**: Does the arguer have (or could they access) the evidence that would fix the gap?
4. **Issue verdict on the steelman**: If the steelman still fails, the argument is genuinely weak. If the steelman succeeds, flag what's missing rather than dismissing the argument wholesale.

This prevents critical thinking from collapsing into "fallacy labeling theater" — where the goal becomes finding labels rather than arriving at justified conclusions.

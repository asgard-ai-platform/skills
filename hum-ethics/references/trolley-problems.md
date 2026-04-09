# Trolley Problems: Variations and Their Implications

Trolley problems are thought experiments designed to isolate specific ethical variables by holding everything else constant. Their value is not in resolving the dilemma — they're stipulated to have no clean answer — but in revealing **which moral intuitions conflict with which frameworks**, and why.

Each variation below is paired with a multi-framework analysis following the format from `SKILL.md`.

---

## The Classic Trolley Problem (Foot, 1967)

**Setup:**
A runaway trolley is heading toward five people tied to the track. You are standing next to a lever. If you pull it, the trolley diverts to a side track where one person is tied. You will not be harmed either way.

**Options:** A) Do nothing → 5 die. B) Pull lever → 1 dies.

| Framework | Recommendation | Reasoning |
|-----------|---------------|-----------|
| Deontology | **A or B** (contested) | Pulling the lever makes you an agent of harm; some Kantians say your duty is not to redirect harm onto an innocent party. Others say inaction is also a choice — you still bear responsibility. No clean answer. |
| Utilitarianism | **B** | 5 lives saved vs. 1 lost. Net utility gain: +4 lives. Pull the lever. |
| Virtue Ethics | **B** | A courageous and practically wise person acts to minimize harm when intervention is possible. Paralysis in the face of preventable death is not virtue. |
| Justice (Rawls) | **B** | Behind the veil of ignorance, you have a 5/6 chance of being one of the five. Expected-value reasoning under fairness favors pulling. |

**Convergence:** 3 of 4 frameworks recommend B. The deontological tension arises from the doctrine of doing vs. allowing (act vs. omission distinction) — your intervention transforms you from bystander to agent.

**Core tension revealed:** Consequences vs. agent-relative duties. Utilitarianism treats outcomes symmetrically; deontology weights the distinction between *causing* harm and *failing to prevent* it.

---

## The Footbridge Variant (Thomson, 1985)

**Setup:** Same five people, same trolley. This time you are on a footbridge above the tracks with a large stranger beside you. The only way to stop the trolley is to push the stranger off the bridge — their body will stop the trolley. You will not fall if you push them.

**Options:** A) Do nothing → 5 die. B) Push stranger → 1 dies, 5 saved.

| Framework | Recommendation | Reasoning |
|-----------|---------------|-----------|
| Deontology | **A** | You are using the stranger as a *means* to save others — a direct violation of Kant's Formula of Humanity. The five people are not saved *by* the stranger's sacrifice but *through* it against their will. |
| Utilitarianism | **B** | Same math as the classic case: 5 lives vs. 1. The physical mechanism of death is irrelevant to the utility calculus. |
| Virtue Ethics | **A** | A person of good character does not murder an innocent bystander. The act of pushing someone to their death crosses a threshold that no virtuous person would cross, regardless of outcome. |
| Justice (Rawls) | **A** | The stranger has not consented to be sacrificed. A system that permits using any individual as an involuntary instrument for collective benefit would be rejected behind the veil of ignorance — you might be that stranger. |

**Divergence:** 3 of 4 frameworks now recommend A — the opposite of B in the classic case.

**Why the arithmetic is the same but the answer flips:**

The footbridge variant isolates the **doctrine of double effect (DDE)**:

> An action that causes harm is permissible only if:
> 1. The action itself is not intrinsically wrong
> 2. The agent intends the good effect, not the bad
> 3. The bad effect is a *side effect*, not the *means* to the good effect
> 4. The good effect is proportionate to the bad

In the classic problem, the one person's death is a *side effect* of redirecting the trolley — the trolley would stop whether or not they were on the track. In the footbridge, the stranger's death is the *mechanism* of stopping the trolley. Their body is the means. DDE says this is categorically different.

Utilitarianism rejects DDE entirely — the mechanism of harm is irrelevant; only consequences matter.

---

## The Loop Track Variant (Thomson, 1985)

**Setup:** A single track loops back. Five people on the main track. One person on the side track — but the side track loops *back to join the main track before the five people*. If you divert the trolley, it will go around the loop and still hit the five unless the one person's body stops it first.

**Options:** A) Do nothing → 5 die. B) Pull lever → trolley goes to loop track, one person's body stops it → 1 dies, 5 saved.

This variant is designed to challenge the DDE defense of the classic trolley case.

**The problem it creates:**

In the loop variant, the one person's body *is* the mechanism — exactly like the footbridge case. If you endorse pulling the lever in the classic case via DDE, you must explain why this case is different. Yet most people's intuition is still to pull the lever.

**Implications by framework:**

- **Utilitarianism:** Pull lever. Same arithmetic. No problem.
- **Deontology:** *Genuinely contested.* The loop closes the DDE gap: the person IS the means. Strict Kantians may say don't pull. Others argue intent matters (you intend diversion, not death), even if death is necessary.
- **Virtue Ethics:** Focus on the agent's character and intentions, not the causal chain. A practically wise person still pulls to save five — the causal mechanism is too abstract to override the moral weight of five deaths.
- **Justice (Rawls):** Pull. The asymmetry (5 vs. 1) holds regardless of causal chain.

**What the loop reveals:** Even within a single framework, trolley variants produce disagreement among practitioners. The loop is a tool for testing whether a deontological position is *internally consistent* or relies on intuitional shortcuts.

---

## The Transplant Surgeon Case (Thomson, 1976)

**Not a trolley problem, but structurally equivalent:**

**Setup:** A surgeon has five patients dying of organ failure. A healthy patient comes in for a checkup. The surgeon could kill the healthy patient and harvest their organs to save the five.

**Options:** A) Do nothing → 5 die. B) Kill one → 5 saved.

The numbers are the same as the trolley problem. Yet almost no one endorses B — including people who pulled the lever in the classic case.

**Why this matters for ethical analysis:**

This case tests whether trolley-problem intuitions generalize, or whether they depend on features specific to the trolley scenario (machinery, distance, physical indirectness).

| Framework | Recommendation | Reasoning |
|-----------|---------------|-----------|
| Deontology | **A** | Killing an innocent patient violates their rights categorically. The doctor's duty of non-maleficence is absolute. |
| Utilitarianism | **B** (in principle) | 5 lives > 1 life. Act utilitarianism is forced to endorse B, which is why most utilitarians retreat to *rule* utilitarianism: a rule permitting organ harvesting would destroy trust in medicine, producing catastrophic long-term consequences. So even utilitarianism says A under rule formulation. |
| Virtue Ethics | **A** | No physician of good character could do this. The act is not just harmful — it destroys the virtue of the agent irreversibly. |
| Justice (Rawls) | **A** | Behind the veil of ignorance, you would never endorse a system in which you could be killed for your organs during a routine visit. |

**Convergence:** All four frameworks recommend A once rule utilitarianism is applied.

**Key lesson:** When act utilitarianism reaches a conclusion that all other frameworks — and strong moral intuition — reject, this is evidence to apply *rule* utilitarianism instead. The divergence is diagnostic.

---

## Decision Table: Which Variables Each Variant Tests

| Variant | Variable Isolated | Classic vs. Variant Verdict |
|---------|------------------|-----------------------------|
| Classic | Acts vs. omissions | B (pull) wins 3-1 |
| Footbridge | Using person as means | A (don't push) wins 3-1 |
| Loop Track | DDE consistency | Contested (2-2 or 3-1 depending on deontological school) |
| Transplant | Physical distance / institutional context | A (don't harvest) wins 4-0 (with rule utilitarianism) |

---

## Using Trolley Variants in Practice

When applying the `hum-ethics` framework to a real-world dilemma, use the trolley variants as **diagnostic probes**:

**Step 1 — Classify the real case:**
- Does the harm happen as a *side effect* of an action, or is the person *the instrument* of benefit? → Classic vs. Footbridge
- Is there physical or procedural distance between decision-maker and harmed party? → Transplant
- Does the causal chain run *through* the harmed party? → Loop

**Step 2 — Apply the matching variant's logic:**
If the real case maps to the footbridge (person is the means), expect deontology and virtue ethics to resist even when utilitarian math favors action.

**Step 3 — Check for rule vs. act utilitarian split:**
If act utilitarianism recommends something that produces moral horror (transplant surgeon), shift to rule utilitarianism and recalculate based on the long-run consequences of adopting that rule universally.

**Step 4 — Make the tension explicit (IRON LAW):**
Do not resolve the tension by picking one framework. State: "Frameworks X and Y converge on A; framework Z recommends B because of [specific feature]. The core conflict is between [value 1] and [value 2]."

---

## Common Errors When Using Trolley Analogies

**Error 1 — Treating the trolley as a policy tool:**
Trolley problems are designed with stipulated certainties (you *know* pulling the lever saves exactly five people). Real decisions have uncertainty. Do not import trolley-level certainty into real-world recommendations.

Correction: After the framework analysis, explicitly add a probability-weighted step for real cases.

**Error 2 — Stopping at "5 > 1, therefore act":**
This applies act utilitarianism only and ignores DDE, rights, and rule-level consequences. Violates the IRON LAW of multiple frameworks.

**Error 3 — Assuming the agent is neutral:**
Trolley problems stipulate a stranger pulled the lever. In real cases, role matters: a doctor has duties that a bystander does not. A government official has powers — and constraints — that a private individual lacks. Apply virtue ethics and deontology *within the agent's role*, not abstractly.

**Error 4 — Using the trolley to justify atrocities at scale:**
"Utilitarian trolley logic" has historically been invoked to justify mass harm (bombing civilians to end a war faster, sacrificing a minority for majority prosperity). The transplant surgeon case exists precisely to show where act utilitarianism fails. Pair every utilitarian argument with a rights-based check.

---

## Source Notes

- Foot, P. (1967). "The Problem of Abortion and the Doctrine of Double Effect." *Oxford Review*, 5, 5–15.
- Thomson, J.J. (1985). "The Trolley Problem." *Yale Law Journal*, 94(6), 1395–1415.
- Thomson, J.J. (1976). "Killing, Letting Die, and the Trolley Problem." *The Monist*, 59(2), 204–217.
- Kamm, F.M. (2007). *Intricate Ethics*. Oxford University Press. (Loop track and further variants)

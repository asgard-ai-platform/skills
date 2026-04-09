# Business Ethics Cases

Real business dilemmas rarely have clean answers. Each case below is worked through all four frameworks from the parent skill. Pay attention to the **divergence pattern** — it reveals which values are structurally in tension.

---

## Case 1: The Ford Pinto (Cost-Benefit vs. Rights)

**Background**: In the 1970s, Ford engineers discovered that the Pinto's fuel tank would rupture in rear-end collisions above 25 mph. An internal cost-benefit memo calculated it was cheaper to pay wrongful-death settlements ($49.5M) than to retrofit all vehicles ($137M). Ford chose not to retrofit. Approximately 500 deaths resulted.

**Decision**: Should Ford retrofit the fuel tank at a cost exceeding projected litigation payouts?

**Stakeholders**: Current and future Pinto owners, their families, Ford shareholders, auto industry at large, public trust in corporate self-regulation.

| Framework | Recommendation | Reasoning |
|-----------|---------------|-----------|
| Deontology | **Yes, retrofit** | Users were not informed of the known risk. Selling a product you know to be lethal — without disclosure — violates the duty of non-maleficence and the duty of honesty. The categorical imperative: if every company treated customers as expendable when repair costs exceeded death settlements, the institution of product safety would collapse entirely. |
| Utilitarianism | **Ambiguous** | Ford's own memo attempted utilitarian calculus, but got it wrong by using only direct litigation costs. Full accounting must include: erosion of brand trust, regulatory backlash, punitive damages (not included in original estimate), and the disutility of unreported crashes that never reached court. Proper utilitarian analysis likely favors the retrofit. |
| Virtue Ethics | **Yes, retrofit** | No person of integrity runs actuarial calculations on whether customers' lives are worth saving. Honesty, courage (to push back on cost-cutting pressure), and justice toward customers — none of these virtues permit knowingly selling a lethal product. |
| Justice (Rawls) | **Yes, retrofit** | Behind the veil of ignorance, you don't know if you'll be a Ford shareholder or a Pinto driver. Any rational agent choosing from that position would not accept a world where corporations assign dollar values to your life without your knowledge or consent. |

**Convergence**: 3 of 4 frameworks clearly say retrofit. Utilitarianism appears to diverge only when done sloppily — it converges when the full cost accounting includes long-run reputational and regulatory costs.

**Core tension**: Short-term shareholder value vs. non-negotiable duties to customers. The Ford memo's failure was treating utilitarianism as a one-period calculation that ignored repeated-game dynamics (regulation, reputation, punitive damages).

**Divergence pattern**: *Rights vs. narrow consequentialism.* This pattern appears whenever a company has private information about risk that customers lack. Deontology and virtue ethics are insensitive to the cost differential; utilitarianism appears to wobble but only because narrow framing excludes systemic costs.

---

## Case 2: Patagonia's Supplier Audit (Complicity by Inaction)

**Background**: An outdoor apparel brand audits its Tier 1 suppliers and discovers that a Tier 2 supplier (a fabric mill) uses forced overtime and withholds worker passports — indicators of labor trafficking. Cutting the Tier 2 supplier requires breaking contract with the Tier 1 supplier, losing 18% of production capacity, and likely a 6-month delivery gap.

**Decision**: Cut the supplier relationship immediately, or negotiate a remediation timeline?

**Stakeholders**: Workers at the mill, Tier 1 supplier (legitimate business, not responsible for Tier 2 behavior), company employees and shareholders, customers who buy the brand on its ethical reputation.

| Framework | Recommendation | Recommendation Detail |
|-----------|---------------|-----------|
| Deontology | **Immediate cut** | Passport confiscation is a rights violation of the first order. Continuing to purchase from that supply chain makes you a partial cause of the harm — not in intent, but in effect. Kant's categorical imperative applied to supply-chain sourcing: if every brand continued buying from traffickers pending "remediation timelines," forced labor would remain commercially viable. |
| Utilitarianism | **Negotiated timeline** | Immediate exit removes the brand's leverage over the mill. A 90-day remediation plan with verifiable milestones may produce faster, more durable improvement for workers than abandonment — especially if no other buyer will demand the same. Harm calculus: the mill's workers likely face worsened conditions if the customer departs without alternative leverage. |
| Virtue Ethics | **Immediate cut with public disclosure** | Courage and integrity both point toward not profiting from trafficking under any timeline. A virtuous organization treats the delay-and-monitor option as rationalization. The additional step of public disclosure follows from honesty — consumers are paying a premium for ethical sourcing. |
| Justice (Rawls) | **Negotiated timeline with worker representation** | From behind the veil of ignorance, you might be one of those workers. The question then becomes: what process would I prefer? Immediate abandonment by the brand that discovered the problem, or a monitored transition with 90-day binding milestones that include worker representation in the audit? The Rawlsian minimum is that the least-advantaged party (the workers) should have voice in the resolution. |

**Convergence**: All four frameworks agree that doing nothing is impermissible. They diverge only on the exit mechanism and timeline.

**Core tension**: Deontology focuses on the act of complicity; utilitarianism focuses on the outcome for workers. This is not merely abstract — both positions represent genuine tradeoffs for real people.

**Divergence pattern**: *Complicity vs. leverage.* This pattern recurs in supply-chain ethics. Deontologists exit immediately; consequentialists stay to fix. A useful heuristic from past cases: the leverage argument is valid only when (a) the company is a large enough buyer to have real influence, (b) milestones are binding and auditable, and (c) the timeline is short enough that harm doesn't compound.

---

## Case 3: Algorithmic Hiring (Disparate Impact)

**Background**: A logistics company deploys an ML model to screen job applications. The model was trained on historical hiring data. An internal audit shows the model rejects women at 2.3× the rate of men, and rejects candidates from two zip codes (historically redlined neighborhoods) at 3.1× the baseline rate. The model is more accurate than human screeners on 30-day and 90-day retention metrics.

**Decision**: Continue using the model, retrain it on balanced data (6-month delay), or revert to human screening?

**Stakeholders**: Applicants (especially women and residents of impacted zip codes), current employees (retention quality), shareholders (efficiency gains), regulators (EEOC), future applicants.

| Framework | Recommendation | Reasoning |
|-----------|---------------|-----------|
| Deontology | **Halt immediately** | The model encodes and automates historical discrimination. Using it is not a neutral act — it is an act of discrimination at scale, regardless of whether any individual reviewer holds biased intent. The categorical imperative: universalizing the use of historically biased data for hiring decisions would perpetuate structural inequality as a permanent feature of labor markets. Intent is not the test; effect on rights is. |
| Utilitarianism | **Retrain on balanced data, do not revert to humans** | The accuracy improvement over human screeners has real value. The harm is also real and quantifiable: roughly 130 qualified applicants per 100 hires are being incorrectly rejected based on protected characteristics. However, reverting to human screeners does not eliminate bias — it makes it less measurable. Utilitarianism favors the path that produces the best outcome, which is a retrained model, not the status quo or full reversion. |
| Virtue Ethics | **Halt immediately, transparent communication** | A just organization does not benefit from biased processes even unknowingly, and certainly not knowingly. Prudence requires acknowledging the flaw publicly; justice requires remediation. An organization that continues running the model while retraining prioritizes its own efficiency over the dignity of applicants — that is not the action of a virtuous institution. |
| Justice (Rawls) | **Halt immediately, set minimum equity threshold** | Behind the veil of ignorance, you don't know your zip code. Rawls's difference principle requires that any arrangement advantaging some (shareholders benefiting from efficiency) must not disadvantage the least well-off (job-seekers in marginalized neighborhoods). 3.1× rejection rate fails this test unconditionally. Rawls would require not just retraining but a binding threshold: the retrained model may not be redeployed until disparate impact is below a specified tolerance. |

**Convergence**: All frameworks oppose continuing the model as-is. Deontology and virtue ethics say halt now. Utilitarianism and Rawls agree the endpoint should be a better model, not no model.

**Core tension**: Aggregate efficiency vs. distributional equity. The company can produce better average outcomes while producing far worse outcomes for specific groups. This is the canonical form of the utilitarian minority problem — and the case that motivates Rawlsian ethics.

**Divergence pattern**: *Aggregate benefit vs. distributional harm.* This pattern is endemic to algorithmic systems. When it appears, pair the utilitarian analysis with a Rawlsian constraint: maximum aggregate utility subject to minimum disparity across protected groups.

---

## Case 4: Whistleblowing (Loyalty vs. Public Harm)

**Background**: A financial analyst at a pharmaceutical company discovers that clinical trial data for a recently approved drug was selectively reported — adverse events in the trial's oldest cohort were excluded from the FDA submission. The drug is now prescribed to 200,000 patients. Going external (FDA, press) violates confidentiality agreements and will likely end her career. Internal escalation has already been ignored twice.

**Decision**: Report externally to the FDA, or remain silent?

**Stakeholders**: 200,000 current patients, future patients, the analyst, the analyst's family, the company, the prescribing physicians, the FDA's credibility.

| Framework | Recommendation | Reasoning |
|-----------|---------------|-----------|
| Deontology | **Report externally** | Withholding material safety information from patients and regulators violates a duty of non-maleficence. The confidentiality agreement cannot be morally binding when its purpose is to conceal harm — contracts that require participating in wrongdoing are void as a matter of moral obligation. Categorical imperative: universalizing silent compliance with fraudulent clinical submissions would undermine the entire drug approval system. |
| Utilitarianism | **Report externally** | The harm is large-scale (200,000 patients at unknown adverse risk) and ongoing. The analyst's career damage is a real cost but not commensurate with the harm. If there is meaningful probability that the excluded data indicates serious adverse events, expected harm of silence dominates expected harm of disclosure. |
| Virtue Ethics | **Report externally** | Courage is a central virtue. The failure mode here is not cruelty but cowardice — choosing personal security over truth. A person of integrity does not allow contract language to override conscience when lives are at stake. Loyalty is also a virtue, but loyalty to a company that is actively harming patients is misplaced loyalty. |
| Justice (Rawls) | **Report externally** | From behind the veil of ignorance, you do not know if you are the analyst or one of the 200,000 patients. The patient position is clear: you would want disclosure. The analyst's position is less decisive — career consequences are real but not in the same category as potential physical harm to patients. |

**Convergence**: All four frameworks reach the same conclusion. This case is instructive not because of divergence but because of *why* frameworks that often conflict align here: the harm is large-scale, concrete, and ongoing; the competing interest (contractual loyalty) is strong but not capable of overriding all four frameworks simultaneously.

**Core tension**: Institutional loyalty vs. public safety. This pattern appears in financial fraud (Enron whistleblowers), environmental violations, and safety cover-ups. When all four frameworks agree on an action and the actor still faces real cost, the cost is borne by the individual to prevent harm to many — the ethical case is clear, the personal case is genuinely hard.

---

## Divergence Pattern Reference

These patterns generalize across business ethics cases:

| Pattern | Description | Which frameworks diverge | Resolution heuristic |
|---------|-------------|-------------------------|---------------------|
| **Rights vs. narrow consequentialism** | Company uses cost-benefit to override duties (Ford Pinto) | Deontology/virtue vs. poorly-framed utilitarianism | Expand utilitarian frame to include long-run systemic costs |
| **Complicity vs. leverage** | Exiting supply-chain vs. staying to reform (supplier audit) | Deontology exits; utilitarianism stays | Leverage argument valid only with binding milestones and real buyer power |
| **Aggregate benefit vs. distributional harm** | System performs well on average but harms specific groups (algorithmic hiring) | Utilitarianism may approve; Rawls blocks | Apply Rawlsian constraint: maximum aggregate utility subject to disparity floor |
| **Loyalty vs. public safety** | Confidentiality agreement covers up harm (whistleblowing) | Usually all frameworks agree to report | Unanimity is diagnostic: cost to actor is real but decision is not ambiguous |
| **Informed consent gap** | Company has private risk information users lack | Deontology/virtue say disclose; narrow consequentialism may calculate silence | Treat information asymmetry as rights violation by default |

---

## Using These Cases in Analysis

When applying the parent skill's output format to a new business dilemma, check which divergence pattern it most resembles:

1. If the dilemma involves **known private risk**, apply the Ford Pinto framing — rerun the utilitarian calculus with full long-run costs before accepting any apparent divergence.
2. If the dilemma involves **supply-chain distance**, apply the complicity/leverage distinction: leverage is only a valid argument with named milestones and real buyer power.
3. If the dilemma involves **algorithmic or statistical decisions**, always add the distributional audit — aggregate metrics hide group-level harm.
4. If all four frameworks agree, the ethical case is clear but this does not mean the personal cost is zero. Acknowledge the cost explicitly; do not pretend the decision is costless for the actor.

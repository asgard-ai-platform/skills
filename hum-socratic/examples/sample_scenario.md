直接寫入檔案：

```markdown
# Example: Coaching an Engineering Lead on the "We Must Migrate to Microservices" Belief

## Scenario

**Context:** Stackline is a 120-person B2B SaaS company (Series B, $18M ARR) offering supply-chain analytics. Priya, the VP of Engineering, wants to coach her engineering lead, Daan, who has become increasingly convinced that the company must migrate their Rails monolith to microservices "or we'll never scale past our current bottlenecks." Daan is preparing a migration proposal for the exec team.

Priya asks the AI to help her design a Socratic questioning sequence she can use in a 1:1 with Daan — not to tell him he's wrong, but to help him stress-test his own reasoning before he presents to the C-suite.

**Daan's starting claim:**
> "Our monolith is the reason we've had three major outages this quarter. If we don't move to microservices in the next six months, we won't be able to handle the growth we're projecting."

---

## Analysis

### Step 1 — Clarify the Claim Precisely

Before probing assumptions, Priya needs to understand what Daan means. "Monolith caused outages" and "microservices enable growth" are two separate claims bundled together.

**Clarifying questions to open with:**

- "When you say the monolith *caused* the outages — do you mean a specific component failed, or that the architecture made recovery slower?"
- "Which growth metric are you projecting will be blocked: request throughput, deployment frequency, or team velocity?"

*Expected insight:* Daan will likely realize the outages had specific root causes (a memory leak in the order-processing module, not architectural coupling) that may not require full decomposition.

---

### Step 2 — Probe Assumptions

Daan's claim rests on several hidden assumptions. Surface them one at a time.

**Assumption questions:**

- "You're assuming microservices would have prevented these outages. What would the same failure have looked like in a microservices architecture?"
- "What are you assuming about the team's ability to operate distributed systems? Do we have on-call runbooks for cross-service tracing today?"

*Expected insight:* The team of 14 engineers has no experience with service meshes, distributed tracing, or independent deployment pipelines. The assumption that microservices *reduce* risk may invert under current staffing.

---

### Step 3 — Request Evidence

**Evidence question:**

- "What do the post-mortems say about the root cause of each of the three outages? Were they caused by tight coupling between modules, or by bugs in isolated code paths?"

*Expected insight:* Post-mortems show two outages were caused by a faulty third-party payment webhook handler and one by a Redis misconfiguration — neither caused by monolithic coupling. The causal story doesn't match the evidence.

---

### Step 4 — Introduce Counter-Perspectives

**Perspective question:**

- "Stack Overflow ran a monolith until 2019 and served 1.5 billion requests per month. Basecamp has stayed monolithic through 20+ years of growth. What would engineers at those companies say about our situation at $18M ARR?"

*Expected insight:* The constraint may not be architecture but deployment discipline — Stackline doesn't have CI/CD guardrails, feature flags, or zero-downtime deploys. All of those are fixable inside a monolith.

---

### Step 5 — Explore Implications

**Implication questions:**

- "If we begin the microservices migration in Q3, what happens to the three features promised to Tier-1 customers in Q4? Who owns those timelines during the migration?"
- "If the migration takes 14 months instead of 6 — which migrations of this scope often do — what does that mean for our Series C fundraise narrative?"

*Expected insight:* Daan hasn't modeled the opportunity cost. A 12–18 month migration at a company six months from a fundraise is a material strategic risk, not just a technical decision.

---

### Step 6 — Synthesize (IRON LAW Checkpoint)

After 2–3 questions in each phase, Priya pauses and summarizes before continuing:

> *"So your core concern is reliability and growth capacity — and you're linking that to the monolith. But so far it sounds like the outages had specific, fixable causes, and the scaling concern is really about deployment speed and team velocity, not request throughput. Is that a fair summary? What am I missing?"*

This checkpoint prevents Daan from feeling interrogated. It demonstrates Priya heard him and gives him a chance to affirm or correct the framing before the session continues.

---

### Step 7 — Meta-Question

- "If you were a skeptical investor reading your own proposal, what's the strongest argument *against* migrating right now?"

*Expected insight:* Asking Daan to steelman the opposition is the final test. If he can articulate decisive counter-arguments himself, the proposal either addresses them or he discovers they're disqualifying.

---

## Result

```markdown
# Socratic Inquiry: Should Stackline Migrate to Microservices?

## Starting Position
"Our Rails monolith caused three Q3 outages. We must migrate to microservices
within 6 months or we won't scale to our growth projections."

## Question Sequence
1. [Clarification] "When you say the monolith caused the outages — was it
   architectural coupling, or did the architecture make recovery slower?"
   → Expected insight: Surfaces whether the claim is causal or correlational

2. [Clarification] "Which growth metric is at risk: request throughput,
   deployment frequency, or team velocity?"
   → Expected insight: Separates three distinct problems with different solutions

3. [Assumption] "What would the same payment-webhook failure look like in a
   microservices architecture with our current ops maturity?"
   → Expected insight: Distributed systems can amplify blast radius without
     strong observability; surfaces the team-readiness gap

4. [Evidence] "What do the three post-mortems say was the root cause?"
   → Expected insight: Two outages were isolated bugs, not coupling failures;
     the causal link between architecture and outages dissolves

5. [Perspective] "Stack Overflow served 1.5B req/month as a monolith until
   2019. What would their engineers say about our situation at $18M ARR?"
   → Expected insight: Architecture is rarely the constraint at Stackline's
     scale; deployment discipline is the actual bottleneck

6. [Implication] "If migration takes 14 months instead of 6, what happens to
   Q4 commitments and the Series C timeline?"
   → Expected insight: Opportunity cost of migration has not been modeled;
     risk is strategic, not just technical

## IRON LAW Checkpoint (after questions 2–3)
"So your core concern is reliability and growth capacity — you're linking
it to the monolith. But the outages had specific, fixable causes and the
scaling concern is about deployment speed, not throughput. Is that fair?
What am I missing?"

## Target Insight
Daan arrives at a revised proposal: fix the specific root causes (webhook
isolation, Redis config management, zero-downtime deploys), adopt modular
monolith patterns for the highest-churn modules, and defer full microservices
decomposition until the team has grown to 20+ engineers or a clear throughput
ceiling is demonstrated in production metrics — not before.
```

**What changed:** Daan still owns the conclusion — Priya never told him he was wrong. By walking through the evidence and implications himself, his revised proposal is scoped to the actual problem, defensible to skeptical investors, and avoids betting 14 engineer-months on an architectural premise the post-mortems don't support.
```

現在把它寫入正確路徑：

```
hum-socratic/examples/sample_scenario.md
```

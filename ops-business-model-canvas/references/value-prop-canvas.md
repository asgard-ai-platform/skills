# Value Proposition Canvas

The Value Proposition Canvas (VPC) is a zoom-in on two BMC blocks: **Value Propositions** and **Customer Segments**. It exists to prevent the most common BMC failure mode — writing a value prop that doesn't map to real customer needs.

---

## Structure

The VPC has two halves:

```
┌─────────────────────────────┬──────────────────────────────┐
│         VALUE MAP           │      CUSTOMER PROFILE        │
│         (left)              │         (right)              │
│                             │                              │
│  Products &    Pain         │  Customer     Pains          │
│  Services   Relievers       │  Jobs                        │
│               ↕             │     ↕                        │
│            Gain             │              Gains           │
│           Creators          │                              │
└─────────────────────────────┴──────────────────────────────┘
                        FIT ←→
```

You always fill the **Customer Profile first**, then build the Value Map to address it. Working in the opposite direction produces solutions looking for problems.

---

## Customer Profile (3 components)

### 1. Customer Jobs

What the customer is trying to accomplish — NOT what they want from you.

Three types:

| Job Type | Definition | Example (B2B SaaS for HR teams) |
|----------|-----------|----------------------------------|
| **Functional** | Practical task | "Process monthly payroll without errors" |
| **Social** | How they appear to others | "Look competent to the CFO during audits" |
| **Emotional** | How they want to feel | "Feel confident we're legally compliant" |

**Rule**: List jobs in priority order. The top 1-2 functional jobs are usually where value prop leverage is highest. Social and emotional jobs explain WHY customers switch providers.

### 2. Pains

Negative outcomes, obstacles, and risks that occur when doing the job — or that prevent the customer from even trying.

Three types:

| Pain Type | Definition | Example |
|-----------|-----------|---------|
| **Outcomes** | Things that go wrong | "Manual payroll errors trigger employee complaints" |
| **Obstacles** | Things that prevent action | "Our legacy system can't integrate with new benefits software" |
| **Risks** | What might go wrong | "If we mis-classify contractors, we get fined" |

**Rate each pain**: Extreme (blocks the job entirely) → Moderate → Mild. Only extreme and moderate pains are worth addressing in a value prop.

### 3. Gains

Benefits the customer expects, desires, or would be surprised by.

Four types (in ascending order of value):

| Gain Type | Definition | Example |
|-----------|-----------|---------|
| **Required** | Minimum expected | "Calculates correct tax withholding" |
| **Expected** | Normal expectation | "Has a reporting dashboard" |
| **Desired** | Nice-to-have | "Integrates with Slack for approval workflows" |
| **Unexpected** | Would delight | "Proactively flags upcoming compliance changes before they affect us" |

**Required and Expected gains don't differentiate** — they're table stakes. Your value prop should reach for Desired and Unexpected.

---

## Value Map (3 components)

### 1. Products & Services

The catalog of what you offer. Not benefits — just the actual things (features, services, information, tools).

- "Automated payroll calculation engine"
- "One-click tax filing integration"
- "Compliance alert system"

These are the raw materials. They create value only through Pain Relievers and Gain Creators.

### 2. Pain Relievers

How your products and services **explicitly reduce specific pains** from the Customer Profile.

Format: `[Product/Service] reduces [specific pain] by [mechanism]`

| Pain Reliever | Addresses Pain |
|--------------|----------------|
| "Automated calculation engine eliminates manual spreadsheet errors" | Outcome pain: payroll errors |
| "Native integration with 40+ HRIS systems" | Obstacle pain: legacy system incompatibility |
| "Built-in compliance rules updated quarterly" | Risk pain: contractor mis-classification fines |

**IRON LAW carry-over**: Every pain reliever must trace to a named pain. If it doesn't, it's a feature looking for a problem.

### 3. Gain Creators

How your products and services **explicitly create gains** the customer wants.

| Gain Creator | Addresses Gain |
|-------------|----------------|
| "One-click reports formatted for CFO review" | Social gain: look competent to CFO |
| "Mobile approval workflows" | Desired gain: Slack/mobile integration |
| "60-day ahead compliance change alerts" | Unexpected gain: proactive compliance notice |

---

## Fit Test

Fit occurs when your Value Map **specifically addresses** the Customer Profile. There are three levels:

| Fit Level | Definition | Test |
|-----------|-----------|------|
| **Problem–Solution Fit** | You address real jobs and extreme pains | Can you map each pain reliever to an extreme/moderate pain? |
| **Product–Market Fit** | Customers actually pay | Do customers renew? Refer? Pay without heavy discounting? |
| **Business Model Fit** | Revenue justifies cost | Does the revenue stream in the BMC support the cost structure? |

VPC handles Level 1. Levels 2 and 3 require real market evidence.

---

## Worked Example: B2B Accounting Software

### Customer Profile — Finance Director, 50-200 person company

**Customer Jobs** (priority order):
1. Close monthly books accurately and on time (functional — critical)
2. Produce board-ready financial reports (functional — critical)
3. Demonstrate fiscal control to board/investors (social)
4. Avoid restatements and regulatory fines (functional + emotional)

**Pains** (rated):
- Extreme: Month-end close takes 5+ days due to manual data reconciliation
- Extreme: Errors found after reports are distributed require embarrassing corrections
- Moderate: Can't give real-time spend visibility to department heads
- Moderate: Audit prep requires pulling data from 4 separate systems
- Mild: Reports look dated/ugly compared to competitors' board decks

**Gains** (by type):
- Required: Accurate double-entry bookkeeping, bank reconciliation
- Expected: Standard financial statements (P&L, balance sheet, cash flow)
- Desired: Automated variance analysis with commentary suggestions
- Unexpected: "CFO co-pilot" that drafts board narrative from the numbers

---

### Value Map — Accounting Software Product

**Products & Services:**
- Automated bank feed reconciliation
- Real-time multi-entity consolidation engine
- AI-assisted variance analysis
- Board report template library

**Pain Relievers:**

| Pain Reliever | → | Pain Addressed |
|--------------|---|----------------|
| Automated bank feed reconciliation (matches 95%+ transactions automatically) | → | Month-end takes 5+ days |
| Pre-close validation engine flags mismatches before close, not after | → | Corrections after distribution |
| Unified data layer pulls from ERP, payroll, expenses in one place | → | Audit prep across 4 systems |

**Gain Creators:**

| Gain Creator | → | Gain Addressed |
|-------------|---|----------------|
| Department self-serve dashboards with drill-down | → | Desired: real-time spend visibility |
| AI commentary that drafts variance explanations | → | Unexpected: CFO co-pilot for board narrative |
| Template library with pixel-perfect board slide output | → | Mild pain (ugly reports) + social gain |

---

### Fit Assessment

```
✓ Extreme pains covered: 2/2
✓ Moderate pains covered: 2/2  
✓ Desired gains addressed: 1
✓ Unexpected gain addressed: 1
⚠ Required/Expected gains: must verify table stakes are met before emphasizing differentiation

RISK: "AI commentary" (unexpected gain) is high-value but unproven — needs customer validation
```

---

## Common Fit Failures

### Failure 1: Pain Reliever Without a Pain

**Symptom**: You list "beautiful mobile UI" but no customer job required mobility.

**Fix**: Audit every pain reliever. If it doesn't map to an extreme or moderate pain, demote it to a nice-to-have feature or cut it from the value prop narrative.

### Failure 2: Feature Stacking on Required Gains

**Symptom**: Value prop says "accurate calculations, fast reporting, easy import" — all required gains.

**Fix**: Required gains are table stakes. Acknowledge them in one sentence, then pivot to Desired/Unexpected gains.

### Failure 3: Single-Segment Mistake on Multi-Sided Business

**Symptom**: You fill one Customer Profile when you have two distinct segments (e.g., marketplace buyers and sellers).

**Fix**: In the BMC, multi-sided platforms need **two separate VPCs** — one per segment. They will have completely different jobs, pains, and gains. A single blended profile produces a value prop that fits no one well.

### Failure 4: Gain Creator That Creates Unwanted Gains

**Symptom**: "Automated emails to department heads" — which Finance Director didn't want; she wants to control information flow.

**Fix**: Validate gains through interviews, not assumptions. What seems like a gain to the builder may be a pain to the customer.

### Failure 5: Confusing Jobs With Solutions

**Symptom**: Customer job listed as "use our API to sync data."

**Fix**: Jobs are always technology-agnostic. "Sync data" is a solution. The job is "maintain a single source of truth across systems." Reframe jobs to surface solution flexibility.

---

## Interview Guide for Customer Profile

Use these questions to fill the profile from primary research rather than assumptions:

**For Customer Jobs:**
- "Walk me through how you handle [domain] today, from start to finish."
- "What does 'done' look like for this? How do you know you succeeded?"
- "When you do this well, what does your boss or board see?"

**For Pains:**
- "What's the most frustrating part of this process?"
- "Has something ever gone wrong here that you're still thinking about?"
- "What would make you reluctant to switch to a new tool?"

**For Gains:**
- "If this worked perfectly, what would that look like?"
- "What would surprise you if a tool actually did this?"
- "What do other tools do that you wish this one did?"

**Signal to watch for**: Unprompted emotional language ("that killed us," "that was embarrassing," "that was a game changer") marks extreme pains and unexpected gains — prioritize these.

---

## VPC → BMC Handoff

Once the VPC is complete, translate its outputs back into the BMC:

| VPC Output | → | BMC Block |
|-----------|---|-----------|
| Customer Segment (from profile) | → | Customer Segments |
| Value Map summary | → | Value Propositions |
| Jobs that require ongoing interaction | → | Customer Relationships |
| Channels implied by the buying journey | → | Channels |
| Key Resources required to deliver pain relievers | → | Key Resources |
| Key Activities required to deliver pain relievers | → | Key Activities |
| Cost of delivering the value map | → | Cost Structure |

The VPC does not directly generate Revenue Streams — that requires pricing research separate from jobs-to-be-done analysis.

---

## Quick Reference: Fill Order

```
1. Customer Jobs        (start here — always)
2. Pains               (derived from jobs)
3. Gains               (derived from jobs)
4. Products & Services (inventory what you have/plan)
5. Pain Relievers      (map each to a pain)
6. Gain Creators       (map each to a gain)
7. Fit Assessment      (are extreme pains covered?)
```

Never start with the Value Map. If you do, you're describing a solution and reverse-engineering a customer — a reliable path to building something nobody wants.

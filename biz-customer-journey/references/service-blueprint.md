# Service Blueprint

Service Blueprint extends a Customer Journey Map by adding the **backstage operations** that deliver each frontstage touchpoint. Where the journey map asks "what does the customer experience?", the service blueprint asks "what has to work behind the scenes to make that happen?"

Use this when you need to:
- Diagnose *why* a customer pain point occurs (root cause is usually backstage)
- Design a new service from both the customer and operational perspective
- Align cross-functional teams on who owns which parts of the experience

---

## The Five Swim Lanes

A service blueprint is read left-to-right (time / journey stages) with five horizontal swim lanes, separated by two boundary lines:

```
┌─────────────────────────────────────────────────────────────────┐
│  PHYSICAL EVIDENCE                                              │  ← what customer sees/touches
├─────────────────────────────────────────────────────────────────┤
│  CUSTOMER ACTIONS                                               │
├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ LINE OF INTERACTION ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤
│  FRONTSTAGE (Visible Employee / System Actions)                 │
├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ LINE OF VISIBILITY ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┤
│  BACKSTAGE (Invisible Employee / System Actions)                │
├─────────────────────────────────────────────────────────────────┤
│  SUPPORT PROCESSES                                              │  ← systems, vendors, infra
└─────────────────────────────────────────────────────────────────┘
```

### Boundary Lines Explained

**Line of Interaction** — the point where the customer directly contacts the service (in-person, phone, UI). Everything above this line the customer initiates; everything below delivers it.

**Line of Visibility** — separates what the customer can see (frontstage) from what they cannot (backstage). A waiter taking your order is frontstage; the kitchen is backstage. A checkout button is frontstage; the payment gateway call is backstage.

---

## Swim Lane Definitions

| Lane | Contains | Examples |
|------|----------|---------|
| Physical Evidence | Tangible artifacts the customer encounters | App UI, packaging, email, receipt, store layout |
| Customer Actions | Steps the customer takes | Searches, clicks, fills form, waits, calls support |
| Frontstage | Direct customer-facing actions (human or system) | Chatbot response, cashier greeting, confirmation email sent |
| Backstage | Internal actions invisible to customer | Kitchen prep, fraud check, inventory query, manager approval |
| Support Processes | Infrastructure, third-party systems, shared services | Payment processor, CRM, logistics partner, database |

---

## Building the Blueprint: Step-by-Step

### Step 1: Borrow the Journey Stages

Start from the journey map you already built. The column headers of the blueprint are your five stages: Awareness → Consideration → Decision → Usage → Advocacy.

### Step 2: Fill Physical Evidence First

For each stage, list every artifact the customer encounters. Be exhaustive — a missing artifact often explains a gap in customer understanding.

Checklist per stage:
- [ ] What do they see on screen / in person?
- [ ] What do they receive (email, SMS, physical item)?
- [ ] What do they hold in their hand?

### Step 3: Fill Customer Actions

Pull directly from the journey map. These are what the customer **does**, not feels. Verbs only: searches, taps, reads, calls, waits, returns.

### Step 4: Map Frontstage Actions

For each customer action, trace the direct service response:
- Who or what responds? (human agent, chatbot, automated system)
- What is the response? (confirmation message, quote generated, item picked from shelf)

Link each frontstage action to the customer action it serves with an arrow in the diagram.

### Step 5: Map Backstage Actions

For each frontstage action, ask: "What has to happen behind the scenes to make this possible?"

Common backstage actions:
- Data lookups (inventory check, credit check, account history)
- Human decisions (pricing approval, fraud flag review)
- Preparation (food prep, order picking, document generation)
- Coordination (scheduling, dispatch, escalation routing)

### Step 6: Map Support Processes

For each backstage action, identify the systems or vendors it depends on:
- Internal systems: CRM, ERP, OMS, POS
- External vendors: payment processor, logistics partner, email service provider
- Shared services: authentication, analytics, customer data platform

### Step 7: Mark Failure Points and Wait Times

Add two annotation types across all lanes:

- **⚡ Failure point** — where errors occur with measurable frequency
- **⏱ Wait time** — how long the customer waits at this step

These are the primary inputs for prioritizing backstage fixes.

---

## Worked Example: Food Delivery App (Lunch Order)

Using the same persona from `SKILL.md`: 30-year-old office worker, ordering lunch on a food delivery app.

This example focuses on the **Decision → Usage** stages since that's where the pain points were identified.

```
STAGE:              │  DECISION                    │  USAGE (Active)              │  USAGE (Post-delivery)
────────────────────┼──────────────────────────────┼──────────────────────────────┼────────────────────────────
PHYSICAL EVIDENCE   │  Cart screen, delivery fee   │  "Preparing order" screen    │  Food packaging, app rating
                    │  displayed, payment UI       │  map with rider location     │  prompt
────────────────────┼──────────────────────────────┼──────────────────────────────┼────────────────────────────
CUSTOMER ACTIONS    │  Sees NT$60 fee + NT$200 min │  Waits, tracks rider         │  Receives food, notices
                    │  → adjusts cart or abandons  │                              │  leaked packaging
                    │  → enters payment            │                              │  → rates 3/5 stars
────────────────────┼──────────────────────────────┼──────────────────────────────┼────────────────────────────
                    LINE OF INTERACTION
────────────────────┼──────────────────────────────┼──────────────────────────────┼────────────────────────────
FRONTSTAGE          │  Fee calculation displayed   │  Push notifications sent     │  Rating prompt displayed
                    │  Payment gateway UI rendered │  ETA updates shown on map    │  24h after delivery
                    │                              │                              │
                    ⚡ Failure: fee display logic   ⚡ Failure: ETA shown as       ⚡ Failure: prompt appears
                    triggers 40% cart abandonment  static; doesn't update when   even when order was late
                    (data-backed)                  kitchen is slow               or damaged
────────────────────┼──────────────────────────────┼──────────────────────────────┼────────────────────────────
                    LINE OF VISIBILITY
────────────────────┼──────────────────────────────┼──────────────────────────────┼────────────────────────────
BACKSTAGE           │  Order validation service    │  Kitchen receives order      │  Rating stored to DB
                    │  Dynamic pricing engine      │  Rider assignment algorithm  │  Merchant reputation score
                    │  Fraud check                 │  Kitchen marks "ready"       │  updated
                    │  ⏱ Fraud check: avg 1.2s     │  ⏱ Avg kitchen prep: 18min  │
                    │  (invisible but adds latency)│  (app says 10min → gap)     │
────────────────────┼──────────────────────────────┼──────────────────────────────┼────────────────────────────
SUPPORT PROCESSES   │  Payment processor (Stripe)  │  Maps API (Google)           │  CRM (Salesforce)
                    │  Fraud vendor (Sift)         │  Push notification service   │  Merchant dashboard
                    │  OMS (in-house)              │  OMS (in-house)              │
```

### Reading the Example

The **ETA mismatch** pain point (customer sees 25min, waits 35min) has its root cause in the backstage: the kitchen prep time averages 18 minutes but the ETA algorithm uses a static 10-minute assumption. The frontstage notification is accurate to what it receives, but the backstage data is wrong. Without the blueprint, this looks like a notification problem; with it, the fix is clearly in the kitchen-time estimation algorithm.

The **packaging leak** pain point is not visible in the blueprint at all — it's a fulfillment quality issue at the restaurant, which would appear in the support processes lane as a merchant SLA gap. The blueprint reveals where to intervene: merchant quality scoring, packaging standards enforcement, or rider pickup inspection.

---

## Failure Point Triage Protocol

Once failure points are marked, triage using this 2×2:

```
                     HIGH customer impact
                            │
          Backstage fix     │     Frontstage fix
          (invisible but    │     (customer-facing;
          high leverage)    │     higher visibility)
                            │
───────────────────────────────────────────────────
Low fix effort             │                High fix effort
                            │
          Quick wins:       │     Major initiatives:
          data, config,     │     process redesign,
          algorithm tuning  │     system rebuild
                            │
                     LOW customer impact
```

Prioritize: **High customer impact × Low fix effort** first (backstage quick wins). The ETA algorithm fix is an example — customer impact is high (sets expectations), fix effort is medium (update the model), and it's invisible to customers (no UI redesign needed).

---

## Common Backstage Root Causes for Frontstage Pain

| Frontstage Symptom | Typical Backstage Root Cause |
|--------------------|------------------------------|
| Slow page / response | Synchronous dependency chain; missing cache |
| Inconsistent pricing | Multiple pricing engines not synchronized |
| "We'll get back to you" delays | No SLA on internal escalation routing |
| Wrong ETA / delivery promise | Static assumption in estimation algorithm |
| Agent gives wrong info | CRM data stale; no single source of truth |
| Onboarding steps feel redundant | Data collected twice due to system silos |
| Failed payment on first attempt | Fraud model over-triggering; no fallback |

---

## When to Use Blueprint vs Journey Map

| Question | Use |
|----------|-----|
| Where does the customer get frustrated? | Journey Map |
| Why does that frustration occur? | Service Blueprint |
| What's the customer experience design? | Journey Map |
| Who owns which part of the service delivery? | Service Blueprint |
| What does this feel like emotionally? | Journey Map |
| What systems need to change? | Service Blueprint |

Journey map first, blueprint second. The journey map tells you *where to look*; the blueprint tells you *what to fix*.

---

## Scope Guidance

Blueprinting the entire service in one diagram becomes unreadable. Narrow the scope:

1. **One persona, one journey** — same rule as journey maps
2. **One or two stages deep** — pick the stages with the highest pain or business impact
3. **One level of backstage** — go one level deeper than you normally see, not infinitely deep

For a complex service (hospital, bank, airline), run separate blueprints per service line or per stage cluster (e.g., "onboarding only", "support interaction only").

---

## Annotation Conventions

Use these consistently across all blueprints in a project:

| Symbol | Meaning |
|--------|---------|
| ⚡ | Known failure point (attach data: rate, severity) |
| ⏱ | Wait time (attach measured or estimated duration) |
| → | Direct dependency between lanes |
| ←→ | Bidirectional data flow |
| 🔴 | High priority fix |
| 🟡 | Medium priority |
| 🟢 | Working well — leave alone |

---

## Relationship to SKILL.md Concepts

**Backstage vs frontstage** (Gotcha in SKILL.md): The service blueprint is the structural tool that enforces this distinction. By drawing the Line of Visibility explicitly, teams stop mapping internal processes as customer experience.

**Moments of Truth** (SKILL.md Step 3): Each Moment of Truth should be exploded into a mini-blueprint. If the "delivery fee shock" is a Moment of Truth, diagram all five swim lanes for just that moment to find the root cause.

**Iron Law — Map Reality**: In the blueprint's support processes lane, map the systems that *actually* exist, not the ideal architecture. If the team uses a spreadsheet instead of a CRM, draw a spreadsheet.

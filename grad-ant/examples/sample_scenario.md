# Example: QR Code Payment Adoption in Taipei Traditional Markets

## Scenario

A product manager at LINE Pay Taiwan is conducting a post-mortem on the 2019–2021 QR code payment rollout. The technology succeeded rapidly in convenience stores and night markets aimed at tourists but stalled badly in traditional wet markets (傳統市場) despite identical marketing budgets and incentive structures. She asks: "What actually held the convenience store network together, and why couldn't we replicate it in wet markets?"

---

## Analysis

### Step 1: Identify the Controversy

The phenomenon: **QR code payment becoming normalized in some retail contexts but not others, despite identical technology and incentive programs.** Following ANT, the question is not "why did vendors resist?" but "what network was successfully assembled in one context and failed to assemble in the other?"

### Step 2: Map the Actants

#### Convenience Store Network
| Actant | Type | Role in Network | Interests |
|--------|------|-----------------|-----------|
| LINE Pay commercial team | Human | Focal actor; defines the problem | Market share, transaction volume |
| 7-Eleven / FamilyMart HQ | Human | Key ally; mandates adoption | Corporate digital KPIs, data collection |
| POS terminal firmware | Non-human | Enrollment device; forces cashier workflow compliance | — |
| QR code sticker at register | Non-human | Interessement device; materializes the network at point of sale | — |
| MoF tax incentive (5% cashback) | Non-human | Enrollment device; aligns consumer interest | — |
| Cashier training manual | Non-human | Interessement device; scripts cashier behavior | — |
| Consumer smartphone | Non-human | Required actant; without it the network cannot close | — |
| Receipt lottery system | Non-human | Pre-existing enrollment; consumers already watch receipts | — |

#### Wet Market Network (Attempted)
| Actant | Type | Role in Network | Interests |
|--------|------|-----------------|-----------|
| LINE Pay commercial team | Human | Focal actor | Same as above |
| Individual stall vendors | Human | Resistant actants | Cash flow speed, avoidance of taxable records |
| Market association leaders | Human | Gatekeepers; partially enrolled, not committed | Maintaining vendor trust |
| QR code printout (laminated) | Non-human | Weak interessement device; no system enforcement | — |
| Vendor's personal smartphone | Non-human | Notification-only; unreliable network connectivity | — |
| Cash float & change coins | Non-human | Competing actant; deeply embedded in transaction ritual | — |
| Tax bureau audit records | Non-human | Threatening actant; vendors feared electronic trails | — |
| MoF cashback (same 5%) | Non-human | Enrollment device; failed — consumer-side only, no vendor incentive | — |

### Step 3: Trace the Four Moments of Translation

#### Convenience Store Network

**Problematization**  
LINE Pay framed the problem as: "Convenience stores cannot remain competitive without digital payment infrastructure." This positioned LINE Pay as the obligatory passage point (OPP) — if corporate HQ wanted digital KPIs, they had to route through LINE Pay's merchant agreement. The framing successfully enrolled HQ decision-makers because it aligned with their own investor-facing narratives.

**Interessement**  
Three devices locked actors into their roles simultaneously:
- POS terminal firmware updates made QR scanning the **default first screen** — cashiers had to actively bypass it to use cash, reversing the effort calculus
- The 5% MoF cashback was **co-branded as LINE Pay benefit**, not a government policy, strengthening brand association
- Consumer LINE app notifications triggered at store entry, priming payment intent before the register

**Enrollment**  
Cashiers accepted the scripted role (ask "LINE Pay?", scan, done) because the firmware made it as fast as cash. Corporate HQ enrolled because transaction data fed their loyalty analytics. Consumers enrolled because cashback was immediate and visible in-app.

**Mobilization**  
By Q3 2020, "LINE Pay accepted here" had become a proxy claim for "this store is modern." Market association surveys, franchise audit reports, and consumer reviews all began citing QR payment availability — each enrolling new actors on behalf of the stabilized network without LINE Pay's direct involvement.

#### Wet Market Network (Failed)

**Problematization**  
LINE Pay framed the same problem: "Wet markets are losing younger shoppers to supermarkets." But the OPP failed — market association leaders controlled vendor trust, and LINE Pay could not route through them without offering vendor-side benefits. The problematization reached only consumers, not vendors.

**Interessement**  
The laminated QR code printout was a **weak interessement device**: it required the vendor to manually check their phone, accept settlement delays (T+1 versus immediate cash), and create an electronic transaction record. No device enforced the role. The tax bureau's digital audit trail became a **counter-interessement** device — vendors actively discouraged QR payments to avoid income documentation.

**Enrollment**  
Partial and fragile. ~12% of wet market vendors enrolled in pilot districts, primarily younger second-generation vendors. The majority refused, citing: settlement speed, phone reliability in humid market conditions, and tax exposure. Market association leaders remained in a "wait and see" stance, never mobilizing their networks in support.

**Mobilization**  
Never reached. No non-human spokespersons (audits, association newsletters, vendor forums) began representing the network autonomously. The laminated QR code could not speak for itself the way firmware-enforced POS screens could.

### Step 4: Assess Network Stability

**Convenience Store Network — Stable**
- Stabilizing factors: POS firmware as iron enrollment device; corporate mandate removes individual choice; consumer cashback creates self-reinforcing demand
- Black boxes formed: By 2021, no cashier questioned why QR scanning was the default — its internal construction (LINE Pay's merchant negotiation, MoF policy design) became invisible
- Residual fragility: Smartphone battery / network outages; merchant fee negotiation renegotiation risk

**Wet Market Network — Dissolved**
- Points of fragility: No non-human enforcement mechanism; tax exposure as counter-actant stronger than cashback incentive; humidity and connectivity undermined smartphone as reliable actant
- Network never stabilized because enrollment remained voluntary with no obligatory passage point the focal actor controlled

---

## Result

```markdown
## ANT Analysis: LINE Pay QR Code Adoption, Taipei 2019–2021

### Focal Actor and Problematization
- Focal actor: LINE Pay Taiwan commercial team
- Obligatory passage point (convenience stores): Corporate HQ digital KPI mandate — vendors had to route through LINE Pay to satisfy HQ
- OPP (wet markets): FAILED — market association leaders never accepted the OPP framing; vendors retained exit options

### Actant Map (summary)
| Actant | Type | Convenience Store | Wet Market |
|--------|------|-------------------|------------|
| POS firmware | Non-human | Strong enrollment device | Absent |
| QR code | Non-human | Enforced default | Voluntary printout |
| MoF cashback | Non-human | Consumer enrollment | Consumer-only; no vendor benefit |
| Tax audit trail | Non-human | Neutral | Counter-interessement |
| Corporate HQ mandate | Human | Key ally | No equivalent |

### Translation Process
1. **Problematization**: Identical framing in both contexts; succeeded only where focal actor could control the OPP
2. **Interessement**: POS firmware was decisive — it removed vendor choice; laminated printout could not replicate this
3. **Enrollment**: Convenience stores: mandatory via firmware; Wet markets: voluntary, dominated by tax-exposure counter-interest
4. **Mobilization**: Convenience stores: black-boxed by 2021; Wet markets: never mobilized

### Network Stability Assessment
- Stabilizing factors (C-stores): Non-human enforcement (firmware), corporate mandate, consumer demand loop
- Points of fragility (wet markets): No non-human enforcement; competing actant (tax exposure) stronger than incentive actant (cashback)
- Black boxes formed: POS scan-first behavior; "LINE Pay = modern store" semiotics in franchise context

### Implications
1. The technology was identical — the networks were not. Success required a non-human enrollment device that removed optionality.
2. Removing the POS firmware update from the convenience store rollout would likely have produced wet-market-level adoption.
3. To stabilize the wet market network, LINE Pay would need to either (a) neutralize the tax-exposure counter-actant via guaranteed MoF amnesty framing, or (b) find a non-human device that enforces vendor-side enrollment — neither of which was in scope.
```

**Key ANT takeaway for the PM**: The failure was not vendor "resistance" (a social explanation) nor technology inadequacy (a technical explanation). It was a **network assembly failure** — the wet market rollout lacked a non-human actant capable of enforcing enrollment and converting the tax bureau from counter-actant to neutral. Diagnosis via ANT reframes the next intervention: find the equivalent of firmware, not a better marketing campaign.

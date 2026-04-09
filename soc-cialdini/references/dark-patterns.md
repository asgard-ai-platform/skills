# Dark Patterns: Cialdini Principles as Manipulation

Dark patterns are interface or messaging designs that exploit persuasion principles against the user's interests. This reference maps each Cialdini principle to its common dark-pattern corruptions, provides a detection test, and documents real-world examples.

---

## The Manipulation Test (From SKILL.md Iron Law)

Before each example below, apply this binary test:

> **Would the person feel grateful or deceived if they knew the technique was being used?**

If the honest answer is "deceived," it's a dark pattern. If "grateful" (or neutral), it's ethical influence.

A more operational version:

```
Is the information used to trigger the principle...
  ├─ TRUE?         → proceed to interests check
  └─ FALSE/FAKE?   → MANIPULATION (always)

If true, does triggering this principle serve...
  ├─ the target's interests?       → ethical influence
  ├─ both parties' interests?      → ethical influence
  └─ only the persuader's?         → MANIPULATION
```

---

## Principle-by-Principle Dark Pattern Catalog

### 1. Reciprocity → Compromised Reciprocity

**Ethical form:** Give something genuinely useful with no strings attached; the recipient is free to decline the return favor.

**Dark pattern corruption:**

| Variant | Mechanism | Detection signal |
|---------|-----------|-----------------|
| **Unsolicited gift trap** | Send unrequested gift, then immediately ask for donation/purchase. The social pressure to reciprocate is manufactured. | "We sent you this free [X], now we're asking for..." within the same message |
| **Obligation escalation** | Start with a tiny free gift, then present a disproportionately large ask framed as "just reciprocating" | Free pen → pressure to buy NT$50,000 insurance package |
| **Fake free trial** | "Free" trial requires credit card, auto-renews, and cancellation is buried in account settings | Hidden auto-renewal terms, no cancellation reminder |

**Worked example — Obligation escalation:**

A charity sends a package containing address labels and a small notepad (cost: ~NT$15). The enclosed letter says: "We've already given you a gift. Now we're asking you to give back." Donation conversion: 35% vs. 18% for plain ask. The manufactured reciprocity is real (the gift was real), but the implied equivalence (NT$15 gift → NT$500 donation) exploits the norm asymmetrically.

**Test:** Was the gift given freely with no implicit contract? Can the recipient decline the return ask without social penalty the persuader has engineered?

---

### 2. Commitment & Consistency → Entrapment Sequences

**Ethical form:** Help people make and keep commitments that genuinely serve their goals.

**Dark pattern corruption:**

| Variant | Mechanism | Detection signal |
|---------|-----------|-----------------|
| **Sunk cost trap** | Get user to invest time/data, then reveal the real cost | Onboarding 15 steps → credit card wall at step 14 |
| **Bait-and-switch commitment** | Get commitment to a principle, then apply it to a specific product the person wouldn't have chosen | "You believe in supporting local business, right?" → "So you'll buy our product" |
| **Roach motel** | Easy in, impossible out — relies on consistency bias to keep user from leaving | Easy signup, impossible cancellation (dark pattern **and** Commitment exploitation) |
| **Public commitment coercion** | Force public declaration to prevent future defection | "Share on Facebook to continue" gates that create artificial social accountability |

**Worked example — Roach motel (quantified):**

A subscription service buries cancellation behind: Settings → Account → Billing → Manage Plan → Contact Support → 48-hour wait → retention call. Each step exploits consistency ("I already started cancelling, I should finish") while simultaneously adding friction that a rational actor would quit. The average user attempts cancellation 2.3 times before succeeding (UX industry data). Each abandoned attempt reinforces the "I'm a member" identity.

---

### 3. Social Proof → Fabricated or Misleading Consensus

**Ethical form:** Accurate representation of real users' behavior or opinions.

**Dark pattern corruption:**

| Variant | Mechanism | Detection signal |
|---------|-----------|-----------------|
| **Astroturfing** | Fake reviews, paid reviews without disclosure | Review dates cluster suspiciously, all 5-star, generic language |
| **Misleading aggregation** | "10,000 satisfied customers" includes free signups, trials, churned users | No definition of "customer" or time period |
| **Manufactured FOMO** | "23 people are looking at this right now" — number is fabricated or inflated | Booking sites: the "X viewing" counter often doesn't reflect real users |
| **Cherry-picked testimonials** | Genuine testimonials from statistical outliers presented as typical | "I lost 30kg in 3 months!" with no disclosure that this is 1-in-500 result |
| **Dead social proof** | Displaying follower counts/logos that are outdated, purchased, or irrelevant | "As seen in" with logos of obscure outlets; Twitter followers from 2018 |

**Worked example — Manufactured FOMO (booking sites):**

A hotel booking platform shows "Only 2 rooms left!" and "18 people viewing." Independent research (Booking.com 2019 EU investigation) found these counters frequently refreshed artificially or reflected searches across all dates, not the specific night selected. The EU required clarification. The original implementation:
- Triggered Scarcity (only 2 left) **and** Social Proof (18 viewing) simultaneously
- Both signals were misleading
- Both pass "true?" check → FALSE → MANIPULATION

---

### 4. Liking → Parasocial Exploitation

**Ethical form:** Genuine relationship-building, authentic brand personality.

**Dark pattern corruption:**

| Variant | Mechanism | Detection signal |
|---------|-----------|-----------------|
| **Parasocial debt** | Creator builds intimacy ("you're my family"), then monetizes with guilt framing | "After everything I've shared with you, I just need you to buy this once" |
| **Fake personalization** | "Hi [First Name], I thought of you specifically" — automated mail to 500,000 people | Personalization tokens that are clearly template-driven |
| **Manufactured similarity** | Adopt target audience's identity markers dishonestly to trigger liking | Political consultants deliberately using local dialect/slang to seem "one of us" |
| **Beauty/attractiveness exploitation** | Use attractive person to imply product benefit transfers | Cologne ads with no product information, just attractive people |

**Note:** Liking-based dark patterns are the hardest to detect because genuine relationships exist on a spectrum with manufactured ones. The test is whether the similarity/relationship is **authentic** or **performed specifically to extract compliance**.

---

### 5. Authority → Fake or Irrelevant Credentials

**Ethical form:** Relevant expert in relevant domain provides honest assessment.

**Dark pattern corruption:**

| Variant | Mechanism | Detection signal |
|---------|-----------|-----------------|
| **Credential laundering** | Real credential in irrelevant domain presented as authority | "PhD" in biology endorsing financial products |
| **Fake credentials** | Fabricated titles, certifications, associations | "Certified by the Institute of [vague-sounding thing]" — check if institute exists |
| **Authority theater** | Uniforms, title language, official-looking design with no actual authority | Phishing emails designed to look like government notices |
| **Sponsored-but-undisclosed** | Paid endorsement without disclosure | Influencer paid post with no #ad tag (also illegal in many jurisdictions) |
| **False attribution** | Quote attributed to authority who never said it | "Einstein said: [motivational platitude]" |

**Worked example — Credential laundering:**

A Taiwanese supplement brand runs ads with "Dr. Chen" (real MD, real credentials, gastroenterologist) endorsing their sleep supplement. The credential is genuine, but gastroenterology expertise does not confer authority on sleep supplement efficacy. The audience hears "doctor = science = this works." The authority is real; the relevance is manufactured.

**Detection check:** Is the authority's expertise **directly relevant** to the specific claim being endorsed? A cardiologist endorsing a running shoe's cardiovascular benefit = plausible. A cardiologist endorsing a running shoe's cushioning technology = credential laundering.

---

### 6. Scarcity → Fake Urgency

**Ethical form:** Accurate representation of genuinely limited availability or time.

**Dark pattern corruption:**

| Variant | Mechanism | Detection signal |
|---------|-----------|-----------------|
| **Evergreen countdown** | Timer resets when it hits zero, or when user revisits page | Open in incognito — does the timer reset? |
| **Fake stock limits** | "Only 3 left!" for a digital product or vastly overstocked item | Digital goods cannot be "only 3 left" |
| **Artificial waitlists** | Waitlist exists to manufacture exclusivity, not because capacity is limited | Product launches with "waitlist" for items available day-of |
| **Permanent "sale" pricing** | "Was NT$1,999, NOW NT$999" — was price never actually charged | Check price history tools (e.g., CamelCamelCamel for Amazon) |
| **Loss framing on gains** | "Don't miss out!" for something the user never had — manufactured loss | Framing ordinary purchase opportunities as losses to be avoided |

**Worked example — Evergreen countdown (measurable):**

A landing page shows: "🔥 Special offer ends in: 01:47:23." If you reload the page, the timer resets to 02:00:00. This was documented in a 2021 FTC action against multiple e-commerce operators. The scarcity signal is entirely fabricated. Conversion lift from fake countdown: ~12-18% vs. no countdown. This is pure extraction — the customer makes a faster decision based on false information.

**Code pattern to detect evergreen timers:**

```javascript
// Red flag: timer initialized from current time + fixed offset
// rather than from a real deadline timestamp
const deadline = Date.now() + (2 * 60 * 60 * 1000); // always 2 hours from now
```

```javascript
// Legitimate: timer initialized from a fixed future date
const deadline = new Date('2026-03-31T23:59:59+08:00').getTime();
```

---

## The Stacking Problem

Dark patterns become more dangerous when combined, because each principle covers a different cognitive system:

```
Fake scarcity         → System 1 (fast, fear-of-loss)
Fabricated reviews    → System 1 (social validation)
Fake authority        → System 2 bypass (defer to expert)
Sunk cost trap        → System 2 rationalization
```

A single dark pattern can be noticed. Stacked dark patterns create overlapping cognitive pressure that makes rational evaluation nearly impossible.

**Example stack (e-commerce dark pattern):**
1. Countdown timer [fake scarcity]
2. "18 people viewing" [fake social proof]
3. "Only 2 left" [fake scarcity, second instance]
4. "⭐⭐⭐⭐⭐ 4,847 reviews" [unverified social proof]
5. Checkout requires account creation [commitment trap]
6. Auto-added travel insurance [manipulation via opt-out default]

Each layer individually might not trigger skepticism. Combined, they compress decision time to prevent any deliberation.

---

## Detection Checklist

Use this when auditing a campaign, landing page, or sales process you didn't design:

```
SCARCITY
□ Is the quantity limit real and verifiable?
□ Is the time limit fixed (not evergreen)?
□ Does the limit apply to what's actually limited (digital vs. physical)?

SOCIAL PROOF
□ Are reviews verified purchasers?
□ Are "X people viewing" numbers based on real sessions?
□ Are testimonials representative, not cherry-picked outliers?
□ Are before/after claims based on typical results?

AUTHORITY
□ Does the credential match the domain of the claim?
□ Is the endorsement disclosed as paid if it is?
□ Does the authority actually exist?

RECIPROCITY
□ Is the gift given with genuine no-strings intent?
□ Is auto-renewal clearly disclosed?
□ Is cancellation as easy as signup?

COMMITMENT
□ Is the path OUT as visible as the path IN?
□ Are sunk costs (time invested in onboarding) used to pressure continued commitment?

LIKING
□ Is expressed similarity genuine or performed?
□ Are parasocial relationships monetized with guilt framing?
```

---

## Legal and Platform Exposure

Dark patterns that exploit Cialdini principles may violate:

| Jurisdiction | Regulation | Relevant Dark Patterns |
|---|---|---|
| EU | GDPR, DSA (Digital Services Act) | Fake reviews, fake urgency, misleading social proof |
| US | FTC Act Section 5 | Undisclosed endorsements, fake countdown timers |
| Taiwan | 公平交易法 (Fair Trade Act) §21 | False advertising, misleading claims including fake scarcity |
| Taiwan | 消費者保護法 (Consumer Protection Act) | Subscription traps, roach motel cancellation |

Relevant case precedent:
- **EU v. Booking.com (2019)**: Required removal of misleading urgency and availability messages
- **FTC v. Sunday Riley (2019)**: Fake reviews posted by employees under instruction
- **台灣公平會 (2022)**: Several e-commerce operators fined for "限時特價" that was not time-limited

---

## The Asymmetry Principle

The same technique can be ethical or a dark pattern depending on **who benefits from the decision**:

```
Technique: Scarcity message
  ↓
Is the scarcity real?
  ├─ NO → Dark pattern (always)
  └─ YES
       ↓
       Does acting on it serve the buyer's interests?
         ├─ YES (genuine deal, limited stock of useful product) → Ethical
         └─ NO (pressure to buy something they don't need faster) → Dark pattern
```

The principle isn't scarcity = bad. Fake scarcity = bad. Real scarcity used to manufacture urgency around a harmful or wasteful purchase = also bad.

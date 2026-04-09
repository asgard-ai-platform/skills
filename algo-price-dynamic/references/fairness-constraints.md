# Fairness Constraints in Dynamic Pricing

Dynamic pricing is mathematically neutral but socially charged. This document defines
concrete constraints an agent can implement to keep dynamic pricing legally defensible
and commercially sustainable.

---

## Why Fairness Fails Silently

Revenue-maximizing algorithms have no natural preference for fairness. Left unconstrained,
they will:

- Charge higher prices to users with inelastic demand (detected via device, location, or
  purchase history)
- Raise prices precisely when buyers are most desperate (emergency supplies, last-minute
  travel, storm-season hotels)
- Create price surfaces that correlate with protected class membership even without
  explicit targeting

None of these are intentional design choices — they emerge from optimization alone.
The constraint layer must be explicit.

---

## Taxonomy of Fairness Violations

| Violation Type | Mechanism | Example | Legality |
|---|---|---|---|
| **Individual price discrimination** | Different prices for same product, same time, based on inferred identity | Charging iOS users more than Android users | Legal in most jurisdictions but PR toxic |
| **Proxy discrimination** | Pricing variable correlates with protected class | ZIP-code surcharges that map to race | Potentially illegal (disparate impact) |
| **Emergency gouging** | Large price increase during declared emergency | 5× hotel price during hurricane evacuation | Illegal in most US states |
| **Bait-and-switch via surge** | Advertise base price, surge triggers at checkout | "From $99" but surge makes it $340 at purchase | FTC deceptive practices risk |
| **Loyalty punishment** | Returning customers shown higher prices (reservation price inferred) | SaaS renewal pricing higher than new customer offer | Legal but churn-inducing |

---

## The Three Permissible Segmentation Axes

Charge different prices only along these three axes. Any other basis requires legal review.

### 1. Time

Price varies by *when* the purchase occurs, not *who* makes it.

```
P(t) = P_base × f(t)
```

Where `t` is time of purchase (or time remaining until service/event). Everyone who
buys at time `t` pays `P(t)`. This is advance-purchase discounting, peak/off-peak
pricing, early-bird pricing.

**Permissible because:** The same price is available to all buyers at that moment.

### 2. Channel / Bundle

Price varies by *how* the product is packaged or *where* it is purchased.

Examples: airport kiosk vs. mobile app; single room vs. room + breakfast bundle.

**Permissible because:** The product itself differs, so different prices are economically
justified.

### 3. Quantity / Commitment

Price varies by volume purchased or duration of commitment.

Examples: bulk discount, annual subscription vs. monthly, group booking.

**Permissible because:** Larger commitments reduce seller risk and transaction costs.

---

## Prohibited Axes (Without Legal Sign-off)

- **Device type** (iOS vs. Android, desktop vs. mobile) — often correlates with income
- **Inferred income** from browsing history, neighborhood, or spending signals
- **Race, religion, national origin, sex, age** — protected classes under anti-discrimination law
- **Prior purchase history used to set reservation price** — legal in most places, but see
  Loyalty Punishment above for commercial risk

---

## Anti-Gouging Constraint Implementation

Most US states define gouging as price increases above a threshold (typically 10-25%)
during a declared state of emergency. Build this as a hard gate.

```python
GOUGING_THRESHOLD = 0.10  # 10% above pre-emergency price

def apply_anti_gouging_gate(
    recommended_price: float,
    pre_emergency_price: float,
    emergency_active: bool,
) -> float:
    if not emergency_active:
        return recommended_price
    ceiling = pre_emergency_price * (1 + GOUGING_THRESHOLD)
    return min(recommended_price, ceiling)
```

**Pre-emergency price** must be stored *before* the emergency declaration, not
calculated from recent data (which is already distorted by demand surge). Log the
snapshot with a timestamp.

---

## Individual Price Discrimination: The Device-Type Case Study

### The Problem

A/B test reveals that iOS users convert at $149 but Android users convert at $99.
Naive revenue maximization would serve $149 to iOS and $99 to Android.

### Revenue Calculation (Why It's Tempting)

Assume 1,000 potential buyers, 60% iOS, 40% Android.

| Segment | Buyers | Price | Revenue |
|---|---|---|---|
| iOS | 600 | $149 | $89,400 |
| Android | 400 | $99 | $39,600 |
| **Discriminated total** | **1,000** | | **$129,000** |

Uniform at $99:

| All buyers | 1,000 | $99 | $99,000 |

Uniform at $149 (lower conversion, assume 60% buy):

| Buyers | 600 | $149 | $89,400 |

So device-based discrimination looks like a $30,000 gain over uniform $99.

### Why You Shouldn't Do It

1. **PR risk**: Discovered by any journalist or researcher, this becomes a headline.
   Uber lost ~$5M in revenue in one quarter following the iOS price discrimination story.
2. **Proxy discrimination liability**: iOS ownership correlates with income, which
   correlates with race in some markets. This is a disparate impact claim waiting to happen.
3. **VPN/browser switching**: Sophisticated users learn to spoof Android UA to get
   the lower price, destroying the segmentation.

### The Permissible Alternative

Use *channel* rather than *device* to justify price differences:

- iOS App Store purchase: $149 (Apple takes 30%, so your net is $104.30)
- Web/Android purchase: $99 (lower transaction fee, your net is $93)

Now the price difference is tied to a real cost difference, which is economically
and legally defensible.

---

## Fairness Constraint Decision Framework

Run this check before any price recommendation is delivered:

```
INPUT: recommended_price, context
       context includes: user_id, device, location, timestamp, emergency_flag,
                         segment_basis, pre_emergency_price

STEP 1 — Emergency gate
  IF emergency_flag:
    recommended_price = min(recommended_price,
                            pre_emergency_price × 1.10)

STEP 2 — Segmentation basis audit
  IF segment_basis NOT IN ["time", "channel", "quantity", "bundle"]:
    REJECT — log violation, fall back to time-only pricing

STEP 3 — Rate-of-change limit
  IF (recommended_price - last_price) / last_price > MAX_SINGLE_CHANGE:
    recommended_price = last_price × (1 + MAX_SINGLE_CHANGE)
  (MAX_SINGLE_CHANGE = 0.25 for most retail use cases)

STEP 4 — Floor / ceiling enforcement
  recommended_price = clamp(recommended_price, price_floor, price_ceiling)

OUTPUT: constrained_price, constraint_log[]
```

The `constraint_log` is essential — record every time a constraint fires so that
product and legal teams can audit the system.

---

## Rate-of-Change Limit (Avoiding Shock Pricing)

Even time-based pricing can cause backlash if prices jump suddenly. Set a maximum
rate of change per update cycle.

```
MAX_SINGLE_CHANGE = 0.25   # 25% per update cycle
MAX_DAILY_CHANGE  = 0.50   # 50% vs. previous day's open price
```

**Formula:**

```
P_next = clamp(
    P_recommended,
    P_current × (1 - MAX_SINGLE_CHANGE),
    P_current × (1 + MAX_SINGLE_CHANGE)
)
```

This prevents the algorithm from responding to a demand spike with a 3× price jump
in one step, which customers experience as predatory even when the math is correct.

**Implementation note:** The daily limit requires storing `P_open` (price at start
of business day / pricing cycle). Don't recalculate from the current price — that
allows the limit to drift via multiple small jumps.

---

## Transparency Requirements

Customers don't need to see the algorithm, but they do need to understand *why*
prices change. Minimum disclosure requirements by context:

| Context | Minimum Disclosure |
|---|---|
| Ride-sharing | Show surge multiplier before user confirms |
| Hotel / airline | Show "prices change frequently" at search results |
| E-commerce | Do NOT show personalized prices without disclosure |
| SaaS renewal | Show new customer price if renewal price differs |

For e-commerce specifically: if you show different prices to different users (even via
permissible channel segmentation), you must disclose this or face FTC deceptive
practices risk. The safest approach is to not show personalized prices in the same
session as non-personalized prices.

---

## Strategic Customer Problem: The Fairness Interaction

The "strategic customer" problem (customers delay purchase expecting price drops) is
described in SKILL.md. Fairness constraints interact with this:

**Wrong fix:** Never drop prices (maintains revenue but sacrifices volume).

**Wrong fix:** Drop prices only for "new" customers (loyalty punishment — see above).

**Correct fix:** Use *advance-purchase discounting* — prices are lower early and rise
as the event/expiration approaches. This is time-based (permissible), rewards
commitment (quantity axis), and doesn't require identifying individual customers.

```
P(t) = P_ceiling × (1 - discount_factor × (t / T))

Where:
  t = days before expiration
  T = total advance-purchase window (e.g., 30 days)
  discount_factor = maximum discount rate (e.g., 0.30 for 30% early discount)
```

At `t = T` (30 days out): `P = P_ceiling × (1 - 0.30) = 0.70 × P_ceiling`
At `t = 0` (day of): `P = P_ceiling`

This trains customers to buy early, not to wait — which is the opposite of the
strategic customer problem — without any individual identification.

---

## Monitoring for Proxy Discrimination

Even with permissible segmentation axes, run a quarterly disparate impact audit:

1. Export all transactions for the period with: price paid, zip code, timestamp, channel
2. Append census data: median household income and racial composition by zip code
3. Run a regression: `price_paid ~ income_quintile + channel + time_of_day`
4. Flag if `income_quintile` coefficient is statistically significant after controlling
   for channel and time

If income predicts price *after* controlling for your legitimate segmentation variables,
your permissible axes are functioning as proxies. Investigate which feature is the leak.

Common leaks: delivery ZIP as a price variable (correlates with income), "premium"
channel that requires credit card (excludes lower-income unbanked customers).

---

## Summary Constraint Checklist

Before deploying a dynamic pricing update:

- [ ] Anti-gouging ceiling defined and pre-emergency price snapshot stored
- [ ] Segmentation basis limited to time / channel / quantity / bundle
- [ ] No device-type or inferred-income pricing variables in the model features
- [ ] Rate-of-change limits set (per-cycle and per-day)
- [ ] Price floor and ceiling enforced as hard constraints, not soft targets
- [ ] Surge indicator shown to customer before confirmation (for ride-sharing / on-demand)
- [ ] Constraint log implemented and being written on every constraint-fire event
- [ ] Disparate impact audit scheduled (quarterly minimum)

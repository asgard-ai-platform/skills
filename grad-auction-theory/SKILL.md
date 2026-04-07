---
name: "grad-auction-theory"
description: "Apply auction theory to compare the four canonical auction formats and assess revenue equivalence. Use this skill when the user needs to choose an auction format, evaluate bidding strategies, or determine when revenue equivalence breaks down due to risk aversion, asymmetry, or correlated values."
metadata:
  category: "WP-27 賽局與制度經濟"
  tags: ["auction-theory", "revenue-equivalence", "Vickrey-auction", "English-auction", "Dutch-auction", "first-price-sealed-bid", "winners-curse"]
---

# Auction Theory: Four Canonical Formats and Revenue Equivalence

## Overview

Auction theory analyzes strategic bidding behavior across different selling mechanisms. The four canonical formats — English (ascending), Dutch (descending), first-price sealed-bid, and second-price sealed-bid (Vickrey) — generate identical expected revenue under standard assumptions. The Revenue Equivalence Theorem (RET) is the central benchmark; deviations from its assumptions drive all practical auction design decisions.

## When to Use

- Choosing among auction formats for selling goods, spectrum, procurement, or ad slots
- Analyzing bidder strategy (bid shading, sniping, jump bidding) under a specific format
- Evaluating whether a proposed auction achieves optimal revenue or efficiency

## When NOT to Use

- Posted-price or negotiated sales where no competitive bidding occurs
- Multi-unit auctions with complex complementarities (use combinatorial auction frameworks)
- The seller has no commitment power to enforce auction rules

## Assumptions

```
IRON LAW: Revenue equivalence holds ONLY with risk-neutral bidders,
independent private values (IPV), and symmetric bidders — violate ANY
assumption and auction format matters.
```

- Single indivisible object for sale
- Bidders are risk-neutral expected-utility maximizers
- Values are independently and identically distributed (IPV)
- Bidders are symmetric (same distribution of values)
- Payment is a function of bids only (no externalities)

## Methodology

**Step 1 — Identify the Value Model**
Classify the setting: independent private values (IPV), common values, or affiliated values. IPV means each bidder knows their own value with certainty; common values mean the object has one true value unknown to all; affiliated values generalize both.

**Step 2 — Derive Equilibrium Bidding Strategies**
For each auction format, solve for the Bayesian Nash equilibrium. In second-price / English auctions under IPV, bidding true value is dominant. In first-price / Dutch auctions, bidders shade below true value: b(v) = E[Y1 | Y1 < v] where Y1 is the highest competing value.

**Step 3 — Apply Revenue Equivalence or Identify Violations**
Under RET assumptions, all four formats yield the same expected revenue. Check for violations: (a) risk aversion favors first-price over second-price; (b) asymmetric bidders break equivalence; (c) common values introduce the winner's curse and favor English auctions (Milgrom-Weber linkage principle); (d) budget constraints, entry costs, or reserve prices create format-dependent effects.

**Step 4 — Recommend Format and Parameters**
Given the identified deviations, recommend the auction format, optimal reserve price (r* where r* = v0 + [1 - F(r*)] / f(r*) in the IPV case), and any additional design features (e.g., entry fees, information disclosure policy).

## Output Format

```markdown
## Auction Analysis: [Context]

### Value Model
- **Type**: IPV / Common / Affiliated
- **Distribution**: [bidder value distribution]
- **Number of bidders**: [N]
- **Risk attitude**: risk-neutral / risk-averse

### Format Comparison
| Format              | Equilibrium Strategy         | Expected Revenue | Notes        |
|--------------------|------------------------------|-----------------|--------------|
| English (ascending) |                              |                 |              |
| Dutch (descending)  |                              |                 |              |
| First-price sealed  |                              |                 |              |
| Second-price sealed |                              |                 |              |

### Revenue Equivalence Assessment
- **RET holds?** Yes / No
- **Violation source**: [risk aversion / asymmetry / common values / other]
- **Ranking**: [which format generates highest revenue and why]

### Optimal Reserve Price
- **r*** = [value]
- **Derivation**: [brief]

### Recommendation
[Chosen format, reserve price, and rationale]
```

## Gotchas

- The winner's curse is a common-value phenomenon — it does not apply in pure IPV settings, yet bidders often behave as if it does
- Revenue equivalence is about *expected* revenue; variance differs across formats (first-price has lower variance)
- Optimal reserve price excludes some efficient trades — the seller sacrifices efficiency for revenue
- In practice, English auctions reveal more information, which helps with affiliated values (Milgrom-Weber linkage principle)
- Collusion is easier in second-price and English auctions; first-price is more robust to bidder rings
- Online auctions (eBay-style) are not pure English auctions — hard close times, proxy bidding, and sniping change equilibrium behavior

## References

- Vickrey, W. (1961). "Counterspeculation, Auctions, and Competitive Sealed Tenders." *Journal of Finance*.
- Riley, J. & Samuelson, W. (1981). "Optimal Auctions." *American Economic Review*.
- Milgrom, P. & Weber, R. (1982). "A Theory of Auctions and Competitive Bidding." *Econometrica*.
- Krishna, V. (2010). *Auction Theory*, 2nd ed. Academic Press.

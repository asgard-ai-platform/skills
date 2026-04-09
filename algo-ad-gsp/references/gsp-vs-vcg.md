# GSP vs VCG: Mechanism Comparison for Ad Auctions

## Core Difference in One Sentence

VCG charges each winner their **externality** on others (truthful, incentive-compatible); GSP charges each winner the **next-competitor's ad rank divided by their own quality score** (strategically manipulable, but simpler to operate).

---

## Mechanism Definitions

### GSP Payment Rule

For K slots, sort advertisers by AdRank descending. Winner in position k pays:

```
CPC_k = AdRank_{k+1} / QualityScore_k
```

The last winner (position K) pays:

```
CPC_K = ReservePrice / QualityScore_K
```

Where `AdRank_i = Bid_i × QualityScore_i`.

### VCG Payment Rule

VCG charges each winner the **social welfare loss** they impose on others by occupying their slot.

Define `CTR_k` as the click-through rate multiplier for slot k (e.g., slot 1 = 1.0, slot 2 = 0.7, slot 3 = 0.4).

Assume advertiser i wins slot k. In a world without advertiser i, the remaining advertisers shift up. VCG payment for winner i:

```
VCG_i = Σ_{j=k+1}^{K+1} value_j × (CTR_{j-1} - CTR_j)
```

Where `value_j = Bid_j × QualityScore_j` for the advertiser who would occupy position j-1 in i's absence.

Equivalently, the per-click payment is:

```
VCG_CPC_i = (1 / CTR_k) × Σ_{j=k+1}^{K+1} value_j × (CTR_{j-1} - CTR_j)
```

---

## Worked Numerical Example

**Setup:** 3 advertisers, 2 slots, reserve price = 0.

| Advertiser | Bid | QS | AdRank |
|------------|-----|----|--------|
| A          | 3.0 | 8  | 24     |
| B          | 4.0 | 5  | 20     |
| C          | 2.0 | 9  | 18     |

**Slot CTR multipliers:** Slot 1 = 1.0, Slot 2 = 0.6, (Slot 3 = 0.3, off-page)

**Slot assignments** (by AdRank): A → slot 1, B → slot 2. C loses.

---

### GSP Payments

```
CPC_A = AdRank_B / QS_A = 20 / 8 = 2.50
CPC_B = AdRank_C / QS_B = 18 / 5 = 3.60
```

**Total platform revenue per query:**
```
Revenue_GSP = CPC_A × CTR_1 + CPC_B × CTR_2
            = 2.50 × 1.0 + 3.60 × 0.6
            = 2.50 + 2.16 = 4.66
```

---

### VCG Payments

**For A (position 1):** Without A, B takes slot 1, C takes slot 2.
- B's gain from A's presence: B moves from slot 1 (CTR=1.0) to slot 2 (CTR=0.6). B *loses* clicks — but that means A *imposes no positive externality by leaving slot 2 to B*. More precisely:

Without A present:
- B occupies slot 1, earns value `20 × 1.0 = 20`
- C occupies slot 2, earns value `18 × 0.6 = 10.8`
- Total others' welfare without A = 20 + 10.8 = **30.8**

With A present:
- B occupies slot 2, earns `20 × 0.6 = 12`
- C earns 0 (knocked out)
- Total others' welfare with A = 12 + 0 = **12**

A's payment = externality A imposes = 30.8 − 12 = **18.8 total**, i.e., `VCG_total_A = 18.8`.

Per-click: `VCG_CPC_A = 18.8 / (CTR_1 × QS_A)` — but VCG is usually expressed as total payment, not per-click, since it's mechanism-theoretic. Converting:

```
VCG_CPC_A = 18.8 / QS_A / CTR_1 = 18.8 / 8 / 1.0 = 2.35
```

**For B (position 2):** Without B, C moves to slot 2.
- C's welfare with B absent = `18 × 0.6 = 10.8`
- C's welfare with B present = 0

B's externality = 10.8 − 0 = **10.8 total**.

```
VCG_CPC_B = 10.8 / QS_B / CTR_2 = 10.8 / 5 / 0.6 = 3.60
```

**Total platform revenue per query:**
```
Revenue_VCG = VCG_total_A + VCG_total_B
            = 18.8 + 10.8 = 29.6  (total clicks-weighted)
```

Per-impression:
```
Revenue_VCG = VCG_CPC_A × CTR_1 × QS_A + VCG_CPC_B × CTR_2 × QS_B
```

Actually for revenue comparison use dollar totals:
```
Revenue_VCG = 2.35 × 1.0 + 3.60 × 0.6 = 2.35 + 2.16 = 4.51
Revenue_GSP = 2.50 × 1.0 + 3.60 × 0.6 = 2.50 + 2.16 = 4.66
```

**Result:** GSP extracts slightly more revenue here. This is a known theoretical property — VCG minimizes payment to incentivize truth-telling; GSP can extract more but sacrifices incentive compatibility.

---

## Summary Table: Same Inputs, Different Outcomes

| Metric        | GSP    | VCG    |
|---------------|--------|--------|
| A's CPC       | 2.50   | 2.35   |
| B's CPC       | 3.60   | 3.60   |
| Platform rev  | 4.66   | 4.51   |
| Truth-telling | ✗ (no) | ✓ (yes)|
| Dominant strategy | ✗  | ✓      |

---

## Why GSP Yields Higher Revenue (Intuition)

VCG pays each winner only for the externality they impose on *others* — it deliberately does not charge them for the value of the slot itself relative to being unranked. GSP inadvertently charges more because the payment formula `AdRank_{k+1} / QS_k` doesn't reduce to the externality formula. In this example, A pays 2.50 under GSP vs 2.35 under VCG — the extra 0.15 is "overcharge" that VCG would not extract but GSP does.

---

## Incentive Compatibility: Why It Matters

**VCG:** Truthful bidding (`Bid_i = true value per click`) is a dominant strategy. Regardless of what others bid, you cannot do better than bidding truthfully. Proof sketch: deviating either (a) wins you a worse slot than your truthful outcome, or (b) overpays without improving your slot.

**GSP:** Truthful bidding is NOT a dominant strategy. Consider advertiser A with true value = 3.0 (CPC), QS = 8, AdRank = 24. If A bids truthfully:
- Wins slot 1, pays 2.50 → profit = (3.0 − 2.50) × clicks_1

But if A bids lower (e.g., bid = 2.4, AdRank = 19.2) to deliberately take slot 2:
- Wins slot 2, pays AdRank_C / QS_A = 18/8 = 2.25 → profit = (3.0 − 2.25) × clicks_2

Whether this is profitable depends on `CTR_1 / CTR_2` ratio vs price differential. If slot 2 is 60% of slot 1's clicks but slot 2 is 10% cheaper, the math might favor slot 2.

**Key implication for analysis:** Observed bids in GSP auctions do NOT equal true willingness to pay. Inferring advertiser valuations from GSP bids requires equilibrium correction (see Nash equilibrium analysis in `references/gsp-equilibrium.md`).

---

## Envy-Freeness: GSP's Partial Substitute for Incentive Compatibility

GSP lacks a dominant strategy equilibrium, but it does admit **envy-free Nash equilibria** under certain conditions (Edelman, Ostrovsky, Schwarz 2007).

An outcome is **envy-free** if no advertiser prefers to swap their slot assignment + payment with any other winner's slot assignment + payment.

Formally: advertiser i in slot k does not envy advertiser j in slot m (m < k) if:
```
(value_i - CPC_i) × CTR_k ≥ (value_i - CPC_j) × CTR_m
```

The "Symmetric Nash Equilibrium" of GSP (the EOS equilibrium) coincides with the VCG outcome in terms of **allocative efficiency** — same slot assignments — but with higher payments. This means:

- GSP and VCG produce the **same winner allocation**
- VCG produces lower payments (better for advertisers)
- GSP extracts more surplus (better for the platform)

---

## When Each Mechanism Applies

| Scenario | Use GSP | Use VCG |
|----------|---------|---------|
| Repeated auction (advertisers learn) | ✓ | — |
| Single-shot sealed bid | — | ✓ |
| Platform wants max revenue (short-term) | ✓ | — |
| Platform wants truthful signals for ML | — | ✓ |
| Advertiser has budget constraints | ✓ (simpler to reason about) | — |
| Multi-item combinatorial auction | — | ✓ |
| Regulatory requirement for transparency | — | ✓ |

---

## Why Google Uses GSP Instead of VCG

Google introduced VCG for AdSense in 2002 (Overture patent issues aside), then switched to GSP-like mechanisms. The practical reasons:

1. **Revenue:** VCG's lower payments transfer surplus to advertisers, not Google.
2. **Simplicity:** GSP's payment rule is explainable as "you pay the next person's score / your QS." VCG externality calculations are harder to audit.
3. **Budget-pacing compatibility:** GSP payments are predictable enough for advertisers to set daily budgets without constantly computing externalities.
4. **Quality Score opacity as a lever:** Google's QS incorporates expected CTR, relevance, and landing page quality — factors only Google observes. This asymmetry breaks VCG's truthfulness guarantee anyway (VCG requires all valuations to be common knowledge or at least private values; if the platform controls QS, VCG incentive compatibility is compromised by design).

**Practical conclusion:** In a world where the platform controls a non-transparent quality multiplier, VCG's incentive compatibility advantage largely disappears. GSP with QS is a pragmatic compromise — not theoretically pure, but operationally tractable and more revenue-extracting.

---

## CPC Formula Reference

| Mechanism | Position k payment (per click) |
|-----------|-------------------------------|
| **GSP**   | `AdRank_{k+1} / QS_k` |
| **VCG**   | `(1 / CTR_k) × Σ_{j=k+1}^{K+1} AdRank_j × (CTR_{j-1} − CTR_j) / QS_k` |
| **First-Price** | `Bid_k` (no reduction, not used in search) |

For position K (last winner), replace `AdRank_{K+1}` with `ReservePrice × QS_k` in GSP, and the sum collapses to `ReservePrice × (CTR_K − 0) / CTR_K = ReservePrice` in VCG.

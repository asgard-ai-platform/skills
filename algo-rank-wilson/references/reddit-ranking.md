# Reddit's Wilson-Based Ranking Algorithm

Reddit's **"Best"** comment-sorting algorithm is one of the most widely cited real-world deployments of Wilson Score. It was published by Evan Miller (2009) and adopted by Reddit to replace naïve upvote-ratio sorting. This document covers the exact parameters Reddit uses, why they differ from the textbook 95% CI, and a worked implementation.

---

## The Core Problem Reddit Solved

Before "Best", Reddit sorted comments by **net score** (upvotes − downvotes) or by **average ratio**. Both fail:

| Method | Failure mode |
|---|---|
| Net score | New comments never catch old ones; popular posts bury new replies |
| Upvote ratio | 1 upvote / 1 total (100%) beats 999 upvotes / 1000 total (99.9%) |
| Wilson lower | Correctly penalizes small samples — IRON LAW enforced |

---

## Reddit's Exact Parameters

Reddit does **not** use the standard 95% confidence interval (z = 1.96). It uses:

```
z = 1.281551565545
```

This is the 90th percentile of the standard normal distribution — equivalently, an **80% two-sided confidence interval** (α = 0.20, z_{α/2} = 1.28).

**Why 80% instead of 95%?**

At 95%, the lower bound penalty for small samples is very steep. A comment with 10 upvotes / 10 total (100%) gets a Wilson lower of ≈ 0.72. At 80%, the same comment gets ≈ 0.80. Reddit found that 95% was *too* conservative — it buried genuinely good newer comments that hadn't accumulated votes yet. 80% strikes a balance between penalizing uncertainty and allowing good new content to surface.

---

## Formula (Reddit's Version)

Variables:
- `u` = upvotes
- `d` = downvotes
- `n` = u + d (total votes)
- `p̂` = u / n (observed positive proportion)
- `z` = 1.281551565545 (80% CI)

```
                    z²          /  p̂(1-p̂)   z²   \
       p̂  +  ─────────  −  z × │ ──────── + ──── │^0.5
                  2n            \     n      4n²  /
lower = ─────────────────────────────────────────────────
                            z²
                     1  +  ────
                             n
```

Edge cases:
- `n = 0`: undefined — return `None` or exclude from ranking
- `u = 0, n > 0`: formula still works, lower bound approaches 0
- `u = n` (100% positive): formula still works, lower bound < 1.0

---

## Worked Example

Three comments on a Reddit post:

| Comment | Upvotes | Downvotes | n | p̂ |
|---|---|---|---|---|
| A | 1 | 0 | 1 | 1.000 |
| B | 40 | 10 | 50 | 0.800 |
| C | 900 | 100 | 1000 | 0.900 |

Using z = 1.281551565545:

**Comment A** (1/1):
```
p̂ = 1.0, n = 1, z² = 1.6424
numerator  = 1.0 + 0.8212 - 1.2816 × sqrt(0 + 0.4106) = 1.8212 - 0.8212 = 1.0000
denominator = 1 + 1.6424 = 2.6424
lower_A = 1.0000 / 2.6424 ≈ 0.3784
```

**Comment B** (40/50):
```
p̂ = 0.80, n = 50, z² = 1.6424
numerator  = 0.80 + 0.01642 - 1.2816 × sqrt(0.0032 + 0.000164)
           = 0.81642 - 1.2816 × sqrt(0.003364)
           = 0.81642 - 1.2816 × 0.058 ≈ 0.81642 - 0.07433 ≈ 0.7421
denominator = 1 + 0.03285 = 1.03285
lower_B ≈ 0.7184
```

**Comment C** (900/1000):
```
p̂ = 0.90, n = 1000, z² = 1.6424
numerator  = 0.90 + 0.000821 - 1.2816 × sqrt(0.000090 + 0.000000411)
           ≈ 0.900821 - 1.2816 × 0.009487 ≈ 0.900821 - 0.01216 ≈ 0.8887
denominator ≈ 1.001642
lower_C ≈ 0.8872
```

**Ranking:** C (0.887) > B (0.718) > A (0.378)

Comment A's perfect ratio is exposed as noise. Comment C — with 100× more evidence — properly ranks first.

---

## Python Implementation (Reddit-exact)

```python
import math

def wilson_lower_bound(upvotes: int, downvotes: int, z: float = 1.281551565545) -> float:
    """
    Reddit's 'Best' comment score.
    z = 1.281551565545 (80% CI, Reddit's choice).
    Returns 0.0 for items with no votes.
    """
    n = upvotes + downvotes
    if n == 0:
        return 0.0
    p_hat = upvotes / n
    z2 = z * z
    numerator = (
        p_hat
        + z2 / (2 * n)
        - z * math.sqrt(p_hat * (1 - p_hat) / n + z2 / (4 * n * n))
    )
    denominator = 1 + z2 / n
    return numerator / denominator


def rank_comments(comments: list[dict]) -> list[dict]:
    """
    comments: list of {"id": str, "up": int, "down": int, ...}
    Returns sorted list with added "wilson" field.
    """
    for c in comments:
        c["wilson"] = wilson_lower_bound(c["up"], c["down"])
    return sorted(comments, key=lambda x: x["wilson"], reverse=True)
```

**Verification:**
```python
# Reproduce worked example
assert abs(wilson_lower_bound(1, 0) - 0.3784) < 0.001
assert abs(wilson_lower_bound(900, 100) - 0.8872) < 0.001
assert wilson_lower_bound(900, 100) > wilson_lower_bound(40, 10)
assert wilson_lower_bound(40, 10) > wilson_lower_bound(1, 0)
assert wilson_lower_bound(0, 0) == 0.0
```

---

## Reddit "Best" vs. Reddit "Hot"

These are often confused. They solve different problems:

| Property | Best | Hot |
|---|---|---|
| Purpose | Rank comment quality | Rank post recency + popularity |
| Time factor | **None** | **Yes** — decays over hours |
| Formula basis | Wilson lower bound | Logarithm of score + time offset |
| Downvotes affect rank | Yes (via proportion) | Indirect (via net score) |
| Use case | Comment threads | Front page post ordering |

**Hot** (Hacker News variant, also used on Reddit for posts):
```
score = log10(max(abs(net_score), 1)) + sign(net_score) × seconds_since_epoch / 45000
```

Hot is **not** Wilson-based. Do not conflate the two. This reference covers only "Best".

---

## Adapting Reddit's Parameters to Your Use Case

Reddit's choice of 80% CI is not universally correct. It was tuned for comment threads where:
1. New content needs a chance to surface (lower penalty for small n)
2. Votes accumulate quickly (sample sizes grow fast, reducing uncertainty)

| Your context | Recommended z | Why |
|---|---|---|
| Comment ranking (Reddit-like) | 1.28 (80%) | Fast vote accumulation; discovery matters |
| Product reviews (e-commerce) | 1.65 (90%) | Slower accumulation; buyers trust well-reviewed items |
| Standard "Best Rated" list | 1.96 (95%) | Most conservative; favors established items |
| High-stakes curation (medical, safety) | 2.33 (98%) | Extreme penalty for low-n claims |

The only constant: **never use z = 0 (simple average)**. That is the failure mode Wilson Score was built to fix.

---

## Controversial Comments: A Limitation

Wilson Score ranks by the lower bound of the **positive proportion**. It does not distinguish between:
- 90 up / 10 down (clearly good)
- 5000 up / 500 down (popular but polarizing)

Both have p̂ = 0.90. With large n, both get a lower bound near 0.90. Reddit's "Controversial" sort is a separate algorithm that specifically surfaces high-vote, polarized comments. If your use case requires detecting controversy, Wilson Score alone is insufficient — you need an additional signal (e.g., standard deviation of ratings, or `min(up, down)` as a controversy score).

---

## Source

Evan Miller, *"How Not To Sort By Average Rating"*, 2009.  
Reddit's open-source implementation (archived): `r2/r2/lib/db/_sorts.pyx` — the relevant function is `_confidence()`, using the exact z value above.

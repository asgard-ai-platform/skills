#!/usr/bin/env python3
"""
Wilson Score confidence interval calculator for binomial proportions.

Ranks items by the LOWER bound of the Wilson score interval, penalizing
items with few observations. Prevents the "5/5 stars with 1 review" problem.

Formula:
  center = (p + z^2/(2n)) / (1 + z^2/n)
  margin = z * sqrt(p(1-p)/n + z^2/(4n^2)) / (1 + z^2/n)
  lower = center - margin
  upper = center + margin

Usage:
  python wilson_score.py --positive 950 --total 1000 --confidence 0.95
  python wilson_score.py --input items.json
  python wilson_score.py --verify
"""
import argparse
import json
import math


# Z-scores for common confidence levels (two-sided)
Z_SCORES = {
    0.80: 1.2816,
    0.90: 1.6449,
    0.95: 1.9600,
    0.99: 2.5758,
    0.999: 3.2905,
}


def compute_interval(positive, total, confidence=0.95):
    """Compute Wilson score confidence interval for a single proportion."""
    if total <= 0:
        raise ValueError("total must be positive")
    if positive < 0 or positive > total:
        raise ValueError("positive must be between 0 and total")
    if confidence not in Z_SCORES:
        # Use normal approximation for arbitrary confidence
        raise ValueError(f"confidence must be one of {list(Z_SCORES.keys())}")

    z = Z_SCORES[confidence]
    p = positive / total
    n = total

    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    margin = (z * math.sqrt((p * (1 - p) / n) + (z**2 / (4 * n**2)))) / denom

    lower = center - margin
    upper = center + margin
    lower = max(0, lower)
    upper = min(1, upper)

    return {
        "observed_proportion": round(p, 6),
        "positive": positive,
        "total": total,
        "wilson_center": round(center, 6),
        "wilson_lower": round(lower, 6),
        "wilson_upper": round(upper, 6),
        "confidence": confidence,
    }


def compute_ranking(items, confidence=0.95):
    """Rank a list of items by Wilson lower bound.

    items: list of {id, positive, total}
    """
    ranked = []
    for item in items:
        r = compute_interval(item["positive"], item["total"], confidence)
        ranked.append({
            "id": item.get("id", "?"),
            **r,
        })
    ranked.sort(key=lambda x: -x["wilson_lower"])
    for i, item in enumerate(ranked, start=1):
        item["rank"] = i
    return {
        "ranking": ranked,
        "count": len(ranked),
        "confidence": confidence,
    }


def verify():
    """Self-test with known values."""
    # Case 1: 950/1000 at 95% confidence
    # p = 0.95, z = 1.96, n = 1000
    # Wilson lower bound should be ~0.935
    r = compute_interval(950, 1000, 0.95)
    assert abs(r["observed_proportion"] - 0.95) < 1e-6
    assert 0.93 < r["wilson_lower"] < 0.95, f"Expected ~0.935, got {r['wilson_lower']}"
    assert r["wilson_upper"] < 1.0

    # Case 2: 1/1 (small sample) — should be much lower than raw 1.0
    r2 = compute_interval(1, 1, 0.95)
    assert r2["observed_proportion"] == 1.0
    assert r2["wilson_lower"] < 0.30, f"1/1 lower bound should be < 0.30, got {r2['wilson_lower']}"

    # Case 3: 9/10 vs 900/1000 — same proportion, different confidence
    r3 = compute_interval(9, 10, 0.95)
    r4 = compute_interval(900, 1000, 0.95)
    assert r3["observed_proportion"] == r4["observed_proportion"]
    assert r3["wilson_lower"] < r4["wilson_lower"], "Larger sample should have higher lower bound"

    # Case 4: Ranking — verify small-sample item ranks below large-sample item
    items = [
        {"id": "A", "positive": 1, "total": 1},        # 100% but 1 review
        {"id": "B", "positive": 950, "total": 1000},   # 95% with 1000 reviews
        {"id": "C", "positive": 80, "total": 100},     # 80% with 100 reviews
    ]
    ranking = compute_ranking(items, 0.95)
    ids_in_order = [r["id"] for r in ranking["ranking"]]
    assert ids_in_order[0] == "B", f"B should rank first, got {ids_in_order}"
    assert ids_in_order[-1] == "A", f"A should rank last (only 1 review), got {ids_in_order}"

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--positive", type=int)
    parser.add_argument("--total", type=int)
    parser.add_argument("--confidence", type=float, default=0.95)
    parser.add_argument("--input", help="JSON file with items list for ranking")
    parser.add_argument("--verify", action="store_true", help="Run self-tests")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        if "items" in data:
            result = compute_ranking(data["items"], data.get("confidence", 0.95))
        else:
            result = compute_interval(data["positive"], data["total"], data.get("confidence", 0.95))
    else:
        if args.positive is None or args.total is None:
            parser.error("Provide --positive and --total, or use --input")
        result = compute_interval(args.positive, args.total, args.confidence)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Bayesian Average ranking calculator (IMDB-style weighted rating).

BR = (C * m + sum_ratings) / (C + n)
   = (C * m + avg_rating * n) / (C + n)

Where:
  C = confidence constant (phantom votes toward the prior)
  m = global mean rating across all items
  n = number of ratings for this item
  avg_rating = item's raw average

Items with few ratings are pulled toward the global mean, preventing
small-sample extremes from dominating rankings.

Usage:
  python bayesian_avg.py --input items.json
  python bayesian_avg.py --verify

Input JSON:
  {
    "confidence_C": 100,             # phantom votes
    "global_mean": null,             # if null, computed from items
    "items": [
      {"id": "A", "avg_rating": 9.5, "n": 5},
      {"id": "B", "avg_rating": 8.5, "n": 500}
    ]
  }
"""
import argparse
import json


def compute(items, confidence_C=None, global_mean=None):
    """Rank items by Bayesian average.

    If confidence_C is None, use the median of n across items.
    If global_mean is None, compute weighted average across all items.
    """
    if not items:
        raise ValueError("items list cannot be empty")
    for it in items:
        if it["n"] < 0:
            raise ValueError(f"n must be non-negative for item {it.get('id', '?')}")

    # Compute global_mean if not given
    if global_mean is None:
        total_ratings = sum(it["avg_rating"] * it["n"] for it in items)
        total_n = sum(it["n"] for it in items)
        if total_n == 0:
            raise ValueError("cannot compute global_mean with all zero-count items")
        global_mean = total_ratings / total_n

    # Default C to median of n
    if confidence_C is None:
        ns = sorted(it["n"] for it in items)
        mid = len(ns) // 2
        confidence_C = ns[mid] if len(ns) % 2 == 1 else (ns[mid - 1] + ns[mid]) / 2

    ranked = []
    for it in items:
        n = it["n"]
        avg = it["avg_rating"]
        if confidence_C + n == 0:
            br = 0
        else:
            br = (confidence_C * global_mean + avg * n) / (confidence_C + n)

        # Shrinkage: how much the Bayesian average differs from the raw average
        shrinkage = br - avg
        ranked.append({
            "id": it.get("id", "?"),
            "n": n,
            "avg_rating": round(avg, 4),
            "bayesian_avg": round(br, 4),
            "shrinkage": round(shrinkage, 4),
        })

    ranked.sort(key=lambda x: -x["bayesian_avg"])
    for i, item in enumerate(ranked, start=1):
        item["rank"] = i

    return {
        "ranking": ranked,
        "parameters": {
            "confidence_C": confidence_C,
            "global_mean": round(global_mean, 4),
        },
        "count": len(ranked),
    }


def verify():
    # Case 1: Small-sample high-rating vs large-sample slightly lower
    # C=100, m=7, Item A: avg=9.5, n=5 → BR = (100*7 + 9.5*5) / 105 = 747.5/105 = 7.119
    # Item B: avg=8.5, n=500 → BR = (100*7 + 8.5*500) / 600 = 4950/600 = 8.25
    items = [
        {"id": "A", "avg_rating": 9.5, "n": 5},
        {"id": "B", "avg_rating": 8.5, "n": 500},
    ]
    r = compute(items, confidence_C=100, global_mean=7.0)
    # B should rank higher than A despite lower raw average
    ids = [it["id"] for it in r["ranking"]]
    assert ids == ["B", "A"], f"Expected B before A, got {ids}"
    a = next(it for it in r["ranking"] if it["id"] == "A")
    b = next(it for it in r["ranking"] if it["id"] == "B")
    assert abs(a["bayesian_avg"] - 7.1190) < 0.001
    assert abs(b["bayesian_avg"] - 8.25) < 0.001

    # Case 2: Extreme small sample (1 rating) → heavy shrinkage
    items2 = [
        {"id": "X", "avg_rating": 10.0, "n": 1},
        {"id": "Y", "avg_rating": 8.0, "n": 1000},
    ]
    r2 = compute(items2, confidence_C=50, global_mean=7.0)
    # X: (50*7 + 10*1)/51 = 360/51 ≈ 7.0588
    # Y: (50*7 + 8*1000)/1050 = 8350/1050 ≈ 7.9524
    x = next(it for it in r2["ranking"] if it["id"] == "X")
    y = next(it for it in r2["ranking"] if it["id"] == "Y")
    assert abs(x["bayesian_avg"] - 7.0588) < 0.001
    assert abs(y["bayesian_avg"] - 7.9524) < 0.001
    assert r2["ranking"][0]["id"] == "Y"

    # Case 3: Very large n → BR converges to raw average
    items3 = [{"id": "Z", "avg_rating": 9.0, "n": 1_000_000}]
    r3 = compute(items3, confidence_C=100, global_mean=7.0)
    assert abs(r3["ranking"][0]["bayesian_avg"] - 9.0) < 0.001  # essentially no shrinkage

    # Case 4: Auto-compute global_mean
    items4 = [
        {"id": "A", "avg_rating": 4.0, "n": 10},
        {"id": "B", "avg_rating": 5.0, "n": 90},
    ]
    r4 = compute(items4, confidence_C=10)
    # global_mean = (4*10 + 5*90) / 100 = 490/100 = 4.9
    assert abs(r4["parameters"]["global_mean"] - 4.9) < 0.001

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", help="JSON file with items list")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if not args.input:
        parser.error("--input required")

    with open(args.input) as f:
        data = json.load(f)
    result = compute(data["items"], data.get("confidence_C"), data.get("global_mean"))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

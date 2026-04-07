#!/usr/bin/env python3
"""
Elo rating system calculator.

Expected score:
  E_A = 1 / (1 + 10^((R_B - R_A) / 400))

Rating update:
  R_A_new = R_A + K * (S_A - E_A)

Usage:
  python elo.py --rating-a 1500 --rating-b 1600 --actual 1 --k 32
  python elo.py --batch matches.json  (process a list of matches)
  python elo.py --verify

IRON LAW: Elo is zero-sum. Winner gains = Loser loses (ignoring rounding).
Total pool rating is preserved.
"""
import argparse
import json


def expected_score(rating_a, rating_b):
    """Probability that A beats B based on current ratings."""
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


def update(rating_a, rating_b, actual_a, k=32):
    """Update Elo ratings after a match.

    actual_a: 1 = A wins, 0 = A loses, 0.5 = draw
    """
    if actual_a not in (0, 0.5, 1):
        raise ValueError("actual_a must be 0, 0.5, or 1")
    if k <= 0:
        raise ValueError("k must be positive")

    e_a = expected_score(rating_a, rating_b)
    e_b = 1 - e_a
    actual_b = 1 - actual_a

    delta_a = k * (actual_a - e_a)
    delta_b = k * (actual_b - e_b)

    new_a = rating_a + delta_a
    new_b = rating_b + delta_b

    # Verify zero-sum
    assert abs((new_a + new_b) - (rating_a + rating_b)) < 1e-9, "Elo is not zero-sum"

    return {
        "new_rating_a": round(new_a, 2),
        "new_rating_b": round(new_b, 2),
        "delta_a": round(delta_a, 2),
        "delta_b": round(delta_b, 2),
        "expected_a": round(e_a, 4),
        "expected_b": round(e_b, 4),
        "actual_a": actual_a,
        "actual_b": actual_b,
        "k_factor": k,
        "zero_sum_check": round((new_a + new_b) - (rating_a + rating_b), 9),
    }


def process_batch(players_init, matches, k=32):
    """Process a sequence of matches, updating ratings in order.

    Args:
        players_init: dict of {player_id: starting_rating}
        matches: list of {a, b, result} where result is 1/0.5/0 for A
    """
    ratings = dict(players_init)
    history = []
    for m in matches:
        a, b, result = m["a"], m["b"], m["result"]
        if a not in ratings:
            ratings[a] = 1500
        if b not in ratings:
            ratings[b] = 1500
        res = update(ratings[a], ratings[b], result, k)
        ratings[a] = res["new_rating_a"]
        ratings[b] = res["new_rating_b"]
        history.append({"match": m, "result": res, "ratings_after": dict(ratings)})

    final = sorted(ratings.items(), key=lambda x: -x[1])
    return {
        "final_ratings": ratings,
        "leaderboard": [{"player": p, "rating": r} for p, r in final],
        "match_count": len(matches),
        "k_factor": k,
    }


def verify():
    # Classic test: equal ratings, A wins
    # E_A = 0.5, S_A = 1
    # Delta = 32 * (1 - 0.5) = 16
    r = update(1500, 1500, 1, k=32)
    assert r["new_rating_a"] == 1516
    assert r["new_rating_b"] == 1484
    assert r["delta_a"] == 16
    assert r["zero_sum_check"] == 0

    # Upset: 1500 beats 1700
    # E_A = 1 / (1 + 10^(200/400)) = 1 / (1 + 3.162) ≈ 0.2403
    # Delta = 32 * (1 - 0.2403) ≈ 24.31
    r2 = update(1500, 1700, 1, k=32)
    assert abs(r2["delta_a"] - 24.31) < 0.1

    # Expected outcome: 1700 beats 1500 → small delta
    # E_A = 0.2403, S_A = 0
    # Delta_A = 32 * (0 - 0.2403) ≈ -7.69 (A loses 7.69)
    r3 = update(1500, 1700, 0, k=32)
    assert abs(r3["delta_a"] - (-7.69)) < 0.1

    # Draw: equal ratings → no change
    r4 = update(1500, 1500, 0.5, k=32)
    assert r4["delta_a"] == 0
    assert r4["delta_b"] == 0

    # Batch processing
    batch = process_batch(
        {"A": 1500, "B": 1500, "C": 1500},
        [
            {"a": "A", "b": "B", "result": 1},
            {"a": "A", "b": "C", "result": 1},
            {"a": "B", "b": "C", "result": 0.5},
        ],
        k=32,
    )
    assert batch["match_count"] == 3
    # A should be top after winning 2
    assert batch["leaderboard"][0]["player"] == "A"
    # Total rating should be conserved (3 * 1500 = 4500)
    assert abs(sum(batch["final_ratings"].values()) - 4500) < 0.01

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rating-a", type=float)
    parser.add_argument("--rating-b", type=float)
    parser.add_argument("--actual", type=float, help="Result for A: 1 win, 0.5 draw, 0 loss")
    parser.add_argument("--k", type=float, default=32)
    parser.add_argument("--batch", help="JSON file with {players, matches}")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if args.batch:
        with open(args.batch) as f:
            data = json.load(f)
        result = process_batch(data["players"], data["matches"], data.get("k", 32))
    else:
        if None in (args.rating_a, args.rating_b, args.actual):
            parser.error("Provide --rating-a --rating-b --actual or --batch")
        result = update(args.rating_a, args.rating_b, args.actual, args.k)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

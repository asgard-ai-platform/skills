#!/usr/bin/env python3
"""
Price elasticity of demand calculator (arc and point methods).

Arc elasticity (midpoint method, symmetric):
  Ed = ((Q2-Q1) / ((Q2+Q1)/2)) / ((P2-P1) / ((P2+P1)/2))

Point elasticity (at a specific price):
  Ed = (dQ/dP) * (P/Q)

Usage:
  python arc_elasticity.py --p1 100 --q1 1000 --p2 110 --q2 850
  python arc_elasticity.py --input data.json
  python arc_elasticity.py --verify
"""
import argparse
import json


def compute_arc(p1, q1, p2, q2):
    """Compute arc (midpoint) elasticity between two price-quantity points."""
    if p1 <= 0 or p2 <= 0 or q1 <= 0 or q2 <= 0:
        raise ValueError("Prices and quantities must be positive")
    if p1 == p2:
        raise ValueError("p1 and p2 must differ")

    avg_p = (p1 + p2) / 2
    avg_q = (q1 + q2) / 2
    pct_dq = (q2 - q1) / avg_q
    pct_dp = (p2 - p1) / avg_p
    elasticity = pct_dq / pct_dp

    abs_e = abs(elasticity)
    if abs_e > 1:
        classification = "elastic"
    elif abs_e < 1:
        classification = "inelastic"
    else:
        classification = "unit_elastic"

    # Revenue impact
    rev1 = p1 * q1
    rev2 = p2 * q2
    rev_change_pct = (rev2 - rev1) / rev1 * 100

    return {
        "method": "arc",
        "elasticity": round(elasticity, 4),
        "abs_elasticity": round(abs_e, 4),
        "classification": classification,
        "interpretation": (
            f"{'Elastic' if abs_e > 1 else 'Inelastic' if abs_e < 1 else 'Unit elastic'}: "
            f"1% price change → {abs_e:.2f}% quantity change"
        ),
        "revenue_impact": {
            "revenue_before": round(rev1, 2),
            "revenue_after": round(rev2, 2),
            "revenue_change_pct": round(rev_change_pct, 2),
            "direction": (
                "revenue rises with price" if rev_change_pct > 0 else
                "revenue falls with price" if rev_change_pct < 0 else
                "revenue unchanged"
            ),
        },
        "pct_change": {
            "price_pct": round(pct_dp * 100, 2),
            "quantity_pct": round(pct_dq * 100, 2),
        },
        "inputs": {"p1": p1, "q1": q1, "p2": p2, "q2": q2},
    }


def compute_point(p, q, dq_dp):
    """Point elasticity at (p, q) given marginal dQ/dP.

    Ed = (dQ/dP) * (P/Q)
    """
    if p <= 0 or q <= 0:
        raise ValueError("Price and quantity must be positive")
    elasticity = dq_dp * (p / q)
    return {
        "method": "point",
        "elasticity": round(elasticity, 4),
        "abs_elasticity": round(abs(elasticity), 4),
        "classification": (
            "elastic" if abs(elasticity) > 1 else
            "inelastic" if abs(elasticity) < 1 else
            "unit_elastic"
        ),
        "inputs": {"p": p, "q": q, "dq_dp": dq_dp},
    }


def verify():
    """Self-test with known values."""
    # Example from the SKILL.md:
    # P: 100 → 110 (+10%), Q: 1000 → 850 (-15%)
    # Arc elasticity: ((850-1000)/((850+1000)/2)) / ((110-100)/((110+100)/2))
    #   = (-150/925) / (10/105)
    #   = -0.1622 / 0.0952
    #   ≈ -1.703
    r = compute_arc(100, 1000, 110, 850)
    assert abs(r["elasticity"] - (-1.7027)) < 0.01, f"Elasticity: expected ~-1.70, got {r['elasticity']}"
    assert r["classification"] == "elastic"

    # Revenue check
    # Rev1 = 100*1000 = 100000, Rev2 = 110*850 = 93500
    # Change: -6.5%
    assert abs(r["revenue_impact"]["revenue_change_pct"] - (-6.5)) < 0.1

    # Inelastic case: P 100→120 (+20%), Q 100→90 (-10%)
    # Arc: (-10/95) / (20/110) = -0.1053 / 0.1818 ≈ -0.579
    r2 = compute_arc(100, 100, 120, 90)
    assert r2["classification"] == "inelastic"

    # Point elasticity: P=100, Q=1000, dQ/dP = -5
    # E = -5 * (100/1000) = -0.5
    r3 = compute_point(100, 1000, -5)
    assert abs(r3["elasticity"] - (-0.5)) < 0.001

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--p1", type=float)
    parser.add_argument("--q1", type=float)
    parser.add_argument("--p2", type=float)
    parser.add_argument("--q2", type=float)
    parser.add_argument("--point-p", type=float, help="Point elasticity: current price")
    parser.add_argument("--point-q", type=float, help="Point elasticity: current quantity")
    parser.add_argument("--point-dq-dp", type=float, help="Point elasticity: dQ/dP")
    parser.add_argument("--input", help="Read inputs from JSON file")
    parser.add_argument("--verify", action="store_true", help="Run self-tests")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        if "dq_dp" in data:
            result = compute_point(data["p"], data["q"], data["dq_dp"])
        else:
            result = compute_arc(data["p1"], data["q1"], data["p2"], data["q2"])
    elif args.point_p is not None:
        result = compute_point(args.point_p, args.point_q, args.point_dq_dp)
    else:
        if None in (args.p1, args.q1, args.p2, args.q2):
            parser.error("Provide --p1, --q1, --p2, --q2 (arc) or --point-* (point) or --input")
        result = compute_arc(args.p1, args.q1, args.p2, args.q2)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

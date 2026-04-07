#!/usr/bin/env python3
"""
Newsvendor single-period inventory optimization calculator.

Optimal order quantity:
  Q* = F^-1(Cu / (Cu + Co))

Where:
  Cu = underage cost (price - cost)
  Co = overage cost (cost - salvage)
  F  = demand CDF (assumed normal by default)

Usage:
  python newsvendor.py --price 50 --cost 20 --salvage 5 --mean 100 --sd 30
  python newsvendor.py --input data.json
  python newsvendor.py --verify

IRON LAW: Q* almost NEVER equals expected demand. The critical ratio,
not the mean, drives the optimal order.
"""
import argparse
import json
import math


def norm_ppf(p):
    """Inverse normal CDF (probit). Abramowitz-Stegun approximation."""
    if p <= 0 or p >= 1:
        raise ValueError("p must be in (0, 1)")
    sign = 1
    if p < 0.5:
        sign = -1
        p = 1 - p
    t = math.sqrt(-2 * math.log(1 - p))
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    z = t - (c0 + c1 * t + c2 * t * t) / (1 + d1 * t + d2 * t * t + d3 * t * t * t)
    return sign * z


def norm_pdf(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def norm_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def standard_loss(z):
    """
    L(z) = phi(z) - z * (1 - Phi(z))
    Expected shortage for standard normal. Used to compute expected leftovers/stockouts.
    """
    return norm_pdf(z) - z * (1 - norm_cdf(z))


def compute(price, cost, salvage, mean_demand, sd_demand):
    """Compute optimal order quantity and expected profit."""
    if price <= cost:
        raise ValueError("price must exceed cost")
    if cost < salvage:
        raise ValueError("cost must be >= salvage (overage cost must be non-negative)")
    if sd_demand < 0:
        raise ValueError("sd_demand must be non-negative")

    cu = price - cost          # underage: missed margin per lost sale
    co = cost - salvage        # overage: loss per unsold unit
    critical_ratio = cu / (cu + co)

    # z such that Phi(z) = critical_ratio
    z_star = norm_ppf(critical_ratio)
    q_star = mean_demand + z_star * sd_demand
    q_star = max(0, q_star)  # clamp to non-negative

    # Expected leftovers and stockouts using standard loss function
    expected_stockout = sd_demand * standard_loss(z_star)
    expected_sales = mean_demand - expected_stockout
    expected_leftover = q_star - expected_sales

    # Expected profit
    # = Cu * expected_sales - Co * expected_leftover
    expected_profit = cu * expected_sales - co * expected_leftover

    return {
        "optimal_quantity": round(q_star, 2),
        "critical_ratio": round(critical_ratio, 4),
        "z_star": round(z_star, 4),
        "underage_cost": cu,
        "overage_cost": co,
        "expected_sales": round(expected_sales, 2),
        "expected_stockout": round(expected_stockout, 2),
        "expected_leftover": round(expected_leftover, 2),
        "expected_profit": round(expected_profit, 2),
        "fill_rate": round(expected_sales / mean_demand, 4) if mean_demand > 0 else None,
        "comparison_vs_mean": {
            "order_above_mean": q_star > mean_demand,
            "q_star": round(q_star, 2),
            "mean_demand": mean_demand,
            "delta": round(q_star - mean_demand, 2),
        },
        "inputs": {
            "price": price,
            "cost": cost,
            "salvage": salvage,
            "mean_demand": mean_demand,
            "sd_demand": sd_demand,
        },
    }


def verify():
    # Textbook example:
    # Price=50, cost=20, salvage=5 → Cu=30, Co=15 → CR = 30/45 = 0.6667
    # Demand ~ N(100, 30)
    # z*(0.6667) ≈ 0.4307
    # Q* = 100 + 0.4307 * 30 ≈ 112.92
    r = compute(50, 20, 5, 100, 30)
    assert abs(r["critical_ratio"] - 0.6667) < 0.001
    assert abs(r["optimal_quantity"] - 112.92) < 0.5, f"Q*: expected ~112.92, got {r['optimal_quantity']}"

    # Verify: Q* is above mean because Cu > Co (high margin, low waste cost)
    assert r["comparison_vs_mean"]["order_above_mean"] is True

    # Symmetric case: Cu = Co → CR = 0.5 → Q* = mean
    r_sym = compute(30, 20, 10, 100, 30)  # Cu=10, Co=10
    assert abs(r_sym["critical_ratio"] - 0.5) < 0.001
    assert abs(r_sym["optimal_quantity"] - 100) < 0.1, f"Q*: expected 100, got {r_sym['optimal_quantity']}"

    # Zero variance → Q* = mean
    r_det = compute(50, 20, 5, 100, 0)
    assert r_det["optimal_quantity"] == 100

    # Error handling: negative margin
    try:
        compute(10, 20, 5, 100, 30)
        assert False, "Should reject price <= cost"
    except ValueError:
        pass

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--price", type=float)
    parser.add_argument("--cost", type=float)
    parser.add_argument("--salvage", type=float, default=0)
    parser.add_argument("--mean", type=float, help="Mean demand")
    parser.add_argument("--sd", type=float, help="Std dev of demand")
    parser.add_argument("--input", help="JSON file")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        result = compute(**data)
    else:
        if None in (args.price, args.cost, args.mean, args.sd):
            parser.error("Provide --price --cost --mean --sd (and optionally --salvage)")
        result = compute(args.price, args.cost, args.salvage, args.mean, args.sd)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

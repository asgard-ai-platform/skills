#!/usr/bin/env python3
"""
CAC / LTV / Unit Economics calculator.

Deterministic calculator for:
  - Customer Acquisition Cost (CAC)
  - Customer Lifetime Value (LTV)
  - LTV/CAC ratio (health metric)
  - CAC payback period (months)

Usage:
  python cac_ltv.py --marketing-cost 100000 --new-customers 500 \
                    --arpu 50 --gross-margin 0.70 --monthly-churn 0.05
  python cac_ltv.py --input data.json
  python cac_ltv.py --verify

All monetary values in the same currency. ARPU and churn must be on the
same time basis (e.g., both monthly).
"""
import argparse
import json
import sys


def compute(marketing_cost, new_customers, arpu, gross_margin, monthly_churn):
    """Compute CAC, LTV, LTV/CAC ratio, and payback period.

    Args:
        marketing_cost: Total marketing + sales spend over the period.
        new_customers: Number of NEW customers acquired in that period.
        arpu: Average revenue per user per month.
        gross_margin: Gross margin as decimal (e.g., 0.70 for 70%).
        monthly_churn: Monthly churn rate as decimal (e.g., 0.05 for 5%).

    Returns:
        Dict with CAC, LTV, ratio, payback_months, health assessment.
    """
    if new_customers <= 0:
        raise ValueError("new_customers must be > 0")
    if not (0 < gross_margin <= 1):
        raise ValueError("gross_margin must be in (0, 1]")
    if not (0 < monthly_churn < 1):
        raise ValueError("monthly_churn must be in (0, 1)")

    cac = marketing_cost / new_customers
    # LTV = ARPU * gross_margin * (1 / monthly_churn)
    # This is the simple LTV formula assuming constant churn.
    monthly_contribution = arpu * gross_margin
    avg_customer_lifetime_months = 1 / monthly_churn
    ltv = monthly_contribution * avg_customer_lifetime_months

    ratio = ltv / cac if cac > 0 else float("inf")
    payback_months = cac / monthly_contribution if monthly_contribution > 0 else float("inf")

    if ratio >= 3:
        health = "healthy"
    elif ratio >= 1:
        health = "marginal"
    else:
        health = "unsustainable"

    return {
        "cac": round(cac, 2),
        "ltv": round(ltv, 2),
        "ltv_cac_ratio": round(ratio, 2),
        "payback_months": round(payback_months, 2),
        "avg_customer_lifetime_months": round(avg_customer_lifetime_months, 2),
        "monthly_contribution": round(monthly_contribution, 2),
        "health": health,
        "inputs": {
            "marketing_cost": marketing_cost,
            "new_customers": new_customers,
            "arpu": arpu,
            "gross_margin": gross_margin,
            "monthly_churn": monthly_churn,
        },
    }


def verify():
    """Self-test with known values."""
    # Case 1: Healthy SaaS
    # CAC = 100_000 / 500 = 200
    # monthly_contribution = 50 * 0.70 = 35
    # lifetime = 1 / 0.05 = 20 months
    # LTV = 35 * 20 = 700
    # ratio = 700 / 200 = 3.5 (healthy)
    # payback = 200 / 35 = 5.71 months
    r = compute(100_000, 500, 50, 0.70, 0.05)
    assert r["cac"] == 200.0, f"CAC: expected 200, got {r['cac']}"
    assert r["ltv"] == 700.0, f"LTV: expected 700, got {r['ltv']}"
    assert r["ltv_cac_ratio"] == 3.5, f"Ratio: expected 3.5, got {r['ltv_cac_ratio']}"
    assert r["health"] == "healthy", f"Health: expected healthy, got {r['health']}"
    assert abs(r["payback_months"] - 5.71) < 0.01, f"Payback: expected ~5.71, got {r['payback_months']}"

    # Case 2: Unsustainable
    r2 = compute(100_000, 500, 20, 0.50, 0.10)
    # CAC = 200, monthly_contrib = 10, lifetime = 10 → LTV = 100, ratio = 0.5
    assert r2["health"] == "unsustainable", f"Health: expected unsustainable, got {r2['health']}"

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--marketing-cost", type=float, help="Total marketing + sales spend")
    parser.add_argument("--new-customers", type=int, help="New customers acquired")
    parser.add_argument("--arpu", type=float, help="Average revenue per user (monthly)")
    parser.add_argument("--gross-margin", type=float, help="Gross margin as decimal (0.70)")
    parser.add_argument("--monthly-churn", type=float, help="Monthly churn rate as decimal (0.05)")
    parser.add_argument("--input", help="Read inputs from JSON file")
    parser.add_argument("--verify", action="store_true", help="Run self-tests")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        result = compute(**data)
    else:
        required = [args.marketing_cost, args.new_customers, args.arpu, args.gross_margin, args.monthly_churn]
        if any(x is None for x in required):
            parser.error("Provide all 5 args or use --input")
        result = compute(args.marketing_cost, args.new_customers, args.arpu, args.gross_margin, args.monthly_churn)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

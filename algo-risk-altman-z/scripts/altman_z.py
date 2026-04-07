#!/usr/bin/env python3
"""
Altman Z-Score bankruptcy prediction calculator.

Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5

Zones:
  Z > 2.99   → Safe
  1.81-2.99  → Grey
  Z < 1.81   → Distress

Also supports Z' (private firms) and Z'' (non-manufacturing / emerging markets).

Usage:
  python altman_z.py --working-capital 200 --retained-earnings 500 \\
                     --ebit 150 --market-cap 2000 --total-liab 1000 \\
                     --sales 2500 --total-assets 3000
  python altman_z.py --input data.json --variant original
  python altman_z.py --verify
"""
import argparse
import json
import sys


COEFFICIENTS = {
    "original": {"X1": 1.2, "X2": 1.4, "X3": 3.3, "X4": 0.6, "X5": 1.0, "safe": 2.99, "distress": 1.81},
    "private": {"X1": 0.717, "X2": 0.847, "X3": 3.107, "X4": 0.420, "X5": 0.998, "safe": 2.90, "distress": 1.23},
    "non_manufacturing": {"X1": 6.56, "X2": 3.26, "X3": 6.72, "X4": 1.05, "X5": 0.0, "safe": 2.60, "distress": 1.10},
}


def compute(working_capital, retained_earnings, ebit, market_or_book_equity,
            total_liabilities, sales, total_assets, variant="original"):
    """Compute Altman Z-Score.

    Args:
        working_capital: Current assets - current liabilities.
        retained_earnings: From balance sheet.
        ebit: Earnings before interest and tax.
        market_or_book_equity: Market cap (original) or book equity (Z').
        total_liabilities: Total debt.
        sales: Annual revenue.
        total_assets: Total assets.
        variant: 'original', 'private', or 'non_manufacturing'.
    """
    if total_assets <= 0:
        raise ValueError("total_assets must be positive")
    if total_liabilities <= 0:
        raise ValueError("total_liabilities must be positive")
    if variant not in COEFFICIENTS:
        raise ValueError(f"variant must be one of {list(COEFFICIENTS.keys())}")

    coef = COEFFICIENTS[variant]

    X1 = working_capital / total_assets
    X2 = retained_earnings / total_assets
    X3 = ebit / total_assets
    X4 = market_or_book_equity / total_liabilities
    X5 = sales / total_assets

    z = coef["X1"] * X1 + coef["X2"] * X2 + coef["X3"] * X3 + coef["X4"] * X4 + coef["X5"] * X5

    if z > coef["safe"]:
        zone = "safe"
    elif z >= coef["distress"]:
        zone = "grey"
    else:
        zone = "distress"

    return {
        "z_score": round(z, 4),
        "zone": zone,
        "variant": variant,
        "components": {
            "X1_working_capital_ta": round(X1, 4),
            "X2_retained_earnings_ta": round(X2, 4),
            "X3_ebit_ta": round(X3, 4),
            "X4_equity_debt": round(X4, 4),
            "X5_sales_ta": round(X5, 4),
        },
        "thresholds": {
            "safe_above": coef["safe"],
            "distress_below": coef["distress"],
        },
    }


def verify():
    """Self-test with known values."""
    # Example from the SKILL.md example:
    # WC=200, RE=500, EBIT=150, MktCap=2000, TL=1000, Sales=2500, TA=3000
    # X1 = 200/3000 = 0.0667
    # X2 = 500/3000 = 0.1667
    # X3 = 150/3000 = 0.05
    # X4 = 2000/1000 = 2.0
    # X5 = 2500/3000 = 0.8333
    # Z = 1.2*0.0667 + 1.4*0.1667 + 3.3*0.05 + 0.6*2.0 + 1.0*0.8333
    #   = 0.08 + 0.233 + 0.165 + 1.2 + 0.833
    #   = 2.511 (grey zone)
    r = compute(200, 500, 150, 2000, 1000, 2500, 3000)
    assert abs(r["z_score"] - 2.5117) < 0.01, f"Z: expected ~2.51, got {r['z_score']}"
    assert r["zone"] == "grey", f"Zone: expected grey, got {r['zone']}"

    # Distress case: everything minimal
    r2 = compute(10, 10, 5, 100, 500, 100, 1000)
    assert r2["zone"] == "distress", f"Zone: expected distress, got {r2['zone']}"

    # Private firm variant
    r3 = compute(200, 500, 150, 2000, 1000, 2500, 3000, variant="private")
    assert r3["variant"] == "private"

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--working-capital", type=float)
    parser.add_argument("--retained-earnings", type=float)
    parser.add_argument("--ebit", type=float)
    parser.add_argument("--market-cap", type=float, help="Market cap (or book equity for --variant private)")
    parser.add_argument("--total-liab", type=float)
    parser.add_argument("--sales", type=float)
    parser.add_argument("--total-assets", type=float)
    parser.add_argument("--variant", choices=list(COEFFICIENTS.keys()), default="original")
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
        required = [args.working_capital, args.retained_earnings, args.ebit, args.market_cap,
                    args.total_liab, args.sales, args.total_assets]
        if any(x is None for x in required):
            parser.error("Provide all 7 inputs or use --input")
        result = compute(args.working_capital, args.retained_earnings, args.ebit, args.market_cap,
                         args.total_liab, args.sales, args.total_assets, args.variant)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

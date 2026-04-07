#!/usr/bin/env python3
"""
DuPont 3-factor and 5-factor decomposition calculator.

Decomposes Return on Equity (ROE) into:
  3-factor: ROE = Net Margin × Asset Turnover × Equity Multiplier
  5-factor: ROE = Tax Burden × Interest Burden × EBIT Margin × Asset Turnover × Equity Multiplier

Usage:
  python dupont.py --net-income 100 --revenue 1000 --total-assets 800 --total-equity 500
  python dupont.py --input data.json --model 5
  python dupont.py --verify

IRON LAW: ROE (direct) must equal ROE (decomposed) up to rounding — if not,
the input data is inconsistent.
"""
import argparse
import json
import sys


def compute_3factor(net_income, revenue, total_assets, total_equity):
    """3-factor DuPont decomposition."""
    if revenue == 0 or total_assets == 0 or total_equity == 0:
        raise ValueError("revenue, total_assets, total_equity must be non-zero")

    net_margin = net_income / revenue
    asset_turnover = revenue / total_assets
    equity_multiplier = total_assets / total_equity

    roe_direct = net_income / total_equity
    roe_decomposed = net_margin * asset_turnover * equity_multiplier

    return {
        "model": "3-factor",
        "roe_direct": round(roe_direct, 6),
        "roe_decomposed": round(roe_decomposed, 6),
        "match": abs(roe_direct - roe_decomposed) < 1e-6,
        "components": {
            "net_margin": round(net_margin, 4),
            "asset_turnover": round(asset_turnover, 4),
            "equity_multiplier": round(equity_multiplier, 4),
        },
        "interpretation": {
            "net_margin_pct": f"{net_margin * 100:.2f}%",
            "asset_turnover": f"{asset_turnover:.2f}x",
            "equity_multiplier": f"{equity_multiplier:.2f}x (leverage)",
            "roe_pct": f"{roe_direct * 100:.2f}%",
        },
    }


def compute_5factor(net_income, ebt, ebit, revenue, total_assets, total_equity):
    """5-factor DuPont decomposition.

    Args:
        net_income: Net income after tax.
        ebt: Earnings before tax.
        ebit: Earnings before interest and tax.
    """
    if 0 in (ebt, ebit, revenue, total_assets, total_equity):
        raise ValueError("All denominators must be non-zero")

    tax_burden = net_income / ebt  # (1 - tax rate)
    interest_burden = ebt / ebit
    ebit_margin = ebit / revenue
    asset_turnover = revenue / total_assets
    equity_multiplier = total_assets / total_equity

    roe_direct = net_income / total_equity
    roe_decomposed = tax_burden * interest_burden * ebit_margin * asset_turnover * equity_multiplier

    return {
        "model": "5-factor",
        "roe_direct": round(roe_direct, 6),
        "roe_decomposed": round(roe_decomposed, 6),
        "match": abs(roe_direct - roe_decomposed) < 1e-6,
        "components": {
            "tax_burden": round(tax_burden, 4),
            "interest_burden": round(interest_burden, 4),
            "ebit_margin": round(ebit_margin, 4),
            "asset_turnover": round(asset_turnover, 4),
            "equity_multiplier": round(equity_multiplier, 4),
        },
    }


def verify():
    """Self-test with known values."""
    # Case 1: 3-factor
    # NI=100, Rev=1000, TA=800, TE=500
    # NM = 100/1000 = 0.10
    # AT = 1000/800 = 1.25
    # EM = 800/500 = 1.60
    # ROE = 0.10 * 1.25 * 1.60 = 0.20 (20%)
    # Direct ROE = 100/500 = 0.20 ✓
    r = compute_3factor(100, 1000, 800, 500)
    assert r["roe_direct"] == 0.20, f"ROE direct: expected 0.20, got {r['roe_direct']}"
    assert r["components"]["net_margin"] == 0.10
    assert r["components"]["asset_turnover"] == 1.25
    assert r["components"]["equity_multiplier"] == 1.6
    assert r["match"] is True

    # Case 2: 5-factor
    # Revenue=1000, EBIT=200, EBT=180, NI=135, TA=800, TE=500
    # Tax burden = 135/180 = 0.75
    # Interest burden = 180/200 = 0.90
    # EBIT margin = 200/1000 = 0.20
    # AT = 1.25, EM = 1.60
    # Decomposed: 0.75 * 0.90 * 0.20 * 1.25 * 1.60 = 0.27
    # Direct: 135/500 = 0.27 ✓
    r2 = compute_5factor(135, 180, 200, 1000, 800, 500)
    assert abs(r2["roe_direct"] - 0.27) < 1e-6
    assert r2["match"] is True

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--net-income", type=float)
    parser.add_argument("--revenue", type=float)
    parser.add_argument("--total-assets", type=float)
    parser.add_argument("--total-equity", type=float)
    parser.add_argument("--ebt", type=float, help="Earnings before tax (for 5-factor)")
    parser.add_argument("--ebit", type=float, help="Earnings before interest and tax (for 5-factor)")
    parser.add_argument("--model", choices=["3", "5"], default="3")
    parser.add_argument("--input", help="Read inputs from JSON file")
    parser.add_argument("--verify", action="store_true", help="Run self-tests")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        model = data.pop("model", "3")
        if model == "5":
            result = compute_5factor(**data)
        else:
            result = compute_3factor(**data)
    else:
        required = [args.net_income, args.revenue, args.total_assets, args.total_equity]
        if any(x is None for x in required):
            parser.error("Provide all of --net-income, --revenue, --total-assets, --total-equity")
        if args.model == "5":
            if args.ebt is None or args.ebit is None:
                parser.error("5-factor requires --ebt and --ebit")
            result = compute_5factor(args.net_income, args.ebt, args.ebit, args.revenue, args.total_assets, args.total_equity)
        else:
            result = compute_3factor(args.net_income, args.revenue, args.total_assets, args.total_equity)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

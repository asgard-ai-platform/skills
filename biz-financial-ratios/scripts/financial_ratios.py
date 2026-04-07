#!/usr/bin/env python3
"""
Financial ratios calculator.

Computes standard liquidity, leverage, profitability, and efficiency ratios
from income statement and balance sheet line items.

Usage:
  python financial_ratios.py --input data.json
  python financial_ratios.py --verify

Input JSON keys (all optional — only ratios with required inputs are computed):
  revenue, cogs, operating_income, ebit, interest_expense, net_income,
  current_assets, current_liabilities, inventory, cash,
  total_assets, total_liabilities, total_equity, long_term_debt,
  shares_outstanding, market_price
"""
import argparse
import json


def _ratio(num, den):
    if den is None or den == 0:
        return None
    if num is None:
        return None
    return num / den


def compute(data):
    """Compute all applicable financial ratios from the provided data."""
    d = dict(data)  # shallow copy

    # Fetch with None defaults
    rev = d.get("revenue")
    cogs = d.get("cogs")
    op_inc = d.get("operating_income") or d.get("ebit")
    ebit = d.get("ebit") or d.get("operating_income")
    interest = d.get("interest_expense")
    ni = d.get("net_income")

    ca = d.get("current_assets")
    cl = d.get("current_liabilities")
    inv = d.get("inventory")
    cash = d.get("cash")

    ta = d.get("total_assets")
    tl = d.get("total_liabilities")
    te = d.get("total_equity")
    ltd = d.get("long_term_debt")

    shares = d.get("shares_outstanding")
    price = d.get("market_price")

    gross_profit = rev - cogs if (rev is not None and cogs is not None) else None

    ratios = {}

    # --- Liquidity ---
    ratios["current_ratio"] = _round(_ratio(ca, cl))
    ratios["quick_ratio"] = _round(_ratio(ca - inv, cl) if (ca is not None and inv is not None and cl) else None)
    ratios["cash_ratio"] = _round(_ratio(cash, cl))

    # --- Leverage ---
    ratios["debt_to_equity"] = _round(_ratio(tl, te))
    ratios["debt_to_assets"] = _round(_ratio(tl, ta))
    ratios["equity_multiplier"] = _round(_ratio(ta, te))
    ratios["interest_coverage"] = _round(_ratio(ebit, interest))

    # --- Profitability ---
    ratios["gross_margin"] = _round(_ratio(gross_profit, rev))
    ratios["operating_margin"] = _round(_ratio(op_inc, rev))
    ratios["net_margin"] = _round(_ratio(ni, rev))
    ratios["roa"] = _round(_ratio(ni, ta))
    ratios["roe"] = _round(_ratio(ni, te))

    # --- Efficiency ---
    ratios["asset_turnover"] = _round(_ratio(rev, ta))
    ratios["inventory_turnover"] = _round(_ratio(cogs, inv))

    # --- Per-share / market ---
    ratios["eps"] = _round(_ratio(ni, shares))
    if ratios.get("eps") and price:
        ratios["pe_ratio"] = _round(price / ratios["eps"])
    if shares and te:
        bvps = te / shares
        ratios["book_value_per_share"] = _round(bvps)
        if price:
            ratios["pb_ratio"] = _round(price / bvps)

    # Strip None values for cleaner output
    available = {k: v for k, v in ratios.items() if v is not None}
    missing = [k for k, v in ratios.items() if v is None]

    return {
        "ratios": available,
        "missing": missing,
        "inputs": {k: v for k, v in d.items() if v is not None},
    }


def _round(x, digits=4):
    return None if x is None else round(x, digits)


def verify():
    # A realistic small example
    data = {
        "revenue": 10000,
        "cogs": 6000,
        "operating_income": 1500,
        "interest_expense": 200,
        "net_income": 1000,
        "current_assets": 3000,
        "current_liabilities": 1500,
        "inventory": 800,
        "cash": 500,
        "total_assets": 8000,
        "total_liabilities": 4000,
        "total_equity": 4000,
        "shares_outstanding": 1000,
        "market_price": 20,
    }
    r = compute(data)
    ratios = r["ratios"]
    # Gross margin = (10000 - 6000) / 10000 = 0.4
    assert ratios["gross_margin"] == 0.4
    # Operating margin = 1500/10000 = 0.15
    assert ratios["operating_margin"] == 0.15
    # Net margin = 1000/10000 = 0.1
    assert ratios["net_margin"] == 0.1
    # Current ratio = 3000/1500 = 2.0
    assert ratios["current_ratio"] == 2.0
    # Quick ratio = (3000 - 800) / 1500 = 1.4667
    assert abs(ratios["quick_ratio"] - 1.4667) < 0.001
    # Cash ratio = 500/1500 = 0.3333
    assert abs(ratios["cash_ratio"] - 0.3333) < 0.001
    # Debt/Equity = 4000/4000 = 1.0
    assert ratios["debt_to_equity"] == 1.0
    # ROE = 1000/4000 = 0.25
    assert ratios["roe"] == 0.25
    # ROA = 1000/8000 = 0.125
    assert ratios["roa"] == 0.125
    # Asset turnover = 10000/8000 = 1.25
    assert ratios["asset_turnover"] == 1.25
    # Interest coverage = 1500/200 = 7.5
    assert ratios["interest_coverage"] == 7.5
    # EPS = 1000/1000 = 1.0
    assert ratios["eps"] == 1.0
    # P/E = 20/1 = 20
    assert ratios["pe_ratio"] == 20.0
    # BVPS = 4000/1000 = 4.0
    assert ratios["book_value_per_share"] == 4.0
    # P/B = 20/4 = 5
    assert ratios["pb_ratio"] == 5.0

    # Partial data — only compute what's available
    r2 = compute({"revenue": 1000, "net_income": 100, "total_equity": 500})
    assert r2["ratios"]["net_margin"] == 0.1
    assert r2["ratios"]["roe"] == 0.2
    assert "current_ratio" in r2["missing"]

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", help="JSON file with financial data")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if not args.input:
        parser.error("--input is required")

    with open(args.input) as f:
        data = json.load(f)
    result = compute(data)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Discounted Cash Flow (DCF) valuation calculator.

Computes enterprise value from projected cash flows using:
  1. Discounted Cash Flow (explicit period)
  2. Terminal Value (Gordon growth model)
  3. Sum of PVs = Enterprise Value

Usage:
  python dcf.py --cash-flows 100,110,120,130,140 --wacc 0.10 --terminal-growth 0.03
  python dcf.py --input data.json
  python dcf.py --verify

IRON LAW: wacc MUST be greater than terminal_growth, otherwise TV diverges.
"""
import argparse
import json
import sys


def compute(cash_flows, wacc, terminal_growth, net_debt=0, shares_outstanding=None):
    """Compute DCF enterprise and equity value.

    Args:
        cash_flows: List of projected free cash flows (year 1, 2, ..., n).
        wacc: Weighted average cost of capital (decimal, e.g., 0.10).
        terminal_growth: Perpetual growth rate after year n (decimal, e.g., 0.03).
        net_debt: Total debt - cash. Subtracted from EV to get equity value.
        shares_outstanding: If provided, also compute per-share value.

    Returns:
        Dict with PV of each CF, terminal value, enterprise value, equity value.
    """
    if not cash_flows:
        raise ValueError("cash_flows cannot be empty")
    if wacc <= terminal_growth:
        raise ValueError(
            f"wacc ({wacc}) must be greater than terminal_growth ({terminal_growth}) "
            "— otherwise terminal value diverges"
        )
    if wacc <= 0:
        raise ValueError("wacc must be positive")

    n = len(cash_flows)
    pvs = []
    for i, cf in enumerate(cash_flows, start=1):
        pv = cf / ((1 + wacc) ** i)
        pvs.append(round(pv, 4))

    # Terminal value at end of year n: TV_n = CF_{n+1} / (wacc - g)
    # where CF_{n+1} = CF_n * (1 + g)
    last_cf = cash_flows[-1]
    terminal_cf = last_cf * (1 + terminal_growth)
    terminal_value_at_n = terminal_cf / (wacc - terminal_growth)
    # Discount terminal value back to present
    pv_terminal = terminal_value_at_n / ((1 + wacc) ** n)

    enterprise_value = sum(pvs) + pv_terminal
    equity_value = enterprise_value - net_debt

    result = {
        "pv_explicit": [round(pv, 2) for pv in pvs],
        "sum_pv_explicit": round(sum(pvs), 2),
        "terminal_value_at_year_n": round(terminal_value_at_n, 2),
        "pv_terminal_value": round(pv_terminal, 2),
        "enterprise_value": round(enterprise_value, 2),
        "equity_value": round(equity_value, 2),
        "terminal_value_pct_of_ev": round(pv_terminal / enterprise_value * 100, 1),
        "inputs": {
            "cash_flows": cash_flows,
            "wacc": wacc,
            "terminal_growth": terminal_growth,
            "net_debt": net_debt,
        },
    }

    if shares_outstanding:
        result["per_share_value"] = round(equity_value / shares_outstanding, 2)
        result["inputs"]["shares_outstanding"] = shares_outstanding

    return result


def verify():
    """Self-test with known values."""
    # Simple case: 5 years CF=100, WACC=10%, g=0%
    # PV each year: 100/1.1, 100/1.21, 100/1.331, 100/1.4641, 100/1.61051
    # = 90.91 + 82.64 + 75.13 + 68.30 + 62.09 = 379.08
    # TV at year 5 = 100 * 1.0 / (0.10 - 0) = 1000
    # PV of TV = 1000 / 1.61051 = 620.92
    # EV = 379.08 + 620.92 = 1000.00
    r = compute([100, 100, 100, 100, 100], 0.10, 0.00)
    assert abs(r["enterprise_value"] - 1000.00) < 0.1, f"EV: expected ~1000, got {r['enterprise_value']}"

    # Growing CF case: CF=[100,110,121,133.1,146.41], WACC=10%, g=3%
    # Last CF next year = 146.41 * 1.03 = 150.8
    # TV = 150.8 / (0.10 - 0.03) = 2154.29
    # PV TV = 2154.29 / 1.61051 ≈ 1337.63
    r2 = compute([100, 110, 121, 133.1, 146.41], 0.10, 0.03)
    assert r2["enterprise_value"] > 0

    # Validation: wacc must exceed growth
    try:
        compute([100], 0.05, 0.05)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    # Per-share: EV=1000, debt=200, shares=100 → equity=800 → per share=8.0
    r3 = compute([100, 100, 100, 100, 100], 0.10, 0.00, net_debt=200, shares_outstanding=100)
    assert r3["per_share_value"] == 8.0, f"Per share: expected 8.0, got {r3['per_share_value']}"

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cash-flows", help="Comma-separated list of CFs, e.g. 100,110,120")
    parser.add_argument("--wacc", type=float)
    parser.add_argument("--terminal-growth", type=float)
    parser.add_argument("--net-debt", type=float, default=0)
    parser.add_argument("--shares-outstanding", type=float)
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
        if not (args.cash_flows and args.wacc is not None and args.terminal_growth is not None):
            parser.error("Provide --cash-flows, --wacc, --terminal-growth or use --input")
        cfs = [float(x) for x in args.cash_flows.split(",")]
        result = compute(cfs, args.wacc, args.terminal_growth, args.net_debt, args.shares_outstanding)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

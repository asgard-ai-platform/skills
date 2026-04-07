#!/usr/bin/env python3
"""
Break-even analysis calculator.

Computes break-even point in units and revenue, contribution margin,
and the contribution margin ratio.

Usage:
  python breakeven.py --fixed-costs 100000 --price 50 --variable-cost 30
  python breakeven.py --input data.json
  python breakeven.py --verify

Formula: BEQ = Fixed Costs / (Price - Variable Cost per unit)
"""
import argparse
import json
import sys


def compute(fixed_costs, price, variable_cost, target_profit=0):
    """Compute break-even point and margin metrics.

    Args:
        fixed_costs: Total fixed costs per period.
        price: Selling price per unit.
        variable_cost: Variable cost per unit.
        target_profit: Optional profit target to reach (default 0 = break-even).

    Returns:
        Dict with break-even quantity, revenue, contribution margin, ratio.
    """
    if price <= variable_cost:
        raise ValueError("price must be greater than variable_cost (negative contribution margin)")
    if fixed_costs < 0:
        raise ValueError("fixed_costs cannot be negative")

    contribution_margin = price - variable_cost
    cm_ratio = contribution_margin / price

    # Break-even with optional profit target
    break_even_qty = (fixed_costs + target_profit) / contribution_margin
    break_even_revenue = break_even_qty * price

    # Margin of safety at break-even is 0 by definition; include sensitivity info
    # 10% price drop impact
    price_drop_10 = price * 0.9
    cm_if_price_drops = price_drop_10 - variable_cost
    beq_if_price_drops = (
        (fixed_costs + target_profit) / cm_if_price_drops if cm_if_price_drops > 0 else float("inf")
    )

    return {
        "break_even_quantity": round(break_even_qty, 2),
        "break_even_revenue": round(break_even_revenue, 2),
        "contribution_margin_per_unit": round(contribution_margin, 2),
        "contribution_margin_ratio": round(cm_ratio, 4),
        "sensitivity": {
            "beq_if_price_drops_10pct": round(beq_if_price_drops, 2),
            "pct_increase_needed": round((beq_if_price_drops / break_even_qty - 1) * 100, 2)
            if break_even_qty > 0
            else 0,
        },
        "inputs": {
            "fixed_costs": fixed_costs,
            "price": price,
            "variable_cost": variable_cost,
            "target_profit": target_profit,
        },
    }


def verify():
    """Self-test with known values."""
    # Case 1: FC=100000, P=50, VC=30
    # CM = 20, CM ratio = 0.4
    # BEQ = 100000 / 20 = 5000 units
    # Revenue = 5000 * 50 = 250000
    r = compute(100_000, 50, 30)
    assert r["break_even_quantity"] == 5000.0, f"BEQ: expected 5000, got {r['break_even_quantity']}"
    assert r["break_even_revenue"] == 250_000.0, f"Revenue: expected 250000, got {r['break_even_revenue']}"
    assert r["contribution_margin_per_unit"] == 20.0
    assert r["contribution_margin_ratio"] == 0.4

    # Case 2: With target profit
    # BEQ = (100000 + 20000) / 20 = 6000
    r2 = compute(100_000, 50, 30, target_profit=20_000)
    assert r2["break_even_quantity"] == 6000.0, f"BEQ with profit: expected 6000, got {r2['break_even_quantity']}"

    # Case 3: Invalid (negative contribution margin)
    try:
        compute(100_000, 20, 30)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--fixed-costs", type=float)
    parser.add_argument("--price", type=float)
    parser.add_argument("--variable-cost", type=float)
    parser.add_argument("--target-profit", type=float, default=0)
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
        if None in (args.fixed_costs, args.price, args.variable_cost):
            parser.error("Provide --fixed-costs, --price, --variable-cost or use --input")
        result = compute(args.fixed_costs, args.price, args.variable_cost, args.target_profit)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

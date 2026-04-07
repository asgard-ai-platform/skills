#!/usr/bin/env python3
"""
Economic Order Quantity (EOQ) calculator.

EOQ = sqrt(2 * D * S / H)

Where:
  D = annual demand (units)
  S = fixed cost per order
  H = holding cost per unit per year

Usage:
  python eoq.py --demand 10000 --order-cost 100 --holding-cost 4
  python eoq.py --input data.json
  python eoq.py --verify
"""
import argparse
import json
import math


def compute(annual_demand, order_cost, holding_cost, lead_time_days=0, daily_demand=None):
    """Compute EOQ and related metrics.

    Args:
        annual_demand: D — annual demand in units.
        order_cost: S — cost per order (setup + processing).
        holding_cost: H — holding cost per unit per year.
        lead_time_days: For computing reorder point.
        daily_demand: If None, computed as annual_demand / 365.
    """
    if annual_demand <= 0 or order_cost <= 0 or holding_cost <= 0:
        raise ValueError("All inputs must be positive")

    eoq = math.sqrt(2 * annual_demand * order_cost / holding_cost)
    orders_per_year = annual_demand / eoq
    cycle_days = 365 / orders_per_year

    # Total annual cost at EOQ
    annual_ordering_cost = orders_per_year * order_cost
    annual_holding_cost = (eoq / 2) * holding_cost  # average inventory = EOQ/2
    total_annual_cost = annual_ordering_cost + annual_holding_cost

    # Reorder point (no safety stock)
    if daily_demand is None:
        daily_demand = annual_demand / 365
    reorder_point = daily_demand * lead_time_days

    # Verify: at EOQ, ordering cost should equal holding cost (approximately)
    cost_balance_ratio = annual_ordering_cost / annual_holding_cost if annual_holding_cost > 0 else float("inf")

    return {
        "eoq": round(eoq, 2),
        "orders_per_year": round(orders_per_year, 2),
        "cycle_days": round(cycle_days, 2),
        "annual_ordering_cost": round(annual_ordering_cost, 2),
        "annual_holding_cost": round(annual_holding_cost, 2),
        "total_annual_cost": round(total_annual_cost, 2),
        "reorder_point": round(reorder_point, 2),
        "cost_balance_check": {
            "ordering_equals_holding": abs(cost_balance_ratio - 1.0) < 0.01,
            "ratio": round(cost_balance_ratio, 4),
            "note": "At EOQ, ordering cost should equal holding cost",
        },
        "inputs": {
            "annual_demand": annual_demand,
            "order_cost": order_cost,
            "holding_cost": holding_cost,
            "lead_time_days": lead_time_days,
        },
    }


def verify():
    """Self-test with known values."""
    # Example from the SKILL.md:
    # D=10000, S=100, H=4
    # EOQ = sqrt(2*10000*100/4) = sqrt(500000) ≈ 707.11
    r = compute(10000, 100, 4)
    assert abs(r["eoq"] - 707.11) < 0.1, f"EOQ: expected ~707.11, got {r['eoq']}"

    # Verify cost balance at EOQ (ordering == holding)
    assert r["cost_balance_check"]["ordering_equals_holding"], "Costs should balance at EOQ"

    # Orders per year ≈ 10000 / 707.11 ≈ 14.14
    assert abs(r["orders_per_year"] - 14.14) < 0.1

    # Total cost at EOQ = sqrt(2*D*S*H) = sqrt(2*10000*100*4) = sqrt(8000000) ≈ 2828.43
    # (Ordering cost 1414.21 + Holding cost 1414.21; they are equal at EOQ.)
    assert abs(r["total_annual_cost"] - 2828.43) < 1

    # Error handling
    try:
        compute(-100, 50, 2)
        assert False, "Should reject negative demand"
    except ValueError:
        pass

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--demand", type=float, help="Annual demand (D)")
    parser.add_argument("--order-cost", type=float, help="Cost per order (S)")
    parser.add_argument("--holding-cost", type=float, help="Holding cost per unit per year (H)")
    parser.add_argument("--lead-time-days", type=float, default=0)
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
        if None in (args.demand, args.order_cost, args.holding_cost):
            parser.error("Provide --demand, --order-cost, --holding-cost or use --input")
        result = compute(args.demand, args.order_cost, args.holding_cost, args.lead_time_days)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

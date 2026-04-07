#!/usr/bin/env python3
"""
Safety stock calculator with combined demand and lead-time variability.

SS = z × sqrt(LT × sigma_d^2 + d^2 × sigma_LT^2)
ROP = d × LT + SS

Where:
  z        = service factor from normal distribution
  LT       = average lead time (days/weeks)
  sigma_d  = std dev of per-period demand
  d        = average per-period demand
  sigma_LT = std dev of lead time

Usage:
  python safety_stock.py --avg-demand 100 --sd-demand 30 --avg-lt 4 --sd-lt 1 --service-level 0.95
  python safety_stock.py --input data.json
  python safety_stock.py --verify

IRON LAW: Going from 95% → 99% service level roughly DOUBLES safety stock.
Always quantify the incremental holding cost.
"""
import argparse
import json
import math


# z-scores for common service levels (one-sided, for cycle service level)
Z_TABLE = {
    0.50: 0.0000,
    0.80: 0.8416,
    0.85: 1.0364,
    0.90: 1.2816,
    0.95: 1.6449,
    0.97: 1.8808,
    0.98: 2.0537,
    0.99: 2.3263,
    0.995: 2.5758,
    0.999: 3.0902,
}


def get_z(service_level):
    """Get z-score for a service level, rounded to nearest tabulated value."""
    if service_level in Z_TABLE:
        return Z_TABLE[service_level]
    # Compute via inverse normal CDF for arbitrary levels
    # Beasley-Springer-Moro approximation
    p = service_level
    if p <= 0 or p >= 1:
        raise ValueError("service_level must be in (0, 1)")
    # Use Abramowitz-Stegun 26.2.23 for p > 0.5
    sign = 1
    if p < 0.5:
        sign = -1
        p = 1 - p
    t = math.sqrt(-2 * math.log(1 - p))
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    z = t - (c0 + c1 * t + c2 * t * t) / (1 + d1 * t + d2 * t * t + d3 * t * t * t)
    return sign * z


def compute(avg_demand, sd_demand, avg_lead_time, sd_lead_time, service_level, holding_cost_per_unit_per_year=None):
    """Compute safety stock and reorder point."""
    if avg_demand < 0 or sd_demand < 0 or avg_lead_time <= 0 or sd_lead_time < 0:
        raise ValueError("demand/lead-time inputs must be non-negative (LT > 0)")
    if not (0 < service_level < 1):
        raise ValueError("service_level must be in (0, 1)")

    z = get_z(service_level)

    # Combined std dev of demand over lead time
    combined_variance = avg_lead_time * sd_demand ** 2 + (avg_demand ** 2) * (sd_lead_time ** 2)
    combined_sigma = math.sqrt(combined_variance)
    safety_stock = z * combined_sigma
    reorder_point = avg_demand * avg_lead_time + safety_stock

    result = {
        "safety_stock": round(safety_stock, 2),
        "reorder_point": round(reorder_point, 2),
        "z_score": round(z, 4),
        "service_level": service_level,
        "combined_sigma": round(combined_sigma, 4),
        "cycle_demand_expected": round(avg_demand * avg_lead_time, 2),
        "contributions": {
            "from_demand_variability": round(math.sqrt(avg_lead_time) * sd_demand * z, 2),
            "from_leadtime_variability": round(avg_demand * sd_lead_time * z, 2),
        },
        "inputs": {
            "avg_demand": avg_demand,
            "sd_demand": sd_demand,
            "avg_lead_time": avg_lead_time,
            "sd_lead_time": sd_lead_time,
            "service_level": service_level,
        },
    }

    if holding_cost_per_unit_per_year is not None:
        result["annual_holding_cost"] = round(safety_stock * holding_cost_per_unit_per_year, 2)

    # Sensitivity: cost of going 1 service-level tier higher
    tiers = [0.90, 0.95, 0.99, 0.999]
    if service_level in tiers:
        idx = tiers.index(service_level)
        if idx < len(tiers) - 1:
            next_level = tiers[idx + 1]
            z_next = get_z(next_level)
            ss_next = z_next * combined_sigma
            result["next_tier_cost"] = {
                "level": next_level,
                "safety_stock": round(ss_next, 2),
                "increment_pct": round((ss_next / safety_stock - 1) * 100, 2) if safety_stock > 0 else None,
            }

    return result


def verify():
    # Example from SKILL.md:
    # avg_demand=100, sd_demand=30, avg_lt=4, sd_lt=1, sl=0.95
    # Combined variance = 4*900 + 10000*1 = 13600
    # Combined sigma = sqrt(13600) ≈ 116.619
    # z(0.95) = 1.6449
    # SS = 1.6449 * 116.619 ≈ 191.83
    # ROP = 100*4 + 191.83 = 591.83
    r = compute(100, 30, 4, 1, 0.95)
    assert abs(r["safety_stock"] - 191.83) < 1, f"SS: expected ~191.83, got {r['safety_stock']}"
    assert abs(r["reorder_point"] - 591.83) < 1

    # 95% → 99% roughly doubles safety stock (iron law check)
    r95 = compute(100, 30, 4, 1, 0.95)
    r99 = compute(100, 30, 4, 1, 0.99)
    ratio = r99["safety_stock"] / r95["safety_stock"]
    assert 1.3 < ratio < 1.6, f"99/95 ratio expected ~1.41, got {ratio}"

    # Zero variability → safety stock should be 0
    r0 = compute(100, 0, 4, 0, 0.95)
    assert r0["safety_stock"] == 0
    assert r0["reorder_point"] == 400

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--avg-demand", type=float)
    parser.add_argument("--sd-demand", type=float)
    parser.add_argument("--avg-lt", type=float, help="Average lead time")
    parser.add_argument("--sd-lt", type=float, help="Lead-time std dev")
    parser.add_argument("--service-level", type=float, default=0.95)
    parser.add_argument("--holding-cost", type=float, help="Holding cost per unit per year (optional)")
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
        if None in (args.avg_demand, args.sd_demand, args.avg_lt, args.sd_lt):
            parser.error("Provide --avg-demand --sd-demand --avg-lt --sd-lt")
        result = compute(args.avg_demand, args.sd_demand, args.avg_lt, args.sd_lt,
                         args.service_level, args.holding_cost)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

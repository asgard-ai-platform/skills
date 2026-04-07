#!/usr/bin/env python3
"""
Process Capability Index (Cpk) calculator.

Cp  = (USL - LSL) / (6 * sigma)          — potential capability (ignores centering)
Cpk = min((USL - mu) / (3*sigma),         — actual capability (accounts for centering)
          (mu - LSL) / (3*sigma))
Pp/Ppk are same formulas but using overall sigma (long-term).
PPM defective is estimated from normal distribution.

Usage:
  python cpk.py --usl 55 --lsl 45 --mean 50.2 --sd 1.5
  python cpk.py --input data.json
  python cpk.py --verify

IRON LAW: Cpk is only valid when the process is in statistical control.
Run SPC charts first.
"""
import argparse
import json
import math


def norm_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def compute(usl=None, lsl=None, mean=None, sd=None, target=None):
    """Compute Cp, Cpk, and PPM defective."""
    if sd is None or sd <= 0:
        raise ValueError("sd must be positive")
    if mean is None:
        raise ValueError("mean is required")
    if usl is None and lsl is None:
        raise ValueError("at least one of usl or lsl must be provided")

    result = {"inputs": {"usl": usl, "lsl": lsl, "mean": mean, "sd": sd, "target": target}}

    # Two-sided
    if usl is not None and lsl is not None:
        if usl <= lsl:
            raise ValueError("usl must be greater than lsl")
        cp = (usl - lsl) / (6 * sd)
        cpu = (usl - mean) / (3 * sd)
        cpl = (mean - lsl) / (3 * sd)
        cpk = min(cpu, cpl)

        # PPM defective via normal distribution
        # P(X > USL) + P(X < LSL) assuming X ~ N(mean, sd^2)
        p_above = 1 - norm_cdf((usl - mean) / sd)
        p_below = norm_cdf((lsl - mean) / sd)
        ppm = (p_above + p_below) * 1_000_000

        result["cp"] = round(cp, 4)
        result["cpk"] = round(cpk, 4)
        result["cpu"] = round(cpu, 4)
        result["cpl"] = round(cpl, 4)
        result["ppm_defective"] = round(ppm, 2)
        result["centering_shift"] = round(mean - (usl + lsl) / 2, 4)
        result["cp_minus_cpk"] = round(cp - cpk, 4)

        # Target-based Cpm (if target given)
        if target is not None:
            tau_sq = sd ** 2 + (mean - target) ** 2
            tau = math.sqrt(tau_sq)
            cpm = (usl - lsl) / (6 * tau)
            result["cpm"] = round(cpm, 4)

        # Interpretation
        if cpk >= 1.67:
            assessment = "excellent (critical-to-quality)"
        elif cpk >= 1.33:
            assessment = "capable (standard acceptance)"
        elif cpk >= 1.0:
            assessment = "marginal (needs improvement)"
        else:
            assessment = "incapable (process will produce defects)"
        result["assessment"] = assessment

    # One-sided upper
    elif usl is not None:
        cpu = (usl - mean) / (3 * sd)
        result["cpu"] = round(cpu, 4)
        result["cpk"] = round(cpu, 4)
        p_above = 1 - norm_cdf((usl - mean) / sd)
        result["ppm_defective"] = round(p_above * 1_000_000, 2)

    # One-sided lower
    else:
        cpl = (mean - lsl) / (3 * sd)
        result["cpl"] = round(cpl, 4)
        result["cpk"] = round(cpl, 4)
        p_below = norm_cdf((lsl - mean) / sd)
        result["ppm_defective"] = round(p_below * 1_000_000, 2)

    return result


def verify():
    # Textbook: USL=55, LSL=45, mean=50, sd=1.5 (perfectly centered)
    # Cp = 10 / 9 = 1.1111
    # Cpk = min((55-50)/(4.5), (50-45)/(4.5)) = min(1.1111, 1.1111) = 1.1111
    r = compute(usl=55, lsl=45, mean=50, sd=1.5)
    assert abs(r["cp"] - 1.1111) < 0.001
    assert abs(r["cpk"] - 1.1111) < 0.001
    assert r["cp_minus_cpk"] == 0.0  # perfectly centered

    # Off-center case: mean=50.2
    # Cpu = (55-50.2)/(4.5) = 1.0667
    # Cpl = (50.2-45)/(4.5) = 1.1556
    # Cpk = min = 1.0667
    r2 = compute(usl=55, lsl=45, mean=50.2, sd=1.5)
    assert abs(r2["cpk"] - 1.0667) < 0.001
    # Cp unchanged (depends only on spec width + sd)
    assert abs(r2["cp"] - 1.1111) < 0.001

    # 6-sigma process: mean centered, USL-LSL = 12*sigma → Cp = 2.0
    r3 = compute(usl=56, lsl=44, mean=50, sd=1)
    # Spec width = 12, 6*sd = 6, Cp = 2.0
    assert abs(r3["cp"] - 2.0) < 0.001
    assert abs(r3["cpk"] - 2.0) < 0.001
    # PPM should be very low (<1)
    assert r3["ppm_defective"] < 2

    # Low Cpk — real defect expected
    r4 = compute(usl=55, lsl=45, mean=50, sd=3)
    # Cp = 10/18 = 0.5556
    assert abs(r4["cp"] - 0.5556) < 0.001
    assert "incapable" in r4["assessment"]

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--usl", type=float)
    parser.add_argument("--lsl", type=float)
    parser.add_argument("--mean", type=float)
    parser.add_argument("--sd", type=float)
    parser.add_argument("--target", type=float, help="Target value for Cpm")
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
        result = compute(usl=args.usl, lsl=args.lsl, mean=args.mean, sd=args.sd, target=args.target)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
A/B test two-proportion z-test calculator.

Computes:
  - Observed proportions (p1, p2)
  - Pooled proportion
  - z-statistic
  - Two-sided p-value (via math.erf → normal CDF)
  - Confidence interval for the difference
  - Effect size (Cohen's h)
  - Minimum Detectable Effect at 80% power (planning tool)

Usage:
  python ab_test.py --conv1 210 --n1 5000 --conv2 190 --n2 5000
  python ab_test.py --input data.json
  python ab_test.py --verify

IRON LAW: Statistical significance ≠ practical significance.
Always report effect size (Cohen's h) alongside p-value.
"""
import argparse
import json
import math


def norm_cdf(x):
    """Standard normal CDF using math.erf."""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def norm_ppf(p):
    """
    Inverse normal CDF (probit) using Beasley-Springer-Moro approximation.
    Accurate to ~1e-7 for p in (0.02, 0.98), good enough for A/B testing.
    """
    if p <= 0 or p >= 1:
        raise ValueError("p must be in (0, 1)")
    # Use symmetry
    sign = 1
    if p < 0.5:
        sign = -1
        p = 1 - p
    # Beasley-Springer-Moro constants
    a = [-39.6968302866538, 220.946098424521, -275.928510446969,
         138.357751867269, -30.6647980661472, 2.50662827745924]
    b = [-54.4760987982241, 161.585836858041, -155.698979859887,
         66.8013118877197, -13.2806815528857]
    c = [-7.78489400243029e-3, -0.322396458041136, -2.40075827716184,
         -2.54973253934373, 4.37466414146497, 2.93816398269878]
    d = [7.78469570904146e-3, 0.32246712907004, 2.445134137143,
         3.75440866190742]
    p_low = 0.02425
    p_high = 1 - p_low
    if p < p_low:
        q = math.sqrt(-2 * math.log(p))
        x = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / \
            ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    elif p <= p_high:
        q = p - 0.5
        r = q * q
        x = (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / \
            (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1)
    else:
        q = math.sqrt(-2 * math.log(1 - p))
        x = -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / \
             ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    return sign * x


def compute(conv1, n1, conv2, n2, alpha=0.05):
    """Run two-proportion z-test."""
    if n1 <= 0 or n2 <= 0:
        raise ValueError("Sample sizes must be positive")
    if conv1 < 0 or conv1 > n1 or conv2 < 0 or conv2 > n2:
        raise ValueError("Conversions must be between 0 and n")

    p1 = conv1 / n1
    p2 = conv2 / n2
    p_pool = (conv1 + conv2) / (n1 + n2)

    se_pool = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    if se_pool == 0:
        return {"error": "zero variance, cannot compute z-statistic"}
    z = (p2 - p1) / se_pool
    # Two-sided p-value
    p_value = 2 * (1 - norm_cdf(abs(z)))

    # Confidence interval for difference (unpooled SE)
    se_diff = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    z_crit = norm_ppf(1 - alpha / 2)
    diff = p2 - p1
    ci_low = diff - z_crit * se_diff
    ci_high = diff + z_crit * se_diff

    # Cohen's h effect size
    # h = 2 * (arcsin(sqrt(p2)) - arcsin(sqrt(p1)))
    h = 2 * (math.asin(math.sqrt(p2)) - math.asin(math.sqrt(p1)))
    abs_h = abs(h)
    if abs_h < 0.2:
        effect_magnitude = "negligible"
    elif abs_h < 0.5:
        effect_magnitude = "small"
    elif abs_h < 0.8:
        effect_magnitude = "medium"
    else:
        effect_magnitude = "large"

    # Significance decision
    significant = p_value < alpha
    if significant:
        decision = f"Reject H0 at alpha={alpha}"
    else:
        decision = f"Fail to reject H0 at alpha={alpha}"

    return {
        "p1": round(p1, 6),
        "p2": round(p2, 6),
        "p_pooled": round(p_pool, 6),
        "absolute_diff": round(diff, 6),
        "relative_lift_pct": round(diff / p1 * 100, 4) if p1 > 0 else None,
        "z_statistic": round(z, 4),
        "p_value_two_sided": round(p_value, 6),
        "confidence_interval": [round(ci_low, 6), round(ci_high, 6)],
        "confidence_level": round(1 - alpha, 2),
        "cohens_h": round(h, 6),
        "effect_magnitude": effect_magnitude,
        "significant": significant,
        "decision": decision,
        "practical_note": (
            "Statistical significance is not the same as practical significance. "
            "A negligible effect size with a significant p-value means the test was "
            "sensitive enough to detect a tiny, possibly meaningless, difference."
        ),
        "inputs": {"conv1": conv1, "n1": n1, "conv2": conv2, "n2": n2, "alpha": alpha},
    }


def sample_size_for_mde(baseline_rate, mde_relative, alpha=0.05, power=0.80):
    """Compute required sample size per arm for a given MDE."""
    p1 = baseline_rate
    p2 = baseline_rate * (1 + mde_relative)
    p_bar = (p1 + p2) / 2
    z_alpha = norm_ppf(1 - alpha / 2)
    z_beta = norm_ppf(power)
    n = ((z_alpha * math.sqrt(2 * p_bar * (1 - p_bar)) +
          z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2) / (p2 - p1) ** 2
    return math.ceil(n)


def verify():
    # Classic A/B: 210/5000 vs 190/5000
    # p1 = 0.042, p2 = 0.038 → negative difference
    # Pooled = 400/10000 = 0.04
    # SE_pool = sqrt(0.04*0.96*(1/5000+1/5000)) = sqrt(0.04*0.96*0.0004) = sqrt(0.00001536) ≈ 0.003919
    # z = (0.038 - 0.042) / 0.003919 ≈ -1.02
    # p ≈ 0.308 (two-sided)
    r = compute(210, 5000, 190, 5000)
    assert r["p1"] == 0.042
    assert r["p2"] == 0.038
    assert abs(r["z_statistic"] - (-1.0206)) < 0.01
    assert abs(r["p_value_two_sided"] - 0.3074) < 0.005
    assert r["significant"] is False
    assert r["effect_magnitude"] == "negligible"

    # Large significant effect
    r2 = compute(500, 5000, 300, 5000)
    # p1=0.1, p2=0.06 → large diff
    assert r2["significant"] is True
    assert r2["p_value_two_sided"] < 0.001

    # Sample size planning
    # To detect 10% relative lift on a 5% baseline at alpha=0.05, power=0.80
    n = sample_size_for_mde(0.05, 0.10)
    assert 25000 < n < 35000, f"Sample size: expected ~30000, got {n}"

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--conv1", type=int)
    parser.add_argument("--n1", type=int)
    parser.add_argument("--conv2", type=int)
    parser.add_argument("--n2", type=int)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--mde-baseline", type=float, help="Sample size planning: baseline rate")
    parser.add_argument("--mde-relative", type=float, help="Sample size planning: MDE as relative change")
    parser.add_argument("--power", type=float, default=0.80)
    parser.add_argument("--input", help="JSON file")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if args.mde_baseline is not None and args.mde_relative is not None:
        n = sample_size_for_mde(args.mde_baseline, args.mde_relative, args.alpha, args.power)
        result = {
            "sample_size_per_arm": n,
            "baseline": args.mde_baseline,
            "mde_relative": args.mde_relative,
            "alpha": args.alpha,
            "power": args.power,
        }
    elif args.input:
        with open(args.input) as f:
            data = json.load(f)
        result = compute(**data)
    elif None not in (args.conv1, args.n1, args.conv2, args.n2):
        result = compute(args.conv1, args.n1, args.conv2, args.n2, args.alpha)
    else:
        parser.error("Provide --conv1 --n1 --conv2 --n2, OR --mde-baseline --mde-relative, OR --input")

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Capital Asset Pricing Model (CAPM) calculator.

E(Ri) = Rf + β_i * (E(Rm) - Rf)

Computes expected return, risk premium, and alpha (if actual return provided).

Usage:
  python capm.py --risk-free 0.03 --market-return 0.10 --beta 1.2
  python capm.py --risk-free 0.03 --market-return 0.10 --beta 1.2 --actual-return 0.15
  python capm.py --input data.json
  python capm.py --verify
"""
import argparse
import json


def compute(risk_free, market_return, beta, actual_return=None):
    """Compute CAPM expected return and related metrics.

    Args:
        risk_free: Rf (decimal, e.g., 0.03 for 3%).
        market_return: E(Rm) — expected market return (decimal).
        beta: Beta coefficient of the asset/portfolio.
        actual_return: Optional — if provided, compute alpha.

    Returns:
        Dict with expected return, risk premium, alpha, interpretation.
    """
    market_risk_premium = market_return - risk_free
    expected_return = risk_free + beta * market_risk_premium
    beta_contribution = beta * market_risk_premium

    # Interpret beta
    if beta < 0:
        beta_type = "inverse (moves opposite to market)"
    elif beta < 0.5:
        beta_type = "low (defensive)"
    elif beta < 1.0:
        beta_type = "below market (less volatile than market)"
    elif beta == 1.0:
        beta_type = "market (moves with market)"
    elif beta <= 1.5:
        beta_type = "above market (more volatile than market)"
    else:
        beta_type = "high (aggressive, much more volatile than market)"

    result = {
        "expected_return": round(expected_return, 6),
        "expected_return_pct": f"{expected_return * 100:.2f}%",
        "risk_free_rate": risk_free,
        "market_risk_premium": round(market_risk_premium, 6),
        "beta": beta,
        "beta_type": beta_type,
        "beta_contribution": round(beta_contribution, 6),
        "inputs": {
            "risk_free": risk_free,
            "market_return": market_return,
            "beta": beta,
        },
    }

    if actual_return is not None:
        alpha = actual_return - expected_return
        if alpha > 0.001:
            verdict = "outperforming (positive alpha)"
        elif alpha < -0.001:
            verdict = "underperforming (negative alpha)"
        else:
            verdict = "fairly priced (zero alpha)"
        result["actual_return"] = actual_return
        result["alpha"] = round(alpha, 6)
        result["alpha_pct"] = f"{alpha * 100:.2f}%"
        result["verdict"] = verdict

    return result


def verify():
    """Self-test with known values."""
    # Case 1: Rf=3%, E(Rm)=10%, β=1.2
    # Risk premium = 10% - 3% = 7%
    # E(Ri) = 3% + 1.2 * 7% = 3% + 8.4% = 11.4%
    r = compute(0.03, 0.10, 1.2)
    assert abs(r["expected_return"] - 0.114) < 1e-6, f"Expected 0.114, got {r['expected_return']}"
    assert r["market_risk_premium"] == 0.07

    # Case 2: β=1.0 → expected return equals market return
    r2 = compute(0.03, 0.10, 1.0)
    assert r2["expected_return"] == 0.10

    # Case 3: β=0 → expected return equals risk-free rate
    r3 = compute(0.03, 0.10, 0.0)
    assert r3["expected_return"] == 0.03

    # Case 4: With actual return → positive alpha
    # E(Ri) = 11.4%, actual = 15% → alpha = +3.6%
    r4 = compute(0.03, 0.10, 1.2, actual_return=0.15)
    assert abs(r4["alpha"] - 0.036) < 1e-6
    assert "outperforming" in r4["verdict"]

    # Case 5: Negative alpha
    r5 = compute(0.03, 0.10, 1.2, actual_return=0.08)
    assert r5["alpha"] < 0
    assert "underperforming" in r5["verdict"]

    # Case 6: Negative beta (inverse ETF)
    r6 = compute(0.03, 0.10, -0.5)
    # E(Ri) = 3% + (-0.5)*7% = 3% - 3.5% = -0.5%
    assert abs(r6["expected_return"] - (-0.005)) < 1e-6

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--risk-free", type=float, help="Risk-free rate (decimal, e.g., 0.03)")
    parser.add_argument("--market-return", type=float, help="Expected market return (decimal)")
    parser.add_argument("--beta", type=float, help="Asset/portfolio beta")
    parser.add_argument("--actual-return", type=float, help="Actual return (optional, for alpha)")
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
        if None in (args.risk_free, args.market_return, args.beta):
            parser.error("Provide --risk-free, --market-return, --beta or use --input")
        result = compute(args.risk_free, args.market_return, args.beta, args.actual_return)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

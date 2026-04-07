#!/usr/bin/env python3
"""
SaaS Unit Economics calculator.

Computes ARPU, payback period, LTV, LTV/CAC, magic number, burn multiple,
NRR (net revenue retention), GRR (gross revenue retention), and the SaaS
Quick Ratio — the standard set of metrics used in SaaS board decks.

Usage:
  python unit_economics.py --input data.json
  python unit_economics.py --verify

Input JSON keys:
  new_mrr                  New MRR added this period
  expansion_mrr            Upgrades from existing customers
  contraction_mrr          Downgrades
  churned_mrr              MRR lost to churn
  starting_mrr             Period-starting MRR (for NRR/GRR)
  ending_mrr               Period-ending MRR
  sales_and_marketing_cost Total S&M spend
  gross_margin             0-1
  monthly_churn            0-1
  cash_burned              Net cash burn this period (for burn multiple)
  new_arr_added            Net new ARR added (for burn multiple + magic number)
"""
import argparse
import json


def compute(**d):
    """Compute SaaS unit economics metrics."""
    result = {}

    new_mrr = d.get("new_mrr", 0)
    expansion = d.get("expansion_mrr", 0)
    contraction = d.get("contraction_mrr", 0)
    churned = d.get("churned_mrr", 0)
    starting = d.get("starting_mrr")
    ending = d.get("ending_mrr")
    sm = d.get("sales_and_marketing_cost")
    gm = d.get("gross_margin")
    churn = d.get("monthly_churn")
    burn = d.get("cash_burned")
    new_arr = d.get("new_arr_added")

    # NRR = (starting + expansion - contraction - churn) / starting
    if starting and starting > 0:
        nrr_num = starting + expansion - contraction - churned
        result["nrr"] = round(nrr_num / starting, 4)
        result["grr"] = round((starting - contraction - churned) / starting, 4)

    # SaaS Quick Ratio = (new + expansion) / (contraction + churn)
    denominator = contraction + churned
    if denominator > 0:
        result["saas_quick_ratio"] = round((new_mrr + expansion) / denominator, 2)
    elif new_mrr + expansion > 0:
        result["saas_quick_ratio"] = float("inf")

    # LTV = (ARPU * GM) / churn    (ARPU ≈ average MRR per customer, but here assume
    # the caller provides monthly_arpu; derive from starting_mrr if customer_count given)
    monthly_arpu = d.get("monthly_arpu")
    customer_count = d.get("customer_count")
    if monthly_arpu is None and starting and customer_count:
        monthly_arpu = starting / customer_count
    if monthly_arpu is not None and gm is not None and churn:
        ltv = monthly_arpu * gm / churn
        result["ltv"] = round(ltv, 2)
        result["monthly_arpu"] = round(monthly_arpu, 2)

    # CAC + Payback (if new customer count provided)
    new_customers = d.get("new_customers")
    if sm is not None and new_customers:
        cac = sm / new_customers
        result["cac"] = round(cac, 2)
        if monthly_arpu is not None and gm is not None:
            contribution_monthly = monthly_arpu * gm
            if contribution_monthly > 0:
                result["cac_payback_months"] = round(cac / contribution_monthly, 2)
                if "ltv" in result:
                    result["ltv_cac_ratio"] = round(result["ltv"] / cac, 2)

    # Magic Number = (new ARR this Q * 4) / (S&M spend last Q) — approximate
    if sm is not None and new_arr is not None and sm > 0:
        result["magic_number"] = round((new_arr) / sm, 2)

    # Burn multiple = net burn / net new ARR
    if burn is not None and new_arr is not None and new_arr > 0:
        result["burn_multiple"] = round(burn / new_arr, 2)

    # Rule of 40 = growth rate + profit margin
    growth_rate = d.get("growth_rate_pct")
    profit_margin_pct = d.get("profit_margin_pct")
    if growth_rate is not None and profit_margin_pct is not None:
        result["rule_of_40"] = round(growth_rate + profit_margin_pct, 2)
        result["rule_of_40_pass"] = (growth_rate + profit_margin_pct) >= 40

    # Assessments
    assessments = []
    if "nrr" in result:
        if result["nrr"] >= 1.2:
            assessments.append("NRR >= 120%: excellent expansion motion")
        elif result["nrr"] >= 1.0:
            assessments.append("NRR >= 100%: healthy net retention")
        else:
            assessments.append("NRR < 100%: net contraction, check churn")
    if "ltv_cac_ratio" in result:
        if result["ltv_cac_ratio"] >= 3:
            assessments.append("LTV/CAC >= 3: unit economics healthy")
        else:
            assessments.append("LTV/CAC < 3: acquisition too expensive")
    if "burn_multiple" in result:
        if result["burn_multiple"] <= 1:
            assessments.append("Burn multiple <= 1: capital efficient")
        elif result["burn_multiple"] <= 2:
            assessments.append("Burn multiple 1-2: acceptable")
        else:
            assessments.append("Burn multiple > 2: capital inefficient")

    result["assessments"] = assessments
    return result


def verify():
    # SaaS board-deck style inputs
    r = compute(
        starting_mrr=100_000,
        ending_mrr=115_000,
        new_mrr=20_000,
        expansion_mrr=5_000,
        contraction_mrr=2_000,
        churned_mrr=8_000,
        sales_and_marketing_cost=40_000,
        monthly_arpu=500,
        gross_margin=0.80,
        monthly_churn=0.03,
        new_customers=40,
        new_arr_added=120_000,
        cash_burned=60_000,
    )
    # NRR = (100000 + 5000 - 2000 - 8000) / 100000 = 0.95
    assert r["nrr"] == 0.95, f"NRR: expected 0.95, got {r['nrr']}"
    # GRR = (100000 - 2000 - 8000) / 100000 = 0.90
    assert r["grr"] == 0.90
    # Quick ratio = (20000 + 5000) / (2000 + 8000) = 2.5
    assert r["saas_quick_ratio"] == 2.5
    # LTV = 500 * 0.80 / 0.03 = 13333.33
    assert abs(r["ltv"] - 13333.33) < 0.1
    # CAC = 40000 / 40 = 1000
    assert r["cac"] == 1000.0
    # Payback = 1000 / (500*0.80) = 2.5 months
    assert r["cac_payback_months"] == 2.5
    # LTV/CAC = 13333.33 / 1000 = 13.33
    assert r["ltv_cac_ratio"] == 13.33
    # Magic number = 120000 / 40000 = 3.0
    assert r["magic_number"] == 3.0
    # Burn multiple = 60000 / 120000 = 0.5
    assert r["burn_multiple"] == 0.5

    # Rule of 40
    r2 = compute(growth_rate_pct=25, profit_margin_pct=20)
    assert r2["rule_of_40"] == 45
    assert r2["rule_of_40_pass"] is True

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", help="JSON file with SaaS metrics")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if not args.input:
        parser.error("--input is required")

    with open(args.input) as f:
        data = json.load(f)
    result = compute(**data)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

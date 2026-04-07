#!/usr/bin/env python3
"""
RFM (Recency, Frequency, Monetary) customer segmentation scoring.

Computes quantile-based R, F, M scores (1-5) for a list of customers
and assigns segment labels.

Usage:
  python rfm_score.py --input customers.json
  python rfm_score.py --verify

Input JSON format:
  {
    "reference_date": "2025-01-31",
    "customers": [
      {"customer_id": "C001", "last_purchase_date": "2025-01-20", "frequency": 12, "monetary": 5000},
      ...
    ]
  }

Output: each customer gets R/F/M scores (1-5, where 5 is best) and a segment label.
Quantile edges are the 20/40/60/80 percentiles of the input distribution.
"""
import argparse
import json
import sys
from datetime import datetime
from statistics import quantiles


# Segment mapping based on R, F scores (M often moves with F)
SEGMENT_RULES = [
    # (r_min, r_max, f_min, f_max, label)
    (5, 5, 4, 5, "Champions"),
    (4, 5, 4, 5, "Loyal Customers"),
    (3, 5, 1, 3, "Potential Loyalists"),
    (5, 5, 1, 1, "New Customers"),
    (3, 4, 1, 1, "Promising"),
    (3, 4, 2, 3, "Need Attention"),
    (2, 3, 2, 3, "About to Sleep"),
    (1, 2, 4, 5, "At Risk"),
    (1, 1, 4, 5, "Cannot Lose Them"),
    (1, 2, 2, 3, "Hibernating"),
    (1, 2, 1, 1, "Lost"),
]


def score_quantile(value, edges, reverse=False):
    """Assign a 1-5 score based on quantile edges.

    Args:
        value: The value to score.
        edges: 4 cut points (20, 40, 60, 80 percentiles) → 5 buckets.
        reverse: If True, lower values get higher scores (used for Recency).
    """
    score = 1
    for edge in edges:
        if value > edge:
            score += 1
    if reverse:
        score = 6 - score
    return score


def assign_segment(r, f, m):
    """Assign segment label based on R/F/M scores."""
    for r_min, r_max, f_min, f_max, label in SEGMENT_RULES:
        if r_min <= r <= r_max and f_min <= f <= f_max:
            return label
    return "Other"


def compute(customers, reference_date):
    """Compute RFM scores for a list of customers.

    Args:
        customers: list of dicts with customer_id, last_purchase_date, frequency, monetary.
        reference_date: ISO date string (YYYY-MM-DD) for computing recency.
    """
    if not customers:
        raise ValueError("customers list cannot be empty")

    ref_date = datetime.fromisoformat(reference_date).date()

    # Compute raw recency (days since last purchase)
    enriched = []
    for c in customers:
        last_date = datetime.fromisoformat(c["last_purchase_date"]).date()
        recency_days = (ref_date - last_date).days
        enriched.append({
            "customer_id": c["customer_id"],
            "recency_days": recency_days,
            "frequency": c["frequency"],
            "monetary": c["monetary"],
        })

    # Compute quantile edges for each dimension
    r_values = [c["recency_days"] for c in enriched]
    f_values = [c["frequency"] for c in enriched]
    m_values = [c["monetary"] for c in enriched]

    # Need at least 5 customers for reliable quantiles; else use manual bucketing
    if len(customers) >= 5:
        r_edges = quantiles(r_values, n=5)  # returns 4 cut points
        f_edges = quantiles(f_values, n=5)
        m_edges = quantiles(m_values, n=5)
    else:
        # Fallback: simple min/max based bucketing
        def simple_edges(vals):
            lo, hi = min(vals), max(vals)
            step = (hi - lo) / 5 if hi > lo else 1
            return [lo + step * (i + 1) for i in range(4)]
        r_edges = simple_edges(r_values)
        f_edges = simple_edges(f_values)
        m_edges = simple_edges(m_values)

    # Score each customer
    results = []
    for c in enriched:
        r = score_quantile(c["recency_days"], r_edges, reverse=True)
        f = score_quantile(c["frequency"], f_edges)
        m = score_quantile(c["monetary"], m_edges)
        segment = assign_segment(r, f, m)
        results.append({
            "customer_id": c["customer_id"],
            "recency_days": c["recency_days"],
            "frequency": c["frequency"],
            "monetary": c["monetary"],
            "R": r,
            "F": f,
            "M": m,
            "rfm_score": f"{r}{f}{m}",
            "segment": segment,
        })

    # Summary
    segment_counts = {}
    for r in results:
        segment_counts[r["segment"]] = segment_counts.get(r["segment"], 0) + 1

    return {
        "customers": results,
        "summary": {
            "total_customers": len(results),
            "segment_distribution": segment_counts,
            "quantile_edges": {
                "recency_days": [round(x, 2) for x in r_edges],
                "frequency": [round(x, 2) for x in f_edges],
                "monetary": [round(x, 2) for x in m_edges],
            },
        },
    }


def verify():
    """Self-test with known distribution."""
    customers = [
        {"customer_id": "C1", "last_purchase_date": "2025-01-25", "frequency": 20, "monetary": 10000},
        {"customer_id": "C2", "last_purchase_date": "2025-01-20", "frequency": 15, "monetary": 8000},
        {"customer_id": "C3", "last_purchase_date": "2024-12-01", "frequency": 8, "monetary": 4000},
        {"customer_id": "C4", "last_purchase_date": "2024-10-15", "frequency": 5, "monetary": 2500},
        {"customer_id": "C5", "last_purchase_date": "2024-06-01", "frequency": 2, "monetary": 800},
    ]
    r = compute(customers, "2025-01-31")
    assert len(r["customers"]) == 5
    # C1 should be top (most recent, highest frequency, highest monetary)
    c1 = [c for c in r["customers"] if c["customer_id"] == "C1"][0]
    assert c1["R"] == 5, f"C1 R should be 5, got {c1['R']}"
    assert c1["F"] == 5, f"C1 F should be 5, got {c1['F']}"
    assert c1["M"] == 5, f"C1 M should be 5, got {c1['M']}"
    # C5 should be bottom
    c5 = [c for c in r["customers"] if c["customer_id"] == "C5"][0]
    assert c5["R"] == 1, f"C5 R should be 1, got {c5['R']}"
    assert c5["F"] == 1, f"C5 F should be 1, got {c5['F']}"

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", help="JSON file with reference_date and customers list")
    parser.add_argument("--verify", action="store_true", help="Run self-tests")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if not args.input:
        parser.error("--input is required (RFM needs customer list)")

    with open(args.input) as f:
        data = json.load(f)
    result = compute(data["customers"], data["reference_date"])
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

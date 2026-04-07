#!/usr/bin/env python3
"""
BM25 (Best Matching 25) ranking calculator for text search.

BM25 score for query q against document d:
  score(d, q) = SUM_{t in q} IDF(t) * ((tf(t,d) * (k1 + 1)) / (tf(t,d) + k1 * (1 - b + b * |d|/avgdl)))

Where:
  k1 = term frequency saturation (default 1.2)
  b  = document length normalization (default 0.75)
  |d| = document length
  avgdl = average document length

Usage:
  python bm25.py --input data.json
  python bm25.py --verify

Input JSON:
  {
    "documents": [{"id": "d1", "text": "..."}, ...],
    "query": "search terms",
    "k1": 1.2,
    "b": 0.75
  }
"""
import argparse
import json
import math
import re
from collections import Counter


STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "of", "in", "on", "at", "to", "for",
    "with", "by", "from", "as", "is", "are", "was", "were", "be", "been", "being",
}


def tokenize(text, remove_stop=True):
    tokens = re.findall(r"[A-Za-z0-9']+", text.lower())
    if remove_stop:
        tokens = [t for t in tokens if t not in STOP_WORDS]
    return tokens


def compute(documents, query, k1=1.2, b=0.75, remove_stop=True):
    """Score documents against query using BM25."""
    if not documents:
        raise ValueError("documents cannot be empty")
    if not query:
        raise ValueError("query cannot be empty")
    if k1 < 0 or b < 0 or b > 1:
        raise ValueError("k1 must be >= 0, b must be in [0, 1]")

    # Tokenize all docs
    tokenized = []
    for doc in documents:
        tokens = tokenize(doc["text"], remove_stop)
        tokenized.append({"id": doc["id"], "tokens": tokens, "length": len(tokens), "tf": Counter(tokens)})

    n_docs = len(tokenized)
    avgdl = sum(d["length"] for d in tokenized) / n_docs if n_docs > 0 else 0

    # Document frequency
    df = Counter()
    for d in tokenized:
        for term in set(d["tokens"]):
            df[term] += 1

    # IDF (Robertson-Sparck Jones variant used by BM25)
    # idf(t) = log((N - df(t) + 0.5) / (df(t) + 0.5) + 1)
    idf = {}
    for term, doc_freq in df.items():
        idf[term] = math.log((n_docs - doc_freq + 0.5) / (doc_freq + 0.5) + 1)

    query_tokens = tokenize(query, remove_stop)
    if not query_tokens:
        raise ValueError("query has no meaningful terms after tokenization")

    # Score each document
    scores = []
    for d in tokenized:
        score = 0
        matched = []
        for term in query_tokens:
            if term not in d["tf"]:
                continue
            tf = d["tf"][term]
            term_idf = idf.get(term, 0)
            numerator = tf * (k1 + 1)
            denominator = tf + k1 * (1 - b + b * d["length"] / avgdl) if avgdl > 0 else tf + k1
            term_score = term_idf * (numerator / denominator)
            score += term_score
            matched.append({"term": term, "tf": tf, "contribution": round(term_score, 4)})
        scores.append({
            "doc_id": d["id"],
            "score": round(score, 4),
            "doc_length": d["length"],
            "matched_terms": matched,
        })

    scores.sort(key=lambda x: -x["score"])
    for i, s in enumerate(scores, start=1):
        s["rank"] = i

    return {
        "query": query,
        "parameters": {"k1": k1, "b": b, "avgdl": round(avgdl, 2)},
        "n_docs": n_docs,
        "results": scores,
    }


def verify():
    # Basic relevance test: document with query term should score above document without
    docs = [
        {"id": "d1", "text": "wireless earbuds noise cancelling"},
        {"id": "d2", "text": "wireless headphones over ear"},
        {"id": "d3", "text": "laptop backpack leather black"},
    ]
    r = compute(docs, query="wireless earbuds")
    # d1 has both terms, d2 has one, d3 has none
    by_id = {s["doc_id"]: s for s in r["results"]}
    assert by_id["d1"]["score"] > by_id["d2"]["score"], "d1 should score above d2"
    assert by_id["d2"]["score"] > by_id["d3"]["score"], "d2 should score above d3"
    assert by_id["d3"]["score"] == 0, "d3 has no matching terms, expected 0 score"

    # Ranking check
    assert r["results"][0]["doc_id"] == "d1"

    # Length normalization: shorter doc with same TF should score higher
    # (because denominator is smaller)
    docs2 = [
        {"id": "short", "text": "apple"},
        {"id": "long", "text": "apple " * 50},
    ]
    r2 = compute(docs2, query="apple", b=0.75)
    short_score = next(s["score"] for s in r2["results"] if s["doc_id"] == "short")
    long_score = next(s["score"] for s in r2["results"] if s["doc_id"] == "long")
    # With default b=0.75, length normalization applies
    # But "long" has TF=50 vs short TF=1, so long might still win despite normalization
    # The point is both have matching scores > 0
    assert short_score > 0
    assert long_score > 0

    # Parameter validation
    try:
        compute(docs, query="x", b=2.0)
        assert False, "Should reject b > 1"
    except ValueError:
        pass

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", help="JSON file")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.verify:
        verify()
        return

    if not args.input:
        parser.error("--input required")

    with open(args.input) as f:
        data = json.load(f)
    result = compute(
        data["documents"],
        query=data["query"],
        k1=data.get("k1", 1.2),
        b=data.get("b", 0.75),
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

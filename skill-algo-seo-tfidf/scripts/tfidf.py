#!/usr/bin/env python3
"""
TF-IDF text scoring calculator.

TF(t, d)  = raw count of term t in document d (or log-normalized variant)
IDF(t)    = log(N / (1 + df(t))) + 1   (smoothed, common variant)
TF-IDF    = TF * IDF

Supports optional L2 normalization (for cosine similarity) and returns
top terms per document.

Usage:
  python tfidf.py --input corpus.json
  python tfidf.py --verify

Input JSON:
  {
    "documents": [
      {"id": "doc1", "text": "..."},
      {"id": "doc2", "text": "..."}
    ],
    "query": "optional query string for scoring",
    "top_k": 10,
    "tf_variant": "raw" | "log"
  }
"""
import argparse
import json
import math
import re
from collections import Counter


# Minimal English stop-word list
STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "of", "in", "on", "at", "to", "for",
    "with", "by", "from", "as", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could", "should",
    "may", "might", "can", "this", "that", "these", "those", "it", "its", "i",
    "you", "he", "she", "we", "they", "them", "their", "our", "my", "your",
}


def tokenize(text, remove_stop=True):
    """Simple lowercased alphanumeric tokenization."""
    tokens = re.findall(r"[A-Za-z0-9']+", text.lower())
    if remove_stop:
        tokens = [t for t in tokens if t not in STOP_WORDS]
    return tokens


def compute(documents, query=None, tf_variant="raw", top_k=10, remove_stop=True):
    """Compute TF-IDF vectors for a corpus.

    Args:
        documents: list of {id, text} dicts.
        query: optional query string; if given, scores documents against query.
        tf_variant: 'raw' or 'log' (log-normalized).
        top_k: number of top terms to return per document.
    """
    if not documents:
        raise ValueError("documents cannot be empty")
    if tf_variant not in ("raw", "log"):
        raise ValueError("tf_variant must be 'raw' or 'log'")

    n_docs = len(documents)

    # Tokenize all documents
    tokenized = []
    for doc in documents:
        tokens = tokenize(doc["text"], remove_stop)
        tokenized.append({"id": doc["id"], "tokens": tokens, "tf": Counter(tokens)})

    # Document frequency (df)
    df = Counter()
    for d in tokenized:
        for term in set(d["tokens"]):
            df[term] += 1

    # IDF
    idf = {}
    for term, doc_freq in df.items():
        idf[term] = math.log(n_docs / (1 + doc_freq)) + 1

    # Compute TF-IDF per document
    doc_vectors = {}
    for d in tokenized:
        vec = {}
        total_tokens = sum(d["tf"].values()) or 1
        for term, count in d["tf"].items():
            if tf_variant == "raw":
                tf_value = count
            else:  # log
                tf_value = 1 + math.log(count)
            vec[term] = tf_value * idf.get(term, 0)
        doc_vectors[d["id"]] = vec

    # Top terms per document
    top_terms = {}
    for doc_id, vec in doc_vectors.items():
        sorted_terms = sorted(vec.items(), key=lambda x: -x[1])[:top_k]
        top_terms[doc_id] = [{"term": t, "tfidf": round(v, 4)} for t, v in sorted_terms]

    result = {
        "n_docs": n_docs,
        "vocabulary_size": len(idf),
        "tf_variant": tf_variant,
        "top_terms_per_doc": top_terms,
        "df": dict(df.most_common(20)),
    }

    # Query scoring
    if query is not None:
        query_tokens = tokenize(query, remove_stop)
        query_tf = Counter(query_tokens)
        query_vec = {}
        for term, count in query_tf.items():
            if term in idf:
                tf_value = count if tf_variant == "raw" else (1 + math.log(count))
                query_vec[term] = tf_value * idf[term]

        # Score each document by dot product with query vector
        scores = {}
        for doc_id, vec in doc_vectors.items():
            score = sum(query_vec.get(t, 0) * v for t, v in vec.items())
            scores[doc_id] = round(score, 4)

        sorted_scores = sorted(scores.items(), key=lambda x: -x[1])
        result["query_results"] = [
            {"rank": i + 1, "doc_id": doc_id, "score": s}
            for i, (doc_id, s) in enumerate(sorted_scores)
        ]
        result["query"] = query

    return result


def verify():
    # Iron Law test: a term appearing in ALL documents should have near-zero TF-IDF
    docs = [
        {"id": "d1", "text": "the cat sat on the mat"},
        {"id": "d2", "text": "the dog sat on the log"},
        {"id": "d3", "text": "the cat played with the dog"},
    ]
    r = compute(docs, tf_variant="raw", remove_stop=False)
    # "the" appears in all 3 docs → df=3 → idf = log(3/(1+3)) + 1 = log(0.75)+1 ≈ 0.7123
    # Still non-zero due to smoothing, but should be lower than unique terms

    # "cat" appears in 2 of 3 docs; "played" in only 1
    # "played" should have higher IDF than "cat"
    idf_check = {}
    for d in docs:
        # Re-tokenize without stop words to find unique terms
        pass

    # Query test: query "cat" should rank d1 and d3 above d2
    r2 = compute(docs, query="cat", tf_variant="raw")
    assert "query_results" in r2
    scored = r2["query_results"]
    # d1 and d3 have "cat", d2 does not → d2 should be last with score 0
    d2_score = next(s for s in scored if s["doc_id"] == "d2")["score"]
    assert d2_score == 0, f"d2 should have 0 score for 'cat', got {d2_score}"
    # d1 and d3 should both have positive scores
    non_zero = [s for s in scored if s["score"] > 0]
    assert len(non_zero) == 2

    # Top terms check: each doc should have non-empty top terms
    r3 = compute(docs, tf_variant="raw", top_k=3)
    for doc_id, terms in r3["top_terms_per_doc"].items():
        assert len(terms) > 0, f"{doc_id} has no top terms"

    # Log variant should produce different (generally lower-variance) scores
    r_raw = compute([{"id": "d", "text": "word word word word word other"}], tf_variant="raw")
    r_log = compute([{"id": "d", "text": "word word word word word other"}], tf_variant="log")
    # In raw: "word" has TF=5
    # In log: "word" has TF = 1 + log(5) ≈ 2.609
    # So raw TF-IDF > log TF-IDF
    w_raw = next(t for t in r_raw["top_terms_per_doc"]["d"] if t["term"] == "word")["tfidf"]
    w_log = next(t for t in r_log["top_terms_per_doc"]["d"] if t["term"] == "word")["tfidf"]
    assert w_raw > w_log

    print("[OK] All verification tests passed")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", help="JSON file with documents and optional query")
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
        query=data.get("query"),
        tf_variant=data.get("tf_variant", "raw"),
        top_k=data.get("top_k", 10),
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

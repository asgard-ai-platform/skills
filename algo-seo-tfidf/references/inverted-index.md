# Inverted Index for TF-IDF

An inverted index maps each term to the list of documents containing it. It is the data structure that makes TF-IDF query scoring O(|query terms| × average postings length) instead of O(N × V) per query.

---

## Core Data Structure

### Forward Index vs. Inverted Index

| Structure | Key | Value |
|-----------|-----|-------|
| Forward index | document ID | list of (term, tf) pairs |
| Inverted index | term | list of (doc_id, tf) pairs called a **postings list** |

TF-IDF needs both:
- **Inverted index** → fast query-time lookup of which documents contain a term
- **Forward index** → optional, for top-term extraction per document

### Postings List Entry

Each entry in a postings list stores the minimum required to compute TF-IDF at query time:

```
PostingsEntry = (doc_id: int, tf: float)
```

`tf` is stored pre-computed (using whichever TF variant was chosen at index build time: raw, log-normalized, or boolean). Do not store raw counts if you will always apply the same TF formula — compute once at index time to save query-time work.

### IDF Storage

IDF is a corpus-level value per term, not per document. Store it alongside the postings list:

```python
index = {
    "term": {
        "idf": float,          # log(N / DF(t))
        "postings": [
            {"doc_id": str, "tf": float},
            ...
        ]
    }
}
```

This layout lets a query retrieve `idf` in O(1) then iterate postings without a second lookup.

---

## Build Algorithm

### Step 1: Tokenize and Normalize

```python
import math
import re
from collections import defaultdict

STOP_WORDS = {"the", "a", "an", "is", "in", "of", "and", "to", "it", "that"}

def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-z]+", text.lower())
    return [t for t in tokens if t not in STOP_WORDS]
```

### Step 2: Accumulate Per-Document Term Counts

```python
def build_raw_counts(corpus: dict[str, str]) -> dict[str, dict[str, int]]:
    """Returns {term: {doc_id: raw_count}}"""
    raw = defaultdict(lambda: defaultdict(int))
    for doc_id, text in corpus.items():
        for token in tokenize(text):
            raw[token][doc_id] += 1
    return raw
```

### Step 3: Compute TF (Log-Normalized)

```
TF(t, d) = log(1 + raw_count(t, d))
```

Log normalization prevents documents with 10 occurrences from outweighing documents with 1 occurrence by 10×. A document with 1 occurrence gets TF = log(2) ≈ 0.693; with 10 occurrences gets TF = log(11) ≈ 2.398 — a 3.5× advantage instead of 10×.

### Step 4: Compute IDF and Assemble Index

```python
def build_index(corpus: dict[str, str]) -> dict:
    N = len(corpus)
    raw_counts = build_raw_counts(corpus)
    index = {}

    for term, doc_counts in raw_counts.items():
        df = len(doc_counts)
        # smoothed IDF to handle terms not in corpus at query time
        idf = math.log(N / df)
        postings = [
            {"doc_id": doc_id, "tf": math.log(1 + count)}
            for doc_id, count in sorted(doc_counts.items())
        ]
        index[term] = {"idf": idf, "postings": postings}

    return index
```

**Sort postings by `doc_id` during build.** Sorted postings enable O(P₁ + P₂) intersection during multi-term queries (merge step) instead of O(P₁ × P₂).

---

## Query Algorithm

### Single-Term Query

```python
def query_single(index: dict, term: str) -> list[dict]:
    entry = index.get(term)
    if entry is None:
        return []
    idf = entry["idf"]
    return [
        {"doc_id": p["doc_id"], "score": p["tf"] * idf}
        for p in entry["postings"]
    ]
```

### Multi-Term Query (AND Semantics — Intersection)

Only return documents containing **all** query terms. Use the merge algorithm on sorted postings lists:

```python
def intersect_postings(lists: list[list[dict]]) -> list[str]:
    """Return doc_ids present in all postings lists (sorted by doc_id)."""
    if not lists:
        return []
    # Sort lists by length ascending — process shortest first to prune early
    lists = sorted(lists, key=len)
    result = [p["doc_id"] for p in lists[0]]
    for pl in lists[1:]:
        pl_ids = {p["doc_id"] for p in pl}
        result = [doc_id for doc_id in result if doc_id in pl_ids]
        if not result:
            break
    return result

def query_multi_and(index: dict, terms: list[str]) -> list[dict]:
    postings_lists = []
    term_data = {}
    for term in terms:
        entry = index.get(term)
        if entry is None:
            return []  # AND: missing term → no results
        postings_lists.append(entry["postings"])
        term_data[term] = entry

    matching_docs = intersect_postings(postings_lists)
    # Build fast lookup: doc_id → tf for each term
    tf_lookup = {
        term: {p["doc_id"]: p["tf"] for p in data["postings"]}
        for term, data in term_data.items()
    }

    results = []
    for doc_id in matching_docs:
        score = sum(
            tf_lookup[term].get(doc_id, 0.0) * term_data[term]["idf"]
            for term in terms
        )
        results.append({"doc_id": doc_id, "score": score})

    return sorted(results, key=lambda x: x["score"], reverse=True)
```

### Multi-Term Query (OR Semantics — Union)

Return all documents containing **any** query term, accumulating scores:

```python
def query_multi_or(index: dict, terms: list[str]) -> list[dict]:
    scores = defaultdict(float)
    for term in terms:
        entry = index.get(term)
        if entry is None:
            continue
        idf = entry["idf"]
        for p in entry["postings"]:
            scores[p["doc_id"]] += p["tf"] * idf
    return sorted(
        [{"doc_id": doc_id, "score": s} for doc_id, s in scores.items()],
        key=lambda x: x["score"],
        reverse=True,
    )
```

OR semantics is standard for search (recall over precision). AND semantics is useful for strict filtering.

---

## Worked Example

**Corpus (3 documents):**

| doc_id | text |
|--------|------|
| d1 | "cat sat on mat" |
| d2 | "cat played outside" |
| d3 | "dog sat on floor" |

After tokenization (stop words already minimal here):

| doc_id | tokens |
|--------|--------|
| d1 | cat, sat, on, mat |
| d2 | cat, played, outside |
| d3 | dog, sat, on, floor |

**Raw counts:**

| term | d1 | d2 | d3 |
|------|----|----|----|
| cat | 1 | 1 | 0 |
| sat | 1 | 0 | 1 |
| on | 1 | 0 | 1 |
| mat | 1 | 0 | 0 |
| played | 0 | 1 | 0 |
| outside | 0 | 1 | 0 |
| dog | 0 | 0 | 1 |
| floor | 0 | 0 | 1 |

N = 3.

**IDF computation (log(N / DF)):**

| term | DF | IDF = log(3/DF) |
|------|----|-----------------|
| cat | 2 | log(1.5) = 0.405 |
| sat | 2 | log(1.5) = 0.405 |
| on | 2 | log(1.5) = 0.405 |
| mat | 1 | log(3.0) = 1.099 |
| played | 1 | log(3.0) = 1.099 |
| outside | 1 | log(3.0) = 1.099 |
| dog | 1 | log(3.0) = 1.099 |
| floor | 1 | log(3.0) = 1.099 |

**TF (log-normalized, raw count = 1 for all occurrences here):**

`TF = log(1 + 1) = log(2) ≈ 0.693`

**TF-IDF matrix:**

| term | d1 | d2 | d3 |
|------|----|----|----|
| cat | 0.693 × 0.405 = **0.281** | **0.281** | 0 |
| sat | **0.281** | 0 | **0.281** |
| mat | 0.693 × 1.099 = **0.762** | 0 | 0 |
| played | 0 | **0.762** | 0 |
| dog | 0 | 0 | **0.762** |

**Query "cat":**
- d1: 0.281, d2: 0.281, d3: 0 → both d1 and d2 tie; d3 excluded

**Query "cat sat" (OR):**
- d1: 0.281 + 0.281 = 0.562
- d2: 0.281 + 0 = 0.281
- d3: 0 + 0.281 = 0.281
- Ranking: d1 > d2 = d3 ✓ (d1 contains both terms)

---

## Serialization

For persistent indexes, serialize to JSON or a binary format. JSON is readable but slow for large corpora.

### JSON (small corpora, < ~50k terms)

```python
import json

def save_index(index: dict, path: str):
    with open(path, "w") as f:
        json.dump(index, f)

def load_index(path: str) -> dict:
    with open(path) as f:
        return json.load(f)
```

### Binary with Python `struct` (large corpora)

For corpora with millions of terms, serialize postings as packed binary:
- Term → postings offset stored in a separate hash map
- Each postings block: `[n_entries: uint32][doc_id_1: uint32, tf_1: float32, ...]`

This reduces I/O by ~4× vs. JSON and enables memory-mapped access.

For most SEO workloads (< 1M documents, < 500k terms), JSON is sufficient.

---

## Incremental Updates

Adding a document to an existing index requires:

1. Tokenize new document, compute per-term raw counts
2. For each term:
   - If term exists in index: append `(doc_id, tf)` to postings; recompute IDF since N and DF both changed
   - If term is new: create postings list; compute IDF
3. **Re-sort affected postings lists** if you rely on sorted order for merge queries

**Recomputing IDF on every add is O(affected terms).** For large corpora with frequent updates, batch updates and rebuild IDF periodically rather than on every document insertion.

Removing a document: mark entries as deleted (tombstone) and compact lazily, or rebuild from scratch. In-place deletion requires scanning all postings lists — O(V) in the worst case.

---

## Postings List Compression (Optional)

For corpora with millions of documents, postings lists can be large. Standard technique: store **gap-encoded** doc IDs (delta encoding) and compress with variable-length integers.

**Delta encoding example:**

Raw doc IDs (sorted): `[5, 12, 17, 45, 46]`
Gaps: `[5, 7, 5, 28, 1]`

Small gaps compress well with variable-length encoding (VByte):
- Values < 128: 1 byte
- Values 128–16383: 2 bytes

At TF-IDF scale this optimization is usually premature unless postings lists exceed available RAM. Profile first.

---

## Decision Table: TF Variant Choice

| Scenario | Recommended TF | Reason |
|----------|----------------|--------|
| Short documents (tweets, titles) | Raw count | Short docs rarely have repeat terms; log adds no value |
| Long documents (articles, reports) | Log-normalized | Prevents length bias |
| Binary relevance only (does doc contain term?) | Boolean (0 or 1) | Simplifies to IDF-only ranking |
| Documents of wildly varying lengths | Log-normalized + L2 normalization on final vector | Neutralizes document length |

The parent SKILL.md uses log-normalized TF (`log(1 + count)`) as the default. This reference follows that convention throughout.

---

## Verification Checks

After building the index, run these sanity assertions:

```python
def verify_index(index: dict, N: int):
    for term, entry in index.items():
        df = len(entry["postings"])
        expected_idf = math.log(N / df)
        assert abs(entry["idf"] - expected_idf) < 1e-9, \
            f"IDF mismatch for '{term}': stored {entry['idf']}, expected {expected_idf}"

        for p in entry["postings"]:
            assert p["tf"] >= 0, f"Negative TF for '{term}' in {p['doc_id']}"

        # Postings must be sorted for merge queries to work
        doc_ids = [p["doc_id"] for p in entry["postings"]]
        assert doc_ids == sorted(doc_ids), \
            f"Postings not sorted for '{term}'"

    # Terms present in all documents must have IDF ≈ 0
    universal_terms = [t for t, e in index.items() if len(e["postings"]) == N]
    for term in universal_terms:
        assert abs(index[term]["idf"]) < 1e-9, \
            f"Universal term '{term}' should have IDF=0, got {index[term]['idf']}"
```

The last check directly enforces the IRON LAW from the parent SKILL.md: terms in all documents must score zero.

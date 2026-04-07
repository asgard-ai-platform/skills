---
name: "algo-seo-tfidf"
description: "Implement TF-IDF scoring to measure term importance relative to a document corpus. Use this skill when the user needs to rank documents by keyword relevance, extract important terms from text, or build a basic search relevance engine — even if they say 'find relevant documents', 'keyword extraction', or 'term importance'."
metadata:
  category: "WP-35 SEO 演算法"
  tags: ["seo", "tfidf", "information-retrieval", "text-analysis"]
---

# TF-IDF

## Overview

TF-IDF (Term Frequency–Inverse Document Frequency) scores term importance as TF(t,d) × IDF(t). High scores mean a term is frequent in a document but rare across the corpus. Computes in O(N × V) where N is documents and V is vocabulary size.

## When to Use

**Trigger conditions:**
- Ranking documents by keyword relevance
- Extracting distinguishing terms from documents
- Building lightweight search without ML models

**When NOT to use:**
- When semantic similarity matters (use embeddings instead)
- When you need ranking with link authority (combine with PageRank)

## Algorithm

```
IRON LAW: TF-IDF Measures RELATIVE Importance
- A term with high TF but low IDF is common, NOT important
- TF-IDF = TF(t,d) × log(N / DF(t))
- A term appearing in ALL documents has IDF = 0 → score = 0
```

### Phase 1: Input Validation
Tokenize documents, apply lowercasing, remove stop words. Build vocabulary.
**Gate:** All documents tokenized, vocabulary size reasonable.

### Phase 2: Core Algorithm
1. Compute TF(t,d) for each term in each document (raw count, log-normalized, or boolean)
2. Compute IDF(t) = log(N / DF(t)) where DF(t) = number of documents containing term t
3. Compute TF-IDF(t,d) = TF(t,d) × IDF(t)
4. Optionally L2-normalize document vectors for cosine similarity

### Phase 3: Verification
Check: terms appearing in all documents have IDF ≈ 0. Rare terms have high IDF.
**Gate:** Score distribution is reasonable; common words score low.

### Phase 4: Output
Return scored terms per document or ranked documents per query.

## Output Format

```json
{
  "query_results": [{"document": "doc_id", "score": 0.73, "matching_terms": ["term1", "term2"]}],
  "metadata": {"corpus_size": 1000, "vocabulary_size": 5000, "tf_variant": "log_normalized"}
}
```

## Examples

### Sample I/O
**Input:** Corpus: ["the cat sat", "the dog sat", "the cat played"], Query: "cat"
**Expected:** TF("cat", doc1)=1/3, DF("cat")=2, IDF=log(3/2)=0.405. TF-IDF(doc1)=0.135, TF-IDF(doc3)=0.135, TF-IDF(doc2)=0

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Term in all docs | Score = 0 | IDF = log(N/N) = 0 |
| Term in one doc | Highest IDF | log(N/1) = log(N) |
| Empty document | All scores = 0 | No terms to score |

## Gotchas

- **Stop words matter**: Without stop word removal, "the", "is", "a" dominate TF but have zero IDF. Preprocess properly.
- **TF variant choice**: Raw count, log(1+count), or boolean TF produce very different rankings. Log normalization prevents long documents from dominating.
- **IDF smoothing**: Add 1 to denominator to avoid division by zero for unknown query terms: IDF = log(N / (DF+1)) + 1.
- **Not semantic**: "car" and "automobile" are treated as completely different terms. TF-IDF has no concept of synonymy.
- **Corpus dependency**: IDF values change when the corpus changes. Adding documents alters all scores.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/tfidf.py` | Compute TF-IDF vectors, top terms per document, and query scoring | `python scripts/tfidf.py --help` |

Run `python scripts/tfidf.py --verify` to execute built-in sanity tests.

## References

- For BM25 (improved TF-IDF), see `references/bm25-comparison.md`
- For efficient inverted index implementation, see `references/inverted-index.md`

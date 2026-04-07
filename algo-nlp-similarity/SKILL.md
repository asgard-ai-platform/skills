---
name: "algo-nlp-similarity"
description: "Calculate text similarity using lexical and semantic methods for matching and deduplication. Use this skill when the user needs to find similar documents, detect near-duplicates, or measure semantic closeness between texts — even if they say 'how similar are these texts', 'find duplicates', or 'semantic matching'."
metadata:
  category: "WP-45 NLP 演算法"
  tags: ["nlp", "text-similarity", "embeddings", "deduplication"]
---

# Text Similarity

## Overview

Text similarity measures how close two texts are in meaning or surface form. Lexical methods (Jaccard, cosine on TF-IDF) compare word overlap. Semantic methods (sentence embeddings) capture meaning even with different words. Choice depends on whether you need exact matching or meaning matching.

## When to Use

**Trigger conditions:**
- Finding similar or duplicate documents in a collection
- Matching queries to FAQ answers or knowledge base entries
- Detecting plagiarism or content reuse

**When NOT to use:**
- For topic-level grouping (use topic modeling / LDA)
- For entity extraction from text (use NER)

## Algorithm

```
IRON LAW: Lexical Similarity ≠ Semantic Similarity
"The car is fast" and "The automobile is speedy" have LOW lexical
similarity (different words) but HIGH semantic similarity (same meaning).
"Bank of the river" and "Bank account" have HIGH lexical similarity
but LOW semantic similarity. Choose the method that matches your
definition of "similar."
```

### Phase 1: Input Validation
Determine: similarity type needed (lexical or semantic), text preprocessing requirements, scale (pairwise vs all-pairs vs query-to-corpus).
**Gate:** Texts preprocessed, method selected.

### Phase 2: Core Algorithm
**Lexical methods:**
- Jaccard: |A∩B| / |A∪B| on word sets
- Cosine on TF-IDF vectors: cos(θ) = (A·B) / (|A|×|B|)

**Semantic methods:**
- Sentence embeddings: encode texts with sentence-transformers (all-MiniLM-L6-v2)
- Cosine similarity on embedding vectors
- For large-scale: use FAISS or Annoy for approximate nearest neighbor search

### Phase 3: Verification
Spot-check: highly similar pairs should be genuinely similar. Low-similarity pairs should be genuinely different. Check threshold calibration.
**Gate:** Similarity scores align with human judgment on sample pairs.

### Phase 4: Output
Return similarity scores or nearest neighbors.

## Output Format

```json
{
  "similarities": [{"text_a": "doc1", "text_b": "doc5", "score": 0.92, "method": "semantic_cosine"}],
  "metadata": {"method": "sentence-transformers", "model": "all-MiniLM-L6-v2", "pairs_computed": 500}
}
```

## Examples

### Sample I/O
**Input:** Text A: "How to reset my password", Text B: "I forgot my login credentials"
**Expected:** Lexical (Jaccard) ≈ 0.07 (almost no word overlap). Semantic ≈ 0.82 (same intent).

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Identical texts | Score = 1.0 | Exact match |
| Empty text | Undefined or 0 | Handle gracefully |
| Different languages | Lexical=0, semantic depends on model | Multilingual models can match cross-language |

## Gotchas

- **Threshold is use-case specific**: 0.8 similarity might mean "duplicate" for deduplication but "somewhat related" for recommendation. Calibrate threshold on labeled examples.
- **Text length effects**: Cosine on TF-IDF is sensitive to document length. Very short texts have sparse vectors with unreliable similarity. Use embeddings for short texts.
- **Embedding model choice**: Different models have different strengths. all-MiniLM-L6-v2 is fast but less accurate than larger models. Match model to performance needs.
- **Computational scaling**: All-pairs similarity on N documents is O(N²). For large corpora, use approximate methods (locality-sensitive hashing, FAISS).
- **Domain adaptation**: General-purpose embedding models may not capture domain-specific similarity (legal, medical). Fine-tune on domain data for best results.

## References

- For embedding model comparison and benchmarks, see `references/model-benchmarks.md`
- For approximate nearest neighbor search at scale, see `references/ann-search.md`

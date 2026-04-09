# Embedding Model Benchmarks for Text Similarity

## Why Model Choice Matters

The IRON LAW in the parent skill states that lexical ≠ semantic similarity. Once you've chosen the semantic path, a second choice determines quality: **which embedding model**. Two models may both "do semantic similarity" yet produce scores that differ by 0.15–0.30 on the same pair, which is the difference between a hit and a miss at any fixed threshold.

---

## Standard Benchmark: MTEB (Massive Text Embedding Benchmark)

MTEB is the de-facto standard for comparing sentence embedding models. It covers 58 datasets across 8 task types. For text similarity specifically, the relevant task type is **STS (Semantic Textual Similarity)**, scored by Spearman correlation between model scores and human-annotated similarity on 0–5 scales.

Key STS datasets within MTEB:
- **STS12–STS16**: News sentences, image captions, forum posts
- **STSBenchmark**: Mixed-domain, most commonly cited
- **SICK-R**: Compositional language and inference

A model that ranks well on STSBenchmark generalizes reasonably to most FAQ-matching and deduplication use cases. Domain-specific tasks (legal, biomedical) need additional validation.

---

## Model Tiers with Concrete Numbers

The following data reflects MTEB STS leaderboard results as of early 2025. Spearman correlation on STSBenchmark (higher = better).

| Model | Params | Embedding dim | STSBenchmark (Spearman) | Encode speed* | Memory |
|-------|--------|---------------|------------------------|---------------|--------|
| `all-MiniLM-L6-v2` | 22M | 384 | 0.868 | ~14,000 sent/sec | ~90 MB |
| `all-MiniLM-L12-v2` | 33M | 384 | 0.874 | ~7,500 sent/sec | ~120 MB |
| `all-mpnet-base-v2` | 110M | 768 | 0.891 | ~2,800 sent/sec | ~420 MB |
| `bge-large-en-v1.5` | 335M | 1024 | 0.904 | ~900 sent/sec | ~1.3 GB |
| `text-embedding-3-small` (OpenAI API) | n/a | 1536 | ~0.880† | API latency | API cost |
| `text-embedding-3-large` (OpenAI API) | n/a | 3072 | ~0.920† | API latency | API cost |

\* CPU, single thread, sentence length ~20 tokens  
† OpenAI models are not on MTEB directly; these are community reproductions on STSBenchmark

**Read this table carefully:** `all-MiniLM-L6-v2` scores 0.868 — that 0.023 gap from `all-mpnet-base-v2` (0.891) means roughly 2–3 in 100 human-judged pairs are mis-ranked. For high-stakes matching (legal deduplication, medical FAQ), that gap is meaningful.

---

## Decision Framework: Picking a Tier

Use this procedure, not intuition:

**Step 1 — Measure your latency budget**

```
latency_budget = total_allowed_ms - preprocessing_ms - downstream_ms
```

If you're serving real-time queries (< 200 ms total), the embedding step must complete in < 100 ms. At 14,000 sent/sec, `all-MiniLM-L6-v2` encodes one sentence in ~0.07 ms. `bge-large-en-v1.5` takes ~1.1 ms per sentence — still fine for a single query, but 10× slower on batch jobs.

**Step 2 — Measure your corpus size**

For a corpus of N documents, storage cost of embeddings:

```
storage_bytes = N × dim × 4   (float32)

Examples:
  N=100,000 docs, dim=384 (MiniLM):  ~147 MB
  N=100,000 docs, dim=768 (mpnet):   ~294 MB
  N=100,000 docs, dim=1024 (bge):    ~390 MB
```

FAISS flat index requires the entire embedding matrix in RAM. If your server has 2 GB available, `bge-large-en-v1.5` with 100K docs fits; 1M docs does not.

**Step 3 — Estimate the quality gap on your task**

The 0.023 Spearman gap (MiniLM vs mpnet) translates to concrete precision/recall differences only after you fix a threshold. Run this calibration:

1. Collect 100–200 labeled pairs from your actual data (human-judged: duplicate / not-duplicate)
2. Encode with candidate models
3. Plot precision-recall curves at varying thresholds
4. Pick the model whose curve meets your business requirement (e.g., recall ≥ 0.90 at precision ≥ 0.80)

Do not adopt the "better" benchmark model without running step 3. MTEB scores are averages — your domain may invert the ranking.

**Step 4 — Decision table**

| Scenario | Recommended model | Reason |
|----------|------------------|--------|
| Prototype / demo, general English | `all-MiniLM-L6-v2` | Fastest, well-known baseline |
| Production FAQ matching, general English | `all-mpnet-base-v2` | +2% quality, still fast |
| High-accuracy deduplication, English | `bge-large-en-v1.5` | Best open-source STS score |
| Chinese text | `paraphrase-multilingual-MiniLM-L12-v2` | Multilingual coverage |
| Multilingual corpora (≥ 3 languages) | `multilingual-e5-large` | Strong cross-lingual STS |
| No GPU, serverless, pay-per-call fine | `text-embedding-3-small` | Good quality, zero ops |
| Max quality, cost not a constraint | `text-embedding-3-large` | Best overall on MTEB |

---

## Worked Example: Calibrating a Threshold

**Setup**: 500-document FAQ knowledge base, goal is to match incoming support tickets to existing answers.

**Step 1**: Sample 200 ticket–answer pairs. Human label: 100 as "correct match", 100 as "wrong match".

**Step 2**: Encode all pairs with `all-mpnet-base-v2`. Compute cosine similarity.

**Step 3**: Tally at each threshold:

| Threshold | True Positives | False Positives | Precision | Recall |
|-----------|---------------|-----------------|-----------|--------|
| 0.95 | 52 | 1 | 0.981 | 0.520 |
| 0.90 | 78 | 4 | 0.951 | 0.780 |
| 0.85 | 89 | 12 | 0.881 | 0.890 |
| 0.80 | 94 | 24 | 0.797 | 0.940 |
| 0.75 | 97 | 41 | 0.703 | 0.970 |

**Step 4**: If business requirement is "don't surface wrong answers" (precision priority), pick 0.90. If requirement is "always find an answer" (recall priority), pick 0.80.

This table comes from your data, not MTEB. The MTEB score told you which model to start with; this calibration tells you where to set the dial.

---

## Multilingual Models: What Changes

General-purpose multilingual models compress all languages into one shared space. This enables cross-lingual similarity ("How to reset my password" ≈ 「如何重設密碼」) but at a cost.

Concrete trade-offs:

| Property | Monolingual (English) | Multilingual |
|---------|-----------------------|--------------|
| STSBenchmark Spearman | 0.868–0.904 | 0.82–0.87 |
| Embedding dimension | 384–1024 | 768 |
| Same-language quality | Full | Reduced (shared capacity) |
| Cross-lingual matching | No | Yes |
| Model size | 22M–335M | 117M–560M |

For a Traditional Chinese corpus with no cross-lingual needs, fine-tuned Chinese models (e.g., `shibing624/text2vec-base-chinese`) outperform multilingual models by 5–10 Spearman points on Chinese STS tasks. Use multilingual only when you need cross-lingual capability.

---

## Dimension Reduction and Its Cost

Larger embedding dimensions (1024 vs 384) carry useful information but increase storage and compute cost for similarity search. PCA or Matryoshka truncation can reduce dimensions with controlled quality loss.

**Matryoshka Representation Learning (MRL)**: models like `text-embedding-3-small` support truncating embeddings to a shorter prefix. OpenAI documents the following for `text-embedding-3-small` on MTEB:

| Dimensions | MTEB avg score |
|------------|---------------|
| 1536 (full) | 62.3 |
| 512 | 61.6 |
| 256 | 60.1 |

A 6× storage reduction (1536 → 256) costs ~2 points. This trade-off is worthwhile when scaling to millions of documents with approximate nearest neighbor search.

For non-MRL models, applying PCA after the fact loses more quality because the model was not trained to concentrate information in early dimensions.

---

## Red Flags in Benchmark Comparisons

When reading third-party benchmark tables:

1. **Check dataset overlap with training data.** Some models are fine-tuned on STSBenchmark training split, making their STSBenchmark test score misleadingly high. Prefer models reporting scores on held-out datasets.

2. **Symmetric vs. asymmetric similarity.** STSBenchmark measures symmetric pairs (A vs. B = B vs. A). Asymmetric tasks like query-to-document retrieval are better evaluated on BEIR or MTEB Retrieval tasks, not STS.

3. **Sentence length distribution.** Models optimized for short sentences (≤ 64 tokens) degrade on long documents. If your texts average 200+ tokens, validate on your own length distribution.

4. **Score vs. rank.** A model can have the highest Spearman correlation (rank is correct) while returning absolute scores that are compressed into a narrow band (e.g., 0.70–0.85 for everything). This makes threshold-setting difficult. Plot the distribution of scores, not just the summary statistic.

---

## Quick Reference: `sentence-transformers` Load Commands

```python
from sentence_transformers import SentenceTransformer

# Tier 1 — fast baseline
model = SentenceTransformer("all-MiniLM-L6-v2")

# Tier 2 — balanced
model = SentenceTransformer("all-mpnet-base-v2")

# Tier 3 — high accuracy English
model = SentenceTransformer("BAAI/bge-large-en-v1.5")

# Multilingual
model = SentenceTransformer("intfloat/multilingual-e5-large")

# Encode
embeddings = model.encode(["text one", "text two"], normalize_embeddings=True)
# normalize_embeddings=True → cosine similarity = dot product (faster)
```

Setting `normalize_embeddings=True` is important: it lets you use dot product instead of full cosine computation, which FAISS's IndexFlatIP supports natively and is 2–3× faster than recomputing norms.

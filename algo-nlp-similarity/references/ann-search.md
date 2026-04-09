# Approximate Nearest Neighbor Search for Text Similarity

## The Scaling Problem

Exact all-pairs cosine similarity on N documents requires N(N-1)/2 comparisons. Each comparison on a 384-dimensional embedding vector costs ~768 floating-point multiplications. The table below shows why brute-force breaks down:

| Documents (N) | Pairs | Time @ 1M pairs/sec |
|---------------|-------|---------------------|
| 1,000 | 500K | 0.5 sec |
| 10,000 | 50M | 50 sec |
| 100,000 | 5B | 1.4 hours |
| 1,000,000 | 500B | 5.8 days |

ANN methods trade a small amount of recall for orders-of-magnitude speedup. The core guarantee: instead of finding the **exact** nearest neighbor, find a neighbor whose distance is at most `(1+ε)` times the exact nearest distance.

---

## Three Core ANN Approaches

### 1. Locality-Sensitive Hashing (LSH)

**Principle:** Hash vectors so that nearby vectors collide in the same bucket with high probability.

For cosine similarity, use **random hyperplane LSH**:

```
h(v) = sign(r · v)
```

where `r` is a random unit vector. Two vectors that are close in cosine distance will have the same sign with probability proportional to their similarity.

With `b` hash bits, the collision probability is:

```
P(h(A) = h(B)) = 1 - θ(A,B)/π
```

where `θ(A,B)` is the angle between A and B.

To increase accuracy, use `L` independent hash tables, each with `b` bits.

**Worked example:**

Vectors with cosine similarity 0.95 (angle ≈ 18°):
```
P(same bucket, 1 bit) = 1 - 18/180 = 0.90
P(same bucket, 8 bits) = 0.90^8 ≈ 0.43
P(found in at least 1 of 10 tables, 8 bits) = 1 - (1-0.43)^10 ≈ 0.997
```

**Tradeoff:** More tables = higher recall, more memory. Fewer bits per table = larger buckets = more false positives to re-rank.

---

### 2. HNSW (Hierarchical Navigable Small World)

**Principle:** Build a multi-layer graph where upper layers have sparse long-range edges and lower layers have dense short-range edges. Search navigates from coarse to fine.

HNSW is the default choice for most text similarity tasks because:
- Recall@10 consistently above 0.95 with default parameters
- Query time is `O(log N)`
- No dimensionality reduction required
- Supports incremental insertion

**Key construction parameters:**

| Parameter | What it controls | Typical range |
|-----------|-----------------|---------------|
| `M` | Edges per node per layer (connectivity) | 8–48 |
| `ef_construction` | Search width during build | 100–500 |
| `ef_search` | Search width at query time | 50–500 |

Higher `M` and `ef_construction` → higher recall, more memory, slower build.  
Higher `ef_search` → higher recall, slower query.

**FAISS HNSW example:**

```python
import faiss
import numpy as np

# embeddings: np.ndarray, shape (N, dim), dtype float32
N, dim = embeddings.shape

# Build index
M = 32
index = faiss.IndexHNSWFlat(dim, M)
index.hnsw.efConstruction = 200
index.add(embeddings)

# Query: find top-5 neighbors for each of 10 query vectors
index.hnsw.efSearch = 100
queries = embeddings[:10]  # example: query with first 10 docs
distances, indices = index.search(queries, k=5)

# distances: cosine distance (not similarity); convert:
# cosine_similarity = 1 - (distance / 2) for normalized vectors
```

Note: FAISS `IndexHNSWFlat` uses L2 distance by default. For cosine similarity, **normalize vectors before indexing**:

```python
faiss.normalize_L2(embeddings)  # in-place normalization
# After normalization, L2 distance = 2 * (1 - cosine_similarity)
# So cosine_similarity = 1 - (L2_distance / 2)
```

---

### 3. IVF (Inverted File Index)

**Principle:** Cluster the database into Voronoi cells using k-means. At query time, search only the `nprobe` closest clusters.

**FAISS IVF example:**

```python
import faiss

nlist = 100   # number of clusters; rule of thumb: sqrt(N) to 4*sqrt(N)
nprobe = 10   # clusters to search at query time; increase for higher recall

quantizer = faiss.IndexFlatL2(dim)
index = faiss.IndexIVFFlat(quantizer, dim, nlist, faiss.METRIC_INNER_PRODUCT)

# Must train before adding (k-means on a sample)
index.train(embeddings)
index.add(embeddings)

index.nprobe = nprobe
distances, indices = index.search(queries, k=5)
```

IVF is preferred over HNSW when:
- You need to compress the index (combine with PQ: `IndexIVFPQ`)
- N > 10M and memory is constrained
- You can tolerate a training step

---

## Decision Table

| Scenario | Recommended | Why |
|----------|-------------|-----|
| N < 50K, any dim | Brute-force (`IndexFlatIP`) | Fast enough; no recall loss |
| N 50K–5M, dim ≤ 768 | HNSW (`IndexHNSWFlat`) | High recall, no training, incremental |
| N > 5M, memory tight | IVF+PQ (`IndexIVFPQ`) | Compressed; accepts recall tradeoff |
| Need exact results | `IndexFlatIP` | No approximation |
| Streaming inserts | HNSW | IVF requires retraining or re-adding |
| Low-latency serving | HNSW with small `ef_search` | Faster per query than IVF at same recall |

---

## Recall Calibration Procedure

Before deploying ANN in production, measure actual recall on a held-out sample:

```python
def measure_recall(index_approx, embeddings_exact, queries, k=10, sample=500):
    """Compare ANN results to exact brute-force on sample queries."""
    exact_index = faiss.IndexFlatIP(embeddings_exact.shape[1])
    exact_index.add(embeddings_exact)
    
    _, exact_ids = exact_index.search(queries[:sample], k)
    _, approx_ids = index_approx.search(queries[:sample], k)
    
    recall_at_k = []
    for ex, ap in zip(exact_ids, approx_ids):
        hit = len(set(ex) & set(ap))
        recall_at_k.append(hit / k)
    
    return sum(recall_at_k) / len(recall_at_k)

# Example output:
# HNSW M=32, efSearch=100 → recall@10 = 0.974
# HNSW M=32, efSearch=50  → recall@10 = 0.951
# IVF nprobe=10            → recall@10 = 0.883
# IVF nprobe=50            → recall@10 = 0.962
```

Target recall depends on use case:
- **Deduplication**: recall@10 ≥ 0.98 (missing a duplicate is a false negative)
- **FAQ retrieval**: recall@5 ≥ 0.95 (user sees top-5 answers)
- **Recommendation**: recall@20 ≥ 0.90 (diversity tolerates some misses)

---

## Practical Pitfalls

**Unnormalized vectors produce wrong cosine similarity.**  
FAISS `METRIC_INNER_PRODUCT` on unit vectors = cosine similarity. On unnormalized vectors it equals the dot product, which conflates magnitude with angle. Always call `faiss.normalize_L2(embeddings)` before indexing if you want cosine.

**HNSW does not support removal.**  
Deleting a document from an HNSW index requires rebuilding. For corpora with frequent deletes, use IVF with periodic rebuilds, or keep a deletion mask and filter results post-search.

**IVF `nlist` must be calibrated to N.**  
Too few clusters (e.g., `nlist=10` for N=1M) → huge clusters, `nprobe` doesn't help. Too many → clusters too small for k-means to converge. Rule of thumb: `nlist ≈ sqrt(N)` for balanced clusters, `nlist ≈ 4*sqrt(N)` for higher precision.

**HNSW memory scales with M × N.**  
At M=32 and dim=384, each node occupies approximately `(M * 2 * 4) + (dim * 4)` ≈ 1.8 KB. For N=1M, that is ~1.8 GB RAM. If memory is constrained, drop to M=16 or switch to IVF+PQ.

**`ef_construction` affects quality permanently.**  
Unlike `ef_search` (adjustable at query time), `ef_construction` is fixed at build time. Building with low `ef_construction` to save time and then raising `ef_search` later does **not** recover the lost graph quality. Build with at least `ef_construction = 2 * M`.

---

## Minimal End-to-End Example

```python
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# 1. Encode corpus
model = SentenceTransformer("all-MiniLM-L6-v2")
corpus = ["How to reset my password",
          "I forgot my login credentials",
          "Shipping times for international orders",
          "When will my package arrive",
          "Refund policy for damaged goods"]

embeddings = model.encode(corpus, normalize_embeddings=True).astype("float32")
# normalize_embeddings=True sets unit norm; FAISS inner product = cosine

# 2. Build HNSW index
dim = embeddings.shape[1]  # 384 for all-MiniLM-L6-v2
index = faiss.IndexHNSWFlat(dim, 32, faiss.METRIC_INNER_PRODUCT)
index.hnsw.efConstruction = 200
index.add(embeddings)

# 3. Query
query = model.encode(["How do I change my password?"],
                     normalize_embeddings=True).astype("float32")
index.hnsw.efSearch = 100
scores, ids = index.search(query, k=3)

for score, idx in zip(scores[0], ids[0]):
    print(f"  score={score:.3f}  '{corpus[idx]}'")

# Expected output (approximate):
#   score=0.923  'How to reset my password'
#   score=0.814  'I forgot my login credentials'
#   score=0.231  'Shipping times for international orders'
```

This confirms the SKILL.md Iron Law: "How to reset my password" and "I forgot my login credentials" score 0.81+ despite near-zero lexical overlap (Jaccard ≈ 0.07).

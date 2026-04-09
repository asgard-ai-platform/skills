# Graph-Based Extractive Summarization

TextRank and LexRank both treat a document as a graph where **sentences are nodes** and **similarity scores are edge weights**, then apply eigenvector-based ranking (PageRank) to surface the most "central" sentences. They differ only in how they build the similarity matrix and normalize it.

---

## Sentence Similarity Matrix

Given a document with sentences $S = \{s_1, s_2, \ldots, s_n\}$, compute an $n \times n$ similarity matrix $W$.

### TextRank: TF-weighted token overlap

$$\text{sim}(s_i, s_j) = \frac{|\{w \mid w \in s_i \cap s_j\}|}{\log(|s_i|) + \log(|s_j|)}$$

- $w$ = tokens (after stopword removal)
- Denominator penalizes long sentences to avoid length bias
- Result is **asymmetric in intuition but symmetric in practice** (both sides use the same token set)

**Why log?** Without it, a 2-sentence document with one 5-word sentence and one 50-word sentence would give the 50-word sentence a near-zero denominator advantage in scoring.

### LexRank: TF-IDF cosine similarity

Each sentence is a TF-IDF vector over the document vocabulary.

$$\text{sim}(s_i, s_j) = \cos(\vec{v}_i, \vec{v}_j) = \frac{\vec{v}_i \cdot \vec{v}_j}{\|\vec{v}_i\| \cdot \|\vec{v}_j\|}$$

LexRank then **thresholds** the matrix:

$$W_{ij} = \begin{cases} \text{sim}(s_i, s_j) & \text{if } \text{sim}(s_i, s_j) \geq \theta \\ 0 & \text{otherwise} \end{cases}$$

Typical $\theta = 0.1$. This converts a dense similarity graph into a sparse one, which makes PageRank converge faster and reduces noise from near-zero similarities.

---

## PageRank on the Sentence Graph

After building $W$, normalize each row to get a stochastic (transition) matrix $M$:

$$M_{ij} = \frac{W_{ij}}{\sum_k W_{ik}}$$

If row $i$ is all zeros (isolated node), set $M_{ij} = \frac{1}{n}$ for all $j$ (uniform fallback).

Apply the **damped PageRank** update:

$$\text{score}(s_i) = \frac{1 - d}{n} + d \sum_{j \neq i} M_{ji} \cdot \text{score}(s_j)$$

- $d$ = damping factor, typically **0.85**
- Initialize all scores to $\frac{1}{n}$
- Iterate until $\|\text{score}^{(t+1)} - \text{score}^{(t)}\|_1 < \epsilon$ (e.g., $\epsilon = 10^{-4}$)
- Usually converges in 20–50 iterations

The damping factor $(1-d)$ represents the probability of a random jump to any sentence, preventing the algorithm from getting stuck in sink nodes.

---

## Worked Example (4 sentences)

```
s1: "Apple reported record revenue of $90B this quarter."
s2: "The revenue growth was driven by iPhone and Services."
s3: "CEO Tim Cook praised the team's performance."
s4: "Analysts expect continued growth next quarter."
```

**Step 1: Token sets** (after stopword removal)

| | tokens |
|---|---|
| s1 | {apple, reported, record, revenue, 90b, quarter} |
| s2 | {revenue, growth, driven, iphone, services} |
| s3 | {ceo, tim, cook, praised, team, performance} |
| s4 | {analysts, expect, continued, growth, next, quarter} |

**Step 2: TextRank similarity matrix**

$$\text{sim}(s_1, s_2) = \frac{|\{\text{revenue}\}|}{\log(6) + \log(5)} = \frac{1}{1.792 + 1.609} = \frac{1}{3.401} \approx 0.294$$

$$\text{sim}(s_1, s_4) = \frac{|\{\text{quarter}\}|}{\log(6) + \log(6)} = \frac{1}{3.584} \approx 0.279$$

$$\text{sim}(s_2, s_4) = \frac{|\{\text{growth}\}|}{\log(5) + \log(6)} \approx 0.294$$

$$\text{sim}(s_1, s_3) = \frac{0}{\ldots} = 0, \quad \text{sim}(s_3, s_4) = 0$$

Raw $W$ (symmetric):

```
     s1     s2     s3     s4
s1 [ 0     0.294   0     0.279 ]
s2 [ 0.294  0      0     0.294 ]
s3 [ 0      0      0     0     ]
s4 [ 0.279  0.294  0     0     ]
```

**Step 3: Row-normalize**

```
s1: [0, 0.513, 0, 0.487]     (0.294 / 0.573, 0.279 / 0.573)
s2: [0.500, 0, 0, 0.500]
s3: [0.25, 0.25, 0.25, 0.25] ← isolated, uniform fallback
s4: [0.487, 0.513, 0, 0]
```

**Step 4: PageRank** (d=0.85, init=0.25 each, after convergence)

Approximate final scores:
- s1: **0.31**
- s2: **0.29**
- s3: 0.09 (isolated — shares no tokens)
- s4: **0.28**

→ Select top-2: `[s1, s2]`, reordered by original position: s1 → s2.

Summary: *"Apple reported record revenue of $90B this quarter. The revenue growth was driven by iPhone and Services."*

---

## Implementation (Python, stdlib only)

```python
import math
import re
from collections import Counter

STOPWORDS = {"the", "a", "an", "is", "was", "were", "be", "been",
             "this", "that", "of", "in", "on", "at", "to", "and", "or"}

def tokenize(sentence: str) -> set[str]:
    tokens = re.findall(r'\b[a-z]+\b', sentence.lower())
    return {t for t in tokens if t not in STOPWORDS}

def textrank_similarity(s_i: set, s_j: set) -> float:
    if not s_i or not s_j:
        return 0.0
    overlap = len(s_i & s_j)
    if overlap == 0:
        return 0.0
    denom = math.log(len(s_i) + 1) + math.log(len(s_j) + 1)
    return overlap / denom

def build_similarity_matrix(sentences: list[str]) -> list[list[float]]:
    token_sets = [tokenize(s) for s in sentences]
    n = len(sentences)
    W = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                W[i][j] = textrank_similarity(token_sets[i], token_sets[j])
    return W

def row_normalize(W: list[list[float]]) -> list[list[float]]:
    n = len(W)
    M = [[0.0] * n for _ in range(n)]
    for i in range(n):
        row_sum = sum(W[i])
        for j in range(n):
            M[i][j] = W[i][j] / row_sum if row_sum > 0 else 1.0 / n
    return M

def pagerank(M: list[list[float]], d: float = 0.85,
             max_iter: int = 100, eps: float = 1e-4) -> list[float]:
    n = len(M)
    scores = [1.0 / n] * n
    for _ in range(max_iter):
        new_scores = [(1 - d) / n] * n
        for i in range(n):
            for j in range(n):
                new_scores[i] += d * M[j][i] * scores[j]
        delta = sum(abs(new_scores[i] - scores[i]) for i in range(n))
        scores = new_scores
        if delta < eps:
            break
    return scores

def textrank_summarize(text: str, top_k: int = 3) -> list[str]:
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    if len(sentences) <= top_k:
        return sentences
    W = build_similarity_matrix(sentences)
    M = row_normalize(W)
    scores = pagerank(M)
    ranked = sorted(range(len(sentences)), key=lambda i: scores[i], reverse=True)
    selected = sorted(ranked[:top_k])          # restore original order
    return [sentences[i] for i in selected]
```

---

## TextRank vs LexRank: Decision Table

| Dimension | TextRank | LexRank |
|---|---|---|
| Similarity metric | Token overlap (log-normalized) | TF-IDF cosine |
| Graph density | Dense (all pairs nonzero if sharing ≥1 token) | Sparse (threshold $\theta$ removes weak edges) |
| IDF weighting | No — all tokens equal weight | Yes — rare terms weighted higher |
| Implementation complexity | Simpler (no IDF needed) | Needs corpus-level IDF |
| Best for | Short documents, quick baseline | Multi-document, topic-diverse corpora |
| Single document | Good | Good |
| Multi-document | Misses cross-doc rare terms | Better — IDF captures cross-doc uniqueness |

**Rule of thumb:** Start with TextRank. Switch to LexRank when the corpus has significant vocabulary diversity (technical domains, multi-domain collections) or when single-document results are satisfactory but multi-document quality is poor.

---

## Selecting Top-K Sentences

After PageRank converges, three strategies for choosing which sentences to include:

### 1. Fixed-K
Select the top-$k$ sentences by score. Simple. Requires tuning $k$ per domain.

### 2. Compression Ratio
Select sentences until cumulative word count reaches `ratio × original_words`. Typical ratios: 0.1–0.2 for news, 0.15–0.25 for technical reports.

```python
def select_by_ratio(sentences, scores, ratio=0.15):
    total_words = sum(len(s.split()) for s in sentences)
    budget = int(total_words * ratio)
    ranked = sorted(range(len(sentences)), key=lambda i: scores[i], reverse=True)
    selected, word_count = [], 0
    for idx in ranked:
        w = len(sentences[idx].split())
        if word_count + w <= budget:
            selected.append(idx)
            word_count += w
    return sorted(selected)
```

### 3. Score Threshold
Select all sentences where `score > mean_score + 0.5 * std_score`. Adaptive to document length but can select 0 sentences on very uniform graphs.

**Recommendation:** Use compression ratio for production pipelines. Fixed-K is fine for prototyping and evaluation.

---

## Positional Bias Correction

For news articles using the **inverted pyramid** structure, the first sentence is almost always the most important. Without correction, TextRank/LexRank may redundantly select multiple early sentences.

**Option A: Position prior** — multiply PageRank score by a position weight before ranking:

$$\text{final\_score}(s_i) = \text{pagerank}(s_i) \times \left(1 + \frac{\alpha}{i + 1}\right)$$

where $\alpha \in [0.5, 1.5]$ boosts early sentences. Set $\alpha = 0$ to disable.

**Option B: MMR (Maximal Marginal Relevance)** — after selecting the highest-ranked sentence, penalize remaining candidates by their similarity to already-selected sentences:

$$\text{MMR}(s_i) = \lambda \cdot \text{pagerank}(s_i) - (1-\lambda) \cdot \max_{s_j \in \text{selected}} \text{sim}(s_i, s_j)$$

$\lambda \in [0.5, 0.7]$ balances relevance vs diversity. MMR is especially useful for **multi-document summarization** where many sentences express the same fact.

---

## Common Failure Modes

| Symptom | Cause | Fix |
|---|---|---|
| All selected sentences from paragraph 1 | Position bias without MMR | Apply MMR or position-decay weight |
| Short sentences dominate | Log-normalization insufficient | Use sentence length as a minimum filter (e.g., ≥ 8 words) |
| Graph fully disconnected | High $\theta$ in LexRank or no shared tokens | Lower threshold; verify tokenization is working |
| Scores all equal (~1/n) | All rows isolated (fallback uniform) | Check tokenizer — likely stripping all tokens |
| Extractive summary is incoherent | Top-K sentences selected without position restore | Always re-sort selected indices by original position before joining |

---

## ROUGE Quick Reference

ROUGE is the standard evaluation metric for extractive summarization quality.

| Metric | Measures | Formula sketch |
|---|---|---|
| ROUGE-1 | Unigram overlap | $\frac{\|S_{\text{summary}} \cap S_{\text{ref}}\|}{\|S_{\text{ref}}\|}$ (recall-oriented) |
| ROUGE-2 | Bigram overlap | Same but over bigrams |
| ROUGE-L | Longest common subsequence | LCS length / reference length |

**Warning from SKILL.md**: ROUGE correlates poorly with human judgement for abstractive summaries. For extractive, ROUGE-1 and ROUGE-2 are more reliable because selected sentences preserve original wording. Even so, a ROUGE-2 of 0.12 on news is typical for single-model extractive systems — do not expect high absolute values.

Typical extractive baselines on CNN/DailyMail:

| System | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---|---|---|---|
| Lead-3 (first 3 sentences) | 40.3 | 17.7 | 36.5 |
| TextRank | 33.2 | 11.8 | 29.6 |
| LexRank | 35.9 | 13.5 | 32.1 |
| Oracle (best possible extractive) | 53.0 | 31.0 | 49.0 |

Lead-3 beats TextRank on news because of the inverted pyramid. On scientific papers or legal documents, graph-based methods outperform Lead-3.

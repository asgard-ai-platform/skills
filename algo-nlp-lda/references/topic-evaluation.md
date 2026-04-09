# Topic Evaluation: Coherence Metrics and K Selection

## What "Good" Topics Look Like

A good topic is one where the top words co-occur frequently in real documents and make semantic sense to a human reader. LDA optimization (maximizing likelihood) does NOT directly optimize for human interpretability — this is why external evaluation is necessary.

Two evaluation axes:

| Axis | Automated Metric | Human Signal |
|------|-----------------|--------------|
| Internal coherence | C_v, UMass, NPMI | "Do these 10 words belong together?" |
| Topic distinctiveness | pairwise cosine distance | "Are topics redundant?" |

---

## Coherence Metrics

### UMass Coherence (fast, uses training corpus)

For a topic with top words w₁, w₂, ..., wₙ (ordered by probability):

$$C_{UMass} = \sum_{j=2}^{N} \sum_{i=1}^{j-1} \log \frac{D(w_i, w_j) + 1}{D(w_i)}$$

Where:
- D(wᵢ, wⱼ) = number of documents containing both wᵢ and wⱼ
- D(wᵢ) = number of documents containing wᵢ
- N = number of top words (typically 10)

**Range**: negative values; closer to 0 = more coherent.  
**Bias**: optimistic because it uses the same corpus for training and evaluation.

### C_v Coherence (recommended, uses external reference)

C_v combines several signals:

1. Compute **normalized pointwise mutual information (NPMI)** for each word pair (wᵢ, wⱼ):

$$NPMI(w_i, w_j) = \frac{\log \frac{P(w_i, w_j)}{P(w_i) \cdot P(w_j)}}{-\log P(w_i, w_j)}$$

2. Represent each word as a **context vector**: for word w, its vector is the NPMI values against all other top words in that topic.

3. Compute topic coherence as **mean cosine similarity** between the context vector of each word and the aggregate context vector of all other words.

**Range**: 0 to 1; typical good scores are 0.4–0.7 for news corpora.  
**Reference corpus**: Wikipedia dump is standard. Use the same domain corpus if available.

### NPMI (simpler C_v approximation)

For topics where you just need a quick ranking between K values:

$$NPMI_{topic} = \frac{1}{\binom{N}{2}} \sum_{i < j} NPMI(w_i, w_j)$$

**Range**: -1 to 1; higher is better.  
**Use case**: fast comparison across multiple K values on the training corpus.

---

## K Selection Procedure

### Starting Point

Use √(corpus_size / 2) as an initial guess, then search a range:

```
corpus_size = number of documents
K_init = max(5, int(sqrt(corpus_size / 2)))
K_range = [5, 10, 15, 20, 25, 30]  # adjust upper bound based on K_init
```

For 1000 documents: K_init ≈ 22, search K ∈ {5, 10, 15, 20, 25, 30}.  
For 10000 documents: K_init ≈ 70, search K ∈ {10, 20, 30, 40, 50, 60, 70}.

### Step-by-Step Protocol

```
1. For each K in K_range:
   a. Train LDA with that K (same random seed for comparability)
   b. Compute C_v coherence on top-10 words per topic
   c. Record: mean coherence, min coherence (worst topic), std dev

2. Plot coherence vs K — look for elbow or peak

3. Among K values within 0.02 coherence of the peak:
   a. Choose the SMALLER K (prefer fewer, broader topics)
   b. Unless the smaller K has clearly redundant topics on inspection

4. Manual inspection: read top-10 words for each topic at finalist K values
   a. Reject K if >20% of topics are "junk" (mixed incoherent words)
   b. Reject K if >30% of topics are near-duplicates of each other

5. Final K = smallest K that passes step 4
```

### Worked Example

**Corpus**: 2000 news articles  
**K range tested**: 5, 10, 15, 20, 25

| K | Mean C_v | Min C_v | Junk topics | Duplicate topics |
|---|----------|---------|-------------|------------------|
| 5 | 0.51 | 0.44 | 0 | 1 (politics+economy merged) |
| 10 | 0.58 | 0.41 | 1 | 0 |
| 15 | 0.61 | 0.38 | 2 | 1 |
| 20 | 0.59 | 0.30 | 4 | 2 |
| 25 | 0.55 | 0.22 | 6 | 3 |

**Decision**: K=10 wins. K=15 has higher mean but 2 junk topics and 1 duplicate. K=10 coherence is 0.03 lower than K=15 but cleaner on inspection.

---

## Detecting and Handling Junk Topics

A "junk" topic has one or more of these signatures:

| Pattern | Example top words | Cause |
|---------|-------------------|-------|
| Stop words survived | "said, would, also, year, one" | Insufficient preprocessing |
| Named entities leaked | "New York, United States, John, Mr." | NER filtering skipped |
| Punctuation/numbers | "2021, 000, %, $, ..." | Tokenization not cleaned |
| Generic news words | "news, report, official, government, spokesperson" | Domain stop words not added |
| Two themes merged | "goal, score, election, vote, win" | K too small |

**Remediation priority**:
1. Stop words → fix preprocessing, re-run
2. Named entity leakage → add NER filter or domain stop list
3. Two themes merged → increase K
4. Generic domain words → add domain-specific stop list (e.g., for news: "said", "told", "according")

Never just delete a junk topic and reindex — fix the root cause.

---

## Topic Distinctiveness Check

Even if each topic is internally coherent, two topics may be near-duplicates. Compute pairwise cosine similarity on topic-word distributions:

```python
import numpy as np

# topic_word_matrix: shape (K, vocab_size), rows sum to 1
def topic_overlap_report(topic_word_matrix, threshold=0.7):
    K = topic_word_matrix.shape[0]
    norms = np.linalg.norm(topic_word_matrix, axis=1, keepdims=True)
    normalized = topic_word_matrix / norms
    sim_matrix = normalized @ normalized.T
    
    duplicates = []
    for i in range(K):
        for j in range(i+1, K):
            if sim_matrix[i, j] > threshold:
                duplicates.append((i, j, sim_matrix[i, j]))
    return duplicates
```

**Threshold guidance**:
- cosine > 0.9: almost certainly duplicates → reduce K
- cosine 0.7–0.9: highly overlapping → inspect manually, likely reduce K
- cosine 0.5–0.7: related but distinct → acceptable, keep K
- cosine < 0.5: distinct topics → good

---

## Perplexity vs Coherence

Perplexity (held-out log-likelihood) is the traditional LDA metric but does NOT correlate with human interpretability. Papers by Chang et al. (2009) showed that models with lower perplexity (better generative fit) can have WORSE human-judged topic quality.

**Rule**: Use perplexity only as a sanity check (perplexity should decrease as training converges). Do NOT use perplexity to select K. Use coherence.

| Metric | Use for | Do NOT use for |
|--------|---------|----------------|
| Perplexity | Checking convergence, comparing same-K runs | Selecting K |
| UMass coherence | Fast K ranking during development | Final evaluation (training bias) |
| C_v coherence | Final K selection and reporting | Quick iteration (slower) |
| Human inspection | Final acceptance | Automation |

---

## Coherence Implementation (gensim)

```python
from gensim.models import LdaModel, CoherenceModel
from gensim.corpora import Dictionary

def evaluate_lda(corpus_tokenized, k_range=(5, 10, 15, 20)):
    """
    corpus_tokenized: list of list of str (already cleaned, lemmatized)
    Returns dict of K -> coherence score
    """
    dictionary = Dictionary(corpus_tokenized)
    dictionary.filter_extremes(no_below=5, no_above=0.5)
    bow_corpus = [dictionary.doc2bow(doc) for doc in corpus_tokenized]
    
    results = {}
    for K in k_range:
        model = LdaModel(
            corpus=bow_corpus,
            id2word=dictionary,
            num_topics=K,
            alpha=50/K,       # standard starting point
            eta=0.01,
            iterations=1000,
            passes=10,
            random_state=42   # fix seed for comparability across K
        )
        cm = CoherenceModel(
            model=model,
            texts=corpus_tokenized,
            dictionary=dictionary,
            coherence='c_v'   # use 'u_mass' for faster but biased estimate
        )
        results[K] = {
            'score': cm.get_coherence(),
            'per_topic': cm.get_coherence_per_topic()
        }
    return results
```

**Runtime note**: C_v coherence for K=20 on 5000 documents takes ~5–15 minutes. If iteration is slow, use `coherence='u_mass'` during development and switch to `c_v` for final evaluation.

---

## Stability Check (Multiple Seeds)

Gibbs sampling is stochastic. A K that looks good on one run may give poor topics on another. Before finalizing K:

```python
seeds = [0, 1, 2, 3, 4]
scores = []
for seed in seeds:
    model = LdaModel(..., random_state=seed)
    cm = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
    scores.append(cm.get_coherence())

mean_score = np.mean(scores)
std_score = np.std(scores)
# Accept if std < 0.03; reject and increase iterations if std >= 0.05
```

**Threshold**: std dev < 0.03 across 5 seeds = stable. If std ≥ 0.05, increase `iterations` or `passes` before trusting the coherence scores.

---

## Decision Checklist Before Reporting Topics

```
[ ] Coherence C_v > 0.40 (news/general), or > 0.35 (specialized domain)
[ ] Mean coherence is within 0.05 of the peak K value
[ ] No topic has cosine similarity > 0.7 with another topic
[ ] Junk topics < 20% of total K
[ ] Coherence std dev across 5 seeds < 0.03
[ ] All topics have been read and labeled by a human
[ ] Labels are written BEFORE seeing document assignments (avoid confirmation bias)
```

If any box is unchecked, diagnose and fix before delivering results. Do not report topics you cannot label.

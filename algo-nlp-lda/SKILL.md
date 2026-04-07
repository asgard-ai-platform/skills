---
name: "algo-nlp-lda"
description: "Implement LDA topic modeling to discover latent topics in document collections. Use this skill when the user needs to extract topics from a text corpus, categorize documents by theme, or explore thematic structure — even if they say 'what are the main topics', 'topic extraction', or 'document clustering by theme'."
metadata:
  category: "WP-45 NLP 演算法"
  tags: ["nlp", "lda", "topic-modeling", "text-mining"]
---

# LDA Topic Modeling

## Overview

Latent Dirichlet Allocation models each document as a mixture of topics and each topic as a distribution over words. Discovers K latent topics from a corpus without supervision. Uses Gibbs sampling or variational inference. Complexity: O(N × K × iterations) where N = total word tokens.

## When to Use

**Trigger conditions:**
- Discovering latent themes in a large document collection
- Organizing/categorizing documents by automatically discovered topics
- Exploratory text analysis when categories are unknown

**When NOT to use:**
- When categories are known (use supervised classification)
- For short texts (tweets, titles) — too few words per document for reliable topic assignment
- When you need semantic understanding (use embeddings)

## Algorithm

```
IRON LAW: The Number of Topics K Must Be Chosen, Not Discovered
LDA does NOT tell you how many topics exist. K is a hyperparameter.
Too few topics: overly broad, mixed themes. Too many: fragmented,
redundant topics. Use coherence score (C_v) to compare K values,
but the final choice requires human judgment on topic interpretability.
```

### Phase 1: Input Validation
Preprocess: tokenize, remove stop words, apply lemmatization. Build document-term matrix. Filter: remove terms appearing in <5 or >50% of documents.
**Gate:** Clean DTM, vocabulary size reasonable (1K-50K terms).

### Phase 2: Core Algorithm
1. Choose K (start with √(N/2), try range K=5,10,15,20,...)
2. Set hyperparameters: α = 50/K (document-topic density), β = 0.01 (topic-word density)
3. Run LDA (Gibbs sampling: 1000+ iterations, or variational inference)
4. Extract: topic-word distributions (top 10-20 words per topic) and document-topic distributions

### Phase 3: Verification
Evaluate: topic coherence (C_v score, higher is better), manual inspection of top words per topic, check for "junk" topics (mixed incoherent words).
**Gate:** Coherence score acceptable, topics are humanly interpretable.

### Phase 4: Output
Return topics with top words and document assignments.

## Output Format

```json
{
  "topics": [{"id": 0, "label": "finance", "top_words": ["revenue", "profit", "quarter", "growth"], "coherence": 0.55}],
  "doc_topics": [{"doc_id": "d1", "dominant_topic": 0, "topic_distribution": [0.7, 0.1, 0.2]}],
  "metadata": {"K": 10, "coherence_avg": 0.48, "documents": 5000, "vocabulary": 8000}
}
```

## Examples

### Sample I/O
**Input:** 1000 news articles, K=5
**Expected:** Topics like: {politics, sports, technology, business, entertainment} with coherent top words per topic.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Very short documents | Poor topic assignment | Too few words for reliable mixture estimation |
| Homogeneous corpus | 1-2 topics dominate | All documents are similar, limited topic diversity |
| K=1 | Single topic = corpus vocabulary | Degenerate case, no discrimination |

## Gotchas

- **Stop words MUST be removed**: LDA will create "junk" topics dominated by common words ("the", "is", "and") if stop words remain.
- **Topic labeling is manual**: LDA gives word distributions, NOT topic names. You must interpret and label topics based on top words.
- **Reproducibility**: Gibbs sampling is stochastic. Different random seeds give different topics. Run multiple times and check stability.
- **Dynamic topics**: Standard LDA assumes topics are static. For evolving corpora (news over years), use Dynamic Topic Models.
- **Hyperparameter sensitivity**: Low α produces documents with fewer, more distinct topics. Low β produces topics with fewer, more specific words. Tune or use automatic methods.

## References

- For coherence metrics and K selection, see `references/topic-evaluation.md`
- For dynamic and correlated topic models, see `references/advanced-lda.md`

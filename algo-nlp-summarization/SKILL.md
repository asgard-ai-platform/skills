---
name: "algo-nlp-summarization"
description: "Implement text summarization using extractive and abstractive approaches. Use this skill when the user needs to condense long documents, build an automatic summarization pipeline, or compare summarization strategies — even if they say 'summarize this document', 'TLDR', or 'key points extraction'."
metadata:
  category: "WP-45 NLP 演算法"
  tags: ["nlp", "summarization", "extractive", "abstractive"]
---

# Text Summarization

## Overview

Text summarization condenses documents while preserving key information. Extractive: selects and concatenates important sentences from the original. Abstractive: generates new text that paraphrases the content. Extractive is simpler and more faithful; abstractive is more fluent but may hallucinate.

## When to Use

**Trigger conditions:**
- Condensing long documents, reports, or article collections
- Building automated summary pipelines for content curation
- Comparing extractive vs abstractive approaches for a use case

**When NOT to use:**
- When full document understanding is needed (summarization loses detail)
- For structured data extraction (use NER or information extraction)

## Algorithm

```
IRON LAW: Abstractive Summarization Can HALLUCINATE
Abstractive models may generate fluent text containing facts NOT in
the source. Always verify key claims in abstractive summaries against
the original document. For high-stakes use cases (legal, medical),
prefer extractive or use abstractive with factual consistency checking.
```

### Phase 1: Input Validation
Determine: input length, target summary length (ratio or word count), single-doc vs multi-doc, domain.
**Gate:** Input text available, target length defined.

### Phase 2: Core Algorithm
**Extractive (TextRank/LexRank):**
1. Split document into sentences
2. Build similarity graph (sentence nodes, cosine similarity edges)
3. Run PageRank on sentence graph
4. Select top-k sentences by rank, reorder by original position

**Abstractive (transformer-based):**
1. Use pre-trained model (BART, T5, Pegasus)
2. Encode input document (handle length limits with chunking if needed)
3. Generate summary with beam search
4. Post-process: check for repetition, factual consistency

### Phase 3: Verification
Evaluate: ROUGE scores (ROUGE-1, ROUGE-2, ROUGE-L) against reference summaries. Manual check for factual accuracy and coherence.
**Gate:** ROUGE scores reasonable for domain, no hallucinations in spot-check.

### Phase 4: Output
Return summary with metadata.

## Output Format

```json
{
  "summary": "The company reported Q4 revenue of...",
  "method": "extractive_textrank",
  "metadata": {"input_words": 2000, "summary_words": 200, "compression_ratio": 0.10, "sentences_selected": 5}
}
```

## Examples

### Sample I/O
**Input:** 2000-word news article about quarterly earnings
**Expected:** 200-word summary covering: revenue, profit, guidance, key highlights. Extractive: 5-6 selected sentences. Abstractive: coherent paragraph.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Very short input (< 100 words) | Return as-is or minimal trimming | Already concise |
| Multiple contradicting sections | Summary may miss nuance | Summarization favors dominant theme |
| Technical jargon | Extractive preserves, abstractive may simplify | Domain expertise affects quality |

## Gotchas

- **ROUGE ≠ quality**: ROUGE measures n-gram overlap with references. A high-ROUGE summary can be incoherent, and a low-ROUGE summary can be excellent with different word choices.
- **Input length limits**: Transformer models have max token limits (512-4096). Long documents need chunking strategies (chunk-then-summarize or hierarchical summarization).
- **Repetition**: Abstractive models sometimes repeat phrases. Use repetition penalty during generation (no_repeat_ngram_size).
- **Position bias**: In news text, important information is front-loaded (inverted pyramid). Simple "take first N sentences" is a strong extractive baseline.
- **Multi-document summarization**: Summarizing multiple related documents requires handling redundancy and contradiction across sources.

## References

- For TextRank/LexRank implementation details, see `references/graph-based-extraction.md`
- For factual consistency checking, see `references/factual-consistency.md`

---
name: "algo-social-sentiment"
description: "Implement VADER sentiment analysis for social media text scoring. Use this skill when the user needs to analyze sentiment in tweets, reviews, or social posts, compute compound sentiment scores, or classify text polarity — even if they say 'is this positive or negative', 'sentiment of these comments', or 'social media mood analysis'."
metadata:
  category: "WP-38 社群演算法"
  tags: ["social-media", "sentiment-analysis", "vader", "nlp"]
---

# VADER Sentiment Analysis

## Overview

VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment tool optimized for social media. Returns compound score [-1, +1] combining positive, negative, and neutral proportions. Runs in O(n) per text where n = word count. No training required.

## When to Use

**Trigger conditions:**
- Analyzing sentiment in social media posts, tweets, or reviews
- Quick sentiment scoring without ML model training
- Processing text with slang, emoticons, and informal language

**When NOT to use:**
- For formal/academic text (VADER is tuned for social media)
- When domain-specific sentiment matters (e.g., financial sentiment — use FinBERT)
- When sarcasm detection is critical (VADER doesn't detect sarcasm)

## Algorithm

```
IRON LAW: VADER Is Designed for SOCIAL MEDIA Text
It handles slang, emoticons, capitalization, and punctuation as
sentiment modifiers. Applying it to formal documents (legal, academic,
medical) produces unreliable scores. For domain-specific text, use
domain-trained models instead.
```

### Phase 1: Input Validation
Tokenize text. Preserve: capitalization (ALL CAPS = emphasis), punctuation (! amplifies), emoticons/emoji.
**Gate:** Text is non-empty, encoding handled correctly.

### Phase 2: Core Algorithm
1. Look up each token in VADER lexicon (7,500+ sentiment-rated terms)
2. Apply grammatical rules: negation ("not good" = negative), degree modifiers ("very good" > "good"), capitalization boost, punctuation amplification
3. Compute raw valence scores for positive, negative, neutral proportions
4. Compute compound score: normalized sum of all valence scores using formula: compound = sum / √(sum² + α) where α = 15

### Phase 3: Verification
Classify: compound ≥ 0.05 → positive, ≤ -0.05 → negative, else neutral. Spot-check sample results.
**Gate:** Classifications pass manual spot-check on 10-20 examples.

### Phase 4: Output
Return compound score and polarity classification per text.

## Output Format

```json
{
  "results": [{"text": "...", "compound": 0.76, "pos": 0.45, "neu": 0.55, "neg": 0.0, "label": "positive"}],
  "metadata": {"texts_analyzed": 500, "distribution": {"positive": 0.45, "neutral": 0.35, "negative": 0.20}}
}
```

## Examples

### Sample I/O
**Input:** "This product is AMAZING!!! 😍"
**Expected:** compound ≈ 0.87 (positive). Boosted by: CAPS, !!!, 😍 emoji.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| "Not bad at all" | Slightly positive (~0.2) | Double negation partially handled |
| "😂😂😂" | Positive | Emoji mapped in lexicon |
| Empty string | Compound = 0, neutral | No tokens to score |

## Gotchas

- **Sarcasm is invisible**: "Oh great, another meeting" reads as positive. VADER has no sarcasm detection.
- **Negation window**: VADER applies negation within a 3-word window. "I do not think this is bad" may misparse the negation chain.
- **Emoji coverage**: VADER's emoji lexicon may not cover newer emoji. Update or supplement as needed.
- **Language limitation**: VADER is English-only. For Chinese/Japanese, use language-specific tools (e.g., SnowNLP for Chinese).
- **Compound threshold sensitivity**: The 0.05 boundary is arbitrary. Adjust thresholds based on your specific use case and tolerance for false positives.

## References

- For VADER lexicon and rules documentation, see `references/vader-rules.md`
- For comparison with transformer-based sentiment models, see `references/model-comparison.md`

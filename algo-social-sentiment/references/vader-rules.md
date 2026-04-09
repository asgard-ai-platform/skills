# VADER Lexicon and Grammatical Rules

VADER's scores come from two distinct sources: a **sentiment lexicon** (7,500+ rated words) and **five grammatical heuristics** applied on top of raw lexicon scores. Understanding both layers is necessary for predicting when VADER will succeed or fail.

---

## Lexicon Structure

Each lexicon entry has the form:

```
token    mean_sentiment_rating    std_dev    raw_human_ratings...
```

Example entries (from the published VADER lexicon):

| Token | Mean Rating | Interpretation |
|-------|-------------|----------------|
| `love` | +3.0 | Strongly positive |
| `hate` | -3.0 | Strongly negative |
| `okay` | +0.9 | Mildly positive |
| `bad` | -2.5 | Negative |
| `epic` | +2.2 | Positive (slang) |
| `sux` | -2.2 | Negative (slang) |
| `😍` | +3.0 | Positive (emoji) |
| `😂` | +2.2 | Positive (emoji) |
| `💔` | -1.5 | Negative (emoji) |

Ratings range roughly from −4 to +4. The lexicon was crowd-rated via Amazon Mechanical Turk (10 raters per item), so ratings reflect **general English-language social media consensus**, not domain-specific sentiment.

---

## Raw Valence Sum

For a text of n tokens, VADER first collects all lexicon hits:

```
valence_scores = [lexicon[token] for token in tokens if token in lexicon]
```

Before applying heuristics, the raw sum is just:

```
raw_sum = Σ valence_scores[i]
```

This raw sum is then modified by the five rules below before normalization.

---

## The Five Grammatical Heuristics

### Rule 1 — Punctuation Amplification

Exclamation marks amplify the overall sentiment magnitude.

```
exclamation_count = count("!" in text, max=3)
amplifier = exclamation_count × 0.292
```

The 0.292 constant was derived empirically. Three or more `!` gives the maximum boost of 0.876. Question marks have no effect in standard VADER.

**Example:**

| Text | Raw Sum | After `!` boost |
|------|---------|-----------------|
| `"great"` | 3.1 | 3.1 |
| `"great!"` | 3.1 | 3.1 + 0.292 = 3.392 |
| `"great!!!"` | 3.1 | 3.1 + 0.876 = 3.976 |

---

### Rule 2 — ALL CAPS Amplification

A token in ALL CAPS gets its valence boosted by a constant (`C_INCR = 0.733`) in the direction of its sentiment. The boost applies **only if** the entire text is not all-caps (all-caps text is ignored as a single-case document).

```python
def apply_caps_boost(valence, token, is_all_caps_text):
    if token.isupper() and not is_all_caps_text:
        if valence > 0:
            valence += C_INCR   # C_INCR = 0.733
        elif valence < 0:
            valence -= C_INCR
    return valence
```

**Example:**

| Text | Compound |
|------|----------|
| `"amazing"` | ~0.57 |
| `"AMAZING"` | ~0.72 |
| `"AMAZING!!!"` | ~0.83 |

The SKILL.md example `"This product is AMAZING!!! 😍"` reaching ~0.87 results from the compound effect of all three amplifiers: ALL CAPS + `!!!` + positive emoji.

---

### Rule 3 — Degree Modifier (Booster Words)

Booster words preceding a sentiment word modify its valence. VADER maintains two lists:

**BOOSTER_DICT** (partial):

| Word | Effect |
|------|--------|
| `very` | +0.293 |
| `really` | +0.293 |
| `extremely` | +0.293 |
| `kind of` | −0.293 |
| `sort of` | −0.293 |
| `marginally` | −0.293 |
| `barely` | −0.293 |

The booster adds or subtracts from the following token's valence. Distance also matters: boosters apply within a 3-token window before the sentiment word, but with diminishing effect:

```
if booster is 1 word before sentiment word: apply full B_INCR (0.293)
if booster is 2 words before:               apply B_INCR * 0.95
if booster is 3 words before:               apply B_INCR * 0.90
```

**Example:**

| Text | Valence of "good" |
|------|-------------------|
| `"good"` | 1.9 |
| `"very good"` | 1.9 + 0.293 = 2.193 |
| `"extremely good"` | 1.9 + 0.293 = 2.193 |
| `"kind of good"` | 1.9 − 0.293 = 1.607 |

---

### Rule 4 — Negation

This is the most complex rule and the most common source of VADER errors.

VADER applies negation by multiplying a sentiment token's valence by `N_SCALAR = −0.74` when a negation word appears **within the preceding 3-token window**.

**Negation word list includes:** `not`, `no`, `never`, `without`, `neither`, `nobody`, `nothing`, `nowhere`, `hardly`, `barely`, `scarcely`, `can't`, `cannot`, `won't`, `don't`, `didn't`, `doesn't`, `isn't`, `wasn't`, `weren't`, `shouldn't`, `wouldn't`, `couldn't`, `mightn't`, `mustn't`.

**Negation + booster interaction:**

When `"but"` appears in text, VADER treats the second clause as more important:

```
tokens before "but": multiply their valence by 0.5
tokens after  "but": multiply their valence by 1.5
```

**Special case — "at least":**

The two-word phrase `"at least"` reduces the negation effect when preceding a negative word.

**Worked example — "not bad at all":**

Tokens: `[not, bad, at, all]`

1. `bad` has lexicon valence −2.5
2. `not` is a negation word; it appears 1 token before `bad` → multiply by −0.74: valence = −2.5 × −0.74 = **+1.85**
3. `at all` after negation is a special intensifier that adds a small positive push
4. Final compound is mildly positive (~0.2)

This matches the SKILL.md edge case table entry.

**Why the 3-word window breaks down:**

```
"I do not think this is bad"
       ^negation        ^sentiment word (5 words away)
```

The `not` in position 3 is 5 tokens from `bad` in position 8 → outside the window → negation ignored → `bad` scores negative → compound is negative despite the intended positive meaning.

---

### Rule 5 — "But" Contrast Shift

Independent of negation, the conjunction `"but"` signals a sentiment shift. VADER re-weights the clauses:

```python
if "but" in tokens:
    but_index = tokens.index("but")
    for i, score in enumerate(valence_scores):
        if i < but_index:
            valence_scores[i] *= 0.5
        else:
            valence_scores[i] *= 1.5
```

**Example:**

| Text | Compound |
|------|----------|
| `"The food was bad but the service was great"` | ~0.34 (positive wins because post-but clause is up-weighted) |
| `"The service was great but the food was bad"` | ~−0.22 (negative wins post-but) |

---

## Compound Score Formula

After applying all five rules, VADER computes the compound score:

```
sum = Σ modified_valence_scores
compound = sum / √(sum² + α)    where α = 15
```

This is a **normalized tanh-like function** that squashes any real-valued sum into [−1, +1]. The α = 15 constant controls the steepness.

**Behavior at key values:**

| Raw Sum | Compound |
|---------|---------|
| 0 | 0.000 |
| ±4 | ±0.720 |
| ±8 | ±0.883 |
| ±12 | ±0.929 |
| ±20 | ±0.962 |

The function asymptotes toward ±1 but rarely reaches it in practice, because the individual lexicon ratings cap at ±4 and texts rarely accumulate very large raw sums.

---

## pos / neu / neg Proportions

The three sub-scores (`pos`, `neu`, `neg`) are computed independently from the compound:

```
positive_sum = Σ valence for tokens with positive valence + punctuation_amplifier
negative_sum = Σ |valence| for tokens with negative valence + punctuation_amplifier
neutral_count = count of tokens with zero/no-lexicon valence

total = positive_sum + |negative_sum| + neutral_count
pos = positive_sum / total
neg = |negative_sum| / total
neu = neutral_count / total
```

Note: `pos + neu + neg` = 1.0 by construction.

These proportions are independent of the compound score. A text with `compound = 0.6` might have `pos = 0.3, neu = 0.7, neg = 0.0` or `pos = 0.5, neu = 0.3, neg = 0.2` — the compound reflects the net balance; the proportions reflect the mixture.

---

## Rule Interaction: Priority Order

When multiple rules apply simultaneously, they stack multiplicatively in this order:

```
1. Fetch base lexicon valence
2. Apply ALL CAPS boost (per token)
3. Apply degree modifier (per token, looking back 3 tokens)
4. Apply negation (per token, looking back 3 tokens)
5. Apply "but" re-weighting (per clause)
6. Sum all modified valences
7. Apply punctuation amplification (to the sum)
8. Apply compound normalization
```

---

## Threshold Reference

The standard VADER thresholds from the original paper:

| Compound | Classification |
|----------|---------------|
| ≥ 0.05 | Positive |
| ≤ −0.05 | Negative |
| Between −0.05 and 0.05 | Neutral |

These thresholds are **not sacred**. The 0.05 boundary was chosen to minimize classification error on the benchmark dataset. For use cases where false positives are costly (e.g., flagging customer complaints), shifting the negative threshold to −0.2 reduces false negatives in the negative class. For use cases where recall matters more, widen the positive band.

**Adjusting for high-stakes classification:**

```python
def classify(compound, pos_threshold=0.05, neg_threshold=-0.05):
    if compound >= pos_threshold:
        return "positive"
    elif compound <= neg_threshold:
        return "negative"
    else:
        return "neutral"
```

---

## Known Lexicon Gaps

Areas where the VADER lexicon is thin or unreliable:

| Category | Issue |
|----------|-------|
| Newer slang (`bussin`, `no cap`, `lowkey`) | Not in original lexicon; score as neutral |
| Domain jargon (`bearish`, `bullish`) | Finance terms may have wrong polarity |
| Emoji released after ~2018 | Not covered; score as neutral |
| Non-English tokens | Silently ignored (score as neutral), no error raised |
| Irony markers (`sure`, `right`, `whatever`) | Score as positive/neutral when contextually sarcastic |

For newer emoji, the `vaderSentiment` Python package accepts custom lexicon extensions via the `SentimentIntensityAnalyzer` constructor:

```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

new_words = {
    "bussin": 2.5,
    "no cap": 1.8,
    "🤌": 2.0,
}
analyzer = SentimentIntensityAnalyzer()
analyzer.lexicon.update(new_words)
```

---

## Quick Diagnostic Checklist

When a VADER result looks wrong:

1. **Is the text English?** Non-English tokens are ignored → compound drifts toward 0.
2. **Does negation span > 3 tokens?** The negation window is short; long-range negation breaks.
3. **Is there sarcasm?** VADER has no detection mechanism. Manual review required.
4. **Are there domain-specific terms?** Check if key sentiment words are in the lexicon with the correct polarity for your domain.
5. **Is ALL CAPS suppressed?** If the *entire* text is upper-case, the caps boost does not fire.
6. **Is there a "but"?** The clause re-weighting may be flipping the expected dominant sentiment.

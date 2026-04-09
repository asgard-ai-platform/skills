# Query Understanding Pipeline

Query understanding transforms raw user input into a structured retrieval signal. It runs before retrieval — errors here cannot be corrected downstream.

## Pipeline Overview

```
Raw query string
      │
      ▼
[1] Normalization          (lowercase, strip punctuation, whitespace)
      │
      ▼
[2] Tokenization           (language-aware splitting)
      │
      ▼
[3] Spell Correction       (per-token and phrase-level)
      │
      ▼
[4] Intent Classification  (product / brand / category / navigational)
      │
      ▼
[5] Attribute Extraction   (color, size, price range, gender, ...)
      │
      ▼
[6] Synonym / Expansion    (conditional on intent)
      │
      ▼
Structured query object    → handed to retrieval stage
```

Each stage is a transformation. Output of stage N is the input of stage N+1. Stages are ordered by destructiveness: normalization is safe; synonym expansion changes recall significantly and runs last.

---

## Stage 1 & 2: Normalization and Tokenization

**Normalization rules (applied in order):**

| Rule | Example |
|------|---------|
| Lowercase | `Nike AIR MAX` → `nike air max` |
| Unicode normalize (NFC) | `café` → `café` (single codepoint) |
| Strip leading/trailing whitespace | `" shoes "` → `"shoes"` |
| Collapse internal whitespace | `"red  shoes"` → `"red shoes"` |
| Remove non-alphanumeric except `-`, `'` | `"men's #1 shoe!"` → `"men's 1 shoe"` |

**Tokenization is language-dependent:**

- **Latin script**: split on whitespace and hyphens. `"v-neck"` → `["v", "neck"]` or keep as compound (system choice — be consistent).
- **Chinese/Japanese/Korean**: requires a segmenter. Do NOT split on whitespace alone. `"皮鞋" `is one token; splitting character-by-character produces nonsense.
  - Recommended: [Jieba](https://github.com/fxsjy/jieba) for Chinese; MeCab for Japanese.
  - Without segmentation, `"男皮鞋"` (men's leather shoes) may fail to match `"皮鞋"` (leather shoes).

---

## Stage 3: Spell Correction

### When to apply

Spell correction fires when the raw query (or a token within it) has low index coverage — meaning few or no products match the exact string.

**Coverage check:**

```
token_coverage(t) = doc_freq(t) / total_indexed_docs
```

If `token_coverage(t) < threshold` (typical: 0.001), flag `t` as a spell-correction candidate.

### Edit-distance correction

Use Damerau-Levenshtein distance (allows transpositions: `wirelss` → `wireless`).

```python
def correction_candidates(token, vocab, max_edit=2):
    return [
        (candidate, damerau_levenshtein(token, candidate))
        for candidate in vocab
        if damerau_levenshtein(token, candidate) <= max_edit
    ]
```

**Rank candidates** by:

```
score(candidate) = freq(candidate) / (1 + edit_distance)
```

Where `freq(candidate)` is unigram frequency from the product index or query logs.

### Worked example

Query: `"wireles earbud"`

| Token | Coverage | Action |
|-------|----------|--------|
| `wireles` | 0.0001 → low | spell-correct |
| `earbud` | 0.003 → borderline | check candidates |

Top candidates for `wireles`:
- `wireless` (edit=1, freq=14200) → score = 14200 / 2 = 7100
- `wirelss` (edit=1, freq=3) → score = 3 / 2 = 1.5

Corrected query: `"wireless earbuds"`

### Phrase-level correction (N-gram approach)

Some misspellings only make sense in context. `"bule tooth"` → `"bluetooth"` requires seeing both tokens together.

Build a bigram frequency table from query logs:

```
bigram_freq("bule tooth")  = 12   ← rare
bigram_freq("blue tooth")  = 890
bigram_freq("bluetooth")   = 45000
```

If `bigram_freq(t1 t2) < single_token_freq(t1+t2 concatenated)`, prefer the compound correction.

### Guardrails

- **Never correct brand names.** Maintain a brand allowlist: `nike`, `adidas`, `zara`. Skip spell correction for any token in this list.
- **Cap edit distance at 2** for queries under 6 characters. `"bag"` must not become `"big"`.
- **Require frequency threshold** for the correction candidate. Rare words in the index are not valid corrections (they may be indexing noise).

---

## Stage 4: Intent Classification

Intent classification determines the **retrieval strategy**, not just the ranking. The four classes:

| Intent | Description | Retrieval strategy |
|--------|-------------|-------------------|
| `product_search` | User wants a specific type of product | Full-text across title, description, attributes |
| `brand_search` | User wants a specific brand | Filter or heavy boost on brand field |
| `category_browse` | User wants to explore a category | Return popular/curated category results; show facets |
| `navigational` | User is looking for a specific page or item (SKU, model number) | Exact match on SKU/model field first |

### Feature-based classifier

For a lightweight production classifier, use these features:

| Feature | Signal |
|---------|--------|
| Query is in brand list | `brand_search` |
| Query matches SKU pattern (e.g., `[A-Z]{2}\d{6}`) | `navigational` |
| Query is a single word that matches a category name | `category_browse` |
| Query contains size/color/gender attributes | `product_search` |
| Query is 1-2 words with no attribute markers | Ambiguous — default `product_search` |

**Decision logic (rule-based, applied in priority order):**

```python
def classify_intent(tokens, brands, categories, sku_pattern):
    query = " ".join(tokens)
    if re.match(sku_pattern, query):
        return "navigational"
    if query in brands or any(t in brands for t in tokens):
        return "brand_search"
    if query in categories and len(tokens) == 1:
        return "category_browse"
    return "product_search"
```

For higher accuracy: train a text classifier on labeled query logs. Label a sample of 2,000 queries manually; logistic regression on TF-IDF features often achieves >90% accuracy for these four classes with minimal data.

### Impact on downstream stages

- `navigational`: **skip** synonym expansion (would pollute exact-match intent)
- `brand_search`: inject `brand:{value}` as a hard filter into the structured query
- `category_browse`: skip attribute extraction; return category-level results with facets prominent
- `product_search`: proceed through attribute extraction and synonym expansion

---

## Stage 5: Attribute Extraction

Attribute extraction parses free-text queries into structured filters. This is the highest-value stage for long-tail queries.

### Attribute taxonomy

Define the attributes your catalog supports. Common ones:

```
color       : red, blue, black, ...
size        : XS, S, M, L, XL, XXL, 36, 37, ...
gender      : men, women, unisex, boys, girls
material    : cotton, leather, denim, silk, ...
price_range : "under 500", "1000 to 2000"
brand       : Nike, Adidas, ... (overlaps with intent)
```

### Extraction approach: pattern matching + lookup

For each attribute, maintain a lookup table and apply it to the normalized token stream.

**Price range patterns** (regex applied after normalization):

```python
PRICE_PATTERNS = [
    (r"under (\d+)",          lambda m: {"price_max": int(m.group(1))}),
    (r"(\d+) to (\d+)",       lambda m: {"price_min": int(m.group(1)), "price_max": int(m.group(2))}),
    (r"below (\d+)",          lambda m: {"price_max": int(m.group(1))}),
    (r"(\d+)\s*[-–]\s*(\d+)", lambda m: {"price_min": int(m.group(1)), "price_max": int(m.group(2))}),
]
```

**Attribute lookup** (token-by-token):

```python
def extract_attributes(tokens, attribute_tables):
    extracted = {}
    remaining_tokens = []
    i = 0
    while i < len(tokens):
        matched = False
        # Try bigrams first (e.g., "dark blue" as a color)
        if i + 1 < len(tokens):
            bigram = tokens[i] + " " + tokens[i+1]
            for attr, table in attribute_tables.items():
                if bigram in table:
                    extracted[attr] = table[bigram]
                    i += 2
                    matched = True
                    break
        if not matched:
            for attr, table in attribute_tables.items():
                if tokens[i] in table and attr not in extracted:
                    extracted[attr] = table[tokens[i]]
                    matched = True
                    break
        if not matched:
            remaining_tokens.append(tokens[i])
        i += 1 if not matched else i  # already incremented in loop
    return extracted, remaining_tokens
```

### Worked example: long-tail query

Query: `"blue cotton v-neck t-shirt men XL"`

After normalization and tokenization: `["blue", "cotton", "v", "neck", "t-shirt", "men", "xl"]`

Attribute extraction pass:

| Token(s) | Matched attribute | Value |
|----------|------------------|-------|
| `blue` | `color` | `blue` |
| `cotton` | `material` | `cotton` |
| `men` | `gender` | `men` |
| `xl` | `size` | `XL` |
| `v`, `neck`, `t-shirt` | no match | remain as text |

Result:

```json
{
  "free_text": "v neck t-shirt",
  "filters": {
    "color": "blue",
    "material": "cotton",
    "gender": "men",
    "size": "XL"
  }
}
```

Retrieval receives: full-text search on `"v neck t-shirt"` filtered by `color=blue AND material=cotton AND gender=men AND size=XL`.

### Filter vs. boost decision

Not every extracted attribute should become a hard filter:

| Attribute | Use as | Reason |
|-----------|--------|--------|
| `size` | Hard filter | Products without size XL are useless to this user |
| `color` | Boost (not filter) | Blue products ranked higher, but other colors shown as fallback |
| `price_range` | Hard filter | User stated budget constraint |
| `material` | Boost | Catalog may have limited exact-material indexing |
| `gender` | Hard filter | Mismatched gender products rarely acceptable |

The distinction matters for zero-result prevention: if you hard-filter on `color=blue` and no blue products exist, you get zero results. If you boost blue products instead, relevant non-blue results still appear.

---

## Stage 6: Synonym and Query Expansion

Expansion increases recall. It runs **after** intent classification and **only** for `product_search` intent.

### Synonym table format

```
earbuds       → earphones, headphones, in-ear headphones
sneakers      → trainers, athletic shoes, running shoes, sports shoes
laptop        → notebook, notebook computer
tv            → television, smart tv, flat screen
couch         → sofa, settee, loveseat
```

Synonyms are **asymmetric by default**: expand the query term to its synonyms; do not expand every synonym back to every other. Direction matters for precision.

### Expansion as query rewriting

Given the spell-corrected query `"wireless earbuds"`, with synonym expansion:

```
Before: "wireless earbuds"
After:  "wireless earbuds" OR "wireless earphones" OR "wireless headphones"
```

In Elasticsearch/OpenSearch syntax:

```json
{
  "query": {
    "bool": {
      "should": [
        {"match": {"title": {"query": "wireless earbuds", "boost": 2.0}}},
        {"match": {"title": {"query": "wireless earphones", "boost": 1.0}}},
        {"match": {"title": {"query": "wireless headphones", "boost": 0.8}}}
      ]
    }
  }
}
```

Boost the original query term highest — it's the user's actual intent signal.

### When NOT to expand

| Condition | Action |
|-----------|--------|
| Intent is `navigational` | Skip expansion |
| Intent is `brand_search` | Skip expansion for the brand token |
| Query already returns >500 results | Expansion adds noise; skip |
| Token is in the brand allowlist | Do not expand brand names to generic synonyms |
| Expansion would change product category | Block cross-category synonyms (e.g., `sandals` ≠ `shoes` for ranking purposes, even though they're related) |

### Synonym maintenance

Synonym tables are not static. Review process:

1. Weekly: pull queries with zero results after spell correction → candidate synonyms.
2. Weekly: pull queries with >30% abandonment rate (user searched, clicked nothing) → possible synonym gaps.
3. Monthly: audit for incorrect synonyms that hurt precision (track CTR on expanded terms separately).

**AirPods is a brand, not a synonym for earbuds.** Treating it as a synonym means searching `"airpods"` returns non-Apple products, which damages trust. Brand names belong in the brand allowlist, not the synonym table.

---

## Structured Query Object

The output of the full pipeline is a structured query object passed to retrieval:

```json
{
  "intent": "product_search",
  "free_text": "v neck t-shirt",
  "spell_corrections": [{"original": "wirelss", "corrected": "wireless"}],
  "attributes": {
    "hard_filters": {"gender": "men", "size": "XL"},
    "boosts": {"color": "blue", "material": "cotton"}
  },
  "synonyms": ["v-neck shirt", "vneck tshirt"],
  "original_query": "blue cotton v-neck t-shirt men XL",
  "processed_query": "v neck t-shirt"
}
```

Retrieval consumes this object, not the raw string. This separation makes it possible to:
- Log which pipeline stages fired (debuggability)
- A/B test individual stages in isolation
- Override specific fields via merchandising rules without re-running the full pipeline

---

## Debugging Checklist

When search results are wrong, trace through the pipeline stages in order:

1. **Check the structured query object** — log it for the failing query. What did each stage produce?
2. **Spell correction misfired?** — verify the corrected form is what the user intended. Check if the brand allowlist is missing an entry.
3. **Wrong intent?** — if `category_browse` was returned for a specific product query, synonym expansion was skipped and retrieval may be wrong.
4. **Attribute extracted incorrectly?** — confirm the attribute table coverage. `"40"` might match size before it matches a price, or vice versa.
5. **Synonym introduced noise?** — temporarily disable expansion for the failing query; if results improve, the synonym is wrong.
6. **Retrieval still fails after correct structured query?** — the problem is in retrieval (field weights, index gaps), not query understanding. Stop debugging this pipeline.

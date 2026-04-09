# BIO Annotation Format and Guidelines

## What BIO Is

BIO (Beginning-Inside-Outside) is a token-level labeling scheme that encodes entity spans as a sequence of per-token tags. Each token gets exactly one tag:

| Tag | Meaning |
|-----|---------|
| `B-TYPE` | First token of an entity of TYPE |
| `I-TYPE` | Non-first token of an entity of TYPE |
| `O` | Not part of any entity |

`TYPE` is replaced by the entity class: `PER`, `ORG`, `LOC`, `DATE`, `MONEY`, etc.

This scheme converts the span-prediction problem into a sequence classification problem, which is what CRF, BiLSTM-CRF, and transformer models actually train on.

---

## Worked Example: Full Sentence

**Raw text:**
```
Tim Cook announced that Apple will open a new store in Taipei on March 15.
```

**Tokenized and labeled:**

```
Token       Tag
----------  ----------
Tim         B-PER
Cook        I-PER
announced   O
that        O
Apple       B-ORG
will        O
open        O
a           O
new         O
store       O
in          O
Taipei      B-LOC
on          O
March       B-DATE
15          I-DATE
.           O
```

**Rules demonstrated:**
- Multi-token spans: `Tim Cook` → `B-PER I-PER`, `March 15` → `B-DATE I-DATE`
- Single-token spans: `Apple` → `B-ORG`, `Taipei` → `B-LOC`
- Everything else: `O`

---

## BIO vs. BIOES vs. BILOU

BIO is the most common scheme but two extensions exist. Use them only if your toolchain explicitly supports them — mixing schemes between training and inference causes silent label errors.

| Scheme | Tags | Extra signal |
|--------|------|-------------|
| BIO | B, I, O | Baseline |
| BIOES | B, I, O, E, S | E = end of span; S = single-token span |
| BILOU | B, I, L, O, U | L = last; U = unit (single-token) |

**BIOES example** for `Tim Cook` and `Apple`:
```
Tim     B-PER
Cook    E-PER
Apple   S-ORG
```

BIOES/BILOU give the model a cleaner signal for span boundaries and often yield 0.5–1.5 F1 improvement on fine-grained entity types. Not worth the schema complexity for standard 4-class NER; potentially worth it for nested or fine-grained types.

---

## Annotation Decision Framework

When you face an ambiguous span, apply these rules in order:

### Rule 1: What is the minimal entity-bearing span?

Include only the tokens that are part of the named entity itself. Strip surrounding determiners, prepositions, and punctuation unless they are conventionally part of the name.

```
Correct:    [Apple]_ORG Inc.   →  B-ORG I-ORG O
Wrong:      [Apple Inc.]_ORG   →  B-ORG I-ORG I-ORG    ← include if "Inc." is part of the formal name
```

Decision: Is "Inc." part of the entity's registered name? If yes → include it. If it is just a generic suffix the annotator added → exclude.

Apply the same logic to titles:

```
"Dr. Jane Smith visited the lab."

Option A (title excluded):  O  B-PER I-PER O  O  O
Option B (title included):  B-PER I-PER I-PER O  O  O
```

**Pick one convention for your entire dataset and document it.** Inconsistency here is the most common cause of annotation noise. The SKILL.md iron law applies: inconsistent annotations directly degrade F1.

### Rule 2: Nested entities — take the outermost span

Standard BIO cannot represent nested entities. `Bank of America` contains both `ORG` (full span) and `LOC` (`America`). Default to the outermost entity.

```
Bank of America headquarters
B-ORG I-ORG I-ORG O
```

If nested NER is required, use a separate nested NER architecture (span-based models like SpERT). Do not try to shoehorn nesting into BIO — it breaks sequence labeling.

### Rule 3: Ambiguous type — use context, not surface form

`Jordan` can be PER, LOC, or even a brand. Tag based on the sentence context:

```
"Jordan scored 40 points."         →  B-PER  (athlete context)
"Exports to Jordan declined."      →  B-LOC  (country context)
"He wore Jordan sneakers."         →  O      (brand; only tag if ORG/BRAND is a defined type)
```

If context is genuinely ambiguous and annotators disagree, flag for adjudication rather than making an arbitrary choice.

### Rule 4: Abbreviations and acronyms

Tag abbreviations if the expanded form would be tagged:

```
"The WHO announced new guidelines."
B-ORG O  O  O
```

Do not expand the abbreviation. The model learns from surface tokens.

### Rule 5: Dates and numeric expressions

Tag only the portion of the expression that is the named temporal or numeric entity. Do not tag relative temporal expressions unless they are anchored to a named date.

```
"on March 15"         →  O B-DATE I-DATE
"last Tuesday"        →  O O         (relative; skip unless your schema includes it)
"Q3 2024"             →  B-DATE I-DATE
"$4.2 billion"        →  B-MONEY I-MONEY I-MONEY
"approximately $4B"   →  O B-MONEY   (skip the hedge; tag the value)
```

---

## Annotation File Format

### CoNLL-2003 format (standard)

One token per line, columns separated by whitespace. Sentence boundaries are blank lines.

```
-DOCSTART- -X- -X- O

Tim         NNP NNP B-PER
Cook        NNP NNP I-PER
announced   VBD VBD O
that        IN  IN  O
Apple       NNP NNP B-ORG
will        MD  MD  O
open        VB  VB  O
.           .   .   O

```

Column order (original CoNLL-2003): `TOKEN POS CHUNK NER`. For custom datasets you can use two columns: `TOKEN NER`. What matters: NER tag is always the last column.

### JSON Lines format (for Hugging Face)

```jsonl
{"tokens": ["Tim", "Cook", "announced", "Apple"], "ner_tags": ["B-PER", "I-PER", "O", "B-ORG"]}
{"tokens": ["Taipei", "is", "a", "city"], "ner_tags": ["B-LOC", "O", "O", "O"]}
```

Use `datasets.ClassLabel` to map string tags to integers before training:
```python
label_list = ["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC", "B-DATE", "I-DATE"]
```

---

## Minimum Viable Annotation Checklist

Before sending annotation data to training:

- [ ] Label set defined and documented (every annotator uses same TYPE names, same capitalization)
- [ ] Guideline decisions written down: titles in/out, nested entities policy, ambiguous types resolved how
- [ ] At least 200 sentences per entity type (aim for 500+ for rarer types)
- [ ] Train / dev / test split: 70 / 15 / 15, split at document level (not sentence level to prevent leakage)
- [ ] Inter-annotator agreement (IAA) computed on 10% overlap; Cohen's κ > 0.80 before proceeding
- [ ] BIO validity check run (no `I-TYPE` without preceding `B-TYPE` of same TYPE)

---

## BIO Validity Check (Python)

A common annotation tool bug or annotator error is emitting an `I-TYPE` as the first token of a sentence, which is illegal in BIO.

```python
def validate_bio(tags: list[str]) -> list[str]:
    """Returns list of error strings. Empty list = valid."""
    errors = []
    prev = "O"
    for i, tag in enumerate(tags):
        if tag.startswith("I-"):
            entity_type = tag[2:]
            if prev == "O" or (prev.startswith("B-") and prev[2:] != entity_type) or \
               (prev.startswith("I-") and prev[2:] != entity_type):
                errors.append(f"Token {i}: illegal '{tag}' after '{prev}'")
        prev = tag
    return errors

# Example
tags = ["B-PER", "I-PER", "I-ORG", "O"]  # I-ORG after I-PER is illegal
print(validate_bio(tags))
# ["Token 2: illegal 'I-ORG' after 'I-PER'"]
```

Run this check on every annotation file before training. Models trained on invalid BIO silently learn wrong boundaries.

---

## Inter-Annotator Agreement

For a 10% overlap subset annotated by two annotators, compute Cohen's κ at the token level:

```
κ = (P_o - P_e) / (1 - P_e)

P_o = observed agreement rate (fraction of tokens where both agree on same tag)
P_e = expected agreement by chance = Σ_tag (p_A(tag) × p_B(tag))
```

**Interpretation:**

| κ | Quality |
|---|---------|
| > 0.80 | Sufficient for training |
| 0.67–0.80 | Marginal; revisit guidelines for disagreement types |
| < 0.67 | Annotation guidelines are ambiguous; stop and fix |

When κ is low, categorize disagreements by type:

1. **Boundary disagreement**: annotators agree an entity exists but differ on span (e.g., one includes "Inc.", other doesn't) → fix in guidelines
2. **Type disagreement**: both tag the span but assign different TYPE → fix TYPE definitions with examples
3. **Existence disagreement**: one annotator tags, other does not → often a guideline gap on edge cases

---

## Annotation Volume vs. F1 (Empirical Benchmarks)

Fine-tuning BERT-base on domain data:

| Annotated examples | Expected F1 (domain test) |
|-------------------|--------------------------|
| 50–100 | 55–65% |
| 200–500 | 70–80% |
| 1,000+ | 80–88% |
| 5,000+ | 88–93% |

These are rough benchmarks. The SKILL.md iron law applies here: if your domain is far from the pre-trained model's training data (e.g., medical entities vs. news-trained model), you need more data to reach the same F1.

For low-resource situations, consider:
1. **Few-shot NER**: GLiNER, SpanMarker with in-context examples
2. **Weak supervision**: generate noisy labels with gazetteers, clean with Snorkel
3. **Active learning**: annotate only the sentences the model is most uncertain about

---

## Common Annotation Mistakes and Fixes

| Mistake | Example | Fix |
|---------|---------|-----|
| Tagging pronouns | "He said..." → B-PER | Never tag pronouns; tag only the referent if it appears |
| Partial spans | "New" instead of "New York City" | Span must cover the complete entity name |
| Over-tagging common nouns | "the bank" → B-ORG | Named entities only; "the bank" is a common noun |
| Inconsistent title inclusion | "Dr. Smith" sometimes B-PER, sometimes I-PER | Write guideline, re-annotate for consistency |
| I- without B- | Sentence starts with I-PER | BIO violation; always start a span with B- |
| Different TYPE names | `PERSON` vs `PER` vs `per` | Standardize at start; a mismatch causes silent training errors |

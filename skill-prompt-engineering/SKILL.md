---
name: "skill-prompt-engineering"
description: "Design effective LLM prompts using structured techniques including few-shot, chain-of-thought, role-playing, and output format control. Use this skill when the user needs to improve AI output quality, design system prompts, build LLM-powered features, or debug why an AI gives bad responses — even if they say 'the AI gives wrong answers', 'how do I write better prompts', 'build an AI feature', or 'why does ChatGPT keep making this mistake'."
metadata:
  category: "WP-11 通用技術"
  tags: ["technology", "prompt-engineering", "llm", "ai"]
---

# Prompt Engineering

## Framework

```
IRON LAW: Be Specific, Structured, and Show Examples

Vague prompt → vague output. The LLM does not read your mind.
"Write something good" → garbage.
"Write a 200-word product description for [product], targeting [audience],
emphasizing [benefit], in a [tone] tone. Follow this template: [template]" → quality.

Specificity, structure, and examples are the three levers.
```

### Core Techniques

| Technique | What It Does | When to Use |
|-----------|-------------|------------|
| **Role/Persona** | "You are a senior tax accountant..." | Domain-specific tasks, tone control |
| **Few-shot examples** | Provide 2-3 input→output examples | Format control, pattern matching |
| **Chain-of-thought** | "Think step by step..." or "Show your reasoning" | Complex reasoning, math, logic |
| **Output format** | "Respond in JSON/Markdown/Table format" | Structured data extraction, API responses |
| **Constraints** | "Maximum 100 words", "Only use information from the text" | Length control, hallucination reduction |
| **System prompt** | Set persistent behavior and rules | Application-level prompt design |

### Prompt Structure Template

```
[ROLE] You are a {role} with expertise in {domain}.

[CONTEXT] The user is {situation}. They need {what}.

[TASK] {Specific instruction with clear deliverable}

[FORMAT] Respond in the following format:
{Template or structure}

[CONSTRAINTS]
- {Constraint 1}
- {Constraint 2}

[EXAMPLES] (few-shot)
Input: {example input}
Output: {example output}
```

### Output Format Control

| Desired Output | Technique |
|---------------|-----------|
| JSON | "Respond with valid JSON matching this schema: {...}" |
| Markdown table | "Format as a markdown table with columns: X, Y, Z" |
| Bullet list | "List as bullet points, maximum 5 items" |
| Specific length | "In exactly 3 sentences" or "Under 200 words" |
| Classification | "Classify as one of: [A, B, C]. Output only the label." |

### Prompt Debugging

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Output too verbose | No length constraint | Add "Be concise. Maximum X words." |
| Output hallucinated facts | No grounding constraint | "Only use information from the provided text. Say 'I don't know' if unsure." |
| Output ignores instructions | Instructions buried in long prompt | Move critical instructions to the START and END of the prompt |
| Output format wrong | No format specification or example | Add explicit format template + 1 example |
| Inconsistent outputs | Temperature too high or prompt too ambiguous | Lower temperature, add more specific instructions |

### System Prompt Design (for Applications)

```
[Identity] You are {role} for {application}.

[Behavior rules]
- Always {do X}
- Never {do Y}
- When unsure, {default behavior}

[Output rules]
- Format: {JSON/Markdown/etc.}
- Language: {always respond in user's language}
- Length: {concise/detailed depending on query}

[Safety]
- Do not {restricted action}
- If asked about {sensitive topic}, respond with {safe response}
```

### Context Window Management

| Strategy | How | When |
|----------|-----|------|
| **Truncation** | Keep most recent N tokens | Chat applications |
| **Summarization** | Summarize old context, keep recent | Long conversations |
| **RAG** | Retrieve relevant context from a database | Knowledge-intensive tasks |
| **Chunking** | Split large documents into overlapping chunks | Document analysis |

## Output Format

```markdown
# Prompt Design: {Use Case}

## Task Definition
- Input: {what the user provides}
- Output: {what the AI should produce}
- Quality criteria: {what "good" looks like}

## Prompt
```
{The complete prompt}
```

## Test Cases
| Input | Expected Output | Actual Output | Pass? |
|-------|----------------|--------------|-------|
| {test 1} | {expected} | {actual} | ✓/✗ |

## Iteration Notes
- V1: {what was tried, what went wrong}
- V2: {what was changed, result}
```

## Gotchas

- **Prompt injection is a real security threat**: If user input is concatenated into a prompt, users can override your instructions. Sanitize inputs and use system prompts for rules.
- **Temperature affects consistency**: Temperature 0 = deterministic (same input → same output). Temperature 1 = creative but unpredictable. Use 0-0.3 for factual tasks, 0.7-1.0 for creative tasks.
- **Models have recency bias**: Instructions at the beginning and end of a long prompt get more attention than the middle. Put critical rules at both start AND end.
- **Few-shot examples set the pattern**: If all your examples show long responses, the model will produce long responses even if you say "be concise." Examples override instructions.
- **Different models need different prompts**: A prompt optimized for GPT-4 may not work well for Claude or Gemini. Test across models if you need portability.

## References

- For RAG (Retrieval-Augmented Generation) architecture, see `references/rag-guide.md`
- For prompt injection prevention, see `references/prompt-security.md`

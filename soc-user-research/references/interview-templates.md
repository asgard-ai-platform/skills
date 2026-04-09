# Interview Templates

Concrete discussion guides for depth interviews. Adapt the structure to your project; treat question wording as defaults, not scripts.

---

## Structure of a 45-Minute Interview

```
Phase          Duration   Purpose
─────────────────────────────────────────────
Warm-up        3 min      Build rapport, lower defenses
Context scan   7 min      Map their world, surface relevant episodes
Core probing   25 min     Follow the most promising threads
Concept probe  5 min      Optional: react to your product/prototype
Wrap-up        5 min      Confirm understanding, close loops
```

The 25-minute core is not scripted — it follows what the participant said in the context scan. Every guide below reserves that space for follow-up branching.

---

## Template 1 — Understanding a Pain Point (General)

Use when: You know the domain but haven't identified the specific friction.

```
SCREENING CRITERIA (before the interview)
  - Has done [target task] at least once in the last 60 days
  - Is the primary decision-maker, not a delegate
  - NOT a power user (>10x/week) if you want mainstream behavior

WARM-UP (3 min)
"Before we start — can you tell me a bit about what you do day-to-day?
 Just the broad strokes."

  Goal: get them talking; listen for vocabulary they'll use later.

CONTEXT SCAN (7 min)
"I'd like to understand a specific time when you had to [do the task].
 Can you think of a recent example — ideally in the last month or so?"

  → "Walk me through what happened, from the very beginning."
  → Let them narrate without interruption. Note every friction word:
    "annoying", "I had to", "I always", "I hate it when", "usually".

CORE — EPISODE RECONSTRUCTION (25 min)
Pick 2-3 friction words from their narrative and probe each:

  Probe A — Reconstruct the moment:
  "You mentioned [friction word]. Can you take me back to that moment?
   What were you doing right before that?"

  Probe B — Emotional temperature:
  "When that happened, how did you feel? What was going through your mind?"

  Probe C — Workaround detection:
  "What did you end up doing instead?"
  "Is that what you always do, or just that time?"

  Probe D — Frequency and severity calibration:
  "How often does this happen?"
  "On a scale of annoyance — is it a mild inconvenience or does it
   actually stop you from getting things done?"

  Probe E — Root cause ladder (5 Whys style):
  "Why do you think it works that way?"
  → Keep asking "Why do you think that is?" until they say "I don't know"
    or you hit a system-level constraint.

WRAP-UP (5 min)
"Before we close — is there anything about [topic] that you thought
 we'd talk about but didn't?"
"If you could change one thing about [current solution], what would it be?"
"Is there anyone else you'd suggest I talk to who experiences this differently?"
```

---

## Template 2 — Validating a Problem Statement

Use when: You have a hypothesis ("users struggle with X because Y") and need to confirm or disconfirm it.

The **IRON LAW** applies here: do not ask "Does this problem sound familiar?" That's leading. Ask about episodes, then judge whether the problem appears.

```
HYPOTHESIS (write this before the interview, not during)
  "We believe [segment] struggles with [task] because [root cause],
   which leads them to [workaround or failure mode]."

  Example:
  "We believe freelance designers struggle with client feedback because
   clients give vague verbal comments rather than annotated files, which
   leads designers to do multiple revision rounds."

WARM-UP (3 min)
Standard rapport questions about role and day-to-day.

CONTEXT SCAN (7 min)
"Tell me about the last time you worked with a client on a design revision.
 Who was the client, roughly, and what was the project?"

  → Deliberately broad. Let them choose the episode.

CORE — HYPOTHESIS TEST (25 min)

  Segment 1 — Task description (does their version of the task match yours?)
  "How does the feedback process typically work for you?
   Walk me through it from when you deliver work to when you get comments."

  Segment 2 — Pain discovery (does your hypothesized cause appear?)
  "What's the most frustrating part of that process for you?"
  → If they DON'T mention your hypothesized cause: probe gently once.
    "Some designers I've talked to mention [vague verbal feedback] as an
     issue — is that something you've experienced?"
    (This is the only time you can name a hypothesis — after exhausting
     open-ended probing. Note in your analysis that you prompted it.)

  Segment 3 — Workaround confirmation (does the failure mode appear?)
  "When you get feedback that's hard to act on, what do you do?"
  → Compare to your hypothesized workaround.

  Segment 4 — Severity (is this important enough to build for?)
  "How much of your project time would you say goes into the feedback loop?"
  "Has this ever caused you to lose a client, or almost lose one?"
  "If this problem disappeared tomorrow, what would be different for you?"

WRAP-UP (5 min)
Standard closing. Then privately note:
  □ Did the hypothesized cause appear without prompting?
  □ Did the hypothesized workaround appear?
  □ How severe did they rate it (in their own words)?
```

### Scoring Hypothesis Interviews

After N interviews, tally:

| Signal | Count | Threshold |
|---|---|---|
| Cause appeared unprompted | — | ≥ 6/10 → hypothesis holds |
| Cause appeared only after prompt | — | Doesn't count as confirmation |
| Workaround appeared | — | ≥ 5/10 → behavioral evidence |
| Severity: "it costs me time/money/clients" | — | ≥ 4/10 → worth building |

If hypothesis fails (cause not mentioned unprompted by most participants): do not pivot your hypothesis mid-study. Finish the study. The real pain will emerge from what they DO mention unprompted.

---

## Template 3 — Mental Model Interview

Use when: You're designing onboarding, IA, or anything that depends on how users think about a domain.

```
GOAL
  Surface the participant's internal model of [domain] — the categories
  they use, the causal chains they believe in, the vocabulary they reach for.

WARM-UP (3 min)
"Tell me how long you've been dealing with [domain] and what role you play."

CONTEXT SCAN — VOCABULARY CAPTURE (7 min)
"If you were explaining [domain] to a new colleague from scratch,
 how would you describe it? What are the main pieces?"

  → Do not supply categories. Map what they say.
  → Write down every noun they use (these are their objects/entities).
  → Write down every verb they use (these are their actions/relationships).

CORE — MODEL EXCAVATION (25 min)

  Segment 1 — Categories
  "You mentioned [noun A] and [noun B]. Are those the same thing or
   different? How?"
  "Where does [noun C] fit — is it part of [noun A], separate, or
   something else entirely?"

  Segment 2 — Causality
  "When [event X] happens, what do you expect to happen next?"
  "If [noun A] is wrong, what breaks?"

  Segment 3 — Exception cases
  "Is there a situation where the usual process doesn't apply?
   What do you do then?"
  "What's the weirdest thing that's ever happened with [domain]?
   How did you figure it out?"

  Segment 4 — Metaphor probe (optional, powerful)
  "If you had to compare [domain] to something else — a machine,
   a relationship, a system you know well — what would it be?"
  → Metaphors reveal the deep structure of their mental model.

WRAP-UP (5 min)
"I want to check my understanding. You're saying [summarize their model
 in 3 sentences]. Is that right? What am I missing?"
  → Intentionally leave a gap. See if they correct it.
```

### Mental Model Map (Post-Interview Artifact)

After each interview, sketch:

```
[Entity A] ──causes──> [State B]
     │
     └──part-of──> [Category C]

[Event X] ──triggers──> [Action Y] ──resolves──> [Entity A]
```

After 5+ interviews: overlay the maps. Where entities and arrows cluster, you have shared mental model. Where they diverge, you have a design problem.

---

## Template 4 — Jobs-to-Be-Done (JTBD) Interview

Use when: You're early in product discovery and need to understand functional, social, and emotional jobs.

Based on the Christensen/Moesta JTBD interview structure. The goal is to reconstruct the **purchase moment** (or first-use moment), not the general use pattern.

```
SCREENING
  Recruit people who have recently made a relevant decision/switch —
  ideally in the last 3-6 months. Recency matters: details fade.

WARM-UP (3 min)
"When did you [first use / switch to / buy] [product or category]?
 I want to focus on that specific moment."

TIMELINE RECONSTRUCTION (10 min)
"Let's go back to that day. Where were you? What were you doing right
 before you decided to [make the switch]?"

  → Reconstruct the scene in physical detail: location, who was there,
    time of day. This anchors memory.

"What made that the moment you decided, versus earlier or later?"

  → Probe for the trigger — what changed in their life/context that
    created the push.

PUSH/PULL FORCES (20 min)

  Push (forces away from the old situation):
  "What was frustrating about how you were handling it before?"
  "Was there a moment when you said 'that's it, something has to change'?"
  "What were you giving up by keeping the old approach?"

  Pull (forces toward the new solution):
  "What made [product/solution] seem like it might work for you?"
  "When you imagined using it, what did you picture your life being like?"
  "What was the promise it made — even if implicitly?"

  Anxiety (forces holding back the switch):
  "What almost stopped you from making the switch?"
  "What were you worried might go wrong?"
  "Did you try anything else first?"

  Habit (inertia of the old solution):
  "What did you have to stop doing when you made the switch?"
  "Was there anything you missed about the old way?"

FUNCTIONAL / SOCIAL / EMOTIONAL JOBS (5 min)

  "When you think about why you made this change, is it mostly practical,
   or does it matter what other people think, or how it makes you feel?"

  → Don't force categories. Their answer will reveal which job type dominates.

WRAP-UP (5 min)
Standard closing.
```

### JTBD Force Map (Post-Interview)

```
PUSH                         PULL
─────────────────────────────────────────────
What was broken/frustrating  What the new solution promised
─────────────────────────────────────────────
"It always crashed at month-  "It said it would sync
end close"                    automatically"

ANXIETY                      HABIT
─────────────────────────────────────────────
What created hesitation      What they had to give up
─────────────────────────────────────────────
"I wasn't sure if it would   "I'd been using Excel for
import our old data"          10 years, knew every shortcut"
```

After 8+ interviews: count how often each force type appears. The dominant forces are your real competition and your real value proposition.

---

## Probing Question Bank

Keep these in your working memory during any interview. Do not read them aloud — internalize them and deploy naturally.

### Go Deeper
- "Tell me more about that."
- "What do you mean by [their word]?"
- "Can you give me an example?"
- "What happened right before that?"
- "What happened next?"

### Get Emotional Temperature
- "How did you feel when that happened?"
- "What was going through your mind?"
- "Was that a big deal, or minor?"

### Detect Workarounds
- "What did you end up doing?"
- "Is that what you always do?"
- "How long have you been doing it that way?"

### Calibrate Frequency
- "How often does this come up?"
- "In the last month, how many times?"

### Detect Social Context
- "Who else is involved when this happens?"
- "What do other people around you do?"

### Challenge Self-Report (gently)
- "You mentioned you usually do X — can you think of the last specific time? What actually happened?"
- "Has there ever been a time when you didn't do it that way?"

### Questions to NEVER Ask
- "Would you use this if we built it?" → hypothetical, unreliable
- "Do you think this is a problem?" → leading
- "Don't you find it annoying when...?" → leading
- "What features would you want?" → users are not designers
- "On a scale of 1-10, how much do you care about X?" → numeric ratings on abstract concepts are noise

---

## Interviewer Calibration Checklist

Run this before your first session and after every session where something felt off.

```
BEFORE THE INTERVIEW
  □ Screener confirmed participant meets criteria
  □ Recording consent obtained (verbal or written)
  □ Note-taker assigned or recording confirmed working
  □ Discussion guide reviewed but NOT memorized verbatim
  □ Hypothesis written down and set aside (don't bring it in)

DURING THE INTERVIEW
  □ Silence used at least 3 times (let them fill gaps)
  □ No "great!", "perfect!", or "interesting!" after their answers
    (neutral reactions only: "mm-hmm", "I see", "okay")
  □ No hypothetical questions asked
  □ Followed their thread, not the guide's order
  □ At least one 5-Whys chain attempted

AFTER THE INTERVIEW
  □ Debrief with note-taker within 30 minutes while memory is fresh
  □ 3 strongest quotes written down verbatim
  □ 1 thing that surprised you written down
  □ Hypothesis status updated: appeared / didn't appear / unclear
```

---

## Note-Taking Format (During Interview)

Use a two-column format: verbatim quotes on the left, your interpretation on the right. Keep them separate — conflation is the primary source of analysis error.

```
VERBATIM                          | INTERPRETATION
──────────────────────────────────┼─────────────────────────────────
"I always just export it to       | Workaround: exports to avoid
 Excel and do it there because    | in-app limitations. Frequency:
 the filters never work right"    | "always" = habitual, not one-off

"My manager asks for it every     | Social job: visibility to manager
 Monday and I have no idea        | is the actual deliverable, not
 what she's going to do with it"  | the task itself
```

Aim for 15-20 verbatim quotes per 45-minute interview. If you have fewer than 10, you paraphrased too much.

---

## After N Interviews: When to Stop

| Observation | Action |
|---|---|
| Last 2 interviews added zero new themes | Stop. You've hit saturation. |
| 70%+ of participants use the same words for a pain point | You have a real finding. |
| Every new interview adds new themes | You have a sampling problem (too heterogeneous). Narrow the segment. |
| Findings contradict each other sharply | Segment the data. Two user types may be mixed. |

Saturation is not "I've done 15 interviews." It's "the last two gave me nothing new." A homogeneous, well-screened sample often saturates at 8. A mixed sample may never saturate.

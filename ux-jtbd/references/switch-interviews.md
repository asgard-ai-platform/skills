# Switch Interviews

Switch interviews reconstruct the exact moment a customer decided to change solutions — what they were doing, thinking, and feeling from the first hint of dissatisfaction to the first use of the new product. Unlike standard user interviews that ask "what do you need?", switch interviews ask "tell me the story of when you switched."

The technique was developed by Bob Moesta and Chris Spiek as an operational method for uncovering JTBD forces of progress. The output is a timeline — called the **timeline of events** — that maps the four forces to specific moments in the customer's decision journey.

---

## The Core Assumption

Customers don't wake up one day and switch. The decision accumulates over weeks or months. The switch interview reconstructs that accumulation, not just the final moment of purchase. Every data point — when they first "thought maybe", when they first searched, when they finally bought — is a signal about which force dominated at that moment.

---

## Who to Interview

**Include:**
- People who have switched TO your product in the last 90 days (recent memory, emotional recall intact)
- People who switched AWAY from your product (churned customers reveal unmet jobs you failed)
- People who evaluated your product and chose a competitor instead

**Exclude:**
- People who haven't decided yet (no switch event to reconstruct)
- People describing an imagined or hypothetical future purchase
- People who were bought for (e.g., IT-mandated software with no personal choice)

**Sample size**: 6–10 interviews per distinct customer segment usually saturates the pattern. Stop when you hear the same timeline structure 3–4 times in a row.

---

## Interview Structure

The interview has four phases. Total time: 45–60 minutes.

### Phase 1: Anchor the Switch Event (5 min)

Start at the moment of purchase/switch. This grounds the timeline.

> "Tell me about the day you actually signed up / bought / switched. Where were you? What did you do right before?"

Do not ask why yet. You're looking for the concrete event, not their explanation of it.

### Phase 2: Walk Backward — First Thought (15 min)

Push back in time to find the first signal of dissatisfaction.

> "Think back further — when did you first have the thought that maybe you needed something different? What was happening at that time?"

Probe for:
- The specific situation (not "I was at work" — "I was trying to do X and Y kept happening")
- Who else was present
- What they were using at the time and what was frustrating about it

This phase surfaces **Push** and **Habit**:
- Push: "every time I tried to X, I had to manually Y"
- Habit: "I'd been doing it that way for two years, I just kept trying to work around it"

### Phase 3: Walk Forward — The Search (15 min)

Move from the first thought to the purchase, step by step.

> "After that first moment — what did you do next? Did you start looking around? How did you find [your product]?"

Probe for:
- What triggered the actual search (the "passive looking" vs "active looking" transition)
- What alternatives they considered
- What caused them to discard alternatives

This phase surfaces **Pull** and **Anxiety**:
- Pull: "I saw a demo and the interface looked so much cleaner"
- Anxiety: "I was worried about migrating all my old data"

### Phase 4: First Use and After (10 min)

> "What happened the first time you used it? Was there a moment you knew it was the right call?"

This reveals whether the job was actually done or just attempted. Buyers can switch but still fail to make the progress they wanted.

---

## Timeline Template

Draw this during or after each interview. Fill in actual quotes from the customer.

```
TIMELINE OF EVENTS

[First Thought]          [Passive Looking]     [Active Looking]      [Decision]           [First Use]
     ↓                         ↓                     ↓                    ↓                    ↓
"I noticed that          "Started looking       "Evaluated 3          "Bought on            "First time I
every Monday            around but             options, eliminated    Tuesday after         used it, I
morning our             didn't act yet"        A because of X,       seeing Y's demo"      realized Z
standup ran long                               B because of Y"                             still wasn't
and nobody had                                                                             solved"
a clear view"

PUSH operating here ──────────────────────┐
                                           ↓
HABIT resisting here ──────────────────────────────────┐
                                                        ↓
PULL appears here ──────────────────────────────────────────────────┐
                                                                      ↓
ANXIETY slowing here ──────────────────────────────────────────────────────┐
```

---

## Question Bank by Force

Use these probes when a customer gives a surface-level answer.

### Push (dissatisfaction with current solution)

- "What was the last straw? Was there a specific incident?"
- "How long had that been bothering you before you did something about it?"
- "What workarounds were you using? How often?"
- "If that frustration weren't there, would you have switched?"

### Pull (attraction toward new solution)

- "What was the first thing that made you think [product] might work?"
- "When you saw it, what specifically stood out?"
- "Was there a moment where you thought 'this could solve my problem'?"

### Anxiety (fear of new solution)

- "Was there anything about switching that worried you?"
- "Did you hesitate before buying? What gave you pause?"
- "What would have happened if the switch didn't work out?"

### Habit (comfort of current solution)

- "How long had you been using your previous solution?"
- "What would you have lost if you left it?"
- "Did you try to fix the problem within the old system before switching?"

---

## Worked Example: Notion vs. Google Docs

**Interview subject**: Marketing manager at a 40-person startup who switched from Google Docs to Notion six weeks ago.

**Phase 1 — Anchor**:
> "I signed up on a Sunday evening. I'd just had a really frustrating Friday and spent the weekend thinking about it."

**Phase 2 — First Thought (walk back)**:
> "The frustration had been building for months actually. Every project we ran had docs scattered everywhere — brief in one folder, feedback in another, the final version somewhere else. I'd spend 15 minutes at the start of every meeting just finding the right doc."

Push emerging: "finding the right doc" is a recurring task failure. Not a one-time event.

> "I'd tried creating a shared drive structure, even made a README explaining how to organize things. Nobody followed it. I gave up trying to fix it and just accepted it as the way things were."

Habit: had already attempted a fix within the old system and failed. Accepted the failure state. Note the word "just accepted" — this is the customer in passive mode.

**Phase 3 — Search (walk forward)**:
> "My designer mentioned Notion in passing — she was using it for design specs. I looked at it briefly but didn't really dig in. Then two weeks later I was at a conference and someone showed me how their team used it for project wikis. That was when I started actually thinking about it seriously."

Two-step Pull: first a weak signal (heard from designer), then a stronger demonstration (conference). The conference converted "passive looking" to "active looking."

> "What held me back was honestly just time. I thought the migration would take forever."

Anxiety: migration cost, not product doubt. This is a common pattern — the product is desired, but the switching cost creates anxiety.

**Phase 4 — First Use**:
> "The first week was rough honestly. I set it up wrong and had to redo the structure. But by week two when I was in a meeting and pulled up the project page in 10 seconds, I knew it was worth it."

Job partially confirmed but delayed. The confirmation happened at second use, not first.

---

**Forces Summary for this interview**:

| Force | Evidence | Strength |
|-------|----------|----------|
| Push | Docs scattered, 15 min per meeting finding files, failed internal fix attempts | Strong — chronic, not one-off |
| Pull | Designer mention (weak), conference demo (strong) | Moderate — needed demonstration to activate |
| Anxiety | Migration time cost | Moderate — delayed switch by ~2 weeks |
| Habit | Accepted failure state, had built workarounds | Weak — had already tried and given up on the old system |

**Job statement derived**:
> "When I'm running a project with a distributed team, I want one place where everything lives in context, so I can find what I need without hunting and look competent in front of stakeholders."

---

## Coding Interviews for Patterns

After 6+ interviews, code each timeline for force patterns. Use a simple table:

| Interview | Primary Push | Primary Pull | Anxiety | Habit Strength | Switch Trigger |
|-----------|-------------|-------------|---------|---------------|----------------|
| 1 | Fragmented docs | Conference demo | Migration cost | Weak | Demo at conference |
| 2 | Missed deadlines | Friend referral | Team adoption | Medium | Specific incident (missed launch) |
| 3 | ... | ... | ... | ... | ... |

Look for:
- **Recurring Push patterns**: these are the jobs you're actually being hired for
- **Dominant anxiety type**: if migration anxiety appears 6/8 times, address it with onboarding
- **Switch trigger type**: passive (word of mouth) vs. active (searched for solution) tells you where acquisition investment pays off

---

## What Switch Interviews Cannot Tell You

- **Non-switchers**: people who considered you and stayed with the competitor are invisible in switch interviews. Complement with "close-lost" interviews (why they chose the competitor) and churned-customer interviews (why they left you).
- **B2B multi-stakeholder decisions**: the person who switched is not always the person who experienced the problem. In enterprise sales, reconstruct multiple timelines — the user's and the buyer's.
- **Aggregate quantitative data**: switch interviews are qualitative. They generate hypotheses about which forces dominate. Test with surveys if you need numbers.

---

## Anti-Patterns

**Leading with "why"**: "Why did you switch?" triggers post-hoc rationalization. Customers will give you a clean narrative that wasn't how the decision actually felt. Instead: "Walk me through what happened."

**Stopping at the purchase**: The job may or may not have been done after the switch. Always ask about first use. A customer who switched but still failed is churned within 60 days.

**Confusing features with jobs**: If a customer says "I switched because of the kanban board", that's a feature. The job is still hidden. Ask: "What were you trying to do that the kanban board helped with?"

**Treating job statements as stable across segments**: Two customers can use the same product for completely different jobs. A Notion user who switched from Google Docs for "project organization" has a different job than one who switched for "personal knowledge management." Separate segments, separate job stories.

# Design Thinking Facilitation Exercises

One exercise per stage, chosen for being underused but high-yield. Each entry includes: setup, step-by-step procedure, time box, materials, and a worked example so facilitators know what good output looks like.

---

## Stage 1 — Empathize: Fly-on-the-Wall + Five Whys Interview

### When to use
You have access to users in their natural context (a workplace, a waiting room, a shop floor). Use this before any interviews to surface behaviors users can't articulate.

### Setup
- **Team size**: 2 observers per user (one watches, one takes notes)
- **Duration**: 45–90 min observation + 30 min debrief
- **Materials**: field notes template (see below), a timer, a camera if permitted

### Observation Protocol

**Field Notes Template**

```
Observer:          ___________
User ID (anon):    ___________
Location:          ___________
Time:              ___________

WHAT I SEE (behavior, actions, sequence of steps)
→

WHAT I HEAR (exact quotes, fragments)
→

WHAT I SENSE (body language, emotional cues, workarounds)
→

SURPRISES (things I didn't expect)
→
```

Do not interpret during observation. Write only what happens, not what you think it means.

### Five Whys Follow-Up

After observing a behavior that seems inefficient or emotional, run a structured Five Whys to reach the root need. Do not literally ask "why?" five times — that feels interrogative. Use softer pivots:

| Why iteration | Pivot phrase |
|---|---|
| 1 | "What made you do that?" |
| 2 | "What happens if you don't?" |
| 3 | "Has it always worked this way?" |
| 4 | "What would make that easier?" |
| 5 | "What would need to be true for that to not be a problem?" |

### Worked Example

**Context**: Observing nurses in a hospital medication room.

| Iteration | Observation / Answer |
|---|---|
| Behavior | Nurse writes patient name on a Post-it and sticks it to the medication cup. |
| Why 1 | "Because by the time I walk to room 4, I forget which patient it was for." |
| Why 2 | "If I give it to the wrong patient it's a serious error." |
| Why 3 | "The cart labels fell off last year. We've done this ever since." |
| Why 4 | "A permanent label on the cup before I fill it." |
| Why 5 | "The cart would need to print labels at point of preparation." |

**Insight extracted**: The nurse's workaround reveals a latent need for *point-of-preparation labeling*, not just better memory or better walking speed.

### Common Mistakes
- Asking users to explain WHY they do something during observation (breaks naturalistic behavior)
- Stopping at Why 2 ("they're forgetful") instead of reaching the systemic root
- Noting interpretations ("user was frustrated") without noting the evidence ("user sighed, restarted the form three times")

---

## Stage 2 — Define: POV + HMW Card Sort

### When to use
After collecting empathy data from multiple users, you have a pile of insights but no agreed-upon problem statement. This exercise forces convergence.

### Setup
- **Team size**: 3–6 people
- **Duration**: 60–90 min
- **Materials**: sticky notes (3 colors: blue = user, yellow = need, pink = insight), a whiteboard, dot stickers for voting

### Step-by-Step

**Step 1 — Dump (10 min)**
Each team member silently writes one insight per sticky, using only observations from the field. No editorializing. Stick all notes randomly on the board.

**Step 2 — Cluster (15 min)**
Group related notes. Name each cluster with a one-line theme. Aim for 4–8 clusters.

**Step 3 — Select the tension cluster (5 min)**
Identify the cluster with the most surprising or contradictory findings. This is usually where the real problem lives. Dot-vote if needed.

**Step 4 — Draft POV statements (15 min)**
Each person writes a POV statement from the tension cluster using the template:

```
[User type] needs to [verb phrase describing need]
because [non-obvious insight — not just "they said so"].
```

The `because` clause must contain an insight, not a restatement of the need.

| Valid | Invalid |
|---|---|
| "…because uncertainty amplifies anxiety beyond what the actual wait causes." | "…because they want to know how long they'll wait." |
| "…because trust is established through smell and texture before price." | "…because they care about product quality." |

**Step 5 — Vote and stress-test (10 min)**
Each team member dots their preferred POV. Read the top 2 aloud and ask:
- Does this exclude something important?
- Would a solution to this POV make users' lives measurably better?
- Is the insight surprising enough that we needed research to find it?

**Step 6 — HMW conversion (15 min)**
Take the winning POV and generate How Might We questions by systematically adjusting scope:

| Adjustment | HMW from hospital example |
|---|---|
| Amplify the good | How might we make the moments of clarity feel even more reassuring? |
| Remove the bad | How might we eliminate the period of total uncertainty? |
| Explore the opposite | How might we make waiting feel like an active, engaged experience? |
| Question the constraint | How might we redesign the process so waiting doesn't happen at all? |
| Change the actor | How might the waiting room itself communicate wait status? |

Generate at least 5 HMW questions. Post them all. They become the brief for Ideation.

---

## Stage 3 — Ideate: Crazy 8s + Concept Poster

### When to use
You have your HMW questions and need to generate a large volume of ideas quickly before converging on 2–3 concepts worth prototyping.

### Crazy 8s (Diverge)

**Setup**
- One sheet of A4 per person, folded into 8 panels
- One HMW question selected as the prompt
- Timer: 8 minutes (1 min per panel)

**Rules**
1. Draw or write one idea per panel. No words-only panels if you can sketch.
2. No explaining your ideas during the 8 minutes.
3. Include bad ideas. Quantity is the point.
4. Each panel must be a different idea — no iterating on panel 1 in panel 2.

**Debrief (5 min per person)**
Each person presents their 8 panels in 2 minutes. Team dots their top 2 per presenter. No criticism — only "I like this because..." or questions.

### Concept Poster (Converge)

After Crazy 8s, select the top 3–5 dotted ideas (from any participant's sheet). For each, one person drafts a Concept Poster in 10 minutes:

```markdown
## Concept: {short name}

**The idea in one sentence:**

**Who it's for:**

**How it works (3 steps max):**
1.
2.
3.

**Why it addresses the POV:**

**Biggest assumption this makes:**

**What could go wrong:**
```

The "Biggest assumption" field is critical — it becomes the hypothesis for the Prototype stage. If you can't name the assumption, the concept isn't concrete enough yet.

### Worked Example

**HMW**: How might we make the waiting room itself communicate wait status?

| Panel | Crazy 8 sketch |
|---|---|
| 1 | Large screen showing queue position (#14 of 20) |
| 2 | Color-coded wristband: green = <15 min, yellow = 15–30, red = 30+ |
| 3 | SMS when you're next |
| 4 | App that lets you leave and come back |
| 5 | Staff member does a 5-min loop and verbally updates |
| 6 | Ticket number + audio announcement |
| 7 | Ambient lighting that shifts from blue to warm as your turn approaches |
| 8 | Digital "your doctor is now seeing patient X" display |

**Concept Poster for panel 7 (ambient lighting):**

```
Concept: Warm Shift

One sentence: The waiting room lighting gradually warms from
blue-white to amber as a patient's estimated wait approaches zero.

Who it's for: Patients with high anxiety who find screens intrusive.

How it works:
1. Patient checks in; system estimates wait time.
2. Room's LED zones shift color over the wait window.
3. When lights reach full amber, patient approaches the desk.

Why it addresses the POV: Communicates status without requiring
active attention — reduces uncertainty passively.

Biggest assumption: Patients will correctly interpret the color
shift without explicit instruction.

What could go wrong: Color meaning is not universal; colorblind
patients are excluded.
```

---

## Stage 4 — Prototype: Paper Prototype with Assumption Mapping

### When to use
You have 2–3 concepts. You need to decide what to build and at what fidelity. This procedure ensures you prototype the right thing — the most uncertain, highest-stakes assumption — not the easiest thing to sketch.

### Assumption Mapping

Before picking up scissors or opening Figma, map all assumptions in the concept against two axes:

```
                HIGH RISK
                    |
    Prototype here  |  Kill the concept?
    (test urgently) |  (validate first)
                    |
HIGH UNKNOWN -------+------- LOW UNKNOWN
                    |
    Background      |  Ignore for now
    reading OK      |  (safe to assume)
                    |
                LOW RISK
```

**Process**:
1. List every assumption in the concept (from "Biggest assumption" in Concept Poster + brainstorm)
2. Rate each: Is it HIGH or LOW unknown? (Do we have any evidence either way?)
3. Rate each: Is it HIGH or LOW risk? (If wrong, does the concept fail?)
4. Place on the 2×2
5. Prototype the HIGH unknown / HIGH risk assumptions first

### Fidelity Decision Table

| What you're testing | Right fidelity | Wrong fidelity |
|---|---|---|
| Information flow ("do users understand the steps?") | Paper sketch, index cards | Coded prototype |
| Visual hierarchy ("do they see the right thing first?") | Greyscale wireframe | Colour mockup with real content |
| Interaction feel ("is the tap target intuitive?") | Clickable Figma prototype | Paper |
| Technical feasibility ("can the API return this in <200ms?") | Spike/proof-of-concept code | Any design tool |
| Emotional response ("does this feel trustworthy?") | High-fidelity visual with real copy | Low-fidelity sketch |

### Paper Prototype Procedure

**Materials**: A4 paper, markers, scissors, tape, a smartphone camera to photograph each state.

**Step 1 — Define the scenario (5 min)**
Write one user task in the form:
`The user wants to [goal]. Starting from [starting state], they should be able to [measurable outcome].`

**Step 2 — Map the screens (10 min)**
List every screen or state the user passes through. Write each as a box on a whiteboard.

**Step 3 — Draw each state (15–20 min)**
One sheet per screen. Draw only what the user sees — no backend detail, no annotations.

Label interactive elements with a small arrow: `→ [next screen name]`

**Step 4 — Simulate (during testing)**
One team member holds the current screen. When the user taps/points at an element, the facilitator swaps in the next sheet. The "computer" never speaks — swap silently.

---

## Stage 5 — Test: Structured Observation Sheet

### When to use
You're sitting with a real user running through your prototype. This sheet prevents the most common testing failures: asking leading questions, narrating the prototype, and forgetting to record surprises.

### Session Structure (45 min per user)

| Phase | Duration | What happens |
|---|---|---|
| Warm-up | 5 min | Explain you're testing the design, not the user. Ask them to think aloud. |
| Task 1 | 10 min | Give the scenario. Be silent. Observe. |
| Task 2 (if any) | 10 min | Same. |
| Debrief | 10 min | Ask open-ended questions (see below). |
| Team note comparison | 10 min | Done without the user present. |

### Observer Sheet

```
User ID (anon): ___  Session #: ___  Prototype version: ___

TASK: ___________________________________________

WHAT I SAW (direct behavior — no interpretation)
→
→
→

QUOTES (verbatim, not paraphrased)
→
→

PLACES USER HESITATED / BACKTRACKED
→

PLACES USER SUCCEEDED WITHOUT PROMPTING
→

MOMENT THAT SURPRISED ME
→

WHAT ASSUMPTION DOES THIS CONFIRM OR DENY?
→
```

### Debrief Question Bank

Ask these in order. Do not skip to #4 if #1 reveals something important.

1. "Walk me through what you just did."  *(reconstruction — reveals their mental model)*
2. "Was there a moment where you weren't sure what to do next?"  *(friction points)*
3. "What did you expect to happen when you [specific action]?"  *(expectation mismatch)*
4. "If this existed tomorrow, would you use it?" *(do NOT ask this first — it's leading if asked early)*
5. "What would make you more confident in this?"  *(trust + missing information)*

**Never ask**: "Did you like it?" / "Was it easy?" / "What would you add?" (leading, evaluative, or generates wish lists rather than insights)

### Analysis: Rainbow Sheet

After testing 5–6 users, consolidate findings with a Rainbow Sheet — a simple table that surfaces patterns across sessions.

```
| Observation                        | U1 | U2 | U3 | U4 | U5 | Pattern? |
|------------------------------------|----|----|----|----|----|-|
| Missed the CTA on screen 2         | ✓  |    | ✓  | ✓  |    | 3/5 → fix |
| Tried to swipe instead of tap      |    | ✓  |    |    | ✓  | 2/5 → monitor |
| Read all the confirmation text     | ✓  | ✓  | ✓  | ✓  | ✓  | 5/5 → valuable |
| Confused by "estimated" qualifier  |    |    | ✓  |    | ✓  | 2/5 → monitor |
```

**Decision rule**: 3+ of 5 users encountering the same issue = fix before next prototype iteration. 1–2 users = note but do not rebuild around it yet.

---

## Iron Law Reinforcement

The exercises above enforce the sequence from SKILL.md:

| Violating move | What goes wrong |
|---|---|
| Running Crazy 8s before Fly-on-the-Wall | Ideas solve the team's assumptions, not real user pain |
| Drafting the POV before clustering insights | POV reflects whoever speaks first, not the pattern in the data |
| Prototyping before Assumption Mapping | Team builds the most comfortable idea, not the most testable one |
| Asking "did you like it?" in testing | Users give socially acceptable answers; no actionable signal |

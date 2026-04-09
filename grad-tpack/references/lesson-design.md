# TPACK Lesson Design Templates

## The Core Design Question

Before selecting any technology, answer three questions in order:

1. **Content question**: What is the specific concept, skill, or misconception this lesson addresses?
2. **Pedagogy question**: What learning process (modeling, discussion, practice, feedback, inquiry) best serves that content?
3. **Technology question**: Does a technology exist that makes that specific pedagogical process more effective for that specific content — and if so, which one?

If you reach step 3 without clear answers to steps 1 and 2, stop. Technology chosen first produces TK-only integration, not TPACK.

---

## Design Protocol: The TPACK Alignment Check

Use this protocol for every lesson before finalizing technology choices.

```
TPACK Alignment Check

Content anchor: [one sentence: what students must understand or be able to do]
Pedagogical mechanism: [one of: direct instruction / modeling / guided practice /
                        collaborative inquiry / formative feedback / discussion]
Technology candidate: [specific tool or platform]

Alignment test (all three must be YES):
  [ ] Does this technology make the PEDAGOGICAL MECHANISM more effective?
  [ ] Does this technology make the CONTENT more accurate, visible, or manipulable?
  [ ] Would removing the technology require changing the pedagogical mechanism?

If the third answer is NO: the technology is decorative, not instructional.
```

The third question is the sharpest filter. If you can do the same pedagogy without the technology (just more slowly), the technology adds convenience, not learning. That may be acceptable — but it is not TPACK integration.

---

## Seven-Domain Lesson Blueprint

Map each lesson element to a TPACK domain. A lesson with entries only in TK or CK rows is under-integrated.

| Domain | Design Element | Example Entry |
|--------|---------------|---------------|
| **TK** | What tool is used? | Desmos graphing calculator |
| **PK** | What learning process? | Guided inquiry with prediction–check–revise cycle |
| **CK** | What content is targeted? | Behavior of quadratic functions near vertex |
| **TPK** | How does the tool enable the pedagogy? | Real-time parameter sliders let students test predictions immediately |
| **TCK** | How does the tool represent the content? | Dynamic graph changes when a, b, c coefficients change — impossible on paper |
| **PCK** | What misconception does this address? | Students think vertex location is always at x = 0 |
| **TPACK** | What can students DO with this tool that serves both the pedagogy and the content? | Students manipulate a, b, c; predict vertex shift; verify; write a rule in their own words |

A lesson designed at the TPACK row has an activity that is simultaneously content-specific, pedagogically intentional, and technologically enabled.

---

## Worked Example: Secondary History Lesson

**Context**: 10th-grade history, topic: propaganda analysis during WWII.

### Step 1 — Content anchor
Students must distinguish rhetorical techniques (emotional appeal, selective omission, loaded language) in primary source propaganda posters. Misconception: students treat posters as neutral historical records rather than persuasion artifacts.

### Step 2 — Pedagogical mechanism
Close reading + structured peer discussion (harkness-style annotation) with formative feedback.

### Step 3 — Technology candidate
Hypothesis annotation tool (e.g., Hypothes.is or Google Classroom comment layer on a scanned image).

### TPACK Alignment Check

| Question | Answer |
|----------|--------|
| Does annotation make close reading more effective? | **YES** — students can tag specific visual zones, building evidence-linked claims rather than general impressions |
| Does annotation make propaganda techniques more visible? | **YES** — color-coded tags for "emotional appeal" vs "omission" create a visible rhetorical map of the poster |
| Would removing the technology require changing the pedagogy? | **YES** — without shared annotation, peer discussion loses the shared visual anchor; the discussion becomes generic |

### Seven-Domain Mapping for This Lesson

| Domain | Element |
|--------|---------|
| TK | Hypothes.is annotation on scanned primary source image |
| PK | Close reading → structured peer discussion → class synthesis |
| CK | WWII propaganda techniques: appeal to fear, enemy dehumanization, selective framing |
| TPK | Shared annotation externalizes thinking, making peer discussion evidence-based not opinion-based |
| TCK | Annotation layers make the propaganda structure spatially explicit — the visual composition IS the content |
| PCK | Addresses the misconception that images are transparent; annotation forces interpretive stance |
| TPACK | Students annotate a poster collaboratively, tag rhetorical moves with evidence-linked labels, then argue a claim about which technique was most effective — using the annotation map as evidence |

---

## Lesson Type Templates

### Template A: Concept Visualization (TCK-heavy)

Use when: abstract content becomes concrete only when visually represented or dynamically manipulated.

```
Content:       [abstract concept that has dynamic or spatial properties]
Pedagogy:      Predict → Observe → Explain (POE cycle)
Technology:    [simulation, dynamic visualization, or modeling tool]

Activity structure:
  1. Pose a "what will happen if..." question (no tool yet)
  2. Students write individual predictions with reasoning (2 min)
  3. Students run the simulation / explore the visualization
  4. Students compare prediction to observation, revise explanation
  5. Class discussion: what rule does the pattern reveal?

TPACK check: The tool must display something not visible in a static
             textbook diagram. If a diagram suffices, the tool adds nothing.
```

**Examples**: PhET simulations for physics/chemistry, Desmos for algebra, GeoGebra for geometry proofs.

---

### Template B: Peer Feedback Loop (TPK-heavy)

Use when: the pedagogy requires rapid iterative feedback that the teacher alone cannot scale.

```
Content:       [skill requiring practice with corrective feedback]
Pedagogy:      Deliberate practice with peer assessment rubric
Technology:    [peer review platform, shared document, or quiz tool with instant scoring]

Activity structure:
  1. Model the skill once (teacher or exemplar)
  2. Students produce a first attempt (individual, 5–10 min)
  3. Structured peer review using a provided rubric (tool-mediated)
  4. Students revise based on feedback
  5. Optional: second peer round or teacher spot-check

TPACK check: The technology must make the feedback faster, more specific,
             or more numerous than teacher-only feedback. If 25 students
             can only get feedback from one teacher, the technology is
             not solving the right problem.
```

**Examples**: Google Docs comment threads for writing, Peergrade for structured peer assessment, Kahoot for immediate vocabulary/concept checks.

---

### Template C: Inquiry with Data (TPACK-heavy)

Use when: content is best understood by students generating and interpreting real data, not receiving it.

```
Content:       [concept where pattern-detection IS the learning]
Pedagogy:      Inquiry cycle: question → collect → analyze → claim → critique
Technology:    [data collection tool + visualization or analysis tool]

Activity structure:
  1. Pose a testable question (teacher-generated or student-generated)
  2. Students collect or access real data using the tool
  3. Students visualize/analyze the data (in-tool or export)
  4. Students make a claim supported by evidence from the data
  5. Class critiques claims: alternative explanations? Data quality issues?

TPACK check: The claim students make must be impossible to make without
             the data. If the "right answer" is pre-known and students
             are just confirming it, this is verification, not inquiry.
```

**Examples**: Google Sheets + public datasets for social studies, Sensor Logger for physics labs, CODAP for statistics, Twitter/Reddit API for media literacy.

---

## Knowledge Gap → Design Decision Table

When assessing a teacher's TPACK profile, use observed gaps to guide which template to assign in professional development:

| Weakest Domain | Symptom | Recommended Design Move |
|---------------|---------|------------------------|
| TK | Teacher avoids tools; low confidence | Template A or B with low-complexity tools (Google Slides, shared docs) before moving to simulations |
| PK | Technology used for transmission, not interaction | Restructure around Template B (peer feedback); force a feedback loop into every lesson |
| CK | Technology chosen before content is clarified | Require completion of Content Anchor field before tool selection; use Template C to force content-first reasoning |
| TPK | Technology present but pedagogy unchanged | Assign Template B; require articulating what students DO with the tool, not what it displays |
| TCK | Tool doesn't represent content accurately | Audit tool choice; require a TCK alignment statement explaining how the tool represents the concept |
| PCK | Lesson doesn't address known misconceptions | Add a "misconception targeted" field to all lesson plans; Template A's POE cycle surfaces prior beliefs |
| TPACK | All three present but not integrated | Require the "TPACK row" to contain a student action verb that is simultaneously content-specific AND tool-dependent |

---

## Activity Design Anti-Patterns

These are the design-level failures that produce weak TPACK in practice, not just in theory.

**Anti-pattern 1: The Digital Worksheet**
Paper activity digitized to Google Forms or a PDF. Content unchanged, pedagogy unchanged, technology adds friction. Fix: ask "what interaction does the tool enable that paper cannot?"

**Anti-pattern 2: The Novelty Hook**
Lesson opens with a VR headset, AR overlay, or AI chatbot to "engage" students, then returns to standard lecture. Technology serves motivation, not cognition. Fix: tie the technology to the content representation or the feedback mechanism.

**Anti-pattern 3: One-Size-All Tool**
Same platform (e.g., Nearpod, Padlet) used across every subject regardless of content type. A tool that fits everything probably fits nothing deeply. Fix: select tool after content anchor and pedagogy are locked in.

**Anti-pattern 4: Teacher-Facing Technology**
Projector + teacher-operated simulation where students watch. The teacher has TPACK; students are passive. Fix: every student must have hands on the technology during the TPACK activity.

**Anti-pattern 5: Assessment Mismatch**
Technology used during instruction but assessment returns to paper-only. Students cannot transfer the technologically-developed understanding to the assessment context. Fix: align at least one assessment task to the same technology-mediated representation.

---

## Minimum Viable Lesson Design Checklist

```
[ ] Content anchor is a single, specific learning objective (not a topic)
[ ] A known student misconception is named
[ ] The pedagogical mechanism is named (not just "activity")
[ ] The technology is named with specificity (not just "the internet")
[ ] The TPACK alignment check passes (all three YES)
[ ] Students are active users of the technology, not observers
[ ] The lesson could not proceed unchanged without the technology
[ ] Assessment requires the same cognitive process as the activity
```

A lesson that passes all eight items is operating at the TPACK intersection. A lesson that fails items 7 or 8 is the most common case — technology integrated in instruction but not in assessment, creating a transfer gap.

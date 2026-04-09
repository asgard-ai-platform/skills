# WCAG Accessibility Checklist

Nielsen's 10 heuristics do not cover accessibility. Use this checklist as a parallel audit track alongside heuristic evaluation, applying the **same 0-4 severity scale** from the parent skill.

## Severity Mapping for Accessibility Violations

| WCAG Level | Default Severity | Reasoning |
|------------|-----------------|-----------|
| AAA failure | 1–2 | Enhanced level; best effort |
| AA failure | 3 | Legal compliance threshold in most jurisdictions; blocks assistive tech users |
| A failure | 4 | Catastrophic — breaks basic access for screen reader / keyboard users |

WCAG has three conformance levels: A (minimum), AA (standard target), AAA (enhanced). Target **AA** in practice.

---

## Checklist by Perception Category

### 1. Color and Contrast

**1.1 Text contrast ratio** (WCAG 1.4.3 — Level AA)

Formula:
```
Contrast Ratio = (L1 + 0.05) / (L2 + 0.05)

where L1 = relative luminance of lighter color
      L2 = relative luminance of darker color
      Luminance = 0.2126R + 0.7152G + 0.0722B (linearized sRGB)
```

Thresholds:
| Text size | Minimum ratio |
|-----------|--------------|
| Normal text (< 18pt / < 14pt bold) | 4.5:1 |
| Large text (≥ 18pt / ≥ 14pt bold) | 3:1 |
| UI components and graphical objects | 3:1 |
| Disabled controls | No requirement |
| Decorative text | No requirement |

**Quick test**: Use browser DevTools → Accessibility panel, or the [contrast ratio formula](https://www.w3.org/TR/WCAG21/#dfn-contrast-ratio) with hex values.

Worked example:
```
Background: #FFFFFF (white)  → L = 1.0
Foreground: #767676 (gray)   → L ≈ 0.215

Ratio = (1.0 + 0.05) / (0.215 + 0.05) = 1.05 / 0.265 ≈ 3.96:1

Result: FAILS normal text (needs 4.5:1), PASSES large text (needs 3:1)
Severity: 3 (AA violation for body copy)
```

**1.2 Color not sole differentiator** (WCAG 1.4.1 — Level A)

Check: Does removing color still convey the same information?

Violation patterns:
- Red/green form validation with no icon or text label
- Chart lines distinguished only by color (no shape or label)
- Required field asterisks in red with no text explanation

Fix pattern: Add icon + color, or text + color — never color alone.

---

### 2. Keyboard Navigation

All interactive elements must be operable via keyboard without a mouse (WCAG 2.1.1 — Level A).

**2.1 Tab order audit** — manual test procedure:
1. Reload the page without touching the mouse
2. Press Tab repeatedly; record element sequence
3. Flag if focus skips interactive elements or jumps illogically
4. Flag if focus goes offscreen or gets trapped (except in dialogs)

Expected order: left-to-right, top-to-bottom in Western layouts, matching visual reading flow.

**2.2 Focus indicator visible** (WCAG 2.4.7 — Level AA)

Test: Tab through the interface. At every step, can you see where focus is?

Violation: `:focus { outline: none }` CSS without a custom visible indicator. This is one of the most common AA failures.

Minimum acceptable indicator: 3:1 contrast between focused and unfocused states (WCAG 2.4.11 — Level AA, WCAG 2.2).

**2.3 Keyboard trap** (WCAG 2.1.2 — Level A)

A keyboard trap severity is always **4**. User cannot exit modal/widget without mouse.

Test: Tab into every modal, dropdown, datepicker, and custom widget. Can you exit with Escape or Tab?

Correct modal behavior:
- Focus moves into modal on open
- Tab cycles only within modal
- Escape closes modal and returns focus to trigger element
- Focus does not escape to background content

**2.4 Skip navigation link** (WCAG 2.4.1 — Level A)

Pages with repeated navigation (header, nav menu) must have a mechanism to skip to main content.

Implementation: `<a href="#main" class="skip-link">Skip to main content</a>` as first DOM element, visible on focus.

---

### 3. Screen Reader Compatibility

**3.1 Images have text alternatives** (WCAG 1.1.1 — Level A)

| Image type | Required `alt` |
|------------|---------------|
| Informative (conveys meaning) | Describe the meaning, not appearance |
| Functional (button/link icon) | Describe the action, not the icon |
| Decorative | `alt=""` (empty, not absent) |
| Complex (chart, diagram) | Short alt + long description nearby |
| Text in image | Repeat the text verbatim |

Anti-pattern: `alt="image"`, `alt="photo"`, `alt="logo"` — these are useless.

Worked example:
```html
<!-- BAD: describes appearance -->
<img src="error.png" alt="red circle with X">

<!-- GOOD: describes meaning -->
<img src="error.png" alt="Error: payment failed">

<!-- BAD: generic -->
<img src="hero.jpg" alt="photo">

<!-- GOOD: decorative gets empty alt -->
<img src="divider.png" alt="">
```

**3.2 Form inputs have labels** (WCAG 1.3.1 + 3.3.2 — Level A)

Every `<input>`, `<select>`, `<textarea>` must have an associated `<label>` (or `aria-label`, or `aria-labelledby`).

Test: In browser DevTools, inspect each form element. Run: `document.querySelectorAll('input:not([type="hidden"])').forEach(i => console.log(i.labels.length, i.getAttribute('aria-label'), i.getAttribute('aria-labelledby')))` — any row with all nulls/zeros is a violation.

Placeholder text is NOT a label substitute — it disappears on input and has poor contrast.

**3.3 Interactive elements have accessible names** (WCAG 4.1.2 — Level A)

All buttons, links, and form controls must have a name a screen reader announces.

Quick test: Run `document.querySelectorAll('button, a, input, select, textarea')` in console. For each, check that it has visible text, `aria-label`, or `aria-labelledby`.

Violation: `<button><img src="close.svg"></button>` with no alt text → announced as "button" with no name.

Fix: `<button aria-label="Close dialog"><img src="close.svg" alt=""></button>`

**3.4 Page has a meaningful title** (WCAG 2.4.2 — Level A)

`<title>` must describe the page, not just the site name.

| Bad | Good |
|-----|------|
| `<title>Acme Corp</title>` | `<title>Checkout — Acme Corp</title>` |
| `<title>Page 1</title>` | `<title>Profile Settings — Acme Corp</title>` |

**3.5 Language declared** (WCAG 3.1.1 — Level A)

`<html lang="zh-TW">` (or appropriate BCP 47 code). Screen readers use this to select the correct voice engine.

---

### 4. Motion and Time

**4.1 Flashing content** (WCAG 2.3.1 — Level A, severity **4**)

Content must not flash more than 3 times per second. Flashing can trigger photosensitive seizures. No exceptions — this is a hard block.

Test: Frame-by-frame inspection of any animation or video. Flag any content that strobes.

**4.2 Auto-playing media** (WCAG 1.4.2 — Level A)

Audio playing for more than 3 seconds must have a mechanism to pause, stop, or mute.

**4.3 Pause/stop/hide moving content** (WCAG 2.2.2 — Level A)

Carousels, auto-scrolling tickers, animated banners: user must be able to pause them.

**4.4 Sufficient time limits** (WCAG 2.2.1 — Level A)

If a session times out, user must be warned and given at least 20 seconds to extend, OR timeout must be ≥ 20 hours, OR user can turn it off.

---

### 5. Text and Readability

**5.1 Text resize** (WCAG 1.4.4 — Level AA)

Text must resize up to 200% without loss of content or functionality. Test with browser zoom at 200%.

Common failure: fixed-height containers that clip text when font size increases. Use `min-height` instead of `height`.

**5.2 Text spacing** (WCAG 1.4.12 — Level AA)

Apply this override CSS and verify no content is lost or truncated:
```css
* {
  line-height: 1.5 !important;
  letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important;
}
p { margin-bottom: 2em !important; }
```

**5.3 Reflow** (WCAG 1.4.10 — Level AA)

At 320px viewport width (equivalent to 400% zoom on 1280px screen), content must reflow to single column with no horizontal scrolling.

Exception: content that requires two-dimensional layout to function (data tables, maps, code editors).

---

## Audit Workflow (Parallel to Heuristic Walk-through)

Run this as a second pass after heuristic evaluation, adding findings to the same report.

```
Step 1 — Automated scan (5 min)
  Run axe DevTools or Lighthouse Accessibility audit.
  Automated tools catch ~30-40% of WCAG violations.
  Do NOT stop here — most failures require manual inspection.

Step 2 — Contrast check (10 min)
  Use color picker + contrast formula on all text colors against backgrounds.
  Check hover/focus states separately — they often have different palettes.

Step 3 — Keyboard-only navigation (15 min)
  Unplug mouse. Navigate entire evaluated flow using only Tab, Shift+Tab,
  Enter, Space, Arrow keys, Escape.
  Record every place where you get stuck, lose focus, or cannot activate a control.

Step 4 — Screen reader spot check (15 min)
  macOS: VoiceOver (Cmd+F5)
  Windows: NVDA (free) or Narrator
  Navigate all forms and confirm all inputs are announced with correct labels.
  Confirm all images have appropriate alt text.

Step 5 — Zoom test (5 min)
  Set browser zoom to 200% and 400%.
  Verify no content is clipped or lost.
  Verify no horizontal scrollbar appears (unless essential).
```

---

## Quick Reference: Most Common AA Failures

| Violation | Heuristic parallel | Default severity |
|-----------|-------------------|-----------------|
| Insufficient contrast ratio | #8 Aesthetic | 3 |
| Missing focus indicator | #6 Recognition | 3 |
| No form label | #6 Recognition | 4 |
| Color as sole error indicator | #9 Error recovery | 4 |
| Icon button with no accessible name | #2 Match real world | 4 |
| Keyboard trap in modal | #3 User control | 4 |
| Missing alt text on informative image | #6 Recognition | 4 |
| Content lost at 200% zoom | #8 Aesthetic | 3 |
| Auto-playing audio with no stop | #3 User control | 4 |

---

## WCAG Reference Versions

- **WCAG 2.1** (2018) — current legal baseline in most jurisdictions including Taiwan (digital accessibility regulations reference this)
- **WCAG 2.2** (2023) — adds focus appearance (2.4.11), dragging alternatives (2.5.7), consistent help (3.2.6); backward compatible
- **WCAG 3.0** — in draft as of 2025; not yet adopted for compliance

For Taiwan government procurement: 《身心障礙者權益保障法》 and related guidelines reference WCAG 2.1 AA as the standard.

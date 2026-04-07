---
name: "ops-meeting-minutes"
description: "Create structured meeting minutes with decisions, action items, and follow-up tracking. Use this skill when the user needs to document meetings effectively, track action items, improve meeting productivity, or set up a meeting note system — even if they say 'take notes for this meeting', 'what was decided', 'who's responsible for what', or 'our meetings have no follow-through'."
metadata:
  category: "WP-10 通用商業"
  tags: ["business", "meetings", "documentation", "productivity"]
---

# Meeting Minutes

## Framework

```
IRON LAW: Every Meeting Must Produce Decisions + Action Items

If a meeting ends with no documented decisions and no action items with
owners and deadlines, the meeting was a waste of time. Capture these
DURING the meeting, not after. Minutes without action items are a diary.
```

### Meeting Minutes Template

```markdown
# Meeting: {Title}
Date: {YYYY-MM-DD} | Time: {HH:MM-HH:MM} | Location: {room/link}
Attendees: {names}
Absent: {names}
Facilitator: {name} | Note-taker: {name}

## Agenda
1. {topic 1} — {presenter} ({X min})
2. {topic 2} — {presenter} ({X min})
3. {topic 3} — {presenter} ({X min})

## Discussion Notes
### {Topic 1}
- {Key point discussed}
- {Different viewpoints raised}
- **DECISION**: {what was decided}

### {Topic 2}
- {Key point}
- **DECISION**: {what was decided} / **DEFERRED**: {to when/what condition}

## Action Items
| # | Action | Owner | Deadline | Status |
|---|--------|-------|----------|--------|
| 1 | {specific task} | {name} | {date} | Open |
| 2 | {specific task} | {name} | {date} | Open |

## Next Meeting
- Date: {next meeting date}
- Agenda items for next time: {carry-over items}
```

### Action Item Format: WHO + WHAT + WHEN

Bad: "Follow up on the pricing issue"
Good: "**@Sarah** to prepare pricing comparison table with 3 competitors by **April 10**"

### Meeting Efficiency Tips

1. **Agenda first**: Distribute agenda 24+ hours before the meeting
2. **Time-box**: Assign time limits per topic. Use a visible timer.
3. **Parking lot**: Off-topic items go to a "parking lot" list for later — don't derail the meeting
4. **Last 5 minutes**: Reserve for summarizing decisions and action items
5. **Distribute within 24 hours**: Send minutes the same day or next morning while memory is fresh

### AI Meeting Tools

| Tool | Capability | Best For |
|------|-----------|----------|
| **Otter.ai** | Transcription + summary | English meetings |
| **Fireflies.ai** | Transcription + action item extraction | Team meetings |
| **Claude/GPT** | Summarize transcript, extract decisions | Post-meeting processing |
| **Notion AI** | In-context meeting notes | Notion-based teams |

Even with AI transcription, a human note-taker should capture DECISIONS and ACTION ITEMS in real-time. AI captures what was said; humans capture what was DECIDED.

## Output Format

```markdown
# Meeting Minutes: {Title} — {Date}

## Decisions Made
1. {decision + context}
2. {decision}

## Action Items
| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | {task} | {name} | {date} |

## Key Discussion Points
- {summary of important discussion, not verbatim}

## Parking Lot (for future discussion)
- {deferred topic}
```

## Gotchas

- **Minutes ≠ transcript**: Don't capture everything said. Capture: decisions, action items, key disagreements, and context needed to understand decisions later.
- **Action items without deadlines don't get done**: "ASAP" is not a deadline. Every action item needs a specific date.
- **The note-taker has power**: They decide what's recorded as a "decision." Assign this role intentionally.
- **Follow up on action items**: Minutes sent without follow-up are ignored. Review action item status at the START of the next meeting.
- **Recurring meetings need structure**: Weekly standups, monthly reviews, and quarterly planning each need different minute formats. One size doesn't fit all.

## References

- For meeting facilitation techniques, see `references/facilitation.md`

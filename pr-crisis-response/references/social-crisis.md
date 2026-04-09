# Social Media Crisis Playbook

## Why Social Crises Move Differently

Traditional PR crises give you hours; social media crises give you minutes. The critical difference is **public velocity** — the rate at which negative sentiment accumulates public visibility before your team can respond.

Three structural reasons social crises are harder to contain:

1. **Asymmetric amplification**: A single verified post with emotional resonance can reach 100k views before your monitoring tool fires an alert.
2. **Screenshot permanence**: Deleting a post does not erase it. Screenshots are re-shared specifically to document that you deleted it ("ratio + deleted = guilty").
3. **Algorithmic acceleration**: Platforms boost content with high engagement. Outrage drives engagement. Your crisis content is being actively promoted by the platforms you're trying to respond on.

---

## Signal Classification: Is This a Crisis or Noise?

Before activating the full protocol, classify the signal using the **Velocity × Sentiment × Source** matrix.

### Velocity Score (V)

Measure over the first 30 minutes after detection:

| Shares/RTs in 30 min | Score |
|----------------------|-------|
| < 100 | 1 |
| 100–500 | 2 |
| 500–2,000 | 3 |
| 2,000–10,000 | 4 |
| > 10,000 | 5 |

### Sentiment Score (S)

Estimated negative sentiment ratio from monitoring tools or manual sample:

| Negative ratio | Score |
|----------------|-------|
| < 20% | 1 |
| 20–40% | 2 |
| 40–60% | 3 |
| 60–80% | 4 |
| > 80% | 5 |

### Source Score (Src)

| Origin | Score |
|--------|-------|
| Unknown individual account | 1 |
| Mid-tier influencer (10k–100k followers) | 2 |
| Large influencer or verified account (100k+) | 3 |
| Journalist or media account | 4 |
| Competitor, regulator, or public figure | 5 |

### Risk Score Formula

```
Risk Score = V × (S + Src)
```

| Risk Score | Classification | Response Trigger |
|------------|---------------|-----------------|
| ≤ 10 | Level 1 Noise | Monitor, no action required |
| 11–25 | Level 2 Issue | Prepare statement, assign owner |
| 26–40 | Level 3 Crisis | Activate crisis team immediately |
| > 40 | Level 3 Crisis (Viral) | C-suite involvement, all-hands |

### Worked Example

A verified food blogger (Src = 3) posts a video claiming your restaurant served undercooked chicken. Within 30 minutes: 1,800 shares (V = 3), 70% negative comments (S = 4).

```
Risk Score = 3 × (4 + 3) = 21 → Level 2 Issue
```

But if the post gets picked up by a journalist and re-shared from a media account (Src bumps to 4) with velocity crossing 2,000 (V = 4):

```
Risk Score = 4 × (4 + 4) = 32 → Level 3 Crisis
```

This is why you re-score every 30 minutes in the first two hours — the classification can escalate.

---

## Platform-Specific Response Rules

Different platforms have different norms. Applying the wrong response style to the wrong platform makes you look out of touch.

### Twitter / X

- **Response window**: 30–60 minutes before a thread develops its own narrative.
- **Tone**: Direct, non-corporate. Long threads are skimmed; your first tweet is often the only one read.
- **Mechanics**: Reply to the original post AND publish a standalone tweet from your brand account. Do not only rely on the reply thread — it won't surface on brand searches.
- **Quote-tweet vs reply**: Reply for individual complaints; quote-tweet for statements that need wider reach. Never quote-tweet to dunk or rebut — it amplifies the original.
- **Character limit discipline**: If your statement doesn't fit in 280 characters, link to a longer statement on your owned domain. Do not use Twitter threads for crisis statements — they look improvised.

### Facebook

- **Response window**: 1–2 hours. Facebook's algorithm surfaces recent activity on brand pages.
- **Tone**: Warmer than Twitter; community-oriented framing works.
- **Mechanics**: Post on your brand page, pin the statement at the top, and respond to top comments by name. Facebook comment sections without brand responses look abandoned.
- **Groups and shares**: You cannot control third-party group shares. Focus on ensuring your owned page response is findable when users search.

### Instagram

- **Response window**: 2–4 hours. Instagram crises often start in Stories (ephemeral) and escalate to posts.
- **Mechanics**: Statement in caption of a dedicated post; also add to Stories with a link sticker back to the full post. Comment responses for individual DMs.
- **Limitation**: You cannot edit a published caption if it's been shared broadly — corrections become a second post, not an edit. Draft carefully.

### TikTok

- **Response window**: 15–30 minutes for viral videos. TikTok's For You Page distributes content to non-followers at unprecedented speed.
- **Mechanics**: If the crisis originated on TikTok (someone posted a video about you), respond with a video — not a text comment. Text-only responses on TikTok look evasive. Use the Duet or Stitch feature to respond directly to the source video if appropriate.
- **Tone**: Authentic > polished. A clearly-read-from-script response is widely mocked. Have a spokesperson speak naturally to camera.
- **When you can't do video**: Post a text card video (your logo + statement text on a clean background with audio) as a fallback. Still better than a comment.

### PTT (Taiwan-specific)

- **Response window**: Within 2 hours for a post trending on hot boards (八卦板, 消費板).
- **Mechanics**: PTT does not have a brand account system. Your options are: (a) engage via a registered account — risky if identified as corporate astroturfing; (b) issue an official statement on your website and brief media simultaneously; (c) authorized PR firm posts an identified corporate response.
- **The pipeline**: A hot PTT post (推文 50+, 熱門標記) typically surfaces in ETtoday, UDN, or LINE Today within 1–3 hours. This is the moment Level 2 becomes Level 3. Do not wait for media calls — get ahead of the pipeline.
- **What not to do**: Hiring accounts to flood the thread with positive push (洗推) is identifiable by PTT veterans within minutes and causes a second, worse crisis.

### LINE (Taiwan-specific)

- **Response window**: LINE crises are invisible until they surface publicly. Group chats spread screenshots before you know they exist.
- **Mechanics**: Monitor brand mentions on public LINE communities. When a LINE-originated complaint surfaces on Twitter/PTT, treat it as already at Level 2 — it was spreading privately before going public.

---

## Pre-Written Holding Statement Templates

Speed in the first hour requires preparation. These templates cover the four most common social media crisis types. Fill in brackets at the moment of crisis.

### Template 1: Product Quality / Safety Complaint

```
We've seen the reports about [product/issue] and take this seriously.
We are investigating immediately. If you've been affected, please
contact us at [contact] — we will respond within [time].
We'll share our findings by [time].
— [Brand name]
```

### Template 2: Customer Service Failure (Viral Complaint)

```
We're sorry [name or "you"] had this experience. This is not the
standard we hold ourselves to. Please DM us or email [contact]
and we will make this right. We're also reviewing what went wrong
to prevent recurrence.
```

### Template 3: Data / Privacy Incident

```
We are aware of reports regarding [data/privacy issue].
Security of your data is our priority. We are investigating and
have engaged [security team/third-party firm]. We will not
speculate until we have facts, but will update at [time/channel].
If you have concerns, contact [privacy contact].
```

### Template 4: Employee / Executive Conduct

```
We are aware of the information circulating regarding [situation].
We treat all such matters with the utmost seriousness. We are
reviewing the situation and will take appropriate action.
We will share what we can once the review is complete.
```

**What these templates have in common:**
- Acknowledge without admitting specific liability
- Name a specific follow-up time (not "soon")
- Provide a contact point
- Do not speculate or assign blame

---

## The "Do Not Delete" Rule

Deleting a social post that has already been screenshot and reshared triggers a predictable and damaging sequence:

1. Screenshots of the original post circulate with captions like "they deleted this"
2. The deletion itself becomes the story ("caught hiding evidence")
3. Journalists use deletion as a data point confirming the severity of the crisis

**Exception**: Delete only if the post contains specific legally dangerous content (e.g., a specific defamatory claim, an accidental data disclosure, or a specific threat). In those cases, acknowledge the deletion publicly:

```
We removed our earlier post [reason: it contained inaccurate
information / a privacy risk to [party] / language we regret].
Our updated statement is [link].
```

Do not silently delete.

---

## Engaging vs. Ignoring Individual Critics

Not every negative comment warrants a response. Over-responding amplifies the signal.

### Respond publicly when:
- The complaint has 50+ likes/shares on the original post
- The user appears to be a genuine customer with a specific, verifiable complaint
- Not responding would be read as confirmation of the claim
- The user has a media, influencer, or journalist flag on their profile

### Respond privately (DM) when:
- The complaint involves personal account details, order information, or anything requiring PII
- The person is clearly willing to resolve and not performing for an audience

### Do not respond when:
- The account is clearly a troll, bot, or bad-faith actor (no post history, generic avatar, inflammatory phrasing)
- Responding would create a screenshot-able exchange that looks worse than silence
- The comment is low-engagement and responding would surface it to your own followers

### The "worst comment" rule

When reviewing your comment section, identify the highest-engagement negative comment. If you respond to only one, respond to that one — it's the one everyone else is reading.

---

## Monitoring Setup for the First 6 Hours

Manual monitoring is insufficient once a crisis reaches Level 3. Minimum monitoring stack:

| Signal | Tool (free tier viable) | Cadence |
|--------|------------------------|---------|
| Brand name mentions | Google Alerts or Brand24 | Real-time |
| Twitter / X keywords | TweetDeck columns or Twitter Advanced Search | Every 15 min |
| PTT keywords | PTT search or ptt.cx search | Every 30 min |
| News mentions | Google News alert for brand name | Real-time |
| Hashtag velocity | Native platform analytics | Every 30 min |

Assign one person the dedicated role of **Monitor** during active crisis. Their only job: watch the dashboards and report velocity changes to the response team every 30 minutes. They do not draft responses.

---

## Escalation Triggers Requiring Immediate C-Suite Action

Move from PR team to C-suite escalation protocol immediately if any of the following appear:

- A journalist has published (not just asked about) a story with your brand named in the headline
- A government official, regulator, or elected representative has commented publicly
- The hashtag is trending nationally on any platform
- A competitor has amplified the crisis content
- The crisis involves potential physical harm, death, or criminal conduct
- Internal employees are posting publicly about the crisis

These conditions indicate the crisis has moved beyond what PR can manage through statement-and-monitor. At this point the CEO or named executive must be briefed and prepared to make a personal statement.

---

## Common Escalation Mistakes

**Mistake 1: Responding only in the channel where it started**

If a TikTok video goes viral and gets picked up by Twitter and PTT, issuing a response only on TikTok means most of the audience never sees it. Publish on all active channels simultaneously.

**Mistake 2: Correcting the facts before acknowledging the feeling**

"Actually, our food safety certifications show..." before "We're sorry you experienced this" reads as dismissive of the person. Lead with empathy, follow with facts.

**Mistake 3: Engaging in a public debate**

If the original poster is responding aggressively to your response, do not continue the public thread. One response, then: "We'd like to address this properly — please DM us." If they refuse, you've demonstrated good faith publicly; let the thread die.

**Mistake 4: The over-apologetic spiral**

Issuing multiple apologies in rapid succession (apology → second apology that it wasn't good enough → third apology) signals panic and invites escalation. One clear, accountable statement is more effective than three anxious revisions.

**Mistake 5: Employees "helping" on personal accounts**

Well-meaning employees who post "I work there, this isn't true" without authorization create a he-said/she-said dynamic that amplifies coverage. The internal communications protocol must explicitly prohibit this.

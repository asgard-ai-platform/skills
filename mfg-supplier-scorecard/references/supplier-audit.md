# Supplier Audit Checklist & Procedure

Supplier audits are the ground-truth complement to scorecard data. A scorecard
reflects what a supplier *reports*; an audit reveals what they *actually do*.
Use this document to plan, execute, and score an on-site or remote supplier
audit that feeds directly into the QCDS scorecard.

---

## Audit Types

| Type | Trigger | Depth | Duration |
|------|---------|-------|----------|
| **Initial qualification** | New supplier evaluation | Full | 1–2 days |
| **Annual surveillance** | A/B-grade suppliers, routine | Targeted | 4–8 hrs |
| **For-cause** | Spike in defect rate, delivery failures | Focused on problem area | 2–4 hrs |
| **Remote/desk audit** | Low-risk commodities, travel not justified | Document review only | 2–4 hrs |

---

## Pre-Audit Preparation

### Document Request List (send 2 weeks before visit)

Request these from the supplier before arriving. Gaps in the list are
themselves audit findings.

```
□ Quality Management System certificate (ISO 9001 / IATF 16949 / AS9100)
□ Most recent internal audit report and corrective action register
□ Process FMEAs for the parts you purchase
□ Control plans for your parts
□ Last 12 months' outgoing inspection data (defect rate by part number)
□ Customer complaint log (last 12 months)
□ Corrective Action / 8D reports for any issues affecting your parts
□ Calibration records for measurement equipment used on your parts
□ Key personnel org chart (Quality Manager, Production Manager)
□ Last 3 months' delivery performance data
□ Supplier's own sub-tier supplier list for critical raw materials
```

### Audit Team

- Lead auditor: knows your engineering/quality requirements
- Optional second auditor for large facilities: splits manufacturing vs. documentation review
- Assign a scribe — do not rely on memory

---

## Audit Execution: Four-Area Checklist

Score each item: **0** = not present / critical gap, **1** = partially
implemented, **2** = fully implemented and effective.

### Area 1 — Quality Management System (QMS)

| # | Checkpoint | 0 | 1 | 2 | Notes |
|---|-----------|---|---|---|-------|
| Q1 | Quality policy posted and understood by line workers (ask 2 randomly) | | | | |
| Q2 | Internal audit program active — audits completed on schedule last 12 mo | | | | |
| Q3 | Management review meeting held ≥ annually with documented outputs | | | | |
| Q4 | Corrective Action process: all open CARs have owner + due date | | | | |
| Q5 | Closed CARs verified effective (not just "action taken") | | | | |
| Q6 | Document control: work instructions at point of use, revision-controlled | | | | |
| Q7 | Training records exist for operators on your parts | | | | |
| Q8 | Change management process — supplier notifies you before process changes | | | | |

**Area 1 max: 16 pts**

---

### Area 2 — Manufacturing Process Control

| # | Checkpoint | 0 | 1 | 2 | Notes |
|---|-----------|---|---|---|-------|
| P1 | Control plan exists for your part numbers; up to date with current drawing rev | | | | |
| P2 | Operators follow control plan (spot-check: ask operator to explain their checks) | | | | |
| P3 | Critical process parameters monitored and recorded (temperature, torque, etc.) | | | | |
| P4 | SPC charts in use at critical CTQ characteristics (if volume warrants) | | | | |
| P5 | First Article / Setup approval before production run begins | | | | |
| P6 | Non-conforming material segregated, labeled, and dispositioned | | | | |
| P7 | Rework process documented and requires re-inspection | | | | |
| P8 | Tooling and equipment maintenance schedule exists and is current | | | | |
| P9 | Visual standards / limit samples available at workstations | | | | |
| P10 | FIFO (First In, First Out) observed in WIP and finished goods | | | | |

**Area 2 max: 20 pts**

---

### Area 3 — Measurement & Inspection

| # | Checkpoint | 0 | 1 | 2 | Notes |
|---|-----------|---|---|---|-------|
| M1 | All gages and measurement equipment calibrated; calibration stickers current | | | | |
| M2 | Calibration performed by accredited lab or against traceable standards | | | | |
| M3 | Incoming inspection process for raw materials / purchased components | | | | |
| M4 | In-process inspection points defined in control plan and executed | | | | |
| M5 | Final outgoing inspection: sample size appropriate for volume | | | | |
| M6 | Gage R&R study performed for critical measurements (ask for records) | | | | |
| M7 | Inspection records retained per agreed retention period | | | | |

**Area 3 max: 14 pts**

---

### Area 4 — Delivery & Supply Chain

| # | Checkpoint | 0 | 1 | 2 | Notes |
|---|-----------|---|---|---|-------|
| D1 | Production scheduling system visible; capacity vs. your orders assessed | | | | |
| D2 | Finished goods inventory policy aligns with your lead time expectations | | | | |
| D3 | Sub-tier supplier qualification: critical materials sourced from approved suppliers | | | | |
| D4 | Packaging and labeling matches your requirements (label format, protection) | | | | |
| D5 | Shipping / logistics process: carrier selection, on-time dispatch tracking | | | | |
| D6 | Early Warning system: supplier proactively notifies you of potential delays | | | | |

**Area 4 max: 12 pts**

---

## Scoring the Audit

**Total possible: 62 points**

```
Audit Score (%) = (Points Earned / 62) × 100
```

### Audit Rating → QCDS Score Mapping

| Audit Score | Audit Rating | QCDS Service Score input |
|-------------|-------------|--------------------------|
| 90–100% | Excellent | 5 |
| 75–89% | Satisfactory | 4 |
| 60–74% | Needs Improvement | 3 |
| 45–59% | Marginal | 2 |
| < 45% | Unacceptable | 1 |

The audit score feeds the **Service** dimension of the QCDS scorecard (as a
proxy for process maturity and management capability). Severe findings in
Areas 2–3 may also trigger a manual override of Quality scorecard scores
regardless of incoming PPM data.

---

## Worked Example

**Supplier**: Apex Machining Co.  
**Audit type**: Annual surveillance  
**Parts supplied**: Turned aluminum housings

### Scores recorded on-site

| Area | Max | Earned | Notes |
|------|-----|--------|-------|
| QMS | 16 | 11 | CAR process weak — 3 open CARs past due date (Q4 = 0) |
| Process Control | 20 | 16 | No SPC on bore diameter CTQ (P4 = 0); rework not re-inspected (P7 = 1) |
| Measurement | 14 | 12 | Gage R&R never performed on CMM fixture (M6 = 0) |
| Delivery | 12 | 10 | No formal early-warning notification process (D6 = 0) |
| **Total** | **62** | **49** | |

```
Audit Score = 49 / 62 × 100 = 79%  →  Satisfactory  →  Service Score = 4
```

### Findings by severity

| Finding ID | Area | Checkpoint | Severity | Required Action |
|-----------|------|-----------|---------|----------------|
| F-01 | QMS | Q4 | **Major** | Close all overdue CARs within 30 days; provide evidence |
| F-02 | Process | P4 | Minor | Implement SPC on bore diameter within 60 days |
| F-03 | Process | P7 | Minor | Update rework procedure to require reinspection sign-off |
| F-04 | Measurement | M6 | **Major** | Conduct Gage R&R on CMM fixture within 45 days |
| F-05 | Delivery | D6 | Observation | Establish early-warning notification protocol |

**Severity definitions**:
- **Major**: Systemic breakdown that creates real risk of defective product shipping or sustained delivery failure. Requires corrective action with deadline; re-audit may be required.
- **Minor**: Process gap not causing current escapes but represents risk. Action required within agreed timeframe.
- **Observation**: Opportunity for improvement; no mandatory action but tracked.

Any single **Major** finding caps the audit rating at *Needs Improvement* (3)
regardless of total score.

After applying the Major-finding cap: F-01 and F-04 both major → Service Score
revised to **3**, not 4.

---

## Audit Report Template

Fill this out within 5 business days of the visit. Send to supplier with
request for corrective action plan within 14 days of receipt.

```markdown
## Supplier Audit Report

**Supplier**: _______________
**Date of Audit**: _______________
**Auditor(s)**: _______________
**Audit Type**: Initial / Annual / For-cause / Remote
**Parts / Part Numbers in Scope**: _______________

### Summary

| Area | Max | Earned | % |
|------|-----|--------|---|
| QMS | 16 | | |
| Process Control | 20 | | |
| Measurement | 14 | | |
| Delivery | 12 | | |
| **Total** | **62** | | |

**Raw Audit Score**: _____ %
**Audit Rating**: Excellent / Satisfactory / Needs Improvement / Marginal / Unacceptable
**Major Finding Cap Applied**: Yes / No
**Adjusted Service Score (1–5)**: _____

### Findings

| ID | Area | Checkpoint | Severity | Required Action | Due Date |
|----|------|-----------|---------|----------------|---------|
| | | | | | |

### Strengths Observed

{List 2–3 genuine positives — this is required, not optional. Audit reports
that contain only findings damage the relationship and reduce supplier
cooperation.}

### Follow-Up Schedule

- Corrective action plan due from supplier: {date}
- Evidence of closure due: {date per finding}
- Re-audit (if Major findings): {date, if applicable}
- Next routine audit: {date}

**Report prepared by**: _______________
**Supplier acknowledgment**: _______________ (name, title, date)
```

---

## For-Cause Audit: Targeted Checklist

When triggered by a specific quality or delivery failure, skip the full
checklist and focus on the failure's root cause chain. Use the 5-Why to
scope which checkpoints are relevant.

**Example**: Customer complaint — 3 shipments with incorrect thread depth.

```
5-Why:
1. Why incorrect thread depth? → Tap wore beyond replacement interval
2. Why tap not replaced? → No defined replacement interval in control plan
3. Why missing from control plan? → FMEA did not identify tap wear as failure mode
4. Why missing from FMEA? → FMEA not updated after material change 8 months ago
5. Why FMEA not updated? → Change management process (Q8) not enforced

→ Audit focus: P1 (control plan), P3 (process parameters), Q8 (change mgmt), Q4 (CAR for this event)
```

This narrows a 2-hour audit to 4 checkpoints instead of 31, with deeper
evidence collection on those four.

---

## Remote Audit Adaptations

When travel is not feasible (low-risk commodity, short timeline, COVID-era
protocol):

| Checkpoint type | Remote substitute |
|----------------|------------------|
| Physical observation of line | Video walkthrough (screen share or recorded) |
| Document review | Supplier uploads to shared folder; auditor reviews live on call |
| Operator interviews | Video call with operator + translator if needed |
| Measurement verification | Supplier demonstrates calibration sticker / cert on camera |
| Non-conforming material area | Photo + video evidence with date/time stamp |

Remote audits **cannot** fully substitute for Areas 2 and 3. If findings are
suspected in those areas, require physical audit or third-party audit agency
before approving supplier.

---

## Re-Audit Trigger Criteria

| Condition | Re-Audit Required Within |
|-----------|--------------------------|
| Audit rating: Unacceptable | 30 days (or phase-out begins) |
| 2 or more Major findings | 60 days after corrective action deadline |
| Audit rating: Marginal + downward trend | 90 days |
| Supplier self-reports significant process change | 30 days of change |
| Customer complaint traceable to process gap found in audit | Immediate for-cause |

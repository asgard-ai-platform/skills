# GDPR Article-by-Article Reference

This reference covers the articles most commonly implicated in compliance assessments. Articles are grouped by function, not numerical order. Each entry includes the article number, what it requires, and the most common compliance failure.

---

## Legal Bases for Processing (Article 6)

The six legal bases are exhaustive — no others exist. Every processing activity must be mapped to exactly one.

| Basis | Article 6(1) | When it applies | Common mistake |
|-------|-------------|-----------------|----------------|
| Consent | (a) | When no other basis fits; subject has genuine choice | Using pre-ticked boxes, bundling consent with T&Cs, no opt-out |
| Contract | (b) | Processing necessary to perform a contract with the data subject | Extending to marketing, analytics — not necessary for contract |
| Legal obligation | (c) | Processing required by EU/member state law | Citing non-EU law (e.g., US FCPA) — must be EU/member state law |
| Vital interests | (d) | Life-or-death emergencies only | Almost never appropriate for commercial contexts |
| Public task | (e) | Public authorities exercising official functions | Not available to private companies |
| Legitimate interests | (f) | Org's interest outweighs data subject's rights | Skipping the three-part LIA test (see below) |

### Legitimate Interests Assessment (LIA) — Three-Part Test

Article 6(1)(f) requires passing all three steps before relying on legitimate interests:

**Step 1 — Purpose test**: Is the legitimate interest real?
- Concrete: fraud prevention, network security, direct marketing to existing customers
- Not concrete: "improving our product," "business analytics" without specifics

**Step 2 — Necessity test**: Is processing necessary to achieve the interest?
- Would a less privacy-invasive alternative work equally well?
- If yes → use the alternative; LI basis fails here

**Step 3 — Balancing test**: Do data subject rights override the interest?

```
Score each factor:
+ Favors processing: low sensitivity of data, data subject would reasonably expect it,
                     processing provides benefit to subject, minimal impact
- Favors subject: sensitive categories involved, subject is vulnerable (minor, employee),
                  data subject cannot reasonably expect processing, high volume
```

If the balance is negative → consent is required instead.

**LIA Documentation Template:**

```
Legitimate Interest: [specific business interest]
Necessity: [why no less-invasive alternative exists]
Balancing:
  Factors favoring LI: [list]
  Factors favoring data subject: [list]
  Conclusion: [tipped in favor of / against LI]
Safeguards added: [e.g., opt-out mechanism, pseudonymization]
```

---

## Special Category Data (Article 9)

Processing health, biometric, genetic, racial/ethnic origin, political opinion, religious belief, trade union membership, sex life/orientation data requires **both** a legal basis under Article 6 **and** an exception under Article 9(2).

Article 9 exceptions most relevant to private-sector compliance:

| Exception | Article 9(2) | Practical scope |
|-----------|-------------|-----------------|
| Explicit consent | (a) | Must be separate from general consent; cannot be bundled |
| Employment law obligation | (b) | Only when national law specifically requires processing |
| Vital interests (incapacity) | (c) | Narrow; requires subject incapable of consenting |
| Substantial public interest | (g) | Must be based on EU/member state law |
| Medical purposes | (h) | Healthcare providers, occupational medicine only |
| Public health | (i) | Requires appropriate safeguards, professional secrecy |
| Research/statistics | (j) | Requires safeguards; cannot use for individual decisions |

**No Article 9(2) exception = processing is unlawful regardless of Article 6 basis.**

Common failure: A wellness app collects health data, relies on general consent under Article 6(1)(a), and forgets that Article 9(2)(a) requires *explicit* (separate, unambiguous) consent for health data specifically.

---

## Consent Requirements (Article 7 + Recital 32/33/42/43)

Consent must be:
- **Freely given**: No genuine choice = no valid consent. Employment relationships are presumed to lack free consent (power imbalance). Conditioning service access on non-essential data processing ("consent or pay" only valid in narrow circumstances per 2023 Meta ruling).
- **Specific**: One consent per purpose. Bundled consent = invalid.
- **Informed**: Must name the controller; state each purpose; disclose retention periods; explain right to withdraw.
- **Unambiguous**: Affirmative action required. Pre-ticked boxes, silence, inactivity = invalid.
- **Withdrawable**: Must be as easy to withdraw as to give. Cannot penalize withdrawal. Processing before withdrawal remains lawful.

### Consent Record Requirements

Article 7(1): Controller must be able to demonstrate consent. Minimum record:

```json
{
  "subject_id": "hashed_identifier",
  "timestamp": "2025-03-15T14:22:00Z",
  "consent_version": "v2.3",
  "purposes": ["marketing_email", "behavioral_analytics"],
  "mechanism": "checkbox_explicit",
  "ip_address_hashed": "sha256:...",
  "withdrawal_timestamp": null
}
```

---

## Data Subject Rights (Articles 15–22)

### Rights Overview

| Right | Article | Response deadline | Key exception |
|-------|---------|------------------|---------------|
| Access | 15 | 1 month (extendable +2 months) | Cannot adversely affect others' rights |
| Rectification | 16 | 1 month | Accuracy dispute: mark as contested |
| Erasure ("right to be forgotten") | 17 | 1 month | Legal obligation to retain; public interest research |
| Restriction of processing | 18 | Without undue delay | Must be able to flag data as restricted |
| Data portability | 20 | 1 month | Only applies to data subject provided; only to automated processing |
| Object to processing | 21 | Without undue delay | Must stop processing unless compelling legitimate grounds |
| Automated decision-making | 22 | — | Right not to be subject to solely automated decisions with legal/significant effect |

### When Erasure (Article 17) Can Be Refused

Erasure must be granted when:
- Data no longer necessary for original purpose
- Consent withdrawn and no other legal basis
- Object under Article 21 and no overriding legitimate grounds
- Data unlawfully processed
- Legal obligation to erase

Erasure **may be refused** when retention is necessary for:
- Compliance with legal obligation (e.g., tax records, accounting law)
- Public interest archiving, scientific/historical research (with safeguards)
- Establishment, exercise, defense of legal claims

**Practical decision tree:**

```
Request to erase received?
  └─ Is data still necessary for original purpose?
       No → Erase
       Yes → Does another legal basis still apply?
              No → Erase
              Yes → Does subject's Art. 21 objection override it?
                     Yes → Erase
                     No → Retain; document reasoning; notify subject
```

### Data Portability (Article 20) — Scope is Narrower Than It Looks

Portability applies only when:
1. Legal basis is **consent** or **contract** (not legitimate interests, not legal obligation)
2. Processing is **automated** (no paper files)
3. Data was **provided by the data subject** (not derived or inferred)

"Data provided by the data subject" includes:
- Name, email, age, location they entered directly
- Activity data they generated (watch history, purchase history)

Does NOT include:
- Scores, risk assessments, inferences derived by the controller
- Data about the subject collected from third parties

---

## Privacy by Design and by Default (Article 25)

**By design**: Implement data protection principles at the time of determining the means of processing (system design stage), not after deployment.

**By default**: Default settings must be the most privacy-protective option. Users should have to actively choose to share more, not opt out of sharing.

Concrete checklist for a new feature before launch:

```
□ Data minimization: Does this feature collect only what's strictly necessary?
□ Purpose limitation: Is each data field tied to a documented purpose?
□ Storage default: Is retention period defined? Is auto-deletion implemented?
□ Access controls: Is access limited to roles that need it?
□ Pseudonymization: Can personal identifiers be separated from payload data?
□ Default settings: Are opt-in (not opt-out) defaults set for non-essential processing?
□ DPIA triggered? (see Article 35 below)
```

---

## Records of Processing Activities (Article 30)

Required for organizations with ≥250 employees, OR organizations whose processing is not occasional, OR processing involves special categories (Article 9) or criminal convictions (Article 10).

In practice: most businesses doing any regular customer data processing need a Record of Processing Activities (RoPA).

**Minimum RoPA fields (Article 30(1)):**

```markdown
## Processing Activity: {name}

| Field | Value |
|-------|-------|
| Controller name & contact | |
| DPO contact (if applicable) | |
| Purpose of processing | |
| Categories of data subjects | |
| Categories of personal data | |
| Categories of recipients | |
| Third-country transfers + safeguards | |
| Retention periods | |
| Security measures (general description) | |
```

Processors (Article 30(2)) must also maintain records covering: categories of processing carried out on behalf of each controller, transfers, and security measures.

---

## Data Protection Impact Assessment (Article 35)

DPIA is mandatory before processing that is "likely to result in a high risk." Must conduct DPIA when processing involves:

- Systematic and extensive profiling with significant effects
- Large-scale processing of special categories (Article 9)
- Systematic monitoring of publicly accessible areas (e.g., CCTV)
- New technologies with unclear risk profile

Supervisory authorities publish lists of processing types requiring mandatory DPIA (Article 35(4)).

**DPIA Structure (Article 35(7)):**

```
1. Systematic description of processing:
   - What data, what purposes, what legitimate interests pursued

2. Necessity and proportionality assessment:
   - Is this processing necessary for the stated purpose?
   - Is the privacy intrusion proportionate to the benefit?

3. Risk assessment:
   For each risk: [unauthorized access / unintended alteration / unavailability]
     - Likelihood: [1-5]
     - Severity: [1-5]
     - Risk score: Likelihood × Severity
     - Mitigation measure: [specific control]
     - Residual risk after mitigation: [1-5]

4. Measures envisaged:
   - Technical: encryption, pseudonymization, access controls
   - Organizational: policies, training, DPA agreements
```

If residual risk remains HIGH after mitigation → must consult supervisory authority (Article 36) before proceeding.

---

## Cross-Border Data Transfers (Chapter V, Articles 44–49)

Transfers of personal data to third countries (outside EU/EEA) require one of:

### Tier 1 — Adequacy Decision (Article 45)

Countries with EU Commission adequacy decisions (as of 2025):
Andorra, Argentina, Canada (commercial orgs), Faroe Islands, Guernsey, Israel, Isle of Man, Japan, Jersey, New Zealand, Republic of Korea, Switzerland, UK, Uruguay, USA (under EU-US Data Privacy Framework).

**Taiwan does not have an adequacy decision.** Transfers to Taiwan require Tier 2 or Tier 3 mechanisms.

### Tier 2 — Appropriate Safeguards (Article 46)

| Mechanism | Article | Notes |
|-----------|---------|-------|
| Standard Contractual Clauses (SCCs) | 46(2)(c)(d) | EU Commission templates; must use 2021 version |
| Binding Corporate Rules (BCRs) | 47 | Internal transfers within corporate group; requires supervisory authority approval |
| Approved code of conduct + binding commitments | 46(2)(e) | Sector-specific |
| Approved certification mechanism | 46(2)(f) | Sector-specific |
| Ad hoc contractual clauses | 46(3)(a) | Requires supervisory authority authorization |

**SCC Transfer Impact Assessment (TIA) — Post-Schrems II Requirement:**

Relying on SCCs is not sufficient alone. You must assess whether the third country's law undermines the SCCs:

```
1. Map the transfer: Who sends? Who receives? What data? What purpose?

2. Assess third-country law:
   - Does the country have mass surveillance laws that could access the data?
   - Do data subjects have effective legal remedies?
   Sources: EDPB's Recommendations 01/2020, country-specific legal opinions

3. If law undermines SCCs → add supplementary measures:
   Technical: End-to-end encryption (controller holds keys, not importer)
   Contractual: Enhanced notification obligations, audit rights
   Organizational: Data minimization, pseudonymization before transfer

4. If effective supplementary measures are not possible → transfer is not permissible
```

### Tier 3 — Derogations (Article 49)

Only for occasional, non-repetitive transfers when Tier 1/2 unavailable:

| Derogation | Article 49(1) | Limitation |
|-----------|--------------|------------|
| Explicit consent (informed of risks) | (a) | Cannot be used for systematic transfers |
| Contract performance with subject | (b) | Must be necessary, not merely convenient |
| Important public interest | (d) | Must be established in EU/member state law |
| Legal claims | (e) | Narrow; litigation context |
| Vital interests | (f) | Subject incapable of consenting |

**Article 49 derogations are not a general fallback.** Using them for routine business operations (e.g., regular data sync to a US SaaS tool) is not permitted.

---

## Breach Notification (Articles 33–34)

### Article 33 — Notification to Supervisory Authority

**72-hour clock starts when the controller "becomes aware."**

A processor becoming aware must notify the controller "without undue delay" (Article 33(2)) — the controller's 72-hour clock then starts.

Notify the lead supervisory authority unless:
- Breach is "unlikely to result in a risk to the rights and freedoms of natural persons" → no notification required, but must document internally

**Minimum content of notification:**

```
1. Nature of breach: categories and approximate number of data subjects affected;
                     categories and approximate number of records affected
2. DPO or contact point for more information
3. Likely consequences of the breach
4. Measures taken or proposed: containment, mitigation
```

Phased notification is permitted ("where and insofar as it is not possible to provide the information at the same time").

### Article 34 — Notification to Data Subjects

Required when breach is "likely to result in a HIGH risk" to individuals.

| Breach type | Risk level | Supervisory authority | Data subjects |
|-------------|-----------|----------------------|---------------|
| Lost encrypted device, key not compromised | Low | No | No |
| Lost encrypted device, key also compromised | Medium | Yes | Maybe |
| Ransomware on HR system, salary data exfiltrated | High | Yes | Yes |
| Phishing: credentials for marketing DB stolen | High | Yes | Yes |

**Exemptions from subject notification (Article 34(3)):**
1. Appropriate technical/organizational measures were in place (e.g., encryption rendered data unintelligible)
2. Subsequent measures eliminated the high risk
3. Disproportionate effort involved → public communication instead

---

## Data Protection Officer (Article 37–39)

### When a DPO is Mandatory (Article 37(1))

- Public authorities or bodies
- Core activities consist of large-scale, regular, systematic monitoring of data subjects
- Core activities consist of large-scale processing of special categories (Article 9) or criminal conviction data (Article 10)

"Large-scale" is not defined numerically. EDPB guidance considers:
- Number of data subjects (regional, national, international)
- Volume of data and range of data items
- Duration or permanence of the processing
- Geographical extent

### DPO Minimum Tasks (Article 39)

The DPO is not personally liable for compliance failures — the controller/processor is. The DPO is an advisor and monitor, not a decision-maker.

```
Mandatory DPO tasks:
□ Inform and advise on GDPR obligations
□ Monitor compliance (training, audits, awareness)
□ Advise on DPIAs and monitor performance
□ Cooperate with supervisory authority
□ Act as contact point for supervisory authority and data subjects
```

The DPO must not receive instructions from the controller on how to perform these tasks (Article 38(3)) — structural independence is required.

---

## Penalties (Article 83)

Two tiers of administrative fines:

**Tier 1 — Up to €10M or 2% of global annual turnover (whichever is higher):**
- Violations of: controller/processor obligations (Articles 8, 11, 25–39, 42, 43)
- Certification body violations
- Monitoring body violations

**Tier 2 — Up to €20M or 4% of global annual turnover (whichever is higher):**
- Violations of: basic principles (Articles 5, 6, 7, 9), data subject rights (Articles 12–22), transfers (Chapter V), supervisory authority orders

Factors supervisory authorities consider when setting fines (Article 83(2)):
- Nature, gravity, duration of infringement
- Intentional vs. negligent character
- Actions to mitigate damage
- Degree of cooperation with authority
- Prior infringements
- Categories of personal data affected
- How the authority learned of the infringement (self-reported vs. third-party complaint)

In addition to fines, supervisory authorities can (Article 58(2)):
- Issue warnings and reprimands
- Order compliance (temporary or permanent processing ban)
- Order erasure of data
- Suspend data flows to third countries

Data subjects can also pursue civil liability for material or non-material damage (Article 82) — courts, not supervisory authorities, handle these.

---

## Key Definitions Cheat Sheet (Article 4)

| Term | Definition | Compliance implication |
|------|-----------|----------------------|
| Personal data | Any information relating to an identified or identifiable natural person | Identifiability includes indirect identification via combination of data |
| Pseudonymous data | Data that cannot be attributed to a specific person without additional key | Still personal data; GDPR applies, but reduced risk acknowledged |
| Anonymous data | Cannot be re-identified by any means reasonably likely | GDPR does not apply — but "truly anonymous" is a high bar |
| Controller | Determines purposes and means of processing | Bears primary compliance obligations |
| Processor | Processes on behalf of controller | Must have Data Processing Agreement (Article 28); cannot subcontract without controller approval |
| Joint controllers | Two+ orgs that jointly determine purposes and means | Must have internal arrangement (Article 26); transparent to data subjects |
| Special categories | Article 9 data types | Requires Art. 9(2) exception in addition to Art. 6 basis |
| Profiling | Automated processing to evaluate personal aspects | Subject to enhanced rights (Article 22) if significant effects |

# Many-to-One Stable Matching

Many-to-one matching extends Gale-Shapley to handle cases where one side has **capacity > 1**: hospitals accept multiple residents, universities accept multiple students, companies fill multiple identical seats.

The standard one-to-one algorithm breaks here because a hospital holding `q` seats is not the same as `q` independent hospitals — accepting or rejecting a new applicant is relative to the hospital's entire current cohort.

---

## Formal Definition

**Participants:**
- `R = {r₁, r₂, ..., rₙ}` — residents (proposers), each wants exactly one position
- `H = {h₁, h₂, ..., hₘ}` — hospitals (reviewers), each has quota `qⱼ ≥ 1`
- `Σqⱼ ≥ n` (enough total capacity; some seats may go unfilled)

**Preferences:**
- Each resident ranks a subset of hospitals (acceptable list)
- Each hospital ranks all residents who listed it as acceptable

**Stable matching conditions (adapted):**

A matching `μ` is **stable** if:
1. No resident is matched to an unacceptable hospital
2. No hospital is matched beyond quota
3. No **blocking pair** `(r, h)` exists such that:
   - `r` prefers `h` over `μ(r)` (or is unmatched)
   - `h` prefers `r` over some resident in `μ(h)` (or has unfilled capacity)

---

## Algorithm: Hospital-Resident Deferred Acceptance

This is the resident-proposing version — residents get their best stable match, hospitals get their worst.

```
Input:
  residents: list of (resident_id, [hospital preferences in order])
  hospitals: list of (hospital_id, quota, [resident preferences in order])

State:
  free_residents: queue of unmatched residents
  hospital_holds: dict mapping hospital_id → set of currently held residents
  next_proposal: dict mapping resident_id → index into their preference list

Algorithm:

1. Initialize:
   free_residents = all residents
   hospital_holds[h] = {} for all h
   next_proposal[r] = 0 for all r

2. While free_residents is not empty:
   r = free_residents.dequeue()
   
   If next_proposal[r] >= len(r.preferences):
     r remains permanently unmatched (exhausted list)
     continue
   
   h = r.preferences[next_proposal[r]]
   next_proposal[r] += 1
   
   hospital_holds[h].add(r)
   
   If len(hospital_holds[h]) > h.quota:
     # Hospital is over capacity — reject worst held resident
     worst = min(hospital_holds[h], key=lambda x: h.rank(x))
     hospital_holds[h].remove(worst)
     free_residents.enqueue(worst)

3. Output:
   matching = {r: h for h in hospitals for r in hospital_holds[h]}
```

**Key difference from one-to-one**: Step 2 uses `>` quota check and ejects the *worst* current hold, not a single current match. The hospital may hold up to `q` residents simultaneously.

---

## Worked Example

Three hospitals, five residents:

```
Hospitals:
  Mass General (MGH): quota=2, ranks residents: A > C > B > D > E
  Beth Israel (BID): quota=2, ranks residents: B > A > D > C > E
  Brigham (BWH): quota=1, ranks residents: C > A > E > B > D

Residents (preference lists):
  A: MGH > BID > BWH
  B: BID > MGH > BWH
  C: BWH > MGH > BID
  D: MGH > BID
  E: BID > BWH
```

**Execution:**

Round 1 — all residents propose to top choice:
- A → MGH (MGH holds: {A}, 1/2)
- B → BID (BID holds: {B}, 1/2)
- C → BWH (BWH holds: {C}, 1/1)
- D → MGH (MGH holds: {A, D}, 2/2)
- E → BID (BID holds: {B, E}, 2/2)

All hospitals within quota. No rejections.

**Result: All 5 matched, 1 BWH seat filled, 0 open MGH seats.**

```
Matching:
  A → MGH  (rank 1 for A, rank 1 for MGH among its held)
  D → MGH  (rank 1 for D, rank 4 for MGH)
  B → BID  (rank 1 for B, rank 1 for BID)
  E → BID  (rank 2 for E, rank 5 for BID)
  C → BWH  (rank 1 for C, rank 1 for BWH)
```

**Blocking pair check:**
- (E, MGH): E prefers BID over MGH → not a blocking pair from E's side
- (D, BID): D only listed MGH and BID. D prefers MGH (current) → not a blocking pair
- No blocking pairs → **stable**

---

## More Contentious Example: Rejection Cascade

```
Hospitals:
  H1: quota=1, ranks: X > Y > Z
  H2: quota=1, ranks: Y > X > Z

Residents:
  X: H1 > H2
  Y: H1 > H2
  Z: H1 > H2
```

Round 1:
- X → H1 (H1 holds: {X})
- Y → H1 (H1 over quota: holds {X,Y}, ejects Y — H1 prefers X over Y)
- Z → H1 (H1 over quota: holds {X,Z}, ejects Z — H1 prefers X over Z)

Round 2:
- Y → H2 (H2 holds: {Y})
- Z → H2 (H2 over quota: holds {Y,Z}, ejects Z — H2 prefers Y over Z)

Z exhausts preference list → Z permanently unmatched.

```
Final matching: X → H1, Y → H2, Z → unmatched
```

This is correct and stable: Z cannot block because both H1 and H2 prefer their current match over Z.

---

## Quota-Filling Edge Cases

| Scenario | Behavior |
|---|---|
| Total quota < n residents | Some residents always unmatched; not an algorithm failure |
| Quota = 1 for all hospitals | Reduces exactly to standard one-to-one GS |
| Hospital with quota > n residents | Hospital can only be filled up to n; remainder of quota goes empty |
| Resident acceptable list is empty | Resident is permanently unmatched from Round 1 |
| Hospital preference list shorter than quota | Hospital treats unlisted residents as unacceptable (cannot fill remaining seats with them) |

---

## Proposer-Optimality Still Holds

The **IRON LAW from the parent skill applies unchanged**:

- **Resident-proposing** → every resident gets their best stable partner
- **Hospital-proposing** → every hospital gets its best stable cohort (as a set)

In practice, national residency matches (NRMP in the USA) use resident-proposing because residents are the weaker bargaining side. If hospitals proposed, they would extract all the surplus.

**Do not let stakeholders flip who proposes without understanding this.** A hospital administrator asking to "optimize for hospital preferences" is asking for hospital-proposing GS, which gives every resident their *worst* stable partner.

---

## Roth-Peranson Extension (Couples)

The real NRMP problem includes **couples** who must match to geographically co-located hospitals. This breaks the clean O(n²) guarantee and stable matching may not exist.

The Roth-Peranson algorithm handles couples by:
1. Running standard many-to-one GS
2. Inserting couple proposals as atomic units (both partners propose together)
3. If a couple causes a cascade of rejections that loop, declare instability

For most practical instances (< 5% couples), a stable matching exists and the algorithm finds it. Theoretical worst-case: no stable matching exists, but this is rare in real data.

**If your problem has couples or joint constraints: flag it explicitly.** The simple many-to-one algorithm above does not handle this.

---

## Implementation Notes

### Ranking lookup must be O(1)

The inner loop runs O(n·q) times. If `h.rank(r)` is a linear scan, total runtime becomes O(n²q). Pre-build a rank dict:

```python
# Build once per hospital
hospital_rank = {
    h_id: {r_id: idx for idx, r_id in enumerate(h_prefs)}
    for h_id, h_prefs in hospital_preferences.items()
}

# O(1) lookup
def rank_of(hospital_id, resident_id):
    return hospital_rank[hospital_id].get(resident_id, float('inf'))
```

Residents not on a hospital's list get rank `inf` — they are never chosen over anyone acceptable.

### Holding structure

Use a **max-heap keyed by hospital's rank of each resident** so ejecting the worst hold is O(log q):

```python
import heapq

# hospital_holds[h] = min-heap of (-hospital_rank, resident_id)
# Negate rank so Python's min-heap gives us the worst (highest rank number) quickly

def add_to_hospital(h_id, r_id, holds, quota):
    rank = rank_of(h_id, r_id)
    heapq.heappush(holds[h_id], (-rank, r_id))  # negated = worst at top
    if len(holds[h_id]) > quota[h_id]:
        _, ejected = heapq.heappop(holds[h_id])  # eject highest rank (worst)
        return ejected
    return None
```

### Stability verification (post-run)

```python
def find_blocking_pairs(matching, resident_prefs, hospital_prefs, hospital_holds, quota):
    blocking = []
    for r, matched_h in matching.items():
        r_pref = resident_prefs[r]
        matched_h_rank = r_pref.index(matched_h) if matched_h else len(r_pref)
        
        for h in r_pref[:matched_h_rank]:  # hospitals r prefers over current
            h_held = hospital_holds[h]
            if len(h_held) < quota[h]:
                blocking.append((r, h, "hospital has capacity"))
            else:
                worst_held_rank = max(hospital_prefs[h].index(x) for x in h_held)
                r_rank_at_h = hospital_prefs[h].index(r) if r in hospital_prefs[h] else float('inf')
                if r_rank_at_h < worst_held_rank:
                    blocking.append((r, h, "hospital prefers r over worst held"))
    return blocking
```

Zero results from this function = confirmed stable.

---

## Complexity

| Operation | Cost |
|---|---|
| Build rank dicts | O(n·m) |
| Main loop (worst case) | O(n²) proposals |
| Each proposal with heap | O(log q) |
| **Total** | **O(n² log q)** |
| Stability verification | O(n·m) |

For n=1000 residents, m=200 hospitals, q=10: roughly 10⁷ operations — fast enough to run interactively.

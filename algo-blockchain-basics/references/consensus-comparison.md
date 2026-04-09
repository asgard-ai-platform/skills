# Consensus Mechanism Comparison

## The Core Problem

Distributed nodes disagree. A consensus mechanism is the protocol that forces agreement on the canonical state of the ledger without a trusted coordinator.

The fundamental question every mechanism must answer: **how do we prove a node has the right to append the next block?**

---

## The Three Families

| Property | PoW | PoS | BFT |
|---|---|---|---|
| Sybil resistance | Computational cost | Economic stake | Identity-gated membership |
| Finality | Probabilistic | Probabilistic or instant | Instant |
| Fault tolerance | 50% hashrate | 33–67% stake (variant-dependent) | < 1/3 faulty nodes |
| Energy | High | Low | Low |
| TPS (typical) | 7–20 (Bitcoin), 15–30 (pre-merge ETH) | 10–100k (varies) | 3,000–20,000 |
| Suitable for | Public, permissionless | Public or permissioned | Permissioned, known validator set |
| Requires known validators? | No | No | Yes |

---

## Proof of Work (PoW)

### Mechanism

Nodes ("miners") find a nonce such that:

```
SHA256(SHA256(block_header || nonce)) < target
```

`target` is adjusted periodically to keep block time constant (Bitcoin: ~10 min, adjusted every 2016 blocks).

### Difficulty Formula

```
new_target = old_target × (actual_time / expected_time)
```

Bitcoin example:
- Expected: 2016 blocks × 10 min = 20,160 min
- Actual: 18,000 min (blocks came faster than expected)
- Adjustment: `new_target = old_target × (18000 / 20160)` → target decreases → harder

### Finality

PoW finality is **probabilistic**. The probability that a block gets reversed decreases exponentially with confirmations.

For Bitcoin, the probability an attacker with hashrate fraction `q` can reverse a block `z` confirmations deep:

```
If q < 0.5:
  P(success) ≈ 1 - Σ_{k=0}^{z} [Poisson(z, λ) × (1 - (q/p)^(z-k))]
```

Where `p = 1 - q`. Rule of thumb used in practice:

| Confirmations | Assumed safety |
|---|---|
| 1 | Risky (small payments only) |
| 3 | Low-value transactions |
| 6 | Standard (Bitcoin) |
| 12+ | High-value settlements |

**Iron Law implication**: For enterprise use cases where settlement must be fast and final, PoW probabilistic finality is a blocker. A 6-block Bitcoin confirmation takes ~60 minutes.

### Attack Vectors

- **51% attack**: Attacker with > 50% hashrate can double-spend or censor transactions. Cost scales with total network hashrate — feasible on small chains, prohibitively expensive on Bitcoin.
- **Selfish mining**: A pool withholds solved blocks to gain disproportionate rewards. Profitable above ~25–33% hashrate threshold.

---

## Proof of Stake (PoS)

### Mechanism

Validators lock ("stake") tokens as collateral. The protocol selects a block proposer, typically with probability proportional to stake:

```
P(validator_i selected) = stake_i / Σ(all stakes)
```

If a validator signs conflicting blocks ("equivocation"), their stake is destroyed ("slashed").

### Finality Variants

**Nakamoto-style PoS** (e.g., early Cardano Ouroboros): probabilistic finality, similar structure to PoW but without energy cost.

**Casper FFG** (Ethereum post-merge): hybrid. PoS produces blocks; a separate finality gadget runs every 32-block epoch (~6.4 min). Once 2/3 of validators attest to a checkpoint, it's finalized. Reverting a finalized block requires burning > 1/3 of staked ETH.

**Tendermint/CometBFT** (Cosmos): instant single-slot finality using BFT voting on every block (covered in BFT section).

### Nothing-at-Stake Problem

In naive PoS, validators have no cost to vote on multiple competing forks — unlike PoW where hashrate is spent. Solution: slashing conditions penalize validators who sign two blocks at the same height.

### Worked Example: Ethereum Post-Merge

- 32 ETH minimum stake per validator
- ~1 million validators as of 2024
- Block proposer selected pseudo-randomly using RANDAO
- Attestation committee (subset of validators) votes each slot (12 sec)
- Epoch = 32 slots = ~6.4 min → checkpoint candidate
- Finalization: two consecutive justified checkpoints → first is finalized

Slashing penalty for equivocation: initial penalty = `1/32 × stake`, plus correlation penalty proportional to how many validators were slashed in the same window (up to 100% if massive coordinated slashing).

---

## Byzantine Fault Tolerance (BFT)

### Mechanism

BFT protocols tolerate up to `f` faulty (Byzantine) nodes out of `n` total, requiring:

```
n ≥ 3f + 1
```

i.e., faulty nodes must be < 1/3 of total validators.

A "Byzantine" failure includes arbitrary behavior: crashing, sending conflicting messages, or deliberately lying.

### PBFT Three-Phase Protocol

Practical BFT (Castro & Liskov, 1999) is the reference implementation. For each block:

```
1. PRE-PREPARE: Primary (leader) broadcasts proposed block to all replicas
2. PREPARE:     Each replica broadcasts PREPARE(block) to all others
               → waits for 2f PREPARE messages
3. COMMIT:      Each replica broadcasts COMMIT to all others
               → waits for 2f+1 COMMIT messages → executes block
```

**Message complexity**: O(n²) per block. This is why BFT does not scale beyond ~100 validators without optimization.

### PBFT Worked Example (n=4, f=1)

```
Validators: V1 (primary), V2, V3, V4
Faulty:     V4 (Byzantine, may send garbage or nothing)

Round:
  V1 → PRE-PREPARE(block B) → V2, V3, V4
  V2 → PREPARE(B) → V1, V3, V4
  V3 → PREPARE(B) → V1, V2, V4
  V4 → PREPARE(garbage) → V1, V2, V3  [Byzantine behavior]

  V2 receives PREPARE from V3 (+ its own = 2 PREPARE messages = 2f), proceeds
  V3 receives PREPARE from V2 (+ its own = 2f), proceeds

  V2 → COMMIT(B) → all
  V3 → COMMIT(B) → all

  Both V2 and V3 received 2f+1 = 3 COMMIT messages (V1, V2, V3)
  → Block B finalized, V4's garbage ignored
```

Result: **instant finality** after the commit phase. No need to wait for additional blocks.

### Modern BFT Variants

| Protocol | Used by | Key change from PBFT |
|---|---|---|
| Tendermint / CometBFT | Cosmos, BNB Chain | Simplified 2-phase (prevote/precommit); O(n²) msgs |
| HotStuff | Diem/Aptos, Stellar | Linear message complexity O(n) via leader aggregation |
| IBFT 2.0 | Hyperledger Besu | PBFT variant, round-change on timeout |
| Raft (CFT, not BFT) | etcd, Consul | Simpler, tolerates crash failures only — NOT Byzantine |

**Raft is not BFT.** It tolerates crash-stop failures (`f < n/2`) but assumes honest nodes. Do not use Raft when participants might act maliciously.

### HotStuff Linear Complexity

HotStuff introduces a "leader aggregation" step: each phase, replicas send votes to the leader only. The leader creates a quorum certificate (QC) = threshold signature over 2f+1 votes. The next PRE-PREPARE includes the QC, proving the previous phase completed.

```
Phase:  PREPARE → PRE-COMMIT → COMMIT → DECIDE
        Each phase: n messages to leader, 1 broadcast back
        Total: O(n) per phase vs O(n²) for PBFT
```

This is why HotStuff is preferred for larger validator sets (50–200 nodes).

---

## Decision Framework

Use this checklist to select a consensus mechanism.

### Step 1: Permissioned or Permissionless?

```
Are all participants known and identity-verified?
  YES → go to Step 2 (BFT is eligible)
  NO  → PoW or PoS only (BFT requires known validator set)
```

### Step 2: Finality Requirement

```
Does the application require instant, irreversible finality?
  YES → BFT family (PBFT, Tendermint, HotStuff)
  NO  → PoW or PoS acceptable; go to Step 3
```

### Step 3: Energy and Environmental Constraints

```
Is energy consumption a concern (ESG, cost, regulations)?
  YES → PoS or BFT
  NO  → PoW remains an option
```

### Step 4: Validator Count

```
How many validators?
  < 20   → PBFT or any BFT variant
  20–100 → Tendermint or HotStuff preferred (O(n²) messages become expensive in PBFT)
  > 100  → PoS with BFT finality gadget (e.g., Ethereum Casper) or HotStuff with rotation
  > 1000 → PoW or Nakamoto-style PoS (O(n²) BFT is infeasible)
```

### Step 5: Throughput Target

```
Required TPS?
  < 100  → Any mechanism works
  100–5k → PoS or BFT
  > 5k   → Requires Layer 2, sharding, or highly optimized BFT (e.g., Aptos/HotStuff)
```

### Summary Decision Table

| Scenario | Recommended |
|---|---|
| Public currency / store of value, maximum security | PoW (Bitcoin) |
| Public smart contract platform, energy-conscious | PoS (Ethereum) |
| Enterprise supply chain, 5–20 known companies | BFT permissioned (Hyperledger Fabric, Besu IBFT) |
| Interchain / cross-org settlement, fast finality | Tendermint / CometBFT |
| High-throughput DeFi, large validator set | HotStuff-based (Aptos, Diem lineage) |
| Internal audit log, single org | Do NOT use blockchain — use a database |

The last row directly reinforces the IRON LAW: if trust already exists within a single organization, no consensus mechanism is needed because there is no Byzantine threat.

---

## Quantitative Trade-Off Summary

| Mechanism | Safety threshold | Finality time | Msg complexity | TPS ceiling (approx.) |
|---|---|---|---|---|
| PoW | < 50% hashrate | Probabilistic (~60 min for Bitcoin) | O(1) per block | ~20 |
| PoS (Nakamoto) | < 50% stake | Probabilistic | O(1) per block | ~100 |
| PoS + BFT gadget | < 33% stake for finality | 1–2 epochs (minutes) | O(n) attestations | ~100k (Ethereum target with sharding) |
| PBFT | < 33% nodes | Instant (2 rounds) | O(n²) | ~3,000–10,000 |
| HotStuff | < 33% nodes | Instant (4 phases) | O(n) | ~100,000+ |

"TPS ceiling" is protocol-level, not network-level. Real-world throughput is lower due to network latency, signature verification, and state execution.

---

## Common Misconceptions

**"PoS is just cheaper PoW."**  
No. PoW sybil resistance is physical (energy); PoS sybil resistance is economic (slashing). The security models are fundamentally different. PoS security degrades if the token price collapses (attacker can buy 33% of stake cheaply); PoW security degrades if electricity becomes cheap or ASICs are concentrated.

**"BFT is always better for enterprise."**  
BFT requires a known, stable validator set. If membership changes frequently (companies join/leave a consortium), the overhead of key management and reconfiguration is significant. For highly dynamic membership, a simpler PoA (Proof of Authority) or a federated model may be more practical despite being weaker theoretically.

**"Finality means immutability."**  
Instant finality means the protocol will not revert the block under normal operation. It does not prevent a consortium with supermajority control from colluding to rewrite history. "Immutability" in permissioned BFT is a social guarantee, not a cryptographic one — unlike large public PoW chains where the cost of rewriting history is astronomical.

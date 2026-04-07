---
name: "algo-blockchain-basics"
description: "Explain blockchain fundamentals including distributed ledger architecture, consensus mechanisms, and block structure. Use this skill when the user needs to understand blockchain concepts, evaluate whether blockchain fits a use case, or design a blockchain-based solution — even if they say 'how does blockchain work', 'do I need blockchain', or 'distributed ledger'."
metadata:
  category: "WP-49 區塊鏈演算法"
  tags: ["blockchain", "distributed-ledger", "consensus", "cryptography"]
---

# Blockchain Fundamentals

## Overview

A blockchain is a distributed, append-only ledger where blocks of transactions are cryptographically linked. Each block contains: transactions, previous block hash, timestamp, and nonce. Consensus mechanisms (PoW, PoS, BFT) ensure agreement without a central authority. Trade-off: decentralization vs performance.

## When to Use

**Trigger conditions:**
- Evaluating whether blockchain is appropriate for a use case
- Designing systems requiring distributed trust, immutability, or transparency
- Understanding blockchain architecture for integration or development

**When NOT to use:**
- When a trusted central authority exists and works well (use a database)
- When performance (thousands of TPS) is the primary requirement
- When data privacy requires deletion capability (blockchain is append-only)

## Algorithm

```
IRON LAW: Blockchain Is Useful ONLY When You Need TRUSTLESS Consensus
If participants trust each other (or trust a central authority), a
traditional database is faster, cheaper, and simpler. Blockchain's
value proposition is: untrusted parties can agree on state without
an intermediary. If trust already exists, blockchain adds overhead
with no benefit. Ask: "Who doesn't trust whom?" before choosing blockchain.
```

### Phase 1: Input Validation
Assess use case against blockchain decision criteria: multiple untrusting writers? Need for immutability? No trusted central party? Public verifiability required?
**Gate:** At least 3 of 4 criteria met to justify blockchain.

### Phase 2: Core Algorithm
**Block structure:**
1. Transactions are grouped into blocks
2. Each block header contains: previous hash, Merkle root of transactions, timestamp, nonce
3. Hash of block header links it to previous block (chain)
4. Modifying any past block invalidates all subsequent hashes

**Consensus mechanisms:**
- PoW (Proof of Work): miners compete to solve hash puzzle. Energy-intensive, secure.
- PoS (Proof of Stake): validators stake tokens. Energy-efficient, relies on economic incentives.
- BFT (Byzantine Fault Tolerance): voting-based, fast finality, requires known validator set.

### Phase 3: Verification
Check: is the use case genuinely multi-party with trust deficits? Would a simpler solution (shared database, digital signatures) suffice?
**Gate:** Blockchain justified, appropriate consensus mechanism selected.

### Phase 4: Output
Return architecture recommendation with trade-off analysis.

## Output Format

```json
{
  "recommendation": {"use_blockchain": true, "type": "permissioned", "consensus": "PBFT", "platform": "Hyperledger Fabric"},
  "trade_offs": {"decentralization": "medium", "throughput_tps": 3000, "finality_seconds": 2, "energy": "low"},
  "metadata": {"use_case": "supply chain provenance", "participants": 5, "trust_level": "low"}
}
```

## Examples

### Sample I/O
**Input:** 5 companies tracking seafood provenance from boat to restaurant
**Expected:** Permissioned blockchain recommended (known participants, no trust, need immutable audit trail). Platform: Hyperledger Fabric or similar.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Single company internal use | Don't use blockchain | Trust already exists internally |
| Need to delete data (GDPR) | Blockchain problematic | Immutability conflicts with right to erasure |
| Public transparency required | Public/consortium chain | Permissionless or hybrid |

## Gotchas

- **Blockchain ≠ cryptocurrency**: Blockchain is the technology; cryptocurrency is one application. Many blockchain use cases have nothing to do with tokens.
- **Immutability is a spectrum**: "Permissioned" blockchains can be rewritten by consortium agreement. True immutability only exists in large public chains.
- **Oracle problem**: Blockchain guarantees integrity of data ON the chain. It cannot guarantee the accuracy of data ENTERING the chain from the real world. Garbage in = immutable garbage.
- **Scalability trilemma**: Decentralization, security, scalability — pick two. No blockchain optimizes all three simultaneously.
- **Regulatory uncertainty**: Legal status of blockchain records, smart contracts, and tokens varies by jurisdiction. Consult legal before production deployment.

## References

- For consensus mechanism comparison, see `references/consensus-comparison.md`
- For blockchain decision framework, see `references/decision-framework.md`

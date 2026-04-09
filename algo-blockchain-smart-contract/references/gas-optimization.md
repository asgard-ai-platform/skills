# Gas Optimization

Gas is the unit measuring computational work on Ethereum. Every opcode has a fixed gas cost; transactions with insufficient gas revert (state changes undo, gas is still consumed). Optimization reduces cost for users and prevents hitting block gas limits.

---

## Gas Cost Hierarchy

From most to least expensive, per operation category:

| Operation | Gas Cost (approx.) | EIP Reference |
|---|---|---|
| `SSTORE` cold slot (new value) | 20,000 | EIP-2929 |
| `SSTORE` cold slot (update non-zero) | 2,900 | EIP-2929 |
| `SSTORE` warm slot | 100 | EIP-2929 |
| `SLOAD` cold slot | 2,100 | EIP-2929 |
| `SLOAD` warm slot | 100 | EIP-2929 |
| `CALL` / external call | 700 base + more | |
| `MLOAD` / `MSTORE` (memory) | 3 | |
| `CALLDATALOAD` | 3 | |
| Arithmetic (`ADD`, `SUB`, `MUL`) | 3–5 | |
| `LOG` (event with 3 topics, 32 bytes) | ~1,500 | |
| Contract deployment (per byte) | 200 | |

**Key takeaway**: Storage reads/writes dominate. One cold `SLOAD` costs as much as ~700 arithmetic ops.

---

## Storage Layout Optimization

### Variable Packing

EVM storage slots are 32 bytes each. Variables smaller than 32 bytes that are declared consecutively get packed into a single slot by the Solidity compiler — but only if they fit.

**Unpacked (bad) — 3 slots used:**
```solidity
uint256 a;   // slot 0 (32 bytes)
uint128 b;   // slot 1 (16 bytes, slot wasted)
uint128 c;   // slot 2 (16 bytes, slot wasted)
```

**Packed (good) — 2 slots used:**
```solidity
uint256 a;   // slot 0 (32 bytes)
uint128 b;   // slot 1 (16 bytes)
uint128 c;   // slot 1 (16 bytes, packed with b)
```

**Packed with bool/address (common pattern) — 1 slot:**
```solidity
address owner;    // 20 bytes
bool    active;   // 1 byte
uint88  balance;  // 11 bytes
// Total: 32 bytes → fits in 1 slot
```

**Rule**: Group smaller types together. Put `uint256` / `bytes32` alone. Never interleave large types between small ones.

### Struct Packing

Same rule applies inside structs. The compiler packs struct fields in declaration order:

```solidity
// Bad: 3 slots per item in an array
struct Order {
    uint256 amount;    // slot A
    address buyer;     // slot B (only 20 bytes used)
    uint256 price;     // slot C
    bool    filled;    // slot D (only 1 byte used)
}

// Good: 2 slots per item
struct Order {
    uint256 amount;    // slot A
    uint256 price;     // slot B
    address buyer;     // slot C: 20 bytes
    bool    filled;    // slot C: 1 byte (packed with buyer)
}
```

For an array of 1,000 `Order` structs, the packed version saves 2,000 storage slots — at 20,000 gas each for initial writes, that's 40M gas saved on population alone.

---

## SSTORE Patterns

### Cache Storage Values in Memory

Every `SLOAD` of a cold slot costs 2,100 gas. If you read the same slot multiple times, cache it:

```solidity
// Bad: 2 cold SLOADs (4,200 gas)
function bad() external {
    require(balances[msg.sender] > 0);
    uint256 amount = balances[msg.sender];
    balances[msg.sender] = 0;
}

// Good: 1 cold SLOAD + 1 warm (2,200 gas)
function good() external {
    uint256 bal = balances[msg.sender];  // cache
    require(bal > 0);
    balances[msg.sender] = 0;
}
```

### Avoid Writing Zero to Already-Zero Slots

Writing a non-zero value to a zero slot costs 20,000 gas. Writing zero to a non-zero slot costs 2,900 gas but triggers a 4,800 gas *refund* (capped at 20% of total gas used as of EIP-3529). Writing zero to an already-zero slot costs 100 gas (the base write).

**Implication**: Don't store boolean flags as `0`/`1` in separate slots if you can encode them in an existing variable. Delete mappings when entries become zero to reclaim some refund — but don't chase refunds as a strategy; they're limited post-EIP-3529.

### Counting Patterns

For counters incremented in a loop, accumulate in memory and write once:

```solidity
// Bad: N SSTOREs
for (uint i = 0; i < n; i++) {
    totalSupply += amounts[i];
}

// Good: 1 SSTORE
uint256 sum = totalSupply;
for (uint i = 0; i < n; i++) {
    sum += amounts[i];
}
totalSupply = sum;
```

---

## Calldata vs Memory vs Storage

| Location | Where | Cost model |
|---|---|---|
| `calldata` | Read-only input to `external` functions | 4 gas/zero byte, 16 gas/non-zero byte (EIP-2028) |
| `memory` | Temporary within function call | 3 gas/word, grows quadratically beyond 724 words |
| `storage` | Persistent on-chain state | 100–20,000 gas/access |

**Use `calldata` for read-only function parameters** instead of `memory`:

```solidity
// memory: copies array into memory
function sum(uint256[] memory arr) external pure returns (uint256) { ... }

// calldata: reads directly from transaction data, no copy
function sum(uint256[] calldata arr) external pure returns (uint256) { ... }
```

For a 100-element array, `calldata` avoids copying 3,200 bytes into memory. At ~3 gas/word, that's ~300 gas saved just on the copy — plus the memory expansion cost.

---

## Events vs Storage: When to Use Each

Events (`LOG` opcodes) are cheap, non-queryable by contracts, but queryable off-chain via RPC. Storage is expensive but queryable on-chain.

**Use events when:**
- Data is only needed off-chain (analytics, UI, indexers)
- Recording history (transfer logs, price history)
- The data never needs to be read by another contract

**Use storage when:**
- Another contract must read the value
- The contract's own logic depends on the value
- You need the value to enforce invariants

**Cost comparison** for 256-bit value:
- `SSTORE` (new slot): 20,000 gas
- `LOG1` (1 topic, 32 bytes data): ~2,000 gas

Emitting an event instead of storing costs ~10× less. If you have audit trail data that doesn't gate logic, use events.

---

## Function Selector Optimization

The first 4 bytes of calldata identify the function (keccak of signature, truncated). The EVM must compare against all known selectors. If a function is called frequently, you want its selector to sort early in the comparison list — but this is minor (a few gas). More impactful:

**Mark functions `external` not `public`** when they're only called from outside the contract. `external` functions can read arguments directly from calldata; `public` functions copy arguments to memory.

**Mark view/pure correctly**: functions that don't modify state should be `view` or `pure`. This doesn't affect on-chain gas when called from another contract (it still costs gas), but enables free off-chain calls via `eth_call`.

---

## Loop Optimization

### Unchecked Arithmetic for Counters

In Solidity 0.8+, arithmetic is checked by default (reverts on overflow). Checked arithmetic costs extra per operation (~20 gas overhead per check). For loop counters that cannot overflow (e.g., iterating up to array length), wrap in `unchecked`:

```solidity
// 0.8+: each i++ has overflow check
for (uint256 i = 0; i < arr.length; i++) { ... }

// Cheaper: skip overflow check on counter
for (uint256 i = 0; i < arr.length; ) {
    // ... loop body
    unchecked { ++i; }  // ++i is cheaper than i++ (no temp variable)
}
```

Note: only use `unchecked` when you're certain overflow cannot occur. Do not apply it to user-supplied arithmetic.

### Cache Array Length

Accessing `arr.length` in a loop condition reads the storage slot on each iteration if `arr` is a storage array:

```solidity
// Bad: SLOAD on every iteration if arr is storage
for (uint i = 0; i < storageArr.length; i++) { ... }

// Good: cache length
uint256 len = storageArr.length;
for (uint i = 0; i < len; i++) { ... }
```

For memory arrays, `arr.length` reads from memory (cheap), so caching is less critical but still a micro-optimization.

---

## Worked Example: Airdrop Contract

Scenario: distribute ERC-20 tokens to 500 addresses.

### Naive approach (expensive)

```solidity
function airdrop(address[] calldata recipients, uint256 amount) external {
    for (uint i = 0; i < recipients.length; i++) {
        token.transfer(recipients[i], amount);  // external call each iteration
    }
}
```

Each `transfer` call: ~700 base gas for `CALL` + 2 `SSTORE`s inside ERC-20 (~25,000 gas) = ~26,000 gas × 500 = **13M gas**. At 30M block gas limit, this barely fits one airdrop.

### Optimized approach

**Option A — Batch transfer with Merkle claim** (pull-based, see SKILL.md Gotcha: Pull over Push):

Store a Merkle root (one `SSTORE`, 20,000 gas). Recipients call `claim()` individually:
- Verify Merkle proof (off-chain data, calldata cost only)
- Mark claimed (1 `SSTORE` per claimer)
- Transfer tokens (1 external call)

Deployment cost: ~20,000 gas for root. Per-claim: ~50,000 gas, but spread across 500 transactions from claimers. Admin pays nothing per recipient.

**Option B — Tight loop with calldata optimization:**

```solidity
function airdrop(
    address[] calldata recipients,
    uint256[] calldata amounts
) external onlyOwner {
    uint256 len = recipients.length;
    for (uint256 i = 0; i < len; ) {
        token.transfer(recipients[i], amounts[i]);
        unchecked { ++i; }
    }
}
```

Savings vs naive: cached length (eliminates N `SLOAD`s on memory array), `++i` instead of `i++`, `calldata` parameters. Rough saving: ~500 × 50 gas = 25,000 gas on overhead alone.

**Which to choose:**

| Factor | Merkle claim | Tight loop |
|---|---|---|
| Admin pays gas | No | Yes |
| Recipients can delay claiming | Yes | No |
| Contract complexity | Higher | Lower |
| Works if recipients are contracts | Needs care | Same |
| Gas per token delivered | Lower for admin | Lower overall if all claim |

---

## Decision Framework

Before writing a gas optimization, answer:

1. **Is this storage?** → Pack variables, cache reads, minimize writes.
2. **Is this a loop?** → Cache length, use `unchecked` counter, accumulate and write once.
3. **Is this a parameter?** → Use `calldata` for external read-only arrays/structs.
4. **Is this data needed on-chain?** → If no, emit event instead of storing.
5. **Is this an external call?** → Each call costs 700+ gas. Batch where possible, or redesign to pull pattern.

**Optimization priority order** (highest impact first):

1. Eliminate unnecessary storage slots (packing, event vs storage choice)
2. Reduce `SLOAD`/`SSTORE` counts (caching, write-once patterns)
3. Replace memory with calldata on external function inputs
4. Loop micro-optimizations (`unchecked`, cached length)
5. Selector and modifier micro-optimizations

Do not invert this order. A tight loop that writes to storage on every iteration is still expensive regardless of `unchecked` counters.

---

## Tooling

**Hardhat Gas Reporter** — prints per-function gas usage on test run:
```
npm install --save-dev hardhat-gas-reporter
```

Add to `hardhat.config.js`:
```js
gasReporter: { enabled: true, currency: "USD" }
```

**Foundry `forge test --gas-report`** — built-in gas table, no plugin needed. Run with:
```
forge test --gas-report
```

**Slither** — static analyzer that flags known gas anti-patterns alongside security issues:
```
slither . --detect costly-loop,unused-return
```

Use gas reports to baseline before and after optimization. Never optimize without measuring — Solidity's compiler (`--optimize --runs N`) already handles many micro-optimizations, and hand-optimizing compiler-handled patterns wastes time.

The `--runs` parameter in `solc` optimizer tells it how many times functions are expected to be called. High `--runs` (e.g., 200) optimizes for runtime gas at the cost of deployment size. Low `--runs` (e.g., 1) optimizes for deployment gas. Set based on actual usage patterns.

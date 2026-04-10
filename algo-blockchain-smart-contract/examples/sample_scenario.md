# Example: 跨境藝術品交易託管合約

## Scenario

ArtVault 是一家台灣新創，協助收藏家在鏈上交易實體藝術品。他們的流程是：

1. 買家將 USDC 存入平台
2. 賣家寄送實體作品
3. 買家收到後確認，款項釋出給賣家
4. 若發生爭議，第三方仲裁人介入裁決

他們已有一個基礎的 Solidity escrow 合約，但創辦人擔心三件事：
- 「合約有 reentrancy 問題嗎？」
- 「仲裁人能不能捲款跑路？」
- 「如果我們要升級合約，現有資金會卡住嗎？」

---

## Analysis

### Phase 1: Input Validation

**合約目的**：三方托管（buyer / seller / arbiter），釋放條件為買家確認或仲裁裁決。

**必須上鏈的邏輯：**
- 資金保管（USDC transferFrom / release）
- 狀態機（AWAITING_DELIVERY → COMPLETE / DISPUTED）
- 存取控制（誰能呼叫 confirm、dispute、resolve）

**可以下鏈的邏輯：**
- 物流追蹤號碼（hash 上鏈即可）
- 仲裁結果理由文字（IPFS 存儲，鏈上只存 CID）

**Gate 通過**：業務邏輯明確，上鏈必要性有根據。

---

### Phase 2: Core Algorithm

#### 狀態變數設計（4 個）

```solidity
address public buyer;
address public seller;
address public arbiter;
EscrowState public state; // AWAITING_DELIVERY | COMPLETE | DISPUTED | REFUNDED
```

儲存最小化：不儲存物流資訊，僅存 `bytes32 trackingHash`。

#### 函式設計（5 個）

| 函式 | 呼叫者 | 動作 |
|------|--------|------|
| `deposit(uint256 amount)` | buyer | 將 USDC 轉入合約，state → AWAITING_DELIVERY |
| `confirmDelivery()` | buyer | state → COMPLETE，釋出 USDC 給 seller |
| `raiseDispute()` | buyer 或 seller | state → DISPUTED |
| `resolve(bool releaseTo Seller)` | arbiter | 仲裁裁決，釋出資金 |
| `refund()` | arbiter | 退款給 buyer（超時或賣家違約） |

#### 安全模式應用

**問題 1：Reentrancy 風險**

原始寫法（危險）：
```solidity
// ❌ 先轉帳再改狀態 — reentrancy 入口
function confirmDelivery() external {
    require(msg.sender == buyer);
    token.transfer(seller, balance);  // 先轉
    state = EscrowState.COMPLETE;     // 後改狀態
}
```

套用 Checks-Effects-Interactions 修正：
```solidity
// ✅ 先改狀態，再轉帳
function confirmDelivery() external {
    require(msg.sender == buyer, "only buyer");
    require(state == EscrowState.AWAITING_DELIVERY, "wrong state");
    // Checks ↑  Effects ↓
    state = EscrowState.COMPLETE;
    uint256 amount = deposited;
    deposited = 0;
    // Interactions ↓
    bool ok = token.transfer(seller, amount);
    require(ok, "transfer failed");
}
```

**問題 2：仲裁人捲款風險**

仲裁人只能裁決資金去向（buyer or seller），不能將資金轉給自己：

```solidity
function resolve(bool releaseToSeller) external {
    require(msg.sender == arbiter, "only arbiter");
    require(state == EscrowState.DISPUTED, "not disputed");
    state = releaseToSeller ? EscrowState.COMPLETE : EscrowState.REFUNDED;
    address recipient = releaseToSeller ? seller : buyer;
    uint256 amount = deposited;
    deposited = 0;
    bool ok = token.transfer(recipient, amount);
    require(ok, "transfer failed");
}
```

仲裁人角色由多簽錢包（2-of-3 Gnosis Safe）持有，不是單一 EOA。

**問題 3：升級合約但資金卡住**

建議採 **透明代理模式（EIP-1967）**：

```
ProxyContract (持有資金 + storage)
    ↓ delegatecall
LogicContract v1 → v2 → v3
```

- 升級時只替換 LogicContract，Proxy 的 storage 和餘額不動
- 升級權限鎖定在 2-of-3 multisig，不是單一 owner
- 升級前需通過 48 小時 timelock（防止突襲升級攻擊）

---

### Phase 3: Verification

**測試覆蓋：**

| 測試案例 | 結果 |
|---------|------|
| 正常流程：deposit → confirm → release | ✅ |
| 仲裁流程：deposit → dispute → resolve(seller) | ✅ |
| Reentrancy 攻擊模擬 | ✅ 阻擋 |
| 非 buyer 呼叫 confirmDelivery | ✅ revert |
| 仲裁人嘗試轉款給自己 | ✅ 不可能（函式不支援） |
| 已 COMPLETE 狀態重複呼叫 confirm | ✅ revert |

**自動化掃描（Slither）：**
- 原始版本：3 個 high severity（2 reentrancy + 1 unchecked return）
- 修正後：0 high，1 info（gas optimization 建議）

**Testnet 部署**：Sepolia，交易 hash 0x3a7f…d209，gas 實際消耗 187,432。

**Gate 通過**：測試全過，Slither clean，testnet 正常。

---

## Result

```json
{
  "contract": {
    "name": "ArtVaultEscrow",
    "functions": 5,
    "state_variables": 4,
    "access_roles": ["buyer", "seller", "arbiter"]
  },
  "security": {
    "audit_status": "passed",
    "patterns_used": [
      "checks_effects_interactions",
      "pull_payment",
      "transparent_proxy_eip1967",
      "multisig_arbiter"
    ],
    "known_risks": [
      "oracle_dependency: 無，此合約不依賴外部資料",
      "upgrade_risk: 緩解 — 48h timelock + 2-of-3 multisig"
    ]
  },
  "metadata": {
    "platform": "ethereum",
    "language": "solidity_0.8.24",
    "estimated_gas": 187432,
    "testnet": "sepolia",
    "proxy_pattern": "EIP-1967 transparent proxy"
  }
}
```

**三個原始疑慮的結論：**

1. **Reentrancy**：改為 CEI 模式後消除。舊版 DAO hack 路徑已封閉。
2. **仲裁人捲款**：函式設計層面不可能；再由多簽持有仲裁角色雙重保護。
3. **升級卡資金**：透明代理模式下，資金永遠在 Proxy，升級只換邏輯層，不影響餘額。

> **注意**：此合約仍需正式安全審計（Certik、OpenZeppelin Audits）再部署主網。測試網驗證 ≠ 生產就緒。
```

以上是 `sample_scenario.md` 的完整內容。要我直接寫入 `algo-blockchain-smart-contract/examples/sample_scenario.md` 嗎？

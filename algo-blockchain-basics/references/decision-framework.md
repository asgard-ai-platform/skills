# Blockchain Decision Framework

## Core Question: Who Doesn't Trust Whom?

Before any technical evaluation, answer this:

> **「哪些參與者彼此不信任，但又必須共享同一份資料？」**

如果無法具體指出「不信任的對象」，就不需要區塊鏈。

---

## The 4-Criteria Gate (Phase 1)

來自 SKILL.md Phase 1：**至少滿足 3 / 4 才進入區塊鏈評估**。

| # | Criteria | Yes / No |
|---|----------|----------|
| 1 | **Multiple untrusting writers** — 有多個組織或個人需要寫入資料，且彼此不完全信任 | |
| 2 | **Immutability required** — 歷史紀錄不可竄改，稽核軌跡需要可驗證 | |
| 3 | **No trusted central party** — 沒有所有參與者都願意信任的中央機構 | |
| 4 | **Public verifiability** — 外部驗證者需要獨立核實資料（監管機構、最終消費者等）| |

**Score 0-2 → Stop. Use a database.**  
**Score 3-4 → Continue to Step 2.**

---

## Step 2: Permissioned vs. Permissionless

通過 Phase 1 Gate 後，第二個決策是鏈的類型。

```
參與者身份是否已知且受控？
│
├── YES (已知的企業/機構清單)
│   └── → Permissioned (許可鏈)
│       例：Hyperledger Fabric, R3 Corda, Quorum
│
└── NO (任何人都可參與)
    └── → Permissionless (無許可鏈)
        例：Ethereum, Bitcoin, Solana
```

### Key Differentiators

| Dimension | Permissioned | Permissionless |
|-----------|-------------|----------------|
| 參與者 | 已知、受邀 | 匿名、公開 |
| 共識機制 | BFT / PBFT (voting-based) | PoW / PoS |
| TPS | 1,000 – 10,000+ | 7 – 4,000（視鏈而定）|
| Finality | 幾秒（即時最終性）| 幾分鐘（概率最終性）|
| 隱私 | 可設存取控制 | 預設公開 |
| 能耗 | 低 | PoW 極高；PoS 低 |
| 適用場景 | B2B 供應鏈、金融清算、聯盟 | 公共代幣、去中心化應用 |

---

## Step 3: Simpler Alternatives Checklist

區塊鏈是高成本方案。先確認這些更簡單的方案是否已被排除：

### Alternative A: Shared Database with Audit Log
- **適用時機**：所有寫入方都信任同一間公司（SaaS 供應商、銀行等）
- **辨識方式**：參與者願意簽約讓第三方持有資料
- **工具**：PostgreSQL + append-only audit table, AWS QLDB

### Alternative B: Digital Signatures + Timestamp Authority
- **適用時機**：需要不可否認性（non-repudiation）但不需要共享狀態
- **辨識方式**：各方只需簽署自己的文件；沒有跨方狀態同步問題
- **工具**：PKI, RFC 3161 timestamp, DocuSign API

### Alternative C: Multi-party Database with Access Controls
- **適用時機**：多方讀寫，但有可信任的聯盟或監管機構做仲裁
- **辨識方式**：存在「仲裁者」角色，即便不受歡迎，仍可被法律強制執行

**若以上三者任何一個可行 → 優先選擇，不用區塊鏈。**

---

## Decision Tree (Complete)

```
需要多方共享資料？
│
├── NO → 單一資料庫即可
│
└── YES
    │
    參與者彼此信任，或有共同信任的中央機構？
    │
    ├── YES → Shared DB / QLDB / 傳統 PKI
    │
    └── NO (信任缺口存在)
        │
        需要資料不可竄改的稽核軌跡？
        │
        ├── NO → 考慮 append-only log + 數位簽章
        │
        └── YES
            │
            參與者身份已知？
            │
            ├── YES → Permissioned Blockchain
            │         → 選 BFT-based 共識
            │         → 平台：Hyperledger Fabric, Corda
            │
            └── NO → Permissionless Blockchain
                      → 選 PoS（能源考量）或 PoW（最高安全性）
                      → 平台：Ethereum, Solana
```

---

## Step 4: Consensus Mechanism Selection (Permissioned Path)

進入 Permissioned Blockchain 後，依節點數量與容錯需求選共識：

### PBFT (Practical Byzantine Fault Tolerance)
- **容錯**：最多容忍 ⌊(n-1)/3⌋ 個惡意節點
- **公式**：需要 n ≥ 3f + 1，其中 f = 預期惡意節點數
- **例**：5 個節點 → 容忍 1 個惡意節點。10 個節點 → 容忍 3 個。
- **限制**：節點數量 > 100 時通訊複雜度 O(n²) 導致效能下降
- **適用**：聯盟鏈、節點數 < 20、需要即時最終性

### Raft (Crash Fault Tolerance only)
- **容錯**：只容忍崩潰，不容忍惡意行為
- **公式**：需要 n ≥ 2f + 1 個節點
- **適用**：所有節點來自同一信任域（例：同一企業的多個資料中心）

### 選擇指引

```
節點來自多個不互信組織？
├── YES → PBFT 或 Istanbul BFT (IBFT)
└── NO  → Raft 即可（更快、更簡單）

節點數 > 50？
├── YES → 考慮 HotStuff 或 Tendermint（O(n) 複雜度）
└── NO  → PBFT 可行
```

---

## Worked Example: 海鮮溯源系統

**情境**：5 家企業（漁船公司、加工廠、物流商、超市、監管機構）需要追蹤海產從捕撈到上架的完整履歷。

### Phase 1 Gate 評估

| Criteria | 評估 | 結論 |
|----------|------|------|
| Multiple untrusting writers | 5 家不同公司，商業競爭關係 | ✅ YES |
| Immutability required | 食安事故需要可追溯的不可竄改紀錄 | ✅ YES |
| No trusted central party | 無單一機構所有參與者都願意信任 | ✅ YES |
| Public verifiability | 消費者掃碼驗真、監管機構稽核 | ✅ YES |

**Score: 4/4 → 進入評估**

### Step 2: 鏈類型

參與者已知（固定 5 家企業）→ **Permissioned**

### Step 3: 排除替代方案

- Shared DB：哪家公司持有？各方不接受。❌
- Digital Signatures only：需要跨方狀態（「這批貨現在在誰手上？」）❌
- Multi-party DB with arbiter：監管機構可做仲裁，但政治敏感，各方不願 ❌

**結論**：替代方案皆不可行

### Step 4: 共識機制

5 個節點，全來自不同組織 → **PBFT**  
驗算：n=5, f=1, 3(1)+1=4 ≤ 5 ✅

### 最終建議

```json
{
  "recommendation": {
    "use_blockchain": true,
    "type": "permissioned",
    "consensus": "PBFT",
    "platform": "Hyperledger Fabric"
  },
  "trade_offs": {
    "decentralization": "medium",
    "throughput_tps": 3000,
    "finality_seconds": 2,
    "energy": "low"
  },
  "metadata": {
    "use_case": "supply chain provenance",
    "participants": 5,
    "trust_level": "low"
  }
}
```

---

## Anti-Patterns: 常見誤用情境

### "我們需要區塊鏈來確保資料安全"
**問題**：傳統資料庫配合加密 + 存取控制同樣可以確保安全。  
**診斷問題**：安全需求不等於信任缺口。詢問「誰不信任誰」。

### "我們需要區塊鏈讓流程更透明"
**問題**：透明度可由公開 API 或唯讀副本達成，不需區塊鏈。  
**診斷問題**：透明度的需求對象是誰？如果只是「管理層想看 dashboard」，用 BI 工具即可。

### "競爭對手都在做區塊鏈"
**問題**：完全不是技術決策依據。  
**診斷問題**：回到 4-Criteria Gate，得分多少？

### "我們有很多資料要存"
**問題**：區塊鏈是世界上最昂貴的資料庫之一。每個節點存全份資料。  
**診斷問題**：高容量資料存鏈外（IPFS 或傳統存儲），鏈上只存雜湊值。

---

## Oracle Problem 補充（決策時的額外考量）

區塊鏈保證鏈上資料的完整性，但**無法保證進入鏈的資料是真實的**。

```
真實世界  →  Oracle  →  區塊鏈
(溫度、重量)   (感測器、API)   (不可竄改紀錄)
                ↑
          信任缺口在這裡
```

**決策影響**：如果使用案例的核心信任問題在於「輸入資料是否真實」（例：農產品有機認證），光靠區塊鏈無法解決。需要額外的 IoT 驗證、第三方稽核或零知識證明。

在決策時須明確回答：**Oracle 的信任問題如何處理？**

---

## Quick Reference Card

```
得分 0-2/4  → 資料庫
得分 3-4/4，有中央仲裁者可接受  → QLDB 或 append-only DB
得分 3-4/4，參與者已知，無中央仲裁者  → Permissioned (Fabric/Corda)
得分 3-4/4，參與者未知，需公開驗證  → Permissionless (Ethereum/Solana)
任何情況下資料需要刪除 (GDPR)  → 重新評估，區塊鏈本質上不相容
```

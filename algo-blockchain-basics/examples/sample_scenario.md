# Example: 台灣漁獲溯源平台的區塊鏈適用性評估

## Scenario

**公司：** 鮮道科技（FreshTrace Co.），台灣新創，2024 年成立  
**用戶問題：**

> 我們正在幫台灣漁業署和五家大型漁獲批發商建立一套「漁獲溯源系統」。從出海捕撈、回港卸魚、冷鏈運輸、批發市場拍賣、到最終餐廳交貨，每個環節都要記錄。
>
> 政府官員、批發商、餐廳老闆三方互不信任，都擔心對方造假（尤其是產地標示）。漁業署要求資料不能被任何一方單方面竄改，且需公開給消費者查詢。
>
> 我們在考慮用區塊鏈。但工程師說「用 PostgreSQL 加上 audit log 就夠了」，PM 說「區塊鏈才有說服力」。你覺得誰對？

**背景數字：**
- 參與方：漁業署（1）＋大型批發商（5）＋冷鏈物流（2）＋餐廳（300+）
- 預期寫入量：每日約 4,000 筆溯源紀錄
- 查詢量：每日約 50,000 次消費者掃碼查詢
- 需保留年限：10 年
- GDPR/個資法：需儲存漁船船員姓名（但不需刪除，屬作業紀錄）

---

## Analysis

### Phase 1：Input Validation — 四項區塊鏈適用標準

| 標準 | 問題 | 本案狀況 | 符合？ |
|------|------|----------|--------|
| 多方互不信任的寫入者 | 政府、批發商、物流、餐廳各自上傳資料 | ✅ 三方明確互不信任，且漁業署是裁判方而非中立方 | ✅ |
| 需要不可竄改性 | 產地標示一旦上鏈不能被任何單方修改 | ✅ 漁業署明確要求，防止業者回溯竄改 | ✅ |
| 沒有可信的中央權威 | 漁業署雖是政府機關，但被批發商質疑是否中立 | ✅ 業者不信任政府單方面維護的系統 | ✅ |
| 需要公開可驗證性 | 消費者要能自行驗證，不只是「相信廠商說的」 | ✅ 消費者掃碼需看到可驗證的鏈上資料 | ✅ |

**Gate 結果：4/4 標準全部符合 → 區塊鏈有正當理由。**

工程師說的「PostgreSQL + audit log」在技術上可行，但無法解決**信任問題**：audit log 由誰維護？漁業署。批發商憑什麼相信漁業署的 audit log 沒有被竄改？這正是區塊鏈存在的意義。

---

### Phase 2：核心架構設計

**參與方分析（Who doesn't trust whom?）**

```
漁業署  ←→  不信任  ←→  批發商（懷疑產地造假）
批發商  ←→  不信任  ←→  物流（懷疑冷鏈斷鏈）
餐廳    ←→  不信任  ←→  批發商（懷疑以次充好）
消費者  ←→  不信任  ←→  整個供應鏈
```

**區塊鏈類型選擇：**

- **公鏈（Ethereum）**：寫入成本高（每筆 gas fee），4,000 筆/日在主網費用難以接受；TPS 不夠；❌
- **私有鏈**：任何人都可以重置，失去不可竄改意義；❌
- **聯盟鏈（Permissioned Consortium）**：已知參與方（漁業署＋8家業者），高 TPS，低能耗，法規合規；✅

**共識機制選擇：**

- PoW：能耗高，無必要；❌
- PoS：適合公鏈場景；❌
- **PBFT（Practical Byzantine Fault Tolerance）**：已知驗證節點，快速最終性（2 秒），支援 f < n/3 的惡意節點容錯；✅

**平台選擇：Hyperledger Fabric**
- 原因：支援 Channel 隔離敏感商業資料（批發價格不需全員可見）；原生支援 MSP（Membership Service Provider）管理各方憑證；台灣政府 IT 採購有 Linux Foundation 開源合規優勢。

**Block 結構（本案溯源紀錄）：**

```
Block Header:
  prev_hash:       sha256(前一個區塊 header)
  merkle_root:     sha256(本批次所有溯源交易)
  timestamp:       2025-03-15T08:23:11+08:00
  block_number:    18472

Transaction (單筆溯源紀錄):
  tx_id:           "CATCH-20250315-002341"
  actor:           "批發商_大洋水產"  (MSP 憑證簽署)
  action:          "transfer"
  fish_batch_id:   "TUNA-20250315-KH001"
  location:        "高雄前鎮漁港"
  weight_kg:       320
  temperature_c:   -18
  prev_actor:      "漁船_永泰168號"
```

**Oracle Problem 處置：**

本案最大風險不是鏈上資料被竄改，而是「上鏈的資料一開始就是假的」。  
解法：漁業署在卸魚碼頭裝設 IoT 感測器（重量計＋GPS＋溫度計）自動上傳，減少人工填寫。但這只是緩解，無法完全消除。

---

### Phase 3：Verification

**再次確認：更簡單的方案夠用嗎？**

| 方案 | 為何不夠 |
|------|----------|
| PostgreSQL + audit log | 漁業署單方面維護，批發商不信任；可被 DBA 竄改 |
| 數位簽章（各方簽署文件） | 解決真實性但不解決可追溯的歷史狀態；無共識機制 |
| 公雲（AWS）中立第三方 | 誰付錢誰說了算；漁業署不願資料存外國雲端 |
| **聯盟鏈（本案選擇）** | 所有方共同維護節點，無單點竄改可能；滿足全部需求 ✅ |

**Scalability Trilemma 確認：**

本案選擇「安全性 ＋ 可擴展性」，犧牲部分去中心化（聯盟鏈不完全去中心）。這是正確取捨：參與方已知，無需完全去中心。

---

## Result

```json
{
  "recommendation": {
    "use_blockchain": true,
    "type": "permissioned",
    "consensus": "PBFT",
    "platform": "Hyperledger Fabric",
    "network_nodes": 9,
    "node_operators": ["漁業署", "大洋水產", "中聯批發", "三和漁貨", "興隆冷鏈", "台灣冷運", "永豐批發", "南海水產", "東港漁業"]
  },
  "trade_offs": {
    "decentralization": "medium",
    "throughput_tps": 3000,
    "finality_seconds": 2,
    "energy": "low",
    "cost_per_tx": "< NT$0.01 (internal network, no gas fee)"
  },
  "metadata": {
    "use_case": "seafood provenance supply chain",
    "participants": 9,
    "trust_level": "low",
    "daily_writes": 4000,
    "daily_reads": 50000,
    "retention_years": 10
  },
  "risks": [
    "oracle_problem: IoT 感測器資料仍需人工安裝驗收，首批上鏈資料可靠性取決於現場執行品質",
    "regulatory: 漁業資料若被認定為個資，需法務確認船員姓名儲存合規性",
    "governance: 聯盟治理規則（誰能加入節點、誰有權提案升級）需在系統上線前以書面合約確定"
  ]
}
```

**給工程師的回覆：** PostgreSQL 技術上可行，但無法解決漁業署與批發商之間的互信問題。區塊鏈在這個場景是架構需求，不是行銷用語。

**給 PM 的回覆：** 區塊鏈確實有說服力，但說服力來自架構，不是「我們用了區塊鏈」這句話。消費者端仍需要清晰的掃碼 UI；鏈上技術對終端用戶透明即可。

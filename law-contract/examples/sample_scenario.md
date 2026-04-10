我沒有直接寫入檔案的工具可用，以下是 `law-contract/examples/sample_scenario.md` 的完整內容，請直接儲存：

---

```markdown
# Example: SaaS 訂閱合約審查 — 台灣新創公司 vs. 美國資料平台供應商

## Scenario

**用戶情況：**
TechFlow Inc.（台灣新創，統編 83921047，員工 45 人）正在評估導入美國 DataNexus Corp. 的企業資料分析平台。年費 USD 48,000（月繳 USD 4,000），合約期 2 年。DataNexus 業務寄來一份 12 頁的「Standard Enterprise Agreement v3.2」，要求本週五簽回。

用戶問：「這份合約有沒有什麼要注意的？業務說是標準合約，應該沒問題吧？」

---

## Analysis

### Step 1 — 辨識當事人

- **Party A（客戶）**：TechFlow Inc. — 合約上寫的是 `TechFlow Inc., a Taiwan corporation`，但台灣公司登記名稱為「科流股份有限公司」。英文名稱 TechFlow Inc. 未必為登記名稱，簽約主體需確認。
- **Party B（供應商）**：DataNexus Corp., a Delaware corporation。
- **簽署人**：確認 TechFlow 一方簽署人是否具授權（需董事會決議或章程授權）。

**風險**：若 TechFlow Inc. 非正式登記名稱，合約效力可能有疑義。

---

### Step 2 — 理解交易內容

TechFlow 支付 USD 48,000/年，取得：
- DataNexus 平台使用授權（最多 20 個帳號）
- 標準技術支援（工作日 9-5，24 小時回應 SLO）
- 資料存儲上限 500 GB

DataNexus 提供：平台存取、維護、資安合規（SOC 2 Type II）。

---

### Step 3 — 檢核四要素

| 要素 | 狀態 | 說明 |
|------|------|------|
| **Offer** | ✅ | 明確的服務範圍、價格、期間 |
| **Acceptance** | ✅ | 雙方簽署即接受 |
| **Consideration** | ✅ | TechFlow 付款 ↔ DataNexus 提供服務 |
| **Legality** | ✅ | 合法 SaaS 服務，跨境交易符合規範 |

四要素齊備，合約形式有效。

---

### Step 4 — 逐條審查

| 條款 | 是否存在 | 評估 | 風險等級 |
|------|---------|------|---------|
| Scope（服務範圍） | Y | 帳號上限 20 人、500 GB 明確；但「API access」未列入，後續若需 API 需另付費 | 🟡 |
| Payment（付款條件） | Y | 每月初預付，逾期 15 天收 1.5%/月利息；無爭議暫停付款機制 | 🟡 |
| Term & Termination（期限與終止） | Y | **2 年自動續約，需於到期前 90 天書面通知不續約**；無 termination for convenience 條款 | 🔴 |
| Liability（責任限制） | Y | DataNexus 責任上限為「過去 3 個月已付費用」≈ USD 12,000；TechFlow 賠償上限**無上限** | 🔴 |
| Indemnity（補償） | Y | TechFlow 須補償 DataNexus 因「TechFlow 使用資料」引起的一切索賠；單向 | 🔴 |
| IP Ownership（智財） | Y | TechFlow 上傳資料歸 TechFlow 所有；但「Aggregated & Anonymized Data」可供 DataNexus 使用於產品改善 | 🟡 |
| Confidentiality（保密） | Y | 5 年保密期；但「Necessary for business operations」例外過於寬泛 | 🟡 |
| Non-compete | N | 無；正常，客戶端通常無此條款 | 🟢 |
| SLA | Y | 99.5% uptime SLO；違反僅退還當月服務費比例（最高 10%）；無終止權 | 🟡 |
| Dispute Resolution | Y | **Delaware 法院管轄，適用 Delaware 州法**；TechFlow 需赴美訴訟 | 🔴 |
| Force Majeure | Y | 標準條款，含 pandemic、政府行為；合理 | 🟢 |

---

### Step 5 — 紅旗彙整

1. **自動續約 + 90 天通知期**（Section 4.2）：合約到期日 2027-04-30，最晚需於 **2027-01-30** 寄出不續約通知。錯過即自動再綁 2 年。
2. **TechFlow 賠償責任無上限**（Section 9.3）：供應商責任上限 USD 12,000，但客戶責任無限。若 TechFlow 員工上傳含第三方智財資料，DataNexus 可向 TechFlow 追索全部損失。
3. **單向補償條款**（Section 10.1）：僅要求 TechFlow 補償 DataNexus，未要求反向補償（如 DataNexus 平台資安事件造成 TechFlow 損失）。
4. **Delaware 管轄**（Section 14）：台灣公司在美國打官司成本極高，實質上放棄法律救濟。
5. **匿名資料使用**（Section 7.4）：TechFlow 的使用行為數據可能含商業敏感資訊（如客戶分析模式），DataNexus 可用於訓練競品功能。

---

## Result

# Contract Review: DataNexus Enterprise Agreement v3.2

## Parties
- Party A: TechFlow Inc.（需確認英文名稱是否為正式登記名稱）
- Party B: DataNexus Corp.（Delaware）

## Deal Summary
TechFlow 以 USD 48,000/年取得 DataNexus 資料分析平台 2 年使用授權（20 帳號、500 GB）。

## Clause Review
| Clause | Present? | Assessment | Risk Level |
|--------|---------|-----------|-----------|
| Scope | Y | API access 未含括，超用費用未定義 | 🟡 |
| Payment | Y | 逾期利率 1.5%/月偏高；無爭議暫停機制 | 🟡 |
| Termination | Y | 自動續約 + 90 天通知期，需立即 calendar | 🔴 |
| Liability | Y | 供應商上限 USD 12,000，客戶無上限 | 🔴 |
| IP | Y | 匿名資料使用條款寬泛 | 🟡 |
| Non-compete | N | 正常，無需關注 | 🟢 |

## Red Flags
1. **Section 4.2**：自動續約 + 90 天通知期 → 立即在行事曆標記 **2027-01-30** 為最後通知日
2. **Section 9.3**：TechFlow 賠償責任無上限 → 要求加入對等上限（建議：合約總金額 USD 96,000）
3. **Section 10.1**：單向補償 → 要求改為「雙向相互補償」（mutual indemnification）
4. **Section 14**：Delaware 管轄 → 談判改為「雙方同意之第三地仲裁（如 SIAC 新加坡）」或台灣法院
5. **Section 7.4**：確認 TechFlow 上傳資料是否含客戶個資，若有，需確認 DataNexus 是否符合台灣個資法（PDPA）及 GDPR（若有歐盟客戶）

## Recommendations
1. **必談判**：Section 9.3 加入責任上限對等條款；Section 10.1 改為 mutual indemnification；Section 14 改為 SIAC 仲裁
2. **建議談判**：Section 4.2 縮短為 30 天通知期；Section 7.4 加入「不得用於訓練競爭性 AI 模型」的明文限制
3. **立即行動**：確認 TechFlow 英文法定名稱；確認簽署人授權文件；在行事曆標記 2027-01-30 不續約通知截止日
4. **法律諮詢**：本分析為教育性評估，建議在簽署前請熟悉跨境 SaaS 合約的律師複審 Section 9、10、14

> ⚠️ 「標準合約」代表對供應商有利，不代表對客戶公平。以上三個 🔴 條款均可談判修改。
```

---

設計說明：

- **場景**：台灣新創買美國 SaaS，是最常見的真實情境
- **數字具體**：USD 48,000/年、90 天通知期、USD 12,000 責任上限、2027-01-30 截止日
- **四個 🔴**：對應 SKILL.md 中明確點名的風險類型（自動續約、單向賠償、無限責任、境外管轄）
- **台灣特色**：加入個資法（PDPA）、法定名稱問題、SIAC 仲裁替代方案
- **符合 Output Format**：完整複製 SKILL.md 的表格與段落結構

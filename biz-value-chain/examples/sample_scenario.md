# Example: 台灣 B2B SaaS 公司找出毛利率下滑原因

## Scenario

**公司：** CloudOps Taiwan（雲端 IT 資產管理 SaaS，成立 2019，ARR $180M NTD）

**用戶提問：**
> 「我們的毛利率從三年前的 78% 掉到現在的 61%，但我們的 ARR 還在成長。我們搞不清楚錢到底漏在哪裡，是要降成本還是要重新定價？」

**背景資訊（用戶提供）：**
- 主要客群：台灣中大型企業 IT 部門（200–2000 人規模）
- 競爭對手：ServiceNow（國際）、叡揚資訊（本土）
- 近期變化：2024 年擴大 CS 團隊（+8 人），新增企業客製化服務線
- 銷售以 enterprise 直銷為主，搭配少量通路商

---

## Analysis

### Step 1: Map Primary Activities

| Activity | Key Processes |
|----------|--------------|
| Inbound Logistics | 雲端基礎設施採購（AWS、GCP）；第三方 API 授權（監控工具、資安掃描） |
| Operations | SaaS 平台開發維運；企業客製化開發；SLA 維持 99.9% uptime |
| Outbound Logistics | 帳號開通、環境部署；客製化環境交付；客戶 onboarding |
| Marketing & Sales | 企業直銷（5 人業務）；行銷活動（itSMF Taiwan 年會、CIO 論壇） |
| Service | CSM 客戶成功團隊（8 人）；技術支援 L1/L2；續約管理 |

### Step 2: Map Support Activities

| Activity | Key Processes |
|----------|--------------|
| Firm Infrastructure | 財務、法務（NDA、SLA 合約）；ISO 27001 認證維護 |
| HR Management | 工程師招募（搶手，常被挖角到大廠）；薪資結構偏低於市場 |
| Technology Development | 核心平台 R&D；AI 功能開發（資產異常偵測）；技術債清償 |
| Procurement | AWS Reserved Instances 採購；SaaS 工具授權議價 |

### Step 3: Assess Each Activity

**Primary Activities:**

| Activity | Value Contribution | Cost % | vs Competitors |
|----------|-------------------|--------|----------------|
| Inbound Logistics | Low | 12% | Worse — AWS 採購無 RI 策略，按需計費 |
| Operations | **High** | 28% | Better — 本土化深度整合（HR 系統、會計系統）競爭對手難複製 |
| Outbound Logistics | Medium | 11% | Worse — 企業客製化交付週期平均 47 天，競對 ServiceNow 約 30 天 |
| Marketing & Sales | Medium | 9% | Same — 論壇口碑佳但缺乏 inbound pipeline |
| Service | **High** | 18% | Worse — CSM 人力大幅增加但無標準化流程，成本失控 |

**Support Activities:**

| Activity | Value Contribution | Cost % | vs Competitors |
|----------|-------------------|--------|----------------|
| Firm Infrastructure | Low | 5% | Same |
| HR Management | **High** | 8% | Worse — 工程師流失率年約 22%，重招成本估每人 NT$300K |
| Technology Development | **High** | 6% | Better — AI 功能是市場差異化，但投資佔比偏低 |
| Procurement | Medium | 3% | Worse — AWS 無 RI，估計可節省 30–35% 雲端費用 |

**成本結構重建（對應毛利率下滑）：**

| 主要原因 | 估計影響 |
|---------|---------|
| AWS 按需計費 vs RI | 約 -4% 毛利率 |
| CS 團隊人力暴增（無流程槓桿） | 約 -7% 毛利率 |
| 企業客製化服務邊際成本被低估 | 約 -6% 毛利率 |
| **合計** | **-17%（符合 78% → 61%）** |

### Step 4: Identify Advantage Sources

**Cost advantage：**
- 無（目前沒有任何一個活動做到比競爭對手更低成本）

**Differentiation advantage：**
- **Operations**（本土化深度整合）— 客戶切換成本高，這是護城河
- **Technology Development**（AI 資產異常偵測）— 目前市場唯一，但投資偏低

**Key linkages：**
- Technology Development ↔ Operations：AI 功能直接嵌入核心平台，強化本土化優勢
- Service ↔ Outbound Logistics：CSM 團隊介入交付流程，延長 onboarding 週期且成本疊加
- Procurement ↔ Inbound Logistics：AWS 議價失敗直接墊高雲端 COGS

---

## Result

```markdown
# Value Chain Analysis: CloudOps Taiwan

## Primary Activities

| Activity | Key Processes | Value Contribution | Cost % | vs Competitors |
|----------|-------------|-------------------|--------|----------------|
| Inbound Logistics | AWS/GCP 採購；第三方 API 授權 | Low | 12% | Worse |
| Operations | 平台維運；本土化整合；企業客製化 | High | 28% | Better |
| Outbound Logistics | Onboarding；客製化環境交付 | Medium | 11% | Worse |
| Marketing & Sales | 企業直銷；CIO 論壇活動 | Medium | 9% | Same |
| Service | CSM 管理；技術支援；續約 | High | 18% | Worse |

## Support Activities

| Activity | Key Processes | Value Contribution | Cost % | vs Competitors |
|----------|-------------|-------------------|--------|----------------|
| Infrastructure | 財務、法務、ISO 認證 | Low | 5% | Same |
| HR Management | 工程師招募與留任 | High | 8% | Worse |
| Technology Dev | AI 功能 R&D；核心平台演進 | High | 6% | Better |
| Procurement | AWS RI 議價；SaaS 工具授權 | Medium | 3% | Worse |

## Advantage Sources
- **Differentiation advantage in**: Operations（本土化整合）、Technology Development（AI 偵測）
- **No cost advantage** in any activity — 需優先修復
- **Key linkages**:
  - Technology Development ↔ Operations（AI 強化本土化，護城河加深）
  - Service ↔ Outbound Logistics（CSM 介入交付 = 成本疊加，需解耦）

## Recommendations

1. **Strengthen**: Technology Development — 將 AI 預算從 6% 提升至 10%；這是目前唯一市場差異化來源，且競爭對手（ServiceNow）尚未本土化 AI 功能

2. **Optimize**: Service — 建立 CSM playbook 與 self-service portal；目前 8 人 CSM 每人服務約 15 個客戶，業界標竿為 25–30；目標在 6 個月內讓 CSM 成本佔比從 18% 降至 12%

3. **Optimize**: Outbound Logistics — 標準化 onboarding 流程；將企業交付週期從 47 天壓縮至 30 天；解耦 CSM 與交付流程避免成本疊加

4. **Outsource/Negotiate**: Procurement — 立即評估 AWS 1 年期 Reserved Instances；按目前用量估算年省 NT$4–6M；委外 FinOps 顧問做一次性優化即可

5. **投資**: HR Management — 提升工程師薪資至市場 P75（預估年增 NT$3M 薪資支出，但可降低 22% 流失率，每年省下 NT$6M 重招成本）
```

**核心結論：** 毛利率下滑不是定價問題，是成本失控。三個主要漏點是雲端採購（RI 策略缺失）、CS 人力無槓桿、企業客製化成本被低估。護城河在 Operations + Technology Development — 這兩個活動要加碼，不能砍。

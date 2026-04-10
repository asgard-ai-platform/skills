工具需要授權，直接撰寫範例。

```markdown
# Example: 製造業 ERP 升級的採用困境

## Scenario

台中精密零件製造商 **Primax Components**（員工約 420 人）於 2025 年 Q3 完成 SAP S/4HANA 導入，取代使用 14 年的老舊 ERP 系統。IT 部門投入 NT$18M，預計 6 個月達到穩定使用率（目標：85% 的生產線班長每日登入並完成工單回報）。

導入後 3 個月（2025 年 12 月），實際每日活躍使用率僅 **41%**，班長普遍回到紙本記錄再交由辦公室人員補登。管理層詢問：「為什麼班長不願意用新系統？我們能做什麼？」

## Analysis

### Step 1 — 技術與使用族群定義

- **技術**：SAP S/4HANA，含行動裝置介面（平板），主要功能為工單領取、進度回報、異常通報
- **目標使用者**：生產線班長（n=68），年齡分布 32–55 歲，平均任期 9 年，多數為高職或專科學歷，日常操作以實體設備為主
- **採用性質**：**強制性**（非自願），公司政策規定所有工單必須透過系統回報，但執行未徹底落實

### Step 2 — 構念測量（基於 12 位班長訪談 + 全體問卷，7 點量表）

| Construct | Score (1-7) | Key Drivers | Key Barriers |
|-----------|-------------|-------------|--------------|
| Performance Expectancy | **3.2** | 即時庫存可見度（少數班長認可） | 班長認為工單速度比系統快；異常通報比LINE慢 |
| Effort Expectancy | **2.4** | — | 平板介面字體小；工單流程需 7 個點擊（紙本 2 步驟）；手套操作觸控不靈敏 |
| Social Influence | **4.1** | 廠長公開支持；部分資深班長帶頭使用 | 同儕間流行說「打系統不如打師傅」；工廠文化重視速度勝流程 |
| Facilitating Conditions | **2.9** | 每條線配備 2 台平板 | 網路訊號在 C 廠區時常斷線；IT 支援 response time 平均 4 小時；無正式教育訓練記錄 |

**Behavioral Intention score：2.7 / 7**（高度低落）

### Step 3 — 調節變項與障礙診斷

**年齡效應：** 40 歲以上班長（佔 61%）Effort Expectancy 分數顯著更低（均值 2.1 vs. 年輕班長 3.1），對系統複雜度的容忍度低。

**經驗效應：** 班長平均任期 9 年，對舊流程高度熟悉，切換成本感知強烈——這是 PEOU 低落的核心原因，而非能力不足。

**強制性矛盾：** 使用雖然強制，但不合規後果不明確（主管未懲處），使 Social Influence 的效力打折。強制情境下 Social Influence 本應最強，但執法不一致反而強化了「可以不用」的集體認知。

**根本障礙優先序：**
1. **Effort Expectancy（最弱，2.4）**：介面設計與操作情境嚴重不匹配
2. **Facilitating Conditions（2.9）**：基礎建設缺口阻斷了使用意願轉為行為
3. **Performance Expectancy（3.2）**：班長看不到「對我有什麼好處」

### Step 4 — 干預設計

針對最弱構念優先介入：

**Effort Expectancy 干預（最高優先）**
- 與 SAP 合作客製化「班長快速介面」：將工單回報壓縮至 3 步驟，移除非必要欄位
- 採購防水、支援手套操作的觸控筆（預算 NT$120K）
- C 廠區補建 Wi-Fi 中繼節點（IT 部門 6 週內完成）

**Facilitating Conditions 干預**
- 指定每班一位「系統聯絡人」（Super User），IT 問題 30 分鐘內回應
- 建立離線快取模式，斷網時仍可登錄，恢復連線後同步

**Performance Expectancy 干預**
- 每週在廠區看板顯示「即時庫存準確率」，將數字歸因於班長的系統回報
- 導入工單完成獎勵：當月系統使用率 ≥ 90% 的班長組別可獲得績效加給 0.5%

**Social Influence 強化**
- 廠長親自公告：2026 年 3 月起，紙本回報不納入正式工單記錄，正式落實執法
- 遴選 3 位高影響力資深班長擔任「推廣大使」，給予系統客製化優先建議權

## Result

## TAM/UTAUT Analysis: SAP S/4HANA — Primax Components 生產線班長

### Construct Assessment

| Construct | Score (1-7) | Key Drivers | Key Barriers |
|-----------|-------------|-------------|--------------|
| Performance Expectancy | 3.2 | 即時庫存可見度 | 班長感知不到個人工作效益；系統速度慢於現行習慣 |
| Effort Expectancy | 2.4 | — | 7 步驟工單流程；觸控介面不適合手套環境；訊號不穩 |
| Social Influence | 4.1 | 廠長支持；部分資深班長帶頭 | 執法不一致導致集體觀望；「速度文化」抵制流程導向 |
| Facilitating Conditions | 2.9 | 平板已部署 | C 廠區斷線；IT 回應慢；未提供正式訓練 |

### Moderator Effects
- **Age**：40 歲以上班長 Effort Expectancy 更低（2.1），為主要風險族群，需優先安排 1-on-1 操作輔導
- **Experience**：長任期造成高習慣慣性，需明確的相對優勢示範，而非一般性訓練
- **Voluntariness**：名義上強制，實際執法寬鬆；建議 2026 Q1 落實稽核機制以啟動規範壓力

### Intervention Recommendations
1. **Effort Expectancy**：客製化班長快速介面（3 步驟），採購手套觸控筆，補強 C 廠無線網路 — *預期 8 週內完成，目標 Effort 分數提升至 4.5+*
2. **Facilitating Conditions**：Super User 制度 + 離線快取模式 — *消除「環境阻礙」的免責理由*
3. **Performance Expectancy**：看板視覺化歸因 + 使用率績效加給 — *讓班長看見「對我的好處」*
4. **Social Influence**：2026-03-01 正式停收紙本；推廣大使計畫 — *將觀望成本從「沒有好處」轉為「有明確損失」*

**預測**：若 Effort Expectancy 提升至 4.5、Facilitating Conditions 提升至 4.0，依 UTAUT 路徑係數估算，Behavioral Intention 可從 2.7 提升至 4.8–5.2，對應使用率約 70–78%，距 85% 目標仍需社會影響機制配合落實。
```

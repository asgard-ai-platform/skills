# ABC 作業成本制的理論演進

## 第一代 ABC（1980 年代後期）

**代表作**：Cooper & Kaplan《Measure Costs Right: Make the Right Decisions》HBR 1988

**核心主張**：
- 傳統量基成本（以工時／機器小時分攤製造費用）會嚴重扭曲多產品企業的成本資訊
- 應以「作業」為分攤中介：**資源 → 作業 → 產品**

**適用條件**：
- 製造費用佔總成本比例高（> 30%）
- 產品多樣化、批量差異大
- 直接人工比例已降低（自動化程度高）

**限制**：
- 作業分類數過多（數十至數百項）→ 維護成本極高
- 需要大量員工訪談以估計作業耗時，主觀偏誤大
- 難以反映產能利用率變化

## 第二代：Time-Driven ABC（TDABC，2004 年）

**代表作**：Kaplan & Anderson《Time-Driven Activity-Based Costing》HBR 2004

**改進**：
- 不再需要員工訪談估算作業比例
- 只需兩個參數：
  1. 產能成本率（每單位時間的成本）= 部門成本 ÷ 可用時間
  2. 每項作業所需的時間方程式（time equation）

**範例時間方程式**：
```
訂單處理時間 = 5 分鐘（基本）
              + 若為新客戶 × 15 分鐘
              + 若跨國訂單 × 20 分鐘
              + 若為緊急訂單 × 10 分鐘
```

**優勢**：
- 可直接從 ERP 系統自動更新
- 能反映閒置產能成本（實際使用時間 vs 可用時間）
- 易於複製到多廠區

## 第三代：策略性成本管理

**代表觀點**：
- ABC 不只是成本分攤，而是 **策略工具**（例如客戶獲利性分析、產品組合決策）
- 結合 Balanced Scorecard（Kaplan 與 Norton 另一發明）→ 成本資訊連結策略

## EMBA 個案常見誤用

1. **把 ABC 當作新的「真實成本」**
   - ABC 仍是分攤，仍有主觀選擇（動因選擇、作業分類邊界）
   - 與傳統系統相比是「不同角度」，非「更正確」

2. **忽略「相關成本」觀念**
   - ABC 會把「承諾性成本」（committed cost，例如廠房折舊）全部分攤出去
   - 但短期決策（例如是否接 OEM 訂單）應看「變動成本」而非完全分攤後成本

3. **忘記「閒置產能成本」歸屬**
   - 若以「實際產量」當動因總量分母，景氣差時分攤率飆升 → 成本被高估
   - 應以「正常產能」或「實務產能」為分母，閒置產能成本直接列為期間費用

## 延伸閱讀

- Kaplan, R. S., & Cooper, R. (1998). *Cost and Effect: Using Integrated Cost Systems to Drive Profitability and Performance*. Harvard Business School Press.
- Kaplan, R. S., & Anderson, S. R. (2007). *Time-Driven Activity-Based Costing: A Simpler and More Powerful Path to Higher Profits*. Harvard Business School Press.
- 台灣學界：鄭丁旺《中級會計學》、吳安妮（政大）關於 BSC 與 ABC 整合的實證研究

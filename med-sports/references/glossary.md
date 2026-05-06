# Sports Statistics & Terminology — Glossary & Formulas

## 棒球統計術語與計算

### 傳統打擊指標

| 術語 | 中文 | 計算公式 | 解釋 |
|------|------|--------|------|
| AVG (Batting Average) | 打擊率 | H / AB | 安打數 ÷ 打數。傳統衡量打者能力的指標。聯盟平均約 .270。 |
| OBP (On Base Percentage) | 上壘率 | (H + BB + HBP) / (AB + BB + HBP + SF) | 衡量上壘能力(不限於安打)。高於 .350 為優秀。 |
| SLG (Slugging Percentage) | 長打率 | TB / AB | 全壘打特別計算為 4 分基壘數,三壘打 3 分等。衡量長打能力。 |
| OPS (On Base Plus Slugging) | OPS | OBP + SLG | OBP 和 SLG 的合計。優秀打者 OPS > .850。 |
| RBI (Runs Batted In) | 打點 | 打者致使得分的次數 | 易受隊友表現影響,非純打者能力指標。 |

### 進階打擊指標 (Advanced)

| 術語 | 計算 | 解釋 |
|------|------|------|
| wRC+ (Weighted Runs Created Plus) | (((wRC / PA) / (lgwRC / lgPA)) - 1) * 100 + 100 | 與聯盟平均相比的得分創造指數,100 為聯盟平均。120 = 20% 高於平均。 |
| xwOBA (Expected Weighted On Base Average) | 基於打球數據 (exit velocity, launch angle 等) 的預期長打率 | 基於球被擊出的物理特性而非實際結果。用於識別運氣因素。 |
| BABIP (Batting Average on Balls in Play) | (H - HR) / (AB - K - HR + SF) | 擊出遊擊的安打率。.300 為平均。過高或過低可能不可持續。 |
| ISO (Isolated Power) | SLG - AVG | 純長打能力(孤立長打)。 |

### 投手指標

| 術語 | 計算 | 解釋 |
|------|------|------|
| ERA (Earned Run Average) | (ER × 9) / IP | 每 9 局自責分。4.00 為聯盟平均;低於 3.50 為優秀。 |
| WHIP (Walks + Hits per Innings Pitched) | (BB + H) / IP | 每局保送 + 安打數。低於 1.20 為優秀。 |
| FIP (Fielding Independent Pitching) | ((13 × HR) + (3 × BB) - (2 × K)) / IP + 常數 | 僅基於投手控制的因素(保送、三振、全壘打),排除守備影響。 |
| xFIP (Expected FIP) | 基於硬Hit% 與 exit velocity 的預期 FIP | 比 FIP 更預測性;考慮球被擊出的品質。 |

## 籃球統計術語與計算

### 傳統進攻指標

| 術語 | 計算 | 解釋 |
|------|------|------|
| FG% (Field Goal Percentage) | 投中 / 投籃 | 整體投籃命中率。45% 為平均,50%+ 為優秀。 |
| 3P% (Three-Point Percentage) | 三分投中 / 三分投籃 | 三分球命中率。35% 為平均,40%+ 為優秀。 |
| FT% (Free Throw Percentage) | 罰球投中 / 罰球 | 罰球命中率。80% 為平均,90%+ 為超級明星等級。 |
| eFG% (Effective Field Goal Percentage) | (FG + 0.5 × 3PM) / FGA | 將三分球額外加權,反映真實進攻效率。 |

### 進階籃球指標

| 術語 | 計算 | 解釋 |
|------|------|------|
| PER (Player Efficiency Rating) | (USGR × (uPER - 1.0) + 15.0) | 根據回合數加權的單位效率,15.0 為平均。20+ 為超級巨星。 |
| TS% (True Shooting Percentage) | PTS / (2 × TSA) | 考慮兩分、三分、罰球的真實投籃效率。50% 為平均,55%+ 為優秀。 |
| BPM (Box Plus-Minus) | 回合基礎上的 +/- 貢獻 | 衡量球員每 100 回合對勝率的影響。正數為貢獻。 |
| VORP (Value Over Replacement Player) | 相對替補球員的勝場貢獻 | 衡量球員與聯盟平均後衛/前鋒的差距。 |

## 跨運動通用術語

| 術語 | 解釋 | 應用 |
|------|------|------|
| **IL / DL (Injured List / Disabled List)** | 傷停名單。棒球通常分 7 日 IL、15 日 IL、60 日 IL。籃球通常列為「Out」或「Day-to-Day」。 | 報導傷停時必須註明 IL 等級或球隊預估復出時間。 |
| **ERA-adjusted 比較** | 將跨不同時代的成績調整至標準化平臺以進行比較。如 OPS+ (相對聯盟平均的 OPS 指數,100 為平均)。 | 「1920 年代的打者不能直接與 2020 年代比較」,必須使用 ERA-adjusted 指標。 |
| **Sample Size** | 樣本量。棒球通常要求 300+ 打數才視為「有效」季度數據。 | 「他上半季 .350 打擊率但打數只有 80,不代表最終季度成績」。 |
| **Pace-of-play / Pace Correction** | 調整球隊或聯盟的比賽節奏。如NBA的進攻回合數;棒球的每 9 局標準化。 | 「2000 年的投手 ERA 不能直接比 2025 年的投手」,需考慮比賽節奏變化。 |
| **Strength of Schedule (SOS)** | 對陣對手強度。用於評估球隊成績時的內容質量。 | 「球隊 10 連勝但對手 SOS 很低」= 成績可能膨脹。 |

## 特定聯盟術語

### MLB 特定

| 術語 | 中文 | 解釋 |
|------|------|------|
| **WAR (Wins Above Replacement)** | 相對替補球員的勝場貢獻 | 綜合性指標,衡量球員相對「替補級」球員的價值。6+ 為超級巨星。 |
| **CBA (Collective Bargaining Agreement)** | 勞資協議 | 約束球員薪資、交易規則、仲裁程序的協議。MLB CBA 每數年重談。 |
| **Arbitration / 仲裁** | 薪資仲裁 | 球員與球隊無法達成合約時,透過仲裁員決定工資。 |
| **Free Agent / 自由球員** | 可自由選擇簽約球隊的球員,通常 6 年大聯盟經驗後符合資格。 |

### NBA 特定

| 術語 | 中文 | 解釋 |
|------|------|------|
| **Salary Cap / 薪資上限** | 聯盟限制球隊支出的上限。超過上限需支付奢侈稅。 | 影響球隊交易與簽約能力。 |
| **Luxury Tax / 奢侈稅** | 薪資總額超過上限時球隊需支付的罰款。 | 用於約束高薪支出。 |
| **Player Option / Team Option** | 球員或球隊有權決定合約是否續行的條款。 | 影響交易與自由市場動態。 |

## 禁藥與紀律相關術語

| 術語 | 解釋 | 使用注意 |
|------|------|--------|
| **WADA (World Anti-Doping Agency)** | 世界反禁藥機構 | 統一禁藥名單與檢測標準的國際組織。 |
| **CAS (Court of Arbitration for Sport)** | 國際體育仲裁法院 | 禁藥與紀律上訴的最終仲裁機構。WADA 與球隊均可上訴至 CAS。 |
| **Tested Positive / 藥檢呈陽性** | 檢測結果為陽性 | 事實陳述;不代表違規認定(須經後續檢驗與聽證)。 |
| **Alleged to have violated / 涉嫌違規** | 指控違規但未定罪 | 用於尚未最終裁定的案件。 |
| **Suspension / 禁賽** | 聯盟或國際組織禁止參賽的懲罰 | 時間期限清晰。 |
| **Banned Substance / 禁用物質** | 列入 WADA 禁藥名單的物質 | 分為競賽期、非競賽期、特定運動禁用等類別。 |


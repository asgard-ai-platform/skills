直接建立檔案：

```markdown
# Example: 新創公司秋招 — 5 名候選人 × 5 個職缺穩定配對

## Scenario

FinStack（金融科技新創）今年秋招開放 5 個職缺：前端工程師（FE）、後端工程師（BE）、資料工程師（DE）、產品經理（PM）、資安工程師（SEC）。人資 Kelly 收到 5 名最終候選人：Alice、Bob、Carol、Dave、Eve。

雙方都已完成互相評分，Kelly 希望產出一份「穩定配對」名單，確保不會在 offer 發出後出現「候選人更想去另一個職缺，而那個職缺也更想要那名候選人」的局面（blocking pair），導致 offer 被拒或內部競爭。

Kelly 決定讓**公司職缺為 proposer 端**（由公司主動出 offer），因為 FinStack 品牌較弱，讓公司優先鎖定首選人選可降低 offer 被拒率。

### 偏好排名

**公司職缺偏好（由高到低）：**

| 職缺 | 第 1 | 第 2 | 第 3 | 第 4 | 第 5 |
|------|------|------|------|------|------|
| FE   | Carol | Alice | Eve  | Bob  | Dave |
| BE   | Alice | Dave  | Bob  | Eve  | Carol |
| DE   | Eve  | Carol | Dave | Alice | Bob |
| PM   | Bob  | Alice | Carol | Dave | Eve |
| SEC  | Dave | Eve   | Alice | Bob  | Carol |

**候選人偏好（由高到低）：**

| 候選人 | 第 1 | 第 2 | 第 3 | 第 4 | 第 5 |
|--------|------|------|------|------|------|
| Alice  | BE   | PM   | FE   | SEC  | DE  |
| Bob    | PM   | BE   | DE   | FE   | SEC |
| Carol  | FE   | DE   | PM   | BE   | SEC |
| Dave   | SEC  | BE   | DE   | PM   | FE  |
| Eve    | DE   | SEC  | FE   | PM   | BE  |

---

## Analysis

### Phase 1：輸入驗證

- 雙方各 5 個，等量 ✓
- 每方對另一方完整排名（5 選 5）✓
- 無重複、無缺漏 ✓
- **Proposer 端：公司職缺**（FE、BE、DE、PM、SEC）

Gate 通過，進入核心演算法。

---

### Phase 2：Gale-Shapley 執行追蹤

> 符號：`X → Y` = X 向 Y 提出，`Y ✓ X` = Y 接受，`Y ✗ X` = Y 拒絕

**Round 1：所有職缺向各自第 1 志願提出**

| 職缺 | 提出給 | 候選人反應 |
|------|--------|-----------|
| FE   | Carol  | Carol 暫時接受（首個 offer） |
| BE   | Alice  | Alice 暫時接受（首個 offer） |
| DE   | Eve    | Eve 暫時接受（首個 offer） |
| PM   | Bob    | Bob 暫時接受（首個 offer） |
| SEC  | Dave   | Dave 暫時接受（首個 offer） |

Round 1 後：全部配對，無自由職缺。  
**→ 演算法在 Round 1 即終止。**（n=5 時最佳情況：所有第 1 志願互不衝突）

---

### Phase 3：穩定性驗證

檢查所有 10 個未配對組合是否存在 blocking pair：

| 未配對組合 | 條件 A（職缺偏好）| 條件 B（候選人偏好）| Blocking？|
|------------|-----------------|-----------------|---------|
| FE ↔ Alice | FE 排 Alice 第 2（高於 Carol 第 1？No，Carol 是第 1）| — | 否 |
| FE ↔ Bob   | FE 排 Bob 第 4（低於 Carol 第 1）| — | 否 |
| FE ↔ Dave  | FE 排 Dave 第 5（低於 Carol 第 1）| — | 否 |
| FE ↔ Eve   | FE 排 Eve 第 3（低於 Carol 第 1）| — | 否 |
| BE ↔ Bob   | BE 排 Bob 第 3（低於 Alice 第 1）| — | 否 |
| BE ↔ Carol | BE 排 Carol 第 5（低於 Alice 第 1）| — | 否 |
| BE ↔ Dave  | BE 排 Dave 第 2（高於 Alice）✓ | Dave 偏好 SEC（第 1）> BE（第 2）→ Dave 不偏好 BE 勝過 SEC | 否 |
| DE ↔ Alice | DE 排 Alice 第 4（低於 Eve 第 1）| — | 否 |
| PM ↔ Alice | PM 排 Alice 第 2（高於 Bob）✓ | Alice 偏好 BE（第 1）> PM（第 2）→ Alice 不偏好 PM 勝過 BE | 否 |
| SEC ↔ Eve  | SEC 排 Eve 第 2（高於 Dave）✓ | Eve 偏好 DE（第 1）> SEC（第 2）→ Eve 不偏好 SEC 勝過 DE | 否 |

**Blocking pairs：0**  
Gate 通過，穩定匹配確認。

---

### Phase 4：結果解讀

因公司為 proposer 端，本結果為 **公司最優穩定匹配**（company-optimal）：

- FE 拿到首選 Carol
- BE 拿到首選 Alice
- DE 拿到首選 Eve
- PM 拿到首選 Bob
- SEC 拿到首選 Dave

這對候選人而言是 **reviewer-pessimal** 的穩定匹配——若改由候選人為 proposer，結果可能對候選人更有利。Kelly 應向候選人說明配對邏輯，以維持透明度。

---

## Result

```json
{
  "matching": [
    {"proposer": "FE",  "reviewer": "Carol", "proposer_rank": 1, "reviewer_rank": 1},
    {"proposer": "BE",  "reviewer": "Alice", "proposer_rank": 1, "reviewer_rank": 1},
    {"proposer": "DE",  "reviewer": "Eve",   "proposer_rank": 1, "reviewer_rank": 1},
    {"proposer": "PM",  "reviewer": "Bob",   "proposer_rank": 1, "reviewer_rank": 1},
    {"proposer": "SEC", "reviewer": "Dave",  "proposer_rank": 1, "reviewer_rank": 1}
  ],
  "metadata": {
    "pairs": 5,
    "rounds": 1,
    "blocking_pairs": 0,
    "proposer_side": "job_positions"
  }
}
```

### 給 Kelly 的行動建議

1. **同步發出 5 封 offer**：第 1 輪無衝突，可立即確認，無需分批。
2. **告知候選人配對為公司優先**：若有候選人反映「這不是我最想要的職缺」，需解釋穩定匹配邏輯，避免誤解為歧視。
3. **備案：候選人拒絕 offer**：若任一人拒絕（偏好外部公司），重新執行 Gale-Shapley，將拒絕者標記為不可用，並補入候補候選人。
4. **下次考慮候選人優先**：若 FinStack 品牌提升，改為候選人 propose，可作為吸引人才的談判籌碼（「我們讓你決定職缺」）。
```

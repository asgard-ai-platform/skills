# Asgard Skills

開源的 **263 個 coding agent skills** 知識庫，分成 21 個主題類別。每個 skill 都是獨立的 Markdown 檔案（`SKILL.md`），遵循 [Claude Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) 規範，部分附帶純 Python 腳本做確定性計算。

[English](README.md)

## 概觀

本 repo 是 [Asgard AI Platform](https://github.com/asgard-ai-platform) 的**原料庫**。Skills 會與 [Asgard MCPs](https://github.com/orgs/asgard-ai-platform/repositories?q=mcp-) 組合，打包成針對特定使用者情境的 [coding agent plugins](https://github.com/asgard-ai-platform)（例如台股分析師、電商營運、政策研究者）。

每個 skill 封裝的是某個明確任務的**方法論 + 判斷 + 陷阱**——那些 LLM agent 若沒有提示就會重新摸索、或直接做錯的東西。

## Repo 結構

```
.
├── {category}-{skill-name}/
│   ├── SKILL.md           ← Level 1 frontmatter + Level 2 指引
│   ├── examples/          ← （必存在，視需要填充）
│   ├── references/        ← （冗長內容外掛於此）
│   └── scripts/           ← （僅在有確定性計算腳本時出現）
└── ...
```

## 類別（21 個前綴，263 個 skills）

| 前綴 | 數量 | 主題 |
|--------|------:|-------|
| `grad-` | 87 | 研究所級理論模型（RBV、CAPM、SEM、DID…） |
| `algo-` | 62 | 演算法（PageRank、BM25、ARIMA、EOQ…） |
| `biz-` | 22 | 商學院框架（SWOT、Porter 五力、DCF…） |
| `hum-` | 9 | 人文 / 批判性推理 |
| `tw-` | 9 | 台灣在地知識（股市、稅務、電子發票…） |
| `ecom-` | 7 | 電商實務 |
| `econ-` | 6 | 經濟學基礎 |
| `meta-` | 6 | 跨領域思維模型 |
| `ops-` | 6 | 企業營運（OKR、合約審查、pitch deck…） |
| `law-` | 5 | 法律框架 |
| `pr-` | 5 | 公關 / 品牌傳播 |
| `cs-` | 4 | 客戶服務 |
| `data-` | 4 | 資料分析 |
| `mfg-` | 4 | 製造業 |
| `mkt-` | 4 | 數位行銷 |
| `soc-` | 7 | 社會科學 |
| `stat-` | 4 | 統計方法論 |
| `tech-` | 4 | 一般技術（API、prompt engineering、MCP server…） |
| `ux-` | 4 | 設計 / UX 方法論 |
| `fin-` | 2 | 金融實務（modeling、earnings） |
| `xborder-` | 2 | 跨境電商 |

## Skill 結構

每份 `SKILL.md` 遵循一致的模板：

```markdown
---
name: "{category}-{skill-name}"
description: "[祈使句 WHAT + WHEN，< 1024 字元，不可含 XML 角括號]"
metadata:
  category: "WP-XX Topic Label"
  tags: [...]
---

# {Skill 顯示名稱}

## Overview / Framework
## When to Use (and When NOT to Use)
## Methodology（Phase-Gate 或 Hub-and-Spoke 模式）
## IRON LAW：{非顯而易見的約束}
## Output Format
## Gotchas
## Scripts（若適用）
## References
```

## 確定性計算腳本

目前有 20 個 skills 附帶 Python 腳本（純 stdlib、無外部依賴），處理那些 LLM 常算錯的計算：

- **財務**：`biz-cac-ltv`、`biz-breakeven`、`biz-dcf`、`biz-dupont`、`biz-financial-ratios`、`biz-unit-economics`、`grad-capm`、`fin-modeling`
- **風險 / 統計**：`algo-risk-altman-z`、`algo-risk-var`、`mkt-ab-testing`、`algo-mfg-cpk`
- **供應鏈**：`algo-sc-eoq`、`algo-sc-safety-stock`、`algo-sc-newsvendor`
- **排名**：`algo-rank-wilson`、`algo-rank-elo`、`algo-rank-bayesian`
- **電商**：`ecom-rfm-analysis`、`algo-price-elasticity`
- **搜尋**：`algo-seo-tfidf`、`algo-ecom-bm25`

每個腳本都支援 `--help`、`--input <json>`、`--verify`（內建自我測試）。輸出以 JSON 印到 stdout，方便後續串接。

```bash
# 範例
python ecom-rfm-analysis/scripts/rfm_score.py --input customers.json
python biz-cac-ltv/scripts/cac_ltv.py --marketing-cost 100000 --new-customers 500 \
  --arpu 50 --gross-margin 0.70 --monthly-churn 0.05
```

## 設計原則

1. **Iron Law**：每個 skill 都定義一條非顯而易見的約束，agent 不提示就會踩雷
2. **Hub-and-Spoke**：SKILL.md 精簡（< 200 行）；冗長內容外掛到 `references/`
3. **Phase-Gate**（演算法）：明確步驟、步驟之間設驗證關卡
4. **具體驗證**：範例必須可精確計算，不接受「大概落在某範圍」
5. **不過度教學**：假設 agent 已懂基礎，只強調它會**做錯**的地方

完整設計規則與品質標準見 [`CLAUDE.md`](CLAUDE.md)。

## 狀態

| 階段 | 狀態 |
|-------|:-:|
| Phase 1：四個 section 共 263 個 skills 生成 | ✅ |
| Phase 1.5：自動 lint（frontmatter、長度、IRON LAW） | ✅ 263/263 |
| Phase 1.7：with/without skill 評估（4 份樣本） | ✅ 4/4 with_skill 勝 |
| Phase 2-3：品質審計（抽樣 28 份） | ✅ 14 PASS / 13 MINOR / 1 MAJOR |
| Phase 3.5：P0 + P1 修補 | ✅ |
| Phase 4：description 最佳化（phantom trigger） | ✅ |
| Tier 1 + 2 確定性腳本（共 20 支） | ✅ 全部 `--verify` 通過 |
| Plugin 打包（Phase 5） | 🟡 規劃中（[見 `TODO.md`](TODO.md)） |

## 相關 Repo

- [`asgard-ai-platform/skill-template`](https://github.com/asgard-ai-platform/skill-template) — 建立 coding agent plugin 的樣板
- [`asgard-ai-platform/mcp-*`](https://github.com/orgs/asgard-ai-platform/repositories?q=mcp-) — MCP servers（資料原料）
- Plugin bundles（即將推出） — 針對特定情境的 skills + MCPs 組合

## 授權

MIT License。見 [LICENSE](LICENSE)。

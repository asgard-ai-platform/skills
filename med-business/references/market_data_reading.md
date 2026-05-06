# Market Data & Multi-Period Comparisons: Pitfalls & Best Practices

Financial reporters often cite stock prices, returns, indices, and multi-year comparisons. This guide covers how to read and report these correctly.

---

## Stock Price & Market Cap

### Timestamp & Close vs. Intra-Day

**The risk:**
- "Stock rose 5% today" — at what time? Close? Intra-day high?
- Market moves; a 5% swing from open to close is different from a 5% swing from yesterday's close to today's close

**Practice:**
- Always specify: "Stock closed up 5% to NT$385 (as of 2026-04-11 market close)"
- If citing intra-day high/low: explicitly label it ("reached NT$390 intra-day before closing at NT$385")

### Market Cap Calculation

**Formula:** Market Cap = Stock Price × Shares Outstanding

**Common mistakes:**
- Not noting the price date: "Company has 100B market cap" (cap changes hourly)
- Not stating shares outstanding: can be diluted vs. undiluted

**Practice:**
- "As of April 11 close, Company X's market cap was NT$385B (stock price NT$385 × 1B shares undiluted)"
- Note if you used diluted shares (includes options, warrants, convertibles)

---

## Index Levels & Returns

### Index Calculation Basis

**Taiwan indices (TWSE, TAIEX):**
- **TAIEX** (Weighted by market cap): larger companies have more weight
- **TAIEX Mid-Cap**: weights mid-size companies more heavily
- **TAIEX Small-Cap**: weights smaller-cap stocks

**The risk:** 
- Saying "Market up 3%" could mean TAIEX (large-cap weighted) or TAIEX Small-Cap (small-cap weighted)
- These can diverge materially

**Practice:**
- Always specify which index: "TAIEX rose 3%" or "Chip sector index rose 5%"
- If citing multiple indices with different movements, note divergence: "Bluechips up 2%, small-caps down 1% — indicating sector rotation"

### Price Return vs. Total Return

- **Price return**: Only stock price movement (ignores dividends)
- **Total return**: Price movement + reinvested dividends

**The risk:**
- Stock A: price down 5%, dividend +3% = total return -2%
- Citing only price return (-5%) ignores the positive dividend component

**Practice:**
- In earnings season, when dividends are announced, track total-return impact
- Example: "Stock closed down 2% today, but announced dividend brought total expected return to +1%"

---

## Multi-Year Returns & Annualization

### Period Selection Bias

**The risk:**
- "Stock up 100% over 5 years" vs. "Stock down 30% over 2 years" — both can be true if price was lower 2 years ago than 5 years ago
- Cherry-picking a bullish or bearish window distorts narrative

**Practice:**
- If citing multi-year performance, cite 3, 5, and 10-year windows for context
- Note if one-year or three-year period was exceptionally good/bad (e.g., pandemic bounce, crash)

### Annualized Returns

**Formula:** Annualized Return = (Ending Price / Starting Price)^(1/n) − 1 (where n = years)

**Example:**
- Stock: NT$300 (5 years ago) → NT$600 (today)
- 5-year total return: 100%
- Annualized return: (600/300)^(1/5) − 1 = 14.9% per year

**The risk:**
- Confusing total return (100%) with annualized return (14.9%)
- Simply dividing total return by years (100% ÷ 5 = 20%) overstates annualized return (compounding effect)

**Practice:**
- Always specify: "14.9% annualized over 5 years" not just "100% return"
- If citing short windows (< 1 year), use total return, not annualized (annualizing short-term noise is misleading)

---

## Currency & Foreign Markets

### Exchange Rate Basis

**The risk:**
- US subsidiary earnings of $100M reported as "NT$3 trillion" (at 30:1) vs. "NT$3.5 trillion" (at 35:1)
- 17% difference, all from FX, none from operations

**Practice:**
- State exchange rate & date: "US$100M at NT$32:USD (2026-04-11 close) = NT$3.2B"
- When comparing prior-year earnings: note FX impact separately
  - "Earnings rose 10% in USD terms but only 5% in NT$ due to NTD appreciation"

### FX Impact Segregation

**Important distinction:**
- **Operating growth** (revenue/profit from business operations)
- **FX translation gain/loss** (balance-sheet revaluation of foreign subsidiaries)
- **FX hedging gain/loss** (realized P&L on currency hedges)

**Practice:**
- When company reports earnings: separate these effects in narrative
- Example: "Profit rose 15% in operating terms, but FX translation loss of 3% reduced NT$-basis profit to 12%"

### Spot Rate vs. Historical Rate

- **Spot rate**: Current market rate (for transactions happening today)
- **Historical rate**: Rate at which foreign subsidiary's balance sheet was originally converted
- **Average rate during period**: Average for revenue/expense items

**Practice:**
- Year-end balance sheet items often use spot rate (as of balance-sheet date)
- Revenue/expense items often use average rate during the period
- If comparing to prior year: FX impact varies by whether you're looking at balance-sheet items (spot-based) vs. income items (period-average)

---

## Technical Indicators & Limitations

### Moving Averages (MA)

- **50-day MA**: Average closing price over last 50 trading days (~ 2 months)
- **200-day MA**: Average over 200 trading days (~ 10 months)
- **Signal**: "Golden cross" (50-day MA crosses above 200-day MA) traditionally bullish; "death cross" bearish

**Limitation:**
- Technical indicators are lagging (past-price-based), not predictive
- Useful for identifying trends already underway; not useful for forecasting reversals

**Practice:**
- Use MAs for narrative color ("Stock has rebounded above 50-day average"), not for investment conclusions
- Avoid implying causality ("Stock broke through MA, therefore it will rise") — that's prediction

### P/E, P/B "Relative to Historical"

**The claim:** "Stock P/E of 20 is cheap relative to its 3-year average of 25"

**Caution:**
- P/E changes as both stock price and earnings change
- If average P/E was high because of temporary earnings dip, current P/E may not be "cheap"
- A company's average P/E can change if fundamentals (growth rate, profitability) change

**Practice:**
- When citing historical multiples, note why the multiple was higher/lower
- Example: "P/E of 20 vs. 3-year average 25, reflecting market's lower growth expectations after recent slowdown"

---

## Volatility & Beta

### Volatility (Standard Deviation)

- **Measures**: Extent of price swings; higher volatility = wider swings
- **Common misuse**: "Stock volatility up 30%" sounds scary but is just variation in daily/weekly returns

**Practice:**
- Use volatility language carefully: "Stock has become more volatile" (wider daily swings) is factual
- Avoid: "Volatility spike signals crash coming" (volatility is retrospective; does not predict direction)

### Beta

- **Beta = 1.0**: Stock moves in line with market
- **Beta > 1.0**: Stock more volatile than market
- **Beta < 1.0**: Stock less volatile than market

**The risk:**
- "High-beta stock" in a bull market outperforms; in a bear market underperforms
- Beta is historical; past volatility does not guarantee future volatility

**Practice:**
- Use beta for describing stock characteristics ("Semiconductor stocks typically have beta > 1, making them more volatile")
- Avoid using beta to predict returns

---

## Sector Rotation & Relative Performance

### Sector Index Performance Divergence

**Good practice:**
- When market is flat or down slightly, note if certain sectors are outperforming
- Example: "TAIEX down 2%, but chip stocks up 3% and financials down 5% — sector divergence signals rotation out of finance into tech"

**Practice:**
- Compare sector-to-market performance, not just absolute sector returns
- Note if divergence is unusual (historically, sectors move together during crises; divergence in calm markets is normal)

---

## Quick Market Data Checklist

Before citing market data, verify:

- [ ] **Price timestamp**: Close? Intra-day? What date/time?
- [ ] **Return type**: Total return (incl. dividends) or price return?
- [ ] **Period clarity**: 1-year, 3-year, 5-year (if multi-year cited)?
- [ ] **Annualization proper**: If using "annualized", did I use compounding formula, not simple division?
- [ ] **Currency**: Stock price in NT$? Index in points? Any FX basis if international?
- [ ] **Index specified**: TAIEX? Sector index? Which one?
- [ ] **FX impact noted** (if applicable): Was return in NT$ or USD terms?
- [ ] **Context given**: For valuation ratios (P/E, beta), is there a peer/historical benchmark?
- [ ] **Causality avoided**: Did I avoid implying that past performance predicts future performance?
- [ ] **Peer comparison noted**: If saying "stock up 20%", is market also up 20% (relative performance is what matters)?

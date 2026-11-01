# Week 11 Student Handout — Investors as Skills

Last week: was the number knowable when you would have traded? This week: can an investor's
philosophy become a skill your AI runs the same way every time — every number computed by code
from the 10-K, the judgment the model's?

## SEC EDGAR, keyless

No key, no account. SEC asks every request to carry a User-Agent header naming the caller: your
name and your email.

| What | Where |
|---|---|
| Ticker to CIK | `https://www.sec.gov/files/company_tickers.json` |
| A company's facts | `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` — the CIK padded with zeros to ten digits |
| The docs | [EDGAR application programming interfaces](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) |

## The rules your numbers follow

| Rule | Value |
|---|---|
| Filings | 10-K only; the last five fiscal years, labelled by fiscal-year-end date |
| Flows | revenue, net income and the cash flows need a one-year period |
| Same period in several filings | the latest filing wins |
| Revenue | `RevenueFromContractWithCustomerExcludingAssessedTax`, then `Revenues` |
| Net income | `NetIncomeLoss` |
| Operating cash flow | `NetCashProvidedByUsedInOperatingActivities` |
| Capital spending | `PaymentsToAcquirePropertyPlantAndEquipment`, then `PaymentsToAcquireProductiveAssets` |
| Equity · liabilities | `StockholdersEquity` · `Liabilities` |
| Current assets · current liabilities | `AssetsCurrent` · `LiabilitiesCurrent` |
| ROE | net income ÷ year-end equity |
| Owner earnings | operating cash flow − capital spending |
| Current ratio | current assets ÷ current liabilities |
| A value not found | prints "not found", never an estimate |
| Equity zero or below | ROE and liabilities ÷ equity are "not known" |
| A check with a missing input | "not known" |

## The digits, once

Costco (COST), $ millions:

| FY end | Net income | Operating cash flow | Capital spending | Owner earnings | Equity | ROE % | Current ratio | Liabilities ÷ equity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2022-08-28 | 5,844 | 7,392 | 3,891 | 3,501 | 20,642 | 28.3 | 1.02 | 2.11 |
| 2023-09-03 | 6,292 | 11,068 | 4,323 | 6,745 | 25,058 | 25.1 | 1.07 | 1.75 |
| 2024-09-01 | 7,367 | 11,339 | 4,710 | 6,629 | 23,622 | 31.2 | 0.97 | 1.96 |
| 2025-08-31 | 8,099 | 13,335 | 5,498 | 7,837 | 29,164 | 27.8 | 1.03 | 1.64 |
| 2026-08-30 | 9,226 | 15,817 | 6,435 | 9,382 | 35,803 | 25.8 | 1.06 | 1.49 |

Revenue: 226,954 in FY2022, 303,154 in FY2026. The panel on COST: Buffett 3 of 3; Graham 2 of 3,
the current ratio failing at 1.06; Burry 2 of 2.

## The rules

- **Numbers in code, judgment in the model.** The script computes every number; the memo uses only
  numbers the script printed, and the app flags any other.
- **Not found stays not found.** A missing value is never estimated; a check with a missing input is
  "not known".
- **Read FAskills, never install it.** Its data sources need paid keys; your data is SEC EDGAR.
- **A threshold is a design choice.** Write down the one you keep, and why.
- **The memo judges the business, not the price.** No price data this week.
- Under every app's title: data from SEC EDGAR; built with AI help, a learning demonstration, not
  investment advice.

Something breaks? Debug with your AI: the exact command and the exact error text.

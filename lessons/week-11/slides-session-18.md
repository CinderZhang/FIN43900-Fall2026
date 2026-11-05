# Session 18 — Legend Investor as Skill

> **One thing today: turn Buffett's page in FAskills into a skill your AI runs the same way every time — code computes every number from the 10-K; the model only judges.**

## Today's run of show

1. Opener — 0–8
2. **R** Buffett's page and the rules — 8–15
3. **Build** your skill and your app — 15–40
4. **V** known answer and probes — 40–52
5. Explain the code — 52–58
6. Decision, learn, reflect — 58–70
7. Checkout — 70–75

[Lab 18](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-11/lab-18-legend-investor-as-skill.md)

---

## D — the question, the same for everyone

**Minutes 0–8**

> **Can an investor's philosophy become a skill your AI runs the same way every time — every number computed by code from the 10-K, the judgment the model's?**

Paste it into a new chat.

**Explain to your partner first** (five minutes, no screen): one thing on Buffett's page that code
can compute, and one that only judgment can. Swap.

Something not working? Debug with your AI: the exact command and the exact error text.

---

## R — Buffett's page, and the rules your numbers follow

**Minutes 8–15**

FAskills pulls its data from paid services: read Buffett's page, never install FAskills or use its
data sources. Your numbers come from SEC EDGAR, keyless, by these rules:

| Rule | Value |
|---|---|
| Filings | 10-K only; the last five fiscal years, labelled by fiscal-year-end date |
| Flows | revenue, net income and the cash flows need a one-year period |
| Same period in several filings | the latest filing wins |
| Revenue | `RevenueFromContractWithCustomerExcludingAssessedTax`, then `Revenues` |
| Net income | `NetIncomeLoss` |
| Operating cash flow | `NetCashProvidedByUsedInOperatingActivities` |
| Capital spending | `PaymentsToAcquirePropertyPlantAndEquipment`, then `PaymentsToAcquireProductiveAssets` |
| Equity | `StockholdersEquity` |
| ROE | net income ÷ year-end equity |
| Owner earnings | operating cash flow − capital spending |
| A value not found | prints "not found", never an estimate |
| Equity zero or below | ROE and liabilities ÷ equity are "not known" |
| A check with a missing input | "not known" |

---

## Build — your skill and your app, your request

**Minutes 15–40**

No request is given: write your own to your AI from this list, Buffett's page and the rules.

**What a skill is:** a folder with a `SKILL.md` file. The file starts with a name and a
description between `---` lines, then gives your AI the instructions. Scripts can sit in the
same folder.

Your skill must:

1. live where your AI reads skills (its skills page says where), with a name and a description
   that says when to use it;
2. bundle a script that, for a ticker, downloads the company's facts from SEC EDGAR — keyless, with
   a User-Agent naming you and your email — and prints the last five fiscal years: revenue, net
   income, operating cash flow, capital spending, equity, ROE and owner earnings, each with its
   XBRL tag;
3. compute Buffett's three checks in code: ROE of 15% or more every year; owner earnings positive
   every year; owner earnings grew, first year to last;
4. then have the AI, as Buffett, write a short memo — own the business, watch it, or pass — using
   only numbers the script printed, saved as a `.md` file. The memo judges the business, not the
   price: no price data this week.

Your app must: a Streamlit app that, for a ticker,

1. shows owner earnings and net income over the five years as a chart;
2. shows the table and the three checks;
3. shows the memo, and flags every number in the memo the script did not print;
4. says under the title: data from SEC EDGAR; built with AI help, a learning demonstration, not
   investment advice.

**Sources:** your AI's skills page — [Antigravity](https://antigravity.google/docs/skills) ·
[Codex](https://developers.openai.com/codex/skills) · SEC EDGAR: ticker to CIK,
`https://www.sec.gov/files/company_tickers.json`; facts,
`https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` (the CIK padded to ten digits);
[EDGAR API docs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) ·
[Buffett's page](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/warren_buffett.md) ·
[Streamlit docs](https://docs.streamlit.io).

Ask your AI to use your skill on COST. *Expect:* Costco's five fiscal years with their tags, the
three checks, and Buffett's memo in a `.md` file. Then run the app. *Expect:* owner earnings and
net income both up from FY2022 to FY2026, the table, the checks and the memo.

**At minute 20:** open the quiz attempt — Brightspace → Quizzes → Lab 18.

---

## V — prove it on the known answer

**Minutes 40–47**

Costco (COST), $ millions:

| FY end | Revenue | Net income | Operating cash flow | Capital spending | Equity | ROE % | Owner earnings |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2022-08-28 | 226,954 | 5,844 | 7,392 | 3,891 | 20,642 | 28.3 | 3,501 |
| 2023-09-03 | 242,290 | 6,292 | 11,068 | 4,323 | 25,058 | 25.1 | 6,745 |
| 2024-09-01 | 254,453 | 7,367 | 11,339 | 4,710 | 23,622 | 31.2 | 6,629 |
| 2025-08-31 | 275,235 | 8,099 | 13,335 | 5,498 | 29,164 | 27.8 | 7,837 |
| 2026-08-30 | 303,154 | 9,226 | 15,817 | 6,435 | 35,803 | 25.8 | 9,382 |

| Buffett's check | COST |
|---|---|
| ROE of 15% or more every year | pass |
| Owner earnings positive every year | pass |
| Owner earnings grew, first year to last | pass |

Every value matches, or debug with your AI until they do.

---

## Probes — it computes, not pastes

**Minutes 47–52**

1. **JPMorgan (JPM).** *Expect:* capital spending "not found", owner earnings "not found", Buffett's
   two owner-earnings checks "not known" — and the memo says it cannot judge owner earnings.
2. **A number by hand.** Type into COST's memo an ROE the script never printed, such as 40.0%.
   *Expect:* the app flags it.
3. **A fresh chat with no skill** (a browser AI does it): "Is Costco a Buffett business? Give its
   ROE for the last five years." Compare with the table: where did its numbers come from?

---

## Explain the code

**Minutes 52–58**

Six minutes, no AI. Open the function in your script that turns EDGAR's
facts into one year's row. Explain it to your partner line by line; your partner asks where "not
found" comes from, and you answer from the code. Swap.

---

## Your decision · Agent skills

**Minutes 58–70**

One line under the memo: **do you trust Buffett's verdict on COST, and why?**

**Agent skills — Learn on your own:**

1. What is it?
2. How does it work — why does the AI read only the name and description until it needs the rest?
3. Explain to your partner why the numbers belong in code, not in the model.

---

## Reflect

**Minutes 58–70**

Explain to your partner:

1. what your skill makes the same every time, and what it leaves to the model;
2. why "not found" is a better answer than an estimate.

---

## Checkout — on GitHub

**Minutes 70–75**

**Brightspace → Quizzes → Lab 18.**

**GitHub links of your files: md, py and/or other files as needed.**

**Before Thursday — do these**

1. Keep your skill and app matching COST.
2. Find the largest company inside one of your Project 2 funds, note its ticker, and read Cathie
   Wood's and Burry's pages: the [Thursday prework](student-prework.md).

**Thursday preview:** the panel — Cathie Wood and Burry join Buffett on the same 10-K facts; then the
largest company inside one of your Project 2 funds.

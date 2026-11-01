<!-- AUTHORED HOME. Rebuilt 2026-11-01 on the owner's order: AI skills from FAskills — a panel of three
     investor skills on the same 10-K facts; the 2026-10-28 trading-strategy version is superseded. -->

# Lab 19 — Legend Panel

**One thing today: add Graham and Burry as skills, run the three on one company, show them side by side in your app, and decide whether to trust the panel.**

**Category:** Thursday merit checkout; anchors below.

**Pace — 75 minutes, on the slides:** opener 0–8 · build the panel 8–33 · V and probe 33–43 · your company 43–50 · explain the code 50–56 · bull and bear 56–62 · decision and learn 62–70 · reflect and checkout 70–75.

**You arrive with:** your [Lab 18](lab-18-holdout-test.md) skill and app matching COST · your Lab 18
chat · your partner · the ticker of the largest company inside one of your Project 2 funds
([the prework](student-prework.md)).

Open your app first: COST's values. **Something not working?** Debug with your AI: paste the exact command and the exact error text.

## D — the question, the same for everyone

> **When three investors' skills read the same 10-K facts, where do they agree, where do they split — and would you trust the panel?**

Paste it into your Lab 18 chat.

**Explain to your partner first** (five minutes, no screen): from their pages, one place Graham or
Burry would read Costco differently from Buffett. Swap.

## Build — the panel, your request

Write your own request to your AI; keep everything your skill and app already do. The same facts
and the same rules as Lab 18, plus `Liabilities`, `AssetsCurrent` and `LiabilitiesCurrent`;
current ratio = current assets ÷ current liabilities.

Your panel must:

1. two more skills, Graham and Burry from FAskills, each with its checks in code on the same facts —
   **Graham:** current ratio of 2 or more, latest year; net income positive every year; net income
   grew, first year to last. **Burry:** operating cash flow at least net income every year;
   liabilities no more than twice equity, latest year;
2. each skill writes its own memo from printed numbers only;
3. the app shows a panel table — investor × check: pass, fail or not known — each investor's
   verdict, the three memos side by side, and the unprinted-number flag across all memos.

**Sources:** [Graham's page](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/ben_graham.md) ·
[Burry's page](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/michael_burry.md) ·
[Streamlit docs](https://docs.streamlit.io).

Run the panel on COST. *Expect:* the panel table, three verdicts and three memos side by side.

**At minute 30:** open the quiz attempt — Brightspace → Quizzes → Lab 19.

## V — prove it on the known answer

Costco (COST), the two new ratios:

| FY end | 2022-08-28 | 2023-09-03 | 2024-09-01 | 2025-08-31 | 2026-08-30 |
|---|---:|---:|---:|---:|---:|
| Current ratio | 1.02 | 1.07 | 0.97 | 1.03 | 1.06 |
| Liabilities ÷ equity | 2.11 | 1.75 | 1.96 | 1.64 | 1.49 |

### The panel on COST

| Investor | Check | COST |
|---|---|---|
| Buffett | ROE of 15% or more every year | pass |
| Buffett | Owner earnings positive every year | pass |
| Buffett | Owner earnings grew, first year to last | pass |
| Graham | Current ratio of 2 or more, latest year | **fail** (1.06) |
| Graham | Net income positive every year | pass |
| Graham | Net income grew, first year to last | pass |
| Burry | Operating cash flow at least net income every year | pass |
| Burry | Liabilities no more than twice equity, latest year | pass (1.49) |

Buffett 3 of 3, Graham 2 of 3, Burry 2 of 2. Every value matches, or debug with your AI until they
do.

**Probe — a threshold is a design choice.** Lower Graham's current-ratio threshold to 1.0 in his
skill. *Expect:* Graham now passes COST. Record the threshold you keep, and why, in one line under
Graham's memo.

## Your company

Run the panel on your fund's largest company. *Expect:* its panel table, verdicts and memos. A
check not known stays not known. No 10-K on EDGAR for it? Take the fund's next-largest company
that files one, and say so.

## V — explain the code, bull and bear

**Explain the code** (six minutes, no AI). Open the function that turns Graham's checks into pass,
fail or not known. Explain it to your partner line by line; your partner asks what it does when an
input is missing, and you answer from the code. Swap.

**Partner attack.** Your partner argues the bear case on your company from the panel; you argue the
bull case from the same panel. Two sentences each. Swap.

## Your decision

**Would you let this panel screen companies for your Project 2 — yes, no, or only with a
condition?** One line, with the condition.

## Floor

The panel matches COST; your company's panel with every gap kept; bull and bear; your decision.
You submit individually.

## A panel of AI agents — Learn on your own

1. What is it? 2. How does it work — why do three personas on the same facts disagree? 3. Explain
it to your partner.

## Reflect

Explain to your partner: 1. where the panel agreed on your company and where it split; 2. what the
threshold probe says about any screen's verdict.

## References

- FAskills, the financial-researcher plugin:
  [github.com/CinderZhang/FAskills](https://github.com/CinderZhang/FAskills).
- Skills pages: [Antigravity](https://antigravity.google/docs/skills) ·
  [Codex](https://developers.openai.com/codex/skills).
- [SEC EDGAR API docs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

## Merit anchors — five criteria, 5 points each, 25 in total

**4** = one minor weakness; **2** = an important link incomplete; **1** = minimal; **0** = missing
or fabricated.

| Criterion | 5 | 3 | 0–1 |
|---|---|---|---|
| Known answer reproduced | the panel matches COST: Buffett 3 of 3, Graham 2 of 3 with the current ratio failing at 1.06, Burry 2 of 2 | one check off | not attempted, or typed in |
| Numbers in code | every memo number printed by a script; the flag works across all memos | the flag misses a memo | memo numbers the script never printed |
| Honest gaps | "not found" and "not known" kept | one gap filled by a guess | estimates in place of gaps |
| Your company run | panel table, verdicts and memos for your fund's largest company | one investor missing | not run |
| The decision | follows the panel and names the condition | decision with a vague condition | contradicts the panel, or no decision |

**Next week:** Project 2 studio.

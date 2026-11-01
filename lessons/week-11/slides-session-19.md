# Session 19 — Legend Panel

> **One thing today: add Graham and Burry as skills, run the three on one company, show them side by side in your app, and decide whether to trust the panel.**

## Today's run of show

1. Opener — 0–8
2. **Build** the panel — 8–33
3. **V** known answer and probe — 33–43
4. Your company — 43–50
5. Explain the code — 50–56
6. Bull and bear — 56–62
7. Decision and learn — 62–70
8. Reflect and checkout — 70–75

[Lab 19](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-11/lab-19-signal-decision.md)

---

## D — the question, the same for everyone

**Minutes 0–8**

Open your app first: COST's values.

> **When three investors' skills read the same 10-K facts, where do they agree, where do they split — and would you trust the panel?**

Paste it into your Lab 18 chat.

**Explain to your partner first** (five minutes, no screen): from their pages, one place Graham or
Burry would read Costco differently from Buffett. Swap.

Something not working? Debug with your AI: the exact command and the exact error text.

---

## Build — the panel, your request

**Minutes 8–33**

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

---

## V — prove it on the known answer

**Minutes 33–43**

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

---

## Your company

**Minutes 43–50**

Run the panel on your fund's largest company. *Expect:* its panel table, verdicts and memos. A
check not known stays not known. No 10-K on EDGAR for it? Take the fund's next-largest company
that files one, and say so.

---

## Explain the code

**Minutes 50–56**

Six minutes, no AI. Open the function that turns Graham's checks into pass,
fail or not known. Explain it to your partner line by line; your partner asks what it does when an
input is missing, and you answer from the code. Swap.

---

## Bull and bear

**Minutes 56–62**

**Partner attack.** Your partner argues the bear case on your company from the panel; you argue the
bull case from the same panel. Two sentences each. Swap.

---

## Your decision · A panel of AI agents

**Minutes 62–70**

**Would you let this panel screen companies for your Project 2 — yes, no, or only with a
condition?** One line, with the condition.

**A panel of AI agents — Learn on your own:**

1. What is it?
2. How does it work — why do three personas on the same facts disagree?
3. Explain it to your partner.

---

## Reflect

**Minutes 70–75**

Explain to your partner:

1. where the panel agreed on your company and where it split;
2. what the threshold probe says about any screen's verdict.

---

## Checkout — on GitHub

**Minutes 70–75**

**Brightspace → Quizzes → Lab 19.**

**GitHub links of your files: md, py and/or other files as needed.**

**Next week:** Project 2 studio.

# Session 18 — Holdout Test

> **One thing today: freeze a trading rule before you look, then let an untouched holdout judge it.**

## Today's run of show

1. Opener: the **D** question — 0–8
2. **R** rule card — 8–18
3. **I** build the backtest — 18–38
4. **V** known answer — 38–48
5. Explain the code — 48–54
6. Swap and break — 54–60
7. Decision, learn, reflect — 60–70
8. Checkout — GitHub — 70–75

[Lab 18](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-11/lab-18-holdout-test.md)

---

## D — the question, the same for everyone

**Minutes 0–8**

> **Does a rule that worked in development still work on months it has never seen — after costs?**

Paste it into your Lab 17 chat. Today the signal is a training series. Thursday it is yours.

**Explain to your partner first** (five minutes, no screen): how one week of timing leakage made
F-Squared's record. Then swap.

Something not working? Debug with your AI: the exact command and the exact error text.

---

## R — freeze the rule first

**Minutes 8–18**

In a new `.md` file, write this rule card **before you build anything**, then commit and push it to
GitHub. The commit time is your proof that the rule came first.

| Rule card | Training value |
|---|---|
| Signal | month-end card-spend change, published by month-end |
| Rule | signal above 0 → hold the equity fund next month; otherwise Treasury bills |
| Lag | one month: this month's signal decides next month's position |
| Cost | 0.10% in any month the position switches; start in bills |
| Bills return | 0.3% a month |
| Development | 2025-01 to 2025-12 |
| Holdout | 2026-01 to 2026-06, run once, never tuned |
| Benchmark | buy-and-hold equity fund |
| Failure rule | stop if the holdout net return trails buy-and-hold |

---

## R — the training table

**Minutes 8–18**

| Month | Signal % | Equity fund % |
|---|---:|---:|
| 2024-12 | 0.8 | — |
| 2025-01 | 1.2 | 2.0 |
| 2025-02 | 0.9 | 1.5 |
| 2025-03 | 1.5 | 3.0 |
| 2025-04 | −1.0 | −2.5 |
| 2025-05 | −0.7 | −1.5 |
| 2025-06 | −1.4 | −3.0 |
| 2025-07 | 1.1 | 2.5 |
| 2025-08 | 0.6 | 1.0 |
| 2025-09 | 0.9 | 2.0 |
| 2025-10 | −0.9 | −2.0 |
| 2025-11 | −0.5 | −1.0 |
| 2025-12 | 1.6 | 3.5 |
| 2026-01 | −1.1 | −2.0 |
| 2026-02 | 0.7 | 1.5 |
| 2026-03 | −1.3 | −3.0 |
| 2026-04 | 0.8 | 2.0 |
| 2026-05 | −0.6 | −1.5 |
| 2026-06 | 0.5 | 1.0 |

---

## I — build the backtest from the instruction

**Minutes 18–38**

1. Send this to your AI partner, then paste the rule card and the table under it:

   > Write one Python file, `backtest.py`, standard library only. At the top, editable inputs: the
   > monthly table I paste below, the lag in months, the cost per switch, the bills return, and the
   > development and holdout months. Apply the rule exactly as my rule card says, starting in
   > bills. For development and for holdout separately, print the rule's compounded return gross
   > and net of costs, buy-and-hold's compounded return, and the number of switches, in percent to
   > two decimals. The holdout starts from the position held at the end of development. Then print
   > whether the failure rule is triggered. Compute everything from the inputs; never type an
   > answer in. Give me the command to run it.

2. Save it as `backtest.py`. Run `python backtest.py`. *Expect:* development and holdout results and the failure-rule line.
3. Ask your AI to quiz you on the line you understand least; answer before it explains.

**At minute 25:** open the quiz attempt — Brightspace → Quizzes → Lab 18.

---

## V — prove it on the known answer

**Minutes 38–48**

| Period | Rule gross | Rule net | Buy-and-hold | Switches |
|---|---:|---:|---:|---:|
| Development | 6.55 | 6.13 | 5.33 | 4 |
| Holdout | −5.52 | −6.09 | −2.09 | 6 |

Failure rule: **triggered** — the holdout trails buy-and-hold by 4 points. Every value matches, or
debug with your AI until they do. Turnover: each switch moves all the money, so 4 switches is 400%
one-way turnover in development and 6 is 600% in the holdout.

---

## Explain the code

**Minutes 48–54**

**Explain the code** (six minutes, no AI). Open the block of `backtest.py` that applies the lag and decides each month's position. Explain it to your partner line by
line; your partner asks one question you answer from the code. Swap. A line you cannot explain is
your next question for your AI.

---

## Swap and break

**Minutes 54–60**

Run your partner's `backtest.py`; same values. In their file set the lag to `0`.

*Expect:* development net jumps to **17.72%**. Undo.

That jump is the leak: the rule is trading on a number it could not have had.

---

## Your decision · Holdout · Reflect

**Minutes 60–70**

**Continue unchanged, stop, or register a new hypothesis** — one line, under your rule card. A new
rule is a new hypothesis that needs new months, never the same holdout.

**Holdout — Learn on your own:**

1. What is it?
2. How does it work — why is a holdout used once?
3. Explain to your partner why tuning the rule after seeing 2026 would make the holdout worthless.

**Reflect — explain to your partner:** 1. why development looked good; 2. what the commit time proves.

---

## Checkout — on GitHub

**Minutes 70–75**

**Brightspace → Quizzes → Lab 18.**

**GitHub links of your files: md, py and/or other files as needed.**

**Before Thursday — do these**

1. Keep `backtest.py` matching the Lab 18 known answer.
2. Have your admitted or quarantined series from Lab 17 ready.
3. Have your prices from Lab 15 ready.

**Thursday preview:** your admitted series from Lab 17, a rule you freeze first, and a placebo.

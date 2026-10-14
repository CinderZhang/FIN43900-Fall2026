# Session 16 — Provenance Gate

> **One thing today: build a point-in-time filter, and prove on the known answer what was knowable on the decision date.**

## Today's run of show

1. Opener — 0–8
2. **D** and **R** — 8–15
3. **I** build — 15–35
4. **V** known answer — 35–45
5. Explain the code — 45–52
6. Swap and break — 52–60
7. Learn and reflect — 60–70
8. Checkout — 70–75

[Lab 16](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-10/lab-16-provenance-gate.md)

---

## Explain to your partner first

**Minutes 0–8**

Five minutes, no screen: the difference between the month a number measures and the day it was
published. Then swap.

Something not working? Debug with your AI: the exact command and the exact error text.

---

## D — the question, the same for everyone

**Minutes 8–15**

> **On the day you would have traded, what did this data actually say — and how much of what you
see now came later?**

Paste it into your Lab 15 chat. Today the data is a training table. Thursday it is your own series.

---

## R — the training table (fictional card-spend index, three retailers)

**Minutes 8–15**

Decision date: **31 March 2026**. A row is knowable only if it was published on or before that day.

| Row | Ticker | Month measured | Published on | Index |
|---:|---|---|---|---:|
| 1 | AAA | 2026-01 | 2026-02-10 | 101.0 |
| 2 | AAA | 2026-02 | 2026-03-10 | 104.0 |
| 3 | AAA | 2026-03 | 2026-04-10 | 109.0 |
| 4 | AAA | 2026-02 | 2026-03-25 | 103.0 |
| 5 | BBB | 2026-01 | 2026-02-10 | 98.0 |
| 6 | BBB | 2026-02 | 2026-03-10 | 97.0 |
| 7 | BBB | 2026-02 | 2026-03-10 | 97.0 |
| 8 | BBB | 2026-03 | 2026-04-10 | 92.0 |
| 9 | CCC | 2026-01 | 2026-02-10 | 110.0 |
| 10 | CCC | 2026-02 | 2026-04-05 | 112.0 |
| 11 |  | 2026-02 | 2026-03-10 | 99.0 |
| 12 | CCC | 2026-02 | 2026-03-10 | 111.0 |

The rules, in this order: (1) quarantine a row with no ticker; (2) remove an exact duplicate;
(3) remove a row published after the decision date; (4) where one ticker and month has two
publications, keep the latest one published by the decision date (a revision). The signal is the
change in the index from the previous month to the latest knowable month.

---

## I — build the filter from the instruction

**Minutes 15–35**

1. Send this to your AI partner, then paste the table and the rules under it. The code it writes
   is yours: read it, run it, debug it.

> Write one Python file, `asof.py`, standard library only. At the top, editable inputs: the
> table I paste below and a decision date of 2026-03-31. Apply my four rules in order and print
> the row funnel: for each rule, how many rows it removed and their row numbers. Print the as-of
> panel that remains. For each ticker print the signal: the percent change from the previous
> month to the latest month in the panel, to two decimals, naming that month. Then print a
> naive signal for comparison: the same calculation using every row's latest publication,
> ignoring the publication date. Compute everything from the inputs; never type an answer in.
> Give me the command to run it.

2. Run `python asof.py`. *Expect:* the funnel, the as-of panel, and the as-of and naive signal for
   each ticker; if not, debug with your AI.
3. Ask your AI to quiz you on the line you understand least; answer before it explains.

**At minute 20:** open the quiz attempt — Brightspace → Quizzes → Lab 16.

---

## V — prove it on the known answer: the row funnel

**Minutes 35–45**

| Funnel step | Rows removed |
|---|---|
| Quarantined: no ticker | 11 |
| Exact duplicate | 7 |
| Published after 31 March | 3, 8, 10 |
| Older vintage replaced by a revision | 2 |
| As-of panel | 1, 4, 5, 6, 9, 12 |

---

## V — prove it on the known answer: the signals

**Minutes 35–45**

| Ticker | As-of signal | Naive signal |
|---|---|---|
| AAA | +1.98% (February) | +5.83% (March) |
| BBB | −1.02% (February) | −5.15% (March) |
| CCC | +0.91% (February) | +1.82% (February, revised) |

Every value matches, or debug with your AI until they do. The classic error: row 2 kept instead
of its revision, row 4, which turns AAA's +1.98% into +2.97%.

---

## Explain the code

**Minutes 45–52**

**Explain the code** (six minutes, no AI). Open the block of `asof.py` that applies rule 4: one
ticker and month, two publications, keep the latest one published by the decision date. Explain
it to your partner line by line; your partner asks one question you answer from the code. Swap.
A line you cannot explain is your next question for your AI.

---

## Swap and break

**Minutes 52–60**

Run your partner's `asof.py`; same values.

In their file set the decision date to `2026-04-15`. *Expect:* the as-of signal becomes the naive
signal, ticker for ticker. Undo.

The gap between the two columns is exactly what had not been published yet.

---

## Point-in-time — Learn on your own · Reflect

**Minutes 60–70**

**Learn on your own:**

1. What is look-ahead bias?
2. How does it work — event time, publication time, revision?
3. Explain it to your partner with AAA: why does +5.83% look better than anything you could have
   known?

**Reflect — explain to your partner:**

1. Which rule removed the row that mattered most;
2. What a backtest built on the naive column would claim.

---

## Checkout — on GitHub

**Minutes 70–75**

**Brightspace → Quizzes → Lab 16.**

**GitHub links of your files: md, py and/or other files as needed.**

**Before Thursday — do these**

1. Keep `asof.py` matching the Lab 16 known answer.
2. Bring your Lab 16 chat and your Project 2 universe from Lab 15.
3. Build your ALFRED series table ([prework](student-prework.md)).

**Thursday preview:** your own monthly series from ALFRED, through the same filter.

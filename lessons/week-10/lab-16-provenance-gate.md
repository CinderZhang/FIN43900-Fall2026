<!-- AUTHORED HOME. Rebuilt 2026-10-13 under the 2026-09 rulings (instruction, not materials; one
     thing per lab; harness the topic; two-person teams; GitHub is the main delivery). -->

# Lab 16 — Provenance Gate

**One thing today: build a point-in-time filter, and prove on the known answer what was knowable on the decision date.**

**Category:** Tuesday completion checkout, **25 or 0**.

**Pace — 75 minutes, on the slides:** opener 0–8 · D and R 8–15 · I 15–35 · V 35–45 · explain the code 45–52 · swap and break 52–60 · learn and reflect 60–70 · checkout 70–75.

**You arrive with:** your Course/Work Folder · your Lab 15 chat · your partner · the
[ALFRED reading](student-prework.md).

**Something not working?** Debug with your AI: paste the exact command and the exact error text.

## D — the question, the same for everyone

> **On the day you would have traded, what did this data actually say — and how much of what you
see now came later?**

Paste it into your Lab 15 chat. Today the data is a training table. Thursday it is your own series.

**Explain to your partner first** (five minutes, no screen): the difference between the month a
number measures and the day it was published. Then swap.

## R — the training table (fictional zero-coupon bond funds, three ratings)

**One table, three lessons.**

1. **Data gating.** Between a source and your model sits a gate: every row is admitted,
   quarantined or removed by a stated rule, and its row number is kept. Today's four rules are a
   *provenance* gate: they ask *when* a number was knowable, not whether it makes sense.
2. **APIs.** Data arrives as records from an API: you send a request, and the server answers with
   rows. ALFRED's API, Thursday's source, would send AAA's two February rows like this:

   ```json
   {"realtime_start": "2026-03-10", "realtime_end": "2026-03-24", "date": "2026-02-01", "value": "104.0"}
   {"realtime_start": "2026-03-25", "realtime_end": "9999-12-31", "date": "2026-02-01", "value": "103.0"}
   ```

   `date` is the month measured, `realtime_start` the published-on date; a revision is a second
   record for the same `date`, published later. The table below is such a response, flattened.
   Thursday you download from the ALFRED website, with no key.
3. **Fixed income.** Read each price as a fund of one-year zero-coupon bonds, per 100 of face
   value, rated AAA, BBB or CCC. A zero pays 100 at maturity and nothing before, so its yield is
   100 ÷ price − 1. BBB in January: 100 ÷ 98.0 − 1 = +2.04%. Two facts every price must respect:
   above 100 the yield is negative (you pay more than you will ever get back); and at the same
   maturity riskier credit yields more, so it is priced lower — AAA above BBB above CCC.

**The errors are planted.** AAA and CCC trade above 100, and CCC is priced above BBB. The four
rules will not catch them; you will, under V.

Decision date: **31 March 2026**. A row is knowable only if it was published on or before that day.

| Row | Ticker | Month measured | Published on | Price |
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
change in the price from the previous month to the latest knowable month: the fund's return.

## I — build the filter from the instruction

1. Send this to your AI partner, then paste the table and the rules above under it. The code it writes is yours: read it,
   run it, debug it.

   > Write one Python file, `asof.py`, standard library only. At the top, editable inputs: the
   > table I paste below and a decision date of 2026-03-31. Apply my four rules in order and print
   > the row funnel: for each rule, how many rows it removed and their row numbers. Print the as-of
   > panel that remains. For each ticker print the signal: the percent change from the previous
   > month to the latest month in the panel, to two decimals, naming that month. Then print a
   > naive signal for comparison: the same calculation using every row's latest publication,
   > ignoring the publication date. Compute everything from the inputs; never type an answer in.
   > Give me the command to run it.

2. Save it as `asof.py`. Run `python asof.py`. *Expect:* the funnel, the panel, and two signals per ticker; if not, debug with
   your AI.
3. Ask your AI to quiz you on the line you understand least; answer before it explains.

## V — prove it on the known answer

### The row funnel

| Funnel step | Rows removed |
|---|---|
| Quarantined: no ticker | 11 |
| Exact duplicate | 7 |
| Published after 31 March | 3, 8, 10 |
| Older vintage replaced by a revision | 2 |
| As-of panel | 1, 4, 5, 6, 9, 12 |

### The signals

| Ticker | As-of signal | Naive signal |
|---|---|---|
| AAA | +1.98% (February) | +5.83% (March) |
| BBB | −1.02% (February) | −5.15% (March) |
| CCC | +0.91% (February) | +1.82% (February, revised) |

Every value matches, or debug with your AI until they do. The classic error: row 2 kept instead
of its revision, row 4, which turns AAA's +1.98% into +2.97%.

### The sanity check — by hand, on the as-of panel

The gate passed all six rows. Work out each yield, 100 ÷ price − 1, and name what it breaks.

| Row | Fund | Month | Price | Yield | Breaks |
|---:|---|---|---:|---:|---|
| 1 | AAA | Jan | 101.0 | −0.99% | negative yield |
| 4 | AAA | Feb | 103.0 | −2.91% | negative yield |
| 5 | BBB | Jan | 98.0 | +2.04% | nothing |
| 6 | BBB | Feb | 97.0 | +3.09% | nothing |
| 9 | CCC | Jan | 110.0 | −9.09% | negative yield; priced above BBB and AAA |
| 12 | CCC | Feb | 111.0 | −9.91% | negative yield; priced above BBB and AAA |

On time is not the same as true: a provenance gate needs a sanity gate behind it.

**Explain the code** (six minutes, no AI). Open the block of `asof.py` that applies rule 4: one ticker and month, two publications, keep the
latest one published by the decision date. Explain it to your partner line by
line; your partner asks one question you answer from the code. Swap. A line you cannot explain is
your next question for your AI.

**Swap and break.** Run your partner's `asof.py`; same values. In their file set the decision date
to `2026-04-15`. *Expect:* the as-of signal becomes the naive signal, ticker for ticker. Undo. The
gap between the two columns is exactly what had not been published yet.

## Floor

The filter matches the known answer, and the partner's later date turns it into the naive signal.
You submit individually.

## Point-in-time — Learn on your own

1. What is look-ahead bias? 2. How does it work — event time, publication time, revision? 3. Explain
it to your partner with AAA: why does +5.83% look better than anything you could have known?

## Reflect

Explain to your partner: 1. which rule removed the row that mattered most; 2. what a backtest built
on the naive column would claim; 3. the fifth rule that would have quarantined rows 1, 4, 9 and 12.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

**Thursday preview:** your own monthly series from ALFRED, through the same filter.

<!-- AUTHORED HOME. Rebuilt 2026-10-28 on the owner's order: Lab 17 shows the data as a web app
     (Streamlit), FRED-style, from live FRED/ALFRED downloads; real cases only. -->

# Lab 17 — Point-in-Time Audit

**One thing today: build a FRED-style rates app that shows what was known on any date, then decide whether Project 2 may use your series.**

**Category:** Thursday merit checkout; anchors below.

**Pace — 75 minutes, on the slides:** opener 0–8 · I the app 8–30 · V known answer 30–42 · E your series 42–52 · explain the code 52–58 · partner attack and your call 58–65 · learn, reflect, checkout 65–75.

**You arrive with:** your Lab 16 chat · your [Lab 15](../week-09/lab-15-portfolio-stability.md)
Streamlit app · the series you chose for [the prework](student-prework.md) · your partner.

**Something not working?** Debug with your AI: paste the exact command and the exact error text.

## D — the question, the same for everyone

> **Was each number in your series knowable on the day you would have traded on it — and may
Project 2 use it?**

Paste it into your Lab 16 chat.

**Explain to your partner first** (five minutes, no screen): one rate you think moves your
universe, and why. Your partner writes the reason down. Swap.

## R — the data, real and live

| Series | What it is | FRED page |
|---|---|---|
| BAA | Moody's Baa corporate bond yield, monthly | [fred.stlouisfed.org/series/BAA](https://fred.stlouisfed.org/series/BAA) |
| FEDFUNDS | Effective federal funds rate, monthly | [fred.stlouisfed.org/series/FEDFUNDS](https://fred.stlouisfed.org/series/FEDFUNDS) |
| DGS10 | 10-year Treasury yield, daily | [fred.stlouisfed.org/series/DGS10](https://fred.stlouisfed.org/series/DGS10) |
| MORTGAGE30US | 30-year fixed mortgage rate, weekly | [fred.stlouisfed.org/series/MORTGAGE30US](https://fred.stlouisfed.org/series/MORTGAGE30US) |
| Yours | the series you chose for the prework | its FRED page; the ID is the code at the end of the address |

**FRED** shows each series as it reads today; **ALFRED**, as it read on an earlier date — Tuesday's
two dates, real. Both free, no key, no account.

## I — the app, from one message

1. Send this to your Lab 16 chat:

   > Build `asof_app.py`, a Streamlit app that works like a FRED page for interest rates. Get the
   > data from FRED's public CSV downloads, no API key, one request per series: today's values from
   > `https://fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES` and the values as known on a date
   > from `https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=SERIES&vintage_date=YYYY-MM-DD`.
   > A "." in the data is a missing day. Put the two downloads in two functions and cache them.
   > Sidebar: a multiselect of series IDs with their names — BAA (Moody's Baa corporate bond
   > yield), FEDFUNDS (federal funds rate), DGS10 (10-year Treasury yield), MORTGAGE30US (30-year
   > mortgage rate), all four selected at the start; a text box to add any other FRED series ID; a
   > start date (1 January 2020 at the start); an "as known on" date (today at the start). Page: one
   > line chart per selected series, today's values from the start date, and under it the last
   > date in the data known on the "as known on" date. Then one table, a row per series: the ID
   > linked to its FRED page; the last date measured and its value as known on that date; the
   > last date measured and its value today; how many values today's data has after the last date
   > known then; how many values on the same dates have been revised since. An unknown ID shows
   > an error for that series and the rest of the page still works. Under the title, one line:
   > data from FRED and ALFRED, Federal Reserve Bank of St. Louis, downloaded today; built with AI
   > help, a learning demonstration, not investment advice. Give me the command to run it.

2. Save the file. Run it with the command your AI gave you. *Expect:* your browser opens four
   rate charts and the table, as of today. An error: paste the exact text to your AI.

**At minute 30:** open the quiz attempt — Brightspace → Quizzes → Lab 17.

## V — prove it on the known answer

Set **As known on** to **5 October 2026**. *Expect* in the "as known on" columns:

| Series | Last date known on 5 Oct 2026 | Value |
|---|---|---|
| BAA | September 2026 | 6.47 |
| FEDFUNDS | September 2026 | 3.75 |
| DGS10 | 2 October 2026 | 5.28 |
| MORTGAGE30US | 1 October 2026 | 7.28 |

If not, the app is wrong: debug with your AI until they match.

**Probe.** Add **PAYEMS** (payroll jobs, thousands); set the date to **15 January 2025**.
*Expect:* December 2024, **159,536** as known then; today's December 2024 is lower and the revised
count is well above zero. Zero revised means the app read today's data twice.

## E — your series

Add your series' ID. Set the date to the last day of last month, then today. *Expect:* the values
that vanish were not yet published then; the revised count shows whether it is revised. A daily
market rate shows almost no lag and no revisions: say so.

In your `.md` file write a **data card**: source and link, what it measures, units, how late it is
published, whether it is revised, the download date. Read three values against the FRED page
yourself.

## V — fresh eyes

**Explain the code** (six minutes, no AI). Open the function that downloads the values as known
on a date. Explain it to your partner line by line; your partner asks one question you answer from
the code. Swap. A line you cannot explain is your next question for your AI.

**Partner attack.** Your partner reads your data card and names the field they trust least:
publication date, revisions, or units. Answer in two sentences under the card, with evidence
from the app or the FRED page. Swap.

## Your call

**Admit, quarantine, or reject** your series for Project 2, with the reason and what would change it.
*Example (PAYEMS):* "Quarantine: published about a week after the month, revised in the next two
months and again each year — December 2024 read 159,536 in January 2025 and is lower today; admit
only as known on each decision date, never today's values with a fixed lag."

## Floor

The app runs and matches the 5 October 2026 known answer and the PAYEMS probe; your series in the
app with a data card; the partner's attack answered; your call. You submit individually.

## Data card — Learn on your own

1. What is it? 2. How does it work — which fields stop a leak before it starts? 3. Explain to your
partner why "cleaned the data" is not a data card.

## Reflect

Explain to your partner: 1. how late your series is published, and what your app's "as known on"
date shows about it; 2. what a backtest on today's values would have overstated.

## References

Reading only: nothing graded needs a key or an account.

- FRED API: the official route to the same data, with a free key.
  [fred.stlouisfed.org/docs/api/fred](https://fred.stlouisfed.org/docs/api/fred/)
- Financial Datasets: an API for prices, financial statements and earnings, built for AI agents.
  Same shape as ALFRED's: a request in, records out, with a key.
  [docs.financialdatasets.ai](https://docs.financialdatasets.ai)
- virattt, *ai-hedge-fund*: an open-source team of AI agents that reads its data from the
  Financial Datasets API. Educational; it makes no trades.
  [github.com/virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
- Francis, A., & Zhang, C. X. (2026). *Can AI match professional analysts? Evidence from a
  multi-agent system.* Finance Research Letters, 103, 110127.
  [doi.org/10.1016/j.frl.2026.110127](https://doi.org/10.1016/j.frl.2026.110127), through the
  Purdue Libraries login.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.** Your `asof_app.py` is one of
them.

## Merit anchors — five criteria, 5 points each, 25 in total

**4** = one minor weakness; **2** = an important link incomplete; **1** = minimal; **0** = missing
or fabricated.

| Criterion | 5 | 3 | 0–1 |
|---|---|---|---|
| Known answer reproduced | all four 5 October values match; the PAYEMS revision shown | one value off, or no probe | not attempted, or typed in |
| The app | four series and a typed ID; charts; the as-known table with late and revised counts; sources linked | one piece missing | does not run, or values hard-coded |
| Data card | source link, measure, units, lag, revisions, download date; three values checked by hand | one field missing | no card, or an unnamed source |
| Fresh eyes | partner's attack answered with evidence from the app or the source | answer without evidence | no attack |
| The call | admit, quarantine or reject with an as-of rule and a condition | call without condition | "useful correlation" overrides the as-of rule |

**Next week:** a rule frozen before you look, and a holdout you do not touch until the end.

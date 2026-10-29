# Session 17 — Point-in-Time Audit

> **One thing today: build a FRED-style rates app that shows what was known on any date, then decide whether Project 2 may use your series.**

## Today's run of show

1. Opener — 0–8
2. **I** the app — 8–30
3. **V** known answer — 30–42
4. **E** your series — 42–52
5. Explain the code — 52–58
6. Partner attack and your call — 58–65
7. Learn, reflect, checkout — 65–75

[Lab 17](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-10/lab-17-point-in-time.md)

---

## D — the question, the same for everyone

**Minutes 0–8**

> **Was each number in your series knowable on the day you would have traded on it — and may
Project 2 use it?**

Paste it into your Lab 16 chat.

**Explain to your partner first** (five minutes, no screen): one rate you think moves your
universe, and why. Your partner writes the reason down. Swap.

Something not working? Debug with your AI: the exact command and the exact error text.

---

## R — the data, real and live

**Minutes 8–30**

| Series | What it is |
|---|---|
| BAA | Moody's Baa corporate bond yield, monthly |
| FEDFUNDS | Effective federal funds rate, monthly |
| DGS10 | 10-year Treasury yield, daily |
| MORTGAGE30US | 30-year fixed mortgage rate, weekly |
| Yours | the series you chose for the prework |

**FRED** shows each series as it reads today; **ALFRED**, as it read on an earlier date — Tuesday's
two dates, real. Both free, no key, no account.

---

## I — the app, from one message

**Minutes 8–30**

Send this to your Lab 16 chat:

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

Run it with the command your AI gave you. *Expect:* four rate charts and the table, as of today.

---

## V — prove it on the known answer

**Minutes 30–42**

**At minute 30:** open the quiz attempt — Brightspace → Quizzes → Lab 17.

Set **As known on** to **5 October 2026**. *Expect:*

| Series | Last date known on 5 Oct 2026 | Value |
|---|---|---|
| BAA | September 2026 | 6.47 |
| FEDFUNDS | September 2026 | 3.75 |
| DGS10 | 2 October 2026 | 5.28 |
| MORTGAGE30US | 1 October 2026 | 7.28 |

**Probe.** Add **PAYEMS**; set the date to **15 January 2025**. *Expect:* December 2024,
**159,536** as known then; today's is lower; the revised count well above zero.

---

## E — your series

**Minutes 42–52**

Add your series' ID. Set the date to the last day of last month, then today. *Expect:* the values
that vanish were not yet published then; the revised count shows whether it is revised.

**Data card** in your `.md` file: source and link, what it measures, units, how late it is
published, whether it is revised, the download date. Read three values against the FRED page.

---

## Explain the code

**Minutes 52–58**

Six minutes, no AI. Open the function that downloads the values as known on a date. Explain it to
your partner line by line; your partner asks one question you answer from the code. Swap.

---

## Partner attack · Your call

**Minutes 58–65**

**Partner attack.** Your partner names the data-card field they trust least: publication date,
revisions, or units. Answer in two sentences, with evidence from the app or the FRED page. Swap.

**Your call: admit, quarantine, or reject** your series for Project 2, with the reason and what
would change it.

*Example (PAYEMS):* "Quarantine: published about a week after the month, revised in the next two
months and again each year — December 2024 read 159,536 in January 2025 and is lower today; admit
only as known on each decision date, never today's values with a fixed lag."

---

## Data card — Learn on your own · Reflect

**Minutes 65–75**

**Learn on your own:**

1. What is it?
2. How does it work — which fields stop a leak before it starts?
3. Explain to your partner why "cleaned the data" is not a data card.

**Reflect — explain to your partner:**

1. How late your series is published, and what your app's "as known on" date shows about it;
2. What a backtest on today's values would have overstated.

---

## Checkout — on GitHub

**Minutes 65–75**

**Brightspace → Quizzes → Lab 17.**

**GitHub links of your files: md, py and/or other files as needed.** Your `asof_app.py` is one of them.

**Before Tuesday — do these**

1. Keep your Lab 17 chat, your app and your call.
2. Read the [F-Squared reading](../week-11/student-prework.md).

**Next week:** a rule frozen before you look, and a holdout you do not touch until the end.

# Session 17 — Point-in-Time Audit

> **One thing today: put your own series through the filter, and decide whether Project 2 may use it.**

## Today's run of show

1. Opener — 0–8
2. **R** your series — 8–25
3. **E** on the training table — 25–40
4. Your series — 40–52
5. Explain the code — 52–58
6. Partner attack and your call — 58–65
7. Learn, reflect, checkout — 65–75

[Lab 17](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-10/lab-17-point-in-time.md)

---

## D — the question, the same for everyone

**Minutes 0–8**

Rerun `python asof.py` first: Tuesday's values.

Something not working? Debug with your AI: the exact command and the exact error text.

> **Was each number in your series knowable on the day you would have traded on it — and may
Project 2 use it?**

Paste it into your Lab 16 chat.

---

## Explain to your partner first

**Minutes 0–8**

Five minutes, no screen: one series you think moves your universe, and why. Your partner writes
the reason down. Swap.

---

## R — your series

**Minutes 8–25**

Bring the series you built before class ([the prework](student-prework.md)): **one monthly series
from [ALFRED](https://alfred.stlouisfed.org)** that is not your funds' own prices, every vintage
of at least its last 26 months, in a table with Tuesday's columns: series name, month measured,
published on, value. In your `.md` file write a **data card**: source and link, what it measures,
units, how late it is published, whether it is revised, the download date. Read three rows
against ALFRED yourself. No table yet: build it now with your AI, as the prework says.

---

## E — many decision dates, from one message

**Minutes 25–40**

Send this to your Lab 16 chat:

> In my `asof.py`, keep everything it already prints exactly as it is. Add a list of decision dates
> at the top. For each date, apply the same four rules and print the as-of signal per ticker, or
> "not enough knowable months", and the row numbers the naive panel used for months already over by
> that date but published after it. Add an option to read my own table from a CSV file I name, with the same columns, and
> run the same report on the last day of each of the last 24 months. One file, one command.

Read what changed in `asof.py` before you run it; ask your AI about any line you cannot explain.

---

## E — the training table first

**Minutes 25–40**

Dates 28 February, 31 March, 30 April 2026. *Expect:*

| Decision date | As-of signal | Naive rows not yet published |
|---|---|---|
| 28 Feb 2026 | not enough knowable months | 4, 6, 10 |
| 31 Mar 2026 | AAA +1.98, BBB −1.02, CCC +0.91 | 3, 8, 10 |
| 30 Apr 2026 | equal to the naive signal | none |

If not, debug with your AI until they match.

**At minute 30:** open the quiz attempt — Brightspace → Quizzes → Lab 17.

---

## Your series

**Minutes 40–52**

Your series, last 24 month-ends. *Expect:* your funnel and, for each month-end, how many naive rows
were not yet published.

A series published the same day it measures shows none: say so.

---

## Explain the code

**Minutes 52–58**

**Explain the code** (six minutes, no AI). Open the block of `asof.py` that runs the filter at each
decision date. Explain it to your partner line by line; your partner asks one question you answer
from the code. Swap. A line you cannot explain is your next question for your AI.

---

## Partner attack · Your call

**Minutes 58–65**

**Partner attack.** Your partner reads your data card and names the field they trust least:
publication date, revisions, or units. Answer in two sentences under the card. Swap.

**Your call: admit, quarantine, or reject** the series for Project 2, with the reason and what
would change it.

*Example (training table):* "Quarantine: a publication lag of 10 to 36 days after month-end and a
revision to AAA February; admit only through the as-of filter — a fixed lag on today's data still
uses CCC's February value, published 5 April."

---

## Data card — Learn on your own · Reflect

**Minutes 65–75**

**Learn on your own:**

1. What is it?
2. How does it work — which fields stop a leak before it starts?
3. Explain to your partner why "cleaned the data" is not a data card.

**Reflect — explain to your partner:**

1. How late your series is published, and why the as-of filter handles it;
2. What a naive backtest on it would have overstated.

---

## Checkout — on GitHub

**Minutes 65–75**

**Brightspace → Quizzes → Lab 17.**

**GitHub links of your files: md, py and/or other files as needed.**

**Before Tuesday — do these**

1. Keep your Lab 17 chat and your call.
2. Read the [F-Squared reading](../week-11/student-prework.md).

**Next week:** a rule frozen before you look, and a holdout you do not touch until the end.

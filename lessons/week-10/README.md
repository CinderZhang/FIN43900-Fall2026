# Week 10 — Alternative Data Provenance and Point-in-Time Admission

## Mission

Tuesday: build a point-in-time filter from an instruction and prove, on a training table, what was
knowable on the decision date. Thursday: build a FRED-style Streamlit app from live FRED and ALFRED
data that shows what was known on any date, and decide whether Project 2 may use your series.

One table, three lessons: the training table is a set of zero-coupon bond-fund prices, delivered
the way an API delivers records, with errors planted on purpose. You practise **data gating**,
learn how an **API** record carries the two dates, and review **fixed income**: price, yield and
credit order.

**GitHub is the main delivery.** Every lab and project is handed in as GitHub links to your own
files.

## You arrive with

- your Lab 15 `app.py` and `portfolio.py`, your Project 2 universe and your Lab 15 chat, in your Course/Work Folder;
- your partner.

## Outcomes

- Tell the month a number measures from the day it was published, and say why it matters.
- Build an as-of filter: quarantine, duplicates, late publications, revisions — in that order.
- Show the gap between a naive signal and a knowable one, row by row.
- Read an API record: the month measured (`date`), the day published (`realtime_start`), the value.
- Price a zero-coupon bond's yield (100 ÷ price − 1) and catch prices that break finance: a
  negative yield, or riskier credit priced above safer credit.
- Build a Streamlit app that charts live FRED rates and shows what was known on any date.
- Write a data card for a real series and decide admit, quarantine or reject.

## Prerequisites and prework

**Before Tuesday — about 20 minutes.** Read only these headings on
[ALFRED Help](https://alfred.stlouisfed.org/help): **"What is ALFRED?"**, **"What is a Release and
what are Release Dates?"**, **"How are Release Dates determined?"**, and **"How does ALFRED verify
vintage data?"** (5–7 minutes). Ask: **what was knowable on the decision date, and what is visible
only because I am looking later?** The [handout's point-in-time section](student-handout.md#point-in-time-in-plain-language)
is the complete alternative.

**Before Thursday — about 15 minutes.** Choose one series on [FRED](https://fred.stlouisfed.org)
that you think moves your Project 2 universe (not your funds' own prices). Note its ID, the code at
the end of its page address (for example BAA), and read its units, frequency and release on the
page. Thursday's app pulls it live.

## The two sessions

| Session | Lab | One thing |
|---|---|---|
| Tuesday | [Lab 16](lab-16-provenance-gate.md) | the as-of filter, proved on the training table |
| Thursday | [Lab 17](lab-17-point-in-time.md) | a FRED-style app showing what was known on any date, and an admit, quarantine or reject call |

## Teams this week

Two people, the same partner; each keeps their own Project 2. Explain before you build, swap
and break on Tuesday, attack one data-card field on Thursday. Checkouts stay individual.

## DRIVER this week

Define: the same question for everyone — what was knowable on the day you would have traded?
Represent: the table and the four rules. Implement: the filter from one request. Validate: the
known answer and the partner's later date. Evolve: the same question as an app on live rates, then your own series.
Reflect: why the as-of filter, not a fixed lag, keeps a backtest honest.

## Package map

- [Lab 16](lab-16-provenance-gate.md) and [Lab 17](lab-17-point-in-time.md) — the labs.
- [Student handout](student-handout.md) — point-in-time, the digits once, the rules.
- [Open challenge](open-ended-challenge.md) — after class.
- [Prework](student-prework.md) — generated from the prework section above.
- Instructor guide, grading key and verification record — instructor only, not published.

## Brightspace order

Overview → Lab 16 → Lab 17. The Brightspace module carries the standard pointer to this page.

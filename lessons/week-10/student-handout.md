# Week 10 Student Handout — Point-in-Time

Last week: the lowest-risk mix, and how far it moves. This week: were the numbers behind it
knowable when you would have acted on them?

## The commands

In the terminal, with your own Python command:

| Command | Expect |
|---|---|
| `python asof.py` | Tuesday: the row funnel, the as-of panel, and as-of beside naive signals |
| the run command your AI gives you for `asof_app.py` | Thursday: the rates app in your browser — charts, and what was known on any date |

Something breaks? Debug with your AI: the exact command and the exact error text.

## Point-in-time in plain language

Every data point has two dates. The **month measured** is what the number describes. The
**published on** date is when anyone could first see it. A decision on 31 March can use only
what was published by 31 March. A **revision** replaces an earlier number, but only from the day the
revision is published; before that, the old number is what the market saw. A backtest that uses
today's file — with every revision and every late release already in it — is answering a question
nobody could have asked at the time. That is **look-ahead bias**, and it makes weak signals look
strong.

## The digits, once

AAA on the training table, decision date 31 March 2026:

| Step | Rule | AAA |
|---|---|---|
| Knowable rows | published on or before 31 March | Jan 101.0 (10 Feb); Feb 104.0 (10 Mar); Feb 103.0 (25 Mar) |
| Revision | keep the latest publication for each month | Feb = 103.0 |
| As-of signal | latest knowable month ÷ previous month − 1 | 103.0 ÷ 101.0 − 1 = +1.98% |
| Naive signal | uses March, published 10 April | 109.0 ÷ 103.0 − 1 = +5.83% |
| The leak | naive − as-of | +3.85 points that nobody had on 31 March |

## The rules

- Every row keeps its row number from start to end. Removing a row is a recorded decision, not a
  cleanup.
- Quarantine first, then duplicates, then late publications, then revisions. The order changes
  the answer.
- A data card names the source, the measure, the units, the publication lag, the revisions and the
  download date. "Cleaned the data" is not a data card.
- If you cannot find a publication date, the series is quarantined until you can.

## DRIVER, one line each

Define — the same question for everyone. Represent — the table and four rules. Implement — the
filter from one request. Validate — the known answer and the partner's later date. Evolve and
Reflect — your own series, and the lag it needs.

<!-- AUTHORED HOME. Rebuilt 2026-10-13 under the 2026-09 rulings; self-paced (guest talk). -->

# Lab 13 — Portfolio Mandate Defense

**One thing today: turn a client's words into rules a computer can check, before anyone builds a portfolio.**

**Category:** Thursday merit checkout; anchors below.

**This lab is on your own time, on your own.** Thursday's class is a guest talk: come to it. Do
this lab after it, before the Lab 13 quiz closes. Where a step names your partner, play both roles:
you, then a sceptical colleague checking your work.

**GitHub is the main delivery from now on.** Every lab and project is handed in as GitHub links to
your files; the quiz only collects them.

**You arrive with:** your Course/Work Folder · your AI · the
[IPS reading](student-prework.md).

**Something not working?** Debug with your AI: paste the exact command and the exact error text.

## D — the question, the same for everyone

> **Which of these portfolios does the Meridian Foundation's mandate permit — and what must the
CIO answer before anyone optimizes?**

Paste it into a new AI chat, for the **assigned common case** only.

## R — the case: Meridian Foundation Reserve (fictional)

The CIO asks you to check candidate portfolios for a **$100 million reserve**.

### What the CIO said

| # | What the CIO said |
|---|---|
| S1 | Horizon seven years; annual rebalancing. |
| S2 | Objective: CPI + 4% a year, net of costs, over rolling five-year periods. |
| S3 | Pays out **$0.75 million every quarter**; twelve months of payouts held in cash or daily-liquid government securities. |
| S4 | Benchmark: 60% global equities, 40% U.S. investment-grade bonds. |
| S5 | Long-only: no borrowing, short sales or derivatives. |
| S6 | No single issuer above **8%**. |
| S7 | Annual turnover at most 25% without committee approval. |
| S8 | At least **90%** redeemable within **five business days**. |
| S9 | "The reserve cannot have a calendar-year loss greater than 10%." No measure, no breach rule. |
| S10 | No sector, ESG, tax or home-bias preference; nobody has said what the pilot should optimize. |

**Sort before you build (no AI).** In a new `.md` file, type each of S1–S10 — **objective**,
**hard constraint**, **preference**, **unverifiable promise** or **missing** — with a one-line reason.

### The holdings you may use

Issuer rule: cash, Treasury and diversified funds are exempt; one company's securities count
together.

| Holding | Issuer | Business days to redeem | Reserve-eligible |
|---|---|---:|---|
| Cash | none | 0 | yes |
| Treasury bills | U.S. Treasury | 1 | yes |
| Treasury 10-year note | U.S. Treasury | 1 | yes |
| Global equity index fund | diversified fund | 2 | no |
| Investment-grade bond fund | diversified fund | 3 | no |
| Private real estate fund | diversified fund | 90 | no |
| Acme Corp bonds | Acme Corp | 4 | no |
| Acme Corp stock | Acme Corp | 1 | no |

### The three candidates (percent of the portfolio)

| Holding | A | B | C |
|---|---:|---:|---:|
| Cash | 2 | 1 | 1 |
| Treasury bills | 2 | 0 | 1 |
| Treasury 10-year note | 10 | 0 | 0 |
| Global equity index fund | 60 | 55 | 70 |
| Investment-grade bond fund | 26 | 20 | 20 |
| Private real estate fund | 0 | 15 | 0 |
| Acme Corp bonds | 0 | 5 | 0 |
| Acme Corp stock | 0 | 4 | 8 |

## I — build the checker from the instruction

1. Send this to your AI partner, then paste the two tables above under it. The code it writes is yours: read it,
   run it, debug it.

   > Write one Python file, `mandate.py`, standard library only. At the top, editable inputs: the
   > holdings table I paste below (holding, issuer, business days to redeem, reserve-eligible);
   > candidates A, B and C as percent weights; reserve size 100 (USD millions); quarterly
   > distribution 0.75; quarters to cover 4; liquidity window 5 business days; minimum liquid
   > share 90%; issuer limit 8%. Cash, the U.S. Treasury and diversified funds are exempt from the
   > issuer limit; all securities of one company count together. Print the reserve minimum first:
   > quarters × distribution ÷ reserve size, as a percent. Then for each candidate print the
   > measured value to one decimal and "pass" or "FAIL" for: weights sum to 100; lowest weight
   > not negative (long-only); reserve-eligible weight at least the reserve minimum; weight
   > redeemable within the window at least the minimum liquid share; largest single company at
   > most the issuer limit. For the calendar-year loss rule print "requires CIO clarification" —
   > never test it. End each candidate with "passes every checkable rule" or "fails N rule(s)".
   > Compute everything from the inputs; never type an answer in. Give me the command to run it.

2. Save it as `mandate.py`. Run `python mandate.py`. *Expect:* the reserve minimum, then each candidate's rules and
   verdict; if not, debug with your AI.
3. Ask your AI to quiz you on the line you understand least; answer before it explains.

## V — prove it on the known answer

Reserve minimum: **3.0%** of the portfolio.

| Rule | A | B | C |
|---|---|---|---|
| Weights sum to 100 | 100.0 pass | 100.0 pass | 100.0 pass |
| Long-only (lowest weight) | 0.0 pass | 0.0 pass | 0.0 pass |
| Reserve ≥ 3.0% | 14.0 pass | 1.0 FAIL | 2.0 FAIL |
| Redeemable in 5 days ≥ 90% | 100.0 pass | 85.0 FAIL | 100.0 pass |
| Largest single company ≤ 8% | 0.0 pass | 9.0 FAIL | 8.0 pass |
| Calendar-year loss | requires CIO clarification | same | same |
| Verdict | passes every checkable rule | fails 3 rule(s) | fails 1 rule(s) |

Every value matches, or debug with your AI until they do. Watch Acme: its bonds and stock count
together.

**Prove it checks.** In A set Cash to `-2` and the global equity fund to `64`. Rerun.
*Expect:* A's lowest weight reads −2.0 and fails long-only, and nothing else fails — the reserve
still passes at 10.0. Set them back.

## E — attack your own checker, from one message

Send this to the same chat:

> Using only the holdings in my table, propose one portfolio that passes every rule my
> `mandate.py` checks but that the Meridian CIO could still reasonably reject. Name the CIO
> statement (S1–S10) it offends or the question it exposes. Do not optimize anything.

Add it as candidate D; run it; confirm it passes. AI closed, two sentences: does the objection
hold, and which statement decides it? Then swap candidate D with your partner: name the statement
you would cite against theirs.

## Your question for the CIO

AI closed. Write the **one** question the CIO must answer before anyone optimizes, and the answer that
would change your portfolio.

## Floor

Checker matches; probe fails long-only; S1–S10 sorted; D judged; one CIO question. You submit
individually.

## Investment policy statement — Learn on your own

1. What is it? 2. How does it work — objectives and constraints? 3. Explain it: map S1–S10 onto it
in your file.

## Reflect

Explain to your partner, then write in your file: 1. why a portfolio can pass every checkable rule
and still be wrong for this client; 2. the S1–S10 type you were least sure of.

## After this lab: your Project 2 mandate

Write your own client's mandate in the same shape: the objective, the hard constraints, and the
one question for your client. Project 2 starts from it in Week 9. Your AI is open for it.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.** Push your `.md` file and
`mandate.py`; paste each link into the Lab 13 quiz. They are the only evidence we see.

## Merit anchors — five criteria, 5 points each, 25 in total

**4** = one minor weakness; **2** = an important link incomplete; **1** = minimal; **0** = missing.

| Criterion | 5 | 3 | 0–1 |
|---|---|---|---|
| Checker | every value matches; probe fails long-only; reserve minimum computed | one rule wrong or probe skipped | does not run, or answers typed in |
| Statement types | S1–S10 typed with reasons; S9 not tested as a rule; S10 missing | reasons thin | no reasons, or S9 tested as a hard limit |
| The attack | D runs and passes; objection judged against a named statement | judgment vague | AI's answer pasted, no judgment |
| Question for the CIO | one question that blocks optimization, and the answer that changes the design | no consequence | several questions, or none |
| Reflect and policy statement | S1–S10 mapped; passing versus suitable explained | one thin | missing |

**Next week:** the same partner; portfolios built and checked against this mandate.

<!-- AUTHORED HOME. Rebuilt 2026-10-13 under the 2026-09 rulings (instruction, not materials; one
     thing per lab; harness the topic; two-person teams; GitHub is the main delivery). Lab 15 is
     the first app (owner 2026-10-14): a Streamlit app on the student's own portfolio.py. -->

# Lab 15 — Portfolio Stability Decision

**One thing today: turn your engine into your first app — a Streamlit page that finds the lowest-risk mix meeting the mandate's objective and reserve rule — and test whether its answer survives a one-point change.**

**Category:** Thursday merit checkout; anchors below.

**Pace — 75 minutes, on the slides:** opener 0–8 · R 8–15 · I the app on Meridian 15–35 · V 35–42 · your universe 42–52 · explain the code 52–58 · partner attack 58–63 · your call and learn 63–70 · reflect and checkout 70–75.

**You arrive with:** `portfolio.py` matching the [Lab 14](lab-14-portfolio-baselines.md) known
answer · Streamlit installed and its demo seen (the [prework](student-prework.md)) · your Lab 14
chat (Antigravity or Codex) · your partner · your own Project 2 mandate, written after
[Lab 13](../week-08/lab-13-portfolio-mandate.md).

Rerun `python portfolio.py` first: Tuesday's values. **Something not working?** Debug with your AI: paste the exact command and the exact error text.

## D — the question, the same for everyone

> **Which mix carries the least risk while meeting the mandate — and does the answer survive a
one-point change in one estimate?**

Paste it into your Lab 14 chat. Today the answer lives in an app your client could use: a web page
with controls, running on your own engine. Meridian first; then your own Project 2 universe.

**Explain to your partner first** (five minutes, no screen): your Project 2 universe, your
objective, and your one hard constraint. Your partner writes them down. Swap.

## R — your universe and your mandate

| Input | Meridian (training) | Yours |
|---|---|---|
| Assets | the four sleeves from Lab 14 | three to six funds from your mandate |
| Return, volatility, correlation | Lab 14's tables | estimated from five years of monthly prices |
| Objective | 6.5% expected return | your mandate's objective, as a number |
| Hard constraint | reserve-eligible weight at least 3% | your mandate's constraint, or `none` stated |

**Your prices.** Bring the `prices.csv` you built after Lab 14: five years of monthly **Adj Close**
prices, the date first, oldest month first, one column per ticker; each ticker's source and
download date in your `.md` file. No file yet: build it now, as the
[end of Lab 14](lab-14-portfolio-baselines.md#before-thursday--your-own-universe-in-funds) says.

A five-year average is history, not a forecast. Label your returns `estimate`.

**Draw your engine first** (four minutes, paper, no AI). Read the message under I, then draw your
`portfolio.py` as it will be: one box per step from your `prices.csv` to the lowest-risk mix. Show
your partner.

## I — the app, from one message

1. Send this to your Lab 14 chat:

   > In my `portfolio.py`, keep everything it already prints exactly as it is. Add two functions:
   > a search that tries every long-only mix of the assets in 5-point steps, keeps the mixes whose
   > expected return is at least the objective and whose reserve-eligible weight is at least a
   > minimum, and returns the one with the lowest volatility, or nothing if no mix meets the
   > objective; and an estimate from a CSV of monthly prices (date first, oldest first, one column per ticker):
   > monthly returns from prices, mean × 12, standard deviation × √12, correlations, on all months
   > or only the last 36. Then build `app.py`, a Streamlit app that imports these functions and the
   > Meridian inputs from `portfolio.py` — reuse them, never copy the math. Sidebar: the objective
   > (start 6.5%), the reserve minimum (start 3%), an upload for my `prices.csv`, and a last-36-months
   > switch. Page: every expected return as a box I can edit; a tick box per asset for
   > reserve-eligible (bills and the 10-year note ticked for Meridian); the lowest-risk mix —
   > weights, return and volatility to two decimals, reserve-eligible weight — or "no mix meets the
   > objective", beside the answer for the inputs as loaded (Meridian's, or the CSV's on all
   > months), with the largest weight change in points. Under the title, one line: built with AI
   > help, a learning demonstration, not investment advice. Give me the command to run it.

2. Save both files. Run `python portfolio.py`. *Expect:* Tuesday's values, unchanged.
3. Run it with the command your AI gave you. *Expect:* your browser opens the app on Meridian's
   answer. An error on the page or in the terminal: paste the exact text to your AI.
4. Ask your AI: "Draw my `portfolio.py` as a Mermaid flowchart for my `.md` file."
   Paste it into your `.md` file. *Expect:* the path you drew on paper; GitHub shows it as a chart.
   A box you did not draw is your next question for your AI.

**At minute 30:** open the quiz attempt — Brightspace → Quizzes → Lab 15.

## V — prove it on the known answer

| Run | Bills / 10-year / IG / equity | Return | Volatility |
|---|---|---:|---:|
| As loaded | 0 / 20 / 25 / 55 | 6.51 | 9.44 |
| Equity return box 8.0 → 7.0 | 0 / 10 / 10 / 80 | 6.53 | 12.94 |

Largest weight change: **25 points**. One point off one estimate moves a quarter of the money. If
not, debug with your AI until they match.

**Prove it is your engine.** In `portfolio.py` set the IG–equity correlation to `0.50` in both
cells and save. Refresh the browser page. *Expect:* **0 / 40 / 0 / 60** at **6.52** and **9.73**.
Set it back. The app shows your engine's answer; it holds no second copy of the math.

## Your universe

Upload your `prices.csv`. Set your objective and your reserve rule (tick the assets that count, or
set the minimum to 0). Read the answer on all months; then flip the switch to the last 36 months.
*Expect:* your mix, or "no mix meets the objective" — a real answer; never lower the objective to get
one. Copy both answers, and the largest change when both have a mix, into your `.md` file.

**Explain the code** (six minutes, no AI). Open the search function in `portfolio.py` that tries
the mixes and keeps the lowest-risk one that meets the objective. Explain it to your partner line
by line; your partner asks one question you answer from the code. Swap. A line you cannot explain
is your next question for your AI.

**Partner attack.** Your partner opens your app, moves the estimate they distrust most, and reads
the answer aloud. Answer in two sentences in your `.md` file. Swap.

## Your call

**Adopt, pilot, or reject** the app's mix as your Project 2 starting allocation, with the
condition that would change it. *Example (Meridian):* "Pilot, not adopt: a one-point lower
equity estimate moves 25 points into equity. Adopt only once the CIO answers S9."

## Floor

The app reproduces Meridian's two runs and moves with your engine; your prices sourced and dated;
your answer on all months and on the last 36; the partner's attack answered; your call. You submit
individually.

## Estimation risk — Learn on your own

1. What is it? 2. How does it work — why does an optimizer amplify small errors in expected
returns? 3. Explain it to your partner using your own largest weight change.

## Reflect

Explain to your partner: 1. why the lowest-risk mix moved so far; 2. what you would need to see
before you adopted it.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.** Your `app.py` is one of them;
it grows into your Project 2 product.

## Merit anchors — five criteria, 5 points each, 25 in total

**4** = one minor weakness; **2** = an important link incomplete; **1** = minimal; **0** = missing
or fabricated.

| Criterion | 5 | 3 | 0–1 |
|---|---|---|---|
| Training reproduced | the app matches both Meridian runs and moves with the engine; 25-point change read | one run off | not attempted, or typed in |
| Data and sources | every ticker with source and download date; returns labelled estimate | dates or labels missing | unsourced or invented prices |
| Search under your mandate | your objective and constraint applied; infeasible stated honestly | constraint vague | objective lowered to force a mix |
| Stability and fresh eyes | 36-month answer; largest change read; partner's attack answered | 36-month answer, thin reading | no 36-month answer |
| The call | adopt, pilot or reject with a condition tied to the stress result | call without condition | "optimal" as the conclusion |

**Next week:** when was each number you used actually knowable? Data provenance and point-in-time.

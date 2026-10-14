# Session 15 — Portfolio Stability Decision

> **One thing today: turn your engine into your first app — a Streamlit page that finds the lowest-risk mix meeting the mandate's objective and reserve rule — and test whether its answer survives a one-point change.**

## Today's run of show

1. Opener — minutes 0–8
2. **R** your universe and your mandate — minutes 8–15
3. **I** the app on Meridian — minutes 15–35
4. **V** the known answer — minutes 35–42
5. Your universe — minutes 42–52
6. Explain the code — minutes 52–58
7. Partner attack — minutes 58–63
8. Your call and learn — minutes 63–70
9. Reflect and checkout — minutes 70–75

[Lab 15](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-09/lab-15-portfolio-stability.md)

---

## D — the question, the same for everyone

**Minutes 0–8**

Rerun `python portfolio.py` first: Tuesday's values.

> **Which mix carries the least risk while meeting the mandate — and does the answer survive a
> one-point change in one estimate?**

Paste it into your Lab 14 chat. Today the answer lives in an app your client could use: a web
page with controls, running on your own engine.

Something not working? Debug with your AI: the exact command and the exact error text.

---

## Explain to your partner first

**Minutes 0–8**

Five minutes, no screen: your Project 2 universe, your objective, and your one hard constraint.
Your partner writes them down. Swap.

---

## R — your universe and your mandate

**Minutes 8–15**

| Input | Meridian (training) | Yours |
|---|---|---|
| Assets | the four sleeves from Lab 14 | three to six funds from your mandate |
| Return, volatility, correlation | Lab 14's tables | estimated from five years of monthly prices |
| Objective | 6.5% expected return | your mandate's objective, as a number |
| Hard constraint | reserve-eligible weight at least 3% | your mandate's constraint, or `none` stated |

**Your prices.** Bring the `prices.csv` you built after Lab 14: five years of monthly **Adj Close**,
date first, oldest month first, one column per ticker; sources and download date in your `.md`
file. No file yet: build it now, as the [end of Lab 14](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-09/lab-14-portfolio-baselines.md#before-thursday--your-own-universe-in-funds) says.

A five-year average is history, not a forecast. Label your returns `estimate`.

---

## I — the app, from one message

**Minutes 15–35**

Send this to your Lab 14 chat:

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

---

## I — run it

**Minutes 15–35**

1. `python portfolio.py` — *Expect:* Tuesday's values, unchanged.
2. Run the app with the command your AI gave you — *Expect:* your browser opens it on Meridian's
   answer. An error: paste the exact text to your AI.

**At minute 30:** open the quiz attempt — Brightspace → Quizzes → Lab 15.

---

## V — prove it on the known answer

**Minutes 35–42**

| Run | Bills / 10-year / IG / equity | Return | Volatility |
|---|---|---:|---:|
| As loaded | 0 / 20 / 25 / 55 | 6.51 | 9.44 |
| Equity return box 8.0 → 7.0 | 0 / 10 / 10 / 80 | 6.53 | 12.94 |

Largest weight change: **25 points**. One point off one estimate moves a quarter of the money.

**Prove it is your engine.** IG–equity correlation `0.50` in `portfolio.py`, save, refresh the
page. *Expect:* **0 / 40 / 0 / 60** at **6.52** and **9.73**. Set it back.

---

## Your universe

**Minutes 42–52**

Upload your `prices.csv`. Your objective, your reserve rule (tick the assets that count, or set the
minimum to 0). All months; then flip to the last 36.

*Expect:* your mix, or "no mix meets the objective" — a real answer; never lower the objective
to get one. Copy both answers, and the largest change when both have a mix, into your `.md` file.

---

## Explain the code

**Minutes 52–58**

> **Explain the code** (six minutes, no AI). Open the search function in `portfolio.py` that tries
> the mixes and keeps the lowest-risk one that meets the objective. Explain it to your partner line
> by line; your partner asks one question you answer from the code. Swap. A line you cannot explain
> is your next question for your AI.

---

## Partner attack

**Minutes 58–63**

Your partner opens your app, moves the estimate they distrust most, and reads the answer aloud.
Answer in two sentences in your `.md` file. Swap.

---

## Your call · Estimation risk — Learn on your own

**Minutes 63–70**

**Adopt, pilot, or reject** the app's mix as your Project 2 starting allocation, with the
condition that would change it.

*Example (Meridian):* "Pilot, not adopt: a one-point lower equity estimate moves 25 points into
equity. Adopt only once the CIO answers S9."

**Learn on your own:**

1. What is it?
2. How does it work — why does an optimizer amplify small errors in expected returns?
3. Explain it to your partner using your own largest weight change.

---

## Reflect

**Minutes 70–75**

**Explain to your partner:**

1. why the lowest-risk mix moved so far;
2. what you would need to see before you adopted it.

---

## Checkout — on GitHub

**Minutes 70–75**

**Brightspace → Quizzes → Lab 15.**

**GitHub links of your files: md, py and/or other files as needed.** Your `app.py` is one of them.

**Before Tuesday — do these**

1. Read the [ALFRED reading](../week-10/student-prework.md).
2. Keep your Lab 15 chat, your `app.py` and your partner.

**Next week:** when was each number you used actually knowable? Data provenance and point-in-time.

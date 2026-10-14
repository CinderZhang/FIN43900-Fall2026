# Session 14 — Portfolio Baselines

> **One thing today: build the risk engine from the instruction, and price three simple portfolios on the known answer.**

## Today's run of show

1. Opener — minutes 0–8
2. Rerun and **D** — minutes 8–15
3. **R** inputs — minutes 15–20
4. **I** build the engine — minutes 20–40
5. **V** known answer — minutes 40–50
6. Explain the code — minutes 50–56
7. Swap and break — minutes 56–62
8. Learn and reflect — minutes 62–70
9. Checkout — minutes 70–75

[Lab 14](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-09/lab-14-portfolio-baselines.md)

---

## Explain to your partner first

**Minutes 0–8**

Five minutes, no screen: why can two risky assets together be less risky than either alone?
Use the 10.46 you worked by hand. Then swap.

Something not working? Debug with your AI: the exact command and the exact error text.

---

## D — the question, the same for everyone

**Minutes 8–15**

Rerun `python mandate.py` first: your Lab 13 verdicts.

> **What does each simple portfolio earn and risk — and does any of them meet the Meridian mandate?**

Paste it into your Lab 13 chat. Today the portfolio is Meridian's. Thursday it is yours.

---

## R — the inputs (course-authored training values, not market estimates)

**Minutes 15–20**

### Return and volatility

| Sleeve | Expected return | Volatility |
|---|---:|---:|
| Treasury bills | 3.5% | 0.5% |
| Treasury 10-year note | 4.3% | 7.0% |
| Investment-grade bond fund | 5.0% | 6.0% |
| Global equity index fund | 8.0% | 16.0% |

### Correlation

| Correlation | Bills | 10-year | IG bonds | Equity |
|---|---:|---:|---:|---:|
| Bills | 1.00 | 0.10 | 0.05 | 0.00 |
| 10-year | 0.10 | 1.00 | 0.80 | −0.10 |
| IG bonds | 0.05 | 0.80 | 1.00 | 0.25 |
| Equity | 0.00 | −0.10 | 0.25 | 1.00 |

Baselines: **Benchmark** 40% IG bonds, 60% equity · **Equal weight** 25% each · **Inverse
volatility** each weight proportional to 1 ÷ volatility. Objective **6.5%**. Reserve-eligible:
bills and the 10-year note.

---

## I — build the engine from the instruction

**Minutes 20–40**

Send this to your AI partner, then paste both tables under it. The code it writes is yours.

> Write one Python file, `portfolio.py`, standard library only. At the top, editable inputs:
> the four sleeves with expected return and volatility, the correlation table I paste below,
> and an objective return of 6.5%. Build the covariance matrix as correlation × volatility ×
> volatility. Refuse to run, with a clear message, if any correlation is outside −1 to 1 or the
> table is not symmetric. Define three portfolios: benchmark (40% investment-grade bond fund,
> 60% global equity index fund); equal weight; inverse volatility (each weight = 1 ÷ its
> volatility, scaled to sum to 100%). For each print the weights in percent to one decimal,
> expected return and volatility in percent to two decimals, the reserve-eligible weight
> (bills plus the 10-year note), and whether expected return meets the objective. Compute
> everything from the inputs; never type an answer in. Put each calculation in its own
> function, so another file can reuse them. Give me the command to run it.

`python portfolio.py`. *Expect:* three portfolios with their numbers. Ask your AI to quiz you on
the line you understand least.

**At minute 25:** open the quiz attempt — Brightspace → Quizzes → Lab 14.

---

## V — prove it on the known answer

**Minutes 40–50**

| Portfolio | Weights: bills / 10-year / IG / equity | Return | Volatility | Reserve-eligible | Meets 6.5%? |
|---|---|---:|---:|---:|---|
| Benchmark | 0.0 / 0.0 / 40.0 / 60.0 | 6.80 | 10.46 | 0.0 | yes |
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 5.20 | 5.21 | 50.0 | no |
| Inverse volatility | 84.3 / 6.0 / 7.0 / 2.6 | 3.77 | 1.05 | 90.3 | no |

Classic error: volatility squared without the correlation term gives the benchmark 9.90.

**Prove it computes.** IG–equity correlation `0.50` in both cells, rerun. *Expect:* benchmark
volatility **11.00**. Set it back.

---

## Explain the code

**Minutes 50–56**

> **Explain the code** (six minutes, no AI). Open the block of `portfolio.py` that turns weights,
> volatilities and correlations into a portfolio volatility. Explain it to your partner line by
> line; your partner asks one question you answer from the code. Swap. A line you cannot explain
> is your next question for your AI.

---

## Swap and break

**Minutes 56–62**

**Swap and break.** Run your partner's `portfolio.py`; same values. In their file set the
IG–equity correlation to `1.3`. *Expect:* it refuses. Undo.

**Read it.** Add the benchmark to `mandate.py` as candidate E (40 IG fund, 60 equity fund). Run it.
*Expect:* it fails the reserve rule at 0.0%. The client's own benchmark breaks the client's mandate.

---

## Diversification — Learn on your own · Reflect

**Minutes 62–70**

**Learn on your own:**

1. What is it?
2. How does it work — why does a correlation below +1 lower risk?
3. Explain it: work the benchmark's volatility by hand from the [handout's digits](student-handout.md#the-digits-once).

**Explain to your partner:**

1. why inverse volatility piles into bills;
2. which baseline you would show the CIO first, and why.

---

## Checkout — on GitHub

**Minutes 70–75**

**Brightspace → Quizzes → Lab 14.**

**GitHub links of your files: md, py and/or other files as needed.**

**Before Thursday — do these**

1. Have `portfolio.py` matching the Lab 14 known answer.
2. Keep your Lab 14 chat and your partner.
3. Have your own Project 2 mandate, in Lab 13's shape, three to six fund tickers for it, and their `prices.csv` —
   cash, bonds, fixed income, equity ([Lab 14, last section](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-09/lab-14-portfolio-baselines.md#before-thursday--your-own-universe-in-funds)). No money market funds: most hold their price at $1.00, so prices cannot show what they earn.
4. Install Streamlit, run its demo, and read its Basic concepts ([prework](student-prework.md)).

**Thursday preview:** turn your engine into your first app, in Streamlit: the lowest-risk mix that
meets the mandate, and whether it survives a one-point change.

<!-- AUTHORED HOME. Rebuilt 2026-10-13 under the 2026-09 rulings (instruction, not materials; one
     thing per lab; harness the topic; two-person teams; GitHub is the main delivery). -->

# Lab 14 — Portfolio Baselines

**One thing today: build the risk engine from the instruction, and price three simple portfolios on the known answer.**

**Category:** Tuesday completion checkout, **25 or 0**.

**Pace — 75 minutes, on the slides:** opener 0–8 · rerun and D 8–15 · R 15–20 · I 20–40 · V 40–50 · explain the code 50–56 · swap and break 56–62 · learn and reflect 62–70 · checkout 70–75.

**You arrive with:** your Course/Work Folder · your Lab 13 `mandate.py` and chat · your partner from Lab 13 · the [diversification reading](student-prework.md).

Rerun `python mandate.py` first: your Lab 13 verdicts. **Something not working?** Debug with your AI: paste the exact command and the exact error text.

## D — the question, the same for everyone

> **What does each simple portfolio earn and risk — and does any of them meet the Meridian mandate?**

Paste it into your Lab 13 chat. Today the portfolio is Meridian's. Thursday it is yours.

**Explain to your partner first** (five minutes, no screen): why can two risky assets together be
less risky than either alone? Use the 10.46 you worked by hand. Then swap.

## R — the inputs (course-authored training values, not market estimates)

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

The three baselines: **Benchmark** 40% IG bonds, 60% equity (Lab 13's S4) · **Equal weight**
25% each · **Inverse volatility** each weight proportional to 1 ÷ volatility. Objective: CPI + 4%,
with CPI taken as 2.5% (a labelled estimate), so **6.5%**. Reserve-eligible: bills and the 10-year
note (Lab 13).

## I — build the engine from the instruction

1. Send this to your AI partner, then paste both tables above under it. The code it writes is yours: read it,
   run it, debug it.

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

2. Save it as `portfolio.py`. Run `python portfolio.py`. *Expect:* three portfolios with their numbers; if not, debug with your AI.
3. Ask your AI to quiz you on the line you understand least; answer before it explains.

## V — prove it on the known answer

| Portfolio | Weights: bills / 10-year / IG / equity | Return | Volatility | Reserve-eligible | Meets 6.5%? |
|---|---|---:|---:|---:|---|
| Benchmark | 0.0 / 0.0 / 40.0 / 60.0 | 6.80 | 10.46 | 0.0 | yes |
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 5.20 | 5.21 | 50.0 | no |
| Inverse volatility | 84.3 / 6.0 / 7.0 / 2.6 | 3.77 | 1.05 | 90.3 | no |

Every value matches, or debug with your AI until they do. The classic error: volatility squared
without the correlation term, which gives the benchmark 9.90 instead of 10.46.

**Prove it computes.** Set the IG–equity correlation to `0.50` in both cells. Rerun. *Expect:*
the benchmark's volatility rises to **11.00**. Set it back.

**Explain the code** (six minutes, no AI). Open the block of `portfolio.py` that turns weights, volatilities and correlations into a portfolio
volatility. Explain it to your partner line by
line; your partner asks one question you answer from the code. Swap. A line you cannot explain is
your next question for your AI.

**Swap and break.** Run your partner's `portfolio.py`; same values. In their file set the
IG–equity correlation to `1.3`. *Expect:* it refuses. Undo. An engine that runs has not been checked.

**Read it.** Add the benchmark to `mandate.py` as candidate E (40 IG fund, 60 equity fund). Run it.
*Expect:* it fails the reserve rule at 0.0%. The client's own benchmark breaks the client's mandate.

## Floor

The engine matches the known answer and refuses a bad correlation; the benchmark run through your
mandate checker. You submit individually.

## Diversification — Learn on your own

1. What is it? 2. How does it work — why does a correlation below +1 lower risk? 3. Explain it: work the
benchmark's volatility by hand from the [handout's digits](student-handout.md#the-digits-once).

## Reflect

Explain to your partner: 1. why inverse volatility piles into bills; 2. which baseline you would show
the CIO first, and why.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

## Before Thursday — your own universe, in funds

Thursday's app runs Meridian first, then your own Project 2 universe. Find three to six funds for
it, one for each role your mandate needs. In your `.md` file write each ticker, the fund's name and
its role.

| Role | Look for | Example ticker |
|---|---|---|
| Cash and reserve | a Treasury-bill fund | BIL |
| Government bonds | a Treasury bond fund | IEF |
| Fixed income | an investment-grade bond fund | LQD |
| Equity | a broad stock index fund | VT |

The examples are for practice, not recommendations. Skip money market funds: most hold their price at
$1.00, so a price history cannot show what they earn; a Treasury-bill fund stands in for cash. Check
each on [Yahoo Finance](https://finance.yahoo.com) → **Historical Data** → **Monthly**: five years
of prices, and the **Adj Close** column, which counts the fund's payouts.

Then ask your AI to put five years of monthly **Adj Close** prices for your funds into one
`prices.csv`: the date first, oldest month first, then one column per ticker. In your `.md` file
record each ticker, the source and the download date.

**Thursday preview:** turn your engine into your first app, in Streamlit: the lowest-risk mix that
meets the mandate, and whether it survives a one-point change.

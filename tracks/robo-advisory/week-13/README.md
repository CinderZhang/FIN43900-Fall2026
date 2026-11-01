# Robo-Advisor Guide, Week 13 — Client to Portfolio

Thursday of Week 13, self-paced: a guide and readings — no lab, no lecture, no checkout, no
grade item. What you build can seed your capstone.

**What you build:** your own robo-advisor app, `robo_app.py` — a client's answers in, an
allocation and its loss check out, both in code you can test.

Design after matvix90/ai-robo-advisor (MIT). Data: Ken French Data Library; FRED, Federal Reserve Bank of St. Louis. Education, not investment advice.

## Readings

- [matvix90/ai-robo-advisor](https://github.com/matvix90/ai-robo-advisor), "How It Works" — the
  design: questionnaire → strategy → portfolio → checks. Who decides the allocation there? Read
  it; do not install it (it needs paid keys).
- [Ken French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
  — stocks and cash: the US market and the 1-month T-bill, monthly.
- [FRED GS10](https://fred.stlouisfed.org/series/GS10) — bonds: the 10-year Treasury yield, monthly.

In matvix90 the AI picks the allocation. In yours, the allocation and the loss check are code you
can test; the AI explains (Week 14).

## Your request

Write your allocation rule where the request says *[my rule]*, then paste it to your AI
(Antigravity or Codex).

> Build a Streamlit app, `robo_app.py`: my robo-advisor on the design of matvix90/ai-robo-advisor (questionnaire, allocation, checks). Do not install that repository.
>
> 1. Questionnaire: age; time horizon (years); when the money may be needed; emergency fund (yes/no); maximum acceptable loss in any 12 months (%); reaction to a 20% market fall; initial investment ($).
> 2. The allocation, in code, from the answers by my rule: [my rule]. Stocks, bonds and cash sum to 100%. Show the allocation and my rule in one line, and let me override the allocation by hand.
> 3. Data pulled live on every run, no key. Stocks and cash: Ken French Data Library, https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip — monthly rows only (six-digit YYYYMM; the annual rows after the second header are not months); from the Mkt-RF and RF columns, stock return = (Mkt-RF + RF) / 100 and cash return = RF / 100. Bonds: FRED GS10, https://fred.stlouisfed.org/graph/fredgraph.csv?id=GS10 — yield y = GS10 / 100. Each month's bond return = P − 1 + y0/12, where y0 is last month's yield, y1 this month's, n = 2 × (10 − 1/12) and P = (y0/y1) × (1 − (1 + y1/2)^−n) + (1 + y1/2)^−n. December 1989's yield starts January 1990. Rebalance to the allocation every month, January 1990 to December 2025.
> 4. Show how many months were used, and for the allocation: CAGR (wealth^(12/months) − 1); volatility (sample standard deviation of monthly returns × √12); max drawdown (from a wealth path starting at 1); worst 12 months (the lowest rolling 12-month compounded return) and the month they ended, in percent and in dollars on the initial investment. Chart the growth of $1 in stocks, bonds, cash and the portfolio.
> 5. The alignment check, as a test in code: if the worst 12 months lost more than the client's maximum acceptable loss, show a red flag. Show "largest stock share within this client's max loss": the largest stock share on a 10% grid, holding my allocation's cash share fixed, bonds taking the rest, whose worst 12 months stays within the maximum acceptable loss — or "no stock/bond mix passes".
> 6. Footer: "Design after matvix90/ai-robo-advisor (MIT). Data: Ken French Data Library; FRED, Federal Reserve Bank of St. Louis. Education, not investment advice."

The bond return is an approximation from real yields, not a published bond index.

Something not working? Debug with your AI: paste the exact command and the exact error text.

## Known answer

Override the allocation to 60/40/0 (stocks/bonds/cash) on $100,000. *Expect:* 432 months, January
1990 to December 2025.

| Stocks/bonds/cash | CAGR | Volatility | Max drawdown | Worst 12 months |
|---|---:|---:|---:|---:|
| 60/40/0 | 8.88% | 9.38% | −28.40% | −24.41% (−$24,415), the 12 months to February 2009 |

Match to within 0.1 percentage point — the French file is revised slightly each year — or debug
with your AI until you do.

## Probes

1. **A client whose max loss is 20%.** *Expect:* largest stock share within this client's max
   loss, 50%.
2. **A client whose max loss is 15%.** *Expect:* no stock/bond mix passes — bonds alone lost
   16.87% in the 12 months to October 2022.
3. **Add cash.** The same 15% client with 20% cash. *Expect:* 30% stocks passes. With 10% cash,
   none.

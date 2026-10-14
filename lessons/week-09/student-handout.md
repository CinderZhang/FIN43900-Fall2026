# Week 9 Student Handout — Portfolio Construction and Stability

Last week: which portfolios does the client's mandate permit? This week: what does each portfolio
earn and risk, and does the "best" one survive a small change in what you assumed?

## The commands

In the terminal, with your own Python command:

| Command | Expect |
|---|---|
| `python portfolio.py` | Tuesday: three Meridian baselines with return, volatility and reserve. Thursday: unchanged; your app imports its functions |
| the run command your AI gives you for `app.py` | Thursday: your first app in the browser — the lowest-risk mix beside the as-loaded answer, then your own universe from `prices.csv`. Reference: [Streamlit's Basic concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts) |
| `python mandate.py` | your Lab 13 verdicts, plus the benchmark failing the reserve rule |

Something breaks? Debug with your AI: the exact command and the exact error text.

## Diversification in plain language

Portfolio risk depends on how assets move **together**, not only on each asset's standalone
volatility. The portfolio-variance calculation therefore includes covariance terms. When two
risky assets are less than perfectly positively correlated, one asset's movement can partly
offset the other's, so the combined volatility can be lower than a standalone-risk comparison
suggests. If correlation is `+1`, that offsetting benefit disappears for the pair.

Adding distinct exposures can reduce diversifiable, issuer-specific risk, but the marginal
benefit normally shrinks as more assets are added. Diversification cannot remove common or
systematic risks shared across the portfolio. A low historical correlation is evidence to test,
not a promise: it may rise in a new window or stress regime.

## The digits, once

The benchmark: 40% investment-grade bonds (return 5.0%, volatility 6.0%), 60% global equity
(8.0%, 16.0%), correlation 0.25.

| Step | Rule | Benchmark |
|---|---|---|
| Expected return | Σ weight × return | 0.40 × 5.0 + 0.60 × 8.0 = 6.80% |
| Covariance, bonds–equity | correlation × vol × vol | 0.25 × 0.06 × 0.16 = 0.0024 |
| Variance | w₁²σ₁² + w₂²σ₂² + 2w₁w₂ × covariance | 0.000576 + 0.009216 + 0.001152 = 0.010944 |
| Volatility | √variance | √0.010944 = 10.46% |
| Without the correlation term | the classic error | √(0.000576 + 0.009216) = 9.90% |
| Inverse volatility, bills | (1 ÷ 0.005) ÷ Σ(1 ÷ vol) | 200 ÷ 237.2 = 84.3% |
| Annualizing monthly data | mean × 12; standard deviation × √12 (simple scaling, not compounded growth; it treats months as independent) | 0.6% a month → 7.2% a year; 4.0% a month → 13.9% a year |

## The rules

- Training values and your estimates are labelled differently. A five-year average is history,
  not a forecast.
- Never lower the objective to make a mix appear. "No mix meets the objective" is an answer.
- A search result is a starting point. If one point on one estimate moves a quarter of the money,
  the call is pilot or reject, not adopt.
- Run every new portfolio through the mandate checker before you call it better.

## DRIVER, one line each

Define — the same question for everyone. Represent — inputs, labelled. Implement — the engine from
one request. Validate — the known answer and the partner's break. Evolve and Reflect — the search,
the stress, and why the answer moved.

# Entry Diagnostic and Recovery Router

This ungraded diagnostic gives you a private starting point. It is not an admission test, creates
no grade item, and is not used to label you. Work for **15 minutes with AI closed**. Then use
the key and choose only the recovery route you need. Do not submit your answers.

## Part 1 — Four fresh checks

### A. Finance direction

A company has enterprise value of $600 million, debt of $180 million, and excess cash of
$40 million. Before calculating, predict whether equity value is above or below enterprise value.
Then calculate equity value. State the bridge in one line.

### B. Source, assumption, or output

Label each item `SOURCE FACT`, `ASSUMPTION`, or `MODEL OUTPUT`:

1. Revenue reported in the company's filed 10-K.
2. A 4% perpetual growth rate chosen by the analyst.
3. Implied value per share produced by the model.

For the source fact, name the filing and as-of date a reviewer would need.

### C. Code and units

Read this code without running it:

```python
debt_millions = 180
cash_dollars = 40_000_000
equity_value = 600 - debt_millions + cash_dollars
```

Predict whether the result will be plausible. Identify the unit defect and write one corrected
line. You do not need to know advanced Python.

### D. Validation and action

An AI says: “The company is undervalued because revenue grew 12%.” Name one missing comparison,
one changed-input test, and one fact that could reverse the action.

## Part 2 — Self-check

Open this section only after the 15-minute attempt.

- **A:** Equity value is below enterprise value: `600 - 180 + 40 = $460 million`.
- **B:** 10-K revenue is a source fact; 4% growth is an assumption; value per share is a model
  output. A reproducible citation needs the exact filing and its filing/period date.
- **C:** Dollars and millions are mixed. One correction is `cash_millions = 40` followed by
  `equity_value = 600 - debt_millions + cash_millions`.
- **D:** Valid answers identify a benchmark or valuation comparison, change a material driver
  rather than formatting, and name evidence capable of reversing the recommendation.

## Part 3 — Route, do not diagnose yourself

Choose the smallest route that addresses your first miss:

| First blocker | Start here | Bring to Week 1 |
|---|---|---|
| EV-to-equity bridge or finance direction | Week 2 handout, “valuation object and bridge” | one handwritten bridge and units |
| Source/assumption/output labels | AI Data Safety Card plus Week 1 evidence ladder | one filing citation with as-of date |
| Python syntax or units | **Course Environment Quickstart**, then the one exact page in its QuantEcon recovery map matching syntax, NumPy, pandas, debugging, or troubleshooting | the exact command, output, first error, and page used |
| Validation or reversal logic | Week 1 DRIVER handout, Validate and Reflect | one prediction and one reversal condition |
| Device, account, connectivity, or access | Support Map | a private support request; never post credentials |

A miss is useful evidence. Week 1 supplies the tested setup path and a live readiness check. Do
not buy an unlisted tool, guess at package versions, or ask AI to manufacture a passing result.

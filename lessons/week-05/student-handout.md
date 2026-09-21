# Week 5 Student Handout — Build the Base Case

Last week: what do investors pay for similar companies? This week: what are five years of your
company's statements worth, built from assumptions you can defend?

## The two commands

In the VS Code terminal (**Terminal → New Terminal**), with your own Python command in place of
`python` (`python`, `py`, or `python3` — the one that answered):

| Command | Expect |
|---|---|
| `python dcf.py` | your Week 3 values still print |
| `python proforma.py` | Tuesday: the ABG statements, the check block, $291.75. Thursday: your company's statements, the check block, one value per share |

Something breaks? Debug with your AI: the exact command and the exact error text.

## The digits, once (ABG, the training case)

| Step | Rule | ABG, FY2026E |
|---|---|---|
| Revenue | prior × (1 + growth) | 17,999.0 × 1.018 = 18,323.0 |
| Gross profit | revenue × margin | 18,323.0 × 17.05% = 3,124.1 |
| SG&A | gross profit × cost ratio | 3,124.1 × 66.5% = 2,077.5 |
| Operating income | gross profit − SG&A − depreciation − impairment | 3,124.1 − 2,077.5 − 82.4 − 120.0 = 844.2 |
| Net income | (operating income − interest) × (1 − tax) | (844.2 − 289.0) × 0.745 = 413.6 |
| Cash flow to equity | net income + non-cash − capex − working capital + floor plan − repayment | 413.6 + 202.4 − 250.0 − 41.5 + 36.9 − 150.0 = 211.4 |
| Cash | opening + cash flow to equity − buyback | 40.4 + 211.4 − 150.0 = 101.8 |
| Check | assets − liabilities − equity | 0.0 |
| Value per share | (PV of five years + PV of terminal) ÷ shares | (1,059.9 + 4,177.5) ÷ 17.951 = 291.75 |

## The rules

- Every assumption carries a label — history, guidance, judgment — and every judgment a reason.
- Cash is computed last. A balance sheet that does not balance is a bug, not a forecast.
- The model refuses to value an unbalanced sheet. Yours must too.
- Reported growth can be bought; carry the growth of the stores already owned.
- Name the line that makes your company different, and treat it the same way everywhere.

## DRIVER, one line each

Define — the same question for everyone; your company is the only variable. Represent — the
labelled assumption set. Implement — the engine from one request. Validate — the known answer,
then the checks that stop the model. Evolve and Reflect — your company; your partner's fresh eyes.

## The video

[Part 1 — Build the base case](https://youtu.be/O4PeC2PqwRY), 27 min. Slides with the spoken text:
[the tutorial page](pro-forma-abg-tutorial.md). Learning demonstration — not investment advice.

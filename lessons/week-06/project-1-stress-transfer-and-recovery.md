# Week 6 Calculation Recovery and Project 1 Stress Transfer

Use this page when code is unavailable and to convert the synthetic stress logic into one bounded
Project 1 downside test. The no-code and code routes require the same prediction, arithmetic,
limitations, and decision consequence.

## When this route applies

All learners complete Part B within the published Week 6 Project 1 planning band. Complete Part A
only if code fails or staff directs a reconciliation. Switch during the same Lab 11/12 session,
show paper/spreadsheet evidence at checkout for visual initials, and keep it; there is no separate
Brightspace upload, deadline, grade item, or extra point. Calculate and freeze your own numbers
first. AI may then check them, but is optional: record any disagreement, source verification, and
which number you kept and why.
The published Lab 11/12 checkout deadlines and ordinary absence/drop rule still apply; this route
is not a makeup.

## A. Synthetic calculation fallback

For each row in `stress_scenarios.csv`, calculate:

- EBIT = EBITDA − depreciation and amortization;
- Debt/EBITDA = total debt ÷ EBITDA;
- EBIT coverage = EBIT ÷ interest expense; and
- cash = the supplied end-state liquidity indicator.

Before calculating the Combined row, predict which threshold fails first. Test Debt/EBITDA ≤
5.0x, EBIT/interest ≥ 2.5x, and period-end cash ≥ USD 50 million. Record each state as `pass`,
`breach`, or `invalid/unknown` and
preserve the causal path. A covenant breach is not automatically payment default or economic loss.
A staff-initialed paper table is acceptable if Python fails; label every unexecuted extension.

These are synthetic-case teaching thresholds, not universal target-company underwriting hurdles.
If you reuse one only as an analyst diagnostic, keep the Week 5 gross-debt/reported-EBITDA/
constructed-EBIT/supplied-gross-interest basis for comparability and show any company-specific
basis separately. Preserve the issuer's reporting currency and unit; do not silently apply the
synthetic USD 50 million cash floor to a non-USD or differently scaled target.

## B. Bounded Project 1 transfer — 40–50 minutes within the Week 6 project band

Append one target-company downside case to `evidence/project1-credit-check.md`:

1. freeze one causal shock before calculation—revenue/volume, margin, interest cost, refinancing,
   or working-capital pressure;
2. state the base values, shock size, units, and why the shock is decision-relevant;
3. propagate the shock through EBITDA/EBIT, coverage or leverage, and one liquidity/cash-flow
   measure without changing unrelated assumptions;
4. record the first threshold, condition, or financing concern reached;
5. distinguish model flag, covenant concern, liquidity pressure, payment default, and loss; and
6. state whether the valuation range or initiate/watch/do-not-initiate action is unchanged,
   narrowed, conditioned, or reversed.

Use only evidence available by the Project 1 valuation date. If the company does not disclose a
covenant threshold, do not invent one: label the test an analyst stress threshold and request the
missing agreement/evidence. Retain one before-run direction prediction and the actual result for
the Project 1 changed-input/validation record.

## Completion boundary

This page creates no extra grade item. Lab 11 and Lab 12 use the synthetic case; the target-company
stress record is Project 1 evidence. A plausible story without a frozen input and traceable
calculation is incomplete.

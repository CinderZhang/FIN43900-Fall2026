# Week 5 Calculation Recovery and Project 1 Credit Transfer

> **This module is being rebuilt as Pro-Forma Financial Modeling I** (see the course
> schedule). The page below is the previous curriculum and will be replaced in full
> before this week begins — do not prepare from it.

Use this page if Python is unavailable **or** after the synthetic screen to transfer the credit
logic to your Project 1 company. The no-code path and code path are judged on the same finance
evidence. Label any result you could not execute; do not invent a value.

## When this route applies

All learners complete Part B within the published Week 5 Project 1 planning band. Complete Part A
only if code fails or staff directs a reconciliation. Switch during the same Lab 09 session, show
the paper/spreadsheet evidence at checkout for visual initials, and keep it; there is no separate
Brightspace upload, deadline, grade item, or extra point. Calculate and freeze your own numbers
first. AI may then check them, but is optional: record any disagreement, source verification, and
which number you kept and why.
The published Lab 09 checkout deadline and ordinary absence/drop rule still apply; this route is
not a makeup.

## A. Synthetic calculation fallback

For one assigned borrower, copy the fields from `credit_cases.csv` and calculate:

- Debt/EBITDA = total debt ÷ EBITDA;
- EBIT coverage = (EBITDA − depreciation and amortization) ÷ interest expense;
- current ratio = current assets ÷ current liabilities; and
- post-capex cash-flow capacity = (CFO − capital expenditures) ÷ total debt.

For this synthetic case, use gross debt as supplied; reported, unadjusted EBITDA for the supplied
period; EBIT = EBITDA − depreciation and amortization; and gross interest expense as supplied.
For the target company, restate and defend any different lease, adjustment, period, or interest
convention rather than silently changing it.

Show numerator, denominator, units, period, result, and any invalid denominator. Apply the class
screen thresholds one factor at a time. Record `approve`, `review`, or `reject`, each reason code,
and the loss from a false approval versus a false rejection. The published Borrower A known answer
is the reconciliation anchor. A staff-initialed paper table is acceptable when the local file or
Python route fails; photograph or retain it only for your own project evidence.

## B. Bounded Project 1 transfer — 35–45 minutes within the Week 5 project band

Create `evidence/project1-credit-check.md` (or the equivalent clearly named notebook/table) and
record exactly these fields for your target company:

| Field | Required evidence |
|---|---|
| decision and as-of date | initiate, watch/defer, or do not initiate; valuation date |
| source map | filing/form, filed date, period end, page/note or table, stable link |
| debt | included instruments and exclusions; current/noncurrent treatment |
| EBITDA or operating proxy | explicit construction; adjustments separately labeled |
| interest | cash or accounting interest convention and period |
| cash-flow capacity | CFO, capex, and any normalization |
| two calculated ratios | numerator, denominator, units, period, result |
| one limitation | missing definition, sector distortion, maturity/refinancing, or off-balance-sheet item |
| recommendation effect | unchanged, narrowed, conditional, or reversed, with reason |

Use the most recent authoritative filing available by the valuation date. A data-provider ratio
may be a cross-check, but it cannot replace the reconstructed definition. Do not turn this into a
full credit model. If a required field is not disclosed, mark it `unknown`, identify the smallest
evidence request, and state how that uncertainty limits the equity recommendation.

## Completion boundary

This page creates no extra submission or points. Lab 09 remains the individual checkout; the
target-company record belongs in the Project 1 repository and later manifest. The synthetic
borrower label is never evidence about the target company.

# Week 5 Synthetic Outcome-Label Convention

> **This module is being rebuilt as Pro-Forma Financial Modeling I** (see the course
> schedule). The page below is the previous curriculum and will be replaced in full
> before this week begins — do not prepare from it.

The `adverse_outcome_next_12m` field is a **synthetic, fully observed teaching label** measured
from the stated underwriting decision date `t0` through `t0 + 12 months`:

- `1` — within the 12-month window, the borrower entered payment default, court-supervised
  insolvency, or a restructuring that caused principal impairment to the modeled lender;
- `0` — none of those events occurred in the complete 12-month observation window.

The six teaching cases have no censoring, unresolved status, recoveries, cures, or competing
events. In the confusion table, a predicted `review/reject` is the **positive** risk flag and
`approve` is negative. Therefore, a false negative is an approved borrower with label `1`
(unsafe case passed); a false positive is a reviewed/rejected borrower with label `0`
(opportunity cost). `Deeper review` and `reject` may be reported separately for decision design,
but both map to positive for this binary validation exercise.

This label tests error-cost reasoning; it is not underwriting truth, a probability of default,
or evidence that historical absence of an event makes a borrower safe.

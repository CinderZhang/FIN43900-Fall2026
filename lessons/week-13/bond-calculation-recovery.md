# Week 13 Bond Calculation and Screening Recovery

Use this no-code route when Python is unavailable. It is the
learner-visible version of the calculator/spreadsheet fallback and uses only fictional course data.

Switch during the same formative session, show the paper/accessible-spreadsheet evidence at the
exit check for visual initials, and keep it. This creates no separate submission, deadline, grade item, or
extra point. Calculate and freeze your own numbers first. AI may then check them, but is optional:
record any disagreement, source verification, and which number you kept and why.

## Price and risk anchor

For K1, use the handout's supplied present-value column. Sum price; calculate Macaulay duration as
`sum(t × PV(CF_t)) ÷ price`; then calculate modified duration as `Macaulay ÷ 1.04`. Reconcile the
published values before interpreting the supplied convexity and exact-versus-approximate +100 bp
results. For the off-cycle microcase, show coupon, accrued fraction, accrued interest, clean quote,
and dirty invoice price. These are two separate anchors: K1 is the annual-pay/annual-compounding
coupon-date case, while the off-cycle microcase is a separate semiannual instrument whose 90/180
accrual fraction is supplied. Do not combine their conventions, substitute another day-count rule, or
apply coupon-date formulas silently to off-cycle settlement. `spread_bps` is the supplied
synthetic option-free-style relative spread defined in that sheet, not an OAS or default measure.

## Screen table

Copy from `synthetic_bonds.csv`: bond ID, coupon, maturity, yield, price, modified duration,
spread, stale days, and 20-day trade count. Before screening, write thresholds, missingness rule,
mandate reason, and override rule. For each bond record:

- pass/fail/unknown reason codes;
- clean/dirty and price-risk reconciliation status;
- measurement/liquidity limitation;
- evidence still required; and
- reject, quarantine, or deeper-review action.

A high spread does not prove cheapness, default probability, or credit quality. A staff-initialed
paper table or accessible spreadsheet is acceptable formative evidence. Mark code-only extensions
unexecuted; no grade item or final buy recommendation is created.

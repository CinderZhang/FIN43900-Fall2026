# Week 11 Signal Calculation Recovery

Use this calculator/spreadsheet route if the starter cannot run. It preserves the frozen-rule and
holdout boundaries; staff release the holdout rows only after the design is recorded.

Switch during the same Lab 18/21 session. Show the frozen design to staff; staff then releases the
sealed holdout rows once. Calculate them once, show the paper/accessible-spreadsheet result for
visual initials, and keep it. This is an equivalent route to the existing lab, not a separate
submission, deadline, grade item, or extra point. Calculate and freeze your own numbers first. AI
may then check them, but is optional: record any disagreement, source verification, and which
number you kept and why.
The published Lab 18/21 checkout deadlines and ordinary absence/drop rule still apply; this route
is not a makeup.

For each available row:

1. set `position_t = sign(signal_t)` under the frozen rule;
2. calculate `gross_return_t = position_t × next_return_t`;
3. with initial position zero, calculate `turnover_t = |position_t − position_(t−1)|`;
4. calculate `cost_t = turnover_t × one_way_cost_bps / 10,000`;
5. calculate `net_return_t = gross_return_t − cost_t`; and
6. average gross and net returns separately by development/holdout regime.

`signal_t` is the information available for the labeled `next_return_t`; do not use that return to
choose the position. The teaching convention is one position, initial position zero, turnover
`|position_t − position_(t−1)|`, and one-way cost in basis points per unit turnover. Do not replace
it with a multi-asset half-turnover convention. The terminal position is carried: do not add a
sample-end liquidation. Total turnover is the sum from `t = 1` through `T`, using `position_0 = 0`.

Reconcile periods 1 and 2 by hand before filling the remaining rows. Keep the late regime covered
until staff release it, run it once, and do not retune the sign, lag, threshold, universe, cost, or
split afterward. Record every alternative in the selection ledger. A staff-initialed paper table
or accessible spreadsheet satisfies the mechanical evidence; label any resampling, chart, or
extension that was not executed. A failed holdout remains valid evidence and must remain visible.

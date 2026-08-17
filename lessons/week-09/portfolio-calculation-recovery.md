# Week 9 Portfolio Calculation Recovery

Use this route if Python, NumPy, or a solver is unavailable. It produces the same required finance
evidence as the code route; it does not waive baselines, constraints, or validation.

Switch during the same Lab 14/17 session, show the paper/accessible-spreadsheet evidence at
checkout for visual initials, and keep it. This is an equivalent route to the existing lab, not a
separate submission, deadline, grade item, or extra point. Calculate and freeze your own numbers
first. AI may then check them, but is optional: record any disagreement, source verification, and
which number you kept and why.
The published Lab 14/17 checkout deadlines and ordinary absence/drop rule still apply; this route
is not a makeup.

1. Copy expected return and volatility from `asset_statistics.csv` and the labeled correlations
   from `correlation.csv` into a spreadsheet or paper grid.
2. Calculate selected covariance cells with `cov(i,j) = volatility_i × correlation(i,j) × volatility_j`.
   Reconcile both one diagonal cell and one off-diagonal cell.
3. Use 25% per asset for equal weight. For inverse volatility, calculate `1/volatility_i` and
   divide each reciprocal by their total.
4. Calculate portfolio expected return as the weighted sum. For variance, use the full labeled
   covariance grid and `sum_i sum_j weight_i × weight_j × cov(i,j)`; take the square root for
   volatility.
5. For a mechanics-probe candidate, state the explicitly provisional objective and every
   constraint before selecting weights. A manual candidate may be a transparent feasible
   allocation; it need not claim to be globally optimal. If the CIO objective remains
   decision-material, record `DEFERRED_NO_ADOPTABLE_CANDIDATE`, the exact CIO question,
   escalation owner, and evidence needed to resume. The mechanics probe cannot support adoption.
6. Verify sum-to-one, bounds, concentration, units/frequency, covariance labels/symmetry, and the
   comparison with both baselines.

The supplied returns, volatilities, and correlations are course-authored synthetic annualized
teaching inputs, not estimates from an observed sample. Record provenance as
`COURSE_SYNTHETIC_TEACHING_INPUTS`, sample boundary as `not applicable — no observed sample`,
and Oct. 20, 2026 course release as the evidence vintage. The supplied tables contain no missing
values; extensions must state their own missingness rule. Because the inputs are annualized, the covariance
matrix and reported portfolio volatility are annualized. If you work from periodic returns in an
extension, state the period: variance scales by the number of periods and volatility by its square
root; covariance scales by the number of periods, but correlation does not scale. For this course,
annualize mean periodic return arithmetically as `periods_per_year × mean_periodic_return` and
label it; a separately reported geometric compounded return is not interchangeable. Report both
periodic and annualized return/volatility for that extension; never mix them.

Use the handout tables for results and limitations. Mark solver-only output `not executed`; do not
copy a weight vector from AI. A staff-initialed calculation sheet or accessible spreadsheet is
acceptable evidence for Lab 14. Lab 15 still requires one predicted changed input, actual result,
mandate effect, and disposition.

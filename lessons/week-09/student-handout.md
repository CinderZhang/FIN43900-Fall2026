# Student Handout — Portfolio Construction and Stability

## Input provenance and decision boundary

`asset_statistics.csv` and `correlation.csv` are fictional, course-authored, annualized teaching
inputs published for the Oct. 20, 2026 class. They are not estimates from a historical sample,
do not describe real securities, and contain no missing values. Record the sample boundary as
`not applicable — course-authored synthetic point-in-time inputs`; record the as-of boundary as
`Oct. 20, 2026 course release`. A historical estimator, live-market inference, or claim about
future returns is outside the evidence supplied here.

The CIO case does not authorize one optimization objective. If that ambiguity remains material,
record `DEFERRED_NO_ADOPTABLE_CANDIDATE`, name the ambiguity and escalation owner, and construct
one transparent mechanics-only feasible allocation under an explicitly labeled provisional
classroom objective. It practices the model mechanics but cannot support adoption. Lab 16 still
requires both baselines, mechanical checks, the exact CIO question, and evidence needed to resume.

## Role and deliverable

You are a portfolio analyst. Recommend whether the committee should adopt, rebalance, pilot, or
reject one constrained allocation under the Week 8 mandate. Your deliverable is not a winning
weight vector; it is a baseline comparison, constraint audit, stability record, and conditional
decision that another analyst can reproduce.

## Prework record

Bring your Week 8 mandate. Run the starter and record its equal weights. Without AI, write:

1. the two assets you expect to be most highly correlated;
2. the asset you expect to receive the largest inverse-volatility weight; and
3. one mandate constraint that could bind.

## Finance reference

### Diversification in plain language

Portfolio risk depends on how assets move **together**, not only on each asset's standalone
volatility. The portfolio-variance calculation therefore includes covariance terms. When two
risky assets are less than perfectly positively correlated, one asset's movement can partly
offset the other's, so the combined volatility can be lower than a standalone-risk comparison
suggests. If correlation is `+1`, that offsetting benefit disappears for the pair.

Adding distinct exposures can reduce diversifiable, issuer-specific risk, but the marginal
benefit normally shrinks as more assets are added. Diversification cannot remove common or
systematic risks shared across the portfolio. A low historical correlation is evidence to test,
not a promise: it may rise in a new window or stress regime.

### Equations and mechanical checks

For volatility vector `σ` and correlation matrix `C`:

`Σ = diag(σ) × C × diag(σ)`

For weights `w`, expected-return vector `μ`, and covariance `Σ`:

- portfolio expected return: `wᵀμ`;
- portfolio variance: `wᵀΣw`;
- portfolio volatility: `sqrt(wᵀΣw)`.

All inputs must use compatible frequency and units. Verify labels/order, symmetry, unit diagonal
in correlation, nonnegative variances, positive semidefiniteness within tolerance, weights that
sum to one, and every mandate bound. A solver success message proves none of these by itself.

### PyPortfolioOpt input-contract archaeology

The optional in-class documentation inspection is about the contract hidden behind a returned
weight vector. A portfolio library may accept historical **prices**, transform them into returns,
estimate expected returns `μ` and covariance `Σ`, annualize them at a selected frequency, and pass
those estimates to an optimizer. Before trusting the output, identify and record:

- whether the interface received prices or returns and how missing observations were handled;
- the return, covariance, frequency, and annualization estimators;
- the chosen objective, risk-free-rate assumption if any, and all weight bounds/constraints;
- solver and post-processing behavior, including cleaning or rounding of weights; and
- which results you can reproduce from the course equations and transparent baselines.

The course does not require importing PyPortfolioOpt. This subsection is the complete readable
alternative if its documentation is unavailable; the manual covariance, equal-weight, and
inverse-volatility baselines still come first.

## Tuesday workflow — baseline before candidate

If Python, NumPy, or a solver is unavailable, open **Week 9 Portfolio Calculation Recovery** and
use its paper/accessible-spreadsheet route. The finance evidence and validation standard do not
change; label optimizer-only output unexecuted.

1. Restate decision user, objective, horizon, benchmark, universe, and hard constraints.
2. Record return/volatility frequency, sample/as-of boundary, missingness policy, and whether
   expected returns are forecasts or teaching inputs.
3. Construct covariance and reconcile at least two cells independently.
4. Calculate equal-weight and inverse-volatility weights and portfolio metrics.
5. Write the explicitly provisional mechanics-probe objective and constraints before asking AI
   for code. If the objective remains unresolved, label the decision
   `DEFERRED_NO_ADOPTABLE_CANDIDATE` and name the exact CIO question and escalation owner.
6. Use AI only for implementation help; keep accepted/rejected suggestions and reasons.
7. Verify sum-to-one, bounds, concentration, units, covariance, and baseline comparison.

| Portfolio | Weight summary | Expected return | Volatility | Constraint breach? | What it establishes |
|---|---|---:|---:|---|---|
| Equal weight |  |  |  |  | transparent baseline |
| Inverse volatility |  |  |  |  | risk-scaling baseline |
| Candidate |  |  |  |  | conditional model output |

## Thursday workflow — attack before adoption

Write expected direction before running each selected test.

| Test | Input/constraint changed | Expected direction | Actual result | Mandate effect | Disposition |
|---|---|---|---|---|---|
| Mean estimate |  |  |  |  |  |
| Covariance/window |  |  |  |  |  |
| Constraint/bound |  |  |  |  |  |
| Turnover/cost |  |  |  |  |  |

Ask two AI systems for opposing recommendations. For every material claim, mark
`output-supported`, `assumption-dependent`, or `unsupported`; verify the first independently.
Then close AI and decide a small changed case without it.

## Decision record

- action: adopt, rebalance, pilot, or reject;
- acceptable allocation/risk range rather than false precision;
- baseline and net-of-cost comparison;
- most fragile estimate or interface;
- binding constraint and unresolved ambiguity;
- monitoring trigger, owner, and review frequency; and
- evidence that would reverse the action.

## Submission checklist

Lab 16 requires the mandate, conventions, baselines, candidate, mechanical checks, known answer,
AI disclosure, and receipt. Lab 17 requires the precommitted stability evidence, cost-aware
comparison, committee decision, and transfer explanation. Submit only for yourself. Teammates
may be named, but their names do not establish your evidence. Artifact links are optional.

# Student Handout — Robust Signal Decision

## F-Squared accessible case summary

The SEC's 2014 F-Squared order describes a hypothetical ETF rotation record advertised as though
it reflected live implementation. The historical signals were shifted one week earlier than a
trade could have occurred. That timing error allowed the backtest to appear to sell before price
drops and buy before price increases. Correcting the timing removed virtually all claimed
pre-October-2008 outperformance in the SEC's findings. This summary is the required accessible
alternative to the linked PDF; the course uses it to study leakage, not to supply legal advice.

## Role and deliverable

You are a quantitative investment researcher. Decide whether the supplied signal should be
rejected, redesigned as a new hypothesis, tested in a bounded prospective pilot, or advanced for
more evidence. Deliver the frozen research card, baseline/holdout record, gross/net convention,
selection ledger, robustness evidence, mechanism/claim map, and conditional decision.

## Freeze before testing

| Design element | Frozen value | Why it is permitted before holdout |
|---|---|---|
| hypothesis and sign |  |  |
| information/availability lag |  |  |
| universe and weighting |  |  |
| naive benchmark |  |  |
| development/holdout split |  |  |
| turnover and one-way cost |  |  |
| primary metric and failure threshold |  |  |
| permitted alternatives |  |  |

After the holdout is visible, changing any material design element creates a new hypothesis.

## Finance and implementation reference

For the teaching sign rule, `position_t = sign(signal_t)` and
`gross_return_t = position_t × next_return_t`. State the availability lag that makes this
alignment valid. Define turnover and the initial position before computing costs. One transparent
convention is `turnover_t = |position_t − position_(t−1)|` with `position_0 = 0`, and
`cost_t = turnover_t × one_way_cost_bps / 10,000`. If you use another defensible convention,
label it and reconcile the difference.

## Tuesday workflow

If code is unavailable, use **Week 11 Signal Calculation Recovery**. Staff release the same
holdout only after the frozen design; a paper or accessible-spreadsheet route is acceptable and a
failed holdout remains evidence.

1. Complete and preserve the frozen research card without AI.
2. Compute a naive benchmark and two manual early-period known answers.
3. Use AI to implement only the frozen rule; reject optimization or retuning suggestions.
4. Audit point-in-time alignment, first position, turnover timing, units, and selection ledger.
5. Reveal/run the holdout once.
6. Report early/late and gross/net evidence, including failure.
7. Decide continue unchanged, stop, or register a new hypothesis.

## Thursday robustness and claim record

| Check | Expected result/failure | Actual evidence | Claim consequence |
|---|---|---|---|
| higher costs/breakpoint |  |  |  |
| early versus late/subperiod |  |  |  |
| placebo/falsification |  |  |  |
| uncertainty interval |  |  |  |
| capacity/turnover |  |  |  |

For an interval, state whether resampling assumes independent periods or uses blocks. An interval
does not repair leakage, multiple testing, or post-hoc design.

### What the teaching panels cannot establish

The required 12-row panel is a known-answer mechanism check, not credible statistical evidence.
The optional 36-row `signal_extension_panel.csv` exposes a positive, mixed, and negative regime,
but it is still synthetic, serially structured, and far too small to establish uncertainty,
capacity, or investability. Use it to test whether the action changes when the regime changes—not
to report a persuasive Sharpe ratio or a production allocation.

## Selection ledger

List every signal, lag, threshold, universe, weighting rule, cost rule, and split inspected—not
only the displayed result. Tag bull/bear AI claims as `output`, `source`, `assumption`, or
`speculation`, and independently verify any claim supporting the action.

## Decision record and submission

State action, permitted pilot size/range if any, economic mechanism, gross/net and capacity
assumptions, most consequential failure, monitoring metric/frequency/owner, kill rule, and evidence
required to reopen a failed decision. Lab 20 records the frozen holdout result; Lab 21 records the
merit decision. Submit individually, disclose AI use, attest truthfully, and verify the receipt.

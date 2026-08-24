# Student Handout — Client Mandate and Portfolio Admissibility

> All people, amounts, portfolios, and outcomes are synthetic teaching inputs. This exercise is
> not individualized advice, market evidence, or a legal compliance determination.

## The open-source project this track replicates

The track's optimizer is **PyPortfolioOpt** by **Robert Andrew Martin** — *PyPortfolioOpt:
portfolio optimization in Python*, Journal of Open Source Software 6(61), 3066 (2021);
MIT-licensed, documented on ReadTheDocs, with its example price data shipped in the
repository. His work, his credit: every notebook that uses it carries a citation cell
naming him. Your Tuesday task is **computational reproduction** — recomputing the
project's documented example from its own data — the first rung of replication; the
suitability judgment layered on top is the part no library automates, and it is yours.

## Your role and decision

You are an analyst preparing a fictional household case for fiduciary review. Decide which model
portfolio may advance to **deeper review**, or defer if the record is insufficient. Do not issue
a trade or claim that any return will occur.

## Four different objects

| Object | Meaning | Example | Ownership |
|---|---|---|---|
| Risk tolerance | willingness to experience loss/volatility | client response to a drawdown | client, elicited and documented |
| Risk capacity | financial ability to absorb loss | cash needs, liabilities, horizon | evidence plus professional analysis |
| Hard constraint | candidate must pass | equity cap, cash floor, fee cap | approved mandate |
| Objective | outcome to compare among admissible choices | funding progress/net-return target | client and decision committee |

An attractive expected return does not cure a hard-constraint breach. A target return is not a
guarantee. If facts conflict or a necessary fact is missing, escalate rather than manufacture it.

## Human-first worksheet

Record decision user, action, horizon, annual cash need, loss limit, equity cap, cash floor,
illiquidity cap, fee cap, objective, four material unknowns, and source/authority for each. Then
predict the admissible set before opening AI or implementing code.

## Transparent tests

For every candidate, record `pass`, `fail`, or `unknown` for:

- `max_drawdown_pct ≤ max_one_year_loss_pct`;
- `equity_pct ≤ max_equity_pct`;
- `cash_pct ≥ min_cash_pct`;
- `illiquid_pct ≤ max_illiquid_pct`; and
- `annual_fee_pct ≤ max_fee_pct`.

Calculate `net_return_pct = gross_return_pct − annual_fee_pct`, but use it only to compare
admissible candidates. Preserve every reason code; never collapse the result into an unexplained
score.

## AI challenge, not AI authority

Give two course-supported systems the same synthetic record through the published packet,
accessible free interfaces, or `COURSE-RUN PROBE:` route. Ask each to
translate it into a mandate and name missing evidence. For every proposal, mark `accept`,
`modify`, `reject`, or `escalate`; cite the governing case fact or explain the unknown. Independently
re-run the constraint tests. Agreement between systems is not validation.

## Committee record

Deliver a one-page record with: selected/deferred action; admissible set and reason codes;
comparison among admissible candidates; strongest evidence; principal unknown; fee and return
limitations; conflict check; monitor/owner/frequency; and two observable triggers that reopen or
reverse the action. Finish with a 45-second no-AI defense.

Retain the record as optional capstone evidence. There is no checkout or grade item.

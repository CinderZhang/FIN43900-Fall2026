# Week 5 Student Handout — Credit Is a Downside Decision

## Decision frame

State borrower/transaction, exposure, horizon, decision user, available actions, loss if an
unsafe case passes, and opportunity cost if a safe case is rejected.

## 5-Cs evidence map

| C | Question | Observable evidence | Common AI/data failure |
|---|---|---|---|
| Character | Willingness/governance/record? | filings, payment/legal/governance evidence | narrative moral judgment without evidence |
| Capacity | Can cash flow service obligations? | coverage, FCF, cyclicality, stress | EBITDA treated as cash |
| Capital | How much loss-absorbing stake exists? | equity, leverage, sponsor support | book/market or entity mismatch |
| Collateral | What supports recovery? | asset quality, lien, seniority, valuation | gross asset value treated as recoverable value |
| Conditions | What external/contract terms matter? | cycle, rates, covenants, maturity, regulation | generic macro list without mechanism |

## Ratio convention sheet

`Debt / EBITDA` — define gross/net debt, leases, LTM/normalized EBITDA.

`EBIT / interest expense` — define operating profit and cash/accrual interest period.

`Current assets / current liabilities` — inspect restricted cash and classification quality.

`(CFO − Capex) / debt` — state capex sign and whether the cash-flow measure is sustainable.

Ratios do not share universal definitions. Document the convention before calculating.

## Screening policy

For every factor record definition, threshold/weight, missingness rule, sector qualification,
override condition, source, and error cost. A score must preserve factor-level reasons.

## Validation

Use **Week 5 Synthetic Outcome-Label Convention**: label `1` is a fully observed payment default, insolvency, or
principal-impairing restructuring within 12 months; label `0` is none of those events. There are
no censored cases. Map `review/reject` to the positive risk flag and `approve` to negative before
interpreting false approvals and false rejections.

- known-answer ratio reconciliation;
- one source/definition check;
- confusion matrix or labeled-case comparison;
- false-positive and false-negative review;
- one changed threshold or missingness rule; and
- one case where qualitative evidence overrides the composite score.

End with `approve`, `deeper review`, or `reject`, plus evidence needed to change the action.

If code fails, follow **Week 5 Calculation Recovery and Project 1 Credit Transfer**; its paper or
accessible-spreadsheet route requires the same ratios, reason codes, and error-cost logic. After
the synthetic lab, complete its bounded target-company section inside your Project 1 repository.
That transfer is project evidence, not an additional checkout.

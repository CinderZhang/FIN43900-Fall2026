# Student Handout — Project 2 Close and Bond Screening

> **Fall 2026 selected track: Fixed-Income Decision Systems.** Release this handout uniformly to
> both sections after the ordinary module release checks pass.

## Tuesday — final Project 2 readiness

### Role and deliverable

You are the final evidence auditor. Verify the 12-row manifest, instructional-team access,
visible output, exact run command, transcripts/durations, as-of dates, and one highest-risk
changed-input result. Freeze remaining must-fix actions; do not open new project scope.

| Item | Ready location/evidence | Remaining defect | Owner/action before cutoff |
|---|---|---|---|
| Edition A and A/B reconciliation |  |  |  |
| repository/environment/visible output |  |  |  |
| memo/deck and numbers/as-of consistency |  |  |  |
| validation, holdout, costs, capacity, kill rule |  |  |  |
| Videos 1–3 and corrected transcripts |  |  |  |

Lab 20 records current evidence and gaps; it does not extend the project deadline or create a
makeup. If dropped, the project evidence remains required.

## Thursday — role and finance reference

You are screening fictional bonds for deeper institutional review—not issuing a final buy order.
Before Thursday, budget **10–15 minutes**. Read the convention sheet and, **without generative
AI**, label clean versus dirty price and predict the direction of the off-cycle invoice price.
Preserve that prediction for class. Do not run the starter or derive convexity before class.

For promised cash flows `CF_t`, annual yield `y`, and integer coupon-date periods:

- `Price = Σ CF_t / (1+y)^t`;
- `Macaulay duration = Σ[t × PV(CF_t)] / Price`;
- `Modified duration = Macaulay / (1+y)`;
- `Convexity = Σ[t(t+1)CF_t/(1+y)^(t+2)] / Price`;
- `ΔP/P ≈ −ModifiedDuration × Δy + 0.5 × Convexity × (Δy)^2`.

These simplified annual coupon-date formulas do not silently apply to an off-cycle bond. For an
off-cycle settlement, reconcile accrued interest and settlement-adjusted timing; dirty/invoice
price equals clean quote plus accrued interest.

## Known-answer gate before screening

If Python is unavailable, use **Week 13 Bond Calculation and Screening Recovery**. Its
calculator/paper/spreadsheet route is the complete learner fallback and preserves the same
convention, screen, and limitation requirements.

1. Reconcile the off-cycle microcase: coupon, accrued fraction, accrued interest, clean price,
   and dirty invoice price.
2. For K1, use the supplied anchor below to sum price and derive Macaulay/modified duration.
   Inspect—not hand-derive—the supplied convexity, exact +100 bp return, and approximation;
   explain why their agreement is a check rather than proof.
3. State the convention and why the result is a teaching anchor rather than market evidence.

| Period `t` | Cash flow | Supplied PV at 4% |
|---:|---:|---:|
| 1 | 5 | 4.807692 |
| 2 | 5 | 4.622781 |
| 3 | 105 | 93.344618 |

Supplied extension outputs: price 102.775091; Macaulay duration 2.861463; modified duration
2.751407; convexity 10.412662; exact +100 bp price return −2.700159%; duration-convexity
approximation −2.699343%. Your core work must reproduce price and both duration measures and
interpret the extension outputs. Hand-calculating convexity is optional extension work.

## Evidence and screen design

| Field/claim | What is supplied | What it may support | What it cannot establish |
|---|---|---|---|
| price/yield/coupon/maturity | synthetic convention-consistent values | promised-cash-flow/rate analysis | real executable quote |
| spread bps | synthetic relative spread | screen prioritization | default probability or cheapness |
| stale days/trade count | synthetic activity indicators | measurement/liquidity caution | actual market depth |
| issuer/sector | fictional labels | concentration grouping | real credit quality |

Before seeing results, state thresholds, missingness treatment, mandate reason, and override rule.
Use AI to implement or challenge only after that policy exists. For each AI rationale, mark
`field-supported`, `assumption`, or `unsupported` and verify the first independently.

## Decision record

For each advanced/quarantined bond record screen reasons, price/risk reconciliation status,
staleness/liquidity limitation, missing evidence, and mandate effect. End with reject, quarantine,
or deeper review; evidence request; condition; monitor; and reversal trigger. A screen result is
not a final investment recommendation.

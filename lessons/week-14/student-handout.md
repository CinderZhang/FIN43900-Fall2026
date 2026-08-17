# Student Handout — Bond Portfolio Mandate Stress

> **Fall 2026 selected track: Fixed-Income Decision Systems.** Release this handout uniformly to
> both sections after the ordinary module release checks pass.

The Capstone Edition A window is **Thu Nov. 19, 6:00 p.m. ET–Tue Nov. 24, 1:30 p.m. ET**.
Budget **20 minutes** and submit the separate ungraded checkpoint before any new
capstone-specific generative-AI work. This studio remains formative.

## Role and deliverable

You are an institutional bond-portfolio analyst. Produce a one-page committee decision containing
validated exposures, separate rate/spread scenario impacts, constraint checks, an AI trade
disposition, action/allocation change if any, and two monitoring/reversal triggers.

This is the **same fictional bond case and data vintage** introduced in Week 13. Bond IDs K1–K5,
issuer, sector, duration, spread, staleness, and activity fields retain their Week 13 identities;
only portfolio weights, mandate, and scenario shocks are new. Treat any identity mismatch as a
data-lineage defect, not a new issuer fact.

## Mandate

- modified duration between 2.5 and 4.0;
- no issuer above 40%;
- no sector above 50%;
- absolute loss under the supplied +75 bp spread scenario no greater than 3.0%;
- at least 20% in bonds with `stale_days ≤ 3` and `trade_count_20d ≥ 10`; and
- no security with `stale_days > 10` may be added.

The no-add rule does not automatically require immediate sale of an existing holding. Explain
current-holding versus incremental-trade treatment rather than silently combining them.

## Prework prediction

Verify weights sum to one. Without AI, predict whether the current portfolio passes the duration
and liquid-weight tests, whether K4 may remain, and whether more K4 may be added. Preserve the
prediction before calculation. Run the starter only to load `portfolio.csv`, `scenarios.csv`, and
`mandate.json`; do not implement the unfinished stress, constraint, or rebalance functions.
Budget **20–25 minutes** for this separate prework task.

## Finance reference

- weighted portfolio modified duration: `Σ weight_i × modified_duration_i`;
- first-order parallel rate return: `−portfolio_duration × Δrate`;
- simplified position-level spread return: `Σ weight_i × (−modified_duration_i × Δspread_i)`.

State shocks in decimal form and outputs as returns. These approximations omit convexity, curve
shape, migration/default/recovery, changing cash flows, and liquidity execution effects.
The spread formula deliberately assumes **spread duration equals modified duration**. State that
assumption. It may fail for callable, credit-sensitive, path-dependent, distressed, or otherwise
cash-flow-changing securities.

## Workflow

If code is unavailable, use **Week 14 Bond Mandate-Stress Calculation Recovery**. Its
calculator/paper/spreadsheet route tests the same mandate and scenario evidence; label any
code-only extension unexecuted.

1. Validate weight total, labels, and current exposure inputs.
2. Compute weighted duration and qualifying liquid weight.
3. Aggregate issuer and sector weights before applying concentration limits.
4. Run the +100 bp rate shock and +75 bp spread shock separately; test the spread-loss bound.
5. Record each mandate test as pass, fail, or unknown with evidence.
6. Ask AI for a yield-pickup rebalance. Tag its claims/trades as mandate-compliant,
   assumption-dependent, unsupported, or prohibited.
7. Propose the smallest compliant alternative—or no trade—and recompute affected constraints.
8. Close AI and defend approve, modify, rebalance, or reject.

| Evidence | Current | Proposed | Mandate/result | Limitation |
|---|---:|---:|---|---|
| weight total |  |  |  |  |
| modified duration |  |  |  |  |
| qualifying liquid weight |  |  |  |  |
| largest issuer weight |  |  |  |  |
| largest sector weight |  |  |  |  |
| +100 bp rate impact |  |  |  |  |
| +75 bp spread impact |  |  |  |  |

## Committee record and optional capstone evidence

State action, allocation change/range, governing constraint, strongest evidence, unsupported AI
claim, approximation boundary, monitor/owner/frequency, and two triggers that reverse or escalate
the action. Retain this as optional capstone evidence; it earns no separate points
and does not force a fixed-income capstone topic.

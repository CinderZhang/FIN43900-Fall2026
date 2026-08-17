# Week 14 Bond Mandate-Stress Calculation Recovery

Use this route when code is unavailable. The same mandate,
scenario, and decision standards apply.

Switch during the same formative session, show the paper/accessible-spreadsheet evidence at the
exit check for visual initials, and keep it. This creates no separate submission, deadline, grade item, or
extra point. Calculate and freeze your own numbers first. AI may then check them, but is optional:
record any disagreement, source verification, and which number you kept and why.

1. Copy every row from `portfolio.csv`; verify weights sum to 1.00.
2. Calculate weighted modified duration as `sum(weight × modified duration)`.
3. Mark qualifying liquid positions using both `stale_days ≤ 3` and `trade_count_20d ≥ 10`, then
   sum their weights.
4. Aggregate weights by issuer and sector and identify the largest of each.
5. Calculate the separate +100 bp rate return as `−portfolio duration × 0.01`.
6. Calculate the separate +75 bp spread return as
   `sum(weight × −modified duration × 0.0075)`, explicitly assuming spread duration equals
   modified duration.
7. Test every `mandate.json` rule. Treat permission to hold K4 separately from permission to add
   K4 because its stale-days value triggers the no-add rule.
8. For one small proposed trade or `no trade`, recompute every affected constraint and state the
   committee action, monitor, owner, frequency, and two reversal/escalation triggers.

These first-order approximations omit convexity, curve shape, migration/default/recovery,
cash-flow change, and execution liquidity. A staff-initialed paper table or accessible spreadsheet
is acceptable formative evidence. Label any code-only or optimizer output unexecuted; an AI trade
cannot relax a mandate or invent an objective.

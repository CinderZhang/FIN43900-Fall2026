# Week 2 Offline/No-Code Fallback — Valuation Object and Bridge

Use this packet when code, network, or provider access fails. The inputs reproduce
the downloadable **Mini Case** file (`mini_case.csv`); they are a synthetic teaching case, not
company evidence.

## Inputs

EBIT 150; tax rate 25%; D&A 40; capex 60; increase in operating NWC 15; enterprise value
1,000; non-operating cash 100; debt 250; noncontrolling interest 20; unfunded pension 10;
diluted shares 100. All monetary amounts are USD millions; shares are millions.

## Required manual work

1. Classify each input as operating, non-operating, debt/debt-like, non-common, or share-basis.
2. Calculate `NOPAT = EBIT × (1 − tax rate)` and
   `FCFF = NOPAT + D&A − capex − increase in operating NWC`.
3. Calculate common equity value from enterprise value and the full bridge, then per-share value.
4. Record one unit/sign failure that would reverse the interpretation.
5. Build two evidence-ledger rows on paper and label the source `SYNTHETIC TEACHING CASE`.

## Reconciliation anchors

NOPAT = 112.5; FCFF = 77.5; common equity value = 820; per-share value = 8.20.
The packet proves finance mechanics and evidence structure only. It cannot validate a student's
target-company facts, filing date, units, normalization, or recommendation.

Submit the same Lab 03/04 fields, plus the exact technical failure and the fallback label.

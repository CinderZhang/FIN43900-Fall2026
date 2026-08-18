# Session 5 — Build the Engine
**Week 3 · Tuesday · Lab 05: Build and Validate an FCFF DCF**

---

## The week the course points at (7 min)

Interviews for analyst seats test one thing in the first ten minutes:
can you build a DCF and say **which assumptions the value hinges on**?
AI assembles spreadsheets. The seat belongs to whoever explains them.

You did the prework walk. Every number today is that training case.

---

## The known answer, on the board (10 min)

FCFF₀ = 100, growth 8/6/5/4/3%, WACC 10%, g 3%, cash 50, debt 300, 50M shares

> FCFF₁ = 100 × 1.08 = **108.00** · PV = 108/1.10 = **98.18**
> ΣPV(5yr) = **448.44** · TV₅ = 132.63/0.07 = **1,894.65** → PV **1,176.43**
> EV = **1,624.87** → equity **1,374.87** → **$27.50/share** · TV share **72.4%**

Your engine must reproduce every one of these within tolerance.

---

## AI off, then on (10 + 20 min)

1. Draw the architecture from memory: FCFF → discount → TV → bridge → per-share
2. Hand-calculate Year-1 FCFF and its PV (the checkout asks for these)
3. AI on: implement the STUDENT_WORK functions; reproduce `dcf_expected_output.csv`

---

## Validate every line (11 min)

- Boundary: reject g ≥ WACC, missing shares, mixed units
- Shape: growing cash flows must have **shrinking** PVs
- Concentration: report TV share — 72.4% is normal; know why

---

## Transfer + checkout (10 + 7 min)

Move your target's reconciled Week-2 inputs into the input table —
label every forecast assumption; never let AI silently complete one.

**Checkout:** convention · hand-calculated FCFF₁ and PV · synthetic EV /
equity / per-share / TV share · one passed test + one fixed failure ·
target rows + one unresolved assumption · AI paths · in-person attendance
declaration · truth attestation · receipt.

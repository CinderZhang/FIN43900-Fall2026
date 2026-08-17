# Week 3 Student Handout — DCF as a Range and a Test

## Training-case convention

- annual FCFF in USD millions;
- five explicit forecast years;
- cash flows occur at each year-end;
- WACC discounts FCFF;
- Gordon-growth terminal value at the end of Year 5;
- terminal growth must be less than WACC; and
- enterprise value is bridged to common equity and diluted per-share value.

## Core equations

`FCFF_t = EBIT_t × (1 − tax rate_t) + D&A_t − Capex_t − ΔOperating NWC_t`

`PV(FCFF_t) = FCFF_t / (1 + WACC)^t`

`Terminal value_5 = FCFF_5 × (1 + g) / (WACC − g)`

`Enterprise value = Σ PV(FCFF_t) + PV(Terminal value_5)`

`Equity value = Enterprise value + non-operating assets − debt − debt-like/non-common claims`

`Per-share value = Equity value / diluted common shares`

## Validation ladder

1. **Known answer:** reproduce the synthetic case before using a real company.
2. **Boundary:** reject `g >= WACC`, missing/negative shares, mixed units, or a zero/negative
   denominator.
3. **Reconciliation:** compare Year 1 forecast mechanics with the final historical period.
4. **Monotonicity:** holding other inputs constant, value should normally fall as WACC rises
   and rise as terminal growth rises.
5. **Concentration:** report the terminal-value share of enterprise value.
6. **Changed input:** show the effect of one economically plausible operating change.
7. **AI risk:** independently verify one AI-proposed assumption, formula, or source.

## Scenario design

A scenario is a coherent causal story, not three arbitrary growth rates.

| Driver | Low case mechanism | Base evidence | High case mechanism | Source/range |
|---|---|---|---|---|
| revenue growth |  |  |  |  |
| operating margin |  |  |  |  |
| reinvestment/capex |  |  |  |  |
| working capital |  |  |  |  |
| WACC |  |  |  |  |
| terminal growth |  |  |  |  |

Name dependencies. Higher growth may require higher reinvestment; higher risk may change both
cash flows and discount rate. Avoid combining mutually inconsistent “best” assumptions.

## Reverse DCF

Reverse DCF begins with an observed market price and solves for one explicit assumption that
makes model value equal market value while other assumptions remain stated. It identifies an
implied expectation; it does not prove the expectation is correct.

Record:

- market price and timestamp/as-of source;
- fixed assumptions;
- solved assumption and feasible range;
- economic interpretation; and
- evidence that would make the implied expectation plausible or implausible.

## Decision language

> My supported valuation range is **[low–high]** per diluted share versus a market price of
> **[price] as of [time/date/source]**. The conclusion is most sensitive to **[driver]**.
> For a committee with no current position, I recommend **[initiate/watch-defer/do not initiate]**
> only if **[condition]**; revisit if
> **[monitorable trigger]**. Terminal value represents **[share]** of enterprise value, so
> **[limitation]** remains material.

Do not use the instructor demonstration company, Asbury Automotive Group (`ABG`).

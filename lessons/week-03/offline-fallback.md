# Week 3 Offline/No-Code Fallback — DCF and Sensitivity

Use this packet when Python, Colab, network, or provider access fails. Inputs and anchors are the
same as the downloadable **Dcf Case** and **Dcf Expected Output** files; all are synthetic.

## Manual sequence

1. Forecast FCFF from starting FCFF 100 using annual growth 8%, 6%, 5%, 4%, and 3%.
2. Discount annual year-end cash flows at 10% WACC.
3. Calculate terminal value at year 5 with 3% perpetual growth and discount it.
4. Bridge enterprise value to equity with cash 50 and debt 300; divide by 50 diluted shares.
5. Calculate terminal-value share of enterprise value.
6. State the expected direction before changing WACC or terminal growth; reject `g ≥ WACC`.

## Reconciliation anchors

FCFF years 1–5: 108.0000, 114.4800, 120.2040, 125.0122, 128.7625. Present value of explicit
FCFF = 448.4408; terminal value at year 5 = 1,894.6486; present value of terminal value =
1,176.4277; enterprise value = 1,624.8685; equity value = 1,374.8685; per-share value = 27.4974;
terminal-value share = 72.4014%.

The worksheet preserves the finance outcome but not a live target-company valuation. Submit the
same lab evidence, the exact execution failure, `SYNTHETIC TEACHING CASE`, and the unresolved
target-company evidence action.

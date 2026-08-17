# Bond Price Reconciliation — Before Relative Value

## Microcase A: accrued interest and invoice price

This fictional bond has par 100, 6% annual coupon paid semiannually, and an explicitly supplied
US 30/360 teaching accrual fraction of 90/180 for the regular nominal half-year. The displayed
last-coupon, settlement, and next-coupon dates are context; they do not establish every real-
market calendar/business-day adjustment. Quoted clean price is 98.25.

Complete and explain:

| Item | Calculation | Known answer |
|---|---|---:|
| semiannual coupon | `100 × 6% / 2` | 3.00 |
| accrued fraction | `90 / 180` | 0.50 |
| accrued interest | `3.00 × 0.50` | 1.50 |
| dirty/invoice price | `clean + accrued` | 99.75 |

State why the dirty price—not the quoted clean price—is the settlement value. This microcase
does not ask you to infer yield or duration without a complete maturity/cash-flow schedule.

## Anchor B: K1 promised cash flows through risk measures

K1 is annual-pay and settles exactly on a coupon date. Show the cash-flow vector `[5, 5, 105]`,
discount each cash flow at the supplied 4% annual yield, reconcile their present values to dirty
and clean price 102.775091, then calculate Macaulay duration, modified duration, convexity, the
exact +100 bp price change, and the duration-convexity approximation. Use the convention sheet;
do not copy the supplied output without the reconciliation.

Only after both reconciliations may you interpret spread, staleness, liquidity, or relative
value. Separate a rate shock from a spread shock before any combined extension.

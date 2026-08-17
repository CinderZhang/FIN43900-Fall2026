# Fixed-Income Conventions — Synthetic Teaching Case

- All bonds are fictional and course-authored; values are not market evidence.
- As-of/settlement date: 2026-11-16, assumed exactly on a coupon date.
- Par value: 100; prices are clean and equal dirty price because accrued interest is zero.
- Fixed coupons are annual; `coupon_rate` is annual coupon divided by par.
- Yield to maturity uses annual compounding and promised cash flows.
- `years_to_maturity` is an integer in the known-answer calculation.
- Macaulay duration is PV-time weighted; modified duration is Macaulay divided by `(1 + y)`.
- Convexity uses `sum[t(t+1)CF_t/(1+y)^(t+2)] / price` for the annual-pay case.
- Known-answer acceptance tolerance is absolute `1e-5` for price, duration, and convexity and
  `1e-6` for reported scenario returns. A result outside tolerance triggers convention/unit/input
  reconciliation before screening.
- `spread_bps` is a supplied synthetic option-free-style relative spread to a same-horizon
  government benchmark; students do not infer a proprietary rating or default probability.
- In the Week 14 first-order teaching scenario, spread duration is explicitly approximated by
  modified duration for these fixed-cash-flow, option-free-style bonds. The numerical equality is
  an assumption for the supplied spread shock—not evidence that rate and spread risk are the same
  economic exposure or that the equality generalizes to callable/path-dependent cash flows.
- `stale_days` counts calendar days since the synthetic last observation; `trade_count_20d`
  is the supplied synthetic 20-day activity count.
- No ratings, proprietary identifiers, actual issuers, or private research data are present.

## Why the anchor settles on a coupon date

Bond K1 deliberately settles exactly on a coupon date, so accrued interest is zero and clean
price equals dirty price. This isolates promised cash-flow discounting, yield, duration, and
convexity inside the 15-minute known-answer gate. Annual payment and annual compounding are an
explicit teaching simplification, not a market-default convention or a claim about every bond.

Before K1, reconcile the off-cycle microcase in `bond-price-reconciliation.md`: semiannual
coupon 3.00; 90 of 180 days accrued under the supplied 30/360 convention; accrued interest
1.50; clean price 98.25; dirty invoice price 99.75. For an off-cycle bond, yield/duration must
use settlement-adjusted cash-flow timing and dirty value; subtract accrued interest only when
reporting clean price. Do not apply K1's integer-period formula silently to an off-cycle bond.

For this synthetic regular semiannual coupon period, **90/180 is explicitly supplied**. Under
the chosen US 30/360 teaching convention, the denominator is the nominal 180-day half-year, not
an inference from the displayed calendar dates. Holiday, business-day, stub-period, and security-
specific convention adjustments are outside this microcase and must be checked in real work.

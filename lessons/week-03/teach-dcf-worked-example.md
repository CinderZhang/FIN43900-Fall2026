# The Training-Case DCF, Worked End to End

*This page teaches. It contains no rules and no submission requirements — those live in the
Week 3 handout and Lab 05. Work through it before class with a calculator or a blank
spreadsheet. Every number below is the official training case: the same figures your Lab 05
engine must reproduce.*

## Why a committee pays for this

An investment committee never asks "what is the stock worth?" as trivia. It asks: *if we put
money here, what future cash actually pays us back, and what must we believe for that to
happen?* A DCF is the only valuation method that answers in those terms — every other method
(multiples, deal comps) prices a company by analogy. That is why the DCF is the spine of your
Project 1 and why an analyst who can defend one — assumption by assumption — is trusted with
capital, while one who can only quote a model's output is not.

## The case

A company generated **free cash flow to the firm (FCFF) of $100 million** in the year just
ended. Growth is expected to fade as the business matures: **8%, 6%, 5%, 4%, 3%** over the
next five years, then **3% forever**. The weighted average cost of capital (**WACC**) is
**10%**. The company holds **$50M of non-operating cash**, owes **$300M of debt**, and has
**50 million diluted shares**. Cash flows arrive at each year-end.

One sentence before any arithmetic: *we are valuing the operating business first (enterprise
value), and only then figuring out how much of it belongs to shareholders (equity value).*
Keeping those two ideas separate is the single most common thing juniors get wrong.

## Step 1 — Forecast the cash flows

Each year's FCFF is last year's grown once. Do the first one by hand — always:

> FCFF₁ = 100 × 1.08 = **108.00**

| Year | Growth | FCFF ($M) |
|---:|---:|---:|
| 1 | 8% | 108.00 |
| 2 | 6% | 108.00 × 1.06 = 114.48 |
| 3 | 5% | 114.48 × 1.05 = 120.20 |
| 4 | 4% | 120.20 × 1.04 = 125.01 |
| 5 | 3% | 125.01 × 1.03 = 128.76 |

Notice what the fade *says economically*: competition arrives, high-return projects run out,
growth converges toward the economy's. A forecast whose growth never fades is a claim that
competition never arrives — that claim needs evidence, not a spreadsheet.

## Step 2 — Discount them

A dollar in year *t* is worth 1/(1.10)ᵗ today. That factor shrinks fast:

| Year | FCFF | ÷ (1.10)ᵗ | Present value |
|---:|---:|---:|---:|
| 1 | 108.00 | 1.1000 | 98.18 |
| 2 | 114.48 | 1.2100 | 94.61 |
| 3 | 120.20 | 1.3310 | 90.31 |
| 4 | 125.01 | 1.4641 | 85.38 |
| 5 | 128.76 | 1.6105 | 79.95 |
| | | **Sum** | **448.44** |

Check the shape before trusting any model: the cash flows *grow* every year, yet their present
values *shrink* every year. If your model's PV column doesn't shrink here, the discounting is
wrong — no further inspection needed.

## Step 3 — Terminal value: the number that dominates everything

Five explicit years never capture a going concern. At the end of Year 5 we bundle every year
thereafter into one number using Gordon growth: next year's cash flow, divided by how much the
discount rate exceeds growth.

> TV₅ = FCFF₅ × (1 + g) / (WACC − g) = 128.76 × 1.03 / (0.10 − 0.03) = 132.63 / 0.07 =
> **1,894.65**

Two things deserve a hard stare:

1. **That denominator is a hair trigger.** It is WACC − g = 7 cents on the dollar. Nudge g
   from 3% to 4% and the denominator drops to 0.06 — the terminal value jumps ~18% from that
   alone. This is why `g < WACC` is enforced as a hard boundary in your engine: at g = WACC
   the formula divides by zero, and above it the math claims infinite value.
2. **TV₅ is a Year-5 number.** It still has to travel back to today:

> PV(TV) = 1,894.65 / 1.6105 = **1,176.43**

## Step 4 — Enterprise value, and the question everyone asks

> EV = 448.44 + 1,176.43 = **1,624.87**

The terminal value is 1,176.43 / 1,624.87 = **72.4%** of enterprise value.

*"Nearly three-quarters of the value comes from years we didn't even model — is the model
broken?"* No — this is **normal**, and knowing that is what separates you from a surface
reading. A going concern's value mostly lives beyond any five-year window; mature-company
DCFs routinely put 60–80% in the terminal. What the 72.4% *does* tell you: the defense of
this valuation is mostly a defense of the terminal assumptions (g and WACC), not the explicit
years. Report the share, then aim your evidence where the value actually is. A terminal share
approaching 90%+ is a different signal — your explicit window may be too short or your fade
story unfinished.

## Step 5 — The bridge: from the business to your shares

Enterprise value belongs to *all* capital providers. Shareholders get what's left:

> Equity value = EV + non-operating assets − debt = 1,624.87 + 50 − 300 = **1,374.87**
> Per share = 1,374.87 / 50 = **$27.50**

Walk the logic, not just the arithmetic: the $50M of cash is real value the operating
forecast never touched, so it is *added*; the $300M of debt has first claim on the operating
value, so it is *subtracted*; what remains is divided over *diluted* shares because options
and RSUs will claim their slice. On a real company this bridge gains more rows — leases,
minority interests, pensions, preferred — and Week 2's evidence ledger is where each row gets
a source and a date. The training case keeps three rows so the *logic* is unmissable.

## Step 6 — Before you ever rerun a model, write your prediction

This is the professional habit Lab 06 will grade, so practice it here. Suppose WACC rises
from 10% to 11%. **Before computing**: which direction does value move, and roughly how much?
Write it down.

Now the answer: every discount factor grows, and the terminal denominator widens from 0.07 to
0.08. Rerun the arithmetic and per-share value falls from **$27.50 to about $23.41 — a 15%
drop from one percentage point.** If your prediction had the direction right but the size
shocked you, that *is* the lesson: this model's conclusion is hostage to the discount rate,
which is exactly what you'll tell the committee when you present a range instead of a point.

## What you now own

- FCFF₁ = 108.00 and PV(FCFF₁) = 98.18, by hand — the known-answer seed for your engine
- The full chain: 448.44 + 1,176.43 = 1,624.87 → 1,374.87 → **$27.50**, TV share **72.4%**
- Why TV dominance is normal, why `g < WACC` is non-negotiable, why the bridge adds cash and
  subtracts debt, and why a 1-point WACC move is a 15% event

**Lab 05 begins exactly here**: you'll draw this architecture from memory, hand-calculate the
Year-1 numbers, then implement the engine that reproduces every figure on this page within
tolerance — and only then point it at your own target company, where the inputs stop being
given and start being defended.

## Check yourself (answers upside-down style — work first)

1. FCFF₃ from the table's FCFF₂, by hand.
2. Why is TV discounted by (1.10)⁵ and not (1.10)⁶, given it uses Year-6 cash flow?
3. Your teammate's model shows PV of Year-4 FCFF *greater* than PV of Year-3. What single
   conclusion do you draw before reading any code?
4. The bridge shows equity value *above* enterprise value. What must be true of the balance
   sheet for that to be legitimate?

*Answers: (1) 114.48 × 1.05 = 120.20. (2) Gordon growth already values the Year-6-and-beyond
stream as of end of Year 5; the result is a Year-5 amount. (3) The discounting is broken —
growing cash flows must have shrinking PVs at a constant positive rate; check before debating
assumptions. (4) Non-operating assets exceed debt-like claims — e.g., a large net-cash
position. Rare, real, and worth verifying against the filing.*

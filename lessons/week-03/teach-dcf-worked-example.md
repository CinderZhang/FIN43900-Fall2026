# The Training-Case DCF, Worked End to End

*This page teaches. It contains no rules and no submission requirements — those live on the
lab pages. Work through it before class with a calculator or a blank spreadsheet. Every number
below is the official training case: the same figures your Lab 05 run must reproduce, and the
same case Lab 06 stresses.*

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

Look at the shape: the cash flows *grow* every year, yet their present values *shrink* every
year. That happens **because every growth rate here is below the 10% discount rate** — 8%, 6%,
5%, 4% and 3% are each less than 10%, so discounting outruns growth.

**It is not a universal rule, and you should not check your model against it as one.** When a
year's growth exceeds the discount rate, that year's present value is *larger* than the
previous year's, and the model is still right. Counterexample, worth twenty seconds with a
calculator: cash flows of **120** in Year 1 and **144** in Year 2 (20% growth), discounted at
10%:

> PV₁ = 120 / 1.10 = **109.09**  ·  PV₂ = 144 / 1.21 = **119.01**

Rising present values, correct arithmetic. So the honest check is conditional: **in a case
where every growth rate is below WACC, the PV column must shrink — and if it does not, the
discounting is wrong.** That describes our training case, so the check applies here. It would
not apply to a company you forecast growing faster than its cost of capital in the early years.

## Step 3 — Terminal value: everything after Year 5, in one number

Five explicit years never capture a going concern. At the end of Year 5 we bundle every year
thereafter into one number using Gordon growth: next year's cash flow, divided by how much the
discount rate exceeds growth.

> TV₅ = FCFF₅ × (1 + g) / (WACC − g) = 128.76 × 1.03 / (0.10 − 0.03) = 132.63 / 0.07 =
> **1,894.65**

Two things deserve a hard stare:

1. **That denominator is a hair trigger.** It is WACC − g = 7 cents on the dollar. Move g from
   3% to 4% and the denominator drops to 0.06 — terminal value goes from 1,894.65 to 2,231.88,
   a **17.8% jump from one percentage point**. This is why `g < WACC` is enforced as a hard
   boundary: at g = WACC the formula divides by zero, and above it the math claims infinite
   value.
2. **TV₅ is a Year-5 number.** It still has to travel back to today:

> PV(TV) = 1,894.65 / 1.6105 = **1,176.43**

## Step 4 — Enterprise value, and what the terminal share actually measures

> EV = 448.44 + 1,176.43 = **1,624.87**

The terminal value is 1,176.43 / 1,624.87 = **72.4%** of enterprise value.

*"Nearly three-quarters of the value comes from years we didn't even model — is the model
broken?"* No. But the usual reassurance — "that's normal for a going concern" — is too loose to
be useful. Be precise about what actually moves that share. Two things do:

- **The spread WACC − g.** A narrower spread puts more weight in the terminal. Same cash flows,
  same model: at WACC 11% and g 2% the terminal share is **66.5%**; at WACC 9% and g 4% it is
  **79.1%**. Nothing about the business changed. Only the two terminal assumptions did.
- **Where you drew the line.** Extend the explicit window from five years to ten, keeping
  growth at 3% after Year 5. The arithmetic is identical, so enterprise value stays at
  **1,624.87** — but the terminal share falls from **72.4% to 52.1%**. Same company, same
  value, a very different-looking share.

Carry that second fact: **the terminal share is partly an artifact of your forecast horizon,
not a measurement of where value comes from.** By itself it is not evidence that a model is
wrong.

What the 72.4% *is* good for: it tells you where your evidence has to be strongest. Here the
defense of the valuation is mostly a defense of g and WACC, not of the explicit years — so
that is where you spend your research time. A terminal share climbing toward 90% deserves a
second look for a specific reason: either the explicit window is short relative to how long the
fade actually takes, or the spread WACC − g has been squeezed so tight that the denominator is
doing all the work.

## Step 5 — The bridge: from the business to your shares

Enterprise value belongs to *all* capital providers. Shareholders get what's left:

> Equity value = EV + non-operating assets − debt = 1,624.87 + 50 − 300 = **1,374.87**
> Per share = 1,374.87 / 50 = **$27.50**

Walk the logic, not just the arithmetic: the $50M of cash is real value the operating forecast
never touched, so it is *added*; the $300M of debt has first claim on the operating value, so
it is *subtracted*; what remains is divided over *diluted* shares because options and RSUs will
claim their slice. On a real company this bridge gains more rows — leases, minority interests,
pensions, preferred — and each of those rows needs a source and a date from the filing. The
training case keeps three rows so the *logic* is unmissable.

## Step 6 — Before you ever rerun a model, write your prediction

This is the professional habit Lab 06 grades, so practice it here. Suppose WACC rises from 10%
to 11%. **Before computing**: which direction does value move, and roughly how much? Write it
down.

Now the answer: every discount factor grows, and the terminal denominator widens from 0.07 to
0.08. Rerun the arithmetic and per-share value falls from **$27.50 to $23.41 — a 14.9% drop
from one percentage point.** If your prediction had the direction right but the size shocked
you, that *is* the lesson: this model's conclusion is hostage to the discount rate, which is
exactly what you tell a committee when you present a range instead of a point.

## Step 7 — One change at a time is not enough: the sensitivity grid

WACC and terminal growth are the two assumptions the value is most hostage to, and they get
argued about together. So vary them together. Hold the five FCFF forecasts fixed and recompute
per-share value at each combination. Here is the training case's grid — **these are the digits
your Lab 06 training grid must reproduce**:

**Value per diluted share ($)**

| WACC (rows) / terminal growth (columns) | g = 2% | g = 3% | g = 4% |
|---|---:|---:|---:|
| **WACC = 9%** | 28.60 | 32.94 | 39.02 |
| **WACC = 10%** | 24.36 | **27.50** | 31.69 |
| **WACC = 11%** | 21.06 | 23.41 | 26.44 |

The base case sits in the middle at $27.50, exactly where Step 5 left it. That is your first
check that the grid is real and not decoration.

Read it the way a committee reads it, in three moves:

1. **Direction.** Value falls as you go down (higher WACC) and rises as you go right (higher
   g). Every cell obeys that. A grid that breaks the pattern has a bug, not an insight.
2. **Asymmetry.** The corners are not equally far from the middle. Down-left (WACC 11%, g 2%)
   is $21.06, **23% below** base. Up-right (WACC 9%, g 4%) is $39.02, **42% above**. The upside
   corner moves more because the terminal denominator, WACC − g, is being squeezed from both
   sides at once — from 0.07 down to 0.05.
3. **The range, not the middle.** This grid says the defensible range is roughly $21 to $39
   under assumptions a reasonable person could hold. That is the honest output. "The stock is
   worth $27.50" is not.

If you widen the grid, `g < WACC` must still hold in every cell. A cell where g ≥ WACC is not a
low number — it is not a number at all, and it should be marked invalid rather than valued.

## Step 8 — Reverse DCF: what is the market already assuming?

A forward DCF asks *what is it worth?* A reverse DCF asks the more useful question: *what would
I have to believe to justify today's price?* You do not argue with a price. You find out what it
assumes, then decide whether you believe that.

Mechanically you freeze everything except one named assumption, and solve for the value of that
assumption which makes the model's output equal the observed price.

**Worked, with digits.** Suppose the shares trade at **$30.00**. Our base case says $27.50, so
the market is more optimistic than we are — but about *what*? Freeze WACC at 10%, terminal
growth at 3%, and cash, debt and share count as given. Solve for a single **additive shift
applied to all five explicit growth rates**. The answer:

> Shift = **+1.78 percentage points**, turning the growth path 8%, 6%, 5%, 4%, 3% into
> **9.78%, 7.78%, 6.78%, 5.78%, 4.78%** — and that path prices the shares at exactly $30.00.

Now say what it means in a sentence a committee would accept: *"At $30, the market is paying
for roughly 1.8 points of extra growth in every one of the next five years, with no change to
the long-run rate or the discount rate. Do I believe this business has 1.8 points more growth
in it than my forecast does?"* That is a researchable question. "The stock looks expensive" is
not.

Three cautions, all of which Lab 06 checks:

- **The answer is conditional on what you froze.** A different frozen WACC gives a different
  implied growth. Always report the solved variable *and* the held-fixed list. "Implied growth"
  with no held-fixed list is ambiguous.
- **It is not proof of mispricing.** The market may be assuming something else entirely — a
  better margin, a lower cost of capital, an acquisition. You have found *one* set of
  assumptions consistent with the price, not *the* set.
- **Some prices are unreachable.** Search shifts between minus two and plus two percentage
  points and you only reach **$24.87 to $30.32**. So ask what shift justifies **$45.00** and the
  honest answer is *no solution in the range searched* — not the nearest edge of the range. A
  solver that quietly returns its own boundary is lying to you. Test it: feed it your own base
  per-share value and it must return a shift of **0.00**. If it does not, the solver is wrong
  before you ask it anything interesting.

## Negative FCFF — when the company is losing money

A growth rate applied to a negative number makes the loss grow: at −100 and +8% the model says
−108 next year, and the terminal formula then capitalizes a loss forever. That is the model
being wrong, not the company. A loss-making company is valued on an **explicit path**: five FCFF
amounts, your forecast of when and how cash flow turns positive — management's guidance in the
MD&A, the company's own trajectory, or a stated assumption — each labelled as a forecast. Year 5
must be positive, because the terminal value stands on it.

*The shape, not your answer:* −120, −60, 0, 40, 90 (USD millions) — "turns positive in Year 3
per the MD&A's cost-program guidance; Years 4 and 5 are my assumption." On the training case's
bridge that path is worth about $9.94 a share; the level of Year 5 is what the value hinges on.

**Send this to your Lab 05 chat:**

> In my `dcf.py`, add an optional input at the top, `FCFF_PATH`: a list of five FCFF amounts in
> USD millions, empty by default. When it is filled in, use those five amounts as Years 1 to 5
> instead of growing the starting FCFF; everything after that — discounting, the terminal value
> on Year 5, the bridge, the twelve lines, the grid — stays exactly as it is. Stop with a clear
> message if Year 5 is not positive. For the reverse DCF, when `FCFF_PATH` is used, the solved
> variable is a uniform amount in USD millions added to all five values instead of a growth
> shift; search between the bounds I set at the top (start with −500 and +500).

**Check it on the training case first:** set `FCFF_PATH` to 108, 114.48, 120.204, 125.01216,
128.762525 — the training case's own path — and the twelve lines must match the known answer
exactly. Then put your own path in. For the reverse DCF, the solved variable becomes the uniform
amount added to your path; on the training case at $30.00 with the loss-maker shape above it
solves at about +77.6 million a year, which says the market is paying for a Year 5 of about
168, not 90.

## Reasonableness bands — a desk reference

Adapted from the course's prior-term materials. These are *smell tests*, not rules: a value
outside a band demands a written justification, not automatic rejection.

| Quantity | Ordinary band | Outside it, ask |
|---|---|---|
| Terminal growth g | ≤ 2–3% (long-run nominal GDP; FRED series `A191RL1Q225SBEA` for the US history) | What lets this company outgrow the economy forever? |
| TV share of EV | 50–80% *at a five-year explicit window* | Above 80%: is the window too short for the fade, or is WACC − g squeezed? |
| WACC | ~8–12% for typical operating companies | Below 6% or above 15%: re-check every input; is cost of equity > cost of debt? |
| Revenue growth path | fades toward industry/economy | Does the growth story match the reinvestment the model shows? |

Our training case sits inside every band (g = 3%, TV share 72.4% on a five-year window, WACC
10%, fading growth) — which is exactly why it makes a clean known answer.

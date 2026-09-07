<!-- AUTHORED HOME. Built under the 2026-09-06 rulings in OWNER-DECISION-GATES.md (Desktop VS Code;
     instruction, not materials; no offline route; one thing per lab; not our business; reverse DCF
     practised on the training case, submitted on the company; voice). -->

# Lab 06 — Sensitivity, Reverse DCF, and Conditional Recommendation

**One thing today: your company through the model — what it is worth, and what the price already assumes.**

**Category:** Thursday merit checkout; anchors below.

**You arrive with:** `dcf.py` matching the twelve known answers · your filing, open · your Lab 05
AI chat · your WACC prediction · what you learned about Reversed DCF.

## Reopen and rerun

1. **VS Code → File → Open Recent** → your Course/Work Folder.
2. **Terminal → New Terminal.**
3. `python dcf.py`. *Expect:* the same twelve numbers as Tuesday. If not, debug with your AI until
   they match.

## R — your company's five rows, each with a source

Start here: [SEC EDGAR full-text search](https://www.sec.gov/edgar/search/) → the company →
latest **10-K** → `Ctrl+F` (`Cmd+F` on macOS) the phrases below.

| Input | Training value | Where yours comes from |
|---|---|---|
| Starting FCFF | 100 | **Consolidated Statements of Cash Flows**: operating cash flow + after-tax interest paid − capital expenditure. A vendor's "free cash flow" is often not FCFF |
| Growth, Years 1–5 | 8%, 6%, 5%, 4%, 3% | **Item 7, MD&A** and the company's own recent history; a forecast, labelled as one |
| WACC | 10% — never copy it | a brief `estimate`: cost of equity ≈ risk-free rate + beta × 5%; cost of debt ≈ debt-note rate × (1 − tax rate); weight by market value. Or `unresolved` |
| Terminal growth | 3% | the long-run economy, not the company |
| Cash · debt · diluted shares | 50 · 300 · 50 | balance sheet; debt note; the EPS note's **diluted weighted-average shares** (the cover-page count is basic shares) |

Every row: value, unit, as-of date, exact locator. Plus **today's share price with date and time**
— the target for the reverse DCF.

A row you cannot source stays `unresolved`. A labelled `estimate` or `placeholder` counts. An
invented number does not.

**Loss-making company (negative FCFF)?** A growth rate on a loss grows the loss. Use an explicit
five-year FCFF path — worked example, section **Negative FCFF**.

## I — your company through the model

1. Right-click your folder → **New File** → any name ending in `.md`. Put your table and the
   price in it.
2. Put your numbers in the inputs block of `dcf.py`. An unresolved row keeps the training value,
   marked `placeholder`. Save.
3. `python dcf.py`. *Expect:* twelve lines for your company.

## V — reasonableness

Your value per share beside today's price. Inside 0.5× to 2×: say so. Outside: do not adjust
anything; name the one input you distrust most, and why.

## E — the grid and the reverse DCF, from one message

*Training case, value per diluted share ($):*

| WACC \ terminal growth | 2% | 3% | 4% |
|---|---:|---:|---:|
| **9%** | 28.60 | 32.94 | 39.02 |
| **10%** | 24.36 | **27.50** | 31.69 |
| **11%** | 21.06 | 23.41 | 26.44 |

Base case in the middle cell; value falls going down and rises going right; the corners are the
answer, not the middle. Reverse DCF on the training case at $30.00: about **+1.78 points** on
every growth rate, holding WACC, terminal growth and the bridge fixed.

Send this to your Lab 05 chat:

> In my `dcf.py`, keep the inputs block and the twelve printed lines exactly as they are —
> they must still match the known answer afterwards. Add a sensitivity grid: value per diluted
> share for every combination of the WACC values and terminal-growth values I list in two
> editable lists at the top (start with WACC 0.09, 0.10, 0.11 and terminal growth 0.02, 0.03,
> 0.04), holding every other input fixed; mark any cell where terminal growth is greater than
> or equal to WACC as invalid rather than valuing it. Print the grid as a table I can read in
> the terminal, underneath the twelve lines. Then add a reverse DCF: given a target share price
> I set at the top, solve for one number I name — start with a uniform shift added to all five
> explicit growth rates — that makes value per share equal that price, holding everything else
> fixed, and print the solved number with the list of inputs held fixed. One file, one command
> — `python dcf.py` prints all three blocks. Do not create a second script.

> For the reverse DCF, search by bisection between the lower and upper bounds I set at the top
> (start with −5 and +10 percentage points); refuse any bracket that pushes an annual growth
> rate to −100% or below. If the target price cannot be reached inside those bounds, report no
> solution in that bracket — never return a bound as if it were the answer. Print the solved
> shift, the target price, and the list of inputs held fixed, so one command still shows me
> everything.

Copy only the code it returns, paste it over `dcf.py`, save, run.

1. **Training case first:** training inputs, target `30.00`. *Expect:* the grid matches the table
   cell for cell; the shift reads about +1.78. If not, debug with your AI until they match.
2. **Your company:** your inputs, target = today's price. *Expect:* your grid and your shift.
   Inputs unresolved? Keep the training result and label it training.

Report the shift with what you held fixed. It is one set of assumptions consistent with the
price, not proof of mispricing.

## Your conditional call

"Initiate if …; otherwise …", plus one thing to monitor. *Example:* "Watch-defer. Initiate if the
growth the price demands drops below my forecast path — a price below about $27.50, or a sourced
reason to raise my growth path two points. Monitor: operating margin next quarter."

## Floor

Your inputs, sourced; your company's value; the grid and the growth the price assumes; your
conditional call. You submit individually. Depth, after class: the
[open challenge page](open-ended-challenge.md).

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

## Merit anchors — five criteria, 5 points each, for reference only

**4** = one minor weakness; **2** = an important link incomplete; **1** = minimal; **0** = missing
or fabricated. Do not double-deduct one defect.

| Criterion | 5 | 3 | 0–1 |
|---|---|---|---|
| Grid and direction | base case in the centre; direction holds; the range read off the corners | grid correct, reported as a table not a range | wrong centre or direction unchecked |
| Reverse DCF | solved variable and held-fixed list stated; training shift reproduced before the company run | number present, held-fixed list thin or practice skipped | quoted with no conditions, or as proof of mispricing |
| Inputs and sources | every row has a locator and an as-of date; unresolved, placeholder and estimate labelled | mostly sourced, one gap | unsourced, or training output presented as the company's |
| Reasonableness | value beside price, band stated, distrusted input named with a reason | comparison present, no input named | none, or the model adjusted to fit the price |
| The conditional call | a real call, a condition that flips it, something to monitor | vague or unmeasurable condition | a point estimate, or no condition |

**Next week:** another company's market valuation tests whether your DCF assumptions survive a
comparison.

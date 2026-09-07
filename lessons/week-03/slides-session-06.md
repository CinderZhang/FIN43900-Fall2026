# Session 6 — What Has to Be True
> **One thing today: your company through the model — what it is worth, and what the price
> already assumes.**

---

## Today's run of show

1. Reopen, rerun
2. **R** five sourced rows
3. **I** your numbers in; **quiz when told**
4. **V** reasonableness
5. **E** grid + reverse DCF
6. Conditional call; floor
7. Temperature check
8. Checkout — GitHub

[Lab 06](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-06-sensitivity-and-reverse-dcf.md)

---

## Reopen and rerun

1. **VS Code → File → Open Recent** → your Course/Work Folder.
2. **Terminal → New Terminal.**
3. `python dcf.py`. **Expect:** Tuesday's twelve numbers; debug until they match.

Resume Tuesday's chat. 90 seconds each way: the input hardest to find.

---

## R — five rows, each sourced

[SEC EDGAR](https://www.sec.gov/edgar/search/) → the company → latest **10-K** → `Ctrl+F` the
phrases below. **Expect:** the statement or note heading on screen.

| Input | Training value | Where yours comes from |
|---|---|---|
| Starting FCFF | 100 | **Cash Flow Statement**: operating cash flow + after-tax interest − capex |
| Growth, Years 1–5 | 8%, 6%, 5%, 4%, 3% | **Item 7, MD&A** plus recent history; a forecast |
| WACC | 10% — never copy it | a brief `estimate`, below — or `unresolved` |
| Terminal growth | 3% | the long-run economy, not the company |
| Cash · debt · shares | 50 · 300 · 50 | balance sheet; debt note; EPS note's **diluted weighted-average shares** |

Every row: value, unit, as-of date, locator. Plus **today's price with date and time** — the
reverse DCF's target. Unsourced stays `unresolved`.

**WACC once:** 4.5% + 1.3 × 5% = 11% equity; 6% × (1 − 0.25) = 4.5% debt; 85/15 → about **10%**.

**Negative FCFF?** Growth on a loss grows the loss — use an explicit five-year path.

---

## I — your company through the model

1. **New File** → any name ending in `.md`. Put your table and the price in it.
2. Your numbers into `dcf.py`'s inputs block; an unresolved row keeps the training value, marked
   `placeholder`. Save.
3. `python dcf.py`. **Expect:** twelve lines for your company.

---

## V — reasonableness

Your value per share beside today's price. Inside 0.5×–2×: say so. Outside: adjust nothing; name
the input you distrust most, and why.

---

## E — grid and reverse DCF, one message

*Training case, $/share:*

| WACC \ terminal growth | 2% | 3% | 4% |
|---|---:|---:|---:|
| **9%** | 28.60 | 32.94 | 39.02 |
| **10%** | 24.36 | **27.50** | 31.69 |
| **11%** | 21.06 | 23.41 | 26.44 |

Base case centre; falls down, rises right; read the corners. Reverse DCF at $30.00: about
**+1.78 points** on every growth rate.

Send this, then predict your grid's furthest corner:

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

Paste only the code over `dcf.py`, save, run.

1. **Training first:** training inputs, target `30.00`. **Expect:** grid matches above, shift
   about +1.78.
2. **Your company:** your inputs, target = today's price. **Expect:** your grid and shift.
   Unresolved? Label the training result training.

Report the shift with what you held fixed — not proof of mispricing.

---

## Conditional call — and the floor

"Initiate if …; otherwise …", plus one thing to monitor.

*Example:* "Watch-defer. Initiate if the growth the price demands drops below my forecast path —
a price below about $27.50, or a sourced reason to raise my growth path two points. Monitor:
operating margin next quarter."

**Floor:** your inputs, sourced; your company's value; the grid and the growth the price
assumes; your conditional call.

Depth after class:
[open challenge page](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/open-ended-challenge.md).

---

## Temperature check

Anonymous, ungraded: what works, what confuses, one change.

---

## Checkout — on GitHub

**Brightspace → Quizzes → Lab 06.**

**GitHub links of your files: md, py and/or other files as needed.**

Anchors on the lab page: grid · reverse DCF · sources · reasonableness · call.

**Next week:** peer selection — freeze your policy before you ask AI.

<!-- AUTHORED HOME. Built under the 2026-09-06 rulings in OWNER-DECISION-GATES.md (Desktop VS Code;
     instruction, not materials; no offline route; one thing per lab; not our business; voice) and
     Gate 7 (pro-forma is a method, not an algorithm; the training case is ABG; two-person teams). -->

# Lab 09 — Pro-Forma Build: the Engine and the Known Answer

**One thing today: build the three-statement engine from the instruction, and prove it on the ABG case.**

**Category:** Tuesday completion checkout, **25 or 0**.


**You arrive with:** your Course/Work Folder · your Week 3 chat · Part 1 of the video watched · your
note on the three judgments · a partner (new this week).

## Open your workspace

1. **VS Code → File → Open Recent** → your Course/Work Folder.
2. **Terminal → New Terminal.**
3. `python dcf.py`. *Expect:* your Week 3 values. If not, debug with your AI until they print.

No folder yet? See previous lab instructions. Nothing from the course goes on your machine: read
the course on GitHub, build in your folder.

**AI partner:** the **Google Antigravity** extension or any AI in a browser tab. Nothing graded
needs an extension or an account.

**Something not working?** Debug with your AI: paste the exact command and the exact error text.

## D — the question, the same for everyone

> **What are five years of a company's statements worth, built from assumptions you can defend,
and how do you know the statements are right?**

Paste it into your chat. Today the company is Asbury (ABG), the case from the video. Thursday it
is yours.

**Explain to your partner first** (five minutes, no screen): the three judgments that carry the
ABG value, and why cash is the last line the model computes. Then swap roles.

## R — the assumption set (from Part 1; the three history ratios are written as the arithmetic that makes them, so your AI uses the exact figure)

| Assumption | ABG value | Label |
|---|---|---|
| Organic revenue growth | 1.8% a year | judgment |
| Gross margin | 17.05% | judgment |
| SG&A ÷ gross profit, 2026 → 2030 | 66.5%, 65.5%, 64.5%, 64.5%, 64.5% | judgment |
| Depreciation ÷ opening PP&E | 82.4 ÷ 3,070.4 (FY2025 depreciation ÷ year-end PP&E) | history |
| Impairment, non-cash | 120 a year | judgment |
| Capital spending | 250 a year | guidance |
| Tax rate | 25.5% | judgment |
| Inventory days | 2,135.8 ÷ (17,999.0 − 3,071.7) × 365 (FY2025 inventory ÷ cost of sales) | history |
| Inventory loans (floor plan) ÷ inventory | 2,027.0 ÷ 2,135.8 (FY2025) | history |
| Other working capital | 0.8% of the change in revenue | judgment |
| Minimum cash / revolver limit / revolver rate | 25 / 850 / 6% | history / judgment / judgment |
| Debt repayment / share buyback | 150 / 150 a year | judgment |
| Interest: floor plan / term debt | 4.67% / 5.44% | history |
| Cost of equity / terminal growth | 10% / 2.5% | judgment |
| Shares outstanding | 17.951349 million | fact (10-Q, 30 June 2026) |

Opening balance sheet, FY2025 (USD millions): revenue 17,999.0 · inventory 2,135.8 · PP&E 3,070.4 ·
other assets 6,371.6 · cash 40.4 · floor plan 2,027.0 · term debt 3,572.0 · other liabilities
2,127.5 · equity 3,891.7.

## I — build the engine from the instruction

1. **VS Code → New File** → `proforma.py`, in your open folder.
2. Send this request to your AI, word for word, then paste the assumption table and the opening
   balance sheet from above under it:

   > Write a single Python file, standard library only, that projects five years (2026 to 2030)
   > of income statement, balance sheet and cash flow for a company from an opening balance sheet
   > and the assumptions I paste below. Compute in this order each year: revenue = prior × (1 +
   > growth); gross profit = revenue × gross margin; SG&A = gross profit × that year's ratio;
   > depreciation = opening PP&E × ratio; impairment as given; operating income = gross profit −
   > SG&A − depreciation − impairment; interest = opening floor plan × its rate + opening debt ×
   > its rate + opening revolver × its rate; tax = max(0, pretax) × rate; net income. Then the
   > balance sheet except cash: inventory = (revenue − gross profit) × days ÷ 365; floor plan =
   > inventory × ratio; PP&E = opening + capex − depreciation; other assets = opening + 0.8% × change
   > in revenue − impairment; debt = opening − repayment; other liabilities flat; equity = opening +
   > net income − buyback. Then free cash flow to equity = net income + depreciation + impairment −
   > capex − change in inventory − change in other working capital + change in floor plan −
   > repayment. Cash = opening cash + FCFE − buyback, drawing a revolver only if cash would fall
   > below the minimum, repaying it first when cash is above the minimum. Print each statement as
   > a table with years across, one decimal. After every year compute the checks: assets minus
   > liabilities minus equity, and cash at or above the minimum; print them. Write a function
   > assert_balanced that raises an error naming the year and the gap if any check fails, and
   > call it before the valuation. Value the equity as the present value at the cost of equity of
   > the five FCFE, plus a terminal value equal to (2030 FCFE + the 2030 repayment) × (1 + terminal
   > growth) ÷ (cost of equity − terminal growth), discounted five years; divide by the share count.
   > Print equity value, the share of value after 2030, and value per share to two decimals.

3. Copy only the code into `proforma.py`. Save.
4. Run `python proforma.py`. *Expect:* three statements, a check block, and a value per share.
   If it errors, paste the error into the chat and run again.

## V — prove it on the known answer

| Line | FY2026E | FY2030E |
|---|---|---|
| Revenue | 18,323.0 | 19,678.3 |
| Operating income | 844.2 | 971.4 |
| Net income | 413.6 | 527.5 |
| Free cash flow to equity | 211.4 | 342.3 |
| Cash, year end | 101.8 | 719.8 |
| Assets − liabilities − equity | 0.0 | 0.0 |
| Value per share | **$291.75** | |

Match to the decimal, or the model is wrong: debug with your AI until they match. The share of
value after 2030 should read about 80%.

**Swap and break.** Run your partner's `proforma.py`. *Expect:* the same values. Then, in your
partner's file, set 2026 cash to the opening 40.4 instead of the computed figure and run it.
*Expect:* the model refuses, naming FY2026E and a gap of −61.4 — the year's change in cash with the
sign flipped. Undo the change. A model that does not refuse has not been checked.

## Floor

Your engine reproduces the ABG value and refuses the broken balance sheet. You submit individually.

## Floor plan — Learn on your own

1. What is it (inventory loans from manufacturers' finance arms and banks)? 2. How does it work
(rises with inventory; interest on the opening balance; inside FCFE as operating)? 3. Explain to your
partner why removing the line sends cash to about −1.1 billion in the video.

## Reflect

Explain to your partner: 1. why the model computes cash last; 2. what the −61.4 tells you before
you open a single cell.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

**Thursday preview:** your company's filings become the assumption set; the engine stays the same.

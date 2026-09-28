<!-- AUTHORED HOME. Scope: OWNER-DECISION-GATES.md, Week 6 sensitivity ruling, 2026-09-28. -->

# Lab 11 — Pro-Forma Sensitivity: Find Your Company's Drivers

**One thing today: find which inputs move your own pro-forma's results, and by how much.**

<!-- Category scale generated from SIMPLE-SYLLABUS-COMPONENTS.md; category consistency checked by lesson_quality_audit.py. -->
**Category:** Tuesday completion checkout, **25 or 0**. Dates and points: Brightspace and the course schedule.

**You arrive with:** your company's working pro-forma from Lab 10, its assumption table,
and the same AI chat. Read the [worked sensitivity example](student-handout.md) before class.

## Open your workspace

1. **VS Code → File → Open Recent** → your Course/Work Folder; **Terminal → New Terminal**.
2. Run your company model using the command from Lab 10. Save its base inputs and visible output.
   *Expect:* the same forecast and passing accounting checks as your last run.
3. With your partner, name the input you expect to matter most and explain why. Write down
   any gap in your understanding before asking AI. *Expect:* your prediction, not AI's ranking.

**Something not working?** Debug with your AI: paste the exact command and exact error text.

## D — the question, the same for everyone

> **Which assumptions drive my company's forecast and value, and what explains their effects?**

Paste this into your resumed chat. Work on your own company throughout.

## R — choose the inputs and the comparison

1. Choose **two operating drivers already in your model**: for example, revenue growth and
   operating margin, or a company-specific volume, price, cost, or reinvestment driver.
   Choose independent inputs from your assumption table, not calculated statement totals.
   *Expect:* inputs you can locate and explain, not copied ABG assumptions.
2. For each driver, record its base, lower and higher values, units, affected forecast years,
   and the reason for the range. For a multi-year path, list the values by year or specify
   the same percentage-point shift to each affected year. Use your company's history or a labelled judgment.
   A percentage point is different from a percent change; money uses your model's currency
   and scale. *Expect:* a range a partner can reproduce.
3. Use the same outputs for every run: **final-year operating profit, final-year free cash
   flow, and value per share if your model supports a defensible valuation**. State FCFF or
   FCFE consistently with your model. *Expect:* comparable results with units.

If your cash flow is negative or valuation is unresolved, keep the signed cash flows and
analyze operating profit and free cash flow. Mark value per share unavailable and explain why;
do not discard negative years or invent a terminal value. The same sensitivity task applies.

Before running a change, close AI and save one prediction with a timestamp or Git commit:
input old → new with units, expected output direction and rough size, and why. This is your
Locked Changed-Input Record. Your partner reads it before you run.

## I — add sensitivity analysis to your own model

Send this request with your model and the input ranges available in the resumed chat:

> Add one-at-a-time sensitivity analysis to my existing company pro-forma. Preserve a separate
> base input set, with a fresh independent copy for every run. For each of my two drivers,
> rerun the entire linked model at its lower,
> base and higher values, changing only that driver in the specified years. Reset all other
> independent assumptions to base before every run; let linked accounting quantities
> recalculate. Show actual input values and units, final-year operating profit, final-year
> free cash flow with its FCFF or FCFE label, and value per share only if the existing
> valuation is valid. Report signed changes from base in output units and each output span
> (maximum minus minimum across valid lower/base/higher results). Retain the statement details
> needed to trace a selected result. Keep the accounting
> checks visible and flag invalid runs instead of ranking them. If valuation is unavailable,
> retain signed cash flows and explain the limitation. Restore the base and rerun it at the
> end. Do not generate company data, choose new ranges, or write my interpretation for me.

Keep your working Lab 10 model. Save the added analysis in your open folder and run it from the terminal.
*Expect:* your company's lower/base/higher results and a restored base that matches the first run.
While AI works, explain your predicted input → statement → output link to your partner.

## V — check the result

| Check | Expected result |
|---|---|
| Base before and after the analysis | Same inputs and outputs, within stated rounding tolerance |
| Lower or higher run | Only the selected independent input changed; linked quantities recalculated |
| Accounting checks | Pass on each usable run; failures labelled and investigated |
| Change from base | Recomputes as changed output minus base output |

Pick one changed result, trace it through the statements, and recompute its difference from
base yourself. Add the actual result and an explanation of any prediction error to your
locked record. State whether the result changes your valuation conclusion or research priority,
and why (including a no-change reason). *Expect:* a result you understand, not just a table that prints.

## E — find the driver

Compare the output spans over your stated input ranges. Identify the larger driver for
operating profit and free cash flow, and for value if available. Say **"over these ranges"**:
a bigger span can reflect a wider input range, not an inherently more important driver.
Explain one causal link using your actual results. *Expect:* a qualified ranking with numbers.

## Floor

Your own company's sensitivity table for two operating drivers, a passing restored-base check,
one reconciled locked prediction, and a short explanation of the main driver over the tested
ranges. Include visible output so a reader need not run your code. You submit individually.

## Sensitivity — Learn on your own

1. What is one-at-a-time sensitivity? 2. How does the chosen input range affect the ranking?
3. Explain why a sensitivity table is not a forecast probability.

## Reflect

Explain to your partner: which driver mattered most over your ranges, and which result surprised you.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

**Thursday preview:** investigate why the drivers matter and whether your conclusion depends on the ranges.

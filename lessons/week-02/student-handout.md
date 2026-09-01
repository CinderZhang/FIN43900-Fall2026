# Week 2 Student Handout — Valuation Contract and Evidence Ledger

## Why this week matters

Before anyone trusts your valuation, they check whether they can trust your *numbers* — where
each one came from, what it means, and what you did to it. That discipline has a desk name:
data integrity, and it is the first thing a senior analyst audits in a junior's model, because
it is where models actually fail. This week you set the contract for your Project 1 target —
what exactly is being valued, in what unit, from which sources — and you capture your own
before-AI baseline, which is the evidence that the judgment in this project is yours. None of
this is busywork: it is the difference between a model someone will put money behind and a
spreadsheet with confident formatting.

## Start with the object being valued

| Output | Meaning | Common error |
|---|---|---|
| Enterprise value | value of operating assets available to all capital providers | comparing directly with common-share market capitalization |
| Equity value | residual value attributable to common equity after the bridge | subtracting debt but forgetting cash or other claims |
| Per-share value | equity value divided by the stated diluted share convention | mixing basic, diluted, and current share counts |

Generic bridge:

`Equity value = Enterprise value + non-operating assets − debt − debt-like claims − non-common claims`

`Per-share value = Equity value / diluted common shares`

The exact bridge is company-specific. Label every included or excluded item and its date.

## FCFF architecture

One common operating formulation is:

`FCFF = EBIT × (1 − tax rate) + D&A − capital expenditures − change in operating NWC`

This is an architecture, not permission to copy standardized fields. Verify sign, period,
currency, units, tax convention, operating/non-operating classification, and whether each input
is reported, normalized, forecast, or calculated.

**Worked once, with digits** — the Week 2 mini case (`starter/mini_case.csv`), which
`starter/valuation_foundations_starter.py` validates when you run it (in Colab: upload both
files, press Run; the checks print PASS or the first failing line):

> FCFF = 150 × (1 − 0.25) + 40 − 60 − 15 = 112.5 + 40 − 60 − 15 = **77.5** ($M)

Read the economics off the arithmetic: the business earned 112.5 after tax on operations,
non-cash depreciation of 40 comes back, and then real money left the building — 60 reinvested
in equipment and 15 tied up funding growth in receivables and inventory. FCFF is what remained
for *all* capital providers. Now the bridge, same case:

> Equity value = 1,000 + 100 − 250 − 20 − 10 = **820** → 820 / 100 diluted shares = **$8.20**

Each subtraction is a claim that stands in line ahead of you: debt (250), the minority owners
of a consolidated subsidiary (20), the unfunded pension promise (10). The 100 of non-operating
cash is added because the enterprise value of 1,000 never counted it. Five rows here; on your
real target every row must carry a source and an as-of date in the evidence ledger below —
that is the entire point of this week.

## Source hierarchy

Use the most authoritative evidence available for the claim:

1. filed financial statements and notes;
2. reconciled company disclosures with definitions;
3. authoritative economic/market series and documented provider fields;
4. standardized APIs or aggregators used with reconciliation; and
5. AI-generated summaries used only as leads until independently verified.

Two sources can share a label and measure different objects. Do not average a discrepancy
before explaining it.

## The contamination catalog — know what poisons a number

A **contamination** is any input that would silently make your valuation wrong if you carried
it forward as a clean fact. Lab 04 asks you to find and correct one plausible contamination in
your own ledger before Week 3 turns these inputs into a DCF. Contaminations come in two
kinds, and professionals hunt both.

### Mechanical contamination — wrong numbers that look right

Nothing unusual happened at the company; the defect is in your pipeline. Units and scale
(thousands vs millions), period (fiscal year vs trailing-twelve-months vs calendar), currency,
basic vs diluted share counts, a provider's label measuring something different from the
filing's definition (Week 1's PEG lesson), or missing data silently filled. Thursday's
injected-defect exercise is mechanical-contamination practice: the code runs perfectly, the
number is plausible, and the model is wrong. **Remedy: correct it at the source** — there is
a right answer.

### Economic contamination — honest numbers that poison a forecast

Nothing is misreported: the filing is correct, audited, and public. The number still cannot
enter your forecast unlabeled. This is exactly what your ledger's `normalization`
classification exists for, and it splits into two groups with different remedies. Every case
below is real; every link is a public filing or primary source you can open.

#### One-time items — the event will not repeat

| Contamination | What it looks like | A real, public case | If you carry it in unlabeled |
|---|---|---|---|
| **One-time expense** | impairment or write-down, restructuring charge, litigation settlement | Kraft Heinz took a combined **$15.4B impairment of goodwill and the Kraft and Oscar Mayer trademarks** in Q4 2018 — the quarter swung to a $12.6B loss ([earnings release](https://www.sec.gov/Archives/edgar/data/1637459/000163745919000010/ex991-erq42018.htm) · [FY2018 10-K](https://www.sec.gov/Archives/edgar/data/1637459/000163745919000049/form10-k2018.htm)) | your base-year EBIT starts in a hole that will not repeat; every margin and growth rate built off that base is fiction |
| **One-time income** | gain on selling a business or marking an investment to a higher price; a tax valuation-allowance release *(a valuation allowance is a reserve saying "we may never get to use our accumulated tax losses"; releasing it books those future savings as one large non-cash gain, all at once)* | Tesla's FY2023 net income includes a **$5.9B one-time non-cash tax benefit** from releasing its valuation allowance ([FY2023 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/tsla-20231231.htm)). Ford's Q4 2021 net income includes an **$8.2B fair-value gain on its Rivian shares** after Rivian's IPO — equity stakes like this are re-marked through net income, and Rivian's share-price decline produced large fair-value losses in 2022 ([FY2021 10-K](https://www.sec.gov/Archives/edgar/data/37996/000003799622000013/f-20211231.htm)) | net income looks like a step-change in earning power; an effective tax rate or margin estimated on that year inherits a never-again event |

**The one-time-item test:** *will this item, at roughly this size, be in next year's number?*
If not, take it out of your base year with a labeled `normalization` row — or keep it and
explicitly qualify the row — and cite the **filing note**, not the summary income-statement
line. Record the direction: did the item flatter income or punish it? Both happen, and both
mislead.

#### Basis changes — the measuring stick changed, and future numbers stay on the new basis

| Contamination | What it looks like | A real, public case | If you carry it in unlabeled |
|---|---|---|---|
| **Change in accounting estimate** | useful lives lengthened or shortened: depreciation shifts, prospectively (no restatement), because management revised how fast the asset's value is consumed | Amazon lengthened server lives 5→6 years effective 2024 (**depreciation −$3.2B**), then shortened a subset back 6→5 effective 2025 because AI-era hardware ages faster (**operating income −$0.7B**) ([FY2024 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm)). Microsoft's 4→6 change added **$3.7B to FY2023 operating income** ([FY2023 10-K](https://www.sec.gov/Archives/edgar/data/789019/000095017023035122/msft-20230630.htm)) | EBIT and margins move in either direction without any current-period operating event, and this year's margin is no longer comparable to last year's; a forecast that silently mixes the two bases mis-reads both |
| **Change in accounting principle** | switching methods — e.g., last-in-first-out (**LIFO**) to first-in-first-out (**FIFO**) or average-cost inventory costing; generally applied retrospectively (prior periods recast when practicable) | Arconic switched inventory costing from LIFO to average cost in Q3 2020; its auditor's formal concurrence that the new method is preferable is filed publicly as [Exhibit 18](https://www.sec.gov/Archives/edgar/data/1790982/000179098220000163/arnc20200930exhibit18.htm) (a "preferability letter") | numbers you pulled from older filings or providers may sit on the old basis while current ones sit on the new — margins shift with no economics behind them |
| **Standards change (hits everyone at once)** | a new accounting rule moves items for every company on the same date — e.g., leases ([ASC Topic 842](https://storage.fasb.org/ASU%202016-02_Section%20A.pdf); ASC = the FASB's Accounting Standards Codification, US GAAP's rulebook) put operating-lease right-of-use assets and lease liabilities on the balance sheet starting in 2019 | every 10-K straddling 2019 | balance-sheet and leverage comparisons break across the boundary year; and if you treat lease liabilities as debt-like in your bridge, your FCFF must treat lease payments consistently — pick one lease policy and label it |
| **Classification and "adjusted" games** | recurring costs excluded from "adjusted EBITDA"; ordinary operating expense presented as "special items" | the SEC polices exactly this — read its [non-GAAP Compliance & Disclosure Interpretations](https://www.sec.gov/divisions/corpfin/guidance/nongaapinterp.htm) | you value earnings the company never actually produces |

**The basis-change test:** *is this year measured on the same basis as the years I am
comparing it to or forecasting from?* If not, do **not** simply delete the change — the new
basis is often management's best current estimate (Amazon's shortening reflects real AI-era
hardware consumption). Instead: reconcile the two bases in a `normalization` row, choose
which basis your forecast uses, and say why. The sin is silently mixing bases across years.

**And one rarer case: error correction / restatement.** Here the original filing *was*
wrong — Kraft Heinz also restated FY2016–2017 after SEC subpoenas (same
[FY2018 10-K](https://www.sec.gov/Archives/edgar/data/1637459/000163745919000049/form10-k2018.htm)).
If any number in your ledger came from a filing that was later restated, it was never a fact:
rebuild the row from the restated filing and note the swap.

### Where professionals learn this

The CFA Program tests this material directly, and these sources are publicly readable:

- CFA Institute, [Financial Reporting Quality](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/financial-reporting-quality) (Level I refresher reading) — the taxonomy above, formalized: conservative vs aggressive choices, non-recurring items, classification shifting.
- CFA Institute, [Evaluating Quality of Financial Reports](https://www.cfainstitute.org/en/membership/professional-development/refresher-readings/evaluating-quality-financial-reports) (Level II refresher reading) — the quality-assessment workflow an analyst runs on a real filing.
- Damodaran, [*Measuring Earnings*](https://pages.stern.nyu.edu/~adamodar/pdfiles/valn2ed/ch9.pdf) (Investment Valuation, ch. 9, free PDF) — normalization specifically for valuation, the use we make of it this week.
- SEC Division of Corporation Finance, [non-GAAP C&DIs](https://www.sec.gov/divisions/corpfin/guidance/nongaapinterp.htm) — where "adjusted" presentation crosses the line.

## This week's working steps

### Evidence ledger fields

| Field | Required content |
|---|---|
| item | precise financial concept |
| classification | reported fact / normalization / forecast assumption / calculated output |
| value and unit | value with currency, scale, ratio, or per-share unit |
| period/as-of date | fiscal period or market/valuation date |
| primary source | filing/series/provider plus locator |
| rationale | why the value and treatment fit the decision |
| independent check | second calculation, source, or reconciliation |
| uncertainty/failure mode | what could make the row wrong |

### AI architecture comparison

After Edition A is submitted, give Codex and Gemini the same requirements. Ask each for a
model architecture and evidence schema—not a valuation conclusion.

| Material suggestion | Codex | Gemini | Accept/modify/reject | Finance reason/evidence |
|---|---|---|---|---|
| valuation object |  |  |  |  |
| FCFF construction |  |  |  |  |
| normalization |  |  |  |  |
| enterprise-equity bridge |  |  |  |  |
| validation tests |  |  |  |  |

Agreement is not validation. Arbitrate with the filing, definitions, finance logic, and known
answers.

### The learning track — your gap list

The comparison above takes a few minutes to generate, and you do not spend them watching.
While one AI track works *for* you on your company, a second works *on* you: you take the gap
list you wrote in Session 3 — every concept you marked "not yet" — and make an AI tutor you
until the gap closes. Running both at once is the working pattern of this course, not a
Week 2 exercise; every later module assumes you do it.

Pick your single biggest "not yet," open your other system, and ask for a quiz rather than an
explanation. The difference matters: an explanation you read feels like learning, while a
question you have to answer finds out whether it was.

> The shape, not your answer: "Quiz me on **why capex comes out of FCFF while D&A goes back
> in** — one question at a time. Don't give me the answer until I commit to one. Then correct
> me in two lines and ask the next. Keep going until I get three right in a row."

Commit to an answer before you are told, even when you expect it to be wrong — a correction
only sticks to an answer you actually committed to. This track is **ungraded and never
collected**: no checkout field, no screenshot, nobody reads it. Its only record is what you
can now explain with an example, which is the point.

### Readiness statement

End the week with three sentences:

1. **Ready:** the evidence/model element safe to carry into Week 3.
2. **Unsafe:** the unresolved item that could contaminate value.
3. **Next test:** the smallest check that can resolve it.

## Rules and receipts — Edition A (AI-off valuation baseline)

*This section is procedure, not teaching. Read it once, follow it exactly; it protects the
evidence that the judgment in Project 1 is yours.*

Preserve:

- decision and intended user;
- company, valuation date, and intended output unit;
- initial initiate/watch-defer/do-not-initiate thesis or neutral hypothesis for a committee with
  no current position;
- evidence already known with sources;
- most consequential assumptions;
- unknowns and uncertainties; and
- research/model/validation plan.

State which ordinary tools and sources you used. Attest that generative AI was not used to
write or analyze this Edition A. Do not overwrite it later; corrections become a dated
addendum while the original remains unchanged.

Submit Edition A to the **separate ungraded Project 1 Edition A assignment**. Record its first
successful receipt/attempt identifier in Lab 03. Do not attach a second copy to the droppable
lab checkout or treat the Lab 03 score as the baseline record. The AI architecture comparison
above begins only after Edition A is submitted.

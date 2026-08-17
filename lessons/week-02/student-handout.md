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

**Worked once, with digits** — the Week 2 mini case (`starter/mini_case.csv`), which your
starter validates:

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

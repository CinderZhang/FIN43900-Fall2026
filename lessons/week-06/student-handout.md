# Week 6 Student Handout — Find and Explain the Drivers

A base forecast gives one answer. Sensitivity analysis shows which assumptions carry that
answer and where better evidence could change your understanding. Both labs use your own pro-forma.

## Run and compare

| Action | Expect |
|---|---|
| Run your company model with the Lab 10 command | The saved base results and accounting checks |
| Run the sensitivity analysis added in Lab 11 | Lower/base/higher inputs and comparable outputs |
| Run the revised range in Lab 12 | A comparison with the same base and other driver's range |

The worksheets give the AI requests and own the completion floors:
[Lab 11](lab-11-proforma-what-if.md) and [Lab 12](lab-12-proforma-present.md).

## Worked example: one input at a time

*Generated numeric teaching example from the course's ABG reference model,
`instructor/week-05-proforma-reference/abg_case.json` and `method.py`; baseline regression
checks live in `test_proforma_reference.py`. Derived spans and differences below use the displayed rounded
outputs. ABG is a reading example; use your own company in the labs.*

The base uses gross margin of 17.05% and annual capital spending of $250 million. Test each
input across the forecast years, keeping all other independent inputs at base. Recalculate the
linked statements each time. Capital spending is an operating reinvestment input: it affects
cash directly and future depreciation through the asset balance.

| Independent input changed | Final-year operating profit ($m) | Final-year FCFE ($m) | Value ($/share) |
|---|---:|---:|---:|
| Base | 971.4 | 342.3 | 291.75 |
| Gross margin 16.05% | 901.5 | 289.3 | 256.1 |
| Gross margin 18.05% | 1041.3 | 395.3 | 327.4 |
| Annual capital spending $200m | 976.6 | 391.0 | 325.2 |
| Annual capital spending $300m | 966.2 | 293.6 | 258.3 |

FCFE means free cash flow to equity. If your model uses free cash flow to the firm (FCFF),
keep that definition throughout your comparisons.

**Units first.** Moving margin from 17.05% to 18.05% adds **one percentage point**, or 0.01
in decimal form. A 1% relative increase would instead produce 17.05% × 1.01 = 17.2205%.
Those are different inputs. Monetary changes need the model's currency and scale.

**Difference from base.** At the higher margin, final-year FCFE changes by
395.3 − 342.3 = **+$53.0m**. The signed difference tells you the direction as well as the size.

**Explain the link.** Higher gross margin raises gross profit at unchanged revenue. The model's
linked expenses and taxes also recalculate, leaving higher operating profit and FCFE. Lower
capital spending reduces the cash outflow directly and changes future depreciation; the model
must carry both effects through its statements. Trace the actual links in your own model.

## Which driver matters most?

An output span is the maximum valid output minus the minimum valid output across the lower,
base and higher runs, including the base. It is nonnegative; input order does not determine
which output is largest.

| Output | Gross-margin span | Capital-spending span |
|---|---:|---:|
| Operating profit | 1041.3 − 901.5 = $139.8m | 976.6 − 966.2 = $10.4m |
| FCFE | 395.3 − 289.3 = $106.0m | 391.0 − 293.6 = $97.4m |
| Value per share | 327.4 − 256.1 = $71.3 | 325.2 − 258.3 = $66.9 |

Gross margin has the larger span for each output **over these ranges**. This is a conclusion
about both the model and the chosen ranges. It does not establish a universal ranking.

## Test the range before trusting the ranking

Suppose a reader asks whether the margin range is too wide. As a teaching illustration, halve
it to 16.55%–17.55%, keeping the base and capital-spending range unchanged. This alternative is
an illustrative judgment, not a newly discovered fact about ABG.

Before running, a prediction could read: “Margin 16.55%–17.55%, in every forecast year: I expect
its output spans to roughly halve. Capital spending may then lead for cash flow and value.”
Save the prediction with a timestamp or Git commit before seeing results.

| Revised margin | Final-year operating profit ($m) | Final-year FCFE ($m) | Value ($/share) |
|---|---:|---:|---:|
| 16.55% | 936.5 | 315.8 | 273.94 |
| 17.55% | 1006.3 | 368.8 | 309.57 |

The revised spans are $69.8m for operating profit, $53.0m for FCFE, and $35.63 per share.
Margin still leads for operating profit; capital spending now leads for FCFE and value.
The prediction was supported: changing the comparison range changed part of the ranking.
A useful partner response is: “The cash-flow ranking changed because I narrowed margin's
range, not because the underlying company or base forecast changed.”

## Sensitivity, uncertainty and research

Sensitivity measures the output's response. Uncertainty concerns how well you know the input.
A large span does not tell you how likely either endpoint is. These tables contain no probabilities.

For example, if the capital-spending range has current company guidance behind it but the margin
range is only judgment, margin may deserve the next research effort despite its smaller revised
cash-flow span. Identify the missing evidence before deciding what to research. This is a
conditional example, not a claim about which ABG input is actually better known.

## Check the model and preserve the sign

Reset independent inputs before each run; linked accounting values should recalculate. Check
that statements still balance, recompute a difference yourself, and restore the base at the end.
A failed run cannot support a driver ranking.

For a loss-making company, retain negative cash flow. In a separate illustrative example,
FCFF moving from −$40m to −$25m is an improvement of +$15m, while cash flow remains negative.
Do not remove negative years. When valuation is unresolved, explain the limitation and compare
operating profit and signed cash flow; do not force a terminal value to fill a table.

## DRIVER in practice

Define the driver question yourself. Represent the ranges and units before asking AI to build.
Implement with AI, then validate the results yourself. Evolve by questioning a range.
Reflect by explaining what you learned about your company.

<!-- AUTHORED HOME. Scope: OWNER-DECISION-GATES.md, Week 6 sensitivity ruling, 2026-09-28. -->

# Lab 12 — Pro-Forma Sensitivity: Interpret and Challenge the Drivers

**One thing today: explain your company's main drivers and test how much your conclusion depends on the input ranges.**

**Category:** Thursday merit checkout; anchors below. Dates and points: Brightspace and the course schedule.

**You arrive with:** your own company model, sensitivity results and locked prediction from
[Lab 11](lab-11-proforma-what-if.md), and the same AI chat.

## Reopen and explain

1. Open your Course/Work Folder in VS Code and rerun Tuesday's analysis from the terminal.
   *Expect:* the saved base and sensitivity results.
2. Explain your driver ranking to your partner without AI. Your partner asks which input
   range has the weakest justification. Swap roles. *Expect:* one specific range to investigate.

## D — the question, the same for everyone

> **Why do these inputs drive my company's results, and would my conclusion change under a different defensible range?**

Paste this into your resumed chat. Keep the company, model, base and output definitions from Lab 11.

## R — follow the mechanism

1. For the driver being questioned, write **input → statement line → cash flow → value**,
   stopping at cash flow if valuation is unavailable. Cite the base and changed results.
   Briefly explain the other driver’s direction. *Expect:* an explanation grounded in your model.
2. Choose a revised lower/higher range for the driver your partner questioned. Use the
   company filings or assumption sources you already used in Lab 10; record the source,
   period, units and reason, or label an unsupported choice as judgment.
   Keep the original base unchanged. *Expect:* a justified alternative range for the same input.
3. Before running it, close AI and extend your locked record: revised input values, expected
   output effect, whether the ranking will change, and why; save a timestamp or Git commit.
   *Expect:* a prediction made before seeing the result.

## I — test the interpretation

Send this request with Tuesday's model, results and your revised range available in the chat:

> Reuse my existing one-at-a-time sensitivity function. Keep the original base, output
> definitions and the other driver's range unchanged. Rerun the selected driver over my
> revised lower/base/higher values. Show the original and revised input ranges with units,
> the resulting operating profit and free cash flow, value per share only when valid,
> signed changes from base, and output spans (maximum minus minimum across valid
> lower/base/higher results). Retain the selected driver’s statement details for tracing
> its effect. Keep the accounting
> checks visible, flag invalid runs, and restore and verify the base. Do not change multiple
> independent inputs together, fill missing company data, or infer probabilities. Leave
> the causal interpretation and conclusion to me.

Save and run the returned code in your open folder. *Expect:* an original-versus-revised
comparison whose only change is the selected driver's tested range.
While AI works, explain to your partner what evidence would justify that range.

## V — decide what the comparison means

1. Verify the unchanged base, the accounting checks and one difference from base by hand.
   *Expect:* a valid comparison; investigate failures before interpreting them.
2. Reconcile your prediction with the result. Does the same driver still matter most for
   each output, or did the ranking change? Explain why using the actual input and output
   values. *Expect:* either conclusion supported by evidence, not a preferred answer.
3. Distinguish **sensitivity** (how much the output moves) from **uncertainty** (how well
   you know the input). Identify which assumption deserves more research, considering both.
   *Expect:* a research priority, not a claim that the largest swing is the most likely outcome.

## E — the partner's challenge

Your partner checks one causal explanation against your model and asks one specific question
about the range or the conclusion. Save the question, your answer and any correction beside
your results. Swap roles. *Expect:* a claim strengthened, qualified or corrected by fresh eyes.

## Floor

In the same analysis, keep the original and revised sensitivity results with visible checks,
your causal explanations, the reconciled prediction, the partner's question and your response,
and a conclusion naming the main driver and the assumption to research next. The signed-cash-flow
and unavailable-valuation rule from Lab 11 still applies. You submit individually.

## Interpretation — Learn on your own

1. What makes a driver economically important? 2. How can an uncertain input have little
impact, or a powerful input be well known? 3. Explain which needs more research in your company.

## Reflect

Explain to your partner what you learned about your company that the base forecast alone did not show.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

<!-- Scale generated from SIMPLE-SYLLABUS-COMPONENTS.md; five criteria checked by lesson_quality_audit.py. -->
## Merit anchors — five criteria, 5 points each

**4** = one minor weakness; **2** = an important link incomplete; **1** = minimal;
**0** = missing or fabricated. Score one underlying defect once.

| Criterion | 5 | 3 | 0–1 |
|---|---|---|---|
| Reproducible sensitivity | Original and revised ranges, units, outputs and unchanged base are visible | A comparison detail is unclear | Results cannot be traced to the inputs |
| Causal interpretation | Selected driver traced through own statements and results; other driver’s direction explained | Mechanism partly explained | Generic explanation or unsupported causal claim |
| Range and ranking judgment | Revised range justified; ranking explicitly qualified by ranges and output | Rationale or qualification incomplete | Ranking treated as universal or as probability |
| Validation and prediction | Checks and restored base verified; prior prediction honestly reconciled | A validation or reconciliation step incomplete | Failed runs treated as valid, or no pre-run prediction evidence |
| Evidence and revision | Partner challenge answered; research priority justified by impact and uncertainty | Challenge or research rationale thin | Neither a supported response nor a research priority |

**Next week:** bring this analysis to the Project 1 studio; use it to explain the assumptions that drive your valuation.

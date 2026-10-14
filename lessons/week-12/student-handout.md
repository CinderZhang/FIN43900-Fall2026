# Week 12 Student Handout — Project 2 Studio

Both meetings are open studios: no lab checkout, no lab points. Bring your Project 2 repository
on GitHub and leave with a cold-run record, a committee answer, and a short must-fix list.

## Where each Project 2 part comes from

You built every piece in the labs; before Tuesday you connect the backtest to your app (the
[prework](student-prework.md)). The studio puts them in one repository.

| Project 2 needs | You built it in |
|---|---|
| Mandate: objective, hard constraints, the question for the client | [Lab 13](../week-08/lab-13-portfolio-mandate.md) and your own mandate |
| Baselines and the mandate check | [Lab 14](../week-09/lab-14-portfolio-baselines.md) |
| Your first app: your universe, the constrained search, the stress run (`app.py`) | [Lab 15](../week-09/lab-15-portfolio-stability.md) |
| Point-in-time rule and data card | [Lab 16](../week-10/lab-16-provenance-gate.md) and [Lab 17](../week-10/lab-17-point-in-time.md) |
| Frozen rule card, holdout, placebo, selection ledger | [Lab 18](../week-11/lab-18-holdout-test.md) and [Lab 19](../week-11/lab-19-signal-decision.md) |
| The product: your app with the holdout panel and the lag and cost controls | Lab 15 and Lab 19, joined in the Week 12 [prework](student-prework.md) |
| Locked Changed-Input Record | the Week 6 pattern ([Lab 11](../week-06/lab-11-proforma-what-if.md)), on one Project 2 input |
| The bundle itself | [the Project 2 page](../../projects/project-2-investment-management-application.md) and the [submission architecture](../../PROJECT-SUBMISSION-ARCHITECTURE.md) |

**GitHub is the main delivery.** Every location in your submission manifest is a GitHub link,
except the videos.

## Local model-risk reference

Use this section if the Federal Reserve page is unavailable. It is sufficient for the prework
question and studio; the external guidance is a professional analogue, not generative-AI law.

- **Conceptual soundness:** the design, assumptions, data, judgments, and developmental evidence
  must fit the model's stated purpose and intended use.
- **Outcome analysis:** compare results with known or subsequently observed outcomes, baselines,
  holdouts, backtests, and outliers. An attractive output is not evidence that the process is
  valid.
- **Ongoing monitoring:** changes in users, data, markets, products, or constraints can make a
  previously acceptable model unfit. Monitor limitations, performance, overrides, and triggers.
- **Independent challenge:** a reviewer may reject or restrict use when the purpose is mismatched,
  assumptions or data are unsupported, known-answer/holdout/outcome checks fail, deterioration is
  unexplained, or monitoring and ownership are absent—even when the output looks polished.

The 2026 guidance expressly leaves generative and agentic AI outside its model definition. Here,
apply these validation ideas to the finance model and decision system only.

## Tuesday — the cold run, with your partner

1. Without AI, write your committee decision and the one claim most likely to reverse it.
2. Give your partner only your repository's README link. They run it in their own folder and
   write: the command, the first failure, the elapsed time, where the result is. Do not coach. Swap.
3. Ask your AI for one concrete test of your riskiest claim. Check it yourself; repair, qualify, or
   drop the claim.
4. Freeze the must-fix list. No new analysis.

## Thursday — the three videos, rehearsed

| Video | The one question it answers |
|---|---|
| Video 1 — how it changed | What changed in your system and your thinking since your first mandate, and which AI output did you check? |
| Video 2 — technical walkthrough | How does your code turn the data into the result, and which test passed or failed? |
| Video 3 — committee presentation | What should the committee do, under what conditions, and what reverses it? |

Rehearse Video 3 to your partner; your partner asks one sceptical question on the mandate, the
timing, the baseline or the holdout. "My system cannot establish that" is an acceptable answer.

## Final studio checklist

- every manifest row is a working link, or marked unresolved;
- your partner's cold run reached your result from the README alone;
- memo, videos and output use the same numbers, dates and conditions;
- the decision names an action, a condition, a monitor and a reversal trigger;
- your README, memo and each video open with the AI announcement and "education, not investment
  advice" ([the Project 2 page](../../projects/project-2-investment-management-application.md)).

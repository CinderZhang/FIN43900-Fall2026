# Week 12 — Project 2 Audit and Investment-Committee Defense

## Mission

Both meetings are studios: no lab checkout. Tuesday, your partner runs your Project 2 repository
cold from the README. Thursday, you rehearse the committee presentation against a sceptic. You
leave with a short must-fix list, not new analysis.

**GitHub is the main delivery.** Your Project 2 repository on GitHub is the bundle; the
manifest's locations are GitHub links, except the videos.

## You arrive with

- your files from [Labs 13–19](student-handout.md#where-each-project-2-part-comes-from), in your
  Project 2 repository on GitHub;
- your own mandate and a draft memo.

## Outcomes

- Put the Lab 13–19 work into one repository a cold reviewer can run from the README.
- Trace the riskiest claim to its source, its test and the decision it supports.
- Keep the three videos distinct: how it changed, technical walkthrough, committee decision.
- Freeze a credible must-fix list instead of adding scope.

## Prerequisites and prework

Read [Federal Reserve SR 26-2, "Supervisory Guidance on Model Risk Management"](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm),
Section V headings **"Conceptual Soundness," "Outcome Analysis," and "Ongoing Model Monitoring"**
(8–10 minutes). Ask: **what evidence would let an independent challenger reject this model even
if its output looks good?** The guidance explicitly excludes generative and agentic AI; apply its
validation ideas to the financial model. The [handout's model-risk reference](student-handout.md#local-model-risk-reference)
is the complete alternative.

Then connect your Lab 19 backtest to your Lab 15 app. Ask your AI to have `app.py` import the
functions from `backtest.py` the way it imports `portfolio.py`, show the frozen rule's holdout
gross and net as locked numbers, and add the lag and the cost as controls. Check that it shows
Lab 18's known-answer values (development net 6.13, holdout net −6.09) before you switch to your
own data.

Then put your Lab 13–19 files into one Project 2 repository and write a README with the one
command that produces your result. **Prework-only budget: 60–75 minutes** (the app join is most of it).

## The two sessions

| Session | What happens |
|---|---|
| Tuesday | Cold run with your partner, the riskiest claim tested, the must-fix list frozen |
| Thursday | Video 3 rehearsed against a sceptic; consultation queue |

The [studio guide](studio-guide.md) runs both sessions; the [handout](student-handout.md) holds the
steps and the checklist.

## Package map

- [Student handout](student-handout.md) — where each Project 2 part comes from, the model-risk
  reference, the two studio routines, the checklist.
- [Studio guide](studio-guide.md) — how a studio session works.
- [Open challenge](open-ended-challenge.md) — after class.
- [Prework](student-prework.md) — generated from the prework section above.
- Instructor guide, grading key and verification record — instructor only, not published.

## Brightspace order

Overview → studio guide. The Brightspace module carries the standard pointer to this page.

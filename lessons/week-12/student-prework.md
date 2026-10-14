# Week 12 — Required Prework and Preparation

<!-- Generated from the matching weekly README by build_student_prework.py. Edit the canonical section, then rebuild. -->

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

# Project 2 — Investment Management Application

## Role and committee decision

You are a portfolio or quantitative analyst. Recommend **adopt, allocate to, rebalance, pilot,
or reject** a proposed investment process under an explicit mandate. The decision must compare
the process with a transparent baseline after timing, risk, constraints, and costs.

Points and the enforced due date appear in the Brightspace assignment header. There is no
Edition A checkpoint and no Edition B: start from your Lab 13 mandate, use AI from day one, and
shape the system your own way within the requirements below.

## Where each part comes from — you build it in the labs

**Planning estimate:** 18–25 hours across Weeks 8–13 outside class. Each week's lab builds one
part on a known answer, then on your own Project 2.

| Week | Outside class | You build | In |
|---:|---:|---|---|
| 8 | 1–1.5 h | your own mandate, in Lab 13's shape | [Lab 13](../lessons/week-08/lab-13-portfolio-mandate.md) |
| 9 | 3–4 h | the risk engine and its baselines on Meridian; your first app — your universe, the constrained search, the stress run; outside class, equal weight and inverse volatility on your own universe | [Lab 14](../lessons/week-09/lab-14-portfolio-baselines.md), [Lab 15](../lessons/week-09/lab-15-portfolio-stability.md) |
| 10 | 3–4 h | the point-in-time rule and the data card for your signal | [Lab 16](../lessons/week-10/lab-16-provenance-gate.md), [Lab 17](../lessons/week-10/lab-17-point-in-time.md) |
| 11 | 3–4 h | the frozen rule card, holdout, placebo, gross and net, selection ledger | [Lab 18](../lessons/week-11/lab-18-holdout-test.md), [Lab 19](../lessons/week-11/lab-19-signal-decision.md) |
| 12 | 4–5 h | one repository; the cold run; the Locked Changed-Input Record (the Week 6 pattern, [Lab 11](../lessons/week-06/lab-11-proforma-what-if.md)); memo and video drafts | [Week 12 studio](../lessons/week-12/student-handout.md) |
| 13 | 4–6.5 h | final reconciliation, transcripts, access check, receipt; no new analysis | [Lab 20](../lessons/week-13/lab-20-project2-readiness.md) |

Week 13 is the only planned band that can exceed the normal six-hour outside-work target. Begin
the access/transcript checks in Week 12; if the remaining Week 13 plan exceeds 6.5 hours, freeze
scope and use the published readiness/support route rather than adding analysis.

## Required finance system

Build a locally runnable analysis/application that:

1. states the intended user, objective, universe, horizon/rebalancing, benchmark, risk measure,
   loss tolerance, liquidity, leverage/shorting, concentration, turnover, and suitability limits;
2. documents return frequency, sample/as-of period, availability lag, missingness, revisions,
   and every material transformation;
3. compares equal-weight or another naive allocation with a second transparent baseline before
   presenting a constrained portfolio/strategy;
4. checks units, weights, bounds, covariance/return assumptions, and mandate compliance;
5. builds one market or alternative signal and uses it point-in-time, with event versus
   availability time, a data card, and a complete selection ledger of signals, lags, thresholds,
   universes, and rules tried — "the signal failed the holdout, so I reject it" is a complete
   answer;
6. freezes the rule before the holdout runs, preserves a true holdout, reports gross and net
   results after costs and turnover, and runs at least one placebo or falsification test;
7. perturbs estimates, window, costs, and constraints and states the condition that kills or
   pauses the process;
8. produces an allocation/action range with monitoring triggers—not “optimal” as a conclusion;
   and
9. **presents all of it as a usable product** that a teammate can operate without you (below).

A failed strategy with an honest reject/redesign recommendation is fully responsive. A rule
changed after seeing the holdout becomes a new hypothesis requiring new/prospective evidence.

## What to build — the shape

As in Project 1, the system is a **semi-adjustable tool**:

- **Locked:** the data and its point-in-time rule, the frozen rule card, and the holdout.
- **Adjustable, with bounded controls:** the objective return, the reserve minimum, the
  estimation window, the signal lag, and the trading cost.
- **Visible:** each portfolio's mandate verdict (pass or fail, and which rule), and the holdout
  result gross and net.

**The product is a Python web app.** It starts as your Lab 15 Streamlit `app.py` and grows with
your Project 2: the controls and the display on top of your own engine, which holds the math once.
It shows the locked results and runs the adjustable controls live. Another Python web framework is
fine; a notebook or a script that computes once is not a product. Hosting it publicly (for
example Streamlit Community Cloud) is your choice and never graded, and interface polish earns
nothing.

## Required validation

- known-answer/manual baseline and constraint checks;
- point-in-time/leakage and revision audit;
- naive benchmark and true holdout;
- costs and changed-input stability (the stress run);
- one **Locked Changed-Input Record** with a human-authored, AI-off prediction before the run,
  precommit timestamp/commit, old/new input and
  units, expected/actual output direction, decision effect, and failure diagnosis or no-change reason;
- cold-run plus visible-output check;
- highest-risk counterexample/failure test; and
- one independently checked AI output.

## Submission and scoring

Submit five parts:

1. **The GitHub repository:** the tool, a README a stranger can run it from, and visible output.
2. **Decision memo:** `docs/decision-memo.md`.
3. **Validation and AI use:** `docs/validation-and-ai-use.md`, including the Locked Changed-Input
   Record.
4. **Three videos,** each with its corrected transcript: Video 1, how your system and your thinking
   changed and one AI output you checked; Video 2, the code walkthrough; Video 3, the committee
   presentation.
5. **The manifest,** with every location as a GitHub link except the videos.

The written parts are Markdown files in your repository, not PDFs; attach the same `.md` files
to the Brightspace submission as the frozen record.

**Two statements open your README, your memo, and each video** — a sentence or two each, in your
own words:

1. **AI announcement:** which AI tools you used and for what; that the analysis, the checks and
   the decision are yours; and, if any voice, image or text in a video is AI-generated, that it is.
2. **Education, not investment advice:** this is a course project, a learning demonstration, not
   investment advice.

**Video 3 opens with the live product demonstration.** Right after the two statements, operate your
own tool on camera: move one bounded control and read the result, show a mandate verdict flip,
and show the holdout gross and net. Then defend the recommendation with the tool still on
screen. A Video 3 without the working demo is missing its required opening element.

The 300-point mapping in the major-project analytic rubric applies. Number of tested strategies
is disclosure, not evidence of rigor; undisclosed selection is a data/validation weakness.

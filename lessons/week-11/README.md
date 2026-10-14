# Week 11 — Signal Robustness and Market Usefulness

## Mission

Tuesday: freeze a trading rule, build the backtest from an instruction, and let an untouched
holdout judge it on a training series. Thursday: your own admitted series from Week 10 through a
frozen rule, a placebo and a holdout — then a decision you can defend.

**GitHub is the main delivery.** Every lab and project is handed in as GitHub links to your own
files; this week the commit time of your rule card is part of the evidence.

## You arrive with

- your Lab 17 `asof.py`, your series and its admit, quarantine or reject call;
- your Lab 15 prices for your Project 2 universe, in your Course/Work Folder;
- your partner.

## Outcomes

- Write a rule card before any result exists, and commit it so the timestamp proves it.
- Build a backtest with a lag, a cost per switch, and separate development and holdout results.
- Show how removing the lag manufactures returns, and why a holdout is used once.
- Compare a signal with a placebo and make a reject, redesign, more-evidence or bounded research
  pilot decision.

## Prerequisites and prework

**Before Tuesday — about 20 minutes.** Read the SEC order
[*In the Matter of F-Squared Investments*](https://www.sec.gov/files/litigation/admin/2014/ia-3988.pdf),
Section III.A **"Summary," paragraphs 1–4, PDF pages labeled 2–3** (5–7 minutes). Ask: **how can one
week of timing leakage manufacture most of the apparent alpha?** The
[handout's F-Squared summary](student-handout.md#f-squared-accessible-case-summary) is the complete
alternative.

**Before Thursday — about 15 minutes.** Put your Lab 17 series — at each month-end, the value your as-of
filter says was published by then — and one fund's monthly returns from your Lab 15 `prices.csv`
side by side by month. Ask your AI to help; check three months by hand.

## The two sessions

| Session | Lab | One thing |
|---|---|---|
| Tuesday | [Lab 18](lab-18-holdout-test.md) | a frozen rule and an untouched holdout, on the training series |
| Thursday | [Lab 19](lab-19-signal-decision.md) | your signal through the rule, a placebo and the holdout; a decision |

## Teams this week

Two people, the same partner; each keeps their own Project 2. Explain before you build, swap
and break on Tuesday, argue bull and bear on Thursday. Checkouts stay individual.

## DRIVER this week

Define: the same question for everyone — does the rule work on months it has never seen, after
costs? Represent: the rule card, committed first. Implement: the backtest from one request.
Validate: the known answer and the lag-0 break. Evolve: the placebo and your own data. Reflect:
what the holdout says that development did not.

## Package map

- [Lab 18](lab-18-holdout-test.md) and [Lab 19](lab-19-signal-decision.md) — the labs.
- [Student handout](student-handout.md) — F-Squared, the digits once, the rules.
- [Open challenge](open-ended-challenge.md) — after class.
- [Prework](student-prework.md) — generated from the prework section above.
- Instructor guide, grading key and verification record — instructor only, not published.

## Brightspace order

Overview → Lab 18 → Lab 19. The Brightspace module carries the standard pointer to this page.

# Week 11 Student Handout — Frozen Rules and Holdouts

Last week: was the number knowable when you would have traded? This week: does a rule built on it
still work on months it has never seen, after costs?

## F-Squared accessible case summary

The SEC's 2014 F-Squared order describes a hypothetical ETF rotation record advertised as though
it reflected live implementation. The historical signals were shifted one week earlier than a
trade could have occurred. That timing error allowed the backtest to appear to sell before price
drops and buy before price increases. Correcting the timing removed virtually all claimed
pre-October-2008 outperformance in the SEC's findings. This summary is the required accessible
alternative to the linked PDF; the course uses it to study leakage, not to supply legal advice.

## The commands

In the terminal, with your own Python command:

| Command | Expect |
|---|---|
| `python backtest.py` | Tuesday: development and holdout, rule and buy-and-hold, and the failure-rule line. Thursday: the placebo beside the rule, then your own data |

Something breaks? Debug with your AI: the exact command and the exact error text.

## The digits, once

The first five development months of the training series (start in bills; cost 0.10% a switch;
bills 0.3% a month):

| Month | Last month's signal | Position | Return | Cost | Net |
|---|---:|---|---:|---:|---:|
| 2025-01 | +0.8 (Dec) | equity | 2.0% | 0.10% (switch) | 1.90% |
| 2025-02 | +1.2 (Jan) | equity | 1.5% | 0 | 1.50% |
| 2025-03 | +0.9 (Feb) | equity | 3.0% | 0 | 3.00% |
| 2025-04 | +1.5 (Mar) | equity | −2.5% | 0 | −2.50% |
| 2025-05 | −1.0 (Apr) | bills | 0.3% | 0.10% (switch) | 0.20% |

Compounding: 1.019 × 1.015 = 1.0343, so two months net +3.43%. With **no lag**, April would use
April's own −1.0 and sit in bills for the −2.5% month: that is the leak, a month's loss avoided with
information nobody had.

## The rules

- Write the rule card first, commit it, then run. The commit time is the proof.
- The holdout is run once. A rule changed after seeing it is a new hypothesis that needs new months.
- Report gross and net. A cost per switch is part of the rule, not an afterthought.
- Keep a selection ledger: every rule you tried, including the ones you dropped.
- Beating buy-and-hold is not enough if a placebo does it too.

## DRIVER, one line each

Define — the same question for everyone. Represent — the rule card, committed. Implement — the
backtest from one request. Validate — the known answer and the lag-0 break. Evolve and Reflect — the
placebo, your own data, and the decision.

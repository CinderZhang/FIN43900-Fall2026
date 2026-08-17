# Week 4 Offline/No-Code Fallback — Comparable Policy and Triangulation

Use this packet when code, network, or deal-data access fails. It reproduces
the downloadable **Peer Case**, **Target Case**, and **Expected Output** files. The Week 4 target
is an **unrelated synthetic issuer**, not the Week 3 DCF company; repeated bridge values are a
teaching simplification and must not be triangulated across weeks.

## Peer inputs

| Peer | EV | EBITDA | Equity value | Net income |
|---|---:|---:|---:|---:|
| Alpha | 1,200 | 120 | 900 | 75 |
| Beta | 1,600 | 100 | 1,200 | 60 |
| Gamma | 900 | 100 | 750 | 50 |
| Delta | 2,000 | 125 | 1,500 | 100 |

Synthetic target: EBITDA 80; net income 40; cash 50; debt 300; diluted shares 50; precedent
EV/EBITDA 14. Monetary amounts are USD millions; shares are millions.

## Required manual work and anchors

Define inclusion/exclusion policy first. Calculate peer EV/EBITDA and P/E, then medians:
13.0× EV/EBITDA and 15.0× P/E. Target implied values are 15.80 per share from trading
EV/EBITDA, 12.00 from P/E, and 17.40 from the precedent multiple. Do not average. State the
object, control/synergy/time differences, one changed-peer or normalization test, supported
range/action, condition, and reversal trigger.

Submit the same lab evidence, the exact failure, and `SYNTHETIC TEACHING CASE`. A live deal claim
still requires a verified source, date, terms, and use-rights review before Project 1.

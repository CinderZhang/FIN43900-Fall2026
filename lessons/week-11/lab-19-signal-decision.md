<!-- AUTHORED HOME. Rebuilt 2026-10-13 under the 2026-09 rulings (instruction, not materials; one
     thing per lab; harness the topic; two-person teams; GitHub is the main delivery). -->

# Lab 19 — Signal Decision

**One thing today: your own signal through a frozen rule, a placebo and an untouched holdout — then a decision.**

**Category:** Thursday merit checkout; anchors below.

**Pace — 75 minutes, on the slides:** opener 0–8 · rule card 8–18 · E on the training panel 18–32 · your data 32–46 · explain the code 46–52 · bull and bear 52–60 · decision and learn 60–70 · reflect and checkout 70–75.

**You arrive with:** `backtest.py` matching the [Lab 18](lab-18-holdout-test.md) known answer · your
Lab 18 chat · your partner · your admitted or quarantined series from
[Lab 17](../week-10/lab-17-point-in-time.md) · your prices from [Lab 15](../week-09/lab-15-portfolio-stability.md).

Rerun `python backtest.py` first: Tuesday's values. **Something not working?** Debug with your AI: paste the exact command and the exact error text.

## D — the question, the same for everyone

> **Does your signal beat a placebo on months it has never seen, after costs — and what will you do
about it?**

Paste it into your Lab 18 chat.

**Explain to your partner first** (five minutes, no screen): the economic reason your series should
move your asset. Your partner writes it down. Swap.

## R — your rule card, frozen and committed

Copy Tuesday's rule card into a new `.md` file and fill it for your own case **before you run
anything on your data**: signal (your Lab 17 series: at each month-end, the value your as-of filter says
was published by then), lag one month as Tuesday (month-end t decides month t+1), one fund from your
Lab 15 universe, bills (your Treasury-bill fund's monthly return, or 0.3% a month labelled an
assumption), cost 0.10% a switch, development = all months except the last 12, holdout = the last
12, benchmark = buy-and-hold, failure rule. Commit and push it. A quarantined series enters only
through the as-of filter; a rejected one means Thursday runs on the training panel — say so. You
have seen these fund returns in Lab 15, never this rule on them: the commit keeps the holdout honest.

Under the card, start a **selection ledger**: every rule you try today, one line each, including the
ones you drop. Number tried is disclosure, not evidence.

## E — the placebo and your data, from one message

Send this to your Lab 18 chat:

> In my `backtest.py`, keep everything it already prints exactly as it is. Add a placebo: the same
> rule with the signal's sign flipped, printed beside the rule for development and holdout, gross
> and net. Add an option to read my own monthly table from a CSV file I name, with columns month,
> signal and asset return in percent, and to set the holdout as the last 12 months. Print the rule
> card values at the top of every run. One file, one command.

Read what changed in `backtest.py` before you run it; ask your AI about any line you cannot explain.

1. **Training first.** *Expect:* the rule as Tuesday, and the placebo beside it:

| Period | Rule net | Placebo net | Buy-and-hold |
|---|---:|---:|---:|
| Development | 6.13 | 2.16 | 5.33 |
| Holdout | −6.09 | 4.88 | −2.09 |

   The placebo beats the rule on the holdout. A flipped signal is a falsification test — it bets the
   opposite way; a random signal would be a pure placebo. If not, debug with your AI until they match.

2. **Your data.** Build the monthly table: month, your as-of signal at that month-end, and your
   fund's monthly return from Lab 15. Run once on the frozen card. *Expect:* your rule, your
   placebo and buy-and-hold, development and holdout.

## V — bull, bear, and the ledger

**Explain the code** (six minutes, no AI). Open the block of `backtest.py` that builds the placebo. Explain it to your partner line by
line; your partner asks one question you answer from the code. Swap. A line you cannot explain is
your next question for your AI.

**Partner attack.** Your partner argues the bear case from your numbers; you argue the bull case
from the same numbers. Write both in two sentences each. Swap.

Check your ledger: if you changed the rule after seeing the holdout, the change is a new hypothesis
and the holdout no longer tests it. Say so.

## Your decision

**Reject, redesign as a new hypothesis, gather more evidence, or a bounded research pilot** —
with the condition that would change it. *Example (training):* "Reject: the holdout trails
buy-and-hold by 4 points and the placebo beats the rule; any revised rule needs months after June
2026."

## Floor

The training placebo matched; your rule card committed before your run; your rule, placebo and
holdout; bull and bear; your ledger; your decision. You submit individually.

## Placebo — Learn on your own

1. What is it? 2. How does it work — what does a flipped or random signal tell you? 3. Explain to
your partner why beating buy-and-hold is not enough if a placebo does it too.

## Reflect

Explain to your partner: 1. what your holdout says that development did not; 2. what you would need
before risking real money on this signal.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

## Merit anchors — five criteria, 5 points each, 25 in total

**4** = one minor weakness; **2** = an important link incomplete; **1** = minimal; **0** = missing
or fabricated.

| Criterion | 5 | 3 | 0–1 |
|---|---|---|---|
| Training reproduced | rule and placebo match; the holdout reversal read | one value off | not attempted, or typed in |
| Frozen design | rule card committed before the own run; as-of signal from Lab 17 | card present, commit after the run | no card, or rule changed after the holdout |
| Own test | rule, placebo and buy-and-hold, development and holdout, net of cost | one of the three missing | in-sample only |
| Bull, bear and ledger | both cases from the numbers; every rule tried listed | ledger thin | hidden search |
| The decision | follows the holdout and the placebo; condition stated | decision with vague condition | holdout reversed after the fact |

**Next week:** Project 2 studio — the rule card, the data card and the mandate become one repository.

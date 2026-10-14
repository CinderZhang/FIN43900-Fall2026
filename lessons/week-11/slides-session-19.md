# Session 19 — Signal Decision

> **One thing today: your own signal through a frozen rule, a placebo and an untouched holdout — then a decision.**

## Today's run of show

1. Opener: rerun, the **D** question — 0–8
2. **R** rule card — 8–18
3. **E** on the training panel — 18–32
4. Your data — 32–46
5. Explain the code — 46–52
6. Bull and bear — 52–60
7. Decision and learn — 60–70
8. Reflect and checkout — 70–75

[Lab 19](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-11/lab-19-signal-decision.md)

---

## D — the question, the same for everyone

**Minutes 0–8**

Rerun `python backtest.py` first: Tuesday's values.

> **Does your signal beat a placebo on months it has never seen, after costs — and what will you do
about it?**

Paste it into your Lab 18 chat.

**Explain to your partner first** (five minutes, no screen): the economic reason your series should
move your asset. Your partner writes it down. Swap.

Something not working? Debug with your AI: the exact command and the exact error text.

---

## R — your rule card, frozen and committed

**Minutes 8–18**

Copy Tuesday's rule card into a new `.md` file and fill it for your own case **before you run
anything on your data**:

- signal: your Lab 17 series, the as-of value at each month-end; lag one month, as Tuesday
- one fund from your Lab 15 universe; bills = your Treasury-bill fund, or 0.3% labelled an
  assumption; cost 0.10% a switch
- development = all months except the last 12; holdout = the last 12
- benchmark = buy-and-hold; failure rule

Commit and push it. Quarantined: only through the as-of filter. Rejected: the training panel — say so.

Under the card, start a **selection ledger**: every rule you try today, one line each, including the
ones you drop. Number tried is disclosure, not evidence.

---

## E — the placebo and your data, from one message

**Minutes 18–32**

Send this to your Lab 18 chat:

> In my `backtest.py`, keep everything it already prints exactly as it is. Add a placebo: the same
> rule with the signal's sign flipped, printed beside the rule for development and holdout, gross
> and net. Add an option to read my own monthly table from a CSV file I name, with columns month,
> signal and asset return in percent, and to set the holdout as the last 12 months. Print the rule
> card values at the top of every run. One file, one command.

Read what changed in `backtest.py` before you run it; ask your AI about any line you cannot explain.

**At minute 30:** open the quiz attempt — Brightspace → Quizzes → Lab 19.

---

## E — training first

**Minutes 18–32**

*Expect:* the rule as Tuesday, and the placebo beside it:

| Period | Rule net | Placebo net | Buy-and-hold |
|---|---:|---:|---:|
| Development | 6.13 | 2.16 | 5.33 |
| Holdout | −6.09 | 4.88 | −2.09 |

The placebo beats the rule on the holdout. If not, debug with your AI until they match.

---

## E — your data

**Minutes 32–46**

Build the monthly table: month, your as-of signal at that month-end, and your fund's monthly
return from Lab 15.

Run once on the frozen card.

*Expect:* your rule, your placebo and buy-and-hold, development and holdout.

---

## Explain the code

**Minutes 46–52**

**Explain the code** (six minutes, no AI). Open the block of `backtest.py` that builds the placebo. Explain it to your partner line by
line; your partner asks one question you answer from the code. Swap. A line you cannot explain is
your next question for your AI.

---

## V — bull, bear, and the ledger

**Minutes 52–60**

**Partner attack.** Your partner argues the bear case from your numbers; you argue the bull case
from the same numbers. Write both in two sentences each. Swap.

Check your ledger: if you changed the rule after seeing the holdout, the change is a new hypothesis
and the holdout no longer tests it. Say so.

---

## Your decision · Placebo

**Minutes 60–70**

**Reject, redesign as a new hypothesis, gather more evidence, or a bounded research pilot** —
with the condition that would change it.

*Example (training):* "Reject: the holdout trails buy-and-hold by 4 points and the placebo beats
the rule; any revised rule needs months after June 2026."

**Placebo — Learn on your own:**

1. What is it?
2. How does it work — what does a flipped or random signal tell you?
3. Explain to your partner why beating buy-and-hold is not enough if a placebo does it too.

---

## Reflect

**Minutes 70–75**

Explain to your partner:

1. what your holdout says that development did not;
2. what you would need before risking real money on this signal.

---

## Checkout — on GitHub

**Minutes 70–75**

**Brightspace → Quizzes → Lab 19.**

**GitHub links of your files: md, py and/or other files as needed.**

**Before Tuesday — do these**

1. Commit and push your rule card, ledger and decision.
2. Have your rule card, your data card and your mandate on GitHub.

**Next week:** Project 2 studio — the rule card, the data card and the mandate become one repository.

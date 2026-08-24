# Session 26 — Replicate the Optimizer, Then Overrule It
**Week 14 · Tuesday · Robo-Advisory II: the replication build and the suitability turn**

---

## Today's run of show

**You arrive with:** Project 2 submitted · your Capstone Edition A receipt · the
PyPortfolioOpt README skimmed · your what-it-maximizes line and one-term question.
**Today has no checkout.** You build, you verify, you judge — and you keep what you build.

1. What a reproduction claims — and what it cannot
2. **The build (AI on, you drive):** their library, their data, their published answer
3. **Validate:** the known-answer gate, with the version ladder
4. **The suitability turn:** the optimal answer meets the client mandate
5. Credit, citation, and where this goes next

---

## What you are doing today *(and what it proves)*

Precisely: this is **computational reproduction** — recomputing a project's published
example from its own shipped data and code. Full **replication** would rebuild the
method independently; **original research** asks new questions. Three rungs; own which
one you are standing on.

- If your numbers **match**: their documented example reproduces under your recorded
  environment — and you now have a working reproduction pipeline you built yourself,
  not a screenshot of one. (Reproduction is not validation of the method or the data.)
- If they **don't**: you have a version difference, a method difference, or an error —
  every one of those is worth documenting *after* the ladder.

---

## The build — you drive, AI implements *(25 minutes)*

Open a Colab notebook. Inputs: `pip install` line for the library, the repository's own
`tests/resources/stock_prices.csv`, their README example, the AI of your choice.
**The deck gives targets, not code.**

**Before any code, state in your notebook:** the library version you installed, the
data file and its date range, what the example maximizes, and what "match" will mean
for you (exact share counts? weights to how many decimals?) — one line each.

**Target — reproduce the published example.** Max-Sharpe weights from their shipped
price history, then the discrete allocation for the stated budget. Their README prints
the expected result — share counts per ticker and funds remaining. Match it.

*(The shape, not your answer: "pypfopt X.Y.Z, their CSV [first date]–[last date],
max Sharpe, match = identical share counts. Result: all tickers matched, leftover
matched to the cent." — the version on the board reproduces the README exactly; pin
it with `pip install` if you want the exact match.)*

---

## Validate — the known-answer gate, with the version ladder

1. **Match?** State library version, data file, and the README location of the
   expected output — then cite it
2. **No match?** Do not declare an error. Check, in order:
   - **Version** — optimizers and solvers change between releases; is your installed
     version newer than the README example? Read the **release notes** first
   - **Method** — same objective, same constraints, same budget as the example?
   - **Data** — their shipped CSV, or something else?
3. Only after all three: "possible difference worth reporting" — open-source projects
  credit people who report reproducible discrepancies clearly

> An unexplained mismatch is a documented discrepancy — it becomes a finding only
> after the ladder. An unchecked match is a guess.

---

## The suitability turn *(the half no optimizer automates)*

Now put your reproduced "optimal" portfolio in front of the Week 13 client:

1. Load `client_case.json` — the five hard limits you classified on Thursday
2. **Translate first:** share counts × latest prices → portfolio weights, plus the
   cash remainder and each holding's mandate-relevant classification. Any client
   attribute the price data cannot tell you is **unresolved** — it escalates, it
   never silently passes
3. **AI off, predict:** will the allocation pass the mandate? Which limit is most
   at risk?
4. Test it transparently — limit by limit, reason codes, no silent fixes
5. Disposition: **approve · modify · reject · escalate** — with the failing limit
   named and a reversal trigger stated

**Optimal is a property of the mathematics. Suitable is a property of the client.**
A defensible *reject* of a perfectly optimized portfolio is advisory work at its
best — the optimizer cannot supply the client's facts, and it cannot carry the
accountability. That stays with the advisor.

---

## Credit and citation *(the professional close)*

Your notebook's first cell, from today onward:

> Optimizer: PyPortfolioOpt (Robert Andrew Martin), *PyPortfolioOpt: portfolio
> optimization in Python*, Journal of Open Source Software 6(61), 3066 (2021).
> MIT-licensed; example data from the project repository. Version X.Y.Z installed
> YYYY-MM-DD. This notebook reproduces the project's documented example; the
> library and method are the author's.

Uncredited reproduction is plagiarism with extra steps. Credited reproduction is how
open-source careers start.

---

## Where this goes *(optional, yours)*

- Your notebook is a legitimate **capstone seed**: swap in a different universe, add
  the mandate screen as a function, and it becomes an integrated-system component with
  a real suitability layer — the part that was never automated
- The library's deeper methods (Black-Litterman, hierarchical risk parity) are
  **optional archaeology** — documented in the same cookbook, never required,
  never graded

---

## Before Week 15 — do these:

1. Enjoy Thanksgiving — Thursday is no class
2. Keep your notebook where you can open it — Week 15's capstone integration work
   begins from what you already have
3. Read the Week 15 prework page before Week 15's first session (it is short; the
   capstone consultation studios are where the remaining time goes)

**Week 15 preview:** assemble your capstone's integration skeleton from components you
have already built — including, if you choose this track, today's optimizer-plus-
mandate pair.

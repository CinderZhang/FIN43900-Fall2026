# Session 25 — Mandate Before Model
**Week 13 · Thursday · Robo-Advisory I: suitability, and the optimizer you will replicate**

---

## Today's run of show

**You arrive with:** your Lab 20 readiness audit done Tuesday · a frozen Project 2
completion plan · Project 2 due before Tuesday's session (the Brightspace assignment
header is the clock).
**Today has no checkout.** The 20-lab sequence is complete; from here the work is yours.

1. What a robo-advisor actually is — and where the judgment lives
2. **Floor:** client facts → mandate → admissibility, on the synthetic case
3. Meet the project: PyPortfolioOpt, the open-source optimizer inside the robo stack
4. **AI off, then on:** read their documented example and its printed answer
5. The mission for Tuesday: replicate the optimizer, then judge its output

---

## Why I'm handing you the rod *(read this once)*

It is not that I don't want to teach you this.

Twelve weeks ago you needed the fish. All semester I've been handing you the
**fishing equipment** instead — DRIVER, the AI toolchain, the validation
discipline. By Week 13 you're supposed to be on your own feet, and these two
weeks are where we find out the equipment works.

The anchors are on the slides, the fallback pages exist, and I'm in the room —
but the rod is in your hands. **That was the plan from day one.**

---

## Two rods on the rack — you pick one *(your decision, this week)*

This deck is the **robo-advisory** rod — replicating PyPortfolioOpt's documented example,
then holding the "optimal" portfolio to a client mandate.

The other rod is **fixed income** — replicating the Open Source Bond Asset Pricing team's
published data work. Class sessions walk that one:
[lessons/week-13](https://github.com/CinderZhang/FIN43900-Fall2026/tree/main/lessons/week-13)

**You decide which one you dig deep on for these two weeks.** Either counts; either can
seed your capstone. Choosing robo still means coming to class — the sessions model the
replication moves both tracks share.

---

## Why this module exists *(the professional stakes)*

Every robo-advisor is two machines bolted together: an **optimizer** that turns prices
into portfolio weights, and a **suitability layer** that decides whether those weights
may ever reach a client.

The optimizer is not a secret anymore — the same mathematics runs in an open-source
library anyone can read, install, and verify. What is *not* automated is the judgment:
whether an optimal portfolio is an admissible one.

This module hands you both halves: replicate the optimizer's published results
yourself, then hold its output to a client mandate — and watch which half does
the real advisory work.

---

## The project whose work you are replicating

**PyPortfolioOpt** — created by **Robert Andrew Martin**, with open-source contributors.

- Anchor paper: *PyPortfolioOpt: portfolio optimization in Python*, **Journal of Open
  Source Software** (2021) — JOSS is a peer-reviewed journal for research software
- Open code: MIT-licensed on GitHub, installable with one `pip` line, documented on
  ReadTheDocs with a cookbook of worked examples
- **Self-contained:** the repository ships its own historical price dataset
  (`tests/resources/stock_prices.csv`) and the README prints the exact expected
  output of its worked example — a published known answer

**This is their work, not ours.** Every notebook that uses it carries a citation
naming the author. First professional convention of the module.

---

## Floor — client facts → mandate → admissibility *(the judgment chain)*

The finance chain this track lives on:

**client facts → auditable mandate → admissibility screen → comparison → recommendation**

- A **client fact** is verified; a **stated preference** is the client's; a
  **professional assumption** is yours to defend; an **unresolved unknown** must be
  named, never filled in by a model
- **Risk tolerance** (how much loss the client accepts) is not **loss capacity**
  (how much the client survives) — the pair governs every screen
- **Admissibility is not optimization**: a portfolio passes hard limits before any
  ranking matters

The Week 13 handout carries the full worked case — the five hard limits of
`client_case.json` and the four model portfolios with digits. That case is Tuesday's
judgment layer.

---

## AI off: read their documented example *(10 minutes, pairs)*

Open the PyPortfolioOpt README (linked on the track page). No AI yet — form your own
picture first.

1. Find the worked example: prices in, **max-Sharpe weights** out, then a
   **discrete allocation** — whole shares for a stated budget — with the exact
   printed result (share counts and funds remaining)
2. Write one line: **what the optimizer was told to maximize, and one thing it was
   never told about the investor** *(the shape, not your answer: "It maximizes the
   Sharpe ratio — return per unit of volatility; it knows nothing about the
   investor's liquidity needs.")*
3. Pick one term you cannot explain and write what you *think* it means

**AI on:** ask it your term — then check its answer against the library's own
documentation. Where they disagree, **the documentation governs.**

---

## Tuesday's mission *(one sentence)*

**Install their library, reproduce their published example exactly from their own
shipped data, then put the "optimal" result in front of a client mandate and defend
what happens.** You drive the AI; the deck gives targets and validation anchors,
not code.

---

## Before Tuesday — do these:

1. **Submit Project 2** — before Tuesday's session; the Brightspace assignment header
   is the clock
2. **Capstone Edition A** — the window sits between this session and Tuesday's class;
   exact times on the Brightspace checkpoint page. ~20 minutes, **before** any
   capstone-specific AI work
3. **Skim the PyPortfolioOpt README** (~10 minutes, linked on the track page) — bring
   your what-it-maximizes line and your one-term question
4. Nothing to install before class — Tuesday's Colab does it in one line

**Session 26 preview:** reproduce the optimizer's published answer from its own data,
then disposition that answer against a real client mandate — the advisory version of
checking the machine before trusting it.

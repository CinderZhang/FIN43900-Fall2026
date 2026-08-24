# Session 25 — The Price You See Is Not the Price You Pay
**Week 13 · Thursday · Fixed Income I: conventions, and the research you will replicate**

---

## Today's run of show

**You arrive with:** your Lab 20 readiness audit done Tuesday · a frozen Project 2
completion plan · Project 2 due before Tuesday's session (the Brightspace assignment
header is the clock).
**Today has no checkout.** The 20-lab sequence is complete; from here the work is yours.

1. Why bonds broke a published paper — the story behind this module
2. **Floor, with digits:** clean vs dirty price, accrued interest, yield vs coupon, duration
3. Meet the researchers: Open Source Bond Asset Pricing
4. **AI off, then on:** open their real data dictionary and map it to today's floor
5. The mission for Tuesday: replicate one published number

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

Class sessions walk **fixed income** — this deck, replicating the Open Source Bond
Asset Pricing team's published data work.

The second rod is **robo-advisory** — replicating PyPortfolioOpt's documented example,
then holding the "optimal" portfolio to a client mandate. Equally complete, decks and all:
[tracks/robo-advisory](https://github.com/CinderZhang/FIN43900-Fall2026/tree/main/tracks/robo-advisory)

**You decide which one you dig deep on for these two weeks.** Either counts; either can
seed your capstone. Choosing robo still means coming to class — the sessions model the
replication moves both tracks share.

---

## Why this module exists *(the professional stakes)*

A few years ago a PhD student tried to replicate a seminal corporate-bond factor
paper — and could not. His detective work exposed data errors serious enough that a
top finance journal issued a **retraction** — a first in its history.

Out of that came **Open Source Bond Asset Pricing**: researchers who rebuilt the
bond data correctly, published every step, and put the data and code where anyone
can check them.

That is what replication is. Not homework — **the quality control of the entire
research industry.** Next Tuesday, you do it.

---

## The people whose work you are replicating

**Open Source Bond Asset Pricing (openbondassetpricing.com)** — built and maintained by
**Alexander Dickerson** (UNSW), **Philippe Mueller** (Warwick), and **Cesare Robotti**
(Warwick), with collaborators.

- Anchor paper: *Priced Risk in Corporate Bonds*, **Journal of Financial Economics** (2023)
- The data: TRACE corporate-bond panels — cleaned, documented, free to download, no account
- The code: the `trace-data-pipeline` repository on GitHub — every cleaning choice visible

**This is their research, not ours.** When you use their data — in class, in a capstone,
anywhere — you cite them. That is the first professional convention of the module.

---

## Floor 1 — clean price, accrued interest, dirty price *(digits)*

A bond's quoted price is the **clean price**. The buyer pays the **dirty price**:
clean **plus the coupon interest accrued** since the last payment.

**Worked microcase** *(synthetic; 30/360 day count, supplied)* —
semiannual coupon **3.00** per period · **90 of 180** days since the last coupon:

| Step | Value |
|---|---|
| Accrued interest = 3.00 × 90/180 | **1.50** |
| Quoted clean price | **98.25** |
| Dirty (invoice) price = 98.25 + 1.50 | **99.75** |

You see 98.25 on the screen. **99.75 leaves your account.**
The full walk-through lives on the Week 13 *Bond Price Reconciliation* page.

---

## Floor 2 — yield vs coupon, and duration *(digits on the K1 anchor)*

- **Coupon** is a promise printed on the bond. **Yield to maturity** is the discount
  rate that makes the promised cash flows worth today's dirty price — always under
  stated day-count, coupon-frequency, and settlement conventions. Price falls →
  yield rises. The coupon never moves.
- **Macaulay duration** — the PV-weighted average wait for your cash flows, in years.
  **Modified duration** = Macaulay ÷ (1 + y) under K1's annual-pay convention — for a
  bond paying m times a year, divide by (1 + y/m). It is the % price change for a
  1-point yield change.

The Week 13 conventions page carries the full **K1 known-answer case** — a bond that
settles exactly on a coupon date, so accrued is zero and the mechanics stand alone.
You will meet these same quantities on **real data** Tuesday: OSBAP publishes daily
and monthly panels carrying `clean price`, `accrued interest`, `yield`, `duration`,
`convexity` — **your download is the monthly panel.**

---

## Why "corrected" data matters *(the audit instinct)*

Real bond data lies with a straight face:

- One major vendor **silently caps monthly bond returns at +100%** — only the upside.
  Documented in OSBAP's own data README, not in the vendor's marketing.
- Raw **TRACE** trades — TRACE is FINRA's Trade Reporting and Compliance Engine, the
  tape every US corporate-bond trade reports to — carry fat-finger price jumps that
  bounce back a day later; naïve filters either miss them or throw away good data
  with the bad.

The OSBAP pipeline exists because **the data is guilty until proven innocent** — the
same discipline you practiced on synthetic data in Weeks 10–11, now at research scale.

---

## AI off: read the real schema *(10 minutes, pairs)*

Open the OSBAP **Data** page (linked on the Week 13 page) and its data dictionary
on GitHub. No AI yet — the timing matters: form your own picture first.

1. Find the columns that carry today's floor: clean price · accrued interest · yield ·
   duration · convexity
2. Pick **one column you cannot explain** and write one sentence saying what you
   *think* it is *(the shape, not your answer: "`t_spread` — I think this is the
   spread to a same-maturity Treasury, but I don't know which curve they use.")*

**AI on:** ask it to explain your column — then check its answer against the
dictionary and the data report. Where they disagree, **the documentation governs.**

---

## Tuesday's mission *(one sentence)*

**Download their data, reproduce one of their published numbers, and explain any
difference you find.** You drive the AI; the deck will give you validation anchors,
not code. Your notebook is yours to keep — it can seed a fixed-income capstone.

---

## Before Tuesday — do these:

1. **Submit Project 2** — Monday night; the Brightspace assignment header is the clock
2. **Capstone Edition A** — the window sits between this session and Tuesday's class;
   exact times on the Brightspace checkpoint page. ~20 minutes, **before** any
   capstone-specific AI work
3. **Download the OSBAP monthly bond panel** (openbondassetpricing.com → Data; zipped
   parquet, no account needed) and note the download date in your notes
4. Skim their data README (~10 min) and bring your one-column question from today

**Session 26 preview:** replicate one published statistic from real TRACE data and
defend the difference — the analyst's version of checking someone else's work.

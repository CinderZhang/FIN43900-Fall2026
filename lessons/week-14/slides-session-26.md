# Session 26 — Replicate the Research
**Week 14 · Tuesday · Fixed Income II: the replication build**

---

## Today's run of show

**You arrive with:** Project 2 submitted · your Capstone Edition A receipt · the OSBAP
monthly panel downloaded (with its download date noted) · one column question.
**Today has no checkout.** You build, you verify, you keep what you build.

1. What a replication claims — and what it cannot
2. **The build (AI on, you drive):** load the panel, reconcile the conventions
3. **Validate against their published numbers** — the known-answer gate, at research scale
4. Divergence clinic: version, changelog, or error?
5. Credit, citation, and where this goes next

---

## What you are doing today *(and what it proves)*

Replication asks one question: **starting from the same inputs and stated methods,
do I get their numbers?**

- If **yes**: their result survives *your* independent look — that is evidence.
- If **no**: you have found a version difference, a method ambiguity, or an error —
  and every one of those is a finding worth writing down.

Precisely: today is **computational reproduction** — recomputing published numbers from
the authors' own processed data. Full **replication** rebuilds from raw inputs; **original
research** asks new questions. Three rungs; own which one you are standing on.

What today is **not**: proof a strategy works, an endorsement, or your own research.
Own the difference between *checking* work and *originating* it.

---

## The build — you drive, AI implements *(30 minutes)*

Open a Colab notebook. Your inputs: the OSBAP parquet you downloaded, their data
dictionary, and the AI of your choice. **The deck gives you targets, not code.**

**Before any code, state in your notebook:** the fields you will use, their units and
frequency (per-100 par? percent or decimal?), your eligible rows, and your tolerance —
the Week 13 policy-before-computation discipline, one line each.

**Target 1 — conventions reconciliation.** From the data dictionary, pin down each floor
column's units and frequency. Then design **one cross-field check the documentation says
must hold** — the Week 13 microcase pattern (3.00 · 90/180 → accrued 1.50 never exceeds
one coupon period) — and verify it on a sample within your stated tolerance. A check that
cannot fail is not a check: don't recompute a column from its own definition.

**Target 2 — reproduce a published statistic.** OSBAP's Data tab publishes detailed data
reports. Pick one reported number for the **monthly** panel, **transcribe its exact
definition first** — units, filters, frequency, report page — then compute and compare.

*(The shape, not your answer: "Report Table X: average bonds per month in 2015 under
filter set F. My file: 3,912 for 2015-06 with the same filters — matched; residual gap
logged as post-publication data revision.")*

---

## Validate — the known-answer gate at research scale

In Week 3 you validated a DCF against a known answer. Same discipline, real stakes:

1. **Match?** State the number, the source page of their report, and your computed value
2. **No match?** Do not declare an error yet. Check, in order:
   - **Version** — the paper behind the data (*The Corporate Bond Factor Replication
     Crisis*) is under journal revision and the data updates with it; is your
     download date after their report date?
   - **Changelog** — the GitHub changelog documents every data change. Read it first.
   - **Method** — did you apply the same filters the report states?
3. Only after all three: "possible error" — which, at OSBAP, is a **contribution**
   (they credit people who find issues; that is how open research works)

> An unexplained mismatch is a documented discrepancy — it becomes a finding only
> after the ladder. An unchecked match is a guess.

---

## AI discipline in the build *(same rules as Week 1, lighter hands)*

- AI writes the loading and computation code — **you** state the target, the filters,
  and the tolerance *before* asking
- Every AI claim about the data ("this column is winsorized") gets checked against
  the dictionary or report — **documentation governs**
- Record accept / modify / reject on the one suggestion that mattered most

No training wheels today: no starter file, no field-by-field checklist. Twelve weeks
built the instincts; this is where they run on their own.

---

## Credit and citation *(the professional close)*

Your notebook's first cell, from today onward:

> Data: Open Source Bond Asset Pricing (openbondassetpricing.com), Dickerson,
> Mueller & Robotti — *Priced Risk in Corporate Bonds*, J. Financial Economics (2023).
> Downloaded YYYY-MM-DD. This notebook replicates their published data report;
> the underlying research is theirs.

Uncredited replication is plagiarism with extra steps. Credited replication is how
careers in research start.

---

## Where this goes *(optional, yours)*

- Your replication notebook is a legitimate **capstone seed**: extend it — a screening
  rule on real bonds, a factor comparison, a data-quality audit — and it becomes an
  integrated-system component with real data provenance
- The full OSBAP pipeline (their `trace-data-pipeline` repo) regenerates everything
  from raw TRACE — that requires WRDS access (Wharton Research Data Services, the
  subscription platform for raw research data) and is **optional archaeology**, never
  required and never graded

---

## Before Week 15 — do these:

1. Enjoy Thanksgiving — Thursday is no class
2. Keep your replication notebook where you can open it — Week 15's capstone
   integration work begins from what you already have
3. Read the Week 15 prework page before Week 15's first session (it is short;
   the capstone consultation studios are where the remaining time goes)

**Week 15 preview:** assemble your capstone's integration skeleton from components
you have already built — including, if you choose fixed income, today's notebook.

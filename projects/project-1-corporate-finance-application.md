# Project 1 — Corporate Finance Application

## Role and committee decision

You are the **AI task force member embedded in a buy-side analyst group**. The fund holds
**no position** in your target company. The senior analysts own the sector view; you were
brought in to do what your generation of analysts does best — build the evidence-and-model
stack with AI acceleration, faster and more transparently than it has ever been built,
**without ever letting the machine own the judgment**. The portfolio manager's ask:
should the fund **initiate a position, place the name on watch/defer, or do not initiate** —
delivered as a defensible valuation range with evidence dates, material conditions, and
reversal/monitoring triggers, never a single confident number. Your group will challenge
your assumptions before the committee does; the committee sees your memo and your recorded
defense. Screening selected the research target; it is not valuation evidence and cannot
determine the recommendation.

Points and the enforced due date appear in the Brightspace assignment header. The separate
**Project 1 — Edition A Checkpoint (AI Closed)** page publishes the supervised baseline window;
do not use the final-assignment page as the Edition A submission location.

**Planning estimate:** 18–25 hours distributed across Weeks 2–8, including research, modeling,
validation, cold run, writing, recording, transcript correction, and access checks.

| Week | Project 1 planning band | Scope boundary |
|---:|---:|---|
| 2 | 3–4 h | Edition A, source map, valuation architecture |
| 3 | 3–4 h | FCFF/WACC/terminal model and validation |
| 4 | 3–4 h | peer policy, multiples, transaction qualification |
| 5 | 3–4 h | pro-forma build: personalized drivers, five-year statements, articulation checks |
| 6 | 3–4 h | own-pro-forma sensitivity analysis; driver identification and interpretation; justified input ranges; fresh-eyes revision |
| 7 | 2.5–4 h | cold run, manifest, memo, product-demo rehearsal, three bounded recordings |
| 8 | 0.5–1 h | access/integrity check and final receipt; no new analysis |

## Required finance system

Build a locally runnable analysis/application that:

1. identifies the intended investment user, decision horizon, target/security, valuation date,
   currency, share basis (basic vs. diluted count), and relevant exclusions;
2. traces material historical inputs to filings or authoritative sources and distinguishes
   facts, normalizations, forecasts, and model outputs — including a base year normalized
   for one-time items and basis changes (the Week 2 contamination catalog);
3. builds a **five-year three-statement pro-forma** (income statement, balance sheet, cash
   flow) with a driver architecture **personalized to the company** — pro-forma is a method,
   not an algorithm; every load-bearing driver carries value · basis · challenge ·
   evidence that would change it — and statements that articulate under checks that can
   fail loudly (balance sheet balances every year, cash flow ties to balance-sheet cash,
   base year reconciles to the filing);
4. constructs the five-year FCFF DCF with WACC, terminal convention, and a complete
   enterprise-to-equity/per-share bridge — built as an engine in Week 3, then **driven by
   the pro-forma's operating forecast** from Week 5 on;
5. reports causal low/base/high cases, a WACC–growth sensitivity, terminal-value share, and one
   reverse-DCF or market-implied expectation;
6. defines a comparable-company policy before selecting peers and calculates at least one
   consistent enterprise-value and one equity-value multiple; use relevant transaction evidence
   only when its control/synergy/time context can be defended;
7. explains disagreement across methods rather than mechanically averaging them;
8. analyzes **one-at-a-time sensitivities of the company’s own pro-forma**, identifies the
   main drivers of operating profit, free cash flow and value, explains the causal links,
   and tests whether the ranking depends on the chosen input ranges. Maintain an assumption-challenge record
   (each load-bearing driver: value · basis · challenge · evidence that would change it);
   partner fresh-eyes challenges from the Weeks 5–6 labs belong in this record, credited to
   the challenger;
9. produces a valuation range and conditional committee action, not false point precision;
   and
10. **presents all of it as a usable product**: a semi-adjustable interface — a driver
    panel with bounded controls, a base reset, and visible sensitivity results and checks — that a
    teammate can operate without you. The notebook-with-driver-panel floor in "What to
    build" fully satisfies this; a bare linear notebook that computes once does not.

## What to build — the shape

Requirements 1–9 say what your system must **do**. Requirement 10 says what it must
**be**: a product — a tool the analyst team can still use after your presentation ends.
The required shape is a **semi-adjustable pro-forma workbench**, and the word doing the
work is *semi*:

- **Locked:** the accounting engine (statement articulation), the provenance layer, and
  the checks. These have right answers; nobody adjusts them.
- **Exposed:** the load-bearing drivers from your assumption-challenge record — each with
  bounds you can defend. *(The shape, not your answer: "revenue-growth slider 0%–6%,
  capped at 6% because the company has never grown same-store above 5% in a decade —
  source: the last five 10-Ks.")* An unbounded slider is an unmade decision.
- **Failing loudly:** the checks panel goes red when an input combination breaks the
  balance sheet or leaves the historical band. The tool teaches its user what the model
  believes.

Any of these emphases satisfies the same ten requirements and the same rubric — a menu
of examples, not tracks, and your own shape is welcome:

1. **Pro-Forma Workbench** — driver panel → live five-year statements, checks, and the
   valuation range. Team value: an analyst tests their own view of your company in
   thirty seconds without touching your engine.
2. **Sensitivity Explorer** — compare one driver at a time with the same base, show
   the input ranges and output changes, and explain which assumptions carry the result.
   Pairs naturally with Video 3: change a driver and explain its effect through the statements.
3. **Assumption Audit Board** — every load-bearing driver with its value · basis ·
   challenge · evidence and its one-way impact on value, so a reviewing analyst knows
   exactly where to push.
4. **Filing Refresh Assistant** *(ambitious)* — drop in the next quarterly filing; the
   base year re-anchors and the tool reports which drivers now look stale.

Product floor and ceiling: a **Colab notebook with a driver panel** (ipywidgets
sliders) fully meets requirement 10. A small local Streamlit or Gradio app is a fine
step up — let Codex or agy scaffold it around your engine; that build is exactly the
AI-accelerated middle, and your judgment lives in what you locked, what you exposed,
and the bounds you chose. **Hosting** remains optional and never graded; no third-party
account is ever required. Interface polish earns nothing under the rubric — the
semi-adjustable decisions are what graders read. The tool you build here is also a
legitimate seed for your capstone system, whose bundle already centers a product
presentation.

## Target eligibility

Because the required architecture is enterprise-value/FCFF, banks, insurers, REITs, and other
issuers for which FCFF and an enterprise-to-equity bridge are economically inappropriate are
not eligible Project 1 targets. Select another operating company by the Week 2 admission gate.
Such issuers may be used later only when an approved project architecture fits the decision.

All market facts carry source and as-of date. Provider labels are reconciled to definitions.
The repository must show the material inputs and result without requiring a grader to run it.

## Edition A boundary

Submit the designated Brightspace Edition A checkpoint during Week 2 before valuation-specific
generative-AI research or coding. The first successful receipt is the baseline of record; a Git
tag may corroborate history but cannot replace the Brightspace checkpoint. Week 1's disclosed
AI-assisted screening occurred before this project boundary; Edition A captures the student's
valuation judgment before valuation-specific AI assistance.

## Required validation

- one synthetic/known-answer reconciliation (against the training-case answers published
  with the weekly starters);
- one independent source/definition check on a load-bearing input;
- one directional changed-input test written before execution;
- one **Locked Changed-Input Record** with a human-authored, AI-off prediction before the run,
  precommit timestamp/commit, old/new input and
  units, expected/actual output direction, decision effect, and failure diagnosis or no-change reason;
- pro-forma articulation checks (balance sheet balances; cash flow ties to cash; base-year
  reconciliation to the filing), DCF boundary/monotonicity checks (outputs move only in the
  expected direction as WACC or growth moves), and enterprise-equity bridge checks;
- peer-policy and multiple-definition consistency check;
- highest-risk failure test plus cold-run log (one clean end-to-end run in a fresh
  environment, recorded); and
- one accepted, corrected, qualified, or rejected AI output with independent evidence.

## Submission and scoring

Submit the uniform seven-part bundle and filenames in the shared checklist: unchanged Edition A
plus Edition B, repository/visible output, research-evolution Video 1, code/validation Video 2,
memo/deck, and committee Video 3 with corrected transcripts and frozen validation/AI-use record.

**Video 3 for Project 1 opens with the live product demonstration — the demo is the main
delivery.** In roughly the first minute, operate your own tool on camera: move one bounded
driver and read the result, explain the sensitivity against the restored base, and show one check failing
loudly on an incoherent input (then recover it). Then defend the recommendation with the
tool still on screen — the committee decides *with your product*, not just your slides. A
Video 3 without the working demo is missing its required opening element.
The 300-point mapping in the major-project analytic rubric applies. No extra points attach to
number of commits, visual polish, framework vocabulary, or video existence.

Before grading, Brightspace also publishes **Project 1 — Annotated Decision-Evidence Excerpt and
Non-Example**. It illustrates observable decision-evidence anchors and common failures but is not
a complete submission, model answer, or source of project facts.

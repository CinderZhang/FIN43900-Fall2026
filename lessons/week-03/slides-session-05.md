# Session 5 — Build the Engine
**Week 3 · Tuesday · Lab 05: Build and Validate an FCFF DCF**

> Interviews for analyst seats test one thing in the first ten minutes:
> can you build a DCF and say **which assumptions the value hinges on**?
> AI assembles spreadsheets. The seat belongs to whoever explains them.

---

## Today's run of show

1. The mission: build the engine, then say what it hinges on
2. **Opener** — tools alive, artifacts out *(nothing typed into AI yet)*
3. **Paired checkpoint defense** — walk your own hand arithmetic
4. Concept **gap check** → your written gap list
5. The known answer, on the board
6. **AI off** — the architecture from memory, and two numbers by hand
7. **Two tracks at once** — research to Codex and Gemini, learning to your gap list;
   **start your quiz attempt when told**
8. Validate — **your** judgment, not the AI's
9. Transfer to your own company
10. **Submit — receipt on screen before you leave**

*You arrived with: the worked example done, with its **three hand checkpoints** ·
the five-part architecture **drawn from memory** · your **WACC-vs-g prediction** ·
your **Week 2 evidence ledger**.*

---

## Opener — tools alive, artifacts out

Follow the projector. Four steps, then stop.

1. **Open Codex** — ChatGPT's coding agent. The CLI (terminal version) if yours works: open your
   terminal *(Windows: Start → type `PowerShell` · Mac: ⌘-Space → type `Terminal`)*, type `codex`.
   No working CLI? **ChatGPT desktop app → Codex.** Confirm it launches — a prompt you could
   type into is enough. Thumbs up. **Type nothing yet:** AI opens in the build block, not here.
2. **Artifacts out:** your Week 2 evidence ledger · your three prework checkpoints ·
   your architecture sketch.
3. **Paired, 2 minutes each way:** defend **one** hand checkpoint. Walk your partner through
   *how* you got **114.48** or **90.31** — step by step, without notes if you can.
4. **Solo, 2 minutes:** mark this week's four concepts — **FCFF forecasting · discounting and
   present value · terminal value · terminal-value concentration** — "can explain with an
   example" or "not yet." **Every "not yet" goes on your written gap list.**

> The shape, not your answer *(step 3)*: "**114.48.** FCFF₁ is 100 grown once at 8% — 108.00.
> Year 2 grows *that* number, not the original 100, at 6%: 108.00 × 1.06 = 114.48. Growth
> compounds on last year's cash flow, which is why a *fading* growth rate still produces a
> *rising* number."

> The shape, not your answer *(step 4)*: "**Terminal-value concentration — not yet.** I can
> compute the share, but I can't say whether 72% means the model is fine or broken."

> `codex` will not run? Put your name on a **parking-lot card** — a TA installs it with you
> during the next block. Nothing today is blocked: **ChatGPT desktop app → Codex** and
> **Gemini in the browser** both work without the CLI.

*No gap list, no learning track. That list is the whole point of the next hour.*

---

## The known answer, on the board

FCFF₀ = 100, growth 8/6/5/4/3%, WACC 10%, g 3%, cash 50, debt 300, 50M shares

> FCFF₁ = 100 × 1.08 = **108.00** · PV = 108/1.10 = **98.18**
> ΣPV(5yr) = **448.44** · TV₅ = 132.63/0.07 = **1,894.65** → PV **1,176.43**
> EV = **1,624.87** → equity **1,374.87** → **$27.50/share** · TV share **72.4%**

Your engine must reproduce every one of these within tolerance.

---

## AI off — architecture from memory, two numbers by hand

AI closed. Paper only. You drew this in prework; this is the redo that shows what stuck.

1. **Draw the five parts, in order:** FCFF forecast → discount each year →
   terminal value at Year 5 → bridge to equity → per diluted share.
2. **Hand-calculate Year-1 FCFF and its present value.** These are checkout fields.
   Commit on paper *before* you look at the board.
3. **Predict, then look:** which is larger, the PV of Year 1 or the PV of Year 5?
   Write the answer down, then check the board and see whether you were right *for the
   right reason*.

> The shape, not your answer *(one part, said properly)*: "**Part 3 — terminal value.** It is
> measured at the *end of Year 5*, using Year-5 cash flow grown once by g. That makes it a
> Year-5 amount, so it travels back **five** years, not six."

*A part you can draw but cannot say out loud is a part you do not own yet — mark it on the
gap list now.*

---

## Two tracks at once — 1. Fire the research track

*(~4 minutes. Send, then walk away from it.)*

1. **Get the three files:** the
   [Week 3 page on GitHub](https://github.com/CinderZhang/FIN43900-Fall2026/tree/main/lessons/week-03)
   → `starter/` → download `dcf_starter.py`, `dcf_case.csv`, `dcf_expected_output.csv`.
2. **Colab, the course path:** [colab.research.google.com](https://colab.research.google.com)
   → **New notebook** → **folder icon** (left sidebar) → **upload** icon → select all three
   files. Then, in the notebook cell, type `!python dcf_starter.py` and press **Run** (▶).
   Output *and* the first error both appear **under the cell**.
3. **Same requirements to both systems**, word for word:
   **Codex (in ChatGPT) builds · Gemini checks.**
4. **Send both, then leave them generating.** Do not sit and watch tokens arrive.

> The shape, not your answer: "Here are `dcf_starter.py`, `dcf_case.csv`, and
> `dcf_expected_output.csv`. Implement the four `STUDENT_WORK` functions — `project_fcff`,
> `value_dcf`, `sensitivity_table`, `reverse_dcf_for_growth` — and leave `load_named_values`
> and `validate_case` exactly as they are. Convention: annual end-of-year FCFF in USD
> millions, five explicit years, Gordon-growth terminal value at the end of Year 5, then the
> enterprise-to-equity bridge in the case file. Your code must reproduce **every row** of
> `dcf_expected_output.csv` within its stated tolerance — **0.01** on the cash and per-share
> rows, **0.0002** on `terminal_value_share` — and print the comparison row by row.
> **Invent no assumptions:** every number you use comes from `dcf_case.csv`. Where you think
> an input is missing, stop and name the input you need — do not choose one for me."

*You are hiring an intern engineer, not an oracle. The known answer is the interview.*

*(Both systems down? **Week 1 — Dual-System Output Packet** in Start Here, or the
`COURSE-RUN PROBE:` route from Start Here's **AI Access** page. Python, Colab, or network
down? **Week 3 Offline/No-Code Fallback — DCF and Sensitivity** — same finance, by hand.)*

---

## Two tracks at once — 2. The learning track

*(~6 minutes, while the code generates.)*

> On one screen the machine works **for** you.
> On the other, you put it to work **on** you. That is the whole pattern.

1. **Gap list out.** Pick your **#1 "not yet"** from the opener.
2. Open your other system — Gemini in the browser, or a fresh ChatGPT thread — and run the
   tutor prompt below.
3. **Commit to an answer before you are told.** A wrong answer you committed to is what makes
   the correction stick; a skipped one teaches nothing.
4. **Ungraded, never collected, yours.** No checkout field, no screenshot. Nobody reads it.

> The shape, not your answer: "Quiz me on **why the terminal value is discounted by (1.10)⁵ and
> not (1.10)⁶**, even though it is built from Year-6 cash flow — one question at a time. Don't
> give me the answer until I commit to one. Then correct me in two lines and ask the next.
> Keep going until I get three right in a row."

*This is what the opener's gap list was for.*

---

## Two tracks at once — 3. Validate — your judgment, not the AI's

*(~12 minutes. Your code finished while you were learning.)*

Run the checks **in this order**. A later check means nothing if an earlier one failed.

1. **Known answer** — every row of `dcf_expected_output.csv` reproduced within tolerance.
   A row that is off is a bug, not a rounding opinion.
2. **Boundary** — feed it `g ≥ WACC`, then missing shares, then mixed units.
   It must **refuse**, not return a number.
3. **Shape** — the cash flows grow every year; their present values must **shrink** every
   year. If the PV column does not shrink, the discounting is wrong — stop reading the rest.
4. **Concentration** — report the TV share. **72.4% is normal.** Say *why* out loud: a going
   concern's value mostly lives past any five-year window, so defending this valuation is
   mostly defending g and WACC.

**Record one test that passed and one failure you corrected** — both are checkout fields.

> The shape, not your answer *(a failure record)*: "**Failure:** `terminal_value_year_5` came
> back **1,839.46** instead of **1,894.65**. **Diagnosis:** the numerator used FCFF₅ without
> growing it once — 128.76/0.07 rather than 128.76 × 1.03/0.07. **Fix:** multiplied the
> numerator by (1 + g). **Re-test:** 1,894.65, and enterprise value landed back on 1,624.87."

---

## Transfer to your own company

1. Open your **Week 2 evidence ledger** and your target's filing.
2. Move the reconciled rows into the input table: starting FCFF · the five growth rates ·
   WACC · terminal growth · non-operating cash · debt · diluted shares.
3. **Label every forecast assumption** where it sits —
   `reported fact · normalization · forecast assumption · calculated output`.
4. **Never let AI silently complete a row.** A missing input is a **named gap**, not a number
   the model picked for you while you weren't looking.

> The shape, not your answer *(one labeled row)*: "`growth_year_1 = 0.06` — **forecast
> assumption.** Basis: management guided FY2026 revenue growth of 5–7% in the Q4 earnings
> release; I took the midpoint. FCFF is assumed to grow with revenue because I am holding
> margin and reinvestment flat. This is **not** a reported fact, and it is the first row I
> revisit if margin compresses."

> And one you leave open: "`wacc` — **unresolved.** I have a cost of equity; I do not have a
> defensible cost of debt. The row stays blank and goes in my checkout as the unresolved
> assumption."

---

## The floor, honestly — and your readiness sentence

> **Lab 05's own words:** a failed implementation satisfies the completion requirement only
> when the **known-answer worksheet, the exact error, the attempted test, and a viable next
> action** are all present.

A working engine is the goal. **An honest record of a broken one is the floor** — a real
floor, not a consolation prize.

1. Code runs and reconciles? Validate it, then transfer.
2. It doesn't? **Stop debugging at the wall.** Write the exact error text, the test you
   attempted, the hand worksheet you already have, and the one next action you would take.
3. Either way, **one readiness sentence**: what is ready · what is unsafe · what is next.

> The shape, not your answer: "**Ready** — the synthetic engine reconciles every row and the
> boundary check refuses g ≥ WACC. **Unsafe** — my target's WACC; I have a cost of equity and
> no defensible cost of debt. **Next** — pull the debt footnote and its weighted average rate
> before Thursday's grid."

---

## Checkout

In your open Lab 05 attempt *(Brightspace → Quizzes → Lab 05)*:

Lab Date · teammates/learning partners + personal contribution · stated DCF convention and
output unit · hand-calculated Year-1 FCFF and PV · synthetic EV / equity / per-share /
TV share · **one passed known-answer or boundary test + one failure you corrected** · target rows from the Week 2
ledger + **one unresolved assumption** · AI-use disclosure naming each access path and its
role · **session token (on the board)** · optional artifact link · in-person attendance
declaration · truth attestation · receipt confirmation.

*Before submit: your ungraded **growth note** — what can you build today that you couldn't
last week, and what still feels shaky?*

**Before Thursday — do these:**

1. Watch the terminal-value video segment named on the Week 3 page and answer its question
2. Reread the worked example's **Step 6** and bring your **written WACC-change prediction** —
   Lab 06 grades the predict-before-run habit
3. Bring today's target input table, unresolved rows included

**Lab 06 preview:** attack your own DCF — a WACC/terminal-growth grid, a **reverse DCF**
*(what growth does today's price imply?)*, and two AI systems trying to break your thesis
while you check their sources.

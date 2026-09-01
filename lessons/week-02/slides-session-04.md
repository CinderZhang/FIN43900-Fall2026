# Session 4 — FCFF and the Bridge, With Real Digits
**Week 2 · Thursday · Lab 04: Evidence Ledger and Enterprise-to-Equity Bridge**

---

## Today's run of show

1. The mission: a model contract another analyst could audit
2. **Opener** — tools alive, inputs out *(still nothing typed into AI)*
3. Worked FCFF + bridge mini case — predict, then look
4. Source hierarchy · find the poisoned row · the contamination catalog
5. **Two tracks at once** — research to Codex and Gemini, learning to your gap list;
   **start your quiz attempt when told**
6. Your company: evidence ledger + starter
7. Unit and share-count attack
8. Committee readiness statement
9. **Submit — receipt on screen before you leave**

*You arrived with: your **gap list** from Tuesday · **3–5 pre-staged model inputs**
in ledger format · your target's current primary filing.*

---

## Opener — tools alive, inputs out

Follow the projector. Four steps, then stop.

1. **Open Codex** — ChatGPT's coding agent. The CLI (terminal version) if yours works: open your terminal
   *(Windows: Start → type `PowerShell` · Mac: ⌘-Space → type `Terminal`)*, type `codex`.
   No working CLI? **ChatGPT desktop app → Codex.**
2. **Confirm it launches** — a prompt you could type into is enough. Thumbs up.
   **Type nothing yet.** Today AI opens for real — in the launch block, not here.
3. **Inputs out:** your gap list from Tuesday, and your 3–5 pre-staged rows.
4. **Paired, 2 minutes each way:** walk your partner through **one** of your input rows —
   value + unit, period, source, as-of date — and **why you trust that source for that row**.

> The shape, not your answer *(training case)*: "Row: **diluted shares, 100.4 million** —
> weighted average for FY2024, from the per-share section of the income statement in the
> 10-K filed 2025-02-03. I trust it for this row because it is the company's own audited
> count over the same period as the EBIT I am using. The provider page gave me a *current*
> share count — that is a different object, on a different date."

> `codex` still won't run? **Parking-lot card** — a TA installs it with you during the next
> two blocks. Nothing today is blocked: the ChatGPT desktop app and Gemini in the browser
> both work without the CLI.

*No gap list? Write it now: name the four Tuesday concepts and mark each one.*

---

## The worked mini case (follow along)

EBIT 150 · tax 25% · D&A 40 · capex 60 · ΔNWC 15

> FCFF = 150 × 0.75 + 40 − 60 − 15 = **77.5**

The business earned 112.5 after tax; non-cash D&A comes back;
real money left for equipment (60) and working capital (15).

---

## The bridge, same case

> Equity = EV 1,000 + cash 100 − debt 250 − NCI 20 − pension 10 = **820**
> Per share = 820 / 100 = **$8.20**

Every subtraction is a claim standing in line ahead of you.
On your real company, every row needs a **source and an as-of date**.

---

## Source hierarchy · the contamination catalog

Filed statements > reconciled disclosures > authoritative series >
provider fields (reconciled) > AI summaries (leads only).

**Mechanical — wrong numbers that look right** *(you just met one)*
units · period · currency · share count · provider label ≠ filing definition
→ **correct at the source**

**Economic — honest numbers that poison a forecast** *(the filing is correct)*

*One-time items — the event won't repeat:*
- **One-time expense** — Kraft Heinz: $15.4B goodwill + trademark
  impairment, Q4 2018
- **One-time income** — Tesla FY2023: $5.9B one-time tax benefit ·
  Ford Q4 2021: $8.2B Rivian fair-value gain (fair-value losses followed in 2022)

> Test: **will it be in next year's number, at this size?**
> If not: normalize it out of the base year — or keep it and say so —
> label the row, cite the filing note.

*Basis changes — the measuring stick changed:*
- **Estimate change** — Amazon: server lives 5→6 years (depreciation −$3.2B)…
  then a subset back 6→5 for AI hardware (operating income −$0.7B)
- **Principle / standards change** — LIFO → average cost; leases moving
  on-balance-sheet in 2019
- **"Adjusted" games** — recurring costs excluded from adjusted EBITDA

> Test: **same basis as the years you compare against?**
> If not: reconcile both bases, choose your forecast basis, say why.
> The sin is silently mixing bases.

*The shape, not your answer: "Row: D&A. My target extended server lives last
year (10-K note) — this year's margin isn't comparable to last year's. My
normalization row reconciles both bases; I forecast on the new life, since
it's management's current estimate, and labeled the choice."*

Full table with the filing links: **Week 2 handout → The contamination catalog.**

---

## Two tracks at once — 1. Fire the research track

*(~3 minutes. Send, then walk away from it.)*

1. **Same requirements to both systems**, word for word:
   **Codex (in ChatGPT) as architect · Gemini as checker.**
2. Ask for a **model architecture + evidence schema** for *your* company, including a
   **KISS reverse-DCF skeleton**.
   *KISS = keep it simple: the smallest model that can answer your decision.
   Reverse DCF = what growth does today's price imply?*
3. **Architecture and schema — not a valuation.** No numbers accepted. If it hands you a
   price target, the ask was wrong.
4. **Send both, then leave them generating.** Do not sit and watch the tokens arrive.

> The shape, not your answer: "You are helping me *design* a valuation, not run one.
> Company: [ticker]. I am valuing **one diluted common share** as of [date], in USD
> millions. Give me (a) a model architecture — the inputs, the order they are computed,
> and where each one lives in a 10-K; (b) an evidence-schema table, one row per input:
> item · classification · value + unit · period · source · check · failure mode;
> (c) the smallest reverse-DCF skeleton that could tell me what revenue growth today's
> price implies. **Produce no valuation, no price target, and no estimated numbers** —
> where you would need a number, name the filing line instead."

*You are hiring an intern architect, not an oracle.*

*(Both systems down? **Week 1 — Dual-System Output Packet** in Start Here, or the
`COURSE-RUN PROBE:` route from Start Here's **AI Access** page.)*

---

## Two tracks at once — 2. The learning track

*(~7 minutes, while the proposals generate.)*

> On one screen the machine works **for** you.
> On the other, you put it to work **on** you. That is the whole pattern.

1. **Gap list out.** Pick your **#1 "not yet."**
2. Open your other system — Gemini in the browser, or a fresh ChatGPT thread — and run
   the tutor prompt below.
3. **Commit to an answer before you are told.** A wrong answer you committed to is what
   makes the correction stick; a skipped one teaches nothing.
4. **Ungraded, never collected, yours.** Nobody reads this but you.

> The shape, not your answer: "Quiz me on **why capex comes out of FCFF while D&A goes
> back in** — one question at a time. Don't give me the answer until I commit to one.
> Then correct me in two lines and ask the next. Keep going until I get three right in
> a row."

*This is what Tuesday's gap list was for.*

---

## Two tracks at once — 3. Back to the proposals

*(~7 minutes. The research track finished while you were learning.)*

1. Read both proposals **side by side**. Where do they disagree?
2. Mark each material suggestion `accept` · `modify` · `reject` — **with a finance
   reason**, never a preference.
3. **At least one of each, when the actual outputs support it.** Do not manufacture
   disagreement.
4. The grid is the handout's comparison table: valuation object · FCFF construction ·
   normalization · enterprise-equity bridge · validation tests.

> The shape, not your answer: "**Bridge — modify.** Codex bridged with total debt off the
> balance sheet; Gemini added operating-lease liabilities as debt-like. I take Gemini's
> row, because my FCFF treats lease payments as financing rather than operating — but I
> label the lease policy in the ledger so both halves stay on one convention."

> **Disagreement between the two systems is information** — it names the design decision
> that is actually contested. Agreement is not validation: arbitrate with the filing, the
> definitions, and this morning's known answers.

---

## Your company: the evidence ledger

**All nine rows are Lab 04's required work.** In the room, work them **in this order**:

`revenue → EBIT → tax → D&A → capex → NWC → cash/non-operating → debt/debt-like → diluted shares`

The checkout asks for **four representative rows, including the reconciled/contaminated
one**. **Write those four completely and well before you widen.**

> A complete, sourced partial ledger with its gaps named beats nine unsourced rows.

Each row carries: item · classification (fact / normalization / forecast / output) ·
value + unit · period · source · rationale · check · failure mode.

Two sources sharing a label may measure different things —
never average a discrepancy before explaining it.

---

## Checkout

In your open Lab 04 attempt *(Brightspace → Quizzes → Lab 04)*:
session token on the board · growth note (ungraded, yours) before submit.

Lab Date · teammates/learning partners + your contribution ·
decision, object, valuation date, currency/unit, intended output ·
synthetic FCFF + per-share results · **four representative ledger rows** (including the
reconciled/contaminated one) · AI access paths + accept/modify/reject evidence ·
one independent source reconciliation · **Ready / Unsafe / Next test** ·
in-person attendance declaration · truth attestation · receipt.

**Before Tuesday — do these:**

1. Do the Week 3 prework: the fully worked DCF page with its hand checkpoints —
   the heaviest prework of the month; start early
2. Bring your Lab 04 evidence ledger, corrected rows included — Week 3 builds on it

**Lab 05 preview:** build and validate a five-year FCFF DCF — the training case
by hand first, then your own company.

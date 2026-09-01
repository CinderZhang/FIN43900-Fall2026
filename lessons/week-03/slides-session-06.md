# Session 6 — Attack the DCF
**Week 3 · Thursday · Lab 06: Sensitivity, Reverse DCF, and Conditional Recommendation**

> A model nobody has tried to break is a model you cannot defend.
> Today you break your own, on purpose, before a committee does it for you.

---

## Today's run of show

1. The prediction reveal — what one point of WACC actually does
2. **Opener** — tools alive, artifacts out *(nothing typed into AI yet)*
3. **Paired prediction defense** — direction *and* size, and why
4. Scenario design is causal, not cosmetic
5. **Two tracks at once, inverted** — the AI attacks while **you** compute;
   **start your quiz attempt when told**
6. Your grid, your reverse DCF
7. Source-check the challenges; disposition each one
8. Temperature check *(anonymous, ungraded)*
9. Defend your range aloud
10. **Submit — receipt on screen before you leave**

*You arrived with: your **Lab 05 target input table**, unresolved rows included ·
your **written WACC prediction** from the worked example's Step 6 · your **gap list**.*

---

## The prediction reveal

Prework Step 6 asked you to predict WACC 10% → 11% **before** running it.

> $27.50 → **$23.41** — a **15% drop** from one percentage point.

Direction right but size shocking? That *is* the lesson: this conclusion is **hostage to the
discount rate**. A committee hears that as a **range**, never as a point.

Nothing about the business changed. Only what you charge for waiting.

---

## Opener — tools alive, artifacts out

Follow the projector. Four steps, then stop.

1. **Open both systems.** Codex — ChatGPT's coding agent. The CLI (terminal version) if yours
   works: open your terminal *(Windows: Start → type `PowerShell` · Mac: ⌘-Space → type
   `Terminal`)*, type `codex`. No working CLI? **ChatGPT desktop app → Codex.** Then open
   **Gemini** in a browser tab — today both systems work for you. **Type nothing yet.**
2. **Artifacts out:** your Lab 05 target input table, and your written WACC prediction.
3. **Paired, 2 minutes each way:** defend your prediction — **direction and size** — and say
   *why* you expected the size you wrote.
4. **Solo, 1 minute:** re-mark the four concepts. Anything still "not yet" goes back on the
   gap list, and it is what your learning track gets pointed at next week.

> The shape, not your answer *(step 3)*: "I predicted value falls, maybe 5%. It fell 15%. I had
> the direction right from the discounting formula, but I only counted the five explicit years.
> I forgot the terminal denominator widens from 0.07 to 0.08 — and nearly three-quarters of
> the value lives in that one fraction. **The size lives in the terminal, not in the years I
> could see.**"

> `codex` still won't run? **Parking-lot card** — a TA installs it with you during the attack
> block. Nothing today is blocked: the ChatGPT desktop app and Gemini in the browser both work
> without the CLI.

---

## Scenario design is causal, not cosmetic

A scenario is a coherent story about a business — not three arbitrary growth rates.

- Higher growth usually needs **higher reinvestment**: capex and working capital move with it.
- Higher risk moves **the cash flows and the rate**, not the rate alone.
- Never combine mutually inconsistent "best" assumptions. High growth + low capex + low WACC
  is not a bull case; it is an arithmetic error with a story stapled to it.

> The shape, not your answer *(one coherent bear case)*: "**The story:** a second supplier
> qualifies a competing part and my target loses its price premium. **What moves together, and
> why:** operating margin down ~150bp — that premium *is* the margin; so FCFF₁–FCFF₅ all fall.
> Growth fades one year faster, because the volume was won on that premium. WACC up 40bp,
> because customer concentration rises as the smaller accounts leave first. Terminal growth
> **unchanged at 2.5%** — a lost premium is a level effect, not a claim about the long-run
> economy. Four inputs, one story, and I can say why each one moved."

*Test your own case out loud: if you cannot name the mechanism that ties two moved inputs
together, one of them is decoration.*

---

## Two tracks at once, inverted — 1. Fire the AI bull/bear challenge

> Tuesday the AI built while you learned.
> Today **the AI attacks while you compute.**
> Both directions are the same skill: staying on the loop of two tracks at once.

*(~4 minutes. Send both, then go do your own arithmetic.)*

1. **Both systems, same ask, word for word** — **Codex (in ChatGPT)** and **Gemini**. Each
   returns a **bull** case *and* a **bear** case, aimed at **your Lab 05 base output**.
2. Give each one your base per-share value, your input table, and your stated convention.
3. **Send, then leave them generating.** Your grid does not wait for them.

> The shape, not your answer: "Here is my base DCF for [ticker]: **[per-share value]** per
> diluted share as of **[valuation date]**; annual end-of-year FCFF in USD millions, five
> explicit years, Gordon-growth terminal value at Year 5. Here are my inputs: [paste the input
> table]. Build the strongest **bull** case *and* the strongest **bear** case against this
> valuation — attack the **assumptions**, not the arithmetic. For **every claim, name the checkable source** — filing and section,
> dated release, or published series — **or mark it UNVERIFIABLE**. Give me no price target.
> I am going to source-check one of your load-bearing claims, so do not hand me anything you
> cannot cite."

> Tell it you will check. It changes what comes back.

*(Both systems down? **Week 1 — Dual-System Output Packet** in Start Here, or the
`COURSE-RUN PROBE:` route from Start Here's **AI Access** page. Code or network down?
**Week 3 Offline/No-Code Fallback — DCF and Sensitivity** — the same grid, by hand.)*

---

## Two tracks at once, inverted — 2. While they generate: your grid

*(~14 minutes. The longest block of the day — protect it.)*

1. **WACC / terminal-growth grid:** `sensitivity_table(inputs, wacc_values,
   terminal_growth_values)` — WACC across, g down, per-share value in every cell.
2. **Predict before you read a single cell.** Write it: as WACC rises, value should **fall**;
   as g rises, value should **rise**.
3. **Monotonicity check.** Walk every row and every column. A cell that breaks the direction is
   an implementation bug — find it *before* you interpret anything.
4. **Blank any cell where `g ≥ WACC`.** At g = WACC the formula divides by zero; above it, the
   math claims infinite value. A blank cell is the honest output.
5. **One operating sensitivity** — the driver *your* thesis actually rests on: margin, the
   growth fade, or capex intensity. Predict its direction first, too.
6. **Reverse DCF:** `reverse_dcf_for_growth(inputs, observed_price, lower, upper)`, with today's
   price and its as-of source. It answers exactly one question: **what growth does today's
   price imply?** Then judge it — is that growth plausible for this business, against its own
   history and its industry? Reverse DCF names an expectation; it never proves the market wrong.
7. **Terminal-value share, base case and one stress case.** Report both, and say what changed.

> The shape, not your answer *(a reverse-DCF reading)*: "Holding my margin, WACC 9.2%, and
> terminal growth 2.5% fixed, today's price implies **7.1%** five-year FCFF growth. The company
> has compounded 4–5% through the last cycle and guides to 5–7%. So the price is paying for the
> top of guidance holding for five years — plausible, not free. That is what I have to believe
> to call it fairly valued."

---

## Two tracks at once, inverted — 3. Back to the challenges

*(~8 minutes. They finished while you were computing.)*

1. Read both cases **side by side**. Where do they disagree about *your* company?
2. **Pick one load-bearing claim from each system** — one whose failure would move your range.
   Not a decoration.
3. **Source-check those two.** Go to the filing, the dated release, or the published series.
   An AI citation is a **lead**, not evidence.
4. **Disposition each:** `accept` · `qualify` · `correct` · `reject` — **with the source named.**

> The shape, not your answer *(one disposition)*: "**Gemini, bear case — 'gross margin has
> declined four consecutive quarters.' → CORRECT.** The segment tables in the last 10-Q show
> three consecutive declines and a fourth quarter flat at 41.2%, not down. The *direction* of
> the argument survives; the 'four consecutive' framing does not. I keep the margin-pressure
> driver, sourced to that 10-Q, and drop the streak claim — it mattered, because the streak was
> the entire reason the case pushed a fifth year of compression."

> Two systems agreeing is not validation. It is two models trained on overlapping text.

---

## Temperature check

**Anonymous. Ungraded. No names.** Three questions:

1. What is working?
2. What is confusing?
3. One change you would make.

*Answers get addressed openly next Tuesday — in both sections, out loud, including
"no change, and here is why."*

---

## Defend your range

> "My range is **[low–high]** vs price **[P] as of [date]**. Most sensitive to **[driver]**.
> I recommend **[action]** only if **[condition]**; revisit if **[trigger]**."

*(The handout carries the fuller version, which also states your terminal-value share.)*

> The shape, not your answer: "My range is **$41.10–$57.80** per diluted share versus a price of
> **$47.30**, taken from the exchange's own quote page at my stated valuation date. Most
> sensitive to **terminal growth** — moving it 2.5% → 3.0% carries the range past the price on
> its own. For a committee with no position I recommend **watch-defer**, and I would move to
> initiate only if **the guided margin recovery shows up in two consecutive quarters**. I
> revisit immediately if **the second supplier is qualified**, because that single event is
> what my whole bear case is built on."

*A range you cannot say aloud in four sentences is not a conclusion yet.*

---

## Merit checkout

In your open Lab 06 attempt *(Brightspace → Quizzes → Lab 06)*:

Lab Date · teammates/learning partners + personal contribution · decision and valuation
convention · low/base/high values and **the causal driver changed in each** · WACC/g grid
excerpt and monotonicity result · **terminal-value shares (base and stress) and
interpretation** · reverse-DCF solved assumption and its economic interpretation · AI
bull/bear claim checks **with sources and dispositions** · range, conditional recommendation,
and reversal trigger · **session token (on the board)** · optional artifact link · in-person
attendance declaration · truth attestation · receipt confirmation.

*Before submit: your ungraded **growth note** — what can you defend today that you couldn't
on Tuesday, and what still feels shaky?*

**Before Tuesday — do these:**

1. Watch the relative-valuation segment named on the Week 4 page and answer its question:
   what are the four steps before applying a multiple, and why can a seemingly consistent peer
   set still mislead?
2. **Without AI**, write your peer-selection policy and predict one reason a
   precedent-transaction multiple may exceed a trading multiple — **freeze the policy before
   you ask any AI for a single peer name**
3. Bring today's DCF range, your valuation date, your bridge conventions, and one candidate
   peer you can defend

**Lab 07 preview:** *Comparable-Company Policy and Implied Range* — your peer policy written
before AI proposes a name, then converted into an implied per-share range you set beside
today's DCF.

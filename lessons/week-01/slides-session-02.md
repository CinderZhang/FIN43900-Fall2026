# Session 2 — Numbers That Lie With a Straight Face
**Week 1 · Thursday · Lab 02: Identify Your Target**

---

## Today's run of show

**You arrive with:** a working toolchain · one company you are curious about
(it's in your Lab 01 checkout) · the DRIVER video watched.
**Today you identify your valuation target.**

1. Parking-lot answers + warm-up cases from the video
2. **AI off, solo:** write your nine-line screening policy (handout Part B)
3. **AI on, pairs:** ChatGPT vs Gemini on the same policy
4. **Apply it** in `screening_starter.py` — **start your quiz attempt when told**
5. **AI off:** validate — one definition check + one stability change
6. **Identify your target** — the 45-second defense
7. **Submit — receipt on screen before you leave**

---

## The lesson of the week *(from your prework video)*

Two providers can both report a "PEG ratio" (price/earnings-to-growth —
a popular value-for-growth shortcut) — and differ by **6×**,
because one uses trailing growth and one uses forward estimates.

**Shared labels can hide different measurements.**
Today you learn to catch that before it costs money.

---

## Warm-up probes

- A stock shows 400 insider "buy" events this quarter. Bullish?
  → Most insider events are compensation mechanics, not conviction.
- A screen ranks a company #1 on "value." Which definition of value?
- Your curiosity company from Tuesday: what single fact would make
  you drop it? *(If you can answer that by the end of today, you have a policy.)*

---

## Before AI: write your screening policy (solo)

**Nine written lines — draft them on Part B of the Week 1 handout**
*(printed copies in the room; also on the Week 1 page)*. This is a research
decision: which company earns your next hundred hours, **not a buy/sell call**.

| Write one line for each | Example of a real answer |
|---|---|
| **Decision user** — who acts on this screen? | a junior analyst proposing a coverage add |
| **Decision** — what does it select? | one company admitted for valuation research |
| **Universe** — which companies can enter? | US-listed public operating companies |
| **Exclusions** — who is out, and why? | banks, insurers, REITs, funds — no FCFF fit |
| **Criteria** (two) — which observable measures? | annualized return; annualized volatility |
| **Definitions** — measured how, over what period? | three years of daily adjusted prices |
| **Thresholds / weights** — pass lines or ranking? | return ≥ 8%, volatility ≤ 25%; lower volatility ranks first |
| **Success test** — what would prove it useful? | survivors still look sound against the filing |
| **Disqualifier** — what overrides a high score? | missing data > 1% or no current filing |

> The example column is the *shape* of an answer — copy nothing from it.
> If you cannot name the fact that would kick your top-ranked company off
> the list, you do not have a policy — you have a mood.

*FCFF = free cash flow to the firm — for now it just means "an operating
business we can value"; Week 2 teaches it with digits. REITs = real-estate
investment trusts.*

---

## AI on: the two-AI comparison

*(pairs — one partner sends the policy to ChatGPT, the other to Gemini)*

1. **Same policy to both systems** — word for word
   *(fallback: the **Week 1 — Dual-System Output Packet** in Start Here, or the
   `COURSE-RUN PROBE:` route from Start Here's **AI Access** page)*
2. **Author one follow-up probe** — write your predicted answer *first*
   *(the shape, not your answer: "Probe: which criterion is most sensitive to the
   three-year lookback? I predict volatility.")*
3. **Mark one material suggestion** `accept` · `modify` · `reject` · `unresolved`

> Two AIs agreeing is a coincidence of training data,
> not a fact about the world.

---

## Apply, then validate

*Open `screening_starter.py` in Colab: colab → File → Upload → run the cell.
Edit only the marked `STUDENT_WORK` lines. Stuck = hand up.*

**Apply (AI on):**
1. Implement your transparent rule — no silent definition changes
2. Network or provider down? Live instructor diagnostics or
   `offline-screening-case.csv` — *same finance either way*

**Validate (AI off):**
3. Check **one load-bearing definition** against the pre-staged provider/filing capture
   *(example: does this provider's "return" include dividends, or price only?)*
4. Run **one ranking-stability change** — one threshold, weight, lookback, or exclusion —
   and compare candidate order
   *(example: lookback three years → five years — is the top company still on top?)*

> `No material change` is a valid result when the test is genuine.
> AI agreement is not validation.

---

## The oral gate — your 45-second defense

Six parts, in order: **target · two dated facts · most sensitive assumption ·
remaining unknown · decision · reversal trigger**

> Training-case example — the *shape*, not your answer:
> "My target is MSFT: it passed my screen on the August training data and its
> latest 10-K is on file. The ranking hinges on my three-year window — I have
> not tested five — so that is my open unknown. I take it as my target, and I
> reverse if volatility crosses my 0.25 ceiling on the longer window."

*(Mapped: target → MSFT · facts → screen pass + 10-K on file · assumption →
the three-year window · unknown → five years untested · decision → take it ·
reversal → the 0.25 ceiling.)*

A defensible **`no admissible target yet`** with a named next candidate
is a strong outcome.

Explain it aloud with the evidence visible.
Explanation is ownership evidence — silent familiarity hides gaps.

---

## Checkout

Session token on the board · growth note (ungraded, yours) before submit.

Lab Date · teammates + contribution · problem and decision · your nine-line
policy · AI-use record · data and evidence · independent validation ·
stability test · **your target** (company · unknown · reversal trigger) ·
optional artifact link · **session token** · in-person attendance
attestation · receipt.

**The company that survives your screen is your Project 1 company.**

**Before Tuesday — do these:**

1. Watch the assigned [three-lens video (23 min)](https://youtu.be/LlmBzbQbNwQ) —
   the template for everything you build in Weeks 2–4
2. Save your target's latest primary filing — the 10-K (annual) or 10-Q
   (quarterly) report it files with the SEC — where you can open it in class
3. Write one sentence: the decision this valuation will support, and for whom

**Lab 03 preview:** write your before-AI valuation baseline — Project 1 **Edition A**,
the frozen proof that the judgment in this project is yours.

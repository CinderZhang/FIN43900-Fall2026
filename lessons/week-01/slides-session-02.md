# Session 2 — Numbers That Lie With a Straight Face
**Week 1 · Thursday · Lab 02: Screen Validation and Research Admission**

---

## Today's run of show

1. Parking-lot answers, then rebuild Tuesday from evidence
2. AI off: audit your own screening policy
3. Pair red team — attack criteria, exclusions, the disqualifier
4. AI on: implement in `screening_starter.py` — **start your quiz attempt when told**
5. AI off: independent validation + ranking-stability test
6. Missing-data / provider-disagreement attack
7. Hostile-committee defenses
8. **Submit — receipt on screen before you leave**

---

## The lesson of the week *(from your prework video)*

Two providers can both report a "PEG ratio" — and differ by **6×**,
because one uses trailing growth and one uses forward estimates.

**Shared labels can hide different measurements.**
Today you learn to catch that before it costs money.

---

## Warm-up probes

- A stock shows 400 insider "buy" events this quarter. Bullish?
  → Most insider events are compensation mechanics, not conviction.
- Your screen ranks a company #1 on "value." Which definition of value?
- What single fact would disqualify your provisional target?

---

## Validate your admission

*Open `screening_starter.py` in Colab: colab → File → Upload notebook/file →
run the cell. Edit only the marked `STUDENT_WORK` lines. Stuck = hand up.*

1. Take your Session-1 target and policy
2. Trace each screening input: **which provider, which definition, which period**
3. Reconcile one input against the primary source (filing or authoritative series)
4. Run the changed-input test your policy names
5. Decision: **admit for research · replace · conditionally admit**

---

## The oral gate — your 45-second defense

Six parts, in order: **target · two dated facts · most sensitive assumption ·
remaining unknown · decision (admit / replace / hold) · reversal trigger**

> Training-case example — the *shape*, not your answer:
> "Admit MSFT for research: it passed my screen on the August training data and
> its latest 10-K is on file. The ranking hinges on my three-year window — I have
> not tested five — so I admit it, and I reverse if the longer window drops it
> below my return bar."

Explain it aloud with the evidence visible.
Explanation is ownership evidence — silent familiarity hides gaps.

---

## Checkout

Session token on the board · growth note (ungraded, yours) before submit.

Lab Date · teammates/learning partners · admission decision + evidence ·
definition reconciliation · changed-input result · AI access paths ·
in-person attendance declaration · truth attestation · receipt.

**The company you admitted today is your Project 1 company.**

**Before Tuesday — do these:**

1. Watch the assigned [three-lens video (23 min)](https://youtu.be/LlmBzbQbNwQ) —
   the template for everything you build in Weeks 2–4
2. Save your company's latest primary filing (10-K or 10-Q) where you can open it in class
3. Write one sentence: the decision this valuation will support, and for whom
4. Confirm both required subscriptions reach Codex and Gemini Pro

**Lab 03 preview:** write your before-AI valuation baseline — Project 1 **Edition A**,
the frozen proof that the judgment in this project is yours.

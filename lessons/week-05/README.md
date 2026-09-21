# Week 5 — Pro-Forma Financial Modeling I: Build the Base Case


## Mission

Tuesday: build a five-year three-statement pro-forma engine from an instruction, and prove it on
the Asbury (ABG) case from the video. Thursday: your own company through it — history from the
filings, every assumption labelled, statements that balance, one value per share.

For four weeks the steps were projected one at a time. That was the training program, and it
worked: you have a workspace, a company, and a DCF. This week is your desk. Every one of you has a
different company, so there is no answer to copy. What does not change: the clock on the screen,
the checkpoints, your AI partner, your teammate, and me.

## You arrive with

- your Lab 05 `dcf.py` and your Lab 08 peer work, in your Course/Work Folder and on GitHub;
- your company's three most recent 10-Ks, open;
- the AI chat you have been working in since Week 3 — this week resumes it;
- Part 1 of the pro-forma video, watched (prework below).

## Outcomes

- Build a three-statement pro-forma with cash computed last, and prove it on a known answer.
- Explain why a balance sheet that does not balance is a bug, not a forecast — and make the model
  refuse to value one.
- Earn each assumption from the filings and label it history, guidance or judgment, with the reason.
- Name the one line that makes your company different, and model it consistently.
- Review a teammate's model with fresh eyes, and defend your own.

## The two sessions

- **Session 9** — build the engine, prove it on ABG. Checkout: [Lab 09](lab-09-proforma-build.md).
- **Session 10** — your company through it. Checkout: [Lab 10](lab-10-proforma-your-company.md).

Dates and points: the course schedule and Brightspace.

## Teams this week

Two people, new partner each Tuesday. A team always holds two companies. Your partner's job is
named in each lab: explain before you build, swap and break on Tuesday, attack one judgment on
Thursday. Checkouts stay individual: your company, your files.

## Prerequisites and prework

**Before Tuesday — about 45 minutes.**

1. Watch [Pro-Forma Valuation with AI, Part 1 — Build the base case](https://youtu.be/O4PeC2PqwRY)
   (27 min). Open the [Part 1 slides](pro-forma-abg-tutorial.md) alongside; press **N** for the
   spoken text under any slide you want to reread.
2. **Answer:** which three judgments carry the ABG valuation, and why is cash the last line the
   model computes? Write it in your own words; you will explain it to your partner first thing.
3. Reopen your Course/Work Folder in **VS Code → File → Open Recent** and run `python dcf.py`.
   *Expect:* your Week 3 values. If not, debug with your AI before class.

**Before Thursday — about 30 minutes.**

1. Have your company's three most recent 10-Ks open, and find its same-store or organic growth
   disclosure (MD&A) if it has one. Ask your AI where to look; read the page yourself.
2. Write one sentence: what is the line that makes your company different from a manufacturer,
   the way floor plan is for a car dealer? If you cannot find one, say so — that is an answer.

## DRIVER this week

Define: the same question for everyone — what are five years of your company's statements worth,
built from assumptions you can defend? Represent: the assumption set, labelled. Implement: the
engine from one request. Validate: the known answer, then the checks that stop the model. Evolve:
Thursday, your company. Reflect: to your partner, before the checkout.

## Package map

- [`pro-forma-abg-tutorial.md`](pro-forma-abg-tutorial.md) — the two videos, the slides with the
  spoken text, captions. The teaching lives here.
- `student-prework.md` — generated from the prework section above.
- `lab-09-proforma-build.md`, `lab-10-proforma-your-company.md` — the checkouts.
- `instructor-guide.md`, `ta-probes-and-key.md`, `verification.md` — instructor only.

## Brightspace order

Watch Part 1 → Lab 09 → Lab 10. The Brightspace module carries the standard pointer to this page.

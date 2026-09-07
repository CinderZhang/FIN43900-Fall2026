# Optional Open-Ended Challenge — Finish the Company DCF

**Ungraded. Never collected. Nobody reads this.** The in-room floors this week were Tuesday's
twelve matching lines with the WACC probe, and Thursday's five sourced rows, your company's
twelve lines, the grid, the implied growth at today's price and a one-condition call. This page is what to do with the rest of the
week if you want to be the person in the room who has actually done it. Start with the piece
Thursday pointed here.

## Let AI argue both sides, then judge it

Send this to your AI partner:

> Here are my company inputs, my sources, and my per-share range. Give me the strongest bull
> case and the strongest bear case against these numbers. For each, name the operating
> mechanism, the single input it would move, and one factual claim that — if false — would
> collapse that case. Do not invent data I did not give you; if a claim needs a source I have
> not provided, say so.

When it comes back, do the one thing that matters: **pick one load-bearing claim and check it
against an original source.** Then dispose of it — accept, qualify, correct, or reject — and
say what that does to your model.

*The shape, not your answer:* "The bear case says margin pressure is permanent. My scenario
ends it after year two, and the filing's MD&A describes the pricing action as contractual
through next year only. I qualify it: the pressure is real but time-boxed, so terminal growth
stays unchanged and only the first two years move."

Two AI systems agreeing is not independent evidence. A source is.

## Your company, all the way through

1. Resolve every `unresolved` and `placeholder` row for your own company, each with a unit, an
   as-of date, and an exact locator: page and statement name, not just a link.
2. Estimate a real WACC instead of the training case's 10%. Cost of equity from a risk-free
   rate, a beta, and an equity premium; after-tax cost of debt from the debt note and the
   effective tax rate; then weight them by market values, not book values. Write down the date
   and source of every component.
3. Rerun `dcf.py` on the resolved rows. Report the value per diluted share, the terminal-value
   share, and the price you are comparing against with its timestamp.
4. Say what you would need to believe for the market price to be right. If you cannot say it in
   one sentence, your model is not yet telling you anything.

## The stretch — when the terminal value owns the model

Hold your price fixed and find two economically different assumption sets that produce roughly
the same per-share value: one leaning on explicit-period operating performance, the other on
terminal assumptions.

1. Report the terminal-value share and the implied reinvestment logic of each.
2. Ask AI which case is "better," then reject the framing. State which is more *supportable*
   for this company, and what evidence would settle it.
3. Close AI and explain, without it, why a stable point estimate can hide two unstable and
   incompatible stories about the same business.

Nothing here is submitted. It can, however, become real sensitivity evidence in your Project 1
package, and the WACC you build now is a WACC you will not have to build later.

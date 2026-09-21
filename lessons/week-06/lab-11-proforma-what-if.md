<!-- AUTHORED HOME. Built under the 2026-09-06 rulings in OWNER-DECISION-GATES.md and Gate 7
     (two full weeks of building; practise changing and researching assumptions; the Locked
     Changed-Input Record is practised here before Project 1). -->

# Lab 11 — Pro-Forma What-If: Shocks, a Named Case, and the Locked Prediction

**One thing today: rerun the model under changed assumptions, with a locked prediction written before every change.**

**Category:** Tuesday completion checkout, **25 or 0**.


**You arrive with:** your company's pro-forma from Lab 10 · `proforma.py` for ABG · Part 2 watched ·
your two written predictions · a new partner.

## Open your workspace

1. **VS Code → File → Open Recent** → your Course/Work Folder.
2. **Terminal → New Terminal.**
3. Run your pro-forma. *Expect:* Lab 10's values. If not, debug with your AI until they match.

**Something not working?** Debug with your AI: paste the exact command and the exact error text.

## D — the question, the same for everyone

> **Which assumptions carry the value, by how much, and what would have to be true for today's
price to be right?**

Paste it into your chat. Today you practise on ABG first, then run your own company.

**Exchange predictions first** (five minutes, no screen): read your partner your two predictions —
which assumptions move value most, and which way. Your partner writes them down. Swap. Neither of
you runs anything until both are written. That written line is the Locked Changed-Input Record;
Project 1 asks for it.

## R — the shocks and the case

| Shock, one at a time | Worse | Better |
|---|---|---|
| Gross margin | −1 point | +1 point |
| Capital spending | +50 a year | −50 a year |
| Organic growth | −1 point | +1 point |
| SG&A ÷ gross profit, whole path | +1 point | −1 point |
| Term-debt interest rate | +1 point | −1 point |
| Floor-plan (or your company's line) rate | +1 point | −1 point |
| Impairment | +40 a year | −40 a year |
| Inventory days | +5 | −5 |

Named downside case, all at once: margin −1, growth −1, cost ratio +1, floor-plan rate +1.

## I — one request that reruns the model

Send this to your chat, word for word:

> Add to my pro-forma a function that reruns the whole model with one or more assumptions
> changed and returns value per share. Use it to print: a table of the shocks I paste below, worse
> and better side by side with the swing; the value under a named downside case with several
> assumptions changed together, beside the value you would get by adding the single shocks;
> and, holding everything else fixed, the cost of equity, the gross margin and the capital spending
> that would each make the value equal a share price I give you, found by bisection over wide
> brackets (cost of equity 5% to 30%; gross margin 5% to 30%; capital spending 0 to 1,000). Keep the
> balance check running on every rerun and refuse any rerun that does not balance.

Paste the shock table and the downside case under it. Save the returned file in your open folder.
Run it on ABG first. *Expect:* a shock table, the named case beside the sum of shocks, and three
price-implied values.

## V — prove it on the ABG known answer (price 183.29)

| Rerun | Value per share |
|---|---|
| Gross margin −1 / +1 point | 256.1 / 327.4 |
| Capital spending +50 / −50 | 258.3 / 325.2 |
| Organic growth −1 / +1 point | 270.2 / 314.1 |
| Named downside case | 210.0 |
| The four single shocks added instead | 206.7 |
| Cost of equity implied by 183.29 | 13.82% |
| Gross margin implied by 183.29 | 14.08% |
| Capital spending implied by 183.29 | 406.6 |

Match to the decimal, or debug with your AI until they match. Explain to your partner why the
named case is not the sum of the shocks: lower margin means lower inventory means lower floor plan
means lower interest — every link you built in Lab 09.

## E — your company, prediction first

1. For each of your two predicted assumptions, before you run: write the predicted direction and
   rough size of a one-point (or 50, or 5) change, in your file, dated.
2. Run the shocks on your company. Under each prediction write what happened and one sentence
   reconciling the two. A wrong prediction with an honest reconciliation is the point of the record.
3. Run your named downside case and the three price-implied solves on your company's current price
   and date. Write the sentence the video uses: "the market is not pricing a slightly worse company;
   it is pricing one that …".

## Floor

The ABG table matched; your two locked predictions reconciled; your named case and one price-implied
value for your company. You submit individually.

## Beta — Learn on your own

1. What is it? 2. How is it measured (sixty monthly returns against the market; the slope; the
standard error)? 3. Explain to your partner why the video's 10% was conservative for ABG.

## Reflect

Explain to your partner: 1. which of your predictions was wrong and why; 2. what the price-implied
table says about your company in operating language.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

**Thursday preview:** the two-line message, the one page, and a sceptic across the table.

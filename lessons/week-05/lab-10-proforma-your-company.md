<!-- AUTHORED HOME. Built under the 2026-09-06 rulings in OWNER-DECISION-GATES.md and Gate 7
     (pro-forma is a method, not an algorithm; the personalization is the skill; own company;
     partner fresh-eyes review). -->

# Lab 10 — Pro-Forma: Your Company Through It

**One thing today: your company's filings become a labelled assumption set, five years of statements that balance, and one value per share.**

**Category:** Thursday merit checkout; anchors below.


**You arrive with:** `proforma.py` matching the ABG known answer · your company's three most recent
10-Ks, open · your Lab 09 chat · your one sentence on the line that makes your company different.

## Reopen and rerun

1. **VS Code → File → Open Recent** → your Course/Work Folder.
2. **Terminal → New Terminal.**
3. `python proforma.py`. *Expect:* the ABG values from Tuesday. If not, debug with your AI until
   they match.

## D — the question, the same for everyone

> **What are five years of your company's statements worth, built from assumptions you can
defend?**

Paste it into your chat, then name your company and its ticker.

**Explain to your partner first:** the line that makes your company different, and what it will do
to your model. Your partner asks one question. Swap.

## R — the history, then the assumptions

1. Ask your AI to pull, from your three 10-Ks, the history grid from Part 1 for three years:
   revenue, gross profit, SG&A, net income, inventory, PP&E, shareholders' equity, each with the
   filing it came from. Open the filing and check two of them yourself. *Expect:* three years of
   history with a source on every item; anything you could not confirm marked unresolved.
2. Ask for the ratios the video computes: gross margin, SG&A ÷ gross profit, inventory days,
   depreciation ÷ PP&E, capital spending from the filing beside the data provider's field, tax
   rate, and reported growth beside any organic or same-store growth the MD&A discloses.
   *Expect:* a ratio table for three years; the growth the stores already owned, if disclosed.
3. Write the assumption set as a table with three columns: value, label (history, guidance,
   judgment), reason. Every judgment gets a reason in your words. Where your company has no
   floor plan, that row becomes the line you named — or a stated "none", which is also an answer.

**If your company loses money or has negative free cash flow:** build the statements anyway; the
checks still apply. Write "negative FCFE" against the years where it is, value only what is
positive, and say in one sentence why a terminal value on a negative cash flow is not a number.

## I — your company through the engine

1. In your chat: "Replace the ABG opening balance sheet and assumptions with these," and paste your
   table and your opening balance sheet.
2. Save the returned file as a new Python file in your open folder. Run it.
   *Expect:* five years that balance, the check block, a value per share.
3. If it refuses, read the year and the gap it names. Fix the assumption or the link; do not
   silence the check.

## V — the check block, and the price

1. The check block reads zero in every year and cash stays at or above your floor. If a year draws
   the revolver, say why in one line.
2. Ask your AI for today's share price and its date. Write one sentence: the model says X, the
   market says Y, on the same share count. No recommendation; a question.

## E — fresh eyes

Your partner opens your assumption table and attacks **one** judgment label: "why that number,
and what would change it?" You answer in two sentences, in your file, under the table. Then you
attack theirs. Record the attack and the answer; the attack is graded on its quality, the answer
on its reasons.

## Floor

Five years for your company that balance in every year, a labelled assumption set with a reason
on every judgment, one value per share, and one partner attack answered. You submit individually.

## Organic growth — Learn on your own

1. What is it? 2. How does the MD&A disclose it for your company (same-store, organic, comparable)?
3. Explain to your partner why the video carries 1.8% for ABG when reported growth was 4.7%.

## Reflect

Explain to your partner: 1. which of your labels you would defend the longest, and why; 2. what
one number in the filing surprised you.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

## Merit anchors — five criteria, 5 points each, 25 in total

**4** = one minor weakness; **2** = an important link incomplete; **1** = minimal; **0** = missing
or fabricated. Score one underlying defect once.

| Criterion | 5 | 3 | 0–1 |
|---|---|---|---|
| History and sources | every history item for three years traced to a filing; two confirmed by hand | sources present, one material line unconfirmed | provider numbers pasted as facts |
| Assumptions and labels | every line labelled; every judgment carries a reason in the student's words | labels present, reasons thin or generic | unlabelled or copied from ABG |
| Statements and checks | the check block prints zero every year and the model refuses when broken | balances but the refusal is missing | does not balance, or cash is typed |
| Personalization | the company-specific line named and modelled consistently, or "none" argued | named but modelled inconsistently | ABG's structure applied unchanged |
| Partner review | one attack recorded and answered with reasons; the student's own attack is specific | attack or answer generic | missing |

**Next week:** Part 2 of the video; the same model taken apart, one assumption at a time, and a
locked prediction before every change.

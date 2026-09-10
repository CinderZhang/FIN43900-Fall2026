# Lab 07 — Comparable-Company Policy and Implied Range

**One thing today: learn and practice a P/E comparison on the Asbury case.**

**Category:** Tuesday completion checkout, 25 or 0.


**You arrive with:** your Week 3 DCF and sources, your Course/Work Folder, your Lab 06 chat,
and the [worked case](teach-comps-worked-example.md) read through the P/E calculation.

## Reopen and explain

1. **VS Code → File → Open Recent** → your Course/Work Folder. Open your Week 3 analysis.
2. **Terminal → New Terminal** → run your existing DCF with your usual Python command.
   *Expect:* the last saved valuation, with its assumptions visible.
3. Open **Codex** and **Google Antigravity** inside VS Code. Resume your Lab 06 chat.
   Any AI partner is acceptable; no grade depends on an extension or account.
4. Before AI, explain to a partner what drives your DCF range. Write down what you cannot
   yet explain about a peer multiple. *Expect:* a specific question to investigate.

## Define/Discover — learn what P/E can tell you

<!-- discover:start -->
**Research and learn:** start with [Why use another company's price?](teach-comps-worked-example.md#why-use-another-companys-price).

1. **What is price-to-earnings (P/E)?** What do price per share and earnings per share measure?
   What does a P/E multiple tell you?
2. **Why use it?** How does comparing earnings help you compare differently sized companies?
   What does this add to your discounted cash flow valuation?
3. **When is it useful—or misleading?** What must match between companies? What happens
   with negative earnings, unusual profits, or different growth prospects?

**Explain to your partner:** why a lower P/E does not automatically mean a better investment.
Then ask: what would my company's share be worth at comparable companies' P/E multiples?
<!-- discover:end -->

## Represent — understand the case's peer policy

Use the Asbury case today. Before AI, explain why franchised vehicle retail and service/parts
matter more than an industry label. Read the case's business evidence for AutoNation and Group 1.
Decide **use / qualify / exclude** for each and explain the business difference behind your decision.
*Expect:* a comparison you can justify before seeing which price you prefer.

## Implement — reproduce the real case

The instructor works the case first. Use the case's frozen inputs below, then send the build
request. While AI writes the calculation, work out one implied price yourself.

<!-- generated:case-inputs:start -->
<!-- Generated from teach-comps-worked-example.md by ../build_week04_views.py; edit the source. -->
| Company / role | December 31, 2024 closing price | FY2024 total GAAP diluted EPS |
| --- | ---: | ---: |
| Asbury Automotive (ABG), target | $243.03 | $21.50 |
| AutoNation (AN), candidate peer | $169.84 | $16.92 |
| Group 1 Automotive (GPI), qualified candidate peer | $421.48 | $36.81 |

*Retrospective training comparison: year-end prices paired with subsequently reported annual earnings. [Case sources and definitions](teach-comps-worked-example.md).*
<!-- generated:case-inputs:end -->

<!-- build:start -->
> Write one standard-library Python file with editable target/peer inputs at the top.
> Deduplicate peers and exclude the target. Compute peer P/E = price / diluted EPS and
> median P/E. Multiply minimum, median and maximum peer P/E by target EPS for implied prices.
> Retain full precision; display multiples to six decimals, prices to cents. Missing or
> nonpositive prices or EPS: label affected calculations not meaningful. One valid peer:
> reference estimate, no range; none: no usable peers. For each peer removal, print the
> remaining median-implied price and dollar change from the full-peer estimate, using
> unrounded values; if none remain, no estimate. Never bridge P/E with cash/debt.
> Do not fetch data or install packages. Give the exact run command using my working Python command.
<!-- build:end -->

**VS Code → New File** → save the returned code as a Python file in your open folder.
**Terminal → New Terminal** → run the exact command AI gives you. *Expect:* calculated
peer multiples and implied prices, not pasted answers.

## Validate — check before trusting

<!-- generated:case-checks:start -->
<!-- Generated from teach-comps-worked-example.md by ../build_week04_views.py; edit the source. -->
| Check | Result |
| --- | ---: |
| AutoNation P/E | 10.037825× |
| Group 1 P/E | 11.450149× |
| Peer median P/E | 10.743987× |
| Asbury peer-implied range | $215.81–$246.18 |
| Asbury at peer median | $231.00 |
| Remove GPI: remaining AN estimate | $215.81 |
| Change from two-peer midpoint | −$15.18 |
<!-- generated:case-checks:end -->

Compare with the case answers. Predict what happens when the higher-multiple peer is removed,
then read the leave-one-out result. If results disagree, debug with your AI using your inputs,
exact command and output. *Expect:* you can explain the direction and the loss of a range.

## Evolve — change the peer set

Use the Asbury calculation. Before reading the result, predict what removing Group 1 will do.
Read the leave-one-peer-out output; explain the price change and why one remaining peer gives
a reference estimate rather than a range. Keep your original peer decision unless business
evidence warrants changing it. *Expect:* an explanation of the result, not a preferred answer.

## Reflect — explain before applying

Explain to your partner what P/E measures, why each case peer belongs or needs qualification,
and why the comparison does not prove Asbury is fairly valued.

**Floor:** the Asbury calculation checked, case peer decisions explained, and the changed-peer
result interpreted. You submit individually.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

**Before Thursday:** follow [Week 4 prework](student-prework.md). Bring this working calculator
and your Week 3 DCF; Lab 08 applies the method to your own company.

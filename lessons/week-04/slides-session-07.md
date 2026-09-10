# Session 7 — Comparable Means Defensible



1. Reopen and explain
2. **Define/Discover** — the comparison question
3. **Represent** — policy before names
4. **Implement** — build the worked case
5. **Validate** — check the result
6. **Evolve** — change the case peer set
7. **Reflect** — defend what the comparison supports
8. Checkout

Open [Lab 07](lab-07-comparable-policy.md).

---

## Reopen and explain

1. **VS Code → File → Open Recent** → your Course/Work Folder.
2. Open your Week 3 analysis. **Terminal → New Terminal** → rerun your saved DCF.
3. Open **Codex** and **Google Antigravity** inside VS Code; resume your Lab 06 chat.
4. Before AI, explain to your partner what drives your DCF range. Write one thing you
   cannot yet explain about peer multiples.

**Expect:** your prior result and a specific question to investigate. Any AI partner is acceptable.

---

## Define/Discover — understand P/E first

<!-- generated:discover:start -->
<!-- Generated from lab-07-comparable-policy.md by ../build_week04_views.py; edit the source. -->
**Research and learn:** start with [Why use another company's price?](teach-comps-worked-example.md#why-use-another-companys-price).

1. **What is price-to-earnings (P/E)?** What do price per share and earnings per share measure?
   What does a P/E multiple tell you?
2. **Why use it?** How does comparing earnings help you compare differently sized companies?
   What does this add to your discounted cash flow valuation?
3. **When is it useful—or misleading?** What must match between companies? What happens
   with negative earnings, unusual profits, or different growth prospects?

**Explain to your partner:** why a lower P/E does not automatically mean a better investment.
Then ask: what would my company's share be worth at comparable companies' P/E multiples?
<!-- generated:discover:end -->

---

## Represent — understand the case peers

Use Asbury today. Read the business evidence in the [worked case](teach-comps-worked-example.md).

1. What business economics make AutoNation and Group 1 candidates?
2. Which differences deserve a qualification?
3. Decide **use / qualify / exclude** before seeing which price you prefer.

**Expect:** explain why a peer belongs; sharing an industry label is not enough.

---

## The real case — value Asbury from two peers

<!-- generated:case-inputs:start -->
<!-- Generated from teach-comps-worked-example.md by ../build_week04_views.py; edit the source. -->
| Company / role | December 31, 2024 closing price | FY2024 total GAAP diluted EPS |
| --- | ---: | ---: |
| Asbury Automotive (ABG), target | $243.03 | $21.50 |
| AutoNation (AN), candidate peer | $169.84 | $16.92 |
| Group 1 Automotive (GPI), qualified candidate peer | $421.48 | $36.81 |

*Retrospective training comparison: year-end prices paired with subsequently reported annual earnings. [Case sources and definitions](teach-comps-worked-example.md).*
<!-- generated:case-inputs:end -->

**P/E = price per share ÷ annual earnings per share.** Compute AutoNation together.
Predict, then calculate Group 1. Asbury is the target, not a member of its own peer set.

---

## Implement — build from the case table

<!-- generated:build:start -->
<!-- Generated from lab-07-comparable-policy.md by ../build_week04_views.py; edit the source. -->
> Write one standard-library Python file with editable target/peer inputs at the top.
> Deduplicate peers and exclude the target. Compute peer P/E = price / diluted EPS and
> median P/E. Multiply minimum, median and maximum peer P/E by target EPS for implied prices.
> Retain full precision; display multiples to six decimals, prices to cents. Missing or
> nonpositive prices or EPS: label affected calculations not meaningful. One valid peer:
> reference estimate, no range; none: no usable peers. For each peer removal, print the
> remaining median-implied price and dollar change from the full-peer estimate, using
> unrounded values; if none remain, no estimate. Never bridge P/E with cash/debt.
> Do not fetch data or install packages. Give the exact run command using my working Python command.
<!-- generated:build:end -->

While AI works, calculate one price. **New File → save → Terminal → run.**

---

## Validate — the answer must reproduce

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

Removing a higher-multiple peer lowers the midpoint. With one peer remaining, you lose the range.
If your result differs, check the inputs and calculation with AI. Keep unrounded multiples until display.

---

## Evolve — change one peer

Use your Asbury calculation:

1. Predict what removing Group 1 will do.
2. Read the leave-one-out result; explain the price change.
3. Explain why one remaining peer gives a reference estimate rather than a range.

Keep the original peer decision unless business evidence warrants changing it.

---

## Reflect — explain the method

Explain to your partner:

1. What P/E measures and why it helps compare companies.
2. Why each case peer belongs or needs qualification.
3. Why the peer-implied band does not prove Asbury is fairly valued.

**Expect:** you can explain the calculation and peer choice before applying them independently.

---

## Checkout — on GitHub

**Brightspace → Quizzes → Lab 07. Start the attempt when told.**

**GitHub links of your files: md, py and/or other files as needed.**

**Before Thursday — do these:**

1. Follow [Thursday prework](student-prework.md).
2. Bring your working calculator and your own company’s DCF and sources.

**Lab 08:** find and defend peers for your own company, then compare with your DCF.

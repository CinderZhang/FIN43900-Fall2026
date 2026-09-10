# The Training-Case Comps, Worked End to End

**A real case: Asbury Automotive, with AutoNation and Group 1 Automotive**

*This page teaches the worked examples. Submission requirements live in the Week 4 handout
and Labs 07–08. Tables copied into other course surfaces are generated from this page.*

## Why use another company's price?

Your discounted cash flow (DCF) model values a company from assumptions about its future cash
flows. Comparable-company valuation asks a different question: **what value would your company
have if investors priced its earnings like those of similar companies?** Disagreement with your
DCF is a reason to investigate assumptions, peer selection, and market conditions.

A share price alone cannot answer this. One company may have many more shares than another.
**Price-to-earnings (P/E)** divides price per share by earnings per share (EPS), putting the
comparison on a common basis: dollars of share price per dollar of annual earnings.

P/E is useful when positive earnings reasonably represent the business and peers have
comparable economics and earnings definitions. Negative earnings do not support this positive
multiple comparison. An unusual profit can inflate earnings and make P/E look deceptively low;
unusually depressed earnings can make it look high. Growth prospects, risk and debt can also
justify different multiples. **A lower P/E is a question to investigate, not an automatic bargain.**

We will value Asbury Automotive, a vehicle retailer. You do not need to have bought a stock
or read an entire annual report to follow this case. Start with how the businesses earn money.

## Before seeing multiples: what makes a peer?

A **candidate** is a company worth investigating. A **peer** is a candidate whose economics
fit your stated comparison. Sharing an industry label does not settle that judgment.

Here is the teaching policy, stated before the numeric comparison:

- Look for publicly traded franchised vehicle retailers with new and used vehicle sales and
  meaningful parts/service operations.
- Compare how they earn money, their scale, geography, and financing activities. Name material
  differences instead of hiding them in an average.
- For this P/E exercise, require positive annual earnings and a consistent earnings definition.
- Qualify a candidate with a material business difference; reject one that does not fit the
  business model or whose needed evidence cannot be verified.

This is a worked policy, not a policy to paste over your own company's economics. A software
company, bank, and car dealership need different comparisons.

## Read the business evidence first

Asbury sells vehicles and provides parts/service and finance/insurance products. AutoNation
has similar revenue activities and also operates AutoNation Finance. Group 1 operates in both
the U.S. and U.K.; its acquisition of 54 Inchcape dealerships during 2024 also affects the
business being compared. See the companies' releases linked in the input table below:
Asbury's company description, AutoNation's operational/segment discussion, and Group 1's
U.K. discussion.

**Pause:** which candidate fits the core business but deserves a qualification? Group 1's
geography and acquisition history provide a concrete answer. That does not automatically
make it unusable. AutoNation's finance business also deserves attention. Neither company is
an exact copy of Asbury.

Decide what those differences mean before seeing which inclusion produces the price you prefer.

## A frozen historical comparison

**This is retrospective:** prices are the December 31, 2024 closes; earnings cover the year
ended December 31, 2024 and were released afterward. It is not a claim about what an investor
could have known or traded on December 31. A point-in-time analysis must use only information
public by its valuation date.

Use **total GAAP diluted EPS**, meaning reported earnings per share including dilution, rather
than management's adjusted EPS. Keep price and EPS on the **same stock-split basis**. A later
split-adjusted price divided by the original unsplit EPS would produce a false multiple.

<!-- case-inputs:start -->
| Company / role | December 31, 2024 closing price | FY2024 total GAAP diluted EPS | Primary sources and locators |
|---|---:|---:|---|
| Asbury Automotive (ABG), target | $243.03 | $21.50 | [2025 proxy](https://www.sec.gov/Archives/edgar/data/1144980/000114498025000092/abg-20250402.htm): outstanding equity awards, footnote (2), search `243.03`. [January 30, 2025 release](https://www.sec.gov/Archives/edgar/data/1144980/000114498025000008/a2024q4ex991.htm): Full Year 2024 Results. |
| AutoNation (AN), candidate peer | $169.84 | $16.92 | [2025 proxy](https://www.sec.gov/Archives/edgar/data/350698/000035069825000068/an-20250311.htm): outstanding equity awards, footnote (1), printed p. 30. [February 11, 2025 release](https://www.sec.gov/Archives/edgar/data/350698/000035069825000026/anearningsrelease123124ex9.htm): Full Year 2024, selected GAAP table. |
| Group 1 Automotive (GPI), qualified candidate peer | $421.48 | $36.81 | [2025 proxy](https://www.sec.gov/Archives/edgar/data/1031203/000103120325000018/gpi-20250320.htm): Termination and Change in Control Tables, introduction, printed p. 59. [January 29, 2025 release](https://www.group1corp.com/2025-01-29-Group-1-Automotive-Reports-2024-Fourth-Quarter-Financial-Results-and-Record-Full-Year-Revenues-of-19-9-billion): annual consolidated statement of operations, total diluted EPS row. |
<!-- case-inputs:end -->

Group 1's headline emphasizes continuing operations. Our table deliberately uses **total**
diluted EPS. Read the row label, not just the first earnings number you find. Do not silently
substitute adjusted EPS when reported earnings make a comparison inconvenient.

## Compute one; then do the next

AutoNation's P/E = its price ÷ its annual diluted EPS. The units are dollars per share divided
by dollars earned per share in a year. The result is a multiple, not dollars.

**Before reading the checks, calculate Group 1's P/E yourself.** Then apply each peer's
multiple to **Asbury's** EPS. That converts the peer comparison into two prices for the same
target. Asbury is not included in its own peer median.

For two peers, the median is halfway between their multiples. With only two observations,
that midpoint is sensitive to both; the word “median” does not make a small sample reliable.
Keep unrounded multiples in calculations and round final prices to cents.

<!-- case-checks:start -->
| Check | Calculation | Result |
|---|---|---:|
| AutoNation P/E | 169.84 ÷ 16.92 | 10.037825× |
| Group 1 P/E | 421.48 ÷ 36.81 | 11.450149× |
| Asbury observed P/E, for comparison only | 243.03 ÷ 21.50 | 11.303721× |
| Peer median P/E | (AN P/E + GPI P/E) ÷ 2 | 10.743987× |
| Asbury price using AN | (169.84 ÷ 16.92) × 21.50 | $215.81 |
| Asbury price using GPI | (421.48 ÷ 36.81) × 21.50 | $246.18 |
| Asbury peer-implied range | Lower to higher peer-implied price | $215.81–$246.18 |
| Asbury at peer median | Peer median P/E × 21.50 | $231.00 |
| Remove GPI: remaining AN estimate | AN P/E × 21.50 | $215.81 |
| Change from two-peer midpoint | AN estimate − median estimate, before rounding | −$15.18 |
<!-- case-checks:end -->

The observed target price lies inside this range. That establishes neither fairness nor an
investment recommendation: the range depends on these peers and this earnings convention.

## Change one judgment and observe the consequence

**Predict first:** removing the higher-multiple qualified peer should lower the midpoint.
The checks confirm that direction. Explain the removal using business evidence, not a desire
for a lower answer. With only AutoNation left, you have **one reference estimate, not a range**.

For your own-company work, the same route begins with two candidates and an audited P/E
comparison where meaningful. If EPS is zero or negative, P/E is not a meaningful positive
valuation reference. Name that limitation; do not invent earnings or automatically switch to
adjusted EPS. The lab governs how incomplete evidence is recorded.

## Compare with your own DCF in Lab 08

Your P/E comparison uses other companies' market prices. Your DCF uses your forecast.
A disagreement should lead you to inspect the peers, earnings basis and forecast assumptions.
It is not a reason to average the answers automatically.

For Asbury, the observed price is inside the peer-implied band. A cautious explanation is:
“The comparison alone does not establish an attractive purchase. I would watch-defer while
checking whether the earnings and peer differences justify this band. I would reconsider if
the price changed and the business evidence still supported the comparison.”

If AI tells you to subtract net debt from a P/E-derived equity value, reject that advice:
this method already values shareholders' earnings. Point to the calculation rather than
accepting technical-sounding wording.

The [optional reading](open-ended-challenge.md) is available if you want to study other methods.

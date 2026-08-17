# Week 1 Student Handout — Readiness and Provisional Company Screening

## Why this week matters

Every research career starts with the same unglamorous decision: *which company deserves your
next hundred hours?* Screening is how professionals ration attention — and it is also where
AI is most seductive and most dangerous, because a model will happily rank companies on
definitions nobody checked. This week you set up the toolchain you'll use all semester and
make your first defended professional judgment: a provisional target you can justify, with a
named disqualifier that would make you drop it. Employers phone-screen for exactly this —
"walk me through why you picked the company you analyzed" — and by Thursday you will have a
real answer.

## Your role and deliverable

You are an equity-research analyst deciding which public operating company deserves deeper
valuation work. You will leave Week 1 with a working course toolchain and a **provisional
research target**. You are not proving that the stock is attractive and you are not making
investment advice.

## Readable DRIVER alternative — six stages and the Week 1 case

Use this section when you prefer text or the video/player/captions are inaccessible. It is a
course-authored equivalent for the assessed objectives, not a verbatim video transcript.

| Stage | Human-owned question | Week 1 observable action |
|---|---|---|
| **D — Define & Discover** | Who needs what decision, under which constraints, and what evidence could matter? | Define the user, deeper-research decision, eligible universe, evidence needs, and disqualifier. |
| **R — Represent** | How will facts, assumptions, definitions, and uncertainty be structured? | Freeze criteria, periods, units, missingness rules, thresholds/weights, and evidence fields before ranking. |
| **I — Implement** | What reproducible calculation or workflow expresses that representation? | Run or adapt the supplied screen without silently changing definitions or substituting unavailable data. |
| **V — Validate** | Which source, known answer, invariant, or changed input could prove the result unreliable? | Verify one load-bearing definition/fact and run one ranking-stability change. AI agreement is not validation. |
| **E — Evolve** | What should be repaired, qualified, removed, or escalated after the test? | Update the policy or quarantine the result; preserve the before/after decision and reason. |
| **R — Reflect** | What do I now know, what remains uncertain, and what would reverse my action? | Defend a provisional target, limitation, evidence request, and observable reversal condition in your own words. |

The central case is simple: a composite screen can identify a company worth investigating, but it
cannot establish undervaluation or an investment recommendation. A high score may be caused by
arbitrary weights, mismatched definitions, short history, missing observations, or an ineligible
business form. Therefore the deliverable is a **provisional research admission decision** with a
source check and stability test—not a buy/sell conclusion. Answer the video's three pre-class
questions from this table and the screening-policy worksheet below.

### Complete readable reference for the practice quiz

The Week 1 practice quiz checks these five ideas. They are stated here so that watching the video
is never the only way to answer an assessed question.

1. **Begin with the task and decision.** In Discover and Define, ask, “What task do I want to
   complete?” before choosing a ticker, metric, or AI tool.
2. **Interpret the mechanism behind an insider-event count.** Many reported insider transactions
   arise from compensation, option exercises, donations, or administrative activity rather than
   a voluntary open-market purchase, so a large raw count may carry little directional signal.
3. **Shared labels can hide different measurements.** Two providers can report PEG ratios that
   differ by roughly six times when one uses backward-looking growth and the other uses forward
   estimates. Verify the definition before comparing or screening on the value.
4. **Explanation is ownership evidence.** Explain the workflow and logic aloud with the evidence
   visible; this exposes gaps that silent familiarity can hide.
5. **DRIVER is deliberately demanding practice, not a shortcut.** Its purpose is to help you do
   useful work with AI while developing understanding, validation, and explanation. The framework
   does not substitute for finance evidence or judgment.

## Part A — technology readiness record

For each item, record `READY`, `RECOVERING`, or `UNVERIFIED`, then retain the evidence.

| Capability | Evidence | Status or exact blocker | Next action and owner |
|---|---|---|---|
| Brightspace attempt and receipt | confirmation/attempt record |  |  |
| Python imports | version/output block |  |  |
| market-data retrieval | ticker, returned dates, row count |  |  |
| chart/output | rendered figure or saved output |  |  |
| AI Access required-subscription check + Week 1 dual-system packet | plain-text confirmation only |  |  |
| Optional accessible free interface or `COURSE-RUN PROBE:` route | plain-text confirmation only |  |  |
| GitHub repository workflow | repository created and accessible |  |  |
| unlisted video/transcript workflow | logged-out link/transcript test or processing state |  |  |
| recording/upload path | Kaltura Capture, Zoom, or approved equivalent; microphone/camera/screen check |  |  |

Never submit or display a password, API key, token, account number, billing page, or private
account screenshot. A documented failure plus a viable remediation action is better evidence
than a hidden or fabricated pass.

## Optional debugging clinic — not a Lab 01 requirement

Use this clinic if your environment is ready early or the instructor assigns it as a targeted
diagnostic. It is not required evidence for Lab 01. Run the deliberately broken metrics case,
ask two accessible course-supported systems separately to diagnose it. The published Week 1
screening packet does not diagnose this debug file. Use `COURSE-RUN PROBE:` for this exact debug
prompt when either required comparison output is inaccessible, and do not show one system the
other system's answer.

| Defect | OpenAI-system output/access path | Google-system output/access path (record only the model identifier actually exposed) | Evidence that arbitrates | Your correction |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

Then close both systems and explain why the correct Sharpe numerator and denominator must use
compatible annual units.

## Part B — screening policy before AI

Write this individually before asking AI for criteria or weights.

This is a deliberate no-generative-AI baseline for the first Define & Discover edge and the
initial representation—not a claim that canonical DRIVER excludes AI from Represent,
Implement, Validate, or Evolve. You will then use AI in the middle, independently validate it,
and finish with a human-owned Reflect/decision defense.

- **Decision user:** Who will use this screen?
- **Decision:** What does the screen select for deeper research?
- **Universe:** Which companies can enter?
- **Exclusions:** Which securities/businesses are outside scope, and why?
- **Criteria:** Which observable measures matter?
- **Definitions:** What does each measure mean and over what period?
- **Threshold or weight:** How does each measure affect the result?
- **Success test:** What evidence would make the screen useful?
- **Disqualifier:** What fact should override a high composite score?

Asbury Automotive Group (`ABG`) is the instructor demonstration company and cannot be your
target. Because Project 1 uses an operating-company FCFF/enterprise-value architecture, banks,
insurers, REITs, ETFs, mutual funds, closed-end funds, shells, and other non-operating vehicles
are outside this equity-valuation exercise. If every screened company is ineligible, report
`no admissible target yet` and name the next operating-company candidate; do not force an
ineligible target through the screen.

## Screening metric reference

These are candidate measures, not a required formula. Define the period and data treatment.

| Measure | Basic interpretation | Failure question |
|---|---|---|
| adjusted total return | price performance including provider adjustments | What exactly is adjusted, and when? |
| annualized volatility | dispersion of periodic returns | Are frequency and annualization consistent? |
| maximum drawdown | worst peak-to-trough decline | Is the observation window representative? |
| return/volatility ratio | return earned per unit of measured volatility | Was a risk-free rate used; are units aligned? |
| positive-period frequency | share of periods with positive return | Does it ignore magnitude and tail loss? |
| data completeness | usable observations relative to expectation | Did missingness improve a company artificially? |
| business/data suitability | filings, operating history, understandable value drivers | Is this measurable or an undocumented preference? |

The starter fails closed if the provider omits `Adj Close`; it never silently substitutes raw
`Close`. It also quarantines annualized return and the return/volatility ratio when a security has
fewer than 365 calendar days of coverage. Preserve `price_basis`, `return_status`,
`drawdown_status`, and `coverage_years` in the evidence rather than ranking quarantined rows.

For the first validation, use **Provider and Filing Definition Check**: the pre-staged yfinance parameter
reference or SEC filing-search route keeps the task bounded. Record page/filing, access or filing
date, exact field/fact, and accept/qualify/reject conclusion.

### SEC filing-search route and equivalent fallback

On **SEC Search Filings**, choose **Company Search**, enter the issuer name/ticker/CIK, confirm the
legal issuer, and open the relevant `10-K`, `10-Q`, or `8-K`. Record company/ticker/CIK, form,
filed date, accession or filing URL, the exact dated fact, and whether it admits, qualifies, or
rejects the provisional target. Do not treat a search-result snippet as the filing evidence.

If SEC Search Filings is unavailable or cannot be used accessibly during the lab, complete the
same validation judgment with the downloaded **Provider Definition Check — yfinance Parameters
for the Screening Lab**: verify one load-bearing metric definition, record its displayed source
and access date, and state accept/qualify/reject. This is the complete no-SEC route for the lab;
the live filing fact can be added later without penalty and is not required to preserve checkout.

A high score is not self-validating. Composite rankings can conceal arbitrary weights,
correlated criteria, incomparable definitions, stale observations, or a disqualifying fact.

## AI comparison protocol

1. Give each course-supported AI system—or the published/course-run route—the same role,
   universe, constraints, definitions, and desired
   output format.
2. Preserve each proposed criterion and its rationale.
3. Mark `accept`, `modify`, or `reject` for every material suggestion.
4. Implement only the policy you can explain.
5. Do not use agreement between two systems as validation; use data, documentation, finance
   logic, and changed-input tests.

## Offline case path

If live market retrieval fails, download **Offline Screening Case** and use the downloaded
`offline-screening-case.csv`. It contains named
public companies but **synthetic training metrics, not market evidence**. You may use it to
complete the DRIVER cycle and name a provisional class target, but you must independently
replace or verify every load-bearing metric before carrying the company into Week 2. Record the
exact `SYNTHETIC_TRAINING_CASE_NOT_MARKET_EVIDENCE` label in the checkout. Lab 01 applies the
policy to the table; Lab 02 implements the rule in code and performs the robustness tests.

## Minimum validation evidence

Complete both:

1. **Independent definition/source check:** verify one load-bearing metric or company fact
   against provider documentation, a filing, or another authoritative source. Record the
   source and as-of date.
2. **Ranking-stability test:** change one defensible threshold, weight, lookback period, or
   exclusion. Record the original and revised top candidates and interpret the change.

`No material change` is a valid result when the test is genuine and the explanation is
specific.

## Provisional-target micro-pitch

Use this structure in no more than 45 seconds:

> Investigate **[company/ticker]** for **[decision user]** because **[two strongest screening
> facts with source dates]**. The ranking is most sensitive to **[assumption/definition]**.
> This is provisional because **[unknown]**. I would disqualify or reverse the choice if
> **[observable condition]**.

## Submission check

- You—not a teammate—submit your dated Brightspace checkout.
- Record every teammate who worked with you and your own contribution.
- Include the requested output/evidence; link a repository only if you created one.
- Name each access path you used. Record only model identifiers the interface actually exposed;
  do not claim the packet's collection tools as your own use.
- Confirm the truth attestation and verify the Brightspace receipt before leaving.

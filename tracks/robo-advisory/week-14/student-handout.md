# Student Handout — Recommendation, Fee, Conflict, and Shock Audit

> The client, portfolios, scenarios, compensation, and expected returns are synthetic. This is a
> teaching control exercise, not individualized advice or a legal compliance conclusion.

The Capstone Edition A window closes before Tuesday's class — the exact window is on the
Brightspace checkpoint page and in `MASTER-SCHEDULE.md`. Budget **20 minutes** and submit
the separate ungraded checkpoint before any new capstone-specific generative-AI work.
This studio remains formative.

## The project this session replicates — and the primary deliverable

Tuesday's build reproduces **PyPortfolioOpt**'s documented example (Robert Andrew Martin;
JOSS 2021; see the Week 13 handout's credit section) from the repository's own shipped
data, then dispositions the reproduced portfolio against the Week 13 client mandate.
**That reproduction-plus-disposition notebook is the session's primary deliverable**; the
recommendation-audit material below is the taught reference layer and the in-class
fallback.

The spine, on paper (self-study recoverable; the Session 26 slides carry the same steps):

1. **Declare before code:** library version installed, data file and its date range, the
   example's objective, and what "match" will mean for you
2. **Reproduce** the README example: max-Sharpe weights, then the discrete allocation
   against the printed expected output
3. **Mismatch?** Version → release notes → method → data — only then "possible
   difference worth reporting"
4. **Translate** the result for the mandate: share counts × latest prices → weights,
   plus the cash remainder and each holding's mandate-relevant classification; any
   client attribute the price data cannot supply is **unresolved**
5. **Disposition** against the five hard limits with reason codes: approve · modify ·
   reject · **escalate** — unresolved attributes escalate, never pass silently
6. **Cite**: the citation cell crediting the author, with version and download date

## Your role and deliverable

You are a second-line review analyst. Produce a one-page retain/change/defer recommendation and a
plain-language client explanation. The evidence must show how a changed fact propagates through
the mandate; an AI narrative or optimized score cannot substitute for that chain.

## Scenario discipline

Freeze the Base admissible set. For each changed scenario:

1. identify the new verified fact or explicit teaching assumption;
2. predict whether the admissible set should expand, contract, or remain unchanged;
3. re-run all five hard limits with reason codes;
4. reconcile expected and actual directions; and
5. escalate if no candidate passes instead of silently relaxing the mandate.

Known control outcomes are Base: Conservative/Balanced; JobLoss: Conservative; LiquidityShock:
none. You must reproduce, explain, and challenge them rather than merely copy them.

## Fee-drag anchor

Under the supplied teaching convention,
`future value = principal × (1 + gross return − annual fee)^years`.
Compare $500,000 at 6% gross for 10 years under 0.25% and 0.90% annual fees. Label the convention:
constant annual gross return, fee deducted once annually, no taxes, flows, trading costs, or path
variation. The result is a sensitivity anchor, not a forecast.

## Conflict and explanation audit

Ask both named AI systems to recommend a portfolio and explain it to the client. Preserve the
prompts and outputs. For each claim, tag:

- `supported by client fact`;
- `supported by synthetic portfolio field`;
- `assumption/model output`;
- `omitted fee or constraint`;
- `provider-conflict question`; or
- `unsupported certainty`.

Independently verify the selected candidate, all reason codes, the fee comparison, and one claim
the AI presented as fact. Provider compensation is a reason to investigate and disclose; it does
not prove a recommendation was corrupted.

## Client explanation standard

State the client's decision and changed fact; what is recommended or deferred; why it fits the
current mandate; why alternatives failed; fees and limitations; conflicts/unknowns; what happens
next; monitor/owner/frequency; and two observable reversal/escalation triggers. Avoid guaranteed,
safe, optimal, personalized, or compliant unless the evidence and authorized process support the
term. Finish with a no-AI committee defense.

Retain the packet as optional capstone evidence. There is no checkout or grade item.

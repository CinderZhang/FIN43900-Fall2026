# Student Handout — Alternative Data Admission

## Role and deliverable

You are a market-data risk analyst. Decide whether the supplied panel may be used for a historical
market test. Deliver a data card, row funnel, point-in-time rule, naive-versus-valid comparison,
AI claim dispositions, and an admit/quarantine/prospective-test/reject decision.

## Prework record

Run the starter at `2026-01-02T10:00:00Z`. Before using AI, record the timestamp that should
control admissibility and one row you expect to be unavailable. Preserve your prediction.

## Data-card template

| Field | Evidence or value | Unknown/limitation | Decision consequence |
|---|---|---|---|
| source/owner and collection method |  |  |  |
| license/use boundary |  |  |  |
| population/unit/coverage |  |  |  |
| entity identifier and mapping |  |  |  |
| event, availability, decision, revision time |  |  |  |
| missingness/duplicates/revisions |  |  |  |
| PII/privacy and retention |  |  |  |
| evaluation label and embargo |  |  |  |

`event_time` describes when an event occurred. `available_time` describes when the observation
could enter the information set. `decision_time` is the portfolio/research cutoff. A revision is
not retroactively available. `future_return` is supplied only for later evaluation and cannot be
used to choose the historical sample, rule, threshold, or disposition.

## Tuesday workflow — provenance gate

1. State the intended market decision and information cutoff.
2. Build the data card and mark unsupported facts as unknown.
3. Preserve row IDs; flag missing identity, exact duplicate, revision, late availability, and
   label leakage separately.
4. Ask AI to draft source/cleanup claims. Disposition every material claim against the actual
   file or documentation; do not accept invented provenance.
5. Build a row funnel with counts and reasons. Quarantine is evidence preservation, not failure.
6. Decide admit, quarantine, prospective test, or reject and name evidence that reverses it.

## Thursday workflow — point-in-time panel

Write the rule before code. At minimum, a row cannot enter if it was not available by the
decision time or lacks a defensible entity. State how exact duplicates and revisions are handled.

| Row ID | Event time | Available time | Issue(s) | Admit/quarantine/exclude | Reason |
|---:|---|---|---|---|---|
|  |  |  |  |  |  |

Compare a naive event-date panel with the valid as-of panel. Quantify row/sample differences and
any mechanical result difference, but do not use the evaluation label to repair the rule. Change
the cutoff or revision policy once and predict the effect first.

## Decision and submission checklist

- research may proceed, must wait, may run only prospectively, or must stop;
- exact as-of/revision/duplicate rule and retained audit trail;
- unsupported AI claim and disposition;
- most consequential limitation and missing evidence;
- monitoring/recheck trigger and reversal condition;
- Lab 16/19 individual fields, AI disclosure, truth attestation, and receipt verified.

If code or network access fails, the row-level table and plain-language rule provide the
equivalent evidence. Do not paste licensed, personal, or nonpublic data into an AI system.

# Offline Fallback — Week 13 Robo Track

Use this page if Python, files, or AI access fails. The same finance evidence is required.

## Supplied client limits

Maximum one-year loss 18%; equity cap 60%; cash floor 5%; illiquidity cap 10%; annual fee cap
0.60%. Net return equals gross return minus annual fee.

## Known-answer table

| Candidate | Net return | Loss | Equity | Cash | Illiquid | Fee | Admissibility |
|---|---:|---|---|---|---|---|---|
| Conservative | 4.85% | pass | pass | pass | pass | pass | admissible |
| Balanced | 5.95% | pass | pass | pass | pass | pass | admissible |
| Growth | 6.95% | fail | fail | fail | fail | pass | inadmissible |
| IncomePlus | 6.05% | fail | pass | fail | fail | fail | inadmissible |

Reproduce the matrix by hand or spreadsheet and show each comparison. Do not infer that Balanced
must be selected merely because its net-return input is higher. Compare only admissible choices,
retain the missing-fact escalation, and complete the same conditional committee record. Mark code
and AI extensions `not executed—access fallback`; they are not required to receive equivalent
formative access.

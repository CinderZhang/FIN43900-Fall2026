# Validation and AI Use

## Decision, version, and as-of boundary

Decision/user; repository commit/tag; run timestamp; source cutoffs; environment.

## Data and convention ledger

| Material input | Source | As-of/availability | Definition/units | Transformation/exclusion | Risk |
|---|---|---|---|---|---|
| [enter input] | [enter source] | [enter date] | [enter definition] | [enter treatment] | [enter risk] |

## Validation register

| Claim/output | Failure mode | Test and expected result/direction | Actual result | Disposition | Evidence location |
|---|---|---|---|---|---|
| [enter claim] | [enter failure] | [enter test] | [enter result] | [enter disposition] | [enter evidence path] |

Include known answer, changed input, highest-risk failure, reproducibility/cold run, and the
project-specific robustness requirements. Failed tests remain visible.

## Locked Changed-Input Record — human prediction first; AI closed during execution

### Precommit before the run and before AI assistance on the prediction

| Precommit timestamp | Repository commit | Material input | Old → new value/units | Expected output direction | Expected decision effect |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Preserved execution result

| Before/after output | Actual decision effect | Prediction reconciliation | Failure diagnosis or why action did not change | Evidence path |
|---|---|---|---|---|
|  |  |  |  |  |

## Named AI-use register

| Tool/model surface and exposed version | Interaction date | Material task | Output/claim used or considered | Independent check | Accept/modify/qualify/reject | Effect on decision |
|---|---|---|---|---|---|---|
| [enter tool/model/version actually exposed] | [enter date] | [enter task] | [enter output] | [enter check] | [enter disposition] | [enter effect] |

Do not paste credentials, private prompts/data, or every trivial completion. Record material
uses needed to understand research, code, validation, and communication decisions.

## Limitations, monitoring, and kill/escalation rules

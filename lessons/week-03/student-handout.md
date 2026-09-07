# Week 3 Student Handout — Your Workspace, Your DCF

Last week: is this company worth looking at? This week: what is it worth, and what does the
price already assume?

## The two commands

In the VS Code terminal (**Terminal → New Terminal**), with your own Python command in place
of `python` (`python`, `py`, or `python3` — the one that answered):

| Command | Expect |
|---|---|
| `python --version` | `Python 3.1x` |
| `python dcf.py` | Tuesday: twelve lines matching the known answer. Thursday: your company's lines, the grid, the solved shift |

Something breaks? Debug with your AI: the exact command and the exact error text. Check the
folder and the filename first.

## The digits, once

Training case: FCFF 100; growth 8%, 6%, 5%, 4%, 3%; WACC 10%; terminal growth 3%; cash 50;
debt 300; 50 million diluted shares.

| Step | Formula | Training case |
|---|---|---|
| Grow | FCFF × (1 + g) | 100 × 1.08 = 108.00 |
| Discount | FCFF ÷ (1 + WACC)ᵗ | 108.00 ÷ 1.10 = 98.18 |
| Terminal value | FCFF₅ × (1 + g) ÷ (WACC − g) | 128.7625 × 1.03 ÷ 0.07 = 1,894.65 |
| Enterprise value | ΣPV + PV of TV | 448.44 + 1,176.43 = 1,624.87 |
| Per share | (EV + cash − debt) ÷ shares | (1,624.87 + 50 − 300) ÷ 50 = 27.50 |

The terminal value is **72.4%** of enterprise value here. Say that number whenever you report a
DCF. Every digit is worked in `teach-dcf-worked-example.md`.

## DRIVER, five lines

- **D** — the same question for everyone: what is one share worth, and what growth does the
  price assume?
- **R** — five inputs. Tuesday: read them on the training case. Thursday: source them from
  your filing; `unresolved` is an honest answer.
- **I** — your AI builds `dcf.py` from the lab's request. You supply the spec and the judgment.
- **V** — the known answer first. Twelve lines reproduce or they do not.
- **E** — Thursday: your company through the model, the grid, the reverse DCF.

## Rules

- Do not use the instructor's demonstration company, Asbury Automotive Group (`ABG`).
- `unresolved` earns full credit. Zero does not. A number with no source does not.
- Never type the known answers into `dcf.py`. The WACC 0.11 probe is what proves the model computes.
- The training-case convention is the graded convention. Do not switch conventions mid-model.
- Nothing graded needs an install, an extension, or a third-party account.

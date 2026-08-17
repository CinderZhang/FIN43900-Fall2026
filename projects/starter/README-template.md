# Project Title

## Finance decision and intended user

State the action this system supports, decision horizon, as-of date, and material constraints.

## Visible result

Point to a frozen output showing material inputs, version/as-of date, range/allocation/action,
and conditions without requiring execution.

## Setup and run

1. Create an isolated environment.
2. Install `requirements.txt`.
3. Copy `.env.example` to `.env` only when credentials are needed; never commit `.env`.
4. Run `streamlit run app.py` and the project tests.

## Repository map

Explain data, analysis, validation, application, docs, and tests.

### Required analysis-to-interface flow

1. Preserve sourced inputs and assumptions in the source ledger or declared input files.
2. Make `analysis.py` compute every material finance result; do not calculate the recommendation
   only inside the interface.
3. Run the known-answer, changed-input, and project-specific validation checks.
4. Deliberately export the validated subset needed by the audience to `visible_output.json`, with
   its as-of date, units, and limitations. This is a frozen, reviewable interface contract—not a
   second hand-entered analysis.
5. Make `app.py` render that frozen contract and its conditions. It may filter or format results,
   but it must not silently replace the analysis engine or contain manually typed material
   outputs other than explicitly disclosed assumptions.

The expected direction is **evidence → analysis → tests → frozen visible output → app**. A reviewer
must be able to trace every displayed material value backward without running the application.

## Data sources and point-in-time boundary

## Financial conventions and assumptions

## Validation and changed-input tests

## Known limitations, monitoring, and reversal triggers

"""FIN 43900 Week 2 valuation-foundations infrastructure.

The synthetic known-answer calculations and ledger schema are provided. Company-specific
normalization, source reconciliation, forecast assumptions, and valuation judgment remain the
student's work.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


REQUIRED_LEDGER_COLUMNS = [
    "item",
    "classification",
    "value",
    "unit",
    "period_or_as_of_date",
    "primary_source_and_locator",
    "rationale",
    "independent_check",
    "uncertainty_or_failure_mode",
]


def load_mini_case(path: str | Path) -> dict[str, float]:
    table = pd.read_csv(path)
    required = {"metric", "value", "unit"}
    missing = required.difference(table.columns)
    if missing:
        raise ValueError(f"Mini-case columns missing: {sorted(missing)}")
    if table["metric"].duplicated().any():
        raise ValueError("Mini-case metric names must be unique")
    return table.set_index("metric")["value"].astype(float).to_dict()


def calculate_known_answers(values: dict[str, float]) -> dict[str, float]:
    nopat = values["ebit"] * (1 - values["tax_rate"])
    fcff = (
        nopat
        + values["depreciation_and_amortization"]
        - values["capital_expenditures"]
        - values["increase_in_operating_nwc"]
    )
    common_equity_value = (
        values["enterprise_value"]
        + values["nonoperating_cash"]
        - values["debt"]
        - values["noncontrolling_interest"]
        - values["unfunded_pension"]
    )
    value_per_diluted_share = common_equity_value / values["diluted_shares"]
    return {
        "nopat": nopat,
        "fcff": fcff,
        "common_equity_value": common_equity_value,
        "value_per_diluted_share": value_per_diluted_share,
    }


def load_and_check_ledger(path: str | Path) -> pd.DataFrame:
    ledger = pd.read_csv(path)
    missing = set(REQUIRED_LEDGER_COLUMNS).difference(ledger.columns)
    if missing:
        raise ValueError(f"Evidence-ledger columns missing: {sorted(missing)}")
    return ledger[REQUIRED_LEDGER_COLUMNS].copy()


def student_company_bridge(ledger: pd.DataFrame) -> dict[str, float]:
    """STUDENT_WORK: calculate the target company's bridge from reconciled ledger rows.

    Do not complete this function until every included value has a date, unit, classification,
    source locator, rationale, check, and failure mode. Return enterprise value, equity value,
    diluted shares, and per-share value only when numerator/denominator conventions align.
    """
    raise NotImplementedError("Complete after the company evidence ledger is reconciled")


def main() -> None:
    folder = Path(__file__).resolve().parent
    values = load_mini_case(folder / "mini_case.csv")
    answers = calculate_known_answers(values)
    ledger = load_and_check_ledger(folder / "evidence_ledger_template.csv")

    print("SYNTHETIC KNOWN-ANSWER CASE - USD millions except per-share value")
    for name, value in answers.items():
        print(f"{name}: {value:.2f}")
    print(f"\nEvidence-ledger rows available: {len(ledger)}")
    print("Populate the target-company ledger before implementing student_company_bridge().")


if __name__ == "__main__":
    main()

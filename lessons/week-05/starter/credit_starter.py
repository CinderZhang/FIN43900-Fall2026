"""FIN 43900 Week 5 credit-screening starter.

Synthetic borrower inputs and fully observed labels are supplied. Label `1` means payment
default, court-supervised insolvency, or lender principal impairment from restructuring within
the complete 12 months after the decision date; `0` means none occurred. There is no censoring.
Students implement documented ratios, screening policy, reason codes, and calibration. The
historical label is not underwriting truth.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "borrower",
    "ebitda",
    "depreciation_amortization",
    "interest_expense",
    "total_debt",
    "current_assets",
    "current_liabilities",
    "cfo",
    "capital_expenditures",
    "adverse_outcome_next_12m",
}


def load_cases(path: str | Path) -> pd.DataFrame:
    cases = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(cases.columns)
    if missing:
        raise ValueError(f"Required credit fields missing: {sorted(missing)}")
    if cases["borrower"].duplicated().any():
        raise ValueError("Borrower identifiers must be unique")
    return cases


def compute_ratios(cases: pd.DataFrame) -> pd.DataFrame:
    """STUDENT_WORK: implement ratios using the published convention sheet and expose invalid inputs."""
    raise NotImplementedError


def apply_credit_screen(ratios: pd.DataFrame, policy: dict) -> pd.DataFrame:
    """STUDENT_WORK: return approve/review/reject, factor reasons, missingness, and overrides."""
    raise NotImplementedError


def evaluate_decisions(screen: pd.DataFrame, label_column: str) -> dict[str, int]:
    """STUDENT_WORK: map review/reject to positive and approve to negative, then calculate errors."""
    raise NotImplementedError


def main() -> None:
    path = Path(__file__).resolve().parent / "credit_cases.csv"
    cases = load_cases(path)
    print(cases.to_string(index=False))
    print("\nBorrower A known answers: leverage 4.00x; EBIT coverage 5.00x;")
    print("current ratio 1.25x; (CFO-capex)/debt 8.3333%.")
    print("Implement ratios, screen, reasons, and error-cost evaluation; then attack one rule.")


if __name__ == "__main__":
    main()

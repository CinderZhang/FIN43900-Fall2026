"""Week 6 credit-stress starter.

Data loading and validation are supplied. Students implement the finance logic in the
three deliberately unfinished functions. Monetary amounts use the same synthetic units.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "scenario",
    "ebitda",
    "depreciation_amortization",
    "interest_expense",
    "total_debt",
    "cash",
}


def load_scenarios(path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    numeric = REQUIRED_COLUMNS.difference({"scenario"})
    if frame[list(numeric)].isna().any().any():
        raise ValueError("Scenario inputs cannot be blank")
    if (frame["interest_expense"] <= 0).any() or (frame["ebitda"] <= 0).any():
        raise ValueError("EBITDA and interest expense must be positive")
    return frame


def calculate_stress_metrics(frame: pd.DataFrame) -> pd.DataFrame:
    """Return scenario, Debt/EBITDA, EBIT/interest, and cash.

    This is a material course objective and is intentionally unfinished.
    """
    raise NotImplementedError("Implement linked credit-stress metrics")


def test_covenants(
    metrics: pd.DataFrame,
    *,
    max_leverage: float = 5.0,
    min_coverage: float = 2.5,
    min_cash: float = 50.0,
) -> pd.DataFrame:
    """Return transparent Boolean breach flags for every threshold."""
    raise NotImplementedError("Implement covenant tests without hiding thresholds")


def committee_action(results: pd.DataFrame) -> pd.DataFrame:
    """Add an action and monitoring trigger; do not equate breach with default."""
    raise NotImplementedError("Translate evidence into a conditional committee action")


if __name__ == "__main__":
    source = Path(__file__).with_name("stress_scenarios.csv")
    scenarios = load_scenarios(source)
    print(scenarios.to_string(index=False))
    print("\nStarter boundary: calculate_stress_metrics, test_covenants, and committee_action remain STUDENT_WORK.")

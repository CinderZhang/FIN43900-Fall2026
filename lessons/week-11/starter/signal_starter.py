"""Week 11 data infrastructure; backtest design and decision remain student work."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {"period", "signal", "next_return", "regime", "one_way_cost_bps"}


def load_panel(path: str | Path) -> pd.DataFrame:
    """Load and validate the ordered synthetic signal panel."""
    frame = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    expected_periods = list(range(1, len(frame) + 1))
    if list(frame.period) != expected_periods:
        raise ValueError("Periods must be ordered and unique")
    return frame


def preregistered_strategy_returns(frame: pd.DataFrame) -> pd.Series:
    raise NotImplementedError("Implement only the frozen rule; do not tune on holdout")


def net_of_cost_returns(frame: pd.DataFrame, positions: pd.Series) -> pd.Series:
    raise NotImplementedError("Define turnover and cost timing explicitly")


def robustness_report(frame: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError("Compare baseline, holdout, costs, subperiods, and placebo")


if __name__ == "__main__":
    panel = load_panel(Path(__file__).with_name("signal_development.csv"))
    print(panel.groupby("regime").size())
    print("Material strategy and robustness functions remain STUDENT_WORK.")

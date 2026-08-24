"""Load synthetic recommendation scenarios; the advisory decision remains unfinished."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ALLOCATION_COLUMNS = ["equity_pct", "fixed_income_pct", "cash_pct", "illiquid_pct"]


def load(folder: str | Path) -> tuple[dict, pd.DataFrame, pd.DataFrame]:
    root = Path(folder)
    with (root / "client_case.json").open(encoding="utf-8") as stream:
        case = json.load(stream)
    portfolios = pd.read_csv(root / "model_portfolios.csv")
    scenarios = pd.read_csv(root / "scenarios.csv")
    if not portfolios[ALLOCATION_COLUMNS].sum(axis=1).between(99.999999, 100.000001).all():
        raise ValueError("Every model portfolio allocation must sum to 100 percent")
    if set(scenarios.scenario) != {"Base", "JobLoss", "LiquidityShock"}:
        raise ValueError("Required scenario set is incomplete")
    return case, portfolios, scenarios


def future_value_after_fee(
    principal: float, gross_return: float, annual_fee: float, years: int
) -> float:
    """Teaching convention: fee is subtracted from annual gross return before compounding."""
    if principal < 0 or years < 0 or gross_return <= -1 or annual_fee < 0:
        raise ValueError("Inputs fall outside the teaching convention")
    return principal * (1 + gross_return - annual_fee) ** years


def scenario_admissibility(portfolios: pd.DataFrame, scenarios: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError("Re-run all hard limits and retain reason codes for every scenario")


def audit_recommendation(
    recommendation: dict, portfolios: pd.DataFrame, scenario_report: pd.DataFrame
) -> dict:
    raise NotImplementedError("Audit facts, fees, conflicts, omissions, and unsupported certainty")


def write_client_explanation(audit: dict) -> str:
    raise NotImplementedError("Explanation must preserve uncertainty and human escalation")


if __name__ == "__main__":
    case, portfolios, scenarios = load(Path(__file__).parent)
    low_fee = future_value_after_fee(500_000, 0.06, 0.0025, 10)
    high_fee = future_value_after_fee(500_000, 0.06, 0.0090, 10)
    print(case["case_label"])
    print(f"Fee-drag anchor: ${low_fee - high_fee:,.2f}")

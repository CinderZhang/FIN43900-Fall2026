"""Load a fictional client case; suitability judgment remains deliberately unfinished."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


REQUIRED_CASE_FIELDS = {
    "case_label",
    "decision_user",
    "decision",
    "horizon_years",
    "target_net_return_pct",
    "max_one_year_loss_pct",
    "max_equity_pct",
    "min_cash_pct",
    "max_illiquid_pct",
    "max_fee_pct",
    "unknowns_requiring_escalation",
}
ALLOCATION_COLUMNS = ["equity_pct", "fixed_income_pct", "cash_pct", "illiquid_pct"]


def load(folder: str | Path) -> tuple[dict, pd.DataFrame]:
    root = Path(folder)
    with (root / "client_case.json").open(encoding="utf-8") as stream:
        case = json.load(stream)
    missing = REQUIRED_CASE_FIELDS.difference(case)
    if missing:
        raise ValueError(f"Client case missing fields: {sorted(missing)}")
    portfolios = pd.read_csv(root / "model_portfolios.csv")
    required_columns = {
        "portfolio",
        "gross_return_pct",
        "annual_fee_pct",
        "volatility_pct",
        "max_drawdown_pct",
        *ALLOCATION_COLUMNS,
    }
    missing_columns = required_columns.difference(portfolios.columns)
    if missing_columns:
        raise ValueError(f"Portfolio table missing columns: {sorted(missing_columns)}")
    allocation_total = portfolios[ALLOCATION_COLUMNS].sum(axis=1)
    if not allocation_total.between(99.999999, 100.000001).all():
        raise ValueError("Every model portfolio allocation must sum to 100 percent")
    portfolios = portfolios.assign(
        net_return_pct=portfolios["gross_return_pct"] - portfolios["annual_fee_pct"]
    )
    return case, portfolios


def assess_admissibility(case: dict, portfolios: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError("Translate each hard client limit into transparent reason codes")


def compare_admissible(case: dict, admissible: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError("Comparison cannot silently turn a return target into a guarantee")


def draft_conditional_recommendation(case: dict, comparison: pd.DataFrame) -> str:
    raise NotImplementedError("A human must own unknowns, conflicts, conditions, and escalation")


if __name__ == "__main__":
    client, candidates = load(Path(__file__).parent)
    print(client["case_label"])
    print(candidates.to_string(index=False))

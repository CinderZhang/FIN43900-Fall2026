"""Load the fictional Week 14 portfolio; material stress/rebalance logic is unfinished."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


PORTFOLIO_REQUIRED = {
    "bond_id", "weight", "modified_duration", "spread_bps", "stale_days",
    "trade_count_20d", "issuer", "sector",
}
SCENARIO_REQUIRED = {"scenario", "rate_shock_bps", "spread_shock_bps"}
MANDATE_REQUIRED = {
    "duration_min", "duration_max", "max_issuer_weight", "max_sector_weight",
    "max_abs_spread_scenario_loss", "min_liquid_weight", "liquid_max_stale_days",
    "liquid_min_trade_count_20d", "no_add_if_stale_days_above",
}


def load(folder: str | Path) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Load portfolio, scenarios, and mandate; enforce a complete weight vector."""
    root = Path(folder)
    portfolio = pd.read_csv(root / "portfolio.csv")
    scenarios = pd.read_csv(root / "scenarios.csv")
    with (root / "mandate.json").open(encoding="utf-8") as stream:
        mandate = json.load(stream)
    missing_portfolio = PORTFOLIO_REQUIRED.difference(portfolio.columns)
    missing_scenarios = SCENARIO_REQUIRED.difference(scenarios.columns)
    missing_mandate = MANDATE_REQUIRED.difference(mandate)
    if missing_portfolio:
        raise ValueError(f"Portfolio missing columns: {sorted(missing_portfolio)}")
    if missing_scenarios:
        raise ValueError(f"Scenarios missing columns: {sorted(missing_scenarios)}")
    if missing_mandate:
        raise ValueError(f"Mandate missing keys: {sorted(missing_mandate)}")
    if portfolio.bond_id.duplicated().any():
        raise ValueError("bond_id must be unique")
    if abs(portfolio.weight.sum() - 1) > 1e-10:
        raise ValueError("Weights must sum to one")
    return portfolio, scenarios, mandate


def stress_portfolio(portfolio: pd.DataFrame, scenarios: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError("Implement separate rate and spread approximations")


def constraint_report(portfolio: pd.DataFrame, mandate: dict) -> pd.DataFrame:
    raise NotImplementedError("Test every mandate constraint transparently")


def propose_rebalance(portfolio: pd.DataFrame, mandate: dict) -> pd.DataFrame:
    raise NotImplementedError("Recommendation requires human-owned tradeoffs")


if __name__ == "__main__":
    portfolio, scenarios, mandate = load(Path(__file__).parent)
    print(portfolio.to_string(index=False))
    print(mandate)

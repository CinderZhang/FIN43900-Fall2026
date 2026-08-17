"""Fixed-income teaching infrastructure using only fictional course-authored records."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


REQUIRED_COLUMNS = {
    "bond_id",
    "coupon_rate",
    "years_to_maturity",
    "ytm",
    "price",
    "modified_duration",
    "convexity",
    "spread_bps",
    "stale_days",
    "trade_count_20d",
}


def load_bonds(path: str | Path) -> pd.DataFrame:
    """Load fictional bond records and validate the supplied schema/identifiers."""
    bonds = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(bonds.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    if bonds.bond_id.duplicated().any():
        raise ValueError("bond_id must be unique")
    return bonds


def annual_cash_flows(coupon_rate: float, years: int, par: float = 100) -> np.ndarray:
    """Build annual coupon/principal cash flows for the coupon-date teaching anchor."""
    if years < 1:
        raise ValueError("years must be positive")
    cash_flows = np.repeat(coupon_rate * par, years).astype(float)
    cash_flows[-1] += par
    return cash_flows


def price_yield_duration(coupon_rate: float, years: int, ytm: float, par: float = 100) -> dict:
    raise NotImplementedError("Implement price, Macaulay/modified duration, and convexity")


def screen_bonds(bonds: pd.DataFrame, mandate: dict) -> pd.DataFrame:
    raise NotImplementedError("Adapt and disclose a transparent mandate screen")


def recommendation(screen: pd.DataFrame) -> str:
    raise NotImplementedError("A screen cannot issue an unconditional investment recommendation")


if __name__ == "__main__":
    bonds = load_bonds(Path(__file__).with_name("synthetic_bonds.csv"))
    columns = ["bond_id", "spread_bps", "stale_days", "trade_count_20d"]
    print(bonds[columns].to_string(index=False))
    print("All records are synthetic teaching data.")

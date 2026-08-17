"""FIN 43900 Week 1 company-screening infrastructure.

Data retrieval and basic price diagnostics are provided because the lesson outcome is the
screening policy, evidence reconciliation, robustness test, and provisional decision. The
scoring/filtering rule is intentionally unfinished.
"""

from __future__ import annotations

import warnings

import numpy as np
import pandas as pd
import yfinance as yf


DEFAULT_UNIVERSE = [
    "MSFT",
    "AAPL",
    "GOOGL",
    "AMZN",
    "META",
    "NVDA",
    "JNJ",
    "PG",
    "KO",
    "PEP",
    "HD",
    "LOW",
    "CAT",
    "DE",
    "HON",
    "UPS",
    "FDX",
    "NEE",
    "DUK",
    "CVX",
    "XOM",
    "LIN",
    "APD",
]
MIN_COVERAGE_DAYS = 365


def download_adjusted_prices(tickers: list[str], period: str = "3y") -> pd.DataFrame:
    """Download adjusted daily close values and retain only usable columns."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", FutureWarning)
        raw = yf.download(
            tickers,
            period=period,
            interval="1d",
            auto_adjust=False,
            actions=False,
            progress=False,
            group_by="column",
            threads=True,
            timeout=20,
        )
    if raw.empty:
        raise ValueError("The provider returned no data. Preserve this error and use the fallback.")

    if isinstance(raw.columns, pd.MultiIndex):
        if "Adj Close" not in raw.columns.get_level_values(0):
            raise ValueError(
                "Adjusted Close is unavailable; do not substitute unadjusted Close silently. "
                "Preserve the error and use the labeled fallback."
            )
        prices = raw["Adj Close"].copy()
    else:
        if "Adj Close" not in raw.columns:
            raise ValueError(
                "Adjusted Close is unavailable; do not substitute unadjusted Close silently. "
                "Preserve the error and use the labeled fallback."
            )
        prices = raw[["Adj Close"]].rename(columns={"Adj Close": tickers[0]})

    prices = prices.sort_index().dropna(axis=1, how="all")
    if prices.shape[1] < 5:
        raise ValueError(f"Only {prices.shape[1]} usable companies returned; expected at least 5")
    prices.attrs["price_basis"] = "ADJUSTED_CLOSE_TOTAL_RETURN_BASIS"
    prices.attrs["provider"] = "Yahoo Finance via yfinance"
    return prices


def compute_price_diagnostics(prices: pd.DataFrame, risk_free_rate: float = 0.04) -> pd.DataFrame:
    """Compute transparent candidate diagnostics; these are not a completed screen."""
    rows: list[dict[str, float | int | str]] = []
    for ticker in prices.columns:
        series = prices[ticker].dropna().astype(float)
        if len(series) < 2:
            continue
        elapsed_days = max((series.index[-1] - series.index[0]).days, 1)
        elapsed_years = elapsed_days / 365.25
        cumulative_return = series.iloc[-1] / series.iloc[0] - 1
        if elapsed_days < MIN_COVERAGE_DAYS:
            annualized_return = np.nan
            return_status = "QUARANTINED_INSUFFICIENT_COVERAGE"
        else:
            annualized_return = (1 + cumulative_return) ** (1 / elapsed_years) - 1
            return_status = "SUFFICIENT_COVERAGE"
        valid_returns = series.pct_change(fill_method=None).dropna()
        volatility = valid_returns.std() * np.sqrt(252)
        missing_share = float(prices[ticker].isna().mean())
        # A missing interval can hide the true peak-to-trough path. Quarantine rather than
        # treating the gap as a zero return or reporting an artificially improved drawdown.
        if missing_share > 0:
            maximum_drawdown = np.nan
            drawdown_status = "QUARANTINED_MISSING_PRICE_PATH"
        else:
            wealth = (1 + valid_returns).cumprod()
            maximum_drawdown = float((wealth / wealth.cummax() - 1).min())
            drawdown_status = "COMPLETE_PRICE_PATH"
        rows.append(
            {
                "ticker": ticker,
                "annualized_return": annualized_return,
                "return_status": return_status,
                "annualized_volatility": volatility,
                "excess_return_to_vol": (
                    (annualized_return - risk_free_rate) / volatility
                    if volatility and not np.isnan(volatility)
                    else np.nan
                ),
                "max_drawdown": maximum_drawdown,
                "drawdown_status": drawdown_status,
                "positive_day_share": float((valid_returns > 0).mean()),
                "usable_observations": int(valid_returns.count()),
                "missing_share": missing_share,
                "coverage_years": elapsed_years,
            }
        )

    metrics = pd.DataFrame(rows).set_index("ticker")
    return metrics.sort_index()


def apply_student_screen(metrics: pd.DataFrame) -> pd.DataFrame:
    """STUDENT_WORK: implement and explain your own filters, weights, or ranking rule.

    Requirements:
    - do not mutate the input DataFrame in place;
    - state every definition, threshold/weight, and exclusion in the handout;
    - expose rather than silently drop missing values;
    - return a DataFrame containing a transparent `screen_score` or pass/fail columns; and
    - do not present the score as a buy recommendation.
    """
    candidate_table = metrics.copy()
    candidate_table["screen_score"] = np.nan
    candidate_table["student_note"] = "STUDENT_WORK - implement and explain the screening policy"
    return candidate_table


def main() -> None:
    prices = download_adjusted_prices(DEFAULT_UNIVERSE)
    metrics = compute_price_diagnostics(prices)
    output = apply_student_screen(metrics)

    print("Returned period:", prices.index.min().date(), "to", prices.index.max().date())
    print("Price basis:", prices.attrs.get("price_basis", "UNLABELED - STOP AND INVESTIGATE"))
    print("Provider:", prices.attrs.get("provider", "UNLABELED - STOP AND INVESTIGATE"))
    print("Usable companies:", len(metrics))
    print("\nBasic diagnostics - NOT a completed ranking:\n")
    print(output.round(4).head(12).to_string())
    output.to_csv("week1_screening_working_table.csv")
    print("\nSaved week1_screening_working_table.csv")
    print("Complete apply_student_screen(), rerun, validate one definition, and attack one input.")


if __name__ == "__main__":
    main()

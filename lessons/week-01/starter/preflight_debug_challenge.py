"""FIN 43900 Week 1 deliberately broken debugging challenge.

The file contains three defects. Ask Codex and Gemini separately to diagnose them, preserve
both answers, then arbitrate with Python evidence and finance logic. Do not submit API keys or
account information in a prompt.
"""

from __future__ import annotations

import warnings

import numpy as np
import pandas as pd
import yfinance as yf


warnings.filterwarnings("ignore", category=FutureWarning, message=r".*ChainedAssignmentError.*")


RISK_FREE_RATE = 0.04


def download_price_history(ticker: str) -> pd.DataFrame:
    """Download one year of daily price history."""
    return yf.Ticker(ticker).history(period="1y", auto_adjust=True)


def compute_metrics(ticker: str) -> dict[str, float]:
    """Return annualized return, volatility, and Sharpe ratio."""
    history = download_price_history(ticker)

    close_prices = price_history["Close"]
    daily_returns = close_prices.pct_change().dropna()

    annualized_return = daily_returns.mean() * 252
    annualized_volatility = daily_returns.std() * np.sqrt(252)
    observation_count = daily_returns.counts()

    daily_volatility = daily_returns.std()
    sharpe_ratio = annualized_return / daily_volatility

    return {
        "ticker": ticker,
        "observations": observation_count,
        "annualized_return": annualized_return,
        "annualized_volatility": annualized_volatility,
        "sharpe_ratio": sharpe_ratio,
    }


def print_report(metrics: dict[str, float]) -> None:
    print(f"Ticker: {metrics['ticker']}")
    print(f"Observations: {metrics['observations']}")
    print(f"Annualized return: {metrics['annualized_return']:.2%}")
    print(f"Annualized volatility: {metrics['annualized_volatility']:.2%}")
    print(f"Sharpe ratio: {metrics['sharpe_ratio']:.3f}")


if __name__ == "__main__":
    print_report(compute_metrics("AAPL"))

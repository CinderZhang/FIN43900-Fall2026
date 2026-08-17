"""FIN 43900 Week 1 technology-readiness diagnostic.

This script verifies the evidence-producing path used in class. A network/provider failure is
reported separately from the local Python/plotting path; the deterministic fallback is not
presented as live market data.
"""

from __future__ import annotations

import platform
import warnings
from pathlib import Path


def record(results: dict[str, tuple[str, str]], name: str, state: str, detail: str) -> None:
    """Store a student readiness state, distinct from software health diagnostics."""
    results[name] = (state, detail)
    print(f"[{state}] {name}: {detail}")


def deterministic_fallback(pd, np):
    """Return clearly labeled synthetic prices for an offline plotting check."""
    dates = pd.date_range("2026-01-02", periods=30, freq="B")
    returns = np.array(
        [
            0.004,
            -0.002,
            0.006,
            0.001,
            -0.003,
            0.005,
            0.002,
            -0.004,
            0.003,
            0.001,
        ]
        * 3
    )
    prices = 100 * (1 + pd.Series(returns, index=dates)).cumprod()
    prices.name = "SYNTHETIC_CLOSE_NOT_MARKET_DATA"
    return prices


def main() -> int:
    print("=" * 68)
    print("FIN 43900 - WEEK 1 TECHNOLOGY READINESS")
    print("=" * 68)
    print(f"Python: {platform.python_version()} ({platform.system()})")
    print("Do not paste credentials, tokens, billing pages, or private account data here.\n")

    results: dict[str, tuple[str, str]] = {}

    try:
        import matplotlib
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
        import yfinance as yf

        detail = (
            f"pandas {pd.__version__}; numpy {np.__version__}; "
            f"matplotlib {matplotlib.__version__}; yfinance {yf.__version__}"
        )
        record(results, "Required imports", "READY", detail)
    except Exception as exc:
        record(results, "Required imports", "RECOVERING", repr(exc))
        print("\nInstall Lab Environment Requirements (requirements-course.txt) from Start Here; "
              "if you are using the Week 1 standalone package, requirements-week1.txt contains "
              "the Week 1 subset. Restart the runtime and rerun.")
        return 1

    series = None
    series_label = None

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", FutureWarning)
            raw = yf.download(
                "AAPL",
                period="6mo",
                interval="1d",
                auto_adjust=False,
                actions=False,
                progress=False,
                timeout=15,
            )
        if raw.empty:
            raise ValueError("provider returned an empty table")

        column = "Adj Close" if "Adj Close" in raw.columns else "Close"
        selected = raw[column]
        if getattr(selected, "ndim", 1) == 2:
            selected = selected.iloc[:, 0]
        selected = selected.dropna().astype(float)
        if len(selected) < 50:
            raise ValueError(f"expected at least 50 usable observations; received {len(selected)}")

        series = selected
        series_label = f"AAPL {column} (live provider response)"
        detail = (
            f"{len(series)} rows; {series.index.min().date()} to "
            f"{series.index.max().date()}; last value {series.iloc[-1]:.2f}"
        )
        record(results, "Market-data retrieval", "READY", detail)
    except Exception as exc:
        record(results, "Market-data retrieval", "RECOVERING", repr(exc))
        series = deterministic_fallback(pd, np)
        series_label = "Synthetic offline fallback - NOT market evidence"
        print("Using deterministic synthetic values only to test Python and plotting.")

    try:
        fig, ax = plt.subplots(figsize=(9, 4.5))
        series.plot(ax=ax, linewidth=1.6)
        ax.set_title(series_label)
        ax.set_xlabel("Date")
        ax.set_ylabel("Index/price level")
        ax.grid(True, alpha=0.25)
        fig.tight_layout()
        output = Path("fin439_week1_preflight.png")
        fig.savefig(output, dpi=120, bbox_inches="tight")
        plt.close(fig)
        record(results, "Visible chart output", "READY", str(output.resolve()))
    except Exception as exc:
        record(results, "Visible chart output", "RECOVERING", repr(exc))

    print("\n" + "=" * 68)
    print("RESULT SUMMARY")
    print("=" * 68)
    for name, (state, detail) in results.items():
        print(f"{state:10} | {name} | {detail}")

    recovering = [name for name, (state, _) in results.items() if state != "READY"]
    if recovering:
        print("\nRECOVERING: preserve the exact evidence and record a next action in the Week 1 readiness record.")
        print("Outstanding checks: " + ", ".join(recovering))
        return 2

    print("\nREADY: imports, live data retrieval, and visible output all succeeded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

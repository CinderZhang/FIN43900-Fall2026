"""Week 9 infrastructure. Portfolio construction and judgment remain student work."""

from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd


def load_inputs(folder: str | Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    folder = Path(folder)
    stats = pd.read_csv(folder / "asset_statistics.csv")
    corr = pd.read_csv(folder / "correlation.csv", index_col="asset")
    assets = list(stats["asset"])
    if list(corr.index) != assets or list(corr.columns) != assets:
        raise ValueError("Correlation matrix labels/order must match statistics")
    if not np.allclose(corr, corr.T) or not np.allclose(np.diag(corr), 1.0):
        raise ValueError("Correlation matrix must be symmetric with a unit diagonal")
    return stats, corr


def equal_weight(n_assets: int) -> np.ndarray:
    if n_assets <= 0:
        raise ValueError("n_assets must be positive")
    return np.repeat(1.0 / n_assets, n_assets)


def covariance_matrix(stats: pd.DataFrame, corr: pd.DataFrame) -> np.ndarray:
    raise NotImplementedError("Implement covariance = diag(vol) @ corr @ diag(vol)")


def constrained_allocation(stats: pd.DataFrame, covariance: np.ndarray, mandate: dict) -> np.ndarray:
    raise NotImplementedError("Implement and document one mandate-consistent allocation")


def perturbation_report(*args, **kwargs) -> pd.DataFrame:
    raise NotImplementedError("Test stability before recommending adoption")


if __name__ == "__main__":
    stats, corr = load_inputs(Path(__file__).parent)
    print(stats.to_string(index=False))
    print("Equal weight:", equal_weight(len(stats)))

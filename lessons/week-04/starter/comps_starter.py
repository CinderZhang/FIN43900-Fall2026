"""FIN 43900 Week 4 market-evidence starter.

Schemas and expected synthetic checkpoints are supplied. Students implement multiple
calculation, peer-policy filtering, source reconciliation, and triangulation.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_cases(folder: Path) -> tuple[pd.DataFrame, dict[str, float], dict[str, float]]:
    peers = pd.read_csv(folder / "peer_case.csv")
    target_table = pd.read_csv(folder / "target_case.csv")
    expected_table = pd.read_csv(folder / "expected_output.csv")
    target = target_table.set_index("metric")["value"].astype(float).to_dict()
    expected = expected_table.set_index("output")["expected_value"].astype(float).to_dict()
    return peers, target, expected


def calculate_peer_multiples(peers: pd.DataFrame) -> pd.DataFrame:
    """STUDENT_WORK: calculate consistent enterprise and equity multiples."""
    raise NotImplementedError


def implied_target_values(
    peer_multiples: pd.DataFrame, target: dict[str, float]
) -> dict[str, float]:
    """STUDENT_WORK: calculate median trading and precedent implied per-share values."""
    raise NotImplementedError


def apply_peer_policy(peers: pd.DataFrame, policy: dict) -> pd.DataFrame:
    """STUDENT_WORK: apply the student's source-supported inclusion/qualification policy."""
    raise NotImplementedError


def main() -> None:
    folder = Path(__file__).resolve().parent
    peers, target, expected = load_cases(folder)
    print(f"Synthetic peers loaded: {len(peers)}; target fields: {len(target)}")
    print("Expected checkpoints:")
    for name, value in expected.items():
        print(f"  {name}: {value:.4f}")
    print("Implement the STUDENT_WORK functions, reconcile checkpoints, then audit real candidates.")


if __name__ == "__main__":
    main()

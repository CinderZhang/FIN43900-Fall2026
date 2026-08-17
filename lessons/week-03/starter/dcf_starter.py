"""FIN 43900 Week 3 DCF starter.

The input contract, boundary validation, and expected synthetic outputs are supplied. Students
implement the material projection, valuation, sensitivity, and reverse-DCF functions with AI
assistance, then explain and validate every result.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_named_values(path: str | Path, name_column: str, value_column: str) -> dict[str, float]:
    table = pd.read_csv(path)
    if name_column not in table or value_column not in table:
        raise ValueError(f"Required columns absent: {name_column}, {value_column}")
    if table[name_column].duplicated().any():
        raise ValueError(f"Duplicate names in {name_column}")
    return table.set_index(name_column)[value_column].astype(float).to_dict()


def validate_case(inputs: dict[str, float]) -> None:
    if inputs["terminal_growth"] >= inputs["wacc"]:
        raise ValueError("Terminal growth must be strictly less than WACC")
    if inputs["diluted_shares"] <= 0:
        raise ValueError("Diluted shares must be positive")
    if inputs["starting_fcff"] <= 0:
        raise ValueError("Training-case starting FCFF must be positive")
    for year in range(1, 6):
        growth = inputs[f"growth_year_{year}"]
        if growth <= -1:
            raise ValueError(f"Year {year} growth cannot be -100% or lower")


def project_fcff(inputs: dict[str, float]) -> list[float]:
    """STUDENT_WORK: sequentially project five annual FCFF values from starting FCFF."""
    raise NotImplementedError


def value_dcf(inputs: dict[str, float], projected_fcff: list[float]) -> dict[str, float]:
    """STUDENT_WORK: discount explicit FCFF, terminal value, and the equity bridge."""
    raise NotImplementedError


def sensitivity_table(
    inputs: dict[str, float], wacc_values: list[float], terminal_growth_values: list[float]
) -> pd.DataFrame:
    """STUDENT_WORK: return per-share values indexed by WACC and terminal growth."""
    raise NotImplementedError


def reverse_dcf_for_growth(
    inputs: dict[str, float], observed_price: float, lower: float, upper: float
) -> float:
    """STUDENT_WORK: solve one clearly named growth assumption while holding others fixed."""
    raise NotImplementedError


def main() -> None:
    folder = Path(__file__).resolve().parent
    inputs = load_named_values(folder / "dcf_case.csv", "input", "value")
    expected = load_named_values(
        folder / "dcf_expected_output.csv", "output", "expected_value"
    )
    validate_case(inputs)

    print("DCF training-case inputs validated.")
    print("Expected synthetic checkpoints:")
    for name, value in expected.items():
        print(f"  {name}: {value:.6f}")
    print("\nImplement the four STUDENT_WORK functions, reconcile every checkpoint, then transfer inputs.")


if __name__ == "__main__":
    main()

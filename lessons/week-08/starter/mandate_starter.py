"""Validate mandate completeness without choosing preferences or an optimizer."""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED = {
    "decision_user", "decision", "objective", "horizon_years", "benchmark",
    "risk_measure", "constraints", "validation_tests", "unresolved_ambiguity",
}


def load_mandate(path: str | Path) -> dict:
    with open(path, encoding="utf-8") as stream:
        record = json.load(stream)
    missing = REQUIRED.difference(record)
    if missing:
        raise ValueError(f"Missing mandate fields: {sorted(missing)}")
    return record


def completeness_gaps(record: dict) -> list[str]:
    gaps = []
    for field in REQUIRED:
        value = record[field]
        if value in ("", None, []) or (field == "constraints" and len(value) < 4):
            gaps.append(field)
    return sorted(gaps)


def choose_optimal_portfolio(record: dict) -> None:
    raise NotImplementedError("A mandate record cannot choose investor preferences or an optimizer")


if __name__ == "__main__":
    mandate = load_mandate(Path(__file__).with_name("mandate_template.json"))
    print("Incomplete fields:", ", ".join(completeness_gaps(mandate)))

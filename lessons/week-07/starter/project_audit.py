"""Mechanical Project 1 manifest audit; finance quality and authorship remain human review."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "item",
    "required",
    "location_or_url",
    "title",
    "duration_or_as_of",
    "timestamp_index",
    "access_checked",
    "frozen_or_commit_id",
    "notes",
}
VIDEO_ITEMS = {"Video 1", "Video 2", "Video 3"}


def load_manifest(path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(path, keep_default_na=False)
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    if len(frame) != 12:
        raise ValueError(f"Expected 12 manifest rows; received {len(frame)}")
    return frame


def mechanical_gaps(frame: pd.DataFrame) -> list[str]:
    gaps: list[str] = []
    for row in frame.to_dict(orient="records"):
        if row["required"].lower() != "yes":
            continue
        base_ready = all(
            row[field].strip()
            for field in ("location_or_url", "access_checked", "frozen_or_commit_id")
        )
        video_ready = row["item"] not in VIDEO_ITEMS or all(
            row[field].strip()
            for field in ("title", "duration_or_as_of", "timestamp_index")
        )
        if not (base_ready and video_ready):
            gaps.append(row["item"])
    return gaps


def evaluate_finance_quality(frame: pd.DataFrame) -> None:
    raise NotImplementedError("A manifest cannot evaluate financial soundness or ownership")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit the completed shared 12-row project submission manifest."
    )
    parser.add_argument(
        "manifest",
        type=Path,
        help="path to your completed project-submission-manifest-template.csv",
    )
    args = parser.parse_args()
    manifest = load_manifest(args.manifest)
    print("Mechanical gaps:")
    for item in mechanical_gaps(manifest):
        print(f"- {item}")


if __name__ == "__main__":
    main()

"""Infrastructure for a point-in-time data audit; admission judgment remains unfinished."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


TIME_COLUMNS = ["event_time", "available_time"]


def load_events(path: str | Path) -> pd.DataFrame:
    """Load the event panel and normalize event/availability timestamps to UTC."""
    frame = pd.read_csv(path)
    return frame.assign(
        **{column: pd.to_datetime(frame[column], utc=True) for column in TIME_COLUMNS}
    )


def mechanical_flags(frame: pd.DataFrame, decision_time: str) -> pd.DataFrame:
    """Expose timing, identity, duplicate, and revision flags without deciding admission."""
    output = frame.copy()
    cutoff = pd.Timestamp(decision_time)
    return output.assign(
        late_available=output.available_time > cutoff,
        missing_entity=output.entity_id.isna(),
        exact_duplicate=output.duplicated(
            ["entity_id", "event_time", "available_time", "signal"], keep=False
        ),
        is_revision=output.revision > 0,
    )


def construct_point_in_time_panel(frame: pd.DataFrame, decision_time: str) -> pd.DataFrame:
    raise NotImplementedError("Define and defend the as-of and revision policy")


def admission_decision(audit: pd.DataFrame) -> str:
    raise NotImplementedError("Human judgment must decide admit, quarantine, or reject")


if __name__ == "__main__":
    events = load_events(Path(__file__).with_name("alternative_events.csv"))
    columns = ["row_id", "late_available", "missing_entity", "exact_duplicate", "is_revision"]
    print(mechanical_flags(events, "2026-01-02T10:00:00Z")[columns].to_string(index=False))

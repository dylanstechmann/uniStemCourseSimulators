"""Generate the deterministic public data for the inactive programming project draft."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

BATCHES = (
    ("B01", "train", -1.0),
    ("B02", "train", 0.0),
    ("B03", "train", 0.0),
    ("B04", "train", 1.0),
    ("B05", "held_out", 4.0),
    ("B06", "held_out", -3.0),
)
STANDARDS_MM = (0.0, 0.5, 1.0, 2.0, 4.0)
REPLICATE_OFFSETS_MV = (-0.2, 0.0, 0.2)
FIELDS = ("record_id", "batch_id", "split", "standard_mM", "signal_mV", "replicate_id")


def build_rows() -> list[dict[str, str]]:
    """Return balanced calibration records from the documented fixed equation."""
    rows: list[dict[str, str]] = []
    for batch_id, split, batch_offset in BATCHES:
        for level_index, standard in enumerate(STANDARDS_MM, start=1):
            for replicate_index, replicate_offset in enumerate(REPLICATE_OFFSETS_MV, start=1):
                signal = 20.0 + 3.0 * standard + batch_offset + replicate_offset
                rows.append(
                    {
                        "record_id": f"{batch_id}-L{level_index}-R{replicate_index}",
                        "batch_id": batch_id,
                        "split": split,
                        "standard_mM": f"{standard:g}",
                        "signal_mV": f"{signal:.1f}",
                        "replicate_id": f"R{replicate_index}",
                    }
                )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("sensor-calibration-records.csv"),
    )
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(build_rows())


if __name__ == "__main__":
    main()

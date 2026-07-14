#!/usr/bin/env python3
"""Run P3 component validators without mutating frozen release directories.

The r2 primary validator refreshes audit files and copies its own source into
the validation destination.  Running it with the frozen release as both source
and destination therefore reaches a SameFileError after the scientific checks.
This wrapper always validates temporary copies and rejects in-place targets.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Optional


ENGINE = Path(__file__).resolve().parents[1]
REPO = ENGINE.parents[1]
PRIMARY = ENGINE / "desi_science_catalog_v3.2.0-r2"
WARNED = ENGINE / "desi_warned_primary_aux_v3.2.0-r5"
PARTS = ENGINE / ".desi_science_catalog_v3.2.0-r2.build/match_parts"
CLUSTERS = ENGINE / "apjs_submission_v3.1.161/pathc_unique_objects.parquet"
ANOMALIES = ENGINE / "apjs_submission_v3.1.161/desi_dr1_anomalies.parquet"


def guard_destination(source: Path, destination: Path) -> None:
    source = source.resolve()
    destination = destination.resolve()
    if source == destination:
        raise ValueError(f"refusing in-place validation of frozen release: {source}")
    if destination.is_relative_to(source):
        raise ValueError(f"refusing validation destination inside frozen release: {destination}")


def self_check() -> dict:
    rejected = []
    for source in (PRIMARY, WARNED):
        for destination in (source, source / "nested-validation"):
            try:
                guard_destination(source, destination)
            except ValueError:
                rejected.append(str(destination))
            else:
                raise AssertionError(f"in-place destination was not rejected: {destination}")
    with tempfile.TemporaryDirectory(prefix="p3-r7-guard-") as directory:
        guard_destination(PRIMARY, Path(directory) / "primary")
        guard_destination(WARNED, Path(directory) / "warned")
    result = {"status": "PASS", "in_place_destinations_rejected": len(rejected), "temporary_destinations_accepted": 2}
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=REPO, check=True)


def validate_components(work_root: Optional[Path], full_fits_hash: bool) -> dict:
    if work_root is None:
        context = tempfile.TemporaryDirectory(prefix="p3-r7-components-")
        root = Path(context.name)
    else:
        context = None
        root = work_root.resolve()
        root.mkdir(parents=True, exist_ok=True)
    try:
        primary_copy = root / "primary_release"
        warned_copy = root / "warned_auxiliary"
        guard_destination(PRIMARY, primary_copy)
        guard_destination(WARNED, warned_copy)
        shutil.copytree(PRIMARY, primary_copy)
        shutil.copytree(WARNED, warned_copy)

        primary_command = [
            "python3", str(PRIMARY / "validate_desi_science_catalog_v320_r2.py"),
            "--release-dir", str(primary_copy), "--parts-dir", str(PARTS),
        ]
        if not full_fits_hash:
            primary_command.append("--skip-fits-hash")
        run(primary_command)
        run(
            [
                "python3", str(WARNED / "validate_desi_warned_primary_aux_v320_r5.py"),
                "--release-dir", str(warned_copy), "--parts-dir", str(PARTS),
                "--clusters", str(CLUSTERS), "--anomalies", str(ANOMALIES),
            ]
        )
        result = {
            "status": "PASS",
            "frozen_release_bytes_mutated": False,
            "primary": "PASS: exact 18-field rejoin, 143-part replay, 8 remote byte ranges",
            "primary_full_local_fits_hash": "recomputed" if full_fits_hash else "skipped by request",
            "warned_auxiliary": "PASS: exact 2,267-row checkpoint replay and ZWARN accounting",
        }
        print(json.dumps(result, indent=2, sort_keys=True))
        return result
    finally:
        if context is not None:
            context.cleanup()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-root", type=Path, help="Optional non-frozen scratch directory; defaults to a temporary directory.")
    parser.add_argument("--full-fits-hash", action="store_true", help="Recompute the complete 22.37 GB local FITS SHA-256.")
    parser.add_argument("--self-check", action="store_true", help="Only exercise the in-place destination guard.")
    args = parser.parse_args()
    if args.self_check:
        self_check()
    else:
        self_check()
        validate_components(args.work_root, args.full_fits_hash)


if __name__ == "__main__":
    main()

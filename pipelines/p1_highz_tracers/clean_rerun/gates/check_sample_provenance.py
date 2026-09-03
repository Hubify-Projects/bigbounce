#!/usr/bin/env python3
"""Gate: fail on any non-science-target row in a flagship sample Parquet.

Prevents recurrence of the finding recorded in
`project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md`: the phase-3
S>8 sample was 84.8% sky fibers (negative TARGETID, or TARGETID>0 rows that
are still OBJTYPE=='SKY'). This script re-checks a built sample Parquet
against the same rule `build_flagship_sample.py --science-targets-only`
enforces at build time:

  - every row must have TARGETID > 0
  - if the sample carries an `objtype` column (i.e. it was built with
    `--science-targets-only`), every row must have objtype == 'TGT'
  - if the sample carries a `fiberstatus` column, every row must have
    fiberstatus == 0

A sample built WITHOUT `--science-targets-only` (the sealed/legacy
behaviour) has no `objtype`/`fiberstatus` columns to check — this gate then
only enforces the TARGETID > 0 sanity check, which is always a bug if it
fails (DESI TARGETID is never <= 0 for a real catalog row).

Usage:
    python check_sample_provenance.py --sample flagship_sample.parquet
Exits 0 on a clean sample, 1 with a diagnostic message otherwise.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any


class ProvenanceGateError(RuntimeError):
    """Raised when a sample fails the provenance gate."""


def check_sample_provenance(sample_path: Path) -> dict[str, Any]:
    """Load `sample_path` and enforce the science-target provenance rule.

    Returns a small report dict on success; raises `ProvenanceGateError`
    (with every offending row category counted, not just the first) on
    failure.
    """
    import pyarrow.parquet as pq

    if not sample_path.exists():
        raise ProvenanceGateError(f"sample not found: {sample_path}")

    table = pq.read_table(sample_path)
    columns = set(table.column_names)
    if "targetid" not in columns:
        raise ProvenanceGateError(f"sample has no targetid column: {sample_path}")

    n = table.num_rows
    targetids = table.column("targetid").to_pylist()

    negative_targetid_count = sum(1 for t in targetids if t is None or t <= 0)

    non_tgt_count = 0
    if "objtype" in columns:
        objtypes = table.column("objtype").to_pylist()
        non_tgt_count = sum(1 for o in objtypes if o != "TGT")

    bad_fiberstatus_count = 0
    if "fiberstatus" in columns:
        fiberstatuses = table.column("fiberstatus").to_pylist()
        bad_fiberstatus_count = sum(1 for f in fiberstatuses if f != 0)

    failures = []
    if negative_targetid_count:
        failures.append(f"{negative_targetid_count}/{n} rows have TARGETID <= 0")
    if non_tgt_count:
        failures.append(f"{non_tgt_count}/{n} rows have objtype != 'TGT'")
    if bad_fiberstatus_count:
        failures.append(f"{bad_fiberstatus_count}/{n} rows have fiberstatus != 0")

    if failures:
        raise ProvenanceGateError(
            f"sample provenance gate FAILED for {sample_path}: " + "; ".join(failures)
        )

    return {
        "sample": str(sample_path),
        "row_count": n,
        "checked_objtype": "objtype" in columns,
        "checked_fiberstatus": "fiberstatus" in columns,
        "status": "clean",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--sample", type=Path, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        report = check_sample_provenance(args.sample)
    except ProvenanceGateError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
    print(f"OK: {report}")


if __name__ == "__main__":
    main()

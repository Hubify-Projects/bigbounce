#!/usr/bin/env python3
"""Row12 pilot gate: thin wrapper over the CANONICAL provenance gate at
`pipelines/p1_highz_tracers/clean_rerun/gates/check_sample_provenance.py`
(never duplicated -- imported unmodified by file path). Adds a
`--shard-glob` mode to check every staged Row12 shard in one call and fail
closed on the first bad shard, since Row12 stages many small per-group
Parquet files rather than one merged sample.

Usage:
    python check_sample_provenance.py --sample flagship_sample.parquet
    python check_sample_provenance.py --shard-glob '/workspace/row12/shards/*.parquet'
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import sys
from pathlib import Path

CANONICAL_PATH = (
    Path(__file__).resolve().parents[3]
    / "p1_highz_tracers"
    / "clean_rerun"
    / "gates"
    / "check_sample_provenance.py"
)


def load_canonical():
    spec = importlib.util.spec_from_file_location("check_sample_provenance_canonical", CANONICAL_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sample", type=Path)
    ap.add_argument("--shard-glob", type=str)
    args = ap.parse_args()

    canonical = load_canonical()

    if args.shard_glob:
        paths = sorted(Path(p) for p in glob.glob(args.shard_glob))
        if not paths:
            print(f"FAIL: no shards matched {args.shard_glob}", file=sys.stderr)
            raise SystemExit(1)
        total_rows = 0
        for p in paths:
            try:
                report = canonical.check_sample_provenance(p)
            except canonical.ProvenanceGateError as exc:
                print(f"FAIL: {exc}", file=sys.stderr)
                raise SystemExit(1)
            total_rows += report["row_count"]
        print(f"OK: {len(paths)} shards, {total_rows} total rows, all clean")
        return

    if not args.sample:
        print("FAIL: must pass --sample or --shard-glob", file=sys.stderr)
        raise SystemExit(2)
    try:
        report = canonical.check_sample_provenance(args.sample)
    except canonical.ProvenanceGateError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
    print(f"OK: {report}")


if __name__ == "__main__":
    main()

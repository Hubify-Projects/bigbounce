#!/usr/bin/env python3
"""Sky-fraction-by-score-bin diagnostic for the AUG-011 clean-rerun sealed scan.

Standalone read-only diagnostic supporting
`project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md`: for the
receipt-verified, post-dedup scored population, joins every unique targetid
to the SHA-verified zcatalog (`OBJTYPE`/`COADD_FIBERSTATUS`, same rule as
`build_flagship_sample.py`'s `--science-targets-only`: a row is a "science
target" iff `OBJTYPE == 'TGT' AND COADD_FIBERSTATUS == 0`, TARGETID>0
asserted) and reports, for a fixed set of `anomaly_score` bins from 3.0 up
through the observed maximum, the sky/non-science fraction in each bin.
Never overwrites or modifies the sealed shards, contract, or zcatalog.

Fail-closed exactly like `build_flagship_sample.py --describe`: re-verifies
receipts against the contract before reading anything, and re-checks the
summary's `contract_sha256` binding.

Outputs (never emitted unless both writes succeed): a JSON report
(`--output-json`) with per-bin counts/fractions, and a PNG line+bar plot
(`--output-png`, matplotlib Agg backend, no display needed) of sky fraction
vs. score bin with total-row counts annotated.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sqlite3
import sys
import tempfile
import types
from pathlib import Path
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
BUILD_SAMPLE_MODULE_PATH = THIS_DIR / "build_flagship_sample.py"


def load_build_sample_module(path: Path = BUILD_SAMPLE_MODULE_PATH) -> types.ModuleType:
    spec = importlib.util.spec_from_file_location("build_flagship_sample_bound", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load build_flagship_sample module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_bins(max_score: float) -> list[tuple[float, float | None, str]]:
    """Bins [3,4) [4,5) [5,6) [6,8) [8,10) [10,max] — pre-declared edges."""
    edges = [3.0, 4.0, 5.0, 6.0, 8.0, 10.0]
    bins: list[tuple[float, float | None, str]] = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        bins.append((lo, hi, f"[{lo:g},{hi:g})"))
    last_lo = edges[-1]
    if max_score > last_lo:
        bins.append((last_lo, None, f"[{last_lo:g},{max_score:.2f}]"))
    else:
        bins.append((last_lo, None, f"[{last_lo:g},+)"))
    return bins


def run(contract_path: Path, shard_dir: Path, receipt_dir: Path, summary_path: Path,
        zcatalog_path: Path, output_json: Path, output_png: Path) -> dict[str, Any]:
    bfs = load_build_sample_module()
    contract_module = bfs.load_contract_module()
    contract = contract_module.read_json(contract_path)
    contract_module.verify_contract(contract)
    shards = contract_module.verify_receipts(contract_path, shard_dir, receipt_dir)
    summary = contract_module.read_json(summary_path)
    contract_sha = bfs.verify_summary_matches_contract(contract_module, contract, summary)

    with tempfile.TemporaryDirectory() as tmp:
        sqlite_path = Path(tmp) / "skyfrac.sqlite"
        connection = sqlite3.connect(sqlite_path)
        try:
            raw_rows = bfs._dedup_scores_into_sqlite(shards, connection)
            unique_rows = connection.execute("SELECT COUNT(*) FROM scored").fetchone()[0]
            if unique_rows == 0:
                raise RuntimeError("zero deduplicated rows found across all verified shards")
            max_score = connection.execute(
                "SELECT MAX(anomaly_score) FROM scored WHERE anomaly_score >= 3.0"
            ).fetchone()[0]
            if max_score is None:
                raise RuntimeError("no rows with anomaly_score >= 3.0 found")

            # Pull every unique targetid with score >= 3.0 in bounded batches.
            targetids: set[int] = set()
            cursor = connection.execute(
                "SELECT targetid FROM scored WHERE anomaly_score >= 3.0"
            )
            while True:
                batch = cursor.fetchmany(500_000)
                if not batch:
                    break
                targetids.update(int(row[0]) for row in batch)

            print(f"[sky_fraction] joining {len(targetids)} targetids (score>=3.0) to zcatalog…", file=sys.stderr)
            flags = bfs.load_science_target_flags(zcatalog_path, targetids)

            bins = make_bins(float(max_score))
            bin_stats = []
            for lo, hi, label in bins:
                if hi is None:
                    q = "SELECT targetid, anomaly_score FROM scored WHERE anomaly_score >= ?"
                    params: tuple = (lo,)
                else:
                    q = "SELECT targetid, anomaly_score FROM scored WHERE anomaly_score >= ? AND anomaly_score < ?"
                    params = (lo, hi)
                total = 0
                sky_or_bad = 0
                joined = 0
                for tid, score in connection.execute(q, params):
                    total += 1
                    info = flags.get(int(tid))
                    if info is None:
                        # TARGETID<=0, or TARGETID not found in zcatalog science HDU at all
                        sky_or_bad += 1
                        continue
                    joined += 1
                    if info["objtype"] != "TGT" or info["fiberstatus"] != 0:
                        sky_or_bad += 1
                bin_stats.append({
                    "bin": label,
                    "score_lo": lo,
                    "score_hi": hi,
                    "total": total,
                    "joined_to_zcat": joined,
                    "science_target_count": total - sky_or_bad,
                    "sky_or_nonscience_count": sky_or_bad,
                    "sky_or_nonscience_fraction": (sky_or_bad / total) if total else None,
                })
        finally:
            connection.close()

    report = {
        "contract_sha256": contract_sha,
        "generation_id": summary.get("generation_id"),
        "zcatalog_path": str(zcatalog_path),
        "rule": "sky_or_nonscience = NOT (OBJTYPE=='TGT' AND COADD_FIBERSTATUS==0); TARGETID<=0 counted as sky_or_nonscience",
        "raw_rows_all_shards": raw_rows,
        "unique_targetids_all_shards": unique_rows,
        "max_score_observed": float(max_score),
        "bins": bin_stats,
    }

    output_json.parent.mkdir(parents=True, exist_ok=True)
    with output_json.open("w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2, sort_keys=True)
        fh.write("\n")

    _plot(report, output_png)
    return report


def _plot(report: dict[str, Any], output_png: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    bins = report["bins"]
    labels = [b["bin"] for b in bins]
    fracs = [b["sky_or_nonscience_fraction"] or 0.0 for b in bins]
    totals = [b["total"] for b in bins]

    fig, ax1 = plt.subplots(figsize=(9, 5))
    x = range(len(labels))
    ax1.bar(x, fracs, color="#c0392b", alpha=0.75, label="sky/non-science fraction")
    ax1.set_ylim(0, 1.0)
    ax1.set_ylabel("sky/non-science fraction")
    ax1.set_xticks(list(x))
    ax1.set_xticklabels(labels, rotation=30, ha="right")
    ax1.set_xlabel("anomaly_score bin")
    ax1.set_title("AUG-011 sealed scan: sky/non-science fraction by anomaly_score bin")
    for xi, (f, t) in enumerate(zip(fracs, totals)):
        ax1.annotate(f"n={t}", (xi, f), textcoords="offset points", xytext=(0, 6), ha="center", fontsize=8)
    fig.tight_layout()
    output_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_png, dpi=150)
    plt.close(fig)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--shard-dir", type=Path, required=True)
    parser.add_argument("--receipt-dir", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--zcatalog", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-png", type=Path, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    report = run(
        contract_path=args.contract,
        shard_dir=args.shard_dir,
        receipt_dir=args.receipt_dir,
        summary_path=args.summary,
        zcatalog_path=args.zcatalog,
        output_json=args.output_json,
        output_png=args.output_png,
    )
    print(json.dumps({"bins": [(b["bin"], b["sky_or_nonscience_fraction"]) for b in report["bins"]]}, indent=2))


if __name__ == "__main__":
    main()

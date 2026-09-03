#!/usr/bin/env python3
"""Phase-3 flagship candidate sample builder for the AUG-011 clean rerun.

Consumes the sealed run contract, the receipt-verified shard set it bound,
and the `summarize-after-dedup` summary it produced, and emits a SELECTED
candidate sample — a deterministic, post-dedup slice of scored targets above
a configured `anomaly_score` floor, plus a sealed sample manifest recording
exactly how it was built.

Fail-closed, in order, every run:

  1. `clean_rerun_contract.py`'s `verify_receipts()` is invoked (imported,
     unmodified) against `--contract`/`--shard-dir`/`--receipt-dir` — every
     shard is re-hashed and its receipt re-checked before anything else
     happens.
  2. `--summary`'s `contract_sha256` must equal the exact contract's own
     `payload_sha256` (the same canonical hash `clean_rerun_contract.py`
     computes internally) — a summary produced against a different contract
     is refused, never silently accepted.
  3. Only after both checks pass does this script re-stream the verified
     shards through its own last-row-wins-per-targetid dedup pass (the same
     rule `clean_rerun_contract.py summarize-after-dedup` uses:
     `identity_column=targetid`, winner = last row in deterministic lexical
     shard-then-row order) to materialize the actual post-dedup
     `(targetid, anomaly_score, mean_mse, survey, program, healpix)` rows —
     `summary.json` alone only carries aggregate counts, never per-row data.

Two modes, mutually exclusive:

  --describe   Prints the post-dedup score distribution (quantiles, plus
               counts/fractions above the candidate thresholds 3/4/5/6/8/10
               sigma) to stdout. Emits NOTHING to disk. This is how the
               `--score-threshold` decision for a real selection run gets
               made FROM the data, never guessed or copied from the
               historical 2,145-row rule (`ANOMALY_FLAGSHIP_MANUSCRIPT_
               ARCHITECTURE_2026-08-05.md` Sec.2b: "must be derived from the
               new run's score distribution, never copied from the
               historical rule or tuned to reproduce 2,145 rows").

  (default)    Requires `--score-threshold`. Selects every post-dedup row
               with `anomaly_score >= --score-threshold`, applies any
               configured optional quality filters, writes the selected rows
               to `--output-sample` (Parquet) and a sealed JSON manifest to
               `--output-manifest` recording the exact rule, thresholds, row
               count, parent generation id, shard-receipt binding, and the
               output file's own SHA-256.

Historical-tooling gap (see module docstring of `taxonomy_flagship.py` for
the larger version of this note): the historical silver-tier rule
(`silver_crossmatch.py`) filtered on `anomaly_score > 3.0` AND
`max_snr > 0.5`, where `max_snr` came from `median_coadd_snr_{b,r,z}`
columns present in the historical `enhanced_18M_deduped` Parquet schema. The
AUG-011 `run_scan.py` shard schema is deliberately narrower — `targetid`,
`anomaly_score`, `mean_mse`, `healpix`, `survey`, `program` only, per
`RUNBOOK.md` step 10 and `run_scan.py`'s own docstring — so an SNR filter
cannot be ported as-is; there is no SNR column to filter on. The "optional
quality filters" this script supports (`--exclude-survey`,
`--exclude-program`) are therefore built from what the actual shard schema
carries, not a re-implementation of the historical SNR cut. If a future scan
generation adds per-shard SNR (or any other quality column), extending the
selection rule here is a small, additive change — never retrofit the
historical SNR threshold onto scores it was never computed against.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sqlite3
import tempfile
import types
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
CONTRACT_MODULE_PATH = REPO_ROOT / "pipelines/p1_highz_tracers/clean_rerun_contract.py"

CANDIDATE_THRESHOLDS = (3.0, 4.0, 5.0, 6.0, 8.0, 10.0)
QUANTILES = (0.0, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99, 1.0)
SHARD_COLUMNS = ["targetid", "anomaly_score", "mean_mse", "survey", "program", "healpix"]


class SampleError(RuntimeError):
    """Raised when the sample cannot be built or trusted."""


def load_contract_module(path: Path = CONTRACT_MODULE_PATH) -> types.ModuleType:
    """Import `clean_rerun_contract.py` unmodified, by exact file path."""
    spec = importlib.util.spec_from_file_location("clean_rerun_contract_bound", path)
    if spec is None or spec.loader is None:
        raise SampleError(f"cannot load contract module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False
    ) as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def verify_summary_matches_contract(
    contract_module: types.ModuleType, contract: dict[str, Any], summary: dict[str, Any]
) -> str:
    """Fail closed unless `summary.json` was produced against THIS exact contract."""
    expected = contract_module.payload_sha256(contract)
    observed = summary.get("contract_sha256")
    if observed != expected:
        raise SampleError(
            f"summary.json contract_sha256 mismatch: expected {expected}, got {observed!r} "
            "(summary was produced against a different contract; refusing to build a sample)"
        )
    return expected


def _dedup_scores_into_sqlite(shards: list[Path], connection: sqlite3.Connection) -> int:
    """Stream verified shards into a fresh SQLite table, last-row-wins per targetid.

    Mirrors `clean_rerun_contract.summarize_after_dedup`'s dedup rule exactly:
    shards are iterated in the sorted (lexical) order `verify_receipts`
    already returns them in, and within a shard, later Parquet row-batches
    overwrite earlier ones for the same targetid (`ON CONFLICT DO UPDATE`).
    """
    import pyarrow.parquet as pq

    connection.execute(
        "CREATE TABLE scored ("
        "targetid INTEGER PRIMARY KEY, anomaly_score REAL NOT NULL, mean_mse REAL, "
        "survey TEXT, program TEXT, healpix INTEGER)"
    )
    raw_rows = 0
    for shard in shards:
        parquet = pq.ParquetFile(shard)
        available = set(parquet.schema_arrow.names)
        columns = [c for c in SHARD_COLUMNS if c in available]
        if "targetid" not in columns or "anomaly_score" not in columns:
            raise SampleError(f"shard lacks required columns targetid/anomaly_score: {shard}")
        for batch in parquet.iter_batches(columns=columns):
            frame = {name: batch.column(i).to_pylist() for i, name in enumerate(columns)}
            n = len(frame["targetid"])
            rows = []
            for i in range(n):
                rows.append(
                    (
                        frame["targetid"][i],
                        frame["anomaly_score"][i],
                        frame.get("mean_mse", [None] * n)[i],
                        frame.get("survey", [None] * n)[i],
                        frame.get("program", [None] * n)[i],
                        frame.get("healpix", [None] * n)[i],
                    )
                )
            raw_rows += len(rows)
            connection.executemany(
                "INSERT INTO scored(targetid, anomaly_score, mean_mse, survey, program, healpix) "
                "VALUES (?, ?, ?, ?, ?, ?) "
                "ON CONFLICT(targetid) DO UPDATE SET "
                "anomaly_score=excluded.anomaly_score, mean_mse=excluded.mean_mse, "
                "survey=excluded.survey, program=excluded.program, healpix=excluded.healpix",
                rows,
            )
    return raw_rows


def _quantiles_and_counts(scores: np.ndarray) -> tuple[dict[str, float], dict[str, dict[str, Any]]]:
    """Shared quantile + candidate-threshold-count computation over a 1-D score array."""
    n = int(scores.shape[0])
    quantiles = {f"q{int(q * 100):02d}": float(np.quantile(scores, q)) for q in QUANTILES}
    counts_above = {}
    for threshold in CANDIDATE_THRESHOLDS:
        count = int(np.sum(scores >= threshold))
        counts_above[f"sigma_{threshold:g}"] = {
            "threshold": threshold,
            "count": count,
            "fraction_of_unique": (count / n) if n else 0.0,
        }
    return quantiles, counts_above


def describe_distribution(
    contract_module: types.ModuleType,
    contract_path: Path,
    shard_dir: Path,
    receipt_dir: Path,
    summary_path: Path,
    science_targets_only: bool = False,
    zcatalog_path: Path | None = None,
) -> dict[str, Any]:
    """Fail-closed post-dedup score-distribution report. Writes nothing to disk.

    Default behaviour (`science_targets_only=False`) is byte-identical to the
    original raw-table-only report. When `science_targets_only=True` (and
    `zcatalog_path` given), the RAW table is still computed exactly as
    before (top-level `quantiles`/`counts_above_threshold` keys are
    unchanged) and an ADDITIONAL `science_only` block is appended, joining
    the same post-dedup scored rows to the zcatalog via
    `load_science_target_flags`/the `OBJTYPE=='TGT' AND
    COADD_FIBERSTATUS==0` rule (see `apply_science_target_filter`) before
    computing its own quantiles/counts. This is what makes the science-only
    threshold-choice grid in `pod_phase3_v2.sh` stage 03 possible from
    `--describe` alone — describe mode previously emitted only the raw
    (sky-fiber-contaminated) table even when `--science-targets-only` was
    passed, which is what caused the v2 chain's stage-3 failure.
    """
    if science_targets_only and zcatalog_path is None:
        raise SampleError("--science-targets-only requires --zcatalog")

    contract = contract_module.read_json(contract_path)
    contract_module.verify_contract(contract)
    shards = contract_module.verify_receipts(contract_path, shard_dir, receipt_dir)
    summary = contract_module.read_json(summary_path)
    contract_sha = verify_summary_matches_contract(contract_module, contract, summary)

    with tempfile.TemporaryDirectory() as tmp:
        sqlite_path = Path(tmp) / "describe.sqlite"
        connection = sqlite3.connect(sqlite_path)
        try:
            raw_rows = _dedup_scores_into_sqlite(shards, connection)
            unique_rows = connection.execute("SELECT COUNT(*) FROM scored").fetchone()[0]
            if unique_rows == 0:
                raise SampleError("zero deduplicated rows found across all verified shards")

            # Memory-bounded percentile computation: pull the score column in
            # fixed-size cursor batches into one preallocated float64 array
            # rather than materializing Python list objects for every row.
            scores = np.empty(unique_rows, dtype=np.float64)
            targetids: list[int] | None = [] if science_targets_only else None
            cursor = connection.execute(
                "SELECT targetid, anomaly_score FROM scored" if science_targets_only else "SELECT anomaly_score FROM scored"
            )
            offset = 0
            while True:
                batch = cursor.fetchmany(200_000)
                if not batch:
                    break
                take = len(batch)
                if science_targets_only:
                    scores[offset : offset + take] = [row[1] for row in batch]
                    targetids.extend(int(row[0]) for row in batch)
                else:
                    scores[offset : offset + take] = [row[0] for row in batch]
                offset += take

            quantiles, counts_above = _quantiles_and_counts(scores)

            science_only_block = None
            if science_targets_only:
                assert targetids is not None
                flags = load_science_target_flags(zcatalog_path, set(targetids))
                science_scores = [
                    scores[i]
                    for i, tid in enumerate(targetids)
                    if (info := flags.get(tid)) is not None
                    and info["objtype"] == "TGT"
                    and info["fiberstatus"] == 0
                ]
                sci_unique = len(science_scores)
                if sci_unique == 0:
                    science_only_block = {
                        "unique_targetids": 0,
                        "quantiles": {},
                        "counts_above_threshold": {},
                        "note": "zero rows survive the science-target join (OBJTYPE=='TGT' AND COADD_FIBERSTATUS==0)",
                    }
                else:
                    sci_quantiles, sci_counts = _quantiles_and_counts(np.array(science_scores, dtype=np.float64))
                    science_only_block = {
                        "unique_targetids": sci_unique,
                        "quantiles": sci_quantiles,
                        "counts_above_threshold": sci_counts,
                    }
        finally:
            connection.close()

    report = {
        "contract_sha256": contract_sha,
        "generation_id": summary.get("generation_id"),
        "raw_rows": raw_rows,
        "unique_targetids": unique_rows,
        "quantiles": quantiles,
        "counts_above_threshold": counts_above,
        "note": "describe mode emits no sample; use --score-threshold to select one",
    }
    if science_targets_only:
        report["science_targets_only"] = True
        report["science_target_rule"] = "OBJTYPE == 'TGT' AND COADD_FIBERSTATUS == 0 (TARGETID > 0 asserted)"
        report["zcatalog_path"] = str(zcatalog_path)
        report["science_only"] = science_only_block
    return report


ZCAT_SCIENCE_COLUMNS = ["TARGETID", "OBJTYPE", "COADD_FIBERSTATUS", "ZWARN", "SPECTYPE", "Z", "DELTACHI2"]


def find_zcat_science_hdu(hdul: Any) -> Any:
    """Find the zcatalog HDU exposing TARGETID/OBJTYPE/COADD_FIBERSTATUS.

    Mirrors `crossmatch_flagship.find_zcat_coordinate_hdu`'s pattern.
    """
    required = {"TARGETID", "OBJTYPE", "COADD_FIBERSTATUS"}
    for hdu in hdul:
        columns = getattr(hdu, "columns", None)
        if columns is not None and required <= set(columns.names):
            return hdu
    raise SampleError("no HDU in the zcatalog exposes TARGETID/OBJTYPE/COADD_FIBERSTATUS columns")


def load_science_target_flags(
    zcatalog_path: Path, targetids: set[int], chunk_rows: int = 500_000
) -> dict[int, dict[str, Any]]:
    """Stream OBJTYPE/COADD_FIBERSTATUS/ZWARN/SPECTYPE/Z/DELTACHI2 for `targetids`.

    Returns a mapping from targetid -> {objtype, fiberstatus, zwarn,
    spectype, z, deltachi2}, containing ONLY the requested targetids and
    ONLY rows where TARGETID > 0 (a negative TARGETID in the DESI zcatalog
    denotes a sky/blank fiber row and is never a real target, per
    `project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md`). Peak
    memory is bounded by one chunk plus the requested targetid set.
    """
    try:
        from astropy.io import fits
    except ImportError as exc:  # pragma: no cover - runtime prerequisite
        raise SampleError("astropy is required to read the zcatalog FITS file") from exc

    remaining = set(targetids)
    found: dict[int, dict[str, Any]] = {}
    with fits.open(zcatalog_path, memmap=True) as hdul:
        table_hdu = find_zcat_science_hdu(hdul)
        data = table_hdu.data
        available = set(data.columns.names)
        n_rows = len(data)
        for start in range(0, n_rows, chunk_rows):
            if not remaining:
                break
            stop = min(start + chunk_rows, n_rows)
            targetid_chunk = data["TARGETID"][start:stop]
            objtype_chunk = data["OBJTYPE"][start:stop]
            fiberstatus_chunk = data["COADD_FIBERSTATUS"][start:stop]
            zwarn_chunk = data["ZWARN"][start:stop] if "ZWARN" in available else None
            spectype_chunk = data["SPECTYPE"][start:stop] if "SPECTYPE" in available else None
            z_chunk = data["Z"][start:stop] if "Z" in available else None
            deltachi2_chunk = data["DELTACHI2"][start:stop] if "DELTACHI2" in available else None
            for i, targetid_raw in enumerate(targetid_chunk):
                targetid = int(targetid_raw)
                if targetid not in remaining:
                    continue
                if targetid <= 0:
                    # Sanity check per the contamination finding: a real
                    # science target never has TARGETID <= 0. Do not add it
                    # to `found`; the caller's science-only join then simply
                    # excludes it (as any non-TGT row would be excluded).
                    remaining.discard(targetid)
                    continue
                objtype_raw = objtype_chunk[i]
                objtype = objtype_raw.decode("utf-8").strip() if isinstance(objtype_raw, bytes) else str(objtype_raw).strip()
                found[targetid] = {
                    "objtype": objtype,
                    "fiberstatus": int(fiberstatus_chunk[i]),
                    "zwarn": int(zwarn_chunk[i]) if zwarn_chunk is not None else None,
                    "spectype": (
                        (spectype_chunk[i].decode("utf-8").strip() if isinstance(spectype_chunk[i], bytes) else str(spectype_chunk[i]).strip())
                        if spectype_chunk is not None
                        else None
                    ),
                    "z": float(z_chunk[i]) if z_chunk is not None else None,
                    "deltachi2": float(deltachi2_chunk[i]) if deltachi2_chunk is not None else None,
                }
                remaining.discard(targetid)
    return found


def apply_science_target_filter(
    selected: dict[str, list[Any]], zcatalog_path: Path
) -> dict[str, list[Any]]:
    """Keep only rows joining to a zcatalog TGT row with COADD_FIBERSTATUS==0.

    Rule (per `project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md`):
    `OBJTYPE == 'TGT' AND COADD_FIBERSTATUS == 0`, with `TARGETID > 0`
    asserted as a sanity check (rows with TARGETID <= 0 are never emitted
    by `load_science_target_flags` in the first place, so any row that
    survives the join already satisfies this). Adds `zwarn`, `spectype`,
    `z`, `deltachi2` columns carried from the zcatalog.
    """
    targetids = {int(t) for t in selected["targetid"]}
    flags = load_science_target_flags(zcatalog_path, targetids)

    kept: dict[str, list[Any]] = {name: [] for name in SHARD_COLUMNS}
    kept["zwarn"] = []
    kept["spectype"] = []
    kept["z"] = []
    kept["deltachi2"] = []

    n = len(selected["targetid"])
    for i in range(n):
        targetid = int(selected["targetid"][i])
        info = flags.get(targetid)
        if info is None:
            continue
        assert targetid > 0, f"science-target join must never carry TARGETID <= 0, got {targetid}"
        if info["objtype"] != "TGT" or info["fiberstatus"] != 0:
            continue
        for name in SHARD_COLUMNS:
            kept[name].append(selected[name][i])
        kept["zwarn"].append(info["zwarn"])
        kept["spectype"].append(info["spectype"])
        kept["z"].append(info["z"])
        kept["deltachi2"].append(info["deltachi2"])
    return kept


def _shard_receipt_binding(receipt_dir: Path, shards: list[Path]) -> dict[str, Any]:
    entries = []
    for shard in shards:
        receipt_path = receipt_dir / f"{shard.name}.receipt.json"
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        entries.append(
            {
                "shard": shard.name,
                "receipt_sha256": hashlib.sha256(
                    json.dumps(receipt, sort_keys=True, separators=(",", ":")).encode("utf-8")
                ).hexdigest(),
            }
        )
    return {"receipt_dir": str(receipt_dir), "shard_count": len(entries), "shards": entries}


def build_sample(
    contract_module: types.ModuleType,
    contract_path: Path,
    shard_dir: Path,
    receipt_dir: Path,
    summary_path: Path,
    score_threshold: float,
    output_sample: Path,
    output_manifest: Path,
    exclude_survey: list[str] | None = None,
    exclude_program: list[str] | None = None,
    science_targets_only: bool = False,
    zcatalog_path: Path | None = None,
) -> dict[str, Any]:
    import pyarrow as pa
    import pyarrow.parquet as pq

    if science_targets_only and zcatalog_path is None:
        raise SampleError("--science-targets-only requires --zcatalog")

    exclude_survey = set(exclude_survey or [])
    exclude_program = set(exclude_program or [])

    contract = contract_module.read_json(contract_path)
    contract_module.verify_contract(contract)
    shards = contract_module.verify_receipts(contract_path, shard_dir, receipt_dir)
    summary = contract_module.read_json(summary_path)
    contract_sha = verify_summary_matches_contract(contract_module, contract, summary)

    with tempfile.TemporaryDirectory() as tmp:
        sqlite_path = Path(tmp) / "select.sqlite"
        connection = sqlite3.connect(sqlite_path)
        try:
            raw_rows = _dedup_scores_into_sqlite(shards, connection)
            unique_rows = connection.execute("SELECT COUNT(*) FROM scored").fetchone()[0]
            if unique_rows == 0:
                raise SampleError("zero deduplicated rows found across all verified shards")

            query = "SELECT targetid, anomaly_score, mean_mse, survey, program, healpix FROM scored WHERE anomaly_score >= ? ORDER BY targetid ASC"
            selected: dict[str, list[Any]] = {name: [] for name in SHARD_COLUMNS}
            cursor = connection.execute(query, (score_threshold,))
            while True:
                batch = cursor.fetchmany(200_000)
                if not batch:
                    break
                for targetid, anomaly_score, mean_mse, survey, program, healpix in batch:
                    if survey in exclude_survey or program in exclude_program:
                        continue
                    selected["targetid"].append(targetid)
                    selected["anomaly_score"].append(anomaly_score)
                    selected["mean_mse"].append(mean_mse)
                    selected["survey"].append(survey)
                    selected["program"].append(program)
                    selected["healpix"].append(healpix)
        finally:
            connection.close()

    science_filtered_from = None
    if science_targets_only:
        science_filtered_from = len(selected["targetid"])
        selected = apply_science_target_filter(selected, zcatalog_path)

    row_count = len(selected["targetid"])
    if row_count == 0:
        raise SampleError(
            f"selection rule (score >= {score_threshold}, exclude_survey={sorted(exclude_survey)}, "
            f"exclude_program={sorted(exclude_program)}, science_targets_only={science_targets_only}) "
            f"selected zero rows out of {unique_rows} unique targetids"
        )

    if selected["targetid"]:
        assert min(int(t) for t in selected["targetid"]) > 0 or not science_targets_only, (
            "science-target sample must never contain TARGETID <= 0"
        )

    columns = {
        "targetid": pa.array(selected["targetid"], type=pa.int64()),
        "anomaly_score": pa.array(selected["anomaly_score"], type=pa.float64()),
        "mean_mse": pa.array(selected["mean_mse"], type=pa.float64()),
        "survey": pa.array(selected["survey"], type=pa.string()),
        "program": pa.array(selected["program"], type=pa.string()),
        "healpix": pa.array(selected["healpix"], type=pa.int64()),
    }
    if science_targets_only:
        columns["zwarn"] = pa.array(selected["zwarn"], type=pa.int64())
        columns["spectype"] = pa.array(selected["spectype"], type=pa.string())
        columns["z"] = pa.array(selected["z"], type=pa.float64())
        columns["deltachi2"] = pa.array(selected["deltachi2"], type=pa.float64())
    table = pa.table(columns)
    output_sample.parent.mkdir(parents=True, exist_ok=True)
    tmp_output = output_sample.with_suffix(output_sample.suffix + ".tmp")
    pq.write_table(table, tmp_output, compression="zstd")
    os.replace(tmp_output, output_sample)
    output_sha256 = sha256_file(output_sample)

    manifest = {
        "manifest_version": "flagship-sample/v1",
        "created_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "rule": {
            "type": "score_threshold",
            "operator": ">=",
            "score_threshold": score_threshold,
            "exclude_survey": sorted(exclude_survey),
            "exclude_program": sorted(exclude_program),
            "science_targets_only": science_targets_only,
            "science_target_rule": (
                "OBJTYPE == 'TGT' AND COADD_FIBERSTATUS == 0 (TARGETID > 0 asserted)"
                if science_targets_only
                else None
            ),
            "zcatalog_path": str(zcatalog_path) if science_targets_only else None,
            "rows_before_science_target_filter": science_filtered_from,
        },
        "row_count": row_count,
        "unique_targetids_considered": unique_rows,
        "raw_rows_considered": raw_rows,
        "parent": {
            "generation_id": summary.get("generation_id"),
            "contract_sha256": contract_sha,
            "catalog_sha256": contract["input_manifest"]["catalog_sha256"],
            "input_manifest_sha256": contract["input_manifest_sha256"],
            "summary_sha256": hashlib.sha256(
                json.dumps(summary, sort_keys=True, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
        },
        "shard_receipt_binding": _shard_receipt_binding(receipt_dir, shards),
        "output": {
            "file_name": output_sample.name,
            "byte_size": output_sample.stat().st_size,
            "sha256": output_sha256,
        },
    }
    write_json_atomic(output_manifest, manifest)
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--shard-dir", type=Path, required=True)
    parser.add_argument("--receipt-dir", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True, help="summarize-after-dedup output (summary.json)")
    parser.add_argument("--describe", action="store_true", help="print the score distribution and exit; emits no sample")
    parser.add_argument("--score-threshold", type=float, default=None, help="anomaly_score floor (required unless --describe)")
    parser.add_argument("--exclude-survey", action="append", default=[], help="repeatable; drop rows with this survey value")
    parser.add_argument("--exclude-program", action="append", default=[], help="repeatable; drop rows with this program value")
    parser.add_argument("--output-sample", type=Path, default=None, help="required unless --describe")
    parser.add_argument("--output-manifest", type=Path, default=None, help="required unless --describe")
    parser.add_argument(
        "--science-targets-only",
        action="store_true",
        help=(
            "default off (sealed behaviour unchanged). Join the scan corpus to --zcatalog by "
            "TARGETID and keep only OBJTYPE=='TGT' AND COADD_FIBERSTATUS==0 rows (TARGETID>0 "
            "asserted); carries ZWARN/SPECTYPE/Z/DELTACHI2 per row. See "
            "project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md."
        ),
    )
    parser.add_argument("--zcatalog", type=Path, default=None, help="zall-pix-iron.fits; required with --science-targets-only")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    contract_module = load_contract_module()
    if args.describe:
        if args.science_targets_only and args.zcatalog is None:
            raise SystemExit("--science-targets-only requires --zcatalog")
        report = describe_distribution(
            contract_module, args.contract, args.shard_dir, args.receipt_dir, args.summary,
            science_targets_only=args.science_targets_only, zcatalog_path=args.zcatalog,
        )
        print(json.dumps(report, indent=2, sort_keys=True))
        return
    if args.score_threshold is None:
        raise SystemExit("--score-threshold is required unless --describe")
    if args.output_sample is None or args.output_manifest is None:
        raise SystemExit("--output-sample and --output-manifest are required unless --describe")
    if args.science_targets_only and args.zcatalog is None:
        raise SystemExit("--science-targets-only requires --zcatalog")
    manifest = build_sample(
        contract_module,
        args.contract,
        args.shard_dir,
        args.receipt_dir,
        args.summary,
        args.score_threshold,
        args.output_sample,
        args.output_manifest,
        exclude_survey=args.exclude_survey,
        exclude_program=args.exclude_program,
        science_targets_only=args.science_targets_only,
        zcatalog_path=args.zcatalog,
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

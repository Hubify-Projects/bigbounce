#!/usr/bin/env python3
"""Build the v1.0.244 catalog payload bound to the P4 v1.0.253 paper closure.

The science-facing Parquet deliberately excludes every raw-pass and reconstructed
flip-pass score column.  A separate provenance-only quarantine contains every
catalog-wide reconstructed-score violator, including the flagged subset in the
declared high-confidence sample.  None of these scores is calibrated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).resolve().parent))
from reproduce_p4_primary_null_v1_0_244 import reproduce


ROOT = Path(__file__).resolve().parents[2]
CATALOG_PAYLOAD_VERSION = "v1.0.244"
PAPER_VERSION = "v1.0.253"
SCHEMA_PATH = Path(__file__).with_name("apjs_release_schema_v1_0_244.json")
DATA_DICTIONARY_PATH = Path(__file__).with_name("CATALOG_SCHEMA.md")
REPRODUCTION_SCRIPT_PATH = Path(__file__).with_name(
    "reproduce_p4_primary_null_v1_0_244.py"
)
CLAIM_AUDIT_SCRIPT_PATH = Path(__file__).with_name(
    "validate_p4_v1_0_244_claims.py"
)
NULL_GENERATOR_SCRIPT_PATH = Path(__file__).with_name(
    "generate_p4_primary_label_shuffle_v1_0_244.py"
)
SOURCE_PATH = ROOT / "pipelines/p5_desi_chirality/data/p4_chirality.parquet"
DEFAULT_OUT = Path(__file__).with_name("apjs_release_v1.0.244")
NULL_PATH = Path(__file__).parent / "outputs/canonical_provenance/p4_primary_hc_label_shuffle_10k.npy"
PIXEL_NULL_PATH = Path(__file__).parent / "outputs/canonical_provenance/c12_queue2_null_amps_10k.npy"
SOURCE_RECEIPT_PATH = (
    Path(__file__).parent
    / "outputs/canonical_provenance/fig7_raw_vs_eq_manifest.json"
)
SOURCE_SHA256 = "e8525ba5c98576f6361580e4a0aa7a86929ccc9f79b1423808774cfaaf313563"
SOURCE_BYTES = 952_115_239
EXPECTED = {
    "catalog_rows": 8_474_531,
    "primary_hc_rows": 949_584,
    "unsafe_catalog_rows": 249_066,
    "unsafe_primary_hc_rows": 59_515,
    "strict_primary_hc_rows": 890_069,
}
RAW_COLUMNS = (
    "p_cw_raw_x", "p_ccw_raw_x", "p_ns_raw_x",
    "p_cw_raw_y", "p_ccw_raw_y", "p_ns_raw_y",
)
INPUT_COLUMNS = (
    "dr8_id", "ra", "dec", "class_eq",
    "p_cw_eq", "p_ccw_eq", "p_ns_eq", *RAW_COLUMNS,
)
PRIMARY_COLUMNS = (
    "object_id", "ra_deg", "dec_deg", "class_eq",
    "score_cw_eq", "score_ccw_eq", "score_ns_eq", "score_eq_max",
    "is_spiral", "primary_hc", "raw_flip_qc_unsafe",
)
QUARANTINE_COLUMNS = (
    "object_id", "ra_deg", "dec_deg", "is_primary_hc", "raw_source_leg",
    "unsafe_raw_score_cw", "unsafe_raw_score_ccw", "unsafe_raw_score_ns",
    "unsafe_reconstructed_flip_score_cw",
    "unsafe_reconstructed_flip_score_ccw",
    "unsafe_reconstructed_flip_score_ns",
    "unsafe_max_bound_excursion", "unsafe_reason_code", "do_not_use_for_science",
)
REASON = "RAW_EQ_PIPELINE_PASS_MISMATCH_GT_1E3"
ALLOWED_CLASSES = ("CW", "CCW", "NOT_SPIRAL")
SCORE_COLUMNS = ("score_cw_eq", "score_ccw_eq", "score_ns_eq")
# The three outputs are uncalibrated ranking scores.  They are nevertheless the
# output of one softmax and therefore have the structural (not probabilistic-
# calibration) contract that they are finite, bounded, and sum to one.  The
# released float64 values originated in float32 inference, hence this tolerance.
SCORE_SIMPLEX_ATOL = 2.0e-6
SCORE_EQUALITY_ATOL = 1.0e-12


class ReleaseError(RuntimeError):
    """Raised when the release contract cannot be proved."""


def sha256_file(path: Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def repo_relative(path: Path) -> str:
    """Return a portable repository-relative path for release receipts."""
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(ROOT.resolve()))
    except ValueError:
        # Tests and external verification may supply a temporary fixture. Keep
        # the receipt portable without leaking a machine-absolute path.
        return resolved.name


def _numpy(batch: pa.RecordBatch, name: str) -> np.ndarray:
    return batch.column(batch.schema.get_field_index(name)).to_numpy(zero_copy_only=False)


def _strings(batch: pa.RecordBatch, name: str) -> np.ndarray:
    return np.asarray(
        batch.column(batch.schema.get_field_index(name)).to_pylist(), dtype=object
    )


def _excursion(values: np.ndarray) -> np.ndarray:
    return np.maximum(np.maximum(-values, values - 1.0), 0.0)


def split_batch(batch: pa.RecordBatch) -> tuple[pa.Table, pa.Table, dict[str, Any]]:
    """Split one source batch into the safe primary and unsafe quarantine tiers."""
    object_id = _strings(batch, "dr8_id")
    class_eq = _strings(batch, "class_eq")
    ra = _numpy(batch, "ra").astype(np.float64, copy=False)
    dec = _numpy(batch, "dec").astype(np.float64, copy=False)
    cw_eq = _numpy(batch, "p_cw_eq").astype(np.float64, copy=False)
    ccw_eq = _numpy(batch, "p_ccw_eq").astype(np.float64, copy=False)
    ns_eq = _numpy(batch, "p_ns_eq").astype(np.float64, copy=False)

    raw = {
        name: _numpy(batch, name).astype(np.float32).astype(np.float64)
        for name in RAW_COLUMNS
    }
    use_y = np.isfinite(raw["p_cw_raw_y"]) & np.isfinite(raw["p_ccw_raw_y"]) & np.isfinite(raw["p_ns_raw_y"])
    cw_raw = np.where(use_y, raw["p_cw_raw_y"], raw["p_cw_raw_x"])
    ccw_raw = np.where(use_y, raw["p_ccw_raw_y"], raw["p_ccw_raw_x"])
    ns_raw = np.where(use_y, raw["p_ns_raw_y"], raw["p_ns_raw_x"])
    raw_present = np.isfinite(cw_raw) & np.isfinite(ccw_raw) & np.isfinite(ns_raw)
    eq_present = np.isfinite(cw_eq) & np.isfinite(ccw_eq) & np.isfinite(ns_eq)
    if not np.all(raw_present & eq_present):
        raise ReleaseError("release source contains rows without complete raw/equivariant score triplets")

    flip_ccw = 2.0 * cw_eq - cw_raw
    flip_cw = 2.0 * ccw_eq - ccw_raw
    flip_ns = 2.0 * ns_eq - ns_raw
    max_excursion = np.maximum.reduce(
        (_excursion(flip_cw), _excursion(flip_ccw), _excursion(flip_ns))
    )
    unsafe = max_excursion > 1.0e-3
    is_spiral = np.isin(class_eq, ("CW", "CCW"))
    primary_hc = (
        is_spiral
        & (np.maximum(cw_eq, ccw_eq) > 0.6)
        & np.isfinite(ra)
        & np.isfinite(dec)
    )
    score_eq_max = np.maximum.reduce((cw_eq, ccw_eq, ns_eq))

    primary = pa.table(
        {
            "object_id": pa.array(object_id, type=pa.string()),
            "ra_deg": pa.array(ra, type=pa.float64()),
            "dec_deg": pa.array(dec, type=pa.float64()),
            "class_eq": pa.array(class_eq, type=pa.string()),
            "score_cw_eq": pa.array(cw_eq, type=pa.float64()),
            "score_ccw_eq": pa.array(ccw_eq, type=pa.float64()),
            "score_ns_eq": pa.array(ns_eq, type=pa.float64()),
            "score_eq_max": pa.array(score_eq_max, type=pa.float64()),
            "is_spiral": pa.array(is_spiral, type=pa.bool_()),
            "primary_hc": pa.array(primary_hc, type=pa.bool_()),
            "raw_flip_qc_unsafe": pa.array(unsafe, type=pa.bool_()),
        }
    )

    q = unsafe
    n_unsafe = int(q.sum())
    quarantine = pa.table(
        {
            "object_id": pa.array(object_id[q], type=pa.string()),
            "ra_deg": pa.array(ra[q], type=pa.float64()),
            "dec_deg": pa.array(dec[q], type=pa.float64()),
            "is_primary_hc": pa.array(primary_hc[q], type=pa.bool_()),
            "raw_source_leg": pa.array(
                np.where(use_y[q], "raw_y", "raw_x_fallback"), type=pa.string()
            ),
            "unsafe_raw_score_cw": pa.array(cw_raw[q], type=pa.float64()),
            "unsafe_raw_score_ccw": pa.array(ccw_raw[q], type=pa.float64()),
            "unsafe_raw_score_ns": pa.array(ns_raw[q], type=pa.float64()),
            "unsafe_reconstructed_flip_score_cw": pa.array(flip_cw[q], type=pa.float64()),
            "unsafe_reconstructed_flip_score_ccw": pa.array(flip_ccw[q], type=pa.float64()),
            "unsafe_reconstructed_flip_score_ns": pa.array(flip_ns[q], type=pa.float64()),
            "unsafe_max_bound_excursion": pa.array(max_excursion[q], type=pa.float64()),
            "unsafe_reason_code": pa.array([REASON] * n_unsafe, type=pa.string()),
            "do_not_use_for_science": pa.array(np.ones(n_unsafe, dtype=bool), type=pa.bool_()),
        }
    )
    stats = {
        "catalog_rows": batch.num_rows,
        "primary_hc_rows": int(primary_hc.sum()),
        "unsafe_catalog_rows": n_unsafe,
        "unsafe_primary_hc_rows": int((unsafe & primary_hc).sum()),
        "strict_primary_hc_rows": int((primary_hc & ~unsafe).sum()),
        "max_bound_excursion": float(max_excursion.max(initial=0.0)),
    }
    return primary, quarantine, stats


def _add_stats(total: dict[str, Any], batch: dict[str, Any]) -> None:
    for key in EXPECTED:
        total[key] += int(batch[key])
    total["max_bound_excursion"] = max(
        float(total["max_bound_excursion"]), float(batch["max_bound_excursion"])
    )


def validate_source_identity(source: Path, receipt_path: Path) -> dict[str, Any]:
    """Validate the local file against an exact, content-addressed receipt.

    The receipt is a committed provenance artifact from an earlier full SHA-256
    pass over the immutable upstream revision. A new full SHA-256 pass over the
    local file is required before its byte and Parquet-row contracts are checked.
    This identity pass is deliberately separate from the later catalog transform.
    """
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    catalog = receipt.get("catalog", {})
    expected = {
        "sha256": SOURCE_SHA256,
        "bytes": SOURCE_BYTES,
        "rows": EXPECTED["catalog_rows"],
    }
    observed = {key: catalog.get(key) for key in expected}
    if observed != expected:
        raise ReleaseError(f"source SHA receipt contract failed: {observed} != {expected}")
    if source.stat().st_size != SOURCE_BYTES:
        raise ReleaseError(f"source byte count mismatch: {source.stat().st_size} != {SOURCE_BYTES}")
    current_sha256 = sha256_file(source)
    if current_sha256 != SOURCE_SHA256:
        raise ReleaseError(
            f"current source SHA-256 mismatch: {current_sha256} != {SOURCE_SHA256}"
        )
    parquet_rows = pq.ParquetFile(source).metadata.num_rows
    if parquet_rows != EXPECTED["catalog_rows"]:
        raise ReleaseError(
            f"source Parquet row count mismatch: {parquet_rows} != {EXPECTED['catalog_rows']}"
        )
    return {
        "receipt_path": repo_relative(receipt_path),
        "receipt_sha256": sha256_file(receipt_path),
        "upstream_revision": catalog.get("revision"),
        "content_sha256": current_sha256,
        "bytes": SOURCE_BYTES,
        "rows": parquet_rows,
        "verification_basis": "current full SHA-256 pass plus committed exact receipt, byte count, and Parquet-row checks",
    }


def validate_release(output_dir: Path, manifest: dict[str, Any] | None = None) -> dict[str, Any]:
    manifest_path = output_dir / "MANIFEST.json"
    payload = manifest or json.loads(manifest_path.read_text(encoding="utf-8"))
    primary = output_dir / payload["products"]["primary"]["filename"]
    quarantine = output_dir / payload["products"]["quarantine"]["filename"]
    primary_names = tuple(pq.ParquetFile(primary).schema_arrow.names)
    if primary_names != PRIMARY_COLUMNS:
        raise ReleaseError("primary Parquet schema differs from the release contract")
    if tuple(pq.ParquetFile(quarantine).schema_arrow.names) != QUARANTINE_COLUMNS:
        raise ReleaseError("quarantine Parquet schema differs from the release contract")
    if pq.ParquetFile(primary).metadata.num_rows != EXPECTED["catalog_rows"]:
        raise ReleaseError("primary Parquet row count mismatch")
    if pq.ParquetFile(quarantine).metadata.num_rows != EXPECTED["unsafe_catalog_rows"]:
        raise ReleaseError("quarantine Parquet row count mismatch")
    primary_semantics = validate_primary_semantics(primary)
    quarantine_equivalence = validate_quarantine_equivalence(primary, quarantine)
    observed = {
        "primary_hc_rows": 0,
        "unsafe_catalog_rows": 0,
        "unsafe_primary_hc_rows": 0,
        "strict_primary_hc_rows": 0,
        "quarantine_primary_hc_rows": 0,
        "quarantine_bad_reason_rows": 0,
        "quarantine_science_enabled_rows": 0,
    }
    for batch in pq.ParquetFile(primary).iter_batches(
        columns=["primary_hc", "raw_flip_qc_unsafe"], batch_size=500_000
    ):
        primary_hc = _numpy(batch, "primary_hc").astype(bool, copy=False)
        unsafe = _numpy(batch, "raw_flip_qc_unsafe").astype(bool, copy=False)
        observed["primary_hc_rows"] += int(primary_hc.sum())
        observed["unsafe_catalog_rows"] += int(unsafe.sum())
        observed["unsafe_primary_hc_rows"] += int((primary_hc & unsafe).sum())
        observed["strict_primary_hc_rows"] += int((primary_hc & ~unsafe).sum())
    for batch in pq.ParquetFile(quarantine).iter_batches(
        columns=["is_primary_hc", "unsafe_reason_code", "do_not_use_for_science"],
        batch_size=500_000,
    ):
        observed["quarantine_primary_hc_rows"] += int(
            _numpy(batch, "is_primary_hc").astype(bool, copy=False).sum()
        )
        observed["quarantine_bad_reason_rows"] += sum(
            value != REASON for value in _strings(batch, "unsafe_reason_code")
        )
        observed["quarantine_science_enabled_rows"] += int(
            (~_numpy(batch, "do_not_use_for_science").astype(bool, copy=False)).sum()
        )
    gates = {
        "primary_hc_rows": observed["primary_hc_rows"] == EXPECTED["primary_hc_rows"],
        "unsafe_catalog_rows": observed["unsafe_catalog_rows"] == EXPECTED["unsafe_catalog_rows"],
        "unsafe_primary_hc_rows": observed["unsafe_primary_hc_rows"] == EXPECTED["unsafe_primary_hc_rows"],
        "strict_primary_hc_rows": observed["strict_primary_hc_rows"] == EXPECTED["strict_primary_hc_rows"],
        "quarantine_primary_hc_rows": observed["quarantine_primary_hc_rows"] == EXPECTED["unsafe_primary_hc_rows"],
        "quarantine_reason_codes": observed["quarantine_bad_reason_rows"] == 0,
        "quarantine_do_not_use": observed["quarantine_science_enabled_rows"] == 0,
        "primary_raw_score_columns_absent": not any(
            "raw_score" in name or "reconstructed" in name
            for name in primary_names
        ),
    }
    if not all(gates.values()):
        raise ReleaseError(f"release semantic gates failed: {gates}; observed={observed}")
    for product in payload["products"].values():
        path = output_dir / product["filename"]
        if path.stat().st_size != product["bytes"] or sha256_file(path) != product["sha256"]:
            raise ReleaseError(f"release checksum mismatch: {path}")
    return {
        "status": "PASS",
        "schema": payload["schema"],
        "counts": payload["counts"],
        "semantic_counts": observed,
        "semantic_gates": gates,
        "primary_semantics": primary_semantics,
        "quarantine_equivalence": quarantine_equivalence,
        "primary_raw_score_columns_absent": gates["primary_raw_score_columns_absent"],
        "quarantine_reason_code": REASON,
        "calibrated_probability_claim": False,
    }


def validate_quarantine_equivalence(primary: Path, quarantine: Path, *, batch_size: int = 250_000) -> dict[str, Any]:
    """Prove quarantine IDs equal exactly the primary unsafe-row IDs."""
    counts = {
        "primary_unsafe_rows": 0, "quarantine_rows": 0,
        "quarantine_null_object_id": 0, "quarantine_duplicate_object_id": 0,
        "quarantine_null_primary_hc": 0,
        "quarantine_missing_unsafe_object_id": 0, "quarantine_extra_object_id": 0,
        "quarantine_primary_hc_mismatch": 0,
    }
    with tempfile.TemporaryDirectory(prefix="p4-quarantine-equivalence-") as directory:
        with sqlite3.connect(Path(directory) / "quarantine_ids.sqlite3") as connection:
            connection.execute("PRAGMA journal_mode=OFF")
            connection.execute("PRAGMA synchronous=OFF")
            connection.execute("CREATE TABLE unsafe_primary (object_id TEXT PRIMARY KEY, primary_hc INTEGER NOT NULL) WITHOUT ROWID")
            connection.execute("CREATE TABLE quarantine (object_id TEXT PRIMARY KEY, primary_hc INTEGER NOT NULL) WITHOUT ROWID")
            for batch in pq.ParquetFile(primary).iter_batches(columns=["object_id", "primary_hc", "raw_flip_qc_unsafe"], batch_size=batch_size):
                ids = _strings(batch, "object_id")
                hc = _numpy(batch, "primary_hc").astype(bool, copy=False)
                unsafe = _numpy(batch, "raw_flip_qc_unsafe").astype(bool, copy=False)
                rows = [(str(object_id), int(is_hc)) for object_id, is_hc in zip(ids[unsafe], hc[unsafe])]
                counts["primary_unsafe_rows"] += len(rows)
                try:
                    connection.executemany("INSERT INTO unsafe_primary VALUES (?, ?)", rows)
                except sqlite3.IntegrityError as exc:
                    raise ReleaseError("duplicate unsafe object_id in primary product") from exc
            for batch in pq.ParquetFile(quarantine).iter_batches(columns=["object_id", "is_primary_hc"], batch_size=batch_size):
                ids = batch.column(batch.schema.get_field_index("object_id")).to_pylist()
                hc = batch.column(batch.schema.get_field_index("is_primary_hc")).to_pylist()
                counts["quarantine_rows"] += batch.num_rows
                counts["quarantine_null_object_id"] += sum(value is None for value in ids)
                counts["quarantine_null_primary_hc"] += sum(value is None for value in hc)
                rows = [
                    (str(object_id), int(bool(is_hc)))
                    for object_id, is_hc in zip(ids, hc)
                    if object_id is not None and is_hc is not None
                ]
                before = connection.total_changes
                connection.executemany("INSERT OR IGNORE INTO quarantine VALUES (?, ?)", rows)
                counts["quarantine_duplicate_object_id"] += len(rows) - (connection.total_changes - before)
            counts["quarantine_missing_unsafe_object_id"] = connection.execute("SELECT COUNT(*) FROM unsafe_primary p LEFT JOIN quarantine q USING(object_id) WHERE q.object_id IS NULL").fetchone()[0]
            counts["quarantine_extra_object_id"] = connection.execute("SELECT COUNT(*) FROM quarantine q LEFT JOIN unsafe_primary p USING(object_id) WHERE p.object_id IS NULL").fetchone()[0]
            counts["quarantine_primary_hc_mismatch"] = connection.execute("SELECT COUNT(*) FROM quarantine q JOIN unsafe_primary p USING(object_id) WHERE q.primary_hc != p.primary_hc").fetchone()[0]
    gates = {
        "quarantine_rows_equal_primary_unsafe_rows": counts["quarantine_rows"] == counts["primary_unsafe_rows"],
        **{name: value == 0 for name, value in counts.items() if name not in {"primary_unsafe_rows", "quarantine_rows"}},
    }
    if not all(gates.values()):
        failed = [name for name, passed in gates.items() if not passed]
        raise ReleaseError(f"quarantine equivalence gates failed: {failed}; counts={counts}")
    return {"status": "PASS", "rows_scanned": counts, "uniqueness_backend": "temporary SQLite PRIMARY KEY (disk-backed)", "gates": gates}


def validate_primary_semantics(
    primary: Path,
    *,
    batch_size: int = 250_000,
) -> dict[str, Any]:
    """Stream every Catalog-C row through the declared machine contract.

    Uniqueness is tracked in a temporary disk-backed SQLite primary-key table,
    avoiding an 8.5-million-element in-memory Python set.  Scores are validated
    only as uncalibrated softmax ranking outputs; this function makes no claim
    that they are calibrated probabilities or likelihood weights.
    """
    columns = (
        "object_id", "ra_deg", "dec_deg", "class_eq", *SCORE_COLUMNS,
        "score_eq_max", "is_spiral", "primary_hc",
    )
    counts = {
        "rows": 0,
        "null_object_id": 0,
        "duplicate_object_id": 0,
        "null_semantic_value": 0,
        "coordinate_out_of_range": 0,
        "class_not_allowed": 0,
        "score_nonfinite": 0,
        "score_out_of_bounds": 0,
        "score_simplex_mismatch": 0,
        "score_eq_max_mismatch": 0,
        "class_argmax_mismatch": 0,
        "is_spiral_mismatch": 0,
        "primary_hc_mismatch": 0,
    }
    class_order = np.asarray(ALLOWED_CLASSES, dtype=object)
    with tempfile.TemporaryDirectory(prefix="p4-catalog-id-audit-") as directory:
        database = Path(directory) / "object_ids.sqlite3"
        with sqlite3.connect(database) as connection:
            connection.execute("PRAGMA journal_mode=OFF")
            connection.execute("PRAGMA synchronous=OFF")
            connection.execute(
                "CREATE TABLE object_ids (object_id TEXT PRIMARY KEY) WITHOUT ROWID"
            )
            parquet = pq.ParquetFile(primary)
            for batch in parquet.iter_batches(columns=list(columns), batch_size=batch_size):
                counts["rows"] += batch.num_rows
                nulls = {
                    name: batch.column(batch.schema.get_field_index(name)).null_count
                    for name in columns
                }
                counts["null_object_id"] += nulls["object_id"]
                counts["null_semantic_value"] += sum(
                    value for name, value in nulls.items() if name != "object_id"
                )

                object_ids = batch.column(
                    batch.schema.get_field_index("object_id")
                ).to_pylist()
                nonnull_ids = [(value,) for value in object_ids if value is not None]
                before = connection.total_changes
                connection.executemany(
                    "INSERT OR IGNORE INTO object_ids(object_id) VALUES (?)", nonnull_ids
                )
                counts["duplicate_object_id"] += len(nonnull_ids) - (
                    connection.total_changes - before
                )

                # Substitute values only to keep the vectorized audit running;
                # nulls remain independently fatal through null_semantic_value.
                ra = np.asarray(
                    batch.column(batch.schema.get_field_index("ra_deg")).to_pylist(),
                    dtype=np.float64,
                )
                dec = np.asarray(
                    batch.column(batch.schema.get_field_index("dec_deg")).to_pylist(),
                    dtype=np.float64,
                )
                classes = np.asarray(
                    batch.column(batch.schema.get_field_index("class_eq")).to_pylist(),
                    dtype=object,
                )
                scores = np.column_stack([
                    np.asarray(
                        batch.column(batch.schema.get_field_index(name)).to_pylist(),
                        dtype=np.float64,
                    )
                    for name in SCORE_COLUMNS
                ])
                score_max = np.asarray(
                    batch.column(batch.schema.get_field_index("score_eq_max")).to_pylist(),
                    dtype=np.float64,
                )
                is_spiral = np.asarray(
                    batch.column(batch.schema.get_field_index("is_spiral")).to_pylist(),
                    dtype=object,
                )
                primary_hc = np.asarray(
                    batch.column(batch.schema.get_field_index("primary_hc")).to_pylist(),
                    dtype=object,
                )

                coordinate_ok = (
                    np.isfinite(ra) & np.isfinite(dec)
                    & (ra >= 0.0) & (ra < 360.0)
                    & (dec >= -90.0) & (dec <= 90.0)
                )
                counts["coordinate_out_of_range"] += int((~coordinate_ok).sum())
                allowed = np.isin(classes, ALLOWED_CLASSES)
                counts["class_not_allowed"] += int((~allowed).sum())
                finite = np.isfinite(scores).all(axis=1) & np.isfinite(score_max)
                counts["score_nonfinite"] += int((~finite).sum())
                bounded = (
                    ((scores >= 0.0) & (scores <= 1.0)).all(axis=1)
                    & (score_max >= 0.0) & (score_max <= 1.0)
                )
                counts["score_out_of_bounds"] += int((finite & ~bounded).sum())
                simplex = np.isclose(
                    scores.sum(axis=1), 1.0, rtol=0.0, atol=SCORE_SIMPLEX_ATOL
                )
                counts["score_simplex_mismatch"] += int((finite & ~simplex).sum())
                derived_max = np.max(scores, axis=1)
                max_matches = np.isclose(
                    score_max, derived_max, rtol=0.0, atol=SCORE_EQUALITY_ATOL
                )
                counts["score_eq_max_mismatch"] += int((finite & ~max_matches).sum())

                # np.argmax selects the first maximum.  The release tie order is
                # therefore CW, then CCW, then NOT_SPIRAL.
                derived_class = class_order[np.argmax(scores, axis=1)]
                counts["class_argmax_mismatch"] += int(
                    (finite & allowed & (classes != derived_class)).sum()
                )
                derived_spiral = np.isin(classes, ("CW", "CCW"))
                bool_spiral = np.asarray([bool(v) if v is not None else False for v in is_spiral])
                bool_hc = np.asarray([bool(v) if v is not None else False for v in primary_hc])
                counts["is_spiral_mismatch"] += int((bool_spiral != derived_spiral).sum())
                derived_hc = (
                    derived_spiral & coordinate_ok
                    & (np.maximum(scores[:, 0], scores[:, 1]) > 0.6)
                )
                counts["primary_hc_mismatch"] += int((bool_hc != derived_hc).sum())
            connection.commit()

    gates = {name: value == 0 for name, value in counts.items() if name != "rows"}
    if not all(gates.values()):
        failed = [name for name, passed in gates.items() if not passed]
        raise ReleaseError(
            f"primary semantic gates failed: {failed}; counts={counts}"
        )
    return {
        "status": "PASS",
        "rows_scanned": counts["rows"],
        "batch_size": batch_size,
        "uniqueness_backend": "temporary SQLite PRIMARY KEY (disk-backed)",
        "score_contract": {
            "calibrated_probability_claim": False,
            "structural_softmax_simplex": True,
            "simplex_atol": SCORE_SIMPLEX_ATOL,
            "argmax_tie_order": list(ALLOWED_CLASSES),
        },
        "violation_counts": {name: value for name, value in counts.items() if name != "rows"},
        "gates": gates,
    }


def write_validation_receipt(
    output_dir: Path,
    validation_result: dict[str, Any],
    receipt_path: Path,
) -> dict[str, Any]:
    """Atomically write a portable receipt for one exact validate-only run."""
    manifest_path = output_dir / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    primary_path = output_dir / manifest["products"]["primary"]["filename"]
    quarantine_path = output_dir / manifest["products"]["quarantine"]["filename"]
    release_schema_path = output_dir / manifest["products"]["schema"]["filename"]
    validator_path = Path(__file__).resolve()
    receipt = {
        "schema": "p4-catalog-c-semantic-validation-receipt/v1",
        "paper": "P4",
        "paper_version": PAPER_VERSION,
        "catalog_payload_version": CATALOG_PAYLOAD_VERSION,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "command_mode": "validate-only",
        "provenance": {
            "validator": {
                "path": repo_relative(validator_path),
                "bytes": validator_path.stat().st_size,
                "sha256": sha256_file(validator_path),
            },
            "validator_schema_source": {
                "path": repo_relative(SCHEMA_PATH),
                "bytes": SCHEMA_PATH.stat().st_size,
                "sha256": sha256_file(SCHEMA_PATH),
            },
            "release_schema": {
                "path": repo_relative(release_schema_path),
                "bytes": release_schema_path.stat().st_size,
                "sha256": sha256_file(release_schema_path),
            },
            "manifest": {
                "path": repo_relative(manifest_path),
                "bytes": manifest_path.stat().st_size,
                "sha256": sha256_file(manifest_path),
            },
            "primary_parquet": {
                "path": repo_relative(primary_path),
                "bytes": primary_path.stat().st_size,
                "sha256": sha256_file(primary_path),
                "manifest_bytes": manifest["products"]["primary"]["bytes"],
                "manifest_sha256": manifest["products"]["primary"]["sha256"],
            },
            "quarantine_parquet": {
                "path": repo_relative(quarantine_path),
                "bytes": quarantine_path.stat().st_size,
                "sha256": sha256_file(quarantine_path),
                "manifest_bytes": manifest["products"]["quarantine"]["bytes"],
                "manifest_sha256": manifest["products"]["quarantine"]["sha256"],
            },
        },
        "validation_result": validation_result,
    }
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = receipt_path.with_name(f".{receipt_path.name}.tmp")
    temporary.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    os.replace(temporary, receipt_path)
    return receipt


def build_release(
    source: Path,
    output_dir: Path,
    schema_path: Path,
    null_path: Path,
    source_receipt_path: Path = SOURCE_RECEIPT_PATH,
) -> dict[str, Any]:
    source_identity = validate_source_identity(source, source_receipt_path)
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    if schema.get("catalog_payload_version") != CATALOG_PAYLOAD_VERSION:
        raise ReleaseError("machine schema catalog payload is not pinned to v1.0.244")
    if schema.get("paper_version") != PAPER_VERSION:
        raise ReleaseError("machine schema paper binding is not pinned to v1.0.253")
    output_dir.mkdir(parents=True, exist_ok=True)
    final_primary = output_dir / schema["primary_product"]["filename"]
    final_quarantine = output_dir / schema["quarantine_product"]["filename"]
    if final_primary.exists() or final_quarantine.exists():
        raise ReleaseError("release outputs already exist; refusing to overwrite checkpoint")
    temp_primary = final_primary.with_suffix(".parquet.tmp")
    temp_quarantine = final_quarantine.with_suffix(".parquet.tmp")
    totals: dict[str, Any] = {key: 0 for key in EXPECTED}
    totals["max_bound_excursion"] = 0.0
    primary_writer = None
    quarantine_writer = None
    try:
        parquet = pq.ParquetFile(source)
        for batch_index, batch in enumerate(
            parquet.iter_batches(batch_size=250_000, columns=list(INPUT_COLUMNS)), start=1
        ):
            primary, quarantine, stats = split_batch(batch)
            primary_writer = primary_writer or pq.ParquetWriter(
                temp_primary, primary.schema, compression="zstd"
            )
            quarantine_writer = quarantine_writer or pq.ParquetWriter(
                temp_quarantine, quarantine.schema, compression="zstd"
            )
            primary_writer.write_table(primary)
            quarantine_writer.write_table(quarantine)
            _add_stats(totals, stats)
            print(
                f"checkpoint batch={batch_index} rows={totals['catalog_rows']:,} "
                f"unsafe={totals['unsafe_catalog_rows']:,} "
                f"unsafe_hc={totals['unsafe_primary_hc_rows']:,}",
                flush=True,
            )
    finally:
        if primary_writer is not None:
            primary_writer.close()
        if quarantine_writer is not None:
            quarantine_writer.close()

    observed = {key: int(totals[key]) for key in EXPECTED}
    if observed != EXPECTED:
        temp_primary.unlink(missing_ok=True)
        temp_quarantine.unlink(missing_ok=True)
        raise ReleaseError(f"source-validated count contract failed: {observed} != {EXPECTED}")
    os.replace(temp_primary, final_primary)
    os.replace(temp_quarantine, final_quarantine)
    schema_copy = output_dir / "SCHEMA.json"
    shutil.copy2(schema_path, schema_copy)
    null_copy = output_dir / "primary_label_shuffle_amps_10000.npy"
    shutil.copy2(null_path, null_copy)
    # Retain the original public filename as a backward-compatible alias, but
    # bind it to the declared fixed-occupancy primary null.  The first public
    # upload accidentally placed the pixel-permutation diagnostic at this
    # ambiguous path; keeping the alias with the correct bytes makes old links
    # safe while the explicit filenames below remove the ambiguity.
    legacy_null_alias = output_dir / "primary_null_amps_10000.npy"
    shutil.copy2(null_path, legacy_null_alias)
    pixel_null_copy = output_dir / "pixel_permutation_amps_10000.npy"
    if PIXEL_NULL_PATH.exists():
        shutil.copy2(PIXEL_NULL_PATH, pixel_null_copy)
    if EXPECTED["catalog_rows"] == 8_474_531:
        reproduction_result = reproduce(
            final_primary,
            null_copy,
            pixel_null_copy if pixel_null_copy.exists() else None,
            enforce_expected=True,
        )
    else:
        # Unit fixtures exercise release splitting with too few supported sky
        # pixels for a non-singular dipole fit.
        reproduction_result = {
            "schema": "p4-primary-null-reproduction/v1",
            "paper_version": PAPER_VERSION,
            "status": "NOT_EVALUATED_TEST_FIXTURE",
        }
    reproduction_result_path = output_dir / "PRIMARY_REPRODUCTION.json"
    reproduction_result_path.write_text(
        json.dumps(reproduction_result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    dictionary_copy = output_dir / "CATALOG_SCHEMA.md"
    shutil.copy2(DATA_DICTIONARY_PATH, dictionary_copy)
    reproduction_copy = output_dir / REPRODUCTION_SCRIPT_PATH.name
    shutil.copy2(REPRODUCTION_SCRIPT_PATH, reproduction_copy)
    claim_audit_copy = output_dir / CLAIM_AUDIT_SCRIPT_PATH.name
    shutil.copy2(CLAIM_AUDIT_SCRIPT_PATH, claim_audit_copy)
    null_generator_copy = output_dir / NULL_GENERATOR_SCRIPT_PATH.name
    shutil.copy2(NULL_GENERATOR_SCRIPT_PATH, null_generator_copy)

    products = {}
    for role, path in (
        ("primary", final_primary),
        ("quarantine", final_quarantine),
        ("schema", schema_copy),
        ("primary_label_shuffle_null", null_copy),
        ("primary_null_legacy_alias", legacy_null_alias),
        ("data_dictionary", dictionary_copy),
        ("reproduction_script", reproduction_copy),
        ("claim_audit_script", claim_audit_copy),
        ("primary_null_generator", null_generator_copy),
        ("primary_reproduction_result", reproduction_result_path),
    ):
        products[role] = {
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
    if pixel_null_copy.exists():
        products["pixel_permutation_robustness"] = {
            "filename": pixel_null_copy.name,
            "bytes": pixel_null_copy.stat().st_size,
            "sha256": sha256_file(pixel_null_copy),
        }
    manifest = {
        "schema": "p4-apjs-release-manifest/v1",
        "paper": "P4",
        "paper_version": PAPER_VERSION,
        "catalog_payload_version": CATALOG_PAYLOAD_VERSION,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "path": repo_relative(source),
            "bytes": SOURCE_BYTES,
            "sha256": SOURCE_SHA256,
            "identity_validation": source_identity,
        },
        "counts": observed,
        "max_reconstructed_bound_excursion": totals["max_bound_excursion"],
        "products": products,
        "unsafe_score_policy": "Quarantine only; never calibrated; never use as science weights or likelihood inputs.",
        "science_scope": schema["scientific_scope"],
        "release_gate": "LOCAL_RELEASE_CANDIDATE_ONLY; immutable archive/DOI and human ApJS review remain open",
    }
    (output_dir / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    validation = validate_release(output_dir, manifest)
    (output_dir / "VALIDATION.json").write_text(
        json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    checksum_lines = [
        f"{product['sha256']}  {product['filename']}"
        for product in products.values()
    ]
    (output_dir / "SHA256SUMS").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--schema", type=Path, default=SCHEMA_PATH)
    parser.add_argument("--null-array", type=Path, default=NULL_PATH)
    parser.add_argument("--source-sha-receipt", type=Path, default=SOURCE_RECEIPT_PATH)
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument(
        "--validation-receipt",
        type=Path,
        help="Atomically write a provenance-bound JSON receipt (requires --validate-only).",
    )
    args = parser.parse_args(argv)
    if args.validation_receipt is not None and not args.validate_only:
        parser.error("--validation-receipt requires --validate-only")
    try:
        if args.validate_only:
            result = validate_release(args.output_dir)
            if args.validation_receipt is not None:
                write_validation_receipt(args.output_dir, result, args.validation_receipt)
        else:
            result = build_release(
                args.source,
                args.output_dir,
                args.schema,
                args.null_array,
                args.source_sha_receipt,
            )
    except (OSError, ValueError, ReleaseError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

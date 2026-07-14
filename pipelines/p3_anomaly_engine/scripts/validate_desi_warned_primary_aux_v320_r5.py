#!/usr/bin/env python3
"""Independently validate the P3 v3.2.0-r5 warned-primary auxiliary table."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


CATALOG = "desi_dr1_warned_global_primary_aux_v3.2.0-r5.parquet"
EXPECTED_ROWS = 2_267
EXPECTED_COLUMNS = 47
EXPECTED_PARTS = 143
STATUS = "SECONDARY_WARNING_BEARING_NOT_PRIMARY_NOT_PHYSICALLY_VALIDATED"
EXPECTED_MASKS = {2: 787, 4: 152, 6: 1294, 2048: 3, 2050: 10, 2052: 2, 2054: 19}
EXPECTED_BITS = {1: 2110, 2: 1467, 11: 34}
GENERATED_COLUMNS = {
    "candidate_id", "auxiliary_status", "primary_catalog_member", "match_quality_tier",
    "original_member_separation_arcsec", "zwarn_hex", "zwarn_decoded_bits",
}
CLUSTER_COLUMNS = [
    "cluster_id", "n_detections", "n_surveys", "survey_list", "cluster_ra_deg",
    "cluster_dec_deg", "cluster_best_score", "member_ids", "best_survey",
    "desi_source_row", "original_internal_tid", "original_ra_deg", "original_dec_deg",
    "original_score", "original_worst_band", "original_residual_b", "original_residual_r",
    "original_residual_z",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path, block_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(block_size), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, payload: Any) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, path)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def exact_set_sha256(frame: pd.DataFrame) -> str:
    rows = [
        [int(row.cluster_id), int(row.targetid), int(row.fits_row), int(row.zwarn)]
        for row in frame.sort_values(["cluster_id", "targetid", "fits_row"]).itertuples()
    ]
    return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


def refresh_manifest(release_dir: Path) -> None:
    files = []
    for path in sorted(release_dir.iterdir()):
        if path.is_file() and path.name != "RELEASE_MANIFEST.json":
            files.append({"path": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    write_json(
        release_dir / "RELEASE_MANIFEST.json",
        {"release": "p3-v3.2.0-r5", "product_role": STATUS, "files": files},
    )


def repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / ".git").exists():
            return parent
    raise RuntimeError("cannot locate repository root from script path")


def parse_args() -> argparse.Namespace:
    root = repo_root()
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-dir", type=Path, required=True)
    parser.add_argument("--parts-dir", type=Path)
    parser.add_argument("--clusters", type=Path, required=True)
    parser.add_argument("--anomalies", type=Path, required=True)
    parser.add_argument(
        "--primary-builder", type=Path,
        default=root / "pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0-r2/build_desi_science_catalog_v320_r2.py",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    parts_dir = args.parts_dir or args.release_dir.parent / ".desi_science_catalog_v3.2.0-r2.build/match_parts"
    catalog = pd.read_parquet(args.release_dir / CATALOG)
    if len(catalog) != EXPECTED_ROWS or len(catalog.columns) != EXPECTED_COLUMNS:
        raise RuntimeError(f"unexpected catalog shape {catalog.shape}")
    expected_ids = [f"P3-DESI-WARNED-{i:06d}" for i in range(1, EXPECTED_ROWS + 1)]
    if catalog["candidate_id"].tolist() != expected_ids:
        raise RuntimeError("stable auxiliary IDs are not exact")
    if not (catalog["auxiliary_status"] == STATUS).all() or catalog["primary_catalog_member"].any():
        raise RuntimeError("secondary/non-primary labels failed")
    if not catalog["zcat_primary"].all() or not (catalog["zwarn"] != 0).all():
        raise RuntimeError("global-primary/warning-bearing selection failed")

    manifest = json.loads((args.release_dir / "RELEASE_MANIFEST.json").read_text())
    for item in manifest["files"]:
        path = args.release_dir / item["path"]
        if path.stat().st_size != item["bytes"] or sha256_file(path) != item["sha256"]:
            raise RuntimeError(f"payload manifest mismatch: {path.name}")

    parts = sorted(parts_dir.glob("matches_*.parquet"))
    if len(parts) != EXPECTED_PARTS:
        raise RuntimeError(f"expected {EXPECTED_PARTS} checkpoint parts, found {len(parts)}")
    raw = pd.concat([pd.read_parquet(path) for path in parts], ignore_index=True)
    if len(raw) != 2_468:
        raise RuntimeError("checkpoint raw-match count failed")

    primary = load_module(args.primary_builder, "p3_primary_builder_r2_validation")
    clusters = primary.load_desi_clusters(args.clusters, args.anomalies)
    cluster_fields = clusters[CLUSTER_COLUMNS].reset_index(names="cluster_table_row")
    raw = raw.merge(cluster_fields, on="cluster_table_row", validate="many_to_one")
    raw["science_target_class"] = primary.decoded_science_class(raw["desi_target"])
    expected = primary.dedupe(raw, raw["zcat_primary"].astype(bool) & (raw["zwarn"] != 0))
    expected = expected.sort_values("cluster_id", kind="mergesort").reset_index(drop=True)
    if len(expected) != EXPECTED_ROWS:
        raise RuntimeError("independent checkpoint reselection did not produce 2,267 rows")

    key_columns = ["cluster_id", "targetid", "fits_row", "zwarn"]
    if not expected[key_columns].equals(catalog[key_columns]):
        raise RuntimeError("exact warned-primary key/order set mismatch")
    source_columns = [column for column in expected.columns if column not in GENERATED_COLUMNS]
    pd.testing.assert_frame_equal(
        expected[source_columns].reset_index(drop=True),
        catalog[source_columns].reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
    )
    recomputed_sep = primary.angular_separation_arcsec(
        catalog["target_ra"].to_numpy(np.float64), catalog["target_dec"].to_numpy(np.float64),
        catalog["original_ra_deg"].to_numpy(np.float64), catalog["original_dec_deg"].to_numpy(np.float64),
    )
    if not np.array_equal(recomputed_sep, catalog["original_member_separation_arcsec"].to_numpy()):
        raise RuntimeError("original-member separation recomputation mismatch")

    masks = {int(k): int(v) for k, v in catalog["zwarn"].value_counts().sort_index().items()}
    bits = {bit: int(((catalog["zwarn"].astype(np.int64) & (1 << bit)) != 0).sum()) for bit in EXPECTED_BITS}
    if masks != EXPECTED_MASKS or bits != EXPECTED_BITS:
        raise RuntimeError(f"ZWARN accounting mismatch: masks={masks}, bits={bits}")
    set_sha = exact_set_sha256(catalog)
    qc = json.loads((args.release_dir / "QC_REPORT.json").read_text())
    if qc["exact_set_sha256_cluster_target_fits_zwarn"] != set_sha:
        raise RuntimeError("QC exact-set digest mismatch")

    assertion = {
        "status": "PASS",
        "validated_utc": utc_now(),
        "scope": "P3 v3.2.0-r5 warned-primary secondary product exact checkpoint replay",
        "product_role": STATUS,
        "checkpoint_parts": len(parts), "raw_matches": len(raw),
        "global_primary_rows": int(raw["zcat_primary"].sum()), "warned_primary_rows": len(catalog),
        "exact_key_set_and_order": True, "all_carried_source_fields_exact": True,
        "pre_post_dedup_rows_equal": True,
        "exact_set_sha256_cluster_target_fits_zwarn": set_sha,
        "exact_zwarn_mask_counts": {str(k): v for k, v in masks.items()},
        "zwarn_set_bit_counts_nonexclusive": {str(k): v for k, v in bits.items()},
        "boundary": "Secondary warning-bearing follow-up list only; not the primary catalog, not physically validated, and not a purity/rate/selection-efficiency result.",
    }
    write_json(args.release_dir / "EXACT_SET_REPLAY_ASSERTION.json", assertion)
    refresh_manifest(args.release_dir)
    print(json.dumps(assertion, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

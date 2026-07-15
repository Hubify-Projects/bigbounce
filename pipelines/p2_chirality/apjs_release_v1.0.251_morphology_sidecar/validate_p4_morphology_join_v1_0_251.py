#!/usr/bin/env python3
"""Fail-closed validator for the P4 v1.0.251 raw morphology sidecar.

This validator does not create a derived catalog.  It proves that the existing
raw DR8 morphology Parquet has a unique, exact one-to-one join to every spiral
in the public-safe P4 catalog using ``object_id == f"{BRICKID}_{OBJID}"``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pyarrow.parquet as pq


ROOT = Path(__file__).resolve().parents[3]
RELEASE_DIR = Path(__file__).resolve().parent
SAFE_CATALOG = ROOT / "pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet"
MORPHOLOGY = ROOT / "pipelines/p2_chirality/outputs/spiral_morphology_dr8.parquet"
MANIFEST = RELEASE_DIR / "MANIFEST.json"
EXPECTED_SPIRALS = 3_201_160


class JoinContractError(RuntimeError):
    """Raised when the sidecar cannot be proved safe to join."""


def sha256_file(path: Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def _require_columns(path: Path, expected: list[str]) -> None:
    observed = pq.ParquetFile(path).schema_arrow.names
    if observed != expected:
        raise JoinContractError(f"schema mismatch for {path.name}: {observed} != {expected}")


def validate_join(
    safe_catalog: Path,
    morphology: Path,
    *,
    expected_spirals: int,
    expected_safe_sha256: str | None = None,
    expected_morphology_sha256: str | None = None,
) -> dict[str, Any]:
    """Validate identity, uniqueness, and exact bidirectional join coverage."""
    if not safe_catalog.is_file() or not morphology.is_file():
        raise JoinContractError("both pinned Parquet inputs must exist locally")

    safe_columns = [
        "object_id", "ra_deg", "dec_deg", "class_eq", "score_cw_eq",
        "score_ccw_eq", "score_ns_eq", "score_eq_max", "is_spiral",
        "primary_hc", "raw_flip_qc_unsafe",
    ]
    morphology_columns = [
        "BRICKID", "OBJID", "TYPE", "FRACDEV", "SHAPEDEV_R",
        "SHAPEDEV_E1", "SHAPEDEV_E2", "SHAPEEXP_R", "SHAPEEXP_E1",
        "SHAPEEXP_E2",
    ]
    _require_columns(safe_catalog, safe_columns)
    _require_columns(morphology, morphology_columns)

    safe_sha = sha256_file(safe_catalog)
    morph_sha = sha256_file(morphology)
    if expected_safe_sha256 and safe_sha != expected_safe_sha256:
        raise JoinContractError("safe-catalog SHA-256 mismatch")
    if expected_morphology_sha256 and morph_sha != expected_morphology_sha256:
        raise JoinContractError("morphology SHA-256 mismatch")

    safe = pd.read_parquet(safe_catalog, columns=["object_id", "is_spiral"])
    safe = safe.loc[safe["is_spiral"], ["object_id"]]
    morph = pd.read_parquet(morphology, columns=["BRICKID", "OBJID"])

    if len(safe) != expected_spirals or len(morph) != expected_spirals:
        raise JoinContractError(
            f"row-count contract failed: safe spirals={len(safe)}, morphology={len(morph)}, expected={expected_spirals}"
        )
    if safe["object_id"].isna().any() or safe["object_id"].duplicated().any():
        raise JoinContractError("safe spiral object_id values must be non-null and unique")
    if morph[["BRICKID", "OBJID"]].isna().any(axis=None):
        raise JoinContractError("morphology BRICKID/OBJID values must be non-null")
    if morph.duplicated(["BRICKID", "OBJID"]).any():
        raise JoinContractError("morphology BRICKID/OBJID keys must be unique")

    safe_ids = np.sort(safe["object_id"].to_numpy(dtype=str), kind="stable")
    morph_ids = np.sort(
        (morph["BRICKID"].astype(str) + "_" + morph["OBJID"].astype(str)).to_numpy(),
        kind="stable",
    )
    if not np.array_equal(safe_ids, morph_ids):
        missing = int(np.count_nonzero(~np.isin(safe_ids, morph_ids)))
        extras = int(np.count_nonzero(~np.isin(morph_ids, safe_ids)))
        raise JoinContractError(
            f"exact-coverage contract failed: missing morphology rows={missing}, extra morphology rows={extras}"
        )

    return {
        "status": "PASS",
        "join_key": "object_id == f'{BRICKID}_{OBJID}'",
        "safe_spiral_rows": len(safe),
        "morphology_rows": len(morph),
        "unique_join_rows": len(safe_ids),
        "missing_rows": 0,
        "extra_rows": 0,
        "safe_catalog": {
            "bytes": safe_catalog.stat().st_size,
            "sha256": safe_sha,
        },
        "morphology_sidecar": {
            "bytes": morphology.stat().st_size,
            "sha256": morph_sha,
        },
        "published_columns": morphology_columns,
        "derived_columns_published": [],
        "unavailable_full_catalog_columns": [
            "redshift", "imaging_leg", "depth", "seeing", "PSF fields",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--safe-catalog", type=Path, default=SAFE_CATALOG)
    parser.add_argument("--morphology", type=Path, default=MORPHOLOGY)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    result = validate_join(
        args.safe_catalog,
        args.morphology,
        expected_spirals=manifest["contract"]["exact_spiral_rows"],
        expected_safe_sha256=manifest["inputs"]["safe_catalog"]["sha256"],
        expected_morphology_sha256=manifest["inputs"]["morphology_sidecar"]["sha256"],
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fail-closed validator for the P4 v1.0.252 raw morphology sidecar.

This validator does not create a derived catalog.  It proves that the existing
raw DR8 morphology Parquet has a unique, exact one-to-one join to every spiral
in the public-safe P4 catalog using ``object_id == f"{BRICKID}_{OBJID}"``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import tempfile
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
REPO_ID = "bamfai/galaxy-chirality-catalog"
SAFE_REVISION = "db11023306ab4eed1d7727670bd78e127b7af17a"
SAFE_REMOTE_PATH = "apjs-release/v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet"
MORPHOLOGY_REVISION = "245ad7c5f1e58c627be1390dc3125cd1ce1e3dc9"
MORPHOLOGY_REMOTE_PATH = "spiral_morphology_dr8.parquet"


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


def verify_file(path: Path, spec: dict[str, Any]) -> str:
    """Verify size and digest before any parser opens artifact bytes."""
    if not path.is_file():
        raise JoinContractError(f"required input is missing: {path}")
    observed_bytes = path.stat().st_size
    if observed_bytes != spec["bytes"]:
        raise JoinContractError(
            f"byte-count mismatch for {path.name}: {observed_bytes} != {spec['bytes']}"
        )
    observed_sha = sha256_file(path)
    if observed_sha != spec["sha256"]:
        raise JoinContractError(f"SHA-256 mismatch for {path.name}")
    return observed_sha


def download_missing_file(path: Path, *, remote_path: str, revision: str) -> None:
    """Retrieve one absent artifact from an immutable HF dataset revision."""
    if path.exists():
        return
    try:
        from huggingface_hub import hf_hub_download
    except ImportError as exc:
        raise JoinContractError(
            "--download-missing requires huggingface_hub"
        ) from exc

    cached = Path(hf_hub_download(
        repo_id=REPO_ID,
        filename=remote_path,
        repo_type="dataset",
        revision=revision,
    ))
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as destination, cached.open("rb") as source:
            shutil.copyfileobj(source, destination)
            destination.flush()
            os.fsync(destination.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        Path(temporary_name).unlink(missing_ok=True)
        raise


def ensure_inputs(
    safe_catalog: Path,
    morphology: Path,
    manifest: dict[str, Any],
    *,
    download_missing: bool,
) -> tuple[str, str]:
    """Optionally retrieve missing inputs, then verify both against the manifest."""
    safe_spec = manifest["inputs"]["safe_catalog"]
    morph_spec = manifest["inputs"]["morphology_sidecar"]
    expected_sources = (
        (safe_spec, SAFE_REMOTE_PATH, SAFE_REVISION),
        (morph_spec, MORPHOLOGY_REMOTE_PATH, MORPHOLOGY_REVISION),
    )
    for spec, remote_path, revision in expected_sources:
        source = spec.get("huggingface", {})
        if source != {
            "repo_id": REPO_ID,
            "repo_type": "dataset",
            "revision": revision,
            "path": remote_path,
        }:
            raise JoinContractError("manifest immutable Hugging Face source mismatch")
    if download_missing:
        download_missing_file(
            safe_catalog,
            remote_path=safe_spec["huggingface"]["path"],
            revision=safe_spec["huggingface"]["revision"],
        )
        download_missing_file(
            morphology,
            remote_path=morph_spec["huggingface"]["path"],
            revision=morph_spec["huggingface"]["revision"],
        )
    return (
        verify_file(safe_catalog, safe_spec),
        verify_file(morphology, morph_spec),
    )


def derive_axis_ratio(
    morphology: pd.DataFrame,
) -> np.ndarray:
    """Derive b/a on demand; b/a is not a stored sidecar column."""
    kind = morphology["TYPE"].astype(str).str.upper().to_numpy()
    use_dev = np.isin(kind, ["DEV", "COMP", "SER"]) | (
        morphology["FRACDEV"].to_numpy(dtype=float) >= 0.5
    )
    e1 = np.where(
        use_dev,
        morphology["SHAPEDEV_E1"].to_numpy(dtype=float),
        morphology["SHAPEEXP_E1"].to_numpy(dtype=float),
    )
    e2 = np.where(
        use_dev,
        morphology["SHAPEDEV_E2"].to_numpy(dtype=float),
        morphology["SHAPEEXP_E2"].to_numpy(dtype=float),
    )
    ellipticity = np.clip(np.hypot(e1, e2), 0.0, 0.999)
    return (1.0 - ellipticity) / (1.0 + ellipticity)


def validate_join(
    safe_catalog: Path,
    morphology: Path,
    *,
    expected_spirals: int,
    expected_safe_sha256: str | None = None,
    expected_morphology_sha256: str | None = None,
    verified_sha256: tuple[str, str] | None = None,
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
    safe_sha, morph_sha = verified_sha256 or (
        sha256_file(safe_catalog), sha256_file(morphology)
    )
    if expected_safe_sha256 and safe_sha != expected_safe_sha256:
        raise JoinContractError("safe-catalog SHA-256 mismatch")
    if expected_morphology_sha256 and morph_sha != expected_morphology_sha256:
        raise JoinContractError("morphology SHA-256 mismatch")

    # Artifact identity is established before parsers inspect untrusted bytes.
    _require_columns(safe_catalog, safe_columns)
    _require_columns(morphology, morphology_columns)

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
        "axis_ratio_derivation": {
            "storage": "derived_on_demand_not_stored",
            "shape_choice": "DEV for TYPE in {DEV,COMP,SER} or FRACDEV >= 0.5; EXP otherwise",
            "ellipticity": "e = clip(hypot(selected_E1, selected_E2), 0, 0.999)",
            "axis_ratio": "b/a = (1-e)/(1+e)",
        },
        "unavailable_full_catalog_columns": [
            "redshift", "imaging_leg", "depth", "seeing", "PSF fields",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--safe-catalog", type=Path, default=SAFE_CATALOG)
    parser.add_argument("--morphology", type=Path, default=MORPHOLOGY)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument(
        "--download-missing",
        action="store_true",
        help="download only absent inputs from the manifest's immutable HF revisions",
    )
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    verified = ensure_inputs(
        args.safe_catalog,
        args.morphology,
        manifest,
        download_missing=args.download_missing,
    )
    result = validate_join(
        args.safe_catalog,
        args.morphology,
        expected_spirals=manifest["contract"]["exact_spiral_rows"],
        expected_safe_sha256=manifest["inputs"]["safe_catalog"]["sha256"],
        expected_morphology_sha256=manifest["inputs"]["morphology_sidecar"]["sha256"],
        verified_sha256=verified,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

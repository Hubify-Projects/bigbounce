#!/usr/bin/env python3
"""Pod-side scan runner for the DESI DR1 clean-rerun BigAE score.

For each `(survey, program, healpix)` group in the locator inventory emitted
by `derive_locator_inventory.py`, this script:

  1. downloads that group's `coadd-<survey>-<program>-<healpix>.fits` with
     retry (via the archived inference module's own `download_file()`);
  2. scores every spectrum in it through the archived inference path
     (`enhanced_18M_inference.py`'s `BigAE`, `downsample()`, and per-spectrum
     median-|flux| normalization, all imported unmodified via
     `process_healpix()`);
  3. converts each spectrum's raw per-spectrum mean MSE into the sealed
     `anomaly_score = (per_spectrum_mean_mse - mse_mean) / mse_std`, using
     the exact calibration bound into the run contract
     (`build_calibration.anomaly_score_from_calibration`, imported — never
     re-derived);
  4. writes one Parquet shard per healpix group with columns `targetid`
     (int64), `anomaly_score` (float64), `mean_mse` (float64), `healpix`,
     `survey`, `program`;
  5. immediately calls `clean_rerun_contract.py`'s `record_receipt()` on
     that shard (hash, row count, schema, and an atomic, contract-bound
     resume checkpoint);
  6. deletes the downloaded coadd FITS file to bound local disk use.

Fail-closed: before scoring anything, this script re-verifies that the
model file at `--model` and the archived inference module on disk still
hash to exactly what the supplied `--contract` bound (`build-contract`
already re-verified both once; this is a second, independent check against
whatever files are actually present on this pod at scan time).

`--start`/`--end` slice the locator inventory so multiple pod workers can
scan disjoint ranges in parallel; `--limit` caps the number of groups
processed after slicing, for a bounded smoke run. Resume is automatic: any
shard already present in the contract-bound checkpoint is skipped.

This script downloads real DESI DR1 spectra and runs GPU/CPU inference; it
is meant to run on the pod, never inside an offline unit test.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import types
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derive_locator_inventory import sha256_file  # noqa: E402
from build_calibration import (  # noqa: E402
    anomaly_score_from_calibration,
    load_archived_inference_module,
    load_model,
    ARCHIVED_INFERENCE_PATH,
)

REPO_ROOT = Path(__file__).resolve().parents[3]
CONTRACT_MODULE_PATH = REPO_ROOT / "pipelines/p1_highz_tracers/clean_rerun_contract.py"
DESI_HEALPIX_BASE_URL = "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/"


class ScanError(RuntimeError):
    """Raised when a scan input cannot be trusted or a shard cannot be produced safely."""


def load_contract_module(path: Path = CONTRACT_MODULE_PATH) -> types.ModuleType:
    """Import `clean_rerun_contract.py` unmodified, by exact file path."""
    spec = importlib.util.spec_from_file_location("clean_rerun_contract_bound", path)
    if spec is None or spec.loader is None:
        raise ScanError(f"cannot load contract module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def iter_inventory(inventory_path: Path) -> list[dict[str, Any]]:
    if not inventory_path.is_file():
        raise ScanError(f"locator inventory is absent: {inventory_path}")
    records = []
    with inventory_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ScanError(f"invalid JSON line {line_number} in {inventory_path}: {exc}") from exc
    return records


def already_completed_shards(checkpoint_path: Path) -> set[str]:
    if not checkpoint_path.exists():
        return set()
    checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    return {entry["shard"] for entry in checkpoint.get("completed_shards", [])}


def shard_name(survey: str, program: str, healpix: int) -> str:
    return f"scored-{survey}-{program}-{healpix}.parquet"


def score_group(module: types.ModuleType, model: Any, device: Any, coadd_path: Path, calibration: dict[str, Any]) -> list[dict[str, Any]]:
    """Score every spectrum in a downloaded coadd via the archived process_healpix()."""
    _n_obj, rows = module.process_healpix(str(coadd_path), None, model, device)
    mse_mean = float(calibration["mse_mean"])
    mse_std = float(calibration["mse_std"])
    scored = []
    for row in rows:
        raw_mse = float(row["anomaly_score"])
        scored.append(
            {
                "targetid": int(row["targetid"]),
                "mean_mse": raw_mse,
                "anomaly_score": anomaly_score_from_calibration(raw_mse, mse_mean, mse_std),
            }
        )
    return scored


def write_shard(scored_rows: list[dict[str, Any]], survey: str, program: str, healpix: int, shard_dir: Path) -> Path:
    import pyarrow as pa
    import pyarrow.parquet as pq

    shard_dir.mkdir(parents=True, exist_ok=True)
    path = shard_dir / shard_name(survey, program, healpix)
    table = pa.table(
        {
            "targetid": pa.array([r["targetid"] for r in scored_rows], type=pa.int64()),
            "anomaly_score": pa.array([r["anomaly_score"] for r in scored_rows], type=pa.float64()),
            "mean_mse": pa.array([r["mean_mse"] for r in scored_rows], type=pa.float64()),
            "healpix": pa.array([healpix] * len(scored_rows), type=pa.int64()),
            "survey": pa.array([survey] * len(scored_rows), type=pa.string()),
            "program": pa.array([program] * len(scored_rows), type=pa.string()),
        }
    )
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    pq.write_table(table, tmp_path, compression="zstd")
    os.replace(tmp_path, path)
    return path


def run_scan(
    inventory_path: Path,
    contract_path: Path,
    model_path: Path,
    shard_dir: Path,
    receipt_dir: Path,
    checkpoint_path: Path,
    coadd_cache_dir: Path,
    base_url: str = DESI_HEALPIX_BASE_URL,
    start: int = 0,
    end: int | None = None,
    limit: int | None = None,
) -> list[Path]:
    import torch

    contract_module = load_contract_module()
    contract = contract_module.read_json(contract_path)
    contract_module.verify_contract(contract)
    calibration = contract["calibration"]

    observed_model_sha = sha256_file(model_path)
    if observed_model_sha != contract["model"]["sha256"]:
        raise ScanError(
            f"model SHA-256 mismatch: contract expects {contract['model']['sha256']}, "
            f"got {observed_model_sha} for {model_path}"
        )
    observed_inference_sha = sha256_file(ARCHIVED_INFERENCE_PATH)
    if observed_inference_sha != contract["inference_code"]["sha256"]:
        raise ScanError(
            "inference-code SHA-256 mismatch: contract expects "
            f"{contract['inference_code']['sha256']}, got {observed_inference_sha}"
        )

    records = iter_inventory(inventory_path)
    records = records[start:end] if end is not None else records[start:]
    if limit is not None:
        records = records[:limit]
    if not records:
        raise ScanError("no inventory records selected by --start/--end/--limit")

    inference_module = load_archived_inference_module()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = load_model(inference_module, model_path, device)

    completed = already_completed_shards(checkpoint_path)
    coadd_cache_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    for record in records:
        survey, program, healpix = record["survey"], record["program"], int(record["healpix"])
        name = shard_name(survey, program, healpix)
        if name in completed:
            continue

        relative = record["coadd_relative_path"]
        if not relative.startswith("healpix/"):
            raise ScanError(f"unexpected coadd_relative_path shape: {relative}")
        coadd_url = base_url + relative[len("healpix/") :]
        coadd_fname = Path(relative).name
        coadd_path = coadd_cache_dir / coadd_fname

        ok = inference_module.download_file(coadd_url, str(coadd_path))
        if not ok:
            raise ScanError(f"failed to download coadd after retries: {coadd_url}")
        try:
            scored_rows = score_group(inference_module, model, device, coadd_path, calibration)
            shard_path = write_shard(scored_rows, survey, program, healpix, shard_dir)
        finally:
            if coadd_path.exists():
                coadd_path.unlink()

        contract_module.record_receipt(contract_path, shard_path, receipt_dir, checkpoint_path)
        completed.add(name)
        written.append(shard_path)

    return written


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True, help="JSON-lines locator inventory")
    parser.add_argument("--contract", type=Path, required=True, help="sealed run-contract.json")
    parser.add_argument("--model", type=Path, required=True, help="best_model_47k.pt on this pod")
    parser.add_argument("--shard-dir", type=Path, required=True)
    parser.add_argument("--receipt-dir", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--coadd-cache-dir", type=Path, required=True)
    parser.add_argument("--base-url", type=str, default=DESI_HEALPIX_BASE_URL)
    parser.add_argument("--start", type=int, default=0, help="inventory slice start (parallel workers)")
    parser.add_argument("--end", type=int, default=None, help="inventory slice end, exclusive")
    parser.add_argument("--limit", type=int, default=None, help="cap groups processed after slicing (smoke mode)")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    written = run_scan(
        args.inventory,
        args.contract,
        args.model,
        args.shard_dir,
        args.receipt_dir,
        args.checkpoint,
        args.coadd_cache_dir,
        base_url=args.base_url,
        start=args.start,
        end=args.end,
        limit=args.limit,
    )
    print(f"wrote {len(written)} shard(s)")
    for path in written:
        print(f"  {path}")


if __name__ == "__main__":
    main()

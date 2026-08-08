#!/usr/bin/env python3
"""Fail-closed provenance scaffold for a clean DESI DR1 BigAE rerun.

This tool intentionally does not download spectra or execute inference.  It
locks inputs/model/calibration before a worker starts, then records and checks
the outputs produced by that worker.  Historical 195,829 and 249,905 counts
are comparison labels only; neither is a target for a new run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CONTRACT_VERSION = "p1-desi-clean-rerun/v1"
HISTORICAL_GENERATIONS = (
    {
        "generation_id": "historical-original-17_651_065",
        "input_rows_reported": 17_651_065,
        "threshold_count_reported": 195_829,
        "status": "frozen release; distinct historical generation",
    },
    {
        "generation_id": "historical-enhanced-22_504_897",
        "input_rows_reported": 22_504_897,
        "threshold_count_reported": 249_905,
        "status": "summary-only; parent shards and calibration unrecovered",
    },
)

MODEL_TENSOR_SHAPES = {
    "enc.0.weight": [512, 496],
    "enc.4.weight": [256, 512],
    "enc.8.weight": [128, 256],
    "enc.10.weight": [128, 128],
    "dec.0.weight": [128, 128],
    "dec.2.weight": [256, 128],
    "dec.6.weight": [512, 256],
    "dec.10.weight": [496, 512],
}
INPUT_REQUIRED = {
    "manifest_version",
    "source_revision",
    "catalog_url",
    "catalog_checksum_url",
    "catalog_sha256",
    "targetid_column",
    "spectrum_locator",
    "locator_inventory_sha256",
}
CALIBRATION_REQUIRED = {
    "artifact_version",
    "status",
    "score_definition",
    "fit_scope",
    "mse_mean",
    "mse_std",
    "training_manifest_sha256",
    "validation_manifest_sha256",
    "fit_code_sha256",
}


class ContractError(RuntimeError):
    """Raised when provenance is incomplete or contradictory."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_bytes(payload: Any) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")


def payload_sha256(payload: Any) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ContractError(f"required artifact is absent: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ContractError(f"invalid JSON artifact: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ContractError(f"JSON artifact must be an object: {path}")
    return value


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False
    ) as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def require_sha(value: Any, label: str) -> None:
    if not isinstance(value, str) or len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise ContractError(f"{label} must be a lowercase SHA-256")


def verify_input_manifest(manifest: dict[str, Any]) -> None:
    missing = sorted(INPUT_REQUIRED - set(manifest))
    if missing:
        raise ContractError(f"input manifest missing required fields: {', '.join(missing)}")
    if manifest["source_revision"] != "iron":
        raise ContractError("input manifest must name the DESI DR1 iron source revision")
    if manifest["targetid_column"] != "TARGETID":
        raise ContractError("input manifest must use TARGETID as its object identity")
    locator = manifest["spectrum_locator"]
    if not isinstance(locator, dict) or locator.get("type") != "desi_dr1_iron_healpix":
        raise ContractError("input manifest needs a DESI DR1 iron HEALPix spectrum locator")
    for label in ("catalog_sha256", "locator_inventory_sha256"):
        require_sha(manifest[label], f"input manifest {label}")


def verify_calibration(calibration: dict[str, Any]) -> None:
    missing = sorted(CALIBRATION_REQUIRED - set(calibration))
    if missing:
        raise ContractError(f"calibration artifact missing required fields: {', '.join(missing)}")
    if calibration["status"] != "sealed":
        raise ContractError("calibration artifact is not sealed; refusing to score")
    if calibration["score_definition"] != "mean_mse_over_per_spectrum_median_abs_flux_normalized_496_bins":
        raise ContractError("unexpected score definition; refusing to compare score axes")
    if calibration["fit_scope"] != "held_out_training_validation_split":
        raise ContractError("calibration must be fit on the held-out training validation split")
    try:
        if float(calibration["mse_std"]) <= 0:
            raise ContractError("calibration mse_std must be positive")
        float(calibration["mse_mean"])
    except (TypeError, ValueError) as exc:
        raise ContractError("calibration MSE statistics must be numeric") from exc
    for label in ("training_manifest_sha256", "validation_manifest_sha256", "fit_code_sha256"):
        require_sha(calibration[label], f"calibration {label}")


def inspect_model(model_path: Path) -> dict[str, Any]:
    if not model_path.is_file():
        raise ContractError(f"model file is absent: {model_path}")
    try:
        import torch
    except ImportError as exc:  # pragma: no cover - runtime prerequisite
        raise ContractError("PyTorch is required to inspect the model state dict") from exc
    try:
        state_dict = torch.load(model_path, map_location="cpu", weights_only=True)
    except Exception as exc:  # pragma: no cover - torch's exception types vary
        raise ContractError(f"cannot safely load model state dict: {exc}") from exc
    if not isinstance(state_dict, dict):
        raise ContractError("model checkpoint is not a state dict")
    observed: dict[str, list[int]] = {}
    for name, expected in MODEL_TENSOR_SHAPES.items():
        tensor = state_dict.get(name)
        shape = list(tensor.shape) if hasattr(tensor, "shape") else None
        if shape != expected:
            raise ContractError(f"model architecture mismatch at {name}: expected {expected}, got {shape}")
        observed[name] = shape
    return {
        "byte_size": model_path.stat().st_size,
        "sha256": sha256_file(model_path),
        "architecture": {
            "name": "BigAE",
            "input_bins": 496,
            "latent_dimensions": 128,
            "required_tensor_shapes": observed,
            "state_dict_key_count": len(state_dict),
        },
    }


def file_binding(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ContractError(f"required file is absent: {path}")
    return {"file_name": path.name, "byte_size": path.stat().st_size, "sha256": sha256_file(path)}


def build_contract(model: Path, inference_code: Path, input_manifest_path: Path, calibration_path: Path) -> dict[str, Any]:
    input_manifest = read_json(input_manifest_path)
    calibration = read_json(calibration_path)
    verify_input_manifest(input_manifest)
    verify_calibration(calibration)
    return {
        "contract_version": CONTRACT_VERSION,
        "created_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "model": file_binding(model) | inspect_model(model),
        "inference_code": file_binding(inference_code),
        "input_manifest": input_manifest,
        "input_manifest_sha256": payload_sha256(input_manifest),
        "calibration": calibration,
        "calibration_sha256": payload_sha256(calibration),
        "deduplication": {
            "identity_column": "targetid",
            "timing": "before threshold counts",
            "winner_rule": "last row in deterministic lexical-shard then row order",
        },
        "comparison_policy": "new counts are a new generation; never merge or tune to historical counts",
        "historical_comparators": HISTORICAL_GENERATIONS,
    }


def verify_contract(contract: dict[str, Any]) -> None:
    if contract.get("contract_version") != CONTRACT_VERSION:
        raise ContractError("unsupported rerun contract version")
    verify_input_manifest(contract.get("input_manifest", {}))
    verify_calibration(contract.get("calibration", {}))
    for binding in (contract.get("model", {}), contract.get("inference_code", {})):
        require_sha(binding.get("sha256"), "contract file binding sha256")
        if not isinstance(binding.get("byte_size"), int) or binding["byte_size"] <= 0:
            raise ContractError("contract file binding byte_size must be positive")
    if contract.get("deduplication", {}).get("timing") != "before threshold counts":
        raise ContractError("contract must deduplicate before threshold counts")


def parquet_metadata(path: Path) -> tuple[int, list[dict[str, str]]]:
    try:
        import pyarrow.parquet as pq
    except ImportError as exc:  # pragma: no cover - runtime prerequisite
        raise ContractError("pyarrow is required for Parquet receipts") from exc
    parquet = pq.ParquetFile(path)
    return parquet.metadata.num_rows, [{"name": field.name, "type": str(field.type)} for field in parquet.schema_arrow]


def record_receipt(contract_path: Path, shard: Path, receipt_dir: Path, checkpoint_path: Path) -> Path:
    contract = read_json(contract_path)
    verify_contract(contract)
    if shard.suffix != ".parquet":
        raise ContractError("a scored shard must be a Parquet file")
    rows, schema = parquet_metadata(shard)
    schema_names = {field["name"] for field in schema}
    missing = {"targetid", "anomaly_score"} - schema_names
    if missing:
        raise ContractError(f"scored shard lacks required columns: {', '.join(sorted(missing))}")
    contract_sha = payload_sha256(contract)
    receipt = {
        "receipt_version": 1,
        "contract_sha256": contract_sha,
        "calibration_sha256": contract["calibration_sha256"],
        "shard": shard.name,
        "byte_size": shard.stat().st_size,
        "sha256": sha256_file(shard),
        "row_count": rows,
        "schema": schema,
    }
    receipt_path = receipt_dir / f"{shard.name}.receipt.json"
    if receipt_path.exists() and read_json(receipt_path) != receipt:
        raise ContractError(f"receipt already exists with different content: {receipt_path}")
    write_json_atomic(receipt_path, receipt)

    checkpoint = read_json(checkpoint_path) if checkpoint_path.exists() else {
        "checkpoint_version": 1,
        "contract_sha256": contract_sha,
        "completed_shards": [],
    }
    if checkpoint.get("contract_sha256") != contract_sha:
        raise ContractError("checkpoint belongs to a different contract; refusing resume")
    completed = {entry["shard"]: entry for entry in checkpoint.get("completed_shards", [])}
    completed[shard.name] = {
        "shard": shard.name,
        "receipt": receipt_path.name,
        "receipt_sha256": payload_sha256(receipt),
    }
    checkpoint["completed_shards"] = [completed[name] for name in sorted(completed)]
    write_json_atomic(checkpoint_path, checkpoint)
    return receipt_path


def verify_receipts(contract_path: Path, shard_dir: Path, receipt_dir: Path) -> list[Path]:
    contract = read_json(contract_path)
    verify_contract(contract)
    contract_sha = payload_sha256(contract)
    shards = sorted(shard_dir.glob("*.parquet"))
    if not shards:
        raise ContractError(f"no Parquet shards found in {shard_dir}")
    for shard in shards:
        receipt_path = receipt_dir / f"{shard.name}.receipt.json"
        receipt = read_json(receipt_path)
        if receipt.get("contract_sha256") != contract_sha:
            raise ContractError(f"receipt is bound to another contract: {receipt_path}")
        rows, schema = parquet_metadata(shard)
        expected = {
            "byte_size": shard.stat().st_size,
            "sha256": sha256_file(shard),
            "row_count": rows,
            "schema": schema,
        }
        for key, value in expected.items():
            if receipt.get(key) != value:
                raise ContractError(f"receipt verification failed for {shard}: {key}")
    return shards


def summarize_after_dedup(
    contract_path: Path, shard_dir: Path, receipt_dir: Path, sqlite_path: Path, output_path: Path
) -> dict[str, Any]:
    """Stream shards through SQLite so all threshold counts are post-deduplication."""
    contract = read_json(contract_path)
    verify_contract(contract)
    shards = verify_receipts(contract_path, shard_dir, receipt_dir)
    try:
        import pyarrow.parquet as pq
    except ImportError as exc:  # pragma: no cover - runtime prerequisite
        raise ContractError("pyarrow is required for Parquet summaries") from exc
    if sqlite_path.exists():
        raise ContractError(f"dedup database already exists; choose a new path: {sqlite_path}")
    connection = sqlite3.connect(sqlite_path)
    raw_rows = 0
    try:
        connection.execute("CREATE TABLE scored (targetid INTEGER PRIMARY KEY, anomaly_score REAL NOT NULL)")
        for shard in shards:
            parquet = pq.ParquetFile(shard)
            for batch in parquet.iter_batches(columns=["targetid", "anomaly_score"]):
                targetids = batch.column(0).to_pylist()
                scores = batch.column(1).to_pylist()
                if len(targetids) != len(scores):
                    raise ContractError(f"column-length mismatch in {shard}")
                rows = list(zip(targetids, scores))
                raw_rows += len(rows)
                connection.executemany(
                    "INSERT INTO scored(targetid, anomaly_score) VALUES (?, ?) "
                    "ON CONFLICT(targetid) DO UPDATE SET anomaly_score=excluded.anomaly_score",
                    rows,
                )
        threshold = float(contract["calibration"].get("selection_threshold", 5.0))
        unique_rows = connection.execute("SELECT COUNT(*) FROM scored").fetchone()[0]
        threshold_rows = connection.execute(
            "SELECT COUNT(*) FROM scored WHERE anomaly_score > ?", (threshold,)
        ).fetchone()[0]
        summary = {
            "summary_version": 1,
            "generation_id": f"clean-rerun-{payload_sha256(contract)[:12]}",
            "contract_sha256": payload_sha256(contract),
            "deduplication": contract["deduplication"],
            "raw_rows": raw_rows,
            "unique_targetids": unique_rows,
            "duplicate_rows_removed": raw_rows - unique_rows,
            "threshold": threshold,
            "threshold_count_after_dedup": threshold_rows,
            "comparison_policy": contract["comparison_policy"],
        }
    finally:
        connection.close()
    write_json_atomic(output_path, summary)
    return summary


def compare_generations(summary_path: Path, output_path: Path) -> dict[str, Any]:
    summary = read_json(summary_path)
    if "threshold_count_after_dedup" not in summary or "generation_id" not in summary:
        raise ContractError("new-generation summary is incomplete")
    comparison = {
        "comparison_version": 1,
        "policy": "separate_generations_only_no_count_targeting_or_merging",
        "new_generation": {
            "generation_id": summary["generation_id"],
            "threshold_count_after_dedup": summary["threshold_count_after_dedup"],
            "threshold": summary["threshold"],
            "contract_sha256": summary["contract_sha256"],
        },
        "historical_generations": HISTORICAL_GENERATIONS,
    }
    write_json_atomic(output_path, comparison)
    return comparison


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description=__doc__)
    subcommands = command.add_subparsers(dest="command", required=True)
    build = subcommands.add_parser("build-contract", help="bind model, code, inputs, and calibration")
    build.add_argument("--model", type=Path, required=True)
    build.add_argument("--inference-code", type=Path, required=True)
    build.add_argument("--input-manifest", type=Path, required=True)
    build.add_argument("--calibration", type=Path, required=True)
    build.add_argument("--output", type=Path, required=True)
    receipt = subcommands.add_parser("record-receipt", help="write a verified per-shard receipt")
    receipt.add_argument("--contract", type=Path, required=True)
    receipt.add_argument("--shard", type=Path, required=True)
    receipt.add_argument("--receipt-dir", type=Path, required=True)
    receipt.add_argument("--checkpoint", type=Path, required=True)
    verify = subcommands.add_parser("verify-receipts", help="re-hash all scored shards")
    verify.add_argument("--contract", type=Path, required=True)
    verify.add_argument("--shard-dir", type=Path, required=True)
    verify.add_argument("--receipt-dir", type=Path, required=True)
    summarize = subcommands.add_parser("summarize-after-dedup", help="deduplicate then count")
    summarize.add_argument("--contract", type=Path, required=True)
    summarize.add_argument("--shard-dir", type=Path, required=True)
    summarize.add_argument("--receipt-dir", type=Path, required=True)
    summarize.add_argument("--sqlite", type=Path, required=True)
    summarize.add_argument("--output", type=Path, required=True)
    compare = subcommands.add_parser("compare-generations", help="label historical counts without merging")
    compare.add_argument("--new-summary", type=Path, required=True)
    compare.add_argument("--output", type=Path, required=True)
    return command


def main() -> None:
    args = parser().parse_args()
    if args.command == "build-contract":
        write_json_atomic(args.output, build_contract(args.model, args.inference_code, args.input_manifest, args.calibration))
    elif args.command == "record-receipt":
        print(record_receipt(args.contract, args.shard, args.receipt_dir, args.checkpoint))
    elif args.command == "verify-receipts":
        print(f"verified {len(verify_receipts(args.contract, args.shard_dir, args.receipt_dir))} shard(s)")
    elif args.command == "summarize-after-dedup":
        print(json.dumps(summarize_after_dedup(args.contract, args.shard_dir, args.receipt_dir, args.sqlite, args.output), indent=2))
    elif args.command == "compare-generations":
        print(json.dumps(compare_generations(args.new_summary, args.output), indent=2))


if __name__ == "__main__":
    main()

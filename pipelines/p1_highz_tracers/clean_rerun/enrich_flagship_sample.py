#!/usr/bin/env python3
"""Phase-3b flagship sample enrichment: per-band SNR + latents, MSE-verified.

The AUG-011 `run_scan.py` shard schema is deliberately narrow —
`targetid`/`anomaly_score`/`mean_mse`/`healpix`/`survey`/`program` only (see
`run_scan.py`'s own docstring and `build_flagship_sample.py`'s
"Historical-tooling gap" note) — because scoring all ~28M spectra and
carrying the historical 45-column-per-row payload for every one of them was
never affordable. But the SELECTED flagship sample (`build_flagship_sample.py`'s
output — thousands of rows, not 28M) is small enough that the richer
per-object features the historical `enhanced_18M_inference.py` pipeline
computed (per-band residuals/SNRs, worst band, peak residual wavelength,
kurtosis, redrock columns when available, and the 128-dim BigAE latent
vector) are affordable to recompute for exactly those rows.

This script re-downloads, ONE TIME PER `(survey, program, healpix)` GROUP
touched by the selected sample, the same coadd FITS files `run_scan.py`
scored, re-runs them through the SAME archived, contract-bound inference
path (`outputs/enhanced_18M/enhanced_18M_inference.py`'s `process_healpix()`,
imported unmodified — never copied or re-derived), keeps ONLY the rows whose
TARGETID is in the selected sample, and emits one enriched Parquet: every
sample column plus everything `process_healpix()`'s row dict emits (except
`targetid`, already present, and `anomaly_score`, which in that dict means
the RAW per-spectrum mean MSE — a different quantity from the sample's own
`anomaly_score` column, the SEALED z-score; see the cross-check gate below
for what the raw value is used for instead of being copied into the output
under a colliding name). The archived module's `lat_000..lat_127` latent
columns are carried through renamed to `latent_000..latent_127` — this is
the ONLY renaming this script performs; every other archived field name is
carried through verbatim. `process_healpix()` is invoked with
`redrock_path=None`, exactly as `run_scan.py` does, so the redrock-only
fields (`z`, `zerr`, `zwarn`, `spectype`, `subtype`, `deltachi2`) are carried
through at their documented defaults (NaN / -1 / '' — see
`enhanced_18M_inference.py`'s `process_healpix` docstring) rather than
fabricated from a source this script never opens.

Cross-check gate (why this script is trustworthy, not just convenient):
`process_healpix()`'s `anomaly_score` field for a given TARGETID is defined,
per `run_scan.py`'s own module docstring, as the RAW per-spectrum mean MSE —
the exact same quantity the scan shard's `mean_mse` column already carries
for that TARGETID (before the calibration z-score transform). Recomputing it
here and requiring it to reproduce the sample's `mean_mse` to within
`MSE_RELATIVE_TOLERANCE` (1e-6 relative) for EVERY enriched row is a
strong, cheap proof that this script's downsampling/normalization/model
forward pass are bit-for-bit the same arithmetic the original scan used —
not a re-implementation that merely looks similar. Any row failing the
tolerance is collected (never just the first one) and the run fails closed,
listing every offender, before any final output is written.

Fault barrier (per `(survey, program, healpix)` group, mirroring
`run_scan.py`'s pattern exactly): a transient failure (archive outage,
partial download, scoring I/O error) skips that group with an audit line
instead of killing the whole run. A per-group Parquet shard + a
contract/sample-bound JSON checkpoint make reruns resumable — an already-
checkpointed group's coadd is never re-downloaded. The FINAL merged
`--output`/`--manifest-output` is written ONLY when zero groups are
skipped in that incarnation (a partial merge would silently under-represent
the sample) — otherwise the run exits nonzero (3) so a supervisor retries.

Downloaded coadd files are deleted immediately after each group is scored,
exactly like `run_scan.py`, so local disk never needs to hold more than a
handful of coadd files at once regardless of how many groups the sample
spans.
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
from derive_locator_inventory import (  # noqa: E402
    coadd_relative_path,
    read_json,
    require_sha,
    sha256_file,
    write_json_atomic,
    verify_zcatalog_checksum,
)
from build_calibration import (  # noqa: E402
    ARCHIVED_INFERENCE_PATH,
    load_archived_inference_module,
    load_model,
)

REPO_ROOT = Path(__file__).resolve().parents[3]
CONTRACT_MODULE_PATH = REPO_ROOT / "pipelines/p1_highz_tracers/clean_rerun_contract.py"
DESI_HEALPIX_BASE_URL = "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/"

# `(per_spectrum_mean_mse_recomputed - sample_mean_mse) / |sample_mean_mse|`
# must not exceed this for ANY enriched row, or the run fails closed.
MSE_RELATIVE_TOLERANCE = 1e-6

# Fields in `process_healpix()`'s row dict that are deliberately NOT carried
# into the enriched output under their archived names: `targetid` is already
# a sample column, and `anomaly_score` there means the RAW per-spectrum mean
# MSE (used only for the cross-check gate below) — copying it verbatim would
# silently collide with and overwrite the sample's own `anomaly_score`
# column, which is the SEALED calibration z-score, a different quantity.
EXCLUDED_ARCHIVED_ROW_FIELDS = {"targetid", "anomaly_score"}
ARCHIVED_LATENT_PREFIX = "lat_"
OUTPUT_LATENT_PREFIX = "latent_"

# The exact sample-column schema `build_flagship_sample.py` writes.
SAMPLE_COLUMNS = ["targetid", "anomaly_score", "mean_mse", "survey", "program", "healpix"]

# Output columns known to need a non-float64 Arrow type; anything else in an
# enriched row is written as float64. Kept as an explicit allow-list (not
# derived from process_healpix's output) so a type mismatch fails loudly at
# write time rather than silently coercing a numeric column to a string.
STRING_COLUMNS = {
    "survey",
    "program",
    "worst_band",
    "spectype",
    "subtype",
    "morphtype",
    "classification",
    "discovery_potential",
}
INT_COLUMNS = {"targetid", "healpix", "zwarn", "coadd_numexp"}
BOOL_COLUMNS = {"is_point_source", "is_star_candidate"}


class EnrichmentError(RuntimeError):
    """Raised when enrichment inputs cannot be trusted or produced safely."""


def load_contract_module(path: Path = CONTRACT_MODULE_PATH) -> types.ModuleType:
    """Import `clean_rerun_contract.py` unmodified, by exact file path."""
    spec = importlib.util.spec_from_file_location("clean_rerun_contract_bound", path)
    if spec is None or spec.loader is None:
        raise EnrichmentError(f"cannot load contract module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_input_sample(sample_path: Path, sample_manifest: dict[str, Any]) -> None:
    if not sample_path.is_file():
        raise EnrichmentError(f"input sample is absent: {sample_path}")
    expected = sample_manifest.get("output", {}).get("sha256")
    require_sha(expected, "sample manifest output.sha256")
    observed = sha256_file(sample_path)
    if observed != expected:
        raise EnrichmentError(
            f"input sample SHA-256 mismatch: expected {expected}, got {observed} for {sample_path}"
        )


def verify_sample_matches_contract(
    contract_module: types.ModuleType, contract: dict[str, Any], sample_manifest: dict[str, Any]
) -> str:
    """Fail closed unless the sample manifest was produced against THIS exact contract."""
    expected = contract_module.payload_sha256(contract)
    observed = sample_manifest.get("parent", {}).get("contract_sha256")
    if observed != expected:
        raise EnrichmentError(
            f"sample manifest parent.contract_sha256 mismatch: expected {expected}, got {observed!r} "
            "(sample was built against a different contract; refusing to enrich)"
        )
    return expected


def load_sample_rows(sample_path: Path) -> list[dict[str, Any]]:
    import pyarrow.parquet as pq

    table = pq.read_table(sample_path, columns=SAMPLE_COLUMNS)
    rows = table.to_pylist()
    if not rows:
        raise EnrichmentError(f"selected sample has zero rows: {sample_path}")
    return rows


def group_sample_rows(rows: list[dict[str, Any]]) -> dict[tuple[str, str, int], list[dict[str, Any]]]:
    grouped: dict[tuple[str, str, int], list[dict[str, Any]]] = {}
    for row in rows:
        key = (row["survey"], row["program"], int(row["healpix"]))
        grouped.setdefault(key, []).append(row)
    return grouped


def shard_name(survey: str, program: str, healpix: int) -> str:
    return f"enriched-{survey}-{program}-{healpix}.parquet"


def load_checkpoint(checkpoint_path: Path, input_sample_sha256: str, contract_sha256: str) -> dict[str, Any]:
    if not checkpoint_path.exists():
        return {
            "checkpoint_version": 1,
            "input_sample_sha256": input_sample_sha256,
            "contract_sha256": contract_sha256,
            "completed_groups": [],
        }
    checkpoint = read_json(checkpoint_path)
    if checkpoint.get("input_sample_sha256") != input_sample_sha256:
        raise EnrichmentError(
            f"checkpoint is bound to a different input sample (expected {input_sample_sha256}, "
            f"got {checkpoint.get('input_sample_sha256')!r}); refusing resume: {checkpoint_path}"
        )
    if checkpoint.get("contract_sha256") != contract_sha256:
        raise EnrichmentError(
            f"checkpoint is bound to a different contract (expected {contract_sha256}, "
            f"got {checkpoint.get('contract_sha256')!r}); refusing resume: {checkpoint_path}"
        )
    return checkpoint


def append_audit_line(audit_log_path: Path, record: dict[str, Any]) -> None:
    """Append one JSON line to the enrichment audit log (never overwrite/truncate)."""
    audit_log_path.parent.mkdir(parents=True, exist_ok=True)
    with audit_log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True, separators=(",", ":"), default=str))
        handle.write("\n")


def rename_archived_field(key: str) -> str:
    if key.startswith(ARCHIVED_LATENT_PREFIX):
        return OUTPUT_LATENT_PREFIX + key[len(ARCHIVED_LATENT_PREFIX) :]
    return key


def enrich_group(
    inference_module: types.ModuleType,
    model: Any,
    device: Any,
    coadd_path: Path,
    group_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Score one downloaded coadd via the archived `process_healpix()`, keep
    ONLY the sample's targetids for this group, and attach the cross-check
    fields (`_recomputed_mean_mse`, `_mse_relative_error`) every enriched row
    carries until the final merge gate has consumed them."""
    _n_obj, rows = inference_module.process_healpix(str(coadd_path), None, model, device)
    row_by_targetid = {int(row["targetid"]): row for row in rows}

    enriched: list[dict[str, Any]] = []
    for sample_row in group_rows:
        targetid = int(sample_row["targetid"])
        if targetid not in row_by_targetid:
            raise EnrichmentError(
                f"sample targetid {targetid} not found in downloaded coadd {coadd_path.name}; "
                "sample and coadd are not provenance-consistent for this group"
            )
        archived_row = row_by_targetid[targetid]
        recomputed_mean_mse = float(archived_row["anomaly_score"])
        sample_mean_mse = float(sample_row["mean_mse"])
        denominator = abs(sample_mean_mse) if abs(sample_mean_mse) > 1e-300 else 1e-300
        relative_error = abs(recomputed_mean_mse - sample_mean_mse) / denominator

        record: dict[str, Any] = dict(sample_row)
        for key, value in archived_row.items():
            if key in EXCLUDED_ARCHIVED_ROW_FIELDS:
                continue
            record[rename_archived_field(key)] = value
        record["_recomputed_mean_mse"] = recomputed_mean_mse
        record["_mse_relative_error"] = relative_error
        enriched.append(record)
    return enriched


def _arrow_array_for_column(name: str, values: list[Any]):
    import pyarrow as pa

    if name in STRING_COLUMNS:
        return pa.array([str(v) for v in values], type=pa.string())
    if name in INT_COLUMNS:
        return pa.array([int(v) for v in values], type=pa.int64())
    if name in BOOL_COLUMNS:
        return pa.array([bool(v) for v in values], type=pa.bool_())
    return pa.array([float(v) for v in values], type=pa.float64())


def write_group_shard(enriched_rows: list[dict[str, Any]], survey: str, program: str, healpix: int, shard_dir: Path) -> Path:
    import pyarrow as pa
    import pyarrow.parquet as pq

    shard_dir.mkdir(parents=True, exist_ok=True)
    path = shard_dir / shard_name(survey, program, healpix)
    columns = list(enriched_rows[0].keys())
    table = pa.table(
        {column: _arrow_array_for_column(column, [row[column] for row in enriched_rows]) for column in columns}
    )
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    pq.write_table(table, tmp_path, compression="zstd")
    os.replace(tmp_path, path)
    return path


def run_enrichment(
    sample_path: Path,
    sample_manifest_path: Path,
    contract_path: Path,
    model_path: Path,
    zcatalog_path: Path,
    coadd_cache_dir: Path,
    shard_dir: Path,
    checkpoint_path: Path,
    audit_log_path: Path,
    output_path: Path,
    manifest_output_path: Path,
    base_url: str = DESI_HEALPIX_BASE_URL,
    inference_module: types.ModuleType | None = None,
) -> dict[str, Any]:
    import pyarrow.parquet as pq
    import torch

    contract_module = load_contract_module()
    contract = contract_module.read_json(contract_path)
    contract_module.verify_contract(contract)

    sample_manifest = read_json(sample_manifest_path)
    verify_input_sample(sample_path, sample_manifest)
    contract_sha256 = verify_sample_matches_contract(contract_module, contract, sample_manifest)

    # The zcatalog is SHA-verified against the exact catalog this contract's
    # input manifest is bound to, AND against the sample manifest's own
    # record of which catalog its targetids were vouched against — a run
    # against the "right" contract but a swapped zcatalog file fails closed.
    verify_zcatalog_checksum(zcatalog_path, contract["input_manifest"])
    sample_catalog_sha256 = sample_manifest.get("parent", {}).get("catalog_sha256")
    if sample_catalog_sha256 != contract["input_manifest"]["catalog_sha256"]:
        raise EnrichmentError(
            "sample manifest parent.catalog_sha256 does not match the contract's own "
            "input_manifest.catalog_sha256; sample and contract disagree about the source zcatalog"
        )

    observed_model_sha256 = sha256_file(model_path)
    if observed_model_sha256 != contract["model"]["sha256"]:
        raise EnrichmentError(
            f"model SHA-256 mismatch: contract expects {contract['model']['sha256']}, "
            f"got {observed_model_sha256} for {model_path}"
        )
    observed_inference_sha256 = sha256_file(ARCHIVED_INFERENCE_PATH)
    if observed_inference_sha256 != contract["inference_code"]["sha256"]:
        raise EnrichmentError(
            "inference-code SHA-256 mismatch: contract expects "
            f"{contract['inference_code']['sha256']}, got {observed_inference_sha256}"
        )

    input_sample_sha256 = sha256_file(sample_path)
    sample_rows = load_sample_rows(sample_path)
    grouped = group_sample_rows(sample_rows)
    total_sample_rows = len(sample_rows)

    checkpoint = load_checkpoint(checkpoint_path, input_sample_sha256, contract_sha256)
    completed_keys = {tuple(entry["group"]) for entry in checkpoint["completed_groups"]}

    coadd_cache_dir.mkdir(parents=True, exist_ok=True)
    shard_dir.mkdir(parents=True, exist_ok=True)

    module = inference_module if inference_module is not None else load_archived_inference_module()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = load_model(module, model_path, device)

    skipped_groups = 0
    for (survey, program, healpix), group_rows in sorted(grouped.items()):
        key = (survey, program, healpix)
        if key in completed_keys:
            continue

        relative = coadd_relative_path(survey, program, healpix)
        coadd_url = base_url + relative[len("healpix/") :]
        coadd_fname = Path(relative).name
        coadd_path = coadd_cache_dir / coadd_fname

        # Per-group fault isolation, mirroring run_scan.py exactly: any
        # failure skips the group with an audit line instead of aborting
        # the whole run; a skipped group has no checkpoint entry, so a
        # later incarnation retries it.
        try:
            ok = module.download_file(coadd_url, str(coadd_path))
            if not ok:
                raise EnrichmentError(f"download failed after retries: {coadd_url}")
            try:
                enriched_rows = enrich_group(module, model, device, coadd_path, group_rows)
                shard_path = write_group_shard(enriched_rows, survey, program, healpix, shard_dir)
            finally:
                if coadd_path.exists():
                    coadd_path.unlink()
            append_audit_line(
                audit_log_path,
                {
                    "survey": survey,
                    "program": program,
                    "healpix": healpix,
                    "sample_rows_enriched": len(enriched_rows),
                    "shard": shard_path.name,
                },
            )
        except Exception as exc:  # noqa: BLE001 — deliberate per-group fault barrier
            skipped_groups += 1
            append_audit_line(
                audit_log_path,
                {
                    "survey": survey,
                    "program": program,
                    "healpix": healpix,
                    "group_error": f"{type(exc).__name__}: {exc}"[:400],
                    "coadd_url": coadd_url,
                },
            )
            print(f"SKIP ({type(exc).__name__}, will retry next incarnation): {coadd_url}", flush=True)
            continue

        checkpoint["completed_groups"].append(
            {"group": [survey, program, healpix], "shard": shard_path.name, "row_count": len(enriched_rows)}
        )
        write_json_atomic(checkpoint_path, checkpoint)
        completed_keys.add(key)

    if skipped_groups:
        print(
            f"{skipped_groups} group(s) skipped on download/scoring failure — exiting for retry; "
            "no final output written this incarnation",
            flush=True,
        )
        return {
            "status": "incomplete",
            "skipped_groups": skipped_groups,
            "completed_groups": len(checkpoint["completed_groups"]),
            "total_groups": len(grouped),
        }

    # Every group in the sample is now checkpointed (this incarnation or a
    # prior one). Re-read every completed group's shard from disk — cheap,
    # no network — and run the MSE cross-check gate over EVERY enriched row
    # before writing anything final, listing every offender rather than
    # failing on the first one.
    merged_rows: list[dict[str, Any]] = []
    offenders: list[dict[str, Any]] = []
    for entry in checkpoint["completed_groups"]:
        shard_path = shard_dir / entry["shard"]
        for row in pq.read_table(shard_path).to_pylist():
            if row["_mse_relative_error"] > MSE_RELATIVE_TOLERANCE:
                offenders.append(
                    {
                        "targetid": row["targetid"],
                        "sample_mean_mse": row["mean_mse"],
                        "recomputed_mean_mse": row["_recomputed_mean_mse"],
                        "relative_error": row["_mse_relative_error"],
                    }
                )
            merged_rows.append(row)

    if offenders:
        append_audit_line(
            audit_log_path,
            {"mse_cross_check_gate": "FAILED", "n_offenders": len(offenders), "offenders": offenders},
        )
        preview = offenders[:5]
        raise EnrichmentError(
            f"MSE cross-check gate failed for {len(offenders)} of {len(merged_rows)} enriched row(s) "
            f"(tolerance={MSE_RELATIVE_TOLERANCE:g} relative); full list in {audit_log_path}. "
            f"First offender(s): {preview}"
        )

    if len(merged_rows) != total_sample_rows:
        raise EnrichmentError(
            f"merged enriched row count ({len(merged_rows)}) does not match the selected sample's "
            f"row count ({total_sample_rows}); internal consistency failure — refusing to write output"
        )

    merged_rows.sort(key=lambda row: int(row["targetid"]))
    final_rows = [{k: v for k, v in row.items() if not k.startswith("_")} for row in merged_rows]

    import pyarrow as pa

    columns = list(final_rows[0].keys())
    for row in final_rows[1:]:
        if list(row.keys()) != columns:
            raise EnrichmentError("enriched rows have inconsistent schemas across groups; refusing to write output")
    table = pa.table(
        {column: _arrow_array_for_column(column, [row[column] for row in final_rows]) for column in columns}
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_output = output_path.with_suffix(output_path.suffix + ".tmp")
    pq.write_table(table, tmp_output, compression="zstd")
    os.replace(tmp_output, output_path)
    output_sha256 = sha256_file(output_path)

    manifest = {
        "manifest_version": "flagship-enrichment/v1",
        "input_sample_sha256": input_sample_sha256,
        "contract_sha256": contract_sha256,
        "model_sha256": observed_model_sha256,
        "inference_code_sha256": observed_inference_sha256,
        "zcatalog_sha256": sample_catalog_sha256,
        "mse_cross_check": {
            "tolerance_relative": MSE_RELATIVE_TOLERANCE,
            "rows_checked": len(merged_rows),
            "offenders": 0,
            "passed": True,
        },
        "row_counts": {
            "input_sample_rows": total_sample_rows,
            "output_rows": len(final_rows),
        },
        "groups": {
            "total": len(grouped),
            "completed": len(checkpoint["completed_groups"]),
            "skipped": 0,
        },
        "output": {
            "file_name": output_path.name,
            "byte_size": output_path.stat().st_size,
            "sha256": output_sha256,
            "columns": columns,
        },
    }
    write_json_atomic(manifest_output_path, manifest)
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--sample", type=Path, required=True, help="build_flagship_sample.py's selected-sample Parquet")
    parser.add_argument("--sample-manifest", type=Path, required=True, help="build_flagship_sample.py's output manifest")
    parser.add_argument("--contract", type=Path, required=True, help="sealed run-contract.json")
    parser.add_argument("--model", type=Path, required=True, help="best_model_47k.pt on this pod")
    parser.add_argument("--zcatalog", type=Path, required=True, help="SHA-verified zall-pix-iron.fits")
    parser.add_argument("--coadd-cache-dir", type=Path, required=True)
    parser.add_argument("--shard-dir", type=Path, required=True, help="per-group intermediate enriched Parquet shards")
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--audit-log", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="final enriched Parquet (written only when zero groups skipped)")
    parser.add_argument("--manifest-output", type=Path, required=True)
    parser.add_argument("--base-url", type=str, default=DESI_HEALPIX_BASE_URL)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    result = run_enrichment(
        args.sample,
        args.sample_manifest,
        args.contract,
        args.model,
        args.zcatalog,
        args.coadd_cache_dir,
        args.shard_dir,
        args.checkpoint,
        args.audit_log,
        args.output,
        args.manifest_output,
        base_url=args.base_url,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    if result.get("status") == "incomplete":
        raise SystemExit(3)


if __name__ == "__main__":
    main()

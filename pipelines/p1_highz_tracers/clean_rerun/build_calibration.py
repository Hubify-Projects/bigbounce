#!/usr/bin/env python3
"""Pod-side calibration fitter for the DESI DR1 clean-rerun BigAE score.

Design: `held_out_training_validation_split`
---------------------------------------------
The archived model's original training corpus is absent (see
`project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`, "Restoration
gate result"), so `clean_rerun_contract.py`'s required calibration
`fit_scope: "held_out_training_validation_split"` is implemented here as a
FRESH two-way split of a deterministic seeded sample drawn from the already
SHA-256-verified DR1 iron zcatalog — it is NOT a recovery of the historical
training/validation split, which is unrecoverable.

  1. Draw 40,000 row indices from the zcatalog with
     `numpy.random.Generator(numpy.random.PCG64(seed=20260804))` via
     `rng.choice(n_rows, size=40_000, replace=False)`, i.e. a uniform sample
     without replacement over zcatalog rows (not unique TARGETID values —
     DESI TARGETIDs can repeat across surveys/programs, and row-level
     sampling over the frozen zcatalog is the reproducible, fully
     seed-determined choice).
  2. The FIRST 20,000 drawn indices (in draw order, not re-sorted) become
     the calibration-fit set — this script's "training manifest".
  3. The LAST 20,000 drawn indices become the held-out validation set —
     this script's "validation manifest".
  4. Both sets are scored through the archived inference path by importing
     `outputs/enhanced_18M/enhanced_18M_inference.py` and calling its own
     `BigAE`, `downsample()`, and `process_healpix()` (which performs the
     per-spectrum median-|flux| normalization: `med = median(|flux|, axis=1)`,
     `X = clip(flux / med, -10, 10)`) on each coadd FITS file that contains a
     sampled TARGETID, then selecting only the sampled rows out of that
     healpix group's output. Nothing about the archived scoring arithmetic
     is reimplemented here — only imported and sliced. The archived
     `process_healpix()`'s `anomaly_score` field IS the raw per-spectrum
     mean MSE over the 496 normalized bins used below as `raw_mse`.
  5. `mse_mean`/`mse_std` are sealed from the FIT set only (sample std,
     ddof=1). The VALIDATION set's mean/std are computed and reported
     alongside as a stability check. Sealing is REFUSED unless

         |validation_mse_mean - mse_mean| <= 5 * (mse_std / sqrt(n_fit))

     i.e. the validation-set mean must fall within 5 standard errors of the
     fit-set mean (treating `mse_std / sqrt(n_fit)` as the standard error of
     the fit mean). This is a coarse compatibility check, not a claim of a
     precise statistical test: the two sets are drawn from the same
     underlying zcatalog population by construction, so a large deviation
     signals a download/scoring bug, a bad healpix join, or a badly
     non-stationary population — any of which should block sealing.

The written `calibration.json` binds:
  - the two manifests (JSON files listing the drawn TARGETIDs, in draw
    order, with their survey/program/healpix) by SHA-256
    (`training_manifest_sha256`, `validation_manifest_sha256`);
  - this file's own SHA-256 at run time (`fit_code_sha256`);
  - `score_definition`: "mean_mse_over_per_spectrum_median_abs_flux_normalized_496_bins";
  - `fit_scope`: "held_out_training_validation_split";
  - `selection_threshold`: 5.0;
  - `anomaly_score_definition`: "(per_spectrum_mean_mse - mse_mean) / mse_std",
    implemented here as `anomaly_score_from_calibration()` and reused
    verbatim by `run_scan.py`.

This script downloads DESI DR1 coadd FITS files over the network and loads
the archived model checkpoint; it is meant to run on the pod, never inside
an offline unit test. `tests/test_clean_rerun_campaign.py` exercises only
the pure, network-free pieces: the seeded split and the anomaly-score
arithmetic (against the real archived `BigAE` class with a fixed-seed
state dict).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
import types
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derive_locator_inventory import (  # noqa: E402
    require_sha,
    sha256_file,
    read_json,
    write_json_atomic,
    verify_zcatalog_checksum,
    find_catalog_hdu,
    decode_fits_str,
    LocatorDerivationError,
)

SEED = 20260804
N_TOTAL_SAMPLE = 40_000
N_FIT = 20_000
STABILITY_SIGMA_MULTIPLIER = 5.0
SCORE_DEFINITION = "mean_mse_over_per_spectrum_median_abs_flux_normalized_496_bins"
FIT_SCOPE = "held_out_training_validation_split"
SELECTION_THRESHOLD = 5.0
ANOMALY_SCORE_DEFINITION = "(per_spectrum_mean_mse - mse_mean) / mse_std"

REPO_ROOT = Path(__file__).resolve().parents[3]
ARCHIVED_INFERENCE_PATH = REPO_ROOT / "pipelines/p1_highz_tracers/outputs/enhanced_18M/enhanced_18M_inference.py"
DESI_HEALPIX_BASE_URL = "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/"


class CalibrationError(RuntimeError):
    """Raised when calibration inputs cannot be trusted or the fit is unstable."""


def load_archived_inference_module(path: Path = ARCHIVED_INFERENCE_PATH) -> types.ModuleType:
    """Import `enhanced_18M_inference.py` unmodified, by exact file path.

    This is the ONLY sanctioned way to get BigAE/downsample/process_healpix
    into this script — never re-typed, never re-derived.
    """
    spec = importlib.util.spec_from_file_location("enhanced_18M_inference_archived", path)
    if spec is None or spec.loader is None:
        raise CalibrationError(f"cannot load archived inference module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def draw_seeded_indices(n_rows: int, seed: int = SEED, n_total: int = N_TOTAL_SAMPLE) -> np.ndarray:
    """Deterministically draw `n_total` distinct row indices from `n_rows`."""
    if n_total > n_rows:
        raise CalibrationError(f"cannot draw {n_total} targets from a zcatalog with only {n_rows} rows")
    rng = np.random.Generator(np.random.PCG64(seed))
    return rng.choice(n_rows, size=n_total, replace=False)


def split_fit_validation(indices: np.ndarray, n_fit: int = N_FIT) -> tuple[np.ndarray, np.ndarray]:
    """Split drawn indices into the first-`n_fit` fit set and the remaining validation set."""
    return indices[:n_fit], indices[n_fit:]


def anomaly_score_from_calibration(raw_mse: float, mse_mean: float, mse_std: float) -> float:
    """`anomaly_score = (per_spectrum_mean_mse - mse_mean) / mse_std`."""
    return (raw_mse - mse_mean) / mse_std


def gather_targets(zcatalog_path: Path, indices: np.ndarray) -> list[dict[str, Any]]:
    """Read TARGETID/SURVEY/PROGRAM/HEALPIX for exactly the sampled rows.

    Memory-bounded: only `len(indices)` rows are ever materialized, never
    the full zcatalog column.
    """
    from astropy.io import fits

    with fits.open(zcatalog_path, memmap=True) as hdul:
        hdu = find_catalog_hdu(hdul)
        data = hdu.data
        targetid_sel = data["TARGETID"][indices]
        survey_sel = data["SURVEY"][indices]
        program_sel = data["PROGRAM"][indices]
        healpix_sel = data["HEALPIX"][indices]
    targets = []
    for targetid_raw, survey_raw, program_raw, healpix_raw in zip(
        targetid_sel, survey_sel, program_sel, healpix_sel
    ):
        targets.append(
            {
                "targetid": int(targetid_raw),
                "survey": decode_fits_str(survey_raw),
                "program": decode_fits_str(program_raw),
                "healpix": int(healpix_raw),
            }
        )
    return targets


def write_manifest(targets: list[dict[str, Any]], seed: int, role: str, output_path: Path) -> Path:
    payload = {
        "manifest_role": role,
        "seed": seed,
        "count": len(targets),
        "targets": targets,
    }
    write_json_atomic(output_path, payload)
    return output_path


def score_targets(
    module: types.ModuleType,
    model: Any,
    device: Any,
    targets: list[dict[str, Any]],
    coadd_cache_dir: Path,
    base_url: str = DESI_HEALPIX_BASE_URL,
) -> dict[int, float]:
    """Download each distinct (survey, program, healpix) coadd once, score
    it through the archived `process_healpix()`, and return raw per-spectrum
    mean MSE keyed by TARGETID for every requested target."""
    coadd_cache_dir.mkdir(parents=True, exist_ok=True)
    groups: dict[tuple[str, str, int], list[int]] = {}
    for target in targets:
        key = (target["survey"], target["program"], target["healpix"])
        groups.setdefault(key, []).append(target["targetid"])

    scores: dict[int, float] = {}
    for (survey, program, healpix), wanted_targetids in sorted(groups.items()):
        coadd_fname = f"coadd-{survey}-{program}-{healpix}.fits"
        dir_url = f"{base_url}{survey}/{program}/{healpix // 100}/{healpix}/"
        coadd_url = dir_url + coadd_fname
        coadd_path = coadd_cache_dir / coadd_fname
        ok = module.download_file(coadd_url, str(coadd_path))
        if not ok:
            raise CalibrationError(f"failed to download coadd for calibration sampling: {coadd_url}")
        try:
            _n_obj, rows = module.process_healpix(str(coadd_path), None, model, device)
        finally:
            if coadd_path.exists():
                coadd_path.unlink()
        row_by_targetid = {row["targetid"]: row["anomaly_score"] for row in rows}
        for targetid in wanted_targetids:
            if targetid not in row_by_targetid:
                raise CalibrationError(
                    f"sampled TARGETID {targetid} not found in downloaded coadd {coadd_fname}"
                )
            scores[targetid] = row_by_targetid[targetid]
    return scores


def load_model(module: types.ModuleType, model_path: Path, device: Any) -> Any:
    import torch

    if not model_path.is_file():
        raise CalibrationError(f"model file is absent: {model_path}")
    model = module.BigAE(n_in=496, n_lat=128).to(device)
    state_dict = torch.load(model_path, map_location=device, weights_only=True)
    model.load_state_dict(state_dict)
    model.eval()
    return model


def build_calibration(
    zcatalog_path: Path,
    manifest_path: Path,
    model_path: Path,
    coadd_cache_dir: Path,
    training_manifest_output: Path,
    validation_manifest_output: Path,
    output_path: Path,
) -> dict[str, Any]:
    import torch

    manifest = read_json(manifest_path)
    verify_zcatalog_checksum(zcatalog_path, manifest)

    from astropy.io import fits

    with fits.open(zcatalog_path, memmap=True) as hdul:
        hdu = find_catalog_hdu(hdul)
        n_rows = len(hdu.data)

    drawn = draw_seeded_indices(n_rows, seed=SEED, n_total=N_TOTAL_SAMPLE)
    fit_idx, val_idx = split_fit_validation(drawn, n_fit=N_FIT)

    fit_targets = gather_targets(zcatalog_path, fit_idx)
    val_targets = gather_targets(zcatalog_path, val_idx)

    write_manifest(fit_targets, SEED, "calibration_fit", training_manifest_output)
    write_manifest(val_targets, SEED, "held_out_validation", validation_manifest_output)

    module = load_archived_inference_module()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = load_model(module, model_path, device)

    all_scores = score_targets(module, model, device, fit_targets + val_targets, coadd_cache_dir)

    fit_scores = np.array([all_scores[t["targetid"]] for t in fit_targets], dtype=np.float64)
    val_scores = np.array([all_scores[t["targetid"]] for t in val_targets], dtype=np.float64)

    fit_mean = float(fit_scores.mean())
    fit_std = float(fit_scores.std(ddof=1))
    if fit_std <= 0:
        raise CalibrationError("fit-set mse_std is not positive; refusing to seal calibration")
    val_mean = float(val_scores.mean())
    val_std = float(val_scores.std(ddof=1))

    standard_error = fit_std / math.sqrt(len(fit_scores))
    stability_bound = STABILITY_SIGMA_MULTIPLIER * standard_error
    deviation = abs(val_mean - fit_mean)
    if deviation > stability_bound:
        raise CalibrationError(
            "validation mean deviates from fit mean by "
            f"{deviation:.6g}, exceeding the stability bound {stability_bound:.6g} "
            f"(5 * fit_std/sqrt(N)); refusing to seal calibration"
        )

    fit_code_sha256 = sha256_file(Path(__file__).resolve())
    calibration = {
        "artifact_version": "desi-bigae-calibration/v1",
        "status": "sealed",
        "score_definition": SCORE_DEFINITION,
        "fit_scope": FIT_SCOPE,
        "selection_threshold": SELECTION_THRESHOLD,
        "anomaly_score_definition": ANOMALY_SCORE_DEFINITION,
        "mse_mean": fit_mean,
        "mse_std": fit_std,
        "n_fit": len(fit_scores),
        "n_validation": len(val_scores),
        "validation_mse_mean": val_mean,
        "validation_mse_std": val_std,
        "stability_check": {
            "rule": "abs(validation_mse_mean - mse_mean) <= 5 * (mse_std / sqrt(n_fit))",
            "bound": stability_bound,
            "observed_deviation": deviation,
            "passed": True,
        },
        "seed": SEED,
        "training_manifest_sha256": sha256_file(training_manifest_output),
        "validation_manifest_sha256": sha256_file(validation_manifest_output),
        "fit_code_sha256": fit_code_sha256,
        "model_path": str(model_path),
        "zcatalog_path": str(zcatalog_path),
        "created_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }
    write_json_atomic(output_path, calibration)
    return calibration


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zcatalog", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True, help="draft or final manifest carrying catalog_sha256")
    parser.add_argument("--model", type=Path, required=True, default=REPO_ROOT / "best_model_47k.pt")
    parser.add_argument("--coadd-cache-dir", type=Path, required=True)
    parser.add_argument("--training-manifest-output", type=Path, required=True)
    parser.add_argument("--validation-manifest-output", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    calibration = build_calibration(
        args.zcatalog,
        args.manifest,
        args.model,
        args.coadd_cache_dir,
        args.training_manifest_output,
        args.validation_manifest_output,
        args.output,
    )
    print(json.dumps(calibration, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

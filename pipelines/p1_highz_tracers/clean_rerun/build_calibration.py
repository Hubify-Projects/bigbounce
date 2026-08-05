#!/usr/bin/env python3
"""Pod-side calibration fitter for the DESI DR1 clean-rerun BigAE score.

Design: `bounded_two_stage_pps_cluster_sample` (v2)
----------------------------------------------------
The original version of this script (committed 2026-08-04) drew 40,000
*uniform* random row indices directly from the ~23M-row zcatalog via
`rng.choice(n_rows, size=40_000, replace=False)`. Each sampled row forces a
download of its own `(survey, program, healpix)` coadd FITS file, and a
uniform draw of 40,000 rows against ~35,000 total coadd groups hits roughly
two-thirds of every group in the corpus (~24,000 distinct coadds) — i.e.
calibration alone would download nearly the full multi-terabyte DESI DR1
`iron` healpix corpus before the actual scan even starts. That is a
cost-critical bug, not a minor inefficiency, and this version replaces the
sampling design outright.

The fix is a **bounded two-stage PPS (probability-proportional-to-size)
cluster sample** that approximates uniform row inclusion while bounding the
number of distinct coadd files touched:

  1. **Pass 1 (group counts, memory-bounded).** Stream `SURVEY`/`PROGRAM`/
     `HEALPIX` from the zcatalog in fixed-size row chunks (reusing
     `derive_locator_inventory.scan_zcatalog_groups`, the same streaming
     helper the locator-inventory step already uses) to build a per-group
     row COUNT table — `(survey, program, healpix) -> row_count` — over
     every group in the catalog. Row-level indices are never materialized
     here, only a scalar count per group (thousands of entries, not
     millions).
  2. **Stage 2 (PPS group selection).** With
     `numpy.random.Generator(numpy.random.PCG64(seed=20260804))`, select
     `--n-groups` (default 200) distinct groups from the full group table
     without replacement, with selection probability proportional to each
     group's row count: `rng.choice(n_groups_total, size=n_groups,
     replace=False, p=counts / counts.sum())`. This is RNG call #1.
  3. **Stage 3a (row-budget allocation).** Allocate the `--n-rows` budget
     (default 40,000) across the selected groups proportional to each
     group's row count, using largest-remainder rounding so the allocation
     sums to EXACTLY `--n-rows`. If a group's proportional share would
     exceed its actual row count (only possible for small/skewed inputs —
     not expected in production at 200-groups-of-thousands-of-rows-each),
     that group's allocation is capped at its full count and the shortfall
     is redistributed deterministically to the groups with the largest
     remaining spare capacity (descending group size, ascending group
     position on ties). This step consumes no RNG state.
  4. **Pass 2 (selected-group row indices, memory-bounded).** Stream the
     zcatalog a second time, collecting actual row indices ONLY for rows
     belonging to the ~200 groups chosen in stage 2 — the per-row index
     lists for the other ~34,800 groups are never built.
  5. **Stage 3b (within-group sampling).** For each selected group, in
     ascending `(survey, program, healpix)` order, continuing the SAME rng
     from stage 2 (RNG calls #2 through #(1 + n_groups)), draw that group's
     allocated row count without replacement from its pass-2 row-index
     list: `rng.choice(len(group_rows), size=alloc_i, replace=False)`.
  6. **Split.** Concatenate every selected group's sampled rows, then apply
     ONE final seeded permutation with the SAME rng (the last RNG call) —
     `rng.permutation(n_rows)` — before splitting: the FIRST half becomes
     the calibration-fit set ("training manifest"), the LAST half becomes
     the held-out validation set. Because both halves are drawn from the
     same permutation of the same 200-group pixel population, they span the
     same pixel set by construction. This means the stability gate below is
     honestly a **within-pixel-population** compatibility check, not a
     cross-pixel generalization check — it was never a claim of
     out-of-sample generalization even in the original uniform-row design,
     but it is worth stating plainly now that the cluster structure is
     explicit.

  Expected calibration download under this design: ~200 coadd files
  (~25 GB at typical DESI DR1 coadd sizes), versus ~24,000 files
  (multi-terabyte) under the original naive uniform-row design it replaces.

  Both sets are then scored through the archived inference path by
  importing `outputs/enhanced_18M/enhanced_18M_inference.py` and calling its
  own `BigAE`, `downsample()`, and `process_healpix()` (which performs the
  per-spectrum median-|flux| normalization: `med = median(|flux|, axis=1)`,
  `X = clip(flux / med, -10, 10)`) on each coadd FITS file that contains a
  sampled TARGETID, then selecting only the sampled rows out of that
  healpix group's output. Nothing about the archived scoring arithmetic is
  reimplemented here — only imported and sliced. The archived
  `process_healpix()`'s `anomaly_score` field IS the raw per-spectrum mean
  MSE over the 496 normalized bins used below as `raw_mse`.

  `mse_mean`/`mse_std` are sealed from the FIT set only (sample std,
  ddof=1). The VALIDATION set's mean/std are computed and reported
  alongside as a stability check. Sealing is REFUSED unless

      |validation_mse_mean - mse_mean| <= 5 * (mse_std / sqrt(n_fit))

  i.e. the validation-set mean must fall within 5 standard errors of the
  fit-set mean (treating `mse_std / sqrt(n_fit)` as the standard error of
  the fit mean, computed the plain simple-random-sample way).

  **Design-effect note, stated plainly.** The estimator here remains the
  plain sample mean/std over selected rows — it is NOT reweighted by
  selection probability and the standard-error formula above is the
  simple-random-sample (SRS) form, not a cluster-robust one. A two-stage
  cluster sample generally has a design effect (deff) >= 1 relative to SRS
  whenever scores are more homogeneous within a group than across the full
  population (plausible here: shared per-exposure/per-healpix systematics),
  which means the TRUE standard error of a cluster-sampled mean is usually
  larger than `mse_std / sqrt(n_fit)` suggests. Concretely: this makes the
  `5 * SE` stability bound narrower than a variance-corrected bound would
  be, so the gate is MORE likely to refuse to seal (fail closed) than a
  cluster-robust test would be — never the reverse. That is conservative
  only in the fail-closed direction this whole scaffold is built around
  (refusing to seal is always the safe failure mode here); it is not a
  claim that the 5x margin is a precise confidence interval. No
  cluster-robust variance correction is implemented, by design: the
  existing 5x margin already provides a wide buffer, and any way in which
  ignoring the design effect could make the gate wrong biases toward
  rejecting a good calibration, never toward sealing a bad one.

The written `calibration.json` binds:
  - the two manifests (JSON files listing the drawn TARGETIDs, in
    post-permutation order, with their survey/program/healpix) by SHA-256
    (`training_manifest_sha256`, `validation_manifest_sha256`);
  - this file's own SHA-256 at run time (`fit_code_sha256`);
  - `score_definition`: "mean_mse_over_per_spectrum_median_abs_flux_normalized_496_bins";
  - `fit_scope`: "held_out_training_validation_split" (unchanged — the
    calibration is still a fit/held-out-validation split; only how the
    underlying rows are sampled has changed);
  - `selection_threshold`: 5.0;
  - `anomaly_score_definition`: "(per_spectrum_mean_mse - mse_mean) / mse_std",
    implemented here as `anomaly_score_from_calibration()` and reused
    verbatim by `run_scan.py`;
  - `sampling_design`: "two-stage-pps-cluster/v2" (self-describing sample
    design tag), plus `n_groups_selected` and `n_rows_target` recording the
    actual stage-2/stage-3 parameters used for this sealed run.

This script downloads DESI DR1 coadd FITS files over the network and loads
the archived model checkpoint; it is meant to run on the pod, never inside
an offline unit test. `tests/test_clean_rerun_campaign.py` exercises only
the pure, network-free pieces: PPS group selection, row-budget allocation,
the seeded two-stage draw + split (against small synthetic group tables,
never a real FITS file), and the anomaly-score arithmetic (against the real
archived `BigAE` class with a fixed-seed state dict).
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
    scan_zcatalog_groups,
    LocatorDerivationError,
)

SEED = 20260804
DEFAULT_N_GROUPS = 200
DEFAULT_N_ROWS = 40_000
DEFAULT_CHUNK_ROWS = 500_000
STABILITY_SIGMA_MULTIPLIER = 5.0
SCORE_DEFINITION = "mean_mse_over_per_spectrum_median_abs_flux_normalized_496_bins"
FIT_SCOPE = "held_out_training_validation_split"
SELECTION_THRESHOLD = 5.0
ANOMALY_SCORE_DEFINITION = "(per_spectrum_mean_mse - mse_mean) / mse_std"
SAMPLING_DESIGN = "two-stage-pps-cluster/v2"

REPO_ROOT = Path(__file__).resolve().parents[3]
ARCHIVED_INFERENCE_PATH = REPO_ROOT / "pipelines/p1_highz_tracers/outputs/enhanced_18M/enhanced_18M_inference.py"
DESI_HEALPIX_BASE_URL = "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/"

GroupKey = tuple[str, str, int]


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


def allocate_row_budget(selected_counts: list[int], n_rows: int) -> list[int]:
    """Largest-remainder proportional allocation of `n_rows` across groups
    sized by `selected_counts`, so the returned allocation sums to EXACTLY
    `n_rows` and never exceeds any group's available row count.

    Deterministic, RNG-free:
      1. Proportional floor + largest-remainder rounding. Remainder rows go
         to the groups with the largest fractional remainder first; ties
         are broken by ascending group position (stable, so identical
         inputs always allocate identically).
      2. If any group's proportional share exceeds its capacity, that
         group's allocation is capped at its full row count and the
         resulting shortfall is redistributed to the groups with the most
         remaining spare capacity, largest group first, ties broken by
         ascending group position. Note this is a defensive safeguard, not
         a load-bearing path: given the `n_rows <= sum(selected_counts)`
         precondition enforced below, `proportional[i] = selected_counts[i]
         * n_rows / sum(selected_counts) <= selected_counts[i]` always
         holds, so `floor(proportional[i]) + 1 <= selected_counts[i]`
         except in the boundary case `n_rows == sum(selected_counts)`
         (full allocation), where `remainder_budget` is 0 and no `+1` is
         ever applied — so this branch should never execute for any input
         that reaches it through this function's own precondition check.
         It is kept anyway as an explicit fail-closed guard rather than a
         silent assumption, exactly like the rest of this fail-closed
         scaffold.
    """
    n = len(selected_counts)
    if n == 0:
        if n_rows == 0:
            return []
        raise CalibrationError("cannot allocate a positive row budget across zero selected groups")
    total_available = sum(selected_counts)
    if n_rows > total_available:
        raise CalibrationError(
            f"cannot allocate {n_rows} rows across {n} selected groups with only "
            f"{total_available} rows available in total"
        )
    if n_rows < 0:
        raise CalibrationError("row budget must be non-negative")

    counts_arr = np.asarray(selected_counts, dtype=np.float64)
    proportional = counts_arr / counts_arr.sum() * n_rows
    floor_alloc = np.floor(proportional).astype(np.int64)
    remainder_budget = int(n_rows - int(floor_alloc.sum()))
    remainders = proportional - floor_alloc

    order = sorted(range(n), key=lambda i: (-remainders[i], i))
    alloc = floor_alloc.copy()
    for i in order[:remainder_budget]:
        alloc[i] += 1

    capacities = np.asarray(selected_counts, dtype=np.int64)
    overflow_positions = [i for i in range(n) if alloc[i] > capacities[i]]
    while overflow_positions:
        i = overflow_positions.pop(0)
        shortfall = int(alloc[i] - capacities[i])
        alloc[i] = capacities[i]
        candidates = sorted(
            (j for j in range(n) if j != i and alloc[j] < capacities[j]),
            key=lambda j: (-capacities[j], j),
        )
        for j in candidates:
            if shortfall <= 0:
                break
            room = int(capacities[j] - alloc[j])
            take = min(room, shortfall)
            alloc[j] += take
            shortfall -= take
        if shortfall > 0:
            raise CalibrationError(
                "cannot allocate row budget: insufficient spare capacity across selected "
                "groups after largest-remainder rounding"
            )

    if int(alloc.sum()) != n_rows:
        raise CalibrationError("internal error: row-budget allocation does not sum to the target")
    for i in range(n):
        if alloc[i] < 0 or alloc[i] > capacities[i]:
            raise CalibrationError("internal error: row-budget allocation violates group capacity")
    return [int(a) for a in alloc]


def select_pps_groups_and_allocate(
    counts_by_group: dict[GroupKey, int],
    seed: int = SEED,
    n_groups: int = DEFAULT_N_GROUPS,
    n_rows: int = DEFAULT_N_ROWS,
) -> tuple[np.random.Generator, list[GroupKey], list[int]]:
    """Stage 2 (PPS group selection) + Stage 3a (row-budget allocation),
    using ONLY per-group row counts (pass 1) — no per-row data is touched.

    Returns the seeded `Generator` (already advanced by exactly ONE
    `rng.choice` call, ready to be reused for stage 3b's per-group
    sampling), the selected groups in ascending `(survey, program,
    healpix)` order, and each selected group's row allocation in that same
    order.
    """
    sorted_groups = sorted(counts_by_group)
    if n_groups > len(sorted_groups):
        raise CalibrationError(
            f"cannot select {n_groups} groups from only {len(sorted_groups)} available groups"
        )
    if n_groups < 0:
        raise CalibrationError("n_groups must be non-negative")

    counts = np.array([counts_by_group[g] for g in sorted_groups], dtype=np.float64)
    rng = np.random.Generator(np.random.PCG64(seed))

    if n_groups == 0:
        return rng, [], []

    p = counts / counts.sum()
    selected_positions = sorted(rng.choice(len(sorted_groups), size=n_groups, replace=False, p=p).tolist())
    selected_groups = [sorted_groups[i] for i in selected_positions]
    selected_counts = [int(counts_by_group[g]) for g in selected_groups]

    alloc = allocate_row_budget(selected_counts, n_rows)
    return rng, selected_groups, alloc


def sample_and_split_rows(
    rng: np.random.Generator,
    selected_groups: list[GroupKey],
    alloc: list[int],
    row_indices_by_group: dict[GroupKey, np.ndarray],
    n_fit: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Stage 3b (per-group row sampling, continuing the SAME rng passed in)
    + the final seeded permutation + fit/validation split.

    `row_indices_by_group` must cover every key in `selected_groups`
    (production: pass-2 zcatalog stream output; tests: a small synthetic
    dict). RNG call order: one `rng.choice` per selected group, in
    `selected_groups` order, followed by exactly one final
    `rng.permutation` — this is the tail of the same call sequence
    `select_pps_groups_and_allocate` started, so results are fully
    reproducible end to end from a single seed.
    """
    if len(selected_groups) != len(alloc):
        raise CalibrationError("selected_groups and alloc must be the same length")
    total_rows = sum(alloc)
    if n_fit < 0 or n_fit > total_rows:
        raise CalibrationError(f"n_fit={n_fit} is out of range for a {total_rows}-row draw")

    chosen: list[np.ndarray] = []
    for group, k in zip(selected_groups, alloc):
        if group not in row_indices_by_group:
            raise CalibrationError(f"missing pass-2 row indices for selected group {group}")
        rows = np.asarray(row_indices_by_group[group])
        if k > len(rows):
            raise CalibrationError(
                f"group {group} was allocated {k} rows but only {len(rows)} are available"
            )
        if k == 0:
            chosen.append(np.array([], dtype=np.int64))
            continue
        local = rng.choice(len(rows), size=k, replace=False)
        chosen.append(rows[local].astype(np.int64, copy=False))

    all_rows = np.concatenate(chosen) if chosen else np.array([], dtype=np.int64)
    if len(all_rows) != total_rows:
        raise CalibrationError("internal error: sampled row count does not match the allocation total")
    if len(set(all_rows.tolist())) != len(all_rows):
        raise CalibrationError("internal error: sampled row indices are not distinct")

    permuted = all_rows[rng.permutation(len(all_rows))]
    return permuted[:n_fit], permuted[n_fit:]


def draw_two_stage_pps_sample(
    row_indices_by_group: dict[GroupKey, np.ndarray],
    seed: int,
    n_groups: int,
    n_rows: int,
    n_fit: int,
) -> tuple[np.ndarray, np.ndarray, list[GroupKey], list[int]]:
    """Convenience wrapper combining stage 2/3a (`select_pps_groups_and_allocate`)
    and stage 3b/split (`sample_and_split_rows`) against a single, already
    fully-materialized per-group row-index table.

    Used directly by offline tests against small synthetic group tables
    (no FITS file involved). Production instead calls the two halves
    separately with a real pass-1/pass-2 zcatalog stream in between, so the
    full-catalog per-group row-index table is never materialized (only the
    ~200 selected groups' row indices are).
    """
    counts_by_group = {g: len(rows) for g, rows in row_indices_by_group.items()}
    rng, selected_groups, alloc = select_pps_groups_and_allocate(
        counts_by_group, seed=seed, n_groups=n_groups, n_rows=n_rows
    )
    fit_idx, val_idx = sample_and_split_rows(rng, selected_groups, alloc, row_indices_by_group, n_fit)
    return fit_idx, val_idx, selected_groups, alloc


def collect_selected_group_row_indices(
    zcatalog_path: Path,
    selected_groups: list[GroupKey],
    chunk_rows: int = DEFAULT_CHUNK_ROWS,
) -> dict[GroupKey, np.ndarray]:
    """Pass 2: stream the zcatalog a second time in memory-bounded chunks,
    collecting row indices ONLY for rows belonging to `selected_groups`
    (the ~200 groups chosen in stage 2). Per-row index lists for the other
    tens of thousands of groups in the catalog are never built.
    """
    from astropy.io import fits

    wanted = set(selected_groups)
    rows_by_group: dict[GroupKey, list[int]] = {g: [] for g in wanted}
    with fits.open(zcatalog_path, memmap=True) as hdul:
        hdu = find_catalog_hdu(hdul)
        data = hdu.data
        n_rows = len(data)
        for start in range(0, n_rows, chunk_rows):
            stop = min(start + chunk_rows, n_rows)
            survey_chunk = data["SURVEY"][start:stop]
            program_chunk = data["PROGRAM"][start:stop]
            healpix_chunk = data["HEALPIX"][start:stop]
            if not (len(survey_chunk) == len(program_chunk) == len(healpix_chunk)):
                raise CalibrationError(f"column-length mismatch in zcatalog chunk [{start}:{stop}]")
            for offset, (survey_raw, program_raw, healpix_raw) in enumerate(
                zip(survey_chunk, program_chunk, healpix_chunk)
            ):
                key = (decode_fits_str(survey_raw), decode_fits_str(program_raw), int(healpix_raw))
                if key in wanted:
                    rows_by_group[key].append(start + offset)
    return {g: np.array(idx, dtype=np.int64) for g, idx in rows_by_group.items()}


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


def write_manifest(
    targets: list[dict[str, Any]],
    seed: int,
    role: str,
    output_path: Path,
    n_groups: int = DEFAULT_N_GROUPS,
    n_rows: int = DEFAULT_N_ROWS,
) -> Path:
    payload = {
        "manifest_role": role,
        "seed": seed,
        "count": len(targets),
        "sampling_design": SAMPLING_DESIGN,
        "n_groups_selected": n_groups,
        "n_rows_target": n_rows,
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
    n_groups: int = DEFAULT_N_GROUPS,
    n_rows: int = DEFAULT_N_ROWS,
    seed: int = SEED,
    chunk_rows: int = DEFAULT_CHUNK_ROWS,
) -> dict[str, Any]:
    import torch

    if n_rows % 2 != 0:
        raise CalibrationError(f"n_rows must be even to split into equal fit/validation halves, got {n_rows}")
    n_fit = n_rows // 2

    manifest = read_json(manifest_path)
    verify_zcatalog_checksum(zcatalog_path, manifest)

    # Pass 1: memory-bounded per-group row counts (never per-row indices).
    counts_by_group = scan_zcatalog_groups(zcatalog_path, chunk_rows=chunk_rows)
    if not counts_by_group:
        raise CalibrationError("zcatalog yielded zero (survey, program, healpix) groups")

    # Stage 2 (PPS group selection) + Stage 3a (row-budget allocation).
    rng, selected_groups, alloc = select_pps_groups_and_allocate(
        counts_by_group, seed=seed, n_groups=n_groups, n_rows=n_rows
    )

    # Pass 2: memory-bounded row indices for ONLY the selected groups.
    row_indices_by_group = collect_selected_group_row_indices(zcatalog_path, selected_groups, chunk_rows=chunk_rows)
    for group in selected_groups:
        observed = len(row_indices_by_group.get(group, ()))
        expected = counts_by_group[group]
        if observed != expected:
            raise CalibrationError(
                f"pass-2 row count for group {group} ({observed}) does not match pass-1 count "
                f"({expected}); refusing to trust an inconsistent zcatalog read"
            )

    # Stage 3b (per-group sampling) + seeded split, continuing the same rng.
    fit_idx, val_idx = sample_and_split_rows(rng, selected_groups, alloc, row_indices_by_group, n_fit)

    fit_targets = gather_targets(zcatalog_path, fit_idx)
    val_targets = gather_targets(zcatalog_path, val_idx)

    write_manifest(fit_targets, seed, "calibration_fit", training_manifest_output, n_groups=n_groups, n_rows=n_rows)
    write_manifest(val_targets, seed, "held_out_validation", validation_manifest_output, n_groups=n_groups, n_rows=n_rows)

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

    # Simple-random-sample-form standard error; see module docstring's
    # "Design-effect note" for why this is conservative in the fail-closed
    # direction only under this two-stage cluster design.
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
        "sampling_design": SAMPLING_DESIGN,
        "n_groups_selected": len(selected_groups),
        "n_rows_target": n_rows,
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
        "seed": seed,
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
    parser.add_argument(
        "--n-groups", type=int, default=DEFAULT_N_GROUPS, help="number of (survey, program, healpix) groups to sample"
    )
    parser.add_argument(
        "--n-rows", type=int, default=DEFAULT_N_ROWS, help="total rows to sample across the selected groups"
    )
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
        n_groups=args.n_groups,
        n_rows=args.n_rows,
    )
    print(json.dumps(calibration, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Rerun P4 harmonic diagnostics on one exact 24,087-pixel FSC support.

The v1.0.257 exact-PDF review found that historical generators mixed the
declared ``N_spiral >= 10`` support with ``N_spiral > 0``.  This generator
fails closed unless the release catalog produces exactly 24,087 support
pixels, persists the support as a checksummed boolean array and index array,
and runs every requested harmonic leg against that same support.

Legs
----
* fixed-occupancy label shuffle, 500 draws, MASTER ell=1 ("direct-MC")
* binomial-monopole null, 500 and 10,000 draws, MASTER ell=1
* fixed-occupancy label shuffle, 500 draws, C2 2-degree apodized MASTER ell=1
* fixed-occupancy label shuffle, 500 draws, binary MASTER ell=1..5

All fields use f_CW-0.5 with N_spiral-weighted mean subtraction before
NaMaster field construction.  The binomial-monopole leg intentionally uses
independent per-pixel Binomial(N_spiral(p), p_CW_global) draws, matching the
existing monopole-only diagnostic.  Other legs condition on both pixel
occupancies and the observed in-support CW total through a multivariate
hypergeometric allocation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from pathlib import Path

import healpy as hp
import numpy as np
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

try:
    import pymaster as nmt
except ImportError as exc:  # fail honestly before writing partial science output
    raise SystemExit(
        "pymaster is required for the MASTER legs; no result was produced"
    ) from exc


HERE = Path(__file__).resolve().parent
P4 = HERE.parent
ROOT = P4.parents[1]
CATALOG = P4 / "apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet"
OUTDIR = P4 / "outputs/canonical_provenance"
MASK_PATH = OUTDIR / "p4_fsc_mask_nspiral_ge10_nside64_v1_0_257.npy"
MASK_INDEX_PATH = OUTDIR / "p4_fsc_mask_indices_nspiral_ge10_nside64_v1_0_257.npy"
ARRAYS_PATH = OUTDIR / "p4_fsc_exact_support_harmonic_nulls_v1_0_257.npz"
RECEIPT_PATH = OUTDIR / "p4_fsc_exact_support_harmonics_v1_0_257.json"

CATALOG_SHA256 = "139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3"
NSIDE = 64
LMAX = 3 * NSIDE - 1
MIN_PIXEL_COUNT = 10
EXPECTED_PIXELS = 24_087
LABEL_DRAWS = 500
MONOPOLE_DRAWS = 10_000
SEED = 42
APODIZATION_DEG = 2.0


def log(message: str, started: float) -> None:
    print(f"[{time.time() - started:8.1f}s] {message}", flush=True)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def relative(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(ROOT.resolve()))
    except ValueError:
        return str(resolved)


def single_ell_bins():
    bpws = np.full(LMAX + 1, -1, dtype=np.int32)
    bpws[1:] = np.arange(LMAX, dtype=np.int32)
    return nmt.NmtBin(
        bpws=bpws,
        ells=np.arange(LMAX + 1, dtype=np.int32),
        weights=np.ones(LMAX + 1, dtype=np.float64),
        lmax=LMAX,
    )


def subtract_weighted_mean(
    cw_counts: np.ndarray, capacities: np.ndarray
) -> np.ndarray:
    field = cw_counts / capacities - 0.5
    field -= np.average(field, weights=capacities)
    return field


def make_workspace(weight: np.ndarray, bins):
    dummy = nmt.NmtField(weight, [np.zeros(weight.size)], lite=True)
    workspace = nmt.NmtWorkspace()
    workspace.compute_coupling_matrix(dummy, dummy, bins)
    return workspace


def decoupled_low_ells(
    values_on_support: np.ndarray,
    support: np.ndarray,
    weight: np.ndarray,
    workspace,
    n_ells: int = 5,
) -> np.ndarray:
    full = np.zeros(support.size, dtype=np.float64)
    full[support] = values_on_support
    field = nmt.NmtField(weight, [full], lite=True)
    coupled = nmt.compute_coupled_cell(field, field)
    decoupled = workspace.decouple_cell(coupled)[0]
    return np.asarray(decoupled[:n_ells], dtype=np.float64)


def summarize(null: np.ndarray, observed: float) -> dict:
    mean = float(null.mean())
    std0 = float(null.std(ddof=0))
    std1 = float(null.std(ddof=1))
    k = int(np.count_nonzero(null >= observed))
    return {
        "observed": observed,
        "null_mean": mean,
        "null_std_ddof0": std0,
        "null_std_ddof1": std1,
        "moment_z_ddof0": (
            (observed - mean) / std0 if std0 > 0 else None
        ),
        "rank_k_upper": k,
        "rank_p_upper_add_one": (k + 1) / (null.size + 1),
        "rank_formula": "(k+1)/(N+1), k=count(null >= observed)",
        "n_draws": int(null.size),
    }


def run(
    catalog_path: Path,
    mask_path: Path,
    mask_index_path: Path,
    arrays_path: Path,
    receipt_path: Path,
    label_draws: int,
    monopole_draws: int,
) -> dict:
    started = time.time()
    if sha256_file(catalog_path) != CATALOG_SHA256:
        raise RuntimeError("catalog SHA-256 does not match the pinned release")

    log("loading pinned release catalog", started)
    table = pq.read_table(
        catalog_path, columns=["ra_deg", "dec_deg", "class_eq"]
    )
    spiral = pc.is_in(table["class_eq"], value_set=pa.array(["CW", "CCW"]))
    table = table.filter(spiral)
    if table.num_rows != 3_201_160:
        raise RuntimeError(f"spiral rows {table.num_rows}; expected 3,201,160")

    ra = table["ra_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    dec = table["dec_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    labels = np.asarray(
        table["class_eq"].combine_chunks().to_pylist(), dtype=object
    )
    pix = hp.ang2pix(
        NSIDE, np.radians(90.0 - dec), np.radians(ra % 360.0)
    )
    npix = hp.nside2npix(NSIDE)
    total = np.bincount(pix, minlength=npix).astype(np.int64)
    cw = np.bincount(pix[labels == "CW"], minlength=npix).astype(np.int64)
    support = total >= MIN_PIXEL_COUNT
    support_idx = np.flatnonzero(support)
    if support_idx.size != EXPECTED_PIXELS:
        raise RuntimeError(
            f"FSC support has {support_idx.size} pixels; expected {EXPECTED_PIXELS}"
        )
    capacities = total[support]
    observed_cw = cw[support]
    n_cw_support = int(observed_cw.sum())
    p_cw_support = n_cw_support / int(capacities.sum())

    mask_path.parent.mkdir(parents=True, exist_ok=True)
    np.save(mask_path, support, allow_pickle=False)
    np.save(mask_index_path, support_idx, allow_pickle=False)
    mask_sha = sha256_file(mask_path)
    index_sha = sha256_file(mask_index_path)
    log(f"persisted exact FSC mask: {support_idx.size:,} pixels", started)

    bins = single_ell_bins()
    binary_weight = support.astype(np.float64)
    log("building binary-mask MASTER workspace", started)
    binary_workspace = make_workspace(binary_weight, bins)
    log("building C2 2-degree apodized MASTER workspace", started)
    apodized_weight = nmt.mask_apodization(
        binary_weight, APODIZATION_DEG, "C2"
    )
    apodized_workspace = make_workspace(apodized_weight, bins)

    observed_field = subtract_weighted_mean(observed_cw, capacities)
    binary_observed = decoupled_low_ells(
        observed_field, support, binary_weight, binary_workspace, 5
    )
    apodized_observed = decoupled_low_ells(
        observed_field, support, apodized_weight, apodized_workspace, 1
    )[0]
    log(
        f"observed binary C1={binary_observed[0]:.6e}; "
        f"apodized C1={apodized_observed:.6e}",
        started,
    )

    rng_label = np.random.default_rng(SEED)
    label_null = np.empty((label_draws, 5), dtype=np.float64)
    apodized_null = np.empty(label_draws, dtype=np.float64)
    for draw in range(label_draws):
        shuffled_cw = rng_label.multivariate_hypergeometric(
            capacities, n_cw_support, method="marginals"
        )
        null_field = subtract_weighted_mean(shuffled_cw, capacities)
        label_null[draw] = decoupled_low_ells(
            null_field, support, binary_weight, binary_workspace, 5
        )
        apodized_null[draw] = decoupled_low_ells(
            null_field, support, apodized_weight, apodized_workspace, 1
        )[0]
        if (draw + 1) % 50 == 0:
            log(f"fixed-occupancy label null {draw + 1}/{label_draws}", started)

    rng_mono = np.random.default_rng(SEED)
    monopole_null = np.empty(monopole_draws, dtype=np.float64)
    for draw in range(monopole_draws):
        null_cw = rng_mono.binomial(capacities, p_cw_support)
        null_field = subtract_weighted_mean(null_cw, capacities)
        monopole_null[draw] = decoupled_low_ells(
            null_field, support, binary_weight, binary_workspace, 1
        )[0]
        if (draw + 1) % 500 == 0:
            log(f"binomial-monopole null {draw + 1}/{monopole_draws}", started)

    np.savez(
        arrays_path,
        fixed_occupancy_binary_c1_to_c5=label_null,
        fixed_occupancy_apodized_c1=apodized_null,
        binomial_monopole_binary_c1=monopole_null,
    )

    multipoles = {
        f"ell_{ell}": summarize(label_null[:, ell - 1], binary_observed[ell - 1])
        for ell in range(1, 6)
    }
    result = {
        "schema": "p4-fsc-exact-support-harmonics/v1",
        "review_basis": "P4 v1.0.257 exact-PDF truth-audit finding 1",
        "status": "complete",
        "generator": {
            "path": relative(Path(__file__)),
            "sha256": sha256_file(Path(__file__)),
        },
        "catalog": {
            "path": relative(catalog_path),
            "sha256": sha256_file(catalog_path),
            "n_spirals": int(table.num_rows),
        },
        "support": {
            "definition": "class_eq in {CW,CCW}; HEALPix NSIDE=64; N_spiral(pixel) >= 10",
            "n_pixels": int(support_idx.size),
            "expected_n_pixels": EXPECTED_PIXELS,
            "f_sky": float(support.mean()),
            "n_spirals_in_support": int(capacities.sum()),
            "n_cw_in_support": n_cw_support,
            "p_cw_in_support": p_cw_support,
            "mask": {"path": relative(mask_path), "sha256": mask_sha},
            "indices": {
                "path": relative(mask_index_path),
                "sha256": index_sha,
            },
        },
        "shared_field": {
            "definition": "f_CW(pixel)-0.5",
            "monopole_subtraction": (
                "N_spiral-weighted support mean, applied identically to data "
                "and every null realization"
            ),
            "master_binning": "single-ell bins ell=1..191; reported ell=1..5",
        },
        "fixed_occupancy_direct_mc_binary": summarize(
            label_null[:, 0], binary_observed[0]
        ),
        "master_monopole_only_binary_500": summarize(
            monopole_null[: min(500, monopole_draws)], binary_observed[0]
        ),
        "master_monopole_only_binary_10000": summarize(
            monopole_null, binary_observed[0]
        ),
        "apodized_fsc_c2_2deg": {
            **summarize(apodized_null, float(apodized_observed)),
            "apodization": "NaMaster C2, 2 degrees, applied to exact FSC binary mask",
            "f_sky_mean_weight": float(apodized_weight.mean()),
            "f_sky_effective": float(
                np.mean(apodized_weight) ** 2 / np.mean(apodized_weight**2)
            ),
        },
        "multipole_spectrum_binary": multipoles,
        "nulls": {
            "fixed_occupancy": {
                "definition": (
                    "multivariate-hypergeometric allocation of the fixed "
                    "observed support CW total over fixed pixel capacities"
                ),
                "seed": SEED,
                "n_draws": label_draws,
            },
            "binomial_monopole": {
                "definition": (
                    "independent Binomial(N_spiral(pixel), p_CW_support) "
                    "draws on the exact support"
                ),
                "seed": SEED,
                "n_draws": monopole_draws,
            },
        },
        "arrays": {
            "path": relative(arrays_path),
            "sha256": sha256_file(arrays_path),
            "members": {
                "fixed_occupancy_binary_c1_to_c5": list(label_null.shape),
                "fixed_occupancy_apodized_c1": list(apodized_null.shape),
                "binomial_monopole_binary_c1": list(monopole_null.shape),
            },
        },
        "common_support_invariants": {
            "all_data_fields_use_mask_sha256": mask_sha,
            "all_null_fields_use_mask_sha256": mask_sha,
            "apodized_weight_derived_from_same_binary_mask": True,
            "apodized_nonzero_pixels_subset_of_support": bool(
                np.all(np.logical_not(apodized_weight > 0) | support)
            ),
            "fixed_occupancy_pixel_capacities_unchanged": True,
            "binomial_monopole_pixel_capacities_unchanged": True,
        },
        "runtime": {
            "wall_seconds": time.time() - started,
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "numpy": np.__version__,
            "healpy": hp.__version__,
            "pyarrow": pa.__version__,
            "pymaster": getattr(nmt, "__version__", "unknown"),
        },
        "interpretation_limits": [
            "systematics diagnostic, not a cosmological detection",
            "moment-z values are not Gaussian-equivalent tail significances",
            "fixed-occupancy and binomial-monopole nulls answer different questions",
        ],
    }
    receipt_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    log(f"wrote {relative(receipt_path)}", started)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    parser.add_argument("--mask", type=Path, default=MASK_PATH)
    parser.add_argument("--mask-indices", type=Path, default=MASK_INDEX_PATH)
    parser.add_argument("--arrays", type=Path, default=ARRAYS_PATH)
    parser.add_argument("--receipt", type=Path, default=RECEIPT_PATH)
    parser.add_argument("--label-draws", type=int, default=LABEL_DRAWS)
    parser.add_argument("--monopole-draws", type=int, default=MONOPOLE_DRAWS)
    args = parser.parse_args()
    if args.label_draws < 1 or args.monopole_draws < 500:
        raise SystemExit("label draws must be >=1 and monopole draws >=500")
    run(
        args.catalog,
        args.mask,
        args.mask_indices,
        args.arrays,
        args.receipt,
        args.label_draws,
        args.monopole_draws,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

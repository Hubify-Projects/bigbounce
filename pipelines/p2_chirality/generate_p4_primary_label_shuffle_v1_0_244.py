#!/usr/bin/env python3
"""Generate the exact fixed-occupancy P4 HC primary label-shuffle null.

The null conditions on the observed HC_REALSPACE_INCLUSIVE support-pixel
occupancies and the observed CW count among galaxies in those support pixels.
Each realization allocates that fixed support-sample CW count across the fixed
pixel capacities with a multivariate-hypergeometric draw. This is the exact
count-level distribution induced by uniformly randomizing the support-sample
CW/CCW labels while holding their positions and the analysis support fixed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import healpy as hp
import numpy as np
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DEFAULT_CATALOG = HERE / "apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet"
DEFAULT_ARRAY = HERE / "outputs/canonical_provenance/p4_primary_hc_label_shuffle_10k.npy"
DEFAULT_RECEIPT = HERE / "outputs/canonical_provenance/p4_primary_hc_label_shuffle_10k.json"
CATALOG_SHA256 = "139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3"
NSIDE = 64
MIN_PIXEL_COUNT = 10
N_DRAWS = 10_000
SEED = 20260715


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def rank_p(null: np.ndarray, observed: float) -> tuple[int, float]:
    k = int(np.count_nonzero(null >= observed))
    return k, (k + 1) / (null.size + 1)


def repo_relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve()))


def generate(catalog_path: Path, array_path: Path, receipt_path: Path) -> dict:
    catalog_sha256 = sha256_file(catalog_path)
    if catalog_sha256 != CATALOG_SHA256:
        raise RuntimeError(
            f"catalog SHA-256 {catalog_sha256}; expected {CATALOG_SHA256}"
        )

    table = pq.read_table(
        catalog_path,
        columns=["ra_deg", "dec_deg", "class_eq", "primary_hc"],
        filters=[("primary_hc", "=", True)],
    )
    table = table.filter(pc.equal(table["primary_hc"], True))
    ra = table["ra_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    dec = table["dec_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    labels = np.asarray(table["class_eq"].combine_chunks().to_pylist(), dtype=object)
    is_cw = labels == "CW"

    npix = hp.nside2npix(NSIDE)
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra % 360.0))
    total = np.bincount(pix, minlength=npix).astype(np.int64)
    cw = np.bincount(pix[is_cw], minlength=npix).astype(np.int64)
    support = total >= MIN_PIXEL_COUNT
    support_idx = np.flatnonzero(support)
    capacities = total[support]
    observed_cw = cw[support]
    n_cw = int(observed_cw.sum())

    observed_map = np.full(npix, hp.UNSEEN)
    observed_map[support] = (2.0 * observed_cw - capacities) / capacities
    _, observed_vector = hp.fit_dipole(observed_map, gal_cut=0)
    observed_amplitude = float(np.linalg.norm(observed_vector))

    theta, phi = hp.pix2ang(NSIDE, support_idx)
    design = np.column_stack(
        [
            np.ones(support_idx.size),
            np.sin(theta) * np.cos(phi),
            np.sin(theta) * np.sin(phi),
            np.cos(theta),
        ]
    )
    projector = np.linalg.inv(design.T @ design) @ design.T
    projected_observed = projector @ observed_map[support]
    projected_amplitude = float(np.linalg.norm(projected_observed[1:]))
    if not np.isclose(projected_amplitude, observed_amplitude, rtol=0, atol=1e-14):
        raise RuntimeError(
            "linear projector does not reproduce healpy.fit_dipole: "
            f"{projected_amplitude} != {observed_amplitude}"
        )

    rng = np.random.default_rng(SEED)
    amplitudes = np.empty(N_DRAWS, dtype=np.float64)
    for draw in range(N_DRAWS):
        shuffled_cw = rng.multivariate_hypergeometric(
            capacities, n_cw, method="marginals"
        )
        asymmetry = (2.0 * shuffled_cw - capacities) / capacities
        coefficients = projector @ asymmetry
        amplitudes[draw] = np.linalg.norm(coefficients[1:])

    array_path.parent.mkdir(parents=True, exist_ok=True)
    np.save(array_path, amplitudes, allow_pickle=False)
    array_sha256 = sha256_file(array_path)
    rank_k, rank_value = rank_p(amplitudes, observed_amplitude)
    receipt = {
        "schema": "p4-primary-hc-label-shuffle/v1",
        "paper_version_basis": "v1.0.245 paper closure; catalog payload v1.0.244",
        "scope": "observed equivariant hard labels; descriptive isotropy null only",
        "selection": "primary_hc == True; HEALPix NSIDE=64; N_spiral(pixel) >= 10",
        "null_definition": (
            "fixed-occupancy galaxy-label randomization: multivariate-hypergeometric "
            "allocation of the observed CW count among support galaxies across "
            "observed support-pixel capacities"
        ),
        "seed": SEED,
        "numpy_bit_generator": type(rng.bit_generator).__name__,
        "runtime_versions": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "healpy": hp.__version__,
            "pyarrow": pa.__version__,
        },
        "n_draws": N_DRAWS,
        "n_primary_hc": int(table.num_rows),
        "n_pixels_inclusive": int(support.sum()),
        "n_galaxies_in_support": int(capacities.sum()),
        "n_cw_in_support": n_cw,
        "observed_amplitude": observed_amplitude,
        "null_mean": float(amplitudes.mean()),
        "null_std_ddof0": float(amplitudes.std(ddof=0)),
        "null_std_ddof1": float(amplitudes.std(ddof=1)),
        "significance_sigma_ddof0": float(
            (observed_amplitude - amplitudes.mean()) / amplitudes.std(ddof=0)
        ),
        "rank_k": rank_k,
        "rank_p_one_sided_upper_tail": rank_value,
        "rank_formula": "(k+1)/(N+1), k=count(A_null >= A_data)",
        "catalog": {"path": repo_relative(catalog_path), "sha256": catalog_sha256},
        "array": {
            "path": repo_relative(array_path),
            "shape": list(amplitudes.shape),
            "dtype": str(amplitudes.dtype),
            "sha256": array_sha256,
        },
        "pixel_permutation_policy": "retained as a robustness diagnostic; not primary",
        "exclusions": [
            "no calibrated-probability claim",
            "no physical-amplitude or primordial bound",
            "no matched-external-estimator claim",
            "no formal-preregistration claim",
        ],
    }
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--array", type=Path, default=DEFAULT_ARRAY)
    parser.add_argument("--receipt", type=Path, default=DEFAULT_RECEIPT)
    args = parser.parse_args()
    print(json.dumps(generate(args.catalog, args.array, args.receipt), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

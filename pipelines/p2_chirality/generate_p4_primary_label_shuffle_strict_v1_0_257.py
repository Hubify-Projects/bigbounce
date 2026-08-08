#!/usr/bin/env python3
"""Recompute P4's primary null after excluding release-quarantined HC rows.

This is the convention-matched closure requested by the exact-PDF v1.0.257
review.  It differs from ``generate_p4_primary_label_shuffle_v1_0_244.py``
only in the declared row selection:

    primary_hc == True and raw_flip_qc_unsafe == False

The HEALPix support rule, fixed-occupancy multivariate-hypergeometric null,
draw count, seed, estimator, and empirical-rank convention are unchanged.
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
DEFAULT_CATALOG = (
    HERE / "apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet"
)
DEFAULT_ARRAY = (
    HERE
    / "outputs/canonical_provenance/"
    "p4_primary_hc_safe_label_shuffle_10k_v1_0_257.npy"
)
DEFAULT_RECEIPT = (
    HERE
    / "outputs/canonical_provenance/"
    "p4_primary_hc_safe_label_shuffle_10k_v1_0_257.json"
)
CATALOG_SHA256 = "139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3"
EXPECTED_SELECTED_ROWS = 890_069
NSIDE = 64
MIN_PIXEL_COUNT = 10
N_DRAWS = 10_000
SEED = 20_260_715


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def repo_relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve()))


def select_strict_primary(table: pa.Table) -> pa.Table:
    """Apply the exact review-mandated safe-HC selection."""
    selected = pc.and_(
        pc.equal(table["primary_hc"], True),
        pc.equal(table["raw_flip_qc_unsafe"], False),
    )
    return table.filter(selected)


def build_projector(
    total: np.ndarray, cw: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    support = total >= MIN_PIXEL_COUNT
    support_idx = np.flatnonzero(support)
    capacities = total[support].astype(np.int64, copy=False)
    observed_cw = cw[support].astype(np.int64, copy=False)

    observed_map = np.full(total.size, hp.UNSEEN)
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
    projected = projector @ observed_map[support]
    if not np.isclose(
        np.linalg.norm(projected[1:]), observed_amplitude, rtol=0, atol=1e-14
    ):
        raise RuntimeError("linear projector does not reproduce healpy.fit_dipole")
    return support, capacities, projector, observed_amplitude


def generate(catalog_path: Path, array_path: Path, receipt_path: Path) -> dict:
    catalog_sha256 = sha256_file(catalog_path)
    if catalog_sha256 != CATALOG_SHA256:
        raise RuntimeError(
            f"catalog SHA-256 {catalog_sha256}; expected {CATALOG_SHA256}"
        )

    table = pq.read_table(
        catalog_path,
        columns=[
            "ra_deg",
            "dec_deg",
            "class_eq",
            "primary_hc",
            "raw_flip_qc_unsafe",
        ],
    )
    n_primary_hc = int(pc.sum(pc.cast(table["primary_hc"], pa.int64())).as_py())
    strict = select_strict_primary(table)
    if strict.num_rows != EXPECTED_SELECTED_ROWS:
        raise RuntimeError(
            f"strict selected rows {strict.num_rows}; expected {EXPECTED_SELECTED_ROWS}"
        )
    selection_mask = np.asarray(
        pc.and_(
            pc.equal(table["primary_hc"], True),
            pc.equal(table["raw_flip_qc_unsafe"], False),
        ).to_numpy(zero_copy_only=False),
        dtype=np.bool_,
    )
    selection_mask_sha256 = hashlib.sha256(
        np.packbits(selection_mask, bitorder="little").tobytes()
    ).hexdigest()

    ra = strict["ra_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    dec = strict["dec_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    labels = np.asarray(
        strict["class_eq"].combine_chunks().to_pylist(), dtype=object
    )
    is_cw = labels == "CW"
    if not np.all(np.logical_or(is_cw, labels == "CCW")):
        raise RuntimeError("strict primary selection contains a non-spiral label")

    npix = hp.nside2npix(NSIDE)
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra % 360.0))
    total = np.bincount(pix, minlength=npix).astype(np.int64)
    cw = np.bincount(pix[is_cw], minlength=npix).astype(np.int64)
    support, capacities, projector, observed_amplitude = build_projector(total, cw)
    n_cw = int(cw[support].sum())

    rng = np.random.default_rng(SEED)
    amplitudes = np.empty(N_DRAWS, dtype=np.float64)
    for draw in range(N_DRAWS):
        shuffled_cw = rng.multivariate_hypergeometric(
            capacities, n_cw, method="marginals"
        )
        coefficients = projector @ (
            (2.0 * shuffled_cw - capacities) / capacities
        )
        amplitudes[draw] = np.linalg.norm(coefficients[1:])

    array_path.parent.mkdir(parents=True, exist_ok=True)
    np.save(array_path, amplitudes, allow_pickle=False)
    rank_k = int(np.count_nonzero(amplitudes >= observed_amplitude))
    receipt = {
        "schema": "p4-primary-hc-safe-label-shuffle/v1",
        "review_basis": "P4 v1.0.257 exact-PDF truth-audit finding 2",
        "selection": (
            "primary_hc == True and raw_flip_qc_unsafe == False; "
            "HEALPix NSIDE=64; N_spiral(pixel) >= 10"
        ),
        "selection_counts": {
            "n_catalog_rows": int(table.num_rows),
            "n_primary_hc_before_qc_exclusion": n_primary_hc,
            "n_raw_flip_qc_unsafe_excluded_from_primary_hc": (
                n_primary_hc - int(strict.num_rows)
            ),
            "n_unsafe_rows_selected": int(
                pc.sum(
                    pc.cast(strict["raw_flip_qc_unsafe"], pa.int64())
                ).as_py()
            ),
            "n_selected_rows": int(strict.num_rows),
            "expected_selected_rows": EXPECTED_SELECTED_ROWS,
            "selected_row_mask_packbits_little_sha256": selection_mask_sha256,
            "n_pixels_inclusive": int(support.sum()),
            "n_galaxies_in_support": int(capacities.sum()),
            "n_cw_in_support": n_cw,
        },
        "null_definition": (
            "fixed-occupancy galaxy-label randomization: multivariate-"
            "hypergeometric allocation of the observed support-sample CW count "
            "among fixed support-pixel capacities"
        ),
        "estimator": "unweighted healpy.fit_dipole amplitude of per-pixel asymmetry",
        "seed": SEED,
        "n_draws": N_DRAWS,
        "numpy_bit_generator": type(rng.bit_generator).__name__,
        "observed_amplitude": observed_amplitude,
        "null_mean": float(amplitudes.mean()),
        "null_std_ddof0": float(amplitudes.std(ddof=0)),
        "null_std_ddof1": float(amplitudes.std(ddof=1)),
        "significance_sigma_ddof0": float(
            (observed_amplitude - amplitudes.mean()) / amplitudes.std(ddof=0)
        ),
        "rank_k": rank_k,
        "rank_p_one_sided_upper_tail": (rank_k + 1) / (N_DRAWS + 1),
        "rank_formula": "(k+1)/(N+1), k=count(A_null >= A_data)",
        "catalog": {"path": repo_relative(catalog_path), "sha256": catalog_sha256},
        "array": {
            "path": repo_relative(array_path),
            "shape": list(amplitudes.shape),
            "dtype": str(amplitudes.dtype),
            "sha256": sha256_file(array_path),
        },
        "runtime_versions": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "healpy": hp.__version__,
            "pyarrow": pa.__version__,
        },
        "interpretation_limits": [
            "observed-label descriptive isotropy null only",
            "not an independent classifier validation",
            "not a calibrated physical or primordial amplitude bound",
        ],
    }
    receipt_path.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--array", type=Path, default=DEFAULT_ARRAY)
    parser.add_argument("--receipt", type=Path, default=DEFAULT_RECEIPT)
    args = parser.parse_args()
    print(
        json.dumps(
            generate(args.catalog, args.array, args.receipt),
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Reproduce P4 v1.0.259's strict observed-label primary null."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import healpy as hp
import numpy as np
import pyarrow.compute as pc
import pyarrow.parquet as pq

CATALOG_SHA256 = "139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3"
NULL_SHA256 = "3a03ca4b008844fd8bf16be4e1e7e918ceaf580992d9462d54233f417e32ce7d"
EXPECTED = {
    "n_selected": 890_069,
    "n_support": 887_472,
    "n_pixels": 23_633,
    "amplitude": 0.004665198792857314,
    "monopole": 0.02550645536278439,
    "ra_deg": 195.48198600769373,
    "dec_deg": -57.16150970329368,
    "null_mean": 0.003620291387422168,
    "null_std": 0.0016464287407124284,
    "z": 0.6346508534484177,
    "rank_k": 2_376,
    "rank_p": 0.23767623237676233,
}


class ReproductionError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def reproduce(catalog: Path, null_array: Path) -> dict:
    if sha256_file(catalog) != CATALOG_SHA256:
        raise ReproductionError("catalog SHA-256 mismatch")
    if sha256_file(null_array) != NULL_SHA256:
        raise ReproductionError("strict null-array SHA-256 mismatch")

    table = pq.read_table(
        catalog,
        columns=["ra_deg", "dec_deg", "class_eq", "primary_hc", "raw_flip_qc_unsafe"],
        filters=[("primary_hc", "=", True)],
    )
    table = table.filter(
        pc.and_(
            pc.equal(table["primary_hc"], True),
            pc.equal(table["raw_flip_qc_unsafe"], False),
        )
    )
    labels = np.asarray(table["class_eq"].combine_chunks().to_pylist(), dtype=object)
    if not np.all(np.isin(labels, ("CW", "CCW"))):
        raise ReproductionError("strict primary contains non-spiral labels")
    ra = table["ra_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    dec = table["dec_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    pix = hp.ang2pix(64, np.radians(90.0 - dec), np.radians(ra % 360.0))
    total = np.bincount(pix, minlength=hp.nside2npix(64))
    cw = np.bincount(pix[labels == "CW"], minlength=hp.nside2npix(64))
    support = total >= 10
    sky = np.full(total.size, hp.UNSEEN)
    sky[support] = (2.0 * cw[support] - total[support]) / total[support]
    monopole, vector = hp.fit_dipole(sky, gal_cut=0)
    amplitude = float(np.linalg.norm(vector))
    ra_dipole = float(np.degrees(np.arctan2(vector[1], vector[0])) % 360.0)
    dec_dipole = float(np.degrees(np.arcsin(vector[2] / amplitude)))

    null = np.load(null_array, allow_pickle=False)
    if null.shape != (10_000,):
        raise ReproductionError("strict null array must have shape (10000,)")
    null_mean = float(null.mean())
    null_std = float(null.std(ddof=0))
    z = float((amplitude - null_mean) / null_std)
    rank_k = int(np.count_nonzero(null >= amplitude))
    rank_p = float((rank_k + 1) / (null.size + 1))
    result = {
        "schema": "p4-primary-null-reproduction/v2",
        "paper_version": "v1.0.259",
        "status": "PASS",
        "selection": (
            "primary_hc == True and raw_flip_qc_unsafe == False; "
            "HEALPix NSIDE=64; N_spiral(pixel) >= 10"
        ),
        "n_selected": int(table.num_rows),
        "n_support": int(total[support].sum()),
        "n_pixels": int(support.sum()),
        "amplitude": amplitude,
        "monopole": float(monopole),
        "equatorial_ra_deg": ra_dipole,
        "equatorial_dec_deg": dec_dipole,
        "null": {
            "definition": (
                "10,000 fixed-occupancy galaxy-label randomizations using a "
                "multivariate-hypergeometric allocation over fixed pixel capacities"
            ),
            "array_sha256": NULL_SHA256,
            "mean": null_mean,
            "std_ddof0": null_std,
            "z_moment": z,
            "rank_k": rank_k,
            "rank_p_one_sided_upper_tail": rank_p,
            "rank_formula": "(k+1)/(N+1), k=count(A_null >= A_data)",
        },
        "interpretation_limits": [
            "post-review corrective analysis; not preregistered before unblinding",
            "observed-label descriptive isotropy null only",
            "not a calibrated physical or primordial amplitude bound",
        ],
    }
    observed = {
        "n_selected": result["n_selected"],
        "n_support": result["n_support"],
        "n_pixels": result["n_pixels"],
        "amplitude": amplitude,
        "monopole": float(monopole),
        "ra_deg": ra_dipole,
        "dec_deg": dec_dipole,
        "null_mean": null_mean,
        "null_std": null_std,
        "z": z,
        "rank_k": rank_k,
        "rank_p": rank_p,
    }
    checks = {
        key: (
            value == EXPECTED[key]
            if isinstance(value, int)
            else bool(np.isclose(value, EXPECTED[key], rtol=0, atol=1e-12))
        )
        for key, value in observed.items()
    }
    result["hard_gates"] = checks
    if not all(checks.values()):
        result["status"] = "FAIL"
        raise ReproductionError(json.dumps(result, indent=2, sort_keys=True))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--null-array", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = reproduce(args.catalog, args.null_array)
    except (OSError, ValueError, ReproductionError) as exc:
        print(f"FAIL: {exc}")
        return 1
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

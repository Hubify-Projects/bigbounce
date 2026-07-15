#!/usr/bin/env python3
"""Minimally reproduce the P4 v1.0.244 observed-label primary null.

This script consumes only the science-facing release Parquet and the retained
10,000-realization null array.  It does not use raw-pass or reconstructed
flip-pass scores, and it does not infer a physical or primordial amplitude.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import healpy as hp
import numpy as np
import pyarrow.compute as pc
import pyarrow.parquet as pq


HERE = Path(__file__).resolve().parent
DEFAULT_RELEASE = HERE / "apjs_release_v1.0.244"
DEFAULT_CATALOG = DEFAULT_RELEASE / "p4_catalog_primary_safe_v1.0.244.parquet"
DEFAULT_NULL = DEFAULT_RELEASE / "primary_null_amps_10000.npy"
NULL_SHA256 = "62bb1c019231974c2a7ed5d5e43ceb77a5596e4675c82d7ff1c899e029a36492"
NSIDE = 64
MIN_PIXEL_COUNT = 10
EXPECTED = {
    "n_primary_hc": 949_584,
    "n_pixels_inclusive": 23_682,
    "amplitude": 0.004597074287780104,
    "equatorial_ra_deg": 294.30537030397005,
    "equatorial_dec_deg": 16.029115977736286,
    "significance_sigma": 0.549120193418297,
    "rank_p_one_sided_upper_tail": 0.26517348265173485,
}


class ReproductionError(RuntimeError):
    """Raised when the declared primary contract cannot be reproduced."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def reproduce(catalog_path: Path, null_path: Path, enforce_expected: bool = True) -> dict:
    table = pq.read_table(
        catalog_path,
        columns=["ra_deg", "dec_deg", "class_eq", "primary_hc"],
        filters=[("primary_hc", "=", True)],
    )
    # The explicit filter result is checked even though a compliant product also
    # stores the primary_hc boolean. This keeps the executable selection visible.
    table = table.filter(pc.equal(table["primary_hc"], True))
    ra = table["ra_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    dec = table["dec_deg"].combine_chunks().to_numpy(zero_copy_only=False)
    labels = np.asarray(table["class_eq"].combine_chunks().to_pylist(), dtype=object)
    is_cw = labels == "CW"

    npix = hp.nside2npix(NSIDE)
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra % 360.0))
    cw = np.bincount(pix, weights=is_cw.astype(float), minlength=npix)
    ccw = np.bincount(pix, weights=(~is_cw).astype(float), minlength=npix)
    total = cw + ccw
    support = total >= MIN_PIXEL_COUNT
    sky = np.full(npix, hp.UNSEEN)
    sky[support] = (cw[support] - ccw[support]) / total[support]
    monopole, vector = hp.fit_dipole(sky, gal_cut=0)
    amplitude = float(np.linalg.norm(vector))
    ra_dipole = float(np.degrees(np.arctan2(vector[1], vector[0])) % 360.0)
    dec_dipole = float(np.degrees(np.arcsin(vector[2] / amplitude)))

    null_sha256 = sha256_file(null_path)
    null = np.load(null_path, allow_pickle=False)
    if null.shape != (10_000,):
        raise ReproductionError(f"primary null shape {null.shape}; expected (10000,)")
    null_mean = float(null.mean())
    null_std = float(null.std(ddof=0))
    sigma = float((amplitude - null_mean) / null_std)
    rank_k = int(np.count_nonzero(null >= amplitude))
    rank_p = float((rank_k + 1) / (null.size + 1))

    result = {
        "schema": "p4-primary-null-reproduction/v1",
        "paper_version": "v1.0.244",
        "status": "PASS",
        "scope": "observed equivariant hard labels; descriptive isotropy null only",
        "support": "HC_REALSPACE_INCLUSIVE",
        "selection": "primary_hc == True; HEALPix NSIDE=64; N_spiral(pixel) >= 10",
        "n_primary_hc": int(table.num_rows),
        "n_pixels_inclusive": int(support.sum()),
        "amplitude": amplitude,
        "equatorial_ra_deg": ra_dipole,
        "equatorial_dec_deg": dec_dipole,
        "monopole": float(monopole),
        "null": {
            "definition": "10,000 per-pixel asymmetry-value permutations on fixed HC_REALSPACE_INCLUSIVE support",
            "n_realizations": int(null.size),
            "array_sha256": null_sha256,
            "mean": null_mean,
            "std_ddof0": null_std,
            "significance_sigma": sigma,
            "rank_k": rank_k,
            "rank_p_one_sided_upper_tail": rank_p,
            "rank_formula": "(k+1)/(N+1), k=count(A_null >= A_data)",
        },
        "exclusions": [
            "no calibrated-probability claim",
            "no physical-amplitude or primordial bound",
            "no matched-external-estimator claim",
            "no formal-preregistration claim",
        ],
    }

    if enforce_expected:
        checks = {
            "n_primary_hc": result["n_primary_hc"] == EXPECTED["n_primary_hc"],
            "n_pixels_inclusive": result["n_pixels_inclusive"] == EXPECTED["n_pixels_inclusive"],
            "amplitude": bool(np.isclose(amplitude, EXPECTED["amplitude"], rtol=0, atol=1e-14)),
            "equatorial_ra_deg": bool(np.isclose(ra_dipole, EXPECTED["equatorial_ra_deg"], rtol=0, atol=1e-10)),
            "equatorial_dec_deg": bool(np.isclose(dec_dipole, EXPECTED["equatorial_dec_deg"], rtol=0, atol=1e-10)),
            "null_sha256": null_sha256 == NULL_SHA256,
            "significance_sigma": bool(np.isclose(sigma, EXPECTED["significance_sigma"], rtol=0, atol=1e-12)),
            "rank_p": bool(np.isclose(rank_p, EXPECTED["rank_p_one_sided_upper_tail"], rtol=0, atol=1e-15)),
        }
        result["hard_gates"] = checks
        if not all(checks.values()):
            result["status"] = "FAIL"
            raise ReproductionError(json.dumps(result, indent=2, sort_keys=True))
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--null-array", type=Path, default=DEFAULT_NULL)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = reproduce(args.catalog, args.null_array)
    except (OSError, ValueError, ReproductionError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

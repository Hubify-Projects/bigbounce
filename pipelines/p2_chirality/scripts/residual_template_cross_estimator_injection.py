#!/usr/bin/env python3
"""Inject the observed full-sample ell=1 remainder into the HC estimator.

This is a deliberately limited, map-level cross-estimator stress test.  It
reconstructs the full-sample observed l=1 vector on the systematic forward-
model mask, subtracts the committed imaging+DR8-morphology l=1 vector, turns
that residual vector back into a pure l=1 map, adds it to the primary HC
real-space asymmetry map, and repeats the canonical uniform-pixel
``healpy.fit_dipole`` fit.

It is not a joint covariance model, does not establish independence between
estimators, and does not turn the harmonic residual into a physical signal.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import healpy as hp
import numpy as np
import pyarrow.parquet as pq
from huggingface_hub import hf_hub_download


ROOT = Path(__file__).resolve().parents[3]
P4 = ROOT / "pipelines" / "p2_chirality"
FORWARD = P4 / "outputs" / "systematic_l1_forward_model_dr8morph.json"
OUT = P4 / "outputs" / "canonical_provenance" / "residual_template_cross_estimator_injection.json"
NSIDE = 64
NPIX = hp.nside2npix(NSIDE)


def canonical_galactic_mask() -> np.ndarray:
    theta, phi = hp.pix2ang(NSIDE, np.arange(NPIX))
    theta_g, _ = hp.Rotator(coord=["C", "G"])(theta, phi)
    return np.abs(90.0 - np.degrees(theta_g)) > 15.0


def pixel_map(pix: np.ndarray, is_cw: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = np.bincount(pix, minlength=NPIX).astype(np.float64)
    c = np.bincount(pix[is_cw], minlength=NPIX).astype(np.float64)
    a = np.zeros(NPIX, dtype=np.float64)
    good = n > 0
    a[good] = (2.0 * c[good] - n[good]) / n[good]
    return a, n


def centered_masked(a: np.ndarray, n: np.ndarray, use: np.ndarray) -> np.ndarray:
    out = np.zeros(NPIX, dtype=np.float64)
    mean = np.average(a[use], weights=n[use])
    out[use] = a[use] - mean
    return out


def alm_l1_vector(field: np.ndarray) -> np.ndarray:
    alm = hp.map2alm(field, lmax=2, iter=1)
    a10 = alm[hp.Alm.getidx(2, 1, 0)]
    a11 = alm[hp.Alm.getidx(2, 1, 1)]
    return np.array([-2.0 * np.real(a11), 2.0 * np.imag(a11), np.real(a10)], dtype=float)


def vector_to_l1_map(v: np.ndarray) -> np.ndarray:
    alm = np.zeros(hp.Alm.getsize(2), dtype=np.complex128)
    alm[hp.Alm.getidx(2, 1, 0)] = v[2]
    alm[hp.Alm.getidx(2, 1, 1)] = -0.5 * v[0] + 0.5j * v[1]
    return hp.alm2map(alm, NSIDE, lmax=2)


def primary_fit(field: np.ndarray, n: np.ndarray) -> dict:
    keep = n >= 10
    m = np.full(NPIX, hp.UNSEEN, dtype=np.float64)
    m[keep] = field[keep]
    mono, dip = hp.fit_dipole(m, gal_cut=0)
    return {
        "n_galaxies": int(n.sum()),
        "n_pixels": int(keep.sum()),
        "monopole": float(mono),
        "vector": [float(x) for x in dip],
        "amplitude": float(np.linalg.norm(dip)),
    }


def main() -> int:
    cat_path = hf_hub_download(
        "bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset"
    )
    tab = pq.read_table(
        cat_path, columns=["ra", "dec", "class_eq", "confidence_eq"]
    )
    ra = np.asarray(tab["ra"], dtype=np.float64)
    dec = np.asarray(tab["dec"], dtype=np.float64)
    cls = np.asarray(tab["class_eq"].to_pylist(), dtype=object)
    conf = np.asarray(tab["confidence_eq"], dtype=np.float64)
    pix_all = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra % 360.0))

    spiral = np.isin(cls, ["CW", "CCW"])
    full_a, full_n = pixel_map(pix_all[spiral], cls[spiral] == "CW")
    gmask = canonical_galactic_mask()
    full_use = gmask & (full_n > 0)
    full_l1 = alm_l1_vector(centered_masked(full_a, full_n, full_use))

    forward = json.loads(FORWARD.read_text())
    sv = forward["extended_forward_model"]["l1_vector"]
    sys_l1 = np.array([sv["cx"], sv["cy"], sv["cz"]], dtype=float)
    vector_residual_l1 = full_l1 - sys_l1
    scalar_remainder_fraction = float(forward["improvement"]["un_modelled_remainder"])
    scalar_remainder_l1 = scalar_remainder_fraction * full_l1

    hc = spiral & (conf > 0.6)
    hc_a, hc_n = pixel_map(pix_all[hc], cls[hc] == "CW")
    baseline = primary_fit(hc_a, hc_n)
    full_injected = primary_fit(hc_a + vector_to_l1_map(full_l1), hc_n)
    scalar_remainder_injected = primary_fit(
        hc_a + vector_to_l1_map(scalar_remainder_l1), hc_n
    )
    vector_remainder_injected = primary_fit(
        hc_a + vector_to_l1_map(vector_residual_l1), hc_n
    )

    def effect(fit: dict) -> dict:
        return {
            **fit,
            "amplitude_change": fit["amplitude"] - baseline["amplitude"],
            "amplitude_ratio": fit["amplitude"] / baseline["amplitude"],
        }

    result = {
        "script": "scripts/residual_template_cross_estimator_injection.py",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": "Observed 47%-remainder map-level cross-estimator stress test on the primary HC real-space estimator.",
        "inputs": {
            "catalog": "bamfai/galaxy-chirality-catalog/catalog_production.parquet",
            "forward_model": str(FORWARD.relative_to(ROOT)),
            "nside": NSIDE,
            "full_sample_mask": "|b|>15 degrees and occupied full-sample pixels, matching the forward-model reconstruction",
            "primary_hc_mask": "p_eq>0.6 hard CW/CCW; pixels with N_spiral>=10",
        },
        "full_sample_l1": {
            "observed_vector": [float(x) for x in full_l1],
            "observed_amplitude": float(np.linalg.norm(full_l1)),
            "forward_model_vector": [float(x) for x in sys_l1],
            "forward_model_amplitude": float(np.linalg.norm(sys_l1)),
            "scalar_47pct_remainder_vector": [float(x) for x in scalar_remainder_l1],
            "scalar_47pct_remainder_amplitude": float(np.linalg.norm(scalar_remainder_l1)),
            "scalar_remainder_fraction": scalar_remainder_fraction,
            "vector_subtraction_remainder_vector": [float(x) for x in vector_residual_l1],
            "vector_subtraction_remainder_amplitude": float(np.linalg.norm(vector_residual_l1)),
            "vector_subtraction_fraction_of_observed_amplitude": float(
                np.linalg.norm(vector_residual_l1) / np.linalg.norm(full_l1)
            ),
            "remainder_definition_note": (
                "The committed 47% is one minus the scalar forward-model/observed amplitude ratio. "
                "Direct vector subtraction leaves 62.3% because the two vectors are not parallel; "
                "both definitions are stress-tested below rather than conflated."
            ),
        },
        "hc_real_space": {
            "baseline": baseline,
            "after_full_observed_l1_injection": effect(full_injected),
            "after_scalar_47pct_remainder_injection": effect(scalar_remainder_injected),
            "after_vector_subtraction_remainder_injection": effect(vector_remainder_injected),
        },
        "scope_limit": (
            "This is a deterministic pure-l=1 map injection of the observed full-sample remainder. "
            "It is not a joint real-space x harmonic covariance likelihood, does not assert estimator "
            "independence, and does not identify the remainder as cosmological or physical."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["hc_real_space"], indent=2))
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

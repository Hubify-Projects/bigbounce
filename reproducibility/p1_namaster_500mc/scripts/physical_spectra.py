"""Pinned physical CMB spectra for the P1B NaMaster simulations.

CAMB returns the lensed-scalar spectra in raw :math:`C_ell` units when
``raw_cl=True``.  Keeping spectrum generation and validation in this small
module prevents a plotted :math:`D_ell` spectrum from being passed to
``healpy.synfast`` as though it were raw :math:`C_ell`.
"""

from __future__ import annotations

import hashlib
import os
from functools import lru_cache

import numpy as np


EXPECTED_CAMB_VERSION = "1.6.6"
CAMB_PARAMETERS = {
    "H0_km_s_Mpc": 67.36,
    "ombh2": 0.02237,
    "omch2": 0.1200,
    "omk": 0.0,
    "mnu_eV": 0.06,
    "tau": 0.0544,
    "As": 2.1e-9,
    "ns": 0.9649,
    "lens_potential_accuracy": 1,
}
SPECTRUM_CONTRACT = {
    "camb_collection": "lensed_scalar",
    "camb_unit": "muK",
    "raw_cl": True,
    "healpy_synfast_order": ["TT", "EE", "BB", "TE"],
    "array_dtype_for_hash": "little-endian float64",
}


def _sha256_array(values: np.ndarray) -> str:
    canonical = np.ascontiguousarray(values, dtype="<f8")
    digest = hashlib.sha256()
    digest.update(str(canonical.shape).encode("ascii"))
    digest.update(b"\0")
    digest.update(canonical.tobytes(order="C"))
    return digest.hexdigest()


def _version_is_allowed(actual: str, require_pinned_version: bool) -> None:
    if actual == EXPECTED_CAMB_VERSION or not require_pinned_version:
        return
    if os.environ.get("NAMASTER_ALLOW_UNPINNED_CAMB") == "1":
        return
    raise RuntimeError(
        "CAMB version mismatch: production requires "
        f"{EXPECTED_CAMB_VERSION}, found {actual}. Install requirements.txt. "
        "NAMASTER_ALLOW_UNPINNED_CAMB=1 is permitted only for bounded tests."
    )


def validate_raw_lensed_spectra(cl_ee: np.ndarray, cl_bb: np.ndarray) -> dict:
    """Fail closed on D_ell-as-C_ell scale mistakes and BB proxies."""
    ee = np.asarray(cl_ee, dtype=float)
    bb = np.asarray(cl_bb, dtype=float)
    if ee.ndim != 1 or bb.shape != ee.shape or len(ee) < 201:
        raise ValueError("EE/BB must be equal-length one-dimensional spectra through ell=200")
    if not np.all(np.isfinite(ee)) or not np.all(np.isfinite(bb)):
        raise ValueError("EE/BB spectra contain non-finite values")
    if np.any(ee < 0) or np.any(bb < 0) or np.any(ee[:2] != 0) or np.any(bb[:2] != 0):
        raise ValueError("raw lensed EE/BB must be non-negative with ell=0,1 set to zero")

    ell_check = 140
    factor = ell_check * (ell_check + 1) / (2 * np.pi)
    d140 = factor * ee[ell_check]
    if not (0.05 < d140 < 10.0) or ee[ell_check] >= 0.05:
        raise ValueError(
            "EE raw-C_ell scale contract failed at ell=140; possible D_ell-as-C_ell input: "
            f"C_140={ee[ell_check]:.9g}, D_140={d140:.9g} microK^2"
        )
    positive = (ee[30:201] > 0) & (bb[30:201] > 0)
    if np.count_nonzero(positive) < 100:
        raise ValueError("lensed BB must be positive across the analysis band")
    ratios = bb[30:201][positive] / ee[30:201][positive]
    if np.allclose(bb, 0.05 * ee, rtol=1e-10, atol=0.0) or np.ptp(ratios) < 1e-4:
        raise ValueError("BB failed physical-shape contract; a fixed fraction of EE is not lensed BB")
    return {
        "ell_scale_check": ell_check,
        "raw_cl_ee_at_ell_check_uK2": float(ee[ell_check]),
        "d_ell_ee_at_ell_check_uK2": float(d140),
        "bb_to_ee_ratio_min_ell30_200": float(np.min(ratios)),
        "bb_to_ee_ratio_max_ell30_200": float(np.max(ratios)),
        "status": "pass",
    }


@lru_cache(maxsize=8)
def _cached_spectra(lmax: int, require_pinned_version: bool):
    import camb

    _version_is_allowed(camb.__version__, require_pinned_version)
    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=CAMB_PARAMETERS["H0_km_s_Mpc"],
        ombh2=CAMB_PARAMETERS["ombh2"],
        omch2=CAMB_PARAMETERS["omch2"],
        omk=CAMB_PARAMETERS["omk"],
        mnu=CAMB_PARAMETERS["mnu_eV"],
        tau=CAMB_PARAMETERS["tau"],
    )
    pars.InitPower.set_params(As=CAMB_PARAMETERS["As"], ns=CAMB_PARAMETERS["ns"])
    pars.set_for_lmax(lmax, lens_potential_accuracy=CAMB_PARAMETERS["lens_potential_accuracy"])
    results = camb.get_results(pars)
    spectra = results.get_cmb_power_spectra(
        pars,
        CMB_unit=SPECTRUM_CONTRACT["camb_unit"],
        raw_cl=SPECTRUM_CONTRACT["raw_cl"],
    )[SPECTRUM_CONTRACT["camb_collection"]]
    if spectra.shape[0] < lmax + 1:
        raise RuntimeError(f"CAMB returned only {spectra.shape[0]} multipoles for lmax={lmax}")
    ee = np.asarray(spectra[: lmax + 1, 1], dtype=float).copy()
    bb = np.asarray(spectra[: lmax + 1, 2], dtype=float).copy()
    ee[:2] = 0.0
    bb[:2] = 0.0
    validation = validate_raw_lensed_spectra(ee, bb)
    metadata = {
        "generator": "CAMB",
        "expected_camb_version": EXPECTED_CAMB_VERSION,
        "resolved_camb_version": camb.__version__,
        "production_version_match": camb.__version__ == EXPECTED_CAMB_VERSION,
        "parameters": dict(CAMB_PARAMETERS),
        "contract": dict(SPECTRUM_CONTRACT),
        "lmax": int(lmax),
        "sha256": {
            "cl_ee_raw_uK2": _sha256_array(ee),
            "cl_bb_raw_uK2": _sha256_array(bb),
        },
        "validation": validation,
    }
    return ee, bb, metadata


def load_camb_lensed_spectra(lmax: int, require_pinned_version: bool = True):
    """Return independent EE/BB arrays plus JSON-serializable provenance."""
    if int(lmax) != lmax or lmax < 200:
        raise ValueError("lmax must be an integer >= 200 for the physical spectrum contract")
    ee, bb, metadata = _cached_spectra(int(lmax), bool(require_pinned_version))
    return ee.copy(), bb.copy(), {**metadata, "sha256": dict(metadata["sha256"])}

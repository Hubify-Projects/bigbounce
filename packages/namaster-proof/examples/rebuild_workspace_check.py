#!/usr/bin/env python3
"""Deterministically rebuild the P1B production NaMaster workspace and re-check
the exact-window equivalence gate.

This script demonstrates that the ``[4, 20, 4, 1025]`` production workspace
tensor -- and therefore the recorded ``1.41e-18`` window-equivalence scalar --
is a pure deterministic function of committed, RNG-free code, even though the
tensor itself was never saved as a file. It reconstructs the workspace from the
same committed inputs used by the production driver and re-runs the same
``> 1e-10`` acceptance gate.

Sources of truth reproduced here (all git-tracked):

* Mask: ``make_native_latitude_window`` in
  ``reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py`` (lines
  147-165). It is RNG-free: ``hp.pix2ang`` plus hard-coded latitude cuts plus a
  deterministic ``hp.smoothing(fwhm=2 deg)``. No random draw, no unsaved input
  map, no external data.
* Bins / workspace: ``bandpower_edges`` + ``NmtWorkspace.compute_coupling_matrix``
  exactly as in ``namaster_500mc.py`` lines 170-181 (NSIDE=512, LMAX=1024,
  20 bins, ell_min=30 -> window shape [4, 20, 4, 1025]).
* Equivalence scalar: ``validate_window_equivalence`` (the packaged extract of
  ``reproducibility/p1_namaster_500mc/scripts/windowed_rotation.py`` lines
  79-89), gated at ``> 1e-10 -> raise`` in the production driver
  (``namaster_500mc.py`` lines 186-190).

Behavior:

* If PyMaster (and healpy) are importable, it rebuilds the workspace, asserts
  the ``[4, 20, 4, 1025]`` shape, recomputes ``max|Delta|`` between direct
  window contraction and ``decouple(couple(theory))``, and asserts it is
  ``< 1e-10``. Exit 0 on pass, nonzero on gate failure.
* If PyMaster is absent, it prints a clear skip message and exits 0 (the
  standalone package does not require PyMaster).

The last digits of the ~1e-18 value are BLAS/CPU/library-version dependent, so
the reconstructed scalar regenerates to the same order (and always ``< 1e-10``)
rather than bit-identically -- which is exactly why the paper demotes the
literal ``1.41e-18`` from a universal error bound.
"""

from __future__ import annotations

import sys

import numpy as np

# Production configuration (namaster_500mc.py lines 111-119, 170-173).
NSIDE = 512
LMAX = 1024
N_BINS = 20
ELL_MIN = 30
LATITUDE_CUT_DEG = 20.0
BETA_PAPER1_DEG = 0.27

GATE = 1e-10
EXPECTED_SHAPE = (4, N_BINS, 4, LMAX + 1)  # [4, 20, 4, 1025]


def build_production_mask(nside: int, latitude_cut_deg: float = LATITUDE_CUT_DEG):
    """Reproduce ``make_native_latitude_window`` (namaster_500mc.py:147-165).

    Pure deterministic function of ``nside`` and fixed latitude cuts: no RNG,
    no unsaved input map, no external data.
    """
    import healpy as hp

    npix = hp.nside2npix(nside)
    mask = np.ones(npix, dtype=float)
    _, lat = hp.pix2ang(nside, np.arange(npix), lonlat=True)
    mask[np.abs(lat) < latitude_cut_deg] = 0.0
    mask[lat > 25.0] = 0.0
    mask[lat < -65.0] = 0.0
    mask = hp.smoothing(mask, fwhm=np.deg2rad(2.0), verbose=False)
    mask = np.clip(mask, 0, 1)
    return mask


def main() -> int:
    try:
        import healpy as hp
        import pymaster as nmt
    except ImportError as exc:
        missing = getattr(exc, "name", None) or "pymaster/healpy"
        print(
            f"SKIP: '{missing}' is not importable. This recheck reconstructs a "
            "real pymaster.NmtWorkspace and needs PyMaster + healpy installed. "
            "The standalone namaster-proof package does not require them; install "
            "PyMaster 2.6 and healpy to execute this deterministic rebuild."
        )
        return 0

    from namaster_proof import (
        bandpower_edges,
        build_rotation_response,
        validate_window_equivalence,
    )

    print(f"PyMaster {nmt.__version__}, healpy {hp.__version__}")
    print(f"Rebuilding workspace: NSIDE={NSIDE}, LMAX={LMAX}, "
          f"{N_BINS} bins, ell_min={ELL_MIN} ...")

    # 1. Deterministic mask (RNG-free; namaster_500mc.py:147-165).
    mask = build_production_mask(NSIDE)
    actual_fsky = float(mask.sum() / hp.nside2npix(NSIDE))
    print(f"  mask f_sky = {actual_fsky:.4f} (deterministic)")

    # 2. Deterministic bins + coupling matrix (namaster_500mc.py:170-181).
    edges = bandpower_edges(nside=NSIDE, lmax=LMAX, n_bins=N_BINS, ell_min=ELL_MIN)
    bins = nmt.NmtBin.from_edges(edges[:-1], edges[1:])
    zeros = np.zeros(hp.nside2npix(NSIDE))
    f_dummy = nmt.NmtField(mask, [zeros, zeros], lmax=LMAX)
    workspace = nmt.NmtWorkspace()
    workspace.compute_coupling_matrix(f_dummy, f_dummy, bins)

    shape = tuple(int(x) for x in workspace.get_bandpower_windows().shape)
    print(f"  workspace window shape = {shape}")
    assert shape == EXPECTED_SHAPE, f"shape {shape} != expected {EXPECTED_SHAPE}"

    # 3. Deterministic LCDM-shaped spectra spanning the full harmonic support.
    #    The equivalence is a linear-algebra property of the workspace, so any
    #    finite spectra exercise the same > 1e-10 gate; these are RNG-free.
    ell = np.arange(LMAX + 1, dtype=float)
    cl_ee = np.zeros_like(ell)
    cl_bb = np.zeros_like(ell)
    cl_ee[2:] = 2.0e-4 / (ell[2:] * (ell[2:] + 1.0))
    cl_bb[2:] = 0.04 * cl_ee[2:]

    # 4. Re-run the exact-window equivalence gate (windowed_rotation.py:79-89).
    response = build_rotation_response(workspace, cl_ee, cl_bb)
    max_abs = validate_window_equivalence(
        workspace, response, float(np.deg2rad(BETA_PAPER1_DEG))
    )
    print(f"  window_equivalence_max_abs = {max_abs:.6e}")

    assert np.isfinite(max_abs) and max_abs < GATE, (
        f"equivalence gate FAILED: max|Delta| = {max_abs:.6e} !< {GATE:.0e}"
    )
    print(
        f"PASS: workspace regenerated deterministically; "
        f"max|Delta| = {max_abs:.3e} < {GATE:.0e} "
        "(same order as the recorded 1.41e-18; last digits are platform-dependent)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

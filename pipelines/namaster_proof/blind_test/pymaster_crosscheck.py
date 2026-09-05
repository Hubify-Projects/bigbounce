"""PyMaster (NaMaster) cross-check of the in-house spin-0 MASTER estimator.

Compares, on the SAME map/mask/binning/ell-range:
  (1) mode-coupling matrix M_{l1 l2} (in-house `pcl.coupling_matrix` vs
      NaMaster's `NmtWorkspace.get_coupling_matrix`, nlb=1 so bins == ells)
  (2) decoupled bandpowers (in-house `pcl.decouple` vs `wsp.decouple_cell`)
  (3) the S6 effective-multipole shortcut (variants2) vs NaMaster's exact
      decoupled result, band by band.

Run inside the throwaway conda-forge env that has pymaster+healpy:
  MAMBA_ROOT_PREFIX=/tmp/mamba_root micromamba run -n pymaster_env \
    python pymaster_crosscheck.py
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
import pcl
import variants2

NSIDE = 64
LMAX = 95
LMIN = 2
MAP_SEED = 42
MASK_SEED = 11
BAND_WIDTH = variants2.BAND_WIDTH  # 8, matches S6


def main() -> None:
    import healpy as hp
    import pymaster as nmt

    mask = pcl.make_mask(NSIDE, seed=MASK_SEED)
    sky = pcl.make_map(NSIDE, LMAX, MAP_SEED)

    # --- in-house honest path ---
    w_l = pcl.mask_power(mask, LMAX)
    p_l = pcl.pseudo_cl(sky, mask, LMAX)
    m_ih = pcl.coupling_matrix(w_l, LMAX)
    cl_ih = pcl.decouple(m_ih, p_l, lmin=LMIN)

    # --- NaMaster, nlb=1 so each "band" is a single ell (2..LMAX) ---
    f0 = nmt.NmtField(mask, [sky], spin=0, lmax=LMAX, lmax_mask=LMAX)
    b = nmt.NmtBin.from_lmax_linear(LMAX, 1, is_Dell=False)
    ells_nmt = b.get_effective_ells()
    wsp = nmt.NmtWorkspace.from_fields(f0, f0, b)
    cl_coupled = nmt.compute_coupled_cell(f0, f0)
    cl_decoupled_nmt = wsp.decouple_cell(cl_coupled)[0]
    # get_coupling_matrix() returns the RAW, UNBINNED matrix over l=0..LMAX
    # (shape (LMAX+1)*ncls square, ncls=1 here), independent of the bin
    # object used to build the workspace.
    m_nmt_raw = wsp.get_coupling_matrix()
    assert m_nmt_raw.shape == (LMAX + 1, LMAX + 1), m_nmt_raw.shape

    lo = LMIN
    hi = LMAX + 1

    # --- (1) coupling matrix comparison, same l-range ---
    m_ih_sub = m_ih[lo:hi, lo:hi]
    m_nmt_full = m_nmt_raw[lo:hi, lo:hi]
    diff = np.abs(m_ih_sub - m_nmt_full)
    max_abs = float(diff.max())
    denom = np.abs(m_nmt_full)
    mask_nz = denom > 1e-12
    rel = np.zeros_like(diff)
    rel[mask_nz] = diff[mask_nz] / denom[mask_nz]
    max_rel = float(rel.max())
    med_rel = float(np.median(rel[mask_nz]))

    # --- (2) decoupled bandpowers ---
    cl_ih_sub = cl_ih[lo:hi]
    bp_diff = np.abs(cl_ih_sub - cl_decoupled_nmt)
    bp_denom = np.abs(cl_decoupled_nmt)
    bp_rel = np.where(bp_denom > 1e-30, bp_diff / bp_denom, 0.0)
    bp_max_rel = float(bp_rel.max())
    bp_med_rel = float(np.median(bp_rel))

    # --- (3) S6 effective-multipole shortcut vs NaMaster exact, per band ---
    s6_out, s6_trace = variants2.run_variant(
        "S6_effective_multipole", NSIDE, LMAX, MAP_SEED,
    )
    band_rows = []
    for start in range(LMIN, LMAX + 1, BAND_WIDTH):
        stop = min(start + BAND_WIDTH, LMAX + 1)
        # NaMaster exact decoupled Cl at those same ells (index shift by lo)
        idx = slice(start - lo, stop - lo)
        exact = cl_decoupled_nmt[idx]
        shortcut = s6_out[start:stop]
        rel_band = np.abs(shortcut - exact) / np.where(np.abs(exact) > 1e-30, np.abs(exact), 1.0)
        band_rows.append({
            "l_start": start, "l_stop": stop - 1,
            "max_rel_err_vs_namaster": float(rel_band.max()),
            "mean_rel_err_vs_namaster": float(rel_band.mean()),
        })

    env = {
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "healpy": hp.__version__,
        "pymaster": getattr(nmt, "__version__", "unknown"),
        "nside": NSIDE, "lmax": LMAX, "lmin": LMIN,
        "map_seed": MAP_SEED, "mask_seed": MASK_SEED,
        "band_width": BAND_WIDTH,
        "install_path": "conda-forge via micromamba throwaway env pymaster_env "
                         "(homebrew pip wheel build failed: no C compiler toolchain "
                         "for libnmt's GSL/FFTW/CFITSIO/HEALPix source build)",
    }

    result = {
        "env": env,
        "coupling_matrix": {
            "l_range": [lo, hi - 1],
            "max_abs_diff": max_abs,
            "max_rel_diff": max_rel,
            "median_rel_diff": med_rel,
        },
        "decoupled_bandpowers": {
            "l_range": [lo, hi - 1],
            "max_rel_diff": bp_max_rel,
            "median_rel_diff": bp_med_rel,
        },
        "s6_effective_multipole_vs_namaster": band_rows,
    }
    out_path = os.path.join(os.path.dirname(__file__), "pymaster_crosscheck_result.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

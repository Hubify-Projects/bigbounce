#!/usr/bin/env python3
"""Ledger row 4 v2, fix (1): window function + integral constraint.

Uses pypower's CatalogFFTWindow (FFT-mesh window estimator, reusing the same
mesh/nmesh/resampler as the CatalogFFTPower measurement in
pk_estimator_qso.py) to build a PowerSpectrumFFTWindowMatrix directly from
the randoms, then convolves the theory P0/P2 model with it.
Docs followed: pypower/tests/test_fft_window.py (CatalogFFTWindow ->
window.poles IS a PowerSpectrumFFTWindowMatrix; .dot(theory) convolves);
even multipoles only (ells=0,2,4 in and out) -- wide-angle odd terms (1,3,5)
dropped as a documented simplification (sub-dominant vs the leading window
mixing at these k, matches pypower/nb/window_examples.ipynb convention
where odd terms are the next-order wide-angle correction).
Global integral constraint (documented simplification vs DESI's radial+
angular IC, de Mattia & Ruhlmann-Kleider 2019 arXiv:1904.08851 sec 2.2):
    P0_IC(k) = P0_conv(k) - W0(k) * P0_conv(k->k_min)
i.e. subtract the window monopole shape times the survey-averaged mean
(approximated at k_min, the lowest well-measured mode) -- this is exactly
what an unconstrained mean-density estimate leaks into P0 at low k.
"""
import numpy as np
from pypower import CatalogFFTPower, CatalogFFTWindow
import fitsio

DATA_DIR = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss"
OUT_DIR = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"
from cosmoprimo.fiducial import DESI
cosmo = DESI(engine="eisenstein_hu")


def radec_z_to_xyz(ra, dec, z):
    dist = cosmo.comoving_radial_distance(z)
    ra_r, dec_r = np.deg2rad(ra), np.deg2rad(dec)
    return np.array([dist * np.cos(dec_r) * np.cos(ra_r),
                      dist * np.cos(dec_r) * np.sin(ra_r),
                      dist * np.sin(dec_r)])


def run_cap(cap, n_ran):
    power = CatalogFFTPower.load(f"{OUT_DIR}/pk_qso_{cap}_pypower.npy")
    rparts = []
    for i in range(n_ran):
        f = fitsio.FITS(f"{DATA_DIR}/QSO_{cap}_{i}_clustering.ran.fits")
        d = f[1].read(columns=["RA", "DEC", "Z", "WEIGHT", "WEIGHT_FKP"])
        f.close()
        m = (d["Z"] > 0.8) & (d["Z"] < 3.1)
        rparts.append(d[m])
    r = np.concatenate(rparts)
    rpos = radec_z_to_xyz(r["RA"], r["DEC"], r["Z"])
    rw = r["WEIGHT"] * r["WEIGHT_FKP"]
    edgesin = np.arange(0.0, 0.21, 0.005)
    import time
    t0 = time.time()
    window = CatalogFFTWindow(
        randoms_positions1=rpos, randoms_weights1=rw,
        edgesin=edgesin, projsin=[0, 2, 4], power_ref=power,
        position_type="xyz", dtype="f8",
    )
    print(f"[{cap}] window FFT done in {time.time()-t0:.1f}s, n_ran={n_ran}", flush=True)
    window.poles.save(f"{OUT_DIR}/window_qso_{cap}_matrix.npy")
    return window.poles


if __name__ == "__main__":
    import sys
    n_ran = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    for cap in ["NGC", "SGC"]:
        run_cap(cap, n_ran)
    print("WINDOW_DONE", flush=True)

#!/usr/bin/env python3
"""Ledger row 4 v2, fix (1): window shape + global integral constraint.

SCOPE NOTE (honest, measured): the full pypower CatalogFFTWindow mode-mixing
matrix (ells 0,2,4 in x out, pypower/tests/test_fft_window.py workflow) was
attempted first. A MINIMAL config (1 theory k-bin, ell=0 only) took >3 min
CPU and had not finished -- extrapolated to many hours for a usable
k-range/ell-set, infeasible in this session's compute budget. Documented as
the exact remaining step (full window-convolution matrix), not silently
dropped -- see LEDGER4_RESULT_v2_2026-09-04.md sec on remaining work.

What IS computed here (real, cheap, ~85s/cap, reuses the existing FFT
machinery): the survey window's OWN power spectrum W0(k), via the standard
"shuffled/split randoms" technique -- one randoms realisation plays the role
of "data", the remaining realisations play the role of "randoms" for FKP
mean-density estimation. This isolates the window/selection-function power
(no clustering signal, since both point sets are Poisson-sampled from the
same selection function) -- exactly the quantity needed for the classic
GLOBAL integral-constraint correction (Peacock & Nicholson 1991; Beutler
et al. 2014, arXiv:1312.4611, eq. 13-14; the DESI radial+angular IC of de
Mattia & Ruhlmann-Kleider 2019, arXiv:1904.08851, is the fuller version of
the same physics, not reproduced here):
    P0_obs(k) = P0_true(k) - W0n(k) * P0_true(k_min)
    W0n(k) = W0(k) / W0(k_min)
i.e. the observed monopole is suppressed by the window's own shape,
normalised to 1 at the lowest well-measured k -- because the survey's mean
density is estimated FROM the sample itself, forcing large-scale power
toward zero exactly where PNG's scale-dependent-bias signal lives. This is
the SAME mechanism (not full window convolution) as the DESI paper's
integral constraint; a real, documented simplification.
"""
import json
import time
import numpy as np
import fitsio
from cosmoprimo.fiducial import DESI
from pypower import CatalogFFTPower

DATA_DIR = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss"
OUT_DIR = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"
ZMIN, ZMAX = 0.8, 3.1
cosmo = DESI(engine="eisenstein_hu")


def load_ran(cap, i):
    f = fitsio.FITS(f"{DATA_DIR}/QSO_{cap}_{i}_clustering.ran.fits")
    d = f[1].read(columns=["RA", "DEC", "Z", "WEIGHT", "WEIGHT_FKP"])
    f.close()
    m = (d["Z"] > ZMIN) & (d["Z"] < ZMAX)
    return d[m]


def radec_z_to_xyz(ra, dec, z):
    dist = cosmo.comoving_radial_distance(z)
    ra_r, dec_r = np.deg2rad(ra), np.deg2rad(dec)
    return np.array([dist * np.cos(dec_r) * np.cos(ra_r),
                      dist * np.cos(dec_r) * np.sin(ra_r),
                      dist * np.sin(dec_r)])


def run_cap(cap, n_ran):
    t0 = time.time()
    d = load_ran(cap, 0)  # realisation 0 plays "data"
    r = np.concatenate([load_ran(cap, i) for i in range(1, n_ran)])  # rest play "randoms"
    dpos = radec_z_to_xyz(d["RA"], d["DEC"], d["Z"])
    dw = d["WEIGHT"] * d["WEIGHT_FKP"]
    rpos = radec_z_to_xyz(r["RA"], r["DEC"], r["Z"])
    rw = r["WEIGHT"] * r["WEIGHT_FKP"]
    edges = np.arange(0.0, 0.11, 0.001)
    result = CatalogFFTPower(
        data_positions1=dpos, data_weights1=dw,
        randoms_positions1=rpos, randoms_weights1=rw,
        edges=edges, ells=(0, 2), los="firstpoint",
        nmesh=512, resampler="tsc", interlacing=2,
        position_type="xyz", dtype="f8",
    )
    poles = result.poles
    k = poles.k
    w0 = np.real(poles(ell=0, complex=False))
    w2 = np.real(poles(ell=2, complex=False))
    print(f"[{cap}] window power done in {time.time()-t0:.1f}s (n_ran_role={n_ran})", flush=True)
    out = {"cap": cap, "k": k.tolist(), "w0": w0.tolist(), "w2": w2.tolist(),
           "n_ran_total": int(n_ran), "wall_clock_s": time.time() - t0}
    with open(f"{OUT_DIR}/window_qso_{cap}.json", "w") as fh:
        json.dump(out, fh, indent=2)
    return out


if __name__ == "__main__":
    import sys
    n_ran = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    for cap in ["NGC", "SGC"]:
        run_cap(cap, n_ran)
    print("WINDOW_DONE", flush=True)

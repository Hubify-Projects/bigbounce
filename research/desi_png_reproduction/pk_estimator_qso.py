#!/usr/bin/env python3
"""Ledger row 4, step 3: pypower P_ell(k) estimator on DESI DR1 QSO (LSScats
v1.5), NGC + SGC separately, then a number-weighted combination.

Plan: research/desi_png_reproduction/LEDGER4_DESI_PNG_PLAN_2026-09-03.md
sec 3.1 (Track 1, pypower fidelity estimator), 3.2 (fit range 0.003-0.08
h/Mpc), 3.3 (window from randoms).

Cosmology: DESI fiducial flat LCDM (h=0.6736, Om=0.3137721), matching the
DESI DR1 LSS catalogue convention, via cosmoprimo with the eisenstein_hu
transfer engine (CLASS unavailable in this environment - see RUN_LOG.md
step 1). RA/DEC/Z -> comoving Cartesian via cosmoprimo's comoving distance.

Randoms: 4 realisations per cap (0-3), concatenated (RUN_LOG.md step 2 -
documented fidelity reduction from the plan's full 18/cap).
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
N_RAN = int(__import__("os").environ.get("PK_N_RAN", "4"))  # realisations 0..N_RAN-1 per cap

cosmo = DESI(engine="eisenstein_hu")


def load_cat(path, zmin, zmax, is_random=False):
    f = fitsio.FITS(path)
    d = f[1].read(columns=["RA", "DEC", "Z", "WEIGHT", "WEIGHT_FKP"])
    f.close()
    m = (d["Z"] > zmin) & (d["Z"] < zmax)
    d = d[m]
    return d


def radec_z_to_xyz(ra, dec, z):
    dist = cosmo.comoving_radial_distance(z)  # Mpc/h
    ra_rad = np.deg2rad(ra)
    dec_rad = np.deg2rad(dec)
    x = dist * np.cos(dec_rad) * np.cos(ra_rad)
    y = dist * np.cos(dec_rad) * np.sin(ra_rad)
    z_ = dist * np.sin(dec_rad)
    return np.array([x, y, z_])


def run_cap(cap):
    t0 = time.time()
    dpath = f"{DATA_DIR}/QSO_{cap}_clustering.dat.fits"
    d = load_cat(dpath, ZMIN, ZMAX)
    dpos = radec_z_to_xyz(d["RA"], d["DEC"], d["Z"])
    dw = d["WEIGHT"] * d["WEIGHT_FKP"]

    rparts = []
    for i in range(N_RAN):
        rpath = f"{DATA_DIR}/QSO_{cap}_{i}_clustering.ran.fits"
        rparts.append(load_cat(rpath, ZMIN, ZMAX))
    r = np.concatenate(rparts)
    rpos = radec_z_to_xyz(r["RA"], r["DEC"], r["Z"])
    rw = r["WEIGHT"] * r["WEIGHT_FKP"]

    print(f"[{cap}] data N={len(d)}, randoms N={len(r)} ({N_RAN} reals), "
          f"load {time.time()-t0:.1f}s", flush=True)

    edges = np.arange(0.0, 0.31, 0.001)
    t1 = time.time()
    result = CatalogFFTPower(
        data_positions1=dpos, data_weights1=dw,
        randoms_positions1=rpos, randoms_weights1=rw,
        edges=edges, ells=(0, 2, 4), los="firstpoint",
        nmesh=512, resampler="tsc", interlacing=2,
        position_type="xyz", dtype="f8",
    )
    print(f"[{cap}] FFTPower done in {time.time()-t1:.1f}s", flush=True)

    poles = result.poles
    out = {
        "cap": cap,
        "k": poles.k.tolist(),
        "power_0": np.real(poles(ell=0, complex=False)).tolist(),
        "power_2": np.real(poles(ell=2, complex=False)).tolist(),
        "power_4": np.real(poles(ell=4, complex=False)).tolist(),
        "nmodes": poles.nmodes.tolist(),
        "shotnoise": float(poles.shotnoise),
        "n_data": int(len(d)),
        "n_randoms": int(len(r)),
        "n_randoms_realisations": N_RAN,
        "wall_clock_s": time.time() - t0,
    }
    np.save(f"{OUT_DIR}/pk_qso_{cap}_nran{N_RAN}_poles.npy",
            np.array([out["k"], out["power_0"], out["power_2"], out["power_4"]]))
    with open(f"{OUT_DIR}/pk_qso_{cap}_nran{N_RAN}.json", "w") as fh:
        json.dump(out, fh, indent=2)
    result.save(f"{OUT_DIR}/pk_qso_{cap}_nran{N_RAN}_pypower.npy")
    print(f"[{cap}] saved. total {time.time()-t0:.1f}s", flush=True)
    return out


if __name__ == "__main__":
    import sys
    caps = sys.argv[1:] or ["NGC", "SGC"]
    for cap in caps:
        run_cap(cap)
    print("ALL_CAPS_DONE", flush=True)

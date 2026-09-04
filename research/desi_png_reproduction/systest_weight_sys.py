#!/usr/bin/env python3
"""Ledger row 4 step 5, test 1 (plan sec 3.4): WEIGHT_SYS on/off null split.
Reruns the QSO P0/P2 estimator with WEIGHT_SYS divided out of the total
catalogue weight, holding everything else (randoms, FKP weight, binning,
mesh settings) identical to pk_estimator_qso.py. Reports the resulting
Delta f_NL for p=1.6 (QSO merger, DESI default) via the same fit model as
fit_fnl.py. This is the plan's primary/headline systematic lever (Rezaie+
2023 established WEIGHT_SYS-type imaging weights as O(10) in f_NL units
for photometric LRGs; this tests the analogous QSO spectroscopic weight).
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
N_RAN = 4
cosmo = DESI(engine="eisenstein_hu")


def load_cat(path, zmin, zmax):
    f = fitsio.FITS(path)
    d = f[1].read(columns=["RA", "DEC", "Z", "WEIGHT", "WEIGHT_SYS", "WEIGHT_FKP"])
    f.close()
    m = (d["Z"] > zmin) & (d["Z"] < zmax)
    return d[m]


def radec_z_to_xyz(ra, dec, z):
    dist = cosmo.comoving_radial_distance(z)
    ra_rad, dec_rad = np.deg2rad(ra), np.deg2rad(dec)
    return np.array([dist * np.cos(dec_rad) * np.cos(ra_rad),
                      dist * np.cos(dec_rad) * np.sin(ra_rad),
                      dist * np.sin(dec_rad)])


def run_cap_variant(cap, use_sys):
    t0 = time.time()
    d = load_cat(f"{DATA_DIR}/QSO_{cap}_clustering.dat.fits", ZMIN, ZMAX)
    dpos = radec_z_to_xyz(d["RA"], d["DEC"], d["Z"])
    dw = (d["WEIGHT"] if use_sys else d["WEIGHT"] / d["WEIGHT_SYS"]) * d["WEIGHT_FKP"]
    rparts = [load_cat(f"{DATA_DIR}/QSO_{cap}_{i}_clustering.ran.fits", ZMIN, ZMAX) for i in range(N_RAN)]
    r = np.concatenate(rparts)
    rpos = radec_z_to_xyz(r["RA"], r["DEC"], r["Z"])
    rw = (r["WEIGHT"] if use_sys else r["WEIGHT"] / r["WEIGHT_SYS"]) * r["WEIGHT_FKP"]

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
    p0 = np.real(poles(ell=0, complex=False))
    p2 = np.real(poles(ell=2, complex=False))
    print(f"[{cap} sys={use_sys}] N={len(d)} done in {time.time()-t0:.1f}s", flush=True)
    return {"k": k.tolist(), "p0": p0.tolist(), "p2": p2.tolist(), "n_data": int(len(d))}


if __name__ == "__main__":
    out = {}
    for cap in ["NGC", "SGC"]:
        for use_sys in [True, False]:
            key = f"{cap}_{'sys' if use_sys else 'nosys'}"
            out[key] = run_cap_variant(cap, use_sys)
    with open(f"{OUT_DIR}/systest_weight_sys_pk.json", "w") as fh:
        json.dump(out, fh, indent=2)
    print("SAVED systest_weight_sys_pk.json")

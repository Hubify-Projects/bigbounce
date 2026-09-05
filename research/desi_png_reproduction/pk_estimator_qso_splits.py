#!/usr/bin/env python3
"""Ledger row 4 v4, item (2) step B: measure P_ell(k) for high/low median
splits of EBV, STARDENS, GALDEPTH_Z (cross-matched in
imaging_splits_crossmatch.py) on NGC+SGC, combined the same way as
pk_estimator_qso.py's headline (number-weighted NGC+SGC). Reduced fidelity
vs the headline (nmesh=256, N_RAN=4 not 18) is an explicit, disclosed
scope reduction for the ~3h session budget -- this is a differential
systematics test (the split DIFFERENCE is the informative quantity, per
the same logic as v2's galactic-latitude split), not a replacement for
the headline measurement.
"""
import json
import sys
import time
import numpy as np
import fitsio
from cosmoprimo.fiducial import DESI
from pypower import CatalogFFTPower

DATA_DIR = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss"
OUT_DIR = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"
ZMIN, ZMAX = 0.8, 3.1
N_RAN = 4
NMESH = 256
cosmo = DESI(engine="eisenstein_hu")


def load_cat(path, zmin, zmax):
    f = fitsio.FITS(path)
    d = f[1].read(columns=["RA", "DEC", "Z", "WEIGHT", "WEIGHT_FKP"])
    f.close()
    m = (d["Z"] > zmin) & (d["Z"] < zmax)
    return d[m], m


def radec_z_to_xyz(ra, dec, z):
    dist = cosmo.comoving_radial_distance(z)
    ra_rad, dec_rad = np.deg2rad(ra), np.deg2rad(dec)
    return np.array([dist * np.cos(dec_rad) * np.cos(ra_rad),
                      dist * np.cos(dec_rad) * np.sin(ra_rad),
                      dist * np.sin(dec_rad)])


def run_cap_split(cap, prop, half, median):
    t0 = time.time()
    dpath = f"{DATA_DIR}/QSO_{cap}_clustering.dat.fits"
    d, mzcut = load_cat(dpath, ZMIN, ZMAX)
    attach = np.load(f"{OUT_DIR}/imaging_attach_{cap}_data.npz")[prop][mzcut]
    sel = (attach > median) if half == "high" else (attach <= median)
    d = d[sel]
    dpos = radec_z_to_xyz(d["RA"], d["DEC"], d["Z"])
    dw = d["WEIGHT"] * d["WEIGHT_FKP"]

    rparts, rselparts = [], []
    for i in range(N_RAN):
        rpath = f"{DATA_DIR}/QSO_{cap}_{i}_clustering.ran.fits"
        r, mzr = load_cat(rpath, ZMIN, ZMAX)
        rattach = np.load(f"{OUT_DIR}/imaging_attach_{cap}_ran{i}.npz")[prop][mzr]
        rsel = (rattach > median) if half == "high" else (rattach <= median)
        rparts.append(r[rsel])
    r = np.concatenate(rparts)
    rpos = radec_z_to_xyz(r["RA"], r["DEC"], r["Z"])
    rw = r["WEIGHT"] * r["WEIGHT_FKP"]

    print(f"[{cap}/{prop}/{half}] data N={len(d)}, randoms N={len(r)}, load {time.time()-t0:.1f}s", flush=True)
    edges = np.arange(0.0, 0.31, 0.001)
    t1 = time.time()
    result = CatalogFFTPower(
        data_positions1=dpos, data_weights1=dw,
        randoms_positions1=rpos, randoms_weights1=rw,
        edges=edges, ells=(0, 2, 4), los="firstpoint",
        nmesh=NMESH, resampler="tsc", interlacing=2,
        position_type="xyz", dtype="f8",
    )
    print(f"[{cap}/{prop}/{half}] FFTPower done in {time.time()-t1:.1f}s", flush=True)
    poles = result.poles
    out = dict(k=poles.k.tolist(), p0=poles(ell=0).real.tolist(),
               p2=poles(ell=2).real.tolist(), p4=poles(ell=4).real.tolist(),
               nmodes=poles.nmodes.tolist(), n_data=len(d), n_ran=len(r))
    with open(f"{OUT_DIR}/pk_split_{cap}_{prop}_{half}.json", "w") as f:
        json.dump(out, f)
    return out


if __name__ == "__main__":
    prop = sys.argv[1]
    with open(f"{OUT_DIR}/imaging_splits_medians.json") as f:
        median = json.load(f)["medians"][prop]
    for cap in ("NGC", "SGC"):
        for half in ("high", "low"):
            run_cap_split(cap, prop, half, median)
    print(f"DONE {prop}", flush=True)

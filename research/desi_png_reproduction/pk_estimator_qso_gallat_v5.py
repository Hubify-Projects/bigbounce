#!/usr/bin/env python3
"""Ledger row 4 v5, item (2): re-measure the Galactic-latitude |b|>40deg vs
|b|<=40deg null split at v4-imaging-split fidelity (nmesh=256, N_RAN=4,
ell=0,2,4, edges to k=0.31) on BOTH caps (NGC+SGC combined via
fit_fnl_splits.py's n_data-weighted mean) -- upgrading v2's NGC-only,
ad-hoc diagonal-sigma gal-lat test to the SAME official-window/official-
EZmock-covariance machinery used for the v4 imaging splits, so the whole
systematics table sits on one convention. "high" = |b|>40 (matches
systest_gal_lat_fast.py's naming), "low" = |b|<=40.
"""
import json
import time
import numpy as np
import fitsio
from astropy.coordinates import SkyCoord
import astropy.units as u
from cosmoprimo.fiducial import DESI
from pypower import CatalogFFTPower

DATA_DIR = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss"
OUT_DIR = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"
ZMIN, ZMAX = 0.8, 3.1
N_RAN = 4
NMESH = 256
cosmo = DESI(engine="eisenstein_hu")


def load_cat(path, cols):
    f = fitsio.FITS(path)
    d = f[1].read(columns=cols)
    f.close()
    m = (d["Z"] > ZMIN) & (d["Z"] < ZMAX)
    return d[m]


def radec_z_to_xyz(ra, dec, z):
    dist = cosmo.comoving_radial_distance(z)
    ra_rad, dec_rad = np.deg2rad(ra), np.deg2rad(dec)
    return np.array([dist * np.cos(dec_rad) * np.cos(ra_rad),
                      dist * np.cos(dec_rad) * np.sin(ra_rad),
                      dist * np.sin(dec_rad)])


def gal_b(ra, dec):
    return SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs").galactic.b.deg


def mask_fn(d, half):
    b = gal_b(d["RA"], d["DEC"])
    return np.abs(b) > 40 if half == "high" else np.abs(b) <= 40


def run_cap_variant(cap, half):
    t0 = time.time()
    d = load_cat(f"{DATA_DIR}/QSO_{cap}_clustering.dat.fits", ["RA", "DEC", "Z", "WEIGHT", "WEIGHT_FKP"])
    d = d[mask_fn(d, half)]
    dpos = radec_z_to_xyz(d["RA"], d["DEC"], d["Z"])
    dw = d["WEIGHT"] * d["WEIGHT_FKP"]

    rparts = []
    for i in range(N_RAN):
        r = load_cat(f"{DATA_DIR}/QSO_{cap}_{i}_clustering.ran.fits", ["RA", "DEC", "Z", "WEIGHT", "WEIGHT_FKP"])
        r = r[mask_fn(r, half)]
        rparts.append(r)
    r = np.concatenate(rparts)
    rpos = radec_z_to_xyz(r["RA"], r["DEC"], r["Z"])
    rw = r["WEIGHT"] * r["WEIGHT_FKP"]

    edges = np.arange(0.0, 0.31, 0.001)
    result = CatalogFFTPower(
        data_positions1=dpos, data_weights1=dw,
        randoms_positions1=rpos, randoms_weights1=rw,
        edges=edges, ells=(0, 2, 4), los="firstpoint",
        nmesh=NMESH, resampler="tsc", interlacing=2,
        position_type="xyz", dtype="f8",
    )
    poles = result.poles
    out = dict(k=poles.k.tolist(), p0=poles(ell=0).real.tolist(),
               p2=poles(ell=2).real.tolist(), p4=poles(ell=4).real.tolist(),
               nmodes=poles.nmodes.tolist(), n_data=int(len(d)), n_ran=int(len(r)))
    print(f"[{cap} GALLAT {half}] N={len(d)} done in {time.time()-t0:.1f}s", flush=True)
    with open(f"{OUT_DIR}/pk_split_{cap}_GALLAT_{half}.json", "w") as fh:
        json.dump(out, fh)
    return out


if __name__ == "__main__":
    for cap in ["NGC", "SGC"]:
        for half in ["high", "low"]:
            run_cap_variant(cap, half)
    print("DONE GALLAT", flush=True)

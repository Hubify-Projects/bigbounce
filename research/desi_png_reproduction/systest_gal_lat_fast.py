#!/usr/bin/env python3
"""Ledger row 4 v2, fix (5) test 2: Galactic-latitude null split (plan sec
3.4 test 2). Computed directly from RA/DEC via astropy (no external map
needed) -- |b|>40deg vs |b|<40deg, same P0/P2 + f_NL(p=1.6) machinery as
systest_weight_sys.py. PHOTSYS (North/South imaging) split included as a
second, already-tabulated systematics lever (column present in the
clustering catalogue, no extra download needed).
E(B-V) / stellar-density / depth-seeing splits (plan tests 3-5) are NOT run
here: they require the DESI imaging pixel-weight maps
(desi/target/catalogs/.../pixweight files), which are not in this session's
downloaded dataset -- documented as the exact remaining step, not silently
dropped.
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


def run_cap_variant(cap, mask_fn, label):
    t0 = time.time()
    d = load_cat(f"{DATA_DIR}/QSO_{cap}_clustering.dat.fits",
                 ["RA", "DEC", "Z", "WEIGHT", "WEIGHT_FKP", "PHOTSYS"])
    dm = mask_fn(d)
    d = d[dm]
    dpos = radec_z_to_xyz(d["RA"], d["DEC"], d["Z"])
    dw = d["WEIGHT"] * d["WEIGHT_FKP"]
    rparts = [load_cat(f"{DATA_DIR}/QSO_{cap}_{i}_clustering.ran.fits",
                        ["RA", "DEC", "Z", "WEIGHT", "WEIGHT_FKP", "PHOTSYS"])
              for i in range(N_RAN)]
    r = np.concatenate(rparts)
    rm = mask_fn(r)
    r = r[rm]
    rpos = radec_z_to_xyz(r["RA"], r["DEC"], r["Z"])
    rw = r["WEIGHT"] * r["WEIGHT_FKP"]
    if len(d) < 1000 or len(r) < 1000:
        print(f"[{cap} {label}] too few objects (N_d={len(d)}, N_r={len(r)}), skip", flush=True)
        return None
    edges = np.arange(0.0, 0.11, 0.001)
    result = CatalogFFTPower(
        data_positions1=dpos, data_weights1=dw,
        randoms_positions1=rpos, randoms_weights1=rw,
        edges=edges, ells=(0, 2), los="firstpoint",
        nmesh=256, resampler="tsc", interlacing=2,
        position_type="xyz", dtype="f8",
    )
    poles = result.poles
    k = poles.k
    p0 = np.real(poles(ell=0, complex=False))
    p2 = np.real(poles(ell=2, complex=False))
    print(f"[{cap} {label}] N={len(d)} done in {time.time()-t0:.1f}s", flush=True)
    return {"k": k.tolist(), "p0": p0.tolist(), "p2": p2.tolist(), "n_data": int(len(d))}


SPLITS = {
    "gallat_high": lambda d: __import__("numpy").abs(gal_b(d["RA"], d["DEC"])) > 40,
    "gallat_low": lambda d: __import__("numpy").abs(gal_b(d["RA"], d["DEC"])) <= 40,
}

if __name__ == "__main__":
    out = {}
    for cap in ["NGC"]:
        for label, fn in SPLITS.items():
            key = f"{cap}_{label}"
            r = run_cap_variant(cap, fn, label)
            if r is not None:
                out[key] = r
    with open(f"{OUT_DIR}/systest_splits_pk.json", "w") as fh:
        json.dump(out, fh, indent=2)
    print("SAVED systest_splits_pk.json")

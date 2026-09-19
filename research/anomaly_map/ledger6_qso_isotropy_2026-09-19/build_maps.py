#!/usr/bin/env python3
"""Ledger #6 second discriminator, step 1: build HEALPix count maps for the
DESI DR1 QSO clustering catalogues (data + randoms 0-3, 0.8 < z < 2.1).

Pre-registration: PREREGISTRATION.md (committed before any statistic was run).
CPU only, no network. Writes outputs/maps_nside{32,64,128}.npz (few MB).
"""
import os, sys, json, hashlib, time
import numpy as np
from astropy.io import fits
import healpy as hp

DATA = os.path.expanduser("~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
NSIDES = [32, 64, 128]
CAPS = ["NGC", "SGC"]
NRAN = 4                      # random files 0..3 per cap (pre-registered)
ZMIN, ZMAX = 0.8, 2.1         # official DR1 QSO clustering range


def pix(nside, ra, dec):
    return hp.ang2pix(nside, np.radians(90.0 - dec), np.radians(ra))


def accumulate(maps, key, nside, p, vals=None):
    npix = hp.nside2npix(nside)
    m = np.bincount(p, weights=vals, minlength=npix)
    maps[key] = maps.get(key, np.zeros(npix)) + m


def read_cols(path, cols):
    with fits.open(path, memmap=True) as h:
        d = h[1].data
        out = {c: np.asarray(d[c], dtype=np.float64) for c in cols}
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    meta = {"data": DATA, "nran_files": NRAN, "zmin": ZMIN, "zmax": ZMAX,
            "nsides": NSIDES, "counts": {}}
    maps = {ns: {} for ns in NSIDES}
    t0 = time.time()
    for cap in CAPS:
        # ---- data ----
        f = f"{DATA}/QSO_{cap}_clustering.dat.fits"
        c = read_cols(f, ["RA", "DEC", "Z", "WEIGHT", "WEIGHT_SYS"])
        m = (c["Z"] > ZMIN) & (c["Z"] < ZMAX)
        ra, dec, w, wsys = c["RA"][m], c["DEC"][m], c["WEIGHT"][m], c["WEIGHT_SYS"][m]
        meta["counts"][f"data_{cap}"] = int(m.sum())
        meta["counts"][f"data_{cap}_sumw"] = float(w.sum())
        for ns in NSIDES:
            p = pix(ns, ra, dec)
            accumulate(maps[ns], f"D_{cap}", ns, p, w)
            accumulate(maps[ns], f"Q_{cap}", ns, p, w * w)
            accumulate(maps[ns], f"n_{cap}", ns, p, None)
            if ns == 64:                     # N3(a): WEIGHT_SYS removed
                wn = w / wsys
                accumulate(maps[ns], f"Dns_{cap}", ns, p, wn)
                accumulate(maps[ns], f"Qns_{cap}", ns, p, wn * wn)
        print(f"[{time.time()-t0:6.1f}s] data {cap}: {m.sum()} objects", flush=True)
        del c, ra, dec, w, wsys
        # ---- randoms ----
        for i in range(NRAN):
            f = f"{DATA}/QSO_{cap}_{i}_clustering.ran.fits"
            c = read_cols(f, ["RA", "DEC", "Z", "WEIGHT", "WEIGHT_SYS"])
            m = (c["Z"] > ZMIN) & (c["Z"] < ZMAX)
            ra, dec, w, wsys = c["RA"][m], c["DEC"][m], c["WEIGHT"][m], c["WEIGHT_SYS"][m]
            meta["counts"][f"ran_{cap}"] = meta["counts"].get(f"ran_{cap}", 0) + int(m.sum())
            for ns in NSIDES:
                p = pix(ns, ra, dec)
                accumulate(maps[ns], f"R_{cap}", ns, p, w)
                if ns == 64:
                    accumulate(maps[ns], f"Rns_{cap}", ns, p, w / wsys)
            print(f"[{time.time()-t0:6.1f}s] ran {cap} {i}: {m.sum()}", flush=True)
            del c, ra, dec, w, wsys
    for ns in NSIDES:
        np.savez_compressed(f"{OUT}/maps_nside{ns}.npz", **maps[ns])
    with open(f"{OUT}/maps_meta.json", "w") as fh:
        json.dump(meta, fh, indent=2)
    print("counts:", json.dumps(meta["counts"], indent=1))
    print(f"done in {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()

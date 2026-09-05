#!/usr/bin/env python3
"""Ledger row 4 v4, item (2) step A: cross-match the DR1 QSO clustering
catalogs (data+randoms, NGC+SGC) to the public Legacy Survey DR9 imaging
pixweight map (main/dark, nside=256 nested; downloaded from
data.desi.lbl.gov/public/edr/target/catalogs/dr9/0.49.0/pixweight/, sha256
in imaging_pixweight.sha256) to attach per-object EBV, STARDENS,
GALDEPTH_Z, then define high/low median splits per property (computed on
the DATA catalog, applied identically to data+randoms so each split keeps
a self-consistent footprint/random pair). DR1's own QSO clustering
catalogs carry no per-object imaging columns (v3 finding) -- this is the
named next step from LEDGER4_RESULT_v3 section 6 item 2.
"""
import numpy as np
import fitsio
import healpy as hp
import json

DATA_DIR = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss"
PIXW = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/imaging_pixweight/pixweight-dark.fits"
OUT = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"
NSIDE = 256
PROPS = ["EBV", "STARDENS", "GALDEPTH_Z"]


def load_pixweight():
    f = fitsio.FITS(PIXW)
    d = f[1].read(columns=["HPXPIXEL"] + PROPS)
    f.close()
    npix = hp.nside2npix(NSIDE)
    maps = {p: np.full(npix, np.nan) for p in PROPS}
    for p in PROPS:
        maps[p][d["HPXPIXEL"]] = d[p]
    return maps


def attach(cap, kind, maps):
    suffix = "clustering.dat.fits" if kind == "data" else None
    if kind == "data":
        path = f"{DATA_DIR}/QSO_{cap}_clustering.dat.fits"
    else:
        path = f"{DATA_DIR}/QSO_{cap}_{kind}_clustering.ran.fits"
    f = fitsio.FITS(path)
    d = f[1].read(columns=["RA", "DEC"])
    f.close()
    pix = hp.ang2pix(NSIDE, d["RA"], d["DEC"], nest=True, lonlat=True)
    out = {p: maps[p][pix] for p in PROPS}
    return out, len(d)


def main():
    maps = load_pixweight()
    medians = {}
    counts = {}
    # medians computed on combined NGC+SGC data
    all_vals = {p: [] for p in PROPS}
    for cap in ("NGC", "SGC"):
        vals, n = attach(cap, "data", maps)
        for p in PROPS:
            all_vals[p].append(vals[p])
        counts[f"{cap}_data_n"] = n
        np.savez(f"{OUT}/imaging_attach_{cap}_data.npz", **vals)
    for p in PROPS:
        v = np.concatenate(all_vals[p])
        good = np.isfinite(v)
        medians[p] = float(np.median(v[good]))
        counts[f"{p}_n_unmatched"] = int((~good).sum())
    for cap in ("NGC", "SGC"):
        for i in range(4):
            vals, n = attach(cap, i, maps)
            np.savez(f"{OUT}/imaging_attach_{cap}_ran{i}.npz", **vals)
            counts[f"{cap}_ran{i}_n"] = n
    with open(f"{OUT}/imaging_splits_medians.json", "w") as fo:
        json.dump({"medians": medians, "counts": counts, "nside": NSIDE, "props": PROPS}, fo, indent=2)
    print(json.dumps({"medians": medians, "counts": counts}, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Ledger row 4 LRG channel: stream the DR1 v1.5 LRG clustering catalogues
and randoms by HTTP range read and keep ONLY the derived columns the five
systematics splits need.

No bulk catalogue is written to disk: each file is read byte 0 -> EOF
exactly once (so the recorded sha256 is the whole-file sha256 at no extra
network cost), the six needed columns are extracted in memory, the three
imaging properties are attached from the LOCAL pixweight map, Galactic
latitude is computed, the z-range cut is applied, and everything else is
dropped. What lands on disk is a float32 derived-column cache outside the
repo -- ~36 bytes/row instead of the catalogue's 97-105 bytes/row of
columns we do not use.
"""
import json
import os
import time

import numpy as np
import healpy as hp

import http_stream as hs

LSS = ("https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/"
       "LSScats/v1.5")
DSETS = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss"
CACHE = f"{DSETS}/lrg_stream_cache"
PIXW = f"{DSETS}/imaging_pixweight/pixweight-dark.fits"
OUT = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/lrg_channel_2026_09_22/outputs"
NSIDE = 256
PROPS = ["EBV", "STARDENS", "GALDEPTH_Z"]
COLS = ["RA", "DEC", "Z", "WEIGHT", "WEIGHT_SYS", "WEIGHT_FKP"]
ZMIN, ZMAX = 0.4, 1.1          # full DR1 LRG full-shape range (3 z-bins)
N_RAN = 4                       # identical to v5's QSO systematics runs

# ICRS -> Galactic pole (IAU 1958, the values astropy uses); vectorised here
# because astropy SkyCoord on 5.7e7 rows is not practical. Agreement with
# astropy is asserted on a sample in main() and recorded in the receipt.
RA_NGP, DEC_NGP, L_NCP = 192.85948, 27.12825, 122.93192


def gal_b(ra, dec):
    r, d = np.deg2rad(ra.astype(np.float64)), np.deg2rad(dec.astype(np.float64))
    dn = np.deg2rad(DEC_NGP)
    s = np.sin(d) * np.sin(dn) + np.cos(d) * np.cos(dn) * np.cos(r - np.deg2rad(RA_NGP))
    return np.rad2deg(np.arcsin(np.clip(s, -1, 1)))


def load_pixweight():
    import fitsio
    f = fitsio.FITS(PIXW)
    d = f[1].read(columns=["HPXPIXEL"] + PROPS)
    f.close()
    npix = hp.nside2npix(NSIDE)
    maps = {p: np.full(npix, np.nan) for p in PROPS}
    for p in PROPS:
        maps[p][d["HPXPIXEL"]] = d[p]
    return maps


def one(url, name, maps, receipts):
    t0 = time.time()
    mb0 = hs.BYTES_STREAMED["n"]

    def zcut(chunk):
        return (chunk["Z"] > ZMIN) & (chunk["Z"] < ZMAX)

    def prog(rows, nrows, pos, size):
        if rows % 2000000 < 400000:
            print(f"   {name} {100*pos/size:5.1f}%", flush=True)

    d, info = hs.stream_fits_sequential(url, COLS, row_filter=zcut, progress=prog)
    pix = hp.ang2pix(NSIDE, d["RA"].astype(np.float64), d["DEC"].astype(np.float64),
                     nest=True, lonlat=True)
    arrs = {c: d[c].astype(np.float32) for c in COLS}
    for p in PROPS:
        arrs[p] = maps[p][pix].astype(np.float32)
    arrs["GALB"] = gal_b(d["RA"], d["DEC"]).astype(np.float32)
    np.savez(f"{CACHE}/{name}.npz", **arrs)
    n = len(arrs["RA"])
    receipts[name] = dict(url=url, sha256=info["sha256"], bytes=info["bytes"],
                          nrows_file=info["nrows"], nrows_kept=int(n),
                          seconds=round(time.time() - t0, 1),
                          streamed_bytes=hs.BYTES_STREAMED["n"] - mb0,
                          n_unmatched_pixweight=int(np.isnan(arrs["EBV"]).sum()))
    print(f"[{name}] {info['nrows']} rows -> {n} kept "
          f"({info['bytes']/1e6:.0f} MB streamed, {time.time()-t0:.0f}s)", flush=True)
    del d, arrs, pix


def main():
    os.makedirs(CACHE, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    maps = load_pixweight()
    receipts = {}

    # verify the vectorised Galactic-latitude formula against astropy, which
    # is what v5's QSO gal-lat split used, before relying on it for 5.7e7 rows
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    rng = np.random.default_rng(4)
    ra = rng.uniform(0, 360, 20000)
    dec = np.rad2deg(np.arcsin(rng.uniform(-1, 1, 20000)))
    b_ap = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs").galactic.b.deg
    dmax = float(np.max(np.abs(b_ap - gal_b(ra, dec))))
    receipts["_galb_vs_astropy_max_absdeg"] = dmax
    assert dmax < 1e-3, dmax
    print(f"gal_b vs astropy: max |delta| = {dmax:.2e} deg", flush=True)

    for cap in ("NGC", "SGC"):
        one(f"{LSS}/LRG_{cap}_clustering.dat.fits", f"LRG_{cap}_data", maps, receipts)
        for i in range(N_RAN):
            one(f"{LSS}/LRG_{cap}_{i}_clustering.ran.fits", f"LRG_{cap}_ran{i}",
                maps, receipts)

    receipts["_total_streamed_bytes"] = hs.BYTES_STREAMED["n"]
    receipts["_cache_bytes"] = sum(
        os.path.getsize(os.path.join(CACHE, f)) for f in os.listdir(CACHE))
    with open(f"{OUT}/stream_manifest.json", "w") as f:
        json.dump(receipts, f, indent=2)
    print(json.dumps({k: v for k, v in receipts.items() if k.startswith("_")}, indent=2))


if __name__ == "__main__":
    main()

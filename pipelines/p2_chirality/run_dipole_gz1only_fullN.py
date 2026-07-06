#!/usr/bin/env python3
"""Full-N GZ1-HUMAN-LABEL-ONLY chirality-dipole re-inference (referee-requested).

Motivation
----------
Both calibrated P4 external referees (Grok, Gemini) judged the committed
GZ1-only independence check (N=14,964, `outputs/gz1only_dipole_result.json`)
UNDERPOWERED: that N came from an arbitrary 20,000-galaxy streaming cap in the
pod inference job, NOT from the true GZ1 x DESI overlap. They want the GZ1-only
null recomputed at the largest N obtainable, using chirality labels that come
ONLY from Galaxy Zoo 1 human classifications (independent of the CE-ResNet
pseudo-labels the main catalog is built on).

This script answers that directly and locally, with NO pod dependency and NO
CE-ResNet model in the chirality label chain at all:

  * Chirality label source = Galaxy Zoo 1 Table 2 HUMAN vote fractions
    (P_CW, P_ACW). This is *more* independent than the pod's GZ1-only *model*
    run, which trained a network on GZ1 labels; here the human votes ARE the
    per-galaxy CW/CCW label. Zero learned CE-ResNet component.
  * Sky positions = the released DESI chirality catalog
    (`catalog_production.parquet`), used ONLY to define the DESI footprint /
    galaxy positions (ra, dec via dr8_id). The catalog's own class_eq column is
    NOT used for the label.
  * Dipole estimator + MC null = byte-identical recipe to the paper headline
    generator `run_dipole_catalog_c.py` (HEALPix NSIDE=64, MIN_PIX_COUNT=10,
    hp.fit_dipole, N_MC=10000 per-pixel label-permutation null, seed 20260418).

Data (both public / already local — no pod, no HF token):
  * GZ1 Table 2: https://data.galaxyzoo.org/data/gz1/GalaxyZoo1_DR_table2.csv.gz
    (Lintott et al. 2011). Auto-downloaded to /tmp if not passed via GZ1_CSV.
  * catalog_production.parquet: local HF cache
    (datasets--bamfai--galaxy-chirality-catalog) or CAT_C_PATH env override.

Cross-match: GZ1 OBJID is an SDSS DR7 objID; the DESI catalog is keyed by
dr8_id and has no SDSS objID, so we cross-match by sky position (KDTree on unit
vectors, <= 1 arcsec) exactly as the committed GZ1 Platt-recal script
(`wave_14_fff_gz1_platt_recal.py`) did. The DESI positions define the footprint;
the label at each matched position is the GZ1 human CW/CCW vote.

Output: outputs/gz1only_fullN_dipole_result.json
"""
import gzip
import json
import os
import time
import urllib.request
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

HERE = Path(__file__).parent
OUT_PATH = HERE / "outputs" / "gz1only_fullN_dipole_result.json"

# --- identical estimator constants to run_dipole_catalog_c.py ---
NSIDE = 64
MIN_PIX_COUNT = 10
CONF_CUT = 0.6          # winning-class prob cut, same as headline
N_MC = 10000
MC_SEED = 20260418      # same seed as the headline generator
MATCH_ARCSEC = 1.0

GZ1_URL = "https://data.galaxyzoo.org/data/gz1/GalaxyZoo1_DR_table2.csv.gz"


def _hms_to_deg(s):
    p = str(s).strip().split(":")
    return (float(p[0]) + float(p[1]) / 60 + float(p[2]) / 3600) * 15.0


def _dms_to_deg(s):
    s = str(s).strip()
    sign = -1 if s.startswith("-") else 1
    p = s.lstrip("+-").split(":")
    return sign * (float(p[0]) + float(p[1]) / 60 + float(p[2]) / 3600)


def _radec_to_xyz(ra_deg, dec_deg):
    ra = np.radians(ra_deg)
    dec = np.radians(dec_deg)
    return np.stack(
        [np.cos(dec) * np.cos(ra), np.cos(dec) * np.sin(ra), np.sin(dec)],
        axis=1,
    )


def _default_cat_path():
    env = os.environ.get("CAT_C_PATH")
    if env:
        return env
    # local HF cache
    import glob

    hits = glob.glob(
        os.path.expanduser(
            "~/.cache/huggingface/hub/datasets--bamfai--galaxy-chirality-catalog/"
            "snapshots/*/catalog_production.parquet"
        )
    )
    if hits:
        return hits[0]
    return "/workspace/chirality/catalog_production.parquet"


def _get_gz1_csv():
    env = os.environ.get("GZ1_CSV")
    if env and Path(env).exists():
        return env
    dest = Path("/tmp/gz1_table2.csv.gz")
    if not dest.exists():
        print(f"Downloading GZ1 Table 2 -> {dest} ...", flush=True)
        urllib.request.urlretrieve(GZ1_URL, dest)
    return str(dest)


def main():
    t_start = time.time()
    print("=" * 70, flush=True)
    print("FULL-N GZ1-HUMAN-LABEL-ONLY CHIRALITY DIPOLE", flush=True)
    print("=" * 70, flush=True)

    # --- 1. GZ1 human labels ---
    gz1_csv = _get_gz1_csv()
    print(f"Loading GZ1 Table 2: {gz1_csv}", flush=True)
    with gzip.open(gz1_csv, "rt") as f:
        gz1 = pd.read_csv(f)
    n_gz1_total = len(gz1)
    gz1["ra_deg"] = gz1["RA"].apply(_hms_to_deg)
    gz1["dec_deg"] = gz1["DEC"].apply(_dms_to_deg)

    spir = gz1[gz1["SPIRAL"] == 1].copy()
    spir["max_cw_acw"] = spir[["P_CW", "P_ACW"]].max(axis=1)
    conf = spir[spir["max_cw_acw"] > CONF_CUT].copy()
    conf["gz1_cw"] = (conf["P_CW"] > conf["P_ACW"]).astype(int)
    n_gz1_spiral = len(spir)
    n_gz1_conf = len(conf)
    print(f"  GZ1 total rows:            {n_gz1_total:,}", flush=True)
    print(f"  GZ1 spirals (SPIRAL=1):    {n_gz1_spiral:,}", flush=True)
    print(f"  GZ1 confident CW/CCW>0.6:  {n_gz1_conf:,}", flush=True)
    print(f"  GZ1 human CW fraction:     {conf['gz1_cw'].mean():.4f}", flush=True)

    # --- 2. DESI positions (footprint only) ---
    cat_path = _default_cat_path()
    print(f"Loading DESI catalog positions: {cat_path}", flush=True)
    cat = pd.read_parquet(cat_path, columns=["ra", "dec"])
    cat = cat[cat["ra"].notna() & cat["dec"].notna()]
    print(f"  DESI catalog rows: {len(cat):,}", flush=True)

    # --- 3. cross-match GZ1 (confident) onto DESI positions, <= 1 arcsec ---
    print("Cross-matching GZ1 confident spirals to DESI (<=1 arcsec)...", flush=True)
    cat_xyz = _radec_to_xyz(cat["ra"].values, cat["dec"].values)
    gz1_xyz = _radec_to_xyz(conf["ra_deg"].values, conf["dec_deg"].values)
    tree = cKDTree(cat_xyz)
    tol = MATCH_ARCSEC / 3600.0 * np.pi / 180.0  # chord ~ angle for small theta
    dist, idx = tree.query(gz1_xyz, k=1, distance_upper_bound=tol)
    matched = np.isfinite(dist)
    n_match = int(matched.sum())
    print(f"  Matched: {n_match:,} / {n_gz1_conf:,}", flush=True)

    m = conf[matched].copy()
    m["ra"] = cat["ra"].values[idx[matched]]
    m["dec"] = cat["dec"].values[idx[matched]]
    cw_frac_matched = float(m["gz1_cw"].mean())
    print(f"  GZ1 human CW fraction (matched): {cw_frac_matched:.4f}", flush=True)

    # --- 4. dipole on GZ1-human-label per-pixel asymmetry (identical recipe) ---
    npix = hp.nside2npix(NSIDE)
    cw_map = np.zeros(npix)
    ccw_map = np.zeros(npix)
    theta = np.radians(90.0 - m["dec"].values)
    phi = np.radians(m["ra"].values % 360.0)
    pix = hp.ang2pix(NSIDE, theta, phi)
    is_cw = m["gz1_cw"].values.astype(bool)
    np.add.at(cw_map, pix, is_cw.astype(float))
    np.add.at(ccw_map, pix, (~is_cw).astype(float))

    tot = cw_map + ccw_map
    mask = tot > MIN_PIX_COUNT
    asym = np.zeros(npix)
    asym[mask] = (cw_map[mask] - ccw_map[mask]) / tot[mask]
    n_pix = int(mask.sum())
    f_sky = n_pix / npix
    print(f"  Pixels used: {n_pix}/{npix} (f_sky={f_sky:.6f})", flush=True)

    asym_full = np.full(npix, hp.UNSEEN)
    asym_full[mask] = asym[mask]
    mono, dip = hp.fit_dipole(asym_full, gal_cut=0)
    amp = float(np.sqrt(np.sum(dip ** 2)))
    l_deg = float(np.degrees(np.arctan2(dip[1], dip[0])) % 360) if amp > 0 else 0.0
    b_deg = float(np.degrees(np.arcsin(dip[2] / amp))) if amp > 0 else 0.0
    print(f"  Dipole amplitude: {amp:.6f}  (l,b)=({l_deg:.1f},{b_deg:.1f})", flush=True)

    # --- 5. MC null: per-pixel label permutation (identical to headline) ---
    print(f"  Running {N_MC:,} per-pixel permutation nulls...", flush=True)
    rng = np.random.default_rng(MC_SEED)
    valid = asym[mask].copy()
    boots = np.empty(N_MC)
    for i in range(N_MC):
        rng.shuffle(valid)
        shuf = np.full(npix, hp.UNSEEN)
        shuf[mask] = valid
        _, d = hp.fit_dipole(shuf, gal_cut=0)
        boots[i] = np.sqrt(np.sum(d ** 2))
    mc_mean = float(np.mean(boots))
    mc_std = float(np.std(boots))
    z_sigma = (amp - mc_mean) / mc_std if mc_std > 0 else 0.0
    k = int((boots >= amp).sum())
    rank_p = float((k + 1) / (N_MC + 1))

    # second null: per-galaxy binomial shuffle (same secondary null as headline)
    p_glob = cw_map[mask].sum() / tot[mask].sum()
    n_tot_pix = tot[mask].astype(int)
    boots2 = np.empty(N_MC)
    for i in range(N_MC):
        cws = rng.binomial(n_tot_pix, p_glob)
        shuf = np.full(npix, hp.UNSEEN)
        shuf[mask] = (2.0 * cws - n_tot_pix) / n_tot_pix
        _, d = hp.fit_dipole(shuf, gal_cut=0)
        boots2[i] = np.sqrt(np.sum(d ** 2))
    mc2_mean = float(np.mean(boots2))
    mc2_std = float(np.std(boots2))
    z2 = (amp - mc2_mean) / mc2_std if mc2_std > 0 else 0.0
    k2 = int((boots2 >= amp).sum())
    rank_p2 = float((k2 + 1) / (N_MC + 1))

    print(
        f"  per-pixel-perm null:  z={z_sigma:+.3f} sigma  rank_p={rank_p:.4f}",
        flush=True,
    )
    print(
        f"  per-galaxy-binom null: z={z2:+.3f} sigma  rank_p={rank_p2:.4f}",
        flush=True,
    )

    result = {
        "job": "GZ1-HUMAN-LABEL-ONLY full-N dipole (referee underpowered-independence closure)",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "label_source": (
            "Galaxy Zoo 1 Table 2 HUMAN votes P_CW/P_ACW (Lintott+2011); "
            "NO CE-ResNet, NO learned model in the chirality label chain"
        ),
        "position_source": "DESI chirality catalog_production.parquet (ra,dec footprint ONLY)",
        "cross_match": {"tol_arcsec": MATCH_ARCSEC, "method": "KDTree unit-vector nearest"},
        "estimator": {
            "source": "run_dipole_catalog_c.py (byte-identical recipe)",
            "nside": NSIDE,
            "min_pix_count": MIN_PIX_COUNT,
            "conf_cut": CONF_CUT,
            "n_mc": N_MC,
            "mc_seed": MC_SEED,
        },
        "selection": {
            "n_gz1_total": n_gz1_total,
            "n_gz1_spirals": n_gz1_spiral,
            "n_gz1_confident": n_gz1_conf,
            "n_matched_to_desi": n_match,
            "cw_fraction_human_matched": cw_frac_matched,
            "n_pix": n_pix,
            "f_sky": f_sky,
        },
        "dipole": {
            "amplitude": amp,
            "l_deg": l_deg,
            "b_deg": b_deg,
            "monopole": float(mono),
        },
        "null_per_pixel_permutation": {
            "mean": mc_mean,
            "std": mc_std,
            "z_sigma": z_sigma,
            "rank_p": rank_p,
            "k": k,
        },
        "null_per_galaxy_binomial": {
            "mean": mc2_mean,
            "std": mc2_std,
            "z_sigma": z2,
            "rank_p": rank_p2,
            "k": k2,
        },
        "comparison": {
            "prior_gz1only_model_N": 14964,
            "prior_gz1only_model_z": -0.0442,
            "prior_gz1only_model_source": "outputs/gz1only_dipole_result.json (pod, 20k stream cap)",
            "headline_ceresnet_N": 949584,
            "headline_ceresnet_sigma": 0.41,
            "headline_source": "outputs/canonical_provenance/catalog_c_post_tta_dipole_summary.json",
        },
        "wall_seconds": round(time.time() - t_start, 1),
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nWrote {OUT_PATH}", flush=True)
    print(
        f"VERDICT: N={n_match:,} GZ1-human-only spirals -> "
        f"per-pixel-perm null z={z_sigma:+.3f} sigma (p={rank_p:.4f})",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

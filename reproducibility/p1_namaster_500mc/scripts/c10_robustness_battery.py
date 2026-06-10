"""
c10 — NaMaster validation robustness battery (R23conf META-M1/M2/M3/M5/M6).

One battery, six configs, all at beta = 0.27 deg, N_REAL = 500, seed_base = 42
(identical seeds to the canonical run for paired comparison):

  canonical_refit  — canonical sky; THREE fits on the same MC ensemble:
                     (a) unweighted (canonical anchor),
                     (b) inverse-variance weighted (META-M1),
                     (c) unweighted restricted to ell_eff <= 1024 (META-M3)
  lensing_bb_camb  — BB = CAMB lensed-LCDM BB (Planck 2018 params) instead of
                     the 0.05*EE proxy (META-M2)
  apod_fwhm_0p5    — mask apodization 0.5 deg FWHM (META-M5)
  apod_fwhm_3p0    — mask apodization 3.0 deg FWHM (META-M5)
  mask_b30         — Galactic cut |b| > 30 deg (META-M6)
  purify_b         — NmtField(..., purify_b=True) on canonical mask (META-M6)

Canonical anchors (pod run 2026-04-29): recovered 0.238 deg, bias 0.032 deg.
Output: results/c10_robustness_battery.json
"""
import json
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "..", "results", "c10_robustness_battery.json")

NSIDE = 512
LMAX = 2 * NSIDE
BETA = np.deg2rad(0.27)
N_REAL = int(os.environ.get("C10_NREAL", "500"))
SEED_BASE = 42
NOISE_LEVEL_UKARMIN = 10.0


def cl_ee_fit(lmax):
    ells = np.arange(lmax + 1, dtype=float)
    ells[0] = 1
    cl = np.zeros(lmax + 1)
    for amp, lc, sig in [(15.0, 5.0, 3.0), (40.0, 140.0, 40.0),
                         (20.0, 400.0, 60.0), (8.0, 700.0, 80.0)]:
        cl += amp * np.exp(-0.5 * ((ells - lc) / sig) ** 2)
    cl *= np.exp(-ells * (ells + 1) / (2 * 2000 ** 2))
    cl[0:2] = 0
    return cl


def camb_lensed_bb(lmax):
    import camb
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=67.36, ombh2=0.02237, omch2=0.12, tau=0.0544)
    pars.InitPower.set_params(As=2.1e-9, ns=0.9649)
    pars.set_for_lmax(lmax, lens_potential_accuracy=1)
    res = camb.get_results(pars)
    cl = res.get_cmb_power_spectra(pars, CMB_unit="muK", raw_cl=True)["lensed_scalar"]
    bb = cl[: lmax + 1, 2].copy()
    bb[0:2] = 0
    return bb


def run_config(cfg):
    import healpy as hp
    import pymaster as nmt

    name = cfg["name"]
    t0 = time.time()
    np.random.seed(SEED_BASE)

    cl_ee = cl_ee_fit(LMAX)
    cl_bb = camb_lensed_bb(LMAX) if cfg.get("camb_bb") else 0.05 * cl_ee

    npix = hp.nside2npix(NSIDE)
    pix_area_arcmin2 = hp.nside2pixarea(NSIDE, degrees=True) * 3600
    noise_sigma = NOISE_LEVEL_UKARMIN / np.sqrt(pix_area_arcmin2)

    mask = np.ones(npix)
    _, lat = hp.pix2ang(NSIDE, np.arange(npix), lonlat=True)
    mask[np.abs(lat) < cfg.get("gal_cut", 20.0)] = 0.0
    ra, dec = hp.pix2ang(NSIDE, np.arange(npix), lonlat=True)
    mask[dec > 25.0] = 0.0
    mask[dec < -65.0] = 0.0
    mask = hp.smoothing(mask, fwhm=np.deg2rad(cfg.get("apod_fwhm", 2.0)))
    mask = np.clip(mask, 0, 1)
    fsky = mask.sum() / npix

    n_bins = 20
    edges = np.linspace(30, 3 * NSIDE, n_bins + 1, dtype=int)
    b = nmt.NmtBin.from_edges(edges[:-1], edges[1:])
    purify = bool(cfg.get("purify_b", False))
    zero = np.zeros(npix)
    f_dummy = nmt.NmtField(mask, [zero, zero], purify_b=purify)
    wsp = nmt.NmtWorkspace()
    wsp.compute_coupling_matrix(f_dummy, f_dummy, b)

    cos2b, sin2b = np.cos(2 * BETA), np.sin(2 * BETA)
    all_eb = []
    for i in range(N_REAL):
        np.random.seed(SEED_BASE + i)
        maps = hp.synfast([np.zeros(LMAX + 1), cl_ee, cl_bb, np.zeros(LMAX + 1)],
                          NSIDE, lmax=LMAX, new=True)
        Q, U = maps[1], maps[2]
        Q += np.random.normal(0, noise_sigma, npix)
        U += np.random.normal(0, noise_sigma, npix)
        Qr, Ur = cos2b * Q - sin2b * U, sin2b * Q + cos2b * U
        f = nmt.NmtField(mask, [Qr, Ur], purify_b=purify)
        all_eb.append(wsp.decouple_cell(nmt.compute_coupled_cell(f, f))[1])

    all_eb = np.array(all_eb)
    mean_eb, std_eb = all_eb.mean(axis=0), all_eb.std(axis=0)
    ell_effs = b.get_effective_ells()
    ee_binned = np.array([cl_ee[int(l)] if int(l) < len(cl_ee) else 0 for l in ell_effs])

    def fit(weights=None, ell_max=None):
        sel = np.ones(len(ell_effs), bool) if ell_max is None else (ell_effs <= ell_max)
        w = np.ones(sel.sum()) if weights is None else weights[sel]
        grid = np.linspace(-1.0, 1.0, 2001)
        chi2 = [np.sum(w * (mean_eb[sel] - np.sin(2 * np.deg2rad(g)) *
                            np.cos(2 * np.deg2rad(g)) * ee_binned[sel]) ** 2)
                for g in grid]
        return float(grid[int(np.argmin(chi2))])

    fits = {"unweighted": fit()}
    if cfg.get("extra_fits"):
        fits["invvar_weighted"] = fit(weights=1.0 / (std_eb ** 2 + 1e-20))
        fits["lmax1024_only"] = fit(ell_max=1024)

    res = {"name": name, "fsky": round(float(fsky), 4), "n_real": N_REAL,
           "purify_b": purify, "apod_fwhm_deg": cfg.get("apod_fwhm", 2.0),
           "gal_cut_deg": cfg.get("gal_cut", 20.0),
           "bb_model": "camb_lensed" if cfg.get("camb_bb") else "0.05*EE",
           "noise_sigma_pix_uK": round(float(noise_sigma), 4),
           "recovered_beta_deg": {k: round(v, 4) for k, v in fits.items()},
           "bias_deg": {k: round(v - 0.27, 4) for k, v in fits.items()},
           "runtime_s": round(time.time() - t0, 1)}
    print(f"[{name}] done in {res['runtime_s']}s: {res['recovered_beta_deg']}", flush=True)
    return res


CONFIGS = [
    {"name": "canonical_refit", "extra_fits": True},
    {"name": "lensing_bb_camb", "camb_bb": True},
    {"name": "apod_fwhm_0p5", "apod_fwhm": 0.5},
    {"name": "apod_fwhm_3p0", "apod_fwhm": 3.0},
    {"name": "mask_b30", "gal_cut": 30.0},
    {"name": "purify_b", "purify_b": True},
]

if __name__ == "__main__":
    t0 = time.time()
    n_pool = int(os.environ.get("C10_POOL", "3"))
    with Pool(processes=min(n_pool, len(CONFIGS))) as pool:
        results = pool.map(run_config, CONFIGS)
    out = {"experiment": "c10 NaMaster robustness battery (R23conf META-M1/M2/M3/M5/M6)",
           "beta_injected_deg": 0.27, "n_real": N_REAL, "seed_base": SEED_BASE,
           "canonical_anchor": {"recovered_beta_deg": 0.238, "bias_deg": -0.032},
           "configs": results, "total_runtime_s": round(time.time() - t0, 1)}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))

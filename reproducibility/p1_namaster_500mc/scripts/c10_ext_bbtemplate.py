"""
c10 battery extension (R24conf QUEUE-30 / META-M2 matched config).

ONE new config appended to results/c10_robustness_battery.json:

  camb_bb_template — legacy extension in which the injected synthetic skies
                     and template both use the physical CAMB EE/BB spectra,
                     including a
                     template that carries the -C_ell^BB term:
                         sin(2*beta)*cos(2*beta)*(C_ell^EE - C_ell^BB)
                     binned at the effective ells (existing configs use an
                     EE-only template). N=500 MC, seeds 42.. (identical to
                     the canonical battery for paired comparison).

This extension is retained for provenance but is no longer a distinct BB-model
check: the corrected canonical suite now uses physical CAMB BB throughout.

Parallelized over MC realizations (Pool); per-realization seeds preserved.
Appends to the existing JSON (load -> append -> save), never overwrites.
"""
import json
import os
import time
from multiprocessing import Pool

import numpy as np

from c10_robustness_battery import (BASE, OUT, NSIDE, LMAX, BETA, N_REAL,
                                    SEED_BASE, NOISE_LEVEL_UKARMIN)
from physical_spectra import load_camb_lensed_spectra

N_POOL = int(os.environ.get("C10_POOL", "10"))

# Globals built once per worker
_G = {}


def _init_worker():
    import healpy as hp
    import pymaster as nmt

    cl_ee, cl_bb, _ = load_camb_lensed_spectra(LMAX)

    npix = hp.nside2npix(NSIDE)
    pix_area_arcmin2 = hp.nside2pixarea(NSIDE, degrees=True) * 3600
    noise_sigma = NOISE_LEVEL_UKARMIN / np.sqrt(pix_area_arcmin2)

    mask = np.ones(npix)
    _, lat = hp.pix2ang(NSIDE, np.arange(npix), lonlat=True)
    mask[np.abs(lat) < 20.0] = 0.0
    ra, dec = hp.pix2ang(NSIDE, np.arange(npix), lonlat=True)
    mask[dec > 25.0] = 0.0
    mask[dec < -65.0] = 0.0
    mask = hp.smoothing(mask, fwhm=np.deg2rad(2.0))
    mask = np.clip(mask, 0, 1)

    n_bins = 20
    edges = np.linspace(30, 3 * NSIDE, n_bins + 1, dtype=int)
    b = nmt.NmtBin.from_edges(edges[:-1], edges[1:])
    zero = np.zeros(npix)
    f_dummy = nmt.NmtField(mask, [zero, zero], purify_b=False)
    wsp = nmt.NmtWorkspace()
    wsp.compute_coupling_matrix(f_dummy, f_dummy, b)

    _G.update(cl_ee=cl_ee, cl_bb=cl_bb, npix=npix, noise_sigma=noise_sigma,
              mask=mask, b=b, wsp=wsp, hp=hp, nmt=nmt)


def _one_real(i):
    hp, nmt = _G["hp"], _G["nmt"]
    np.random.seed(SEED_BASE + i)
    maps = hp.synfast([np.zeros(LMAX + 1), _G["cl_ee"], _G["cl_bb"],
                       np.zeros(LMAX + 1)], NSIDE, lmax=LMAX, new=True)
    Q, U = maps[1], maps[2]
    Q += np.random.normal(0, _G["noise_sigma"], _G["npix"])
    U += np.random.normal(0, _G["noise_sigma"], _G["npix"])
    cos2b, sin2b = np.cos(2 * BETA), np.sin(2 * BETA)
    Qr, Ur = cos2b * Q - sin2b * U, sin2b * Q + cos2b * U
    f = nmt.NmtField(_G["mask"], [Qr, Ur], purify_b=False)
    return _G["wsp"].decouple_cell(nmt.compute_coupled_cell(f, f))[1]


if __name__ == "__main__":
    t0 = time.time()
    with Pool(processes=N_POOL, initializer=_init_worker) as pool:
        all_eb = np.array(pool.map(_one_real, range(N_REAL)))

    mean_eb = all_eb.mean(axis=0)

    # Rebuild binning info for the template (cheap, main process)
    import pymaster as nmt
    n_bins = 20
    edges = np.linspace(30, 3 * NSIDE, n_bins + 1, dtype=int)
    b = nmt.NmtBin.from_edges(edges[:-1], edges[1:])
    ell_effs = b.get_effective_ells()
    cl_ee, cl_bb, spectrum_metadata = load_camb_lensed_spectra(LMAX)
    ee_binned = np.array([cl_ee[int(l)] if int(l) < len(cl_ee) else 0
                          for l in ell_effs])
    bb_binned = np.array([cl_bb[int(l)] if int(l) < len(cl_bb) else 0
                          for l in ell_effs])
    tmpl = ee_binned - bb_binned

    grid = np.linspace(-1.0, 1.0, 2001)
    chi2 = [np.sum((mean_eb - np.sin(2 * np.deg2rad(g)) *
                    np.cos(2 * np.deg2rad(g)) * tmpl) ** 2) for g in grid]
    beta_hat = float(grid[int(np.argmin(chi2))])

    # fsky for the record (same canonical mask as worker)
    import healpy as hp
    npix = hp.nside2npix(NSIDE)
    mask = np.ones(npix)
    _, lat = hp.pix2ang(NSIDE, np.arange(npix), lonlat=True)
    mask[np.abs(lat) < 20.0] = 0.0
    ra, dec = hp.pix2ang(NSIDE, np.arange(npix), lonlat=True)
    mask[dec > 25.0] = 0.0
    mask[dec < -65.0] = 0.0
    mask = hp.smoothing(mask, fwhm=np.deg2rad(2.0))
    mask = np.clip(mask, 0, 1)
    fsky = float(mask.sum() / npix)
    pix_area_arcmin2 = hp.nside2pixarea(NSIDE, degrees=True) * 3600
    noise_sigma = NOISE_LEVEL_UKARMIN / np.sqrt(pix_area_arcmin2)

    res = {"name": "camb_bb_template",
           "fsky": round(fsky, 4), "n_real": N_REAL, "purify_b": False,
           "apod_fwhm_deg": 2.0, "gal_cut_deg": 20.0,
           "bb_model": "camb_lensed",
           "physical_spectra": spectrum_metadata,
           "template": "sin(2b)cos(2b)*(C_ell^EE - C_ell^BB) binned",
           "noise_sigma_pix_uK": round(float(noise_sigma), 4),
           "recovered_beta_deg": {"unweighted": round(beta_hat, 4)},
           "bias_deg": {"unweighted": round(beta_hat - 0.27, 4)},
           "runtime_s": round(time.time() - t0, 1),
           "note": ("R24conf QUEUE-30 extension: CAMB lensed BB in injected "
                    "skies AND -C_ell^BB-bearing template; paired seeds with "
                    "battery (seed_base 42).")}
    print(f"[camb_bb_template] done in {res['runtime_s']}s: "
          f"beta_hat={beta_hat:.4f} bias={beta_hat - 0.27:+.4f}", flush=True)

    with open(OUT) as f:
        out = json.load(f)
    out["configs"] = [c for c in out["configs"]
                      if c["name"] != "camb_bb_template"] + [res]
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    print("appended to", os.path.abspath(OUT))

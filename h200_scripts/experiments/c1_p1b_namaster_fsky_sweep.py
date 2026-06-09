#!/usr/bin/env python3
"""
C1 — P1B NaMaster beta-injection recovery validation at published-analysis
sky fractions: f_sky ~ 0.85 (Planck-like) and f_sky ~ 0.65 (ACT-DR6-like).

Extends the canonical P1B Sec. IV / Appendix validation
(reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py: f_sky=0.32
apodized, NSIDE=512, lmax=1024, 500 MC, beta=0.27 deg -> recovered
0.238 deg, SNR^SE=20.32) to the sky fractions of the published
birefringence analyses the paper compares against (Planck NPIPE ~0.85+,
ACT DR6 ~0.65 effective-coverage class).

Method (identical to the canonical reproduction script, mask swapped):
  1. Synthetic LCDM EE (+5% lensing BB) Q/U maps via hp.synfast.
  2. Uniform birefringence rotation by beta = 0.27 deg.
  3. ACT-like white noise 10 uK-arcmin.
  4. Galactic-cut mask at |b| > b_cut with b_cut = asin(1 - fsky_target),
     2-deg Gaussian smoothing apodization (same recipe as canonical run).
  5. NaMaster decoupled C_l^EB, Delta_ell binned, 30 <= ell <= 3*NSIDE.
  6. beta recovered by chi^2 fit of C_l^EB to sin(2b)cos(2b) C_l^EE.
  7. 500 MC realizations per f_sky, seeds 42..541 (same as canonical).

CPU-time fallback: a 3-realization timing probe at NSIDE=512 projects the
total wallclock; if > MAX_HOURS (default 20 h), the run drops to NSIDE=256
(lmax=512) and records the fallback in the output JSON.

Run on pod:
  tmux new -s c1 -d 'cd /workspace && python3 c1_p1b_namaster_fsky_sweep.py 2>&1 | tee c1.log'
Output: /workspace/c1_results/c1_fsky_sweep.json
ETA: ~4-16 h CPU at NSIDE=512 depending on cores (canonical run: 2.0 h on H200 host for 3 beta values at one f_sky).
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

import numpy as np
import healpy as hp
import pymaster as nmt

NSIDE_PRIMARY = 512
NSIDE_FALLBACK = 256
MAX_HOURS = float(os.environ.get("C1_MAX_HOURS", "20"))
BETA_INJECT_DEG = 0.27
N_REAL = int(os.environ.get("C1_NREAL", "500"))
SEED_BASE = 42
NOISE_LEVEL_UKARMIN = 10.0
FSKY_TARGETS = [0.85, 0.65]
CANONICAL_REF = {"fsky": 0.32, "recovered_beta_deg": 0.238, "bias_deg": 0.032,
                 "snr_se": 20.32}
OUTDIR = Path(os.environ.get("C1_OUTDIR", "/workspace/c1_results"))
OUT = OUTDIR / "c1_fsky_sweep.json"


def lcdm_cl_ee(lmax):
    """Approximate LCDM EE spectrum in uK^2 (same fit as canonical script)."""
    ells = np.arange(lmax + 1, dtype=float)
    ells[0] = 1
    cl_ee = np.zeros(lmax + 1)
    for amp, lc, sig in [(15.0, 5.0, 3.0), (40.0, 140.0, 40.0),
                         (20.0, 400.0, 60.0), (8.0, 700.0, 80.0)]:
        cl_ee += amp * np.exp(-0.5 * ((ells - lc) / sig) ** 2)
    cl_ee *= np.exp(-ells * (ells + 1) / (2 * 2000 ** 2))
    cl_ee[0:2] = 0
    return cl_ee


def make_galactic_mask(nside, fsky_target):
    """Galactic-cut mask |b| > b_cut for the target f_sky, 2-deg smoothing
    apodization (same apodization recipe as the canonical f_sky=0.32 run)."""
    b_cut_deg = np.rad2deg(np.arcsin(1.0 - fsky_target))
    npix = hp.nside2npix(nside)
    mask = np.ones(npix, dtype=float)
    # Galactic latitude of each pixel: maps are generated in the mask's own
    # frame; for a synthetic-sky validation the frame label is irrelevant,
    # only the cut geometry matters.
    _, lat = hp.pix2ang(nside, np.arange(npix), lonlat=True)
    mask[np.abs(lat) < b_cut_deg] = 0.0
    try:
        mask = hp.smoothing(mask, fwhm=np.deg2rad(2.0), verbose=False)
    except TypeError:  # healpy >= 1.16 removed verbose kwarg
        mask = hp.smoothing(mask, fwhm=np.deg2rad(2.0))
    mask = np.clip(mask, 0, 1)
    return mask, b_cut_deg


def apply_birefringence(Q, U, beta):
    c2b, s2b = np.cos(2 * beta), np.sin(2 * beta)
    return c2b * Q - s2b * U, s2b * Q + c2b * U


def run_fsky(nside, fsky_target, beta_deg, n_real, t0, probe_only=False):
    lmax = 2 * nside
    beta = np.deg2rad(beta_deg)
    cl_ee = lcdm_cl_ee(lmax)
    cl_bb = 0.05 * cl_ee
    pix_area_arcmin2 = hp.nside2pixarea(nside, degrees=True) * 3600
    noise_var = (NOISE_LEVEL_UKARMIN / np.sqrt(pix_area_arcmin2)) ** 2
    npix = hp.nside2npix(nside)

    mask, b_cut_deg = make_galactic_mask(nside, fsky_target)
    actual_fsky = float(mask.sum() / npix)
    print(f"[{time.time()-t0:.0f}s] fsky target {fsky_target}: b_cut={b_cut_deg:.2f} deg, "
          f"apodized fsky={actual_fsky:.4f}, NSIDE={nside}", flush=True)

    n_ell_bins = 20
    ells_bins = np.linspace(30, 3 * nside, n_ell_bins + 1, dtype=int)
    b = nmt.NmtBin.from_edges(ells_bins[:-1], ells_bins[1:])
    f_dummy = nmt.NmtField(mask, [np.zeros(npix), np.zeros(npix)])
    wsp = nmt.NmtWorkspace()
    wsp.compute_coupling_matrix(f_dummy, f_dummy, b)
    print(f"[{time.time()-t0:.0f}s]  coupling matrix done", flush=True)

    all_cl_eb = []
    t_mc = time.time()
    for i in range(n_real):
        np.random.seed(SEED_BASE + i)
        maps = hp.synfast([np.zeros(lmax + 1), cl_ee, cl_bb, np.zeros(lmax + 1)],
                          nside, lmax=lmax, new=True)
        Q, U = maps[1], maps[2]
        Q = Q + np.random.normal(0, np.sqrt(noise_var), npix)
        U = U + np.random.normal(0, np.sqrt(noise_var), npix)
        Qr, Ur = apply_birefringence(Q, U, beta)
        f_pol = nmt.NmtField(mask, [Qr, Ur])
        cl_dec = wsp.decouple_cell(nmt.compute_coupled_cell(f_pol, f_pol))
        all_cl_eb.append(cl_dec[1])
        if probe_only and i + 1 >= 3:
            return (time.time() - t_mc) / 3.0
        if (i + 1) % 25 == 0:
            el = time.time() - t_mc
            eta = el / (i + 1) * (n_real - i - 1)
            print(f"[{time.time()-t0:.0f}s]  MC {i+1}/{n_real} "
                  f"({el/(i+1):.1f}s/real, ETA {eta/3600:.1f}h)", flush=True)

    all_cl_eb = np.array(all_cl_eb)
    mean_cl_eb = all_cl_eb.mean(axis=0)
    std_cl_eb = all_cl_eb.std(axis=0)
    ell_effs = b.get_effective_ells()
    cl_ee_binned = np.array([cl_ee[int(l)] if int(l) < len(cl_ee) else 0
                             for l in ell_effs])

    # chi^2 beta recovery (same grid as canonical script)
    beta_grid = np.linspace(-1.0, 1.0, 2001)
    chi2 = np.array([np.sum((mean_cl_eb - np.sin(2 * np.deg2rad(g))
                             * np.cos(2 * np.deg2rad(g)) * cl_ee_binned) ** 2)
                     for g in beta_grid])
    beta_rec = float(beta_grid[np.argmin(chi2)])

    # Per-realization recovered betas -> SNR^SE = beta_hat * sqrt(N)/sigma
    betas_per_real = []
    for row in all_cl_eb:
        chi2_r = np.array([np.sum((row - np.sin(2 * np.deg2rad(g))
                                   * np.cos(2 * np.deg2rad(g)) * cl_ee_binned) ** 2)
                           for g in beta_grid])
        betas_per_real.append(beta_grid[np.argmin(chi2_r)])
    betas_per_real = np.array(betas_per_real)
    sigma_beta = float(betas_per_real.std(ddof=1))
    snr_se = float(beta_rec * np.sqrt(n_real) / sigma_beta) if sigma_beta > 0 else float("inf")
    snr_real = snr_se / np.sqrt(n_real)

    # Theory-template SNR (canonical script definition)
    cl_eb_theory = np.sin(2 * beta) * np.cos(2 * beta) * cl_ee_binned
    snr_template = float(np.sqrt(np.sum((cl_eb_theory / (std_cl_eb + 1e-20)) ** 2)))

    return {
        "fsky_target": fsky_target,
        "fsky_actual_apodized": actual_fsky,
        "galactic_cut_deg": float(b_cut_deg),
        "nside": nside, "lmax": lmax, "n_real": n_real,
        "beta_injected_deg": beta_deg,
        "beta_recovered_deg": beta_rec,
        "bias_deg": float(beta_rec - beta_deg),
        "sigma_beta_per_realization_deg": sigma_beta,
        "snr_se": snr_se,
        "snr_per_realization": float(snr_real),
        "snr_template_canonical_def": snr_template,
        "wallclock_s": time.time() - t_mc,
    }


def main() -> int:
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    print(f"NaMaster version: {nmt.__version__}", flush=True)
    print(f"[C1] beta-injection fsky sweep: targets {FSKY_TARGETS}, "
          f"beta={BETA_INJECT_DEG} deg, N={N_REAL}, seeds {SEED_BASE}..{SEED_BASE+N_REAL-1}",
          flush=True)

    # ---- NSIDE timing probe ----
    nside = NSIDE_PRIMARY
    fallback_note = None
    print(f"[{time.time()-t0:.0f}s] timing probe: 3 realizations at NSIDE={nside}, "
          f"fsky={FSKY_TARGETS[0]} ...", flush=True)
    t_per = run_fsky(nside, FSKY_TARGETS[0], BETA_INJECT_DEG, N_REAL, t0, probe_only=True)
    projected_h = t_per * N_REAL * len(FSKY_TARGETS) / 3600.0
    print(f"[{time.time()-t0:.0f}s] probe: {t_per:.1f}s/realization -> projected total "
          f"{projected_h:.1f} h for {len(FSKY_TARGETS)}x{N_REAL} MC", flush=True)
    if projected_h > MAX_HOURS:
        nside = NSIDE_FALLBACK
        fallback_note = (f"NSIDE=512 projected {projected_h:.1f} h > {MAX_HOURS} h cap; "
                         f"fell back to NSIDE={NSIDE_FALLBACK} (lmax={2*NSIDE_FALLBACK}).")
        print(f"[{time.time()-t0:.0f}s] {fallback_note}", flush=True)

    results = []
    for fsky in FSKY_TARGETS:
        r = run_fsky(nside, fsky, BETA_INJECT_DEG, N_REAL, t0)
        results.append(r)
        print(f"[{time.time()-t0:.0f}s] fsky={fsky}: recovered beta = "
              f"{r['beta_recovered_deg']:.3f} deg (bias {r['bias_deg']:+.3f}), "
              f"SNR^SE = {r['snr_se']:.2f}", flush=True)
        # checkpoint after each fsky
        OUT.write_text(json.dumps({"job": "C1-P1B-namaster-fsky-sweep",
                                   "partial": True, "results": results}, indent=2))

    summary = {
        "job": "C1-P1B-namaster-fsky-sweep",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("P1B Sec. IV NaMaster beta-injection pipeline validation rerun at "
                    "the published-analysis sky fractions: fsky~0.85 (Planck-like) and "
                    "fsky~0.65 (ACT-DR6-like) galactic-cut masks, same apodization "
                    "recipe (2-deg smoothing) and same synthetic-LCDM + 10 uK-arcmin "
                    "noise MC method as the canonical fsky=0.32 run."),
        "scope_note": ("Pipeline-recovery validation on synthetic skies (mirrors "
                       "reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py); "
                       "NOT a sky measurement. SNR^SE = beta_hat*sqrt(N)/sigma_beta is "
                       "the estimator-calibration metric of P1B fn:snr_definition."),
        "config": {
            "nside": nside, "n_real": N_REAL, "seed_base": SEED_BASE,
            "beta_injected_deg": BETA_INJECT_DEG,
            "noise_ukarcmin": NOISE_LEVEL_UKARMIN,
            "fsky_targets": FSKY_TARGETS,
            "nside_fallback_note": fallback_note,
        },
        "canonical_reference_fsky032": CANONICAL_REF,
        "results": results,
        "wallclock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(summary, indent=2))
    print(f"\n=== C1 RESULTS ===", flush=True)
    for r in results:
        print(f"  fsky={r['fsky_target']}: beta_rec={r['beta_recovered_deg']:.3f} "
              f"bias={r['bias_deg']:+.3f} SNR^SE={r['snr_se']:.2f}", flush=True)
    print(f"wrote {OUT}  ({time.time()-t0:.0f}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

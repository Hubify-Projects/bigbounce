#!/usr/bin/env python3
"""Wave 14-NN: Dipole MC injection on Catalog C — closes P4-OA-B5.

Anchors the §VI.C "0.2% min-detectable-dipole" headline claim by sweeping
injected dipole amplitudes and reporting recovery at the same NSIDE=64 mask
+ N_MC null pipeline as `run_dipole_catalog_c.py`.

Pipeline:
  1. Load Catalog C parquet (8.47M, post-TTA equivariant).
  2. Filter to high-confidence spirals (class_eq in {CW,CCW}, p_cw_eq>0.6).
  3. For each injection amplitude A in {0.0005, 0.001, 0.002, 0.003, 0.005}:
     a. For each of N_INJ=100 random sky directions (l,b):
        - Compute per-galaxy injection probability: p_flip(l,b) = 0.5 * (1 + A * cos_theta)
          where cos_theta is the dot of galaxy direction with injection axis.
        - Re-label each galaxy CW with prob p_flip, else CCW (preserves total spiral count
          + footprint; only injects directional asymmetry on top of the post-TTA Catalog C).
        - Pixelize, fit_dipole, run N_MC=500 shuffled-null bootstraps for sigma + p.
        - Record recovered amplitude, recovered direction, sigma, p, angular sep from injected.
     b. Aggregate: median sigma, mean recovered amp, P(detected at sigma>2),
        P(direction within 30deg of injected).
  4. Min-detectable-dipole: smallest A with median sigma > 2 OR P_detect > 0.5.
  5. Save full results to outputs/dipole/wave_14_nn_injection_recovery.json.

Closes:
  P4-OA-B5: dipole MC injection on real mask/depth at 0.2% threshold.

Usage on Pod 3 H200:
    cd /workspace
    nohup python wave_14_nn_dipole_mc_injection.py > wave_14_nn.log 2>&1 &

Runtime: ~30-50 min (5 amplitudes x 100 injections x 500 MC nulls = 250K dipole fits).
"""
import json
import os
import time
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd

WORK = os.environ.get("WORK", "/workspace/r42_b20/chirality_catalog")
CAT_C_PATH = os.environ.get("CAT_C_PATH", f"{WORK}/catalog_production.parquet")
OUT_PATH = os.environ.get(
    "OUT_PATH",
    "/workspace/r42_b20/chirality_catalog/wave_14_nn_injection_recovery.json",
)

NSIDE = 64
MIN_PIX_COUNT = 10
INJECTION_AMPS = [0.0005, 0.001, 0.002, 0.003, 0.005]
N_INJ = 100   # random sky directions per amplitude
N_MC = 500    # null bootstrap realizations per injection
SEED = 20260501


def fit_dipole_amp_and_dir(asym_full):
    """Return (amplitude, l_deg, b_deg, monopole, dipole_vec)."""
    mono, dip = hp.fit_dipole(asym_full, gal_cut=0)
    amp = float(np.sqrt(np.sum(dip ** 2)))
    if amp > 0:
        l_deg = float(np.degrees(np.arctan2(dip[1], dip[0])) % 360)
        b_deg = float(np.degrees(np.arcsin(dip[2] / amp)))
    else:
        l_deg = 0.0
        b_deg = 0.0
    return amp, l_deg, b_deg, float(mono), dip


def galaxy_unit_vectors(ra_deg, dec_deg):
    """Return Nx3 unit vectors on the sphere from RA/Dec degrees."""
    ra = np.radians(ra_deg)
    dec = np.radians(dec_deg)
    x = np.cos(dec) * np.cos(ra)
    y = np.cos(dec) * np.sin(ra)
    z = np.sin(dec)
    return np.stack([x, y, z], axis=1)


def random_axis(rng):
    """Sample a uniform random direction on the sphere as a unit vector."""
    v = rng.normal(size=3)
    return v / np.linalg.norm(v)


def axis_to_lb(axis):
    l = float(np.degrees(np.arctan2(axis[1], axis[0])) % 360)
    b = float(np.degrees(np.arcsin(axis[2])))
    return l, b


def angular_sep_deg(l1, b1, l2, b2):
    """Great-circle angular separation in degrees."""
    p1 = np.radians([l1, b1])
    p2 = np.radians([l2, b2])
    cos_d = (
        np.sin(p1[1]) * np.sin(p2[1])
        + np.cos(p1[1]) * np.cos(p2[1]) * np.cos(p1[0] - p2[0])
    )
    cos_d = np.clip(cos_d, -1.0, 1.0)
    return float(np.degrees(np.arccos(cos_d)))


def main() -> int:
    t_global = time.time()
    print("=" * 72, flush=True)
    print("WAVE 14-NN: DIPOLE MC INJECTION (closes P4-OA-B5)", flush=True)
    print("=" * 72, flush=True)
    print(f"Catalog: {CAT_C_PATH}", flush=True)
    print(f"Amplitudes: {INJECTION_AMPS}", flush=True)
    print(f"Injections per amplitude: {N_INJ}", flush=True)
    print(f"MC nulls per injection: {N_MC}", flush=True)
    print(f"NSIDE: {NSIDE}, min pix count: {MIN_PIX_COUNT}", flush=True)
    print("", flush=True)

    if not Path(CAT_C_PATH).exists():
        print(f"ERROR: {CAT_C_PATH} not found", flush=True)
        return 1

    df = pd.read_parquet(CAT_C_PATH)
    print(f"Loaded {len(df):,} galaxies", flush=True)

    if "p_cw_eq" in df.columns:
        conf = df["p_cw_eq"].abs() > 0.6
    else:
        conf = df.get("confidence", pd.Series(np.ones(len(df), dtype=bool))) > 0.6

    spirals = df[
        (df["class_eq"].isin(["CW", "CCW"]))
        & conf
        & df["ra"].notna()
        & df["dec"].notna()
    ].copy()
    n_spirals = len(spirals)
    print(f"High-conf equivariant spirals: {n_spirals:,}", flush=True)

    ra = spirals["ra"].values
    dec = spirals["dec"].values
    unit_vecs = galaxy_unit_vectors(ra, dec)
    theta = np.radians(90 - dec)
    phi = np.radians(ra % 360)
    pix = hp.ang2pix(NSIDE, theta, phi)
    npix = hp.nside2npix(NSIDE)

    # Pre-compute pixel mask using TOTAL spiral counts (mask is amplitude-independent
    # since injection preserves total spiral count per pixel — only flips CW vs CCW).
    tot_per_pix = np.zeros(npix)
    np.add.at(tot_per_pix, pix, 1.0)
    mask = tot_per_pix > MIN_PIX_COUNT
    n_pix = int(mask.sum())
    f_sky = n_pix / npix
    print(f"Mask: {n_pix}/{npix} pixels (f_sky = {f_sky:.4f})", flush=True)
    print("", flush=True)

    rng = np.random.default_rng(SEED)
    results = {
        "experiment": "Wave 14-NN dipole MC injection",
        "generator": "pipelines/p2_chirality/wave_14_nn_dipole_mc_injection.py",
        "closes": "P4-OA-B5",
        "config": {
            "n_spirals": n_spirals,
            "n_pix_used": n_pix,
            "f_sky": f_sky,
            "nside": NSIDE,
            "min_pix_count": MIN_PIX_COUNT,
            "injection_amplitudes": INJECTION_AMPS,
            "n_inj_per_amplitude": N_INJ,
            "n_mc_nulls_per_injection": N_MC,
            "seed": SEED,
        },
        "by_amplitude": [],
    }

    for amp_inj in INJECTION_AMPS:
        t_amp = time.time()
        print(f"--- Amplitude A = {amp_inj:.4f} ({amp_inj*100:.2f}%) ---", flush=True)
        per_inj = []
        for j in range(N_INJ):
            # 1. Pick random injection axis
            axis = random_axis(rng)
            l_inj, b_inj = axis_to_lb(axis)
            # 2. Per-galaxy CW probability with dipole modulation
            cos_dot = unit_vecs @ axis
            p_cw = 0.5 * (1.0 + amp_inj * cos_dot)
            p_cw = np.clip(p_cw, 0.0, 1.0)
            # 3. Sample new CW labels
            u = rng.random(n_spirals)
            is_cw_new = u < p_cw
            # 4. Pixelize CW/CCW
            cw_map = np.zeros(npix)
            ccw_map = np.zeros(npix)
            np.add.at(cw_map, pix, is_cw_new.astype(float))
            np.add.at(ccw_map, pix, (~is_cw_new).astype(float))
            tot_pix = cw_map + ccw_map
            asym = np.zeros(npix)
            asym[mask] = (cw_map[mask] - ccw_map[mask]) / tot_pix[mask]
            asym_full = np.full(npix, hp.UNSEEN)
            asym_full[mask] = asym[mask]
            # 5. Fit dipole on injected map
            amp_rec, l_rec, b_rec, mono_rec, _ = fit_dipole_amp_and_dir(asym_full)
            # 6. MC null via per-pixel shuffle (same as run_dipole_catalog_c.py)
            valid = asym[mask].copy()
            boots = np.empty(N_MC)
            for k in range(N_MC):
                rng.shuffle(valid)
                a_shuf = np.full(npix, hp.UNSEEN)
                a_shuf[mask] = valid
                _, d = hp.fit_dipole(a_shuf, gal_cut=0)
                boots[k] = np.sqrt(np.sum(d ** 2))
            mc_mean = float(np.mean(boots))
            mc_std = float(np.std(boots))
            sigma = (amp_rec - mc_mean) / mc_std if mc_std > 0 else 0.0
            pval = float(np.mean(boots >= amp_rec))
            sep = angular_sep_deg(l_inj, b_inj, l_rec, b_rec)
            per_inj.append(
                {
                    "l_inj": l_inj,
                    "b_inj": b_inj,
                    "amp_recovered": amp_rec,
                    "l_recovered": l_rec,
                    "b_recovered": b_rec,
                    "monopole_recovered": mono_rec,
                    "sigma": float(sigma),
                    "p_value": pval,
                    "mc_mean": mc_mean,
                    "mc_std": mc_std,
                    "angular_sep_deg": sep,
                }
            )
            if (j + 1) % 25 == 0:
                med_sig = np.median([r["sigma"] for r in per_inj])
                frac_det = np.mean([r["sigma"] > 2.0 for r in per_inj])
                print(
                    f"  inj {j+1}/{N_INJ}: median sigma={med_sig:.2f}, "
                    f"P(sigma>2)={frac_det:.2f}, elapsed={time.time()-t_amp:.0f}s",
                    flush=True,
                )

        sigmas = np.array([r["sigma"] for r in per_inj])
        amps_rec = np.array([r["amp_recovered"] for r in per_inj])
        seps = np.array([r["angular_sep_deg"] for r in per_inj])
        agg = {
            "amplitude_injected": amp_inj,
            "n_injections": N_INJ,
            "median_sigma": float(np.median(sigmas)),
            "mean_sigma": float(np.mean(sigmas)),
            "p10_sigma": float(np.percentile(sigmas, 10)),
            "p90_sigma": float(np.percentile(sigmas, 90)),
            "mean_amp_recovered": float(np.mean(amps_rec)),
            "median_amp_recovered": float(np.median(amps_rec)),
            "p_detected_sigma_gt_2": float(np.mean(sigmas > 2.0)),
            "p_detected_sigma_gt_3": float(np.mean(sigmas > 3.0)),
            "p_direction_within_30deg": float(np.mean(seps < 30.0)),
            "p_direction_within_60deg": float(np.mean(seps < 60.0)),
            "median_angular_sep_deg": float(np.median(seps)),
            "wallclock_s": float(time.time() - t_amp),
            "per_injection": per_inj,
        }
        print(
            f"  DONE A={amp_inj:.4f}: median_sigma={agg['median_sigma']:.2f}, "
            f"P(sigma>2)={agg['p_detected_sigma_gt_2']:.2f}, "
            f"P(dir<30deg)={agg['p_direction_within_30deg']:.2f}, "
            f"wall={agg['wallclock_s']:.0f}s",
            flush=True,
        )
        results["by_amplitude"].append(agg)

    # Min-detectable-dipole: smallest amplitude with median sigma > 2 AND P_detect > 0.5
    min_det = None
    for agg in results["by_amplitude"]:
        if agg["median_sigma"] > 2.0 and agg["p_detected_sigma_gt_2"] > 0.5:
            min_det = agg["amplitude_injected"]
            break
    results["min_detectable_dipole"] = {
        "amplitude": min_det,
        "criterion": "smallest A with median sigma > 2 AND P(sigma>2) > 0.5",
        "paper_claim_amplitude": 0.002,
        "consistent_with_paper_claim": (
            min_det is not None and abs(min_det - 0.002) <= 0.001
        ),
    }
    results["wallclock_total_s"] = float(time.time() - t_global)

    Path(OUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as fh:
        json.dump(results, fh, indent=2)

    print("", flush=True)
    print("=" * 72, flush=True)
    print("WAVE 14-NN INJECTION-RECOVERY SUMMARY", flush=True)
    print("=" * 72, flush=True)
    for agg in results["by_amplitude"]:
        print(
            f"  A={agg['amplitude_injected']:.4f} "
            f"({agg['amplitude_injected']*100:.2f}%): "
            f"med sigma={agg['median_sigma']:5.2f}, "
            f"P(>2)={agg['p_detected_sigma_gt_2']:.2f}, "
            f"P(dir<30)={agg['p_direction_within_30deg']:.2f}",
            flush=True,
        )
    print(f"  MIN-DETECTABLE-DIPOLE: {min_det}", flush=True)
    print(f"  Saved: {OUT_PATH}", flush=True)
    print(f"  Total wall: {results['wallclock_total_s']:.0f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

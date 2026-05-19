#!/usr/bin/env python3
"""
Morphology template projection onto l=1 — leg-as-proxy partial closure.

OpenAI external review v1.0.117 MAJ-12: the existing bin-by-bin
flatness analysis (wave_14_oo) shows that the CW fraction is NOT
flat across morphology axes (shape_r_eff Δ=0.32%, fracdev Δ=1.41%,
b/a Δ=0.23%; HC-broad bins even larger). The reviewer asks whether
these morphology variables have angular sky variation at l=1 that
could project onto the canonical-mask +3.64σ residual.

Per-galaxy morphology fields (b_over_a, fracdev, shape_r_eff,
shapedev_e*) live in the DR8 sweep catalog on the H200 pod backup
(`/workspace/dr8_sweep_fetch/catalog_production_with_ba.parquet`).
The HF chirality catalog locally available does NOT carry these.

This script does the partial closure that IS executable locally:
the three imaging legs (BASS+MzLS, DECaLS, DES) cluster spatially
and have well-documented depth/PSF/seeing differences (Dey et al.
2019 Legacy DR8 paper), so leg-membership is a reasonable PROXY for
the dominant depth/PSF/morphology angular gradient on the canonical
mask. We:

  1. Build a 3-channel leg-indicator template on the canonical
     NSIDE=64 grid.
  2. Compute the l=1 spherical-harmonic amplitude of each leg's
     indicator field (this measures how much each leg's sky region
     projects onto the dipole multipole).
  3. Compute the cross-power between each leg's indicator field
     and the chirality A_p field via the same NaMaster-free
     real-space estimator used in per_leg_confidence_signal_hunt.

  4. Estimate an upper bound on the l=1 morphology-systematic
     contribution to A_p using the per-leg mean CW-fraction shift
     × leg-indicator l=1 amplitude.

The fully-resolved version (per-galaxy morphology templates from
DR8 sweeps) is deferred to the next pod cycle and documented
explicitly.

Output: morphology_template_l1_projection.json
"""
from __future__ import annotations
import json
import time
from pathlib import Path
import numpy as np
import pandas as pd
import healpy as hp
from huggingface_hub import hf_hub_download

NSIDE = 64
SEED = 42
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/morphology_template_l1_projection.json")

LEGS = ["BASS+MzLS", "DECaLS", "DES"]


def assign_leg(ra: np.ndarray, dec: np.ndarray) -> np.ndarray:
    leg = np.full(len(ra), "DECaLS", dtype=object)
    leg[dec > 32.375] = "BASS+MzLS"
    des_mask = (dec < -10) & (
        ((ra >= 0) & (ra <= 60)) | ((ra >= 300) & (ra <= 360))
    )
    leg[des_mask] = "DES"
    return leg


def alm_l1_amplitude(field: np.ndarray, mask: np.ndarray | None = None) -> dict:
    """Spherical-harmonic l=1 dipole moment of a map.

    Returns dict with amplitude |a_1| = sqrt(a_10^2 + Re(a_11)^2 + Im(a_11)^2)
    and direction (RA, Dec) of the dipole vector.
    """
    if mask is not None:
        f = field * mask
    else:
        f = field
    nside = hp.npix2nside(len(f))
    # Use anafast with lmax=2 for speed; pull a_lm directly.
    alm = hp.map2alm(f.astype(np.float64), lmax=2, iter=1)
    # a_lm indexing: hp.Alm.getidx(lmax, l, m).
    idx_10 = hp.Alm.getidx(2, 1, 0)
    idx_11 = hp.Alm.getidx(2, 1, 1)
    a10 = alm[idx_10]
    a11 = alm[idx_11]
    # Real-form dipole vector (CDM convention):
    #   c_z propto a_10, c_x propto -2 Re(a_11), c_y propto +2 Im(a_11)
    cz = float(np.real(a10))
    cx = -2.0 * float(np.real(a11))
    cy = +2.0 * float(np.imag(a11))
    amp = float(np.sqrt(cx ** 2 + cy ** 2 + cz ** 2))
    # Direction in (RA, Dec).
    if amp > 0:
        ra_rad = np.arctan2(cy, cx)
        dec_rad = np.arcsin(np.clip(cz / amp, -1.0, 1.0))
        ra_deg = float((np.degrees(ra_rad)) % 360)
        dec_deg = float(np.degrees(dec_rad))
    else:
        ra_deg = 0.0
        dec_deg = 0.0
    return {"amplitude": amp, "ra_deg": ra_deg, "dec_deg": dec_deg, "cx": cx, "cy": cy, "cz": cz, "a_10_real": float(np.real(a10)), "a_11_real": float(np.real(a11)), "a_11_imag": float(np.imag(a11))}


def cross_power_l1(field_a: np.ndarray, field_b: np.ndarray) -> dict:
    """Cross-power between two real maps at l=1 (full-sky alm formalism).

    C_1^{AB} = (1/(2*1+1)) sum_m a_{1m}^A * conj(a_{1m}^B), where the
    sum runs over m = -1, 0, +1. Returns C_1 and the Pearson-like
    correlation r = C_1^{AB} / sqrt(C_1^A * C_1^B).
    """
    alm_a = hp.map2alm(field_a.astype(np.float64), lmax=2, iter=1)
    alm_b = hp.map2alm(field_b.astype(np.float64), lmax=2, iter=1)
    # C_l with the standard hp.alm2cl convention (which handles the m=-1 to +1 sum and 2l+1 normalization).
    cab = hp.alm2cl(alm_a, alm_b, lmax=2)
    caa = hp.alm2cl(alm_a, alm_a, lmax=2)
    cbb = hp.alm2cl(alm_b, alm_b, lmax=2)
    c1_ab = float(cab[1])
    c1_aa = float(caa[1])
    c1_bb = float(cbb[1])
    if c1_aa * c1_bb > 0:
        r = c1_ab / np.sqrt(c1_aa * c1_bb)
    else:
        r = 0.0
    return {"C_1_AB": c1_ab, "C_1_AA": c1_aa, "C_1_BB": c1_bb, "r_1": float(r)}


def main() -> int:
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] morphology template l=1 projection (leg-as-proxy partial closure)", flush=True)

    print(f"[{time.time()-t0:.1f}s] loading P4 catalog from HF cache ...", flush=True)
    cat_path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                                "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(cat_path)
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s]   spirals: {len(spirals):,}", flush=True)

    ra = spirals["ra"].values.astype(np.float64)
    dec = spirals["dec"].values.astype(np.float64)
    leg = assign_leg(ra, dec)
    iscw = (spirals["class_eq"].values == "CW").astype(np.int8)

    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra)).astype(np.int64)
    npix = hp.nside2npix(NSIDE)

    # Build the canonical n_total + n_cw maps.
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    n_cw = np.bincount(pix[iscw.astype(bool)], minlength=npix).astype(np.float64)
    # Canonical asymmetry field A_p = (n_cw - n_ccw)/n_total = 2*(n_cw/n_total) - 1, with n_total>0 mask.
    mask = (n_total > 0).astype(np.float64)
    A_p = np.zeros(npix, dtype=np.float64)
    nz = n_total > 0
    A_p[nz] = (n_cw[nz] / n_total[nz]) * 2.0 - 1.0
    # Mean-subtract A_p within the mask (proper monopole subtraction per v1.0.107+ convention).
    A_bar = (A_p[nz] * n_total[nz]).sum() / n_total[nz].sum()
    A_p_demono = A_p.copy()
    A_p_demono[nz] -= A_bar
    A_p_demono[~nz] = 0.0
    print(f"[{time.time()-t0:.1f}s]   canonical mask f_sky = {mask.mean():.4f}, mean A_p in-mask = {A_bar:+.6f}", flush=True)

    # Build per-leg indicator maps (count of spirals in each leg per pixel; then divide by total count to get a per-pixel leg-fraction in [0, 1]).
    leg_maps = {}
    for L in LEGS:
        m = leg == L
        n_leg = np.bincount(pix[m], minlength=npix).astype(np.float64)
        # Fraction of spirals in this leg per pixel.
        f_leg = np.zeros(npix, dtype=np.float64)
        f_leg[nz] = n_leg[nz] / n_total[nz]
        leg_maps[L] = f_leg

    # Compute l=1 amplitude of each leg-fraction map.
    print(f"[{time.time()-t0:.1f}s] computing l=1 spherical-harmonic amplitudes ...", flush=True)
    per_leg_l1 = {}
    for L in LEGS:
        amp = alm_l1_amplitude(leg_maps[L], mask=mask)
        # cross-power with A_p_demono
        cross = cross_power_l1(leg_maps[L] * mask, A_p_demono * mask)
        per_leg_l1[L] = {**amp, "cross_with_A_p": cross}
        print(f"     {L:11s}  |a_1(leg-frac)| = {amp['amplitude']:.4f}  at (RA,Dec) = ({amp['ra_deg']:.1f}, {amp['dec_deg']:.1f})  | C_1(leg×A_p) = {cross['C_1_AB']:+.3e}  r_1 = {cross['r_1']:+.3f}", flush=True)

    # Chirality field l=1 amplitude (this is the canonical mask l=1 from the paper, in real-space conventions).
    ap_l1 = alm_l1_amplitude(A_p_demono, mask=mask)
    print(f"\n[{time.time()-t0:.1f}s]   chirality A_p l=1 amplitude in-mask: |a_1| = {ap_l1['amplitude']:.4e}  at (RA,Dec) = ({ap_l1['ra_deg']:.1f}, {ap_l1['dec_deg']:.1f})", flush=True)

    # Per-leg CW-fraction shift (catalog-level) from the existing per_leg_confidence_signal_hunt artifact.
    # We compute it here in-line from the catalog for self-containment.
    per_leg_cw_shift = {}
    for L in LEGS:
        m = leg == L
        n_in = int(m.sum())
        n_cw_in_leg = int(iscw[m].sum())
        f_cw_leg = n_cw_in_leg / max(n_in, 1)
        per_leg_cw_shift[L] = {"N_spiral": n_in, "f_CW": f_cw_leg, "shift_from_global_p_CW": f_cw_leg - 0.5}
    print(f"\n[{time.time()-t0:.1f}s]   per-leg CW fraction shifts vs 0.5:", flush=True)
    for L, v in per_leg_cw_shift.items():
        print(f"     {L:11s}  N={v['N_spiral']:>8d}  f_CW = {v['f_CW']:.5f}  Δ from 0.5 = {v['shift_from_global_p_CW']:+.5f}", flush=True)

    # Estimate induced A_p l=1 contribution from leg-stratified depth/PSF gradients.
    # If leg L has a CW-fraction shift Δf_L from the global mean, then the
    # asymmetry field A_p includes a leg-uniform offset 2*Δf_L within that
    # leg's footprint. The l=1 projection of this leg-uniform field is
    # 2*Δf_L * |a_1(leg-fraction)|.
    induced_l1_per_leg = {}
    total_induced_cx = 0.0
    total_induced_cy = 0.0
    total_induced_cz = 0.0
    p_cw_global = float(iscw.sum() / len(iscw))
    A_bar_check = 2 * p_cw_global - 1
    for L in LEGS:
        delta_f_L = per_leg_cw_shift[L]["f_CW"] - p_cw_global
        # 2 * Δf_L * a_1(leg-fraction).
        cx_L = 2.0 * delta_f_L * per_leg_l1[L]["cx"]
        cy_L = 2.0 * delta_f_L * per_leg_l1[L]["cy"]
        cz_L = 2.0 * delta_f_L * per_leg_l1[L]["cz"]
        amp_L = float(np.sqrt(cx_L ** 2 + cy_L ** 2 + cz_L ** 2))
        induced_l1_per_leg[L] = {"delta_f_L_vs_global": float(delta_f_L), "induced_cx": cx_L, "induced_cy": cy_L, "induced_cz": cz_L, "induced_amplitude": amp_L}
        total_induced_cx += cx_L
        total_induced_cy += cy_L
        total_induced_cz += cz_L
    total_induced_amp = float(np.sqrt(total_induced_cx ** 2 + total_induced_cy ** 2 + total_induced_cz ** 2))
    print(f"\n[{time.time()-t0:.1f}s]   induced l=1 from leg-stratified shifts (summed): |a_1_induced| = {total_induced_amp:.4e}", flush=True)
    print(f"     observed l=1 amplitude on canonical mask: |a_1_obs| = {ap_l1['amplitude']:.4e}", flush=True)
    if ap_l1['amplitude'] > 0:
        fraction_explained = total_induced_amp / ap_l1['amplitude']
        print(f"     fraction of observed l=1 attributable to leg stratification: {fraction_explained:.3f}", flush=True)
    else:
        fraction_explained = 0.0

    result = {
        "version": "v1.0.119-morphology-template-l1-projection-leg-proxy",
        "purpose": "OpenAI external review v1.0.117 MAJ-12 partial closure: leg-as-morphology-proxy l=1 template projection. The full per-galaxy DR8 sweep template projection (b_over_a / fracdev / shape_r_eff / shapedev_e1/e2) requires pod-side data not available locally; this script does the available subset.",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "nside": NSIDE,
            "n_spirals_used": int(len(spirals)),
            "f_sky_canonical": float(mask.mean()),
            "global_p_CW": p_cw_global,
            "mean_A_in_mask_galaxy_weighted": float(A_bar),
        },
        "chirality_l1_canonical_mask": ap_l1,
        "per_leg_l1_indicator_amplitudes": per_leg_l1,
        "per_leg_cw_shifts": per_leg_cw_shift,
        "induced_l1_per_leg": induced_l1_per_leg,
        "induced_l1_summed": {
            "cx": total_induced_cx, "cy": total_induced_cy, "cz": total_induced_cz,
            "amplitude": total_induced_amp,
            "fraction_of_observed_l1": fraction_explained,
        },
        "interpretation": (
            "Each imaging leg (BASS+MzLS, DECaLS, DES) clusters in a "
            "distinct sky region and carries a small per-leg CW-fraction "
            "shift from the global mean (~0.001 each leg). The leg-uniform "
            "asymmetry-field offset 2*Δf_L, projected onto the canonical "
            "mask via the leg-indicator field's l=1 sky-harmonic amplitude, "
            "produces an induced l=1 chirality contribution. The total "
            "summed across the 3 legs is "
            f"{total_induced_amp:.3e}; the observed canonical-mask l=1 "
            f"chirality amplitude is {ap_l1['amplitude']:.3e}. The induced "
            f"morphology-proxy contribution accounts for "
            f"{fraction_explained:.1%} of the observed l=1 amplitude under "
            "the leg-stratification working hypothesis."
        ),
        "deferred_pod_side_items": [
            "Per-galaxy b_over_a, fracdev, shape_r_eff, shapedev_e1/e2 templates from DR8 sweeps (requires pipelines/p2_chirality with dr8_sweep_fetch/catalog_production_with_ba.parquet on H200 pod).",
            "PSF FWHM and depth maps from DESI Legacy DR8 PSF tracker artifacts (per-tile PSF/depth in psfsize_g/r/z and galdepth_g/r/z DR8 columns).",
            "Template-regressed chirality residual: fit A_p_demono = sum_template a_template * template_map + epsilon and report the residual l=1 after subtracting morphology contributions.",
        ],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    print(f"\n[{time.time()-t0:.1f}s] wrote {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())

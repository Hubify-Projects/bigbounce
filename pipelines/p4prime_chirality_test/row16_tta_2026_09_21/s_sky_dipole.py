#!/usr/bin/env python3
"""Step S — projecting the row-16(ii-b) S6 sky dependence onto a dipole.

Pre-registration: PREREGISTRATION_2026-09-21.md "Step S", committed BEFORE this
script was run (git 712e9e7e).

Mechanism, fixed in advance (sec. S0): observed-label asymmetry
A_obs(n) = D(n) A_true(n). A sky-varying dilution cannot manufacture a dipole
from a zero true asymmetry; the spurious dipole is sourced by the product of the
sky-varying dilution and the NON-ZERO MONOPOLE of the observed label asymmetry.
Writing D(n) = Dbar (1 + delta(n)), A_obs acquires a dipole |A_mono| * a_delta.

Statistics S1, S2a-S2d and the threshold of S3 are as declared. Anything beyond
them is labelled POST-HOC in this file and in the results document.

Input : ../row16_pa_parity_transfer/pa_transfer_probs.npz  (stage-1 cropped grid)
        ../injection_pilot/scale20k_sample.parquet         (RA/Dec)
        ../../p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet
Output: s_sky_dipole.json
"""
import json
import sys
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

HERE = Path(__file__).resolve().parent
ROW16 = HERE.parent / "row16_pa_parity_transfer"
PILOT = HERE.parent / "injection_pilot"
CATALOG = HERE.parents[1] / "p2_chirality" / "apjs_release_v1.0.244" / "p4_catalog_primary_safe_v1.0.244.parquet"
OUT = HERE / "s_sky_dipole.json"

sys.path.insert(0, str(HERE.parent / "full_parent"))
import full_parent_estimator_lib as lib  # noqa: E402  (imports build_projector verbatim)

CW, CCW, NS = 0, 1, 2
CONTROL_ANGLES = (0, 180)
NSIDE_MAP = 8           # resolution of the epsilon map (pre-registered)
MIN_GAL_PIX = 5         # pre-registered
N_BOOT = 1000
N_PERM = 1000
SEED = 20260921
AXIS_STRICT = (195.5, -57.2)
AXIS_PARENT = (278.629719594135, 25.3202680239249)
A95_FULL_PARENT = 0.005095238095238095   # row16i_full_parent_dipole.json
A95_STRICT = 0.0098                      # comparison_887k_strict_primary
A_OBS_FULL_PARENT = 0.005660281175118039


def eq_triple(P, angles, kind, ai):
    """Production Z2 flip-TTA equivariant (cw, ccw, ns); identical to
    row16_pa_parity_transfer/s1_pa_transfer_analysis.py."""
    nai = angles.index((-angles[ai]) % 360)
    a, b = P[:, kind, ai, :], P[:, 1 - kind, nai, :]
    return np.stack([(a[:, 0] + b[:, 1]) / 2,
                     (a[:, 1] + b[:, 0]) / 2,
                     (a[:, 2] + b[:, 2]) / 2], axis=1)


def unit(ra_deg, dec_deg):
    ra, dec = np.radians(ra_deg), np.radians(dec_deg)
    return np.array([np.cos(dec) * np.cos(ra), np.cos(dec) * np.sin(ra), np.sin(dec)])


def vec_to_radec(v):
    v = np.asarray(v, dtype=float)
    v = v / np.linalg.norm(v)
    return float(np.degrees(np.arctan2(v[1], v[0])) % 360.0), float(np.degrees(np.arcsin(v[2])))


def fit_eps_dipole(pix, eps, npix):
    """NSIDE_MAP map of mean epsilon over pixels with >= MIN_GAL_PIX galaxies,
    then healpy.fit_dipole (unweighted -- the P4' estimator convention)."""
    tot = np.bincount(pix, minlength=npix)
    s = np.bincount(pix, weights=eps, minlength=npix)
    keep = tot >= MIN_GAL_PIX
    m = np.full(npix, hp.UNSEEN)
    m[keep] = s[keep] / tot[keep]
    mono, vec = hp.fit_dipole(m, gal_cut=0)
    return float(mono), np.asarray(vec, dtype=float), int(keep.sum()), int(tot[keep].sum())


def main():
    rng = np.random.default_rng(SEED)
    d = np.load(ROW16 / "pa_transfer_probs.npz")
    P, idx, angles = d["probs"], d["idx"], [int(a) for a in d["angles"]]
    n = len(idx)
    assert int(d["n_done"]) == n and not np.isnan(P).any(), "stage-1 inference incomplete"
    informative = [a for a in angles if a not in CONTROL_ANGLES]

    clsX = {phi: np.argmax(eq_triple(P, angles, 0, i), 1) for i, phi in enumerate(angles)}
    clsY = {phi: np.argmax(eq_triple(P, angles, 1, i), 1) for i, phi in enumerate(angles)}

    # ---- S1: per-galaxy transfer statistic over the informative angles ----
    num = np.zeros(n)
    den = np.zeros(n)
    for phi in informative:
        sx, sy = clsX[phi], clsY[phi]
        spiral = sx != NS
        swap = np.where(sx == CW, CCW, np.where(sx == CCW, CW, NS))
        den += spiral
        num += spiral & (sy == swap)
    has = den > 0
    eps_i = np.zeros(n)
    eps_i[has] = num[has] / den[has]

    sample = pd.read_parquet(PILOT / "scale20k_sample.parquet")
    ra = sample["ra"].values[idx][has]
    dec = sample["dec"].values[idx][has]
    eps = eps_i[has]
    m = eps.size

    # consistency with the S1 confusion-matrix eps_bar (different weighting; not
    # required to be equal, reported so the difference is visible)
    s1_eps_bar_inf = 0.6363   # ROW16IIB sec.5, s1_pa_transfer_results.json
    per_galaxy_mean = float(eps.mean())

    # ---- S2a: hemisphere splits on both axes ----
    s2a = {}
    for name, axis in (("strict_887k_axis", AXIS_STRICT), ("full_parent_axis", AXIS_PARENT)):
        nhat = unit(*axis)
        g = unit(ra, dec).T @ nhat
        north = g >= 0
        dlt = float(eps[north].mean() - eps[~north].mean())
        bd = np.empty(N_BOOT)
        for b in range(N_BOOT):
            rn = rng.integers(0, north.sum(), size=int(north.sum()))
            rs = rng.integers(0, (~north).sum(), size=int((~north).sum()))
            bd[b] = eps[north][rn].mean() - eps[~north][rs].mean()
        s2a[name] = {"axis_ra_dec_deg": list(axis),
                     "n_north": int(north.sum()), "n_south": int((~north).sum()),
                     "eps_bar_north": float(eps[north].mean()),
                     "eps_bar_south": float(eps[~north].mean()),
                     "delta": dlt, "delta_boot_se": float(bd.std(ddof=1)),
                     "delta_z": float(dlt / bd.std(ddof=1))}

    # ---- S2b: dipole fit to the epsilon map, with bootstrap and permutation null ----
    npix = hp.nside2npix(NSIDE_MAP)
    pix = hp.ang2pix(NSIDE_MAP, np.radians(90.0 - dec), np.radians(ra % 360.0))
    mono, vec, n_pix_used, n_gal_used = fit_eps_dipole(pix, eps, npix)
    amp = float(np.linalg.norm(vec))
    a_delta = amp / mono
    dip_ra, dip_dec = vec_to_radec(vec)

    boot_amp = np.empty(N_BOOT)
    boot_frac = np.empty(N_BOOT)
    boot_vec = np.empty((N_BOOT, 3))
    for b in range(N_BOOT):
        r = rng.integers(0, m, size=m)
        mo, ve, _, _ = fit_eps_dipole(pix[r], eps[r], npix)
        boot_amp[b] = np.linalg.norm(ve)
        boot_frac[b] = boot_amp[b] / mo
        boot_vec[b] = ve
    perm_amp = np.empty(N_PERM)
    for b in range(N_PERM):
        _, ve, _, _ = fit_eps_dipole(pix, rng.permutation(eps), npix)
        perm_amp[b] = np.linalg.norm(ve)
    rank_k = int(np.count_nonzero(perm_amp >= amp))

    s2b = {"nside_map": NSIDE_MAP, "min_galaxies_per_pixel": MIN_GAL_PIX,
           "n_pixels_used": n_pix_used, "n_galaxies_used": n_gal_used,
           "n_galaxies_with_informative_angle": m, "n_dropped_no_informative_angle": int(n - m),
           "monopole_eps": mono, "dipole_amplitude_eps": amp,
           "dipole_amplitude_eps_boot_se": float(boot_amp.std(ddof=1)),
           "fractional_dipole_a_delta": a_delta,
           "fractional_dipole_a_delta_boot_se": float(boot_frac.std(ddof=1)),
           "dipole_ra_deg": dip_ra, "dipole_dec_deg": dip_dec,
           "permutation_null": {"n_perm": N_PERM, "mean": float(perm_amp.mean()),
                                "std": float(perm_amp.std(ddof=0)),
                                "z_moment": float((amp - perm_amp.mean()) / perm_amp.std(ddof=0)),
                                "rank_k_ge_observed": rank_k,
                                "rank_p_one_sided": (rank_k + 1) / (N_PERM + 1)}}

    # ---- S2c: induced spurious label dipole through the EXACT P4' estimator ----
    table = pq.read_table(CATALOG, columns=["ra_deg", "dec_deg", "class_eq",
                                            "primary_hc", "raw_flip_qc_unsafe"])
    n_parent_rows = table.num_rows
    spiral = pc.is_in(table["class_eq"], value_set=pa.array(["CW", "CCW"]))
    strict_sel = pc.and_(pc.equal(table["primary_hc"], True),
                         pc.equal(table["raw_flip_qc_unsafe"], False))

    def support_block(mask, label):
        t = table.filter(mask)
        pra = t["ra_deg"].combine_chunks().to_numpy(zero_copy_only=False)
        pdec = t["dec_deg"].combine_chunks().to_numpy(zero_copy_only=False)
        lab = np.asarray(t["class_eq"].combine_chunks().to_pylist(), dtype=object)
        total, cwm = lib.maps_from_radec(pra, pdec, lab == "CW")
        support, capacities, projector, A_obs = lib.build_projector(total, cwm)
        sidx = np.flatnonzero(support)
        obs = (2.0 * cwm[support] - capacities) / capacities
        coeff = projector @ obs
        A_mono = float(coeff[0])
        th, ph = hp.pix2ang(lib.NSIDE, sidx)
        nvec = np.column_stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])

        def induced(v, mo):
            delta = (nvec @ v) / mo
            return float(np.linalg.norm((projector @ (A_mono * (1.0 + delta)))[1:4]))

        A_ind = induced(vec, mono)
        b_ind = np.array([induced(boot_vec[b], mono) for b in range(N_BOOT)])
        return {"selection": label, "n_rows": t.num_rows,
                "n_support_pixels": int(sidx.size), "n_galaxies_in_support": int(capacities.sum()),
                "A_obs_amplitude": A_obs, "A_monopole": A_mono,
                "A_induced_spurious_dipole": A_ind,
                "A_induced_boot_se": float(b_ind.std(ddof=1)),
                "A_induced_pct": 100.0 * A_ind}, projector, nvec, A_mono

    full_blk, _, _, _ = support_block(spiral, "class_eq in (CW,CCW) -- full parent")
    strict_blk, _, _, _ = support_block(pc.and_(strict_sel, spiral),
                                        "primary_hc AND NOT raw_flip_qc_unsafe -- strict primary")

    # ---- S2d: alignment of the epsilon dipole with the observed A_obs axis ----
    def sep(axis):
        c = float(np.dot(unit(*axis), np.asarray(vec) / np.linalg.norm(vec)))
        return {"axis_ra_dec_deg": list(axis), "cos_angle": c,
                "angle_deg": float(np.degrees(np.arccos(np.clip(c, -1, 1))))}

    s2d = {"vs_full_parent_A_obs_axis": sep(AXIS_PARENT),
           "vs_strict_887k_axis": sep(AXIS_STRICT)}

    # ---- S3: pre-declared threshold ----
    thr_full = 0.10 * A95_FULL_PARENT
    thr_strict = 0.10 * A95_STRICT
    caveat = (full_blk["A_induced_spurious_dipole"] > thr_full
              or strict_blk["A_induced_spurious_dipole"] > thr_strict)
    verdict = {
        "threshold": "caveat required iff A_induced > 0.10 * A95_obs on either support "
                     "(pre-registered Step S sec.S3)",
        "A95_obs_full_parent": A95_FULL_PARENT, "threshold_full_parent": thr_full,
        "A95_obs_strict_887k": A95_STRICT, "threshold_strict": thr_strict,
        "A_induced_over_A95_full_parent": full_blk["A_induced_spurious_dipole"] / A95_FULL_PARENT,
        "A_induced_over_A95_strict": strict_blk["A_induced_spurious_dipole"] / A95_STRICT,
        "A_induced_over_A_obs_full_parent": full_blk["A_induced_spurious_dipole"] / A_OBS_FULL_PARENT,
        "CAVEAT_REQUIRED": bool(caveat),
    }

    # ---- POST-HOC (not pre-registered, labelled here and in the document) ----
    pairs = pd.read_parquet(PILOT / "scale20k_pairs.parquet").set_index("idx")
    common = [i for i in idx.tolist() if i in pairs.index]
    pr = pairs.loc[common]
    eqc = np.stack([(pr["p_cw_orig"].values + pr["p_ccw_flip"].values) / 2,
                    (pr["p_ccw_orig"].values + pr["p_cw_flip"].values) / 2,
                    (pr["p_ns_orig"].values + pr["p_ns_flip"].values) / 2], 1)
    hc_mask_common = (np.argmax(eqc, 1) != NS) & (np.max(eqc[:, :2], axis=1) > 0.6)
    pos = {v: k for k, v in enumerate(idx.tolist())}
    hc_rows = np.array([pos[i] for i in common])[hc_mask_common]
    hc_in_has = np.isin(np.flatnonzero(has), hc_rows)
    posthoc = {"_label": "POST-HOC, not pre-registered: the same dipole fit restricted "
                         "to the catalogue's primary_hc galaxies, because S2c applies a "
                         "delta measured on all parent spirals to the strict-primary support"}
    if hc_in_has.sum() >= 500:
        mo_h, ve_h, npx_h, ng_h = fit_eps_dipole(pix[hc_in_has], eps[hc_in_has], npix)
        posthoc.update({"n": int(hc_in_has.sum()), "n_pixels_used": npx_h,
                        "monopole_eps": mo_h,
                        "dipole_amplitude_eps": float(np.linalg.norm(ve_h)),
                        "fractional_dipole_a_delta": float(np.linalg.norm(ve_h) / mo_h),
                        "dipole_ra_deg": vec_to_radec(ve_h)[0],
                        "dipole_dec_deg": vec_to_radec(ve_h)[1]})

    out = {
        "preregistration": "PREREGISTRATION_2026-09-21.md Step S (git 712e9e7e, committed "
                           "before this script ran)",
        "input_grid": "row16(ii-b) stage-1 cropped 8-angle grid (the grid the S6 finding "
                      "was made on)",
        "n_galaxies_total": int(n),
        "S1_per_galaxy_eps_definition": "per galaxy: (#informative phi with L(X_phi) spiral "
                                        "and L(Y_phi)=swap) / (#informative phi with L(X_phi) spiral)",
        "S1_per_galaxy_eps_mean": per_galaxy_mean,
        "S1_confusion_matrix_eps_bar_informative_for_comparison": s1_eps_bar_inf,
        "S2a_hemisphere_splits": s2a,
        "S2b_eps_dipole_fit": s2b,
        "S2c_induced_label_dipole": {"catalog": str(CATALOG.relative_to(HERE.parents[2])),
                                     "n_parent_rows": n_parent_rows,
                                     "estimator": "build_projector imported verbatim via "
                                                  "full_parent_estimator_lib (NSIDE=64, support>=10)",
                                     "model": "m(n) = A_mono * (1 + delta(n)), delta from the "
                                              "fitted epsilon dipole (Step S sec.S0)",
                                     "full_parent": full_blk, "strict_primary": strict_blk},
        "S2d_alignment": s2d,
        "S3_verdict": verdict,
        "POSTHOC_primary_hc_eps_dipole": posthoc,
        "n_bootstrap": N_BOOT, "n_permutations": N_PERM, "seed": SEED,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ("S2c_induced_label_dipole",)}, indent=2))
    print(json.dumps(out["S2c_induced_label_dipole"], indent=2))


if __name__ == "__main__":
    main()

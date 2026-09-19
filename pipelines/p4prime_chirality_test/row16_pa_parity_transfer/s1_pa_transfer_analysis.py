#!/usr/bin/env python3
"""Row 16(ii-b) analysis — PA-restoring parity transfer through the released
P4' chirality pipeline.

Pre-registration: PREREGISTRATION_2026-09-19.md (commit 12248d70), written and
committed BEFORE any statistic here was computed. Statistics S1, S2, S3, S5, S6
are as declared there; anything computed beyond them is labelled POST-HOC in
both this file and the results document.

Input : pa_transfer_probs.npz  (run_pa_transfer_inference.py)
Output: s1_pa_transfer_results.json
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
PILOT = HERE.parent / "injection_pilot"
NPZ = HERE / "pa_transfer_probs.npz"
OUT = HERE / "s1_pa_transfer_results.json"

CW, CCW, NS = 0, 1, 2
CONTROL_ANGLES = (0, 180)              # exact TTA identity; positive control
N_BOOT = 1000                          # pre-registered cluster bootstrap
FRACTIONS = [0.0, 0.005, 0.01, 0.02, 0.05]
N_SEEDS_S3 = 200
# strict-887,472-subset dipole axis, ROW16IB_AXIS_SHIFT_2026-09-04.md line 95
AXIS_STRICT = (195.5, -57.2)
AXIS_PARENT = (278.629719594135, 25.3202680239249)   # row16i_full_parent_dipole.json


def eq_triple(P, angles, kind, ai):
    """Production Z2 flip-TTA equivariant (cw, ccw, ns) at rotation angles[ai].
    kind 0 = X (observed galaxy, rotated); 1 = Y (parity-flipped, PA restored)."""
    nai = angles.index((-angles[ai]) % 360)
    a = P[:, kind, ai, :]
    b = P[:, 1 - kind, nai, :]
    return np.stack([(a[:, 0] + b[:, 1]) / 2,
                     (a[:, 1] + b[:, 0]) / 2,
                     (a[:, 2] + b[:, 2]) / 2], axis=1)


def confusion(src, dst):
    """3x3 row-normalised transition matrix P(dst = c' | src = c)."""
    M = np.zeros((3, 3))
    for c in range(3):
        m = src == c
        nc = int(m.sum())
        M[c] = np.bincount(dst[m], minlength=3) / nc if nc else np.nan
    return M


def eps_rho_L(src, dst):
    M = confusion(src, dst)
    return (float((M[CW, CCW] + M[CCW, CW]) / 2),
            float((M[CW, CW] + M[CCW, CCW]) / 2),
            float((M[CW, NS] + M[CCW, NS]) / 2), M)


def main():
    d = np.load(NPZ)
    P, idx, angles = d["probs"], d["idx"], [int(a) for a in d["angles"]]
    n = len(idx)
    assert int(d["n_done"]) == n and not np.isnan(P).any(), "inference incomplete"

    clsX = {phi: np.argmax(eq_triple(P, angles, 0, i), 1) for i, phi in enumerate(angles)}
    clsY = {phi: np.argmax(eq_triple(P, angles, 1, i), 1) for i, phi in enumerate(angles)}

    # ---- S2 positive control: at phi in {0,180} the TTA identity is exact ----
    # PRE-REGISTRATION DEVIATION (recorded, see results doc sec.6): the
    # pre-registration phrased the control as "the exact-swap fraction of the
    # hard CLASSES must be 1.000000". The underlying claim is the identity on
    # the equivariant triples, eq_cw(Y_phi) = eq_ccw(X_phi) and
    # eq_ns(Y_phi) = eq_ns(X_phi); the class swap is that identity composed with
    # argmax, which is undefined when eq_cw == eq_ccw exactly. Such perfect ties
    # occur (a saturated galaxy at eq = (0.5, 0.5, 7e-12)) and argmax sends both
    # X and Y to CW, so the class-level swap fraction is 1 - (tie rate) rather
    # than exactly 1. The control is therefore evaluated on the identity itself,
    # at machine precision, and the tie count is reported rather than hidden.
    control = {}
    for phi in CONTROL_ANGLES:
        i = angles.index(phi)
        EX, EY = eq_triple(P, angles, 0, i), eq_triple(P, angles, 1, i)
        resid = float(np.max(np.abs(np.stack([EY[:, 0] - EX[:, 1],
                                              EY[:, 1] - EX[:, 0],
                                              EY[:, 2] - EX[:, 2]]))))
        ties = int((EX[:, 0] == EX[:, 1]).sum())
        swap = np.where(clsX[phi] == CW, CCW, np.where(clsX[phi] == CCW, CW, NS))
        frac = float((clsY[phi] == swap).mean())
        control[str(phi)] = {"max_identity_residual": resid,
                             "exact_cw_ccw_ties": ties,
                             "class_swap_fraction": frac,
                             "class_swap_fraction_excluding_ties":
                                 float((clsY[phi][EX[:, 0] != EX[:, 1]]
                                        == swap[EX[:, 0] != EX[:, 1]]).mean())}
        assert resid == 0.0, f"S2 FAILED at phi={phi}: identity residual {resid}"
        assert control[str(phi)]["class_swap_fraction_excluding_ties"] == 1.0, \
            f"S2 FAILED at phi={phi}: non-tie class swap {frac}"

    informative = [a for a in angles if a not in CONTROL_ANGLES]

    # ---- S1 primary: paired parity-transfer matrix, Y_phi vs X_phi ----
    s1 = {}
    for phi in angles:
        e, r, l, M = eps_rho_L(clsX[phi], clsY[phi])
        s1[str(phi)] = {"eps": e, "rho": r, "L": l, "T": M.tolist(),
                        "n_cw_X": int((clsX[phi] == CW).sum()),
                        "n_ccw_X": int((clsX[phi] == CCW).sum()),
                        "n_ns_X": int((clsX[phi] == NS).sum())}
    eps_bar_all = float(np.mean([s1[str(a)]["eps"] for a in angles]))
    eps_bar_inf = float(np.mean([s1[str(a)]["eps"] for a in informative]))

    # ---- S5 rotation-stability control: X_phi vs X_0 (no parity operation) ----
    s5 = {str(phi): {"R_same_class": float((clsX[phi] == clsX[0]).mean()),
                     "T": confusion(clsX[0], clsX[phi]).tolist()} for phi in angles}

    # ---- POST-HOC (not pre-registered, labelled as such): end-to-end transfer
    # against the ORIENTATION THE CATALOGUE ACTUALLY SAW, X_0, rather than the
    # co-rotated X_phi. This is the operative quantity for the released labels,
    # and it necessarily folds in the rotation instability measured by S5.
    posthoc_obs = {}
    for phi in angles:
        e, r, l, M = eps_rho_L(clsX[0], clsY[phi])
        posthoc_obs[str(phi)] = {"eps_obs": e, "rho_obs": r, "L_obs": l, "T": M.tolist()}
    eps_obs_bar = float(np.mean([posthoc_obs[str(a)]["eps_obs"] for a in angles]))

    # ---- cluster bootstrap over galaxies (pre-registered, 1000 resamples) ----
    flip_cw = {phi: ((clsX[phi] == CW) & (clsY[phi] == CCW)).astype(np.float64) for phi in angles}
    flip_ccw = {phi: ((clsX[phi] == CCW) & (clsY[phi] == CW)).astype(np.float64) for phi in angles}
    is_cw = {phi: (clsX[phi] == CW).astype(np.float64) for phi in angles}
    is_ccw = {phi: (clsX[phi] == CCW).astype(np.float64) for phi in angles}
    obs_flip_cw = {phi: ((clsX[0] == CW) & (clsY[phi] == CCW)).astype(np.float64) for phi in angles}
    obs_flip_ccw = {phi: ((clsX[0] == CCW) & (clsY[phi] == CW)).astype(np.float64) for phi in angles}
    o_cw, o_ccw = (clsX[0] == CW).astype(np.float64), (clsX[0] == CCW).astype(np.float64)

    rng = np.random.default_rng(20260919)
    boot_eps = {phi: np.empty(N_BOOT) for phi in angles}
    boot_bar_all, boot_bar_inf, boot_obs_bar = (np.empty(N_BOOT), np.empty(N_BOOT), np.empty(N_BOOT))
    for b in range(N_BOOT):
        w = np.bincount(rng.integers(0, n, size=n), minlength=n).astype(np.float64)
        vals, ovals = [], []
        for phi in angles:
            e = 0.5 * (w @ flip_cw[phi] / (w @ is_cw[phi]) + w @ flip_ccw[phi] / (w @ is_ccw[phi]))
            boot_eps[phi][b] = e
            vals.append(e)
            ovals.append(0.5 * (w @ obs_flip_cw[phi] / (w @ o_cw)
                                + w @ obs_flip_ccw[phi] / (w @ o_ccw)))
        boot_bar_all[b] = np.mean(vals)
        boot_bar_inf[b] = np.mean([v for a, v in zip(angles, vals) if a not in CONTROL_ANGLES])
        boot_obs_bar[b] = np.mean(ovals)
    for phi in angles:
        s1[str(phi)]["eps_boot_se"] = float(boot_eps[phi].std(ddof=1))
        s1[str(phi)]["z_vs_unity"] = float((s1[str(phi)]["eps"] - 1.0)
                                           / boot_eps[phi].std(ddof=1)) if boot_eps[phi].std(ddof=1) > 0 else 0.0

    se_bar_inf = float(boot_bar_inf.std(ddof=1))
    z_bar_inf = (eps_bar_inf - 1.0) / se_bar_inf

    # ---- S3 injection-recovery slope at each phi (closed form over labels) ----
    s3 = {}
    xs = np.repeat(FRACTIONS, N_SEEDS_S3).astype(float)
    xc = xs - xs.mean()
    den = (xc ** 2).sum()
    rng3 = np.random.default_rng(31415)
    for phi in angles:
        X, Y = clsX[phi], clsY[phi]
        ys = np.empty(len(xs))
        k = 0
        for f in FRACTIONS:
            nf = int(round(f * n))
            for _ in range(N_SEEDS_S3):
                cl = X.copy()
                if nf:
                    S = rng3.choice(n, size=nf, replace=False)
                    cl[S] = Y[S]
                ncw, nccw = int((cl == CW).sum()), int((cl == CCW).sum())
                ys[k] = 2.0 * ncw / (ncw + nccw) - 1.0
                k += 1
        slope = float((xc * (ys - ys.mean())).sum() / den)
        A0 = float(2.0 * (X == CW).sum() / ((X == CW).sum() + (X == CCW).sum()) - 1.0)
        s3[str(phi)] = {"A0_cls_at_phi": A0, "slope_dA_df": slope,
                        "exact_identity_slope_if_eps_1": -2.0 * A0,
                        "slope_over_identity": float(slope / (-2.0 * A0)) if A0 else None}

    # ---- S6 hemisphere split on the strict-subset dipole axis ----
    sample = pd.read_parquet(PILOT / "scale20k_sample.parquet").iloc[idx]
    ra = np.radians(sample["ra"].values)
    dec = np.radians(sample["dec"].values)

    def hemi(axis):
        ar, ad = np.radians(axis[0]), np.radians(axis[1])
        cosang = (np.sin(dec) * np.sin(ad) + np.cos(dec) * np.cos(ad) * np.cos(ra - ar))
        return cosang >= 0

    s6 = {}
    for name, axis in (("strict_887k_axis", AXIS_STRICT), ("full_parent_axis", AXIS_PARENT)):
        m = hemi(axis)
        hs = {}
        for lab, sel in (("north_of_axis", m), ("south_of_axis", ~m)):
            v = [eps_rho_L(clsX[phi][sel], clsY[phi][sel])[0] for phi in informative]
            hs[lab] = {"n": int(sel.sum()), "eps_bar_informative": float(np.mean(v))}
        hs["delta"] = hs["north_of_axis"]["eps_bar_informative"] - hs["south_of_axis"]["eps_bar_informative"]
        s6[name] = {"axis_ra_dec_deg": list(axis), **hs}

    # ---- POST-HOC: effect of the 106 px centre crop on the baseline labels ----
    pairs = pd.read_parquet(PILOT / "scale20k_pairs.parquet").set_index("idx")
    common = [i for i in idx.tolist() if i in pairs.index]
    pr = pairs.loc[common]
    eqc = np.stack([(pr["p_cw_orig"].values + pr["p_ccw_flip"].values) / 2,
                    (pr["p_ccw_orig"].values + pr["p_cw_flip"].values) / 2,
                    (pr["p_ns_orig"].values + pr["p_ns_flip"].values) / 2], 1)
    cls_uncropped = np.argmax(eqc, 1)
    pos = {v: k for k, v in enumerate(idx.tolist())}
    sel = np.array([pos[i] for i in common])
    posthoc_crop = {
        "n_compared": len(common),
        "agreement_cropped106_vs_committed_uncropped150": float((clsX[0][sel] == cls_uncropped).mean()),
        "spiral_fraction_cropped": float(np.mean(clsX[0][sel] != NS)),
        "spiral_fraction_uncropped": float(np.mean(cls_uncropped != NS)),
        "A0_cls_cropped": float(2 * (clsX[0][sel] == CW).sum()
                                / ((clsX[0][sel] == CW).sum() + (clsX[0][sel] == CCW).sum()) - 1),
        "A0_cls_uncropped": float(2 * (cls_uncropped == CW).sum()
                                  / ((cls_uncropped == CW).sum() + (cls_uncropped == CCW).sum()) - 1),
    }

    # ---- S5b (DERIVED from the pre-registered S5; the geometry argument is
    # written out in ROW16IIB_PA_PARITY_TRANSFER_2026-09-19.md sec.4):
    # a galaxy's true handedness h does not depend on the orientation at which
    # it is presented, so any disagreement between L(0) and L(theta) proves a
    # label error. The survey presents each galaxy at its own position angle,
    # uniformly distributed, so the per-orientation error rate e = P(L != h) is
    # the same at every theta; then
    #     2 e >= P(L(0) != L(theta)) = d(theta)
    # and the dilution of ANY true population asymmetry, D = 1 - 2e, obeys
    #     D <= 1 - d(theta)   for every theta,  hence D <= 1 - max_theta d(theta).
    # d is measured on galaxies labelled spiral at BOTH orientations, so the
    # NOT_SPIRAL channel cannot inflate it. theta in {90,180,270} are exact
    # pixel permutations (PIL transposes): those d values carry no interpolation
    # artefact at all, and the bound is quoted from them.
    EXACT_ROT = [90, 180, 270]
    s5b = {}
    for phi in angles:
        if phi == 0:
            continue
        both = ((clsX[0] != NS) & (clsX[phi] != NS))
        dis = both & (clsX[0] != clsX[phi])
        d = float(dis.sum() / both.sum())
        s5b[str(phi)] = {"n_both_spiral": int(both.sum()), "d_disagreement": d,
                         "D_upper_bound": 1.0 - d,
                         "rotation_is_exact_pixel_permutation": phi in EXACT_ROT}
    d_exact = [s5b[str(p_)]["d_disagreement"] for p_ in EXACT_ROT]
    d_all = [v["d_disagreement"] for v in s5b.values()]
    boot_D = np.empty(N_BOOT)
    for b in range(N_BOOT):
        rs = rng.integers(0, n, size=n)
        vals = []
        for p_ in EXACT_ROT:
            both = (clsX[0][rs] != NS) & (clsX[p_][rs] != NS)
            vals.append((both & (clsX[0][rs] != clsX[p_][rs])).sum() / both.sum())
        boot_D[b] = 1.0 - max(vals)
    s5b_summary = {
        "max_d_over_exact_rotations": float(max(d_exact)),
        "D_upper_bound_from_exact_rotations": float(1.0 - max(d_exact)),
        "D_upper_bound_boot_se": float(boot_D.std(ddof=1)),
        "max_d_over_all_angles": float(max(d_all)),
        "D_upper_bound_from_all_angles": float(1.0 - max(d_all)),
    }

    # ---- POST-HOC (declared after the 200-galaxy smoke run showed eps ~ 0.6,
    # but BEFORE any full-sample statistic was computed; labelled post-hoc, not
    # pre-registered): does the deficit apply to the subset the released
    # catalogue actually uses? The P4' strict 887,472-row selection is
    # primary_hc = is_spiral AND max(eq_cw, eq_ccw) > 0.6
    # (pipelines/p2_chirality/build_apjs_release_v1_0_244.py:163-168), evaluated
    # on the UNCROPPED committed probabilities, i.e. exactly the catalogue's own
    # cut on exactly these galaxies.
    conf_unc = np.max(eqc[:, :2], axis=1)
    hc_mask_common = (cls_uncropped != NS) & (conf_unc > 0.6)
    hc_sel = sel[hc_mask_common]
    posthoc_hc = {
        "selection": "primary_hc: is_spiral AND max(eq_cw,eq_ccw) > 0.6 on the committed uncropped probabilities",
        "n": int(hc_mask_common.sum()),
        "eps_by_angle": {str(phi): eps_rho_L(clsX[phi][hc_sel], clsY[phi][hc_sel])[0] for phi in angles},
    }
    posthoc_hc["eps_bar_informative"] = float(np.mean(
        [posthoc_hc["eps_by_angle"][str(a)] for a in informative]))
    boot_hc = np.empty(N_BOOT)
    m_hc = len(hc_sel)
    for b in range(N_BOOT):
        rs = hc_sel[rng.integers(0, m_hc, size=m_hc)]
        boot_hc[b] = float(np.mean([eps_rho_L(clsX[phi][rs], clsY[phi][rs])[0] for phi in informative]))
    posthoc_hc["eps_bar_informative_boot_se"] = float(boot_hc.std(ddof=1))
    # the S5b dilution bound restricted to the catalogue's own strict selection
    hc_d = {}
    for phi in [90, 180, 270]:
        both = (clsX[0][hc_sel] != NS) & (clsX[phi][hc_sel] != NS)
        hc_d[str(phi)] = {"n_both_spiral": int(both.sum()),
                          "d_disagreement": float(((both) & (clsX[0][hc_sel] != clsX[phi][hc_sel])).sum() / both.sum())}
    boot_hcD = np.empty(N_BOOT)
    for b in range(N_BOOT):
        rs = hc_sel[rng.integers(0, m_hc, size=m_hc)]
        vv = []
        for phi in [90, 180, 270]:
            both = (clsX[0][rs] != NS) & (clsX[phi][rs] != NS)
            vv.append((both & (clsX[0][rs] != clsX[phi][rs])).sum() / both.sum())
        boot_hcD[b] = 1.0 - max(vv)
    posthoc_hc["S5b_d_exact_rotations"] = hc_d
    posthoc_hc["S5b_D_upper_bound"] = float(1.0 - max(v["d_disagreement"] for v in hc_d.values()))
    posthoc_hc["S5b_D_upper_bound_boot_se"] = float(boot_hcD.std(ddof=1))

    # confidence deciles of the same uncropped max(eq_cw, eq_ccw), spirals only
    spi = cls_uncropped != NS
    q = np.quantile(conf_unc[spi], np.linspace(0, 1, 11))
    deciles = []
    for k in range(10):
        m = spi & (conf_unc >= q[k]) & (conf_unc <= q[k + 1] if k == 9 else conf_unc < q[k + 1])
        ss = sel[m]
        if len(ss) < 50:
            continue
        deciles.append({"decile": k + 1, "conf_lo": float(q[k]), "conf_hi": float(q[k + 1]),
                        "n": int(len(ss)),
                        "eps_bar_informative": float(np.mean(
                            [eps_rho_L(clsX[phi][ss], clsY[phi][ss])[0] for phi in informative]))})

    deficit = z_bar_inf < -3.0
    res = {
        "preregistration": "PREREGISTRATION_2026-09-19.md (commit 12248d70)",
        "n_galaxies": int(n), "angles_deg": angles,
        "model": "bamfai/galaxy-chirality-v2 chirality_model_v2_best.pt rev 237d021c451d75cf86a875e86d4de498b74e2f12",
        "pipeline": "production equivariant Z2 flip-TTA (equivariant_postprocess.py), 106 px centre crop, bicubic rotation",
        "S2_positive_control_exact_swap_fraction": control,
        "S1_paired_parity_transfer": s1,
        "S1_eps_bar_all_angles": eps_bar_all,
        "S1_eps_bar_informative": eps_bar_inf,
        "S1_eps_bar_informative_boot_se": se_bar_inf,
        "S1_z_vs_unity": float(z_bar_inf),
        "S3_injection_slope_by_angle": s3,
        "S5_rotation_stability": s5,
        "S5b_label_self_disagreement_under_rotation": s5b,
        "S5b_dilution_bound": s5b_summary,
        "S6_hemisphere_split": s6,
        "POSTHOC_observed_orientation_transfer": posthoc_obs,
        "POSTHOC_eps_obs_bar_all_angles": eps_obs_bar,
        "POSTHOC_eps_obs_bar_boot_se": float(boot_obs_bar.std(ddof=1)),
        "POSTHOC_crop_effect_on_baseline": posthoc_crop,
        "POSTHOC_primary_hc_subset": posthoc_hc,
        "POSTHOC_eps_by_confidence_decile": deciles,
        "n_bootstrap": N_BOOT,
        "threshold": "deficit declared iff eps_bar_informative < 1 by > 3 sigma (pre-registered sec.7.2)",
        "verdict": ("PA-DEPENDENT PARITY-TRANSFER DEFICIT DETECTED" if deficit
                    else "NULL: no deficit at the measured precision"),
    }
    OUT.write_text(json.dumps(res, indent=2))
    print(json.dumps({k: v for k, v in res.items()
                      if k not in ("S1_paired_parity_transfer", "S5_rotation_stability",
                                   "S3_injection_slope_by_angle",
                                   "POSTHOC_observed_orientation_transfer")}, indent=2))
    print("\n-- S1 eps(phi) --")
    for phi in angles:
        e = s1[str(phi)]
        print(f"  phi={phi:3d}  eps={e['eps']:.4f}+-{e['eps_boot_se']:.4f}  "
              f"rho={e['rho']:.4f}  L={e['L']:.4f}  R_rot={s5[str(phi)]['R_same_class']:.4f}  "
              f"eps_obs={posthoc_obs[str(phi)]['eps_obs']:.4f}")
    print("\n-- S5b dilution bound --")
    for phi in angles:
        if phi == 0:
            continue
        v = s5b[str(phi)]
        print(f"  theta={phi:3d} {'exact' if v['rotation_is_exact_pixel_permutation'] else 'bicub'}"
              f"  d={v['d_disagreement']:.4f}  D<= {v['D_upper_bound']:.4f}  n={v['n_both_spiral']}")
    print(f"  => D <= {s5b_summary['D_upper_bound_from_exact_rotations']:.4f}"
          f" +- {s5b_summary['D_upper_bound_boot_se']:.4f} (exact rotations only)")
    print("\n-- POST-HOC primary_hc subset (the catalogue's own cut) --")
    print(f"  n={posthoc_hc['n']}  eps_bar_inf={posthoc_hc['eps_bar_informative']:.4f}"
          f"+-{posthoc_hc['eps_bar_informative_boot_se']:.4f}"
          f"  D<= {posthoc_hc['S5b_D_upper_bound']:.4f}+-{posthoc_hc['S5b_D_upper_bound_boot_se']:.4f}")
    print("-- POST-HOC eps_bar_inf by confidence decile --")
    for dd in deciles:
        print(f"  d{dd['decile']:2d} conf[{dd['conf_lo']:.3f},{dd['conf_hi']:.3f}) "
              f"n={dd['n']:6d}  eps={dd['eps_bar_informative']:.4f}")


if __name__ == "__main__":
    main()

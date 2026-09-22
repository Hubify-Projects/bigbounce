#!/usr/bin/env python3
"""Row 16(ii-b) — POST-HOC (not pre-registered): parity-transfer efficiency
measured on the EXACT released preprocessing.

Why this exists. The pre-registered S1 grid (s1_pa_transfer_analysis.py) uses a
106 px centre crop so that all eight angles, including the bicubic 45 deg ones,
draw only from inside the original frame. Addendum A1 showed that crop is not
benign for the classifier (only 68.3% of galaxies keep their committed class
under it), so the headline eps must also be available on the preprocessing the
released pipeline actually applies: Resize((224,224)) of the full 150 px cutout,
with rotations restricted to the lossless 90/180/270 transposes.

The statistic and the estimator are IDENTICAL in form to the pre-registered S1
and to the s1 script's POSTHOC_observed_orientation_transfer; only the input
probabilities change (nocrop_probs.npz instead of pa_transfer_probs.npz). This
block was computed AFTER unblinding and is reported as post-hoc throughout. The
pre-registered threshold test of section 7.2 is decided on S1, not on this file;
the numbers here are quoted beside S1, never instead of it, and the only figure
propagated to P4' is the addendum-A1 dilution bound in s5b_nocrop_dilution.json.

Input : nocrop_probs.npz   Output: posthoc_nocrop_eps.json
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
PILOT = HERE.parent / "injection_pilot"
NPZ = HERE / "nocrop_probs.npz"
OUT = HERE / "posthoc_nocrop_eps.json"
CW, CCW, NS = 0, 1, 2
N_BOOT = 1000


def eq_triple(P, angles, kind, ai):
    nai = angles.index((-angles[ai]) % 360)
    a, b = P[:, kind, ai, :], P[:, 1 - kind, nai, :]
    return np.stack([(a[:, 0] + b[:, 1]) / 2,
                     (a[:, 1] + b[:, 0]) / 2,
                     (a[:, 2] + b[:, 2]) / 2], axis=1)


def confusion(src, dst):
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

    clsX = {t: np.argmax(eq_triple(P, angles, 0, i), 1) for i, t in enumerate(angles)}
    clsY = {t: np.argmax(eq_triple(P, angles, 1, i), 1) for i, t in enumerate(angles)}

    # same positive control as S2: the TTA identity is exact at theta = 0, 180
    control = {}
    for t in (0, 180):
        i = angles.index(t)
        EX, EY = eq_triple(P, angles, 0, i), eq_triple(P, angles, 1, i)
        resid = float(np.max(np.abs(np.stack([EY[:, 0] - EX[:, 1],
                                              EY[:, 1] - EX[:, 0],
                                              EY[:, 2] - EX[:, 2]]))))
        nt = EX[:, 0] != EX[:, 1]
        swap = np.where(clsX[t] == CW, CCW, np.where(clsX[t] == CCW, CW, NS))
        control[str(t)] = {"max_identity_residual": resid,
                           "exact_cw_ccw_ties": int((~nt).sum()),
                           "class_swap_fraction_excluding_ties": float((clsY[t][nt] == swap[nt]).mean())}
        assert resid == 0.0 and control[str(t)]["class_swap_fraction_excluding_ties"] == 1.0

    # catalogue's own strict cut, from the committed uncropped probabilities
    pairs = pd.read_parquet(PILOT / "scale20k_pairs.parquet").set_index("idx")
    common = [i for i in idx.tolist() if i in pairs.index]
    pr = pairs.loc[common]
    eqc = np.stack([(pr["p_cw_orig"].values + pr["p_ccw_flip"].values) / 2,
                    (pr["p_ccw_orig"].values + pr["p_cw_flip"].values) / 2,
                    (pr["p_ns_orig"].values + pr["p_ns_flip"].values) / 2], 1)
    cls_committed = np.argmax(eqc, 1)
    pos = {v: k for k, v in enumerate(idx.tolist())}
    sel = np.array([pos[i] for i in common])
    hc = (cls_committed != NS) & (np.max(eqc[:, :2], axis=1) > 0.6)
    subsets = {"all_galaxies": np.arange(n), "primary_hc_subset": sel[hc]}

    # co-rotated eps(theta): informative only where the mirror does not commute
    # with the rotation, i.e. theta in {90, 270}
    INF_CO = [t for t in angles if t not in (0, 180)]
    # observed-orientation eps_obs(theta): class(Y_theta) vs class(X_0), the
    # pairing the released catalogue actually realises. theta = 0 is the trivial
    # control; 90/180/270 all carry information.
    INF_OBS = [t for t in angles if t != 0]

    rng = np.random.default_rng(20260919)
    boots = {k: {"co": np.empty(N_BOOT), "obs": np.empty(N_BOOT)} for k in subsets}
    for b in range(N_BOOT):
        for k, ii in subsets.items():
            r = ii[rng.integers(0, len(ii), size=len(ii))]
            boots[k]["co"][b] = np.mean([eps_rho_L(clsX[t][r], clsY[t][r])[0] for t in INF_CO])
            boots[k]["obs"][b] = np.mean([eps_rho_L(clsX[0][r], clsY[t][r])[0] for t in INF_OBS])

    out = {
        "status": "POST-HOC — computed after unblinding; NOT part of the "
                  "pre-registered section-7.2 threshold test, which is decided on S1",
        "preregistration": "PREREGISTRATION_2026-09-19.md (commit 12248d70) + addendum A1",
        "preprocessing": "EXACT released preprocessing: Resize((224,224)) on the full 150 px "
                         "cutout, no crop; rotations are lossless PIL transposes (90/180/270)",
        "model": "bamfai/galaxy-chirality-v2 chirality_model_v2_best.pt rev 237d021c451d75cf86a875e86d4de498b74e2f12",
        "n_galaxies": int(n),
        "angles_deg": angles,
        "positive_control": control,
        "informative_angles_corotated": INF_CO,
        "informative_angles_observed": INF_OBS,
        "n_bootstrap": N_BOOT,
    }
    for k, ii in subsets.items():
        per = {}
        for t in angles:
            e, r, l, M = eps_rho_L(clsX[t][ii], clsY[t][ii])
            eo, ro, lo, Mo = eps_rho_L(clsX[0][ii], clsY[t][ii])
            per[str(t)] = {"eps_corotated": e, "rho_corotated": r, "L_corotated": l,
                           "eps_observed": eo, "rho_observed": ro, "L_observed": lo,
                           "R_rotation_stability": float((clsX[t][ii] == clsX[0][ii]).mean()),
                           "T_corotated": M.tolist(), "T_observed": Mo.tolist()}
        bc, bo = boots[k]["co"].std(ddof=1), boots[k]["obs"].std(ddof=1)
        ebc = float(np.mean([per[str(t)]["eps_corotated"] for t in INF_CO]))
        ebo = float(np.mean([per[str(t)]["eps_observed"] for t in INF_OBS]))
        out[k] = {"n": int(len(ii)), "per_theta": per,
                  "eps_bar_corotated_informative": ebc,
                  "eps_bar_corotated_boot_se": float(bc),
                  "eps_bar_corotated_z_vs_unity": float((ebc - 1.0) / bc),
                  "eps_bar_observed_informative": ebo,
                  "eps_bar_observed_boot_se": float(bo),
                  "eps_bar_observed_z_vs_unity": float((ebo - 1.0) / bo)}

    OUT.write_text(json.dumps(out, indent=2))
    for k in subsets:
        v = out[k]
        print(f"{k} (n={v['n']})")
        for t in angles:
            p = v["per_theta"][str(t)]
            print(f"  theta={t:3d}  eps_co={p['eps_corotated']:.4f}  "
                  f"eps_obs={p['eps_observed']:.4f}  R_rot={p['R_rotation_stability']:.4f}")
        print(f"  eps_bar_co  = {v['eps_bar_corotated_informative']:.4f} "
              f"+- {v['eps_bar_corotated_boot_se']:.4f}  (z={v['eps_bar_corotated_z_vs_unity']:+.1f})")
        print(f"  eps_bar_obs = {v['eps_bar_observed_informative']:.4f} "
              f"+- {v['eps_bar_observed_boot_se']:.4f}  (z={v['eps_bar_observed_z_vs_unity']:+.1f})")


if __name__ == "__main__":
    main()

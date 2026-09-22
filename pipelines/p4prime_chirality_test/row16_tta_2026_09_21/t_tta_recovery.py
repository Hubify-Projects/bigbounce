#!/usr/bin/env python3
"""Step T — how much of the row-16(ii-b) epsilon deficit is recoverable by
rotation equivariance, measured as a test-time average over the EXISTING
committed checkpoint.

Pre-registration: PREREGISTRATION_2026-09-21.md "Step T" (git 712e9e7e),
committed BEFORE any statistic here was computed. Statistics T0-C, T2a-T2e and
the T3 decision rule are as declared; anything else is labelled POST-HOC.

Input : ../row16_pa_parity_transfer/pa_transfer_probs.npz  (stage 1, 45 deg grid)
        stage3_offset_probs.npz                            (stage 3, 22.5 offsets)
        ../injection_pilot/scale20k_pairs.parquet           (committed catalogue probs)
Output: t_tta_recovery.json
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROW16 = HERE.parent / "row16_pa_parity_transfer"
PILOT = HERE.parent / "injection_pilot"
OUT = HERE / "t_tta_recovery.json"

CW, CCW, NS = 0, 1, 2
N_BOOT = 1000
SEED = 20260921
IDENTITY_TOL = 1e-6      # float32 summation-order residual; 0 in exact arithmetic
GROUPS = {"Z2_released": [0.0],
          "D4": [0.0, 90.0, 180.0, 270.0],
          "D8": [0.0, 45.0, 90.0, 135.0, 180.0, 225.0, 270.0, 315.0]}


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
            float((M[CW, NS] + M[CCW, NS]) / 2))


def main():
    s1 = np.load(ROW16 / "pa_transfer_probs.npz")
    s3 = np.load(HERE / "stage3_offset_probs.npz")
    assert s1["idx"].tolist() == s3["idx"].tolist(), "stage 1/3 galaxy lists differ"
    done = s3["done_mask"]
    sel = np.flatnonzero(done)
    n = sel.size
    a1 = [float(a) for a in s1["angles"]]
    a3 = [float(a) for a in s3["angles"]]
    angles = sorted(a1 + a3)
    P = np.concatenate([s1["probs"][sel], s3["probs"][sel]], axis=2)
    order = [(a1 + a3).index(a) for a in angles]
    P = P[:, :, order, :]
    assert not np.isnan(P).any(), "NaN in the combined 16-angle grid"

    def eq(kind, ai):
        nai = angles.index((-angles[ai]) % 360.0)
        a, b = P[:, kind, ai, :], P[:, 1 - kind, nai, :]
        return np.stack([(a[:, 0] + b[:, 1]) / 2,
                         (a[:, 1] + b[:, 0]) / 2,
                         (a[:, 2] + b[:, 2]) / 2], axis=1)

    EQX = {phi: eq(0, i) for i, phi in enumerate(angles)}
    EQY = {phi: eq(1, i) for i, phi in enumerate(angles)}

    def tta(EQ, psis):
        """G-TTA: average the released equivariant triple over the rotation
        subgroup. Computed independently for each phi (no coset short-cut), so
        the T0 invariance control is a real numerical check."""
        return {phi: np.mean([EQ[(phi + p) % 360.0] for p in psis], axis=0)
                for phi in angles}

    Q = {g: (tta(EQX, psis), tta(EQY, psis)) for g, psis in GROUPS.items()}
    CLS = {g: ({phi: np.argmax(qx[phi], 1) for phi in angles},
               {phi: np.argmax(qy[phi], 1) for phi in angles})
           for g, (qx, qy) in Q.items()}

    # ---- T0-C: the three declared identities, asserted numerically ----
    controls = {}
    for g, psis in GROUPS.items():
        qx, qy = Q[g]
        nrot = len(psis)
        inv = max(float(np.abs(qx[(0.0 + p) % 360.0] - qx[0.0]).max()) for p in psis)
        par_angles = [phi for phi in angles if (2 * phi) % 360.0 in psis]
        par, swapfrac, ties = 0.0, [], 0
        for phi in par_angles:
            par = max(par, float(np.abs(qy[phi][:, 0] - qx[phi][:, 1]).max()),
                      float(np.abs(qy[phi][:, 2] - qx[phi][:, 2]).max()))
            nt = qx[phi][:, 0] != qx[phi][:, 1]
            ties += int((~nt).sum())
            sx = CLS[g][0][phi]
            sw = np.where(sx == CW, CCW, np.where(sx == CCW, CW, NS))
            swapfrac.append(float((CLS[g][1][phi][nt] == sw[nt]).mean()))
        controls[g] = {"n_rotations": nrot,
                       "max_C_n_invariance_residual": inv,
                       "parity_exact_angles": par_angles,
                       "max_parity_identity_residual": par,
                       "min_class_swap_fraction_excluding_ties": min(swapfrac),
                       "exact_cw_ccw_ties_over_those_angles": ties}
        assert inv < IDENTITY_TOL, f"{g}: C_n invariance control failed ({inv})"
        assert par < IDENTITY_TOL, f"{g}: parity identity control failed ({par})"
        assert min(swapfrac) == 1.0, f"{g}: class-swap control failed"

    # ---- catalogue subsets ----
    pairs = pd.read_parquet(PILOT / "scale20k_pairs.parquet").set_index("idx")
    idx_sel = s1["idx"][sel].tolist()
    common = [i for i in idx_sel if i in pairs.index]
    pr = pairs.loc[common]
    eqc = np.stack([(pr["p_cw_orig"].values + pr["p_ccw_flip"].values) / 2,
                    (pr["p_ccw_orig"].values + pr["p_cw_flip"].values) / 2,
                    (pr["p_ns_orig"].values + pr["p_ns_flip"].values) / 2], 1)
    cls_committed = np.argmax(eqc, 1)
    pos = {v: k for k, v in enumerate(idx_sel)}
    rows_common = np.array([pos[i] for i in common])
    hc = (cls_committed != NS) & (np.max(eqc[:, :2], axis=1) > 0.6)
    hc_rows = rows_common[hc]

    def d_of(g, ii, phi):
        cx = CLS[g][0]
        both = (cx[0.0][ii] != NS) & (cx[phi][ii] != NS)
        nb = int(both.sum())
        return (float((both & (cx[0.0][ii] != cx[phi][ii])).sum() / nb) if nb else float("nan")), nb

    def informative_d(g):
        psis = GROUPS[g]
        return [phi for phi in angles if phi != 0.0 and phi % 360.0 not in psis]

    def informative_eps(g):
        psis = GROUPS[g]
        return [phi for phi in angles if (2 * phi) % 360.0 not in psis]

    def block(ii, tag):
        res = {}
        for g in GROUPS:
            per_phi, dd = {}, {}
            for phi in angles:
                if phi != 0.0:
                    dv, nb = d_of(g, ii, phi)
                    dd[f"{phi:g}"] = {"d": dv, "n_both_spiral": nb}
                e, r, l = eps_rho_L(CLS[g][0][phi][ii], CLS[g][1][phi][ii])
                per_phi[f"{phi:g}"] = {"eps": e, "rho": r, "L": l}
            di = informative_d(g)
            ei = informative_eps(g)
            dmax = max(dd[f"{phi:g}"]["d"] for phi in di)
            res[g] = {
                "rotation_subgroup_deg": GROUPS[g],
                "informative_angles_for_d": [f"{p:g}" for p in di],
                "informative_angles_for_eps": [f"{p:g}" for p in ei],
                "d_by_angle": dd,
                "max_d_informative": dmax,
                "D_upper_bound": 1.0 - dmax,
                "eps_rho_L_by_angle": per_phi,
                "eps_bar_informative": (float(np.mean([per_phi[f"{p:g}"]["eps"] for p in ei]))
                                        if ei else None),
            }
        return {"n": int(len(ii)), "subset": tag, "by_group": res}

    allg = np.arange(n)
    out_all = block(allg, "all galaxies (stage-3 completed subset)")
    out_hc = block(hc_rows, "catalogue primary_hc cut (committed uncropped probabilities)")

    # ---- bootstrap on D_G and on the recovery fraction F_G ----
    rng = np.random.default_rng(SEED)
    keys = list(GROUPS)
    boot = {tag: {g: np.empty(N_BOOT) for g in keys} for tag in ("all", "hc")}
    bootF = {tag: {g: np.empty(N_BOOT) for g in keys} for tag in ("all", "hc")}
    m_hc = len(hc_rows)
    for b in range(N_BOOT):
        ra = rng.integers(0, n, size=n)
        rh = hc_rows[rng.integers(0, m_hc, size=m_hc)]
        for tag, ii in (("all", ra), ("hc", rh)):
            base = None
            for g in keys:
                dmax = max(d_of(g, ii, phi)[0] for phi in informative_d(g))
                D = 1.0 - dmax
                boot[tag][g][b] = D
                if g == "Z2_released":
                    base = D
                bootF[tag][g][b] = (D - base) / (1.0 - base)
    for tag, blk in (("all", out_all), ("hc", out_hc)):
        base = blk["by_group"]["Z2_released"]["D_upper_bound"]
        for g in keys:
            D = blk["by_group"][g]["D_upper_bound"]
            blk["by_group"][g]["D_upper_bound_boot_se"] = float(boot[tag][g].std(ddof=1))
            blk["by_group"][g]["recovery_fraction_F"] = (D - base) / (1.0 - base)
            blk["by_group"][g]["recovery_fraction_F_boot_se"] = float(bootF[tag][g].std(ddof=1))
            blk["by_group"][g]["residual_1_minus_D"] = 1.0 - D

    # ---- T2e: catalogue churn at theta = 0 ----
    churn = {g: float((CLS[g][0][0.0][rows_common] != cls_committed).mean()) for g in keys}
    # POST-HOC (not pre-registered): churn against the SAME cropped grid's released
    # pipeline, which isolates the TTA's own effect from the 106 px crop's effect
    # (row 16(ii-b) sec.6: the crop alone moves ~32% of classes).
    churn_vs_cropped = {g: float((CLS[g][0][0.0] != CLS["Z2_released"][0][0.0]).mean())
                        for g in keys}

    # ---- T3: decision rule, evaluated exactly as pre-registered ----
    F = out_all["by_group"]["D4"]["recovery_fraction_F"]
    resid = out_all["by_group"]["D4"]["residual_1_minus_D"]
    if F >= 0.5 and resid >= 0.10:
        verdict = "GPU GO"
    elif F >= 0.5:
        verdict = "NO-GPU, ADOPT-TTA"
    else:
        verdict = "NO-GPU, WRONG-LEVER"

    out = {
        "preregistration": "PREREGISTRATION_2026-09-21.md Step T (git 712e9e7e, committed "
                           "before this script ran)",
        "grid": "stage 1 (45 deg) + stage 3 (22.5 deg offsets) = uniform 16-angle 22.5 deg "
                "grid, 106 px centre crop, identical preprocessing and checkpoint pin",
        "model": "bamfai/galaxy-chirality-v2 chirality_model_v2_best.pt rev "
                 "237d021c451d75cf86a875e86d4de498b74e2f12",
        "n_galaxies_stage3_complete": int(n),
        "n_galaxies_stage1": int(len(s1["idx"])),
        "stage3_completion": float(n / len(s1["idx"])),
        "T0_controls": controls,
        "T2_all_galaxies": out_all,
        "T2_primary_hc": out_hc,
        "T2e_catalogue_churn_at_theta0": churn,
        "POSTHOC_churn_vs_same_grid_released_pipeline": {
            "_label": "POST-HOC, not pre-registered: isolates the TTA's effect from the 106 px crop's effect, which dominates T2e",
            **churn_vs_cropped},
        "T3_decision": {
            "rule": "GPU GO iff F_D4 >= 0.5 AND residual (1 - D_D4) >= 0.10; "
                    "NO-GPU/ADOPT-TTA iff F_D4 >= 0.5 and residual < 0.10; "
                    "NO-GPU/WRONG-LEVER iff F_D4 < 0.5 (pre-registered Step T sec.T3)",
            "F_D4": F, "residual_1_minus_D_D4": resid,
            "D_D4": out_all["by_group"]["D4"]["D_upper_bound"],
            "D_D8": out_all["by_group"]["D8"]["D_upper_bound"],
            "D_Z2_released": out_all["by_group"]["Z2_released"]["D_upper_bound"],
            "VERDICT": verdict,
        },
        "scope_limitation": "A TTA over non-equivariant weights and a D4-equivariant "
                            "architecture agree exactly on the annihilation of d on the C4 "
                            "orbit (a theorem, control T0-C) and differ only in the learned "
                            "features that set the OFF-GROUP residual. This measurement bounds "
                            "the equivariance-attributable part of the deficit and says nothing "
                            "about the feature-quality part.",
        "n_bootstrap": N_BOOT, "seed": SEED,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ("T2_all_galaxies", "T2_primary_hc")}, indent=2))
    for tag in ("T2_all_galaxies", "T2_primary_hc"):
        b = out[tag]
        print(f"\n{tag}  n={b['n']}")
        for g, r in b["by_group"].items():
            print(f"  {g:12s} D<={r['D_upper_bound']:.4f}+-{r['D_upper_bound_boot_se']:.4f}"
                  f"  max_d={r['max_d_informative']:.4f}"
                  f"  F={r['recovery_fraction_F']:+.4f}+-{r['recovery_fraction_F_boot_se']:.4f}"
                  f"  eps_bar={r['eps_bar_informative']}")


if __name__ == "__main__":
    main()

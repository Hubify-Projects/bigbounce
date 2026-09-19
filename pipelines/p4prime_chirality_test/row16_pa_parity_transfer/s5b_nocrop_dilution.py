#!/usr/bin/env python3
"""Row 16(ii-b) addendum-A1 analysis — the label-self-disagreement dilution
bound measured on the EXACT released preprocessing (no crop, lossless
rotations).

Pre-registration: PREREGISTRATION_2026-09-19.md addendum A1 (commit 06cf6fbb).

Argument (results doc sec.4): true handedness does not depend on the
orientation at which a galaxy is presented, so L(0) != L(theta) proves a label
error. With the survey presenting each galaxy at a uniformly distributed
position angle, the per-orientation error rate e = P(L != h) is the same at
every theta, so d(theta) <= 2e and the dilution of any true population
asymmetry, D = 1 - 2e, obeys D <= 1 - d(theta).

theta = 180 needs no PA-uniformity argument at all: position angle is defined
mod 180, so a cutout rotated by 180 degrees depicts the same galaxy at the same
position angle and the two error rates are equal by construction.

Input : nocrop_probs.npz   Output: s5b_nocrop_dilution.json
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
PILOT = HERE.parent / "injection_pilot"
NPZ = HERE / "nocrop_probs.npz"
OUT = HERE / "s5b_nocrop_dilution.json"
CW, CCW, NS = 0, 1, 2
N_BOOT = 1000
G_GZ1 = 0.397616   # P4's illustrative GZ1 bridge, chirality_catalog_paper.tex:1533


def eq_triple(P, angles, kind, ai):
    nai = angles.index((-angles[ai]) % 360)
    a, b = P[:, kind, ai, :], P[:, 1 - kind, nai, :]
    return np.stack([(a[:, 0] + b[:, 1]) / 2,
                     (a[:, 1] + b[:, 0]) / 2,
                     (a[:, 2] + b[:, 2]) / 2], axis=1)


def main():
    d = np.load(NPZ)
    P, idx, angles = d["probs"], d["idx"], [int(a) for a in d["angles"]]
    n = len(idx)
    assert int(d["n_done"]) == n and not np.isnan(P).any(), "inference incomplete"

    EQ = {phi: eq_triple(P, angles, 0, i) for i, phi in enumerate(angles)}
    EQY = {phi: eq_triple(P, angles, 1, i) for i, phi in enumerate(angles)}
    cls = {phi: np.argmax(EQ[phi], 1) for phi in angles}
    clsY = {phi: np.argmax(EQY[phi], 1) for phi in angles}

    # positive control: the TTA identity is exact at theta = 0 and 180
    control = {}
    for phi in (0, 180):
        resid = float(np.max(np.abs(np.stack([EQY[phi][:, 0] - EQ[phi][:, 1],
                                              EQY[phi][:, 1] - EQ[phi][:, 0],
                                              EQY[phi][:, 2] - EQ[phi][:, 2]]))))
        ties = int((EQ[phi][:, 0] == EQ[phi][:, 1]).sum())
        nt = EQ[phi][:, 0] != EQ[phi][:, 1]
        swap = np.where(cls[phi] == CW, CCW, np.where(cls[phi] == CCW, CW, NS))
        control[str(phi)] = {"max_identity_residual": resid, "exact_cw_ccw_ties": ties,
                             "class_swap_fraction_excluding_ties": float((clsY[phi][nt] == swap[nt]).mean())}
        assert resid == 0.0, f"control failed at {phi}: residual {resid}"
        assert control[str(phi)]["class_swap_fraction_excluding_ties"] == 1.0

    # catalogue's own strict selection, from the committed UNCROPPED probabilities
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
    hc_sel = sel[hc]

    # sanity: theta = 0 here IS the committed preprocessing, so the classes must
    # agree with the committed catalogue values exactly on the common galaxies
    agree0 = float((cls[0][sel] == cls_committed).mean())

    def dvals(ii, thetas):
        out = {}
        for th in thetas:
            both = (cls[0][ii] != NS) & (cls[th][ii] != NS)
            out[str(th)] = {"n_both_spiral": int(both.sum()),
                            "d_disagreement": float((both & (cls[0][ii] != cls[th][ii])).sum() / both.sum())}
        return out

    thetas = [90, 180, 270]
    allg = np.arange(n)
    res_all, res_hc = dvals(allg, thetas), dvals(hc_sel, thetas)

    rng = np.random.default_rng(20260919)
    boot = {"all": np.empty(N_BOOT), "hc": np.empty(N_BOOT),
            "all_180": np.empty(N_BOOT), "hc_180": np.empty(N_BOOT)}
    m_hc = len(hc_sel)
    for b in range(N_BOOT):
        ra = rng.integers(0, n, size=n)
        rh = hc_sel[rng.integers(0, m_hc, size=m_hc)]
        da, dh = dvals(ra, thetas), dvals(rh, thetas)
        va = [da[str(t)]["d_disagreement"] for t in thetas]
        vh = [dh[str(t)]["d_disagreement"] for t in thetas]
        boot["all"][b] = 1.0 - max(va)
        boot["hc"][b] = 1.0 - max(vh)
        boot["all_180"][b] = 1.0 - va[thetas.index(180)]
        boot["hc_180"][b] = 1.0 - vh[thetas.index(180)]

    def pack(res, key):
        dmax = max(v["d_disagreement"] for v in res.values())
        return {
            "per_theta": res,
            "max_d": float(dmax),
            "D_upper_bound": float(1.0 - dmax),
            "D_upper_bound_boot_se": float(boot[key].std(ddof=1)),
            "D_upper_bound_theta180_only": float(1.0 - res["180"]["d_disagreement"]),
            "D_upper_bound_theta180_boot_se": float(boot[key + "_180"].std(ddof=1)),
            "z_vs_D_equals_1": float((1.0 - dmax - 1.0) / boot[key].std(ddof=1)),
        }

    out = {
        "preregistration": "PREREGISTRATION_2026-09-19.md addendum A1 (commit 06cf6fbb)",
        "preprocessing": "EXACT released preprocessing: Resize((224,224)) on the full 150 px cutout, "
                         "no crop; rotations are lossless PIL transposes (90/180/270)",
        "model": "bamfai/galaxy-chirality-v2 chirality_model_v2_best.pt rev 237d021c451d75cf86a875e86d4de498b74e2f12",
        "n_galaxies": int(n),
        "positive_control": control,
        "theta0_class_agreement_with_committed_catalogue": agree0,
        "n_common_with_committed_pairs": len(common),
        "all_galaxies": pack(res_all, "all"),
        "primary_hc_subset": {"n": int(hc.sum()),
                              "selection": "is_spiral AND max(eq_cw,eq_ccw) > 0.6 on the committed uncropped probabilities",
                              **pack(res_hc, "hc")},
        "g_gz1_illustrative_bridge": G_GZ1,
        "n_bootstrap": N_BOOT,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

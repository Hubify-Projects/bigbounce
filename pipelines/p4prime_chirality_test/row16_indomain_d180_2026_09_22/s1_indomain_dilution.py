#!/usr/bin/env python3
"""Analysis stage — the in-domain d(theta) and the dilution bound D.

Pre-registration: PREREGISTRATION_2026-09-22.md (commit f45c9d1b), committed
BEFORE any statistic here was computed. Statistic, selections, controls, the
in-domain threshold and the decision rule are all fixed there.

`eq_triple` is IMPORTED from ../row16_pa_parity_transfer/s5b_nocrop_dilution.py,
not re-implemented, so the in-domain and out-of-domain numbers are produced by
the same estimator.

Input : indomain_probs.npz, stream_manifest.json, c1_e2e_catalogue_agreement.json
        ../../p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet
Output: s1_indomain_dilution.json
"""
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "row16_pa_parity_transfer"))
from s5b_nocrop_dilution import eq_triple  # noqa: E402  (same estimator, imported)

NPZ = HERE / "indomain_probs.npz"
OUT = HERE / "s1_indomain_dilution.json"
CATALOG = HERE.parents[1] / "p2_chirality" / "apjs_release_v1.0.244" / "p4_catalog_primary_safe_v1.0.244.parquet"
CW, CCW, NS = 0, 1, 2
N_BOOT = 1000
SEED = 20260922
THETAS = [90, 180, 270]
A95_OBS_STRICT = 0.98            # per cent, P4' strict-887,472 observed-label floor
G_GZ1 = 0.397616                 # P4's illustrative GZ1 bridge
HELD = {"primary_hc": {"D_max": 0.7166, "se": 0.0047, "D_180": 0.7887, "se_180": 0.0047,
                       "n": 7982, "A95_phys": 1.37},
        "catalogue_spiral": {"D_max": 0.6296, "se": 0.0040, "D_180": 0.6928, "se_180": 0.0038,
                             "n": 19800, "A95_phys": 1.56}}


def main():
    t0 = time.time()
    d = np.load(NPZ, allow_pickle=True)
    P, ids, angles = d["probs"], np.array(d["dr8_id"]), [int(a) for a in d["angles"]]
    n = len(ids)
    assert P.shape == (n, 2, 4, 3) and not np.isnan(P).any(), "inference incomplete"
    man = json.loads((HERE / "stream_manifest.json").read_text())

    EQ = {phi: eq_triple(P, angles, 0, i) for i, phi in enumerate(angles)}
    EQY = {phi: eq_triple(P, angles, 1, i) for i, phi in enumerate(angles)}
    cls = {phi: np.argmax(EQ[phi], 1) for phi in angles}
    clsY = {phi: np.argmax(EQY[phi], 1) for phi in angles}

    # ---- control C3: the flip-TTA parity identity is exact at theta = 0 and 180 ----
    c3 = {}
    for phi in (0, 180):
        resid = float(np.max(np.abs(np.stack([EQY[phi][:, 0] - EQ[phi][:, 1],
                                              EQY[phi][:, 1] - EQ[phi][:, 0],
                                              EQY[phi][:, 2] - EQ[phi][:, 2]]))))
        nt = EQ[phi][:, 0] != EQ[phi][:, 1]
        swap = np.where(cls[phi] == CW, CCW, np.where(cls[phi] == CCW, CW, NS))
        c3[str(phi)] = {"max_identity_residual": resid,
                        "exact_cw_ccw_ties": int((~nt).sum()),
                        "class_swap_fraction_excluding_ties": float((clsY[phi][nt] == swap[nt]).mean())}
        assert resid == 0.0, f"C3 failed at {phi}: residual {resid}"
        assert c3[str(phi)]["class_swap_fraction_excluding_ties"] == 1.0

    # ---- released catalogue join ----
    rel = pq.read_table(CATALOG, columns=["object_id", "ra_deg", "dec_deg", "class_eq",
                                          "score_cw_eq", "score_ccw_eq", "score_ns_eq",
                                          "score_eq_max", "primary_hc", "raw_flip_qc_unsafe"]
                        ).to_pandas().set_index("object_id")
    r = rel.reindex(ids)
    matched = r["class_eq"].notna().values
    assert matched.all(), f"{int((~matched).sum())} drawn dr8_id absent from the released catalogue"
    rel_cls = np.argmax(r[["score_cw_eq", "score_ccw_eq", "score_ns_eq"]].values, 1)

    # ---- control C2: this lane's theta=0 label vs the released catalogue label ----
    dcw = np.abs(EQ[0][:, 0] - r["score_cw_eq"].values)
    c2 = {
        "n": int(n),
        "class_agreement_all": float((cls[0] == rel_cls).mean()),
        "class_agreement_catalogue_spirals": float((cls[0] == rel_cls)[rel_cls != NS].mean()),
        "class_agreement_primary_hc": float((cls[0] == rel_cls)[r["primary_hc"].values.astype(bool)].mean()),
        "max_abs_eq_cw_difference": float(dcw.max()),
        "median_abs_eq_cw_difference": float(np.median(dcw)),
        "threshold_for_in_domain": 0.99,
        "out_of_domain_reference_agreement": 0.439,
    }
    c1 = json.loads((HERE / "c1_e2e_catalogue_agreement.json").read_text())

    in_domain = c2["class_agreement_all"] >= 0.99
    verdict_gate = ("IN-DOMAIN" if in_domain
                    else "AMBIGUOUS" if c2["class_agreement_all"] >= 0.90
                    else "CONTROL FAILED - larger finding than the bound")

    # ---- selections ----
    hc = r["primary_hc"].values.astype(bool)
    unsafe = r["raw_flip_qc_unsafe"].values.astype(bool)
    SEL = {"all_drawn": np.arange(n),
           "catalogue_spiral": np.where(rel_cls != NS)[0],
           "primary_hc": np.where(hc)[0],
           "primary_hc_safe": np.where(hc & ~unsafe)[0]}

    def dvals(ii):
        out = {}
        for th in THETAS:
            both = (cls[0][ii] != NS) & (cls[th][ii] != NS)
            nb = int(both.sum())
            out[str(th)] = {"n_both_spiral": nb,
                            "d_disagreement": float((both & (cls[0][ii] != cls[th][ii])).sum() / nb)
                            if nb else float("nan")}
        return out

    rng = np.random.default_rng(SEED)
    results = {}
    for tag, ii in SEL.items():
        res = dvals(ii)
        dmax = max(v["d_disagreement"] for v in res.values())
        d180 = res["180"]["d_disagreement"]
        b_max = np.empty(N_BOOT); b_180 = np.empty(N_BOOT)
        m = len(ii)
        for b in range(N_BOOT):
            rr = ii[rng.integers(0, m, size=m)]
            db = dvals(rr)
            b_max[b] = 1.0 - max(v["d_disagreement"] for v in db.values())
            b_180[b] = 1.0 - db["180"]["d_disagreement"]
        se, se180 = float(b_max.std(ddof=1)), float(b_180.std(ddof=1))
        entry = {
            "n_selected": int(m),
            "per_theta": res,
            "max_d": float(dmax),
            "D_upper_bound": float(1.0 - dmax),
            "D_upper_bound_boot_se": se,
            "D_upper_bound_theta180_only": float(1.0 - d180),
            "D_upper_bound_theta180_boot_se": se180,
            "z_vs_D_equals_1": float((1.0 - dmax - 1.0) / se) if se > 0 else float("inf"),
            "A95_phys_percent_from_max": A95_OBS_STRICT / (1.0 - dmax),
            "A95_phys_percent_from_theta180": A95_OBS_STRICT / (1.0 - d180),
            "g_gz1_below_bound": bool(G_GZ1 <= 1.0 - dmax),
        }
        if tag in HELD:
            h = HELD[tag]
            comb = float(np.hypot(se, h["se"]))
            entry["held_out_of_domain"] = h
            entry["delta_vs_held_D_max"] = float(entry["D_upper_bound"] - h["D_max"])
            entry["delta_in_combined_se"] = float(abs(entry["D_upper_bound"] - h["D_max"]) / comb)
            entry["agrees_with_held_within_2_combined_se"] = bool(entry["delta_in_combined_se"] <= 2.0)
        results[tag] = entry
        print(f"[{time.time()-t0:.0f}s] {tag}: n={m} D<={entry['D_upper_bound']:.4f}"
              f"+-{se:.4f} (d180 row {entry['D_upper_bound_theta180_only']:.4f})", flush=True)

    # ---- sample description (is the draw a fair slice of the parent?) ----
    par_hc = rel["primary_hc"].values.astype(bool)
    sample_desc = {
        "n_galaxies": int(n),
        "row_groups": man["row_groups_completed"],
        "row_groups_planned": man["plan"]["row_groups_planned"],
        "shards": man["plan"]["shards"],
        "ra_range": [float(r["ra_deg"].min()), float(r["ra_deg"].max())],
        "dec_range": [float(r["dec_deg"].min()), float(r["dec_deg"].max())],
        "fraction_dec_negative": float((r["dec_deg"].values < 0).mean()),
        "fraction_dec_negative_parent": float((rel["dec_deg"].values < 0).mean()),
        "fraction_catalogue_spiral": float((rel_cls != NS).mean()),
        "fraction_catalogue_spiral_parent": float((rel["class_eq"].values != "NOT_SPIRAL").mean()),
        "fraction_primary_hc": float(hc.mean()),
        "fraction_primary_hc_parent": float(par_hc.mean()),
        "note": "the sample is a uniform random draw of row groups from a fully sky-shuffled "
                "dataset; it is NOT the same galaxies as the row-16(ii-b) N=19,800 sample and is "
                "never described as a measurement on the 8,474,531-row parent",
    }

    out = {
        "preregistration": "PREREGISTRATION_2026-09-22.md (commit f45c9d1b)",
        "images": man["dataset"],
        "model": man["model"],
        "preprocessing": man["preprocessing"],
        "estimator": "eq_triple imported verbatim from ../row16_pa_parity_transfer/s5b_nocrop_dilution.py",
        "statistic": "d(theta) = P(L(0) != L(theta) | both spiral); D <= 1 - max_theta d(theta), "
                     "theta in {90,180,270}; A95_phys = A95_obs / D with A95_obs = 0.98%",
        "sample": sample_desc,
        "control_C1_catalogue_scale": {
            "n_compared": c1["n_compared"],
            "class_agreement_all": c1["class_agreement_all"],
            "class_agreement_catalogue_spirals": c1["class_agreement_catalogue_spirals"],
            "class_agreement_primary_hc": c1["class_agreement_primary_hc"],
            "source": "p2_chirality/outputs/canonical_provenance/e2e_fullrun (192 shards, 2026-07-11)",
        },
        "control_C2_this_lane": c2,
        "control_C3_tta_identity": c3,
        "in_domain_gate": verdict_gate,
        "results": results,
        "n_bootstrap": N_BOOT,
        "seed": SEED,
        "wall_clock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(json.dumps({k: v for k, v in out.items() if k != "results"}, indent=2))


if __name__ == "__main__":
    main()

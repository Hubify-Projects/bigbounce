#!/usr/bin/env python3
"""Step P — d(180) beyond the 19,800-galaxy sample, and the explicitly-labelled
confidence-stratified catalogue-wide ESTIMATE.

Pre-registration: PREREGISTRATION_2026-09-21.md "Step P" (git 712e9e7e),
committed BEFORE any statistic here was computed. Sec. P0 declares in advance
that a literal d(180) on the 8,474,531-row parent is infeasible in this lane
(no parent cutouts are cached and new downloads are excluded), so the largest
feasible subset is the union of the three committed caches. Nothing below is
described as a measurement on 8.47M galaxies.

Input : ../row16_pa_parity_transfer/nocrop_probs.npz   (19,800, exact released preproc)
        stage4_scale5k_probs.npz, stage4_pilot500_probs.npz   (5,000 + 500, same preproc)
        ../injection_pilot/{scale20k,scale,pilot}_sample.parquet
        ../../p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet
Output: p_d180_catalogue_wide.json
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

HERE = Path(__file__).resolve().parent
ROW16 = HERE.parent / "row16_pa_parity_transfer"
PILOT = HERE.parent / "injection_pilot"
CATALOG = HERE.parents[1] / "p2_chirality" / "apjs_release_v1.0.244" / "p4_catalog_primary_safe_v1.0.244.parquet"
OUT = HERE / "p_d180_catalogue_wide.json"

CW, CCW, NS = 0, 1, 2
N_BOOT = 1000
SEED = 20260921
N_DECILES = 10
MIN_CELL = 50            # pre-registered minimum for the 2-D sensitivity check
AXIS_STRICT = (195.5, -57.2)
DRAWS = [("scale20k", ROW16 / "nocrop_probs.npz", PILOT / "scale20k_sample.parquet",
          "seed 44, NSIDE=64 sky-uniform (the row 16(ii-b) sample)"),
         ("scale5k", HERE / "stage4_scale5k_probs.npz", PILOT / "scale_sample.parquet",
          "seed 43, NSIDE=32 sky-uniform"),
         ("pilot500", HERE / "stage4_pilot500_probs.npz", PILOT / "pilot_sample.parquet",
          "seed 42, NSIDE=32 sky-uniform pilot")]


def eq_triple(P, angles, kind, ai):
    nai = angles.index((-angles[ai]) % 360)
    a, b = P[:, kind, ai, :], P[:, 1 - kind, nai, :]
    return np.stack([(a[:, 0] + b[:, 1]) / 2,
                     (a[:, 1] + b[:, 0]) / 2,
                     (a[:, 2] + b[:, 2]) / 2], axis=1)


def d180(c0, c180, ii):
    both = (c0[ii] != NS) & (c180[ii] != NS)
    nb = int(both.sum())
    return (float((both & (c0[ii] != c180[ii])).sum() / nb) if nb else float("nan")), nb


def unit(ra_deg, dec_deg):
    ra, dec = np.radians(ra_deg), np.radians(dec_deg)
    return np.array([np.cos(dec) * np.cos(ra), np.cos(dec) * np.sin(ra), np.sin(dec)])


def main():
    rng = np.random.default_rng(SEED)

    # ---- parent catalogue (local; no download) ----
    t = pq.read_table(CATALOG, columns=["ra_deg", "dec_deg", "class_eq", "score_eq_max",
                                        "primary_hc", "raw_flip_qc_unsafe"])
    n_parent_rows = t.num_rows
    spiral = pc.is_in(t["class_eq"], value_set=pa.array(["CW", "CCW"]))
    ts = t.filter(spiral)
    par = pd.DataFrame({
        "ra": np.round(ts["ra_deg"].combine_chunks().to_numpy(zero_copy_only=False), 7),
        "dec": np.round(ts["dec_deg"].combine_chunks().to_numpy(zero_copy_only=False), 7),
        "score_eq_max": ts["score_eq_max"].combine_chunks().to_numpy(zero_copy_only=False),
        "primary_hc": ts["primary_hc"].combine_chunks().to_numpy(zero_copy_only=False),
        "unsafe": ts["raw_flip_qc_unsafe"].combine_chunks().to_numpy(zero_copy_only=False),
        "class_eq": np.asarray(ts["class_eq"].combine_chunks().to_pylist(), dtype=object),
    })
    n_parent_spiral = len(par)
    # pre-registered strata: deciles of score_eq_max over the parent spiral set
    edges = np.quantile(par["score_eq_max"].values, np.linspace(0, 1, N_DECILES + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    par["stratum"] = np.digitize(par["score_eq_max"].values, edges[1:-1])
    w_all = np.bincount(par["stratum"].values, minlength=N_DECILES) / n_parent_spiral
    hcm = par["primary_hc"].values & ~par["unsafe"].values
    n_parent_strict = int(hcm.sum())
    w_strict = (np.bincount(par["stratum"].values[hcm], minlength=N_DECILES) / n_parent_strict)
    lookup = par.set_index(["ra", "dec"])[["score_eq_max", "primary_hc", "unsafe",
                                           "stratum", "class_eq"]]

    rows, controls, per_draw = [], {}, {}
    for tag, npz_path, sample_path, prov in DRAWS:
        d = np.load(npz_path)
        P, idx, angles = d["probs"], d["idx"], [int(a) for a in d["angles"]]
        n = len(idx)
        assert int(d["n_done"]) == n and not np.isnan(P).any(), f"{tag}: inference incomplete"
        i0, i180 = angles.index(0), angles.index(180)
        EQ0, EQ180 = eq_triple(P, angles, 0, i0), eq_triple(P, angles, 0, i180)
        EY0, EY180 = eq_triple(P, angles, 1, i0), eq_triple(P, angles, 1, i180)
        c0, c180 = np.argmax(EQ0, 1), np.argmax(EQ180, 1)

        # positive control (hard assert): the flip-TTA identity is exact at 0 and 180
        ctl = {}
        for lab, EX, EY, cx, cy in (("0", EQ0, EY0, c0, np.argmax(EY0, 1)),
                                    ("180", EQ180, EY180, c180, np.argmax(EY180, 1))):
            resid = float(np.max(np.abs(np.stack([EY[:, 0] - EX[:, 1], EY[:, 1] - EX[:, 0],
                                                  EY[:, 2] - EX[:, 2]]))))
            nt = EX[:, 0] != EX[:, 1]
            sw = np.where(cx == CW, CCW, np.where(cx == CCW, CW, NS))
            ctl[lab] = {"max_identity_residual": resid,
                        "exact_cw_ccw_ties": int((~nt).sum()),
                        "class_swap_fraction_excluding_ties": float((cy[nt] == sw[nt]).mean())}
            assert resid == 0.0, f"{tag}: control failed at theta={lab}"
            assert ctl[lab]["class_swap_fraction_excluding_ties"] == 1.0

        sample = pd.read_parquet(sample_path)
        key = pd.DataFrame({"ra": np.round(sample["ra"].values[idx], 7),
                            "dec": np.round(sample["dec"].values[idx], 7)})
        j = key.join(lookup, on=["ra", "dec"], how="left")
        matched = j["stratum"].notna().values
        # released-catalogue agreement at theta = 0 (this chain IS the released pipeline)
        cat_cls = np.where(j["class_eq"].values == "CW", CW,
                           np.where(j["class_eq"].values == "CCW", CCW, NS))
        agree0 = float((c0[matched] == cat_cls[matched]).mean())
        cls_ns = float((c0 == NS).mean())
        sp = c0 != NS
        controls[tag] = {
            **ctl, "parent_match_rate": float(matched.mean()),
            "theta0_class_agreement_with_released_catalogue": agree0,
            "fraction_we_label_NOT_SPIRAL": cls_ns,
            "cw_ccw_agreement_among_our_spirals": float(
                (c0[sp & matched] == cat_cls[sp & matched]).mean()),
            "P2c_PREREGISTERED_CONTROL": "PASS" if agree0 >= 0.999 else "FAIL",
        }
        # The pre-registered control P2c required >= 99.9% agreement with the
        # RELEASED catalogue at theta = 0. It FAILS, and the failure is recorded
        # rather than asserted away: the released catalogue's inference ran on
        # images from the HF dataset Smith42/galaxies (run_eq_fast.py:37), not on
        # the jpeg-cutout `image_url` the row 13/16 fetch scripts used. Per the
        # pre-registration the CATALOGUE-WIDE claim of step P is VOID; the
        # measured d(180) values remain valid statements about the released
        # CHECKPOINT on these cutouts (they never used catalogue labels), and are
        # reported as such. See posthoc_provenance_diagnostic.json.

        rows.append(pd.DataFrame({
            "draw": tag, "ra": key["ra"].values, "dec": key["dec"].values,
            "c0": c0, "c180": c180, "matched": matched,
            "stratum": j["stratum"].values, "primary_hc": j["primary_hc"].values,
            "unsafe": j["unsafe"].values}))
        per_draw[tag] = {"provenance": prov, "n": int(n)}

    U = pd.concat(rows, ignore_index=True)
    U["dup"] = U.duplicated(subset=["ra", "dec"], keep="first")
    n_dup = int(U["dup"].sum())

    def pack(df, label):
        c0, c180 = df["c0"].values, df["c180"].values
        ii = np.arange(len(df))
        dv, nb = d180(c0, c180, ii)
        bs = np.empty(N_BOOT)
        for b in range(N_BOOT):
            bs[b] = d180(c0, c180, rng.integers(0, len(df), size=len(df)))[0]
        return {"subset": label, "n": int(len(df)), "n_both_spiral": nb,
                "d_180": dv, "d_180_boot_se": float(bs.std(ddof=1)),
                "D_upper_bound": 1.0 - dv, "D_upper_bound_boot_se": float(bs.std(ddof=1))}

    measured = {}
    for tag, _, _, _ in DRAWS:
        sub = U[U["draw"] == tag]
        measured[tag] = {**per_draw[tag], "all": pack(sub, f"{tag} all"),
                         "primary_hc": pack(sub[sub["primary_hc"].fillna(False).astype(bool)],
                                            f"{tag} primary_hc")}
    uni = U[~U["dup"]]
    uni_hc = uni[uni["primary_hc"].fillna(False).astype(bool) & ~uni["unsafe"].fillna(True).astype(bool)]
    measured["UNION"] = {"provenance": "de-duplicated union of the three committed caches "
                                       "(duplicates matched on (ra,dec) to 1e-7 deg)",
                         "n_duplicates_removed": n_dup,
                         "all": pack(uni, "union all"),
                         "strict_primary": pack(uni_hc, "union primary_hc AND NOT unsafe")}

    # ---- P3: EXPLICIT extrapolation -- stratified re-weighted catalogue-wide ESTIMATE ----
    um = uni[uni["matched"].values].copy()
    strat = um["stratum"].values.astype(int)

    def reweight(w, mask=None):
        sub = um if mask is None else um[mask]
        s = strat if mask is None else strat[mask]
        ds, ns = np.full(N_DECILES, np.nan), np.zeros(N_DECILES, dtype=int)
        for k in range(N_DECILES):
            m = s == k
            ns[k] = int(m.sum())
            if ns[k]:
                ds[k] = d180(sub["c0"].values, sub["c180"].values, np.flatnonzero(m))[0]
        ok = ~np.isnan(ds)
        est = float(np.sum(w[ok] * ds[ok]) / np.sum(w[ok]))
        return est, ds, ns, float(np.sum(w[ok]))

    est_all, d_s, n_s, cov_all = reweight(w_all)
    hcmask = (um["primary_hc"].fillna(False).astype(bool)
              & ~um["unsafe"].fillna(True).astype(bool)).values
    est_hc, d_s_hc, n_s_hc, cov_hc = reweight(w_strict, hcmask)

    bse = np.empty(N_BOOT)
    bse_hc = np.empty(N_BOOT)
    c0u, c180u = um["c0"].values, um["c180"].values
    for b in range(N_BOOT):
        r = rng.integers(0, len(um), size=len(um))
        ds = np.full(N_DECILES, np.nan)
        for k in range(N_DECILES):
            m = np.flatnonzero(strat[r] == k)
            if m.size:
                ds[k] = d180(c0u[r], c180u[r], m)[0]
        ok = ~np.isnan(ds)
        bse[b] = np.sum(w_all[ok] * ds[ok]) / np.sum(w_all[ok])
        rh = np.flatnonzero(hcmask)[rng.integers(0, int(hcmask.sum()), size=int(hcmask.sum()))]
        ds = np.full(N_DECILES, np.nan)
        for k in range(N_DECILES):
            m = np.flatnonzero(strat[rh] == k)
            if m.size:
                ds[k] = d180(c0u[rh], c180u[rh], m)[0]
        ok = ~np.isnan(ds)
        bse_hc[b] = np.sum(w_strict[ok] * ds[ok]) / np.sum(w_strict[ok])

    # pre-registered sensitivity check: decile x hemisphere of the strict axis
    nhat = unit(*AXIS_STRICT)
    g = unit(um["ra"].values, um["dec"].values).T @ nhat
    north = g >= 0
    cells_ok, cell_counts = True, {}
    for k in range(N_DECILES):
        for lab, msk in (("N", north), ("S", ~north)):
            c = int(((strat == k) & msk).sum())
            cell_counts[f"{k}{lab}"] = c
            if c < MIN_CELL:
                cells_ok = False
    sens = {"evaluable": bool(cells_ok), "min_cell_required": MIN_CELL,
            "cell_counts": cell_counts}
    if cells_ok:
        wn = np.zeros((N_DECILES, 2))
        pg = unit(par["ra"].values, par["dec"].values).T @ nhat
        pn = pg >= 0
        for k in range(N_DECILES):
            wn[k, 0] = ((par["stratum"].values == k) & pn).sum()
            wn[k, 1] = ((par["stratum"].values == k) & ~pn).sum()
        wn /= wn.sum()
        num = den = 0.0
        for k in range(N_DECILES):
            for j, msk in enumerate((north, ~north)):
                m = np.flatnonzero((strat == k) & msk)
                if m.size:
                    num += wn[k, j] * d180(c0u, c180u, m)[0]
                    den += wn[k, j]
        sens["d_180_estimate_2d"] = float(num / den)

    out = {
        "preregistration": "PREREGISTRATION_2026-09-21.md Step P (git 712e9e7e, committed "
                           "before this script ran)",
        "P0_feasibility_declared_in_advance": (
            "A literal d(180) on the 8,474,531-row parent needs one forward pass per galaxy "
            "per orientation ON THE IMAGE. The repository caches cutouts for 25,300 galaxies "
            "only; fetching 8.47M is excluded by this lane's no-large-download and ~10 GB disk "
            "constraint. The full parent was therefore declared infeasible BEFORE the run and "
            "the largest feasible subset is the de-duplicated union of the three committed "
            "caches. No number below is a measurement on 8.47M galaxies."),
        "preprocessing": "EXACT released preprocessing (Resize((224,224)) of the full 150 px "
                         "cutout, no crop); theta = 180 is a lossless PIL transpose, so no "
                         "interpolation enters anywhere",
        "n_parent_rows": n_parent_rows, "n_parent_spiral": n_parent_spiral,
        "n_parent_strict_primary": n_parent_strict,
        "positive_controls": controls,
        "P2c_CONTROL_OUTCOME": {
            "status": "FAILED",
            "requirement": "theta=0 classes agree with the RELEASED catalogue on >= 99.9% "
                           "of matched galaxies (pre-registered Step P sec.P2c)",
            "measured": "43.9% on scale20k (99.99% against the row-16 lane's OWN committed "
                        "forward passes, which validates this implementation)",
            "consequence_per_preregistration": "the CATALOGUE-WIDE claim of step P is VOID. "
                                               "The measured d(180) numbers below are valid "
                                               "statements about the released CHECKPOINT on "
                                               "the cached Legacy DR9 jpeg-cutouts (the same "
                                               "images row 16(ii-b) used, and its bound never "
                                               "used catalogue labels either); the P3 "
                                               "re-weighting is retained ONLY as the "
                                               "confidence-re-weighted value of that same "
                                               "checkpoint statistic, NOT as a statement about "
                                               "the released catalogue's own labels.",
            "diagnosis": "posthoc_provenance_diagnostic.json -- the catalogue's inference ran "
                         "on HF dataset Smith42/galaxies images (run_eq_fast.py:37); the "
                         "`image_url` jpeg-cutout column was appended afterwards for display "
                         "(run_eq_fast.py:265-270). Neither the field of view (flat zoom sweep) "
                         "nor the ls-dr8/ls-dr9 layer (0.453 vs 0.460 agreement) explains it.",
        },
        "MEASURED": measured,
        "P3_REWEIGHTED_ESTIMATE": {
            "_label": "VOID as a catalogue-wide claim (control P2c FAILED); retained as the confidence-re-weighted value of the checkpoint statistic. EXTRAPOLATION, NOT A MEASUREMENT. Stratified re-weighting of the "
                      "measured union onto the parent's score_eq_max decile distribution.",
            "assumption": "within a score_eq_max stratum, d(180) is independent of the "
                          "quantities the sky-uniform sampling distorts (principally local "
                          "sky density). Declared in advance (Step P sec.P3).",
            "strata": "deciles of score_eq_max over the parent spiral set",
            "decile_edges": [float(e) for e in edges[1:-1]],
            "n_measured_matched": int(len(um)),
            "parent_all_spirals": {
                "d_180_estimate": est_all, "d_180_estimate_boot_se": float(bse.std(ddof=1)),
                "D_upper_bound_estimate": 1.0 - est_all,
                "parent_weight_covered": cov_all,
                "d_by_decile": [None if np.isnan(v) else float(v) for v in d_s],
                "n_measured_by_decile": n_s.tolist(),
                "parent_weight_by_decile": w_all.tolist()},
            "parent_strict_primary": {
                "d_180_estimate": est_hc, "d_180_estimate_boot_se": float(bse_hc.std(ddof=1)),
                "D_upper_bound_estimate": 1.0 - est_hc,
                "parent_weight_covered": cov_hc,
                "d_by_decile": [None if np.isnan(v) else float(v) for v in d_s_hc],
                "n_measured_by_decile": n_s_hc.tolist(),
                "parent_weight_by_decile": w_strict.tolist()},
            "sensitivity_2d_decile_x_hemisphere": sens,
        },
        "n_bootstrap": N_BOOT, "seed": SEED,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2)[:4000])
    for k, v in measured.items():
        for sub in ("all", "primary_hc", "strict_primary"):
            if sub in v:
                r = v[sub]
                print(f"{k:10s} {sub:15s} n={r['n']:6d} d(180)={r['d_180']:.4f}"
                      f"+-{r['d_180_boot_se']:.4f}  D<={r['D_upper_bound']:.4f}")


if __name__ == "__main__":
    main()

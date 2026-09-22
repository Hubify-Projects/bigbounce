"""LS12 / DA3M-R12-06 -- the pointwise perturbativity diagnostic on the PBH
headline grid.

Pre-registration: PREREGISTRATION.md (committed alone at b289aa0f, before any
number below existed). Read it first; every definition, threshold, gate and
decision branch used here is fixed there.

WHAT THIS DOES
  For each of the 255 points of the committed extended compaction scan
  (`row11_pbh_residuals/results/row11_gammacr_extension.json`), re-run the
  compaction script's OWN variance integral (Choudhury et al. 2025 Eq. 53, as
  implemented in `pbh_compaction_fnl.covariances` / the row-11 wide-k twin) at
  that point's own spectrum shape and at the amplitude that point's own
  solution requires, and evaluate

      epsilon = 1.2 |f_NL| sigma_r        (the paper's Sec. V B criterion)

  at BOTH legs of the headline ratio (f_NL = -35/16 and -35/8).

WHAT THIS DOES NOT DO
  It does not re-solve any A(f_PBH), does not change any committed number, and
  never estimates sigma_r from an adjacent point.

Venue: local CPU, seconds, $0.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import simpson

HERE = Path(__file__).resolve().parent
A3 = HERE.parent
sys.path.insert(0, str(A3))
import pbh_compaction_fnl as PC  # noqa: E402

ROW11 = A3 / "row11_pbh_residuals/results/row11_gammacr_extension.json"
COMMITTED = A3 / "outputs/pbh_compaction_fnl.json"
OUT = HERE / "results.json"

F16, F8 = -35.0 / 16.0, -35.0 / 8.0
PERT_COEFF = 1.2                       # Sec. V B / r9_perturbativity.py
EPS_GATE = 1.0                         # pre-registered threshold
INLAB = (0.267, 0.630)                 # the headline window
HEADLINE = {"n": 144, "mean": 1.8374128034538420,
            "std": 0.03117312621980982,
            "min": 1.7594059994225366, "max": 1.8914930409818205}

_ORIG_COV, _ORIG_SPEC, _ORIG_DL = PC.covariances, PC.delta2_zeta, PC.DL


# --------------------------------------------------------------- integrands
def cov_wide(A, rp, kp=1.0, nk=12000, dl=None):
    """Eqs. 52-54 on the wide k-grid -- byte-identical to
    row11_gammacr_extension._cov_wide (the integrator the 255 points used)."""
    k = np.logspace(np.log10(kp) - 9.0, np.log10(kp) + 3.0, nk)
    lnk = np.log(k)
    d2 = PC.delta2_zeta(k, A, kp, dl) * PC.transfer(k, rp) ** 2
    wg, ws = PC.W_gauss(k, rp), PC.W_sph(k, rp)
    s_c2 = 4.0 * (PC.F_W / 3.0) ** 2 * simpson((k * rp) ** 4 * wg ** 2 * d2, x=lnk)
    s_r2 = simpson(ws ** 2 * d2, x=lnk)
    s_cr2 = 2.0 * (PC.F_W / 3.0) * simpson((k * rp) ** 2 * wg * ws * d2, x=lnk)
    sc, sr = np.sqrt(s_c2), np.sqrt(s_r2)
    return sc, sr, s_cr2, float(np.clip(s_cr2 / (sc * sr), -0.999999, 0.999999))


def powerlaw(ns, ir_cut):
    """row11_gammacr_extension._powerlaw, verbatim."""
    def d2(k, A, kp=1.0, dl=None):
        kk = np.asarray(k, dtype=float) / kp
        out = A * kk ** (ns - 1.0)
        return np.where(kk < ir_cut, 0.0, out) if ir_cut > 0 else out
    return d2


def _set_shape(p):
    """Install the point's own spectrum family into the module globals."""
    if p["family"] == "lognormal":
        PC.delta2_zeta, PC.DL = _ORIG_SPEC, p["Delta"]
    else:
        PC.delta2_zeta = powerlaw(p["n_s"], p["k_min_over_k_p"])
    return p["rp_kp"]


def _restore():
    PC.covariances, PC.delta2_zeta, PC.DL = _ORIG_COV, _ORIG_SPEC, _ORIG_DL


def rel(a, b):
    return abs(a - b) / abs(b) if b else abs(a - b)


# ------------------------------------------------------------------- gates
def gate_G1():
    """cov_wide reproduces the committed narrow integrator on the lognormal
    family (<1e-6). Re-run here, not quoted from row 11's log."""
    worst = 0.0
    for dl, rpk in [(0.35, 1.5), (0.5, 1.0), (0.8, 0.75), (0.35, 0.75)]:
        PC.DL = dl
        a, b = _ORIG_COV(0.1, rpk, 1.0), cov_wide(0.1, rpk, 1.0)
        worst = max(worst, max(rel(x, y) for x, y in
                               zip(a[:2] + (a[3],), b[:2] + (b[3],))))
    PC.DL = _ORIG_DL
    return {"name": "G1 wide vs committed integrator, lognormal family",
            "max_rel_diff": worst, "tol": 1e-6, "pass": bool(worst < 1e-6)}


def gate_G2(points):
    """Recomputed gamma_cr reproduces every stored gamma_cr (<1e-10)."""
    worst, argworst = 0.0, None
    for p in points:
        rpk = _set_shape(p)
        g = cov_wide(0.1, rpk, 1.0)[3]
        d = rel(g, p["gamma_cr"])
        if d > worst:
            worst, argworst = d, p
    _restore()
    return {"name": "G2 gamma_cr reproduced for all 255 stored points",
            "n": len(points), "max_rel_diff": worst, "tol": 1e-10,
            "pass": bool(worst < 1e-10),
            "worst_point": {k: argworst[k] for k in
                            ("family", "rp_kp", "C_th", "gamma_cr")} if argworst else None}


def gate_G3(committed):
    """sigma_r and 1.2|f_NL|sigma_r at (Delta,rp_kp)=(0.5,1.0), A=A_*,
    reproduce the three committed calibration rows (<1e-10). These three rows
    are where the paper's printed 0.54-1.01 / 1.09-2.02 actually come from."""
    rows, worst = [], 0.0
    PC.DL, PC.delta2_zeta = 0.5, _ORIG_SPEC
    for key, r in committed["calibrated_amplitude_comparison"].items():
        _, sr, _, g = _ORIG_COV(r["A_star_gaussian_fPBH1"], 1.0, 1.0)
        d_sr, d_g = rel(sr, r["sigma_r"]), rel(g, r["gamma_cr"])
        eps = {n: PERT_COEFF * abs(v["f_NL"]) * sr for n, v in r["per_fNL"].items()}
        d_eps = max(rel(eps[n], v["perturbativity_1.2_absfNL_sigma_r"])
                    for n, v in r["per_fNL"].items() if v["f_NL"] != 0.0)
        worst = max(worst, d_sr, d_g, d_eps)
        rows.append({"row": key, "sigma_r_recomputed": sr,
                     "sigma_r_committed": r["sigma_r"],
                     "gamma_cr": g,
                     "eps_-35/16": eps["matter_bounce_Li_-35/16"],
                     "eps_-35/8": eps["matter_bounce_Cai_-35/8"],
                     "max_rel_diff": max(d_sr, d_g, d_eps)})
    PC.DL = _ORIG_DL
    return {"name": "G3 committed calibration sigma_r + printed epsilon range",
            "rows": rows, "max_rel_diff": worst, "tol": 1e-10,
            "pass": bool(worst < 1e-10)}


def gate_G4(committed):
    """Narrow integrator reproduces all 27 stored robust-grid gamma_cr."""
    worst = 0.0
    PC.delta2_zeta = _ORIG_SPEC
    for key, r in committed["robust_amplitude_requirement_grid"].items():
        parts = dict(kv.split("=") for kv in key.split(","))
        PC.DL = float(parts["Delta"])
        g = _ORIG_COV(0.1, float(parts["rp_kp"]), 1.0)[3]
        worst = max(worst, rel(g, r["gamma_cr"]))
    PC.DL = _ORIG_DL
    return {"name": "G4 committed 27-point grid gamma_cr, narrow integrator",
            "n": len(committed["robust_amplitude_requirement_grid"]),
            "max_rel_diff": worst, "tol": 1e-10, "pass": bool(worst < 1e-10)}


def gate_G5(head):
    """The headline population reproduces from the JSON: n=144, 1.8374+-0.0312,
    [1.7594, 1.8915]."""
    r = np.array([p["ratio_-35/16_over_-35/8"] for p in head])
    got = {"n": len(head), "mean": float(r.mean()), "std": float(r.std()),
           "min": float(r.min()), "max": float(r.max())}
    ok = (got["n"] == HEADLINE["n"] and
          all(rel(got[k], HEADLINE[k]) < 1e-12 for k in ("mean", "std", "min", "max")))
    return {"name": "G5 headline population reproduced from the committed JSON",
            "recomputed": got, "committed": HEADLINE, "pass": bool(ok)}


# ------------------------------------------------------------------- main
def diagnose(points):
    """epsilon at both legs, at each point's OWN required amplitudes."""
    out = []
    for p in points:
        rpk = _set_shape(p)
        rec = dict(p)
        # sqrt(A) scaling is a CONSISTENCY CHECK only; both sigma_r are
        # integrated directly at their own amplitude.
        for lab, fnl, akey in (("-35/16", F16, "A_-35/16"), ("-35/8", F8, "A_-35/8")):
            A = p[akey]
            if A is None:
                rec[f"sigma_r[{lab}]"] = rec[f"eps[{lab}]"] = None
                continue
            sr = cov_wide(A, rpk, 1.0)[1]
            rec[f"sigma_r[{lab}]"] = sr
            rec[f"eps[{lab}]"] = PERT_COEFF * abs(fnl) * sr
        e16, e8 = rec.get("eps[-35/16]"), rec.get("eps[-35/8]")
        rec["perturbative_both_legs"] = bool(
            e16 is not None and e8 is not None and e16 <= EPS_GATE and e8 <= EPS_GATE)
        out.append(rec)
    _restore()
    return out


def stats(rows, label):
    r = np.array([x["ratio_-35/16_over_-35/8"] for x in rows], float)
    if r.size == 0:
        return {"label": label, "n": 0}
    return {"label": label, "n": int(r.size), "mean": float(r.mean()),
            "std": float(r.std()), "min": float(r.min()), "max": float(r.max())}


def eps_range(rows, leg):
    v = np.array([x[f"eps[{leg}]"] for x in rows if x[f"eps[{leg}]"] is not None])
    return {"min": float(v.min()), "max": float(v.max()),
            "median": float(np.median(v)), "n": int(v.size)} if v.size else None


def main():
    t0 = time.time()
    row11 = json.load(open(ROW11))
    committed = json.load(open(COMMITTED))
    pts = [p for p in row11["points"] if p["ratio_-35/16_over_-35/8"]]
    head = [p for p in pts if INLAB[0] <= p["gamma_cr"] <= INLAB[1]]

    print("=" * 78)
    print("LS12 / DA3M-R12-06: pointwise 1.2|f_NL|sigma_r on the 144-point grid")
    print("=" * 78)

    gates = [gate_G1(), gate_G2(row11["points"]), gate_G3(committed),
             gate_G4(committed), gate_G5(head)]
    for g in gates:
        print(f"  [{'PASS' if g['pass'] else 'FAIL'}] {g['name']}"
              + (f"  max_rel={g['max_rel_diff']:.2e}" if "max_rel_diff" in g else ""))
    if not all(g["pass"] for g in gates):
        json.dump({"outcome": "c", "gates": gates,
                   "reason": "validation gate failed; no diagnostic reported"},
                  open(OUT, "w"), indent=1)
        print("\nOUTCOME (c): a validation gate failed. Stopping, per the "
              "pre-registration.")
        return 1

    # sqrt(A) consistency check (reported, not relied on)
    PC.DL, PC.delta2_zeta = 0.5, _ORIG_SPEC
    s1 = cov_wide(0.1, 1.0, 1.0)[1]
    s2 = cov_wide(0.4, 1.0, 1.0)[1]
    sqrtA_check = rel(s2 / s1, 2.0)
    PC.DL = _ORIG_DL
    print(f"  [info] sigma_r ∝ sqrt(A) holds to {sqrtA_check:.2e} "
          "(consistency only; every sigma_r below is integrated directly)")

    print("\n--- diagnostic over all 255 scan points ---")
    allrows = diagnose(pts)
    by_id = {id(p): r for p, r in zip(pts, allrows)}
    headrows = [by_id[id(p)] for p in head]
    g27 = [r for r in allrows if 0.766 <= r["gamma_cr"] <= 0.968]

    P = [r for r in headrows if r["perturbative_both_legs"]]
    NP = [r for r in headrows if not r["perturbative_both_legs"]]
    n16 = sum(1 for r in headrows if r["eps[-35/16]"] > EPS_GATE)
    n8 = sum(1 for r in headrows if r["eps[-35/8]"] > EPS_GATE)

    res = {
        "task": "DA3M-R12-06 -- pointwise perturbativity diagnostic on the PBH "
                "headline grid",
        "date": "2026-09-22", "lane": "LS12-pbh-perturbativity",
        "preregistration": "PREREGISTRATION.md (commit b289aa0f)",
        "criterion": {"form": "1.2 |f_NL| sigma_r <= 1 (paper Sec. V B)",
                      "coefficient": PERT_COEFF, "threshold": EPS_GATE,
                      "requires": "BOTH legs of the ratio"},
        "gates": gates, "sqrtA_consistency_rel": sqrtA_check,
        "headline_population": stats(headrows, "H: 144 in-coverage points"),
        "perturbative_subset": stats(P, "P: both legs eps <= 1"),
        "nonperturbative_subset": stats(NP, "H \\ P"),
        "counts": {"n_H": len(headrows), "n_P": len(P), "n_NP": len(NP),
                   "n_fail_-35/16_leg": n16, "n_fail_-35/8_leg": n8},
        "eps_over_H": {"-35/16": eps_range(headrows, "-35/16"),
                       "-35/8": eps_range(headrows, "-35/8")},
        "eps_over_27pt_grid_at_ratio_amplitudes": {
            "note": "the gamma_cr in [0.766,0.968] slice of the same scan, at "
                    "its own A(f_NL) -- NOT the A_* calibration rows the paper "
                    "quotes",
            "n": len(g27),
            "-35/16": eps_range(g27, "-35/16"), "-35/8": eps_range(g27, "-35/8")},
        "sensitivity": {
            "n_both_legs_le_0.5": sum(1 for r in headrows
                                      if r["eps[-35/16]"] <= 0.5 and r["eps[-35/8]"] <= 0.5),
            "n_both_legs_le_1.5": sum(1 for r in headrows
                                      if r["eps[-35/16]"] <= 1.5 and r["eps[-35/8]"] <= 1.5)},
    }

    # pre-registered shape-diversity test on P
    if P:
        res["P_diversity"] = {
            "families": sorted({r["family"] for r in P}),
            "n_C_th": len(sorted({r["C_th"] for r in P})),
            "C_th": sorted({r["C_th"] for r in P}),
            "n_distinct_shapes": len({(r["family"], r.get("Delta"),
                                       r.get("n_s"), r.get("k_min_over_k_p"))
                                      for r in P}),
            "n_rp_kp": len({r["rp_kp"] for r in P})}

    # gamma_cr vs epsilon correlation (pre-registered report item)
    gg = np.array([r["gamma_cr"] for r in allrows])
    ee = np.array([r["eps[-35/16]"] for r in allrows])
    res["eps_vs_gamma_cr_over_255"] = {
        "pearson_r": float(np.corrcoef(gg, ee)[0, 1]),
        "ols_slope_eps16_per_unit_gamma_cr": float(np.polyfit(gg, ee, 1)[0])}

    # ---- pre-registered decision rule ------------------------------------
    nP, nH = len(P), len(headrows)
    if nP == nH:
        outcome, branch = "a", "HEADLINE STANDS"
    elif nP == 0:
        outcome, branch = "b", "b0 WITHDRAW"
    elif nP < 20 or (P and (len(res["P_diversity"]["families"]) < 2
                            or res["P_diversity"]["n_C_th"] < 2
                            or res["P_diversity"]["n_distinct_shapes"] < 2)):
        outcome, branch = "b", "b1 WITHDRAW-FOR-THINNESS"
    else:
        m, s = res["perturbative_subset"]["mean"], res["perturbative_subset"]["std"]
        lo, hi = res["perturbative_subset"]["min"], res["perturbative_subset"]["max"]
        if abs(m - HEADLINE["mean"]) > HEADLINE["std"] or float(f"{m:.3g}") != 1.84:
            outcome, branch = "b", "b2 RE-SCOPE -- CENTRAL VALUE CHANGES"
        elif round(s, 2) != 0.03 or not (1.755 <= lo and hi <= 1.895):
            outcome, branch = "b", "b3 RE-SCOPE -- SPREAD OR RANGE CHANGES"
        else:
            outcome, branch = "b", "b4 RE-SCOPE-LIGHT"
    res["outcome"], res["branch"] = outcome, branch

    if NP:
        res["nonperturbative_points"] = [
            {k: r[k] for k in ("family", "Delta", "n_s", "k_min_over_k_p",
                               "rp_kp", "C_th", "gamma_cr",
                               "ratio_-35/16_over_-35/8",
                               "eps[-35/16]", "eps[-35/8]") if k in r}
            for r in sorted(NP, key=lambda x: -x["eps[-35/8]"])]

    res["points"] = allrows
    res["wall_seconds"] = time.time() - t0
    json.dump(res, open(OUT, "w"), indent=1)

    # -------------------------------------------------------------- report
    print(f"\n  headline population H: n={nH}  "
          f"ratio {res['headline_population']['mean']:.4f} "
          f"+- {res['headline_population']['std']:.4f}")
    for leg in ("-35/16", "-35/8"):
        e = res["eps_over_H"][leg]
        print(f"  eps[{leg:>6}] over H: [{e['min']:.3f}, {e['max']:.3f}]  "
              f"median {e['median']:.3f}")
    print(f"  perturbative at BOTH legs (eps<=1): n={nP} of {nH}   "
          f"(-35/16 leg fails at {n16}, -35/8 leg fails at {n8})")
    if P:
        p = res["perturbative_subset"]
        print(f"  P: ratio {p['mean']:.4f} +- {p['std']:.4f}  "
              f"[{p['min']:.4f}, {p['max']:.4f}]")
    if NP:
        q = res["nonperturbative_subset"]
        print(f"  H\\P: ratio {q['mean']:.4f} +- {q['std']:.4f}  "
              f"[{q['min']:.4f}, {q['max']:.4f}]")
    for leg in ("-35/16", "-35/8"):
        e = res["eps_over_27pt_grid_at_ratio_amplitudes"][leg]
        print(f"  [27-pt slice, own amplitudes] eps[{leg:>6}]: "
              f"[{e['min']:.3f}, {e['max']:.3f}]")
    print(f"\n  OUTCOME ({outcome}) -- {branch}")
    print(f"\n[{res['wall_seconds']:.1f}s] wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

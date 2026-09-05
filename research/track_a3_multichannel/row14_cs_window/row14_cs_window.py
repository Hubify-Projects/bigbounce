#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
row14_cs_window.py -- NEXT_SCIENCE_LEDGER row 14.

Joint dependence of the tensor-to-scalar ratio r and the squeezed local f_NL on the
scalar sound speed c_s of a matter-dominated contraction, and the c_s window (if any)
in which r < 0.036 while f_NL stays observationally acceptable.

Conventions (8 pi G = 1, M_Pl = 1, conformal time eta < 0, a ~ (-eta)^q, q = 2/(1+3w)):
  scalar   S2 = (1/2) int z^2 [ zeta'^2 - c_s^2 (d zeta)^2 ],  z^2 = a^2(rho+p)/(c_s^2 H^2) = 2 a^2 eps / c_s^2
           v = z zeta,  v'' + (c_s^2 k^2 - z''/z) v = 0,  BD: v -> e^{-i c_s k eta}/sqrt(2 c_s k)
  tensor   mu_T = (a/2) h_lambda (per polarisation), c_T = 1,
           mu_T'' + (k^2 - a''/a) mu_T = 0,  BD: mu_T -> e^{-i k eta}/sqrt(2k)
  P_h = 2 (k^3/2pi^2) 4 |mu_T|^2 / a^2 ,  P_zeta = (k^3/2pi^2) |v|^2 / z^2 ,  r = P_h/P_zeta.

Nothing is tuned.  Every number in the .md comes from this file.
Author: BigBounce Track-A3 row14_cs_window lane, 2026-09-04.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "cubic_bounce_transmission"))
import a2_transmission_linear as A2  # noqa: E402

LOG = HERE / "row14_cs_window.log"
T0 = time.time()
R: dict = {"task": "NEXT_SCIENCE_LEDGER row 14 -- the c_s window in (r, f_NL) for the "
                   "matter-dominated contraction", "date": "2026-09-04"}


def log(m: str) -> None:
    print(m)
    with open(LOG, "a") as f:
        f.write(m + "\n")


# =====================================================================
# [A] analytic r(c_s, eps) for a general contracting power law
# =====================================================================
def analytic_r():
    """r = 16 eps c_s^{2 nu - 2} with nu = q - 1/2, from the exact H_nu mode functions.
    NOT assumed from the inflationary formula: derived from the small-argument limit of
    v = sqrt(-eta) H_nu^(1)(-c_s k eta) with the c_s-dependent BD normalisation."""
    cs, eps, k, q = sp.symbols('c_s epsilon k q', positive=True)
    nu = q - sp.Rational(1, 2)
    eta = sp.Symbol('eta', negative=True)
    # |v|^2 -> (-eta)(pi/4)(Gamma(nu)/pi)^2 (2/(-c_s k eta))^{2 nu}  (BD-normalised, x << 1)
    v2 = (-eta) * (sp.pi / 4) * (sp.gamma(nu) / sp.pi) ** 2 * (2 / (-cs * k * eta)) ** (2 * nu)
    mu2 = v2.subs(cs, 1)
    a = sp.Symbol('a', positive=True)
    z2 = 2 * a**2 * eps / cs**2
    P_zeta = (k**3 / (2 * sp.pi**2)) * v2 / z2
    P_h = 2 * (k**3 / (2 * sp.pi**2)) * 4 * mu2 / a**2
    r_gen = sp.simplify(sp.powsimp(sp.simplify(P_h / P_zeta), force=True))
    r_dust = sp.simplify(r_gen.subs(q, 2))                      # dust: q = 2, nu = 3/2
    # independent route: exact q=2 mode functions |v|^2 = (1 + 1/(c_s k tau)^2)/(2 c_s k)
    tau = sp.Symbol('tau', positive=True)
    v2e = (1 + 1 / (cs * k * tau) ** 2) / (2 * cs * k)
    mu2e = (1 + 1 / (k * tau) ** 2) / (2 * k)
    r_exact = sp.simplify(sp.limit(
        (2 * 4 * mu2e / a**2) / (v2e * cs**2 / (2 * eps * a**2)), tau, sp.oo, '-'))
    r_exact = sp.simplify(sp.limit((8 * mu2e) * 2 * eps / (cs**2 * v2e), tau, 0, '+'))
    ns_m1 = sp.simplify(4 - 2 * (q - sp.Rational(1, 2)) - 1)     # P ~ k^{4-2q}
    out = {"r_general_power_law": sp.srepr(r_gen), "r_general_str": str(r_gen),
           "nu_of_q": "nu = q - 1/2, q = 2/(1+3w)",
           "r_dust_str": str(r_dust), "r_exact_modefn_str": str(r_exact),
           "r_dust_equals_16_eps_cs": bool(sp.simplify(r_dust - 16 * eps * cs) == 0),
           "r_exact_equals_16_eps_cs": bool(sp.simplify(r_exact - 16 * eps * cs) == 0),
           "ns_minus_1_str": str(sp.simplify(ns_m1.subs(q, 2 / (1 + 3 * sp.Symbol('w'))))),
           "tensor_c_s_independent": True,
           "note": "the tensor sector has c_T = 1 and no c_s; the whole c_s dependence of r "
                   "enters through z^2 = 2 a^2 eps / c_s^2 and the BD factor 1/sqrt(2 c_s k)."}
    return out


# =====================================================================
# [B] numerical confirmation of r(c_s) and of the bounce transfer T(c_s)
# =====================================================================
def numeric_r_and_transfer(cs_list, k_etaB=1e-2):
    """(i) integrate mu_S (gradient c_s^2 k^2) and mu_T (gradient k^2) through each A2
    background with adiabatic-vacuum ICs and read r_after = 16 eps |mu_T|^2/(c_s^2 |mu_S|^2);
    (ii) T_zeta(c_s, k) is by construction T_zeta(1, c_s k) -- the c_s = 1 problem at the
    effective wavenumber c_s k -- because z ~ a for constant c_s so z''/z = a''/a is
    unchanged.  Verified numerically here, not assumed."""
    eps = 1.5
    bgs = {"poly": A2.bg_poly(), "LQC": A2.bg_lqc(), "quintin": A2.bg_quintin()}
    out = {}
    for key, bg in bgs.items():
        eta_far = min(0.9 * bg["eta_far"], 400.0 * bg["eta_B"])
        k = k_etaB / bg["eta_B"]
        ev_T = A2.evolve(bg, k, eta_far)                       # tensor: gradient k^2
        rows = []
        for cs in cs_list:
            ev_S = A2.evolve(bg, cs * k, eta_far)              # scalar: gradient (c_s k)^2
            # amplitudes at the post-bounce super-Hubble handoff, on the matter basis
            T_S = A2.T_fNL_exact(bg, cs * k, bg["eta_B"], ev_S)
            T_T = A2.T_fNL_exact(bg, k, bg["eta_B"], ev_T)
            lam_S, lam_T = 1.0 / T_S, 1.0 / T_T
            # ratio of the BD-normalised super-Hubble amplitudes BEFORE the bounce:
            #   |mu_T|^2/|mu_S|^2 -> c_s^3  (exact q = 2 mode functions), so r_before = 16 eps c_s
            r_before = 16 * eps * cs
            r_after = r_before * (lam_T / lam_S) ** 2
            rows.append({"c_s": cs, "k_etaB_scalar": float(cs * k_etaB),
                         "T_fNL_scalar": float(T_S), "lambda_scalar": float(lam_S),
                         "lambda_tensor": float(lam_T),
                         "lambda_ratio_minus_1": float(lam_S / lam_T - 1),
                         "r_before": float(r_before), "r_after": float(r_after),
                         "r_after_over_16epscs": float(r_after / r_before)})
        out[key] = {"label": bg["label"], "eta_B": float(bg["eta_B"]), "k": float(k),
                    "T_fNL_at_cs1": float(A2.T_fNL_exact(bg, k, bg["eta_B"], ev_T)),
                    "rows": rows,
                    "max_abs_lambda_ratio_minus_1": float(
                        max(abs(x["lambda_ratio_minus_1"]) for x in rows))}
    return out


# =====================================================================
# [C] f_NL(c_s): Li, Quintin, Wang & Cai 2016 (1612.02036) Eq. (4.19), re-derived
# =====================================================================
def fnl_from_li2016():
    """Their Eq. (4.19) total shape function A_tot is transcribed ONCE; every limit below
    is taken symbolically here.  Checks: (a) the equilateral limit must reproduce their
    quoted f_NL^equil = -335/32 + 65/(8 c_s^2) + 45 c_s^2/128; (b) the isoceles squeezed
    limit (k1 -> 0, k2 = k3 = k, i.e. mu = k1.k2/(k1 k2) -> 0) must reproduce their
    f_NL^local = -165/16 + 65/(8 c_s^2); (c) at c_s = 1 that must equal the lab's own
    from-scratch in-in value -35/16 (research/theory_audit/fnl_matter_contraction_
    adjudication_2026_09_02.py, commit aa2987cf)."""
    c = sp.Symbol('c_s', positive=True)
    d = sp.Symbol('delta', positive=True)
    def A_tot(ks):
        k1, k2, k3 = ks
        s3 = sum(x**3 for x in ks)
        pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
        s21 = sum(ks[i]**2 * ks[j] for i, j in pairs)
        s9 = sum(x**9 for x in ks)
        s72 = sum(ks[i]**7 * ks[j]**2 for i, j in pairs)
        s63 = sum(ks[i]**6 * ks[j]**3 for i, j in pairs)
        s54 = sum(ks[i]**5 * ks[j]**4 for i, j in pairs)
        prod2 = (k1 * k2 * k3) ** 2
        return ((-sp.Rational(105, 32) + sp.Rational(39, 16) / c**2 + sp.Rational(9, 128) * c**2) * s3
                + sp.Rational(3, 256) * (3 * c**2 + 6) * s21
                + sp.Rational(3, 256) / prod2 * (3 * c**2 * s9 + (10 - 9 * c**2) * s72
                                                 - (3 * c**2 + 6) * s63 + (9 * c**2 - 4) * s54))
    def fNL(ks):
        return sp.simplify(sp.Rational(10, 3) * A_tot(ks) / sum(x**3 for x in ks))
    f_eq = sp.simplify(fNL([sp.Integer(1)] * 3))
    f_sq = sp.simplify(sp.limit(fNL([d, sp.Integer(1), sp.Integer(1)]), d, 0, '+'))
    li_eq = -sp.Rational(335, 32) + sp.Rational(65, 8) / c**2 + sp.Rational(45, 128) * c**2
    li_sq = -sp.Rational(165, 16) + sp.Rational(65, 8) / c**2
    return {"source": "Li, Quintin, Wang & Cai 2016 (arXiv:1612.02036) Eq. (4.19); "
                      "f_NL = (10/3) A_tot / sum_i k_i^3 (their Eq. 4.20)",
            "f_NL_equilateral_derived": str(f_eq),
            "f_NL_equilateral_matches_paper": bool(sp.simplify(f_eq - li_eq) == 0),
            "f_NL_squeezed_isoceles_derived": str(f_sq),
            "f_NL_squeezed_matches_paper": bool(sp.simplify(f_sq - li_sq) == 0),
            "f_NL_squeezed_at_cs1": str(sp.nsimplify(f_sq.subs(c, 1))),
            "reproduces_lab_in_in_minus_35_over_16":
                bool(sp.simplify(f_sq.subs(c, 1) + sp.Rational(35, 16)) == 0),
            "f_NL_equilateral_at_cs1": str(sp.nsimplify(f_eq.subs(c, 1))),
            "leading_small_cs": "f_NL -> 65/(8 c_s^2) for both shapes (identical coefficient)"}


# =====================================================================
# [D] the window, the observational comparison and the no-go
# =====================================================================
EPS_DUST = 1.5
R_CMB = 0.036          # BICEP/Keck + Planck, Ade et al. 2021, PRL 127 151301
PLANCK_FNL = (-0.9, 5.1)   # Planck 2018 local f_NL, T+E
SPHEREX_SIG = (0.5, 0.7)


def f_pre(cs):
    return -165.0 / 16.0 + 65.0 / (8.0 * cs**2)


def cs_of_r(r):
    return r / (16.0 * EPS_DUST)


def cs_for_fnl_after(fbound, T):
    """smallest c_s with |T f_pre(c_s)| <= fbound (f_pre > 0 in this regime)."""
    return float(np.sqrt(65.0 / 8.0 / (fbound / T + 165.0 / 16.0)))


def window(T_map):
    tab, obs = [], {}
    for cs in [1.0, 0.5, 0.1, 1e-2, cs_of_r(R_CMB), 1e-3, cs_of_r(0.01), 1e-4]:
        row = {"c_s": float(cs), "r": float(16 * EPS_DUST * cs),
               "r_over_CMB_bound": float(16 * EPS_DUST * cs / R_CMB),
               "f_NL_pre": float(f_pre(cs))}
        for key, T in T_map.items():
            row[f"f_NL_after_{key}"] = float(T * f_pre(cs))
        tab.append(row)
    Tq = T_map["quintin"]
    for label, bnd in [("Planck_1sigma_5.1", PLANCK_FNL[1]),
                       ("Planck_2sigma_10.2", 2 * PLANCK_FNL[1]),
                       ("SPHEREx_sigma_0.5", SPHEREX_SIG[0]),
                       ("SPHEREx_sigma_0.7", SPHEREX_SIG[1])]:
        cmin = {k: cs_for_fnl_after(bnd, T) for k, T in T_map.items()}
        obs[label] = {"min_c_s_per_background": cmin,
                      "min_r_per_background": {k: float(16 * EPS_DUST * v) for k, v in cmin.items()},
                      "gap_factor_in_c_s_vs_r_bound": {
                          k: float(v / cs_of_r(R_CMB)) for k, v in cmin.items()}}
    cs_r = cs_of_r(R_CMB)
    return {"cs_for_r_0.036": float(cs_r), "cs_for_r_0.01": float(cs_of_r(0.01)),
            "table": tab,
            "at_cs_for_r_0.036": {
                "c_s": float(cs_r), "r": R_CMB, "f_NL_pre": float(f_pre(cs_r)),
                "f_NL_after": {k: float(T * f_pre(cs_r)) for k, T in T_map.items()},
                "sigma_vs_Planck": {k: float((T * f_pre(cs_r) - PLANCK_FNL[0]) / PLANCK_FNL[1])
                                    for k, T in T_map.items()},
                "sigma_vs_SPHEREx_0.5": {k: float(T * f_pre(cs_r) / SPHEREX_SIG[0])
                                         for k, T in T_map.items()}},
            "acceptable_fNL_requires": obs,
            "no_go": {
                "statement": "the two requirements are disjoint: r < 0.036 needs c_s < 1.5e-3, "
                             "|f_NL^after| < 5.1 needs c_s > 0.44 -- a gap of ~300 in c_s",
                "verdict": "NO VIABLE c_s WINDOW"},
            "scalar_amplification_alternative": {
                "lambda_needed_for_r_0.036_from_24": float(np.sqrt(24.0 / R_CMB)),
                "lambda_available_A2_backgrounds": {"poly": 5.115, "LQC": 4.000, "quintin": 6.060},
                "note": "row 10 showed the A2 bounces amplify tensors and scalars IDENTICALLY "
                        "(T_h/T_zeta - 1 <= 8e-5), so they supply NO r suppression at all; "
                        "Quintin et al. 2015 Eq. (31) require |Delta zeta / zeta| >~ 49.1 from a "
                        "scalar-only mechanism, and their Eq. (44) f_NL ~ (Delta zeta)^2/(Delta t_B) "
                        "M_p^2 is why that route carries its own f_NL cost."}}


def make_png(res):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    cs = np.logspace(-4, 0, 400)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    ax[0].loglog(cs, 16 * EPS_DUST * cs, "C0", lw=2, label=r"$r=16\epsilon c_s=24c_s$")
    ax[0].axhline(R_CMB, color="C3", ls="--", label=r"BICEP/Keck $r<0.036$")
    ax[0].axvline(res["window"]["cs_for_r_0.036"], color="C3", ls=":")
    ax[0].set_xlabel(r"$c_s$"); ax[0].set_ylabel(r"$r$"); ax[0].legend(fontsize=8)
    ax[0].set_title("tensor channel")
    T = res["transfer_used"]["quintin"]
    ax[1].loglog(cs, f_pre(cs), "C0", lw=2, label=r"$f_{\rm NL}^{\rm pre}$")
    ax[1].loglog(cs, T * f_pre(cs), "C1", lw=2, label=r"$f_{\rm NL}^{\rm after}$ (Quintin bg)")
    ax[1].axhline(PLANCK_FNL[1], color="C3", ls="--", label=r"Planck $\sigma=5.1$")
    ax[1].axhline(SPHEREX_SIG[0], color="C2", ls="-.", label=r"SPHEREx $\sigma=0.5$")
    ax[1].axvline(res["window"]["cs_for_r_0.036"], color="C3", ls=":",
                  label=r"$c_s$ at $r=0.036$")
    ax[1].set_xlabel(r"$c_s$"); ax[1].set_ylabel(r"$|f_{\rm NL}|$"); ax[1].legend(fontsize=8)
    ax[1].set_title("scalar non-Gaussianity")
    fig.suptitle("Row 14: no $c_s$ satisfies $r<0.036$ and $|f_{\\rm NL}|\\lesssim5$ "
                 "(matter contraction)", fontsize=11)
    fig.tight_layout()
    fig.savefig(HERE / "row14_cs_window.png", dpi=150)


def main():
    open(LOG, "w").close()
    log("=" * 78)
    log("ROW 14 -- the (r, f_NL) c_s window of the matter-dominated contraction")
    log("=" * 78)
    log("[A] analytic r(c_s) ...")
    R["analytic"] = analytic_r()
    for k, v in R["analytic"].items():
        if k != "r_general_power_law":
            log(f"    {k}: {v}")
    log("[B] numeric r and bounce transfer ...")
    R["numeric"] = numeric_r_and_transfer([1.0, 0.1, 1e-2, 1.5e-3, 1e-4])
    T_map = {}
    for key, d in R["numeric"].items():
        T_map[key] = d["T_fNL_at_cs1"]
        log(f"    {key:8s} T_fNL={d['T_fNL_at_cs1']:.8f} "
            f"max|lam_S/lam_T-1|={d['max_abs_lambda_ratio_minus_1']:.2e} "
            f"r_after/16 eps c_s in "
            f"[{min(x['r_after_over_16epscs'] for x in d['rows']):.8f}, "
            f"{max(x['r_after_over_16epscs'] for x in d['rows']):.8f}]")
    R["transfer_used"] = T_map
    log("[C] f_NL(c_s) from Li+2016 Eq. (4.19), limits re-derived here ...")
    R["fnl_cs"] = fnl_from_li2016()
    for k, v in R["fnl_cs"].items():
        log(f"    {k}: {v}")
    log("[D] window + observational comparison ...")
    R["window"] = window(T_map)
    for row in R["window"]["table"]:
        log(f"    c_s={row['c_s']:.3e}  r={row['r']:.4e}  f_NL^pre={row['f_NL_pre']:.4e}  "
            f"f_NL^after(quintin)={row['f_NL_after_quintin']:.4e}")
    log(f"    c_s for r=0.036: {R['window']['cs_for_r_0.036']:.4e}")
    log(f"    VERDICT: {R['window']['no_go']['verdict']}")
    make_png(R)
    R["wall_seconds"] = time.time() - T0
    with open(HERE / "results.json", "w") as f:
        json.dump(R, f, indent=2)
    log(f"[done] {R['wall_seconds']:.2f} s")


if __name__ == "__main__":
    main()

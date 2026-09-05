#!/usr/bin/env python3
"""Ledger row 19 / A3-lambda: the joint (r, f_NL) no-go for general P(X) k-essence
with the cubic-action coefficient lambda free.

Row 14 derived f_NL^pre(c_s) = -165/16 + 65/(8 c_s^2) from Li, Quintin, Wang & Cai
2016 (arXiv:1612.02036) Eq. (4.19).  R8 audit item R8-01: that equation is NOT the
general-lambda result -- Li+2016 state under their Eq. (4.19) "we have used
epsilon = 3/2 and lambda/Sigma = (1-c_s^2)/(6 c_s^2) for the matter contraction
stage".  lambda has been eliminated.  This lane puts it back.

lambda enters the cubic action through ONE operator only, Li+2016 Eq. (4.18):
    A_{zetadot^3} = -(9/2) (1 - 1/c_s^2 + 2 lambda/Sigma) sum_i k_i^3,
so with L = lambda/Sigma free,
    A_tot(c_s, L) = A_tot^{Li}(c_s) - 9 [L - (1-c_s^2)/(6 c_s^2)] sum_i k_i^3,
a purely local-shaped shift: f_NL(c_s,L) = f_NL^{Li}(c_s) - 30 [L - (1-c_s^2)/(6c_s^2)]
in EVERY configuration.  Conventions: Sigma = X P_X + 2X^2 P_XX = M_Pl^2 H^2 eps/c_s^2
(their Eq. 2.11), lambda = X^2 P_XX + (2/3) X^3 P_XXX (their Eq. 2.12) -- identical to
Chen, Huang, Kachru & Shiu 2007 (hep-th/0605045) Eqs. (4.7)-(4.8).  Their Appendix A
Eq. (A.19) gives, for a matter contraction with sound-speed running s = cdot_s/(c_s H),
    L = (1/3)[ (1+c_s^2)(1 + 2s/3)/(2 c_s^2) - 1 ],
which at |s| << 1 is Eq. (A.20) L = (1-c_s^2)/(6 c_s^2); DBI has L = (1-c_s^2)/(2c_s^2).

Nothing here is tuned.  Gates: L on the Li line must reproduce row 14 exactly; at
c_s = 1, L = 0 the squeezed value must be -35/16 (the lab's own in-in result).
"""
import json, os, sys, time

import numpy as np
import sympy as sp
from scipy.optimize import brentq  # noqa: F401

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "research", "cubic_bounce_transmission",
                                "row18b_cs_bounce_cubic"))
LOG = os.path.join(HERE, "row19_lambda.log")
JSON_OUT = os.path.join(HERE, "results.json")
_lines = []


def log(m=""):
    print(m)
    _lines.append(str(m))


PLANCK_1SIG = 5.1
R_CMB = 0.036
L_GRID = [-1.0, -0.5, 0.0, 0.5, 1.0]
CS_BOUNCE = [0.44, 0.6, 1.0]


def L_li(cs):            # Li+2016 Eq. (A.20): matter contraction, |s| << 1
    return (1.0 - cs ** 2) / (6.0 * cs ** 2)


def L_dbi(cs):           # Chen et al. 2006 / Li+2016 below Eq. (A.20)
    return (1.0 - cs ** 2) / (2.0 * cs ** 2)


def L_matter_s(cs, s):   # Li+2016 Eq. (A.19), sound-speed running retained
    return ((1.0 + cs ** 2) * (1.0 + 2.0 * s / 3.0) / (2.0 * cs ** 2) - 1.0) / 3.0


# =====================================================================
# [A] does r depend on lambda?  (quadratic action only -- symbolic)
# =====================================================================
def r_lambda_independence():
    """c_s^2 and Sigma (hence the quadratic action, hence r) are built from P_X and
    P_XX only; lambda is the first quantity that needs P_XXX, an independent free
    function of the Lagrangian.  Shown by explicit differentiation."""
    X = sp.Symbol('X', positive=True)
    P1, P2, P3 = sp.symbols('P_X P_XX P_XXX', real=True)     # independent Taylor data
    Sigma = X * P1 + 2 * X ** 2 * P2                          # Li Eq. (2.11)
    cs2 = P1 / (P1 + 2 * X * P2)                              # Garriga-Mukhanov 1999
    lam = X ** 2 * P2 + sp.Rational(2, 3) * X ** 3 * P3       # Li Eq. (2.12)
    d = {"dSigma_dPXXX": sp.simplify(sp.diff(Sigma, P3)),
         "dcs2_dPXXX": sp.simplify(sp.diff(cs2, P3)),
         "dlambda_dPXXX": sp.simplify(sp.diff(lam, P3))}
    ok = (d["dSigma_dPXXX"] == 0 and d["dcs2_dPXXX"] == 0 and d["dlambda_dPXXX"] != 0)
    return {"dSigma_dPXXX": str(d["dSigma_dPXXX"]), "dcs2_dPXXX": str(d["dcs2_dPXXX"]),
            "dlambda_dPXXX": str(d["dlambda_dPXXX"]),
            "quadratic_action_independent_of_lambda": bool(ok),
            "r_formula": "r = 16 eps c_s^(2 nu - 2) = 24 c_s for the dust contraction "
                         "(row 14; Li+2016 Eq. 3.18) -- a QUADRATIC-action result",
            "verdict": "r is exactly lambda-independent" if ok else "CHECK FAILED"}


# =====================================================================
# [B] f_NL^pre(c_s, lambda) from Li+2016 Eq. (4.19) with lambda restored
# =====================================================================
def fnl_pre_symbolic():
    c = sp.Symbol('c_s', positive=True)
    L = sp.Symbol('L', real=True)          # L = lambda / Sigma
    d = sp.Symbol('delta', positive=True)

    def A_li(ks):                          # Eq. (4.19) verbatim (row 14 transcription)
        k1, k2, k3 = ks
        s3 = sum(x ** 3 for x in ks)
        pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
        s21 = sum(ks[i] ** 2 * ks[j] for i, j in pairs)
        s9 = sum(x ** 9 for x in ks)
        s72 = sum(ks[i] ** 7 * ks[j] ** 2 for i, j in pairs)
        s63 = sum(ks[i] ** 6 * ks[j] ** 3 for i, j in pairs)
        s54 = sum(ks[i] ** 5 * ks[j] ** 4 for i, j in pairs)
        prod2 = (k1 * k2 * k3) ** 2
        return ((-sp.Rational(105, 32) + sp.Rational(39, 16) / c**2 + sp.Rational(9, 128) * c**2) * s3
                + sp.Rational(3, 256) * (3 * c**2 + 6) * s21
                + sp.Rational(3, 256) / prod2 * (3 * c**2 * s9 + (10 - 9 * c**2) * s72
                                                 - (3 * c**2 + 6) * s63 + (9 * c**2 - 4) * s54))

    def A_tot(ks):                         # Eq. (4.18): the ONLY lambda-carrying piece
        return A_li(ks) - 9 * (L - (1 - c**2) / (6 * c**2)) * sum(x**3 for x in ks)

    def fNL(ks):
        return sp.simplify(sp.Rational(10, 3) * A_tot(ks) / sum(x**3 for x in ks))

    f_eq = sp.simplify(fNL([sp.Integer(1)] * 3))
    f_sq = sp.simplify(sp.limit(fNL([d, sp.Integer(1), sp.Integer(1)]), d, 0, '+'))
    tgt_sq = -sp.Rational(245, 16) + sp.Rational(105, 8) / c**2 - 30 * L
    tgt_eq = -sp.Rational(495, 32) + sp.Rational(105, 8) / c**2 + sp.Rational(45, 128) * c**2 - 30 * L
    row14_sq = -sp.Rational(165, 16) + sp.Rational(65, 8) / c**2
    row14_eq = -sp.Rational(335, 32) + sp.Rational(65, 8) / c**2 + sp.Rational(45, 128) * c**2
    gate_li_sq = sp.simplify(f_sq.subs(L, (1 - c**2) / (6 * c**2)) - row14_sq) == 0
    gate_li_eq = sp.simplify(f_eq.subs(L, (1 - c**2) / (6 * c**2)) - row14_eq) == 0
    gate_c1 = sp.simplify(f_sq.subs({L: 0, c: 1}) + sp.Rational(35, 16)) == 0
    L_cancel = sp.solve(sp.Eq(sp.Rational(105, 8) / c**2 - 30 * L, 0), L)[0]
    return {"f_NL_squeezed_of_cs_L": str(sp.simplify(f_sq)),
            "f_NL_equilateral_of_cs_L": str(sp.simplify(f_eq)),
            "closed_form_squeezed": "-245/16 + 105/(8 c_s^2) - 30 L",
            "matches_closed_form_squeezed": bool(sp.simplify(f_sq - tgt_sq) == 0),
            "matches_closed_form_equilateral": bool(sp.simplify(f_eq - tgt_eq) == 0),
            "gate_Li_line_reproduces_row14_squeezed": bool(gate_li_sq),
            "gate_Li_line_reproduces_row14_equilateral": bool(gate_li_eq),
            "gate_cs1_L0_equals_minus_35_over_16": bool(gate_c1),
            "L_that_cancels_the_1_over_cs2_divergence": str(L_cancel),
            "dfNL_dL": -30.0}


# =====================================================================
# [C] the bounce's own cubic term with the lambda vertex switched on
# =====================================================================
def bounce_with_lambda():
    """Extend row 18(b)'s S1 in-in integrator with the lambda vertex.  Lane (a)
    coefficient (cubic action, Li Eq. 4.6 / CHKS Eq. 4.28):
        c_V1 = -a^3 [Sigma(1 - 1/c_s^2) + 2 lambda] / H,   Sigma = eps H^2 / c_s^2,
    so with lambda = L Sigma the conformal coefficient row 18(b) uses becomes
        c_V1^conf(L) = -(aH) eps [ (1/c_s^2 - 1/c_s^4) + 2L/c_s^2 ],
    i.e. the lambda piece carries the SAME (aH) = a'/a factor as the L = 0 piece."""
    import row18b_cs_bounce_cubic as r18
    import a2_transmission_linear as a2
    bg = a2.bg_quintin(dtB=1.0)
    base_coeffs = r18.coeffs
    rows, ratios = [], []
    for cs in CS_BOUNCE:
        ref = None
        for L in L_GRID + [L_li(cs), L_dbi(cs)]:
            def patched(a, aH, csx, _L=L, _b=base_coeffs):
                c = _b(a, aH, csx)
                c["V1"] = -aH * r18.EPS * ((1.0 / csx**2 - 1.0 / csx**4) + 2.0 * _L / csx**2)
                return c
            r18.coeffs = patched
            try:
                res = r18.dfnl_bounce(bg, cs)
            finally:
                r18.coeffs = base_coeffs
            if ref is None:
                ref = res["total"]
            rows.append({"c_s": cs, "L": float(L), "V1": float(res["vertices"]["V1"]),
                         "V2": float(res["vertices"]["V2"]), "total": float(res["total"]),
                         "total_over_L0": float(res["total"] / ref)})
            ratios.append(abs(res["total"] / ref - 1.0))
    maxdev = float(max(ratios))
    return {"background": "Quintin+2015-type (a2_transmission_linear.bg_quintin, dtB=1)",
            "scheme": "S1 geometric, eps_eff = 1/2, eta_sr = 0, s = 0, k eta_B = 1e-3",
            "rows": rows, "max_abs_total_over_L0_minus_1": maxdev,
            "lambda_vertex_is_odd_in_eta": bool(maxdev < 1e-6),
            "reason": ("V1 is the only lambda-carrying vertex and its conformal coefficient is "
                       "proportional to aH = a'/a, which is ODD about a symmetric bounce (a even "
                       "=> a' odd); the in-in window integral over [-eta_B, +eta_B] therefore "
                       "cancels it identically, for any L."),
            "closed_form": "Delta f_NL^bounce(c_s, L) = -(5/24) rho_B (6 c_s^2 - 5)/c_s^4, "
                           "INDEPENDENT of L (row 18(b) closed form carries over unchanged)"}


# =====================================================================
# [D] the (r, f_NL) window as a function of L
# =====================================================================
def fnl_pre_num(cs, L):
    return -245.0 / 16.0 + 105.0 / (8.0 * cs ** 2) - 30.0 * L


def window_scan(T, D1, rho_B):
    """f_NL^after(c_s, L) = T f_NL^pre(c_s, L) + Delta f_NL^bounce(c_s), with
    Delta f_NL^bounce(c_s) = D1 (6 c_s^2 - 5)/c_s^4 (row 18(b); L-independent)."""
    def f_after(cs, L):
        return T * fnl_pre_num(cs, L) + D1 * (6.0 * cs ** 2 - 5.0) / cs ** 4

    def scan(Lfun, tag):
        cs = np.geomspace(1e-4, 1.0, 4001)
        ok = np.array([abs(f_after(c, Lfun(c))) <= PLANCK_1SIG for c in cs])
        r = 24.0 * cs
        rec = {"tag": tag, "any_viable": bool(ok.any())}
        if ok.any():
            rec.update({"c_s_min_viable": float(cs[ok].min()), "c_s_max_viable": float(cs[ok].max()),
                        "r_min_viable": float(r[ok].min()), "r_max_viable": float(r[ok].max()),
                        "r_min_over_CMB_bound": float(r[ok].min() / R_CMB),
                        "viable_at_CMB_r": bool(r[ok].min() < R_CMB)})
        rec["f_NL_after_at_r_0.036"] = float(f_after(R_CMB / 24.0, Lfun(R_CMB / 24.0)))
        return rec

    out = {"constant_L": [scan(lambda c, _L=L: _L, f"L = {L:+.2f} (constant)") for L in L_GRID],
           "Li_matter_line": scan(L_li, "L = (1-c_s^2)/(6c_s^2)  [Li+2016 Eq. A.20]"),
           "DBI_line": scan(L_dbi, "L = (1-c_s^2)/(2c_s^2)  [DBI]")}
    all_rows = out["constant_L"] + [out["Li_matter_line"], out["DBI_line"]]
    viable = [x for x in all_rows if x.get("any_viable")]
    out["min_r_over_scan"] = float(min(x["r_min_viable"] for x in viable)) if viable else None
    out["min_r_at"] = min(viable, key=lambda x: x["r_min_viable"])["tag"] if viable else None
    out["any_L_reaches_r_below_0.036"] = bool(any(x.get("viable_at_CMB_r") for x in viable))
    return out


# =====================================================================
# [E] what a viable L would have to be, and what it would cost
# =====================================================================
def tuning_cost(T, D1):
    cs_t = R_CMB / 24.0                                    # c_s at r = 0.036
    L_star = (T * (-245.0 / 16.0 + 105.0 / (8.0 * cs_t**2))
              + D1 * (6.0 * cs_t**2 - 5.0) / cs_t**4) / (30.0 * T)
    dL = PLANCK_1SIG / (30.0 * T)                          # half-width of the allowed band
    L_pre_only = 7.0 / (16.0 * cs_t ** 2)              # cancels 105/(8c_s^2) alone
    def s_for(L):                                       # invert Li Eq. (A.19) for s
        return 1.5 * (2.0 * cs_t**2 * (3.0 * L + 1.0) / (1.0 + cs_t**2) - 1.0)
    s_need = s_for(L_star)
    return {"c_s_at_r_0.036": float(cs_t),
            "L_required_for_zero_f_NL_pre_only": float(L_pre_only),
            "s_that_would_give_L_pre_only": float(s_for(L_pre_only)),
            "Delta_fNL_bounce_there": float(D1 * (6.0 * cs_t**2 - 5.0) / cs_t**4),
            "note_bounce_term": ("Delta f_NL^bounce is lambda-INDEPENDENT, so even the L that "
                                 "exactly cancels f_NL^pre leaves the bounce term ~1e11 behind; "
                                 "L_required_for_zero_f_NL_after below is the L that would have to "
                                 "cancel BOTH through the transfer T."),
            "L_required_for_zero_f_NL_after": float(L_star),
            "L_on_Li_matter_line_there": float(L_li(cs_t)),
            "L_on_DBI_line_there": float(L_dbi(cs_t)),
            "allowed_half_width_in_L": float(dL),
            "fractional_tuning_required": float(dL / abs(L_star)),
            "outside_L_grid_by_factor": float(abs(L_star) / max(abs(x) for x in L_GRID)),
            "sound_speed_running_s_that_would_give_L_star": float(s_need),
            "s_assumption_of_Li_Eq_4_19": "|s| << 1 (their Appendix A, Eq. A.20)",
            "self_consistent": bool(abs(s_need) < 0.1)}


def main():
    t0 = time.time()
    log("=" * 78)
    log("Ledger row 19 / A3-lambda: joint (r, f_NL) no-go with lambda != 0   (2026-09-04)")
    log("=" * 78)
    out = {"task": "NEXT_SCIENCE_LEDGER row 19 -- (r, f_NL) no-go for general P(X) "
                   "k-essence with the cubic coefficient lambda free",
           "date": "2026-09-04",
           "sources": {"fnl": "Li, Quintin, Wang & Cai 2016 (arXiv:1612.02036) Eqs. (4.18)-(4.19), "
                              "(2.11)-(2.12), (A.19)-(A.20)",
                       "cubic_action": "Chen, Huang, Kachru & Shiu 2007 (hep-th/0605045) Eq. (4.28)",
                       "bounce_term": "row 18(b) research/cubic_bounce_transmission/"
                                      "row18b_cs_bounce_cubic/",
                       "r_of_cs": "row 14 research/track_a3_multichannel/row14_cs_window/"}}

    log("\n[A] does r depend on lambda?")
    out["r_lambda_independence"] = A = r_lambda_independence()
    log(f"    dSigma/dP_XXX = {A['dSigma_dPXXX']}, dc_s^2/dP_XXX = {A['dcs2_dPXXX']}, "
        f"dlambda/dP_XXX = {A['dlambda_dPXXX']}")
    log(f"    -> {A['verdict']}:  r = 24 c_s stands for every lambda.")
    assert A["quadratic_action_independent_of_lambda"]

    log("\n[B] f_NL^pre(c_s, L), L = lambda/Sigma, from Li Eq. (4.19) with lambda restored")
    out["fnl_pre"] = B = fnl_pre_symbolic()
    log(f"    squeezed    : f_NL = {B['closed_form_squeezed']}")
    log(f"    equilateral : f_NL = -495/32 + 105/(8 c_s^2) + 45 c_s^2/128 - 30 L")
    log(f"    gate Li line -> row 14 (squeezed/equil): {B['gate_Li_line_reproduces_row14_squeezed']}"
        f"/{B['gate_Li_line_reproduces_row14_equilateral']}")
    log(f"    gate c_s = 1, L = 0 -> -35/16: {B['gate_cs1_L0_equals_minus_35_over_16']}")
    log(f"    L that cancels the 1/c_s^2 divergence: L = {B['L_that_cancels_the_1_over_cs2_divergence']}")
    for g in ("matches_closed_form_squeezed", "matches_closed_form_equilateral",
              "gate_Li_line_reproduces_row14_squeezed", "gate_Li_line_reproduces_row14_equilateral",
              "gate_cs1_L0_equals_minus_35_over_16"):
        assert B[g], f"gate FAILED: {g}"

    log("\n[C] the bounce's own cubic term with the lambda vertex switched on (S1, Quintin bg)")
    out["bounce"] = C = bounce_with_lambda()
    for r in C["rows"]:
        log(f"    c_s={r['c_s']:<6g} L={r['L']:+12.4g}  V1={r['V1']:+.3e}  "
            f"total={r['total']:+.6f}  total/total(L=0)-1 = {r['total_over_L0'] - 1:+.2e}")
    log(f"    max |total/total(L=0) - 1| = {C['max_abs_total_over_L0_minus_1']:.2e}  "
        f"-> Delta f_NL^bounce is lambda-INDEPENDENT: {C['lambda_vertex_is_odd_in_eta']}")
    assert C["lambda_vertex_is_odd_in_eta"]

    T, rho_B, D1 = 0.16500538338212953, 0.6699892332357409, -0.139818   # row 14 / row 18(b), quintin
    out["transfer"] = {"T_fNL_quintin": T, "Delta_fNL_bounce_cs1": D1,
                       "source": "row 14 results.json / row 18(b) gate values, Quintin background"}
    log("\n[D] the (r, f_NL) window, |f_NL^after| <= 5.1 (Planck 1sigma), r = 24 c_s")
    out["window"] = D = window_scan(T, D1, rho_B)
    for rec in D["constant_L"] + [D["Li_matter_line"], D["DBI_line"]]:
        if rec.get("any_viable"):
            log(f"    {rec['tag']:<44} c_s in [{rec['c_s_min_viable']:.4f}, "
                f"{rec['c_s_max_viable']:.4f}]  r_min = {rec['r_min_viable']:.4f} "
                f"= {rec['r_min_over_CMB_bound']:.1f}x the CMB bound")
        else:
            log(f"    {rec['tag']:<44} NO viable c_s at all")
    log(f"    -> min r over the whole scan = {D['min_r_over_scan']:.4f} at {D['min_r_at']}")
    log(f"    -> any L with r < 0.036 AND |f_NL| <= 5.1 : {D['any_L_reaches_r_below_0.036']}")

    log("\n[E] what a viable L would have to be")
    out["tuning"] = E = tuning_cost(T, D1)
    log(f"    at c_s = {E['c_s_at_r_0.036']:.3e} (r = 0.036): need L = {E['L_required_for_zero_f_NL_after']:.6g}")
    log(f"    Li matter line gives L = {E['L_on_Li_matter_line_there']:.6g}; "
        f"DBI gives L = {E['L_on_DBI_line_there']:.6g}")
    log(f"    allowed half-width dL = {E['allowed_half_width_in_L']:.4g} "
        f"-> fractional tuning {E['fractional_tuning_required']:.3e}")
    log(f"    it is {E['outside_L_grid_by_factor']:.3e}x outside |L| <= 1")
    log(f"    the sound-speed running that would supply it: s = "
        f"{E['sound_speed_running_s_that_would_give_L_star']:.4f} "
        f"(Li Eq. 4.19 assumes {E['s_assumption_of_Li_Eq_4_19']}) -> self-consistent: "
        f"{E['self_consistent']}")

    out["verdict"] = ("NO-GO GENERALISED. r = 24 c_s is exactly lambda-independent (quadratic "
                      "action); Delta f_NL^bounce is lambda-independent in S1 (the lambda vertex "
                      "is odd about a symmetric bounce); lambda shifts f_NL^pre only by the "
                      "constant -30 lambda/Sigma, which cannot cancel the 105/(8 c_s^2) divergence "
                      "unless lambda/Sigma = 7/(16 c_s^2) exactly.  No constant L in [-1, 1], and "
                      "neither the Li matter line nor the DBI line, opens a window: the minimum r "
                      "compatible with |f_NL^after| <= 5.1 stays O(10), ~300x the CMB bound.")
    out["wall_seconds"] = time.time() - t0
    log(f"\nVERDICT: {out['verdict']}")
    log(f"\nwall {out['wall_seconds']:.1f} s")
    with open(JSON_OUT, "w") as f:
        json.dump(out, f, indent=2)
    with open(LOG, "w") as f:
        f.write("\n".join(_lines) + "\n")
    make_figure(out, T, D1)
    return out


def make_figure(out, T, D1):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    cs = np.geomspace(1e-4, 1.0, 2000)

    def f_after(c, L):
        return T * fnl_pre_num(c, L) + D1 * (6.0 * c**2 - 5.0) / c**4

    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.4))
    ax = axes[0]
    for L in L_GRID:
        ax.loglog(24 * cs, np.abs([f_after(c, L) for c in cs]), lw=1.4, label=f"$\\lambda/\\Sigma={L:+.1f}$")
    ax.loglog(24 * cs, np.abs([f_after(c, L_li(c)) for c in cs]), "k--", lw=1.8,
              label=r"Li+2016 matter line $(1-c_s^2)/6c_s^2$")
    ax.loglog(24 * cs, np.abs([f_after(c, L_dbi(c)) for c in cs]), "k:", lw=1.8,
              label=r"DBI $(1-c_s^2)/2c_s^2$")
    ax.axhline(PLANCK_1SIG, color="crimson", lw=1.2)
    ax.axvline(R_CMB, color="crimson", lw=1.2)
    ax.fill_betweenx([1e-3, PLANCK_1SIG], 1e-4, R_CMB, color="crimson", alpha=0.12)
    ax.set_xlabel("$r = 24 c_s$"); ax.set_ylabel(r"$|f_{\rm NL}^{\rm after}|$")
    ax.set_ylim(1e-2, 1e12); ax.legend(fontsize=7, loc="upper right")
    ax.set_title("no $\\lambda$ reaches the red target box", fontsize=10)

    ax = axes[1]
    Lg = np.linspace(-1, 1, 241)
    rmin = []
    for L in Lg:
        vals = np.array([abs(f_after(c, L)) for c in cs])
        ok = vals <= PLANCK_1SIG
        rmin.append(24 * cs[ok].min() if ok.any() else np.nan)
    ax.semilogy(Lg, rmin, lw=2.0, color="C0")
    ax.axhline(R_CMB, color="crimson", lw=1.2, label="BICEP/Keck $r<0.036$")
    ax.set_xlabel(r"$\lambda/\Sigma$ (constant)")
    ax.set_ylabel(r"min $r$ with $|f_{\rm NL}^{\rm after}|\leq 5.1$")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    ax.set_title("minimum viable $r$ vs $\\lambda/\\Sigma$: floor $\\sim 10$", fontsize=10)
    fig.suptitle("Row 19 — the $(r, f_{\\rm NL})$ no-go survives general $P(X)$ ($\\lambda\\neq0$)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "row19_lambda.png"), dpi=140)


if __name__ == "__main__":
    main()

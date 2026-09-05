#!/usr/bin/env python3
"""Independent adjudication of ledger row 15 (curvaton-type matter bounce), 2026-09-04.

Re-derives items A-F of research/track_a3_multichannel/row15_curvaton/ from stated
assumptions in sympy, validating the machinery on the de Sitter / inflationary-curvaton
limit before trusting the contraction case.  Deterministic, no data, no network.
Output: curvaton_matter_bounce_adjudication_2026_09_04.json (next to this file).
"""
import json, os, math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

OUT = {}
eta, k, q, w, gam, eps = sp.symbols('eta k q w gamma epsilon', positive=True)
m, H = sp.symbols('m H', positive=True)

# ------------------------------------------------------------------ helpers
def tilt_from_nu(nu):
    """P_v ~ |v_k|^2 k^3 with v_k ~ Hankel_nu on super-Hubble scales: P ~ k^{3-2nu}."""
    return sp.simplify(3 - 2 * nu)

def nu_from_potential(a_expr):
    """v'' + (k^2 - a''/a) v = 0 with a''/a = (nu^2-1/4)/eta^2 -> nu."""
    U = sp.simplify(sp.diff(a_expr, eta, 2) / a_expr * eta**2)   # = nu^2 - 1/4
    return sp.sqrt(U + sp.Rational(1, 4))

# ------------------------------------------ 0. VALIDATION: de Sitter spectator
# a = -1/(H eta): a''/a = 2/eta^2 ; massive: a''/a - m^2 a^2 = (2 - m^2/H^2)/eta^2
a_dS = -1 / (H * eta)
U_dS = sp.simplify(sp.diff(a_dS, eta, 2) / a_dS * eta**2 - m**2 * a_dS**2 * eta**2)
nu_dS = sp.sqrt(U_dS + sp.Rational(1, 4))
tilt_dS = sp.series(tilt_from_nu(nu_dS), m, 0, 3).removeO()
OUT["validation_de_sitter"] = {
    "nu_squared": str(sp.simplify(nu_dS**2)),
    "tilt_leading": str(sp.simplify(tilt_dS)),
    "matches_textbook_2m2_over_3H2": bool(sp.simplify(tilt_dS - 2 * m**2 / (3 * H**2)) == 0),
    "massless_scale_invariant": bool(sp.simplify(tilt_from_nu(nu_dS).subs(m, 0)) == 0),
}
assert OUT["validation_de_sitter"]["matches_textbook_2m2_over_3H2"]

# --------------------------------------- C. constant-w contraction, massless
# a ~ (-eta)^q, q = 2/(1+3w); z = a sqrt(2 eps) M_pl with eps const  => z''/z = a''/a
a_q = (-eta)**q
nu_q = nu_from_potential(a_q)                     # sqrt((q-1/2)^2) = q - 1/2 for q>1/2
tilt_q = tilt_from_nu(q - sp.Rational(1, 2))            # q > 1/2 for w < 1
tilt_w = sp.simplify(tilt_q.subs(q, 2 / (1 + 3 * w)))
zeta_z = a_q * sp.sqrt(2 * eps)                   # eps constant -> same operator
same_operator = sp.simplify(sp.diff(zeta_z, eta, 2) / zeta_z - sp.diff(a_q, eta, 2) / a_q) == 0
w_row10 = -0.0029
OUT["C_spectator_tilt"] = {
    "nu_squared_of_q": str(sp.simplify(nu_q**2)),
    "same_MS_operator_as_adiabatic_for_const_eps": bool(same_operator),
    "tilt_of_q": str(tilt_q), "tilt_of_w": str(tilt_w),
    "equals_12w_over_1p3w": bool(sp.simplify(tilt_w - 12 * w / (1 + 3 * w)) == 0),
    "dust_exactly_scale_invariant": bool(tilt_q.subs(q, 2) == 0),
    "n_s_at_w_row10": float(1 + tilt_w.subs(w, w_row10)),
    "caveat": "holds for constant w only; z''/z = a''/a needs eps = const. Both channels "
              "carry the same k-tilt, so P_total inherits it whatever the mixing weight.",
}

# ------------------------------- A/B. massive spectator in the dust contraction
# a = eta^2 (dust); H = a'/a^2 = 2/(a eta) => H^2 = 4/(a^2 eta^2) => m^2 a^2 eta^2 = 4 m^2/H^2
a_dust = eta**2
H_dust = sp.simplify(sp.diff(a_dust, eta) / a_dust**2)
gamma_ident = sp.simplify(m**2 * a_dust**2 * eta**2 - 4 * m**2 / H_dust**2) == 0
# tracking mass (m^2 ∝ H^2, CXB11's g^2 phi~^2): gamma constant
nu_tr = sp.sqrt(sp.Rational(9, 4) - gam)
tilt_tr = sp.series(tilt_from_nu(nu_tr), gam, 0, 2).removeO()          # = 2 gamma/3
tilt_tr_m = sp.simplify(tilt_tr.subs(gam, 4 * m**2 / H**2))          # = 8 m^2/(3 H^2)
# CXB11 internal check: Eq.18 n_chi = 2 m_chi^2/(3H^2); Eq.19 n_chi = g^2 m_pl^2/(2 pi m^2)
g, mpl, mm, t = sp.symbols('g m_pl m t', positive=True)
phit = mpl / (sp.sqrt(3 * sp.pi) * mm * t)                      # CXB11 Eq. 12
Hc = 2 / (3 * t)                                                 # CXB11 Eq. 10
mchi2_half = g**2 * phit**2 / 2                                  # Eq. 13 mass (with their 1/2)
mchi2_full = g**2 * phit**2
eq19 = g**2 * mpl**2 / (2 * sp.pi * mm**2)
OUT["A_massive_spectator_dust"] = {
    "gamma_identity_4m2_over_H2": bool(gamma_ident),
    "tilt_tracking_mass_of_gamma": str(tilt_tr),
    "tilt_tracking_mass": str(tilt_tr_m),
    "coefficient_ratio_contraction_over_deSitter": str(sp.simplify(tilt_tr_m / (2 * m**2 / (3 * H**2)))),
    "sign_positive_mass_squared": "blue (n_sigma - 1 > 0)",
    "CXB11_eq18_equals_deSitter_formula": True,
    "CXB11_eq18_to_eq19_with_half_mass": str(sp.simplify(sp.Rational(2, 3) * mchi2_half / Hc**2 / eq19)),
    "CXB11_eq18_to_eq19_with_full_mass": str(sp.simplify(sp.Rational(2, 3) * mchi2_full / Hc**2 / eq19)),
    "lane_8_3_to_eq19_with_half_mass": str(sp.simplify(sp.Rational(8, 3) * mchi2_half / Hc**2 / eq19)),
}
# ------------------------------------------- B. massive spectator: numeric tilt sign
# v'' + (k^2 + M2(eta) - 2/eta^2) v = 0, a = eta^2; adiabatic (WKB) vacuum at eta_i where the
# mode is deep sub-Hubble; P(k) = k^3 |v/a|^2 at eta_f.  M2 = m^2 eta^4 (constant mass) or
# M2 = gamma/eta^2 (tracking mass, exact Bessel -> validates the integrator against 2 gamma/3).
def power_at(kval, M2, eta_i=-300.0, eta_f=-0.02):
    def rhs(e, y):
        vr, vi, dr, di = y
        om2 = kval**2 + M2(e) - 2.0 / e**2
        return [dr, di, -om2 * vr, -om2 * vi]
    om_i = math.sqrt(kval**2 + M2(eta_i))
    dom_i = (math.sqrt(kval**2 + M2(eta_i + 1e-4)) - math.sqrt(kval**2 + M2(eta_i - 1e-4))) / 2e-4
    amp = 1 / math.sqrt(2 * om_i)                                     # v = e^{-i∫ω}/√(2ω), first-order WKB:
    y0 = [amp, 0.0, -dom_i / (2 * om_i) * amp, -om_i * amp]           # v' = (-iω - ω'/2ω) v
    sol = solve_ivp(rhs, [eta_i, eta_f], y0, rtol=1e-11, atol=1e-16, method="DOP853")
    vr, vi = sol.y[0, -1], sol.y[1, -1]
    return kval**3 * (vr**2 + vi**2) / eta_f**4

def numeric_tilt(M2, k1=0.2, k2=0.4):
    return math.log(power_at(k2, M2) / power_at(k1, M2)) / math.log(k2 / k1)

tilt0 = numeric_tilt(lambda e: 0.0)
track = [{"gamma": gv, "numeric_tilt": numeric_tilt(lambda e, gv=gv: gv / e**2), "exact_3_minus_2nu": 3 - 2 * math.sqrt(2.25 - gv)}
         for gv in [0.01, 0.03]]
rows = []
for mval in [3e-5, 1e-4, 2e-4, 3e-4]:
    Hk = {kk: kk**3 / 4 for kk in (0.2, 0.4)}                  # |H| at k = aH: eta=-2/k, H=2/eta^3
    rows.append({"m": mval, "m2_over_Hk2": {str(kk): (mval / h)**2 for kk, h in Hk.items()},
                 "m_over_H_at_eta_i": mval * 300.0**3 / 2, "nonadiabaticity_sqrt_m_over_8Hk": {str(kk): math.sqrt(mval / (8 * h)) for kk, h in Hk.items()},
                 "crossing_estimate_2over3_diff": 2 * ((mval / Hk[0.2])**2 - (mval / Hk[0.4])**2) / 3,
                 "numeric_tilt_minus_massless": numeric_tilt(lambda e, mv=mval: mv**2 * e**4) - tilt0})
OUT["B_massive_numeric"] = {
    "massless_numeric_tilt": tilt0, "tracking_mass_validation": track, "constant_mass_rows": rows,
    "sign_of_mass_induced_tilt": "positive (blue)" if all(r["numeric_tilt_minus_massless"] > 0 for r in rows) else "NOT uniformly positive",
    "noise_floor_from_tracking_validation": max(abs(tv["numeric_tilt"] - tv["exact_3_minus_2nu"]) for tv in track),
    "note": "constant m in a contraction: m/H ∝ |t| so the field is HEAVY in the far past (m ≫ H at eta_i) and light only "
            "near the bounce; the heavy->relativistic transition at eta_m = -sqrt(k/m) has non-adiabaticity sqrt(m/8H_k), "
            "k-dependent, so the initial state is not BD-light and the crossing-time argument does not fix the sign.",
}
# branch-W's step: they wrote n-1 = 2 nu - 3 (should be 3 - 2 nu) with nu = 3/2 - m^2/(3H^2)
nu_bw = sp.Rational(3, 2) - m**2 / (3 * H**2)
OUT["B_branchW_step"] = {
    "branchW_wrote": "n_sigma - 1 = 2 nu - 3 = -2 m^2/(3 H_k^2)",
    "correct": "n_sigma - 1 = 3 - 2 nu = " + str(sp.simplify(3 - 2 * nu_bw)),
    "erring_step": "03_tilt_mechanisms.md: 'n_sigma - 1 ≈ 2ν − 3' — P_v ∝ k^{3-2ν}, so the sign of the "
                   "tilt relation is inverted; the ν expansion itself (ν < 3/2 for m^2 > 0) is correct.",
}
# ----------------------------------------------------- D. two-channel r formula
# Same mode function v for zeta_ad (z = a sqrt(2 eps) M_pl), delta sigma (a) and each h pol (a M_pl/2):
# P_zeta,ad = P_v/(2 eps a^2 M^2); P_dsigma = P_v/a^2; P_h = 2 * 4 P_v/(a^2 M^2) = 8 P_v/(a^2 M^2)
Pv, M, rdec, sig = sp.symbols('P_v M_pl r_dec sigma_star', positive=True)
a_s = sp.symbols('a', positive=True)
P_ad = Pv / (2 * eps * a_s**2 * M**2)
P_ds = Pv / a_s**2
P_h = 8 * Pv / (a_s**2 * M**2)
P_curv = (rdec * sp.Rational(2, 3) / sig)**2 * P_ds        # zeta_curv = r_dec (2/3) dsigma/sigma_* (quadratic V)
ratio = sp.simplify(P_curv / P_ad)
r_expr = sp.simplify(P_h / (P_ad + P_curv))
r_single = sp.simplify(P_h / P_ad)
ratio_dust = ratio.subs(eps, sp.Rational(3, 2))
x = sp.symbols('x', positive=True)                          # x = r_dec M_pl/sigma_*
r_dust = 24 / (1 + sp.Rational(4, 3) * x**2)
thr = {str(rt): float(sp.solve(sp.Eq(r_dust, rt), x)[0]) for rt in (sp.Rational(36, 1000), sp.Rational(1, 100))}
OUT["D_r_formula"] = {
    "P_curv_over_P_ad": str(ratio), "P_curv_over_P_ad_dust": str(ratio_dust),
    "r_single_field": str(r_single), "r_two_channel": str(r_expr),
    "lane_form_matches_8eps_over_9": bool(sp.simplify(ratio - sp.Rational(8, 9) * eps * rdec**2 * M**2 / sig**2) == 0),
    "x_threshold_for_r_lt_0.036": thr["9/250"], "x_threshold_for_r_lt_0.01": thr["1/100"],
    "F_threshold_r_lt_0.036_row10_norm": math.sqrt(24 / 0.036), "F_threshold_r_lt_0.036_CXB11_35": math.sqrt(35 / 0.036),
    "assumptions": "sigma_* (the homogeneous curvaton value at conversion) is constant through contraction+bounce "
                   "and the same transfer multiplies dsigma and zeta_ad (both obey the massless operator); "
                   "curvaton is subdominant during the contraction; conversion after reheating (radiation era).",
}
# ------------------------------------ E. curvaton f_NL: delta-N sudden-decay derivation
# (1-Om) e^{4(z - z_r)} + Om e^{3(z - z_s)} = 1 with z_r = 0 (Gaussian radiation), z_s = (2/3) ds/s + (1/3)(ds/s)^2
z, ds, Om = sp.symbols('zeta delta_s Omega', positive=True)     # ds = delta sigma/sigma_*
zs = sp.log(1 + 2 * ds + ds**2) / 3                               # rho_s ∝ sigma^2 exactly (quadratic V)
F = (1 - Om) * sp.exp(-4 * z) + Om * sp.exp(3 * (zs - z)) - 1   # rho_r e^{4(z_r - z)} + rho_s e^{3(z_s - z)}
z1, z2 = sp.symbols('z1 z2')
Fser = sp.series(F.subs(z, z1 * ds + z2 * ds**2), ds, 0, 3).removeO()
sol = sp.solve([Fser.coeff(ds, 1), Fser.coeff(ds, 2)], [z1, z2], dict=True)[0]
rd_of_Om = 3 * Om / (4 - Om)                                      # r_dec = 3 rho_s/(3 rho_s + 4 rho_r)
fNL_dN = sp.simplify((sp.Rational(5, 3) * sol[z2] / sol[z1]**2).subs(Om, 4 * rdec / (3 + rdec)))
fNL_svw = 5 / (4 * rdec) - sp.Rational(5, 3) - 5 * rdec / 6
zero = [s0 for s0 in sp.solve(sp.Eq(fNL_svw, 0), rdec) if s0.is_positive]
def fnl(rv): return 5 / (4 * rv) - 5 / 3 - 5 * rv / 6
def rdec_at(fval):                                                # monotone decreasing
    lo, hi = 1e-4, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if fnl(mid) > fval else (lo, mid)
    return 0.5 * (lo + hi)
OUT["E_curvaton_fNL"] = {
    "deltaN_sudden_decay_fNL": str(fNL_dN), "svw_quadratic": str(fNL_svw),
    "deltaN_matches_SVW": bool(sp.simplify(fNL_dN - fNL_svw) == 0),
    "zero_crossing_r_dec": float(zero[0]), "zero_crossing_exact": str(zero[0]),
    "f_at_r_dec_1": fnl(1.0), "r_dec_min_Planck_2sigma(-0.9+2*5.1)": rdec_at(-0.9 + 2 * 5.1),
    "f_at_that_r_dec": fnl(rdec_at(-0.9 + 2 * 5.1)),
    "assumptions": "sudden decay; quadratic potential (g''=0: sigma at decay linear in sigma_*, unchanged by the bounce); "
                   "Gaussian delta sigma; radiation-dominated background at decay; no phi-sigma cross term N_{phi sigma}.",
}
# ---------------------------------------- F. dilution of the adiabatic bispectrum
# zeta = zeta_1 + zeta_2, independent Gaussian seeds; zeta_i = g_i + (3/5) f_i g_i^2.
# B = (6/5) sum_i f_i P_i(k1) P_i(k2) + perms; P = P_1 + P_2  =>  f_eff = sum_i f_i (P_i/P)^2
f1, f2, P1, P2 = sp.symbols('f1 f2 P1 P2', positive=True)
B = sp.Rational(6, 5) * (f1 * P1**2 + f2 * P2**2)          # equilateral-normalised, one perm
f_eff = sp.simplify(B / (sp.Rational(6, 5) * (P1 + P2)**2))
rr = sp.symbols('r', positive=True)
w_ad = sp.simplify(f_eff.subs({f2: 0, f1: 1, P1: rr / 24, P2: 1 - rr / 24}))   # P_ad/P_tot = r/24
FNL_B = -sp.Rational(35, 16)
T = {"pre-transfer (T=1)": 1.0, "LQC (T=0.250)": 0.250, "Quintin (T=0.165)": 0.165}
def r_min_spherex(Tv, sig_f=0.5):
    return 24 * math.sqrt(sig_f / (abs(float(FNL_B)) * Tv))
OUT["F_dilution"] = {
    "f_eff_two_channels": str(f_eff), "adiabatic_weight_of_r": str(w_ad),
    "weight_at_r_0.036": float(w_ad.subs(rr, 0.036)),
    "bounce_term_at_r_0.036": {kk: float(FNL_B) * Tv * float(w_ad.subs(rr, 0.036)) for kk, Tv in T.items()},
    "r_min_for_SPHEREx_1sigma_0.5": {kk: r_min_spherex(Tv) for kk, Tv in T.items()},
    "lane_22.95_corresponds_to": "T = 0.250 (LQC); T=1 gives 11.5, T=0.165 gives 28.2 (> 24, unreachable)",
    "assumptions": "no cross term N_{phi sigma}; the adiabatic f_NL is treated as a local amplitude "
                   "(its mu-dependence rides along with the same weight); transfer T from row-10/A2, not re-derived.",
}
# -------------------------------------------- A(ii). CXB11 Case-1 f_NL arithmetic
d, C, Fk, mpl2, m2 = sp.symbols('d C F m_pl m', positive=True)
dchi_f = m2 / (3 * sp.pi**2) * sp.sqrt(C) * Fk                                     # Eq. 55
dzeta = m2 / (6 * sp.sqrt(3 * sp.pi) * mpl2) * sp.sqrt(C) * Fk                    # Eq. 60
zeta_NL = 32 * m2 / (sp.pi * mpl2**3) * (1 - 8 * d**2 * C * mpl2 / (sp.pi**2 * m2)) * dchi_f**2   # Eq. 64
fNL_full = sp.simplify(sp.Rational(5, 3) * zeta_NL / dzeta**2)
fNL_lead = sp.simplify(fNL_full - 640 * m2 / (sp.pi**4 * mpl2))                     # drop the O(m/m_pl) piece
case1 = sp.simplify(fNL_lead.subs(C, (sp.pi / (4 * d))**2))
OUT["A_CXB11_case1"] = {
    "fNL_from_eqs_60_64": str(fNL_full), "leading_term": str(fNL_lead),
    "matches_eq65_minus5120_d2C_over_pi6": bool(sp.simplify(fNL_lead + 5120 * d**2 * C / sp.pi**6) == 0),
    "case1_symbolic": str(case1), "case1_value": float(case1), "CXB11_quote": -3.3,
    "subleading_dropped": "+640 m/(pi^4 m_pl) (positive, O(1e-2) for m ~ 1e-5 m_pl)",
    "parameter_free_condition": "C = (pi/4 d_1)^2 with d = d_1 (chi dominates first); d cancels exactly.",
    "not_rederived": "Eqs. 62-64 (the zeta_NL integral through deflation/bounce) are CXB11 estimates ('≃'); "
                     "the collapse to -320/pi^4 is arithmetic on THEIR equations, not an independent derivation.",
}
OUT["sympy_version"] = sp.__version__
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "curvaton_matter_bounce_adjudication_2026_09_04.json"), "w") as fh:
    json.dump(OUT, fh, indent=2, default=str)
print(json.dumps(OUT, indent=2, default=str))

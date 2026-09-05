#!/usr/bin/env python3
"""Ledger row 15 - the curvaton-type matter bounce: can it give r < 0.036 with
n_s ~ 0.965 and an O(1) local f_NL, and at what value/sign?

Every number in ROW15_CURVATON_2026-09-04.md comes from this script.  No tuning:
free parameters are scanned, never chosen to hit a target.

Route
  A. Symbolic: the light-spectator (curvaton) mode in a power-law contraction
     a ~ (-eta)^q, q = 2/(1+3w).  Same MS operator as the adiabatic variable
     when eps = const, so nu = q - 1/2 and n_sigma - 1 = 4 - 2q = 12w/(1+3w):
     the curvaton inherits EXACTLY the adiabatic tilt (row 10's anchor).
     A tracking mass m_chi^2 a^2 = gamma/eta^2 (CXB11's g^2 phi^2) shifts it.
  B. Power ratio and r: P_zeta,curv / P_zeta,ad = (8 eps / 9) r_dec^2 (Mpl/sigma_*)^2
     for a quadratic curvaton (zeta_sigma = (2/3) dsigma/sigma, LUW 2003),
     hence r = 16 eps / (1 + that) with 16 eps = 24 (row 10).
  C. f_NL: LUW/SVW local curvaton formula over r_dec, PLUS the dilution of the
     intrinsic matter-bounce -35/16 by the squared adiabatic power fraction.
  D. CXB11's own realisation: r ~ 24 F^-2 (their Eq. 61 in our normalisation)
     and the parameter-free Case-1 f_NL = -(5120/pi^6) d^2 C with C=(pi/4d)^2.

Refs: Cai, Xue & Brandenberger 2011 (1101.0822) Eqs. (18),(58),(61),(65),(66);
Lyth, Ungarelli & Wands 2003 (astro-ph/0208055); Sasaki, Valiviita & Wands 2006
(astro-ph/0607627); Li, Quintin, Wang & Cai 2016 (1612.02036) Eq. (4.19);
row 10 (r = 16 eps = 24, n_s-1 = 12w/(1+3w)); row 14 (c_s no-go, A2 transfers).
"""
import json, math, os, sys
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {"task": "NEXT_SCIENCE_LEDGER row 15 -- the curvaton-type matter bounce",
       "date": "2026-09-04"}

# ---------------------------------------------------------------- observables
PLANCK_FNL, PLANCK_SIG = -0.9, 5.1          # Planck 2018 local f_NL
R_CMB, R_TIGHT = 0.036, 0.01                # BICEP/Keck 2021; a tighter target
SPHEREX_SIG = 0.5                           # SPHEREx forecast sigma(f_NL^local)
NS_OBS = 0.9649
W_ANCHOR = -0.0029                          # row 10's Planck-anchored w branch
FNL_BOUNCE = sp.Rational(-35, 16)           # lab in-in, squeezed isoceles
# A2 bounce transfers, verbatim from row 14 results.json
T_A2 = {"poly": 0.1955011060855527, "LQC": 0.24999984088268537,
        "quintin": 0.16500538338212953}

# ------------------------------------------------------- A. symbolic spectrum
q, w, eta, k, gam, eps = sp.symbols('q w eta k gamma epsilon', positive=True)
nu = q - sp.Rational(1, 2)                       # a''/a = q(q-1)/eta^2
ns_minus_1 = sp.simplify(3 - 2 * nu)             # P ~ k^(3-2nu) = k^(4-2q)
q_of_w = 2 / (1 + 3 * w)
ns_w = sp.simplify(ns_minus_1.subs(q, q_of_w))
# massive tracking spectator: a''/a - m^2 a^2 = (q(q-1) - gamma)/eta^2
nu_m = sp.sqrt(sp.Rational(1, 4) + q * (q - 1) - gam)
dn_m = sp.simplify(sp.series(3 - 2 * nu_m.subs(q, 2), gam, 0, 2).removeO())
# dust: a ~ eta^2, aH = 2/eta, H^2 = 4/(a^2 eta^2)  =>  gamma = m^2 a^2 eta^2 = 4 m^2/H^2
mh = sp.symbols('m_over_H', positive=True)
dn_of_m = sp.simplify(dn_m.subs(gam, 4 * mh**2))
OUT["analytic"] = {
    "nu_of_q": "nu = q - 1/2 for the light spectator (same MS operator as the adiabatic mode)",
    "ns_minus_1_spectator_str": str(sp.simplify(ns_minus_1)),
    "ns_minus_1_of_w_str": str(ns_w),
    "spectator_tilt_equals_adiabatic_tilt": bool(sp.simplify(ns_w - 12 * w / (1 + 3 * w)) == 0),
    "dust_massless_exactly_scale_invariant": bool(sp.simplify(ns_minus_1.subs(q, 2)) == 0),
    "massive_shift_str": "n_sigma - 1 = " + str(dn_of_m) + "  (gamma = m^2 a^2 eta^2 = 4 m^2/H^2)",
    "massive_shift_coeff_over_m2H2": float(sp.simplify(dn_of_m / mh**2)),
    "CXB11_Eq18_coeff_over_m2H2": 2.0 / 3.0,
    "massive_shift_note": ("CXB11 Eq. (18) quotes 2 m^2/(3H^2), the de Sitter spectator value "
                           "(m^2 a^2 = m^2/(H^2 eta^2)); in a MATTER CONTRACTION a^2 eta^2 = 4/H^2, "
                           "so the same derivation gives 8 m^2/(3H^2), a factor 4 larger. "
                           "Sign is unchanged: m^2 > 0 is BLUE."),
}
OUT["analytic"]["ns_at_w_anchor"] = float(1 + ns_w.subs(w, W_ANCHOR))

# ------------------------------------------- B. power ratio, r, and the window
EPS_DUST = sp.Rational(3, 2)
R_SINGLE = float(16 * EPS_DUST)                            # = 24, row 10
rd, sig = sp.symbols('r_dec sigma_star', positive=True)
# zeta_curv = r_dec * (2/3) dsigma/sigma_*, P_dsigma = P_(adiabatic v-mode) since
# the spectator obeys the same equation; P_zeta,ad = P_dsigma/(2 eps Mpl^2).
ratio = sp.simplify((sp.Rational(2, 3) * rd / sig)**2 / (1 / (2 * eps)))
ratio_dust = sp.simplify(ratio.subs(eps, EPS_DUST))        # sigma_* in Mpl units
r_of = sp.simplify(16 * eps / (1 + ratio)).subs(eps, EPS_DUST)
OUT["power_ratio"] = {
    "P_curv_over_P_ad_str": str(ratio) + "   (sigma_star in Mpl)",
    "P_curv_over_P_ad_dust_str": str(ratio_dust),
    "r_of_rdec_sigma_str": str(r_of),
    "r_single_field_dust": R_SINGLE,
}
def sigma_max(r_target, r_dec):
    """largest sigma_*/Mpl (weakest curvaton) that still reaches r <= r_target"""
    need = R_SINGLE / r_target - 1.0
    return float(sp.sqrt(sp.Rational(4, 3)) * r_dec / math.sqrt(need))
def r_of_num(r_dec, sigma_star):
    return R_SINGLE / (1.0 + (4.0 / 3.0) * r_dec**2 / sigma_star**2)
OUT["power_ratio"]["F_needed_CXB_Eq61"] = {
    "r<0.036": math.sqrt(R_SINGLE / R_CMB), "r<0.01": math.sqrt(R_SINGLE / R_TIGHT)}

# ---------------------------------------------------------------- C. f_NL map
def fnl_curvaton(r_dec):                       # LUW 2003 / SVW 2006, quadratic
    return 5.0 / (4.0 * r_dec) - 5.0 / 3.0 - 5.0 * r_dec / 6.0
rdx = sp.symbols('r_d', positive=True)
fnl_sym = 5 / (4 * rdx) - sp.Rational(5, 3) - 5 * rdx / 6
sign_flip = [s for s in sp.solve(sp.Eq(fnl_sym, 0), rdx) if s.is_real and s > 0]
OUT["fnl"] = {
    "formula": "f_NL = 5/(4 r_dec) - 5/3 - 5 r_dec/6  (LUW03; SVW06 Eq. for a quadratic curvaton)",
    "f_NL_at_rdec_1": fnl_curvaton(1.0),
    "sign_change_r_dec": float(sign_flip[0]),
    "monotonic_decreasing_in_rdec": True,
    "min_over_rdec_in_0_1": fnl_curvaton(1.0),
    "non_quadratic_caveat": ("SVW06 add potential-shape terms proportional to sigma V'''/V'' etc.; "
                             "the values here are the exact-quadratic case, the standard quoted branch."),
}

# r_dec range allowed by Planck (2 sigma) and by |f_NL| <= 1 sigma
def rdec_min_for(fmax):
    lo, hi = 1e-4, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if fnl_curvaton(mid) > fmax: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)
OUT["fnl"]["rdec_min_Planck_2sigma"] = rdec_min_for(PLANCK_FNL + 2 * PLANCK_SIG)
OUT["fnl"]["rdec_min_Planck_1sigma"] = rdec_min_for(PLANCK_FNL + PLANCK_SIG)
OUT["fnl"]["Planck_window"] = [PLANCK_FNL - 2 * PLANCK_SIG, PLANCK_FNL + 2 * PLANCK_SIG]

# dilution of the intrinsic matter-bounce f_NL: two independent channels
# zeta = zeta_ad + zeta_curv  =>  f_NL^tot = sum_i f_NL^i (P_i/P_tot)^2
def dilution(r_val):                          # adiabatic power fraction = r/24
    return (r_val / R_SINGLE)**2
OUT["fnl"]["dilution_law"] = "f_NL^tot = f_NL^bounce (r/24)^2 + f_NL^curv (1 - r/24)^2"
OUT["fnl"]["f_NL_bounce_pre"] = float(FNL_BOUNCE)
OUT["fnl"]["f_NL_bounce_after_A2"] = {b: float(FNL_BOUNCE) * t for b, t in T_A2.items()}
OUT["fnl"]["bounce_term_at_r_0.036"] = {
    b: float(FNL_BOUNCE) * t * dilution(R_CMB) for b, t in T_A2.items()}
OUT["fnl"]["bounce_term_at_r_0.036_pre"] = float(FNL_BOUNCE) * dilution(R_CMB)
OUT["fnl"]["adiabatic_power_fraction_at_r_0.036"] = R_CMB / R_SINGLE

# CXB11's own realisation (their Eqs. 61, 65, 66)
d_s, C_s = sp.symbols('d C', positive=True)
fnl_cxb = sp.simplify((-5120 / sp.pi**6 * d_s**2 * C_s).subs(C_s, (sp.pi / (4 * d_s))**2))
OUT["cxb11"] = {
    "r_eq61_their_norm": "r ~ 35 F^-2 (their Eq. 61); in our row-10 normalisation r = 24 F^-2",
    "f_NL_case1_symbolic": str(fnl_cxb),
    "f_NL_case1_value": float(fnl_cxb),
    "f_NL_case1_paper_quote": -3.3,
    "f_NL_case1_is_parameter_free": True,
    "f_NL_case2": "f_NL ~ -5.3 m^4/(d^2 M^4) (their Eq. 67) -- one free combination",
    "sigma_vs_Planck_case1": abs(float(fnl_cxb) - PLANCK_FNL) / PLANCK_SIG,
    "sigma_detection_SPHEREx_case1": abs(float(fnl_cxb)) / SPHEREX_SIG,
}

# ------------------------------------------------------- viable-window table
rows = []
for r_dec in [0.05, 0.10, 0.1153, 0.20, 0.30, 0.50, 0.5811, 0.75, 1.00]:
    smax_cmb = sigma_max(R_CMB, r_dec)
    smax_tight = sigma_max(R_TIGHT, r_dec)
    f_curv = fnl_curvaton(r_dec)
    f_tot = f_curv * (1 - dilution(R_CMB)) + float(FNL_BOUNCE) * T_A2["LQC"] * dilution(R_CMB)
    rows.append({
        "r_dec": r_dec,
        "sigma_star_max_over_Mpl_for_r_0.036": smax_cmb,
        "sigma_star_max_over_Mpl_for_r_0.01": smax_tight,
        "r_at_that_sigma": r_of_num(r_dec, smax_cmb),
        "n_s": float(1 + ns_w.subs(w, W_ANCHOR)),
        "f_NL_curvaton": f_curv,
        "f_NL_total_at_r_0.036": f_tot,
        "sigma_vs_Planck": abs(f_tot - PLANCK_FNL) / PLANCK_SIG,
        "Planck_2sigma_ok": bool(abs(f_tot - PLANCK_FNL) <= 2 * PLANCK_SIG),
        "SPHEREx_detect_sigma": abs(f_tot) / SPHEREX_SIG,
    })
OUT["table"] = rows
OUT["viable"] = {
    "exists": any(r["Planck_2sigma_ok"] for r in rows),
    "r_dec_window_Planck_2sigma": [OUT["fnl"]["rdec_min_Planck_2sigma"], 1.0],
    "r_dec_window_Planck_1sigma": [OUT["fnl"]["rdec_min_Planck_1sigma"], 1.0],
    "f_NL_range_over_window_2sigma": [fnl_curvaton(1.0),
                                      fnl_curvaton(OUT["fnl"]["rdec_min_Planck_2sigma"])],
    "n_s": float(1 + ns_w.subs(w, W_ANCHOR)),
    "r_free": "r = 24/(1 + (4/3) r_dec^2 (Mpl/sigma_*)^2): any r <= 24 by choosing sigma_*",
}
# what the bounce channel would need to stay observable
OUT["observability"] = {
    "r_max_for_bounce_term_above_SPHEREx_0.5": float(R_SINGLE * math.sqrt(
        SPHEREX_SIG / (abs(float(FNL_BOUNCE)) * T_A2["LQC"]))),
    "note": "solve |f_NL^bounce| T (r/24)^2 = 0.5 for r",
}

# ------------------------------------------- D. transmission of the spectator
# The massless spectator u = a*sigma obeys u'' + (k^2 - a''/a)u = 0 -- the SAME
# ODE the A2 module integrates (its rhs uses w = a''/a), and the same ODE the
# tensor mode obeys.  So T_sigma == T_h identically; row 10 measured
# T_h/T_zeta - 1 <= 8e-5 and row 14 lambda_scalar/lambda_tensor - 1 <= 4e-11.
# Numerical check here: the constant (frozen) super-Hubble branch of sigma
# passes the bounce with T_c = 1 on all three A2 backgrounds.
sys.path.insert(0, os.path.join(HERE, "..", "..", "cubic_bounce_transmission"))
trans = {}
try:
    import a2_transmission_linear as A2
    for name, ctor in (("poly", A2.bg_poly), ("LQC", A2.bg_lqc), ("quintin", A2.bg_quintin)):
        bg = ctor()
        kk = 0.01 / bg["eta_B"]
        scan = {}
        for u_out in (0.2, 0.1, 0.05, 0.02):
            tc = A2.constant_branch_transmission(bg, kk, u_out=u_out)
            if tc:
                scan[str(u_out)] = {"T_c": tc["T_c"], "abs_T_c_minus_1": tc["abs_T_c_minus_1"]}
        trans[name] = {"eta_B": float(bg["eta_B"]), "k": float(kk),
                       "T_c_sigma_frozen_branch_vs_u_out": scan}
except Exception as exc:                                            # pragma: no cover
    trans["error"] = repr(exc)
OUT["transmission"] = {
    "spectator_ODE": "u'' + (k^2 - a''/a) u = 0  with u = a*sigma (m << H)",
    "identical_to_tensor_ODE": True,
    "identical_to_adiabatic_ODE_at_cs1": "yes when eps = const (z ~ a), which holds for dust",
    "frozen_branch_check": trans,
    "row10_T_h_over_T_zeta_minus_1_max": 8e-5,
    "row14_lambda_scalar_over_tensor_minus_1_max": 4.123168473313399e-11,
    "delta_fNL_bounce_applies_to_curvaton": False,
    "delta_fNL_note": ("The curvaton's local f_NL is generated at curvaton DECAY, after the "
                       "bounce, from a Gaussian sigma; the A2 transfer T = 0.165-0.250 acts on "
                       "the pre-bounce adiabatic bispectrum only.  In CXB11's variant the "
                       "conversion happens AT the bounce and their Eq. (65) already contains it."),
}

# ------------------------------------------------------- E. multi-channel map
OUT["multichannel"] = {
    "tensor_PTA": ("r is now free; the nHz first-order tensor amplitude scales with r, so at "
                   "r <= 0.036 Omega_GW h^2 <= 1.7e-14 * (0.036/24) = 2.5e-17 -- the PTA null "
                   "(row 10: 10^5.3 below NANOGrav) becomes STRONGER, not weaker."),
    "Omega_GW_h2_nHz_at_r_0.036": 1.69e-14 * (R_CMB / R_SINGLE),
    "PBH": "unchanged: set by the scalar amplitude at small scales, which the curvaton does not tilt.",
    "fNL_channel": ("the observable f_NL becomes PURELY LOCAL and set by r_dec; the bounce's "
                    "orientation-dependent shape f(mu) = -35/16 + (15/16) mu^2 is diluted by "
                    "(r/24)^2 and is unobservable."),
    "SPHEREx_reach_on_curvaton_fNL": {str(r["r_dec"]): r["SPHEREx_detect_sigma"] for r in rows},
}

# ------------------------------------------------------------------- outputs
grid = np.linspace(0.02, 1.0, 500)
fc = np.array([fnl_curvaton(x) for x in grid])
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    ax[0].plot(grid, fc, lw=2, color="C0")
    ax[0].axhspan(PLANCK_FNL - 2 * PLANCK_SIG, PLANCK_FNL + 2 * PLANCK_SIG,
                  color="0.85", label=r"Planck $2\sigma$")
    ax[0].axhspan(-SPHEREX_SIG, SPHEREX_SIG, color="C1", alpha=.25, label=r"SPHEREx $1\sigma$")
    ax[0].axhline(0, color="k", lw=.6)
    ax[0].axvline(OUT["fnl"]["rdec_min_Planck_2sigma"], ls="--", color="C3",
                  label=r"$r_{\rm dec}^{\min}$")
    ax[0].plot([1.0], [fnl_curvaton(1.0)], "o", color="C3")
    ax[0].plot([1.0], [OUT["cxb11"]["f_NL_case1_value"]], "s", color="C2",
               label=r"CXB11 Case 1 $-320/\pi^4$")
    ax[0].set_xlabel(r"$r_{\rm dec}$"); ax[0].set_ylabel(r"$f_{\rm NL}^{\rm local}$")
    ax[0].set_ylim(-8, 25); ax[0].legend(fontsize=7); ax[0].set_title("curvaton local $f_{NL}$")
    sg = np.logspace(-3, 0, 400)
    for rdv, cc in ((1.0, "C0"), (0.3, "C1"), (0.1, "C2")):
        ax[1].loglog(sg, [r_of_num(rdv, s) for s in sg], color=cc, label=rf"$r_{{\rm dec}}={rdv}$")
    ax[1].axhline(R_SINGLE, color="k", ls=":", label="single field $r=24$")
    ax[1].axhline(R_CMB, color="C3", ls="--", label="BICEP/Keck 0.036")
    ax[1].set_xlabel(r"$\sigma_*/M_{\rm pl}$"); ax[1].set_ylabel("$r$")
    ax[1].legend(fontsize=7); ax[1].set_title("tensor-to-scalar ratio")
    fig.suptitle("Row 15 - curvaton-type matter bounce", fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "row15_curvaton.png"), dpi=140)
except Exception as exc:                                            # pragma: no cover
    OUT["plot_error"] = repr(exc)

with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(OUT, fh, indent=2, sort_keys=False, default=str)
lines = ["ROW 15 - curvaton-type matter bounce", "=" * 60,
         f"spectator tilt n_s-1 = {OUT['analytic']['ns_minus_1_of_w_str']} (== adiabatic): "
         f"n_s = {OUT['analytic']['ns_at_w_anchor']:.4f} at w = {W_ANCHOR}",
         f"massive shift: {OUT['analytic']['massive_shift_str']} (BLUE for m^2>0)",
         f"r = {OUT['power_ratio']['r_of_rdec_sigma_str']}",
         f"F needed (CXB Eq.61): {OUT['power_ratio']['F_needed_CXB_Eq61']}",
         f"f_NL(r_dec=1) = {OUT['fnl']['f_NL_at_rdec_1']:.4f}; sign flip at r_dec = "
         f"{OUT['fnl']['sign_change_r_dec']:.4f}; r_dec_min(Planck 2s) = "
         f"{OUT['fnl']['rdec_min_Planck_2sigma']:.4f}",
         f"bounce term at r=0.036: {OUT['fnl']['bounce_term_at_r_0.036']}",
         f"CXB11 Case 1 f_NL = {OUT['cxb11']['f_NL_case1_value']:.4f} "
         f"({OUT['cxb11']['sigma_detection_SPHEREx_case1']:.1f} sigma for SPHEREx)",
         f"r_max keeping bounce f_NL above SPHEREx: "
         f"{OUT['observability']['r_max_for_bounce_term_above_SPHEREx_0.5']:.3f}",
         "-" * 60]
for r in rows:
    lines.append(f"r_dec={r['r_dec']:.4f}  sig*max(r<0.036)={r['sigma_star_max_over_Mpl_for_r_0.036']:.4f} "
                 f"n_s={r['n_s']:.4f}  f_NL_curv={r['f_NL_curvaton']:+.3f}  "
                 f"f_NL_tot={r['f_NL_total_at_r_0.036']:+.3f}  Planck2s={r['Planck_2sigma_ok']}")
lines.append(f"transmission: {json.dumps(OUT['transmission']['frozen_branch_check'], default=str)}")
open(os.path.join(HERE, "row15_curvaton.log"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))

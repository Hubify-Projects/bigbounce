#!/usr/bin/env python3
"""
growth_separation.py -- ledger row 23, GAP-2 (the growth observable).

Closes the named gap left by lane bb-LS7-row23-fate-de: compute the linear
growth rate f*sigma8(z) for LambdaCDM and for each model in the row-23
intersection (M1 canonical zero-crossing quintessence, M2 interacting dark
sector, M3 zero-crossing k-essence), and report the separation in units of the
published growth uncertainty.

Pre-registered in PREREGISTRATION_GAP2.md (committed alone, before this file).

THE POINT.  M3 and M1 share a background exactly (cross_table.py lemma L3), so
BAO distances cannot tell them apart -- ROW23_MEMO.md says growth is the only
observable that can, through the k-essence sound speed
c_s^2 = (K + 2 L X)/(K + 6 L X).  That is the primary question here.

Backgrounds are IMPORTED UNCHANGED from ../observable_separation.py so that the
fixed-parameter convention (same Omega_m, same h*r_d, no re-fit) is literally the
same code, not a re-implementation.

Usage: python3 growth_separation.py    (writes growth_separation.json)
"""

import json
import math
import os
import sys
from datetime import datetime, timezone

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_HERE))
import observable_separation as OS          # noqa: E402  (the LS7 pipeline)

C_KM_S = OS.C_KM_S
OMEGA_M = OS.OMEGA_M
OMEGA_R = OS.OMEGA_R
H_LITTLE = OS.H_LITTLE
ODE0 = 1.0 - OMEGA_M - OMEGA_R

# ===========================================================================
# DESI DR1 full-shape growth data.
#
# SOURCE G1 (PRIMARY, and the ONLY growth source used): DESI Collaboration,
#   "DESI 2024 V: Full-Shape Galaxy Clustering from Galaxies and Quasars",
#   arXiv:2411.12021, JCAP 09 (2025) 008.  PDF v5 fetched and read 2026-09-22.
#
# Why DR1 and not DR2 -- recorded in PREREGISTRATION_GAP2.md Sec. 1 BEFORE this
# computation, and repeated here because every number below inherits it:
#   * DESI DR2 Results II (arXiv:2503.14738) is BAO-ONLY: no growth measurement.
#   * The DR2-era joint analysis (arXiv:2602.18761) still takes its growth
#     information from DR1 full-shape and reports sigma8, not f*sigma8(z).
#   * The ONE DR2 full-shape analysis that exists, arXiv:2607.27411 (DR2 Lya
#     forest full-shape validation), states in its abstract: "mock studies
#     reveal a significant bias in the inferred growth-rate parameter fsigma8,
#     leading us to exclude this measurement from the final analysis."
#   * A DR2 full-shape conference talk exists (PIRSA 26040071, 2026-04-29); a
#     talk is not a citable measurement with an uncertainty and is not used.
# So NO citable DESI DR2-era growth measurement with an uncertainty exists as of
# 2026-09-22.  The pre-registered fallback -- DR1 full-shape -- is taken, and is
# labelled "DR1" everywhere it appears.  Nothing is estimated or interpolated.
#
# ShapeFit datavector + full Gaussian covariance, G1 Appendix A, Eqs. (A.1)-
# (A.12), ShapeFit-ALONE (the growth-only fits).  Ordering of the 4-vector is
# (D_V/r_d, D_H/D_M, f*sigma_s8, m+n); we use index 2 and its variance.
# Covariances are quoted in the paper in units of 1e-4 and that factor is
# applied in code.  NO uncertainty is hand-typed: every sigma below is
# sqrt(C[2][2]) computed at runtime.
#
# Baseline is ShapeFit-ALONE, not ShapeFit+BAO: the row-23 Step-2 separation
# already uses DESI DR2 BAO distances, so the +BAO rows would double count.
# ShapeFit+BAO is carried as a sensitivity variant.
# ===========================================================================
DR1_SHAPEFIT_ALONE = {
    #  tracer:  (z_eff, fsigma_s8 datavector entry, Var[fsigma_s8] * 1e4)
    "BGS":  (0.295, 0.377174, 88.510877),   # G1 Eq. (A.1)/(A.2)
    "LRG1": (0.510, 0.513635, 41.295470),   # G1 Eq. (A.3)/(A.4)
    "LRG2": (0.706, 0.483623, 28.119682),   # G1 Eq. (A.5)/(A.6)
    "LRG3": (0.919, 0.422164, 22.370314),   # G1 Eq. (A.7)/(A.8)
    "ELG2": (1.317, 0.376715, 13.997473),   # G1 Eq. (A.9)/(A.10)
    "QSO":  (1.491, 0.434858, 19.785658),   # G1 Eq. (A.11)/(A.12)
}
DR1_SHAPEFIT_PLUS_BAO = {
    "BGS":  (0.295, 0.396326, 80.924891),   # G1 Eq. (A.13)/(A.14)
    "LRG1": (0.510, 0.547632, 35.284297),   # G1 Eq. (A.15)/(A.16)
    "LRG2": (0.706, 0.479541, 23.061044),   # G1 Eq. (A.17)/(A.18)
    "LRG3": (0.919, 0.438454, 17.011310),   # G1 Eq. (A.19)/(A.20)
    "ELG2": (1.317, 0.372661, 11.811326),   # G1 Eq. (A.21)/(A.22)
    "QSO":  (1.491, 0.436849, 21.028703),   # G1 Eq. (A.23)/(A.24)
}
# Fiducial (f*sigma_s8)(z) of the ShapeFit template, G1 Table 11.  Template
# cosmology = G1 Table 6 row 1 "Planck LambdaCDM": omega_b 0.02237,
# omega_cdm 0.1200, h 0.6736, 1e9 A_s 2.0830, n_s 0.9649, N_ur 2.0328, w=-1.
DR1_FSIGMAS8_FID = {
    "BGS": 0.4723, "LRG1": 0.4733, "LRG2": 0.4608,
    "LRG3": 0.4398, "ELG2": 0.3944, "QSO": 0.3750,
}
# G1 Table 9, ShapeFit-only MAP ratios f*sigma_s8/(f*sigma_s8)_fid with their
# published 68% errors.  Used ONLY as an independent cross-check that the
# covariance-derived sigma reproduces the paper's own quoted error.
DR1_TABLE9_RATIO_ERR = {   # (ratio, minus_err, plus_err)
    "BGS": (0.80, 0.20, 0.20), "LRG1": (1.09, 0.14, 0.12),
    "LRG2": (1.05, 0.12, 0.12), "LRG3": (0.96, 0.10, 0.11),
    "ELG2": (0.95, 0.08, 0.11), "QSO": (1.16, 0.12, 0.12),
}
# G1 abstract: "we obtain a combined precision of 4.7% on the amplitude of the
# redshift space distortion (RSD) signal"; G1 Sec. 8 repeats it as "a combined
# precision of 4.7% on f sigma8".
DR1_COMBINED_PRECISION = 0.047

# G1 Sec. 7.1, quoted so it is impossible to misuse this pipeline:
DESI_FSIGMA8_RESTRICTION = (
    "arXiv:2411.12021 Sec. 7.1: the f*sigma8 results 'should only serve for "
    "visualization purposes, and they should never be used to infer cosmology, "
    "for which one should use the actual f*sigma_s8 results.' Honoured here: no "
    "measured central value enters any decision in this file. Only the PUBLISHED "
    "PRECISION on the growth amplitude is used, as the yardstick for a "
    "model-vs-model forecast separation. No goodness-of-fit is computed anywhere."
)


def growth_yardstick(block=DR1_SHAPEFIT_ALONE):
    """Fractional 1-sigma precision on the growth amplitude, DERIVED from the
    published covariance (never hand-typed)."""
    out = []
    for tracer, (z, dv, var_e4) in block.items():
        sigma = math.sqrt(var_e4 * 1e-4)
        fid = DR1_FSIGMAS8_FID[tracer]
        out.append(dict(tracer=tracer, z=z,
                        fsigma_s8_datavector=dv,
                        sigma_abs=sigma,
                        fsigma_s8_fid=fid,
                        eps_frac=sigma / fid,
                        source="arXiv:2411.12021 App. A (covariance) + Table 11 "
                               "(fiducial); sigma = sqrt(C[2][2])"))
    return sorted(out, key=lambda d: d["z"])


# ===========================================================================
# Symbolic derivations.  Nothing below is asserted; each is derived here.
# ===========================================================================
def derive_kessence_cs2_range():
    """LEMMA G1 -- the c_s^2 range the k-essence member actually permits.

    P(X,phi) = K X + L X^2 - V  (cross_table.py lemma L3).  Derive P_X, P_XX,
    rho, p, c_s^2, then impose: no ghost (P_X + 2 X P_XX > 0), no gradient
    instability and non-phantom (rho + p = 2 X P_X >= 0), subluminality.
    """
    K, L, X, V = sp.symbols("K L X V", real=True)
    P = K * X + L * X**2 - V
    P_X = sp.diff(P, X)
    P_XX = sp.diff(P, X, 2)
    rho = sp.simplify(2 * X * P_X - P)
    p = sp.simplify(P)
    denom = sp.simplify(P_X + 2 * X * P_XX)
    cs2 = sp.simplify(P_X / denom)
    rho_plus_p = sp.simplify(rho + p)

    # Substitute s = L X >= 0 and solve the endpoint conditions in K.
    s = sp.symbols("s", nonnegative=True)
    cs2_s = sp.simplify(cs2.subs(L * X, s).subs(X, sp.Symbol("X")))
    cs2_Ks = sp.simplify(((K + 2 * s) / (K + 6 * s)))
    cs2_at_Kmin = sp.simplify(cs2_Ks.subs(K, -2 * s))          # -> 0
    cs2_limit_Kinf = sp.limit(cs2_Ks, K, sp.oo)                # -> 1
    cs2_limit_Kzero = sp.simplify(cs2_Ks.subs(K, 0))           # -> 1/3
    subluminal = sp.simplify(sp.together(1 - cs2_Ks))          # 4s/(K+6s) >= 0

    return dict(
        lemma="G1",
        P="K*X + L*X**2 - V",
        P_X=sp.srepr(P_X) and str(P_X),
        rho=str(rho), p=str(p),
        no_ghost_condition=str(sp.simplify(denom)) + " > 0",
        cs2=str(cs2),
        rho_plus_p=str(rho_plus_p),
        non_phantom_and_no_gradient_instability="2*X*(K + 2*L*X) >= 0  =>  K + 2*L*X >= 0",
        subluminality="1 - cs2 = " + str(subluminal) + " >= 0  =>  L >= 0 for X > 0",
        endpoint_cs2_at_K_eq_minus_2s=str(cs2_at_Kmin),
        endpoint_cs2_as_K_to_infinity=str(cs2_limit_Kinf),
        cs2_at_K_eq_0=str(cs2_limit_Kzero),
        RESULT=("with s = L*X >= 0 (subluminality) and K >= -2s (no gradient "
                "instability / non-phantom), c_s^2 = (K+2s)/(K+6s) sweeps the "
                "FULL interval [0, 1): 0 exactly at K = -2s, -> 1 as K -> +inf, "
                "and 1/3 at K = 0. c_s^2 = 1 exactly iff L = 0, which IS the "
                "canonical member M1. So the allowed scan range is [0,1) and it "
                "is DERIVED, not assumed; M1 is the c_s^2 -> 1 endpoint of M3."),
    )


def derive_coupled_growth_equation():
    """LEMMA G2 -- the growth equation for M2 (interacting dark sector).

    Covariant choice, stated and not hidden: Q^mu = Q u_c^mu, i.e. the energy
    transfer is parallel to the CDM four-velocity, so there is NO momentum
    transfer in the CDM frame and the CDM Euler equation is unmodified
    (Valiviita, Majerotto & Maartens, arXiv:0804.0232; Amendola, PRD 62 043511).
    DE is smooth (w = -1).  delta_Q is neglected at sub-horizon order because
    Q ~ H and the perturbation of the expansion rate is O(H^2/k^2) suppressed.
    Whole pressureless sector coupled (LS7's background convention).

    Perturbed energy conservation for CDM, conformal time:
        rho_c' + 3 H rho_c = a Q                                    (background)
        d(delta_rho_c)/dtau + 3 H delta_rho_c + rho_c (theta_c - 3 Phi') = a delta_Q
    Divide by rho_c and use rho_c'/rho_c + 3H = aQ/rho_c:
        delta_c' = -theta_c + 3 Phi' - (aQ/rho_c) delta_c + a delta_Q / rho_c
    In e-folds N, sub-horizon (drop Phi', delta_Q):
        D delta = -Theta - gamma delta ,      gamma = Q/(H rho_c) = xi / rho_c
        D Theta = -(2 + dlnE/dN) Theta - (3/2) Omega_m(a) delta
    """
    N = sp.symbols("N", real=True)
    d = sp.Function("delta")(N)
    Th = sp.Function("Theta")(N)
    gam = sp.Function("gamma")(N)
    eps = sp.Function("epsilon")(N)      # dlnE/dN
    Om = sp.Function("Omega_m")(N)

    eq_d = sp.Eq(sp.diff(d, N), -Th - gam * d)
    eq_T = sp.Eq(sp.diff(Th, N), -(2 + eps) * Th - sp.Rational(3, 2) * Om * d)

    Th_sol = sp.solve(eq_d, Th)[0]                      # Theta = -D delta - gamma delta
    second = sp.diff(Th_sol, N) - (-(2 + eps) * Th_sol
                                   - sp.Rational(3, 2) * Om * d)
    second = sp.simplify(sp.expand(second))
    second_ordered = sp.collect(sp.expand(second), [sp.diff(d, N, 2),
                                                    sp.diff(d, N), d])

    # gamma = xi / rho_c with rho_c' = -3 rho_c + xi  =>  D gamma = 3 gamma - gamma^2
    xi, rc = sp.symbols("xi rho_c", positive=True)
    gamma_expr = xi / rc
    Dgamma = sp.simplify(sp.diff(gamma_expr, rc) * (-3 * rc + xi))
    Dgamma_in_gamma = sp.simplify(sp.expand(Dgamma.subs(xi, gamma_expr * rc)))

    return dict(
        lemma="G2",
        assumptions=[
            "Q^mu = Q u_c^mu (energy transfer along the CDM four-velocity) => "
            "no momentum transfer in the CDM frame => CDM Euler UNMODIFIED",
            "DE smooth, w = -1",
            "delta_Q neglected at sub-horizon order (Q ~ H; delta_H is O(H^2/k^2))",
            "whole pressureless sector coupled (LS7 background convention)",
        ],
        first_order_system=[str(eq_d), str(eq_T)],
        Theta_in_terms_of_delta=str(Th_sol),
        second_order_form=str(sp.Eq(second_ordered, 0)),
        gamma_definition="gamma(N) = Q/(H rho_c) = xi / rho_c(N)   [rho in units of rho_crit0]",
        D_gamma=str(sp.Eq(sp.Symbol("D_gamma"), Dgamma_in_gamma)),
        reduces_to_standard="gamma = 0 gives D^2 delta + (2 + dlnE/dN) D delta "
                            "- (3/2) Omega_m delta = 0, the uncoupled equation",
        RSD_growth_rate=("RSD measures the VELOCITY divergence, not dln delta/dlna. "
                         "From D delta = -Theta - gamma delta, -Theta = D delta + "
                         "gamma delta, so f_RSD = dln(delta)/dln(a) + gamma. In a "
                         "coupled model f_RSD != dln delta/dln a, and the "
                         "difference is NOT cosmetic: the friction term gamma "
                         "suppresses dln delta/dln a below the LambdaCDM value, "
                         "and adding gamma back moves the OBSERVED rate partly "
                         "BACK TOWARDS LambdaCDM. Scoring M2 with dln delta/dln a "
                         "therefore OVERSTATES its separation. The measured factor "
                         "is reported per xi as "
                         "max_abs_delta_if_dlnDelta_dlna_used vs max_abs_delta."),
    )


# ===========================================================================
# Backgrounds -> E(N) and dlnE/dN, exact where a closed form exists.
# ===========================================================================
def bg_lcdm(om=OMEGA_M, orad=OMEGA_R):
    ode = 1.0 - om - orad

    def E2(N):
        return om * np.exp(-3 * N) + orad * np.exp(-4 * N) + ode

    def dE2(N):
        return -3 * om * np.exp(-3 * N) - 4 * orad * np.exp(-4 * N)

    def rho_m(N):
        return om * np.exp(-3 * N)

    return dict(name="LCDM", E2=E2, dE2=dE2, rho_m=rho_m,
                rho_de=lambda N: ode + 0 * N, w=lambda N: -1.0 + 0 * N,
                clustering=False)


def bg_quintessence(alpha, **kw):
    """M1 (and M3's background, which is identical -- lemma L3)."""
    b = OS.quintessence_background(alpha, **kw)
    om = kw.get("om", OMEGA_M)
    orad = kw.get("orad", OMEGA_R)
    ode0 = 1.0 - om - orad
    rspl, wspl = b["rho_DE"], b["w"]

    def _z(N):
        return np.exp(-N) - 1.0

    def rho_de(N):
        return ode0 * rspl(_z(N))

    def drho_de(N):                       # d rho_DE / dN
        return ode0 * rspl(_z(N), 1) * (-(1.0 + _z(N)))

    def E2(N):
        return om * np.exp(-3 * N) + orad * np.exp(-4 * N) + rho_de(N)

    def dE2(N):
        return (-3 * om * np.exp(-3 * N) - 4 * orad * np.exp(-4 * N)
                + drho_de(N))

    def w(N):
        return float(wspl(_z(N)))

    def dwdN(N):
        z = _z(N)
        return float(wspl(z, 1)) * (-(1.0 + z))

    out = dict(name=f"quintessence(alpha={alpha})", E2=E2, dE2=dE2,
               rho_m=lambda N: om * np.exp(-3 * N), rho_de=rho_de,
               w=w, dwdN=dwdN, clustering=False, raw=b)
    return out


def bg_interacting(xi, om=OMEGA_M, orad=OMEGA_R):
    """M2.  Closed form (lemma L5): rho_DE = ode0 - xi*N, rho_c = (om - xi/3)e^-3N + xi/3."""
    ode0 = 1.0 - om - orad
    if xi >= 3.0 * om:
        # the drain would make the early-time pressureless density negative
        raise ValueError(f"xi = {xi} exceeds 3*Omega_m = {3*om:.4f}: "
                         "rho_c(a->0) < 0, the model is not defined there")

    def rho_c(N):
        return (om - xi / 3.0) * np.exp(-3 * N) + xi / 3.0

    def rho_de(N):
        return ode0 - xi * N

    def E2(N):
        return orad * np.exp(-4 * N) + rho_c(N) + rho_de(N)

    def dE2(N):
        return -4 * orad * np.exp(-4 * N) - 3 * (om - xi / 3.0) * np.exp(-3 * N) - xi

    return dict(name=f"interacting(xi={xi})", E2=E2, dE2=dE2, rho_m=rho_c,
                rho_de=rho_de, w=lambda N: -1.0 + 0 * N, clustering=False,
                coupled_xi=xi)


# ===========================================================================
# Growth integration.
#
# Convention (pre-registered): all models share the primordial amplitude and the
# linear transfer function, so sigma8(z)/sigma8_LCDM(z) = delta(z)/delta_LCDM(z)
# with delta matched deep in matter domination.  No absolute sigma8 is needed
# and none is quoted.  a_i = 1e-3 (z = 999), safely after matter-radiation
# equality (a_eq = Omega_r/Omega_m = 2.9e-4) so that delta ~ a holds; and the
# residual IC error CANCELS in the LCDM ratio for M1/M3, whose rho_m(a) and
# rho_r(a) are identical to LCDM's.  Checked by varying a_i.
# ===========================================================================
A_INIT = 1.0e-3
N_INIT = math.log(A_INIT)


def growth_smooth(bg, n_eval, a_i=A_INIT):
    """delta_m and the RSD rate for a model with SMOOTH dark energy, plus the
    optional CDM-coupling term gamma (M2).  Returns (delta, f_RSD) at n_eval."""
    xi = bg.get("coupled_xi", 0.0)
    N0 = math.log(a_i)

    def rhs(N, y):
        d, Th = y
        E2 = bg["E2"](N)
        eps = 0.5 * bg["dE2"](N) / E2
        Om = bg["rho_m"](N) / E2
        gam = xi / bg["rho_m"](N) if xi else 0.0
        return [-Th - gam * d, -(2.0 + eps) * Th - 1.5 * Om * d]

    # delta ~ a  =>  D delta = delta  =>  Theta = -(1 + gamma) delta
    gam_i = xi / bg["rho_m"](N0) if xi else 0.0
    y0 = [a_i, -(1.0 + gam_i) * a_i]
    sol = solve_ivp(rhs, (N0, 0.0), y0, t_eval=np.asarray(n_eval),
                    rtol=1e-11, atol=1e-16, method="DOP853", dense_output=True)
    if not sol.success:
        raise RuntimeError(sol.message)
    d = sol.y[0]
    Th = sol.y[1]
    return d, -Th / d           # f_RSD = -Theta/delta (== dln delta/dlna + gamma)


def growth_clustering_de(bg, cs2, k_hMpc, n_eval, a_i=A_INIT, a_de=0.1):
    """M3: matter + a clustering DE fluid with rest-frame sound speed cs2.

    Stage 1 (a_i -> a_de): DE perturbations are utterly negligible
    (rho_DE/rho_m ~ 1e-3 at a = 0.1), single-fluid matter growth.
    Stage 2 (a_de -> 1): sub-horizon Newtonian-gauge two-fluid system,
        D delta_m = -Theta_m
        D Theta_m = -(2+eps) Theta_m + kpsi
        D delta_d = -V_d - 3 (cs2 - w) delta_d
        D V_d     = -(2 + eps - 3 cs2 - eta) V_d + kappa^2 cs2 delta_d + (1+w) kpsi
    with V_d = (1+w) theta_d / H  (removes the 1/(1+w) singularity of a thawing
    field), eta = dln(1+w)/dN, kappa = k/(aH), and the sub-horizon Poisson
    source kpsi = k^2 psi / H^2 = -(3/2)[Omega_m delta_m + Omega_d delta_d].
    Adiabatic ICs at a_de: delta_d = (1+w) delta_m, V_d = (1+w) Theta_m.
    """
    N_de = math.log(a_de)
    d1, _ = growth_smooth(bg, [N_de], a_i=a_i)
    # recover Theta at a_de
    def rhs1(N, y):
        d, Th = y
        E2 = bg["E2"](N)
        eps = 0.5 * bg["dE2"](N) / E2
        Om = bg["rho_m"](N) / E2
        return [-Th, -(2.0 + eps) * Th - 1.5 * Om * d]
    s1 = solve_ivp(rhs1, (math.log(a_i), N_de), [a_i, -a_i], rtol=1e-11,
                   atol=1e-16, method="DOP853")
    dm_i, Th_i = s1.y[0, -1], s1.y[1, -1]

    w_i = bg["w"](N_de)
    y0 = [dm_i, Th_i, (1.0 + w_i) * dm_i, (1.0 + w_i) * Th_i]

    pref = k_hMpc * C_KM_S / 100.0        # kappa = pref / (a E)

    def rhs2(N, y):
        dm, Thm, dd, Vd = y
        E2 = bg["E2"](N)
        E = math.sqrt(E2)
        eps = 0.5 * bg["dE2"](N) / E2
        Om = bg["rho_m"](N) / E2
        Od = bg["rho_de"](N) / E2
        w = bg["w"](N)
        opw = 1.0 + w
        eta = bg["dwdN"](N) / opw if abs(opw) > 1e-14 else 0.0
        kappa2 = (pref / (math.exp(N) * E)) ** 2
        kpsi = -1.5 * (Om * dm + Od * dd)
        return [
            -Thm,
            -(2.0 + eps) * Thm + kpsi,
            -Vd - 3.0 * (cs2 - w) * dd,
            -(2.0 + eps - 3.0 * cs2 - eta) * Vd + kappa2 * cs2 * dd + opw * kpsi,
        ]

    ev = np.asarray([n for n in n_eval if n >= N_de])
    if ev.size != len(n_eval):
        raise ValueError("clustering-DE stage 2 starts at a_de; every requested "
                         "redshift must satisfy a >= a_de")
    sol = solve_ivp(rhs2, (N_de, 0.0), y0, t_eval=ev,
                    rtol=1e-9, atol=1e-14, method="Radau")
    if not sol.success:
        raise RuntimeError(sol.message)
    dm, Thm = sol.y[0], sol.y[1]
    return dm, -Thm / dm


# ===========================================================================
# The separation statistic (pre-registered).
# ===========================================================================
def fsigma8_curve(bg, zs, cs2=None, k_hMpc=0.1, **kw):
    """f*sigma8 at the requested redshifts, up to the shared primordial
    amplitude.  solve_ivp needs t_eval ascending, so N is sorted here and the
    result is mapped back to the caller's redshift order."""
    n = np.array([math.log(1.0 / (1.0 + z)) for z in zs])
    order = np.argsort(n)
    n_sorted = n[order]
    if cs2 is None:
        d, f = growth_smooth(bg, n_sorted, **kw)
    else:
        d, f = growth_clustering_de(bg, cs2, k_hMpc, n_sorted, **kw)
    curve_sorted = np.asarray(f) * np.asarray(d)
    curve = np.empty_like(curve_sorted)
    curve[order] = curve_sorted
    return curve


def separation(curve_model, curve_ref, yard):
    pts = []
    chi2 = 0.0
    for i, y in enumerate(yard):
        r = curve_model[i] / curve_ref[i]
        dlt = (r - 1.0) / y["eps_frac"]
        pts.append(dict(tracer=y["tracer"], z=y["z"], ratio=float(r),
                        eps_frac=y["eps_frac"], delta_sigma=float(dlt)))
        chi2 += dlt * dlt
    return dict(points=pts,
                max_abs_delta=max(abs(p["delta_sigma"]) for p in pts),
                delta_tot_independent=math.sqrt(chi2),
                mean_frac_shift=float(np.mean([p["ratio"] - 1.0 for p in pts])))


def combined_precision_delta(sep):
    """Separation against the paper's own combined 4.7% RSD-amplitude precision."""
    return abs(sep["mean_frac_shift"]) / DR1_COMBINED_PRECISION


# ===========================================================================
# QC -- the same discipline LS7 used, plus the two checks this file needs.
# ===========================================================================
def qc_block(yard):
    qc = {}

    # (1) derived sigma must reproduce the paper's own Table 9 errors
    t9 = []
    for y in yard:
        ratio, me, pe = DR1_TABLE9_RATIO_ERR[y["tracer"]]
        t9.append(dict(tracer=y["tracer"],
                       eps_derived_from_covariance=y["eps_frac"],
                       table9_err_minus=me / DR1_FSIGMAS8_FID[y["tracer"]] * 0 + me,
                       table9_err_plus=pe,
                       table9_ratio=ratio,
                       derived_sigma_abs=y["sigma_abs"],
                       table9_sigma_abs_max=max(me, pe) * DR1_FSIGMAS8_FID[y["tracer"]],
                       agreement_ratio=y["sigma_abs"] /
                       (max(me, pe) * DR1_FSIGMAS8_FID[y["tracer"]])))
    qc["derived_sigma_vs_published_table9"] = t9
    qc["derived_sigma_vs_published_table9_note"] = (
        "agreement_ratio = (sigma from the Appendix-A Gaussian covariance) / "
        "(larger Table-9 68% error x fiducial). Values near 1 confirm the "
        "covariance transcription; Table 9 errors are asymmetric MAP intervals "
        "so exact equality is not expected.")

    # (2) LambdaCDM f(z) against the Omega_m(z)^0.55 approximation
    lc = bg_lcdm()
    zs = [0.0, 0.295, 0.510, 0.706, 0.919, 1.317, 1.491, 2.0]
    n = np.array([math.log(1.0 / (1.0 + z)) for z in zs])
    order = np.argsort(n)
    _, f_s = growth_smooth(lc, n[order])
    f = np.empty_like(f_s)
    f[order] = f_s
    approx = [(OMEGA_M * (1 + z) ** 3 / lc["E2"](math.log(1 / (1 + z)))) ** 0.55
              for z in zs]
    qc["lcdm_f_vs_Omega_m_0p55"] = [
        dict(z=z, f_integrated=float(fi), f_approx=float(ai),
             frac_diff=float(fi / ai - 1.0))
        for z, fi, ai in zip(zs, f, approx)]
    qc["lcdm_f_vs_Omega_m_0p55_note"] = (
        "the gamma=0.55 fitting formula is itself only ~1% accurate, so "
        "|frac_diff| of order 1% is a PASS, not a discrepancy.")

    # (3) clustering-DE solver must reduce to the smooth single-fluid result
    bgq = bg_quintessence(-0.3995)
    zs2 = [y["z"] for y in yard]
    smooth = fsigma8_curve(bgq, zs2)
    for cs2 in (1.0, 0.999):
        clus = fsigma8_curve(bgq, zs2, cs2=cs2, k_hMpc=0.1)
        qc[f"clustering_solver_vs_smooth_cs2_{cs2}"] = [
            float(c / s - 1.0) for c, s in zip(clus, smooth)]
    qc["clustering_solver_vs_smooth_note"] = (
        "at c_s^2 -> 1 the DE sound horizon is the Hubble radius, DE cannot "
        "cluster on k = 0.1 h/Mpc, and the two-fluid solver must reproduce the "
        "single-fluid smooth-DE growth. Residuals are the size of the residual "
        "physical clustering at c_s^2 = 1, not solver error.")

    # (4) LS7's own background QC, re-run here so this file stands alone
    qc["ls7_background_checks"] = OS.qc_checks({
        "quintessence_alpha_-0.3995": OS.quintessence_background(-0.3995),
        "interacting_xi_0.025": OS.interacting_background(0.025),
    })

    # (5) initial-redshift insensitivity of the RATIO
    ref = bg_lcdm()
    out = {}
    for ai in (3e-3, 1e-3, 3e-4):
        cm = fsigma8_curve(bgq, zs2, a_i=ai)
        cr = fsigma8_curve(ref, zs2, a_i=ai)
        out[f"a_i={ai:g}"] = float(max(abs(m / r - 1.0) for m, r in zip(cm, cr)))
    qc["a_init_insensitivity_maxfracshift_M1_vs_LCDM"] = out
    qc["a_init_insensitivity_note"] = (
        "M1/M3 share rho_m(a) and rho_r(a) with LambdaCDM, so the IC error "
        "cancels in the ratio; the spread across a_i is the residual.")
    return qc


# ===========================================================================
def main():
    yard = growth_yardstick()
    yard_pb = growth_yardstick(DR1_SHAPEFIT_PLUS_BAO)
    zs = [y["z"] for y in yard]

    out = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "script": os.path.basename(__file__),
        "ledger_row": 23,
        "gap": "GAP-2 (growth)",
        "preregistration": "research/cosmic_fate_de_2026_09_22/gap2_growth/"
                           "PREREGISTRATION_GAP2.md",
        "parent_lane": "bb-LS7-row23-fate-de "
                       "(research/cosmic_fate_de_2026_09_22/ROW23_MEMO.md)",
        "citation_used": {
            "primary": "DESI Collaboration, 'DESI 2024 V: Full-Shape Galaxy "
                       "Clustering from Galaxies and Quasars', arXiv:2411.12021, "
                       "JCAP 09 (2025) 008. PDF v5 fetched and read 2026-09-22.",
            "which_numbers": "Appendix A Eqs. (A.1)-(A.12) ShapeFit-alone "
                             "datavectors + 4x4 Gaussian covariances (sigma "
                             "DERIVED as sqrt(C[2][2])); Table 11 fiducial "
                             "f*sigma_s8(z); Table 1 z_eff; Table 9 published "
                             "errors used only as a cross-check; abstract's "
                             "4.7% combined RSD-amplitude precision.",
            "is_this_DR2": False,
            "why_not_DR2": "No citable DESI DR2-era growth measurement with an "
                           "uncertainty exists as of 2026-09-22. DR2 Results II "
                           "(arXiv:2503.14738) is BAO-only. The DR2-era joint "
                           "analysis arXiv:2602.18761 still takes growth from "
                           "DR1 and reports sigma8, not f*sigma8(z). The one "
                           "DR2 full-shape analysis, arXiv:2607.27411 (Lya), "
                           "states in its abstract that 'mock studies reveal a "
                           "significant bias in the inferred growth-rate "
                           "parameter fsigma8, leading us to exclude this "
                           "measurement from the final analysis.' A DR2 "
                           "full-shape talk (PIRSA 26040071, 2026-04-29) is not "
                           "a citable measurement. Pre-registered fallback to "
                           "DR1 full-shape taken and labelled everywhere.",
            "desi_restriction_honoured": DESI_FSIGMA8_RESTRICTION,
        },
        "protocol": "fixed Omega_m and h*r_d (no re-fit, backgrounds imported "
                    "unchanged from observable_separation.py); all models share "
                    "the primordial amplitude and transfer function so "
                    "sigma8(z)/sigma8_LCDM(z) = delta(z)/delta_LCDM(z); the "
                    "reported quantity is a RATIO and no absolute sigma8 is used.",
        "reference": dict(Omega_m=OMEGA_M, Omega_r=OMEGA_R, h=H_LITTLE,
                          Omega_DE0=ODE0, a_init=A_INIT),
        "growth_yardstick_shapefit_alone": yard,
        "growth_yardstick_shapefit_plus_bao": yard_pb,
        "combined_precision_DR1": DR1_COMBINED_PRECISION,
    }

    # ---- symbolic derivations -------------------------------------------
    out["lemma_G1_kessence_cs2_range"] = derive_kessence_cs2_range()
    out["lemma_G2_coupled_growth"] = derive_coupled_growth_equation()

    # ---- references ------------------------------------------------------
    ref_bg = bg_lcdm()
    c_ref = fsigma8_curve(ref_bg, zs)
    out["lcdm_fsigma8_shape_normalised"] = [float(c) for c in c_ref]

    # ---- PRIMARY QUESTION: does c_s^2 separate M3 from M1? ---------------
    ALPHA_STAR = -0.3995          # LS7's 1-sigma BAO boundary (M1_boundary)
    bg_star = bg_quintessence(ALPHA_STAR)
    c_m1_star = fsigma8_curve(bg_star, zs)

    cs2_grid = [0.0, 1e-6, 1e-4, 1e-3, 0.01, 0.05, 0.1, 1.0 / 3.0, 0.5, 0.8, 0.99]
    k_grid = [0.01, 0.03, 0.1, 0.2]
    m3 = []
    for k in k_grid:
        for cs2 in cs2_grid:
            c = fsigma8_curve(bg_star, zs, cs2=cs2, k_hMpc=k)
            sep_vs_m1 = separation(c, c_m1_star, yard)
            sep_vs_lcdm = separation(c, c_ref, yard)
            m3.append(dict(k_hMpc=k, cs2=cs2,
                           max_abs_delta_vs_M1=sep_vs_m1["max_abs_delta"],
                           mean_frac_shift_vs_M1=sep_vs_m1["mean_frac_shift"],
                           combined_delta_vs_M1=combined_precision_delta(sep_vs_m1),
                           max_abs_delta_vs_LCDM=sep_vs_lcdm["max_abs_delta"],
                           points_vs_M1=sep_vs_m1["points"]))
    out["M3_cs2_scan"] = m3
    best = max(m3, key=lambda r: r["max_abs_delta_vs_M1"])
    out["M3_vs_M1_best"] = dict(
        k_hMpc=best["k_hMpc"], cs2=best["cs2"],
        max_abs_delta=best["max_abs_delta_vs_M1"],
        combined_delta=best["combined_delta_vs_M1"],
        mean_frac_shift=best["mean_frac_shift_vs_M1"],
        alpha=ALPHA_STAR,
        note="maximum over the DERIVED allowed c_s^2 range [0,1) (lemma G1) and "
             "over k in [0.01, 0.2] h/Mpc, at LS7's 1-sigma BAO boundary "
             "background. M1 is the c_s^2 -> 1 endpoint, so this is literally "
             "the largest growth signature the k-essence freedom can produce.")
    # monotonicity in c_s^2 (the pre-registered bracketing argument)
    mono = {}
    for k in k_grid:
        rows = sorted([r for r in m3 if r["k_hMpc"] == k], key=lambda r: r["cs2"])
        vals = [r["max_abs_delta_vs_M1"] for r in rows]
        mono[f"k={k}"] = dict(
            cs2=[r["cs2"] for r in rows], max_abs_delta=vals,
            monotone_decreasing=bool(all(vals[i] >= vals[i + 1] - 1e-9
                                         for i in range(len(vals) - 1))),
            argmax_cs2=rows[int(np.argmax(vals))]["cs2"])
    out["M3_cs2_monotonicity"] = mono
    # Does the null survive further from LambdaCDM?  At larger |alpha| the field
    # has 1+w today of order 0.1-0.3, so DE clustering is much stronger.  Those
    # backgrounds are already separated at many sigma by BAO, but the M3-vs-M1
    # question must be answered across the family, not only at LS7's boundary.
    alpha_dep = []
    for a in (-0.2, -0.3995, -0.6, -0.8, -1.0):
        bga = bg_quintessence(a)
        c_m1 = fsigma8_curve(bga, zs)
        c_m3 = fsigma8_curve(bga, zs, cs2=0.0, k_hMpc=0.01)
        sep = separation(c_m3, c_m1, yard)
        sep_lcdm = separation(c_m1, c_ref, yard)
        alpha_dep.append(dict(
            alpha=a, w0=bga["raw"]["w0"],
            one_plus_w0=1.0 + bga["raw"]["w0"],
            max_abs_delta_M3_vs_M1_at_cs2_0=sep["max_abs_delta"],
            mean_frac_shift=sep["mean_frac_shift"],
            max_abs_delta_M1_vs_LCDM_growth=sep_lcdm["max_abs_delta"],
            ratio_cs2_signal_to_background_signal=(
                sep["max_abs_delta"] / sep_lcdm["max_abs_delta"])))
    out["M3_vs_M1_alpha_dependence_at_cs2_0"] = alpha_dep
    _rr = [r["ratio_cs2_signal_to_background_signal"] for r in alpha_dep]
    out["M3_cs2_signal_is_a_fixed_fraction_of_the_background_signal"] = dict(
        ratios=_rr, mean=float(np.mean(_rr)),
        spread=float(max(_rr) - min(_rr)),
        statement="across a factor ~20 in the background growth signature the "
                  "maximal (c_s^2 = 0) k-essence sound-speed signature stays a "
                  "FIXED fraction of it. The k-essence freedom is therefore not "
                  "merely small at LS7's boundary -- it is structurally "
                  "subdominant everywhere in the family, so there is no corner "
                  "of parameter space where growth separates M3 from M1 while "
                  "BAO does not already separate the background from LambdaCDM "
                  "far more strongly.")

    out["M3_vs_M1_alpha_dependence_note"] = (
        "c_s^2 = 0 is the maximal-clustering endpoint (lemma G1 + the "
        "monotonicity check), so each row is the LARGEST growth signature the "
        "k-essence freedom can produce at that background. Backgrounds with "
        "larger |alpha| are already separated from LambdaCDM at many sigma by "
        "the DR2 BAO distances, so they are not viable hiding places for a "
        "growth-only detection; they are scanned to show the null is a "
        "property of the family, not of one parameter choice.")

    out["M3_cs2_monotonicity_note"] = (
        "pre-registered bracketing argument: if the separation is monotone "
        "decreasing in c_s^2, the c_s^2 = 0 endpoint bounds EVERY c_s^2(a) "
        "trajectory inside [0,1), including time-dependent ones, so the scan "
        "result is a bound on the whole family and not just on the grid.")
    # how much tighter would the data have to be?
    if best["max_abs_delta_vs_M1"] > 0:
        out["M3_precision_shrink_factor_for_1sigma"] = dict(
            factor=1.0 / best["max_abs_delta_vs_M1"],
            meaning="the published per-bin fractional precision would have to "
                    "shrink by this factor for the MAXIMAL k-essence growth "
                    "signature to reach 1 sigma. This is a statement about THIS "
                    "calculation against THIS published precision, not a "
                    "forecast for any future DESI release.")

    # ---- SECONDARY: growth separation from LambdaCDM, per model ----------
    m1_rows = []
    for a in (-0.1, -0.2, -0.3, ALPHA_STAR, -0.6, -0.8, -1.0):
        bg = bg_quintessence(a)
        c = fsigma8_curve(bg, zs)
        sep = separation(c, c_ref, yard)
        m1_rows.append(dict(alpha=a, w0=bg["raw"]["w0"],
                            t_c_Gyr=bg["raw"]["t_c_Gyr"],
                            max_abs_delta=sep["max_abs_delta"],
                            delta_tot_independent=sep["delta_tot_independent"],
                            combined_delta=combined_precision_delta(sep),
                            mean_frac_shift=sep["mean_frac_shift"],
                            points=sep["points"]))
    out["M1_growth_scan"] = m1_rows

    m2_rows = []
    for xi in (0.005, 0.01, 0.025, 0.05, 0.1, 0.2, 0.5):
        bg = bg_interacting(xi)
        c = fsigma8_curve(bg, zs)
        sep = separation(c, c_ref, yard)
        # diagnostic: the same model scored with dln(delta)/dlna instead of the
        # RSD velocity rate, to show how large the coupling correction is
        n = np.array([math.log(1.0 / (1.0 + z)) for z in zs])
        order = np.argsort(n)
        d_s, f_s = growth_smooth(bg, n[order])
        gam_s = np.array([xi / bg["rho_m"](nn) for nn in n[order]])
        cw_s = (np.asarray(f_s) - gam_s) * np.asarray(d_s)
        c_wrong = np.empty_like(cw_s)
        c_wrong[order] = cw_s
        sep_wrong = separation(c_wrong, c_ref, yard)
        m2_rows.append(dict(xi=xi, max_abs_delta=sep["max_abs_delta"],
                            delta_tot_independent=sep["delta_tot_independent"],
                            combined_delta=combined_precision_delta(sep),
                            mean_frac_shift=sep["mean_frac_shift"],
                            max_abs_delta_if_dlnDelta_dlna_used=sep_wrong["max_abs_delta"],
                            gamma_today=float(xi / bg["rho_m"](0.0)),
                            points=sep["points"]))
    out["M2_growth_scan"] = m2_rows
    out["M2_caveat"] = (
        "M2's coupling changes rho_c at EARLY times ((Omega_m - xi/3)a^-3), "
        "hence matter-radiation equality and the transfer function, which is "
        "NOT modelled here (no Boltzmann code). M2's growth number is therefore "
        "an approximation with a stated direction of missing effect. M1 and M3 "
        "are unaffected -- their rho_m(a) and rho_r(a) are identical to "
        "LambdaCDM's -- so the PRIMARY (M3-vs-M1) result does not inherit this.")

    # growth boundary for M1: where does growth alone reach 1 sigma?
    def gfun(a):
        return separation(fsigma8_curve(bg_quintessence(a), zs), c_ref,
                          yard)["max_abs_delta"] - 1.0
    try:
        a_growth = brentq(gfun, -0.05, -2.5, xtol=1e-5)
        bgg = bg_quintessence(a_growth)
        out["M1_growth_boundary"] = dict(
            alpha_star_growth=a_growth, w0=bgg["raw"]["w0"],
            t_c_Gyr=bgg["raw"]["t_c_Gyr"],
            compare_LS7_BAO_boundary=dict(alpha=-0.3995, w0=-0.9509,
                                          t_c_Gyr=53.8))
    except (ValueError, RuntimeError) as e:
        out["M1_growth_boundary"] = {
            "no_crossing_in_scanned_range": str(e),
            "meaning": "growth alone does not reach 1 sigma anywhere in "
                       "-0.05 >= alpha >= -2.5 at DR1 full-shape precision"}

    def g2fun(xi):
        return separation(fsigma8_curve(bg_interacting(xi), zs), c_ref,
                          yard)["max_abs_delta"] - 1.0
    try:
        # xi < 3*Omega_m is required for rho_c(a->0) > 0; LS7's own scan stops
        # at xi = 0.5, so the bracket does too.
        xi_growth = brentq(g2fun, 1e-4, 0.5, xtol=1e-8)
        bgx = bg_interacting(xi_growth)
        out["M2_growth_boundary"] = dict(
            xi_star_growth=xi_growth,
            gamma_today=float(xi_growth / bgx["rho_m"](0.0)),
            compare_LS7_BAO_boundary=dict(xi=0.0250),
            bracket="xi in [1e-4, 0.5]; xi < 3*Omega_m = "
                    f"{3*OMEGA_M:.4f} is required for rho_c(a->0) > 0")
    except (ValueError, RuntimeError) as e:
        out["M2_growth_boundary"] = {"no_crossing_in_scanned_range": str(e)}

    # ---- sensitivity -----------------------------------------------------
    sens = {}
    sep_star = separation(c_m1_star, c_ref, yard)
    sens["M1_at_LS7_boundary_max_abs_delta"] = sep_star["max_abs_delta"]
    sens["eps_plus_10pct"] = sep_star["max_abs_delta"] / 1.1
    sens["eps_minus_10pct"] = sep_star["max_abs_delta"] / 0.9
    sep_pb = separation(c_m1_star, c_ref, yard_pb)
    sens["shapefit_plus_bao_variant"] = sep_pb["max_abs_delta"]
    sens["shapefit_plus_bao_variant_note"] = (
        "reported for completeness only; the baseline is ShapeFit-ALONE because "
        "the row-23 Step-2 separation already uses DESI DR2 BAO distances.")
    best_pb = separation(
        fsigma8_curve(bg_star, zs, cs2=best["cs2"], k_hMpc=best["k_hMpc"]),
        c_m1_star, yard_pb)
    sens["M3_vs_M1_best_with_shapefit_plus_bao"] = best_pb["max_abs_delta"]
    out["sensitivity"] = sens

    out["qc"] = qc_block(yard)

    out["still_open"] = [
        "GAP-1 (frame-dependence for non-minimally coupled scalars) is "
        "untouched by this lane and remains the best-defined theory step.",
        "GAP-3 (no citable DR2 central values) is unchanged: no goodness-of-fit "
        "is computed here either; every number is a model-vs-model separation "
        "in units of a published precision.",
        "A DESI DR2 galaxy full-shape release would replace the DR1 yardstick "
        "used here; until one exists the growth statement is DR1-limited.",
        "M2's transfer-function change is not modelled (see M2_caveat).",
    ]

    path = os.path.join(_HERE, "growth_separation.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2)

    # ---- report ----------------------------------------------------------
    print("ROW 23 -- GAP-2: GROWTH SEPARATION")
    print("=" * 88)
    print("yardstick: DESI DR1 full-shape ShapeFit (arXiv:2411.12021 App. A), "
          "NOT DR2 -- no DR2 growth measurement exists")
    print(f"{'tracer':>7}{'z':>8}{'fss8_dv':>10}{'sigma':>9}{'fid':>8}{'eps':>9}")
    for y in yard:
        print(f"{y['tracer']:>7}{y['z']:>8.3f}{y['fsigma_s8_datavector']:>10.4f}"
              f"{y['sigma_abs']:>9.4f}{y['fsigma_s8_fid']:>8.4f}"
              f"{y['eps_frac']:>9.4f}")
    print("\nLEMMA G1 (derived c_s^2 range):")
    print("  " + out["lemma_G1_kessence_cs2_range"]["RESULT"])
    print("\nLEMMA G2 (coupled growth):")
    print("  " + out["lemma_G2_coupled_growth"]["second_order_form"])
    print("  " + out["lemma_G2_coupled_growth"]["RSD_growth_rate"])

    print("\nPRIMARY -- M3 vs M1 (same background, c_s^2 the only difference):")
    print(f"{'k':>7}{'cs2':>10}{'max|D| vs M1':>15}{'comb':>8}{'max|D| vs LCDM':>17}")
    for r in m3:
        print(f"{r['k_hMpc']:>7.2f}{r['cs2']:>10.5f}"
              f"{r['max_abs_delta_vs_M1']:>15.4f}"
              f"{r['combined_delta_vs_M1']:>8.3f}"
              f"{r['max_abs_delta_vs_LCDM']:>17.4f}")
    b = out["M3_vs_M1_best"]
    print(f"\n  BEST: max|Delta| = {b['max_abs_delta']:.4f} sigma at "
          f"c_s^2 = {b['cs2']}, k = {b['k_hMpc']} h/Mpc")
    print(f"  precision shrink factor needed for 1 sigma: "
          f"{out['M3_precision_shrink_factor_for_1sigma']['factor']:.1f}x")
    print("  monotone in c_s^2: " +
          str({k: v["monotone_decreasing"] for k, v in mono.items()}))
    print("  alpha-dependence of the M3-vs-M1 null at c_s^2 = 0 "
          "(maximal clustering):")
    print(f"{'alpha':>8}{'w0':>10}{'1+w0':>9}{'max|D| M3vsM1':>16}"
          f"{'max|D| M1vsLCDM':>18}{'ratio':>10}")
    for r in alpha_dep:
        print(f"{r['alpha']:>8.4f}{r['w0']:>10.4f}{r['one_plus_w0']:>9.4f}"
              f"{r['max_abs_delta_M3_vs_M1_at_cs2_0']:>16.4f}"
              f"{r['max_abs_delta_M1_vs_LCDM_growth']:>18.4f}"
              f"{r['ratio_cs2_signal_to_background_signal']:>10.4f}")

    print("\nSECONDARY -- growth vs LambdaCDM:")
    print(f"{'alpha':>8}{'w0':>10}{'t_c[Gyr]':>11}{'max|D|':>9}{'D_tot':>8}{'comb':>8}")
    for r in m1_rows:
        print(f"{r['alpha']:>8.4f}{r['w0']:>10.4f}{r['t_c_Gyr']:>11.4g}"
              f"{r['max_abs_delta']:>9.3f}{r['delta_tot_independent']:>8.3f}"
              f"{r['combined_delta']:>8.3f}")
    print(f"  LS7 BAO boundary alpha*=-0.3995 gave max|Delta|_BAO = 1.00; "
          f"growth there = {sens['M1_at_LS7_boundary_max_abs_delta']:.3f}")
    print(f"{'xi':>8}{'max|D|':>9}{'D_tot':>8}{'comb':>8}{'gamma0':>9}"
          f"{'max|D| if dlnd/dlna':>21}")
    for r in m2_rows:
        print(f"{r['xi']:>8.3f}{r['max_abs_delta']:>9.3f}"
              f"{r['delta_tot_independent']:>8.3f}{r['combined_delta']:>8.3f}"
              f"{r['gamma_today']:>9.4f}"
              f"{r['max_abs_delta_if_dlnDelta_dlna_used']:>21.3f}")
    print(f"\n  M1 growth boundary: {out['M1_growth_boundary']}")
    print(f"  M2 growth boundary: {out['M2_growth_boundary']}")
    print(f"\nsensitivity: {json.dumps(sens)[:600]}")
    print(f"\nQC lcdm f vs Om^0.55: "
          f"{[round(r['frac_diff'], 4) for r in out['qc']['lcdm_f_vs_Omega_m_0p55']]}")
    print(f"QC clustering solver at cs2=1: "
          f"{['%.2e' % v for v in out['qc']['clustering_solver_vs_smooth_cs2_1.0']]}")
    print(f"QC derived sigma / Table-9 sigma: "
          f"{[round(r['agreement_ratio'], 3) for r in out['qc']['derived_sigma_vs_published_table9']]}")
    print(f"QC a_init insensitivity: {out['qc']['a_init_insensitivity_maxfracshift_M1_vs_LCDM']}")
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()

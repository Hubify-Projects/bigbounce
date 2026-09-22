#!/usr/bin/env python3
"""
observable_separation.py -- ledger row 23, Step 2.

For every DE class that Step 1 (cross_table.py) places in BOTH sets -- Branch I
bounce-compatible AND admitting a future turnaround -- compute the PRESENT-DAY
separation from LambdaCDM in the observables DESI DR2 constrains, in units of
the published DR2 uncertainties.

Classes carried forward from cross_table.json:
  M1  canonical quintessence with a potential crossing zero
      (Branch I Class 2 / Phase-1 Class A; memo Sec. 3(d)).
      Concrete realisation: the linear potential V = V0 + alpha*phi of
      Kallosh, Kratochvil, Linde, Linder & Shmakova, arXiv:astro-ph/0307185,
      integrated exactly here (no slow-roll approximation), thawing initial
      condition phi' = 0 deep in matter domination.
  M2  interacting dark sector with a sustained drain
      (Branch I Class 6; memo Sec. 3(e) case 1).  Closed form from
      cross_table.py lemma L5.
  M3  k-essence with a zero-crossing effective potential
      (Branch I Class 3 / Phase-1 Class B).  At the BACKGROUND level this is
      M1 with a rescaled kinetic term: cross_table.py lemma L3 gives
      rho = K X + 3 L X^2 + V and p = K X + L X^2 - V, so the background
      trajectory is that of M1 for the canonical member and the distinctive
      k-essence freedom is c_s^2, which moves GROWTH, not BAO distances.
      Its distinguishing observable is therefore f*sigma8 -- a NAMED GAP here
      (no citable DR2-era f sigma8 value with an uncertainty was obtained in
      this lane; see ROW23_MEMO.md GAP-2).  It is NOT given a fabricated number.

RULER (not in the intersection, used only to calibrate the metric):
  R1  constant-w dark energy at the DESI DR2 BAO-only wCDM central value.

Comparison protocol (pre-registered): fixed Omega_m and fixed h*r_d, i.e. the
model is NOT re-fit.  The resulting separation is an UPPER BOUND on what a
marginalised analysis would find.  Stated with every number.

Usage: python3 observable_separation.py   (writes observable_separation.json)
"""

import json
import math
import os
from datetime import datetime, timezone

import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

# ---------------------------------------------------------------------------
# Constants (CODATA c exact; Mpc, Gyr as in the row-20 script
# research/archaeology_2025/outputs/cosmic_fate_turnaround_2026_09_18.py)
# ---------------------------------------------------------------------------
C_KM_S = 299792.458              # km/s, exact
KM = 1.0e3                       # m
MPC = 3.085_677_581_491_367e22   # m (IAU)
GYR = 3.155_76e16                # s

# ---------------------------------------------------------------------------
# DESI DR2 inputs.  EVERY number below is quoted from a citable source; none is
# estimated, interpolated or assumed.  sigma and rho are DERIVED in code from
# the published covariance blocks -- no uncertainty is hand-typed.
# ---------------------------------------------------------------------------
# Source S1: DESI Collaboration, DESI DR2 Results II: BAO measurements and
#   cosmological constraints, arXiv:2503.14738 (Phys. Rev. D 112, 2025).
#   -- the primary measurement paper.
# Source S2: arXiv:2507.01380, "Comparing LambdaCDM, wCDM, and w0waCDM models
#   with DESI DR2 BAO", Sec. III.B "Covariance Matrix Reconstruction".  This
#   SECONDARY source reproduces, block by block, the covariance it reconstructs
#   from "the publicly released uncertainties and correlation coefficients" of
#   S1 (its Table IV).  The blocks are transcribed verbatim below.  Flagged as
#   secondary everywhere it is used.
# Source S3: DESI Collaboration, DESI DR2 Results IV (Lyman-alpha AP),
#   arXiv:2607.27410 -- abstract values already verified into
#   research/archaeology_2025/memos/COSMIC_FATE_MEMO.md Sec. 4.1.
# Source S4: Planck 2018 VI, arXiv:1807.06209 (reference background only).

DR2_COV_BLOCKS = {
    # tracer: (z_eff, [[var_DM, cov],[cov, var_DH]])  in the (D_M/r_d, D_H/r_d)
    # basis, verbatim from S2 Sec. III.B "Case 2" ... "Case 7".
    "LRG1":      (0.510, [[2.788900e-2, -3.257752e-2], [-3.257752e-2, 1.806250e-1]]),
    "LRG2":      (0.706, [[3.132900e-2, -2.359764e-2], [-2.359764e-2, 1.089000e-1]]),
    "LRG3+ELG1": (0.934, [[2.310400e-2, -1.220377e-2], [-1.220377e-2, 3.724900e-2]]),
    "ELG2":      (1.321, [[1.011240e-1, -3.050065e-2], [-3.050065e-2, 4.884100e-2]]),
    "QSO":       (1.484, [[5.776000e-1, -1.960800e-1], [-1.960800e-1, 2.662560e-1]]),
    "Lya":       (2.330, [[2.819610e-1, -2.311496e-2], [-2.311496e-2, 1.020100e-2]]),
}
# BGS contributes a single D_V/r_d point (S2 "Case 1": C_BGS = [0.005625]).
DR2_BGS = (0.295, 0.005625)

# Sensitivity variant: the tighter Lya numbers of S3 (memo Sec. 4.1),
# D_H/r_d = 8.600 +- 0.066, D_M/r_d = 39.32 +- 0.33 at z_eff = 2.33.  Their
# correlation is not given in the verified abstract text, so this variant
# treats them as uncorrelated and says so.
DR2_IV_LYA = (2.330, 0.33, 0.066, 0.0)

# Reference LambdaCDM background: DESI DR2 BAO-only LambdaCDM, quoted by the
# collaboration (S1) and reproduced in S2 Table I as "LambdaCDM^DESI":
OMEGA_M = 0.2975          # +- 0.0086
H_RD_MPC = 101.54         # +- 0.73  (h * r_d, Mpc)
R_D_MPC = 147.09          # +- 0.26  (Planck DR3 prior, S2 Table IV)
H_LITTLE = H_RD_MPC / R_D_MPC
# Standard photon + 3 massless-neutrino radiation density, Omega_r h^2 = 4.15e-5
# (textbook value; the run is repeated with Omega_r = 0 to show insensitivity).
OMEGA_R_H2 = 4.15e-5
OMEGA_R = OMEGA_R_H2 / H_LITTLE**2

# DESI DR2 BAO-only wCDM central value (S2 Table I, "wCDM^DESI"): w = -0.916
RULER_W = -0.916
RULER_SIGMA_W = 0.078        # S2 Table I, "wCDM^DESI": w = -0.916 +- 0.078

HUBBLE_TIME_GYR = (MPC / (100.0 * H_LITTLE * KM)) / GYR   # 1/H0 in Gyr


# ---------------------------------------------------------------------------
# data vector assembly
# ---------------------------------------------------------------------------
def build_data_spec(use_dr2_iv_lya=False):
    spec = []
    z_bgs, var_v = DR2_BGS
    spec.append(dict(tracer="BGS", z=z_bgs, kind="DV",
                     sigma=math.sqrt(var_v), source="S2 Case 1 <- S1"))
    for name, (z, cov) in DR2_COV_BLOCKS.items():
        if name == "Lya" and use_dr2_iv_lya:
            z, sm, sh, r = DR2_IV_LYA
            spec.append(dict(tracer=name, z=z, kind="DM_DH", sigma_M=sm,
                             sigma_H=sh, rho=r,
                             source="S3 abstract (memo Sec. 4.1); correlation "
                                    "not published -> treated as 0"))
            continue
        sm = math.sqrt(cov[0][0])
        sh = math.sqrt(cov[1][1])
        spec.append(dict(tracer=name, z=z, kind="DM_DH", sigma_M=sm,
                         sigma_H=sh, rho=cov[0][1] / (sm * sh),
                         source=f"S2 covariance block <- S1"))
    return spec


# ---------------------------------------------------------------------------
# backgrounds.  Each returns E(z) as a callable on [0, 3].
# ---------------------------------------------------------------------------
def E_lcdm(om=OMEGA_M, orad=OMEGA_R):
    ode = 1.0 - om - orad
    return lambda z: np.sqrt(om * (1 + z) ** 3 + orad * (1 + z) ** 4 + ode)


def E_wcdm(w, om=OMEGA_M, orad=OMEGA_R):
    ode = 1.0 - om - orad
    return lambda z: np.sqrt(om * (1 + z) ** 3 + orad * (1 + z) ** 4
                             + ode * (1 + z) ** (3 * (1 + w)))


# --- M1: linear-potential quintessence, integrated exactly --------------------
def _quint_rhs_u(u, s, alpha, om, orad):
    """d/du of (x, y) with y = dx/du, x = phi/M_pl, v = V/rho_crit0."""
    x, y = s
    v = _pot[0](x, _v0_cache[0], alpha)
    alpha = _dpot[0](x, _v0_cache[0], alpha)   # v_x at this x
    num = om * math.exp(-3 * u) + orad * math.exp(-4 * u) + v
    den = 1.0 - y * y / 6.0
    E2 = num / den
    rho_plus_p = (om * math.exp(-3 * u) + (4.0 / 3.0) * orad * math.exp(-4 * u)
                  + E2 * y * y / 3.0)
    dlnE = -1.5 * rho_plus_p / E2
    dydu = -3.0 * y - 3.0 * alpha / E2 - y * dlnE
    return [y, dydu]


_v0_cache = [0.0]
# potential and its derivative, v(x; v0, alpha) and dv/dx.  Default: linear.
_pot = [lambda x, v0, a: v0 + a * x]
_dpot = [lambda x, v0, a: a]


def quintessence_background(alpha, om=OMEGA_M, orad=OMEGA_R,
                            u_i=math.log(1e-4), pot=None, dpot=None,
                            x_i=0.0):
    """Thawing linear-potential quintessence.

    Shoots on V0 so that E^2(a=1) = 1 exactly (equivalently rho_phi(today) =
    1 - Omega_m - Omega_r), starting frozen (phi' = 0) at a = 1e-4.
    Returns dict with E(z) spline, w(z), rho_DE(z), and the future turnaround.
    """
    ode0 = 1.0 - om - orad
    _pot[0] = pot or (lambda x, v0, a: v0 + a * x)
    _dpot[0] = dpot or (lambda x, v0, a: a)

    def E2_today(v0):
        _v0_cache[0] = v0
        sol = solve_ivp(_quint_rhs_u, (u_i, 0.0), [x_i, 0.0],
                        args=(alpha, om, orad), rtol=1e-10, atol=1e-12,
                        dense_output=True, max_step=0.05)
        x, y = sol.y[0, -1], sol.y[1, -1]
        v = _pot[0](x, v0, alpha)
        E2 = (om + orad + v) / (1.0 - y * y / 6.0)
        return E2 - 1.0, sol

    f = lambda v0: E2_today(v0)[0]
    lo, hi = 0.2 * ode0, 4.0 * ode0
    v0 = brentq(f, lo, hi, xtol=1e-14, rtol=1e-15)
    _, sol = E2_today(v0)

    # past/present grid
    us = np.linspace(u_i, 0.0, 4000)
    xs, ys = sol.sol(us)
    vs = np.array([_pot[0](xx, v0, alpha) for xx in xs])
    E2s = (om * np.exp(-3 * us) + orad * np.exp(-4 * us) + vs) / (1 - ys**2 / 6)
    rho_de = E2s * ys**2 / 6.0 + vs
    p_de = E2s * ys**2 / 6.0 - vs
    zs = np.exp(-us) - 1.0
    order = np.argsort(zs)
    E_spline = CubicSpline(zs[order], np.sqrt(E2s[order]))
    w_spline = CubicSpline(zs[order], (p_de / rho_de)[order])
    rde_spline = CubicSpline(zs[order], (rho_de / ode0)[order])

    # future, in cosmic time, to the turnaround
    x0, y0 = xs[-1], ys[-1]
    p0 = y0                      # dx/dtau = E*y, E(0) = 1

    def rad(u, x, p):
        return (om * math.exp(-3 * u) + orad * math.exp(-4 * u)
                + p * p / 6.0 + _pot[0](x, v0, alpha))

    def rhs_tau(tau, s):
        u, x, p = s
        E = math.sqrt(max(rad(u, x, p), 0.0))
        return [E, p, -3.0 * E * p - 3.0 * _dpot[0](x, v0, alpha)]

    def ev(tau, s):
        return rad(s[0], s[1], s[2])
    ev.terminal = True
    ev.direction = -1
    fut = solve_ivp(rhs_tau, (0.0, 5000.0), [0.0, x0, p0], events=ev,
                    rtol=1e-10, atol=1e-12, max_step=0.5)
    if fut.t_events[0].size:
        tau_t = float(fut.t_events[0][0])
        a_t = math.exp(float(fut.y_events[0][0][0]))
        t_c_gyr = tau_t * HUBBLE_TIME_GYR
    else:
        tau_t, a_t, t_c_gyr = float("nan"), float("nan"), float("inf")

    return dict(alpha=alpha, v0=v0, E=E_spline, w=w_spline, rho_DE=rde_spline,
                w0=float(w_spline(0.0)), t_c_Gyr=t_c_gyr, a_turnaround=a_t,
                tau_turnaround=tau_t)


# --- M2: interacting dark sector, sustained drain (lemma L5) -----------------
def interacting_background(xi, om=OMEGA_M, orad=OMEGA_R):
    ode0 = 1.0 - om - orad

    def E2_of_u(u):
        rho_de = ode0 - xi * u
        rho_c = (om - xi / 3.0) * np.exp(-3 * u) + xi / 3.0
        return orad * np.exp(-4 * u) + rho_c + rho_de

    zs = np.linspace(0.0, 3.0, 3000)
    us = -np.log1p(zs)
    E_spline = CubicSpline(zs, np.sqrt(E2_of_u(us)))
    rho_de_arr = (ode0 - xi * us) / ode0
    rde_spline = CubicSpline(zs, rho_de_arr)
    # effective w defined by  w_eff = -1 - (1/3) dln rho_DE / dln a
    drho = -xi
    w_eff = CubicSpline(zs, -1.0 - (1.0 / 3.0) * drho / (ode0 - xi * us))

    # turnaround: first u > 0 with E^2 = 0
    g = lambda u: float(E2_of_u(np.array([u]))[0])
    u_hi, u_t = 0.1, None
    while u_hi < 200.0:
        if g(u_hi) <= 0:
            u_t = brentq(g, max(1e-6, u_hi / 2), u_hi, xtol=1e-14)
            break
        u_hi *= 1.6
    if u_t is None:
        t_c = float("inf")
    else:
        tau = quad(lambda u: 1.0 / math.sqrt(max(g(u), 1e-300)), 0.0,
                   u_t, limit=400, points=[u_t])[0]
        t_c = tau * HUBBLE_TIME_GYR
    return dict(xi=xi, E=E_spline, w=w_eff, rho_DE=rde_spline,
                w0=float(w_eff(0.0)), t_c_Gyr=t_c,
                a_turnaround=math.exp(u_t) if u_t else float("nan"))


# ---------------------------------------------------------------------------
# observables and the separation statistic
# ---------------------------------------------------------------------------
def distances(E, z):
    """(D_M/r_d, D_H/r_d, D_V/r_d) at fixed h*r_d."""
    pref = C_KM_S / 100.0 / H_RD_MPC          # (c/H0)/r_d, dimensionless
    dm = pref * quad(lambda zz: 1.0 / float(E(zz)), 0.0, z, limit=200)[0]
    dh = pref / float(E(z))
    dv = (z * dm * dm * dh) ** (1.0 / 3.0)
    return dm, dh, dv


def separation(E_model, E_ref, spec):
    """Per-point Delta_i in sigma, plus the pre-registered aggregates."""
    pts, chi2_block, chi2_indep = [], 0.0, 0.0
    for s in spec:
        if s["kind"] == "DV":
            _, _, dv_m = distances(E_model, s["z"])
            _, _, dv_r = distances(E_ref, s["z"])
            d = (dv_m - dv_r) / s["sigma"]
            pts.append(dict(tracer=s["tracer"], z=s["z"], obs="D_V/r_d",
                            delta_sigma=d, sigma=s["sigma"],
                            model=dv_m, lcdm=dv_r))
            chi2_block += d * d
            chi2_indep += d * d
        else:
            dm_m, dh_m, _ = distances(E_model, s["z"])
            dm_r, dh_r, _ = distances(E_ref, s["z"])
            dM = (dm_m - dm_r) / s["sigma_M"]
            dH = (dh_m - dh_r) / s["sigma_H"]
            pts.append(dict(tracer=s["tracer"], z=s["z"], obs="D_M/r_d",
                            delta_sigma=dM, sigma=s["sigma_M"],
                            model=dm_m, lcdm=dm_r))
            pts.append(dict(tracer=s["tracer"], z=s["z"], obs="D_H/r_d",
                            delta_sigma=dH, sigma=s["sigma_H"],
                            model=dh_m, lcdm=dh_r))
            chi2_indep += dM * dM + dH * dH
            r = s["rho"]
            chi2_block += (dM * dM - 2 * r * dM * dH + dH * dH) / (1 - r * r)
    return dict(points=pts,
                max_abs_delta=max(abs(p["delta_sigma"]) for p in pts),
                delta_tot_independent=math.sqrt(chi2_indep),
                delta_tot_block_cov=math.sqrt(chi2_block))


def qc_checks(bgs):
    """Independent consistency checks, not used by any result."""
    qc = {}
    for name, bg in bgs.items():
        E0 = float(bg["E"](0.0))
        r = bg["rho_DE"]
        zz = np.linspace(0.0, 2.5, 200)
        rho = np.array([float(r(z)) for z in zz])
        # rho_DE must be non-increasing in TIME, i.e. non-decreasing in z
        monotone = bool(np.all(np.diff(rho) >= -1e-10))
        qc[name] = dict(E_at_z0_minus_1=E0 - 1.0,
                        rho_DE_nondecreasing_with_z=monotone,
                        rho_DE_at_z2p33_over_rho_DE0=float(r(2.33)))
    return qc


# ---------------------------------------------------------------------------
def main():
    spec = build_data_spec()
    Eref = E_lcdm()
    out = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "script": os.path.basename(__file__),
        "ledger_row": 23,
        "preregistration": "research/cosmic_fate_de_2026_09_22/PREREGISTRATION.md",
        "protocol": "fixed Omega_m and fixed h*r_d; the model is NOT re-fit. "
                    "Every separation below is an UPPER BOUND on a marginalised "
                    "separation.",
        "reference": dict(Omega_m=OMEGA_M, h_rd_Mpc=H_RD_MPC, r_d_Mpc=R_D_MPC,
                          h=H_LITTLE, Omega_r=OMEGA_R,
                          hubble_time_Gyr=HUBBLE_TIME_GYR,
                          source="DESI DR2 BAO-only LambdaCDM (S1), as quoted "
                                 "in S2 Table I; r_d from S2 Table IV"),
        "data_spec": spec,
    }

    # ---- ruler -----------------------------------------------------------
    sep_r1 = separation(E_wcdm(RULER_W), Eref, spec)
    out["ruler_wCDM"] = dict(
        w=RULER_W, note="DESI DR2 BAO-only wCDM central value w = -0.916 +- "
                        "0.078 (S2 Table I). Calibrates the metric: this is "
                        "what a ~1.1 sigma marginalised departure from w = -1 "
                        "looks like in the fixed-parameter statistic.",
        max_abs_delta=sep_r1["max_abs_delta"],
        delta_tot_independent=sep_r1["delta_tot_independent"],
        delta_tot_block_cov=sep_r1["delta_tot_block_cov"],
        points=sep_r1["points"])

    # ---- M1 scan ---------------------------------------------------------
    alphas = [-0.02, -0.05, -0.1, -0.15, -0.2, -0.3, -0.4, -0.6, -0.8, -1.0]
    m1 = []
    for a in alphas:
        bg = quintessence_background(a)
        sep = separation(bg["E"], Eref, spec)
        m1.append(dict(alpha=a, v0=bg["v0"], w0=bg["w0"],
                       t_c_Gyr=bg["t_c_Gyr"], a_turnaround=bg["a_turnaround"],
                       rho_DE_over_rho_DE0_at_z1=float(bg["rho_DE"](1.0)),
                       w_at_z1=float(bg["w"](1.0)),
                       max_abs_delta=sep["max_abs_delta"],
                       delta_tot_independent=sep["delta_tot_independent"],
                       delta_tot_block_cov=sep["delta_tot_block_cov"],
                       worst_point=max(sep["points"],
                                       key=lambda p: abs(p["delta_sigma"])),
                       absurd_epoch=bool(bg["a_turnaround"] > 1e6)))
    out["M1_quintessence_scan"] = m1
    out["absurd_epoch_note"] = (
        "a_turnaround > 1e6 flags a formal turnaround at an epoch where a "
        "linear potential -- itself a local expansion of V about today's field "
        "value -- carries no physical content. Those rows are reported for "
        "completeness, not as models.")

    # boundary: alpha where max|Delta| = 1
    def g(a):
        return separation(quintessence_background(a)["E"], Eref,
                          spec)["max_abs_delta"] - 1.0
    try:
        a_star = brentq(g, -0.02, -1.0, xtol=1e-6)
        bg_star = quintessence_background(a_star)
        sep_star = separation(bg_star["E"], Eref, spec)
        out["M1_boundary"] = dict(
            alpha_star=a_star, w0_star=bg_star["w0"],
            t_c_star_Gyr=bg_star["t_c_Gyr"],
            a_turnaround=bg_star["a_turnaround"],
            max_abs_delta=sep_star["max_abs_delta"],
            delta_tot_independent=sep_star["delta_tot_independent"],
            delta_tot_block_cov=sep_star["delta_tot_block_cov"],
            meaning="turnaround SOONER than t_c_star_Gyr => conservative "
                    "per-point separation exceeds 1 sigma at DR2 precision "
                    "(fixed-parameter, hence optimistic)")
    except ValueError as e:
        out["M1_boundary"] = {"error": str(e)}

    # ---- marginalisation calibration from the ruler ----------------------
    # The fixed-parameter statistic overstates a marginalised significance.
    # The ruler gives the conversion for a one-parameter DE departure:
    #   kappa = max|Delta|_ruler / (|w+1| / sigma_w)  [fixed-param sigma per
    #   marginalised sigma].  Approximate, single-ruler, explicitly labelled.
    marg_sig_ruler = abs(RULER_W + 1.0) / RULER_SIGMA_W
    kappa = sep_r1["max_abs_delta"] / marg_sig_ruler
    out["marginalisation_calibration"] = dict(
        ruler_marginalised_sigma=marg_sig_ruler,
        ruler_fixed_param_max_abs_delta=sep_r1["max_abs_delta"],
        kappa_fixed_param_sigma_per_marginalised_sigma=kappa,
        caveat="single-ruler, one-parameter DE departure, assumes comparable "
               "degeneracy directions. Use only as an order-of-magnitude "
               "conversion; it is NOT a marginalised likelihood analysis.")

    def gk(a):
        return separation(quintessence_background(a)["E"], Eref,
                          spec)["max_abs_delta"] - kappa
    try:
        a_k = brentq(gk, -0.05, -1.5, xtol=1e-6)
        bgk = quintessence_background(a_k)
        out["M1_boundary_marginalisation_calibrated"] = dict(
            alpha=a_k, w0=bgk["w0"], t_c_Gyr=bgk["t_c_Gyr"],
            a_turnaround=bgk["a_turnaround"],
            meaning="turnaround sooner than this t_c would be a ~1 sigma "
                    "MARGINALISED departure, using the ruler conversion")
    except ValueError as e:
        out["M1_boundary_marginalisation_calibrated"] = {"error": str(e)}

    # ---- M2 scan ---------------------------------------------------------
    xis = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5]
    m2 = []
    for xi in xis:
        bg = interacting_background(xi)
        sep = separation(bg["E"], Eref, spec)
        m2.append(dict(xi=xi, w0_eff=bg["w0"], t_c_Gyr=bg["t_c_Gyr"],
                       a_turnaround=bg["a_turnaround"],
                       rho_DE_over_rho_DE0_at_z1=float(bg["rho_DE"](1.0)),
                       max_abs_delta=sep["max_abs_delta"],
                       delta_tot_independent=sep["delta_tot_independent"],
                       delta_tot_block_cov=sep["delta_tot_block_cov"],
                       worst_point=max(sep["points"],
                                       key=lambda p: abs(p["delta_sigma"])),
                       absurd_epoch=bool(bg["a_turnaround"] > 1e6)))
    out["M2_interacting_scan"] = m2

    def g2(xi):
        return separation(interacting_background(xi)["E"], Eref,
                          spec)["max_abs_delta"] - 1.0
    try:
        xi_star = brentq(g2, 0.001, 1.0, xtol=1e-8)
        bg2 = interacting_background(xi_star)
        out["M2_boundary"] = dict(xi_star=xi_star, w0_eff=bg2["w0"],
                                  t_c_star_Gyr=bg2["t_c_Gyr"],
                                  a_turnaround=bg2["a_turnaround"])
    except ValueError as e:
        out["M2_boundary"] = {"error": str(e)}

    # ---- robustness ------------------------------------------------------
    spec_iv = build_data_spec(use_dr2_iv_lya=True)
    a_ref = out["M1_boundary"].get("alpha_star")
    if a_ref:
        bg = quintessence_background(a_ref)
        out["robustness"] = {
            "with_DR2_IV_Lya_errors": separation(bg["E"], Eref, spec_iv)["max_abs_delta"],
            "no_radiation": separation(
                quintessence_background(a_ref, orad=0.0)["E"],
                E_lcdm(orad=0.0), spec)["max_abs_delta"],
            "note": "both re-evaluated at the boundary alpha_star; compare to "
                    "max_abs_delta = 1 by construction in the baseline run",
        }

    # ---- potential-shape robustness: quadratic top V = V0 - m^2 phi^2/2 ---
    # Checks whether the (w0, t_c, separation) relation found for the linear
    # potential is an artefact of that potential's shape.  x_i = 0.1 (the field
    # must start displaced or it never rolls); m2 is the scanned parameter.
    qt = []
    for m2v in (0.3, 0.6, 1.0, 1.5, 2.0, 3.0):
        pot = (lambda x, v0, a, _m=m2v: v0 - 0.5 * _m * x * x)
        dpot = (lambda x, v0, a, _m=m2v: -_m * x)
        bg = quintessence_background(0.0, pot=pot, dpot=dpot, x_i=0.1)
        sep = separation(bg["E"], Eref, spec)
        qt.append(dict(m2=m2v, w0=bg["w0"], t_c_Gyr=bg["t_c_Gyr"],
                       a_turnaround=bg["a_turnaround"],
                       max_abs_delta=sep["max_abs_delta"],
                       delta_tot_block_cov=sep["delta_tot_block_cov"],
                       absurd_epoch=bool(bg["a_turnaround"] > 1e6)))
    out["M1b_quadratic_top_scan"] = qt
    def gq(m2v):
        pot = (lambda x, v0, a, _m=m2v: v0 - 0.5 * _m * x * x)
        dpot = (lambda x, v0, a, _m=m2v: -_m * x)
        bg = quintessence_background(0.0, pot=pot, dpot=dpot, x_i=0.1)
        return separation(bg["E"], Eref, spec)["max_abs_delta"] - 1.0
    try:
        m2_star = brentq(gq, 0.3, 4.0, xtol=1e-6)
        pot = (lambda x, v0, a, _m=m2_star: v0 - 0.5 * _m * x * x)
        dpot = (lambda x, v0, a, _m=m2_star: -_m * x)
        bgq = quintessence_background(0.0, pot=pot, dpot=dpot, x_i=0.1)
        out["M1b_boundary"] = dict(
            m2_star=m2_star, w0_star=bgq["w0"], t_c_star_Gyr=bgq["t_c_Gyr"],
            a_turnaround=bgq["a_turnaround"])
    except ValueError as e:
        out["M1b_boundary"] = {"error": str(e)}
    lin = out.get("M1_boundary", {})
    qua = out.get("M1b_boundary", {})
    if "t_c_star_Gyr" in lin and "t_c_star_Gyr" in qua:
        out["boundary_universality"] = dict(
            t_c_star_linear_Gyr=lin["t_c_star_Gyr"],
            t_c_star_quadratic_top_Gyr=qua["t_c_star_Gyr"],
            t_c_ratio=lin["t_c_star_Gyr"] / qua["t_c_star_Gyr"],
            w0_star_linear=lin["w0_star"],
            w0_star_quadratic_top=qua["w0_star"],
            w0_spread=abs(lin["w0_star"] - qua["w0_star"]),
            statement="the 1-sigma boundary is nearly the same in w0 across the "
                      "two potential families but differs by the quoted factor "
                      "in t_c: DESI DR2 constrains the PRESENT-DAY equation of "
                      "state, and the translation into a turnaround epoch is "
                      "potential-family dependent.")
    out["M1b_note"] = ("quadratic-top potential V = V0 - m^2 phi^2/2, x_i = 0.1, "
                       "scanned in m^2 (in units where rho is measured in "
                       "rho_crit0 and phi in M_pl). Tests potential-shape "
                       "dependence of the t_c <-> separation relation.")

    # ---- trajectories for the memo --------------------------------------
    traj_z = [0.0, 0.295, 0.51, 0.706, 0.934, 1.321, 1.484, 2.33]
    tr = {}
    for a in (-0.1, -0.2, -0.4):
        bg = quintessence_background(a)
        tr[f"quintessence_alpha_{a}"] = dict(
            z=traj_z, w=[float(bg["w"](z)) for z in traj_z],
            rho_DE_over_rho_DE0=[float(bg["rho_DE"](z)) for z in traj_z],
            t_c_Gyr=bg["t_c_Gyr"])
    for xi in (0.05, 0.2):
        bg = interacting_background(xi)
        tr[f"interacting_xi_{xi}"] = dict(
            z=traj_z, w_eff=[float(bg["w"](z)) for z in traj_z],
            rho_DE_over_rho_DE0=[float(bg["rho_DE"](z)) for z in traj_z],
            t_c_Gyr=bg["t_c_Gyr"])
    out["trajectories"] = tr

    out["qc"] = qc_checks({
        "quintessence_alpha_-0.4": quintessence_background(-0.4),
        "interacting_xi_0.05": interacting_background(0.05),
    })
    out["qc"]["lcdm_DH_over_rd_at_z0.51"] = distances(Eref, 0.510)[1]
    out["qc"]["lcdm_DM_over_rd_at_z0.51"] = distances(Eref, 0.510)[0]
    out["qc"]["note"] = ("E(z=0) must equal 1 by construction; rho_DE must be "
                         "non-decreasing with z because rho_dot_phi = "
                         "-3 H phidot^2 <= 0. The two LambdaCDM distances are "
                         "printed so the pipeline can be checked against any "
                         "published DR2 central value later (GAP-3).")

    out["named_gaps"] = [
        "GAP-2: no citable DESI DR2-era f*sigma8 measurement with an "
        "uncertainty was obtained in this lane, so the growth observable -- the "
        "one that separates the k-essence member (M3) from the canonical one -- "
        "is NOT computed. It is not estimated.",
        "GAP-1 (from cross_table.py): the turnaround criterion is frame-"
        "dependent for non-minimally coupled scalars, so Branch I classes D and "
        "E have no Set-T verdict.",
        "GAP-3: DR2 central values were not obtained from a citable source in "
        "this lane, so no goodness-of-fit to the data is computed; only "
        "model-vs-LambdaCDM separations in units of the published sigma.",
    ]

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "observable_separation.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2)

    # ---- report ----------------------------------------------------------
    print("ROW 23 -- STEP 2 OBSERVABLE SEPARATION")
    print("=" * 84)
    print(f"reference LambdaCDM: Omega_m={OMEGA_M}, h*r_d={H_RD_MPC} Mpc, "
          f"h={H_LITTLE:.4f}, Omega_r={OMEGA_R:.3e}, 1/H0={HUBBLE_TIME_GYR:.4f} Gyr")
    r = out["ruler_wCDM"]
    print(f"\nRULER wCDM w={RULER_W}: max|Delta|={r['max_abs_delta']:.2f} sigma, "
          f"Delta_tot(indep)={r['delta_tot_independent']:.2f}, "
          f"Delta_tot(block)={r['delta_tot_block_cov']:.2f}")
    print("\nM1 zero-crossing quintessence (linear potential, thawing):")
    print(f"{'alpha':>7}{'w0':>9}{'t_c [Gyr]':>12}{'a_turn':>11}"
          f"{'max|D|':>9}{'D_indep':>9}{'D_block':>9}  worst")
    for m in m1:
        wp = m["worst_point"]
        print(f"{m['alpha']:>7.3f}{m['w0']:>9.4f}{m['t_c_Gyr']:>12.4g}"
              f"{m['a_turnaround']:>11.3g}{m['max_abs_delta']:>9.2f}"
              f"{m['delta_tot_independent']:>9.2f}{m['delta_tot_block_cov']:>9.2f}"
              f"  {wp['tracer']} {wp['obs']}")
    b = out["M1_boundary"]
    if "alpha_star" in b:
        print(f"\n  BOUNDARY: max|Delta| = 1 sigma at alpha* = {b['alpha_star']:.4f}, "
              f"w0* = {b['w0_star']:.4f}, t_c* = {b['t_c_star_Gyr']:.1f} Gyr "
              f"(Delta_tot block = {b['delta_tot_block_cov']:.2f})")
    print("\nM2 interacting dark sector (sustained drain):")
    print(f"{'xi':>7}{'w0_eff':>9}{'t_c [Gyr]':>12}{'a_turn':>11}"
          f"{'max|D|':>9}{'D_indep':>9}{'D_block':>9}  worst")
    for m in m2:
        wp = m["worst_point"]
        print(f"{m['xi']:>7.3f}{m['w0_eff']:>9.4f}{m['t_c_Gyr']:>12.4g}"
              f"{m['a_turnaround']:>11.3g}{m['max_abs_delta']:>9.2f}"
              f"{m['delta_tot_independent']:>9.2f}{m['delta_tot_block_cov']:>9.2f}"
              f"  {wp['tracer']} {wp['obs']}")
    b2 = out["M2_boundary"]
    if "xi_star" in b2:
        print(f"\n  BOUNDARY: max|Delta| = 1 sigma at xi* = {b2['xi_star']:.5f}, "
              f"w0_eff* = {b2['w0_eff']:.4f}, t_c* = {b2['t_c_star_Gyr']:.1f} Gyr")
    print("\nM1b quadratic-top potential (shape robustness):")
    print(f"{'m^2':>7}{'w0':>9}{'t_c [Gyr]':>12}{'a_turn':>11}{'max|D|':>9}{'D_block':>9}")
    for m in out["M1b_quadratic_top_scan"]:
        print(f"{m['m2']:>7.2f}{m['w0']:>9.4f}{m['t_c_Gyr']:>12.4g}"
              f"{m['a_turnaround']:>11.3g}{m['max_abs_delta']:>9.2f}"
              f"{m['delta_tot_block_cov']:>9.2f}")

    bq = out.get("M1b_boundary", {})
    if "t_c_star_Gyr" in bq:
        print(f"  BOUNDARY (quadratic top): m^2* = {bq['m2_star']:.4f}, "
              f"w0* = {bq['w0_star']:.4f}, t_c* = {bq['t_c_star_Gyr']:.1f} Gyr")
    bu = out.get("boundary_universality", {})
    if bu:
        print(f"  UNIVERSALITY: t_c* ratio linear/quadratic = {bu['t_c_ratio']:.2f}; "
              f"w0* = {bu['w0_star_linear']:.4f} vs {bu['w0_star_quadratic_top']:.4f} "
              f"(spread {bu['w0_spread']:.4f})")

    k = out.get("marginalisation_calibration", {})
    if k:
        print(f"\n  ruler calibration: {k['ruler_fixed_param_max_abs_delta']:.2f} "
              f"fixed-param sigma per {k['ruler_marginalised_sigma']:.2f} "
              f"marginalised sigma  ->  kappa = "
              f"{k['kappa_fixed_param_sigma_per_marginalised_sigma']:.2f}")
    bk = out.get("M1_boundary_marginalisation_calibrated", {})
    if "t_c_Gyr" in bk:
        print(f"  CALIBRATED BOUNDARY (~1 sigma marginalised): alpha = "
              f"{bk['alpha']:.4f}, w0 = {bk['w0']:.4f}, "
              f"t_c = {bk['t_c_Gyr']:.1f} Gyr")
    print(f"\n  QC: {json.dumps(out['qc'])[:400]}")
    if "robustness" in out:
        print(f"\nrobustness at alpha*: {out['robustness']}")
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()

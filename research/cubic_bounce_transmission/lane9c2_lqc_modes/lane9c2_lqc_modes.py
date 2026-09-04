#!/usr/bin/env python3
"""Lane 9c-2 - EXACT dressed-metric modes on the LQC-dust bounce, three initial
states, and the scheme-S1 bounce-window in-in integral over k*eta_B in [0.1, 10].

Executes the computation named in the lane-9c verdict
(../lane9c_abs_operator/LANE9C_ABS_OPERATOR_2026-09-04.md sec. 5): lane (b)'s
in-in machinery run OUTSIDE its super-Hubble reduction, with the initial state
varied, to test whether the Agullo-Bolliet-Sreenath 2017 (arXiv:1712.08148)
enhancement of f_NL near k*eta_B ~ 1 appears in the lab's model.

Reuses, unmodified and by import:
  ../a2_transmission_linear.py        LQC-dust background, a''/a = x^(1/3)(1/6 + x/3),
                                      matter-basis projection, adiabatic dust vacuum
  ../lane_b_numerical/bounce_cubic_inin.py   the S1 vertex set V1-V7, redefinition
                                      terms R1-R4, the in-in convention, f_NL = (5/6)B/sum(PP)

Only the INITIAL STATE of the mode functions and the k-range are new.  No vertex
coefficient, kernel, or convention is altered.  Nothing is tuned to any target.

States (all normalised to the Wronskian Im(mu* mu') = -1/2):
  S-lab   the lab's adiabatic (exact dust) contraction vacuum imposed at eta -> -eta_far,
          mu = exp(-i k tau)(1 - i/(k tau))/sqrt(2k)      [A2 sec. 4; a2.evolve ic='vacuum']
  S-ABS0  adiabatic-order-zero (Minkowski positive-frequency) vacuum imposed at a FIXED
          pre-bounce time eta_0, mu = exp(-i k eta)/sqrt(2k), mu' = -i k mu
          [ABS sec. IV F: their state at eta_0 = -281.5 T_Pl "is only of adiabatic order zero"]
  S-ad4   4th-order adiabatic (WKB) vacuum imposed at the same eta_0 when k^2 > W(eta_0),
          otherwise at the latest pre-bounce time with k^2 >= 4 W(eta) (recorded per k)
"""
import json
import os
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp, cumulative_trapezoid

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "lane_b_numerical"))
import a2_transmission_linear as a2          # noqa: E402
import bounce_cubic_inin as lb               # noqa: E402

LOG = os.path.join(HERE, "lane9c2_lqc_modes.log")
JSON_OUT = os.path.join(HERE, "results.json")
_lines = []


def log(m=""):
    print(m)
    _lines.append(m)


# ---------------------------------------------------------------- configuration
SQUEEZE = 0.02                    # k_long/k_short, squeezed isoceles (same as lane b)
K_SCAN = [0.1, 0.3, 1.0, 3.0, 10.0]          # k*eta_B, the row-9 band
K_GATE = 1e-3                                 # gate point (lane b's headline k)
ETA0_FAC = -3.0                               # headline fixed pre-bounce time, in eta_B
ETA0_SCAN = [-2.0, -3.0, -10.0, -30.0, -100.0]
ETA_STAR_FAC = 10.0                           # headline eta_*/eta_B for the k-scan
ETA_STAR_SCAN = [2.0, 5.0, 10.0, 30.0]
ABS_PLATEAU = 1.0e3                           # ABS sec. IV B / VII |f_NL| plateau
ABS_DECAY = 1.830229                          # exp(-alpha k_t/k_LQC) -> exp(-1.83 k eta_B), lane 9c sec. 2.2
K_LQC_ETAB = 1.060146                         # lane 9c sec. 2.2, LQC dust


# =====================================================================
# [S] initial states
# =====================================================================
def _W_tools(bg):
    """W(eta) = a''/a as a spline, plus a helper for smooth local derivatives."""
    return CubicSpline(bg["eta"], bg["appa"])


def _adiabatic_order4(Wspl, k, eta0, half=None, npts=4001):
    """4th-order adiabatic (WKB) vacuum at eta0 for mu'' + (k^2 - W) mu = 0.

    omega0^2 = k^2 - W;  Omega_(2)^2 = omega0^2 - (1/2)(omega0''/omega0) + (3/4)(omega0'/omega0)^2
               Omega_(4)^2 = omega0^2 - (1/2)(Omega_2''/Omega_2) + (3/4)(Omega_2'/Omega_2)^2
    mu = (2 Omega_(4))^(-1/2),  mu' = (-i Omega_(4) - Omega_(4)'/(2 Omega_(4))) mu
    (overall phase irrelevant; Wronskian Im(mu* mu') = -1/2 exactly).
    Returns (mu0, dmu0, diagnostics) or (None, None, reason).
    """
    if half is None:
        half = max(0.02 * abs(eta0), 1e-3)
    e = np.linspace(eta0 - half, eta0 + half, npts)
    w2 = k * k - Wspl(e)
    if np.any(w2 <= 0):
        return None, None, {"defined": False, "reason": "k^2 - W <= 0 in the WKB window"}
    w0 = np.sqrt(w2)
    s0 = CubicSpline(e, w0)
    O2sq = w2 - 0.5 * s0.derivative(2)(e) / w0 + 0.75 * (s0.derivative(1)(e) / w0) ** 2
    if np.any(O2sq <= 0):
        return None, None, {"defined": False, "reason": "2nd-order adiabatic Omega^2 <= 0"}
    O2 = np.sqrt(O2sq)
    s2 = CubicSpline(e, O2)
    O4sq = w2 - 0.5 * s2.derivative(2)(e) / O2 + 0.75 * (s2.derivative(1)(e) / O2) ** 2
    if np.any(O4sq <= 0):
        return None, None, {"defined": False, "reason": "4th-order adiabatic Omega^2 <= 0"}
    O4 = np.sqrt(O4sq)
    s4 = CubicSpline(e, O4)
    Om, dOm = float(s4(eta0)), float(s4.derivative(1)(eta0))
    mu0 = 1.0 / np.sqrt(2.0 * Om) + 0.0j
    dmu0 = (-1j * Om - dOm / (2.0 * Om)) * mu0
    diag = {"defined": True, "Omega4": Om, "omega0": float(np.interp(eta0, e, w0)),
            "adiabaticity_dOmega_over_Omega2": float(abs(dOm) / Om ** 2)}
    return mu0, dmu0, diag


def _find_ad4_time(Wspl, bg, k, eta0, margin=4.0):
    """Latest pre-bounce eta <= eta0 with k^2 >= margin * W(eta); None if there is none."""
    e = -np.geomspace(abs(eta0), 0.95 * bg["eta_far"], 4000)
    ok = k * k >= margin * Wspl(e)
    if not np.any(ok):
        return None
    return float(e[np.argmax(ok)])


class ModesIC:
    """mu'' + (k^2 - a''/a) mu = 0 with a selectable initial state.

    Exposes the interface lane (b)'s vertex_fnl/redef_fnl consume:
    zeta_dz(eta) -> (zeta, dzeta/deta) with zeta = mu/a (scheme S1: z = a).
    """

    def __init__(self, bg, k, state, eta_far, eta0=None, rtol=1e-11, atol=1e-14):
        self.bg, self.k, self.state = bg, float(k), state
        self.af = bg["af"]
        self.apf = bg["af"].derivative()
        Wspl = _W_tools(bg)
        self.info = {"state": state}
        if state == "S-lab":
            e_i = -eta_far
            tau_i = e_i - bg["eta_off"]
            u = k * tau_i
            mu0 = np.exp(-1j * u) * (1 - 1j / u) / np.sqrt(2 * k)
            dmu0 = (np.exp(-1j * u) * (-1j * k) * (1 - 1j / u)
                    + np.exp(-1j * u) * (1j / (k * tau_i ** 2))) / np.sqrt(2 * k)
            self.info["eta_start"] = float(e_i)
        elif state == "S-ABS0":
            e_i = float(eta0)
            mu0 = np.exp(-1j * k * e_i) / np.sqrt(2 * k)
            dmu0 = -1j * k * mu0
            self.info["eta_start"] = e_i
            self.info["k2_over_W_at_eta0"] = float(k * k / Wspl(e_i))
        elif state == "S-ad4":
            e_i = float(eta0)
            mu0, dmu0, diag = _adiabatic_order4(Wspl, k, e_i)
            if mu0 is None:
                e_alt = _find_ad4_time(Wspl, bg, k, eta0)
                if e_alt is None or abs(e_alt) > 0.9 * eta_far:
                    self.ok = False
                    self.info.update({"defined": False, "reason": diag["reason"]})
                    return
                mu0, dmu0, diag = _adiabatic_order4(Wspl, k, e_alt)
                if mu0 is None:
                    self.ok = False
                    self.info.update({"defined": False, "reason": diag["reason"]})
                    return
                e_i = e_alt
                self.info["relocated"] = True
            self.info["eta_start"] = float(e_i)
            self.info.update(diag)
        else:
            raise ValueError(state)
        wr0 = float(np.imag(np.conj(mu0) * dmu0))
        self.info["wronskian_initial"] = wr0
        e_f = eta_far
        sol = solve_ivp(lb.a2._rhs_factory(CubicSpline(bg["eta"], bg["appa"]), k),
                        [e_i, e_f], [mu0.real, dmu0.real, mu0.imag, dmu0.imag],
                        rtol=rtol, atol=atol, method="DOP853", dense_output=True)
        self.sol = sol
        self.ok = bool(sol.success)
        self.info["ode_success"] = self.ok

    def _mu(self, eta):
        y = self.sol.sol(eta)
        return y[0] + 1j * y[2], y[1] + 1j * y[3]

    def zeta_dz(self, eta):
        mu, dmu = self._mu(eta)
        a, ap = self.af(eta), self.apf(eta)
        return mu / a, (dmu - mu * ap / a) / a

    def zeta_dz_closed(self, eta):
        raise RuntimeError("closed-form super-Hubble modes are not used in lane 9c-2")

    def wronskian(self, eta):
        mu, dmu = self._mu(eta)
        return float(np.imag(np.conj(mu) * dmu))


# =====================================================================
# [G] growth factor and power-spectrum modification
# =====================================================================
def adiabatic_occupation(m, bg, Wspl, eta):
    """N_tot(eta) = omega |mu|^2 + |mu'|^2/omega = |alpha|^2 + |beta|^2 relative to the
    INSTANTANEOUS adiabatic vacuum (exact identity to WKB accuracy; = 1 in that vacuum).
    Oscillation-free, so it is the envelope measure used for the growth factor.
    Returns (N_tot, omega) or (nan, nan) where omega^2 <= 0 (no adiabatic vacuum)."""
    w2 = m.k ** 2 - float(Wspl(eta))
    if w2 <= 0:
        return float("nan"), float("nan")
    w = np.sqrt(w2)
    mu, dmu = m._mu(eta)
    return float(w * abs(mu) ** 2 + abs(dmu) ** 2 / w), float(w)


def wkb_reference_time(bg, Wspl, k, factor=10.0, lo=10.0, hi=0.9):
    """Smallest |eta| >= lo*eta_B with k^2 >= factor*W(eta) (WKB-safe on BOTH sides;
    the LQC-dust background is exactly time-symmetric, a(-eta) = a(eta))."""
    e = np.geomspace(lo * bg["eta_B"], hi * bg["eta_far"], 6000)
    ok = k * k >= factor * Wspl(e)
    if not np.any(ok):
        return None
    return float(e[np.argmax(ok)])


def growth_factor(m, bg, Wspl, eta_ref):
    """|zeta_after / zeta_before| across the bounce, envelope-averaged.

    The background is time-symmetric, so a(+eta_ref) = a(-eta_ref) and
      |zeta|^2_avg = N_tot/(2 omega a^2)  =>  |zeta_after/zeta_before| = sqrt(N_+/N_-).
    The power-spectrum modification is its square."""
    Nm, wm = adiabatic_occupation(m, bg, Wspl, -eta_ref)
    Np, wp = adiabatic_occupation(m, bg, Wspl, +eta_ref)
    if not np.isfinite(Nm) or not np.isfinite(Np) or Nm <= 0:
        return dict(defined=False, reason="omega^2 <= 0 at eta_ref")
    G = float(np.sqrt(Np / Nm))
    return dict(defined=True, eta_ref=float(eta_ref), N_before=Nm, N_after=Np,
                omega=float(wp), growth_factor=G, power_modification=float(G ** 2),
                beta_sq_after=float(max(0.0, (Np - 1.0) / 2.0)),
                beta_sq_before=float(max(0.0, (Nm - 1.0) / 2.0)))

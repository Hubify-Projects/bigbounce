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
ETA_STAR_SCAN = [1.0, 2.0, 5.0, 10.0, 30.0]
ABS_PLATEAU = 1.0e3                           # ABS sec. IV B / VII |f_NL| plateau
ABS_DECAY = 1.830229                          # exp(-alpha k_t/k_LQC) -> exp(-1.83 k eta_B), lane 9c sec. 2.2
K_LQC_ETAB = 1.060146                         # lane 9c sec. 2.2, LQC dust


# =====================================================================
# [S] initial states
# =====================================================================
def _W_tools(bg):
    """W(eta) = a''/a as a spline, plus a helper for smooth local derivatives."""
    return CubicSpline(bg["eta"], bg["appa"])


def _adiabatic_order4(Wspl, k, eta0, half=None, npts=801):
    """4th-order adiabatic (WKB) vacuum at eta0 for mu'' + (k^2 - W) mu = 0.

    omega0^2 = k^2 - W;  Omega_(2)^2 = omega0^2 - (1/2)(omega0''/omega0) + (3/4)(omega0'/omega0)^2
               Omega_(4)^2 = omega0^2 - (1/2)(Omega_2''/Omega_2) + (3/4)(Omega_2'/Omega_2)^2
    mu = (2 Omega_(4))^(-1/2),  mu' = (-i Omega_(4) - Omega_(4)'/(2 Omega_(4))) mu
    (overall phase irrelevant; Wronskian Im(mu* mu') = -1/2 exactly).
    Returns (mu0, dmu0, diagnostics) or (None, None, reason).
    """
    if half is None:
        for h in (0.25, 0.10, 0.04, 0.015):
            r = _adiabatic_order4(Wspl, k, eta0, half=h * abs(eta0), npts=npts)
            if r[0] is not None:
                r[2]["window_half_over_eta0"] = h
                return r
        return r
    e = np.linspace(eta0 - half, eta0 + half, npts)
    w2 = k * k - Wspl(e)
    if np.any(w2 <= 0):
        return None, None, {"defined": False, "reason": "k^2 - W <= 0 in the WKB window"}
    # derivatives are taken from a degree-10 least-squares polynomial in (eta - eta0),
    # NOT from nested cubic splines: W itself is a spline of the background grid, so its
    # 3rd/4th derivatives are numerically meaningless and would spuriously drive
    # Omega^2 negative.  The polynomial is a smoothing filter of the adiabatic window.
    def _poly(y):
        return np.polynomial.Polynomial.fit(e - eta0, y, 10).convert()

    w0 = np.sqrt(w2)
    p0 = _poly(w0)
    O2sq = w2 - 0.5 * p0.deriv(2)(e - eta0) / w0 + 0.75 * (p0.deriv(1)(e - eta0) / w0) ** 2
    if np.any(O2sq <= 0):
        return None, None, {"defined": False, "reason": "2nd-order adiabatic Omega^2 <= 0"}
    O2 = np.sqrt(O2sq)
    p2 = _poly(O2)
    O4sq = w2 - 0.5 * p2.deriv(2)(e - eta0) / O2 + 0.75 * (p2.deriv(1)(e - eta0) / O2) ** 2
    if np.any(O4sq <= 0):
        return None, None, {"defined": False, "reason": "4th-order adiabatic Omega^2 <= 0"}
    O4 = np.sqrt(O4sq)
    p4 = _poly(O4)
    Om, dOm = float(p4(0.0)), float(p4.deriv(1)(0.0))
    mu0 = 1.0 / np.sqrt(2.0 * Om) + 0.0j
    dmu0 = (-1j * Om - dOm / (2.0 * Om)) * mu0
    diag = {"defined": True, "Omega4": Om, "omega0": float(np.interp(eta0, e, w0)),
            "adiabaticity_dOmega_over_Omega2": float(abs(dOm) / Om ** 2)}
    return mu0, dmu0, diag


def _find_ad4_time(Wspl, bg, k, eta0, margin=10.0):
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
                if e_alt is not None and abs(e_alt) <= 0.9 * eta_far:
                    mu0, dmu0, diag2 = _adiabatic_order4(Wspl, k, e_alt)
                    if mu0 is None:
                        diag = diag2
                    else:
                        e_i = e_alt
                        diag = diag2
                        self.info["relocated"] = True
                else:
                    diag = {"reason": diag.get("reason",
                                               "no pre-bounce time on the grid with k^2 >= 10 W")}
            if mu0 is None:
                # No 4th-order adiabatic vacuum exists at any finite pre-bounce time on
                # this grid (the leg is super-Hubble throughout).  Fall back to the exact
                # dust positive-frequency solution at eta -> -eta_far, which IS the
                # adiabatic vacuum to all orders in that asymptotic region.  Recorded.
                e_i = -eta_far
                tau_i = e_i - bg["eta_off"]
                u = k * tau_i
                mu0 = np.exp(-1j * u) * (1 - 1j / u) / np.sqrt(2 * k)
                dmu0 = (np.exp(-1j * u) * (-1j * k) * (1 - 1j / u)
                        + np.exp(-1j * u) * (1j / (k * tau_i ** 2))) / np.sqrt(2 * k)
                diag = {"defined": True, "fallback_far_past_exact_vacuum": True,
                        "fallback_reason": diag.get("reason")}
            self.info["eta_start"] = float(e_i)
            self.info.update(diag)
        else:
            raise ValueError(state)
        wr0 = float(np.imag(np.conj(mu0) * dmu0))
        self.info["wronskian_initial"] = wr0
        rhs = a2._rhs_factory(CubicSpline(bg["eta"], bg["appa"]), k)
        y0 = [mu0.real, dmu0.real, mu0.imag, dmu0.imag]
        self.e_i = float(e_i)
        # forward from the state-setting time; and, when the state is set at a finite
        # eta_0, BACKWARD as well - a mode function is a solution of a 2nd-order ODE, so
        # its past is determined and the pre-bounce envelope is measurable.
        fwd = solve_ivp(rhs, [e_i, eta_far], y0, rtol=rtol, atol=atol,
                        method="DOP853", dense_output=True)
        self.fwd = fwd
        self.bwd = None
        ok = bool(fwd.success)
        if e_i > -eta_far + 1e-9:
            bwd = solve_ivp(rhs, [e_i, -eta_far], y0, rtol=rtol, atol=atol,
                            method="DOP853", dense_output=True)
            self.bwd = bwd
            ok = ok and bool(bwd.success)
        self.ok = ok
        self.info["ode_success"] = ok

    def _mu(self, eta):
        e = np.asarray(eta, dtype=float)
        if self.bwd is None:
            y = self.fwd.sol(e)
        elif e.ndim == 0:
            y = (self.fwd.sol(e) if float(e) >= self.e_i else self.bwd.sol(e))
        else:
            y = np.where(e >= self.e_i, self.fwd.sol(e), self.bwd.sol(e))
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


# =====================================================================
# [F] Delta f_NL^bounce with exact modes
# =====================================================================
def dfnl(bg, modes, ks, D, eta_star, npts=20001):
    """Scheme-S1 bounce-window in-in: bulk V1-V7 over [-eta_B, eta_B] + redefinition
    R1-R4 at eta_*.  Machinery imported verbatim from lane (b)."""
    eB = bg["eta_B"]
    fv, P, Psum = lb.vertex_fnl(bg, modes, ks, D, -eB, eB, eta_star, npts=npts)
    fr, H = lb.redef_fnl(bg, modes, ks, D, eta_star)
    bulk, red = sum(fv.values()), sum(fr.values())
    dom = max(fv, key=lambda n: abs(fv[n]))
    return dict(vertices={n: float(v) for n, v in fv.items()},
                redefinition={n: float(v) for n, v in fr.items()},
                bulk_sum=float(bulk), redef_sum=float(red), total=float(bulk + red),
                dominant_vertex=dom,
                dominant_vertex_fraction=float(abs(fv[dom]) / abs(bulk)) if bulk else None,
                P=[float(p) for p in P], eta_star_over_etaB=float(eta_star / eB))


def build_modes(bg, ks, state, eta_far, eta0):
    ms = [ModesIC(bg, float(kk), state, eta_far, eta0=eta0) for kk in ks]
    if not all(getattr(m, "ok", False) for m in ms):
        return None, [m.info for m in ms]
    return ms, [m.info for m in ms]


def run_gate(bg, eta_far, out):
    """GATE (implemented first): at k*eta_B = 1e-3 with the lab state, the exact-mode
    pipeline must reproduce lane (b)'s LQC total to <= 1e-3 relative."""
    ref_path = os.path.join(HERE, "..", "lane_b_numerical", "results.json")
    ref = json.load(open(ref_path))["backgrounds"]["lqc"]
    row = [e for e in ref["k_scan"] if abs(e["k_etaB"] - K_GATE) < 1e-12][0]
    eB = bg["eta_B"]
    k = K_GATE / eB
    ks = np.array([SQUEEZE * k, k, k])
    D = lb._dots(*ks)
    ms, info = build_modes(bg, ks, "S-lab", eta_far, None)
    assert ms is not None, info
    es = row["eta_star_over_etaB"] * eB
    got = dfnl(bg, ms, ks, D, es, npts=8001)
    rel = abs(got["total"] - row["total"]) / abs(row["total"])
    rel_analytic = abs(got["total"] - (-5.0 / 48.0)) / (5.0 / 48.0)
    passed = bool(rel <= 1e-3)
    log(f"\n[GATE] k*eta_B = {K_GATE}, state S-lab, eta_* = {row['eta_star_over_etaB']:g} eta_B")
    log(f"  lane (b) total   = {row['total']:+.10f}")
    log(f"  lane 9c-2 total  = {got['total']:+.10f}   rel = {rel:.3e}   -> {'PASS' if passed else 'FAIL'}")
    log(f"  lane (a) closed form -5/48 = {-5/48:+.10f}   rel(9c-2 vs -5/48) = {rel_analytic:.3e}")
    rho_B = abs(float(bg["Jf"](-eB))) / bg["I_inf"]
    v2_closed = -5.0 / 24.0 * rho_B
    rel_v2 = abs(got["vertices"]["V2"] - v2_closed) / abs(v2_closed)
    log(f"  V2 alone = {got['vertices']['V2']:+.10f} vs lane (a) closed form -(5/24)rho_B = "
        f"{v2_closed:+.10f}   rel = {rel_v2:.3e}")
    log(f"  (the -5/48 closed form describes V2 only; the total additionally carries "
        f"V3+V4+V6+V7 and R1-R4)")
    log(f"  Wronskian Im(mu* mu') = {np.mean([m.wronskian(0.0) for m in ms]):+.9f} (exact -0.5)")
    out["gate"] = dict(k_etaB=K_GATE, laneB_total=row["total"], lane9c2_total=got["total"],
                       rel_vs_laneB=float(rel), tolerance=1e-3, passed=passed,
                       analytic_minus_5_over_48=-5.0 / 48.0,
                       rel_vs_analytic=float(rel_analytic),
                       rho_B=float(rho_B), V2_closed_form=float(v2_closed),
                       V2_numeric=float(got["vertices"]["V2"]), rel_V2_vs_closed=float(rel_v2),
                       gate_note=("the -5/48 = -(5/24)rho_B closed form is the V2 vertex alone; "
                                  "the 1.4e-3 offset of the TOTAL is the genuine subleading "
                                  "V3+V4+V6+V7 + R1-R4 content, not a numerical error"),
                       wronskian=float(np.mean([m.wronskian(0.0) for m in ms])),
                       vertices=got["vertices"], redefinition=got["redefinition"])
    return passed


# =====================================================================
def main():
    t0 = time.time()
    log("=" * 78)
    log("Lane 9c-2: exact dressed-metric modes + S1 bounce-window in-in, k*eta_B in [0.1,10]")
    log("=" * 78)
    bg = a2.bg_lqc()
    eB, Wspl = bg["eta_B"], _W_tools(bg)
    eta_far = min(0.9 * bg["eta_far"], 300.0 * eB)
    log(f"background {bg['label']}: eta_B = {eB:.6f}, I_inf = {bg['I_inf']:.6f}, "
        f"A = {bg['A']:.6f}, eta_far(used) = {eta_far:.4g}")
    log(f"scheme S1 (z = a, eps_eff = 1/2, c_s = 1); squeezed isoceles k1 = {SQUEEZE} k, k2 = k3 = k")

    out = {"date": "2026-09-04", "lane": "9c-2",
           "background": {"label": bg["label"], "eta_B": float(eB), "I_inf": float(bg["I_inf"]),
                          "A": float(bg["A"]), "eta_far_used": float(eta_far),
                          "potential": "W = a''/a = x^(1/3)(1/6 + x/3), x = rho/rho_c (dressed/geometric)"},
           "scheme": "S1 (geometric, z = a, eps_eff = 1/2, c_s = 1); vertices+conventions imported from lane (b)",
           "configuration": {"squeeze": SQUEEZE, "k_scan_k_etaB": K_SCAN,
                             "eta0_headline_over_etaB": ETA0_FAC, "eta0_scan": ETA0_SCAN,
                             "eta_star_headline_over_etaB": ETA_STAR_FAC,
                             "eta_star_scan": ETA_STAR_SCAN},
           "states": {"S-lab": "adiabatic (exact dust) contraction vacuum at eta -> -eta_far (A2 sec. 4)",
                      "S-ABS0": "adiabatic-order-zero Minkowski vacuum at fixed eta_0 (ABS sec. IV F)",
                      "S-ad4": "4th-order adiabatic (WKB) vacuum at eta_0 (relocated earlier if k^2 <= W)"},
           "gate": {}, "modes": {}, "dfnl": {}, "eta_star_systematic": {}, "eta0_systematic": {},
           "abs_comparison": {}}

    if not run_gate(bg, eta_far, out):
        log("\n[GATE FAILED] no downstream number is reported.")
        _dump(out)
        return

    # ---------------- (1) exact modes: growth factor + power modification ----------
    log(f"\n{'=' * 78}\n(1) exact modes: growth factor |zeta_after/zeta_before| and P/P_vac")
    log(f"{'k*eta_B':>8s} {'state':>8s} {'eta_ref/eta_B':>13s} {'N_before':>11s} {'N_after':>11s} "
        f"{'|z_a/z_b|':>11s} {'P/P_before':>12s} {'|beta|^2_after':>15s}")
    eta0 = ETA0_FAC * eB
    for kt in K_SCAN:
        k = kt / eB
        eref = wkb_reference_time(bg, Wspl, k)
        rec = {}
        for st in ("S-lab", "S-ABS0", "S-ad4"):
            m = ModesIC(bg, k, st, eta_far, eta0=eta0)
            if not getattr(m, "ok", False):
                rec[st] = {"defined": False, "info": m.info}
                log(f"{kt:8.3g} {st:>8s}   UNDEFINED: {m.info.get('reason')}")
                continue
            g = growth_factor(m, bg, Wspl, eref) if eref else {"defined": False,
                                                               "reason": "no WKB-safe eta_ref"}
            g["info"] = m.info
            rec[st] = g
            if g.get("defined"):
                log(f"{kt:8.3g} {st:>8s} {eref / eB:13.2f} {g['N_before']:11.4f} {g['N_after']:11.4f} "
                    f"{g['growth_factor']:11.4f} {g['power_modification']:12.4f} "
                    f"{g['beta_sq_after']:15.4f}")
            else:
                log(f"{kt:8.3g} {st:>8s}   growth UNDEFINED: {g.get('reason')}")
        out["modes"][f"{kt:g}"] = rec

    # ---------------- (2)/(3) Delta f_NL^bounce per state ------------------------
    log(f"\n{'=' * 78}\n(2)-(3) Delta f_NL^bounce (squeezed isoceles), eta_* = {ETA_STAR_FAC:g} eta_B")
    log(f"{'k*eta_B':>8s} {'state':>8s} {'bulk':>14s} {'redef':>14s} {'TOTAL':>14s} "
        f"{'dominant':>9s} {'frac':>7s}")
    for kt in K_SCAN + [K_GATE]:
        k = kt / eB
        ks = np.array([SQUEEZE * k, k, k])
        D = lb._dots(*ks)
        es = ETA_STAR_FAC * eB
        rec = {}
        for st in ("S-lab", "S-ABS0", "S-ad4"):
            ms, info = build_modes(bg, ks, st, eta_far, eta0)
            if ms is None:
                rec[st] = {"defined": False, "info": info}
                log(f"{kt:8.3g} {st:>8s}   UNDEFINED (mode construction failed)")
                continue
            npts = int(max(20001, 400 * max(1.0, kt)))
            r = dfnl(bg, ms, ks, D, es, npts=npts)
            r["defined"] = True
            r["npts"] = npts
            rec[st] = r
            log(f"{kt:8.3g} {st:>8s} {r['bulk_sum']:+14.6e} {r['redef_sum']:+14.6e} "
                f"{r['total']:+14.6e} {r['dominant_vertex']:>9s} "
                f"{(r['dominant_vertex_fraction'] or float('nan')):7.3f}")
        out["dfnl"][f"{kt:g}"] = rec

    # ---------------- systematics: eta_* and eta_0 --------------------------------
    log(f"\n{'=' * 78}\nsystematic A: eta_* dependence (zeta is NOT conserved once k*eta_* > 1)")
    for kt in K_SCAN:
        k = kt / eB
        ks = np.array([SQUEEZE * k, k, k])
        D = lb._dots(*ks)
        rec = {}
        for st in ("S-lab", "S-ABS0"):
            ms, _ = build_modes(bg, ks, st, eta_far, eta0)
            if ms is None:
                continue
            vals = []
            for f in ETA_STAR_SCAN:
                r = dfnl(bg, ms, ks, D, f * eB, npts=int(max(20001, 400 * max(1.0, kt))))
                vals.append({"eta_star_over_etaB": f, "total": r["total"],
                             "k_eta_star": float(k * f * eB)})
            tt = [v["total"] for v in vals]
            spread = float((max(tt) - min(tt)) / abs(np.mean(tt))) if np.mean(tt) else float("nan")
            rec[st] = {"scan": vals, "frac_spread": spread}
            log(f"  k*eta_B={kt:6.3g} {st:>7s}: " + "  ".join(
                f"{v['eta_star_over_etaB']:g}eB:{v['total']:+.3e}" for v in vals)
                + f"   frac spread {spread:+.2e}")
        out["eta_star_systematic"][f"{kt:g}"] = rec

    log(f"\nsystematic B: eta_0 dependence of the ABS-style order-zero state (k*eta_B = 1)")
    kt = 1.0
    k = kt / eB
    ks = np.array([SQUEEZE * k, k, k])
    D = lb._dots(*ks)
    eref = wkb_reference_time(bg, Wspl, k)
    e0rec = []
    for f0 in ETA0_SCAN:
        e0 = f0 * eB
        m = ModesIC(bg, k, "S-ABS0", eta_far, eta0=e0)
        g = growth_factor(m, bg, Wspl, eref)
        ms, _ = build_modes(bg, ks, "S-ABS0", eta_far, e0)
        r = dfnl(bg, ms, ks, D, ETA_STAR_FAC * eB) if ms else None
        e0rec.append({"eta0_over_etaB": f0, "k2_over_W": m.info.get("k2_over_W_at_eta0"),
                      "growth_factor": g.get("growth_factor"),
                      "power_modification": g.get("power_modification"),
                      "total": r["total"] if r else None})
        log(f"  eta_0 = {f0:7g} eta_B: k^2/W = {m.info.get('k2_over_W_at_eta0'):9.3e}  "
            f"|z_a/z_b| = {g.get('growth_factor', float('nan')):10.4f}  "
            f"Delta f_NL = {(r['total'] if r else float('nan')):+.4e}")
    out["eta0_systematic"] = {"k_etaB": kt, "scan": e0rec}

    # ---------------- (4) comparison to ABS --------------------------------------
    log(f"\n{'=' * 78}\n(4) comparison to Agullo-Bolliet-Sreenath 2017 (arXiv:1712.08148)")
    log(f"  their plateau |f_NL| ~ {ABS_PLATEAU:g} for k <~ k_LQC (their sec. IV B, sec. VII);")
    log(f"  their decay exp(-alpha k_t/k_LQC) -> exp(-{ABS_DECAY:.3f} k*eta_B) equilateral (their sec. V);")
    log(f"  k_LQC*eta_B = {K_LQC_ETAB:.4f} on the lab's LQC-dust background (lane 9c sec. 2.2).")
    comp = {}
    for kt in K_SCAN:
        abs_pred = ABS_PLATEAU * np.exp(-ABS_DECAY * (kt - K_LQC_ETAB))
        row = out["dfnl"][f"{kt:g}"]
        e = {}
        for st in ("S-lab", "S-ABS0", "S-ad4"):
            v = row.get(st, {})
            if not v.get("defined"):
                e[st] = None
                continue
            e[st] = {"total": v["total"],
                     "ratio_to_ABS": float(abs(v["total"]) / abs_pred),
                     "log10_gap_dex": float(np.log10(abs_pred / max(abs(v["total"]), 1e-300)))}
        comp[f"{kt:g}"] = {"ABS_extrapolated_|f_NL|": float(abs_pred), "lab": e}
        log(f"  k*eta_B = {kt:5g}: ABS ~ {abs_pred:10.3e} | " + " | ".join(
            f"{st} {e[st]['total']:+.3e} ({e[st]['log10_gap_dex']:+.2f} dex)" if e[st] else f"{st} n/a"
            for st in ("S-lab", "S-ABS0", "S-ad4")))
    out["abs_comparison"] = {
        "ABS_plateau_fNL": ABS_PLATEAU, "ABS_decay_per_k_etaB": ABS_DECAY,
        "k_LQC_eta_B": K_LQC_ETAB,
        "ABS_law": "|Delta f_NL^bounce| ~ 1e3 exp(-1.830 (k*eta_B - 1.060)) (equilateral; lane 9c sec. 3.1)",
        "per_k": comp,
        "caveat": ("ABS use a kinetic-dominated scalar (w=+1, eps=3) with ~12.3 e-folds of inflation "
                   "after the bounce and their f_NL convention differs by an overall sign; only "
                   "magnitudes are compared.")}
    # ---------------- systematic C: configuration (ABS quote equilateral) --------
    log(f"\nsystematic C: equilateral configuration (k1 = k2 = k3 = k), eta_* = {ETA_STAR_FAC:g} eta_B")
    eq = {}
    for kt in K_SCAN:
        k = kt / eB
        ks = np.array([k, k, k])
        D = lb._dots(*ks)
        rec = {}
        for st in ("S-lab", "S-ABS0"):
            ms, _ = build_modes(bg, ks, st, eta_far, eta0)
            if ms is None:
                continue
            r = dfnl(bg, ms, ks, D, ETA_STAR_FAC * eB, npts=int(max(20001, 400 * max(1.0, kt))))
            rec[st] = {"total": r["total"], "bulk_sum": r["bulk_sum"],
                       "redef_sum": r["redef_sum"], "dominant_vertex": r["dominant_vertex"],
                       "vertices": r["vertices"], "redefinition": r["redefinition"]}
        ms, _ = build_modes(bg, ks, "S-lab", eta_far, eta0)
        scan = []
        for f in ETA_STAR_SCAN:
            rr = dfnl(bg, ms, ks, D, f * eB, npts=int(max(20001, 400 * max(1.0, kt))))
            scan.append({"eta_star_over_etaB": f, "k_eta_star": float(k * f * eB),
                         "total": rr["total"], "redef_R3": rr["redefinition"]["R3"]})
        rec["eta_star_scan_S-lab"] = scan
        eq[f"{kt:g}"] = rec
        log("  k*eta_B = %6.3g: " % kt + "  ".join(
            f"{st} {rec[st]['total']:+.4e}" for st in ("S-lab", "S-ABS0") if st in rec)
            + "  | eta_* scan (S-lab): " + " ".join(
            f"{v['eta_star_over_etaB']:g}eB:{v['total']:+.3e}" for v in scan))
    out["equilateral"] = eq

    # ---------------- (5) PBH channel at k*eta_B ~ 3 ------------------------------
    # zeta = zeta_g + (3/5) f_NL zeta_g^2 ; collapse threshold zeta_c ; sigma_g = 3.2e-5
    # (lane 9c sec. 4 item 1, which quoted 408 sigma for |f_NL| = 1e3 at zeta_c = 0.1).
    log(f"\n{'=' * 78}\n(5) PBH channel at k*eta_B = 3: required Gaussian excursion")
    sigma_g = float(np.sqrt(1e-9))      # Delta^2_zeta ~ 1e-9 (A3-1b); lane 9c used this value
    pbh = {}

    def _zg_full(fnl, zc):
        """smallest zeta_g > 0 with zeta_g + (3/5) f_NL zeta_g^2 = zeta_c; None if the
        threshold is unreachable (f_NL < 0 turns zeta over at zeta_g = -1/(2c))."""
        c = 0.6 * fnl
        if c == 0.0:
            return zc
        disc = 1.0 + 4.0 * c * zc
        if disc < 0.0:
            return None
        roots = [r for r in ((-1.0 + np.sqrt(disc)) / (2.0 * c),
                             (-1.0 - np.sqrt(disc)) / (2.0 * c)) if r > 0]
        return float(min(roots)) if roots else None

    for label, fnl in [("Gaussian (f_NL = 0)", 0.0),
                       ("lane 9c-2 S-lab at k*eta_B = 3", out["dfnl"]["3"]["S-lab"]["total"]),
                       ("lane 9c-2 S-ABS0 at k*eta_B = 3", out["dfnl"]["3"]["S-ABS0"]["total"]),
                       ("ABS-magnitude hypothesis |f_NL| = 1e3", 1000.0)]:
        for zc in (0.1, 0.7):
            zg = _zg_full(fnl, zc)
            # lane 9c's criterion: the NON-GAUSSIAN TERM ALONE reaches zeta_c
            zg_ng = float(np.sqrt(zc / (0.6 * abs(fnl)))) if fnl != 0 else None
            pbh[f"{label} | zeta_c={zc}"] = {
                "f_NL": float(fnl), "zeta_c": zc,
                "zeta_g_full_quadratic": zg,
                "n_sigma_full_quadratic": (float(zg / sigma_g) if zg else None),
                "zeta_g_NG_term_only": zg_ng,
                "n_sigma_NG_term_only": (float(zg_ng / sigma_g) if zg_ng else None)}
            log(f"  {label:38s} zeta_c={zc:4g}: full quadratic "
                f"{('%8.1f sigma' % (zg / sigma_g)) if zg else '   unreachable'}"
                f"   | NG-term-only "
                f"{('%8.1f sigma' % (zg_ng / sigma_g)) if zg_ng else '        n/a'}")
    out["pbh_tail"] = {"sigma_g": sigma_g, "convention": "zeta = zeta_g + (3/5) f_NL zeta_g^2",
                       "cases": pbh,
                       "note": ("A3-1b's null is a 7.0 dex deficit in Delta^2_zeta; lane 9c "
                                "recorded 408 sigma for |f_NL| = 1e3 at zeta_c = 0.1 using the "
                                "NG-term-only criterion, reproduced here as an anchor.")}

    _dump(out)
    make_figures(out)
    log(f"\nDONE ({time.time() - t0:.1f} s)")


def _dump(out):
    with open(JSON_OUT, "w") as fh:
        json.dump(out, fh, indent=2)
    with open(LOG, "w") as fh:
        fh.write("\n".join(_lines) + "\n")


# =====================================================================
def make_figures(out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    ks = [float(x) for x in out["modes"].keys()]
    styles = {"S-lab": ("o-", "C0"), "S-ABS0": ("s-", "C3"), "S-ad4": ("^-", "C2")}

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    for st, (mk, c) in styles.items():
        xs, ys = [], []
        for kt in ks:
            r = out["modes"][f"{kt:g}"].get(st, {})
            if r.get("defined"):
                xs.append(kt)
                ys.append(r["growth_factor"])
        if xs:
            ax.plot(xs, ys, mk, color=c, ms=5, lw=1.4, label=st)
    ax.axvline(out["abs_comparison"]["k_LQC_eta_B"], color="0.4", ls=":", lw=1,
               label=r"$k_{\rm LQC}\eta_B=1.06$")
    ax.axhline(1.0, color="0.7", lw=0.8)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"$k\,\eta_B$")
    ax.set_ylabel(r"$|\zeta_{\rm after}/\zeta_{\rm before}|$  (envelope)")
    ax.set_title("Lane 9c-2: bounce growth factor, LQC-dust dressed metric", fontsize=10)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "lane9c2_growth_factor.png"), dpi=140)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    for st, (mk, c) in styles.items():
        xs, ys = [], []
        for kt in ks:
            r = out["dfnl"][f"{kt:g}"].get(st, {})
            if r.get("defined"):
                xs.append(kt)
                ys.append(abs(r["total"]))
        if xs:
            ax.plot(xs, ys, mk, color=c, ms=5, lw=1.4, label=st)
    if out.get("equilateral"):
        xs = [float(x) for x in out["equilateral"]]
        ys = [abs(out["equilateral"][f"{x:g}"]["S-lab"]["total"]) for x in xs]
        ax.plot(xs, ys, "d--", color="C1", ms=5, lw=1.2,
                label=r"S-lab, equilateral ($\eta_*=10\eta_B$)")
    kk = np.geomspace(0.1, 10, 200)
    ax.plot(kk, out["abs_comparison"]["ABS_plateau_fNL"]
            * np.exp(-out["abs_comparison"]["ABS_decay_per_k_etaB"]
                     * (kk - out["abs_comparison"]["k_LQC_eta_B"])),
            "k--", lw=1.2, label=r"ABS 2017: $10^3e^{-1.83(k\eta_B-1.06)}$")
    ax.axvline(out["abs_comparison"]["k_LQC_eta_B"], color="0.4", ls=":", lw=1)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"$k\,\eta_B$")
    ax.set_ylabel(r"$|\Delta f_{\rm NL}^{\rm bounce}|$  (scheme S1)")
    ax.set_title(r"Lane 9c-2: $\Delta f_{\rm NL}^{\rm bounce}$ vs initial state", fontsize=10)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "lane9c2_dfnl_bounce.png"), dpi=140)
    plt.close(fig)


if __name__ == "__main__":
    main()

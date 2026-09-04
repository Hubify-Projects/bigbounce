#!/usr/bin/env python3
"""Lane (b) - numerical bounce-window in-in evaluation of Delta f_NL^bounce.

Ledger item #2 (second half).  Uses lane (a)'s vertex table + regularisation
prescription (../lane_a_vertex_table/) and the A2 backgrounds/mode functions of
../a2_transmission_linear.py.  In-in conventions follow the lab adjudication
engine (research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py
Sec. 1): B = -2 Im[ u1u2u3(eta_*) int d eta c_V^conf(eta) sum_{S3} K_V prod_j
T_j[u*] ], f_NL = (5/6) B / (P1P2+P1P3+P2P3); the 3! leg attachments are each
counted once and no hand symmetry factors are inserted.

Scheme S1 (geometric / dressed-metric extension): z = a, eps_eff = 1/2, c_s = 1,
eta_sr = 0, s = 0, lambda = 0.  S2 (effective fluid) is reported ONLY as a
divergence diagnostic (d_cut scaling exponent), never as a number.

The contraction-phase value f_NL^before = -35/16 is an INPUT (ledger #1), not
recomputed here.

Nothing in this script is tuned to any target value.
"""
import json
import os
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import a2_transmission_linear as a2  # noqa: E402

LOG = os.path.join(HERE, "bounce_cubic_inin.log")
JSON_OUT = os.path.join(HERE, "results.json")
_lines = []


def log(m=""):
    print(m)
    _lines.append(m)


# =====================================================================
# [V] The S1 vertex set (lane (a) table, eps -> 1/2, c_s -> 1, lambda -> 0)
# =====================================================================
# Each vertex: conformal-time coefficient c^conf(eta) (c_V^cosmic * a^{1-n_dot},
# with any explicit 1/a^2 of the operator absorbed), a slot list (which leg
# carries zeta and which carries zeta' at time eta), and a momentum kernel
# K(i, j, l) where (i, j, l) is the leg triple assigned to slots (1, 2, 3).
#
#   V1  zetadot^3                     c = -a^3/H [eps H^2 (1-1/c_s^2)/c_s^2 + 2 lam]  -> 0 in S1
#   V2  zeta zetadot^2                c = a^3 eps (eps-3+3c_s^2)/c_s^4 = a^3/4  -> c^conf = a^2/4
#   V3  zeta (d zeta)^2 / a^2         c = a eps (eps-2s+1-c_s^2)/c_s^2 = a/4    -> c^conf = 1/4
#   V4  zetadot (d zeta)(d chit)      c = -2 a^3 eps^2/c_s^4 = -a^3/2           -> c^conf = -a^2/2
#   V5  zeta^2 zetadot                c propto d/dt(eta_sr/c_s^2)               -> 0 in S1
#   V6  (d zeta)(d chit) d^2 chit     c = a^3 eps^3/(2 c_s^4) = a^3/16          -> c^conf = a^2/16
#   V7  d^2 zeta (d chit)^2           c = a^3 eps^3/(4 c_s^4) = a^3/32          -> c^conf = a^2/32
#
# chit = del^-2 zetadot  =>  chit_k = -zetadot_k / k^2   (del^-2 -> -1/k^2).


def _dots(k1, k2, k3):
    """k_i . k_j for a closed triangle k1 + k2 + k3 = 0."""
    ks = [k1, k2, k3]
    D = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            if i == j:
                D[i, j] = ks[i] ** 2
            else:
                l = 3 - i - j
                D[i, j] = 0.5 * (ks[l] ** 2 - ks[i] ** 2 - ks[j] ** 2)
    return D


VERTICES = {
    "V1": dict(slots=("d", "d", "d"), coeff=lambda a, ks, D: 0.0 * a,
               kern=lambda i, j, l, ks, D: 1.0,
               note="zetadot^3; coefficient vanishes identically in S1 (c_s=1, lambda=0)"),
    "V2": dict(slots=("z", "d", "d"), coeff=lambda a, ks, D: a ** 2 / 4.0,
               kern=lambda i, j, l, ks, D: 1.0,
               note="zeta zetadot^2, c^conf = a^2 eps_eff^2 = a^2/4"),
    "V3": dict(slots=("z", "z", "z"), coeff=lambda a, ks, D: 0.25 + 0.0 * a,
               kern=lambda i, j, l, ks, D: -D[j, l],
               note="zeta (d zeta)^2/a^2, c^conf = eps_eff^2 = 1/4; kernel -(k_j.k_l)"),
    "V4": dict(slots=("d", "z", "d"), coeff=lambda a, ks, D: -a ** 2 / 2.0,
               kern=lambda i, j, l, ks, D: D[j, l] / ks[l] ** 2,
               note="zetadot (d zeta)(d chit); kernel +(k_j.k_l)/k_l^2 (slot3 carries chit)"),
    "V5": dict(slots=("z", "z", "d"), coeff=lambda a, ks, D: 0.0 * a,
               kern=lambda i, j, l, ks, D: 1.0,
               note="zeta^2 zetadot; coefficient propto d/dt(eta_sr) = 0 in S1"),
    "V6": dict(slots=("z", "d", "d"), coeff=lambda a, ks, D: a ** 2 / 16.0,
               kern=lambda i, j, l, ks, D: D[i, j] / ks[j] ** 2,
               note="(d zeta)(d chit) d^2 chit; kernel (k_i.k_j)/k_j^2"),
    "V7": dict(slots=("z", "d", "d"), coeff=lambda a, ks, D: a ** 2 / 32.0,
               kern=lambda i, j, l, ks, D: ks[i] ** 2 * D[j, l] / (ks[j] ** 2 * ks[l] ** 2),
               note="d^2 zeta (d chit)^2; kernel k_i^2 (k_j.k_l)/(k_j^2 k_l^2)"),
}

PERMS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

# Field redefinition zeta = zeta_n + f(zeta_n) in S1 (eta_sr = 0, eps = 1/2, c_s = 1):
#   R1  eta_sr/(4 c_s^2) zeta^2                                       -> 0 in S1
#   R2  zeta zetadot / (c_s^2 H)                       F = 1/H,      slots (z, d), K = 1
#   R3  [-(d zeta)^2 + del^-2 d_i d_j(d_i zeta d_j zeta)]/(4 a^2 H^2)
#                                                       F = 1/(4 a^2 H^2), slots (z, z),
#                                                       K = (p.q) - (k.p)(k.q)/k^2
#   R4  eps[(d zeta)(d chit) - del^-2 d_i d_j(d_i zeta d_j chit)]/(2 c_s^2 H)
#                                                       F = eps/(2H) = 1/(4H), slots (z, d),
#                                                       K = (p.q)/q^2 - (k.p)(k.q)/(k^2 q^2)
REDEF = {
    "R1": dict(slots=("z", "z"), F=lambda a, H: 0.0, kern=lambda c, p, q, ks, D: 1.0,
               note="eta_sr zeta^2/4; eta_sr = 0 in S1"),
    "R2": dict(slots=("z", "d"), F=lambda a, H: 1.0 / H, kern=lambda c, p, q, ks, D: 1.0,
               note="zeta zetadot / H"),
    "R3": dict(slots=("z", "z"), F=lambda a, H: 1.0 / (4.0 * a ** 2 * H ** 2),
               kern=lambda c, p, q, ks, D: D[p, q] - D[c, p] * D[c, q] / ks[c] ** 2,
               note="geometric gradient boundary term / (4 a^2 H^2)"),
    "R4": dict(slots=("z", "d"), F=lambda a, H: 1.0 / (4.0 * H),
               kern=lambda c, p, q, ks, D: (D[p, q] / ks[q] ** 2
                                            - D[c, p] * D[c, q] / (ks[c] ** 2 * ks[q] ** 2)),
               note="eps[(d zeta)(d chit) - ...]/(2H), eps_eff = 1/2"),
}


# =====================================================================
# [M] mode functions on a background (S1: zeta = mu/a)
# =====================================================================
class Modes:
    """Numerically evolved zeta_k(eta), zeta'_k(eta) from the A2 adiabatic vacuum."""

    def __init__(self, bg, k, eta_far, rtol=1e-11, atol=1e-14):
        self.bg, self.k = bg, float(k)
        self.ev = a2.evolve(bg, k, eta_far, ic="vacuum", rtol=rtol, atol=atol)
        self.af = bg["af"]
        self.apf = bg["af"].derivative()
        # closed-form super-Hubble reference (A2 Sec. 3): zeta = C1 + C2 J
        am, bm = self.ev["alpha_pre"], self.ev["beta_pre"]
        self.C1, self.C2 = am + bm * bg["I_inf"], bm

    def zeta(self, eta):
        y = self.ev["sol"].sol(eta)
        mu = y[0] + 1j * y[2]
        return mu / self.af(eta)

    def zeta_dz(self, eta):
        """(zeta, dzeta/deta) from the ODE solution."""
        y = self.ev["sol"].sol(eta)
        mu, dmu = y[0] + 1j * y[2], y[1] + 1j * y[3]
        a, ap = self.af(eta), self.apf(eta)
        return mu / a, (dmu - mu * ap / a) / a

    def zeta_dz_closed(self, eta):
        J = self.bg["Jf"](eta)
        return self.C1 + self.C2 * J, self.C2 / self.af(eta) ** 2

    def wronskian(self, eta):
        y = self.ev["sol"].sol(eta)
        mu, dmu = y[0] + 1j * y[2], y[1] + 1j * y[3]
        return float(np.imag(np.conj(mu) * dmu))     # must equal -1/2


def _grid(e1, e2, n):
    return np.linspace(e1, e2, n)


def _simps(y, x):
    from scipy.integrate import simpson
    return float(simpson(y, x=x))


def _simps_c(y, x):
    return _simps(np.real(y), x) + 1j * _simps(np.imag(y), x)


def vertex_fnl(bg, modes, ks, D, e1, e2, eta_star, npts=4001, closed=False):
    """f_NL contribution of every bulk vertex over the window [e1, e2]."""
    eta = _grid(e1, e2, npts)
    a = bg["af"](eta)
    getter = (lambda m: m.zeta_dz_closed(eta)) if closed else (lambda m: m.zeta_dz(eta))
    z, dz = zip(*[getter(m) for m in modes])                    # per-leg arrays
    zs = [m.zeta_dz_closed(eta_star)[0] if closed else m.zeta_dz(eta_star)[0] for m in modes]
    pref = zs[0] * zs[1] * zs[2]
    P = [float(abs(v) ** 2) for v in zs]
    Psum = P[0] * P[1] + P[0] * P[2] + P[1] * P[2]
    out = {}
    for name, V in VERTICES.items():
        c = V["coeff"](a, ks, D)
        tot = np.zeros_like(eta, dtype=complex)
        for (i, j, l) in PERMS:
            legs = (i, j, l)
            amp = np.ones_like(eta, dtype=complex)
            for slot, leg in zip(V["slots"], legs):
                amp = amp * (np.conj(z[leg]) if slot == "z" else np.conj(dz[leg]))
            tot = tot + V["kern"](i, j, l, ks, D) * amp
        integral = _simps_c(c * tot, eta)
        B = -2.0 * float(np.imag(pref * integral))
        out[name] = 5.0 / 6.0 * B / Psum
    return out, P, Psum


def redef_fnl(bg, modes, ks, D, eta_star, closed=False):
    """f_NL from the field-redefinition (boundary) terms evaluated at eta_*."""
    a = float(bg["af"](eta_star))
    ap = float(bg["af"].derivative()(eta_star))
    H = ap / a ** 2
    vals = [(m.zeta_dz_closed(eta_star) if closed else m.zeta_dz(eta_star)) for m in modes]
    Q = {}
    for i, (z, dz) in enumerate(vals):
        Q[("z", i)] = float(abs(z) ** 2)                       # <zeta zeta>
        Q[("d", i)] = float(np.real(dz / a * np.conj(z)))       # <zetadot zeta>, cosmic time
    P = [Q[("z", i)] for i in range(3)]
    Psum = P[0] * P[1] + P[0] * P[2] + P[1] * P[2]
    out = {}
    for name, R in REDEF.items():
        F = R["F"](a, H)
        B = 0.0
        for c in range(3):                                     # which leg carries f
            p, q = [x for x in range(3) if x != c]
            for (pp, qq) in [(p, q), (q, p)]:
                B += F * R["kern"](c, pp, qq, ks, D) * Q[(R["slots"][0], pp)] * Q[(R["slots"][1], qq)]
        out[name] = 5.0 / 6.0 * B / Psum
    return out, H


# =====================================================================
# [S2] divergence diagnostic (never a number)
# =====================================================================
def s2_divergence(bg, dcuts=(3e-2, 1e-2, 3e-3, 1e-3, 3e-4)):
    """Effective-fluid scheme: the V6+V7 (eps^3, constraint-sector) bounce-window
    integrand has an even t^-2 pole.  Excise |eta| < d_cut and fit the scaling
    exponent of the bare integral  int c^conf_{V6+V7} (zeta')^2 d eta  with the S2
    super-Hubble mode zeta' = C2/z^2, z^2 = 2 a^2 eps.  Reports the exponent only."""
    eB = bg["eta_B"]
    af = bg["af"]
    a1, a2_, a3 = af.derivative(1), af.derivative(2), af.derivative(3)

    def integrand(e):
        a = af(e)
        ap, app = a1(e), a2_(e)
        H = ap / a ** 2
        Hp = app / a ** 2 - 2.0 * ap ** 2 / a ** 3      # dH/deta
        Hdot = Hp / a
        eps = -Hdot / H ** 2
        z2 = 2.0 * a ** 2 * eps
        # c^conf_{V6+V7} = (3/4) a^2 eps^3 ; two zeta' legs carry 1/z2 each
        return 0.75 * a ** 2 * eps ** 3 / z2 ** 2

    vals = []
    for d in dcuts:
        e = np.concatenate([-np.geomspace(eB, d * eB, 20001),
                            np.geomspace(d * eB, eB, 20001)])
        vals.append(abs(float(np.trapezoid(integrand(e), e))))
    x, y = np.log(np.array(dcuts)), np.log(np.array(vals))
    slope = float(np.polyfit(x, y, 1)[0])
    return dict(dcuts=list(dcuts), values=vals, log_log_slope=slope,
                statement=("effective-fluid (S2) V6+V7 bounce-window integral has no d_cut -> 0 "
                           "limit; the fitted scaling exponent is reported, NOT a regulated value"))


# =====================================================================
def main():
    t0 = time.time()
    log("=" * 78)
    log("Lane (b): numerical bounce-window in-in evaluation of Delta f_NL^bounce  (2026-09-03)")
    log("=" * 78)
    log("scheme S1 (geometric, z = a, eps_eff = 1/2, c_s = 1); contraction value -35/16 is INPUT")

    SQUEEZE = 0.02          # k_long / k_short, squeezed isoceles
    KT = np.array([1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1])   # k eta_B band
    ETA_STAR_FAC = 150.0     # eta_* / eta_B; deep post-bounce so J(eta_*) -> I_inf

    out = {"date": "2026-09-03", "scheme": "S1 (geometric, z=a, eps_eff=1/2, c_s=1)",
           "conventions": {
               "in_in": ("B = -2 Im[ u1u2u3(eta_*) int d eta c_V^conf(eta) sum_{sigma in S3} "
                         "K_V(sigma) prod_j T_j[u*_{sigma j}(eta)] ]; all 3! attachments counted "
                         "once, no hand symmetry factors (lab adjudication engine Sec. 1)"),
               "fNL": "f_NL = (5/6) B / (P1 P2 + P1 P3 + P2 P3)",
               "configuration": f"squeezed isoceles, k1 = {SQUEEZE} k, k2 = k3 = k",
               "contraction_input": -35.0 / 16.0},
           "vertices": {k: v["note"] for k, v in VERTICES.items()},
           "redefinition": {k: v["note"] for k, v in REDEF.items()},
           "gates": {}, "backgrounds": {}, "S2_divergence": {}}

    # ---- gate: local redefinition normalisation F zeta^2 -> f_NL = (5/3) F ----
    ks_t = np.array([0.3, 1.0, 1.0])
    D_t = _dots(*ks_t)
    Ftest = 0.37
    Pt = np.array([2.0, 3.0, 5.0])
    Bt = sum(2 * Ftest * Pt[p] * Pt[q] for (p, q) in [(1, 2), (0, 2), (0, 1)])
    fnl_t = 5.0 / 6.0 * Bt / (Pt[0] * Pt[1] + Pt[0] * Pt[2] + Pt[1] * Pt[2])
    log(f"\n[gate] local redefinition F zeta^2 -> f_NL = {fnl_t:.10f} vs (5/3)F = "
        f"{5 / 3 * Ftest:.10f}  (diff {abs(fnl_t - 5 / 3 * Ftest):.2e})")
    assert abs(fnl_t - 5 / 3 * Ftest) < 1e-12
    out["gates"]["local_redefinition_5over3"] = dict(value=fnl_t, expected=5 / 3 * Ftest)

    # ---- gate: triangle closure of the dot-product table ----
    kk = np.array([SQUEEZE, 1.0, 1.0])
    Dc = _dots(*kk)
    clos = max(abs(Dc[i, 0] + Dc[i, 1] + Dc[i, 2]) for i in range(3))
    log(f"[gate] triangle closure sum_j k_i.k_j = 0: max residual {clos:.2e}")
    assert clos < 1e-12
    out["gates"]["triangle_closure_residual"] = clos

    bgs = {"quintin": a2.bg_quintin(dtB=1.0), "lqc": a2.bg_lqc(), "poly": a2.bg_poly(eta_b=1.0)}

    for bkey, bg in bgs.items():
        eB, Ii = bg["eta_B"], bg["I_inf"]
        rho_B = abs(float(bg["Jf"](-eB))) / Ii
        T_lin = 0.5 * (1.0 - rho_B)
        eta_far = min(0.9 * bg["eta_far"], 300.0 * eB)
        log(f"\n{'=' * 74}\n[{bg['label']}]  eta_B={eB:.6f}  I_inf={Ii:.6f}  A={bg['A']:.6f}  "
            f"rho_B={rho_B:.6f}  T_fNL={T_lin:.6f}  eta_far={eta_far:.4g}")
        brec = dict(label=bg["label"], params=bg["params"], eta_B=eB, I_inf=Ii, A=bg["A"],
                    rho_B=rho_B, T_fNL_linear=T_lin, eta_far=eta_far, k_scan=[])

        for kt in KT:
            k = kt / eB
            ks = np.array([SQUEEZE * k, k, k])
            D = _dots(*ks)
            modes = [Modes(bg, kk_, eta_far) for kk_ in ks]
            if not all(m.ev["success"] for m in modes):
                log(f"  k eta_B = {kt:.4g}: ODE FAILED - skipped")
                continue
            wr = [m.wronskian(0.0) for m in modes]
            # eta_* must be (i) deep post-bounce so J(eta_*) -> I_inf and (ii) still
            # super-Hubble, k eta_* << 1.  Both are satisfiable only for k eta_B << 1.
            esf = min(ETA_STAR_FAC, max(10.0, 0.05 / kt), 0.85 * eta_far / eB)
            eta_star = esf * eB
            J_star_over_Iinf = float(bg['Jf'](eta_star)) / Ii
            valid = bool(k * eta_star < 0.3 and J_star_over_Iinf > 0.99)

            fv, P, Psum = vertex_fnl(bg, modes, ks, D, -eB, eB, eta_star)
            fv_c, _, _ = vertex_fnl(bg, modes, ks, D, -eB, eB, eta_star, closed=True)
            fr, Hstar = redef_fnl(bg, modes, ks, D, eta_star)
            bulk = sum(fv.values())
            red = sum(fr.values())
            tot = bulk + red
            closed_V2 = -5.0 / 24.0 * rho_B

            log(f"  k eta_B = {kt:.4g}  (k = {k:.5g}, k_L = {ks[0]:.5g})   Wronskian Im(mu* mu') = "
                f"{np.mean(wr):+.8f} (exact -0.5)")
            for name in VERTICES:
                log(f"     {name}: {fv[name]:+.6e}   [closed-form modes {fv_c[name]:+.6e}]")
            for name in REDEF:
                log(f"     {name}: {fr[name]:+.6e}   (boundary, at eta_* = {esf:g} eta_B)")
            log(f"     bulk sum = {bulk:+.6f}   redef sum = {red:+.6e}   TOTAL Delta f_NL^bounce "
                f"= {tot:+.6f}   [eta_*={esf:g} eta_B, k eta_*={k * eta_star:.3f}, "
                f"J_*/I_inf={J_star_over_Iinf:.5f}, VALID={valid}]")
            log(f"     lane (a) closed form for V2 alone: -(5/24) rho_B = {closed_V2:+.6f}; "
                f"numeric V2 = {fv['V2']:+.6f}  (rel {abs(fv['V2'] - closed_V2) / abs(closed_V2):.2e})")

            brec["k_scan"].append(dict(
                k_etaB=float(kt), k=float(k), k_long=float(ks[0]),
                wronskian=[float(w) for w in wr], eta_star_over_etaB=float(esf),
                J_star_over_Iinf=float(J_star_over_Iinf), k_eta_star=float(k * eta_star),
                valid=valid,
                vertices={n: float(v) for n, v in fv.items()},
                vertices_closed_form_modes={n: float(v) for n, v in fv_c.items()},
                redefinition={n: float(v) for n, v in fr.items()},
                bulk_sum=float(bulk), redef_sum=float(red), total=float(tot),
                laneA_closed_form_V2=float(closed_V2),
                V2_rel_diff_vs_laneA=float(abs(fv["V2"] - closed_V2) / abs(closed_V2)),
                P=[float(p) for p in P]))

        # ------------- tests at a reference k -------------
        kt_ref = 1e-3
        k = kt_ref / eB
        ks = np.array([SQUEEZE * k, k, k])
        D = _dots(*ks)
        modes = [Modes(bg, kk_, eta_far) for kk_ in ks]
        es_ref = min(ETA_STAR_FAC, 0.05 / kt_ref, 0.85 * eta_far / eB) * eB

        # (i) eta_*-independence: bulk integrated up to eta_*, plus boundary terms at eta_*
        log(f"\n  [test] eta_*-independence (k eta_B = {kt_ref}); bulk over [-eta_B, eta_*] "
            f"+ redefinition at eta_*")
        estar_scan = []
        for fac in (2.0, 5.0, 10.0, 20.0, 50.0, 150.0, 250.0):
            if fac * kt_ref > 0.3:
                continue
            es = fac * eB
            if es > 0.85 * eta_far:
                continue
            fv, _, _ = vertex_fnl(bg, modes, ks, D, -eB, es, es, npts=8001)
            fr, _ = redef_fnl(bg, modes, ks, D, es)
            estar_scan.append(dict(eta_star_over_etaB=fac, bulk=float(sum(fv.values())),
                                   redef=float(sum(fr.values())),
                                   total=float(sum(fv.values()) + sum(fr.values()))))
            log(f"     eta_* = {fac:5g} eta_B (k eta_* = {k * es:.3f}) : bulk {estar_scan[-1]['bulk']:+.6f}  redef "
                f"{estar_scan[-1]['redef']:+.3e}  total {estar_scan[-1]['total']:+.6f}")
        tt = [e["total"] for e in estar_scan]
        spread = (max(tt) - min(tt)) / abs(np.mean(tt)) if tt else float("nan")
        tf = [e["total"] for e in estar_scan if e["eta_star_over_etaB"] >= 10.0]
        spread_far = (max(tf) - min(tf)) / abs(np.mean(tf)) if tf else float("nan")
        log(f"     => fractional spread of the total over eta_*: {spread:.3e} (all), "
            f"{spread_far:.3e} for eta_* >= 10 eta_B")

        # (ii) window independence: vary eta_1, eta_2 about the NEC boundary
        log("  [test] window independence (bounce-window edges)")
        win_scan = []
        for f1 in (0.8, 1.0, 1.5, 2.0, 3.0):
            fv, _, _ = vertex_fnl(bg, modes, ks, D, -f1 * eB, f1 * eB, es_ref, npts=8001)
            win_scan.append(dict(window_over_etaB=f1, bulk=float(sum(fv.values())),
                                 V2=float(fv["V2"])))
            log(f"     [-{f1:g},{f1:g}] eta_B : bulk {win_scan[-1]['bulk']:+.6f}   "
                f"V2 {win_scan[-1]['V2']:+.6f}")

        # (iii) step-size convergence
        log("  [test] step-size convergence of the bulk integral")
        conv = []
        for n in (1001, 2001, 4001, 8001, 16001):
            fv, _, _ = vertex_fnl(bg, modes, ks, D, -eB, eB, es_ref, npts=n)
            conv.append(dict(npts=n, bulk=float(sum(fv.values()))))
            log(f"     npts = {n:6d} : bulk {conv[-1]['bulk']:+.10f}")
        rel = abs(conv[-1]["bulk"] - conv[-2]["bulk"]) / abs(conv[-1]["bulk"])
        log(f"     => last-halving relative change {rel:.2e}")

        brec["eta_star_ref"] = float(es_ref / eB)
        brec["tests"] = dict(eta_star_scan=estar_scan, eta_star_frac_spread=float(spread),
                             eta_star_frac_spread_far=float(spread_far),
                             window_scan=win_scan, step_convergence=conv,
                             step_convergence_rel=float(rel))
        brec["S2"] = s2_divergence(bg)
        log(f"  [S2] effective-fluid V6+V7 bounce-window integral vs d_cut: log-log slope "
            f"{brec['S2']['log_log_slope']:+.4f}  (divergence, no regulated number quoted)")
        out["backgrounds"][bkey] = brec

    # ---- combined statement ----
    log(f"\n{'=' * 74}\n[combined] f_NL^after = T_fNL * (-35/16) + Delta f_NL^bounce   (S1, k eta_B << 1)")
    comb = {}
    for bkey, brec in out["backgrounds"].items():
        ref = [e for e in brec["k_scan"] if e["valid"]]
        head = min(ref, key=lambda e: e["k_etaB"]) if ref else None
        d = float(np.mean([e["total"] for e in ref])) if ref else float("nan")
        dsp = float(np.max([e["total"] for e in ref]) - np.min([e["total"] for e in ref])) if ref else float("nan")
        T = brec["T_fNL_linear"]
        before = -35.0 / 16.0
        dom = max(head["vertices"], key=lambda n: abs(head["vertices"][n])) if head else None
        comb[bkey] = dict(T_fNL=T, transmitted=T * before,
                          headline_k_etaB=head["k_etaB"] if head else None,
                          headline_total=head["total"] if head else None,
                          headline_f_NL_after=(T * before + head["total"]) if head else None,
                          dominant_vertex=dom,
                          dominant_vertex_fraction=(abs(head["vertices"][dom]) / abs(head["bulk_sum"]))
                          if head else None, dfnl_bounce=d,
                          dfnl_bounce_spread_over_k=dsp, f_NL_after=T * before + d)
        log(f"  {brec['label']:>22s}: T = {T:.6f}, T*(-35/16) = {T * before:+.6f}, "
            f"Delta f_NL^bounce = {d:+.6f}  ->  f_NL^after = {T * before + d:+.6f}")
    out["combined"] = comb
    out["validity"] = ("super-Hubble, k eta_B << 1; S1 cubic coefficients are the lane (a) scheme "
                       "assumption (eps -> 1/2, c_s -> 1), NOT the dressed-metric H_3 of Agullo+2017; "
                       "P(X,phi) cubic action only (no Horndeski/Galileon terms); first-order in-in")

    log(f"\nDONE ({time.time() - t0:.1f} s)")
    with open(JSON_OUT, "w") as fh:
        json.dump(out, fh, indent=2)
    with open(LOG, "w") as fh:
        fh.write("\n".join(_lines) + "\n")
    make_figures(out)


def make_figures(out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    for bkey, brec in out["backgrounds"].items():
        ks_ = [e["k_etaB"] for e in brec["k_scan"]]
        if not ks_:
            continue
        fig, ax = plt.subplots(figsize=(6.2, 4.4))
        for name in ["V2", "V3", "V4", "V6", "V7"]:
            ax.plot(ks_, [e["vertices"][name] for e in brec["k_scan"]], "o-", ms=4, lw=1, label=name)
        ax.plot(ks_, [e["total"] for e in brec["k_scan"]], "s-", color="k", ms=5, lw=2, label="total")
        bad = [e["k_etaB"] for e in brec["k_scan"] if not e["valid"]]
        if bad:
            ax.axvspan(min(bad), max(ks_) * 1.3, color="0.85", zorder=0)
            ax.text(min(bad) * 1.1, 0.02, "outside validity\n($k\\eta_*\\gtrsim0.3$)",
                    fontsize=7, va="bottom")
        ax.set_ylim(-0.35, 0.12)
        ax.axhline(-5.0 / 24.0 * brec["rho_B"], color="r", ls="--", lw=1,
                   label=r"lane (a) $-\frac{5}{24}\rho_B$")
        ax.set_xscale("log")
        ax.set_xlabel(r"$k\,\eta_B$")
        ax.set_ylabel(r"$\Delta f_{\rm NL}^{\rm bounce}$  (scheme S1)")
        ax.set_title(f"{brec['label']}  ($\\rho_B$ = {brec['rho_B']:.4f})", fontsize=10)
        ax.legend(fontsize=7, ncol=2)
        ax.grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig(os.path.join(HERE, f"dfnl_bounce_{bkey}.png"), dpi=140)
        plt.close(fig)


if __name__ == "__main__":
    main()

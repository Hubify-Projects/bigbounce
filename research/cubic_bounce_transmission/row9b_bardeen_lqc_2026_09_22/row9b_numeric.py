#!/usr/bin/env python3
"""Leg B of row 9b: the Bardeen linear transfer lambda_zeta on the LQC and poly backgrounds.

Equations (Leg A, `row9b_symbolic.py`, residual 0; identical to row 9's system written in conformal time):

    Phi' = (Q/a^2) Xi - Hc Phi ,   Xi' = a^2 (1 - k^2/Q) Phi + Hc Xi ,
    zeta = Phi + Hc Xi / a^2 ,     zeta' = -k^2 Hc Phi / Q ,     Q = Hc^2 - Hc' = -a^2 Hdot .

At a SIMPLE zero of Q (the smooth NEC crossing that LQC and poly have and the Quintin-type background does
not) Leg A gives: indicial exponents {0, 2}; Phi, Phi' continuous with Phi'(eta_c) = -Hc(eta_c) Phi(eta_c);
the r = 0 branch carries a t^2 log t term with amplitude C = -Phi(eta_c) k^2 / 2, so zeta and Xi diverge
LOGARITHMICALLY with the closed-form amplitude  c_log = -k^2 Hc(eta_c) Phi(eta_c) / Q'(eta_c).
The crossing is therefore integrable and the continuation is the principal value, taken two independent ways:
  P1  1/Q -> Q/(Q^2 + eps^2), eps -> 0        P2  excise |eta - eta_c| < delta (pole term off), delta -> 0

lambda is defined EXACTLY as A3M/a2 define T_fNL = 1/lambda: lambda = zeta_C(+infty) / zeta(-eta_B), the
constant-branch amplitude in the dust expansion over zeta at the NEC boundary, each scheme using its own
zeta propagated from the same dust adiabatic vacuum.  On LQC/poly zeta(-eta_B) is the LOG-DIVERGENT point,
so its FINITE PART is used and the log amplitude is checked against the closed form above.

Run: python3 row9b_numeric.py -> row9b_numeric.log, results.json, row9b_bardeen_lqc.png
"""
import json, os, sys, time
import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../lane9b2_s2_rawadm"))
from lane9b2_s2_rawadm import matter_mode, matter_real_basis      # committed, unmodified
import row9b_backgrounds as BG

LOG, OUT = [], {}
def log(s=""):
    print(s); LOG.append(str(s))

T0 = time.time()
KS = [1e-3, 3e-3, 1e-2]
RTOL, ATOL = 1e-12, 1e-16
SQ3 = np.sqrt(3.0)


# ------------------------------------------------------------------ initial data (dust adiabatic vacuum)
def dust_ic(bg, k, route):
    """Exact positive-frequency dust mode at the start of the contracting tail.
    route='bardeen' -> (Phi, Xi); route='S1' -> (mu, mu')."""
    em = bg.eta_m_start
    a, Hc, Q, _ = bg.charts()[0].fields(bg.charts()[0].s0)
    v, dv = matter_mode(k, em)
    if route == "S1":
        return np.array([v / SQ3, dv / SQ3]), None
    z, dz = SQ3 * a, SQ3 * a * Hc
    zeta = v / z
    dzeta = (dv * z - v * dz) / z**2
    Phi = -Q * dzeta / (k * k * Hc)
    Xi = a * a * (zeta - Phi) / Hc
    return np.array([Phi, Xi]), zeta


# ------------------------------------------------------------------ the two routes
def rhs_bardeen(s, y, fields, k, rinv):
    a, Hc, Q, J = fields(s)
    a2 = a * a
    coef = a2 * (1.0 - k * k * rinv(Q))
    PR, XR, PI, XI = y[1], y[2], y[3], y[4]
    return [J,
            J * (Q * XR / a2 - Hc * PR), J * (coef * PR + Hc * XR),
            J * (Q * XI / a2 - Hc * PI), J * (coef * PI + Hc * XI)]


def rhs_s1(s, y, fields, k, rinv):
    a, Hc, Q, J = fields(s)
    W = 2.0 * Hc * Hc - Q - k * k                      # a''/a - k^2
    return [J, J * y[2], J * W * y[1], J * y[4], J * W * y[3]]


W_LOCAL = 0.2          # half-width (in units of eta_B) of the window in which a regulator is applied


def _segments(bg, ich, s0, s1, mode, delta_eta):
    """Split a chart around its Q = 0 crossings.

    'gap'  -> the excised interval |eta - eta_c| < delta_eta carries NO pole term (pole flag False).
    'eps'  -> the LOCAL window |eta - eta_c| <= W_LOCAL*eta_B carries the regularised 1/Q (flag 'eps');
              everywhere else the exact 1/Q is used.  The local window matters: on the poly background
              Q -> 6/eta^2 -> 0 in the dust tails as well, so a globally applied Q/(Q^2+eps^2) would
              corrupt the tails (measured: it does, by two orders of magnitude).
    """
    cr = [c for (i, c) in getattr(bg, "crossings_s", []) if i == ich]
    if mode == "exact" or not cr:
        return [(s0, s1, True)]
    segs, cur = [], s0
    fwd = s1 > s0
    for sc in sorted(cr, reverse=not fwd):
        a, Hc, Q, J = bg.charts()[ich].fields(sc)
        half = (delta_eta if mode == "gap" else W_LOCAL * bg.eta_B) / abs(J)
        lo, hi = (sc - half, sc + half) if fwd else (sc + half, sc - half)
        inner = False if mode == "gap" else "eps"
        segs.append((cur, lo, True)); segs.append((lo, hi, inner)); cur = hi
    segs.append((cur, s1, True))
    return segs


def propagate(bg, k, route="bardeen", mode="exact", eps_eta=0.0, delta_eta=0.0, upto=None):
    """Integrate from the start of the contracting dust tail.  upto = (ichart, s_stop) stops early."""
    rhs = rhs_bardeen if route == "bardeen" else rhs_s1
    y0, zeta0 = dust_ic(bg, k, route)
    y = np.array([bg.eta_start, y0[0].real, y0[1].real, y0[0].imag, y0[1].imag], dtype=float)
    charts = bg.charts()
    for ich, ch in enumerate(charts):
        for (sa, sb, use_pole) in _segments(bg, ich, ch.s0, ch.s1, mode, delta_eta):
            if sa == sb:
                continue
            stop_here = upto is not None and upto[0] == ich and min(sa, sb) <= upto[1] <= max(sa, sb)
            sb_eff = upto[1] if stop_here else sb
            if use_pole is False:
                rinv = lambda Q: 0.0
            elif use_pole == "eps":
                e2 = (abs(bg.Qprime_at_crossing()[0]) * eps_eta) ** 2
                rinv = lambda Q, e2=e2: Q / (Q * Q + e2)
            else:
                rinv = lambda Q: 1.0 / Q
            if sa != sb_eff:
                sol = solve_ivp(rhs, (sa, sb_eff), y, args=(ch.fields, k, rinv),
                                rtol=RTOL, atol=ATOL, method="DOP853")
                assert sol.success, (bg.label, ich, sol.message)
                y = sol.y[:, -1]
            if stop_here:
                return y, ich, ch
    return y, len(charts) - 1, charts[-1]


def zeta_of(bg, ich, s, y, route, k):
    a, Hc, Q, J = bg.charts()[ich].fields(s)
    if route == "S1":
        mu = y[1] + 1j * y[3]
        dmu = y[2] + 1j * y[4]
        return mu / a, (dmu - mu * Hc) / a                        # zeta, zeta'
    Phi = y[1] + 1j * y[3]
    Xi = y[2] + 1j * y[4]
    zeta = Phi + Hc * Xi / (a * a)
    dzeta = -k * k * Hc * Phi / Q
    return zeta, dzeta


def const_branch(bg, k, ich, s, y, route):
    """Constant-zeta branch amplitude in the dust expansion (exact real matter basis)."""
    a, Hc, Q, J = bg.charts()[ich].fields(s)
    zeta, dzeta = zeta_of(bg, ich, s, y, route, k)
    em = bg.eta_m_end
    if route == "S1":
        f, df = a * zeta, a * (Hc * zeta + dzeta)                 # mu = a zeta
        norm = -k * k / (3.0 * bg.A)
    else:
        f, df = SQ3 * a * zeta, SQ3 * a * (Hc * zeta + dzeta)     # v = sqrt(3) a zeta
        norm = -k * k / (3.0 * SQ3 * bg.A)
    g1, g2, dg1, dg2 = matter_real_basis(k, np.array([em]))
    M = np.array([[float(g1[0]), float(g2[0])], [float(dg1[0]), float(dg2[0])]])
    cA, cB = np.linalg.solve(M, np.array([f, df]))
    return cA * norm


# ------------------------------------------------------------------ zeta at the NEC boundary (finite part)
def zeta_ref(bg, k, route, deltas=(1e-2, 3e-3, 1e-3, 3e-4, 1e-4)):
    """zeta(-eta_B).  On Quintin, Q != 0 there and this is just the value.  On LQC/poly it is the
    LOG-DIVERGENT point: the value is taken at -eta_B - Delta, the measured log slope is compared with the
    closed form c_log = -k^2 Hc Phi / Q', and the finite part is returned."""
    if not bg.has_crossing:
        y, ich, ch = propagate(bg, k, route=route, mode="exact", upto=(0, -bg.tm))
        z, _ = zeta_of(bg, ich, -bg.tm, y, route, k)
        return dict(zeta=complex(z), measured_log_slope=None, closed_form_log=None, spread=0.0,
                    log_over_zeta=0.0)
    ich_c, s_c = bg.first_crossing
    a_c, Hc_c, Q_c, J_c = bg.charts()[ich_c].fields(s_c)
    fwd = bg.charts()[ich_c].s1 > bg.charts()[ich_c].s0
    rows = []
    for D in deltas:
        ds = D / abs(J_c)
        s_stop = s_c - ds if fwd else s_c + ds
        y, ich, ch = propagate(bg, k, route=route, mode="exact", upto=(ich_c, s_stop))
        z, _ = zeta_of(bg, ich, s_stop, y, route, k)
        Phi = y[1] + 1j * y[3]
        rows.append((D, complex(z), complex(Phi)))
    # closed-form log amplitude from Leg A, evaluated with Phi at the smallest Delta
    qp = bg.Qprime_at_crossing()[0]
    c_log = -k * k * Hc_c * rows[-1][2] / qp
    if route == "S1":
        c_log = 0.0 * c_log
    lnD = np.array([np.log(r[0]) for r in rows])
    zz = np.array([r[1] for r in rows])
    slope = np.polyfit(lnD, zz.real, 1)[0] + 1j * np.polyfit(lnD, zz.imag, 1)[0]
    fp = zz - c_log * lnD
    return dict(zeta=complex(fp[-1]), finite_parts=[complex(v) for v in fp],
                measured_log_slope=complex(slope), closed_form_log=complex(c_log),
                spread=float(np.ptp(np.abs(fp)) / abs(fp[-1])),
                log_over_zeta=float(abs(c_log / fp[-1])))


# ------------------------------------------------------------------ lambda
def lam(bg, k, route="bardeen", mode="exact", eps_eta=0.0, delta_eta=0.0, zref=None):
    y, ich, ch = propagate(bg, k, route=route, mode=mode, eps_eta=eps_eta, delta_eta=delta_eta)
    s_end = ch.s1
    zc = const_branch(bg, k, ich, s_end, y, route)
    zr = zref if zref is not None else zeta_ref(bg, k, route)["zeta"]
    return float(abs(zc / zr)), complex(zc)


# ------------------------------------------------------------------ Wronskian gate
def wronskian(bg, k, mode, eps_eta=0.0, delta_eta=0.0):
    """W = (a^2/Q)(Phi_1 Psi_2 - Phi_2 Psi_1) = Phi_1 Xi_2 - Phi_2 Xi_1 is conserved (traceless system
    in the conformal-time (Phi, Xi) variables)."""
    outs = []
    win = bg.wronskian_window()
    for y0 in ([1.0, 0.0], [0.0, 1.0]):
        y = np.array([0.0, y0[0], y0[1], 0.0, 0.0])
        charts = bg.charts()
        for (ich, wa, wb) in win:
            ch = charts[ich]
            for (sa, sb, use_pole) in _segments(bg, ich, wa, wb, mode, delta_eta):
                if sa == sb:
                    continue
                if use_pole is False:
                    rinv = lambda Q: 0.0
                elif use_pole == "eps":
                    e2 = (abs(bg.Qprime_at_crossing()[0]) * eps_eta) ** 2
                    rinv = lambda Q, e2=e2: Q / (Q * Q + e2)
                else:
                    rinv = lambda Q: 1.0 / Q
                sol = solve_ivp(rhs_bardeen, (sa, sb), y, args=(ch.fields, k, rinv),
                                rtol=RTOL, atol=ATOL, method="DOP853")
                assert sol.success
                y = sol.y[:, -1]
        outs.append(y)
    W0 = 1.0
    W1 = outs[0][1] * outs[1][2] - outs[1][1] * outs[0][2]
    scale = max(abs(outs[0][1] * outs[1][2]), abs(outs[1][1] * outs[0][2]))
    return float(abs(W1 / W0 - 1.0)), float(scale)


# ------------------------------------------------------------------ independent analytic cross-check
def R_superhubble(bg):
    """Independent, ODE-free prediction of R.

    At k = 0 the exact solutions are zeta = C1 + C2 J_s(eta), J_s = int deta/z_s^2, and the dust adiabatic
    vacuum has C1 = C2 I_s (i.e. zeta(-infty) = 0), so zeta_C(+infty) = 2 C2 I_s with I_s = J_s(+infty).
    In the dust tails z_eps^2 = 3 a^2 = 3 z_S1^2, so matching the SAME zeta(eta) gives C2_eps = 3 C2_S1, and

            R  =  3 I_eps / I_S1 ,        I_s = int_0^infty deta / z_s^2 ,

    with I_eps taken as a PRINCIPAL VALUE through the Q = 0 poles.  z_eps^2 = 2 a^2 Q / Hc^2, z_S1^2 = a^2.
    """
    from scipy.integrate import quad
    out = {}
    if bg.label.startswith("LQC"):
        I1 = np.pi / SQ3
        f = lambda x: np.sqrt(1 - x) / (3 * SQ3 * np.sqrt(x) * (1 - 2 * x))
        rows = []
        for d in (1e-3, 1e-4, 1e-5, 1e-6):
            Ie = quad(f, 0, 0.5 - d, limit=400)[0] + quad(f, 0.5 + d, 1, limit=400, points=[1])[0]
            rows.append((d, Ie, 3 * Ie / I1))
        out = dict(I_S1=float(I1), I_S1_closed_form="pi/sqrt(3)", pv_scan=rows,
                   R=float(rows[-1][2]), R_closed_form="3*(pi/(6 sqrt3))/(pi/sqrt3) = 1/2",
                   I_eps_closed_form="pi/(6 sqrt(3)) -- identical to the DUST effective-fluid mixing integral")
    elif bg.label.startswith("poly"):
        I1 = quad(lambda e: 1.0 / (1 + e * e) ** 2, 0, np.inf, limit=400)[0]
        def fp(e):
            a = 1 + e * e
            return (2 * e / a) ** 2 / (2 * a * a * (2 * (3 * e * e - 1) / (a * a)))
        ec = 1.0 / SQ3
        rows = []
        for d in (1e-3, 1e-4, 1e-5, 1e-6):
            Ie = quad(fp, 1e-12, ec - d, limit=400)[0] + quad(fp, ec + d, np.inf, limit=400)[0]
            rows.append((d, Ie, 3 * Ie / I1))
        out = dict(I_S1=float(I1), I_S1_closed_form="pi/4", pv_scan=rows, R=float(rows[-1][2]),
                   R_closed_form="3*(pi/32)/(pi/4) = 3/8", I_eps_closed_form="pi/32")
    else:
        Ups, tm = bg.Ups, bg.tm
        aa = lambda t: bg._a(t)
        eps = lambda t: -1.0 / (Ups * t * t) if abs(t) <= tm else 1.5
        Ie = (quad(lambda t: 1.0 / (aa(t) * 2 * aa(t) ** 2 * eps(t)), 1e-9, tm, limit=400)[0]
              + quad(lambda t: 1.0 / (aa(t) * 3 * aa(t) ** 2), tm, np.inf, limit=400)[0])
        I1 = (quad(lambda t: 1.0 / aa(t) ** 3, 0, tm, limit=400)[0]
              + quad(lambda t: 1.0 / aa(t) ** 3, tm, np.inf, limit=400)[0])
        out = dict(I_S1=float(I1), pv_scan=[(0.0, float(Ie), float(3 * Ie / I1))], R=float(3 * Ie / I1),
                   R_closed_form=None, I_eps_closed_form=None,
                   note="no Q = 0 crossing: the integral is ordinary, no principal value needed")
    return out


# ------------------------------------------------------------------ main
def main():
    log("=" * 108)
    log("ROW 9b LEG B - the Bardeen linear transfer on the LQC and poly backgrounds (smooth NEC crossings)")
    log("=" * 108)
    bgs = [("quintin", BG.Quintin()), ("LQC", BG.LQC()), ("poly", BG.Poly())]
    OUT["backgrounds"] = {n: dict(label=b.label, eta_B=b.eta_B, A=b.A, has_crossing=b.has_crossing,
                                  Qprime_at_crossings=(b.Qprime_at_crossing() if b.has_crossing else None))
                          for n, b in bgs}

    # ---------- G1 control: reproduce row 9's committed Quintin numbers
    ROW9 = {1e-3: 0.969924, 3e-3: 0.969946, 1e-2: 0.970188}
    q = bgs[0][1]
    g1 = {}
    for keta in KS:
        k = keta / q.eta_B
        zr = zeta_ref(q, k, "bardeen")["zeta"]
        L, _ = lam(q, k, "bardeen", "exact", zref=zr)
        g1[str(keta)] = dict(lam=L, row9=ROW9[keta], rel=abs(L / ROW9[keta] - 1))
    g1_ok = max(v["rel"] for v in g1.values()) <= 1e-4
    log("\n[G1] control - Bardeen lambda on the Quintin-type background vs row 9's committed values:")
    for keta in KS:
        v = g1[str(keta)]
        log("     k eta_B=%-7g  this lane %.6f   row 9 %.6f   rel %.1e" % (keta, v["lam"], v["row9"], v["rel"]))
    log("     -> %s" % ("PASS" if g1_ok else "FAIL"))
    OUT["G1_control_quintin"] = dict(g1, **{"pass": bool(g1_ok)})
    if not g1_ok:
        log("\nG1 FAILED - nothing further is reported (pre-registration section 5).")
        return

    # ---------- G2 matter limit, G3 S1 reference, G5 Wronskian
    g2, g3, g5, g5scale = {}, {}, {}, {}
    for n, b in bgs:
        ch = b.charts()[0]
        a_, Hc_, Q_, J_ = ch.fields(ch.s0)
        g2[n] = dict(zeta_over_Phi=float(1 + Hc_ * Hc_ / Q_), target=5.0 / 3.0,
                     err=float(abs((1 + Hc_ * Hc_ / Q_) / (5.0 / 3.0) - 1)))
        k = 1e-3 / b.eta_B
        zr1 = zeta_ref(b, k, "S1")["zeta"]
        L1, _ = lam(b, k, "S1", "exact", zref=zr1)
        g3[n] = dict(lam_S1=L1, T_S1=1.0 / L1)
        g5[n], g5scale[n] = wronskian(b, k, "gap" if b.has_crossing else "exact", delta_eta=1e-4)
    A2_T = {"quintin": 0.16500538, "LQC": 0.24999984, "poly": 0.19550111}
    for n in g3:
        g3[n]["a2_T_fNL"] = A2_T[n]
        g3[n]["rel"] = abs(g3[n]["T_S1"] / A2_T[n] - 1)
    g2_ok = max(v["err"] for v in g2.values()) <= 1e-6
    g3_ok = max(v["rel"] for v in g3.values()) <= 0.01
    g5_ok = max(g5.values()) <= 1e-8
    log("\n[G2] dust limit zeta/Phi (Phi = const): " + ", ".join(
        "%s %.12f (err %.1e)" % (n, g2[n]["zeta_over_Phi"], g2[n]["err"]) for n, _ in bgs)
        + "  -> %s" % ("PASS" if g2_ok else "FAIL"))
    log("[G3] S1 reference, this lane's own projection vs the committed a2_transmission_linear T_fNL:")
    for n, _ in bgs:
        log("     %-8s lambda_S1 = %.6f  T = %.6f   (a2: %.6f, rel %.1e)"
            % (n, g3[n]["lam_S1"], g3[n]["T_S1"], g3[n]["a2_T_fNL"], g3[n]["rel"]))
    log("     -> %s" % ("PASS" if g3_ok else "FAIL"))
    log("[G5] Wronskian Phi_1 Xi_2 - Phi_2 Xi_1 over the singular sub-domain (both Q = 0 crossings + H = 0): "
        + ", ".join("%s %.1e (term scale %.2g)" % (n, g5[n], g5scale[n]) for n, _ in bgs)
        + "  -> %s" % ("PASS" if g5_ok else "FAIL"))
    OUT["G2_dust_limit"] = dict(g2, **{"pass": bool(g2_ok)})
    OUT["G3_S1_reference"] = dict(g3, **{"pass": bool(g3_ok)})
    OUT["G5_wronskian"] = dict(err=g5, term_scale=g5scale, window="bounded sub-domain spanning both "
                               "Q = 0 crossings and H = 0", **{"pass": bool(g5_ok)})

    # ---------- Leg B: R = zeta_C^Phi(+inf) / zeta_C^S1(+inf) at fixed incoming dust vacuum
    log("\n[B] R = |zeta_C^Bardeen(+inf) / zeta_C^S1(+inf)| at the SAME incoming dust adiabatic vacuum.")
    log("    This is the convention-free transfer ratio: it needs no handoff surface, and because")
    log("    zeta^Bardeen == zeta^S1 identically in the dust contraction, f_NL^after,lin scales as 1/R.")
    EPSD = [3e-3, 1e-3, 3e-4, 1e-4]
    Rres, g4 = {}, {}
    for n, b in bgs:
        Rres[n] = {}
        for keta in KS:
            k = keta / b.eta_B
            zc1 = lam(b, k, "S1", "exact", zref=1.0)[1]
            if not b.has_crossing:
                zcP = lam(b, k, "bardeen", "exact", zref=1.0)[1]
                Rres[n][str(keta)] = dict(R=float(abs(zcP / zc1)), eps_scan=None, gap_scan=None)
            else:
                es = [float(abs(lam(b, k, "bardeen", "eps", eps_eta=v, zref=1.0)[1] / zc1)) for v in EPSD]
                gs = [float(abs(lam(b, k, "bardeen", "gap", delta_eta=v, zref=1.0)[1] / zc1)) for v in EPSD]
                # both converge linearly in the regulator -> Richardson
                Re = 2 * es[-1] - es[-2]
                Rg = 2 * gs[-1] - gs[-2]
                Rres[n][str(keta)] = dict(R=float(0.5 * (Re + Rg)), R_eps=float(Re), R_gap=float(Rg),
                                          eps_scan=es, gap_scan=gs,
                                          P1_P2_disagreement=float(abs(Re / Rg - 1)),
                                          eps_last3_spread=float(np.ptp(es[-3:]) / np.mean(es[-3:])),
                                          gap_last3_spread=float(np.ptp(gs[-3:]) / np.mean(gs[-3:])))
        log("    %-8s " % n + "   ".join("k eta_B=%g: R=%.6f" % (keta, Rres[n][str(keta)]["R"]) for keta in KS))
        if b.has_crossing:
            r = Rres[n][str(KS[0])]
            log("             P1(eps) scan %s -> %.6f | P2(gap) scan %s -> %.6f | disagreement %.1e"
                % (["%.6f" % v for v in r["eps_scan"]], r["R_eps"],
                   ["%.6f" % v for v in r["gap_scan"]], r["R_gap"], r["P1_P2_disagreement"]))
            g4[n] = dict(disagreement=max(Rres[n][str(kk)]["P1_P2_disagreement"] for kk in KS),
                         eps_spread=max(Rres[n][str(kk)]["eps_last3_spread"] for kk in KS),
                         gap_spread=max(Rres[n][str(kk)]["gap_last3_spread"] for kk in KS))
    g4_ok = all(v["disagreement"] <= 0.02 and v["eps_spread"] <= 0.02 and v["gap_spread"] <= 0.02
                for v in g4.values())
    log("[G4] P1 vs P2: " + ", ".join("%s disagree %.1e, eps-spread %.1e, gap-spread %.1e"
                                      % (n, v["disagreement"], v["eps_spread"], v["gap_spread"])
                                      for n, v in g4.items()) + "  -> %s" % ("PASS" if g4_ok else "FAIL"))
    OUT["R"] = Rres
    OUT["G4_crossing_convergence"] = dict(g4, **{"pass": bool(g4_ok)})

    # ---------- G6 independent analytic cross-check
    log("\n[G6] independent super-Hubble cross-check  R = 3 I_eps / I_S1  (principal-value quadrature, no ODE):")
    g6 = {}
    for n, b in bgs:
        sh = R_superhubble(b)
        num = Rres[n][str(KS[0])]["R"]
        sh["R_from_ODE"] = float(num)
        sh["rel"] = float(abs(sh["R"] / num - 1))
        g6[n] = sh
        log("     %-8s analytic R = %.7f %s | ODE R = %.7f | rel %.1e"
            % (n, sh["R"], ("= " + sh["R_closed_form"]) if sh["R_closed_form"] else "", num, sh["rel"]))
    g6_ok = max(v["rel"] for v in g6.values()) <= 1e-3
    log("     -> %s" % ("PASS" if g6_ok else "FAIL"))
    OUT["G6_analytic_crosscheck"] = dict(g6, **{"pass": bool(g6_ok)})

    # ---------- G7 the log at the crossing, measured vs the Leg-A closed form
    log("\n[G7] the logarithm at Q = 0: measured slope of zeta vs Leg A's closed form c_log = -k^2 Hc Phi / Q':")
    g7 = {}
    for n, b in bgs:
        if not b.has_crossing:
            continue
        k = 1e-3 / b.eta_B
        zr = zeta_ref(b, k, "bardeen")
        g7[n] = dict(measured=str(zr["measured_log_slope"]), closed_form=str(zr["closed_form_log"]),
                     rel=float(abs(zr["measured_log_slope"] / zr["closed_form_log"] - 1)),
                     log_over_finite_part=zr["log_over_zeta"], finite_part_spread=zr["spread"],
                     zeta_finite_part=str(zr["zeta"]))
        log("     %-8s measured %.6g  closed form %.6g  rel %.1e | |c_log/zeta_fp| = %.3f"
            % (n, abs(zr["measured_log_slope"]), abs(zr["closed_form_log"]), g7[n]["rel"],
               zr["log_over_zeta"]))
    g7_ok = max(v["rel"] for v in g7.values()) <= 0.01
    log("     -> %s (the log is REAL and its amplitude is the Leg-A closed form)" % ("PASS" if g7_ok else "FAIL"))
    OUT["G7_log_amplitude"] = dict(g7, **{"pass": bool(g7_ok)})

    # ---------- G8 robustness to the two numerical truncations, and the dust-phase agreement the
    #            propagation rule f_NL^after,lin ~ 1/R depends on
    log("\n[G8] robustness: R vs the LQC dust-tail truncation x_i and the poly far boundary eta_far; and the")
    log("     dust-phase identity zeta^Bardeen == zeta^S1 (without which 1/R is not the propagation rule):")
    g8 = {"R_vs_truncation": {}, "dust_identity": {}}
    for xi in (1e-8, 1e-10, 1e-12):
        b = BG.LQC(x_i=xi); k = 1e-3 / b.eta_B
        zc1 = lam(b, k, "S1", "exact", zref=1.0)[1]
        zc = lam(b, k, "bardeen", "gap", delta_eta=1e-4, zref=1.0)[1]
        g8["R_vs_truncation"]["LQC x_i=%.0e" % xi] = float(abs(zc / zc1))
    for ef in (2000.0, 4000.0, 8000.0):
        b = BG.Poly(eta_far=ef); k = 1e-3 / b.eta_B
        zc1 = lam(b, k, "S1", "exact", zref=1.0)[1]
        zc = lam(b, k, "bardeen", "gap", delta_eta=1e-4, zref=1.0)[1]
        g8["R_vs_truncation"]["poly eta_far=%g" % ef] = float(abs(zc / zc1))
    for n, b in bgs[1:]:
        k = 1e-3 / b.eta_B; ch = b.charts()[0]
        sm = ch.s0 + 0.15 * (ch.s1 - ch.s0)
        yB, iB, _ = propagate(b, k, "bardeen", "exact", upto=(0, sm)); zB, _ = zeta_of(b, iB, sm, yB, "bardeen", k)
        y1, i1, _ = propagate(b, k, "S1", "exact", upto=(0, sm)); z1, _ = zeta_of(b, i1, sm, y1, "S1", k)
        a_, H_, Q_, J_ = ch.fields(sm)
        g8["dust_identity"][n] = dict(eps=float(Q_ / (H_ * H_)), rel=float(abs(zB / z1 - 1)))
    log("     " + ", ".join("%s: %.7f" % (kk, vv) for kk, vv in g8["R_vs_truncation"].items()))
    log("     " + ", ".join("%s eps=%.8f rel=%.1e" % (kk, vv["eps"], vv["rel"])
                            for kk, vv in g8["dust_identity"].items()))
    g8_ok = (float(np.ptp(list(g8["R_vs_truncation"].values())[:3])) < 1e-5
             and float(np.ptp(list(g8["R_vs_truncation"].values())[3:])) < 1e-5
             and max(v["rel"] for v in g8["dust_identity"].values()) < 1e-6)
    log("     -> %s" % ("PASS" if g8_ok else "FAIL"))
    OUT["G8_robustness"] = dict(g8, **{"pass": bool(g8_ok)})

    # ---------- handoff-convention comparison (the one place where "the Bardeen T" is not unique)
    log("\n[H] the two handoff conventions for converting R into a transfer coefficient:")
    log("    A = common DUST handoff, where zeta^Bardeen == zeta^S1 (gate G8) -> T = T_S1/R exactly;")
    log("    B = the paper's handoff at -eta_B, each scheme using its own zeta there (Bardeen: log finite part).")
    log("    On the Quintin-type background -eta_B IS the end of the exact dust phase, so A and B must coincide;")
    log("    on LQC/poly -eta_B is the Q = 0 surface, where eps = Q/Hc^2 = 0 EXACTLY -- so the matter-contraction")
    log("    value f_NL^before = -35/16 (an eps = 3/2 result) cannot be evaluated there at all, and zeta is")
    log("    additionally log-divergent. Convention A is therefore the defensible one; B is reported anyway.")
    hand = {}
    for n, b in bgs:
        hand[n] = {}
        for keta in KS:
            k = keta / b.eta_B
            zc1 = lam(b, k, "S1", "exact", zref=1.0)[1]
            zcP = (lam(b, k, "bardeen", "gap", delta_eta=1e-4, zref=1.0)[1] if b.has_crossing
                   else lam(b, k, "bardeen", "exact", zref=1.0)[1])
            R = float(abs(zcP / zc1))
            zr1 = zeta_ref(b, k, "S1"); zrP = zeta_ref(b, k, "bardeen")
            T1 = float(abs(zr1["zeta"] / zc1))
            TA = T1 / R
            TB = float(abs(zrP["zeta"] / zcP))
            hand[n][str(keta)] = dict(R=R, T_S1=T1, T_conventionA=TA, T_conventionB=TB, ratio_B_over_A=TB / TA,
                                      log_over_finite_part=zrP.get("log_over_zeta", 0.0),
                                      eps_at_handoff=float(0.0 if b.has_crossing else 1.5))
        r = hand[n][str(KS[0])]
        log("    %-8s T_S1 %.4f | A %.4f | B %.4f | B/A %.3f | log/finite-part %.2f | eps at handoff %.3f"
            % (n, r["T_S1"], r["T_conventionA"], r["T_conventionB"], r["ratio_B_over_A"],
               r["log_over_finite_part"], r["eps_at_handoff"]))
    qn = hand["quintin"][str(KS[0])]["ratio_B_over_A"]
    log("    -> the two conventions agree to %.1e on the Quintin-type background, where the handoff is"
        % abs(qn - 1.0))
    log("       legitimate; they differ by the log contamination elsewhere. Convention A is adopted.")
    OUT["handoff_conventions"] = hand

    # ---------- consequences
    FNL_BEFORE = -35.0 / 16.0
    DELTA_S1 = {"quintin": -0.140, "LQC": -0.104, "poly": -0.127}
    DELTA_S2_QUINTIN = 1.007
    log("\n" + "=" * 108)
    log("CONSEQUENCES (linear transfer only; the cubic term Delta_T is OUT OF SCOPE on LQC/poly by "
        "pre-registration)")
    log("=" * 108)
    cons = {}
    for n, b in bgs:
        R = Rres[n][str(KS[0])]["R"]
        T1 = g3[n]["T_S1"]
        TB = T1 / R
        lin1 = T1 * FNL_BEFORE
        linB = TB * FNL_BEFORE
        cons[n] = dict(R=R, T_S1=T1, T_Bardeen=TB, ratio=1.0 / R,
                       fNL_after_lin_S1=lin1, fNL_after_lin_Bardeen=linB,
                       fNL_after_S1=lin1 + DELTA_S1[n],
                       fNL_after_Bardeen=(linB + DELTA_S2_QUINTIN) if n == "quintin" else None,
                       fNL_after_Bardeen_bracket=None if n == "quintin" else
                       [linB + DELTA_S1[n], linB + DELTA_S2_QUINTIN],
                       r_after_S1=24.0, r_after_Bardeen=24.0 / R**2)
        log("  %-8s R = %.5f  ->  T_fNL: S1 %.4f -> Bardeen %.4f (x%.3f) | "
            "f_NL^after,lin: %.4f -> %.4f | r_after: 24.0 -> %.1f"
            % (n, R, T1, TB, 1.0 / R, lin1, linB, 24.0 / R**2))
    OUT["consequences"] = cons
    OUT["fNL_before"] = FNL_BEFORE
    OUT["Delta_S1_committed"] = DELTA_S1
    OUT["Delta_S2_quintin_committed"] = DELTA_S2_QUINTIN

    # ---------- verdict against the pre-registration
    devs = {n: abs(cons[n]["R"] - 1.0) for n, _ in bgs}
    both_differ = devs["LQC"] > 0.02 and devs["poly"] > 0.02
    both_agree = devs["LQC"] <= 0.02 and devs["poly"] <= 0.02
    gates = g1_ok and g2_ok and g3_ok and g4_ok and g5_ok and g6_ok and g7_ok and g8_ok
    verdict = ("INCONCLUSIVE" if not gates else
               "OUTCOME-UNIVERSAL(b)" if both_differ else
               "OUTCOME-UNIVERSAL(a)" if both_agree else "OUTCOME-UNIVERSAL(c)")
    log("\n" + "=" * 108)
    log("VERDICT (PREREGISTRATION.md section 4.1): gates %s ; |R-1| = LQC %.3f, poly %.3f  ->  %s"
        % ("ALL PASS" if gates else "FAILED", devs["LQC"], devs["poly"], verdict))
    log("=" * 108)
    OUT["verdict"] = dict(outcome=verdict, gates_all_pass=bool(gates), dev_from_unity=devs)
    OUT["runtime_s"] = time.time() - T0

    # ---------- figure
    try:
        import matplotlib; matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 3, figsize=(13.5, 4.0))
        # (a) Q(eta) for the three backgrounds, showing the crossings
        for n, b in bgs:
            ee, QQ = [], []
            if n == "poly":
                ee = np.linspace(-3, 3, 800); QQ = [b._f(e)[2] for e in ee]
                ax[0].plot(ee / b.eta_B, QQ, label="poly")
            elif n == "LQC":
                ws = np.linspace(-0.948, 0.948, 800)
                et = [0.0]
                for i in range(1, len(ws)):
                    et.append(et[-1] + 0.5 * (b._fw(ws[i])[3] + b._fw(ws[i - 1])[3]) * (ws[i] - ws[i - 1]))
                et = np.array(et) - np.interp(0.0, ws, et)
                ax[0].plot(et / b.eta_B, [b._fw(w)[2] for w in ws], label="LQC")
            else:
                tt = np.linspace(-2.0, 2.0, 800)
                ax[0].plot([b._eta(t) / b.eta_B for t in tt], [b._f(t)[2] for t in tt], label="Quintin-type")
        ax[0].axhline(0, color="0.6", lw=0.8); ax[0].axvline(-1, color="0.85", lw=0.8, ls=":")
        ax[0].axvline(1, color="0.85", lw=0.8, ls=":")
        ax[0].set_xlim(-3, 3); ax[0].set_xlabel(r"$\eta/\eta_B$")
        ax[0].set_ylabel(r"$Q=\mathcal{H}^2-\mathcal{H}'=-a^2\dot H$")
        ax[0].set_title("Q = 0: smooth crossing (LQC, poly) vs a jump (Quintin)", fontsize=9)
        ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)
        # (b) regulator convergence
        for n, b in bgs:
            if not b.has_crossing:
                continue
            r = Rres[n][str(KS[0])]
            ax[1].plot(EPSD, r["eps_scan"], "o-", ms=3, label="%s  P1 ($\\epsilon$)" % n)
            ax[1].plot(EPSD, r["gap_scan"], "s--", ms=3, label="%s  P2 ($\\delta$)" % n)
            ax[1].axhline(r["R"], color="0.5", lw=0.8, ls=":")
        ax[1].set_xscale("log"); ax[1].set_xlabel(r"regulator / $\eta_B$")
        ax[1].set_ylabel("$R$"); ax[1].set_title("principal value: two prescriptions, same limit", fontsize=9)
        ax[1].legend(fontsize=7); ax[1].grid(alpha=0.3)
        # (c) consequences
        names = [n for n, _ in bgs]
        xs = np.arange(3)
        ax[2].bar(xs - 0.2, [abs(cons[n]["fNL_after_lin_S1"]) for n in names], 0.4, label="S1 ($z=a$)")
        ax[2].bar(xs + 0.2, [abs(cons[n]["fNL_after_lin_Bardeen"]) for n in names], 0.4,
                  label="Bardeen continuation")
        ax[2].set_xticks(xs); ax[2].set_xticklabels(names)
        ax[2].set_ylabel(r"$|\,T_{f_{\rm NL}}\cdot f_{\rm NL}^{\rm before}|$  (linear transfer only)")
        ax[2].set_title("transmitted amplitude, cubic term excluded", fontsize=9)
        ax[2].legend(fontsize=8); ax[2].grid(alpha=0.3, axis="y")
        fig.tight_layout(); fig.savefig("row9b_bardeen_lqc.png", dpi=140)
        log("[fig] row9b_bardeen_lqc.png")
    except Exception as e:
        log("[fig] skipped: %s" % e)

    open("row9b_numeric.log", "w").write("\n".join(LOG) + "\n")
    json.dump(OUT, open("results.json", "w"), indent=2, default=str)
    log("\n[done] %.1f s" % OUT["runtime_s"])


if __name__ == "__main__":
    main()

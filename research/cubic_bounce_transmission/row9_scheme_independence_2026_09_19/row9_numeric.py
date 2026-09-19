#!/usr/bin/env python3
"""Leg B / B' of ledger row 9 (D-A3-9): the scheme-free linear transfer lambda_zeta via the Bardeen system.

Leg A (row9_symbolic.py) proved, from the exact linearised Einstein equations for a single minimally
coupled scalar (c_s = 1, arbitrary V) on an arbitrary a(eta), all residuals 0:
  (i)   Phi'' + 2(H - pp)Phi' + (k^2 + 2H' - 2 H pp)Phi = 0,  pp = (2HH'-H'')/(2(H^2-H')),
        self-adjoint with mu = a^2/(H^2-H') = -1/Hdot   -- no z, no 1/H;
  (ii)  zeta = Phi + H Xi/a^2 and zeta' = -k^2 H Phi/(H^2-H'), with Xi = mu(Phi' + H Phi);
  (iii) the first-order system  Phi' = -Hdot Xi - H Phi ,  Xi' = (a^2 - mu k^2)Phi + H Xi
        is DELTA-FREE, so Phi and Xi are continuous across any jump in Hdot -- the Bardeen system
        needs no junction prescription, and that continuity is identically scheme S2's
        ([zeta] = 0, [z^2 zeta'] = 0);
  (iv)  scheme S2 (z^2 = 2a^2 eps) IS implied by those equations; scheme S1 (z = a) is NOT, unless
        eps = -Hdot/H^2 is constant.
In cosmic time (used here, d/deta = a d/dt):
      Phidot = -Hdot Xi/a - H Phi ,   Xidot = (a + k^2/(a Hdot)) Phi + H Xi ,   zeta = Phi + H Xi/a.
Run:  python3 row9_numeric.py  ->  row9_numeric.log, results.json, row9_scheme_independence.png
"""
import json, os, sys, time
import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, os.path.abspath("../lane9b2_s2_rawadm"))
from lane9b2_s2_rawadm import Quintin, BounceModes          # committed S1/S2 machinery, unmodified

LOG, OUT = [], {}
def log(s=""):
    print(s); LOG.append(str(s))

T0 = time.time()
KS = [1e-3, 3e-3, 1e-2]
RTOL, ATOL = 1e-12, 1e-16
Q = Quintin(1.0)
TM, UPS, AM, ETA_B = Q.tm, Q.Ups, Q.am, Q.eta_B
# The contraction/expansion matter modes are EXACT analytic solutions (matter_mode / matter_real_basis),
# so no long integration is needed: initial data are set on the contraction side of the junction and the
# post-bounce state is decomposed on the exact matter basis.  TI/TF are used only for the gates.
TI, TF = -400.0, 400.0


# ------------------------------------------------------------------ backgrounds
def smoothstep(x):
    x = min(max(x, 0.0), 1.0); return x**3 * (10 - 15 * x + 6 * x**2)
def dsmoothstep(x):
    return 0.0 if (x <= 0 or x >= 1) else 30 * x**2 * (1 - x) ** 2

class Sharp:
    """The exact committed piecewise Quintin-type background."""
    tm, Ups, smooth = TM, UPS, False
    a  = staticmethod(lambda t: float(Q.a(t)))
    H  = staticmethod(lambda t: float(Q.H(t)))
    Hd = staticmethod(lambda t: float(Q.Hd(t)))

class SmoothBG:
    """Hdot's jump at |t| = tm replaced by a C^2 blend of half-width d:
    Hdot = (1-s)(-3/2 H^2) + s Ups,  s = smootherstep((tm + d - |t|)/(2d)).
    Integrated together with the perturbation (no interpolation error).  Because 1.5 H(tm)^2 = Ups
    exactly on this background, Hdot passes through ZERO inside each layer: the background genuinely
    crosses rho + p = 0, where scheme S2's own variable z^2 = 2a^2 eps VANISHES."""
    smooth = True
    def __init__(self, d, eps=0.0):
        self.d, self.tm, self.Ups, self.eps = float(d), TM, UPS, float(eps)
    def s(self, t):    return smoothstep((self.tm + self.d - abs(t)) / (2 * self.d))
    def sdot(self, t): return dsmoothstep((self.tm + self.d - abs(t)) / (2 * self.d)) * (-np.sign(t) / (2 * self.d))
    def Hd_of(self, t, H): return (1 - self.s(t)) * (-1.5 * H * H) + self.s(t) * self.Ups
    def inv_Hd(self, Hd):
        """1/Hdot regularised as the PRINCIPAL VALUE  Hdot/(Hdot^2 + eps^2).  At the NEC crossing
        (Hdot = 0) the exact integrand k^2 Phi/(a Hdot) is genuinely non-integrable: zeta = Phi + H Xi/a
        is LOGARITHMICALLY DIVERGENT there while Phi and its equation stay finite.  The crossing is
        linear, so the principal value is the unique symmetric finite part; eps -> 0 is scanned."""
        return Hd / (Hd * Hd + self.eps * self.eps) if self.eps > 0 else 1.0 / Hd


# ------------------------------------------------------------------ exact dictionary (Leg A)
def zeta_of(a, H, Xi, Phi):   return Phi + H * Xi / a
def Xi_of(a, H, zeta, Phi):   return a * (zeta - Phi) / H

def matter_ic(k, t):
    """Adiabatic-vacuum matter mode of the contraction, exactly as lane9b2 sets it:
    v = e^{-ik eta}(1 - i/(k eta))/sqrt(2k), zeta = v/z, z = a sqrt(3) (eps = 3/2).
    Returns (Phi, Xi) via  Phi = zetadot a^2 Hdot/(k^2 H)  and  Xi = a(zeta - Phi)/H."""
    e = float(Q.eta_m(t)); a = float(Q.a(t)); H = float(Q.H(t)); Hd = -1.5 * H * H
    v  = np.exp(-1j * k * e) * (1 - 1j / (k * e)) / np.sqrt(2 * k)
    dv = np.exp(-1j * k * e) * (-1j * k * (1 - 1j / (k * e)) + 1j / (k * e * e)) / np.sqrt(2 * k)
    z, dz = np.sqrt(3.0) * a, np.sqrt(3.0) * a * a * H
    zeta = v / z
    zetadot = ((dv * z - v * dz) / z**2) / a
    Phi = zetadot * a * a * Hd / (k * k * H)
    return Phi, Xi_of(a, H, zeta, Phi), zeta


# ------------------------------------------------------------------ constant-branch projection
from lane9b2_s2_rawadm import matter_real_basis

def zetadot_of(a, H, Hd, k, Phi):    return k * k * H * Phi / (a * a * Hd)

def const_branch_zeta(k, t, zeta, zetadot):
    """Amplitude of the surviving (constant-zeta) branch in the matter expansion phase.
    v = z zeta with z = sqrt(3) a; v = cA g1 + cB g2 with g1 = cos x - sin x/x -> -x^2/3 the
    constant-zeta branch and g2 = sin x + cos x/x the eta^-3 branch.  Returns cA's asymptotic zeta."""
    em = float(Q.eta_m(t)); a = float(Q.a(t)); H = float(Q.H(t))
    z = np.sqrt(3.0) * a
    v = z * zeta
    vp = np.sqrt(3.0) * a * a * (H * zeta + zetadot)
    g1, g2, dg1, dg2 = matter_real_basis(k, np.array([em]))
    M = np.array([[float(g1[0]), float(g2[0])], [float(dg1[0]), float(dg2[0])]])
    cA, cB = np.linalg.solve(M, np.array([v, vp]))
    return cA * (-k * k / (3.0 * np.sqrt(3.0) * Q.A))


# ------------------------------------------------------------------ evolution (Phi, Xi)
def rhs_sharp(t, y, k):
    Phi, Xi = y
    a, H, Hd = Sharp.a(t), Sharp.H(t), Sharp.Hd(t)
    return [-Hd * Xi / a - H * Phi, (a + k * k / (a * Hd)) * Phi + H * Xi]

def rhs_smooth(t, y, k, bg):
    H, lna, Phi, Xi = y
    a = np.exp(lna); Hd = bg.Hd_of(t, H)
    return [Hd, H, -Hd * Xi / a - H * Phi, (a + k * k * bg.inv_Hd(Hd) / a) * Phi + H * Xi]

def evolve(rhs, ta, tb, y0, args, teval=None, method="DOP853"):
    """Real and imaginary parts are integrated separately; t_eval defaults to the endpoint so the
    two solutions always have the same shape."""
    if teval is None:
        teval = [tb]
    out = []
    for part in ("real", "imag"):
        yy = [getattr(v, part) if isinstance(v, complex) else float(v) for v in y0]
        sol = solve_ivp(rhs, (ta, tb), yy, args=args, rtol=RTOL, atol=ATOL, method=method, t_eval=teval)
        assert sol.success, sol.message
        out.append(sol)
    return out


def lam_sharp(k):
    """Bardeen (Phi, Xi) from the contraction side of the NEC boundary straight through to the
    expansion side.  Both variables are continuous (Leg A A3c) so NO junction prescription is used."""
    Phi0, Xi0, zeta0 = matter_ic(k, -TM)
    r, i = evolve(rhs_sharp, -TM, TM, [Phi0, Xi0], (k,))
    Phi = r.y[0, -1] + 1j * i.y[0, -1]; Xi = r.y[1, -1] + 1j * i.y[1, -1]
    a, H = Sharp.a(TM), Sharp.H(TM); Hd = -1.5 * H * H
    zeta = zeta_of(a, H, Xi, Phi); zdot = zetadot_of(a, H, Hd, k, Phi)
    return dict(lam=float(abs(const_branch_zeta(k, TM, zeta, zdot) / zeta0)), zeta0=zeta0)


def lam_naive(k):
    """REJECTED control: the NAIVE self-adjoint junction [Phi]=0, [mu Phi']=0, i.e.
    Xi_+ = Xi_- + (mu_+ - mu_-) H_conf Phi  instead of  Xi_+ = Xi_- ."""
    Phi0, Xi0, zeta0 = matter_ic(k, -TM)
    a, H = Sharp.a(-TM), Sharp.H(-TM)
    mu_in, mu_out = -1.0 / (-1.5 * H * H), -1.0 / UPS
    y = [Phi0, Xi0 + (mu_out - mu_in) * (a * H) * Phi0]
    r, i = evolve(rhs_sharp, -TM, TM, y, (k,))
    Phi = r.y[0, -1] + 1j * i.y[0, -1]; Xi = r.y[1, -1] + 1j * i.y[1, -1]
    a, H = Sharp.a(TM), Sharp.H(TM)
    mu_in, mu_out = -1.0 / UPS, -1.0 / (-1.5 * H * H)
    Xi = Xi + (mu_out - mu_in) * (a * H) * Phi
    Hd = -1.5 * H * H
    zeta = zeta_of(a, H, Xi, Phi); zdot = zetadot_of(a, H, Hd, k, Phi)
    return float(abs(const_branch_zeta(k, TM, zeta, zdot) / zeta0))


def lam_smooth(k, d, eps_rel=1e-3):
    """Same, with the Hdot jumps replaced by C^2 blends of half-width d: the background then genuinely
    crosses rho + p = 0 inside each layer, where scheme S2's own z^2 = 2a^2 eps VANISHES."""
    bg = SmoothBG(d, eps=eps_rel * UPS)
    t0, t1 = -TM - 2 * d, TM + 2 * d
    Phi0, Xi0, zeta0 = matter_ic(k, t0)
    r, i = evolve(rhs_smooth, t0, t1, [Sharp.H(t0), np.log(Sharp.a(t0)), Phi0, Xi0], (k, bg),
                  method="LSODA")
    H = r.y[0, -1]; a = np.exp(r.y[1, -1])
    Phi = r.y[2, -1] + 1j * i.y[2, -1]; Xi = r.y[3, -1] + 1j * i.y[3, -1]
    Hd = bg.Hd_of(t1, H)
    zeta = zeta_of(a, H, Xi, Phi); zdot = zetadot_of(a, H, Hd, k, Phi)
    return dict(lam=float(abs(const_branch_zeta(k, t1, zeta, zdot) / zeta0)),
                bg_drift=float(abs(a / Sharp.a(t1) - 1)))


# ------------------------------------------------------------------ reference S1 / S2 (committed machinery)
def lam_scheme(keta, scheme):
    """Same definition as the Phi route: constant-branch amplitude after / zeta(-tm)."""
    k = keta / ETA_B
    bm = BounceModes(Q, k, scheme)
    z0 = bm.window(-TM)[0]
    z_, zd = bm.late(TM)
    return float(abs(const_branch_zeta(k, TM, complex(z_), complex(zd)) / z0))


# ------------------------------------------------------------------ gates
def gate_G1():
    a, H = Sharp.a(TI), Sharp.H(TI)
    r = zeta_of(a, H, Xi_of(a, H, 0.0, 1.0) * 0 + (-1.0 / (-1.5 * H * H)) * a * (0 + H * 1.0), 1.0)
    # Phi = 1, Phi' = 0  ->  Xi = mu * H_conf * Phi = (-1/Hdot) a H
    Xi = (-1.0 / (-1.5 * H * H)) * (a * H) * 1.0
    r = zeta_of(a, H, Xi, 1.0)
    return dict(zeta_over_Phi=float(r), target=5.0 / 3.0, err=float(abs(r / (5.0 / 3.0) - 1)))

def gate_G2(k):
    ta, tb = TI, 0.02 * TI
    Phi0, Xi0, _ = matter_ic(k, ta)
    _, _, zeta_b_exact = matter_ic(k, tb)
    r, i = evolve(rhs_sharp, ta, tb, [Phi0, Xi0], (k,))
    Phi = r.y[0, -1] + 1j * i.y[0, -1]; Xi = r.y[1, -1] + 1j * i.y[1, -1]
    zb = zeta_of(Sharp.a(tb), Sharp.H(tb), Xi, Phi)
    return dict(err=float(abs(zb / zeta_b_exact - 1)))

def gate_G3(k):
    """Wronskian of the (Phi, Xi) system across the whole bounce: W = Phi_1 Xi_2 - Phi_2 Xi_1
    The system matrix [[-H, -Hdot/a], [a + k^2/(a Hdot), H]] is TRACELESS, so W is exactly conserved."""
    def prop(y0):
        r, i = evolve(rhs_sharp, -20.0, 20.0, list(y0), (k,))
        return np.array([r.y[0, -1], r.y[1, -1]])
    A0, B0 = np.array([1.0, 0.0]), np.array([0.0, 1.0])
    A1, B1 = prop(A0), prop(B0)
    W0 = A0[0] * B0[1] - B0[0] * A0[1]
    W1 = A1[0] * B1[1] - B1[0] * A1[1]
    return dict(W0=float(W0), W1=float(W1), err=float(abs(W1 / W0 - 1)))


# ------------------------------------------------------------------ main
def main():
    log("=" * 104)
    log("LEG B / B' - scheme-free linear transfer lambda_zeta through the Quintin-type bounce, via (Phi, Xi)")
    log("background Ups=%.6f tm=%.3f a_m=%.6f eta_B=%.6f | t in [%g, %g] | rtol=%g atol=%g"
        % (UPS, TM, AM, ETA_B, TI, TF, RTOL, ATOL))
    log("=" * 104)

    kp = KS[1] / ETA_B
    g1, g2, g3 = gate_G1(), gate_G2(kp), gate_G3(kp)
    log("\n[G1] matter-domination limit  zeta/Phi (Phi = const) = %.12f  (5/3)  rel err %.2e -> %s"
        % (g1["zeta_over_Phi"], g1["err"], "PASS" if g1["err"] < 1e-6 else "FAIL"))
    log("[G2] constant-eps control (pure matter contraction, where S1 == S2 identically):"
        " Phi route vs the exact vacuum mode, rel err %.2e -> %s" % (g2["err"], "PASS" if g2["err"] < 1e-6 else "FAIL"))
    log("[G3] Wronskian Phi_1 Xi_2 - Phi_2 Xi_1 (traceless system) across t in [-20,20] (both junctions + H=0): rel err %.2e -> %s"
        % (g3["err"], "PASS" if g3["err"] < 1e-8 else "FAIL"))
    OUT["gates"] = dict(G1=dict(g1, **{"pass": bool(g1["err"] < 1e-6)}),
                        G2=dict(g2, **{"pass": bool(g2["err"] < 1e-6)}),
                        G3=dict(g3, **{"pass": bool(g3["err"] < 1e-8)}))

    log("\n[ref] committed S1/S2 machinery (lane9b2 BounceModes), |zeta_after/zeta(-tm)|:")
    ref = {}
    for keta in KS:
        ref[keta] = dict(S1=lam_scheme(keta, "S1"), S2=lam_scheme(keta, "S2"))
        log("      k eta_B=%-8g S1 %.4f    S2 %.4f" % (keta, ref[keta]["S1"], ref[keta]["S2"]))
    OUT["reference_S1_S2"] = {str(k): v for k, v in ref.items()}

    log("\n[B] SHARP background, Bardeen (Phi, Xi) integrated straight through -- no junction prescription:")
    sharp = {}
    for keta in KS:
        k = keta / ETA_B
        r = lam_sharp(k); nv = lam_naive(k)
        sharp[keta] = dict(lam=r["lam"], naive_rejected=nv,
                           dev_S1=abs(r["lam"] / ref[keta]["S1"] - 1), dev_S2=abs(r["lam"] / ref[keta]["S2"] - 1))
        log("      k eta_B=%-8g lambda_Phi = %.6f | dev from S1 %.4f, from S2 %.2e | REJECTED naive junction: %.5g"
            % (keta, r["lam"], sharp[keta]["dev_S1"], sharp[keta]["dev_S2"], nv))
    OUT["sharp"] = {str(k): v for k, v in sharp.items()}

    log("\n[B'] SMOOTHED-junction control -- the background genuinely crosses rho+p = 0, where scheme S2's")
    log("     own variable z^2 = 2a^2 eps VANISHES and zeta is LOG-DIVERGENT, while Phi stays finite.")
    log("     1/Hdot is taken as the principal value Hdot/(Hdot^2 + eps^2); both d and eps are scanned.")
    smooth = {}
    for keta in KS:
        k = keta / ETA_B; row = {}
        for d in [0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005]:
            for er in ([1e-3] if d < 0.02 else [1e-2, 1e-3]):
                try:
                    row["%g|%g" % (d, er)] = lam_smooth(k, d, er)["lam"]
                except Exception as e:
                    row["%g|%g" % (d, er)] = None
        smooth[keta] = row
        log("      k eta_B=%-8g " % keta + "  ".join(
            "%s:%s" % (kk, ("%.5f" % v) if v is not None else "FAIL") for kk, v in row.items()))
        vals = [v for v in row.values() if v is not None]
        if len(vals) >= 4:
            tail = vals[-3:]
            log("               last three (smallest d): %s -> spread %.2e about %.5f  [G4 %s]"
                % (", ".join("%.5f" % v for v in tail), np.ptp(tail) / np.mean(tail), np.mean(tail),
                   "PASS" if np.ptp(tail) / np.mean(tail) < 0.02 else "FAIL"))
            rich = 2 * vals[-1] - vals[-2]          # lambda(d) - lambda(0) is linear in d (measured)
            log("               Richardson d -> 0 : %.6f   (sharp-background lambda_Phi = %.6f, rel %.1e)"
                % (rich, sharp[keta]["lam"], abs(rich / sharp[keta]["lam"] - 1)))
            OUT.setdefault("smooth_summary", {})[str(keta)] = dict(
                limit_richardson=float(rich), vs_sharp=float(abs(rich / sharp[keta]["lam"] - 1)),
                spread_last3=float(np.ptp(tail) / np.mean(tail)),
                G4_pass=bool(np.ptp(tail) / np.mean(tail) < 0.02), n=len(vals))
    OUT["smooth"] = {str(k): r for k, r in smooth.items()}

    # ------------------------------------------------------------------ verdict against the pre-registration
    L = np.mean([sharp[k]["lam"] for k in KS])
    dS1 = abs(L / np.mean([ref[k]["S1"] for k in KS]) - 1)
    dS2 = abs(L / np.mean([ref[k]["S2"] for k in KS]) - 1)
    verdict = ("OUTCOME-S2" if (dS2 <= 0.02 and dS1 > 0.02) else
               "OUTCOME-S1" if (dS1 <= 0.02 and dS2 > 0.02) else "OUTCOME-NEITHER")
    log("\n" + "=" * 104)
    log("VERDICT (against PREREGISTRATION.md section 3):  L = %.6f ; |L/S1 - 1| = %.4f ; |L/S2 - 1| = %.2e"
        % (L, dS1, dS2))
    log("  -> %s" % verdict)
    log("=" * 104)
    OUT["verdict"] = dict(L=float(L), dev_S1=float(dS1), dev_S2=float(dS2), outcome=verdict)

    OUT["runtime_s"] = time.time() - T0
    try:
        import matplotlib; matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.0))
        keta = KS[0]; k = keta / ETA_B
        ts = np.concatenate([np.linspace(-6 * TM, -TM, 300), np.linspace(-TM, TM, 500)[1:-1],
                             np.linspace(TM, 6 * TM, 300)])
        for nm, sc, col in (("S1  ($z=a$)", "S1", "C0"), ("S2  ($z^2=2a^2\\epsilon$)", "S2", "C1")):
            bm = BounceModes(Q, k, sc)
            zz = np.array([complex(bm.window(t)[0]) if abs(t) <= TM else
                           complex(bm.early(t)[0] if t < 0 else bm.late(t)[0]) for t in ts])
            ax[0].plot(ts / TM, np.abs(zz / complex(bm.window(-TM)[0])), col, label=nm)
        Phi0, Xi0, z0 = matter_ic(k, -TM)
        segs = []
        for (ta, tb, y0) in [(-TM, -6 * TM, [Phi0, Xi0]), (-TM, 6 * TM, [Phi0, Xi0])]:
            tt = np.linspace(ta, tb, 700)
            r, i2 = evolve(rhs_sharp, ta, tb, y0, (k,), teval=tt)
            aa = np.array([Sharp.a(t) for t in tt]); HH = np.array([Sharp.H(t) for t in tt])
            Hd = np.where(np.abs(tt) <= TM, UPS, -1.5 * HH ** 2)
            segs.append((tt, np.abs(zeta_of(aa, HH, r.y[1] + 1j * i2.y[1], r.y[0] + 1j * i2.y[0]) / z0)))
        for n, (tt, zb) in enumerate(segs):
            ax[0].plot(tt / TM, zb, "k--", lw=2, label=("Bardeen $\\Phi$ route (scheme-free)" if n == 0 else None))
        ax[0].axvline(0, color="0.7", lw=0.6, ls=":"); ax[0].axvline(-1, color="0.7", lw=0.6, ls=":")
        ax[0].axvline(1, color="0.7", lw=0.6, ls=":")
        ax[0].annotate("S1: 6.06", (5.2, 5.4), fontsize=8, color="C0")
        ax[0].annotate("S2 = $\\Phi$: 0.970", (3.0, 0.60), fontsize=8, color="C1")
        ax[0].set_xlabel("$t/t_m$  (bounce $H=0$ at 0, NEC boundaries at $\\pm1$)")
        ax[0].set_ylabel("$|\\zeta(t)/\\zeta(-t_m)|$"); ax[0].set_yscale("log"); ax[0].set_ylim(1e-2, 3e1)
        ax[0].set_title("linear transfer of $\\zeta$, $k\\eta_B=10^{-3}$", fontsize=10)
        ax[0].legend(fontsize=8, loc="lower left"); ax[0].grid(alpha=0.3)
        for keta in KS:
            row = smooth[keta]
            ds = sorted({float(kk.split("|")[0]) for kk in row})
            vv = [row["%g|%g" % (d, 1e-3 if d < 0.02 else 1e-2)] for d in ds]
            ax[1].plot(ds, vv, "o-", ms=3, label="$k\\eta_B=%g$" % keta)
        ax[1].axhline(np.mean([ref[k2]["S2"] for k2 in KS]), color="C1", ls="--", lw=1,
                      label="S2 = %.4f" % np.mean([ref[k2]["S2"] for k2 in KS]))
        ax[1].axhline(np.mean([sharp[k2]["lam"] for k2 in KS]), color="k", ls=":", lw=1.2,
                      label="$\\Phi$ route (sharp)")
        ax[1].set_xscale("log"); ax[1].set_xlabel("smoothing half-width $d/t_m \\times 2$")
        ax[1].set_ylabel("$|\\lambda_\\zeta|$")
        ax[1].set_title("smoothed NEC crossing: $d\\to0$ control", fontsize=10)
        ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)
        fig.tight_layout(); fig.savefig("row9_scheme_independence.png", dpi=140)
        log("[fig] row9_scheme_independence.png")
    except Exception as e:
        log("[fig] skipped: %s" % e)
    with open("row9_numeric.log", "w") as f: f.write("\n".join(LOG) + "\n")
    with open("results.json", "w") as f: json.dump(OUT, f, indent=2, default=str)
    log("\n[done] %.1f s" % OUT["runtime_s"])


if __name__ == "__main__":
    main()

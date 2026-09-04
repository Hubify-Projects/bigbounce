#!/usr/bin/env python3
"""Lane 9b-2: Delta f_NL^bounce in scheme S2 from the RAW ADM cubic Lagrangian on exact S2 modes.

Raw form = Maldacena 2003 Eq. 2.4 (M_pl^-2 = 8 pi G = 1):
    L = (1/2) sqrt(h) [ N R3 - 2 N V + N^-1 (E_ij E^ij - E^2) + N^-1 phidot^2 ],
comoving gauge h_ij = a^2 e^{2 zeta} delta_ij, N = 1 + N1, N_i = d_i psi, expanded to CUBIC order in
(zeta, N1, psi) with NO integration by parts.  Background enters only through (a, H, Hdot):
phidot^2 = rho + p = -2 Hdot,  V = 3 H^2 + Hdot  (c_s = 1 effective fluid, P linear in X).
The Fourier kernel of the cubic Lagrangian for three legs (k_1, k_2, k_3) is obtained by inserting
plane-wave superpositions and extracting the trilinear E1 E2 E3 coefficient (all 3! leg attachments
counted once, no hand symmetry factors -- same counting as lane (b) and the adjudication engine).
In-in: B = -2 Im[ u1 u2 u3(t*) int dt K3(t; u*_j, udot*_j, N1_j, psi_j) ],  f_NL = (5/6) B / sum P P.
Nothing here is tuned to any target value.
"""
import json, os, sys, time
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
_lines = []


def log(m=""):
    print(m, flush=True); _lines.append(m)


# ---------------------------------------------------------------- multilinear plane-wave algebra
class MP:
    """Polynomial in plane-wave symbols E_j, truncated to multilinear terms (each E_j at most once).
    Stored as {frozenset(legs): sympy coefficient}."""
    __slots__ = ("d",)

    def __init__(self, d=None):
        self.d = dict(d) if d else {}

    @staticmethod
    def const(c):
        return MP({frozenset(): sp.sympify(c)})

    def __add__(self, o):
        o = o if isinstance(o, MP) else MP.const(o)
        r = MP(self.d)
        for k, v in o.d.items():
            r.d[k] = r.d.get(k, 0) + v
        return r

    __radd__ = __add__

    def __neg__(self):
        return MP({k: -v for k, v in self.d.items()})

    def __sub__(self, o):
        return self + (-(o if isinstance(o, MP) else MP.const(o)))

    def __rsub__(self, o):
        return MP.const(o) - self

    def __mul__(self, o):
        if not isinstance(o, MP):
            return MP({k: v * o for k, v in self.d.items()})
        r = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                if k1 & k2:
                    continue
                k = k1 | k2
                r[k] = r.get(k, 0) + v1 * v2
        return MP(r)

    __rmul__ = __mul__

    def coeff(self, legs):
        return sp.expand(self.d.get(frozenset(legs), 0))


def mp_exp(x, n):
    """exp(n x) truncated at cubic order (sufficient for multilinear extraction with <= 3 legs)."""
    return MP.const(1) + n * x + sp.Rational(1, 2) * n**2 * (x * x) + sp.Rational(1, 6) * n**3 * (x * x * x)


def mp_inv1p(x):
    """1/(1+x) truncated at cubic order."""
    return MP.const(1) - x + x * x - x * x * x


# ---------------------------------------------------------------- symbols
a_s, H_s, Hd_s = sp.symbols("a H Hd")
LEGS = (1, 2, 3)
Z = {j: sp.Symbol(f"Z{j}") for j in LEGS}     # zeta_j
D = {j: sp.Symbol(f"D{j}") for j in LEGS}     # zetadot_j (cosmic time)
N = {j: sp.Symbol(f"N{j}") for j in LEGS}     # N1_j
P = {j: sp.Symbol(f"P{j}") for j in LEGS}     # psi_j
KX = {j: sp.Symbol(f"kx{j}") for j in LEGS}
KY = {j: sp.Symbol(f"ky{j}") for j in LEGS}
KV = {j: (KX[j], KY[j], sp.Integer(0)) for j in LEGS}   # coplanar triangle, k_z = 0


# ---------------------------------------------------------------- the raw ADM Lagrangian (symbolic)
def _field(amp, legs):
    return MP({frozenset([j]): amp[j] for j in legs})


def _grad(amp, i, legs):                       # d_i F  ->  i k_i F
    return MP({frozenset([j]): sp.I * KV[j][i] * amp[j] for j in legs})


def _grad2(amp, i, l, legs):                   # d_i d_l F  ->  -k_i k_l F
    return MP({frozenset([j]): -KV[j][i] * KV[j][l] * amp[j] for j in legs})


def raw_lagrangian(legs):
    """(1/2) sqrt(h) [N R3 - 2 N V + N^-1 (E_ij E^ij - E^2) + N^-1 phidot^2] as an MP over `legs`,
    with phidot^2 = -2 Hd, V = 3 H^2 + Hd, h_ij = a^2 e^{2 zeta} delta_ij, N = 1 + N1, N_i = d_i psi."""
    zeta, N1 = _field(Z, legs), _field(N, legs)
    dz = [_grad(Z, i, legs) for i in range(3)]
    dp = [_grad(P, i, legs) for i in range(3)]
    ddz = [[_grad2(Z, i, l, legs) for l in range(3)] for i in range(3)]
    ddp = [[_grad2(P, i, l, legs) for l in range(3)] for i in range(3)]
    lap_z = ddz[0][0] + ddz[1][1] + ddz[2][2]
    gz2 = dz[0] * dz[0] + dz[1] * dz[1] + dz[2] * dz[2]
    gzgp = dz[0] * dp[0] + dz[1] * dp[1] + dz[2] * dp[2]
    zdot = _field(D, legs)
    e2z, e3z, em2z, em4z = mp_exp(zeta, 2), mp_exp(zeta, 3), mp_exp(zeta, -2), mp_exp(zeta, -4)
    invN = mp_inv1p(N1)
    Nl = MP.const(1) + N1
    # M_ij = nabla_i nabla_j psi on the conformally flat slice
    M = [[ddp[i][l] - dz[i] * dp[l] - dz[l] * dp[i] + (gzgp if i == l else MP.const(0))
          for l in range(3)] for i in range(3)]
    trM = M[0][0] + M[1][1] + M[2][2]
    trM2 = MP.const(0)
    for i in range(3):
        for l in range(3):
            trM2 = trM2 + M[i][l] * M[l][i]
    Hz = zdot + H_s                                   # H + zetadot
    EE = (Hz * Hz) * (-6) + (Hz * em2z * trM) * (4 / a_s**2) + (em4z * (trM2 - trM * trM)) * (1 / a_s**4)
    R3 = (em2z * (lap_z * 2 + gz2)) * (-2 / a_s**2)
    V = 3 * H_s**2 + Hd_s
    phidot2 = -2 * Hd_s
    L = e3z * (Nl * R3 + Nl * (-2 * V) + invN * EE + invN * phidot2) * (a_s**3 / 2)
    return L


def build_kernels():
    """Cubic Fourier kernel K3 (coefficient of E1E2E3) and quadratic kernel K2 (E1E2, k2 = -k1)."""
    t0 = time.time()
    L3 = raw_lagrangian(LEGS)
    K3 = L3.coeff(LEGS)
    L2 = raw_lagrangian((1, 2))
    K2 = L2.coeff((1, 2)).subs({KX[2]: -KX[1], KY[2]: -KY[1]})
    log(f"[symbolic] raw ADM cubic kernel built: {len(sp.Add.make_args(K3))} terms ({time.time() - t0:.1f} s)")
    return K3, K2


def constraint_gate(K2):
    """Gate (i-a): vary the quadratic Fourier Lagrangian w.r.t. N1(-k) and psi(-k):
    must give N1 = zetadot/H and psi = -zeta/H + chi, chi = -a^2 eps zetadot/k^2, eps = -Hd/H^2."""
    k2 = KX[1]**2 + KY[1]**2
    eqN = sp.diff(K2, N[2]); eqP = sp.diff(K2, P[2])
    sol = sp.solve([eqN, eqP], [N[1], P[1]], dict=True)[0]
    eps = -Hd_s / H_s**2
    N_exp = D[1] / H_s
    P_exp = -Z[1] / H_s - a_s**2 * eps * D[1] / k2
    okN = sp.simplify(sol[N[1]] - N_exp) == 0
    okP = sp.simplify(sol[P[1]] - P_exp) == 0
    log(f"[gate i-a] Hamiltonian constraint -> N1 = {sp.simplify(sol[N[1]])}   (expected zetadot/H): {okN}")
    log(f"[gate i-a] momentum constraint    -> psi = {sp.simplify(sol[P[1]])}   (expected -zeta/H - a^2 eps zetadot/k^2): {okP}")
    assert okN and okP, "raw quadratic Lagrangian does not reproduce Maldacena Eq. 2.13-2.14"
    return dict(N1=str(sp.simplify(sol[N[1]])), psi=str(sp.simplify(sol[P[1]])), passed=bool(okN and okP))


# ---------------------------------------------------------------- Quintin-type background (cosmic time, exact)
from math import factorial
from scipy.special import erf


class Quintin:
    """H = Ups t, a = exp(Ups t^2/2) for |t| <= tm; matter (eps = 3/2) outside, matched at |t| = tm = dtB/2
    with Ups = 8/(3 dtB^2) (same piecewise background as a2_transmission_linear.bg_quintin)."""

    def __init__(self, dtB=1.0):
        self.Ups, self.tm = 8.0 / (3.0 * dtB**2), dtB / 2.0
        self.am = np.exp(self.Ups * self.tm**2 / 2.0)
        self.eta_B = float(np.sqrt(np.pi / (2 * self.Ups)) * erf(self.tm * np.sqrt(self.Ups / 2)))
        self.A = self.am**3 / (9.0 * self.tm**2)              # a = A eta_m^2 in the matter phases
        self.eta_off = 3.0 * self.tm / self.am - self.eta_B     # bounce-centred eta = eta_m + sgn * eta_off

    def a(self, t):
        t = np.asarray(t, dtype=float)
        return np.where(np.abs(t) <= self.tm, np.exp(self.Ups * np.minimum(t * t, self.tm**2) / 2),
                        self.am * (np.maximum(np.abs(t), self.tm) / self.tm) ** (2.0 / 3.0))

    def H(self, t):
        t = np.asarray(t, dtype=float)
        return np.where(np.abs(t) <= self.tm, self.Ups * t, 2.0 / (3.0 * np.where(np.abs(t) > self.tm, t, 1.0)))

    def Hd(self, t):
        t = np.asarray(t, dtype=float)
        return np.where(np.abs(t) <= self.tm, self.Ups, -1.5 * self.H(t) ** 2)

    def eta_m(self, t):                                       # matter-phase conformal time (a = A eta_m^2)
        return np.sign(t) * 3.0 * self.tm ** (2.0 / 3.0) * np.abs(t) ** (1.0 / 3.0) / self.am

    def eta(self, t):                                         # bounce-centred conformal time
        t = np.asarray(t, dtype=float)
        inw = np.sqrt(np.pi / (2 * self.Ups)) * erf(np.clip(t, -self.tm, self.tm) * np.sqrt(self.Ups / 2))
        return np.where(np.abs(t) <= self.tm, inw, self.eta_m(t) + np.sign(t) * self.eta_off)

    def t_of_eta(self, eta):                                  # inverse, matter phases only (|eta| > eta_B)
        em = abs(eta) - self.eta_off
        return np.sign(eta) * (em * self.am / (3.0 * self.tm ** (2.0 / 3.0))) ** 3


def matter_mode(k, eta_m, alpha=1.0, beta=0.0):
    """v(eta_m) = [alpha e^{-ik eta}(1 - i/(k eta)) + beta e^{+ik eta}(1 + i/(k eta))]/sqrt(2k); returns v, dv/deta."""
    e = eta_m
    fp, fm = np.exp(-1j * k * e) * (1 - 1j / (k * e)), np.exp(1j * k * e) * (1 + 1j / (k * e))
    dfp = np.exp(-1j * k * e) * (-1j * k * (1 - 1j / (k * e)) + 1j / (k * e * e))
    dfm = np.exp(1j * k * e) * (1j * k * (1 + 1j / (k * e)) - 1j / (k * e * e))
    return (alpha * fp + beta * fm) / np.sqrt(2 * k), (alpha * dfp + beta * dfm) / np.sqrt(2 * k)


def matter_real_basis(k, eta_m):
    """Real solutions of v'' + (k^2 - 2/eta^2) v = 0: g1 = cos x - sin x/x (~ -x^2/3, the constant-zeta branch),
    g2 = sin x + cos x/x (the eta^-3 branch), x = k eta; returns g1, g2, dg1/deta, dg2/deta (well conditioned)."""
    x = k * eta_m
    if abs(x) < 0.5:
        n = np.arange(0, 14)
        c = (-1.0) ** n * (2 * n) / np.array([factorial(2 * m + 1) for m in n], dtype=float)
        g1 = float((c * x ** (2 * n)).sum())
        dg1 = float((c[1:] * 2 * n[1:] * x ** (2 * n[1:] - 1)).sum())
    else:
        g1 = np.cos(x) - np.sin(x) / x
        dg1 = -np.sin(x) - np.cos(x) / x + np.sin(x) / x**2
    g2 = np.sin(x) + np.cos(x) / x
    dg2 = g1 - np.cos(x) / x**2
    return g1, g2, k * dg1, k * dg2


def window_series(bg, k, scheme, order=90):
    """Two power-series basis solutions of the window MS equation (coefficient arrays).
    S2: t zdd + (3 Ups t^2 - 2) zd + k^2 t e^{-Ups t^2} z = 0  (Frobenius exponents 0, 3; c1 = 0 forced).
    S1: zdd + 3 Ups t zd + k^2 e^{-Ups t^2} z = 0            (regular; c0, c1 free)."""
    U = bg.Ups
    g = [(-U) ** m / factorial(m) for m in range(order // 2 + 2)]
    basis = []
    for s in [(1.0, 0.0), (0.0, 1.0)]:               # (c0, c3) for S2 ; (c0, c1) for S1
        c = np.zeros(order + 1)
        if scheme == "S2":
            c[0], c[3] = s
            c[2] = k * k * c[0] / 2.0
            for n in range(4, order + 1):
                conv = sum(g[m] * c[n - 2 - 2 * m] for m in range(0, (n - 2) // 2 + 1))
                c[n] = (-3 * U * (n - 2) * c[n - 2] - k * k * conv) / (n * (n - 3))
        else:
            c[0], c[1] = s
            for n in range(0, order - 1):
                conv = sum(g[m] * c[n - 2 * m] for m in range(0, n // 2 + 1))
                c[n + 2] = -(3 * U * n * c[n] + k * k * conv) / ((n + 2) * (n + 1))
        basis.append(c)
    return basis


def series_eval(c, t):
    """value, first derivative, and zd/t (regular at t = 0) of sum c_n t^n."""
    n = np.arange(len(c))
    tt = np.asarray(t, dtype=float)[..., None]
    f = (c * tt ** n).sum(-1)
    fd = (n[1:] * c[1:] * tt ** (n[1:] - 1)).sum(-1)
    fd_over_t = (n[2:] * c[2:] * tt ** (n[2:] - 2)).sum(-1)      # exact when c1 = 0 (S2 Frobenius)
    return f, fd, fd_over_t


# ---------------------------------------------------------------- modes through the bounce (both schemes)
class BounceModes:
    """zeta_k(t) through the Quintin bounce.  Contraction: adiabatic vacuum matter mode, zeta = v/z,
    z = a sqrt(2 eps_c) (S2: eps_c = 3/2 true; S1: eps_c = 1/2, z = a).  Junctions at |t| = tm: zeta and
    a^3 eps zetadot continuous (S2: zetadot flips sign since eps: +3/2 -> -3/2; S1: eps_eff constant).
    Window: exact power series (window_series).  Expansion: exact matter basis (alpha, beta)."""

    def __init__(self, bg, k, scheme):
        self.bg, self.k, self.scheme = bg, float(k), scheme
        self.eps_c = 1.5 if scheme == "S2" else 0.5
        tm, am = bg.tm, bg.am
        s2e = np.sqrt(2 * self.eps_c)
        # contraction side of the junction
        em = bg.eta_m(-tm)
        v, dv = matter_mode(k, em)
        z, dz = s2e * am, s2e * am**2 * bg.H(-tm)              # dz/deta = sqrt(2eps) a' = sqrt(2eps) a^2 H
        zeta, zp = v / z, (dv * z - v * dz) / z**2
        zd = zp / am
        if scheme == "S2":
            zd = -zd                                            # eps_-/eps_+ = (3/2)/(-3/2)
        self.f1, self.f2 = window_series(bg, k, scheme)
        F = np.array([[series_eval(self.f1, -tm)[0], series_eval(self.f2, -tm)[0]],
                      [series_eval(self.f1, -tm)[1], series_eval(self.f2, -tm)[1]]])
        self.A, self.B = np.linalg.solve(F, np.array([zeta, zd]))
        # expansion side
        zeta_p, zd_p, _ = self.window(tm)
        if scheme == "S2":
            zd_p = -zd_p
        g1, g2, dg1, dg2 = matter_real_basis(k, bg.eta_m(tm))
        zz, dzz = s2e * am, s2e * am**2 * bg.H(tm)
        vv, vvp = zz * zeta_p, dzz * zeta_p + zz * zd_p * am
        self.cA, self.cB = np.linalg.solve(np.array([[g1, g2], [dg1, dg2]]), np.array([vv, vvp]))
        # S2 regular constraint data: psi = (a^2 w/k^2 - zeta)/(Ups t)  -> series of the numerator / t
        if scheme == "S2":
            self.p1, self.p2 = [self._psi_series(c) for c in (self.f1, self.f2)]

    def _psi_series(self, c):
        U, k2 = self.bg.Ups, self.k**2
        n = len(c)
        gp = [U**m / factorial(m) for m in range(n // 2 + 2)]           # a^2 = e^{Ups t^2}
        w = np.zeros(n); w[:-2] = np.arange(2, n) * c[2:]                  # w = zd/t = sum (n c_n) t^{n-2}
        num = np.zeros(n)
        for j in range(n):
            num[j] = sum(gp[m] * w[j - 2 * m] for m in range(0, j // 2 + 1)) / k2 - c[j]
        assert abs(num[0]) < 1e-12 * max(1.0, abs(c[0]))                    # residue cancellation
        return num[1:] / U                                                  # psi = sum num_{j+1} t^j / Ups

    def window(self, t):
        z1, d1, w1 = series_eval(self.f1, t); z2, d2, w2 = series_eval(self.f2, t)
        return self.A * z1 + self.B * z2, self.A * d1 + self.B * d2, self.A * w1 + self.B * w2

    def psi_window(self, t):
        n = np.arange(len(self.p1)); tt = np.asarray(t, dtype=float)[..., None]
        return self.A * (self.p1 * tt**n).sum(-1) + self.B * (self.p2 * tt**n).sum(-1)

    def late(self, t):
        """(zeta, zetadot) in the expansion phase t >= tm."""
        a = self.bg.a(t)
        g1, g2, dg1, dg2 = matter_real_basis(self.k, float(self.bg.eta_m(t)))
        v, dv = self.cA * g1 + self.cB * g2, self.cA * dg1 + self.cB * dg2
        z, dz = np.sqrt(2 * self.eps_c) * a, np.sqrt(2 * self.eps_c) * a**2 * self.bg.H(t)
        return v / z, (dv * z - v * dz) / z**2 / a

    def early(self, t):
        em = self.bg.eta_m(t); a = self.bg.a(t)
        v, dv = matter_mode(self.k, em)
        z, dz = np.sqrt(2 * self.eps_c) * a, np.sqrt(2 * self.eps_c) * a**2 * self.bg.H(t)
        return v / z, (dv * z - v * dz) / z**2 / a

    def wronskian(self, t):
        """2 a^3 eps (u udot* - u* udot) / i  (must be 1; eps = scheme's eps at t)."""
        bg = self.bg
        if abs(t) < bg.tm:
            u, ud, _ = self.window(t); eps = (-bg.Hd(t) / bg.H(t)**2) if self.scheme == "S2" else 0.5
        else:
            u, ud = (self.late(t) if t > 0 else self.early(t)); eps = self.eps_c
        return float(np.real(2 * bg.a(t)**3 * eps * (u * np.conj(ud) - np.conj(u) * ud) / 1j))


# ---------------------------------------------------------------- in-in engine on the Fourier kernel
from scipy.integrate import simpson
from scipy.special import hankel1, hankel2

KARGS = ([a_s, H_s, Hd_s] + [KX[j] for j in LEGS] + [KY[j] for j in LEGS] + [Z[j] for j in LEGS]
         + [D[j] for j in LEGS] + [N[j] for j in LEGS] + [P[j] for j in LEGS])


def kernel_fn(K3):
    return sp.lambdify(KARGS, K3, "numpy")


def triangle(kL, kS):
    """squeezed isoceles: k1 = kL (x-axis), |k2| = |k3| = kS, k1 + k2 + k3 = 0; coplanar."""
    h = np.sqrt(kS**2 - kL**2 / 4.0)
    return [(kL, 0.0), (-kL / 2.0, h), (-kL / 2.0, -h)]


def kernel_values(K3f, kv, a, H, Hd, legs):
    """legs: list of dicts with Z, D (conjugated mode values on the grid) and N, P (constraint solutions)."""
    kx, ky = [v[0] for v in kv], [v[1] for v in kv]
    return K3f(a, H, Hd, *kx, *ky, *[l["Z"] for l in legs], *[l["D"] for l in legs],
               *[l["N"] for l in legs], *[l["P"] for l in legs])


def onshell_legs(ZD, kv, a, H, Hd, eps):
    """generic constraint substitution N1 = zetadot/H, psi = -zeta/H - a^2 eps zetadot/k^2 (H != 0)."""
    out = []
    for (Zj, Dj), (kx, ky) in zip(ZD, kv):
        k2 = kx * kx + ky * ky
        out.append(dict(Z=Zj, D=Dj, N=Dj / H, P=-Zj / H - a**2 * eps * Dj / k2))
    return out


def fnl_from(K, x, jac, u_star):
    """B = -2 Im[u1 u2 u3(t*) int K jac dx];  f_NL = (5/6) B / (P1P2 + P1P3 + P2P3)."""
    integ = simpson(np.real(K * jac), x=x) + 1j * simpson(np.imag(K * jac), x=x)
    pref = u_star[0] * u_star[1] * u_star[2]
    B = -2.0 * float(np.imag(pref * integ))
    Pw = [float(abs(u) ** 2) for u in u_star]
    Psum = Pw[0] * Pw[1] + Pw[0] * Pw[2] + Pw[1] * Pw[2]
    return 5.0 / 6.0 * B / Psum, integ, Pw


PERMS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]


def mald_kernel_values(kv, ZD, a, eps):
    """Maldacena/Chen integrated-by-parts cubic kernel (lane (a) table, c_s = 1, eta_sr = 0, cosmic time):
    V2 a^3 eps^2 z zd^2 ; V3 a eps^2 z (dz)^2 ; V4 -2 a^3 eps^2 zd dz d(chit) ; V6 a^3 eps^3/2 ; V7 a^3 eps^3/4."""
    kk = np.array(kv); Dm = kk @ kk.T; ks = [np.hypot(*v) for v in kv]
    K = 0
    for (i, j, l) in PERMS:
        Zi, Di = ZD[i]; Zj, Dj = ZD[j]; Zl, Dl = ZD[l]
        K = (K + a**3 * eps**2 * Zi * Dj * Dl - a * eps**2 * Dm[j, l] * Zi * Zj * Zl
             - 2 * a**3 * eps**2 * (Dm[j, l] / ks[l]**2) * Di * Zj * Dl
             + a**3 * eps**3 / 2 * (Dm[i, j] / ks[j]**2) * Zi * Dj * Dl
             + a**3 * eps**3 / 4 * (ks[i]**2 * Dm[j, l] / (ks[j]**2 * ks[l]**2)) * Zi * Dj * Dl)
    return K


# ---------------------------------------------------------------- gate (i-b): power-law inflation, exact background
def powerlaw_gate(K3f, eps=0.1, ratio=0.02, delta=0.1, npts=60001, k_eta_star=1e-3):
    """Constant-eps power-law inflation a = (-eta)^q, q = p/(1-p), p = 1/eps: exact background, exact Hankel
    modes, raw-ADM in-in from eta = -inf (contour eta = eta* + s(1 - i delta)) to eta* with k_S eta* -> 0.
    Maldacena consistency relation (exact for any single-field attractor, leading order in k_L/k_S):
    f_NL^sq = (5/12)(1 - n_s) with n_s - 1 = -2 eps/(1 - eps)  =>  (5/6) eps/(1 - eps)."""
    p = 1.0 / eps; q = p / (1.0 - p); nu = (3 * p - 1) / (2 * (p - 1))
    kS = 1.0; kL = ratio * kS; kv = triangle(kL, kS); ks = [np.hypot(*v) for v in kv]
    eta_star = -k_eta_star / kS
    Ktot = kL + 2 * kS
    L = 70.0 / (Ktot * delta)
    s = -np.concatenate([[0.0], np.geomspace(1e-5, L, npts - 1)])[::-1]
    eta_c = eta_star + s * (1 - 1j * delta)
    me = -eta_c
    a, H = me**q, (p / (p - 1.0)) * me ** (-q - 1)
    Hd = -eps * H**2
    z, dz = np.sqrt(2 * eps) * a, np.sqrt(2 * eps) * (-q) * me ** (q - 1)     # dz/deta

    def vbar(k, eta):                                    # analytic continuation of v*  (H^(2) branch)
        x = -k * eta
        h2, h2m = hankel2(nu, x), hankel2(nu - 1, x)
        v = (np.sqrt(np.pi) / 2) * np.sqrt(x / k) * h2
        dv = -(np.sqrt(np.pi) / 2) * np.sqrt(k) * (h2 / (2 * np.sqrt(x)) + np.sqrt(x) * (h2m - nu / x * h2))
        return v, dv

    def v_real(k, eta):
        x = -k * eta
        return (np.sqrt(np.pi) / 2) * np.sqrt(x / k) * hankel1(nu, x)

    ZD = []
    for k in ks:
        v, dv = vbar(k, eta_c)
        zeta = v / z
        zetad = (dv * z - v * dz) / z**2 / a
        ZD.append((zeta, zetad))
    legs = onshell_legs(ZD, kv, a, H, Hd, eps)
    K = kernel_values(K3f, kv, a, H, Hd, legs)
    a_star = (-eta_star) ** q
    u_star = [v_real(k, eta_star) / (np.sqrt(2 * eps) * a_star) for k in ks]
    fnl, integ, Pw = fnl_from(K, s, a * (1 - 1j * delta), u_star)
    fnl_m, _, _ = fnl_from(mald_kernel_values(kv, ZD, a, eps), s, a * (1 - 1j * delta), u_star)
    # Wronskian on the real axis (mode normalisation): v v'* - v* v' = i
    e0 = -3.0 / kS; vb, dvb = vbar(kS, e0); W = float(np.imag(np.conj(vb) * dvb - vb * np.conj(dvb)))
    expected = 5.0 / 6.0 * eps / (1.0 - eps)
    return dict(eps=eps, ratio=ratio, delta=delta, npts=npts, k_eta_star=k_eta_star, f_NL_raw=fnl,
                f_NL_maldacena_form=fnl_m, raw_over_mald_minus_1=fnl / fnl_m - 1.0,
                expected_consistency=expected, mald_over_consistency_minus_1=fnl_m / expected - 1.0,
                wronskian_im=W, n_s_minus_1=-2 * eps / (1 - eps))


def run_gate_ib(K3f):
    """Gate (i-b): raw = Maldacena form (+ boundary terms that vanish as (k eta*)^2) on an exact background."""
    log("\n[gate i-b] power-law inflation (exact eps = const background), raw ADM vs Maldacena form vs consistency relation")
    rows = []
    for eps, ratio in ((0.1, 0.02), (0.2, 0.02), (0.1, 0.1)):
        pts = []
        for kes in (0.05, 0.03, 0.02):
            r = powerlaw_gate(K3f, eps=eps, ratio=ratio, delta=0.15, k_eta_star=kes)
            pts.append(r)
            log(f"   eps={eps} k_L/k_S={ratio} k eta*={kes}: raw {r['f_NL_raw']:.7f}  Mald {r['f_NL_maldacena_form']:.7f}  "
                f"raw/Mald-1 {r['raw_over_mald_minus_1']:+.3e}  Mald/consistency-1 {r['mald_over_consistency_minus_1']:+.3e}")
        x = np.array([q['k_eta_star'] ** 2 for q in pts]); y = np.array([q['raw_over_mald_minus_1'] for q in pts])
        c, b = np.polyfit(x, y, 1)
        rd = powerlaw_gate(K3f, eps=eps, ratio=ratio, delta=0.3, k_eta_star=0.03)
        log(f"   => raw/Mald-1 = {b:+.2e} + ({c:+.2f}) (k eta*)^2 ; contour-independence at k eta*=0.03: "
            f"delta 0.15 vs 0.30 differ by {abs(pts[1]['f_NL_raw'] - rd['f_NL_raw']) / abs(rd['f_NL_raw']):.1e}")
        rows.append(dict(eps=eps, ratio=ratio, points=pts, extrapolated_raw_over_mald_minus_1=float(b),
                         keta2_slope=float(c), contour_check_rel=float(abs(pts[1]['f_NL_raw'] - rd['f_NL_raw']) / abs(rd['f_NL_raw']))))
    worst = max(abs(r['extrapolated_raw_over_mald_minus_1']) for r in rows)
    log(f"   gate (i-b) {'PASS' if worst < 2e-3 else 'FAIL'}: worst extrapolated |raw/Mald - 1| = {worst:.2e} (bar 2e-3)")
    return dict(rows=rows, worst_extrapolated=float(worst), passed=bool(worst < 2e-3))

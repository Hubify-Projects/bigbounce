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

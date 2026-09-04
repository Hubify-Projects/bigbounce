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

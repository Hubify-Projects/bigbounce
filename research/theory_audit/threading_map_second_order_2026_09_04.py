#!/usr/bin/env python3
"""Second-order threading map: Maldacena comoving zeta -> zero-shift (fluid-congruence) e-fold variable delta N_c.

Ledger row 11(c), 2026-09-04.  Exact sympy, cosmic time t = -tau (tau > 0, contraction), constant epsilon,
a = tau^p with p = 1/epsilon, Mp = 1.  Comoving gauge (delta phi = 0): h_ij = a^2 e^{2 zeta} delta_ij,
N = 1 + alpha, N_i = d_i psi + Ntilde_i.  Long (k_L, along x) and short (k_S in the xy-plane) plane waves.

Exact identity used (derived in the .md, eq. (1)):  along a fluid worldline (normal to the delta phi = 0 slices,
dx^i/dt = -N^i),  N K = d/dt ln sqrt(h) - d_i N^i,  so the e-folds of the fluid congruence from the asymptotically
flat comoving slice at t -> -infinity to the final comoving slice are
        delta N_c(x_f) = zeta(t_f, x_f) - (1/3) int^{t_f} d_i N^i (t, x(t)) dt .
Everything is solved to second order in the L x S cross term including the second-order lapse/shift from the exact
ADM constraints.  No number from the adjudication is used before the comparison section.
"""
import sympy as sp, json, time, sys
T0 = time.time()
tau = sp.symbols('tau', positive=True)
eps = sp.symbols('epsilon', positive=True)
x, y, zc = sp.symbols('x y z', real=True)
kL, kS = sp.symbols('k_L k_S', positive=True)
mu = sp.symbols('mu', real=True)
zL, zS = sp.symbols('z_L z_S')
X = [x, y, zc]
p = 1 / eps
a = tau**p
def ddt(f):            # cosmic time t = -tau
    return -sp.diff(f, tau)
H = sp.simplify(ddt(a) / a)                     # = -p/tau  (H < 0: contraction)
phidot2 = 2 * eps * H**2
V = (3 - eps) * H**2
assert sp.simplify(3 * H**2 - phidot2 / 2 - V) == 0
assert sp.simplify(-ddt(H) / H**2 - eps) == 0
# growing mode of (a^3 eps zetadot)^. = 0 :  zeta = tau^(1-3p)
Zt = tau**(1 - 3 * p)
assert sp.simplify(ddt(a**3 * eps * ddt(Zt))) == 0
s = sp.sqrt(1 - mu**2)
eL = sp.exp(sp.I * kL * x)
eS = sp.exp(sp.I * kS * (mu * x + s * y))
zetaL, zetaS = zL * Zt * eL, zS * Zt * eS
zeta1 = zetaL + zetaS
def grad(f): return [sp.diff(f, xi) for xi in X]
def lap(f): return sum(sp.diff(f, xi, 2) for xi in X)
# first-order Maldacena solution (verified below by the constraints themselves)
alpha1 = ddt(zeta1) / H
chiL = -a**2 * eps * ddt(zetaL) / kL**2         # d^2 chi = a^2 eps zetadot, d^-2 -> -1/k^2
chiS = -a**2 * eps * ddt(zetaS) / kS**2
psi1 = -zeta1 / H + chiL + chiS
# second-order unknowns at wavevector K = k_L + k_S (functions of tau)
A2, P2, T2 = [sp.Function(n)(tau) for n in ('A2', 'P2', 'T2')]
Kvec = [kL + kS * mu, kS * s, 0]
eperp = [-kS * s, kL + kS * mu, 0]              # in-plane transverse direction
alpha2 = A2 * zL * zS * eL * eS
psi2 = P2 * zL * zS * eL * eS
Nt = [T2 * zL * zS * eL * eS * c for c in eperp]
assert sp.simplify(sum(sp.diff(Nt[i], X[i]) for i in range(3))) == 0
def trunc(expr, deg=2):
    """keep monomials of total degree <= deg in (zL, zS)"""
    e = sp.expand(expr)
    out = 0
    for term in sp.Add.make_args(e):
        d = sp.degree(term, zL) + sp.degree(term, zS)
        if d <= deg:
            out += term
    return out
def cross(expr):
    """coefficient of zL*zS (then evaluated at the origin, where e_L e_S = 1)"""
    e = sp.expand(expr)
    return sp.simplify(e.coeff(zL, 1).coeff(zS, 1).subs({x: 0, y: 0}))
def lin(expr, zv):
    e = sp.expand(expr)
    return sp.simplify(e.coeff(zv, 1).coeff(zL if zv is zS else zS, 0).subs({x: 0, y: 0}))
zeta = zeta1
alpha = alpha1 + alpha2
psi = psi1 + psi2
Nlow = [sp.diff(psi, X[i]) + Nt[i] for i in range(3)]      # N_i (lower index)
e2z = trunc(1 + 2 * zeta + 2 * zeta**2)                       # e^{2 zeta}
em2z = trunc(1 - 2 * zeta + 2 * zeta**2)                      # e^{-2 zeta}
Ninv = trunc(1 - alpha + alpha**2)
Ninv2 = trunc(1 - 2 * alpha + 3 * alpha**2)
print("setup done", round(time.time() - T0, 1), "s", flush=True)
# ---------------------------------------------------------------- exact ADM constraints, truncated at 2nd order
dz = grad(zeta)
Nk_dz = sum(Nlow[k] * dz[k] for k in range(3))
def DN(i, j):   # D_i N_j for h_ij = a^2 e^{2 zeta} delta_ij
    return sp.diff(Nlow[j], X[i]) - Nlow[i] * dz[j] - Nlow[j] * dz[i] + (Nk_dz if i == j else 0)
hdot_diag = trunc(2 * a**2 * (H + ddt(zeta)) * e2z)
E = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        E[i, j] = trunc(sp.Rational(1, 2) * ((hdot_diag if i == j else 0) - DN(i, j) - DN(j, i)))
hinv = em2z / a**2
Emix = sp.zeros(3, 3)          # E^i_j
for i in range(3):
    for j in range(3):
        Emix[i, j] = trunc(hinv * E[i, j])
Etr = trunc(sum(Emix[i, i] for i in range(3)))
EE = trunc(sum(Emix[i, j] * Emix[j, i] for i in range(3) for j in range(3)))   # E_ij E^ij
R3 = trunc(-2 * hinv * (2 * lap(zeta) + sum(d**2 for d in dz)))
Ham = trunc(R3 - 2 * V - Ninv2 * (EE - Etr**2 + phidot2))
Tm = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        Tm[i, j] = trunc(Ninv * (Emix[i, j] - (Etr if i == j else 0)))
def Mom(j):
    expr = sum(sp.diff(Tm[i, j], X[i]) for i in range(3))
    expr += sum(3 * dz[k] * Tm[k, j] for k in range(3))
    expr -= dz[j] * sum(Tm[i, i] for i in range(3)) + sum(dz[i] * Tm[i, j] for i in range(3)) \
            - sum(dz[k] * Tm[j, k] for k in range(3))
    return trunc(expr)
Momx, Momy = Mom(0), Mom(1)
print("constraints built", round(time.time() - T0, 1), "s", flush=True)
# background and first-order checks (exact, all k)
bg = [sp.simplify(sp.expand(c).coeff(zL, 0).coeff(zS, 0)) for c in (Ham, Momx, Momy)]
assert bg == [0, 0, 0], bg
for zv in (zL, zS):
    for c in (Ham, Momx, Momy):
        assert lin(c, zv) == 0, (zv, lin(c, zv))
print("background + first-order constraints satisfied exactly by alpha1 = zetadot/H, psi1 = -zeta/H + chi",
      round(time.time() - T0, 1), "s", flush=True)
# second order: solve the L x S cross terms for A2, P2, T2 (algebraic in tau)
eqs = [cross(Ham), cross(Momx), cross(Momy)]
sol2 = sp.solve(eqs, [A2, P2, T2], dict=True)
assert len(sol2) == 1
sol2 = {k: sp.simplify(v) for k, v in sol2[0].items()}
print("second-order lapse/shift solved", round(time.time() - T0, 1), "s", flush=True)
OUT = {'second_order_constraint_solution': {str(k): str(v) for k, v in sol2.items()}}

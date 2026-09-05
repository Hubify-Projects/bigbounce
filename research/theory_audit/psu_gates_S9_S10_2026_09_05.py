#!/usr/bin/env python3
"""paper-su gates S9 + S10 at second order (ledger row 17, 2026-09-05).

Same machinery as threading_map_second_order_2026_09_04.py (exact identity along the fluid worldline,
  delta N_c(t, x) = zeta(t, x) - (1/3) int_{-inf}^{t} d_i N^i(t', x(t')) dt',   dx^i/dt = -N^i,
ADM constraints solved to second order in the L x S cross term), generalised to independent long/short
histories zeta_L ~ tau^-mL, zeta_S ~ tau^-mS so that a constant long mode (mL = 0) can be run (S10, K_c).
S9: continue the fluid-congruence e-fold field N_c(t, x) from the uniform-phi slice t = t_f to the uniform-rho
surface t = t_f + dt(x), with rho = phidot^2/(2 N^2) + V exact in comoving gauge, dt solved to second order.
Cosmic time t = -tau (tau > 0, contraction), constant eps, a = tau^(1/eps), Mp = 1.  No number from the delta N
note is used before the comparison section.
"""
import sympy as sp, json, time, os, pickle, sys
T0 = time.time()
R = sp.Rational
tau = sp.symbols('tau', positive=True)
eps = sp.symbols('epsilon', positive=True)
x, y, zc = sp.symbols('x y z', real=True)
kL, kS = sp.symbols('k_L k_S', positive=True)
mu = sp.symbols('mu', real=True)
zL, zS = sp.symbols('z_L z_S')
mL, mS = sp.symbols('m_L m_S', nonnegative=True)
X = [x, y, zc]
p = 1 / eps
a = tau**p
def ddt(f): return -sp.diff(f, tau)
H = sp.simplify(ddt(a) / a)
phidot2 = 2 * eps * H**2
V = (3 - eps) * H**2
assert sp.simplify(3 * H**2 - phidot2 / 2 - V) == 0 and sp.simplify(-ddt(H) / H**2 - eps) == 0
m_grow = 3 * p - 1
ZL, ZS = tau**(-mL), tau**(-mS)
assert sp.simplify(ddt(a**3 * eps * ddt(ZS)).subs(mS, m_grow)) == 0
s = sp.sqrt(1 - mu**2)
eL = sp.exp(sp.I * kL * x)
eS = sp.exp(sp.I * kS * (mu * x + s * y))
zetaL, zetaS = zL * ZL * eL, zS * ZS * eS
zeta1 = zetaL + zetaS
def grad(f): return [sp.diff(f, xi) for xi in X]
def lap(f): return sum(sp.diff(f, xi, 2) for xi in X)
alpha1 = ddt(zeta1) / H
chiL = -a**2 * eps * ddt(zetaL) / kL**2
chiS = -a**2 * eps * ddt(zetaS) / kS**2
psi1 = -zeta1 / H + chiL + chiS
A2, P2, T2 = [sp.Function(n)(tau) for n in ('A2', 'P2', 'T2')]
eperp = [-kS * s, kL + kS * mu, 0]
alpha2 = A2 * zL * zS * eL * eS
psi2 = P2 * zL * zS * eL * eS
Nt = [T2 * zL * zS * eL * eS * c for c in eperp]
def trunc(expr, deg=2):
    e = sp.expand(expr); out = 0
    for term in sp.Add.make_args(e):
        if sp.degree(term, zL) + sp.degree(term, zS) <= deg: out += term
    return out
def cross(expr):
    return sp.simplify(sp.expand(expr).coeff(zL, 1).coeff(zS, 1).subs({x: 0, y: 0}))
def lin(expr, zv):
    return sp.simplify(sp.expand(expr).coeff(zv, 1).coeff(zL if zv is zS else zS, 0).subs({x: 0, y: 0}))
zeta = zeta1; alpha = alpha1 + alpha2; psi = psi1 + psi2
Nlow = [sp.diff(psi, X[i]) + Nt[i] for i in range(3)]
e2z = trunc(1 + 2 * zeta + 2 * zeta**2); em2z = trunc(1 - 2 * zeta + 2 * zeta**2)
Ninv = trunc(1 - alpha + alpha**2); Ninv2 = trunc(1 - 2 * alpha + 3 * alpha**2)
dz = grad(zeta)
Nk_dz = sum(Nlow[k] * dz[k] for k in range(3))
def DN(i, j): return sp.diff(Nlow[j], X[i]) - Nlow[i] * dz[j] - Nlow[j] * dz[i] + (Nk_dz if i == j else 0)
hdot_diag = trunc(2 * a**2 * (H + ddt(zeta)) * e2z)
E = sp.zeros(3, 3); Emix = sp.zeros(3, 3); Tm = sp.zeros(3, 3)
hinv = em2z / a**2
for i in range(3):
    for j in range(3):
        E[i, j] = trunc(R(1, 2) * ((hdot_diag if i == j else 0) - DN(i, j) - DN(j, i)))
        Emix[i, j] = trunc(hinv * E[i, j])
Etr = trunc(sum(Emix[i, i] for i in range(3)))
EE = trunc(sum(Emix[i, j] * Emix[j, i] for i in range(3) for j in range(3)))
R3 = trunc(-2 * hinv * (2 * lap(zeta) + sum(d**2 for d in dz)))
Ham = trunc(R3 - 2 * V - Ninv2 * (EE - Etr**2 + phidot2))
for i in range(3):
    for j in range(3):
        Tm[i, j] = trunc(Ninv * (Emix[i, j] - (Etr if i == j else 0)))
def Mom(j):
    expr = sum(sp.diff(Tm[i, j], X[i]) for i in range(3)) + sum(3 * dz[k] * Tm[k, j] for k in range(3))
    expr -= dz[j] * sum(Tm[i, i] for i in range(3)) + sum(dz[i] * Tm[i, j] for i in range(3)) - sum(dz[k] * Tm[j, k] for k in range(3))
    return trunc(expr)
Momx, Momy = Mom(0), Mom(1)
print("constraints built (general mL, mS)", round(time.time() - T0, 1), "s", flush=True)

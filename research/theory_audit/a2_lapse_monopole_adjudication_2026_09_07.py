#!/usr/bin/env python3
"""Independent adjudication of the L x S second-order lapse monopole A2(eps) in comoving gauge
(delta phi = 0, h_ij = a^2 e^{2 zeta} delta_ij, N_i = d_i psi), constant-eps contraction, growing mode.
Part A: exact ADM Hamiltonian + momentum constraints to second order, two plane waves, squeezed
        gradient-free limit -> A2(mu, kS/kL, eps), monopole.
Part B: exact local (monopole) system  K^2/9 = rho/3  +  energy conservation  -> u_LS = c(eps) u_L u_S,
        f^SU on both slices, and the consistency relation with the in-in monopole.
Part C: the composition step: lambda' is a time-derivative operator, not a multiplicative map.
Run: python3 a2_lapse_monopole_adjudication_2026_09_07.py  (writes the .json alongside)."""
import json, sys, time
import sympy as sp

t0 = time.time()
T, eps, x, y, z, kL, kS, mu, l, s, dl = sp.symbols('T epsilon x y z k_L k_S mu l s delta', positive=True)
def ddt(f):            # t = -T (contraction, t<0), d/dt = -d/dT
    return -sp.diff(f, T)
a = T**(1/eps); H = sp.simplify(ddt(a)/a)          # H = -1/(eps T) < 0
assert sp.simplify(H + 1/(eps*T)) == 0
phidot2 = 2*eps*H**2; V = 3*H**2 - phidot2/2
# growing mode zeta ~ a^{-(3-eps)}, unknown second-order amplitudes are functions of T
ZL = T**(-(3-eps)/eps); ZS = T**(-(3-eps)/eps)
AL, AS, PL, PS = sp.symbols('A_L A_S P_L P_S')      # linear lapse/shift amplitudes (solved below)
Z2 = sp.Function('Z2')(T); A2 = sp.Function('A2')(T); P2 = sp.Function('P2')(T)
nu = sp.sqrt(1-mu**2)
EL = sp.exp(sp.I*kL*z); ES = sp.exp(sp.I*kS*(mu*z+nu*x))
zeta = l*ZL*EL + s*ZS*ES + l*s*Z2*EL*ES
alpha = l*AL*EL + s*AS*ES + l*s*A2*EL*ES           # N = 1 + alpha
psi = l*PL*EL + s*PS*ES + l*s*P2*EL*ES
X = [x, y, z]
d = lambda f, i: sp.diff(f, X[i])
# second-order-exact truncations (l*s extraction kills higher orders)
e2z = 1 + 2*zeta + 2*zeta**2; em2z = 1 - 2*zeta + 2*zeta**2; em4z = 1 - 4*zeta + 8*zeta**2
Ninv = 1 - alpha + alpha**2; Ninv2 = 1 - 2*alpha + 3*alpha**2
dz = [d(zeta, i) for i in range(3)]; dpsi = [d(psi, i) for i in range(3)]
gradzpsi = sum(dz[i]*dpsi[i] for i in range(3))
E = [[a**2*e2z*(H+ddt(zeta))*(1 if i == j else 0)
      - (sp.diff(psi, X[i], X[j]) - dz[i]*dpsi[j] - dz[j]*dpsi[i] + (gradzpsi if i == j else 0))
      for j in range(3)] for i in range(3)]
Emix = [[a**-2*em2z*E[i][j] for j in range(3)] for i in range(3)]   # E^i_j
Etr = sum(Emix[i][i] for i in range(3))
EE = a**-4*em4z*sum(E[i][j]*E[i][j] for i in range(3) for j in range(3))
R3 = -a**-2*em2z*(4*sum(d(dz[i], i) for i in range(3)) + 2*sum(dz[i]**2 for i in range(3)))
rho = phidot2/2*Ninv2 + V
HAM = R3 + Ninv2*(Etr**2 - EE) - 2*rho
Tm = [[Ninv*(Emix[i][j] - (Etr if i == j else 0)) for j in range(3)] for i in range(3)]  # T^i_j
MOM = [sum(d(Tm[j][i], j) for j in range(3)) + 3*sum(dz[k]*Tm[k][i] for k in range(3))
       - dz[i]*sum(Tm[k][k] for k in range(3)) for i in range(3)]
def coeff(expr, *vars_):
    e = expr
    for v in vars_: e = sp.diff(e, v)
    return sp.simplify(e.subs({l: 0, s: 0, x: 0, y: 0, z: 0}))
# ---- background and linear order (checks the machinery) ----
assert sp.simplify(HAM.subs({l: 0, s: 0})) == 0
mom1 = coeff(MOM[2], l); ham1 = coeff(HAM, l)
AL_sol = sp.solve(mom1, AL)[0]; assert sp.simplify(AL_sol - ddt(ZL)/H) == 0     # N1 = zeta_dot/H
PL_sol = sp.solve(ham1.subs(AL, AL_sol), PL)[0]
assert sp.simplify(PL_sol - (-ZL/H - a**2*eps*ddt(ZL)/kL**2)) == 0              # psi = -zeta/H + chi, d^2 chi = a^2 eps zeta_dot
AS_sol = AL_sol.subs(ZL, ZS); PS_sol = PL_sol.subs({kL: kS}).subs(ZL, ZS)
lin = {AL: AL_sol, AS: AS_sol, PL: PL_sol, PS: PS_sol}
print('linear order reproduced (N1 = zeta_dot/H, d^2 chi = a^2 eps zeta_dot)', round(time.time()-t0, 1), 's')
# ---- second order, L x S ----
ham2 = coeff(HAM, l, s).subs(lin)
kvec = [kS*nu, 0, kL + kS*mu]                                   # k_L + k_S
mom2_long = sp.simplify(sum(kvec[i]*coeff(MOM[i], l, s) for i in range(3)).subs(lin))   # longitudinal projection
# squeezed, gradient-free limit: k -> delta*k, leading order in delta; P2 ~ 1/delta^2
p2 = sp.Symbol('p2')
scale = {kL: dl*kL, kS: dl*kS}
ham2s = sp.series(sp.expand(ham2.subs(scale).subs(P2, p2/dl**2)), dl, 0, 1).removeO()
mom2s = sp.series(sp.expand(mom2_long.subs(scale)), dl, 0, 3).removeO()   # projection adds one power of k
assert sp.simplify(ham2s.coeff(dl, -1)) == 0 and sp.simplify(mom2s.coeff(dl, 0)) == 0 and sp.simplify(mom2s.coeff(dl, 1)) == 0
ham0 = sp.simplify(ham2s.coeff(dl, 0)); mom1s = sp.simplify(mom2s.coeff(dl, 2))
A2_sol = sp.solve(mom1s, A2)[0]
A2_quad = sp.simplify((A2_sol - ddt(Z2)/H)/(ZL*ZS))              # coefficient of zeta_L zeta_S beyond zeta_dot/H
A2_quad = sp.simplify(sp.expand(A2_quad))
print('A2(mu, kS/kL, eps) =', A2_quad)
r = sp.Symbol('r', positive=True)                                 # r = k_L/k_S -> 0 (squeezed), pole kept
A2_sq = sp.series(A2_quad.subs(kL, r*kS), r, 0, 1).removeO()
pole = sp.factor(A2_sq.coeff(r, -1)); A2_0 = sp.factor(sp.expand(A2_sq.coeff(r, 0)))
print('1/k_L pole  :', pole, '* k_S/k_L   (odd in mu, zero monopole:', sp.integrate(pole, (mu, -1, 1)) == 0, ')')
print('A2 O(k^0)(mu):', A2_0)
A2_mono = sp.factor(sp.integrate(A2_0, (mu, -1, 1))/2)
A2_S9 = eps*(3-eps)**2/3; A2_S9c = 2*(3-eps)**2
print('A2 monopole =', A2_mono, '| S9:', A2_S9, '| S9c-required:', A2_S9c)
verdict_A2 = ('S9' if sp.simplify(A2_mono - A2_S9) == 0 else 'S9c' if sp.simplify(A2_mono - A2_S9c) == 0 else 'neither')
print('A2 monopole matches:', verdict_A2, '| at dust:', A2_mono.subs(eps, sp.Rational(3, 2)), '| eps->0:', sp.limit(A2_mono, eps, 0))
assert verdict_A2 == 'S9'
# the second-order shift divergence (Hamiltonian constraint), for the record
p2_sol = sp.solve(ham0.subs(A2, A2_sol), p2)[0]
DN2 = sp.simplify(-(kL+kS*mu)**2*p2_sol/a**2 - kS**2*nu**2*p2_sol/a**2)   # d^2 psi_2 / a^2 at leading order (|k_L+k_S|^2 = kL^2+2kLkS mu+kS^2)
print('Part A done', round(time.time()-t0, 1), 's')

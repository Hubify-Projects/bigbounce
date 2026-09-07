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
# ================= Part B: exact local (monopole) system along a worldline =================
# u = 1/N.  Hamiltonian monopole: K^2/9 = rho/3, rho = phidot^2 u^2/2 + V  ->  K = 3H sqrt(1+eps(u^2-1)/3)
# energy conservation (= KG): u phi_ddot + u_dot phi_dot + K phi_dot + V'/u = 0, phi_ddot = -eps H phi_dot, V' = (eps-3)H phi_dot
u, A = sp.symbols('u A')
g = 1 + eps*(u**2-1)/3
F = eps*H*u - 3*H*sp.sqrt(g) + (3-eps)*H/u                    # u_dot = F(u)
Theta = H*sp.sqrt(g)/u                                        # d ln a_loc/dt = N K/3 = K/(3u)
F1 = sp.simplify(sp.diff(F, u).subs(u, 1)); F2 = sp.simplify(sp.diff(F, u, 2).subs(u, 1))
assert sp.simplify(F.subs(u, 1)) == 0 and sp.simplify(F1 + (3-eps)*H) == 0   # linear growing mode v ~ a^{-(3-eps)}
c_loc = sp.factor(F2/F1)                                      # v_LS = c v_L v_S  (particular solution; homogeneous is O(1/W))
print('local system: u_LS = c u_L u_S with c(eps) =', c_loc, '| dust:', c_loc.subs(eps, sp.Rational(3, 2)))
v1 = T**(-(3-eps)/eps)                                        # normalised growing mode of v = u - 1
v = A*v1 + A**2*(c_loc/2)*v1**2                             # v_dot = F' v + (F''/2) v^2  ->  v_2 = (c/2) v_1^2, i.e. v_LS = c v_L v_S
Th1 = sp.diff(Theta, u).subs(u, 1); Th2 = sp.diff(Theta, u, 2).subs(u, 1)
# int H v1 dt = -v1/(3-eps), int H v1^2 dt = -v1^2/(2(3-eps))  (both vanish at the initial flat slice, W->0 side)
dNc = sp.expand(A*(Th1/H)*(-v1/(3-eps)) + A**2*((Th1/H)*(c_loc/2)*(-v1**2/(2*(3-eps))) + (Th2/H)/2*(-v1**2/(2*(3-eps)))))
n1 = sp.simplify(dNc.coeff(A, 1)/v1); assert sp.simplify(n1 - sp.Rational(1, 3)) == 0   # delta N_c = v/3 = (1-eps/3) zeta  (lambda)
def fnl(dN):                                                  # initial-position label by construction (worldline quantities)
    return sp.factor(sp.Rational(5, 6)*2*dN.coeff(A, 2)/dN.coeff(A, 1)**2)
f_phi_loc = fnl(dNc)                                          # comoving slice t = t_f
# uniform-density slice: rho(T_f+dT, u) = rho_bar(T_f), rho = H^2 (3 + eps(u^2-1)), H^2 = 1/(eps T)^2
dT1, dT2 = sp.symbols('dT1 dT2')
Tf = sp.Symbol('T_f', positive=True); dT = A*dT1 + A**2*dT2
rho_loc = (3 + eps*((1+v)**2 - 1))/(eps*T)**2
eq = sp.series(sp.expand(rho_loc.subs(T, Tf + dT)*(eps*Tf)**2 - 3), A, 0, 3).removeO()
dT1s = sp.solve(eq.coeff(A, 1), dT1)[0]; dT2s = sp.solve(eq.coeff(A, 2).subs(dT1, dT1s), dT2)[0]
Nbar = sp.log(T)/eps
dNrho = sp.series(sp.expand((dNc + Nbar).subs(T, Tf + dT).subs({dT1: dT1s, dT2: dT2s}) - Nbar.subs(T, Tf)), A, 0, 3).removeO()
f_rho_loc = fnl(dNrho)
lam = 1 - eps/3; lamp = sp.simplify(dNrho.coeff(A, 1)/dNc.coeff(A, 1).subs(T, Tf))
print('f_phi^loc =', f_phi_loc, '| f_rho^loc =', f_rho_loc, "| lambda'/lambda =", lamp)
assert sp.simplify(f_phi_loc + 5) == 0 and sp.simplify(f_rho_loc - 5*(eps-7)/8) == 0 and lamp == 2
# consistency with the momentum-constraint lapse: u = 1/N, N = 1 + zeta_dot/H + A2 zeta_L zeta_S  =>
# u_LS = -zeta2_dot/H + (2(3-eps)^2 - A2) zeta_L zeta_S, zeta2 = c_zeta zeta_L zeta_S ~ a^{-2(3-eps)}, v_L = (3-eps) zeta_L
c_zeta = sp.factor((c_loc*(3-eps)**2 - 2*(3-eps)**2 + A2_mono)/(2*(3-eps)))
f_inin_mono = sp.factor(sp.Rational(5, 6)*c_zeta)             # classical late-time in-in monopole implied by (A2, local system)
print('implied in-in monopole f(eps) =', f_inin_mono, '| dust:', f_inin_mono.subs(eps, sp.Rational(3, 2)), '(row-1 in-in: -35/16 + 15/16 * 1/3 = -15/8)')
assert f_inin_mono.subs(eps, sp.Rational(3, 2)) == -sp.Rational(15, 8)
# ================= Part C: the composition step =================
lamp_val = 2*lam                                              # growing mode: lambda' = lambda + H dt^(1)/zeta = 2 lambda
w2 = lam + 2*lam                                              # on zeta_2 ~ a^{-2(3-eps)}: H dt^(1) = -zeta2_dot/(3H) = 2 lambda zeta2  -> weight 3 lambda
f_map_mono = sp.simplify(f_rho_loc - (w2/lamp_val)*f_inin_mono/lamp_val)      # what the quadratic map must contribute
f_S9_chain = sp.simplify(f_inin_mono/lamp_val + f_map_mono)   # S9's composition f^{in-in}/lambda' + f_map with the same map
print('f_map monopole (rho-normalised) =', f_map_mono, "| S9-style composition f^{in-in}/lambda' + f_map =", sp.factor(f_S9_chain),
      '| S9 quoted 5(2eps-15)/24 ->', sp.simplify(f_S9_chain - 5*(2*eps-15)/24) == 0)
gap = sp.factor(f_rho_loc - f_S9_chain); print('gap = (1/2) f^{in-in}/lambda\' =', gap, '| S9c gap 5(eps-6)/24 ->', sp.simplify(gap - 5*(eps-6)/24) == 0)
assert sp.simplify(f_S9_chain - 5*(2*eps-15)/24) == 0 and sp.simplify(gap - 5*(eps-6)/24) == 0 and sp.simplify(f_map_mono + sp.Rational(5, 8)) == 0
# independent f_map from the ADM objects (no S9 table): f_extra chain (S9c section 3) with my A2 + comoving shift-divergence kernel
# D_i N^i = a^-2 e^-2zeta (d^2 psi + dzeta.dpsi): L x S, O(k^0) = a^-2 d^2 psi_2 - 2 zeta_L (eps zeta_S_dot) - 2 zeta_S (eps zeta_L_dot) (+ odd-mu pole)
DN2_full = DN2.subs(A2, A2_sol) - 2*eps*(ZL*ddt(ZS) + ZS*ddt(ZL)) - eps*ddt(Z2)   # minus the linear operator eps*zeta2_dot (already in lambda*zeta_2)
DN2_sq = sp.series(sp.simplify(DN2_full.subs(kL, r*kS)), r, 0, 1).removeO()
DN2_pole = sp.integrate(DN2_sq.coeff(r, -1), (mu, -1, 1)); assert DN2_pole == 0
DN2_mono = sp.simplify(sp.integrate(DN2_sq.coeff(r, 0), (mu, -1, 1))/2)                     # d_i N^i at L x S, O(k^0), monopole
kern = sp.simplify(DN2_mono/(ZL*ZS*H))                                                       # DN2 = kern * H zeta_L zeta_S,  ~ a^{-2(3-eps)}
M_phi = sp.simplify(-sp.Rational(1, 3)*kern*(-1/(2*(3-eps))))                                 # -(1/3) int DN2 dt  (int H W^2 dt = -W^2/(2(3-eps)))
M_extra = -A2_mono/3 + (3-eps)**2*(2*eps-3)/9
f_map_adm = sp.factor(sp.Rational(5, 6)*(M_phi + M_extra)/lamp_val**2)
print('shift-divergence kernel d_iN^i|_LS = H zeta_L zeta_S *', sp.factor(kern), '| f_map (ADM, rho-normalised) =', f_map_adm)
print('   f_map from local system =', f_map_mono, '| difference =', sp.simplify(f_map_adm - f_map_mono))
assert sp.simplify(f_map_adm - f_map_mono) == 0
# the named step: lambda' is a derivative operator. On zeta_2 ~ a^{-2(3-eps)}: delta N_c = lambda zeta_2, H dt = -zeta2_dot/(3H) = 2 lambda zeta_2
Z2g = T**(-2*(3-eps)/eps); w_on_zeta2 = sp.simplify((lam*Z2g - ddt(Z2g)/(3*H))/Z2g); assert sp.simplify(w_on_zeta2 - 3*lam) == 0
w_on_zeta1 = sp.simplify((lam*ZL - ddt(ZL)/(3*H))/ZL); assert sp.simplify(w_on_zeta1 - 2*lam) == 0
out = {'A2_full_mu_k': str(A2_quad), 'A2_pole_coeff_of_kS_over_kL': str(pole), 'A2_O_k0_mu': str(A2_0),
       'A2_monopole': str(A2_mono), 'A2_monopole_dust': str(A2_mono.subs(eps, sp.Rational(3, 2))), 'A2_eps_to_0': str(sp.limit(A2_mono, eps, 0)),
       'A2_matches': verdict_A2, 'A2_S9': str(A2_S9), 'A2_S9c_required': str(A2_S9c),
       'local_c_u': str(c_loc), 'f_phi_local': str(f_phi_loc), 'f_rho_local': str(f_rho_loc), 'f_rho_local_dust': str(f_rho_loc.subs(eps, sp.Rational(3, 2))),
       'lambda_prime_over_lambda': str(lamp), 'implied_inin_monopole': str(f_inin_mono), 'implied_inin_monopole_dust': str(f_inin_mono.subs(eps, sp.Rational(3, 2))),
       'shift_div_LS_kernel_over_H': str(sp.factor(kern)), 'f_map_monopole_rho_normalised': str(f_map_adm),
       'weight_on_zeta1': str(w_on_zeta1), 'weight_on_zeta2': str(w_on_zeta2),
       'S9_composition_reproduced': str(f_S9_chain), 'gap_S9_minus_true': str(gap),
       'f_rho_true_dust': '-55/16', 'f_rho_S9_dust': '-5/2',
       'verdict': 'A2 = eps(3-eps)^2/3 (S9 constraint solve correct); f^rho = 5(eps-7)/8 = -55/16 (S9c/SU number correct, same variable delta N_c on the uniform-density surface, initial label); '
                  'the S9 map error is the composition f^{in-in}/lambda\': lambda\' = lambda + H dt^(1)/zeta is a time-derivative operator that equals 2 lambda only on the linear growing mode; '
                  'on the second-order zeta_2 ~ a^{-2(3-eps)} it equals 3 lambda, so f^rho = (3/2) f^{in-in}/lambda\' + f_map; S9c\'s A2_req = 2(3-eps)^2 inherits the same assumption and is not a lapse.',
       'runtime_s': round(time.time()-t0, 1), 'sympy': sp.__version__}
json.dump(out, open(__file__.replace('.py', '.json'), 'w'), indent=1)
print('all asserts pass; json written;', out['runtime_s'], 's')

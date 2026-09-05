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
# zeta history kept GENERAL, zeta ~ tau^(-m): the constraints hold for any history (only the dynamics fix m).
# Growing mode of (a^3 eps zetadot)^. = 0 is m = 3p - 1 = 3/eps - 1 (substituted later); m = 0 is the constant
# (attractor) mode.
m = sp.symbols('m', positive=True)
Zt = tau**(-m)
m_grow = 3 * p - 1
assert sp.simplify(ddt(a**3 * eps * ddt(Zt)).subs(m, m_grow)) == 0
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
# ---------------------------------------------------------------- the threading map  delta N_c = zeta - (1/3) int d_i N^i dt
subs2 = {A2: sol2[A2], P2: sol2[P2], T2: sol2[T2]}
Nup = [trunc(hinv * Nlow[i]) for i in range(3)]                       # N^i = h^{ij} N_j
div = trunc(sum(sp.diff(Nup[i], X[i]) for i in range(3))).subs(subs2)  # d_i N^i to second order
d = sp.symbols('delta', positive=True)                                # super-Hubble scaling k -> delta k
def superhubble(expr):
    """leading (delta^0) term as k_L, k_S -> 0 jointly; asserts no 1/delta poles"""
    e = sp.expand(expr.subs({kL: d * kL, kS: d * kS}))
    ser = sp.series(e, d, 0, 1).removeO()
    lead = sp.expand(ser)
    assert lead.coeff(d, -1) == 0 and lead.coeff(d, -2) == 0, "1/delta pole"
    return sp.simplify(lead.coeff(d, 0))
tf = sp.symbols('tau_f', positive=True)
def tail(expr):
    """int_{tau_f}^{infinity} expr d tau  (= int_{-inf}^{t_f} ... dt), term-by-term power law; records convergence"""
    out, conds = 0, []
    for term in sp.Add.make_args(sp.expand(sp.powsimp(expr, force=True))):
        c, tp = term.as_independent(tau)
        base, ex = sp.powsimp(tp, force=True).as_base_exp()
        if tp == 1:
            base, ex = tau, 0
        assert base == tau, (term, base)
        out += -c * tf**(ex + 1) / (ex + 1)
        conds.append(str(sp.simplify(ex + 1)) + ' < 0')
    return sp.simplify(out), conds
def anti(expr):
    """antiderivative F(tau) of a power-law sum"""
    out = 0
    for term in sp.Add.make_args(sp.expand(sp.powsimp(expr, force=True))):
        c, tp = term.as_independent(tau)
        base, ex = sp.powsimp(tp, force=True).as_base_exp()
        if tp == 1:
            base, ex = tau, 0
        out += c * tau**(ex + 1) / (ex + 1)
    return out
DL, DS, DLS = superhubble(lin(div, zL)), superhubble(lin(div, zS)), superhubble(cross(div))
NxL = superhubble(lin(Nup[0], zL))              # N^x of the long mode at the origin (per z_L)
print("d_i N^i: linear", DL, "| cross", sp.factor(DLS), round(time.time() - T0, 1), "s", flush=True)
# linear map:  delta N_c^(1) / zeta  = 1 - (1/3) int D_S dt / Z(t_f)
intDS, cDS = tail(DS)
lam = sp.simplify(1 - sp.Rational(1, 3) * intDS / Zt.subs(tau, tf))
print("linear threading factor  delta N_c / zeta_Mald =", sp.factor(lam), " (conv:", set(cDS), ")", flush=True)
# displacement of the fluid worldline ending at x_f = 0:  Delta^x(tau) = int_{tau_f}^{tau} N^x_L dtau'
Fx = anti(NxL)
Delta_fin = sp.simplify(Fx - Fx.subs(tau, tf))                      # final-label threading
Delta_init_const = sp.simplify(-tail(NxL)[0])                        # Delta_init(tau) = Delta_fin(tau) + const
print("k_L . Delta_fin(tau) / zeta_L(tau)  (pure-translation scale)  =",
      sp.simplify(sp.I * kL * Delta_fin / Zt), flush=True)
# ---------------------------------------------------------------- second-order cross kernel, split by origin
D_psi2 = superhubble(cross(sum(sp.diff(psi2, xi, 2) for xi in X) / a**2).subs(subs2))     # 2nd-order shift
D_grad = superhubble(cross(-2 / a**2 * sum(dz[i] * sp.diff(psi1, X[i]) for i in range(3))))  # -2 d zeta . d psi1
D_zlap = superhubble(cross(-2 / a**2 * zeta1 * lap(psi1)))                                  # -2 zeta d^2 psi1
assert sp.simplify(D_psi2 + D_grad + D_zlap - DLS) == 0
Zf2 = Zt.subs(tau, tf)**2
def kern(integrand):
    val, conds = tail(integrand)
    return sp.simplify(-sp.Rational(1, 3) * val / Zf2), conds
pieces = {}
pieces['psi2'], c1 = kern(D_psi2)
pieces['grad'], c2 = kern(D_grad)
pieces['zlap'], c3 = kern(D_zlap)
pieces['wl_fin'], c4 = kern(Delta_fin * sp.I * kS * mu * DS)            # short divergence read along the displaced worldline
pieces['wl_initextra'], c5 = kern(Delta_init_const * sp.I * kS * mu * DS)  # extra when the patch is labelled by its initial position
pieces['lab_init'] = sp.simplify(sp.I * kS * mu * Delta_init_const * Zt.subs(tau, tf) / Zf2)  # zeta_S read at the displaced final point
OUT['convergence_conditions'] = sorted(set(c1 + c2 + c3 + c4 + c5 + cDS))
print("kernel pieces built", round(time.time() - T0, 1), "s", flush=True)
# ---------------------------------------------------------------- bispectrum assembly in the squeezed limit
#  B_{delta N}(k_L, p, q) = lam^3 B_zeta + lam^2 P_L [ M(k_L, q) P(q) + M(k_L, p) P(p) ],  P(k) = k^-3,
#  p = k_S n - k_L/2, q = -k_S n - k_L/2, mu = x.n ;  f = (5/12) B / (lam^4 P_L P_S)
def f_of(M, lam_):
    kp = sp.sqrt(kS**2 - mu * kS * kL + kL**2 / 4)
    kq = sp.sqrt(kS**2 + mu * kS * kL + kL**2 / 4)
    Mp = M.subs({kS: kp, mu: (mu * kS - kL / 2) / kp}, simultaneous=True)
    Mq = M.subs({kS: kq, mu: (-mu * kS - kL / 2) / kq}, simultaneous=True)
    B = Mq / kq**3 + Mp / kp**3
    f = sp.Rational(5, 12) / lam_**2 * B * kS**3
    ser = sp.series(f.subs(kL, d * kS), d, 0, 1).removeO()
    ser = sp.expand(ser)
    assert ser.coeff(d, -1) == 0, ("1/k_L pole survives", ser.coeff(d, -1))
    f0 = sp.simplify(ser.coeff(d, 0))
    assert sp.simplify(sp.im(f0)) == 0 or sp.simplify(f0 - sp.conjugate(f0)) == 0
    f0 = sp.expand(sp.re(f0)) if f0.has(sp.I) else sp.expand(f0)
    poly = sp.Poly(f0, mu)
    assert poly.degree() <= 2 and poly.coeff_monomial(mu) == 0, f0
    return sp.simplify(poly.coeff_monomial(1)), sp.simplify(poly.coeff_monomial(mu**2))   # (constant, mu^2 coeff)
def mono(c0, c2): return sp.simplify(c0 + c2 / 3)
def report(label, M, lam_):
    c0, c2 = f_of(M, lam_)
    print(f"  {label:28s} f = {c0} + ({c2}) mu^2   monopole {mono(c0, c2)}", flush=True)
    return {'const': str(c0), 'mu2': str(c2), 'monopole': str(mono(c0, c2))}
# ---------------------------------------------------------------- contraction growing mode  m = 3/eps - 1
sub_grow = {m: m_grow}
lamg = sp.simplify(lam.subs(sub_grow))
print("\nCONTRACTION (constant eps, growing mode): linear factor delta N_c/zeta =", sp.factor(lamg), flush=True)
OUT['linear_threading_factor'] = str(sp.factor(lamg))
Pg = {k: sp.simplify(v.subs(sub_grow)) for k, v in pieces.items()}
for k, v in Pg.items():
    assert not v.has(tf), (k, v)          # end-time independence
OUT['kernels_growing_mode'] = {k: str(v) for k, v in Pg.items()}
print("  kernels M (delta N_c^(2) = M zeta_L zeta_S), general eps:")
for k, v in Pg.items():
    print(f"    {k:14s} {sp.factor(v)}")
print("\n  f_NL contributions of the map (delta N_c normalisation, P ~ k^-3):")
res = {}
for k in ('psi2', 'grad', 'zlap', 'wl_fin'):
    res[k] = report(k, Pg[k], lamg)
M_fin = sum(Pg[k] for k in ('psi2', 'grad', 'zlap', 'wl_fin'))
M_init = M_fin + Pg['wl_initextra'] + Pg['lab_init']
res['total_final_label'] = report('TOTAL (final-position label)', M_fin, lamg)
res['total_initial_label'] = report('TOTAL (initial-position label)', M_init, lamg)
res['pure_translation_init'] = report('pure translation (lab_init)', Pg['lab_init'], lamg)
res['wl_initextra'] = report('wl_initextra', Pg['wl_initextra'], lamg)
OUT['map_fNL_pieces'] = res
# ---------------------------------------------------------------- comparison with the in-in result (read only now)
f_inin = sp.Rational(5, 12) * (eps**2 * mu**2 - eps**2 + 6 * eps - 12)     # adjudication 2026-09-03 §4
c0i, c2i = sp.Rational(5, 12) * (-eps**2 + 6 * eps - 12), sp.Rational(5, 12) * eps**2
def total(label, key):
    c0 = sp.simplify(c0i / lamg + sp.sympify(res[key]['const']))
    c2 = sp.simplify(c2i / lamg + sp.sympify(res[key]['mu2']))
    print(f"  f_NL[delta N_c] via in-in/lam + map, {label}: {c0} + ({c2}) mu^2 ; monopole {mono(c0, c2)}", flush=True)
    return {'const': str(c0), 'mu2': str(c2), 'monopole': str(mono(c0, c2)),
            'const_eps_3_2': str(c0.subs(eps, sp.Rational(3, 2))), 'mu2_eps_3_2': str(c2.subs(eps, sp.Rational(3, 2)))}
print("\nPREDICTED delta N_c bispectrum = lam^3 B_inin + map:")
OUT['prediction'] = {'final_label': total('final label', 'total_final_label'),
                     'initial_label': total('initial label', 'total_initial_label')}
# the adjudication's recorded identity  [L] - delta N_c = 5 eps/4  and its 'pure translation' reading
OUT['adjudication_identity'] = {'5eps/4': str(5 * eps / 4), 'L_minus_dNc': str(sp.Rational(5, 4) * (eps - 4) + 5),
                                'pure_translation_monopole_this_work': res['pure_translation_init']['monopole']}
# ---------------------------------------------------------------- limits
DLS0, DS0 = sp.simplify(DLS.subs(m, 0)), sp.simplify(DS.subs(m, 0))
print("\nATTRACTOR (constant zeta, m = 0): d_i N^i linear =", DS0, ", cross =", DLS0, "-> map is the identity at O(k^0)")
OUT['attractor_limit'] = {'div_linear': str(DS0), 'div_cross': str(DLS0),
                          'statement': 'delta N_c = zeta_Mald + O(k^2/a^2H^2); Maldacena consistency relation unchanged'}
r = sp.symbols('r', real=True)                                     # r = zetadot/(H zeta) = -m eps, held fixed
usr = {k: sp.simplify(sp.series(v.subs(m, -r / eps), eps, 0, 2).removeO()) for k, v in
       {'DS': DS, 'DLS': DLS, 'NxL*kS': NxL * kS}.items()}
print("USR-type limit (eps -> 0 at fixed zetadot/H zeta = r):", {k: str(v) for k, v in usr.items()})
OUT['usr_limit'] = {k: str(v) for k, v in usr.items()}
OUT['wall_clock_s'] = round(time.time() - T0, 1)
json.dump(OUT, open(__file__.replace('.py', '.json'), 'w'), indent=2)
print("done", OUT['wall_clock_s'], "s")

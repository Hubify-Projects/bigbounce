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
# ---------------------------------------------------------------- background + first-order checks (exact, all k)
bg = [sp.simplify(sp.expand(c).coeff(zL, 0).coeff(zS, 0)) for c in (Ham, Momx, Momy)]
assert bg == [0, 0, 0], bg
for zv in (zL, zS):
    for c in (Ham, Momx, Momy):
        assert lin(c, zv) == 0, (zv, lin(c, zv))
print("background + first-order constraints hold for arbitrary (mL, mS)", round(time.time() - T0, 1), "s", flush=True)
cHam, cMx, cMy = cross(Ham), cross(Momx), cross(Momy)
m = sp.symbols('m', positive=True)
LOC = {'tau': tau, 'epsilon': eps, 'k_L': kL, 'k_S': kS, 'mu': mu, 'm': m}
_cache = os.environ.get('PSU_S9S10_CACHE')
def solve_cross(hist, key):
    """second-order lapse/shift A2, P2, T2 for the history substitution hist = {mL: ., mS: .}"""
    if _cache and os.path.exists(_cache + key):
        d = pickle.load(open(_cache + key, 'rb'))
        return {sp.Function(k)(tau): sp.sympify(v, locals=LOC) for k, v in d.items()}
    eqs = [sp.simplify(c.subs(hist)) for c in (cHam, cMx, cMy)]
    sol = sp.solve(eqs, [A2, P2, T2], dict=True)
    assert len(sol) == 1
    sol = {k: sp.simplify(v) for k, v in sol[0].items()}
    if _cache: pickle.dump({str(k.func): str(v) for k, v in sol.items()}, open(_cache + key, 'wb'))
    return sol
d = sp.symbols('delta', positive=True)
def superhubble(expr, order=0):
    e = sp.expand(expr.subs({kL: d * kL, kS: d * kS}))
    lead = sp.expand(sp.series(e, d, 0, order + 1).removeO())
    for n in range(order - 2, order):
        assert lead.coeff(d, n) == 0, ("unexpected pole", n, lead.coeff(d, n))
    return sp.simplify(lead.coeff(d, order))
tf = sp.symbols('tau_f', positive=True)
def powterms(expr):
    out = []
    for term in sp.Add.make_args(sp.expand(expr)):
        if term == 0: continue
        ex = sp.simplify(tau * sp.diff(term, tau) / term)
        assert not ex.has(tau), (term, ex)
        out.append((sp.simplify(term / tau**ex), ex))
    return out
def tail(expr):          # int_{tau_f}^{inf} expr dtau = int_{-inf}^{t_f} ... dt
    out, conds = 0, []
    for c, ex in powterms(expr):
        out += -c * tf**(ex + 1) / (ex + 1); conds.append(str(sp.simplify(ex + 1)) + ' < 0')
    return sp.simplify(out), conds
def anti(expr): return sum(c * tau**(ex + 1) / (ex + 1) for c, ex in powterms(expr))
def f_of(M, lamL, lamS):
    """squeezed f_NL of the map kernel M(kL, kS, mu): B = lamL lamS P_L [M(kL,q)P(q) + M(kL,p)P(p)], P = k^-3,
    f = (5/12) B / (lamL^2 lamS^2 P_L P_S) -> (5/12) [..]/(lamL lamS P_S).  Returns (const, mu^2 coefficient)."""
    kp = sp.sqrt(kS**2 - mu * kS * kL + kL**2 / 4); kq = sp.sqrt(kS**2 + mu * kS * kL + kL**2 / 4)
    Mp = M.subs({kS: kp, mu: (mu * kS - kL / 2) / kp}, simultaneous=True)
    Mq = M.subs({kS: kq, mu: (-mu * kS - kL / 2) / kq}, simultaneous=True)
    f = R(5, 12) / (lamL * lamS) * (Mq / kq**3 + Mp / kp**3) * kS**3
    ser = sp.expand(sp.series(f.subs(kL, d * kS), d, 0, 1).removeO())
    assert ser.coeff(d, -1) == 0, ("1/k_L pole survives", ser.coeff(d, -1))
    f0 = sp.simplify(ser.coeff(d, 0))
    f0 = sp.expand(sp.re(f0)) if f0.has(sp.I) else sp.expand(f0)
    poly = sp.Poly(f0, mu)
    assert poly.degree() <= 2 and poly.coeff_monomial(mu) == 0, f0
    return sp.simplify(poly.coeff_monomial(1)), sp.simplify(poly.coeff_monomial(mu**2))
def mono(c0, c2): return sp.simplify(c0 + c2 / 3)
def SY(v): return sp.sympify(v, locals=LOC)
def kernels(hist, sol):
    """the five threading-map pieces (delta N_c^(2) = M zeta_L zeta_S at tau_f) for the history hist, plus the
    linear factor, the divergences and the worldline displacement -- exactly as in the 2026-09-04 script"""
    sub = {A2: sol[A2], P2: sol[P2], T2: sol[T2]}
    Nup = [trunc(hinv * Nlow[i]) for i in range(3)]
    div = trunc(sum(sp.diff(Nup[i], X[i]) for i in range(3))).subs(sub).subs(hist)
    DS, DLS = superhubble(lin(div, zS)), superhubble(cross(div))
    DL = superhubble(lin(div, zL))
    NxL = superhubble(lin(Nup[0], zL).subs(hist), order=-1)
    Zf = ZS.subs(hist).subs(tau, tf); ZLf = ZL.subs(hist).subs(tau, tf)
    intDS, cDS = tail(DS)
    lamS_ = sp.simplify(1 - R(1, 3) * intDS / Zf)
    Fx = anti(NxL); Delta_fin = sp.simplify(Fx - Fx.subs(tau, tf)); Delta_init_const = sp.simplify(-tail(NxL)[0])
    Zf2 = ZLf * Zf
    def kern(integrand): return sp.simplify(-R(1, 3) * tail(integrand)[0] / Zf2)
    K = {}
    K['psi2'] = kern(superhubble(cross(sum(sp.diff(psi2, xi, 2) for xi in X) / a**2).subs(sub).subs(hist)))
    K['grad'] = kern(superhubble(cross(-2 / a**2 * sum(dz[i] * sp.diff(psi1, X[i]) for i in range(3))).subs(hist)))
    K['zlap'] = kern(superhubble(cross(-2 / a**2 * zeta1 * lap(psi1)).subs(hist)))
    assert sp.simplify(K['psi2'] + K['grad'] + K['zlap'] - kern(DLS)) == 0
    K['wl_fin'] = kern(Delta_fin * sp.I * kS * mu * DS)
    K['wl_initextra'] = kern(Delta_init_const * sp.I * kS * mu * DS)
    K['lab_init'] = sp.simplify(sp.I * kS * mu * Delta_init_const * Zf / Zf2)
    return dict(K=K, lamS=lamS_, DS=DS, DL=DL, DLS=DLS, Delta_init=Delta_init_const, conv=cDS, A2sh=superhubble(sol[A2].subs(hist)))
OUT = {'sympy': sp.__version__}
# ================================================================ S9: uniform-rho final slice at second order
# Both modes on the growing mode of the same constant-eps background: hist_g = {mL: m, mS: m} with m kept symbolic
# (m = 3/eps - 1 substituted for the numbers; m -> 0 is the attractor, eps -> 0 at fixed m the USR-type limit).
hist_g = {mL: m, mS: m}
sol_g = solve_cross(hist_g, '_mm')
print("second-order lapse/shift solved (m_L = m_S = m)", round(time.time() - T0, 1), "s", flush=True)
Kg = kernels(hist_g, sol_g)
lam1 = sp.simplify(Kg['lamS'].subs(m, m_grow))                     # delta N_c,phi / zeta_phi  (= 1 - eps/3)
assert sp.simplify(lam1 - (1 - eps / 3)) == 0
Pg = {k: sp.simplify(v.subs(m, m_grow)) for k, v in Kg['K'].items()}
for k, v in Pg.items(): assert not v.has(tf), (k, v)
M_fin = sum(Pg[k] for k in ('psi2', 'grad', 'zlap', 'wl_fin'))
M_init = M_fin + Pg['wl_initextra'] + Pg['lab_init']
c0, c2 = f_of(M_fin, lam1, lam1)
assert (sp.simplify(c0 + 5 * eps / 4), sp.simplify(c2 - 5 * eps / 4)) == (0, 0)     # frozen 2026-09-04 result reproduced
print("phi-slice map reproduced: f_map(final label) =", c0, "+", c2, "mu^2", flush=True)
# --- the uniform-rho surface.  rho = phidot^2/(2N^2) + V exactly (delta phi = 0, no field gradients), so
#     delta rho = -phidot^2 alpha + (3/2) phidot^2 alpha^2 + O(3);  rho_bar = 3H^2.
#     Surface: rho(t_f + dt, x) = rho_bar(t_f)  =>  rhobar' dt + rhobar'' dt^2/2 + drho + drho' dt = 0, solved order by order.
rhob = 3 * H**2; rhob1 = ddt(rhob); rhob2 = ddt(rhob1)
alL = sp.simplify(lin(alpha1, zL).subs(hist_g)); alS = sp.simplify(lin(alpha1, zS).subs(hist_g))   # per unit z at the origin
drL, drS = -phidot2 * alL, -phidot2 * alS
dtL, dtS = sp.simplify(-drL / rhob1), sp.simplify(-drS / rhob1)
assert sp.simplify(dtS + ddt(ZS.subs(hist_g)) / (3 * H**2)) == 0                    # S9.1 of the 2026-09-04 note
drho2 = -phidot2 * Kg['A2sh'] + 3 * phidot2 * alL * alS                            # L x S cross part of delta rho^(2)
dt2 = sp.simplify(-(drho2 + ddt(drL) * dtS + ddt(drS) * dtL + rhob2 * dtL * dtS) / rhob1)
# --- continue the scalar field N_c(t, x) to the surface:  delta N_c,rho(x_f) = delta N_c(t_f + dt, x_f) + Nbar(t_f + dt) - Nbar(t_f)
#     = delta N_c(t_f, x_f) + H dt - (eps/2) H^2 dt^2 + d_t delta N_c^(1) dt,   d_t delta N_c^(1) = zetadot - D/3 (linear, super-Hubble)
dNdotL = ddt(ZL.subs(hist_g)) - Kg['DL'] / 3; dNdotS = ddt(ZS.subs(hist_g)) - Kg['DS'] / 3
Zf_g = (ZL * ZS).subs(hist_g).subs(tau, tf)
lam_rho_lin = sp.simplify((Kg['lamS'] * ZS.subs(hist_g) + H * dtS).subs(tau, tf) / ZS.subs(hist_g).subs(tau, tf))   # delta N_c,rho / zeta_phi
extra = H * dt2 - eps * H**2 * dtL * dtS + dNdotL * dtS + dNdotS * dtL
M_rho_extra = sp.simplify(extra.subs(tau, tf) / Zf_g)                             # general m, general eps
M_rho_extra_g = sp.simplify(M_rho_extra.subs(m, m_grow))
lamr = sp.simplify(lam_rho_lin.subs(m, m_grow))
assert sp.simplify(lamr - 2 * lam1) == 0                                            # linear: delta N_c,rho = 2 lambda zeta_phi
print("rho-slice linear factor delta N_c,rho / zeta_phi =", sp.factor(lamr), "| extra cross kernel:", sp.factor(M_rho_extra_g), flush=True)
M_rho_fin = M_fin + M_rho_extra_g
M_rho_init = M_rho_fin + (lamr / lam1) * (Pg['wl_initextra'] + Pg['lab_init'])      # translate the full linear rho-field lamr*zeta_S
res9 = {}
for lab, M_ in (('final', M_rho_fin), ('initial', M_rho_init), ('extra_only', M_rho_extra_g)):
    a0, a2 = f_of(M_, lamr, lamr)
    res9[lab] = {'const': str(a0), 'mu2': str(a2), 'monopole': str(mono(a0, a2)), 'const_3_2': str(a0.subs(eps, R(3, 2))), 'mu2_3_2': str(a2.subs(eps, R(3, 2)))}
    print(f"  f_map^rho ({lab:10s}) = {a0} + ({a2}) mu^2   [eps=3/2: {a0.subs(eps, R(3,2))} + ({a2.subs(eps, R(3,2))}) mu^2]", flush=True)
OUT['S9'] = {'lambda_phi': str(lam1), 'lambda_rho_prime(dNc_rho/zeta_phi)': str(lamr), 'dt1_S': str(dtS), 'dt2_LS_over_ZLZS': str(sp.simplify((dt2 / (ZL * ZS)).subs(hist_g).subs(m, m_grow))),
             'A2_superhubble_growing': str(sp.simplify(Kg['A2sh'].subs(m, m_grow))), 'M_rho_extra_growing': str(M_rho_extra_g),
             'M_rho_extra_general_m': str(M_rho_extra), 'f_map_rho': res9}

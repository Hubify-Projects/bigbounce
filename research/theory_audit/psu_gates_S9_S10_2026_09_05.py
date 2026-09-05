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
# --- S9 composition (the delta N value is read only now): f^rho = f_inin / lambda' + f_map^rho
f_inin_c0, f_inin_c2 = R(5, 12) * (-eps**2 + 6 * eps - 12), R(5, 12) * eps**2       # adjudication 2026-09-03 / threading note eq. (4)
comp9 = {}
for lab in ('final', 'initial'):
    a0 = sp.simplify(f_inin_c0 / lamr + SY(res9[lab]['const'])); a2 = sp.simplify(f_inin_c2 / lamr + SY(res9[lab]['mu2']))
    comp9[lab] = {'const': str(sp.factor(a0)), 'mu2': str(sp.factor(a2)), 'monopole': str(sp.factor(mono(a0, a2))),
                  'const_3_2': str(a0.subs(eps, R(3, 2))), 'mu2_3_2': str(a2.subs(eps, R(3, 2)))}
    print(f"  f_NL[delta N_c,rho] ({lab:7s} label) = {sp.factor(a0)} + ({sp.factor(a2)}) mu^2 ; eps=3/2: {a0.subs(eps, R(3,2))} + ({a2.subs(eps, R(3,2))}) mu^2", flush=True)
f_rho_init = SY(comp9['initial']['const']); assert sp.simplify(SY(comp9['initial']['mu2'])) == 0        # isotropic in the initial label
f_dN_lab = 5 * (eps - 7) / 8                                                         # lab delta N on uniform density (2026-09-02): -55/16 at 3/2
gap9 = sp.factor(f_rho_init - f_dN_lab)
print("  lab delta N (uniform rho) 5(eps-7)/8 =", f_dN_lab.subs(eps, R(3, 2)), "| threading rho-slice initial label =", f_rho_init.subs(eps, R(3, 2)),
      "| difference (threading - lab) =", gap9, "=", gap9.subs(eps, R(3, 2)), flush=True)
# --- limits: attractor (m -> 0: constant zeta, both slices coincide) and eps -> 0 at fixed m (USR-type)
extra_attr = sp.simplify(M_rho_extra.subs(m, 0)); A2_attr = sp.simplify(Kg['A2sh'].subs(m, 0)); dt1_attr = sp.simplify(dtS.subs(m, 0))
extra_usr = sp.simplify(sp.limit(M_rho_extra, eps, 0))
print("  attractor m->0: dt^(1) =", dt1_attr, ", A2 =", A2_attr, ", rho-extra kernel =", extra_attr, "| eps->0 at fixed m: rho-extra kernel ->", sp.factor(extra_usr), flush=True)
OUT['S9'].update({'composition': comp9, 'lab_deltaN_uniform_rho': str(f_dN_lab), 'threading_minus_lab_deltaN': str(gap9),
                  'attractor_m0': {'dt1': str(dt1_attr), 'A2_superhubble': str(A2_attr), 'rho_extra_kernel': str(extra_attr)},
                  'eps_to_0_fixed_m': {'rho_extra_kernel': str(extra_usr), 'lambda_rho_prime': str(sp.limit(lam_rho_lin, eps, 0))}})
assert extra_attr == 0 and A2_attr == 0 and dt1_attr == 0
# ================================================================ S10: constant long mode (m_L = 0) x growing short mode -> K_c
hist_c = {mL: 0, mS: m}
sol_c = solve_cross(hist_c, '_0m')
print("second-order lapse/shift solved (m_L = 0, m_S = m)", round(time.time() - T0, 1), "s", flush=True)
Kc_all = kernels(hist_c, sol_c)
Pc = {k: sp.simplify(v.subs(m, m_grow)) for k, v in Kc_all['K'].items()}
for k, v in Pc.items(): assert not v.has(tf), (k, v)
print("  constant-long-mode kernels:", {k: str(sp.factor(v)) for k, v in Pc.items()}, flush=True)
assert all(Pc[k] == 0 for k in ('grad', 'wl_fin', 'wl_initextra', 'lab_init')) and sp.simplify(Pc['zlap'] - 2 * eps / 3) == 0
K_c = Pc['psi2']                                                                     # THE constant-mode psi_2 kernel
K_c_general_m = sp.simplify(Kc_all['K']['psi2'])
print("  K_c(eps) =", sp.factor(K_c), "| general short history m:", sp.factor(K_c_general_m), flush=True)
fKc0, fKc2 = f_of(K_c, 1, lam1)                                                      # its f contribution, lambda_L = 1 (constant mode), lambda_S = lambda_1
# --- mixed long mode zeta_L = C + G, g = G_f / zeta_{L,f}:  lambda_g = 1 - eps g/3 (linear, exact), kernel bilinear in zeta_L:
#     M(g) = (2 eps/3) + g K_rest^grow + (1 - g) K_c,   f_map(g) = (5/12)/(lambda_g lambda_1) * Assemble[M(g)]   (two-lambda normalisation)
g = sp.symbols('g', nonnegative=True)
lam_g = 1 - eps * g / 3
assert sp.simplify(Kc_all['lamS'].subs(m, m_grow) - lam1) == 0                     # short leg unchanged
K_rest_init = M_init - Pg['zlap']; K_rest_fin = M_fin - Pg['zlap']
def fmap_g(K_rest):
    Mg = 2 * eps / 3 + g * K_rest + (1 - g) * K_c
    return f_of(Mg, lam_g, lam1)
fg_init = fmap_g(K_rest_init); fg_fin = fmap_g(K_rest_fin)
res10 = {}
for lab, (b0, b2) in (('initial', fg_init), ('final', fg_fin)):
    b0, b2 = sp.simplify(b0), sp.simplify(b2)
    v1 = (sp.simplify(b0.subs(g, 1)), sp.simplify(b2.subs(g, 1))); v0 = (sp.simplify(b0.subs(g, 0)), sp.simplify(b2.subs(g, 0)))
    res10[lab] = {'f_map(g)': {'const': str(b0), 'mu2': str(b2)}, 'g1': {'const': str(v1[0]), 'mu2': str(v1[1])}, 'g0': {'const': str(sp.factor(v0[0])), 'mu2': str(sp.factor(v0[1]))},
                  'g0_3_2': {'const': str(v0[0].subs(eps, R(3, 2))), 'mu2': str(v0[1].subs(eps, R(3, 2)))}}
    print(f"  f_map(g) [{lab:7s} label]: g=1 -> {v1[0]} + ({v1[1]}) mu^2 ; g=0 -> {sp.factor(v0[0])} + ({sp.factor(v0[1])}) mu^2", flush=True)
# g = 1 must be the frozen growing-mode map; composed with the in-in this is -5 (initial) and -25/4 + (15/4) mu^2 (final) at eps = 3/2
i0, i2 = [sp.simplify(v) for v in fg_init]; n0, n2 = [sp.simplify(v) for v in fg_fin]
assert sp.simplify(f_inin_c0 / lam1 + i0.subs(g, 1) + 5) == 0 and sp.simplify(f_inin_c2 / lam1 + i2.subs(g, 1)) == 0
tot_fin = (sp.simplify(f_inin_c0 / lam1 + n0.subs(g, 1)), sp.simplify(f_inin_c2 / lam1 + n2.subs(g, 1)))
assert (tot_fin[0].subs(eps, R(3, 2)), tot_fin[1].subs(eps, R(3, 2))) == (R(-25, 4), R(15, 4))
assert sp.simplify(n0.subs(g, 1) + 5 * eps / 4) == 0 and sp.simplify(n2.subs(g, 1) - 5 * eps / 4) == 0
# g = 0: label independent (no worldline / translation pieces for a constant long mode)
assert sp.simplify(i0.subs(g, 0) - n0.subs(g, 0)) == 0 and sp.simplify(i2.subs(g, 0) - n2.subs(g, 0)) == 0
# limits of K_c: both modes constant (m -> 0) and eps -> 0 at fixed short history
Kc_m0 = sp.simplify(K_c_general_m.subs(m, 0)); Kc_eps0 = sp.simplify(sp.limit(K_c, eps, 0))
print("  K_c limits: m_S -> 0 (both constant):", Kc_m0, "| eps -> 0:", Kc_eps0, "| f-contribution of K_c alone:", sp.factor(fKc0), "+", sp.factor(fKc2), "mu^2", flush=True)
assert Kc_m0 == 0 and Kc_eps0 == 0
OUT['S10'] = {'kernels_constant_long_mode': {k: str(v) for k, v in Pc.items()}, 'K_c': str(sp.factor(K_c)), 'K_c_general_short_history_m': str(K_c_general_m),
              'K_c_limits': {'m_S_to_0': str(Kc_m0), 'eps_to_0': str(Kc_eps0)}, 'f_of_K_c_alone(lamL=1,lamS=lam1)': {'const': str(fKc0), 'mu2': str(fKc2)},
              'normalisation_note': 'f_map(g) = (5/12)/(lambda_g lambda_1) Assemble[M(g)]: the long leg carries lambda_g, the short leg lambda_1; '
                                    'the 2026-09-04 S10.1 prefactor 5/(6 lambda_g^2) is correct only at g = 1',
              'lambda_g': str(lam_g), 'f_map_g': res10, 'convergence_conditions': sorted(set(Kc_all['conv'] + Kg['conv']))}
OUT['wall_clock_s'] = round(time.time() - T0, 1)
json.dump(OUT, open(__file__.replace('.py', '.json'), 'w'), indent=1, default=str)
print("ALL ASSERTIONS PASS; done", OUT['wall_clock_s'], "s")

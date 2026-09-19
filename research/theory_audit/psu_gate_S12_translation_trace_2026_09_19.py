#!/usr/bin/env python3
"""PSU gate S12 -- the translation term's trace part at general constant-epsilon.

GATE (DISPOSITIONS/PSU.md sec.S12, Gemini R3VERIFY pass-2):  paper-su Appendix A3 states
    T(eps,mu) = f_map^init - f_map^fin = 5 eps/(4(3-eps)) (1 - 3 mu^2),  monopole 0 (all eps),
justified in the text by "the O(k_S/k_L) poles cancel between the two short legs, THE TRACE PART
VANISHES AT n_s = 1, and the shear gives the quadrupole-only translation term".  For a general
constant-eps background n_s != 1, so the exact monopole may carry an eps-dependent correction
that would break the exact, eps-independent  f_deltaN^init == -5.  Nobody had independently
re-derived the trace part.

THIS SCRIPT (from scratch, exact sympy):
  S1  re-derives the first-order comoving-gauge ADM solution by SOLVING the linearised
      Hamiltonian + momentum constraints (not by asserting Maldacena's result), extracts the
      long-mode Lagrangian displacement xi^i, and splits d_i xi_j into trace + shear.
  S2  builds the translation (label-change) kernel from that xi ALONE and checks it against the
      committed threading-map kernels lab_init + wl_initextra.
  S3  builds an EXACT general-tilt squeezed-bispectrum assembly operator, P(k) = k^(s-3)
      with s = n_s - 1 (s = 0 <=> P ~ k^-3 <=> the n_s = 1 assumption hardwired in BOTH
      committed sources: threading_map_second_order_2026_09_04.py line "B = Mq/kq**3 + Mp/kp**3"
      and fnl_monopole_adjudication_2026_09_03_general_eps.py line "Pw = {k1:k1**-3,...}").
  S4  VALIDATES the machinery at s = 0 against every committed/printed number
      (per-piece f's, T, f_map^fin, f_map^init, monopole -5 eps/6, eps=3/2 dust values,
      eps->0, USR) before any general-tilt claim is made.
  S5  general-tilt lemma: the entire s-dependence of f[M] is fixed by the 1/k_L pole of M.
  S6  derives n_s(eps) for a constant-eps background from the Mukhanov-Sasaki mode functions.
  S7  re-runs the in-in squeezed bispectrum (same committed vertices) at general tilt and
      composes  f_deltaN^init = f^in-in/lambda + f_map^init  at s = s(eps).

Local CPU, no network, no data.  Manifest:
reproducibility/manifests/experiments/psu-gate-s12-translation-trace.json
"""
import sympy as sp, json, time, os
T0 = time.time()
OUT = {}
def say(*a):
    print(*a, flush=True)

eps = sp.Symbol('epsilon', positive=True)
mu  = sp.Symbol('mu', real=True)
s   = sp.Symbol('s', real=True)              # s = n_s - 1 ; P(k) = k^(s-3)
kL, kS = sp.symbols('k_L k_S', positive=True)
d   = sp.Symbol('delta', positive=True)      # squeezing parameter, k_L -> d k_S
lam = 1 - eps/3                              # linear threading factor deltaN_c = lam zeta

# ======================================================================== S1
# First-order comoving-gauge ADM solution, SOLVED (not asserted), then xi.
say("[S1] first-order ADM constraints ...")
tau = sp.Symbol('tau', positive=True)        # cosmic time t = -tau (contraction), a = tau^(1/eps)
x, y, z = sp.symbols('x y z', real=True); X = [x, y, z]
pexp = 1/eps
a = tau**pexp
def ddt(f): return -sp.diff(f, tau)          # d/dt with t = -tau
H = sp.simplify(ddt(a)/a)
phidot2 = 2*eps*H**2
V = (3 - eps)*H**2
assert sp.simplify(3*H**2 - phidot2/2 - V) == 0
assert sp.simplify(-ddt(H)/H**2 - eps) == 0
m = sp.Symbol('m', positive=True)
Zt = tau**(-m); m_grow = 3*pexp - 1
assert sp.simplify(ddt(a**3*eps*ddt(Zt)).subs(m, m_grow)) == 0     # growing mode of (a^3 eps zetadot)^. = 0
zL = sp.Symbol('z_L')
# long mode along x, unknown lapse/shift potentials A1(tau), PS1(tau) -- to be SOLVED for
A1 = sp.Function('A1')(tau); PS1 = sp.Function('PS1')(tau)
eLw = sp.exp(sp.I*kL*x)
zeta = zL*Zt*eLw
alpha = A1*zL*Zt*eLw
psi   = PS1*zL*Zt*eLw
def grad(f): return [sp.diff(f, xi) for xi in X]
def lap(f):  return sum(sp.diff(f, xi, 2) for xi in X)
Nlow = grad(psi)
dz = grad(zeta)
def lin(e):                                   # O(z_L) coefficient at the origin
    return sp.simplify(sp.expand(e).coeff(zL, 1).subs({x: 0, y: 0, z: 0}))
def trunc(e, deg=1):
    out = 0
    for t in sp.Add.make_args(sp.expand(e)):
        if sp.degree(t, zL) <= deg: out += t
    return out
Nk_dz = sum(Nlow[k]*dz[k] for k in range(3))
def DN(i, j):
    return sp.diff(Nlow[j], X[i]) - Nlow[i]*dz[j] - Nlow[j]*dz[i] + (Nk_dz if i == j else 0)
hdot_diag = trunc(2*a**2*(H + ddt(zeta))*(1 + 2*zeta))
E = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        E[i, j] = trunc(sp.Rational(1, 2)*((hdot_diag if i == j else 0) - DN(i, j) - DN(j, i)))
hinv = (1 - 2*zeta)/a**2
Emix = sp.Matrix(3, 3, lambda i, j: trunc(hinv*E[i, j]))
Etr  = trunc(sum(Emix[i, i] for i in range(3)))
EE   = trunc(sum(Emix[i, j]*Emix[j, i] for i in range(3) for j in range(3)))
R3   = trunc(-2*hinv*(2*lap(zeta) + sum(dd**2 for dd in dz)))
Ham  = trunc(R3 - 2*V - trunc(1 - 2*alpha + 3*alpha**2)*(EE - Etr**2 + phidot2))
Tm   = sp.Matrix(3, 3, lambda i, j: trunc(trunc(1 - alpha + alpha**2)*(Emix[i, j] - (Etr if i == j else 0))))
def Mom(j):
    e = sum(sp.diff(Tm[i, j], X[i]) for i in range(3))
    e += sum(3*dz[k]*Tm[k, j] for k in range(3))
    e -= dz[j]*sum(Tm[i, i] for i in range(3)) + sum(dz[i]*Tm[i, j] for i in range(3)) \
         - sum(dz[k]*Tm[j, k] for k in range(3))
    return trunc(e)
bg = [sp.simplify(sp.expand(c).coeff(zL, 0)) for c in (Ham, Mom(0))]
assert bg == [0, 0], bg                                                    # background solved exactly
sol1 = sp.solve([lin(Ham), lin(Mom(0))], [A1, PS1], dict=True)
assert len(sol1) == 1, sol1
A1s, PS1s = sp.simplify(sol1[0][A1]), sp.simplify(sol1[0][PS1])
say("      SOLVED  alpha_1/zeta =", A1s, "   psi_1/zeta =", sp.factor(PS1s))
assert sp.simplify(A1s - ddt(Zt)/(H*Zt)) == 0                              # = zetadot/H  (Maldacena), DERIVED
chi_expected = -a**2*eps*ddt(Zt)/kL**2                                     # d^2 chi = a^2 eps zetadot
assert sp.simplify(PS1s - (-Zt/H + chi_expected)/Zt) == 0                  # = -zeta/H + chi, DERIVED
OUT['S1_first_order_solution'] = {'alpha1_over_zeta': str(A1s),
                                  'psi1_over_zeta': str(sp.factor(PS1s)),
                                  'solved_not_asserted': True}

# Lagrangian displacement of a fluid worldline:  dx^i/dt = -N^i,  x_i = x_f + xi,  xi = int N^i dt.
Nup_x = sp.simplify(hinv*Nlow[0])                                          # N^x = h^{xj} N_j, linear order
Nup_x_lin = sp.simplify(sp.expand(Nup_x.subs({A1: A1s, PS1: PS1s})).coeff(zL, 1).subs({x: 0, y: 0, z: 0}))
def powterms(e):
    out = []
    for t in sp.Add.make_args(sp.expand(e)):
        if t == 0: continue
        ex = sp.simplify(tau*sp.diff(t, tau)/t); assert not ex.has(tau), (t, ex)
        out.append((sp.simplify(t/tau**ex), ex))
    return out
tf = sp.Symbol('tau_f', positive=True)
def tail(e):                                                               # int_{tau_f}^{inf} e dtau  = int_{-inf}^{t_f} e dt
    tot, conds = 0, []
    for c, ex in powterms(e):
        tot += -c*tf**(ex + 1)/(ex + 1); conds.append(str(sp.simplify(ex + 1)) + ' < 0')
    return sp.simplify(tot), conds
xi_x, xi_conds = tail(Nup_x_lin)                                           # total displacement, initial slice -> final slice
xi_over_zeta = sp.powsimp(sp.simplify((xi_x/Zt.subs(tau, tf)).subs(m, m_grow)), force=True)
assert not xi_over_zeta.has(tf) or sp.simplify(sp.diff(xi_over_zeta, tf)).has(kL)   # tf-dependence only in the O(k_L^2) gradient piece
# super-Hubble leading term (k_L -> 0): keep the O(1/k_L) pole, drop the O(k_L) gradient remainder
xi_sh = sp.simplify(sp.limit(sp.expand(xi_over_zeta.subs(kL, d*kL))*d, d, 0))
assert sp.simplify(xi_sh + sp.I*eps/kL) == 0, xi_sh                        # xi^x = -i eps zeta_L / k_L
# trace / shear split of d_i xi_j for the plane wave xi^j = xi_sh delta^{jx} e^{i k_L x}
div_xi = sp.simplify(sp.I*kL*xi_sh)                                        # (d_i xi^i)/zeta_L(t_f)
shear_xx = sp.simplify(sp.I*kL*xi_sh - div_xi/3)                           # traceless part, xx component
say("      xi^x/zeta_L =", xi_sh, "   TRACE  d_i xi^i / zeta_L =", div_xi, "   SHEAR (xx) =", shear_xx)
assert sp.simplify(div_xi - eps) == 0, div_xi                              # <<< THE TRACE PART: d.xi = eps zeta_L, EXACT
OUT['S2_trace'] = {'xi_x_over_zetaL': str(xi_sh), 'div_xi_over_zetaL': str(div_xi), 'shear_xx': str(shear_xx),
                   'statement': 'd_i xi^i = eps zeta_L exactly (super-Hubble), independent of n_s',
                   'convergence': sorted(set(xi_conds))}

# ======================================================================== S2
# Translation (label-change) kernel from xi alone:  F_init(x) = F_fin(x - xi)  =>  Delta F = -xi.grad F_S.
# deltaN_c is linear-order lam*zeta, so the kernel in the script's zeta_L zeta_S normalisation is
#   M_T = -lam * i k_S.xi / zeta_L = -lam * eps * k_S mu / k_L .
M_T = sp.simplify(-lam*sp.I*(kS*mu)*xi_sh)
say("[S2] translation kernel from scratch:  M_T =", sp.simplify(M_T))
J = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'threading_map_second_order_2026_09_04.json')))
SY = lambda v: sp.sympify(v, locals={'epsilon': eps, 'mu': mu, 'k_L': kL, 'k_S': kS})
K = {k: SY(v) for k, v in J['kernels_growing_mode'].items()}
assert sp.simplify(M_T - (K['lab_init'] + K['wl_initextra'])) == 0          # independent reproduction
say("      == committed  lab_init + wl_initextra   OK")
OUT['S2_translation_kernel'] = {'from_scratch': str(sp.simplify(M_T)),
                                'committed_lab_init_plus_wl_initextra': str(sp.simplify(K['lab_init'] + K['wl_initextra'])),
                                'agree': True}

# ======================================================================== S3
# EXACT general-tilt squeezed assembly.   P(k) = k^(s-3);  s = 0 <=> n_s = 1 <=> the committed assumption.
def assemble(M, tilt, lam_=lam):
    """f = (5/12)/lam^2 * [ M_q P(kq) + M_p P(kp) ] / P(kS),  leading order as k_L -> 0. Exact in `tilt`."""
    kp = sp.sqrt(kS**2 - mu*kS*kL + kL**2/4)
    kq = sp.sqrt(kS**2 + mu*kS*kL + kL**2/4)
    Mp = M.subs({kS: kp, mu: (mu*kS - kL/2)/kp}, simultaneous=True)
    Mq = M.subs({kS: kq, mu: (-mu*kS - kL/2)/kq}, simultaneous=True)
    B  = Mq*kq**(tilt - 3) + Mp*kp**(tilt - 3)
    f  = sp.Rational(5, 12)/lam_**2*B*kS**(3 - tilt)
    ser = sp.expand(sp.series(f.subs(kL, d*kS), d, 0, 1).removeO())
    assert sp.simplify(ser.coeff(d, -1)) == 0, ("1/k_L pole survives", sp.simplify(ser.coeff(d, -1)))
    f0 = sp.simplify(ser.coeff(d, 0))
    f0 = sp.expand(sp.re(f0)) if f0.has(sp.I) else sp.expand(f0)
    return sp.simplify(f0)
def mono(f):  return sp.simplify(sp.integrate(sp.expand(f), (mu, -1, 1))/2)

# ======================================================================== S4  VALIDATION at s = 0
say("[S4] validating the machinery at s = 0 (n_s = 1) against every committed/printed value ...")
val = {}
for name in ('psi2', 'grad', 'zlap', 'wl_fin'):
    f0 = assemble(K[name], 0)
    ref = SY(J['map_fNL_pieces'][name]['const']) + SY(J['map_fNL_pieces'][name]['mu2'])*mu**2
    assert sp.simplify(f0 - ref) == 0, (name, f0, ref)
    val[name] = str(f0)
M_fin  = sum(K[n] for n in ('psi2', 'grad', 'zlap', 'wl_fin'))
M_init = M_fin + K['wl_initextra'] + K['lab_init']
f_fin0, f_init0 = assemble(M_fin, 0), assemble(M_init, 0)
assert sp.simplify(mono(f_fin0) + 5*eps/6) == 0                             # paper App. A2 "Totals"
assert sp.simplify(mono(f_init0) + 5*eps/6) == 0
assert sp.simplify(f_fin0 - (-sp.Rational(5, 4)*eps*(1 - mu**2))) == 0       # paper Eq. f_map^fin
assert sp.simplify(f_init0 - sp.Rational(5, 4)*eps/(3 - eps)*((eps - 2) - eps*mu**2)) == 0   # paper Eq. f_map^init
T0_paper = sp.Rational(5, 4)*eps/(3 - eps)*(1 - 3*mu**2)                    # paper App. A3 T(eps,mu)
T0_here  = assemble(M_T, 0)
assert sp.simplify(T0_here - T0_paper) == 0, (T0_here, T0_paper)
assert sp.simplify(mono(T0_here)) == 0                                      # the paper's "monopole 0 (all eps)" -- at s=0
say("      T(eps,mu)|_{n_s=1} =", sp.factor(T0_here), "  monopole", mono(T0_here), " == paper App.A3  OK")
f_inin0 = sp.Rational(5, 12)*(eps**2*mu**2 - eps**2 + 6*eps - 12)           # committed general-eps in-in shape
assert sp.simplify(mono(f_inin0) + 5*(eps - 3)*(eps - 6)/18) == 0
comp0 = sp.simplify(f_inin0/lam + f_init0)
assert sp.simplify(comp0 + 5) == 0                                          # <<< the paper's eps-independent -5, at s=0
say("      f_deltaN^init |_{n_s=1} =", comp0, " == -5 for every constant eps  OK")
# dust eps=3/2 headline numbers
e32 = {eps: sp.Rational(3, 2)}
comp_fin0 = sp.simplify(f_inin0/lam + f_fin0)                               # composed, FINAL label
assert sp.simplify(comp_fin0.subs(e32) - (-sp.Rational(25, 4) + sp.Rational(15, 4)*mu**2)) == 0
assert sp.simplify(mono(comp_fin0) + 5) == 0                                # both labels compose to monopole -5
assert sp.simplify(f_fin0.subs(e32) - (-sp.Rational(15, 8) + sp.Rational(15, 8)*mu**2)) == 0
assert mono(f_inin0).subs(e32) == sp.Rational(-15, 8)                       # in-in monopole
assert sp.simplify((mono(f_inin0) - (-5)).subs(e32)) == sp.Rational(25, 8)  # the gap
assert sp.simplify((-5)/mono(f_inin0).subs(e32)) == sp.Rational(8, 3)       # the headline factor 8/3
# eps -> 0 and USR: every map kernel carries an explicit eps
assert all(sp.limit(v, eps, 0) == 0 for v in K.values())
say("      dust (eps=3/2): composed final-label -25/4 + 15/4 mu^2, in-in monopole -15/8, gap 25/8, factor 8/3  OK")
say("      eps->0 / USR: every map kernel -> 0  OK")
OUT['S4_validation_s0'] = {'per_piece_f': val, 'f_map_fin': str(f_fin0), 'f_map_init': str(f_init0),
    'T': str(sp.factor(T0_here)), 'T_monopole': str(mono(T0_here)), 'composed': str(comp0),
    'all_committed_and_printed_values_reproduced': True}

# ======================================================================== S5  general tilt
say("[S5] general tilt s = n_s - 1 ...")
T_s = assemble(M_T, s)
dT  = sp.simplify(sp.expand(T_s - T0_here))
say("      T(eps,mu,s) =", sp.factor(T_s))
say("      delta T      =", sp.factor(dT), "   monopole(delta T) =", sp.factor(mono(dT)))
assert sp.simplify(dT - sp.Rational(5, 4)*eps/(3 - eps)*s*mu**2) == 0
assert sp.simplify(mono(T_s) - 5*eps*s/(12*(3 - eps))) == 0
f_fin_s, f_init_s = assemble(M_fin, s), assemble(M_init, s)
assert sp.simplify(f_fin_s - f_fin0) == 0          # FINAL-label map is tilt-INDEPENDENT
assert sp.simplify(f_init_s - f_init0 - dT) == 0   # all map tilt-dependence sits in the translation term
say("      f_map^fin is tilt-INDEPENDENT; the whole map tilt-dependence is the translation term  OK")
# lemma: the s-dependence of f[M] is fixed by the 1/k_L pole of M,  M -> (k_S/k_L) g(mu)
def pole_g(M):
    return sp.simplify(sp.limit(sp.expand(M.subs(kL, d*kS))*d, d, 0))   # M -> (k_S/k_L) g(mu)
g_fin, g_init, g_T = pole_g(M_fin), pole_g(M_init), pole_g(M_T)
say("      pole coefficients g(mu):  final label", g_fin, "| initial label", sp.factor(g_init), "| translation", sp.factor(g_T))
assert sp.simplify(g_fin) == 0 and sp.simplify(g_init - g_T) == 0 and sp.simplify(g_T + lam*eps*mu) == 0
for M in (M_fin, M_init, M_T, K['psi2'], K['grad'], K['zlap'], K['wl_fin']):
    assert sp.simplify(assemble(M, s) - assemble(M, 0) + sp.Rational(5, 12)/lam**2*s*mu*pole_g(M)) == 0
say("      LEMMA verified on all 7 kernels:  f[M](s) - f[M](0) = -(5 s /(12 lam^2)) mu g(mu)")
OUT['S5_general_tilt'] = {'T_of_s': str(sp.factor(T_s)), 'delta_T': str(sp.factor(dT)),
    'T_monopole_of_s': str(sp.factor(mono(T_s))), 'f_map_fin_tilt_independent': True,
    'pole_g': {'final': str(g_fin), 'initial': str(sp.factor(g_init)), 'translation': str(sp.factor(g_T))},
    'lemma': 'f[M](s) - f[M](0) = -(5 s/(12 lam^2)) mu g(mu),  M -> (k_S/k_L) g(mu)'}

# ======================================================================== S6  n_s(eps)
say("[S6] n_s for a constant-eps background (Mukhanov-Sasaki) ...")
eta = sp.Symbol('eta', negative=True)
p_eta = 1/(eps - 1)                                   # a ~ (-eta)^p_eta  <=>  a ~ t^(1/eps)
zMS = (-eta)**p_eta                                   # z = a sqrt(2 eps), eps const => z ~ a
nu2 = sp.simplify(sp.diff(zMS, eta, 2)/zMS*eta**2 + sp.Rational(1, 4))
assert sp.simplify(nu2 - (p_eta - sp.Rational(1, 2))**2) == 0
# The calculation correlates the GROWING branch zeta ~ (-eta)^(1-2p) (m = 3/eps - 1); its index:
s_grow = sp.simplify(4 - 2*p_eta)                     # = 2(2 eps - 3)/(eps - 1)
# The LATE-TIME DOMINANT super-horizon mode has index 3 - 2|nu| (constant mode when p < 1/2):
s_of_eps = 3 - 2*sp.Abs(p_eta - sp.Rational(1, 2))
# they coincide exactly where the growing branch IS the dominant one, p > 1/2  <=>  1 < eps < 3
for e_ in (sp.Rational(5, 4), sp.Rational(3, 2), 2, sp.Rational(5, 2)):
    assert sp.simplify(s_grow.subs(eps, e_) - s_of_eps.subs(eps, e_)) == 0, e_
assert sp.simplify(s_grow.subs(eps, sp.Rational(3, 2))) == 0                      # dust: scale-invariant
assert sp.simplify(sp.limit(s_grow, eps, sp.oo)) == 4 and sp.simplify(sp.limit(s_grow, eps, 0)) == 6
say("      growing-branch      n_s - 1 =", sp.factor(s_grow), "  (the mode these kernels correlate)")
say("      late-time dominant  n_s - 1 =", s_of_eps, "  (equal to the above iff 1 < eps < 3)")
checks = {'dust eps=3/2': (sp.Rational(3, 2), 0), 'eps=2': (2, 2), 'eps=3': (3, 3), 'eps=6': (6, sp.Rational(12, 5))}
for lbl, (e_, want) in checks.items():
    got = sp.simplify(s_of_eps.subs(eps, e_)); assert sp.simplify(got - want) == 0, (lbl, got, want)
assert sp.simplify(sp.limit(s_of_eps, eps, 0)) == 0                      # de Sitter / slow-roll: scale invariant
assert sp.simplify(sp.limit(s_of_eps, eps, sp.oo)) == 2                  # ekpyrotic: strongly blue, n_s = 3
say("      checks: eps=3/2 -> 0 (scale-invariant matter contraction); eps->0 -> 0; eps->oo -> 2 (n_s=3, blue)  OK")
OUT['S6_ns_of_eps'] = {'n_s_minus_1_growing_branch': str(sp.factor(s_grow)),
    'equal_iff': '1 < eps < 3 (p > 1/2), where the growing branch is the dominant super-horizon mode',
    'n_s_minus_1': str(s_of_eps), 'nu': 'p - 1/2, p = 1/(eps-1)',
    'validated': {'eps=3/2': '0', 'eps->0': '0', 'eps=2': '2', 'eps=3': '3', 'eps->oo': '2'}}

# ======================================================================== S7  in-in at general tilt + composition
say("[S7] in-in squeezed bispectrum at general tilt (committed vertices, tilt only in the external P's) ...")
k1, k2, k3 = sp.symbols('k1 k2 k3', positive=True)
def dot(P, Q, R): return (R**2 - P**2 - Q**2)/2
aI  = (-eta)**p_eta
a2I = aI**2; calH = sp.simplify(sp.diff(aI, eta)/aI); a2eps = a2I*eps
gI  = 1 - 2*p_eta
z1  = (-eta)**gI
assert sp.simplify(sp.diff(a2eps*sp.diff(z1, eta), eta)) == 0
verts = {'T1': dict(coef=a2I*(eps**2 - eps**3/2), legs=[(0, False), (1, False), (1, False)], V=lambda P, Q, R: sp.Integer(1)),
         'T3': dict(coef=-2*a2I*eps**2, legs=[(1, False), (0, False), (1, True)], V=lambda P, Q, R: dot(Q, R, P)/R**2),
         'T4': dict(coef=a2I*eps**3/2, legs=[(0, False), (1, True), (1, True)], V=lambda P, Q, R: dot(Q, R, P)**2/(Q**2*R**2))}
def mode1(al): return z1 if al == 0 else sp.diff(z1, eta)
Fs = sp.Symbol('F')
def kern(vert, j, k, P, Q):
    legs = vert['legs']; others = [i for i in range(3) if i != j]
    momv = [None]*3; momv[j] = k; momv[others[0]] = P; momv[others[1]] = Q
    prod = vert['coef']*vert['V'](*momv)*mode1(legs[others[0]][0])*mode1(legs[others[1]][0])
    src = prod if legs[j][0] == 0 else -sp.diff(prod, eta)
    lhs = 2*sp.diff(a2eps*sp.diff(Fs*(-eta)**(2*gI), eta), eta)
    return sp.simplify(sp.solve(sp.Eq(lhs, src), Fs)[0])
def redef(k, P, Q):
    pq = dot(P, Q, k); kp_ = (k**2 + P**2 - Q**2)/2; kq_ = (k**2 + Q**2 - P**2)/2
    fa = sp.simplify(mode1(0)*mode1(1)/calH/(-eta)**(2*gI))
    fb = sp.simplify((eps/(2*calH))*(pq/Q**2 - kp_*kq_/(k**2*Q**2))*mode1(0)*mode1(1)/(-eta)**(2*gI))
    return {'fa': sp.simplify(fa), 'fb': sp.simplify(fb)}
def pieces(k, P, Q):
    out = {}
    for vn, vert in verts.items():
        for j in range(3):
            for order, (pp, qq) in enumerate([(P, Q), (Q, P)]):
                out[(vn, j, order)] = kern(vert, j, k, pp, qq)/2
    for order, (pp, qq) in enumerate([(P, Q), (Q, P)]):
        r = redef(k, pp, qq); out[('fa', 'r', order)] = r['fa']/2; out[('fb', 'r', order)] = r['fb']/2
    return out
kp_s = sp.sqrt(kS**2 - mu*kS*kL + kL**2/4); kq_s = sp.sqrt(kS**2 + mu*kS*kL + kL**2/4)
def f_inin(tilt):
    """f = (5/12) [ 2 F(kq;kL,kp) P(kp) + 2 F(kp;kL,kq) P(kq) ] / P(kS),  P(k)=k^(tilt-3)."""
    tot = 0
    for (ko, kother) in ((kq_s, kp_s), (kp_s, kq_s)):
        for key, F in pieces(k1, k2, k3).items():
            c = sp.Rational(5, 12)*2*F.subs({k1: ko, k2: kL, k3: kother}, simultaneous=True)*kother**(tilt - 3)*kS**(3 - tilt)
            ser = sp.series(sp.expand(c).subs(kL, d*kS), d, 0, 1).removeO()
            tot += sp.expand(ser).coeff(d, 0)
    return sp.simplify(sp.expand(tot))
f_inin_0 = f_inin(0)
say("      f^in-in(mu,eps) | s=0  =", sp.factor(f_inin_0))
assert sp.simplify(f_inin_0 - f_inin0) == 0          # reproduces the committed general-eps in-in shape EXACTLY
say("      == committed (5/12)(eps^2 mu^2 - eps^2 + 6 eps - 12)  OK")
f_inin_s = f_inin(s)
d_inin = sp.simplify(sp.expand(f_inin_s - f_inin_0))
say("      delta f^in-in(s) =", sp.factor(d_inin), "  monopole", sp.factor(mono(d_inin)))
comp_s = sp.simplify(f_inin_s/lam + f_init_s)
say("      f_deltaN^init(eps,mu,s) =", sp.factor(comp_s))
say("      composed monopole      =", sp.factor(mono(comp_s)))
resid = sp.simplify(sp.expand(comp_s + 5))
say("      residual (composed + 5) =", sp.factor(resid))
comp_phys = sp.simplify(comp_s.subs(s, s_of_eps))
OUT['S7_inin_and_composition'] = {
    'f_inin_s0': str(sp.factor(f_inin_0)), 'f_inin_general_s': str(sp.factor(f_inin_s)),
    'delta_f_inin': str(sp.factor(d_inin)), 'delta_f_inin_monopole': str(sp.factor(mono(d_inin))),
    'composed_general_s': str(sp.factor(comp_s)), 'composed_monopole': str(sp.factor(mono(comp_s))),
    'residual_composed_plus_5': str(sp.factor(resid)),
    'composed_at_physical_ns': str(sp.factor(comp_phys)),
    'composed_at_eps_3_2': str(sp.simplify(comp_s.subs(s, s_of_eps).subs(eps, sp.Rational(3, 2))))}
say("      at the physical n_s(eps):  f_deltaN^init =", sp.factor(comp_phys))
say("      at eps = 3/2 (dust):        f_deltaN^init =", sp.simplify(comp_s.subs(s, s_of_eps).subs(eps, sp.Rational(3, 2))))
# ======================================================================== S8  numeric convergence check
# The squeezed limits above are taken by sympy series in k_L.  Re-evaluate the FULL finite-k_L
# assemblies numerically at shrinking k_L/k_S and confirm they converge to the symbolic answers.
say("[S8] finite-k_L numeric convergence check (guards the series extraction) ...")
def assemble_numeric(M, tilt_v, eps_v, mu_v, r):
    """exact-rational evaluation of f[M] at finite k_L/k_S = r (no series)."""
    sub = {eps: sp.Rational(eps_v), mu: sp.nsimplify(mu_v), kS: 1, kL: sp.Rational(r)}
    kp_ = sp.sqrt(1 - sp.nsimplify(mu_v)*sp.Rational(r) + sp.Rational(r)**2/4)
    kq_ = sp.sqrt(1 + sp.nsimplify(mu_v)*sp.Rational(r) + sp.Rational(r)**2/4)
    Mp = M.subs({kS: kp_, mu: (sp.nsimplify(mu_v) - sp.Rational(r)/2)/kp_}, simultaneous=True)
    Mq = M.subs({kS: kq_, mu: (-sp.nsimplify(mu_v) - sp.Rational(r)/2)/kq_}, simultaneous=True)
    B = Mq*kq_**(tilt_v - 3) + Mp*kp_**(tilt_v - 3)
    lam_v = 1 - sp.Rational(eps_v)/3
    return sp.N((sp.Rational(5, 12)/lam_v**2*B).subs({eps: sp.Rational(eps_v), kL: sp.Rational(r)}), 30)
num_checks = {}
for (eps_v, tilt_v, mu_v) in [(sp.Rational(3, 2), 0, sp.Rational(2, 5)), (2, 2, sp.Rational(2, 5)),
                              (sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(-3, 4))]:
    tgt = complex(sp.N(assemble(M_T, s).subs({s: tilt_v, eps: eps_v, mu: mu_v}), 30))
    seq = [complex(assemble_numeric(M_T, tilt_v, eps_v, mu_v, sp.Rational(1, 10**n))) for n in (2, 3, 4)]
    errs = [abs(v - tgt) for v in seq]
    say(f"      T: eps={eps_v} s={tilt_v} mu={mu_v}  symbolic {tgt.real:.10f}  |err| at k_L/k_S=1e-2,-3,-4: "
        + ", ".join(f"{e:.2e}" for e in errs))
    assert errs[-1] < 1e-7 and errs[-1] < errs[0], (eps_v, tilt_v, errs)     # converging to the symbolic limit
    num_checks[f"T_eps{eps_v}_s{tilt_v}"] = {'symbolic': f"{tgt.real:.12f}", 'abs_err_1e-4': f"{errs[-1]:.3e}"}
# same for the two full map totals
for lbl, M in (('map_fin', M_fin), ('map_init', M_init)):
    tgt = complex(sp.N(assemble(M, s).subs({s: 2, eps: 2, mu: sp.Rational(2, 5)}), 30))
    got = complex(assemble_numeric(M, 2, 2, sp.Rational(2, 5), sp.Rational(1, 10**4)))
    say(f"      {lbl}: eps=2 s=2 mu=2/5  symbolic {tgt.real:.10f}  numeric {got.real:.10f}  |err| {abs(got-tgt):.2e}")
    assert abs(got - tgt) < 1e-6, (lbl, tgt, got)
    num_checks[lbl] = {'symbolic': f"{tgt.real:.12f}", 'numeric_1e-4': f"{got.real:.12f}"}
say("      series extraction confirmed against finite-k_L evaluation  OK")
OUT['S8_numeric_convergence'] = num_checks
# ======================================================================== S9  adjudicator reconciliation
# An independent blind Fable adjudicator (model "fable", given the setup but NOT this file or its
# conclusion) returned verdict (b) with its own expressions.  Every one is checked here.
say("[S9] reconciling against the independent blind adjudicator ...")
ns = 1 + s
adj = {
 'T':            sp.Rational(5, 4)*eps/(3 - eps)*(1 + (ns - 4)*mu**2),
 'T_monopole':   5*eps*(ns - 1)/(12*(3 - eps)),
 'f_inin':       sp.Rational(5, 12)*(eps**2*mu**2 - eps**2 + 6*eps - 12 - eps*(ns - 1)*mu**2),
 'f_map_fin':    -sp.Rational(5, 4)*eps*(1 - mu**2),
 'f_map_init':   sp.Rational(5, 4)*eps/(3 - eps)*((eps - 2) - (eps - ns + 1)*mu**2),
 'f_map_init_monopole': 5*eps*(2*eps - 7 + ns)/(12*(3 - eps)),
 'f_dN_fin':     5*(eps*(ns - 4)*mu**2 - 3*eps + 12)/(4*(eps - 3)),
}
f_dN_fin_here = sp.simplify(f_inin_s/lam + f_fin_s)
pairs = [('T', T_s), ('T_monopole', mono(T_s)), ('f_inin', f_inin_s), ('f_map_fin', f_fin_s),
         ('f_map_init', f_init_s), ('f_map_init_monopole', mono(f_init_s)), ('f_dN_fin', f_dN_fin_here)]
for k, here in pairs:
    assert sp.simplify(sp.expand(here - adj[k])) == 0, (k, sp.simplify(here - adj[k]))
    say(f"      {k:22s} agrees")
# the two statements the adjudicator caught that this lane had not flagged as printable defects
assert sp.simplify(mono(f_init_s).subs(s, 0) + 5*eps/6) == 0                  # "both monopole -5 eps/6" is n_s=1-only
assert sp.simplify(mono(f_init_s) - (-5*eps/6)) != 0
assert sp.simplify(f_inin_s.subs(s, 0) - f_inin0) == 0                        # printed in-in shape is n_s=1-only
say("      CONFIRMED extra printable defects: f_map^init monopole is -5eps/6 only at n_s=1;")
say("      the printed f^in-in shape is the n_s=1 shape.  f_deltaN^fin is NOT -5 at general n_s.")
OUT['S9_adjudicator_reconciliation'] = {'independent_model': 'fable (blind: not shown this file or its conclusion)',
    'verdict_both': '(b) nonzero n_s-dependent correction to T; composed -5 survives exactly',
    'expressions_checked': [k for k, _ in pairs], 'all_agree': True,
    'f_map_init_monopole_general': str(sp.factor(mono(f_init_s))),
    'f_dN_fin_general': str(sp.factor(f_dN_fin_here)),
    'disagreement': 'none on the physics; the only difference was which mode n_s labels (S6), reconciled there'}
OUT['wall_clock_s'] = round(time.time() - T0, 1)
json.dump(OUT, open(os.path.abspath(__file__).replace('.py', '.json'), 'w'), indent=2)
say("done", OUT['wall_clock_s'], "s")

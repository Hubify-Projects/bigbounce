#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
psu_gate_S9b_intrinsic_term_2026_09_05.py

Gate S9b: does the intrinsic flat-slice initial-data non-Gaussianity omitted by the
lab's delta-N lane (fnl_matter_contraction_second_method_2026_09_02.py) supply the
gap  5(6-eps)/24 = 15/16 (dust)  between  f^{deltaN} = 5(eps-7)/8 = -55/16  and the
threaded in-in uniform-density value  f^rho = 5(2 eps-15)/24 = -5/2 ?

Method: the lane's exact second-order patch solution is rebuilt from the same ODE;
then ARBITRARY intrinsic NG of the flat-slice data (u_i = u_g + r u_g^2,
delta s_i = s_g + c_s s_g^2) is pushed through the delta-N map in closed form
(general constant epsilon, finite growth W = e^{alpha Sigma}).  The result is what
any in-in flat-gauge three-point function would contribute, as a function of the
number r it produces.  No steering: the closed form decides.
"""
import json, hashlib, sys, os
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {}

def show(label, expr):
    print(f"  {label:<48} = {expr}")

# ---------------------------------------------------------------------------
# Step 1 : rebuild the lane's closed forms (same parametrisation, same ODE)
# ---------------------------------------------------------------------------
print("=== Step 1: lane closed forms (epsilon = 3/(1+q^2), alpha = q^2) ===")
s  = sp.Symbol('sigma', nonnegative=True)
Sg = sp.Symbol('Sigma', positive=True)
ui = sp.Symbol('u_i')
ep = sp.Symbol('epsilon', positive=True)
q  = sp.Symbol('q', positive=True)
ep_q = 3 / (1 + q**2)
q_of_ep = sp.sqrt(3 / ep - 1)
xs = sp.sqrt(ep_q / 3)                       # x* ; epsilon = 3 x*^2
u  = sp.Symbol('u')
x  = sp.Symbol('x'); lam = sp.Symbol('lambda')
dxdN = (1 - x**2) * (sp.sqrt(6) * lam / 2 - 3 * x)
duds = sp.simplify(sp.expand(sp.simplify((dxdN * (-1 / (3 * x**2))).subs(lam, sp.sqrt(6) * xs).subs(x, xs + u))))
ser = sp.expand(sp.series(duds, u, 0, 3).removeO())
alpha = sp.simplify(ser.coeff(u, 1)); beta = sp.simplify(-ser.coeff(u, 2) / alpha)
assert sp.simplify(alpha - q**2) == 0
integ = sp.expand(sp.series(-1 / (3 * (xs + u)**2) + 1 / (3 * xs**2), u, 0, 3).removeO())
P = sp.simplify(integ.coeff(u, 1)); Q = sp.simplify(integ.coeff(u, 2))
g = sp.Function('g')
g_sol = sp.simplify(sp.dsolve(sp.Eq(sp.Derivative(g(s), s), alpha * g(s) - alpha * beta * sp.exp(2 * alpha * s)),
                              g(s), ics={g(0): 0}).rhs)
u_of_s = ui * sp.exp(alpha * s) + ui**2 * g_sol
zint = sp.expand(sp.series(sp.expand(P * u_of_s + Q * u_of_s**2), ui, 0, 3).removeO())
N_u  = sp.simplify(sp.integrate(zint.coeff(ui, 1), (s, 0, Sg)))      # zeta_1 / u_i
N_uu2 = sp.simplify(sp.integrate(zint.coeff(ui, 2), (s, 0, Sg)))     # zeta_2 / u_i^2 = N_uu/2
W = sp.Symbol('W', positive=True)                                    # W = e^{alpha Sigma}
N_u_W  = sp.simplify(N_u.subs(sp.exp(q**2 * Sg), W))
N_uu2_W = sp.simplify(N_uu2.subs(sp.exp(2 * q**2 * Sg), W**2).subs(sp.exp(q**2 * Sg), W))
show("N_u  = zeta_1/u_i   [q, W]", sp.factor(N_u_W))
show("N_uu/2 = zeta_2/u_i^2 [q, W]", sp.factor(N_uu2_W))
ratio_inf = sp.simplify(sp.limit(N_uu2 / N_u**2, Sg, sp.oo))
f_lane = sp.nsimplify(sp.simplify((sp.Rational(5, 3) * ratio_inf).subs(q, q_of_ep)))
show("lane f_NL (Gaussian data, W->oo) [epsilon]", f_lane)
assert sp.simplify(f_lane - sp.Rational(5, 8) * (ep - 7)) == 0
OUT['step1'] = {'N_u': str(N_u_W), 'N_uu_over_2': str(N_uu2_W), 'f_lane_general_eps': str(f_lane),
                'P': str(sp.simplify(P.subs(q, q_of_ep))), 'alpha': str(sp.simplify(alpha.subs(q, q_of_ep))),
                'beta': str(sp.simplify(beta.subs(q, q_of_ep)))}
print("  lane value -55/16 at dust reproduced:", f_lane.subs(ep, sp.Rational(3, 2)))

# ---------------------------------------------------------------------------
# Step 2 : arbitrary intrinsic NG of the flat-slice data, pushed through delta N
#   N(u_i, s_i) = -(s_f - s_i)/eps + N_u(Sigma) u_i + (N_uu/2)(Sigma) u_i^2,  Sigma = s_f - s_i
#   flat-slice data:  u_i = u_g + r u_g^2 ,  delta s_i = s_g + c_s s_g^2 ,  s_g = kappa_s u_g
#   (any in-in three-point function of the flat-gauge field/momentum at t_i enters
#    ONLY through the three numbers r, c_s, kappa_s: it fixes them, nothing else.)
# ---------------------------------------------------------------------------
print("=== Step 2: intrinsic contribution in closed form (finite W) ===")
r, cs, ks, ug, ds = sp.symbols('r c_s kappa_s u_g delta_s')
Sig = sp.Symbol('Sigma_bar', positive=True)
epsq = ep_q
Nfun = -(Sig - ds) / epsq + N_u.subs(Sg, Sig - ds) * ui + N_uu2.subs(Sg, Sig - ds) * ui**2
Nfun = Nfun.subs({ui: ug + r * ug**2, ds: ks * ug + cs * ks**2 * ug**2})
lamb = sp.Symbol('t')
Nser = sp.expand(sp.series(Nfun.subs(ug, lamb * ug), lamb, 0, 3).removeO())
zeta1 = sp.simplify(Nser.coeff(lamb, 1)); zeta2 = sp.simplify(Nser.coeff(lamb, 2))
zeta1 = zeta1.subs(sp.exp(q**2 * Sig), W); zeta2 = sp.simplify(zeta2.subs(sp.exp(2 * q**2 * Sig), W**2).subs(sp.exp(q**2 * Sig), W))
ratio = sp.simplify(zeta2 / zeta1**2)
ratio_G = sp.simplify(ratio.subs({r: 0, cs: 0, ks: 0}))
intrinsic = sp.simplify(ratio - ratio_G)          # everything that depends on (r, c_s, kappa_s)
f_int = sp.Rational(5, 3) * intrinsic
show("zeta_2/zeta_1^2, Gaussian data, finite W [q,W]", sp.factor(ratio_G))
show("intrinsic piece of f_NL (r,c_s,kappa_s; q,W)", sp.factor(sp.simplify(f_int.subs(ks, 0))))
# leading large-W behaviour of each intrinsic channel
f_int_r = sp.simplify(f_int.subs({cs: 0, ks: 0}))
f_int_r_eps = sp.simplify(f_int_r.subs(q, q_of_ep))
show("r-channel:  f_int(r) [epsilon, W]", sp.factor(f_int_r_eps))
lead_r = sp.simplify(sp.limit(f_int_r_eps * W, W, sp.oo))
show("r-channel:  lim W*f_int(r)  (=> f_int ~ this / W)", sp.factor(lead_r))
f_int_s = sp.simplify(sp.limit(sp.simplify((f_int - f_int_r) * W), W, sp.oo).subs(q, q_of_ep))
show("s-channels (c_s, kappa_s): lim W*(rest)", f_int_s)
assert sp.simplify(sp.limit(f_int.subs(q, q_of_ep).subs(ep, sp.Rational(3, 2)), W, sp.oo)) == 0
print("  W->oo: every intrinsic channel -> 0  (asserted at eps=3/2; general form above)")
# what r would have to be to close the gap 5(6-eps)/24
gap = sp.Rational(5, 24) * (6 - ep)
r_req = sp.simplify(sp.solve(sp.Eq(f_int_r_eps, gap), r)[0])
show("r required to close the gap [epsilon, W]", sp.factor(r_req))
show("r required at eps=3/2", sp.factor(r_req.subs(ep, sp.Rational(3, 2))))
OUT['step2'] = {'ratio_gaussian_finiteW': str(ratio_G), 'f_intrinsic_r_channel': str(f_int_r_eps),
                'W_times_f_intrinsic_r_limit': str(lead_r), 'W_times_f_intrinsic_s_channels_limit': str(f_int_s),
                'r_required_general': str(r_req), 'r_required_dust': str(r_req.subs(ep, sp.Rational(3, 2))),
                'gap_general': str(gap), 'gap_dust': str(gap.subs(ep, sp.Rational(3, 2)))}

# ---------------------------------------------------------------------------
# Step 3 : the (delta phi, delta pi) chain.  Flat-slice local data (M=1):
#   3 H_loc^2 = pi^2/2 + V(phi),  V = Vbar e^{-lam dphi}, lam = sqrt6 x*,
#   x_loc = pi/(sqrt6 H_loc), s_loc = ln|H_loc|;  u_i = x_loc - x*,  ds_i = s_loc - sbar.
#   N_phi, N_pi, N_phiphi, N_pipi, N_phipi by composition; intrinsic data
#   dphi = dphi_g + r_phi dphi_g^2, dpi = varpi dphi_g + r_pi dphi_g^2 (varpi = growing-mode ratio).
# ---------------------------------------------------------------------------
print("=== Step 3: (delta phi, delta pi) chain rule and where the in-in enters ===")
dphi, dpi, rphi, rpi, varpi = sp.symbols('delta_phi delta_pi r_phi r_pi varpi')
Hbar = -1                                   # contracting, |H|=1 at t_i (s_bar = 0)
pibar = sp.sqrt(6) * xs * Hbar              # x* = pibar/(sqrt6 Hbar) > 0
Vbar = 3 - pibar**2 / 2
lam_v = sp.sqrt(6) * xs
Hloc = -sp.sqrt((( pibar + dpi)**2 / 2 + Vbar * sp.exp(-lam_v * dphi)) / 3)
u_loc = (pibar + dpi) / (sp.sqrt(6) * Hloc) - xs
s_loc = sp.log(-Hloc)
Nphi_pi = (-(Sig - s_loc) / epsq + N_u.subs(Sg, Sig - s_loc) * u_loc + N_uu2.subs(Sg, Sig - s_loc) * u_loc**2)
def d(e, *vs):
    return sp.simplify(sp.diff(e, *vs).subs({dphi: 0, dpi: 0}).subs(sp.exp(q**2 * Sig), W))
N_phi, N_pi = d(Nphi_pi, dphi), d(Nphi_pi, dpi)
N_phiphi, N_pipi, N_phipi = d(Nphi_pi, dphi, dphi), d(Nphi_pi, dpi, dpi), d(Nphi_pi, dphi, dpi)
for k, v in [('N_phi', N_phi), ('N_pi', N_pi), ('N_phiphi', N_phiphi), ('N_pipi', N_pipi), ('N_phipi', N_phipi)]:
    show(k + "  [q, W]", sp.factor(v))
# the flat-slice Jacobian: u_phi, u_pi, s_phi, s_pi
u_phi, u_pi = d(u_loc, dphi), d(u_loc, dpi); s_phi, s_pi = d(s_loc, dphi), d(s_loc, dpi)
show("u_phi, u_pi", (sp.simplify(u_phi), sp.simplify(u_pi))); show("s_phi, s_pi", (sp.simplify(s_phi), sp.simplify(s_pi)))
assert sp.simplify(N_phi - (N_u_W * u_phi + s_phi / epsq)) == 0 and sp.simplify(N_pi - (N_u_W * u_pi + s_pi / epsq)) == 0
# intrinsic contribution with a single Gaussian seed dphi_g and growing-mode ratio varpi
z1 = N_phi + varpi * N_pi
z2 = sp.Rational(1, 2) * (N_phiphi + 2 * varpi * N_phipi + varpi**2 * N_pipi) + N_phi * rphi + N_pi * rpi
f_tot = sp.Rational(5, 3) * z2 / z1**2
f_intr_chain = sp.simplify(sp.Rational(5, 3) * (N_phi * rphi + N_pi * rpi) / z1**2)
show("intrinsic f (chain) [q,W]", sp.factor(f_intr_chain))
# leading large-W: numerator ~ W, denominator ~ W^2  -> 1/W, for every varpi with u_phi + varpi u_pi != 0
lead_chain = sp.simplify(sp.limit(f_intr_chain * W, W, sp.oo))
show("lim W * f_intrinsic(chain)", sp.factor(lead_chain))
assert sp.simplify(sp.limit(f_intr_chain.subs({rphi: 1, rpi: 1, varpi: 1, q: 1}), W, sp.oo)) == 0
# consistency: the Gaussian part of the chain reproduces the lane's -55/16 at dust for any varpi
fG_chain = sp.simplify(sp.limit((f_tot - f_intr_chain).subs(q, q_of_ep).subs(ep, sp.Rational(3, 2)), W, sp.oo))
show("Gaussian part of chain, W->oo, eps=3/2 (any varpi)", fG_chain)
assert sp.simplify(fG_chain + sp.Rational(55, 16)) == 0
OUT['step3'] = {k: str(v) for k, v in [('N_phi', N_phi), ('N_pi', N_pi), ('N_phiphi', N_phiphi), ('N_pipi', N_pipi),
                ('N_phipi', N_phipi), ('u_phi', u_phi), ('u_pi', u_pi), ('s_phi', s_phi), ('s_pi', s_pi),
                ('f_intrinsic_chain', f_intr_chain), ('W_times_f_intrinsic_chain_limit', lead_chain),
                ('gaussian_part_dust_Winf', fG_chain)]}

# ---------------------------------------------------------------------------
# Step 4 : validations of the machinery
#  (a) USR (NFS 2013): N(phi,pi) = -(1/3) ln(1 - 3H(phi_e - phi)/pi);  Gaussian dphi, dpi=0
#      => zeta_2/zeta_1^2 = 3/2, f_NL = 5/2; the intrinsic term enters with weight 1/N_phi ~ e^{-3N}.
#  (b) attractor / no-growth: the lane map at W -> 0 (decaying u) gives a finite intrinsic weight.
#  (c) mpmath: exact nonlinear patch ODE with NON-Gaussian data u_i = u_g + r u_g^2 reproduces
#      the closed-form intrinsic shift  5 r alpha /(3 P (W-1)).
# ---------------------------------------------------------------------------
print("=== Step 4: validations ===")
phi, pi_, phie, H0, N0, rU = sp.symbols('phi pi phi_e H_0 N_0 r_U')
N_usr = -sp.Rational(1, 3) * sp.log(1 - 3 * H0 * (phie - phi) / pi_)
Nphi_usr = sp.diff(N_usr, phi); Nphiphi_usr = sp.diff(N_usr, phi, 2); Npi_usr = sp.diff(N_usr, pi_); Npipi_usr = sp.diff(N_usr, pi_, 2)
# evaluate on the trajectory where the remaining USR duration is N_0:  1 - 3H(phi_e-phi)/pi = e^{-3 N_0}
sub_usr = {phie: phi + pi_ * (1 - sp.exp(-3 * N0)) / (3 * H0)}
ratio_usr = sp.simplify((Nphiphi_usr / (2 * Nphi_usr**2)).subs(sub_usr))
f_usr = sp.simplify(sp.Rational(5, 3) * ratio_usr)
show("USR: zeta_2/zeta_1^2 from N(phi,pi), dpi=0", ratio_usr); show("USR: f_NL", f_usr)
assert f_usr == sp.Rational(5, 2)
w_usr = sp.simplify(sp.Rational(5, 3) * (1 / Nphi_usr).subs(sub_usr))     # weight of an intrinsic r_phi
show("USR: intrinsic weight (5/3)/N_phi", w_usr)
print("     -> intrinsic weight ~ e^{-3 N_0}: NFS's vanishing intrinsic term is doubly safe in USR;")
print("        N_pi-terms: N_pi =", sp.simplify(Npi_usr.subs(sub_usr)), " (dpi=0 for the constant flat-gauge mode)")
OUT['step4_usr'] = {'f_usr': str(f_usr), 'intrinsic_weight': str(w_usr), 'N_pi': str(sp.simplify(Npi_usr.subs(sub_usr)))}
# (b) attractor / decaying direction: W -> 0
w_att = sp.simplify(sp.limit(f_int_r_eps / r, W, 0))
show("attractor (W->0): intrinsic weight df/dr", w_att)
print("     finite, O(1): with no growth the initial-data NG passes through undiluted (Maldacena-type term).")
OUT['step4_attractor'] = {'intrinsic_weight_W0': str(w_att)}
# (c) mpmath on the exact nonlinear ODE at dust with non-Gaussian initial data
mp.mp.dps = 40
xs_n = mp.sqrt(mp.mpf(1) / 2); A_n = 1 - xs_n**2
def rhs(_s, yv):
    uu, _ = yv
    return [uu * (A_n - 2 * xs_n * uu - uu**2) / (xs_n + uu)**2, -1 / (3 * (xs_n + uu)**2) + 1 / (3 * xs_n**2)]
def zeta_of(u0, SIG):
    sol = mp.odefun(rhs, 0, [u0, mp.mpf(0)], tol=mp.mpf(10)**(-36))
    return sol(SIG)[1]
def fnl_numeric(r_num, SIG, ug=mp.mpf('1e-7')):
    zp = zeta_of(ug + r_num * ug**2, SIG); zm = zeta_of(-ug + r_num * ug**2, SIG)
    z1 = (zp - zm) / 2; z2 = (zp + zm) / 2
    return mp.mpf(5) / 3 * z2 / z1**2
SIG_n = mp.mpf(6); W_n = mp.e**SIG_n
P_n = 2 / (3 * xs_n**3); alpha_n = mp.mpf(1)
res_c = {}
for r_num in [mp.mpf(0), mp.mpf(3), mp.mpf(-3)]:
    f_num = fnl_numeric(r_num, SIG_n)
    f_pred = fnl_numeric(mp.mpf(0), SIG_n) + mp.mpf(5) * r_num * alpha_n / (3 * P_n * (W_n - 1))
    print(f"     r = {mp.nstr(r_num,3):>4}:  numeric f_NL = {mp.nstr(f_num, 12)}   closed-form = {mp.nstr(f_pred, 12)}"
          f"   |diff| = {mp.nstr(abs(f_num - f_pred), 3)}")
    res_c[str(int(r_num))] = {'numeric': float(f_num), 'closed_form': float(f_pred), 'absdiff': float(abs(f_num - f_pred))}
    assert abs(f_num - f_pred) < mp.mpf('1e-6')
OUT['step4_mpmath'] = {'Sigma': 6, 'W': float(W_n), 'runs': res_c}

# ---------------------------------------------------------------------------
# Verdict block (computed, not typed): can  -55/16 + intrinsic = -5/2  hold?
# ---------------------------------------------------------------------------
print("=== Verdict ===")
f_int_dust = sp.simplify(f_int_r_eps.subs(ep, sp.Rational(3, 2)))
show("intrinsic term at dust, r-channel [r, W]", f_int_dust)
show("intrinsic term at dust, W -> oo", sp.limit(f_int_dust, W, sp.oo))
show("gap to close (S9.5)", gap.subs(ep, sp.Rational(3, 2)))
closes = sp.simplify(sp.limit(f_int_dust, W, sp.oo) - gap.subs(ep, sp.Rational(3, 2))) == 0
print("  -55/16 + intrinsic(W->oo) == -5/2 ?", closes)
verdict = "RECONCILED" if closes else "NOT"
OUT['verdict'] = {
    'verdict': verdict,
    'intrinsic_general_eps_finiteW': str(f_int_r_eps),
    'intrinsic_general_eps_Winf': '0',
    'intrinsic_dust_finiteW': str(f_int_dust),
    'intrinsic_dust_Winf': '0',
    'residual_general_eps': str(gap), 'residual_dust': str(gap.subs(ep, sp.Rational(3, 2))),
    'r_that_would_be_needed_dust': str(r_req.subs(ep, sp.Rational(3, 2))),
    'step_where_residual_arises': ("the super-Hubble evolution between the flat slice at t_i and the uniform-density "
                                   "slice at t_f (the separate-universe map itself), not the initial data: any "
                                   "t_f-independent intrinsic bispectrum of the flat-slice field/momentum enters f_NL "
                                   "with weight O(1/W) and vanishes in the growing-mode-dominated limit that defines "
                                   "the lane's number"),
}
out_path = os.path.join(HERE, 'psu_gate_S9b_intrinsic_term_2026_09_05.json')
OUT['script_sha256'] = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()
OUT['sympy_version'] = sp.__version__
json.dump(OUT, open(out_path, 'w'), indent=1, sort_keys=True)
print("  wrote", out_path, " verdict:", verdict)

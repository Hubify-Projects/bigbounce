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

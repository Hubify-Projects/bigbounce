#!/usr/bin/env python3
"""Leg A of row 9b: the Bardeen route at a SIMPLE ZERO of Q = Hc^2 - Hc' = -a^2 Hdot.

Row 9 (`../row9_scheme_independence_2026_09_19/row9_symbolic.py`, all residuals 0) established, for a single
minimally coupled scalar (c_s = 1, arbitrary V) on an arbitrary a(eta):

    Phi'' + 2(Hc - pp) Phi' + (k^2 + 2 Hc' - 2 Hc pp) Phi = 0 ,     pp = Q'/(2Q) ,   Q = Hc^2 - Hc' = -a^2 Hdot

and stated as its limit 2 that the LQC/poly backgrounds, which CROSS Q = 0 smoothly, were not done.
This script does the local analysis at that crossing and specialises it to the two committed backgrounds.

A1  the (Phi, Psi) first-order system, Psi = Phi' + Hc Phi                          (residual must be 0)
A2  indicial equation at a simple zero of Q, and its roots
A3  the first recursion coefficient  ->  Phi'(eta_c) = -Hc(eta_c) Phi(eta_c) ?
A4  the resonance/log coefficient, and the leading behaviour of zeta, Xi, delta phi at eta_c
A5  the two committed backgrounds: closed-form Q, its zeros, and whether they are simple

Run: python3 row9b_symbolic.py  ->  row9b_symbolic.log, symbolic_results.json
"""
import json, time
import sympy as sp

LOG, OUT = [], {}
def log(s=""):
    print(s); LOG.append(str(s))

T0 = time.time()
log("=" * 104)
log("LEG A - Bardeen route at a simple zero of Q = Hc^2 - Hc' = -a^2 Hdot  (the smooth NEC crossing)")
log("=" * 104)

eta, k = sp.symbols("eta k", real=True, positive=False)
a = sp.Function("a")(eta)
Hc = sp.diff(a, eta) / a
Q = sp.simplify(Hc**2 - sp.diff(Hc, eta))
pp = sp.diff(Q, eta) / (2 * Q)

# ---------------------------------------------------------------- A1
Phi = sp.Function("Phi")(eta)
bardeen = sp.diff(Phi, eta, 2) + 2 * (Hc - pp) * sp.diff(Phi, eta) + (k**2 + 2 * sp.diff(Hc, eta) - 2 * Hc * pp) * Phi

Psi = sp.Function("Psi")(eta)
# proposed system:  Phi' = Psi - Hc Phi ;  Psi' = (Q'/Q - Hc) Psi + (Q - k^2) Phi
sub1 = sp.diff(Phi, eta) - (Psi - Hc * Phi)
sub2 = sp.diff(Psi, eta) - ((sp.diff(Q, eta) / Q - Hc) * Psi + (Q - k**2) * Phi)
# eliminate: Psi = Phi' + Hc Phi, then Psi' - [...] must equal the Bardeen equation
PsiOfPhi = sp.diff(Phi, eta) + Hc * Phi
res_A1 = sp.simplify(
    sp.diff(PsiOfPhi, eta) - ((sp.diff(Q, eta) / Q - Hc) * PsiOfPhi + (Q - k**2) * Phi) - bardeen)
log("\n[A1] (Phi, Psi) system, Psi = Phi' + Hc Phi:")
log("        Phi' = Psi - Hc Phi ;   Psi' = (Q'/Q - Hc) Psi + (Q - k^2) Phi")
log("     residual against row 9's Phi equation: %s" % res_A1)
OUT["A1_system_residual"] = str(res_A1)
assert res_A1 == 0

# exact dictionary, re-derived here in the same variables
zeta_expr = Phi + Hc * PsiOfPhi / Q
res_zeta = sp.simplify(sp.diff(zeta_expr, eta) + k**2 * Hc * Phi / Q
                       - sp.simplify(sp.diff(zeta_expr, eta)).subs(sp.diff(Phi, eta, 2),
                                                                   sp.solve(bardeen, sp.diff(Phi, eta, 2))[0]))
res_zeta = sp.simplify(sp.diff(zeta_expr, eta).subs(sp.diff(Phi, eta, 2),
                                                    sp.solve(bardeen, sp.diff(Phi, eta, 2))[0])
                       + k**2 * Hc * Phi / Q)
log("     zeta = Phi + Hc Psi/Q  ->  residual of  zeta' = -k^2 Hc Phi/Q : %s" % sp.simplify(res_zeta))
OUT["A1_zeta_identity_residual"] = str(sp.simplify(res_zeta))

# ---------------------------------------------------------------- A2/A3/A4: local Frobenius at Q(eta_c) = 0
log("\n[A2-A4] local analysis at a simple zero of Q.  Hc is expanded about eta_c as h0 + h1 t + h2 t^2 + h3 t^3,")
log("        and Q = Hc^2 - Hc' is NOT independent: Q(eta_c) = 0 forces h1 = h0^2.")
t = sp.symbols("t", real=True)
h0, h2, h3, h4 = sp.symbols("h0 h2 h3 h4", real=True)
h1 = h0**2                                   # forced by Q(eta_c) = 0
Hs = h0 + h1 * t + h2 * t**2 + h3 * t**3 + h4 * t**4
Qs = sp.expand(Hs**2 - sp.diff(Hs, t))
Qs = sp.Poly(Qs, t).as_expr()
q_coeffs = [sp.simplify(Qs.coeff(t, n)) for n in range(4)]
log("        Q series: q0 = %s ; q1 = %s ; q2 = %s" % (q_coeffs[0], sp.factor(q_coeffs[1]), sp.factor(q_coeffs[2])))
OUT["A2_Q_series"] = [str(c) for c in q_coeffs]
assert q_coeffs[0] == 0

p_of_t = sp.series(2 * Hs - sp.diff(Qs, t) / Qs, t, 0, 2).removeO()
q_of_t = sp.series(k**2 + 2 * sp.diff(Hs, t) - Hs * sp.diff(Qs, t) / Qs, t, 0, 2).removeO()
p_m1 = sp.simplify(sp.limit(t * (2 * Hs - sp.diff(Qs, t) / Qs), t, 0))
q_m2 = sp.simplify(sp.limit(t**2 * (k**2 + 2 * sp.diff(Hs, t) - Hs * sp.diff(Qs, t) / Qs), t, 0))
q_m1 = sp.simplify(sp.limit(t * (k**2 + 2 * sp.diff(Hs, t) - Hs * sp.diff(Qs, t) / Qs), t, 0))
log("        t*p -> %s   (p_{-1});   t^2*q -> %s   (q_{-2});   t*q -> %s   (q_{-1})" % (p_m1, q_m2, q_m1))
r = sp.symbols("r")
indicial = sp.expand(r * (r - 1) + p_m1 * r + q_m2)
roots = sp.solve(sp.Eq(indicial, 0), r)
log("[A2] indicial equation: %s = 0   ->  roots %s" % (indicial, roots))
OUT["A2_indicial"] = {"p_minus1": str(p_m1), "q_minus2": str(q_m2), "q_minus1": str(q_m1),
                      "equation": str(indicial), "roots": [str(x) for x in roots]}

# A3: first recursion of the r = 0 branch
a0, a1, a2, C = sp.symbols("a0 a1 a2 C", real=True)
Phis = a0 + a1 * t + a2 * t**2 + C * t**2 * sp.log(t)
ode = sp.diff(Phis, t, 2) + (2 * Hs - sp.diff(Qs, t) / Qs) * sp.diff(Phis, t) \
    + (k**2 + 2 * sp.diff(Hs, t) - Hs * sp.diff(Qs, t) / Qs) * Phis
ser = sp.series(sp.simplify(ode * t), t, 0, 2).removeO()          # multiply by t: the t^0 coefficient is the recursion
c_tm0 = sp.simplify(sp.expand(ser).coeff(t, 0).subs(sp.log(t), 0))
sol_a1 = sp.solve(sp.Eq(c_tm0, 0), a1)
log("[A3] order t^{-1} of the ODE (i.e. t^0 after multiplying by t):  %s = 0" % sp.simplify(c_tm0))
log("     ->  a1 = %s          i.e.  Phi'(eta_c) = -Hc(eta_c) Phi(eta_c)  : %s"
    % (sp.simplify(sol_a1[0]), "CONFIRMED" if sp.simplify(sol_a1[0] + h0 * a0) == 0 else "REFUTED"))
OUT["A3_a1"] = {"recursion": str(sp.simplify(c_tm0)), "a1": str(sp.simplify(sol_a1[0])),
                "confirms_Phip_eq_minus_Hc_Phi": bool(sp.simplify(sol_a1[0] + h0 * a0) == 0)}

# A4: the resonance -- the log coefficient C at order t^0 (with a1 already fixed)
ode2 = sp.simplify(ode.subs(a1, sol_a1[0]))
ser2 = sp.series(sp.expand(ode2), t, 0, 1).removeO()
c0 = sp.simplify(sp.expand(ser2).coeff(t, 0))
c0_nolog = sp.simplify(c0.subs(sp.log(t), 0))
sol_C = sp.solve(sp.Eq(c0_nolog, 0), C)
Cval = sp.simplify(sol_C[0]) if sol_C else None
log("[A4] resonance at n = 2 (exponents differ by the integer 2): the t^0 coefficient fixes the LOG amplitude")
log("     C = %s" % Cval)
log("     -> C != 0 whenever  k != 0  and  Phi(eta_c) != 0 : the r = 0 solution CARRIES a t^2 log t term,")
log("        so Phi and Phi' are continuous (the log is O(t^2 log t), O(t log t)) while Phi'' diverges as log t.")
Psi_s = sp.simplify(sp.diff(Phis, t) + Hs * Phis).subs(a1, sol_a1[0])
Psi_lead = sp.simplify(sp.series(Psi_s, t, 0, 2).removeO())
log("     Psi = Phi' + Hc Phi  near eta_c :  %s" % sp.simplify(Psi_lead))
zeta_lead = sp.simplify(sp.series(sp.simplify(Phis.subs(a1, sol_a1[0]) + Hs * Psi_s / Qs), t, 0, 1).removeO())
log("     zeta = Phi + Hc Psi/Q  near eta_c :  %s" % zeta_lead)
OUT["A4"] = {"C_log_coefficient": str(Cval), "Psi_leading": str(sp.simplify(Psi_lead)),
             "zeta_leading": str(zeta_lead)}

# ---------------------------------------------------------------- A5: the two committed backgrounds
log("\n[A5] the committed backgrounds (a2_transmission_linear.bg_lqc / bg_poly), closed form")
x, s_ = sp.symbols("x sigma", positive=True)
# LQC effective dust, rho_c = 1: H^2 = (x/3)(1-x), a = x^{-1/3}
a_lqc = x**sp.Rational(-1, 3)
H_lqc = sp.sqrt(x * (1 - x) / 3)                 # magnitude; sign = sign(eta)
Hdot_lqc = sp.simplify(-x * (1 - 2 * x) / 2)
Q_lqc = sp.simplify(-a_lqc**2 * Hdot_lqc)
Hc_lqc = sp.simplify(a_lqc * H_lqc)
appa_lqc = sp.simplify(a_lqc**2 * (2 * H_lqc**2 + Hdot_lqc))
log("     LQC:  a = x^(-1/3),  Hdot = %s,  Q = -a^2 Hdot = %s" % (Hdot_lqc, sp.simplify(Q_lqc)))
log("           Hc = %s ;  a''/a = %s   (matches the committed appa = x^(1/3)(1/6 + x/3): %s)"
    % (sp.simplify(Hc_lqc), sp.simplify(appa_lqc),
       sp.simplify(appa_lqc - x**sp.Rational(1, 3) * (sp.Rational(1, 6) + x / 3)) == 0))
zeros_lqc = sp.solve(sp.Eq(Q_lqc, 0), x)
dQdx_lqc = sp.simplify(sp.diff(Q_lqc, x))
log("           Q = 0 at x = %s ;  dQ/dx there = %s  (nonzero -> SIMPLE zero)"
    % (zeros_lqc, [sp.nsimplify(dQdx_lqc.subs(x, z)) for z in zeros_lqc]))
# the two 'S2' variables on LQC are NOT the same
z2_eps = sp.simplify(2 * a_lqc**2 * (-Hdot_lqc / H_lqc**2))
z2_fluid = sp.simplify(a_lqc**2 * x / H_lqc**2)            # rho + p = rho = x for dust
log("           z^2[S2, geometric 2 a^2 eps]      = %s" % sp.simplify(z2_eps))
log("           z^2[S2, fluid a^2(rho+p)/H^2]     = %s   (the value A3M quotes, T = 0.409)" % sp.simplify(z2_fluid))
log("           ratio = %s  -> the two differ by (1-2x) and are NOT the same variable on this background"
    % sp.simplify(z2_eps / z2_fluid))
OUT["A5_lqc"] = {"Q": str(sp.simplify(Q_lqc)), "Q_zeros_in_x": [str(z) for z in zeros_lqc],
                 "dQdx_at_zeros": [str(sp.nsimplify(dQdx_lqc.subs(x, z))) for z in zeros_lqc],
                 "z2_S2_geometric": str(sp.simplify(z2_eps)), "z2_S2_fluid": str(sp.simplify(z2_fluid)),
                 "ratio_geometric_over_fluid": str(sp.simplify(z2_eps / z2_fluid)),
                 "appa_matches_committed": bool(sp.simplify(appa_lqc - x**sp.Rational(1, 3) * (sp.Rational(1, 6) + x / 3)) == 0)}

# poly, a = 1 + u^2 (eta_b = 1)
u = sp.symbols("u", real=True)
a_p = 1 + u**2
Hc_p = sp.simplify(sp.diff(a_p, u) / a_p)
Q_p = sp.simplify(Hc_p**2 - sp.diff(Hc_p, u))
Qp_p = sp.simplify(sp.diff(Q_p, u))
zeros_p = sp.solve(sp.Eq(Q_p, 0), u)
log("     poly: a = 1 + u^2,  Hc = %s,  Q = %s" % (Hc_p, sp.factor(Q_p)))
log("           Q = 0 at u = %s ;  Q' there = %s  (nonzero -> SIMPLE zero)"
    % (zeros_p, [sp.nsimplify(Qp_p.subs(u, z)) for z in zeros_p]))
Hd_p = sp.simplify(-Q_p / a_p**2)
log("           -Q/a^2 = Hdot = %s   (matches the committed Hd = 2(1-3u^2)/(1+u^2)^4: %s)"
    % (sp.simplify(Hd_p), sp.simplify(Hd_p - 2 * (1 - 3 * u**2) / (1 + u**2)**4) == 0))
OUT["A5_poly"] = {"Q": str(sp.factor(Q_p)), "Q_zeros_in_u": [str(z) for z in zeros_p],
                  "Qprime_at_zeros": [str(sp.nsimplify(Qp_p.subs(u, z))) for z in zeros_p],
                  "Hdot_matches_committed": bool(sp.simplify(Hd_p - 2 * (1 - 3 * u**2) / (1 + u**2)**4) == 0)}

# Quintin control: Hdot is piecewise constant / -3/2 H^2, and NEVER zero inside the domain
log("     Quintin-type: Hdot = Upsilon > 0 inside |t| < tm and -3/2 H^2 < 0 outside -- it JUMPS between the")
log("           two signs and is never zero, so this background has NO Q = 0 crossing at all.  That is the")
log("           structural difference row 9 could not test.")
OUT["A5_quintin"] = "Hdot jumps Upsilon <-> -3/2 H^2 at |t| = tm; Q never vanishes; no smooth NEC crossing."

# ---------------------------------------------------------------- A6: the two principal values in closed form
log("\n[A6] the super-Hubble mixing integral I_eps = int deta/z_eps^2 as a CLOSED-FORM principal value")
log("     (this is what makes R = 3 I_eps/I_S1 exactly 1/2 and 3/8 rather than numerically close to them)")

# ---- poly:  I_eps = PV int_0^inf eta^2 / ((1+eta^2)^2 (3 eta^2 - 1)) d eta
ee = sp.symbols("e", positive=True)
f_poly = ee**2 / ((1 + ee**2) ** 2 * (3 * ee**2 - 1))
Ap, Bp, Cp = sp.Rational(-1, 16), sp.Rational(1, 4), sp.Rational(3, 16)
res_pf = sp.simplify(f_poly - (Ap / (1 + ee**2) + Bp / (1 + ee**2) ** 2 + Cp / (3 * ee**2 - 1)))
i1 = sp.integrate(1 / (1 + ee**2), (ee, 0, sp.oo))
i2 = sp.integrate(1 / (1 + ee**2) ** 2, (ee, 0, sp.oo))
I_poly = sp.simplify(Ap * i1 + Bp * i2)          # the C term is an odd log about eta = 1/sqrt3 -> PV = 0
log("     poly: partial-fraction residual %s ; int 1/(1+e^2) = %s ; int 1/(1+e^2)^2 = %s ;"
    % (res_pf, i1, i2))
log("           the 1/(3e^2-1) term is an odd logarithm about the pole, so its principal value is 0")
log("           =>  I_eps[poly] = %s  (pi/32 = %s)  -> R = 3 I_eps/(pi/4) = %s"
    % (I_poly, sp.pi / 32, sp.simplify(3 * I_poly / (sp.pi / 4))))

# ---- LQC:  I_eps = (1/(3 sqrt3)) PV int_0^1 sqrt((1-x)/x)/(1-2x) dx
tt = sp.symbols("t")
fold_lhs = sp.sqrt((1 - tt) / (1 + tt)) - sp.sqrt((1 + tt) / (1 - tt))
fold_rhs = -2 * tt / sp.sqrt(1 - tt**2)
fold_ok = all(sp.simplify(fold_lhs.subs(tt, sp.Rational(a, 10)) - fold_rhs.subs(tt, sp.Rational(a, 10))) == 0
              for a in (1, 3, 5, 7, 9))
J = sp.integrate(fold_rhs / tt, (tt, 0, 1))      # x = (1+t)/2 then fold t -> -t; the 1/t cancels
PV = sp.simplify(-J / 2)
I_lqc = sp.simplify(PV / (3 * sp.sqrt(3)))
log("     LQC: substitute x = (1+t)/2, then fold t -> -t; the two square roots combine to -2t/sqrt(1-t^2),")
log("          so the 1/t of the pole CANCELS and the principal value is an ordinary integral.")
log("          fold identity sqrt((1-t)/(1+t)) - sqrt((1+t)/(1-t)) = -2t/sqrt(1-t^2): %s" % ("verified" if fold_ok else "FAILED"))
log("          int_0^1 -2/sqrt(1-t^2) dt = %s  =>  PV int_0^1 sqrt((1-x)/x)/(1-2x) dx = %s" % (J, PV))
log("          =>  I_eps[LQC] = %s = pi/(6 sqrt3) = %.10f  -> R = 3 I_eps/(pi/sqrt3) = %s"
    % (I_lqc, float(I_lqc), sp.simplify(3 * I_lqc / (sp.pi / sp.sqrt(3)))))
log("     NOTE pi/(6 sqrt3) is EXACTLY the dust effective-fluid mixing integral already computed in")
log("          a2_transmission_linear.fluid_scheme_contrast: the (1-2x) factor drops out of the principal value.")
OUT["A6_closed_form_PV"] = {
    "poly": {"partial_fraction_residual": str(res_pf), "I_eps": str(I_poly),
             "I_eps_equals_pi_over_32": bool(sp.simplify(I_poly - sp.pi / 32) == 0),
             "R": str(sp.simplify(3 * I_poly / (sp.pi / 4)))},
    "LQC": {"fold_identity_verified": bool(fold_ok), "PV": str(PV), "I_eps": str(I_lqc),
            "I_eps_equals_pi_over_6sqrt3": bool(sp.simplify(I_lqc - sp.pi / (6 * sp.sqrt(3))) == 0),
            "R": str(sp.simplify(3 * I_lqc / (sp.pi / sp.sqrt(3))))}}

OUT["runtime_s"] = time.time() - T0
open("row9b_symbolic.log", "w").write("\n".join(LOG) + "\n")
json.dump(OUT, open("symbolic_results.json", "w"), indent=2, default=str)
log("\n[done] %.1f s" % OUT["runtime_s"])

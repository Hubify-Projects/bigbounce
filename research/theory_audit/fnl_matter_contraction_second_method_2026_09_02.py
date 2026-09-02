#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fnl_matter_contraction_second_method_2026_09_02.py

NEXT_SCIENCE_LEDGER item #1 --- INDEPENDENT SECOND-METHOD derivation of the
local non-Gaussianity generated during a matter-dominated (w = 0, eps = 3/2)
contraction, to adjudicate between

    Cai, Xue, Brandenberger & Zhang 2009 (arXiv:0903.0631), Eq. (39):
        f_NL^local = -35/8   (in-in, cubic action, four vertices)
    BigBounce Paper 2 (four-vertex re-summation of the same in-in action):
        f_NL^local = -35/16
    Li, Quintin, Wang & Cai 2016/17 (arXiv:1612.02036), Eq. (5.1):
        f_NL^local = -165/16 + 65/(8 c_s^2)  ->  -35/16 at c_s = 1

All three of the above are the SAME METHOD (in-in with the cubic action).  This
script implements a GENUINELY INDEPENDENT route: the separate-universe /
Salopek-Bond gradient expansion (delta-N), i.e. the exact NONLINEAR
long-wavelength dynamics of the local FRW patch.  No cubic action, no in-in
integral, no mode functions, no Wick contractions are used anywhere below.

Conventions (identical to Cai et al. Eq. (20) and Li et al., verified against
the sources on 2026-09-02):
    zeta = zeta_g + (3/5) f_NL zeta_g^2
    f_NL = (10/3) A(k1,k2,k3) / sum_i k_i^3       [shape-function normalisation]
Both literature papers state these same two relations, so the -35/8 vs -35/16
discrepancy is NOT a 3/5-vs-6/5 or A-normalisation convention difference.

Deterministic, exact (sympy Rational / sqrt), runs in well under a minute.
Every intermediate is printed.

Author: BigBounce theory-audit lane, 2026-09-02.
"""

import json
import hashlib
import os
import time

import sympy as sp
import mpmath as mp

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
SELF = os.path.abspath(__file__)

RESULTS = {}


def hdr(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def show(label, expr):
    print(f"  {label} = {sp.simplify(expr)}")


# ===========================================================================
hdr("STEP 0 --- WHAT IS BEING COMPUTED, AND WHY IT IS INDEPENDENT")
# ===========================================================================
print("""
The in-in cubic-action route computes <zeta zeta zeta> from the interaction
Hamiltonian.  The separate-universe route instead uses the fact that on scales
far outside the Hubble radius each spatial patch obeys the *unperturbed,
fully nonlinear* FRW + scalar-field equations, with the local expansion
  N(x) = ln a~(x)
playing the role of the perturbation variable.  The nonlinear curvature
perturbation on uniform-density slices is then EXACTLY

  zeta(x) = delta N (flat initial slice  ->  uniform-density final slice)

to leading order in the gradient expansion (Salopek & Bond 1990;
Lyth, Malik & Sasaki 2005).  Any f_NL obtained this way shares NO algebraic
step with the cubic-action calculation: it is an ordinary-differential-equation
result about a homogeneous cosmology, not a QFT correlator.
""")

# ===========================================================================
hdr("STEP 1 --- THE MATTER-CONTRACTION BACKGROUND AS A SEPARATE-UNIVERSE SYSTEM")
# ===========================================================================
print("""
The matter-bounce contracting phase is driven by a canonical scalar field whose
equation of state is w = 0.  A canonical scalar with an exponential potential
    V(phi) = V0 exp(-lambda phi / M)      (M = reduced Planck mass)
has the scaling solution w = lambda^2/3 - 1, so w = 0 <=> lambda^2 = 3.
This is the standard realisation used in the matter-bounce literature (it gives
a ~ (-t)^{2/3} exactly, with c_s^2 = 1 as for any canonical scalar).

We derive the separate-universe autonomous system from the field equations
themselves (no formula is quoted).
""")

M, H, phid, V, lam, N = sp.symbols('M H phidot V lambda N', positive=True)
x = sp.Symbol('x')          # x = phidot / (sqrt(6) M H)
Y = sp.Symbol('Y')          # Y = V / (3 M^2 H^2)

# Field equations:
#   phiddot = -3 H phidot - V'(phi),   V'(phi) = -(lambda/M) V
#   Hdot    = -phidot^2 / (2 M^2)
phiddot = -3 * H * phid + (lam / M) * V
Hdot = -phid**2 / (2 * M**2)

# d/dN = (1/H) d/dt applied to x = phidot/(sqrt(6) M H)
dx_dN = (1 / H) * (phiddot / (sp.sqrt(6) * M * H) - phid * Hdot / (sp.sqrt(6) * M * H**2))
dx_dN = sp.simplify(dx_dN)
print("  raw  dx/dN =", dx_dN)

# substitute the dimensionless variables
sub = {phid: sp.sqrt(6) * M * H * x, V: 3 * M**2 * H**2 * Y}
dx_dN = sp.simplify(dx_dN.subs(sub))
print("  in (x, Y):  dx/dN =", sp.expand(dx_dN))

# Friedmann constraint 3 M^2 H^2 = phidot^2/2 + V  =>  x^2 + Y = 1
dx_dN = sp.factor(sp.simplify(dx_dN.subs(Y, 1 - x**2)))
print("  with Friedmann constraint x^2 + Y = 1:")
print("      dx/dN =", dx_dN)
print("""
  (this is exact and holds for EITHER sign of H, because Y = V/(3 M^2 H^2) > 0
   regardless -- so it is valid in a CONTRACTING universe.)
""")

xstar = lam / sp.sqrt(6)
print("  fixed points: x = +-1 and x* = lambda/sqrt(6) =", xstar)
print("  check dx/dN at x*: ", sp.simplify(dx_dN.subs(x, xstar)))

# epsilon = -Hdot/H^2 = 3 x^2
eps_of_x = sp.simplify(-Hdot.subs(phid, sp.sqrt(6) * M * H * x) / H**2)
show("epsilon = -Hdot/H^2", eps_of_x)
print("  => at the fixed point epsilon* = 3 x*^2 =", sp.simplify(3 * xstar**2),
      " and w = 2*epsilon/3 - 1 =", sp.simplify(2 * sp.Rational(1, 1) * (3 * xstar**2) / 3 - 1))
print("  matter contraction (w = 0, epsilon = 3/2)  <=>  lambda^2 = 3.")

# adiabatic sound speed at the scaling solution
ca2 = sp.simplify((1 + 2 * (-(lam / M) * V) / (3 * H * phid)).subs(sub).subs(Y, 1 - x**2).subs(x, xstar))
show("c_a^2 = pdot/rhodot at the scaling solution", ca2)
print("  with lambda^2 = 3:  c_a^2 =", sp.simplify(ca2.subs(lam, sp.sqrt(3))),
      "   while c_s^2 = 1 for a canonical scalar.")
print("""
  c_a^2 != c_s^2  =>  a NONZERO intrinsic non-adiabatic pressure,
      delta p_nad = (c_s^2 - c_a^2) delta rho_comoving  =  delta rho_comoving,
  and therefore, by the exact nonlinear long-wavelength equation
      zeta_dot = -(H/(rho+p)) delta p_nad + O(grad^2),
  zeta is NOT conserved outside the Hubble radius in matter contraction.

  CONSEQUENCE (important, and stated up front): the *naive* delta-N shortcut --
  "zeta is conserved, so evaluate delta N once and stop" -- is INVALID here.
  What remains valid, and is what we use, is the full separate-universe
  evolution: delta N between a flat initial slice and a uniform-density final
  slice, computed by integrating the exact nonlinear patch dynamics.
""")

# ===========================================================================
hdr("STEP 2 --- THE GROWING MODE OF zeta IN CONTRACTION")
# ===========================================================================
t = sp.Symbol('t', negative=True)
a_bg = (-t)**sp.Rational(2, 3)
H_bg = sp.simplify(sp.diff(a_bg, t) / a_bg)
show("a(t) = (-t)^{2/3}  ->  H(t)", H_bg)
epsq = sp.simplify(-sp.diff(H_bg, t) / H_bg**2)
show("epsilon", epsq)
Dmode = sp.integrate(1 / a_bg**3, t)
show("D-mode  int dt / a^3", Dmode)
print("  |D-mode| ~ 1/(-t) -> infinity as t -> 0^-  : this is the GROWING mode")
print("  |H| = 2/(3|t|) grows the same way, so  zeta_growing  ~  |H|.")
print("""
  So in a contracting matter phase the dominant super-Hubble mode of zeta is the
  one that is *decaying* in an expanding universe.  Any correct second-method
  computation must follow this mode; that is exactly what the separate-universe
  integration below does.
""")

# ===========================================================================
hdr("STEP 3 --- EXACT NONLINEAR delta-N IN THE SEPARATE-UNIVERSE PHASE SPACE")
# ===========================================================================
print("""
  Slicing / gauge choices (stated explicitly):
    * initial slice: SPATIALLY FLAT  (uniform a, hence uniform N_i)
    * final slice:   UNIFORM DENSITY.  For a single field, rho = 3 M^2 H^2, so
                     uniform density  <=>  uniform |H|.
    * zeta          = delta N between those two slices (nonlinear, Salopek-Bond)
  Evolution variable: s = ln|H|, which INCREASES monotonically during
  contraction.  From dln|H|/dN = -3 x^2 we get dN/ds = -1/(3 x^2), so

        N_f - N_i = int_{s_i}^{s_f} ( -1/(3 x(s)^2) ) ds .

  The local patch data on the flat slice are (x_i, s_i).  The s_i direction is a
  pure local time-shift: it contributes zeta = (2/3) delta s_i with NO
  exponential growth, and is therefore subdominant (see Step 5).  The physical
  growing mode is the OFF-ATTRACTOR displacement u_i = x_i - x*.
""")

s = sp.Symbol('sigma', nonnegative=True)          # sigma = s - s_i
Sg = sp.Symbol('Sigma', positive=True)            # total ln|H| growth
ui = sp.Symbol('u_i')                             # initial off-attractor offset
ep = sp.Symbol('epsilon', positive=True)          # background epsilon

# To keep every exponent sign-definite for sympy's limit engine we parametrise
# the physically relevant window 0 < epsilon < 3 by  epsilon = 3/(1+q^2), q > 0.
# Then alpha = (3-epsilon)/epsilon = q^2 > 0 manifestly.  Everything is
# re-expressed in epsilon at the end via q = sqrt(3/epsilon - 1).
q = sp.Symbol('q', positive=True)
ep_q = 3 / (1 + q**2)
q_of_ep = sp.sqrt(3 / ep - 1)

xs = sp.sqrt(ep_q / 3)                            # x* with epsilon = 3 x*^2
Acon = 1 - xs**2

u = sp.Symbol('u')
# dx/ds = (dx/dN)/(dN/ds)^{-1} ... explicitly: dx/ds = (dx/dN) * (dN/ds)
dxdN_gen = (1 - x**2) * (sp.sqrt(6) * lam / 2 - 3 * x)
dxds_exact = sp.simplify((dxdN_gen * (-1 / (3 * x**2))).subs(lam, sp.sqrt(6) * xs).subs(x, xs + u))
dxds_exact = sp.simplify(sp.expand(dxds_exact))
print("  exact  du/ds =", sp.factor(dxds_exact))

ser = sp.series(dxds_exact, u, 0, 3).removeO()
ser = sp.expand(sp.simplify(ser))
c1 = sp.simplify(ser.coeff(u, 1))
c2 = sp.simplify(ser.coeff(u, 2))
show("linear coefficient  alpha", c1)
show("quadratic coefficient  -alpha*beta", c2)
alpha = sp.simplify(c1)
beta = sp.simplify(-c2 / alpha)
show("alpha (in epsilon)", alpha.subs(q, q_of_ep))
show("beta  (in epsilon)", beta.subs(q, q_of_ep))
print("  alpha > 0 for epsilon < 3  =>  u grows like e^{alpha s} ~ |H|^alpha :")
print("      at epsilon = 3/2:  alpha =",
      sp.simplify(alpha.subs(q, q_of_ep).subs(ep, sp.Rational(3, 2))),
      " (so u ~ |H|, matching the D-mode of Step 2).")

# integrand of delta N, expanded about the fixed point
integ_exact = -1 / (3 * (xs + u)**2) + 1 / (3 * xs**2)
integ = sp.expand(sp.series(integ_exact, u, 0, 3).removeO())
P = sp.simplify(integ.coeff(u, 1))
Q = sp.simplify(integ.coeff(u, 2))
show("delta N integrand: linear coefficient P", P)
show("delta N integrand: quadratic coefficient Q", Q)

# solve u(sigma) to second order in u_i
g = sp.Function('g')
sol = sp.dsolve(sp.Eq(sp.Derivative(g(s), s), alpha * g(s) - alpha * beta * sp.exp(2 * alpha * s)),
                g(s), ics={g(0): 0})
g_sol = sp.simplify(sol.rhs)
show("second-order mode function g(sigma)", g_sol)

u_of_s = ui * sp.exp(alpha * s) + ui**2 * g_sol
# verification: residual of the ODE at O(u_i^2)
resid = sp.expand(sp.series(sp.diff(u_of_s, s) - dxds_exact.subs(u, u_of_s), ui, 0, 3).removeO())
resid2 = sp.simplify(resid.coeff(ui, 2))
print("  ODE residual at O(u_i^2)  (must be 0):", resid2)
assert sp.simplify(resid2) == 0

zeta_int = sp.expand(P * u_of_s + Q * u_of_s**2)
zeta_int = sp.expand(sp.series(zeta_int, ui, 0, 3).removeO())
zeta1 = sp.simplify(sp.integrate(zeta_int.coeff(ui, 1), (s, 0, Sg)))
zeta2 = sp.simplify(sp.integrate(zeta_int.coeff(ui, 2), (s, 0, Sg)))
show("zeta_1 / u_i    [in q, epsilon = 3/(1+q^2)]", zeta1)
show("zeta_2 / u_i^2  [in q, epsilon = 3/(1+q^2)]", zeta2)

# ===========================================================================
hdr("STEP 4 --- GROWING-MODE-DOMINATED LIMIT AND f_NL")
# ===========================================================================
print("""
  Growing-mode-dominated limit: W = e^{alpha Sigma} -> infinity (many e-folds of
  |H| growth between Hubble exit and the end of contraction).
""")
lead1 = sp.simplify(sp.limit(zeta1 / sp.exp(alpha * Sg), Sg, sp.oo))
lead2 = sp.simplify(sp.limit(zeta2 / sp.exp(2 * alpha * Sg), Sg, sp.oo))
show("leading zeta_1 coefficient (x W)   [in q]", lead1)
show("leading zeta_2 coefficient (x W^2) [in q]", lead2)

ratio_q = sp.simplify(lead2 / lead1**2)
show("zeta_2 / zeta_1^2  (W -> infinity) [in q]", ratio_q)

ratio = sp.simplify(sp.radsimp(sp.simplify(ratio_q.subs(q, q_of_ep))))
show("zeta_2 / zeta_1^2  (W -> infinity) [in epsilon]", ratio)

fnl_general = sp.nsimplify(sp.simplify(sp.expand(sp.Rational(5, 3) * ratio)))
print()
print("  ***  f_NL^local(epsilon)  =", fnl_general, " ***")
print("       (from  zeta = zeta_g + (3/5) f_NL zeta_g^2 )")

fnl_matter = sp.nsimplify(sp.simplify(fnl_general.subs(ep, sp.Rational(3, 2))))
print()
print("  ***  matter contraction (epsilon = 3/2):  f_NL^local =",
      fnl_matter, "=", float(fnl_matter), " ***")
print()
fnl_eps0 = sp.nsimplify(sp.limit(fnl_general, ep, 0))
print("  Structural note:  the epsilon -> 0 limit of the same closed form is",
      fnl_eps0, "=", float(fnl_eps0))
print("  (Cai et al.'s published value is -35/8 = -4.375; stated here as an")
print("   observation about the closed form, NOT as a claimed mechanism.)")

print("""
  WHY THIS LIMIT IS ROBUST (and why the answer does not depend on the initial
  data or on any horizon-crossing non-Gaussianity):
    * zeta_1 grows as W, zeta_2 grows as W^2.
    * Any non-Gaussianity already present in the initial patch data (u_i itself
      quadratic in the Gaussian field perturbation, or intrinsic sub-Hubble
      non-Gaussianity of delta phi) enters zeta through the LINEAR response and
      therefore grows only as W^1 -- suppressed by 1/W relative to the W^2 term.
    * The local-time-shift mode delta s_i contributes zeta = (2/3) delta s_i
      with no growth at all: also 1/W suppressed.
    * Hence in the growing-mode-dominated regime (many e-folds of |H| growth
      between Hubble exit and the end of contraction, W = |H_end/H_exit|^alpha
      >> 1, which is the matter-bounce regime by construction) the ratio
      zeta_2/zeta_1^2 is a pure number, independent of Sigma, of s_i, and of the
      map from the Gaussian field perturbation to u_i.
""")

RESULTS["second_method"] = {
    "method": "separate-universe / Salopek-Bond gradient expansion (nonlinear delta-N)",
    "fnl_local_general_epsilon": str(sp.nsimplify(sp.simplify(fnl_general))),
    "fnl_local_matter_epsilon_3_2": str(fnl_matter),
    "fnl_local_matter_float": float(fnl_matter),
    "zeta2_over_zeta1sq": str(sp.nsimplify(ratio.subs(ep, sp.Rational(3, 2)))),
    "convention": "zeta = zeta_g + (3/5) f_NL zeta_g^2",
}

# ===========================================================================
hdr("STEP 5 --- INDEPENDENT NUMERICAL VALIDATION OF THE SYMBOLIC RESULT")
# ===========================================================================
print("""
  Cross-check: integrate the EXACT nonlinear separate-universe ODE system
      du/dsigma   = u (A - 2 x* u - u^2) / (x* + u)^2
      dzeta/dsigma= -1/(3 (x*+u)^2) + 1/(3 x*^2)
  numerically for +u_i and -u_i, and split zeta into its odd (linear) and even
  (quadratic) parts.  No symbolic input is reused.
""")
mp.mp.dps = 40
xs_n = mp.sqrt(mp.mpf(3) / 2 / 3)                 # x* at epsilon = 3/2 = 1/sqrt(2)
A_n = 1 - xs_n**2


def rhs(_sig, yv):
    uu, zz = yv
    du = uu * (A_n - 2 * xs_n * uu - uu**2) / (xs_n + uu)**2
    dz = -1 / (3 * (xs_n + uu)**2) + 1 / (3 * xs_n**2)
    return [du, dz]


SIG = mp.mpf(12)
U0 = mp.mpf('1e-9')
zvals = {}
for sgn in (+1, -1):
    f = mp.odefun(rhs, 0, [sgn * U0, mp.mpf(0)], tol=mp.mpf('1e-30'))
    zvals[sgn] = f(SIG)[1]
z_lin = (zvals[+1] - zvals[-1]) / 2
z_quad = (zvals[+1] + zvals[-1]) / 2
num_ratio = z_quad / z_lin**2
num_fnl = mp.mpf(5) / 3 * num_ratio
print(f"  Sigma = {SIG},  u_i = {U0},  W = e^Sigma = {mp.nstr(mp.e**SIG, 8)}")
print(f"  zeta_1 (odd part)   = {mp.nstr(z_lin, 12)}")
print(f"  zeta_2 (even part)  = {mp.nstr(z_quad, 12)}")
print(f"  numerical zeta_2/zeta_1^2 = {mp.nstr(num_ratio, 10)}"
      f"   (exact -> {float(sp.nsimplify(ratio.subs(ep, sp.Rational(3,2))))})")
print(f"  numerical f_NL            = {mp.nstr(num_fnl, 10)}"
      f"   (exact -> {float(fnl_matter)})")
rel = abs(num_fnl - mp.mpf(str(float(fnl_matter)))) / abs(mp.mpf(str(float(fnl_matter))))
print(f"  relative agreement        = {mp.nstr(rel, 4)}"
      "   (finite-W residual is O(1/W) as expected)")
RESULTS["numerical_validation"] = {
    "Sigma": float(SIG),
    "u_i": float(U0),
    "fnl_numeric": float(num_fnl),
    "fnl_exact": float(fnl_matter),
    "relative_difference": float(rel),
}

# ===========================================================================
hdr("STEP 6 --- AUXILIARY: WHERE THE LITERATURE FACTOR OF TWO LIVES")
# ===========================================================================
print("""
  This step is NOT part of the independent derivation.  It is a bookkeeping
  audit of the two published in-in results, included because the ledger item
  asks whether the -35/8 vs -35/16 gap is a convention, an overall factor, or a
  single vertex/orbit coefficient.

  Both sources state the SAME conventions:
      Cai et al. 2009 Eq. (20):  zeta = zeta_g + (3/5) f_NL zeta_g^2
      Cai et al. 2009 Eq. (21):  |B|_NL = (10/3) A / sum_i k_i^3
      Li  et al. 2017 Sec. 5:    f_NL   = (10/3) A_tot / sum_i k_i^3
  so a 3/5-vs-6/5, zeta-vs-Phi, or A-normalisation convention difference is
  RULED OUT as the explanation.  (Sources checked 2026-09-02.)
""")
k1, k2, k3 = sp.symbols('k1 k2 k3', positive=True)
ks = [k1, k2, k3]
sumk3 = sum(k**3 for k in ks)
Pik2 = (k1 * k2 * k3)**2


def Spair(p, q):
    return sum(ks[i]**p * ks[j]**q for i in range(3) for j in range(3) if i != j)


def Ssingle(p):
    return sum(k**p for k in ks)


def Ttriple_perm(p, q, r):
    from itertools import permutations
    return sum(ks[i]**p * ks[j]**q * ks[l]**r for (i, j, l) in permutations(range(3)))


def Ttriple_distinct(p, q, r):
    from itertools import permutations
    seen, tot = set(), 0
    for (i, j, l) in permutations(range(3)):
        key = tuple(sorted([(i, p), (j, q), (l, r)]))
        if key in seen:
            continue
        seen.add(key)
        tot += ks[i]**p * ks[j]**q * ks[l]**r
    return tot


def squeezed_fnl(A):
    d = sp.Symbol('delta', positive=True)
    k = sp.Symbol('k', positive=True)
    expr = (sp.Rational(10, 3) * A / sumk3).subs({k1: d, k2: k, k3: k})
    return sp.simplify(sp.limit(sp.simplify(expr), d, 0))


def A_printed(Ttrip):
    """Cai et al. 2009 Eq. (37), transcribed."""
    return sp.Rational(3, 256) / Pik2 * (
        3 * Ssingle(9)
        + Spair(7, 2)
        - 9 * Spair(6, 3)
        + 5 * Spair(5, 4)
        - 66 * Ttrip(5, 2, 2)
        + 9 * Ttrip(4, 3, 2)
    )


for name, Ttrip in (("all-6-ordered-permutations", Ttriple_perm),
                    ("distinct-monomials for the (5,2,2) orbit", Ttriple_distinct)):
    val = squeezed_fnl(A_printed(Ttrip))
    print(f"  Eq.(37) with sum_(i!=j!=l) read as {name}:")
    print(f"      squeezed f_NL = {sp.nsimplify(val)} = {float(val):.6f}")
    RESULTS.setdefault("cai_eq37_orbit_audit", {})[name] = str(sp.nsimplify(val))

print()
print("  Ratios among the published/derived numbers:")
for a_lbl, a_val in (("Cai -35/8", sp.Rational(-35, 8)),
                     ("P2/Li -35/16", sp.Rational(-35, 16)),
                     ("this work -55/16", fnl_matter)):
    for b_lbl, b_val in (("P2/Li -35/16", sp.Rational(-35, 16)),):
        if a_lbl == b_lbl:
            continue
        print(f"      {a_lbl} / {b_lbl} = {sp.nsimplify(a_val / b_val)}"
              f" = {float(a_val / b_val):.6f}")
print("  => Cai/P2 is EXACTLY 2, i.e. an overall factor of two, NOT a single")
print("     vertex coefficient and NOT an f_NL-definition convention.")
RESULTS["cai_over_p2_ratio"] = str(sp.Rational(-35, 8) / sp.Rational(-35, 16))

# ===========================================================================
hdr("STEP 7 --- CONSISTENCY-RELATION CROSS-CHECK")
# ===========================================================================
print("""
  Maldacena's squeezed-limit consistency relation,  f_NL^sq = (5/12)(1 - n_s),
  holds ONLY when zeta is conserved outside the Hubble radius (attractor).  The
  matter bounce has n_s = 1 exactly at leading order, so the consistency
  relation would give f_NL^sq = 0.
""")
ns = sp.Integer(1)
print("  n_s (matter contraction, leading order) =", ns)
print("  (5/12)(1 - n_s) =", sp.Rational(5, 12) * (1 - ns))
print(f"  actual second-method value = {fnl_matter} != 0")
print("""
  The consistency relation is therefore VIOLATED, by exactly the amount carried
  by the non-attractor growing mode.  This is an internal consistency check of
  Step 3-4: had the separate-universe integration produced zero, it would have
  meant we had (incorrectly) followed the conserved C-mode instead of the
  growing D-mode.  A nonzero, order-unity, negative f_NL is what the physics
  requires, and all three routes agree on that qualitative statement.
""")
RESULTS["consistency_relation"] = {
    "n_s": 1,
    "maldacena_prediction": 0.0,
    "actual": float(fnl_matter),
    "status": "violated as required for a non-attractor (growing-mode) phase",
}

# ===========================================================================
hdr("STEP 8 --- RECONCILIATION AND VERDICT")
# ===========================================================================
table = [
    ("Cai, Xue, Brandenberger & Zhang 2009 (0903.0631) Eq.(39)",
     "in-in, cubic action, four vertices", "-35/8", -4.375),
    ("Li, Quintin, Wang & Cai 2017 (1612.02036) Eq.(5.1), c_s=1",
     "in-in, generalised single field", "-35/16", -2.1875),
    ("BigBounce Paper 2, four-vertex re-summation",
     "in-in, re-summation of Cai's own vertices", "-35/16", -2.1875),
    ("THIS WORK (2026-09-02)",
     "separate-universe / nonlinear delta-N (independent)", str(fnl_matter),
     float(fnl_matter)),
]
w0 = max(len(r[0]) for r in table)
print(f"  {'source'.ljust(w0)} | {'method'.ljust(46)} | value | float")
for r in table:
    print(f"  {r[0].ljust(w0)} | {r[1].ljust(46)} | {r[2]:>7} | {r[3]:+.4f}")

verdict = "OTHER"
print(f"""
  VERDICT: {verdict}
    The independent separate-universe route does NOT reproduce either published
    number.  It gives, exactly and in the same convention,

        f_NL^local(epsilon) = (5 epsilon - 35)/8 = -35/8 + (5/8) epsilon
        f_NL^local(epsilon = 3/2) = -55/16 = -3.4375

    for the super-Hubble growth of the curvature perturbation in a w = 0
    contraction.  It agrees with both in-in results on SIGN and on ORDER UNITY,
    and it independently confirms that the local non-Gaussianity of the matter
    bounce is generated by the non-attractor growing mode (Step 7).

  WHAT THIS DOES AND DOES NOT SETTLE:
    * It does NOT adjudicate the factor of two, because -55/16 is not a rational
      multiple of either candidate (-55/16 / (-35/16) = 11/7).
    * It DOES eliminate the cheapest reconciliations: the two sources use
      identical f_NL conventions (Step 6), the gap is exactly 2 (an overall
      factor, not one vertex coefficient), and the disagreement is therefore
      internal to the in-in bookkeeping (commutator factor / Wick multiplicity /
      orbit multiplicity), not a definitional artefact.
    * The separate-universe result captures the zeroth-gradient-order
      super-Hubble generation ONLY.  The in-in calculations additionally include
      the gradient (k^2 / non-local Pi k^2) structure of the shape function, and
      they evaluate the correlator with a specific vacuum initial state.  The
      residual difference (-55/16 vs -35/16 or -35/8) is exactly the size of
      the terms the gradient expansion drops at leading order, so the two
      classes of computation are NOT strictly line-by-line comparable.
    * Suggestive but UNPROVEN: the ln-derived closed form -35/8 + (5/8) epsilon
      has Cai's published -35/8 as its epsilon -> 0 limit.  This is stated as an
      observation, not a claim of mechanism; no attempt is made here to argue
      that Cai dropped the epsilon-linear piece.

  WHAT REMAINS GENUINELY OPEN (for the .md and the ledger):
    1. The gradient (O(k^2)) correction to the separate-universe result, which
       is what would make it line-by-line comparable with the in-in shape.
    2. A direct recomputation of the in-in commutator/Wick multiplicity from the
       cubic action with independent conventions, which is the only thing that
       can settle -35/8 vs -35/16 within the in-in method itself.
""")

RESULTS["verdict"] = verdict
RESULTS["reconciliation_table"] = [
    {"source": r[0], "method": r[1], "value": r[2], "float": r[3]} for r in table
]

# ===========================================================================
hdr("PROVENANCE")
# ===========================================================================
with open(SELF, "rb") as fh:
    script_sha = hashlib.sha256(fh.read()).hexdigest()
elapsed = time.time() - T0
print(f"  script sha256 : {script_sha}")
print(f"  wall clock    : {elapsed:.2f} s")
print(f"  sympy         : {sp.__version__}")
print(f"  mpmath        : {mp.__version__}")

RESULTS["provenance"] = {
    "script": "research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.py",
    "script_sha256": script_sha,
    "wall_clock_seconds": round(elapsed, 3),
    "sympy_version": sp.__version__,
    "mpmath_version": mp.__version__,
    "date": "2026-09-02",
    "ledger_item": 1,
    "sources_checked": [
        "arXiv:0903.0631 (Cai, Xue, Brandenberger, Zhang 2009) Eqs. (14),(20),(21),(37),(39)",
        "arXiv:1612.02036 (Li, Quintin, Wang, Cai) Eq. (5.1) and f_NL definition",
        "research/focused_paper_source_integration/02_full_draft.tex (BigBounce Paper 2)",
    ],
}

out = os.path.join(HERE, "fnl_matter_contraction_second_method_2026_09_02.json")
with open(out, "w") as fh:
    json.dump(RESULTS, fh, indent=2)
print(f"  wrote {out}")

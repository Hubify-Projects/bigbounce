#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fnl_matter_contraction_adjudication_2026_09_02.py

ADJUDICATION of the local f_NL generated during a canonical matter-dominated contraction
(w = 0, eps = 3/2, c_s = 1).  Three routes disagree in the record:

    Cai, Xue, Brandenberger & Zhang 2009 (arXiv:0903.0631), in-in, Eq. (39):      f_NL^local = -35/8
    BigBounce Paper 2 / Li, Quintin, Wang & Cai 2016 (1612.02036) Eq. (5.1), c_s=1: f_NL^local = -35/16
    lab second method 2026-09-02 (separate-universe / delta-N, uniform-density slices): f_NL = (5 eps-35)/8 = -55/16

This script is a FROM-SCRATCH in-in calculation (no per-vertex expression is transcribed from any
paper), validated against two independent literature benchmarks before it is applied, followed by an
exact delta-N calculation on BOTH slicings and an ADM computation of the long-mode shear that decides
why the separate-universe route cannot reproduce the in-in number.

Conventions (fixed once, used everywhere)
  * M_Pl = 1, c_s = 1, conformal time eta < 0, end of contraction eta_* = -S with |k eta_*| << 1.
  * Quadratic action S2 = int d eta d^3x  a^2 eps [ zeta'^2 - (d zeta)^2 ]   (Maldacena, comoving gauge).
  * zeta_k = u_k a_k + u_k^* a^dag_{-k}, Bunch-Davies u_k ~ e^{-ik eta}, Wronskian u u*' - u* u' = i/(2 a^2 eps).
  * Cubic action: Maldacena's comoving-gauge form (canonical field, eta_sr = 0), in conformal time with
    chi~ = d^{-2} zeta'  (Maldacena's chi = a eps chi~):
        L3 = a^2 (eps^2 - eps^3/2) zeta zeta'^2 + a^2 eps^2 zeta (d zeta)^2 - 2 a^2 eps^2 zeta' d zeta . d chi~
           + (a^2 eps^3/2) zeta (d_i d_j chi~)^2  + f(zeta) dL2/dzeta|_1
    The (eps/2a)(dzeta)(dchi)d^2chi + (eps/4a)(d^2 zeta)(dchi)^2 -> -(a^3 eps^3/2) zeta zdot^2 + (eps/2a) zeta (d_i d_j chi)^2
    rewriting is CHECKED here at the level of Fourier kernels (Sec. 2).
  * Field redefinition zeta = zeta_n + f(zeta_n),
        f = zeta zeta'/calH + (eps/2calH)[(dzeta)(dchi~) - d^-2 d_i d_j(d_i zeta d_j chi~)]
                            + (1/4calH^2)[-(dzeta)^2 + d^-2 d_i d_j(d_i zeta d_j zeta)]     (+ (eta_sr/4) zeta^2, = 0 here)
  * In-in at first order:  <zeta^3(eta_*)> = -i int d eta <[zeta^3(eta_*), H_int(eta)]>,  H_int = -L_int
                         = -2 Im int_{-inf(1-i0)}^{eta_*} d eta <zeta^3(eta_*) L_int(eta)>.
  * Wick: all 3! contractions of the external legs with the ordered monomial of each vertex, each counted once
    (no hand-inserted symmetry factors; the sum over S_3 is explicit).
  * Shape function and amplitude (Cai Eqs. 20-21 = Li Sec. 5):
        <zeta zeta zeta> = (2 pi)^7 delta^3(sum k) P_zeta^2 / prod k_i^3  A(k1,k2,k3),   f_NL = (10/3) A / sum_i k_i^3,
    equivalent to zeta = zeta_g + (3/5) f_NL zeta_g^2 for the local template.
  * All time integrals are done EXACTLY (recurrence down to E_1(iKS), Bunch-Davies contour) and then expanded
    in S; the leading Im part is S^-12, i.e. a pure number x P_zeta^2 (no end-time dependence; corrections O(k^2 S^2)).

Every intermediate is printed.  Deterministic (exact rationals).  See the .md for the derivation narrative.
Author: BigBounce theory-audit lane (Fable-tier adjudicator), 2026-09-02.
"""
import hashlib
import json
import os
import sys
import time
from itertools import permutations
import multiprocessing as mp

import sympy as sp

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
SELF = os.path.abspath(__file__)
RESULTS = {}

I = sp.I
eta = sp.Symbol('eta', negative=True)
S = sp.Symbol('S', positive=True)                # eta_* = -S
k1, k2, k3 = sp.symbols('k1 k2 k3', positive=True)
KS = [k1, k2, k3]
Ksum = k1 + k2 + k3
Lg = sp.Symbol('L', real=True)                   # L = log(K S): tracked; must not appear at leading order
gam = sp.EulerGamma
kk = sp.Symbol('k', positive=True)
mu = sp.Symbol('mu', real=True)
sumk3 = k1**3 + k2**3 + k3**3


def hdr(t):
    print()
    print("=" * 96)
    print(t)
    print("=" * 96)


def dot(p, q, r):
    """p.q for p+q+r = 0, in terms of magnitudes."""
    return (r**2 - p**2 - q**2) / 2


# =====================================================================================================
# 0.  EXACT IN-IN MACHINERY
# =====================================================================================================
_I_cache = {}


def I_n(n, K):
    """I_n = int_{-inf(1-i0)}^{-S} eta^{-n} e^{iK eta} d eta, exact.
    n>=2: I_n = e^{iK eta_*} eta_*^{1-n}/(1-n) + (iK/(n-1)) I_{n-1};   I_1 = -E_1(iKS);
    n<=0: antiderivative at eta_* (the -inf end is killed by the i0 rotation)."""
    key = (n, K)
    if key in _I_cache:
        return _I_cache[key]
    etas = -S
    if n <= 0:
        val = sp.integrate(eta**(-n) * sp.exp(I * K * eta), eta).subs(eta, etas)
    elif n == 1:
        val = -sp.Function('E1')(I * K * S)
    else:
        val = sp.exp(I * K * etas) * etas**(1 - n) / (1 - n) + (I * K / (n - 1)) * I_n(n - 1, K)
    _I_cache[key] = val
    return val


def E1_series(z, order):
    return -gam - sp.log(z) - sum((-z)**m / (m * sp.factorial(m)) for m in range(1, order + 1))


def expand_exact(expr, order, K):
    """E_1 -> series, log(iKS) -> L + i pi/2, every exp(.) node -> truncated series (robust to sympy splitting exp)."""
    E1 = sp.Function('E1')
    z = I * K * S
    expr = expr.replace(E1, lambda arg: E1_series(arg, order))
    expr = expr.subs(sp.log(z), Lg + I * sp.pi / 2)
    expr = expr.replace(sp.log, lambda arg: sp.expand_log(sp.log(arg), force=True))
    expr = expr.subs(sp.log(K * S), Lg).subs(sp.log(S), Lg - sp.log(K))
    expr = expr.replace(lambda e: e.func == sp.exp,
                        lambda e: sum(e.args[0]**m / sp.factorial(m) for m in range(order + 1)))
    expr = sp.expand(expr)
    assert not expr.has(sp.exp) and not expr.has(E1), "transcendental leftovers"
    return expr


def im_part(expr):
    conj = expr.subs(I, -I)
    return sp.expand((expr - conj) / (2 * I))


def wick_sum(vertex_V, alphas, W0, W1):
    """Sum over the 6 contractions of (k1,k2,k3) with the ordered monomial zeta^{(a1)}_p zeta^{(a2)}_q zeta^{(a3)}_r."""
    tot = 0
    for perm in permutations(range(3)):
        ks = [KS[i] for i in perm]
        V = vertex_V(*ks)
        prod = 1
        for a, kq in zip(alphas, ks):
            prod *= (W1 if a == 1 else W0)(kq)
        tot += V * prod
    return tot


def bispectrum_vertex(prefactor_eta, vertex_V, alphas, u, ubar, ubar_p, order):
    """B_v(k1,k2,k3;S) = -2 Im int d eta prefactor(eta) <zeta^3(eta_*) O_v(eta)>  (Laurent series in S)."""
    W0 = lambda kq: u(kq, -S) * ubar(kq, eta)
    W1 = lambda kq: u(kq, -S) * ubar_p(kq, eta)
    integrand = prefactor_eta * wick_sum(vertex_V, alphas, W0, W1)
    lau = sp.expand(sp.powsimp(sp.expand(integrand * sp.exp(-I * Ksum * eta) * sp.exp(-I * Ksum * S))))
    assert not lau.has(sp.exp), "integrand not of the form e^{iK eta} x Laurent(eta)"
    poly = sp.Poly(sp.expand(lau * eta**40), eta)
    total = 0
    for (m,), cf in poly.terms():
        total += cf * I_n(40 - m, Ksum)
    total = sp.exp(I * Ksum * S) * total
    total = expand_exact(total, order, Ksum)
    return sp.expand(-2 * im_part(total))


def laurent_in_S(expr, lo, hi):
    expr = sp.expand(expr)
    out = {}
    for p in range(lo, hi + 1):
        cf = sp.simplify(expr.coeff(S, p))
        if cf != 0:
            out[p] = cf
    return out


def make_background(case):
    """Return (a, eps, calH, u, ubar, ubar_p, N2, exponent) for the three backgrounds used."""
    Nn = sp.Symbol('N', positive=True)
    if case == 'dS':
        H, epsv = sp.symbols('H epsilon', positive=True)
        a = -1 / (H * eta)
        epsf = epsv
        u_gen = Nn * (1 + I * kk * eta) * sp.exp(-I * kk * eta)
    elif case == 'USR':
        H, es, etas = sp.symbols('H epsilon_s eta_s', positive=True)
        a = -1 / (H * eta)
        epsf = es * (eta / (-etas))**6
        u_gen = Nn * (1 + I * kk * eta) * sp.exp(-I * kk * eta) / eta**3
    elif case == 'matter':
        c = sp.Symbol('c', positive=True)
        a = c * eta**2
        epsf = sp.Rational(3, 2)
        u_gen = Nn * (1 + I * kk * eta) * sp.exp(-I * kk * eta) / eta**3
    eom = sp.simplify(sp.diff(a**2 * epsf * sp.diff(u_gen, eta), eta) + a**2 * epsf * kk**2 * u_gen)
    assert eom == 0, f"{case}: mode function does not solve the EOM"
    ubar_gen = u_gen.subs(I, -I)
    W = sp.simplify(u_gen * sp.diff(ubar_gen, eta) - ubar_gen * sp.diff(u_gen, eta))
    N2 = sp.solve(sp.Eq(W, I / (2 * a**2 * epsf)), Nn**2)[0]
    sub = lambda expr, kq, e: expr.subs(kk, kq).subs(eta, e).subs(Nn, sp.sqrt(N2.subs(kk, kq)))
    u = lambda kq, e: sub(u_gen, kq, e)
    ubar = lambda kq, e: sub(ubar_gen, kq, e)
    ubar_p = lambda kq, e: sub(sp.diff(ubar_gen, eta), kq, e)
    calH = sp.simplify(sp.diff(a, eta) / a)
    return a, epsf, calH, u, ubar, ubar_p, N2


VERTEX_SPECS = {
    # label: (prefactor as function of (a, eps), V(p,q,r), alphas)
    "zeta zeta'^2 [eps^2 - eps^3/2]":      (lambda a, e: a**2 * (e**2 - e**3 / 2), lambda p, q, r: 1, [0, 1, 1]),
    "zeta zeta'^2 [eps^2 part only]":      (lambda a, e: a**2 * e**2, lambda p, q, r: 1, [0, 1, 1]),
    "zeta (d zeta)^2 [eps^2]":             (lambda a, e: a**2 * e**2, lambda p, q, r: -dot(p, q, r), [0, 0, 0]),
    "zeta' d zeta . d chi~ [-2 eps^2]":    (lambda a, e: -2 * a**2 * e**2, lambda p, q, r: dot(q, r, p) / r**2, [1, 0, 1]),
    "zeta (d_i d_j chi~)^2 [eps^3/2]":     (lambda a, e: a**2 * e**3 / 2, lambda p, q, r: dot(q, r, p)**2 / (q**2 * r**2), [0, 1, 1]),
}


def run_vertex(args):
    """Worker: (case, label, order) -> (label, B as string)."""
    case, label, order = args
    a, epsf, calH, u, ubar, ubar_p, N2 = make_background(case)
    pref_f, V, al = VERTEX_SPECS[label]
    B = bispectrum_vertex(pref_f(a, epsf), V, al, u, ubar, ubar_p, order)
    return label, sp.srepr(B)


def shape_from_B(Bs, P2, power):
    lead = laurent_in_S(Bs, power - 2, power + 2)
    other = {p: cf for p, cf in lead.items() if p != power}
    A = sp.factor(sp.simplify(lead.get(power, sp.Integer(0)) * (k1 * k2 * k3)**3 / ((2 * sp.pi)**4 * P2)))
    return A, sorted(lead.keys()), other


def limits(A):
    f = sp.Rational(10, 3) * A / sumk3
    fsq = sp.simplify(f.subs({k2: kk, k3: kk}))
    sq = sp.nsimplify(sp.limit(fsq, k1, 0))
    sq_ser = sp.expand(sp.series(fsq, k1, 0, 3).removeO())
    eq = sp.nsimplify(sp.simplify(f.subs({k2: k1, k3: k1})))
    fo = sp.nsimplify(sp.simplify(f.subs({k2: k1 / 2, k3: k1 / 2})))
    fmu = f.subs({k2: kk, k3: sp.sqrt(kk**2 + k1**2 + 2 * kk * k1 * mu)})
    mu_lead = sp.simplify(sp.expand(sp.series(fmu, k1, 0, 1).removeO()))
    return dict(squeezed=sq, squeezed_series=sq_ser, equilateral=eq, folded=fo, squeezed_mu=mu_lead)


# =====================================================================================================
hdr("SECTION 1 --- VALIDATION OF THE MACHINERY AGAINST TWO INDEPENDENT LITERATURE BENCHMARKS")
# =====================================================================================================
print("""
  1a. de Sitter slow roll (constant eps, eta_sr = 0): the three eps^2 bulk vertices must reproduce
      Maldacena 2003 / Chen-Huang-Kachru-Shiu 2007 (c_s = 1):
        A_eps = eps [ -(1/8) sum k^3 + (1/8) sum_{i!=j} k_i k_j^2 + (1/K) sum_{i>j} k_i^2 k_j^2 ]
      This tests: mode normalisation, -2 Im commutator, Wick counting (six contractions), the three vertex
      kernels, the Bunch-Davies contour, and the exact-integral + expansion pipeline.
  1b. Ultra-slow-roll (eps ~ a^-6, eta_sr = -6, non-attractor, zeta ~ a^3): the field-redefinition term alone
      must give f_NL = 5/2 (Namjoo, Firouzjahi & Sasaki 2012).  This tests the sign and structure of
      f = (eta_sr/4) zeta^2 + zeta zeta'/calH in a non-attractor phase where zeta grows outside the horizon.
""")
ctx = mp.get_context('fork')
order_dS = 4
dS_labels = ["zeta zeta'^2 [eps^2 - eps^3/2]", "zeta (d zeta)^2 [eps^2]", "zeta' d zeta . d chi~ [-2 eps^2]"]
# NB for the dS check the eps^3 piece is dropped by using the eps^2-only vertex:
dS_labels[0] = "zeta zeta'^2 [eps^2 part only]"
with ctx.Pool(processes=min(8, os.cpu_count() or 1)) as pool:
    jobs = [('dS', lb, order_dS) for lb in dS_labels] + [('matter', lb, 6) for lb in VERTEX_SPECS]
    results = pool.map(run_vertex, jobs)
Bres = {}
for (case, lb, _), (lb2, Bs) in zip(jobs, results):
    Bres[(case, lb)] = sp.sympify(Bs, locals={'k1': k1, 'k2': k2, 'k3': k3, 'S': S, 'L': Lg})
    Bres[(case, lb)] = sp.sympify(eval(Bs, {**sp.__dict__, 'k1': k1, 'k2': k2, 'k3': k3, 'S': S, 'L': Lg,
                                             'eta': eta, 'mu': mu, 'k': kk}))

# --- 1a
a, epsv, calH, u, ubar, ubar_p, N2 = make_background('dS')
H = sp.Symbol('H', positive=True)
epsym = sp.Symbol('epsilon', positive=True)
PdS = lambda kq: kq**3 * N2.subs(kk, kq) / (2 * sp.pi**2)
P2dS = sp.simplify(PdS(k1) * PdS(k2))
A_dS = 0
print("  de Sitter |N|^2 =", N2)
for lb in dS_labels:
    B = Bres[('dS', lb)]
    neg = {p: sp.simplify(B.coeff(S, p)) for p in range(-4, 0)}
    assert all(v == 0 for v in neg.values()), "dS: divergent Im parts must cancel"
    Av = sp.factor(sp.simplify(B.coeff(S, 0) * (k1 * k2 * k3)**3 / ((2 * sp.pi)**4 * P2dS)))
    print(f"  dS vertex {lb:38s}: A =", Av)
    A_dS += Av
A_Mald = epsym * (-sp.Rational(1, 8) * sumk3
                  + sp.Rational(1, 8) * sum(KS[i] * KS[j]**2 for i in range(3) for j in range(3) if i != j)
                  + (k1**2 * k2**2 + k1**2 * k3**2 + k2**2 * k3**2) / Ksum)
d1 = sp.simplify(A_dS - A_Mald)
print("  A(dS, from scratch) - A_Maldacena =", d1)
assert d1 == 0
RESULTS["validation_deSitter_Maldacena"] = "PASS (difference identically 0)"

# --- 1b
a_u, eps_u, calH_u, uu, uub, uubp, N2u = make_background('USR')
eta_sr = sp.simplify(sp.diff(eps_u, eta) / (calH_u * eps_u))
print("  USR eta_sr =", eta_sr, " |N|^2 =", N2u)
Pk_u = lambda kq: sp.simplify(uu(kq, -S) * uub(kq, -S))
Rp_u = lambda kq: sp.simplify((uu(kq, -S) * uubp(kq, -S) + uub(kq, -S) * sp.diff(uu(kq, eta), eta).subs(eta, -S)) / 2)
calHS_u = calH_u.subs(eta, -S)
B = 0
for i, j, l in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
    B += (eta_sr / 4) * 2 * Pk_u(KS[j]) * Pk_u(KS[l]) + (1 / calHS_u) * (Pk_u(KS[j]) * Rp_u(KS[l]) + Pk_u(KS[l]) * Rp_u(KS[j]))
Bl = sp.simplify(sp.limit(sp.simplify(B) * S**12, S, 0))
Pl_u = lambda kq: sp.limit(Pk_u(kq) * S**6, S, 0) * kq**3 / (2 * sp.pi**2)
A_usr = sp.simplify(Bl * (k1 * k2 * k3)**3 / ((2 * sp.pi)**4 * Pl_u(k1) * Pl_u(k2)))
f_usr = sp.nsimplify(sp.simplify(sp.Rational(10, 3) * A_usr / sumk3))
print("  USR redefinition: A =", sp.factor(A_usr), " -> f_NL =", f_usr, "(expected 5/2)")
assert f_usr == sp.Rational(5, 2)
RESULTS["validation_USR_Namjoo"] = "PASS (f_NL = 5/2 exactly)"

# =====================================================================================================
hdr("SECTION 2 --- THE CUBIC ACTION IN THE MATTER CONTRACTION: KERNEL-LEVEL CHECK OF THE eps^3 REWRITING")
# =====================================================================================================
p, q, r = sp.symbols('p q r', positive=True)
pq, pr, qr = dot(p, q, r), dot(p, r, q), dot(q, r, p)
# (eps/2a)(dzeta)(dchi)d^2chi + (eps/4a)(d^2zeta)(dchi)^2 in conformal time with chi = a eps chi~ :
T1 = sp.Rational(1, 2) * pq / q**2            # x a^2 eps^3, monomial zeta_p zeta'_q zeta'_r   [(dzeta)(dchi~) zeta']
T2 = sp.Rational(1, 4) * p**2 * qr / (q**2 * r**2)   # x a^2 eps^3, monomial zeta_p zeta'_q zeta'_r   [(d^2 zeta)(dchi~)^2]
RHS = -sp.Rational(1, 2) + sp.Rational(1, 2) * qr**2 / (q**2 * r**2)   # -(1/2) zeta zeta'^2 + (1/2) zeta (d_i d_j chi~)^2
lhs_sym = (T1 + T1.subs({q: r, r: q}, simultaneous=True)) / 2 + T2
rhs_sym = RHS
ident = sp.simplify((lhs_sym - rhs_sym))
print("  symmetrised kernel of [(eps/2a)(dz)(dchi)d^2chi + (eps/4a)(d^2z)(dchi)^2]  minus  [-(eps^3/2)a^3 z zdot^2 + (eps/2a) z(d_i d_j chi)^2] =", ident)
assert ident == 0
print("  => the Maldacena-form action used by Cai (their Eq. 15) is exactly equivalent to Maldacena's original cubic action")
print("     at the level of Fourier kernels; the boundary term K is irrelevant for the three-point function.")
RESULTS["cubic_action_rewriting_check"] = "PASS (kernel identity exact)"

# =====================================================================================================
hdr("SECTION 3 --- MATTER CONTRACTION: EXACT PER-VERTEX SHAPE FUNCTIONS (BULK VERTICES)")
# =====================================================================================================
a_m, eps_m, calH_m, um, umb, umbp, N2m = make_background('matter')
c = sp.Symbol('c', positive=True)
print("  a = c eta^2, calH =", calH_m, ", eps = 3/2, u_k = N (1 + i k eta) e^{-i k eta}/eta^3,  |N|^2 =", N2m)
Pk_m = lambda kq: sp.simplify(um(kq, -S) * umb(kq, -S))
Pl_m = lambda kq: sp.limit(Pk_m(kq) * S**6, S, 0) * kq**3 / (2 * sp.pi**2)
P2m = sp.simplify(Pl_m(k1) * Pl_m(k2))
print("  P_zeta(eta_*) = ", sp.simplify(Pl_m(k1)), "/ S^6   (scale invariant; the shape function is c-independent)")
A_v = {}
lim_v = {}
for lb in VERTEX_SPECS:
    A, pows, other = shape_from_B(Bres[('matter', lb)], P2m, -12)
    assert not A.has(Lg), "log at leading order"
    A_v[lb] = A
    lim_v[lb] = limits(A)
    print(f"\n  vertex {lb}")
    print(f"     Im powers of S in [-14,-10]: {pows}  (leading -12 = pure number x P^2; -10 = O(k^2 S^2) correction)")
    print(f"     A_v = {A}")
    print(f"     f_NL: squeezed(isoceles k1<<k2=k3) = {lim_v[lb]['squeezed']}  [series {lim_v[lb]['squeezed_series']}],"
          f"  equilateral = {lim_v[lb]['equilateral']},  folded(k1=2k2=2k3) = {lim_v[lb]['folded']},"
          f"  squeezed at fixed angle mu = {lim_v[lb]['squeezed_mu']}")

# =====================================================================================================
hdr("SECTION 4 --- MATTER CONTRACTION: FIELD-REDEFINITION TERM (EXACT AT eta_*)")
# =====================================================================================================
calHS_m = calH_m.subs(eta, -S)
Rp_m = lambda kq: sp.simplify((um(kq, -S) * umbp(kq, -S) + umb(kq, -S) * sp.diff(um(kq, eta), eta).subs(eta, -S)) / 2)


def kernels(kq, pa, qa):
    pq_ = dot(pa, qa, kq); kp_ = dot(kq, pa, qa); kq_ = dot(kq, qa, pa)
    Fa = 1 / calHS_m
    Fb = (eps_m / (2 * calHS_m)) * (pq_ / qa**2 - kp_ * kq_ / (kq**2 * qa**2))
    Fc = (1 / (4 * calHS_m**2)) * (pq_ - kp_ * kq_ / kq**2)
    return Fa, Fb, Fc


def B_redef(which):
    B = 0
    for i, j, l in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
        ki, kj, kl = KS[i], KS[j], KS[l]
        for (pa, qa) in [(kj, kl), (kl, kj)]:
            Fa, Fb, Fc = kernels(ki, pa, qa)
            if which == 'a':
                B += Fa * Pk_m(pa) * Rp_m(qa)
            if which == 'b':
                B += Fb * Pk_m(pa) * Rp_m(qa)
            if which == 'c':
                B += Fc * Pk_m(pa) * Pk_m(qa)
    return sp.simplify(B)


A_red = {}
for which, desc in [('a', "zeta zeta'/calH (local)"), ('b', "(eps/2calH)[(dz)(dchi~) - d^-2 dd(dz dchi~)] (non-local)"),
                    ('c', "(1/4calH^2)[-(dz)^2 + d^-2 dd(dz dz)] (gradient)")]:
    A, pows, other = shape_from_B(B_redef(which), P2m, -12)
    A_red[which] = A
    lm = limits(A)
    print(f"\n  f_{which} = {desc}")
    print(f"     powers of S present: {pows};  A = {A}")
    print(f"     f_NL: squeezed = {lm['squeezed']}, equilateral = {lm['equilateral']}, fixed-mu squeezed = {lm['squeezed_mu']}")
A_v["field redefinition (a+b+c)"] = sp.factor(A_red['a'] + A_red['b'] + A_red['c'])
lim_v["field redefinition (a+b+c)"] = limits(A_v["field redefinition (a+b+c)"])
print("\n  field redefinition total: squeezed", lim_v["field redefinition (a+b+c)"]['squeezed'],
      " equilateral", lim_v["field redefinition (a+b+c)"]['equilateral'])

# =====================================================================================================
hdr("SECTION 5 --- TOTAL, LIMITS, AND COMPARISON WITH CAI 2009 / LI 2016 / PAPER 2")
# =====================================================================================================
contrib = ["field redefinition (a+b+c)", "zeta zeta'^2 [eps^2 - eps^3/2]", "zeta (d zeta)^2 [eps^2]",
           "zeta' d zeta . d chi~ [-2 eps^2]", "zeta (d_i d_j chi~)^2 [eps^3/2]"]
A_tot = sp.factor(sp.simplify(sum(A_v[lb] for lb in contrib)))
lt = limits(A_tot)
print("  A_total (x 256 prod k_i^2) =", sp.expand(A_tot * 256 * (k1 * k2 * k3)**2))
print()
print("  PER-VERTEX TABLE (from scratch; eps = 3/2):")
print(f"  {'vertex':44s} {'squeezed':>10s} {'equilateral':>12s} {'folded':>8s}   squeezed at fixed angle mu")
for lb in contrib:
    lm = lim_v[lb]
    print(f"  {lb:44s} {str(lm['squeezed']):>10s} {str(lm['equilateral']):>12s} {str(lm['folded']):>8s}   {lm['squeezed_mu']}")
print(f"  {'TOTAL':44s} {str(lt['squeezed']):>10s} {str(lt['equilateral']):>12s} {str(lt['folded']):>8s}   {lt['squeezed_mu']}")
print("  isoceles squeezed series:", lt['squeezed_series'])

# ---- Cai's source-level rows (matterbounceng2.tex, first forms; triple sums over the six ordered all-distinct triples)
ks = KS


def Sig(p_, q_):
    return sum(ks[i]**p_ * ks[j]**q_ for i in range(3) for j in range(3) if i != j)


def T6(p_, q_, r_):
    return sum(ks[i]**p_ * ks[j]**q_ * ks[l]**r_ for (i, j, l) in permutations(range(3)))


def T3(p_, q_, r_):
    seen, tot = set(), 0
    for (i, j, l) in permutations(range(3)):
        key = tuple(sorted([(i, p_), (j, q_), (l, r_)]))
        if key in seen:
            continue
        seen.add(key)
        tot += ks[i]**p_ * ks[j]**q_ * ks[l]**r_
    return tot


e = sp.Rational(3, 2)
Pik2 = (k1 * k2 * k3)**2
cai_rows = {
    "field redefinition (a+b+c)": -e / 2 * sumk3 - e**2 / (32 * Pik2) * (Sig(7, 2) + Sig(6, 3) - 2 * Sig(5, 4) - 2 * T6(5, 2, 2) - T6(4, 3, 2)),
    "zeta zeta'^2 [eps^2 - eps^3/2]": (-e**2 / 12 + e**3 / 24) * sumk3,
    "zeta' d zeta . d chi~ [-2 eps^2]": e**2 / (24 * Pik2) * (2 * Sig(7, 2) - 2 * Sig(5, 4) - T6(5, 2, 2)),
    "zeta (d_i d_j chi~)^2 [eps^3/2]": e**3 / (96 * Pik2) * (Sig(1, 0) * 0 + sum(x**9 for x in ks) - 3 * Sig(7, 2) - Sig(6, 3) + 3 * Sig(5, 4) - T6(5, 2, 2) + T6(4, 3, 2)),
}
print("\n  COMPARISON WITH CAI ET AL.'S FOUR SOURCE-LEVEL VERTEX ROWS (arXiv:0903.0631v2 source, eps = 3/2):")
row_diffs = {}
for lb, row in cai_rows.items():
    d = sp.simplify(A_v[lb] - row)
    row_diffs[lb] = str(d)
    print(f"     {lb:44s}: A(from scratch) - A(Cai row) = {d}")
# Cai printed Eq. (37) under both readings of sum_{i!=j!=k}
A37 = lambda T: sp.Rational(3, 256) / Pik2 * (3 * sum(x**9 for x in ks) + Sig(7, 2) - 9 * Sig(6, 3) + 5 * Sig(5, 4) - 66 * T(5, 2, 2) + 9 * T(4, 3, 2))
d37_3 = sp.simplify(A_tot - A37(T3))
d37_6 = sp.simplify(A_tot - A37(T6))
print("\n  Cai Eq. (37) with the (5,2,2) sum over the THREE distinct monomials: A_total - A_T =", d37_3)
print("  Cai Eq. (37) with the (5,2,2) sum over SIX ordered permutations       : A_total - A_T =", sp.factor(d37_6))
# Li 2016 Eq. (4.19) at c_s = 1
cs = sp.Integer(1)
A_Li = ((-sp.Rational(105, 32) + sp.Rational(39, 16) / cs**2 + 9 * cs**2 / 128) * sumk3
        + sp.Rational(3, 256) * (3 * cs**2 + 6) * Sig(2, 1)
        + sp.Rational(3, 256) / Pik2 * (3 * cs**2 * sum(x**9 for x in ks) + (10 - 9 * cs**2) * Sig(7, 2)
                                        - (3 * cs**2 + 6) * Sig(6, 3) + (9 * cs**2 - 4) * Sig(5, 4)))
dLi = sp.simplify(A_tot - A_Li)
print("  Li et al. Eq. (4.19) at c_s = 1: A_total - A_tot^Li =", dLi)
fLi = -sp.Rational(165, 16) + sp.Rational(65, 8)
print("  Li et al. Eq. (5.1) at c_s = 1: f_NL^local =", fLi)
print("\n  CAI'S QUOTED AMPLITUDES vs FROM-SCRATCH:")
for name, cai, mine in [("local (squeezed isoceles)", sp.Rational(-35, 8), lt['squeezed']),
                        ("equilateral", sp.Rational(-255, 64), lt['equilateral']),
                        ("folded k1=2k2=2k3", sp.Rational(-9, 4), lt['folded'])]:
    print(f"     {name:28s}: Cai {str(cai):>8s}   from scratch {str(mine):>9s}   ratio Cai/from-scratch = {sp.nsimplify(cai / mine)}")
# P2 table
p2_table = {"field redefinition (a+b+c)": (sp.Rational(-25, 16), sp.Rational(-35, 32)),
            "zeta zeta'^2 [eps^2 - eps^3/2]": (sp.Rational(-5, 32), sp.Rational(-5, 32)),
            "zeta' d zeta . d chi~ [-2 eps^2]": (0, sp.Rational(-5, 8)),
            "zeta (d_i d_j chi~)^2 [eps^3/2]": (sp.Rational(-15, 32), sp.Rational(-15, 128))}
p2_ok = all(lim_v[lb]['squeezed'] == v[0] and lim_v[lb]['equilateral'] == v[1] for lb, v in p2_table.items())
print("  Paper 2 Table tab:vertexwalk (per-vertex squeezed/equilateral) reproduced exactly:", p2_ok)
RESULTS["in_in_from_scratch"] = {
    "convention": "comoving-gauge zeta (Maldacena), zeta = zeta_g + (3/5) f_NL zeta_g^2, f_NL = (10/3) A / sum k^3, evaluated at eta_* with |k eta_*|<<1",
    "per_vertex": {lb: {"A": str(A_v[lb]), "f_squeezed": str(lim_v[lb]['squeezed']), "f_equilateral": str(lim_v[lb]['equilateral']),
                        "f_folded": str(lim_v[lb]['folded']), "f_squeezed_fixed_mu": str(lim_v[lb]['squeezed_mu'])} for lb in contrib},
    "A_total_times_256_prodk2": str(sp.expand(A_tot * 256 * Pik2)),
    "f_local_squeezed_isoceles": str(lt['squeezed']),
    "f_squeezed_isoceles_series_in_k1_over_k": str(lt['squeezed_series']),
    "f_squeezed_fixed_angle_mu": str(lt['squeezed_mu']),
    "f_equilateral": str(lt['equilateral']),
    "f_folded": str(lt['folded']),
    "cai_row_differences": row_diffs,
    "cai_eq37_minus_total_distinct_monomial_reading": str(d37_3),
    "cai_eq37_minus_total_six_permutation_reading": str(sp.factor(d37_6)),
    "li_eq419_minus_total_at_cs1": str(dLi),
    "li_eq51_at_cs1": str(fLi),
    "cai_quoted_over_from_scratch": {"local": "2", "equilateral": "2", "folded": "2"},
    "paper2_vertexwalk_table_reproduced": bool(p2_ok),
}

# =====================================================================================================
hdr("SECTION 6 --- SEPARATE-UNIVERSE (delta-N) ON BOTH SLICINGS, EXACT TO SECOND ORDER, GENERAL eps")
# =====================================================================================================
print("""
  Exponential potential V = V0 e^{-lambda phi}, lambda^2 = 2 eps (w = 2eps/3 - 1), separate-universe system derived
  from the field equations (as in the second-method script): x = phidot/(sqrt6 H), dx/dN = (1-x^2)(sqrt6 lambda/2 - 3x),
  dphi/dN = sqrt6 x, dln|H|/dN = -3x^2.  Growing mode = off-attractor displacement u = x - x*, u ~ W = e^{-alpha N},
  alpha = 3 - eps.  Growing-mode-dominated limit W -> inf.  Two final slicings:
     (c) uniform-phi  = comoving (delta phi = 0)  = the variable the in-in computes;
     (rho) uniform-|H| = uniform density         = the variable the 2026-09-02 second method computed.
""")
ep = sp.Symbol('epsilon', positive=True)
Wn = sp.Symbol('W', positive=True)
ui, dphi = sp.symbols('u_i deltaphi_i')
xs = sp.sqrt(ep / 3)
lam = sp.sqrt(6) * xs
x, uu_ = sp.symbols('x u')
dxdN = (1 - x**2) * (sp.sqrt(6) * lam / 2 - 3 * x)
rhs = sp.expand(dxdN.subs(x, xs + uu_))
c1 = sp.simplify(rhs.coeff(uu_, 1)); c2 = sp.simplify(rhs.coeff(uu_, 2))
alpha = sp.simplify(-c1)
A2 = sp.simplify(c2 / (-alpha))
uN = ui * Wn + ui**2 * A2 * (Wn**2 - Wn)
dN_ = lambda f: -alpha * Wn * sp.diff(f, Wn)
res = sp.simplify(sp.expand(sp.series(dN_(uN) - rhs.subs(uu_, uN), ui, 0, 3).removeO()).coeff(ui, 2))
print("  du/dN = (", c1, ") u + (", c2, ") u^2 ;  alpha = 3 - eps ;  ODE residual at O(u_i^2):", res)
assert res == 0
IntU = sp.expand(ui * (1 - Wn) / alpha + ui**2 * A2 * ((1 - Wn**2) / (2 * alpha) - (1 - Wn) / alpha))
IntU2 = ui**2 * (1 - Wn**2) / (2 * alpha)
assert sp.simplify(dN_(IntU) - uN) == 0 and sp.simplify(dN_(IntU2) - (ui * Wn)**2) == 0
lead = lambda expr, power: sp.simplify(sp.expand(expr).coeff(Wn, power))
dN1 = -dphi / (sp.sqrt(6) * xs) - IntU.coeff(ui, 1) * ui / xs
dN2 = -(IntU.coeff(ui, 2) * ui**2 + uN.coeff(ui, 1) * ui * dN1) / xs
z1c = lead(dN1.coeff(ui, 1) * ui, 1); z2c = lead(sp.expand(dN2).coeff(ui, 2) * ui**2, 2)
f_c = sp.simplify(sp.Rational(5, 3) * z2c / z1c**2)
dN1r = -(6 * xs * IntU.coeff(ui, 1) * ui) / (3 * xs**2)
dN2r = -(6 * xs * (IntU.coeff(ui, 2) * ui**2 + uN.coeff(ui, 1) * ui * dN1r) + 3 * IntU2) / (3 * xs**2)
z1r = lead(dN1r, 1); z2r = lead(sp.expand(dN2r), 2)
f_r = sp.simplify(sp.Rational(5, 3) * z2r / z1r**2)
ratio_lin = sp.simplify(z1r / z1c)
print("  comoving slicing   : zeta_1 =", sp.factor(z1c), "W ; zeta_2 =", sp.factor(z2c), "W^2 ;  f_NL(eps) =", sp.factor(f_c),
      "; eps=3/2 ->", f_c.subs(ep, sp.Rational(3, 2)))
print("  uniform-rho slicing: zeta_1 =", sp.factor(z1r), "W ; zeta_2 =", sp.factor(z2r), "W^2 ;  f_NL(eps) =", sp.factor(f_r),
      "; eps=3/2 ->", f_r.subs(ep, sp.Rational(3, 2)))
print("  linear growing mode: zeta_rho / zeta_c =", ratio_lin, "  (the two 'zeta's are NOT the same variable in a non-attractor phase)")
print("  f_rho - f_c =", sp.factor(sp.simplify(f_r - f_c)))
RESULTS["delta_N"] = {
    "comoving_slicing_fNL_general_eps": str(sp.factor(f_c)), "comoving_slicing_fNL_eps_3_2": str(f_c.subs(ep, sp.Rational(3, 2))),
    "uniform_density_slicing_fNL_general_eps": str(sp.factor(f_r)), "uniform_density_slicing_fNL_eps_3_2": str(f_r.subs(ep, sp.Rational(3, 2))),
    "linear_ratio_zeta_rho_over_zeta_c": str(ratio_lin),
    "second_method_2026_09_02_reproduced": str(f_r.subs(ep, sp.Rational(3, 2))) == "-55/16",
}

# =====================================================================================================
hdr("SECTION 7 --- WHY THE ISOTROPIC SEPARATE UNIVERSE CANNOT REPRODUCE THE IN-IN: THE LONG MODE'S SHEAR")
# =====================================================================================================
print("""
  ADM, comoving gauge (Maldacena): h_ij = a^2 e^{2 zeta} delta_ij, N = 1 + zetadot/H, N_i = d_i psi,
  psi = -zeta/H + a^2 eps d^-2 zetadot.   K_ij = (1/2N)(hdot_ij - D_i N_j - D_j N_i).
  Linear order:  K^i_j = H delta^i_j - d_i d_j psi / a^2.
  Fourier, growing mode (zetadot = -(3/2) H zeta, i.e. zeta ~ eta^-3):
""")
Hs, as_, zs, kv = sp.symbols('H a zeta k', positive=True)
epsn = sp.Rational(3, 2)
zdot = -sp.Rational(3, 2) * Hs * zs
psi = -zs / Hs + as_**2 * epsn * (-zdot / kv**2)         # d^-2 -> -1/k^2
dK = sp.simplify(kv**2 * psi / as_**2)                   # trace perturbation: -d^2 psi/a^2 -> +k^2 psi/a^2
sigma_along_k = sp.simplify(sp.Rational(2, 3) * kv**2 * psi / as_**2)   # eigenvalue of -(d_i d_j - delta d^2/3) psi/a^2 along k-hat
print("  psi_k =", sp.factor(psi))
print("  delta K (trace)  =", sp.factor(dK), "   ->  k -> 0 limit:", sp.limit(dK, kv, 0), "  = eps * zetadot  (O(k^0): local expansion-rate perturbation)")
print("  shear eigenvalue along k-hat = (2/3) delta K, i.e. sigma^i_j = (k-hat_i k-hat_j - delta_ij/3) * eps * zetadot   (O(k^0), SAME order)")
print("  attractor comparison (zetadot = 0): delta K = -k^2 zeta/(a^2 H) -> 0 and shear -> 0 as k -> 0: an FRW patch.")
print("""
  => In the non-attractor matter contraction the k -> 0 limit of a comoving-gauge growing mode is NOT an FRW patch:
     it carries a traceless shear of the same order as its expansion-rate perturbation, with the fixed angular pattern
     (k-hat k-hat - delta/3).  An isotropic separate-universe (delta-N) calculation keeps the trace and drops the shear.
     The in-in bispectrum keeps both, and its squeezed limit therefore has a monopole AND a quadrupole in the angle
     mu = k-hat_1 . k-hat between the long and short modes (Section 5):
""")
fmu = lt['squeezed_mu']
f0 = sp.nsimplify(fmu.subs(mu, 0)); f2 = sp.nsimplify(sp.simplify((fmu - f0) / mu**2))
print("     f_NL^sq(mu) =", fmu, "=", f0, "+", f2, "mu^2")
print("     isoceles (mu -> 0, the 'local' number quoted in the literature):", f0)
print("     angle-averaged monopole (<mu^2> = 1/3):", sp.nsimplify(f0 + f2 / 3), ";  quadrupole coefficient of (mu^2 - 1/3):", f2)
print("     along k-hat (mu = +-1):", sp.nsimplify(f0 + f2))
print("  The quadrupole comes entirely from the two vertices that contain the long mode's d chi~ (its shift/shear):")
for lb in contrib:
    m2 = sp.nsimplify(sp.simplify((lim_v[lb]['squeezed_mu'] - lim_v[lb]['squeezed_mu'].subs(mu, 0)) / mu**2)) if lim_v[lb]['squeezed_mu'].has(mu) else 0
    print(f"     {lb:44s}: mu^2 coefficient = {m2}")
RESULTS["long_mode_shear"] = {
    "deltaK_k_to_0": "eps*zetadot (O(k^0))", "shear_k_to_0": "(khat_i khat_j - delta_ij/3) eps zetadot (O(k^0))",
    "squeezed_fNL_mu": str(fmu), "monopole_isoceles": str(f0), "quadrupole": str(f2),
    "angle_averaged": str(sp.nsimplify(f0 + f2 / 3)),
}

# =====================================================================================================
hdr("SECTION 8 --- RECONCILIATION LEDGER AND VERDICT")
# =====================================================================================================
f_inin = lt['squeezed']
print(f"""
  ROUTE                                                        f_NL^local     status
  Cai et al. 2009 Eq. (39), in-in                                  -35/8      arithmetic: exactly 2x their own Eq. (37); all three of their
                                                                              quoted amplitudes (-35/8, -255/64, -9/4) are 2x the from-scratch
                                                                              values ({f_inin}, {lt['equilateral']}, {lt['folded']})  => uniform factor-2
                                                                              slip in the amplitude-parameter step (Eqs. 38-40), NOT a vertex.
  Li, Quintin, Wang, Cai 2016 Eq. (5.1) at c_s = 1                -35/16     correct; NOT independent of Cai: their four c_s=1 rows are Cai's
                                                                              rows coefficient-for-coefficient and their Eq. (4.19) is Cai's Eq. (37).
  Quintin, Sherkatghanad, Cai, Brandenberger 2015 (1508.04141)    -35/16     a quotation ('the authors of [Cai] found -35/16'), no computation.
  BigBounce Paper 2, Appendix A                                    -35/16     correct value; its per-vertex table is reproduced exactly here.
                                                                              Its 'spurious -(99/128) sum k^3 term' is a READING of the
                                                                              sum_(i!=j!=k) k^5 k^2 k^2 symbol in Eq. (37): with the natural
                                                                              distinct-monomial reading Eq. (37) EQUALS the vertex sum exactly.
  THIS WORK, in-in from scratch (validated on dS + USR)             {f_inin}     comoving zeta, isoceles squeezed limit, end of contraction.
  lab second method 2026-09-02, delta-N, uniform-density slices    -55/16     correct for ITS variable (reproduced here for general eps),
                                                                              but zeta_rho = {ratio_lin} zeta_c already at linear order: different variable.
  THIS WORK, delta-N, comoving (uniform-phi) slices                {f_c.subs(ep, sp.Rational(3, 2))}         same variable as the in-in at zeroth gradient order, still != in-in:
                                                                              the isotropic separate universe drops the O(1) shear of the
                                                                              non-attractor long mode (Sec. 7); the in-in squeezed limit is
                                                                              f(mu) = {fmu}, and neither its isoceles value nor its monopole
                                                                              is a separate-universe quantity.
""")
verdict = {
    "value": str(f_inin),
    "definition": ("f_NL^local = lim_{k1->0} (10/3) A(k1,k,k)/(2k^3) of the comoving-gauge (Maldacena zeta, h_ij = a^2 e^{2 zeta} delta_ij) "
                   "three-point function at the end of the matter contraction (|k eta_B| << 1), Bunch-Davies vacuum, canonical field, "
                   "eps = 3/2, eta_sr = 0, c_s = 1, with <zeta^3> = (2 pi)^7 delta P^2 A/prod k^3 and zeta = zeta_g + (3/5) f_NL zeta_g^2; "
                   "the same definition used by Cai 2009 (Eqs. 20-21) and Li 2016 (Sec. 5). The limit is end-time independent at leading order "
                   "(corrections O(k^2 eta_B^2)) but ORIENTATION dependent: f(mu) = -35/16 + (15/16) mu^2."),
    "which_published_number_is_correct": "-35/16 (Li 2016 Eq. 5.1 at c_s=1; Paper 2). Cai 2009's -35/8 is exactly a factor 2 too large.",
    "discrepancy_origins": {
        "Cai_-35/8": "uniform factor 2 in the amplitude-parameter evaluation (their Eqs. 38-40 are each 2x their own Eq. 37 evaluated correctly); no vertex error; Eq. (37) itself is right under the distinct-monomial reading of sum_(i!=j!=k)",
        "deltaN_-55/16": "(c) slicing: uniform-density zeta_rho vs comoving zeta_c differ by a factor 2 at linear order and by 5(eps+1)/8 in f_NL; f_rho = 5(eps-7)/8 reproduced",
        "deltaN_comoving_-5": "(b') not an O(k^2) gradient term: the k->0 limit of a non-attractor comoving mode carries traceless shear (k-hat k-hat - delta/3) eps zetadot of the same order as its expansion perturbation eps zetadot; an isotropic separate universe cannot represent it, and the in-in squeezed limit is correspondingly anisotropic (quadrupole 15/16 mu^2)",
        "end_time_(d)": "excluded: leading Im part is the pure S^-12 term; next term is O(k^2 S^2)",
    },
    "remaining_single_computation": ("a second-order anisotropic (Bianchi-I) separate-universe calculation of the comoving zeta response to a long mode "
                                     "carrying shear (k-hat k-hat - delta/3) eps zetadot, to reproduce the in-in monopole -15/8 and quadrupole 15/16 "
                                     "from a gradient-expansion route; until then the in-in is the only complete route and its result stands"),
}
RESULTS["verdict"] = verdict
print("  VERDICT: f_NL^local (comoving zeta, isoceles squeezed limit) =", f_inin, "; Cai 2009's -35/8 = 2 x this, mechanism = amplitude-step factor 2;")
print("           delta-N values (-55/16 uniform-density, -5 comoving) are separate-universe quantities of a non-FRW limit and are not the in-in number.")

# =====================================================================================================
hdr("PROVENANCE")
# =====================================================================================================
with open(SELF, "rb") as fh:
    script_sha = hashlib.sha256(fh.read()).hexdigest()
elapsed = time.time() - T0
RESULTS["provenance"] = {
    "script": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py",
    "script_sha256": script_sha, "wall_clock_seconds": round(elapsed, 1),
    "sympy_version": sp.__version__, "python": sys.version.split()[0], "date": "2026-09-02",
    "sources_read_2026_09_02": [
        "arXiv:0903.0631v2 source matterbounceng2.tex (Cai, Xue, Brandenberger, Zhang 2009): Eqs. 14-15, 20-21, 25-39",
        "arXiv:1612.02036 source (Li, Quintin, Wang, Cai 2016): Secs. 3-5, Eqs. 4.1-4.19, 5.1",
        "arXiv:1508.04141 source (Quintin, Sherkatghanad, Cai, Brandenberger 2015): f_NL^local quotation, App. cubic action",
        "arXiv:astro-ph/0210603 source (Maldacena 2003): cubic action, dS three-point function, integral I",
        "arXiv:1210.3692 (Namjoo, Firouzjahi, Sasaki 2012): USR f_NL = 5/2, delta-N with N(phi, phidot)",
        "arXiv:1301.5699 (Chen, Firouzjahi, Namjoo, Sasaki 2013): non-attractor in-in, field-redefinition dominance",
        "research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.{py,md,json} (commit d7dac953)",
        "research/focused_paper_source_integration/02_full_draft.tex App. A + scripts/p2_vertex_check.py",
    ],
}
print(f"  script sha256: {script_sha}\n  wall clock   : {elapsed:.1f} s\n  sympy        : {sp.__version__}")
out = os.path.join(HERE, "fnl_matter_contraction_adjudication_2026_09_02.json")
with open(out, "w") as fh:
    json.dump(RESULTS, fh, indent=2)
print("  wrote", out)

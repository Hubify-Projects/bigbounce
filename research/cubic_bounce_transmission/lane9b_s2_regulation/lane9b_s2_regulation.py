#!/usr/bin/env python3
"""Lane 9b — is the S2 (effective-fluid, z^2 = 2 a^2 eps / c_s^2) divergence of Delta f_NL^bounce
physical or an artefact of the *form* of the cubic action?

Equation-level test on the Quintin+2015-type background H = Ups t, a = exp(Ups t^2/2), eps = -1/(Ups t^2):
  [A] exact Frobenius solution of the S2 Mukhanov-Sasaki equation for zeta around the bounce t = 0,
      keeping the k^2 correction of the constant mode (which is 1/t-enhanced because int z^2 dt ~ 1/t);
  [B] on-shell ADM constraint solutions in comoving gauge (Maldacena 2003 Eq. 2.13-2.14, Chen+2007 Eq. 3.5-3.6):
      N_1 = zetadot/H,  psi = -zeta/H + chi,  d^2 chi = a^2 eps zetadot / c_s^2 ;
      Laurent expansion of each at t = 0  ->  is the comoving-gauge metric regular at H = 0 ?
  [C] pole orders of the Maldacena/Chen-form vertices (lane (a) table) on the EXACT modes of [A]
      vs lane (a)'s super-Hubble counting (zetadot ~ H^2);
  [D] pole orders of the same physics written in the raw ADM building blocks (a, H, phidot, V; zeta, N_1, psi).
Outputs: lane9b_s2_regulation.json, lane9b_s2_regulation.log.  Literature statements are labelled; nothing
from Quintin+2015 is re-derived here.
"""
import json, os, sys, time
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "lane9b_s2_regulation.log"), "w")
RES = {"lane": "9b", "date": "2026-09-04", "background": "Quintin+2015-type: H=Ups t, a=exp(Ups t^2/2), eps=-1/(Ups t^2)"}


def log(m=""):
    print(m); LOG.write(m + "\n"); LOG.flush()


t, Ups, cs, k = sp.symbols("t Upsilon c_s k", positive=True)
C1, C2 = sp.symbols("C1 C2")
NSER = 8  # series order in t

# ---------------- background (exact, symbolic) ----------------
a = sp.exp(Ups * t**2 / 2)
H = Ups * t
eps = sp.simplify(-sp.diff(H, t) / H**2)          # -1/(Ups t^2)
z2 = sp.simplify(2 * a**2 * eps / cs**2)           # S2 weight, pole at H=0 (and negative: NEC violation)
phidot2 = sp.simplify(-2 * sp.diff(H, t))          # rho+p = phidot^2 = -2 Hdot = -2 Ups  (P(X,phi) fluid; sign = NEC violation)


def lead(expr, var=t):
    """leading power and coefficient of a Laurent series in var at 0."""
    e = sp.series(expr, var, 0, NSER).removeO()
    e = sp.expand(e)
    if e == 0:
        return None, 0
    terms = sp.Add.make_args(e)
    pows = []
    for term in terms:
        c, p = term.as_coeff_exponent(var)
        pows.append((p, c))
    pmin = min(p for p, _ in pows)
    coef = sum(c for p, c in pows if p == pmin)
    return pmin, sp.simplify(coef)


def main():
    t0 = time.time()
    log("# Lane 9b — S2 regularisation test (Quintin-type bounce)")
    log(f"eps = {eps};  z^2 = {z2};  phidot^2 = rho+p = {phidot2}")
    RES["z2_pole_order"] = int(lead(z2)[0])
    log(f"[A0] z^2 pole order at t=0: {RES['z2_pole_order']}  (S2 pathology, as in the brief);  int z^2 dt ~ {sp.integrate(sp.series(z2,t,0,4).removeO(),t)}")
    return t0


STEPS = []


def step_A_frobenius():
    """Exact series solution of the S2 MS equation  d/dt( (z^2/a) zetadot ) + c_s^2 k^2 a z^2 zeta = 0
    (conformal-time (z^2 zeta')' + c_s^2 k^2 z^2 zeta = 0 rewritten in cosmic time).
    Indicial exponents at t=0 are 0 and 3  ->  zeta = C1*(1 + ...) + C2*(t^3 + ...)."""
    cs_ = [sp.Symbol(f"c{n}") for n in range(NSER + 2)]
    zeta = sum(cs_[n] * t**n for n in range(NSER + 2))
    w = sp.series(z2 / a, t, 0, NSER + 2).removeO()
    eq = sp.expand(sp.series(sp.diff(w * sp.diff(zeta, t), t) + cs**2 * k**2 * sp.series(a * z2, t, 0, NSER + 2).removeO() * zeta,
                             t, 0, NSER - 1).removeO())
    sol = {cs_[0]: C1, cs_[3]: C2}
    # solve order by order for the remaining coefficients
    for p in range(-3, NSER - 2):
        coef = eq.coeff(t, p).subs(sol)
        unknowns = [c for c in cs_ if c in coef.free_symbols and c not in sol]
        if coef == 0 or not unknowns:
            continue
        s = sp.solve(coef, unknowns[0], dict=True)
        if s:
            sol.update({kk: sp.simplify(v) for kk, v in s[0].items()})
    zeta_sol = sp.expand(zeta.subs(sol))
    # any coefficient left unsolved beyond the truncation is set to 0 (truncation only)
    zeta_sol = zeta_sol.subs({c: 0 for c in cs_ if c not in sol})
    zeta_sol = sp.expand(sp.series(zeta_sol, t, 0, 6).removeO())
    log("\n[A] Frobenius solution of the S2 MS equation about the bounce (to O(t^5)):")
    log(f"    zeta = {zeta_sol}")
    zd = sp.expand(sp.diff(zeta_sol, t))
    c1_part = sp.expand(zd.coeff(C1)); c2_part = sp.expand(zd.coeff(C2))
    p1, l1 = lead(c1_part); p2, l2 = lead(c2_part)
    log(f"    zetadot|C1 = {l1}*t^{p1} + ... (k^2 correction, 1/t-ENHANCED by int z^2 dt ~ 1/t: NOT ~H^2)")
    log(f"    zetadot|C2 = {l2}*t^{p2} + ... (lane (a)'s ~H^2 mode)")
    RES["A_frobenius"] = {"zeta_series": str(zeta_sol), "zetadot_C1_leading": f"{l1}*t^{p1}",
                          "zetadot_C2_leading": f"{l2}*t^{p2}", "indicial_exponents": [0, 3]}
    # residual check: plug back
    resid = sp.expand(sp.series(sp.diff((z2 / a) * sp.diff(zeta_sol, t), t) + cs**2 * k**2 * a * z2 * zeta_sol, t, 0, 3).removeO())
    log(f"    residual of the MS equation through O(t^2): {resid}")
    RES["A_frobenius"]["residual_through_t2"] = str(resid)
    return zeta_sol


STEPS.append(step_A_frobenius)

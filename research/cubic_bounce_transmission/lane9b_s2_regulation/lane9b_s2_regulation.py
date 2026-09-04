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
    pw = sorted(sp.Poly(e.subs(var, 1 / var) if False else e, var).as_dict().keys()) if False else None
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

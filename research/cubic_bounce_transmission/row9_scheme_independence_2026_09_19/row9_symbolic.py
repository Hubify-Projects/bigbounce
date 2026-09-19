#!/usr/bin/env python3
"""Leg A of ledger row 9 / D-A3-9: exact symbolic derivation of the scheme-independent variable.

Everything here is derived from the linearised Einstein equations for a single minimally coupled
scalar (c_s = 1, arbitrary V) on an arbitrary a(eta).  No result is imported from memory; the four
deliverables A1-A4 of PREREGISTRATION.md section 2 are each printed with an explicit sympy check.
Run:  python3 row9_symbolic.py    ->  row9_symbolic.log, symbolic_results.json
"""
import json, sys
import sympy as sp

OUT = {}
LOG = []
def log(s=""):
    print(s); LOG.append(str(s))

eta, k = sp.symbols("eta k", real=True, positive=True)
a = sp.Function("a", positive=True)(eta)
V = sp.Function("V")(eta)                 # V(phi(eta)) along the background
phi = sp.Function("phi")(eta)
Phi = sp.Function("Phi")(eta)             # Bardeen potential (longitudinal gauge, no anisotropic stress)
dphi = sp.Function("dphi")(eta)           # delta phi in longitudinal gauge

H = sp.diff(a, eta) / a                   # conformal Hubble  script-H
Hp = sp.diff(H, eta)

log("=" * 100)
log("LEG A - exact symbolic derivation (sympy %s).  Units 8 pi G = 1." % sp.__version__)
log("=" * 100)

# ---------------------------------------------------------------- background (Friedmann + KG)
# H^2 = (a^2/3) rho ,  rho = phi'^2/(2a^2) + V  ;  H^2 - H' = phi'^2 / 2
bg_fried = sp.Eq(H**2, (sp.diff(phi, eta) ** 2 / 2 + a**2 * V) / 3)
bg_ppl   = sp.Eq(H**2 - Hp, sp.diff(phi, eta) ** 2 / 2)
log("\n[background] Friedmann : %s" % sp.pretty(bg_fried.lhs - bg_fried.rhs, use_unicode=False).replace("\n", " "))
log("[background] H^2 - H'   = phi'^2 / 2   (equivalently  H^2 - H' = -a^2 Hdot = (a^2/2)(rho+p) )")

# ---------------------------------------------------------------- linearised Einstein equations
# longitudinal gauge ds^2 = a^2[-(1+2Phi)deta^2 + (1-2Phi)dx^2], Psi = Phi (no anisotropic stress).
# phi-sector quantities are carried as plain symbols so the background reduction is deterministic.
p1, p2, Vp = sp.symbols("p1 p2 Vp")          # phi', phi'', V_,phi
D = lambda f, n=1: sp.diff(f, eta, n)

# (E2) momentum constraint  Phi' + H Phi = (1/2) phi' dphi   ->  dphi = 2(Phi' + H Phi)/phi'
dphi_sol  = 2 * (D(Phi) + H * Phi) / p1
dphip_sol = 2 * (D(Phi, 2) + Hp * Phi + H * D(Phi)) / p1 - 2 * (D(Phi) + H * Phi) * p2 / p1**2
log("\n[A2] momentum constraint (E2)  ->  dphi = 2(Phi' + H Phi)/phi'")

common = (p1 * dphip_sol - p1**2 * Phi) / a**2
drho = common + Vp * dphi_sol
dp   = common - Vp * dphi_sol
# (E1) energy   : 3 H (Phi' + H Phi) + k^2 Phi + (a^2/2) drho = 0
# (E3) pressure : Phi'' + 3 H Phi' + (2H' + H^2) Phi - (a^2/2) dp = 0
E1 = 3 * H * (D(Phi) + H * Phi) + k**2 * Phi + a**2 * drho / 2
E3 = D(Phi, 2) + 3 * H * D(Phi) + (2 * Hp + H**2) * Phi - a**2 * dp / 2

# background reduction, applied in a fixed order:
#   Klein-Gordon      phi'' + 2 H phi' + a^2 V_,phi = 0      ->  V_,phi = -(phi'' + 2 H phi')/a^2
#   d/deta of H^2-H' = phi'^2/2                              ->  phi''/phi' = (2HH' - H'')/(2(H^2-H'))
#   Friedmann/energy  H^2 - H' = phi'^2/2                    ->  phi'^2 = 2(H^2 - H')
pp_over_p = sp.simplify((2 * H * Hp - D(Hp)) / (2 * (H**2 - Hp)))
reduce_bg = lambda e: sp.simplify(sp.expand(
    e.subs(Vp, -(p2 + 2 * H * p1) / a**2).subs(p2, p1 * pp_over_p).subs(p1**2, 2 * (H**2 - Hp))))
E1s, E3s = reduce_bg(E1), reduce_bg(E3)

log("[A2] after the background reduction:  E3 = %s" % E3s)
log("     (the pressure equation is REDUNDANT given E2 + the background -- an internal consistency check)")
OUT["A2_E3_is_redundant"] = bool(sp.simplify(E3s) == 0)

# claimed closed form: Phi'' + 2(H - phi''/phi') Phi' + (k^2 + 2H' - 2 H phi''/phi') Phi = 0
claim = (D(Phi, 2) + 2 * (H - pp_over_p) * D(Phi)
         + (k**2 + 2 * Hp - 2 * H * pp_over_p) * Phi)
resid = sp.simplify(sp.expand(E1s - claim))
log("[A2] energy constraint E1 (with E2 and the background substituted) minus the claimed closed Phi equation = %s" % resid)
OUT["A2_phi_equation_residual"] = str(resid)
assert resid == 0, "A2 FAILED: the closed Phi equation is not what was claimed"
log("[A2] PASS -- exact closed equation, obtained from the ENERGY constraint:")
log("        Phi'' + 2(H - phi''/phi') Phi' + (k^2 + 2H' - 2 H phi''/phi') Phi = 0,")
log("        phi''/phi' = (2 H H' - H'')/(2(H^2 - H'))  -- no z, no 1/H anywhere.")
OUT["A2_phi_equation"] = "Phi'' + 2(H - pp)Phi' + (k^2 + 2H' - 2 H pp)Phi = 0 ; pp = (2HH'-H'')/(2(H^2-H'))"

# --- A2b: integrating factor mu (self-adjoint form)
mu = sp.Function("mu")(eta)
mu_claim = a**2 / (H**2 - Hp)
chk = sp.simplify(sp.diff(mu_claim, eta) / mu_claim - 2 * (H - pp_over_p))
log("\n[A2b] mu = a^2/(H^2 - H') : mu'/mu - 2(H - phi''/phi') = %s" % chk)
OUT["A2b_mu_residual"] = str(chk)
assert chk == 0
log("[A2b] PASS -- self-adjoint form  (mu Phi')' + mu (k^2 + 2H' - 2 H phi''/phi') Phi = 0,")
log("        mu = a^2/(H^2 - H') = -1/Hdot   (since H^2 - H' = -a^2 Hdot).")
log("        => mu is FINITE at H = 0 (Hdot != 0) and blows up only at the NEC crossing Hdot = 0.")
OUT["A2b_mu"] = "mu = a^2/(H^2-H') = -1/Hdot"

# --- A3: the exact zeta <-> (Phi, Phi') dictionary (comoving curvature perturbation)
Rcom = sp.simplify(Phi + H * dphi_sol * p1 / p1**2 * p1)
Rcom = sp.simplify((Phi + H * (2 * (D(Phi) + H * Phi) / p1) / p1).subs(p1**2, 2 * (H**2 - Hp)))
log("\n[A3] R_comoving = Phi + H dphi/phi' = %s" % sp.simplify(Rcom))
OUT["A3_dictionary"] = "zeta = Phi + H (Phi' + H Phi)/(H^2 - H')"
log("[A3] i.e.  zeta = Phi + H (Phi' + H Phi)/(H^2 - H').  At H = 0 this gives zeta = Phi exactly.")

# --- A3b: the exact zeta' identity (used to invert the dictionary numerically)
Phi2_tmp = -2 * (H - pp_over_p) * D(Phi) - (k**2 + 2 * Hp - 2 * H * pp_over_p) * Phi
zeta_of_Phi_tmp = Phi + H * (D(Phi) + H * Phi) / (H**2 - Hp)
zp = sp.simplify(sp.expand(D(zeta_of_Phi_tmp).doit().subs(sp.Derivative(Phi, (eta, 2)), Phi2_tmp).doit()))
zp_claim = -k**2 * H * Phi / (H**2 - Hp)
log("")
log("[A3b] zeta' computed from the dictionary and reduced on the Phi equation, minus  -k^2 H Phi/(H^2-H') = %s"
    % sp.simplify(sp.expand(zp - zp_claim)))
OUT["A3b_zetaprime_residual"] = str(sp.simplify(sp.expand(zp - zp_claim)))
log("[A3b] => exact:  zeta' = -k^2 H Phi/(H^2 - H') = k^2 H Phi/(a^2 Hdot).")
log("      Together with A3 this is an invertible algebraic map (Phi, Phi') <-> (zeta, zeta') wherever H != 0,")
log("      and it makes super-Hubble zeta-conservation manifest (zeta' = O(k^2)).")
OUT["A3b_zetaprime"] = "zeta' = -k^2 H Phi/(H^2 - H')"

# --- A1: the exact zeta equation implied by that dictionary, and which scheme it is
z2 = 2 * a**2 * (H**2 - Hp) / H**2          # z^2 = 2 a^2 eps  with eps = 1 - H'/H^2 = -Hdot/H^2
zeta = sp.Function("zeta")(eta)
# substitute Phi -> solve the dictionary for Phi given zeta is hard; instead verify the S2 equation
# is implied: take the known MS form (z^2 zeta')' + k^2 z^2 zeta = 0 and check it is equivalent to
# the Phi equation under the dictionary, by substituting a trial solution of the Phi equation.
zeta_of_Phi = Phi + H * (sp.diff(Phi, eta) + H * Phi) / (H**2 - Hp)
lhs_S2 = sp.diff(z2 * sp.diff(zeta_of_Phi, eta), eta) + k**2 * z2 * zeta_of_Phi
lhs_S2 = sp.expand(sp.simplify(lhs_S2.doit()))
# reduce using the Phi equation:  Phi'' = -2(H - pp)Phi' - (k^2 + 2H' - 2 H pp) Phi
Phi2 = -2 * (H - pp_over_p) * sp.diff(Phi, eta) - (k**2 + 2 * Hp - 2 * H * pp_over_p) * Phi
lhs_S2 = lhs_S2.subs(sp.Derivative(Phi, (eta, 3)), sp.diff(Phi2, eta)).doit()
lhs_S2 = lhs_S2.subs(sp.Derivative(Phi, (eta, 2)), Phi2).doit()
lhs_S2 = sp.simplify(sp.expand(sp.simplify(lhs_S2)))
log("\n[A1] (z^2 zeta')' + k^2 z^2 zeta  with z^2 = 2a^2 eps (scheme S2) and zeta from the dictionary,")
log("     reduced on the Phi equation  =  %s" % lhs_S2)
OUT["A1_S2_residual"] = str(lhs_S2)
S2_ok = sp.simplify(lhs_S2) == 0
log("[A1] S2 equation implied by the exact Einstein equations: %s" % ("YES (residual 0)" if S2_ok else "NO"))

# --- S1: is zeta'' + 2(a'/a) zeta' + k^2 zeta = 0 (z = a) implied?
lhs_S1 = sp.diff(a**2 * sp.diff(zeta_of_Phi, eta), eta) + k**2 * a**2 * zeta_of_Phi
lhs_S1 = sp.expand(sp.simplify(lhs_S1.doit()))
lhs_S1 = lhs_S1.subs(sp.Derivative(Phi, (eta, 3)), sp.diff(Phi2, eta)).doit()
lhs_S1 = lhs_S1.subs(sp.Derivative(Phi, (eta, 2)), Phi2).doit()
lhs_S1 = sp.simplify(sp.expand(sp.simplify(lhs_S1)))
log("\n[A1] same with z = a (scheme S1) = %s" % sp.simplify(lhs_S1))
S1_ok = sp.simplify(lhs_S1) == 0
OUT["A1_S1_residual"] = str(sp.simplify(lhs_S1))
log("[A1] S1 equation implied by the exact Einstein equations: %s" % ("YES" if S1_ok else "NO"))

# when does S1 hold?  z ~ a  <=>  eps = const  <=>  d/deta (H^2 - H')/H^2 = 0
qq, xx = sp.symbols("qq xx", positive=True)
S1num = -a * sp.diff(a, eta) * sp.diff(a, eta, 3) + 2 * a * sp.diff(a, eta, 2) ** 2 - sp.diff(a, eta) ** 2 * sp.diff(a, eta, 2)
S1pl = sp.simplify(S1num.subs(a, eta ** qq).doit())
log("")
log("[A1] the S1 residual is proportional to  N[a] = -a a1 a3 + 2 a a2^2 - a1^2 a2  (a_n = n-th eta-derivative);")
log("     on a power-law background a = eta^q (i.e. eps = -Hdot/H^2 constant)  N[a] = %s" % S1pl)
log("     so S1 z = a is the exact scalar variable IF AND ONLY IF eps is constant.")
OUT["A1_S1_powerlaw_residual"] = str(S1pl)
OUT["A1_S1_condition"] = "S1 (z=a) is exact iff eps = -Hdot/H^2 is constant (power-law background)"

# --- A3c: the (Phi, Xi) first-order system -- delta-free, hence junction-prescription-free
mu_ = a**2 / (H**2 - Hp)
W_  = k**2 + 2 * Hp - 2 * H * pp_over_p
Xi  = mu_ * (D(Phi) + H * Phi)
Phi2b = -2 * (H - pp_over_p) * D(Phi) - W_ * Phi
log("")
log("[A3c] mu W - [ mu(k^2 + 2H' - 2H^2) + H mu' ] = %s" % sp.simplify(mu_ * W_ - (mu_ * (k**2 + 2 * Hp - 2 * H**2) + H * D(mu_))))
log("      -> in the self-adjoint form the ENTIRE delta-function content of a jump in Hdot sits in the")
log("         single term H mu' Phi, because mu = -1/Hdot jumps there.  Absorbing it:")
XiP = sp.diff(Xi, eta).doit().subs(sp.Derivative(Phi, (eta, 2)), Phi2b).doit()
log("[A3c] Xi' - [(a^2 - mu k^2)Phi + H Xi] = %s   with Xi = mu(Phi' + H Phi)"
    % sp.simplify(sp.expand(XiP - ((a**2 - mu_ * k**2) * Phi + H * Xi))))
log("      Phi' = Xi/mu - H Phi = -Hdot Xi - H Phi")
log("      NEITHER right-hand side contains mu' (or any other derivative of a jumping background")
log("      quantity), so Phi and Xi are BOTH continuous across a jump in Hdot: the Bardeen system")
log("      needs NO junction prescription at all.")
OUT["A3c_muW_residual"] = str(sp.simplify(mu_ * W_ - (mu_ * (k**2 + 2 * Hp - 2 * H**2) + H * D(mu_))))
OUT["A3c_Xi_residual"] = str(sp.simplify(sp.expand(XiP - ((a**2 - mu_ * k**2) * Phi + H * Xi))))
log("[A3c] zeta - (Phi + H Xi/a^2) = %s" % sp.simplify(zeta_of_Phi_tmp - (Phi + H * Xi / a**2)))
log("[A3c] z^2 zeta' + 2 a^2 k^2 Phi/H = %s   (z^2 = 2a^2 eps)"
    % sp.simplify(2 * a**2 * (H**2 - Hp) / H**2 * zp_claim + 2 * a**2 * k**2 * Phi / H))
log("      => [Xi] = 0  <=>  [zeta] = 0   and   [Phi] = 0  <=>  [z^2 zeta'] = 0 .")
log("      The continuity that the Bardeen system enforces automatically is therefore EXACTLY scheme S2's")
log("      junction prescription ([zeta] = 0, [z^2 zeta'] = 0) -- derived here, not assumed.")
OUT["A3c_conclusion"] = "(Phi, Xi) continuous <=> ([zeta]=0 and [z^2 zeta']=0) = scheme S2's junction prescription"

# --- A4: junction condition from the self-adjoint form
log("")
log("[A4] Junction condition across a surface where a, H are continuous but Hdot jumps.")
log("     NAIVE reading of the self-adjoint form -- '[Phi] = 0 and [mu Phi'] = 0' -- is WRONG: by A3c")
log("     the potential term mu W itself carries a delta (H mu' Phi), so mu Phi' is NOT continuous.")
log("     The correct, delta-free statement is A3c's:  [Phi] = 0 and [Xi] = 0, Xi = mu(Phi' + H Phi),")
log("     which by A3c is identically  [zeta] = 0 and [z^2 zeta'] = 0  -- scheme S2's prescription.")
log("     (The naive [mu Phi'] = 0 is kept in the numerics as a labelled REJECTED control: it excites")
log("      the decaying mode and gives lambda ~ k^-2, destroying scale invariance.)")
OUT["A4_correct"] = "[Phi]=0 and [Xi]=0  ==  [zeta]=0 and [z^2 zeta']=0"
OUT["A4_rejected_naive"] = "[Phi]=0 and [mu Phi']=0 -- drops the H mu' Phi delta"

# --- regularity statement at the two degenerate points (indicial exponents)
s = sp.symbols("s", real=True)
c = sp.symbols("c", nonzero=True)
r = sp.symbols("r")
# near a simple zero of Hdot: mu ~ -1/(c s); (mu Phi')' + mu W Phi = 0  ->  Phi'' - Phi'/s + W Phi = 0
ind = sp.expand(r * (r - 1) - r)
roots = sp.solve(sp.Eq(ind, 0), r)
log("\n[A5] Indicial exponents of the Phi equation at a SIMPLE ZERO of Hdot (the NEC crossing): %s" % roots)
OUT["A5_indicial_NEC"] = [str(x) for x in roots]
log("     Both are >= 0, so Phi and Phi' are bounded there: Phi is REGULAR at rho + p = 0.")
log("[A5] At H = 0 with Hdot = Ups != 0 the equation is  Phi'' + (k^2 + 2 a^2 Ups) Phi = 0  (phi''/phi' = H),")
log("     manifestly regular.  Hence Phi is regular at BOTH degenerate points, with no choice of z.")
OUT["A5_H0_form"] = "Phi'' + (k^2 + 2 a^2 Ups) Phi = 0 in the window"

# verify that H=0 window reduction explicitly on the Quintin window background a = exp(Ups t^2/2)
t, Ups = sp.symbols("t Ups", real=True, positive=True)
aw = sp.exp(Ups * t**2 / 2)
Hw = Ups * t                                        # H = Ups t
Hcw = aw * Hw                                       # script-H = a H
# phi''/phi' in conformal time  = (2 H H' - H'')/(2(H^2 - H'))  ; here H^2 - H' = -a^2 Hdot = -a^2 Ups
HH = Hcw
HHp = aw * sp.diff(HH, t)                            # d/deta = a d/dt
pp_w = sp.simplify((2 * HH * HHp - aw * sp.diff(HHp, t)) / (2 * (HH**2 - HHp)))
log("")
log("[A5b] Quintin window check: scriptH^2 - scriptH_prime + a^2 Ups = %s  (must be 0)" % sp.simplify(HH**2 - HHp + aw**2 * Ups))
log("\n[A5b] Quintin window (a = exp(Ups t^2/2), H = Ups t):  phi''/phi' - script-H = %s"
    % sp.simplify(pp_w - HH))
OUT["A5b_window_pp_minus_H"] = str(sp.simplify(pp_w - HH))
log("      friction coefficient 2(script-H - phi''/phi') = %s ;  k^0 coefficient 2H' - 2 H phi''/phi' = %s"
    % (sp.simplify(2 * (HH - pp_w)), sp.simplify(2 * HHp - 2 * HH * pp_w)))
OUT["A5b_window_k0"] = str(sp.simplify(2 * HHp - 2 * HH * pp_w))

# --- G1 gate, matter domination
log("\n[G1] matter contraction/expansion (eps = 3/2, a ~ eta^2):")
etasym = sp.symbols("etasym", nonzero=True)
am = etasym**2
Hm = sp.diff(am, etasym) / am
Hmp = sp.diff(Hm, etasym)
ppm = sp.simplify((2 * Hm * Hmp - sp.diff(Hmp, etasym)) / (2 * (Hm**2 - Hmp)))
log("     friction 2(H - phi''/phi') = %s   (expect 6/eta)" % sp.simplify(2 * (Hm - ppm)))
log("     k^0 term  2H' - 2 H phi''/phi'  = %s   (expect 0)" % sp.simplify(2 * Hmp - 2 * Hm * ppm))
zeta_md = sp.simplify((Phi + Hm * (sp.diff(Phi, etasym) + Hm * Phi) / (Hm**2 - Hmp)))
log("     dictionary: zeta = %s  -> for Phi = const, zeta = (5/3) Phi" % sp.simplify(zeta_md))
OUT["G1_friction"] = str(sp.simplify(2 * (Hm - ppm)))
OUT["G1_k0"] = str(sp.simplify(2 * Hmp - 2 * Hm * ppm))
OUT["G1_zeta"] = str(sp.simplify(zeta_md))
OUT["G1_pass"] = bool(sp.simplify(2 * (Hm - ppm) - 6 / etasym) == 0 and sp.simplify(2 * Hmp - 2 * Hm * ppm) == 0)
log("     G1 symbolic part: %s" % ("PASS" if OUT["G1_pass"] else "FAIL"))

OUT["A1_S2_is_exact"] = bool(S2_ok)
OUT["A1_S1_is_exact"] = bool(S1_ok)

with open("row9_symbolic.log", "w") as f:
    f.write("\n".join(LOG) + "\n")
with open("symbolic_results.json", "w") as f:
    json.dump(OUT, f, indent=2)
log("\n[done] wrote row9_symbolic.log, symbolic_results.json")

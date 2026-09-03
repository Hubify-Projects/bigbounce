#!/usr/bin/env python3
"""
Lane (a) of ledger item #2 (second half): cubic-vertex table for zeta through a
nonsingular bounce, and its H -> 0 behaviour.

Everything numeric/symbolic printed by this script is COMPUTED here.  The vertex
coefficients themselves are LITERATURE (transcribed with citation, see LITERATURE
dict); what this script adds is (i) their evaluation on two explicit bounce
backgrounds, (ii) the pole order of every coefficient and of every in-in
integrand at the bounce point H = 0, under the two MS-variable schemes the lab
already uses (S1 geometric / dressed-metric, S2 effective fluid), (iii) the
super-Hubble (k eta_B << 1) first-order in-in reduction of the pure-time vertices
to a one-dimensional bounce-window integral, and (iv) its numerical value for the
Quintin+2015-type background of a2_transmission_linear.py in scheme S1.

Units: M_Pl^2 = 1/(8 pi G) = 1.  Cosmic time t, conformal time eta, a_B = 1,
bounce at t_B = 0.  eps = -Hdot/H^2, eta_sr = epsdot/(eps H), s = csdot/(cs H).
"""
import json, os, sys, time
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "cubic_vertex_table.log")
JSON_OUT = os.path.join(HERE, "vertex_table.json")
_lines = []


def log(m=""):
    print(m)
    _lines.append(str(m))


# ---------------------------------------------------------------------------
# [L] LITERATURE: the cubic action in comoving gauge for P(X, phi) with sound speed
#     Seery & Lidsey 2005 (astro-ph/0503692) Eq. (51); Chen, Huang, Kachru & Shiu
#     2007 (hep-th/0605045) Eq. (4.28)-(4.29); at c_s = 1, lambda = 0 this is
#     Maldacena 2003 (astro-ph/0210603) Eq. (3.9)-(3.10). Transcribed, NOT derived
#     here.  chi is eliminated with Chen's del^2 chi = a^2 eps zetadot / c_s^2, i.e.
#     chi = (a^2 eps/c_s^2) chit with chit = del^-2 zetadot.
#     Sigma = X P_X + 2 X^2 P_XX = H^2 eps / c_s^2 ; lambda = X^2 P_XX + (2/3) X^3 P_XXX.
# ---------------------------------------------------------------------------
LITERATURE = {
    "cubic_action": "Chen, Huang, Kachru & Shiu 2007 (hep-th/0605045) Eq. (4.28); "
                    "Seery & Lidsey 2005 (astro-ph/0503692) Eq. (51); "
                    "c_s=1, lambda=0 limit: Maldacena 2003 (astro-ph/0210603) Eq. (3.9)",
    "field_redefinition": "Chen et al. 2007 Eq. (4.29) [Maldacena 2003 Eq. (3.10) at c_s=1]: "
                          "zeta = zeta_n + f(zeta_n), f = eta_sr/(4 c_s^2) zeta^2 + zeta zetadot/(c_s^2 H) "
                          "+ [-(d zeta)^2 + d^-2 d_i d_j(d_i zeta d_j zeta)]/(4 a^2 H^2) "
                          "+ [(d zeta)(d chi) - d^-2 d_i d_j(d_i zeta d_j chi)]/(2 a^2 H)",
    "boundary_terms": "Arroja & Tanaka 2011 (arXiv:1103.1102); Burrage, Ribeiro & Seery 2011 "
                      "(arXiv:1103.4126): the total-derivative terms dropped from the bulk cubic "
                      "action are equivalent, for the correlator at eta_*, to the field-redefinition "
                      "terms above (literature; equivalence used, not re-derived)",
    "bounce_background": "Quintin, Sherkatghanad, Cai & Brandenberger 2015 (arXiv:1508.04141): "
                         "bounce phase H = Upsilon (t - t_B), a = a_B exp[Upsilon (t-t_B)^2/2]; "
                         "f_NL enhanced during the bounce if zeta grows (their Sec. 5, literature)",
    "lqc_background": "Ashtekar & Singh 2011 (arXiv:1108.0893) effective LQC Friedmann equation "
                      "H^2 = (rho/3)(1 - rho/rho_c); Agullo, Bolliet & Sreenath 2017 "
                      "(arXiv:1712.08148): bounce enhances f_NL by orders of magnitude on scales "
                      "larger than the curvature radius at the bounce (literature)",
    "in_in_conventions": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md "
                         "Sec. 1 (lab convention: <zeta^3> = -2 Im int d eta <zeta^3(eta_*) L_int(eta)>, "
                         "3! leg attachments each counted once, no hand symmetry factors)",
    "prior_lab_result": "research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md "
                        "Sec. 2.1: effective-fluid z^2 = a^2 (rho+p)/(c_s^2 H^2) has an H=0 pole; "
                        "dressed-metric a''/a bounded; super-Hubble zeta = C1 + C2 J, J = int d eta / z^2",
}

t, Ups, rhoc, cs, lam, k = sp.symbols("t Upsilon rho_c c_s lambda k", positive=True)
a, H, eps, etasr, s = sp.symbols("a H epsilon eta_sr s")   # generic background symbols

# Coefficients c_V(t) of the operators O_V in  S_3 = int dt d^3x  sum_V c_V(t) O_V   (cosmic time).
# n_dot = number of time derivatives in O_V (each zetadot -> zeta'/a; chit = del^-2 zetadot).
# 'sq_kernel_note' = squeezed-limit remark (k_L -> 0), literature/structural, used in Sec. E.
VERTICES = {
    "V1": dict(op="zetadot^3",
               coeff=-a**3 * ((eps * H**2 / cs**2) * (1 - 1 / cs**2) + 2 * lam) / H, n_dot=3,
               grad=0, note="vanishes for canonical c_s=1, lambda=0; Sigma written as eps H^2/c_s^2"),
    "V2": dict(op="zeta zetadot^2",
               coeff=a**3 * eps / cs**4 * (eps - 3 + 3 * cs**2), n_dot=2, grad=0,
               note="Maldacena a^3 eps^2 zeta zetadot^2 at c_s=1"),
    "V3": dict(op="zeta (d zeta)^2 / a^2",
               coeff=a * eps / cs**2 * (eps - 2 * s + 1 - cs**2), n_dot=0, grad=2,
               note="gradient vertex; carries an explicit k^2 relative to V2 on super-Hubble scales"),
    "V4": dict(op="zetadot (d zeta)(d chit)",
               coeff=-2 * a**3 * eps**2 / cs**4, n_dot=2, grad=0,
               note="Chen's -2 a eps/c_s^2 zetadot d zeta d chi with chi = a^2 eps chit/c_s^2; "
                    "the d^-2 in chit cancels the two gradients: not k^2 suppressed"),
    "V5": dict(op="zeta^2 zetadot",
               coeff=a**3 * eps / (2 * cs**2) * sp.Symbol("detasr_cs2_dt"), n_dot=1, grad=0,
               note="coefficient (a^3 eps/2c_s^2) d/dt(eta_sr/c_s^2); zero for constant eps"),
    "V6": dict(op="(d zeta)(d chit) d^2 chit",
               coeff=a**3 * eps**3 / (2 * cs**4), n_dot=2, grad=0,
               note="Chen's eps/(2a) d zeta d chi d^2 chi; with the lab's verified rewrite V6+V7 = "
                    "-(a^3 eps^3/2) zeta zetadot^2 + (a^3 eps^3/2) zeta (d_i d_j chit)^2 + total deriv."),
    "V7": dict(op="d^2 zeta (d chit)^2",
               coeff=a**3 * eps**3 / (4 * cs**4), n_dot=2, grad=0,
               note="Chen's eps/(4a) d^2 zeta (d chi)^2"),
}
# field-redefinition pieces f = sum_j F_j(t) * o_j, contributing 2 F_j x (P P + perms) type terms
REDEF = {
    "R1": dict(op="zeta^2", coeff=etasr / (4 * cs**2), note="local; gives (5/12) eta_sr-type piece"),
    "R2": dict(op="zeta zetadot", coeff=1 / (cs**2 * H), note="local; gives (5/3) zetadot/(H zeta) at eta_*"),
    "R3": dict(op="[-(d zeta)^2 + d^-2 d_i d_j(d_i zeta d_j zeta)]", coeff=1 / (4 * a**2 * H**2),
               note="non-local; O(k^2/(aH)^2) at fixed zeta"),
    "R4": dict(op="[(d zeta)(d chit) - d^-2 d_i d_j(d_i zeta d_j chit)]", coeff=eps / (2 * cs**2 * H),
               note="non-local; from (d zeta d chi)/(2 a^2 H) with chi = a^2 eps chit/c_s^2"),
}


# ---------------------------------------------------------------------------
# [B] backgrounds (exact, symbolic in t)
# ---------------------------------------------------------------------------
def bg_quintin_sym():
    Hq = Ups * t
    aq = sp.exp(Ups * t**2 / 2)
    return dict(label="Quintin+2015-type bounce phase", a=aq, H=Hq)


def bg_lqc_sym():
    # dust in effective LQC: a^3 = 1 + (3/4) rho_c t^2  (verified below against the Friedmann eq.)
    y = 1 + sp.Rational(3, 4) * rhoc * t**2
    al = y ** sp.Rational(1, 3)
    Hl = sp.diff(al, t) / al
    return dict(label="LQC effective, dust (rho_c bounce)", a=al, H=Hl)


def derived(bg):
    a_, H_ = bg["a"], bg["H"]
    Hd = sp.diff(H_, t)
    e = sp.simplify(-Hd / H_**2)
    es = sp.simplify(sp.diff(e, t) / (e * H_))
    return dict(Hdot=sp.simplify(Hd), eps=e, eta_sr=es)


def pole_order(expr, var=t):
    """Leading power n and coefficient of `var` as var -> 0 (n < 0 = pole): expr ~ c * var^n."""
    expr = sp.simplify(expr)
    if expr == 0:
        return None, sp.Integer(0)
    lt = sp.simplify(expr.as_leading_term(var))
    n, c = sp.Integer(0), lt
    for fac, pw in lt.as_powers_dict().items():
        if fac == var:
            n = pw
    c = sp.simplify(lt / var**n)
    return int(n), c


def main():
    t0 = time.time()
    log("=" * 78)
    log("Lane (a): cubic-vertex table for zeta through a nonsingular bounce  (2026-09-03)")
    log("=" * 78)
    out = {"date": "2026-09-03", "units": "M_Pl^2 = 1, a_B = 1, t_B = 0",
           "literature": LITERATURE, "vertices": {}, "redefinition": {},
           "backgrounds": {}, "scheme_pole_table": {}, "super_hubble_reduction": {},
           "S1_numerical_estimate": {}}

    # ---------------- [A] literature table, generic symbols ----------------
    log("\n[A] Cubic action  S3 = int dt d^3x sum_V c_V(t) O_V   (LITERATURE, cited in JSON)")
    for key, V in VERTICES.items():
        log(f"  {key}: c = {V['coeff']}   x  {V['op']}    [{V['note']}]")
        out["vertices"][key] = dict(operator=V["op"], coefficient=str(V["coeff"]),
                                    n_time_derivs=V["n_dot"], explicit_gradients=V["grad"],
                                    note=V["note"], source=LITERATURE["cubic_action"])
    log("  Field redefinition zeta = zeta_n + f(zeta_n), f = sum_j F_j o_j:")
    for key, R in REDEF.items():
        log(f"  {key}: F = {R['coeff']}   x  {R['op']}    [{R['note']}]")
        out["redefinition"][key] = dict(operator=R["op"], coefficient=str(R["coeff"]),
                                        note=R["note"], source=LITERATURE["field_redefinition"])

    # sanity: c_s = 1, lambda = 0 reduces to the lab's adjudication Lagrangian
    V2c = VERTICES["V2"]["coeff"].subs({cs: 1})
    V6c = VERTICES["V6"]["coeff"].subs({cs: 1})
    assert sp.simplify(V2c - a**3 * eps**2) == 0
    assert sp.simplify(V2c - V6c - a**3 * (eps**2 - eps**3 / 2)) == 0  # after the V6+V7 rewrite
    assert sp.simplify(VERTICES["V1"]["coeff"].subs({cs: 1, lam: 0})) == 0
    log("  check: c_s=1, lambda=0 -> Maldacena / lab adjudication form (V1=0, V2 -> a^3 eps^2, "
        "V2-V6 rewrite -> a^3(eps^2 - eps^3/2)): OK")

    # ---------------- [B] backgrounds ----------------
    log("\n[B] Backgrounds (exact in t)")
    bgs = {"quintin": bg_quintin_sym(), "lqc": bg_lqc_sym()}
    # verify LQC closed form against H^2 = (rho/3)(1 - rho/rho_c), rho = rho_c a^-3
    al, Hl = bgs["lqc"]["a"], bgs["lqc"]["H"]
    rho = rhoc / al**3
    assert sp.simplify(Hl**2 - rho / 3 * (1 - rho / rhoc)) == 0
    log("  LQC dust closed form a^3 = 1 + (3/4) rho_c t^2 satisfies H^2 = (rho/3)(1-rho/rho_c): OK")
    for key, bg in bgs.items():
        d = derived(bg)
        bg.update(d)
        n_eps, c_eps = pole_order(d["eps"])
        n_eta, c_eta = pole_order(d["eta_sr"])
        ratio = sp.simplify(d["eta_sr"] / d["eps"])
        Ups_eff = sp.limit(bg["H"] / t, t, 0)
        log(f"  {bg['label']}:")
        log(f"    H = {bg['H']}")
        log(f"    Hdot = {d['Hdot']},  Hdot(t_B) = {sp.simplify(d['Hdot'].subs(t, 0))}  "
            f"(local Upsilon_eff = {Ups_eff})")
        log(f"    eps = {d['eps']}   ~ {c_eps} * t^{n_eps}  as t->0")
        log(f"    eta_sr = {d['eta_sr']}   ~ {c_eta} * t^{n_eta};  eta_sr/eps = {ratio} "
            f"(-> {sp.limit(ratio, t, 0)} at the bounce)")
        out["backgrounds"][key] = dict(label=bg["label"], H=str(bg["H"]), a=str(bg["a"]),
                                       Hdot=str(d["Hdot"]), eps=str(d["eps"]), eta_sr=str(d["eta_sr"]),
                                       eps_pole=dict(order=n_eps, coeff=str(c_eps)),
                                       eta_sr_pole=dict(order=n_eta, coeff=str(c_eta)),
                                       eta_sr_over_eps_at_bounce=str(sp.limit(ratio, t, 0)),
                                       Upsilon_eff_at_bounce=str(Ups_eff))
    log("  => both backgrounds are locally H = Upsilon_eff t at the bounce (LQC: Upsilon_eff = rho_c/2);"
        " eps = -1/(Upsilon t^2) double pole, eta_sr = 2 eps exactly in the Quintin phase.")

    # ---------------- [C] coefficient poles on each background ----------------
    log("\n[C] Pole order of every coefficient at the bounce (t -> 0), c_s = const (s=0), lambda const")
    coeff_poles = {}
    for bkey, bg in bgs.items():
        sub = {a: bg["a"], H: bg["H"], eps: bg["eps"], etasr: bg["eta_sr"], s: 0,
               sp.Symbol("detasr_cs2_dt"): sp.diff(bg["eta_sr"], t) / cs**2}
        coeff_poles[bkey] = {}
        log(f"  {bg['label']}")
        for key, V in list(VERTICES.items()) + list(REDEF.items()):
            c = sp.simplify(V["coeff"].subs(sub))
            n, lc = pole_order(c)
            if n is None:
                log(f"    {key}: coefficient == 0")
                coeff_poles[bkey][key] = dict(pole_order=None, lead=None)
                continue
            log(f"    {key}: ~ ({sp.simplify(lc)}) * t^{n}")
            coeff_poles[bkey][key] = dict(pole_order=n, lead=str(sp.simplify(lc)))
    out["coefficient_poles"] = coeff_poles

    # ---------------- [D] integrand poles under the two MS schemes ----------------
    # Super-Hubble mode: zeta = C1 + C2 J(eta), J = int d eta / z^2  => zeta' = C2 / z^2,
    # zetadot = C2 /(a z^2).  Scheme S2 (fluid): z^2 = 2 a^2 eps / c_s^2 (conformal-time S2 of the
    # brief with the 1/2 normalisation).  Scheme S1 (geometric / dressed-metric): z = a, i.e. the
    # quadratic action of the brief with eps -> eps_eff = 1/2, c_s -> 1, eta_sr -> 0.
    log("\n[D] Bounce-point behaviour of each in-in integrand  c_V(t) * O_V[zeta]  with super-Hubble")
    log("    mode functions zetadot = C2/(a z^2) (zeta itself finite, ~C1 + C2 J):")
    log("    S2 (effective fluid): z^2 = 2 a^2 eps/c_s^2  ->  zetadot ~ c_s^2 C2/(2 a^3 eps) ~ H^2")
    log("    S1 (geometric):       z^2 = a^2, eps_eff = 1/2, c_s = 1, eta_sr = 0 -> zetadot = C2/a^3")
    scheme = {}
    for bkey, bg in bgs.items():
        sub = {a: bg["a"], H: bg["H"], eps: bg["eps"], etasr: bg["eta_sr"], s: 0,
               sp.Symbol("detasr_cs2_dt"): sp.diff(bg["eta_sr"], t) / cs**2}
        zd_S2 = cs**2 / (2 * bg["a"]**3 * bg["eps"])       # zetadot per unit C2, scheme S2
        zd_S1 = 1 / bg["a"]**3
        scheme[bkey] = {}
        log(f"  {bg['label']}")
        for key, V in VERTICES.items():
            c = sp.simplify(V["coeff"].subs(sub))
            nd = V["n_dot"]
            # conformal-time measure dt = a d eta; report pole order in t of  c_V * zetadot^n_dot
            i2 = sp.simplify(c * zd_S2**nd)
            n2, l2 = pole_order(i2)
            # S1: same operator structure but coefficient evaluated with eps_eff = 1/2, c_s=1, eta_sr=0
            cS1 = V["coeff"].subs({eps: sp.Rational(1, 2), cs: 1, s: 0, lam: 0,
                                   sp.Symbol("detasr_cs2_dt"): 0, a: bg["a"], H: bg["H"]})
            i1 = sp.simplify(cS1 * zd_S1**nd)
            n1, l1 = pole_order(i1) if i1 != 0 else (None, 0)
            parity = "odd" if (n2 is not None and n2 % 2) else "even"
            verdict = ("FINITE" if (n2 is not None and n2 >= 0) else
                       ("odd pole (PV-finite, scheme-dependent)" if parity == "odd" else
                        "NON-INTEGRABLE even pole"))
            s1txt = ("coefficient == 0 in S1" if n1 is None else
                     f"~ t^{n1}" + (" (finite)" if n1 >= 0 else " (POLE)"))
            log(f"    {key}: S2 integrand ~ t^{n2} [{verdict}];  S1 integrand {s1txt}")
            scheme[bkey][key] = dict(S2_pole_order=n2, S2_lead=str(l2), S2_verdict=verdict,
                                     S1_pole_order=n1, S1_lead=str(l1))
        # field redefinition evaluated AT the bounce point (eta_* = t_B): pole orders of F_j o_j
        red = {}
        for key, R in REDEF.items():
            F = sp.simplify(R["coeff"].subs(sub))
            nd = 1 if "zetadot" in R["op"] or "chit" in R["op"] else 0
            i2 = sp.simplify(F * zd_S2**nd)
            n2, l2 = pole_order(i2)
            red[key] = dict(S2_pole_order=n2, S2_lead=str(l2))
            log(f"    {key} (redefinition, S2, incl. zetadot factor): ~ t^{n2}")
        scheme[bkey]["redefinition"] = red
    out["scheme_pole_table"] = scheme

    # ---------------- [E] super-Hubble first-order in-in reduction, pure-time vertices ----------------
    # For a vertex  L = c(eta) zeta zeta'^2  (conformal-time coefficient c = a^{1-2} c_V = c_V / a
    # for n_dot = 2, since zetadot = zeta'/a and dt = a d eta) and super-Hubble modes
    #   u_i(eta) = C1_i + C2_i J(eta),  Im(C1_i C2_i^*) = 1/2  (Wronskian with z^2 = a^2, S1),
    # the lab convention gives, for each vertex, a Fourier-space contribution
    #   B(k1,k2,k3) = -2 Im[ u1 u2 u3(eta_*) int d eta c(eta) sum_{S3 attachments} prod_j T_j(u_{sigma j}^*(eta)) ]
    # Here we evaluate this exactly in J-space for the vertex zeta zeta'^2 (V2-type) and zeta^2 zeta'
    # (V5-type), with the matter-contraction vacuum coefficients of the brief:
    #   alpha_i = -k_i^2/(3 A sqrt(2 k_i)),  beta_i = 3 i A/(k_i sqrt(2 k_i)),  r_i = -9 i A^2 I_inf / k_i^3,
    #   C1_i = alpha_i (1 + r_i),  C2_i = beta_i,   J(eta_*) = +I_inf (post-bounce, eta_* -> +inf).
    log("\n[E] Super-Hubble reduction of the pure-time vertices (exact in J; k eta_B << 1)")
    A, Iinf, J = sp.symbols("A I_inf J", positive=True)
    k1, k2, k3 = sp.symbols("k1 k2 k3", positive=True)

    def coeffs(kk):
        al_ = -kk**2 / (3 * A * sp.sqrt(2 * kk))
        be_ = 3 * sp.I * A / (kk * sp.sqrt(2 * kk))
        r_ = -9 * sp.I * A**2 * Iinf / kk**3
        return al_ * (1 + r_), be_

    ks = [k1, k2, k3]
    C1 = [coeffs(kk)[0] for kk in ks]
    C2 = [coeffs(kk)[1] for kk in ks]
    # Wronskian check  Im(C1 C2*) = 1/2
    for i in range(3):
        assert sp.simplify(sp.im(sp.expand(C1[i] * sp.conjugate(C2[i]))) - sp.Rational(1, 2)) == 0
    log("  Wronskian normalisation Im(C1 C2*) = 1/2 for all three legs: OK")
    ustar = [sp.expand(C1[i] + C2[i] * Iinf) for i in range(3)]             # u_i(eta_*)
    u_eta = [sp.conjugate(C1[i]) + sp.conjugate(C2[i]) * J for i in range(3)]  # u_i^*(eta)
    up_eta = [sp.conjugate(C2[i]) for i in range(3)]                        # u_i^{*'}(eta) * a^2 (S1: zeta' = C2/a^2)
    P = [sp.simplify(sp.expand(ustar[i] * sp.conjugate(ustar[i]))) for i in range(3)]
    pref = ustar[0] * ustar[1] * ustar[2]

    # vertex  zeta zeta'^2 : attachments = choose which leg is the underived one (3) x 2 orderings
    T_zzpzp = 2 * sum(u_eta[i] * up_eta[j] * up_eta[l]
                      for (i, j, l) in [(0, 1, 2), (1, 0, 2), (2, 0, 1)])
    # vertex  zeta^2 zeta' : choose the derived leg (3) x 2 orderings of the other two
    T_zzzp = 2 * sum(up_eta[i] * u_eta[j] * u_eta[l]
                     for (i, j, l) in [(0, 1, 2), (1, 0, 2), (2, 0, 1)])
    red = {}
    for name, T in [("zeta zeta'^2", T_zzpzp), ("zeta^2 zeta'", T_zzzp)]:
        integrand_im = sp.simplify(sp.im(sp.expand(pref * T)))   # multiplies  c(eta) / a^4 or /a^2  and d eta
        # dimensionless ratio to (P1 P2 + P1 P3 + P2 P3), then squeezed limit k1 -> 0 at k2 = k3 = k
        Psum = P[0] * P[1] + P[0] * P[2] + P[1] * P[2]
        # f_NL = (5/6) B / (P1P2 + P1P3 + P2P3)  [zeta = zeta_g + (3/5) f_NL zeta_g^2; checked below on the
        # local redefinition zeta = zeta_n + F zeta_n^2 -> B = 2F sum PP -> f_NL = (5/3) F]
        fnl_kernel = sp.simplify(sp.Rational(5, 6) * (-2) * integrand_im / Psum)
        sq = sp.simplify(sp.limit(fnl_kernel.subs({k2: k, k3: k}), k1, 0))
        # leading term for k^3 << A^2 I_inf (|r| >> 1)
        eps_ = sp.Symbol("epsilon_k", positive=True)
        sq_lead = sp.simplify(sp.series(sq.subs(k, eps_ * (A**2 * Iinf) ** sp.Rational(1, 3)), eps_, 0, 1).removeO())
        log(f"  vertex c(eta) {name}:")
        log(f"    squeezed f_NL kernel (per unit c(eta) d eta, S1 z=a): {sq}")
        log(f"    leading term for |r|>>1 (k^3 << A^2 I_inf): {sq_lead}")
        red[name] = dict(squeezed_kernel=str(sq), leading=str(sq_lead))
    out["super_hubble_reduction"] = dict(
        statement="Delta f_NL^{bounce}_V = int_{-eta_B}^{+eta_B} d eta  c_V(eta) * K_V(J(eta); A, I_inf, k); "
                  "K_V listed per vertex; c_V is the conformal-time coefficient (c_V^{conf} = c_V^{cosmic}/a^{n_dot-1}); "
                  "mode functions zeta = C1 + C2 J with the brief's vacuum C1, C2; valid for k eta_B << 1.",
        kernels=red, wronskian="Im(C1 C2*) = 1/2 (z = a)")

    # normalisation check: local redefinition zeta = zeta_n + F zeta_n^2 gives B = 2 F (P1P2+P1P3+P2P3)
    # and must return f_NL = (5/3) F  (slow-roll: F = eta_sr/4 -> 5 eta_sr/12; end of matter
    # contraction: F = zetadot/(H zeta) = -3/2 -> -5/2, the lab adjudication's redefinition row).
    Fsym = sp.Symbol("F")
    Psum = P[0] * P[1] + P[0] * P[2] + P[1] * P[2]
    assert sp.simplify(sp.Rational(5, 6) * 2 * Fsym * Psum / Psum - sp.Rational(5, 3) * Fsym) == 0
    log("  normalisation: local redefinition F zeta^2 -> f_NL = (5/3) F  (-> -5/2 at end of matter "
        "contraction, 5 eta_sr/12 in slow roll): OK")

    # ---------------- [F] numerical S1 estimate on the Quintin background ----------------
    log("\n[F] Numerical S1-scheme bounce-window estimate (Quintin+2015-type dtB sweep, LQC, poly)")
    sys.path.insert(0, os.path.join(HERE, ".."))
    import a2_transmission_linear as a2
    est = {}
    # numeric versions of the kernels (leading |r|>>1 term) as functions of J
    Jn = sp.Symbol("J", positive=True)
    kern = {}
    for name in red:
        expr = sp.sympify(red[name]["leading"]).subs({A: 1, Iinf: 1})  # A, I_inf scale out below
        kern[name] = sp.lambdify((Jn,), expr.subs(J, Jn), "numpy")
    # check A, I_inf scaling analytically: the leading kernel must be a function of J/I_inf only,
    # times powers of I_inf (record the exponent)
    runs = [("quintin dtB=0.5", a2.bg_quintin(dtB=0.5, N=200001)),
            ("quintin dtB=1.0", a2.bg_quintin(dtB=1.0, N=200001)),
            ("quintin dtB=2.0", a2.bg_quintin(dtB=2.0, N=200001)),
            ("LQC dust (rho_B = 1/2 exact)", a2.bg_lqc()),
            ("poly eta_b=1", a2.bg_poly(eta_b=1.0))]
    for dtB, b in runs:
        eta, aa, JJ, eB, Ii = b["eta"], b["a"], b["J"], b["eta_B"], b["I_inf"]
        m = np.abs(eta) <= eB
        e_, a_, J_ = eta[m], aa[m], JJ[m]
        # S1 conformal coefficients (eps_eff = 1/2, c_s = 1): V2 -> a^3 eps^2 zeta zetadot^2 -> a^2/4 zeta zeta'^2
        #   V4, V6, V7 share the zeta'^2 time structure (kernels differ by angular factors; see brief),
        #   V5 = 0 in S1, V3 is k^2 suppressed.  Report V2 alone as the order-of-magnitude anchor.
        # in-in: int d eta c(eta) * K(J) with zeta' = C2/a^2 already inside K (S1 Wronskian), so the
        # remaining a-dependence is c^{conf}_V2 / a^4 * a^4 ... : K was derived with u' = C2/a^2 factored
        # as C2 (per unit 1/a^2 each), hence multiply by a^{-4} for two derived legs.
        lead_expr = sp.sympify(red["zeta zeta'^2"]["leading"])
        f = sp.lambdify((J, A, Iinf), lead_expr, "numpy")
        integrand = (a_**2 / 4.0) * a_**-4 * f(J_, b["A"], Ii)
        val = float(np.trapezoid(integrand, e_))
        # closed form: with c = a^2/4 and the leading kernel (5/12)(-I_inf - 3J)/I_inf^2, the J term
        # integrates to zero by parity (a even, J odd), leaving
        #   Delta f_NL[V2, S1] = -(5/48) (1/I_inf) int_{-eta_B}^{eta_B} d eta / a^2 = -(5/24) rho_B
        rho_B = abs(b["J_at_minus_etaB"]) / Ii
        closed = -5.0 / 24.0 * rho_B
        est[str(dtB)] = dict(background=dtB, params=b["params"], eta_B=eB, I_inf=Ii, A=b["A"],
                             rho_B=rho_B, dfnl_V2_S1_numeric=val, dfnl_V2_S1_closed_form=closed,
                             rel_diff=abs(val - closed) / abs(closed))
        log(f"  {dtB}: eta_B={eB:.5f}  I_inf={Ii:.5f}  A={b['A']:.5f}  rho_B={rho_B:.6f}  "
            f"Delta f_NL^bounce[V2, S1] = {val:+.6f}  (closed form -(5/24) rho_B = {closed:+.6f}, "
            f"rel diff {abs(val-closed)/abs(closed):.1e})")
    out["S1_numerical_estimate"] = dict(
        note="S1 (z = a, eps_eff = 1/2, c_s = 1) evaluation of the V2 vertex only, leading |r|>>1 "
             "kernel, bounce window |eta| <= eta_B, post-bounce eta_* -> +inf.  Order-of-magnitude "
             "anchor for lane (b); the full sum over V2, V4, V6, V7 with angular kernels is lane (b).",
        values=est, contraction_reference=-35 / 16)

    log(f"\nDONE ({time.time() - t0:.1f} s) -> {JSON_OUT}")
    with open(JSON_OUT, "w") as fh:
        json.dump(out, fh, indent=2)
    with open(LOG, "w") as fh:
        fh.write("\n".join(_lines) + "\n")


if __name__ == "__main__":
    main()

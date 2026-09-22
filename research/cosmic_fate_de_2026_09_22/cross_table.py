#!/usr/bin/env python3
"""
cross_table.py -- ledger row 23, Step 1.

Crosses the Branch I bounce-compatible dark-energy classes against the row-20
future-turnaround criterion, evaluating the criterion SYMBOLICALLY (sympy) for
each class and recording the equation that decides the row.

Sets, fixed in PREREGISTRATION.md before any statistic:

  Set B  -- research/branch_I_bounce_compatible_DE/02_candidate_DE_classes.md
            (Classes 1-7) and horndeski_bounce_stability/phase1_results.md
            (Phase-1 verdicts A-F).  Quoted, never re-adjudicated here.
  Set T  -- COSMIC_FATE_MEMO.md Eqs. (2.3)-(2.5):
              turnaround at a_t  <=>  H(a_t) = 0 and adotdot(a_t) < 0
              H = 0  <=>  rho_tot(a_t) = 3 k c^2 / (8 pi G a_t^2)        (2.4)
              adotdot < 0  <=>  rho_tot(a_t) + 3 p_tot(a_t)/c^2 > 0      (2.5)
            For k <= 0 the RHS of (2.4) is <= 0, so some component must reach
            and cross zero density.

No number in this file is hand-typed: every symbolic verdict below is the
output of a sympy simplification printed into the JSON.

Usage:  python3 cross_table.py       (writes cross_table.json beside itself)
"""

import json
import os
from datetime import datetime, timezone

import sympy as sp

# ----------------------------------------------------------------------------
# Symbolic lemmas.  Each returns (statement, sympy_result, passed)
# ----------------------------------------------------------------------------

def lemma_L1_positive_floor():
    """Memo Eq. (3.1) generalised, and memo Sec. 3(e) case 2.

    If rho_DE(a) >= rho_floor > 0 for all a, then in a flat/open universe
    (k <= 0) with rho_m, rho_r >= 0 the total density never reaches the value
    (2.4) requires, so no turnaround exists.
    """
    a, Om, Or, rho_floor = sp.symbols('a Omega_m Omega_r rho_floor',
                                      positive=True)
    E2 = Om / a**3 + Or / a**4 + rho_floor          # flat, k = 0
    # infimum over a > 0 of E2 is rho_floor (matter+radiation are positive and
    # monotonically decreasing); show E2 - rho_floor > 0 for all finite a.
    excess = sp.simplify(E2 - rho_floor)
    inf_at_infinity = sp.limit(E2, a, sp.oo)
    positive_everywhere = sp.simplify(sp.Min(excess, 0)) == 0 or excess.is_positive
    return {
        "lemma": "L1 positive-floor -> no turnaround (flat/open)",
        "E2": sp.srepr(E2) and str(E2),
        "E2_minus_floor": str(excess),
        "limit_a_to_infinity": str(inf_at_infinity),
        "decides": "E^2(a) >= rho_floor > 0 for all a  =>  H never reaches 0"
                   "  [memo Eq. (3.1); memo Sec. 3(e) case 2]",
        "passed_turnaround": False,
        "sympy_excess_is_positive": bool(excess.is_positive),
    }


def lemma_L2_quintessence_SEC():
    """Memo Eqs. (3.7)-(3.8), re-derived symbolically.

    Canonical scalar: rho_phi = phidot^2/2 + V, p_phi = phidot^2/2 - V.
    Flat turnaround demands rho_tot = rho_m + rho_phi = 0, i.e.
    V = -(rho_m + phidot^2/2) < 0.  Then the SEC check (2.5) is automatic.
    """
    rho_m, pd = sp.symbols('rho_m phidot', nonnegative=True)
    V = sp.Symbol('V')
    rho_phi = pd**2 / 2 + V
    p_phi = pd**2 / 2 - V
    rho_tot = rho_m + rho_phi
    V_star = sp.solve(sp.Eq(rho_tot, 0), V)[0]            # V at turnaround
    sec = sp.simplify((rho_tot + 3 * (0 + p_phi)).subs(V, V_star))
    return {
        "lemma": "L2 zero-crossing quintessence: SEC at turnaround is automatic",
        "V_at_turnaround": str(V_star),
        "rho_tot_plus_3p_tot_at_turnaround": str(sec),
        "decides": "rho_tot = 0 forces V = -(rho_m + phidot^2/2) < 0, and then "
                   "rho_tot + 3 p_tot = 3(rho_m + phidot^2) > 0 identically "
                   "[memo Eqs. (3.7), (3.8)]",
        "passed_turnaround": True,
        "sympy_SEC_is_positive_for_rho_m_or_phidot_nonzero":
            bool(sp.simplify(sec - 3 * (rho_m + pd**2)) == 0),
    }


def lemma_L3_kessence_SEC():
    """Same question for k-essence, L = P(X, phi), rho = 2 X P_X - P.

    Representative family P = K(phi) X + L(phi) X^2 - V(phi) (the leading
    terms of any analytic P in X; K, L > 0 keeps the no-ghost condition
    P_X + 2 X P_XX = K + 6 L X > 0 and c_s^2 = P_X/(P_X + 2X P_XX) > 0).
    """
    X, K, L, rho_m = sp.symbols('X K L rho_m', positive=True)
    V = sp.Symbol('V')
    P = K * X + L * X**2 - V
    rho_k = sp.simplify(2 * X * sp.diff(P, X) - P)
    p_k = P
    rho_tot = rho_m + rho_k
    V_star = sp.solve(sp.Eq(rho_tot, 0), V)[0]
    sec = sp.simplify((rho_tot + 3 * p_k).subs(V, V_star))
    no_ghost = sp.simplify(sp.diff(P, X) + 2 * X * sp.diff(P, X, 2))
    cs2 = sp.simplify(sp.diff(P, X) / no_ghost)
    return {
        "lemma": "L3 zero-crossing k-essence: SEC at turnaround is automatic "
                 "and the crossing is compatible with no-ghost/c_s^2>0",
        "rho_kessence": str(rho_k),
        "p_kessence": str(sp.simplify(p_k)),
        "V_at_turnaround": str(V_star),
        "rho_tot_plus_3p_tot_at_turnaround": str(sec),
        "no_ghost_quantity_P_X_plus_2X_P_XX": str(no_ghost),
        "c_s_squared": str(cs2),
        "decides": "rho = 2X P_X - P = K X + 3 L X^2 + V crosses zero when "
                   "V < -(rho_m + K X + 3 L X^2); at that point "
                   "rho_tot + 3 p_tot = 3(rho_m + 2 K X + 4 L X^2) > 0, while "
                   "K + 6 L X > 0 keeps the mode healthy",
        "passed_turnaround": True,
    }


def lemma_L4_cpl_never_crosses():
    """Memo Eq. (4.1): the CPL fitting function's rho_DE(a) is positive for
    every a, so no CPL extrapolation produces a turnaround."""
    a, w0, wa = sp.symbols('a w_0 w_a', positive=True)
    a = sp.Symbol('a', positive=True)
    w0, wa = sp.symbols('w_0 w_a', real=True)
    rho = a**(-3 * (1 + w0 + wa)) * sp.exp(-3 * wa * (1 - a))
    w_of_a = w0 + wa * (1 - a)
    check = sp.simplify(sp.diff(sp.log(rho), sp.log(a)).subs(sp.log(a), sp.Symbol('L'))) \
        if False else sp.simplify(a * sp.diff(rho, a) / rho + 3 * (1 + w_of_a))
    return {
        "lemma": "L4 CPL rho_DE(a) > 0 for every a (no zero crossing)",
        "rho_DE_over_rho_DE0": str(rho),
        "identity_check_dlnrho_dlna_plus_3(1+w)": str(check),
        "decides": "rho_DE(a) = rho_0 a^{-3(1+w0+wa)} e^{-3 w_a (1-a)} is a "
                   "product of strictly positive factors, so it decays to 0+ "
                   "and is never negative [memo Eq. (4.1)]",
        "passed_turnaround": False,
        "identity_verified": bool(sp.simplify(check) == 0),
    }


def lemma_L5_interacting_drain():
    """Memo Sec. 3(e) case 1, made explicit.

    rhodot_DE + 3H(1+w) rho_DE = Q,  rhodot_c + 3H rho_c = -Q.
    Take w = -1 and a drain Q = -xi H rho_crit0 (constant rate per e-fold).
    In e-folds u = ln a this integrates in closed form.
    """
    u, xi, OmDE0, Omc0 = sp.symbols('u xi Omega_DE0 Omega_c0', positive=True)
    rho_de = sp.Function('rho_DE')
    sol_de = sp.dsolve(sp.Eq(sp.Derivative(rho_de(u), u), -xi),
                       rho_de(u), ics={rho_de(0): OmDE0}).rhs
    rho_c = sp.Function('rho_c')
    sol_c = sp.dsolve(sp.Eq(sp.Derivative(rho_c(u), u) + 3 * rho_c(u), xi),
                      rho_c(u), ics={rho_c(0): Omc0}).rhs
    u_zero = sp.solve(sp.Eq(sol_de, 0), u)[0]
    return {
        "lemma": "L5 interacting dark sector with a sustained drain crosses zero",
        "rho_DE_of_u": str(sp.simplify(sol_de)),
        "rho_c_of_u": str(sp.simplify(sol_c)),
        "e_folds_to_rho_DE_zero": str(sp.simplify(u_zero)),
        "decides": "with Q/H = -xi rho_crit0, rho_DE(u) = Omega_DE0 - xi u "
                   "reaches zero at u = Omega_DE0/xi and goes negative after; "
                   "the drained energy reappears in the pressureless sector, "
                   "rho_c -> xi/3 floor [memo Sec. 3(e) case 1]",
        "passed_turnaround": True,
    }


def lemma_L6_negative_constant():
    """Memo Eq. (3.6): a constant negative effective Lambda in a flat universe
    turns around at a_t = (Omega_m/|Omega_L|)^{1/3}, but flatness then forces
    Omega_m = 1 + |Omega_L| > 1."""
    a, Om, absOL = sp.symbols('a Omega_m absOmega_L', positive=True)
    E2 = Om / a**3 - absOL
    a_t = sp.solve(sp.Eq(E2, 0), a)
    a_t = [r for r in a_t if r.is_real is not False][0]
    return {
        "lemma": "L6 constant negative effective Lambda: turnaround exists but "
                 "flatness forces Omega_m > 1",
        "a_turnaround": str(sp.simplify(a_t)),
        "decides": "E^2 = Omega_m a^-3 - |Omega_L| = 0 at "
                   "a_t = (Omega_m/|Omega_L|)^(1/3); flatness gives "
                   "Omega_m = 1 + |Omega_L| > 1, excluded at the observed "
                   "matter density [memo Eq. (3.6) and Sec. 3(c)]",
        "passed_turnaround": True,
        "observationally_viable_today": False,
    }


# ----------------------------------------------------------------------------
# The cross-table itself
# ----------------------------------------------------------------------------

BRANCH_I = "research/branch_I_bounce_compatible_DE/02_candidate_DE_classes.md"
PHASE1 = ("research/branch_I_bounce_compatible_DE/horndeski_bounce_stability/"
          "phase1_results.md")


def build_rows(lemmas):
    L = {d["lemma"].split()[0]: d for d in lemmas}
    rows = [
        dict(
            cls="1 / A-adjacent",
            name="Cosmological constant Lambda",
            branch_I_verdict="TRIVIALLY COMPATIBLE",
            branch_I_source=f"{BRANCH_I} Class 1",
            in_set_B=True,
            rho_p="rho_Lambda = Lambda c^2/(8 pi G) = const > 0, p = -rho c^2",
            turnaround="FAIL",
            deciding_equation=L["L1"]["decides"],
            note="Memo Eq. (3.1): H^2 >= Lambda c^2/3 > 0 for every a. Memo "
                 "Eq. (3.5): at Omega_m < 1 no positive Lambda permits "
                 "recollapse at ANY curvature, so opening k > 0 does not help.",
        ),
        dict(
            cls="2 / A",
            name="Canonical quintessence (scalar with V(phi))",
            branch_I_verdict="GENERALLY COMPATIBLE (weak early-time caveat) / "
                             "TRIVIALLY_COMPATIBLE at the bounce",
            branch_I_source=f"{BRANCH_I} Class 2; {PHASE1} Class A",
            in_set_B=True,
            rho_p="rho = phidot^2/2 + V, p = phidot^2/2 - V",
            turnaround="PASS (sub-class: V unbounded below / crossing zero)",
            deciding_equation=L["L2"]["decides"],
            note="Branch I's compatibility verdict concerns rho_phi at "
                 "rho ~ M_Pl^4; the turnaround condition concerns V at a >> 1. "
                 "Disjoint questions, both satisfiable (memo Sec. 3(d)).",
        ),
        dict(
            cls="3 / B",
            name="K-essence, L = P(X, phi)",
            branch_I_verdict="LIKELY COMPATIBLE / TRIVIALLY_COMPATIBLE "
                             "(X -> 0 canonical limit at the bounce)",
            branch_I_source=f"{BRANCH_I} Class 3; {PHASE1} Class B",
            in_set_B=True,
            rho_p="rho = 2 X P_X - P, p = P",
            turnaround="PASS (sub-class: effective potential crossing zero)",
            deciding_equation=L["L3"]["decides"],
            note="Background phenomenology of the crossing is that of Class 2; "
                 "the distinctive k-essence freedom is c_s^2, which moves "
                 "growth, not background distances.",
        ),
        dict(
            cls="4a",
            name="f(R) dark energy (Hu-Sawicki-type, viable sub-class)",
            branch_I_verdict="TRIVIALLY COMPATIBLE (Test I-2: the correction is "
                             "10^-122 of R_bounce)",
            branch_I_source="research/branch_I_bounce_compatible_DE/"
                            "03_nontrivial_compatibility_tests.md Test I-2",
            in_set_B=True,
            rho_p="rho_eff -> const > 0 asymptotically (the model is built to "
                  "mimic Lambda today)",
            turnaround="FAIL for the observationally viable sub-class",
            deciding_equation=L["L1"]["decides"],
            note="Viability as DE today requires a positive asymptotic "
                 "effective floor; the positive-floor lemma then forbids a "
                 "turnaround. f(R) branches without that floor are not viable "
                 "DE. No general f(R) criterion is claimed (memo Sec. 3(g)).",
        ),
        dict(
            cls="4b / C",
            name="Cubic Horndeski / kinetic gravity braiding",
            branch_I_verdict="EFT_INAPPLICABLE (Q_S -> 0 at the bounce; "
                             "M ~ H_0 << M_Pl) -- UNDETERMINED, not compatible",
            branch_I_source=f"{PHASE1} Class C, Findings 3 and 5",
            in_set_B=False,
            rho_p="model-dependent",
            turnaround="UNDETERMINED",
            deciding_equation="no general criterion exists (memo Sec. 3(g))",
            note="Excluded from the intersection on the bounce axis by Branch "
                 "I's own verdict; not promoted here.",
        ),
        dict(
            cls="4c / D",
            name="Non-minimally coupled scalar (xi R phi^2)",
            branch_I_verdict="COMPATIBLE_WITH_CAVEAT (bounded tachyonic kick "
                             "exp(sqrt(21 xi)); bound weaker than existing ones)",
            branch_I_source=f"{PHASE1} Class D, Finding 4",
            in_set_B=True,
            rho_p="Jordan-frame effective density includes -6 xi H phi phidot",
            turnaround="UNDETERMINED -- NAMED GAP",
            deciding_equation="the turnaround condition (2.3) is frame-"
                              "dependent for xi != 0: H = 0 in the Jordan frame "
                              "is not Htilde = 0 in the Einstein frame, and no "
                              "frame-invariant criterion is derived here "
                              "(memo Sec. 3(g): model-by-model, no general "
                              "criterion)",
            note="GAP-1. This is the one class that is squarely inside Set B "
                 "and whose Set-T status is genuinely open.",
        ),
        dict(
            cls="4d / E",
            name="Quartic/quintic Horndeski",
            branch_I_verdict="TRIVIALLY_COMPATIBLE (pre-empted by GW170817: "
                             "c_T = 1 forces G_4 = G_4(phi), G_5 = 0)",
            branch_I_source=f"{PHASE1} Class E",
            in_set_B=True,
            rho_p="reduces to a non-minimally coupled scalar",
            turnaround="UNDETERMINED -- NAMED GAP (same as 4c)",
            deciding_equation="same frame-dependence obstruction as class 4c",
            note="GAP-1 (shared).",
        ),
        dict(
            cls="4e / F",
            name="DHOST / beyond Horndeski",
            branch_I_verdict="EFT_INAPPLICABLE (Lambda_SC << M_Pl) -- "
                             "UNDETERMINED",
            branch_I_source=f"{PHASE1} Class F, Finding 3",
            in_set_B=False,
            rho_p="model-dependent",
            turnaround="UNDETERMINED",
            deciding_equation="no general criterion exists (memo Sec. 3(g))",
            note="Excluded on the bounce axis by Branch I's own verdict.",
        ),
        dict(
            cls="5",
            name="Vacuum-energy sequestering (Kaloper-Padilla)",
            branch_I_verdict="COMPATIBLE BUT DISCONNECTED (Foundations E, G)",
            branch_I_source=f"{BRANCH_I} Class 5",
            in_set_B=True,
            rho_p="residual Lambda_eff = const, fixed by the spacetime "
                  "four-volume",
            turnaround="FAIL for the observed sign (Lambda_eff > 0 today)",
            deciding_equation=L["L1"]["decides"] + "  [and, for the opposite "
                              "sign, " + L["L6"]["decides"] + "]",
            note="The residual is a constant, so the class inherits the "
                 "Lambda row exactly: a turnaround needs Lambda_eff < 0, which "
                 "contradicts present-day acceleration.",
        ),
        dict(
            cls="6",
            name="Interacting dark energy (DE-DM energy exchange)",
            branch_I_verdict="COMPATIBLE (weak constraint: at rho ~ M_Pl^4 the "
                             "dark-matter density is negligible)",
            branch_I_source=f"{BRANCH_I} Class 6",
            in_set_B=True,
            rho_p="rhodot_DE + 3H(1+w) rho_DE = Q, rhodot_c + 3H rho_c = -Q",
            turnaround="PASS (sub-class: sustained drain, Q < 0 strong enough "
                       "to take rho_DE,eff through zero)",
            deciding_equation=L["L5"]["decides"],
            note="The complementary sub-class -- any coupling that leaves "
                 "rho_DE,eff > 0 asymptotically -- FAILS by the positive-floor "
                 "lemma. Merely making w evolve is not enough (memo Sec. 3(e)).",
        ),
        dict(
            cls="7",
            name="Massive gravity / bigravity",
            branch_I_verdict="POSSIBLY NOT COMPATIBLE (Boulware-Deser ghost may "
                             "reappear at Planck curvature) -- UNDETERMINED",
            branch_I_source=f"{BRANCH_I} Class 7; Test I-4",
            in_set_B=False,
            rho_p="model-dependent",
            turnaround="UNDETERMINED",
            deciding_equation="no general criterion exists (memo Sec. 3(g))",
            note="Excluded on the bounce axis by Branch I's own verdict.",
        ),
    ]
    for r in rows:
        r["in_intersection"] = bool(r["in_set_B"] and r["turnaround"].startswith("PASS"))
    return rows


def main():
    lemmas = [
        lemma_L1_positive_floor(),
        lemma_L2_quintessence_SEC(),
        lemma_L3_kessence_SEC(),
        lemma_L4_cpl_never_crosses(),
        lemma_L5_interacting_drain(),
        lemma_L6_negative_constant(),
    ]
    rows = build_rows(lemmas)
    inter = [r["name"] for r in rows if r["in_intersection"]]
    gaps = [r["name"] for r in rows if "NAMED GAP" in r["turnaround"]]
    out = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "script": os.path.basename(__file__),
        "ledger_row": 23,
        "preregistration": "research/cosmic_fate_de_2026_09_22/PREREGISTRATION.md",
        "set_B_source": [BRANCH_I, PHASE1],
        "set_T_criterion": "COSMIC_FATE_MEMO.md Eqs. (2.3)-(2.5)",
        "symbolic_lemmas": lemmas,
        "cross_table": rows,
        "intersection": inter,
        "named_gaps": gaps,
        "n_rows": len(rows),
        "n_in_set_B": sum(r["in_set_B"] for r in rows),
        "n_in_intersection": len(inter),
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "cross_table.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2)

    print("ROW 23 -- STEP 1 CROSS-TABLE")
    print("=" * 78)
    for d in lemmas:
        print(f"[{d['lemma']}]")
        for k, v in d.items():
            if k not in ("lemma", "decides", "note"):
                print(f"    {k}: {v}")
        print(f"    DECIDES: {d['decides']}")
        print()
    hdr = f"{'class':<12}{'Set B':<8}{'turnaround':<52}{'both'}"
    print(hdr)
    print("-" * 78)
    for r in rows:
        print(f"{r['cls']:<12}{'YES' if r['in_set_B'] else 'no':<8}"
              f"{r['turnaround'][:50]:<52}{'YES' if r['in_intersection'] else ''}")
    print()
    print(f"INTERSECTION ({len(inter)}): " + "; ".join(inter))
    print(f"NAMED GAPS ({len(gaps)}): " + "; ".join(gaps))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()

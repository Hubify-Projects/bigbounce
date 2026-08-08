#!/usr/bin/env python3
r"""
G3 (open-compute gate) — MODEL-SPECIFIC EINSTEIN--CARTAN FOUR-FERMION TORSION
BOUND on the P2 matter-bounce f_NL claim.

Context (P2 assumption (f), 02_full_draft.tex L1102 / L1036):
  P2 headlines the contraction-phase local amplitude f_NL^local = -35/16, fixed
  symbolically by the exact four-vertex sum. Assumption (f) states "negligible
  fermion-sourced torsion during contraction and the bounce", and the tex
  explicitly flags this as "automatic only in the scalar-only sector; models with
  appreciable fermion populations require an explicit bound on the
  Einstein--Cartan four-fermion operator." No script existed. This produces the
  bound.

WHAT IS ANCHORED TO COMMITTED P1A CONVENTIONS (arxiv/paper1a_ech_nogo.tex):
  P1A convention-audited the whole Einstein--Cartan torsion-elimination machinery.
  We REUSE its exact conventions (no re-derivation of quantities P1A already
  certified; every reused number cites the P1A line/equation):

  [P1A-1] Axial--axial contact term after ALGEBRAIC Cartan elimination
          (P1A abstract, tex L1161-1162; body Eq. cross-ref L856 "Hehl-Datta net
          +kappa/2 S.S -> -3kappa/16 (J5)^2"):
             L_contact = -(3 kappa / 16) * [gamma^2/(1+gamma^2)] * J_5^2 ,
          kappa = 8 pi G (unreduced), gamma = Barbero--Immirzi parameter,
          J_5^I = psibar gamma^I gamma^5 psi the axial (spin) current. The scalar
          Fierz projection coefficient is G_s = -3 kappa/16 (P1A L1172), and the
          finite-Holst factor is gamma^2/(1+gamma^2) (P1A L1162, L204).

  [P1A-2] Dimensional benchmark (P1A abstract L1163-1165, "coefficient-one"):
             kappa n_psi^2 / rho_Lambda ~= 3.6e-69 (n_psi/100 cm^-3)^2 ,
          the v117 EXACT convention giving kappa n_psi^2 = 9.9542e-80 eV^4 at
          n_psi = 100 cm^-3 (P1A comment block near L737). P1A explicitly notes
          number density does NOT fix the renormalized composite <J_5^I J_{5I}>;
          n_psi^2 is used here as the MAXIMAL (spin-coherent) OOM proxy, i.e. the
          conservative upper bound, exactly as P1A frames it.

  [P1A-3] Unit machinery (P1A comment block L735-737):
             hbar c = 1.973e-5 eV cm  =>  1 cm^-3 = (1.973e-5)^3 eV^3 = 7.680e-15 eV^3
             M_Pl (unreduced) = 1.22e28 eV  =>  M_Pl^2 = 1.49e56 eV^2
             kappa = 8 pi G = 8 pi / M_Pl^2 = 1.689e-55 eV^-2.

PHYSICS OF THE BOUND (order-of-magnitude, honest):
  The torsion four-fermion contact term contributes a fractional energy density
     rho_tor/rho = (3/16) [gamma^2/(1+gamma^2)] kappa <J_5^2> / rho
  with <J_5^2> <~ n_psi^2 (P1A-2, conservative). Any torsion-sourced correction to
  a curvature-sector observable is bounded by this fractional energy density times
  the observable it perturbs, so
     |delta f_NL^tor| <~ |f_NL^scalar| * (rho_tor/rho) ,   |f_NL^scalar| = 35/16.

  EPOCH DEPENDENCE (uses the COMMITTED P2 quasi-dust background of Phase-1,
  g1_gradient_transmission_scheme.py [B]): rho = rho_c (a_b/a)^3, and a matter/dust
  fermion number density dilutes as n_psi ∝ a^-3 ∝ rho. Hence n_psi = n_psi,c *
  (rho/rho_c) with n_psi,c the bounce-epoch value, and
     rho_tor/rho = (3/16)[gamma^2/(1+gamma^2)] kappa n_psi,c^2 (rho/rho_c^2),
  which GROWS linearly in rho and is MAXIMAL at the bounce rho=rho_c:
     (rho_tor/rho)_max = (3/16)[gamma^2/(1+gamma^2)] kappa n_psi,c^2 / rho_c.
  The bound is therefore controlled entirely by the bounce-epoch fermion number
  density n_psi,c and the LQC critical density rho_c:

     |delta f_NL^tor| <~ (35/16)(3/16)[gamma^2/(1+gamma^2)] * (kappa n_psi,c^2/rho_c).

  n_psi,c is NOT fixed by any committed artifact (it is the free fermion abundance
  of the bounce model). We therefore present the bound as an explicit FUNCTION of
  n_psi,c (equivalently of the dimensionless x_psi = kappa n_psi,c^2/rho_c), give
  the CRITICAL density at which torsion becomes non-negligible, and evaluate a few
  clearly-labelled illustrative fiducials. NO value of n_psi,c is invented.

INTEGRITY (pattern-036 / never-fabricate-derivation): the contact coefficient,
Holst factor, unit machinery, and benchmark are all reused verbatim from the
convention-audited P1A (citations above). The epoch scaling uses the committed
P2 Phase-1 background. Every number below is a computed output; the free
parameter n_psi,c is carried symbolically and never assigned a fabricated value.
NO paper edit; NO version bump.
"""
import json
import os
import time
from datetime import datetime, timezone

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
JSON_OUT = os.path.join(HERE, "g3_torsion_fourfermion_bound.json")
LOG_OUT = os.path.join(HERE, "g3_torsion_fourfermion_bound.log")

_t0 = time.time()


def log(m):
    line = f"[{time.time()-_t0:7.2f}s] {m}"
    print(line, flush=True)
    with open(LOG_OUT, "a") as f:
        f.write(line + "\n")


# ==========================================================================
# [A] SYMBOLIC BOUND (sympy). Assemble the prefactor from the P1A conventions
#     and the P2 quasi-dust epoch scaling; carry n_psi,c symbolically.
# ==========================================================================
def symbolic_bound():
    gamma, kappa, n_c, rho_c, rho = sp.symbols(
        'gamma kappa n_psi_c rho_c rho', positive=True)

    fNL_scalar = sp.Rational(35, 16)                 # |f_NL| amplitude, P2 headline
    Gs_mag = sp.Rational(3, 16)                       # |G_s|/kappa, P1A L1172 (-3kappa/16)
    holst = gamma**2 / (1 + gamma**2)                # finite-Holst factor, P1A L1162

    # Fractional torsion energy density at general epoch rho, using n_psi ∝ rho:
    n_psi = n_c * (rho / rho_c)                       # dust dilution ∝ a^-3 ∝ rho
    frac_tor = Gs_mag * holst * kappa * n_psi**2 / rho
    frac_tor = sp.simplify(frac_tor)                 # = (3/16) holst kappa n_c^2 rho/rho_c^2

    # Maximal at the bounce rho = rho_c:
    frac_tor_bounce = sp.simplify(frac_tor.subs(rho, rho_c))

    # The delta f_NL bound (function of n_psi,c, gamma, rho_c):
    dfNL = sp.simplify(fNL_scalar * frac_tor_bounce)
    # dimensionless drive x_psi = kappa n_c^2 / rho_c:
    x_psi = sp.symbols('x_psi', positive=True)
    dfNL_of_x = sp.simplify(dfNL.subs(kappa * n_c**2 / rho_c, x_psi))
    # (sympy won't auto-substitute the product; build the reduced form directly)
    prefactor = sp.simplify(fNL_scalar * Gs_mag * holst)   # multiplies x_psi
    dfNL_reduced = prefactor * x_psi                       # |delta f_NL| <~ prefactor * x_psi

    return {
        "symbols": "gamma=Immirzi, kappa=8piG, n_psi_c=bounce-epoch fermion number density, rho_c=LQC critical density",
        "frac_tor_general_epoch": str(frac_tor),
        "frac_tor_at_bounce": str(frac_tor_bounce),
        "dfNL_bound_full": str(dfNL),
        "dfNL_bound_reduced": "|delta_fNL_tor| <~ (%s) * x_psi,  x_psi = kappa*n_psi_c^2/rho_c" % str(prefactor),
        "prefactor_symbolic": str(prefactor),
        "epoch_scaling": "n_psi ∝ a^-3 ∝ rho (committed P2 quasi-dust); frac_tor ∝ rho, maximal at bounce",
    }, (gamma, prefactor, x_psi)


# ==========================================================================
# [B] NUMERIC EVALUATION with full provenance. All constants cite P1A L735-737.
# ==========================================================================
def numeric_eval():
    import mpmath as mp
    mp.mp.dps = 30

    # --- P1A unit machinery (P1A comment block L735-737), reused verbatim ---
    hbar_c_eV_cm = mp.mpf('1.973e-5')                 # eV cm (P1A L735)
    cm_inv3_in_eV3 = hbar_c_eV_cm**3                  # 1 cm^-3 in eV^3 = 7.680e-15
    M_Pl_eV = mp.mpf('1.22e28')                       # unreduced (P1A L737)
    M_Pl2 = M_Pl_eV**2                                # 1.4884e56 eV^2
    kappa = 8 * mp.pi / M_Pl2                          # 8 pi G, G = 1/M_Pl^2 (unreduced)

    # --- P1A benchmark cross-check (P1A abstract L1163-1165 / L737) ---
    n_ISM = 100 * cm_inv3_in_eV3                       # n_psi = 100 cm^-3 in eV^3
    kappa_nISM2 = kappa * n_ISM**2                     # should reproduce 9.95e-80 eV^4
    rho_Lambda = mp.mpf('2.798e-11')                   # eV^4, implied by P1A benchmark ratio
    p1a_ratio = kappa_nISM2 / rho_Lambda               # should reproduce ~3.56e-69

    # --- bound prefactors ---
    def holst(g):
        g = mp.mpf(g)
        return g**2 / (1 + g**2)

    def prefactor(g):
        # (35/16)(3/16) gamma^2/(1+gamma^2)
        return mp.mpf(35) / 16 * mp.mpf(3) / 16 * holst(g)

    # --- LQC critical density fiducials (Planck units) ---
    # Standard effective-LQC: rho_c = sqrt(3)/(32 pi^2 gamma^3) * M_Pl^4 (unreduced-Pl form).
    def rho_c_LQC(g):
        g = mp.mpf(g)
        return mp.sqrt(3) / (32 * mp.pi**2 * g**3) * M_Pl_eV**4

    # Barbero-Immirzi fiducials: 0.2375 (BH entropy, P1A uses this class), and O(1).
    gammas = {"BH_entropy_0.2375": mp.mpf('0.2375'), "O(1)_gamma=1": mp.mpf('1')}

    results = {}
    for name, g in gammas.items():
        rc = rho_c_LQC(g)                              # eV^4
        pf = prefactor(g)
        # dimensionless drive at which |delta f_NL| = target:
        # |delta f_NL| = pf * x_psi,  x_psi = kappa n_c^2 / rho_c.
        # Critical n_c for x_psi = 1 (torsion energy = background => EFT breakdown):
        n_c_eft = mp.sqrt(rc / kappa)                  # eV^3
        # Critical n_c for |delta f_NL| = 1 (torsion comparable to the -35/16 signal):
        # pf * kappa n_c^2 / rc = 1  => n_c = sqrt(rc/(pf kappa))
        n_c_dfnl1 = mp.sqrt(rc / (pf * kappa))
        # Critical n_c for |delta f_NL| = 1e-3 (the disclosed linear-transmission residual):
        n_c_dfnl1em3 = mp.sqrt(rc * mp.mpf('1e-3') / (pf * kappa))

        # |delta f_NL| as an explicit function of nu = n_c/M_Pl^3:
        # |delta f_NL| = pf * kappa (nu M_Pl^3)^2 / rc = pf * kappa M_Pl^6 nu^2 / rc
        coeff_nu2 = pf * kappa * M_Pl_eV**6 / rc       # multiplies nu^2

        results[name] = {
            "gamma": mp.nstr(g, 6),
            "holst_factor_gamma2_over_1plusgamma2": mp.nstr(holst(g), 6),
            "prefactor_35o16_3o16_holst": mp.nstr(pf, 6),
            "rho_c_LQC_eV4": mp.nstr(rc, 6),
            "rho_c_over_MPl4": mp.nstr(rc / M_Pl_eV**4, 6),
            "dfNL_bound_coeff_times_nu2": mp.nstr(coeff_nu2, 6),
            "dfNL_bound_formula": "|delta f_NL^tor| <~ %s * (n_psi,c / M_Pl^3)^2" % mp.nstr(coeff_nu2, 6),
            "n_c_crit_EFT_breakdown_x_psi_eq_1": {
                "n_psi_c_eV3": mp.nstr(n_c_eft, 6),
                "n_psi_c_over_MPl3": mp.nstr(n_c_eft / M_Pl_eV**3, 6),
            },
            "n_c_crit_for_dfNL_eq_1": {
                "n_psi_c_eV3": mp.nstr(n_c_dfnl1, 6),
                "n_psi_c_over_MPl3": mp.nstr(n_c_dfnl1 / M_Pl_eV**3, 6),
            },
            "n_c_crit_for_dfNL_eq_1e-3_disclosed_residual": {
                "n_psi_c_eV3": mp.nstr(n_c_dfnl1em3, 6),
                "n_psi_c_over_MPl3": mp.nstr(n_c_dfnl1em3 / M_Pl_eV**3, 6),
            },
        }

    # --- illustrative fiducials (clearly labelled; provenance recorded) ---
    # (i) P1A ISM continuity: n_psi = 100 cm^-3 (a PRESENT-DAY density, context only).
    # (ii) GUT-scale thermal: n_psi ~ T^3 with T = 1e16 GeV = 1e25 eV.
    illus = {}
    g_ref = mp.mpf('0.2375')
    rc_ref = rho_c_LQC(g_ref)
    pf_ref = prefactor(g_ref)

    def dfNL_from_nc(n_c_eV3):
        return pf_ref * kappa * n_c_eV3**2 / rc_ref

    n_ISM_val = 100 * cm_inv3_in_eV3
    T_GUT = mp.mpf('1e25')                             # 1e16 GeV in eV
    n_GUT = T_GUT**3                                    # relativistic thermal ~ T^3
    illus = {
        "note": "illustrative only; n_psi,c remains the free model parameter",
        "gamma_used": mp.nstr(g_ref, 6),
        "ISM_100cm-3_present_day_context_only": {
            "n_psi_eV3": mp.nstr(n_ISM_val, 6),
            "n_psi_over_MPl3": mp.nstr(n_ISM_val / M_Pl_eV**3, 6),
            "dfNL_bound": mp.nstr(dfNL_from_nc(n_ISM_val), 6),
        },
        "GUT_thermal_T1e16GeV": {
            "n_psi_eV3_approx_T3": mp.nstr(n_GUT, 6),
            "n_psi_over_MPl3": mp.nstr(n_GUT / M_Pl_eV**3, 6),
            "dfNL_bound": mp.nstr(dfNL_from_nc(n_GUT), 6),
            "caveat": "T^3 is a RELATIVISTIC estimate; the matter-bounce is w=0 (non-relativistic) so this is an upper-context figure, not the model value",
        },
    }

    provenance = {
        "hbar_c_eV_cm": "1.973e-5 (P1A tex L735)",
        "one_cm_inv3_in_eV3": mp.nstr(cm_inv3_in_eV3, 6) + " (P1A L735-736)",
        "M_Pl_unreduced_eV": "1.22e28 (P1A L737)",
        "kappa_8piG_eV-2": mp.nstr(kappa, 6),
        "P1A_benchmark_crosscheck": {
            "kappa_n_psi2_at_100cm-3_eV4": mp.nstr(kappa_nISM2, 6),
            "P1A_target_9.9542e-80": "reproduced" if abs(kappa_nISM2 - mp.mpf('9.9542e-80')) / mp.mpf('9.9542e-80') < mp.mpf('0.01') else "MISMATCH",
            "rho_Lambda_eV4_implied": mp.nstr(rho_Lambda, 6),
            "kappa_n2_over_rhoLambda": mp.nstr(p1a_ratio, 6),
            "P1A_target_3.5571e-69": "reproduced" if abs(p1a_ratio - mp.mpf('3.5571e-69')) / mp.mpf('3.5571e-69') < mp.mpf('0.02') else "MISMATCH",
        },
    }
    return results, illus, provenance


def main():
    open(LOG_OUT, "w").close()
    log("=" * 74)
    log("G3: Einstein-Cartan four-fermion TORSION BOUND on P2 f_NL (assumption f)")
    log("=" * 74)

    log("[A] symbolic bound (sympy), anchored to P1A -(3kappa/16)[g^2/(1+g^2)]J5^2 ...")
    sym, _ = symbolic_bound()
    log("    frac_tor(bounce) = " + sym["frac_tor_at_bounce"])
    log("    |delta f_NL^tor| <~ " + sym["dfNL_bound_reduced"])

    log("[B] numeric evaluation with P1A unit machinery + provenance ...")
    results, illus, provenance = numeric_eval()
    log("    P1A benchmark cross-check: kappa n_psi^2(100cm^-3) = "
        + provenance["P1A_benchmark_crosscheck"]["kappa_n_psi2_at_100cm-3_eV4"]
        + " eV^4 -> " + provenance["P1A_benchmark_crosscheck"]["P1A_target_9.9542e-80"])
    for name, r in results.items():
        log(f"    [{name}] prefactor={r['prefactor_35o16_3o16_holst']}  "
            f"rho_c/MPl^4={r['rho_c_over_MPl4']}")
        log(f"        |delta f_NL^tor| <~ {r['dfNL_bound_coeff_times_nu2']} (n_psi,c/M_Pl^3)^2")
        log(f"        critical n_psi,c (delta f_NL=1): "
            f"{r['n_c_crit_for_dfNL_eq_1']['n_psi_c_over_MPl3']} M_Pl^3")
        log(f"        critical n_psi,c (delta f_NL=1e-3): "
            f"{r['n_c_crit_for_dfNL_eq_1e-3_disclosed_residual']['n_psi_c_over_MPl3']} M_Pl^3")

    conclusion = (
        "The Einstein-Cartan four-fermion torsion contribution to the P2 "
        "matter-bounce f_NL is |delta f_NL^tor| <~ (35/16)(3/16)[gamma^2/(1+gamma^2)] "
        "kappa n_psi,c^2/rho_c, with n_psi,c the (free) bounce-epoch fermion number "
        "density. Using the committed P2 quasi-dust dilution n_psi ∝ rho, the "
        "fraction is maximal AT the bounce. The contribution reaches the disclosed "
        "1e-3 linear-transmission residual only for n_psi,c ~ 3e-2 M_Pl^3 and "
        "becomes comparable to the -35/16 amplitude only for n_psi,c ~ 1 M_Pl^3 "
        "(gamma=0.2375) -- i.e. only at Planck-density fermion populations, where "
        "the effective LQC bounce itself breaks down (x_psi = kappa n_psi,c^2/rho_c "
        ">~ 1 is the EFT-breakdown line). SHARPEST STATEMENT: within the EFT's own "
        "validity domain x_psi < 1, the bound saturates at |delta f_NL^tor| <~ the "
        "prefactor (35/16)(3/16)[gamma^2/(1+gamma^2)] = 0.022 (gamma=0.2375) to 0.21 "
        "(gamma=1), so torsion can never exceed ~1-10% of the -35/16 amplitude "
        "anywhere the effective bounce description holds, and is <<1e-3 for realistic "
        "sub-Planckian abundances. For ANY sub-Planckian fermion abundance "
        "(n_psi,c << M_Pl^3, required for a semiclassical bounce), torsion is "
        "negligible and assumption (f) holds. This converts assumption (f) from "
        "asserted to BOUNDED, with n_psi,c the explicit free parameter. NO value of "
        "n_psi,c is fabricated; NO paper edit; NO version bump.")

    out = {
        "gate": "G3 -- model-specific Einstein-Cartan four-fermion torsion bound (P2 assumption f)",
        "phase": "campaign 2026-07-17 Task A (real computation, bounded result, no paper edit)",
        "meta": {
            "date_utc": datetime.now(timezone.utc).isoformat(),
            "runtime_s": round(time.time() - _t0, 2),
            "sympy": sp.__version__,
        },
        "P1A_conventions_reused": {
            "contact_term": "-(3 kappa/16)[gamma^2/(1+gamma^2)] J_5^2  (P1A tex L1161-1162, L856, L1172)",
            "kappa": "8 pi G, unreduced M_Pl (P1A L737)",
            "benchmark": "kappa n_psi^2/rho_Lambda ~= 3.6e-69 (n/100cm^-3)^2 (P1A L1163-1165)",
            "J5_squared_proxy": "<J_5^2> <~ n_psi^2 (P1A: n_psi does not fix <J5 J5>; n^2 is the conservative spin-coherent upper bound)",
        },
        "P2_background_reused": "quasi-dust rho = rho_c (a_b/a)^3, n_psi ∝ a^-3 ∝ rho (g1_gradient_transmission_scheme.py [B])",
        "A_symbolic_bound": sym,
        "B_numeric_by_gamma": results,
        "B_illustrative_fiducials": illus,
        "provenance": provenance,
        "conclusion": conclusion,
    }
    with open(JSON_OUT, "w") as f:
        json.dump(out, f, indent=2)
    log(f"DONE -> {JSON_OUT}")


if __name__ == "__main__":
    main()

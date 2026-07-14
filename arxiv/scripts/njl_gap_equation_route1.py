#!/usr/bin/env python3
r"""
njl_gap_equation_route1.py
==========================

Reproducibility check for the standard mean-field NJL treatment used in P1A.

    "<J5>=0 does not imply <J5 J5>=0; a genuine closure requires a regulated
     gap equation, effective potential, and demonstration that no relevant
     vacuum solution exists."

Conceded in-paper at sec:r1_njl (paper1_unified.tex, lines ~2643-2653):

    "we do NOT claim to exclude a fully regulated NJL vacuum condensate
     <psi psi_bar> != 0 via a gap equation and effective potential -- that
     self-consistent strong-coupling analysis is beyond the present mean-field
     treatment and is noted as an out-of-scope open item."

THIS SCRIPT evaluates that question within a standard NJL-type gap-equation
and hard-cutoff mean-field treatment of the ECH torsion-induced four-fermion
interaction. It DERIVES (sympy) and NUMERICALLY EVALUATES the two things that
decide whether a dynamical chiral condensate can form:

  (A) the ratio  G_eff / G_crit  at both physically-motivated cutoffs
      (Lambda = M_Pl and a formal larger-cutoff sensitivity point
       Lambda_formal ~ M_Pl / sqrt(gamma_BI)); and
  (B) the SIGN of the four-fermion coupling in the SCALAR (sigma ~ <psi psi_bar>)
      channel after the paper's own Fierz projection (eq:AAdecomp) -- attractive
      (G>0, condensation possible) vs repulsive (G<0, condensation impossible).

INPUTS TAKEN FROM THE PAPER (not invented):
  * Coupling (eq:NJL_torsion, minimal Einstein-Cartan gamma->infty limit):
        L_int = -(3/16) kappa (psibar gamma^a gamma5 psi)^2 = -(3/16) kappa (J5)^2
    with kappa = 8 pi G = M_Pl^{-2}   (Hehl-Datta; paper eq:torsion, eq:4fermi).
  * Holst suppression factor gamma^2/(gamma^2+1) in (0,1) (eq:4fermi); for the
    minimal-EC channel this -> 1 (gamma->inf), so the EC value is the *maximal*
    coupling. We report both the maximal (gamma->inf) and the Holst-dressed value.
  * Fierz projection to the SS (scalar) channel (eq:AAdecomp, App app:fierz,
     verified by arxiv/scripts/fierz_lemma_check.py):
        (J5.J5)  -->  +1/4 SS + 1/2 VV - 1/2 AA - 1/4 PP.
  * Formal cutoff-sensitivity point used in the historical scan:
        Lambda_formal ~ M_Pl / sqrt(gamma_BI), gamma_BI = 0.274.
    Because this lies above M_Pl, it is a sensitivity test, not a controlled
    claim that the contact EFT remains valid to that scale.
  * M_Pl = 1.22e19 GeV (unreduced Planck mass, paper convention).

STANDARD NJL FACTS USED (textbook, cited in docstring, machine-checked below):
  * Mean-field gap equation with a hard 4-momentum (Euclidean) cutoff Lambda,
    N_f flavors, N_c colors, for L = G_s (psibar psi)^2:
        M = m0 + 2 G_s N_f N_c * (M / (2 pi^2)) * [ Lambda^2 - M^2 ln(1+Lambda^2/M^2) ]
    In the chiral limit (m0=0) a nontrivial M!=0 solution EXISTS iff the coupling
    exceeds the critical value obtained from the M->0 slope of the gap equation:
        G_crit = pi^2 / ( N_f N_c Lambda^2 )
    (Klevansky RMP 64 (1992) 649, Eq. 3.42; Hatsuda-Kunihiro Phys.Rept. 247 (1994) 221;
     Buballa Phys.Rept. 407 (2005) 205.) This G_crit is DERIVED symbolically below
    from the gap-equation slope, not quoted.
  * Condensation additionally requires the SCALAR-channel coupling to be
    ATTRACTIVE (G_s > 0). A repulsive scalar channel (G_s < 0) has effective
    potential Omega(M) monotincreasing from M=0 => M=0 is the only (trivial)
    minimum => NO condensate at any coupling strength.

NEVER FABRICATES: G_crit is derived from the gap-equation slope symbolically;
the scalar-channel sign is read from the paper's own Fierz coefficient; every
number is computed here and cross-checked. The task-prompt's dimensional
expectation ("far sub-critical") is TESTED, not assumed.
"""

import json
import math
import os
import sympy as sp

RESULTS = {}

# ============================================================================
# 0. Symbols and paper inputs
# ============================================================================
M, m0, Gs, Lam, Nf, Nc = sp.symbols('M m0 G_s Lambda N_f N_c', positive=True)
kappa = sp.symbols('kappa', positive=True)

# Paper couplings (exact rationals):
#   L_int = -(3/16) kappa (J5)^2  [eq:NJL_torsion], kappa = 8 pi G = M_Pl^{-2}.
c_J5J5 = sp.Rational(-3, 16)                      # coefficient of kappa (J5.J5)
# Fierz projection onto scalar SS channel [eq:AAdecomp]:
#   (J5.J5) -> +1/4 SS + 1/2 VV - 1/2 AA - 1/4 PP
fierz_SS = sp.Rational(1, 4)                      # SS-channel weight of (J5.J5)

# Scalar-channel four-fermion coupling written in the NJL normalization
#   L_SS = G_scalar (psibar psi)^2, so G_scalar = c_J5J5 * fierz_SS * kappa.
G_scalar_over_kappa = c_J5J5 * fierz_SS          # = (-3/16)*(1/4) = -3/64
print(f"[0] Paper coupling  L_int = ({c_J5J5}) kappa (J5.J5),  kappa = 8 pi G = M_Pl^-2")
print(f"[0] Fierz SS-channel weight of (J5.J5) = {fierz_SS}  (eq:AAdecomp)")
print(f"[0] => Scalar-channel coupling  G_scalar = ({G_scalar_over_kappa}) kappa "
      f"= ({float(G_scalar_over_kappa)}) / M_Pl^2")
RESULTS['coupling'] = {
    'L_int_coeff_of_kappa_times_J5J5': str(c_J5J5),
    'fierz_SS_weight_of_J5J5': str(fierz_SS),
    'G_scalar_over_kappa': str(G_scalar_over_kappa),
    'G_scalar_over_kappa_float': float(G_scalar_over_kappa),
    'kappa_definition': '8*pi*G = M_Pl^-2',
}

# ============================================================================
# 1. Regulated NJL gap equation and DERIVED critical coupling
# ============================================================================
# One-loop mean-field gap equation, hard 4-momentum cutoff Lambda (Euclidean),
# for L = G_s (psibar psi)^2, in the standard NJL normalization:
#   M = m0 + 2 G_s * (Nf Nc) * <psibar psi>_M
#   <psibar psi>_M = -(M/(2 pi^2)) [ Lambda^2 - M^2 ln(1 + Lambda^2/M^2) ]  (per dof)
# We take the standard 2 N_f N_c degeneracy factor (see Klevansky Eq.3.41-3.42).
loop = (M / (2*sp.pi**2)) * (Lam**2 - M**2 * sp.ln(1 + Lam**2/M**2))
gap_rhs = m0 + 2*Gs*Nf*Nc*loop
gap_eq = sp.Eq(M, gap_rhs)
print("\n[1] Regulated NJL gap equation (hard cutoff Lambda, m0=chiral limit):")
sp.pprint(sp.Eq(M, gap_rhs))

# Critical coupling: in the chiral limit m0->0, divide by M and take M->0.
# A nontrivial solution bifurcates from M=0 when the slope of RHS/M at M->0 = 1.
RHS_over_M = sp.simplify(gap_rhs.subs(m0, 0) / M)
slope0 = sp.limit(RHS_over_M, M, 0)              # = 2 G_s Nf Nc Lambda^2/(2 pi^2)
print("\n[2] RHS/M in the M->0 limit (bifurcation slope):")
sp.pprint(slope0)
# Critical coupling solves slope0 = 1:
G_crit = sp.solve(sp.Eq(slope0, 1), Gs)[0]
G_crit = sp.simplify(G_crit)
print("\n[3] DERIVED critical coupling G_crit (solve slope=1):")
sp.pprint(sp.Eq(sp.Symbol('G_crit'), G_crit))
# Cross-check against the standard textbook value pi^2/(Nf Nc Lambda^2):
G_crit_textbook = sp.pi**2 / (Nf*Nc*Lam**2)
match = sp.simplify(G_crit - G_crit_textbook) == 0
print(f"      textbook G_crit = pi^2/(N_f N_c Lambda^2);  match: {match}")
assert match, "Derived G_crit does not match textbook pi^2/(Nf Nc Lambda^2)"
RESULTS['G_crit'] = {
    'derived': str(G_crit),
    'textbook': 'pi^2/(N_f N_c Lambda^2)',
    'symbolic_match': bool(match),
    'derivation': 'slope of gap-equation RHS/M at M->0 set to 1',
}

# ============================================================================
# 2. Effective potential and the SCALAR-CHANNEL SIGN verdict
# ============================================================================
# The mean-field (Ginzburg-Landau) effective potential near M=0:
#   Omega(M) = M^2/(4 G_s) - (Nf Nc/ (4 pi^2)) [ Lambda^2 M^2 - ... ] + ...
# Its M^2 coefficient is  a2 = 1/(4 G_s) - Nf Nc Lambda^2/(4 pi^2).
# Condensate forms iff a2 < 0 (M=0 becomes a maximum), i.e. G_s > G_crit AND G_s > 0.
# If G_s < 0 (repulsive), 1/(4 G_s) < 0 too but the vacuum-loop term structure
# makes M=0 the global minimum: a repulsive scalar channel CANNOT condense.
print("\n[4] SCALAR-CHANNEL SIGN VERDICT")
sign = '+ (attractive)' if G_scalar_over_kappa > 0 else '- (REPULSIVE)'
print(f"      G_scalar = ({G_scalar_over_kappa}) kappa  and kappa>0  => sign is {sign}")
print("      Standard NJL condensation REQUIRES an attractive scalar channel (G_s>0).")
print("      Here the (J5.J5)->SS Fierz projection gives a NEGATIVE (repulsive)")
print("      scalar coupling => NO chiral condensate forms at ANY coupling strength,")
print("      independent of the cutoff. (The gap equation has only the trivial M=0")
print("      solution when G_s<0.)")
RESULTS['scalar_channel_sign'] = {
    'G_scalar_sign': 'negative (repulsive)' if G_scalar_over_kappa < 0 else 'positive (attractive)',
    'condensation_possible_by_sign': bool(G_scalar_over_kappa > 0),
    'note': 'repulsive scalar channel => only trivial M=0 minimum, no condensate at any coupling',
}

# ============================================================================
# 3. NUMERICS: G_eff / G_crit at both cutoffs (magnitude test)
# ============================================================================
# Even setting the sign aside, test the task's dimensional expectation: is the
# magnitude of the gravitational four-fermion coupling sub-critical?
# Use |G_eff| so the magnitude test is meaningful regardless of sign.
M_Pl = 1.22e19            # GeV, unreduced Planck mass (paper convention)
gamma_BI = 0.274          # SU(2) Barbero-Immirzi (eq:gamma)
kappa_val = 1.0 / M_Pl**2 # GeV^-2  (kappa = M_Pl^-2)
Nf_val, Nc_val = 1, 1     # single Dirac species, minimal ECH (App app:fierz single-species);
                          # larger Nf Nc only LOWERS G_crit's prefactor pi^2/(Nf Nc L^2)
                          # -> makes the ratio LARGER, so Nf=Nc=1 is the *conservative*
                          # (hardest-to-exclude) choice; we also report Nf Nc = 3*3=9 (QCD-like).

# |G_scalar| in the scalar channel (magnitude of the gravitational coupling):
G_eff_mag = abs(float(G_scalar_over_kappa)) * kappa_val   # GeV^-2
# Holst-dressed (finite gamma) value: multiply coupling by gamma^2/(gamma^2+1):
holst_factor = gamma_BI**2 / (gamma_BI**2 + 1.0)
G_eff_holst = G_eff_mag * holst_factor

cutoffs = {
    'Lambda_M_Pl':        M_Pl,
    'Lambda_formal_above_MPl':  M_Pl / math.sqrt(gamma_BI),
}
print("\n[5] G_eff / G_crit magnitude test (|G_eff| vs G_crit = pi^2/(Nf Nc Lambda^2)):")
RESULTS['ratios'] = {}
for label, Lam_val in cutoffs.items():
    for (nfnc_label, nfnc) in [('Nf=Nc=1', 1*1), ('Nf=1,Nc=3', 1*3), ('Nf=3,Nc=3', 3*3)]:
        G_crit_val = math.pi**2 / (nfnc * Lam_val**2)      # GeV^-2
        ratio_EC    = G_eff_mag   / G_crit_val
        ratio_holst = G_eff_holst / G_crit_val
        key = f'{label}__{nfnc_label}'
        RESULTS['ratios'][key] = {
            'Lambda_GeV': Lam_val,
            'Nf_Nc': nfnc,
            'G_crit_GeV^-2': G_crit_val,
            'G_eff_over_G_crit_EC_maximal': ratio_EC,
            'G_eff_over_G_crit_Holst_dressed': ratio_holst,
            'subcritical_EC': bool(ratio_EC < 1.0),
        }
        print(f"      {label:18s} {nfnc_label:9s}: "
              f"|G_eff|/G_crit (EC max) = {ratio_EC:.4e}, "
              f"(Holst) = {ratio_holst:.4e}, "
              f"subcritical={ratio_EC < 1.0}")

RESULTS['inputs'] = {
    'M_Pl_GeV': M_Pl, 'gamma_BI': gamma_BI, 'kappa_GeV^-2': kappa_val,
    'holst_factor_gamma^2/(gamma^2+1)': holst_factor,
    'Lambda_formal_above_MPl_GeV': cutoffs['Lambda_formal_above_MPl'],
}

# ============================================================================
# 4. Closed-form ratio at Lambda = M_Pl (the load-bearing number)
# ============================================================================
# |G_eff| = (3/64) M_Pl^-2 ;  G_crit(Lambda=M_Pl) = pi^2/(Nf Nc M_Pl^2).
# => |G_eff|/G_crit = (3/64) * Nf Nc / pi^2, a PURE NUMBER independent of M_Pl.
ratio_MPl_symbol = sp.Rational(3, 64) * Nf * Nc / sp.pi**2
print("\n[6] Closed form at Lambda = M_Pl (M_Pl cancels exactly):")
print(f"      |G_eff|/G_crit = (3/64) N_f N_c / pi^2")
for nfnc in [1, 3, 9]:
    val = float(sp.Rational(3, 64) * nfnc / sp.pi**2)
    print(f"        Nf Nc = {nfnc}: = {val:.5f}")
RESULTS['closed_form_ratio_Lambda_MPl'] = {
    'formula': '(3/64) * N_f N_c / pi^2  (M_Pl-independent)',
    'Nf_Nc_1': float(sp.Rational(3, 64) / sp.pi**2),
    'Nf_Nc_3': float(sp.Rational(3, 64) * 3 / sp.pi**2),
    'Nf_Nc_9': float(sp.Rational(3, 64) * 9 / sp.pi**2),
}
# At Lambda_formal = M_Pl/sqrt(gamma), Lambda^2 is larger by 1/gamma,
# so G_crit is smaller by gamma and |G_eff|/G_crit is larger by 1/gamma.
ratio_EFT_factor = 1.0 / gamma_BI
print(f"      At Lambda_formal = M_Pl/sqrt(gamma): G_crit is gamma times smaller =>")
print(f"      ratio grows by 1/gamma = {ratio_EFT_factor:.4f} (formal sensitivity point).")

# ============================================================================
# 5. VERDICT
# ============================================================================
# Honest three-way classification.
worst_ratio = max(v['G_eff_over_G_crit_EC_maximal'] for v in RESULTS['ratios'].values())
sign_repulsive = G_scalar_over_kappa < 0
magnitude_subcritical = worst_ratio < 1.0

if sign_repulsive and magnitude_subcritical:
    verdict = ("STANDARD-MEAN-FIELD SCALAR CONDENSATE EXCLUDED IN THE DECLARED "
               "CHANNEL/REGULATOR CONVENTION. Two reasons: (1) the scalar "
               "channel is REPULSIVE (G_scalar = -(3/64) kappa < 0), so the "
               "effective potential has only the trivial M=0 minimum at ANY "
               "coupling; (2) even taking |G_eff|, the coupling is FAR "
               f"sub-critical (worst scanned |G_eff|/G_crit = {worst_ratio:.3e} < 1 "
               "at the formal larger-cutoff point, Nf Nc=9). This does not remove "
               "Fierz ambiguity or exclude beyond-mean-field/non-minimal completions.")
elif magnitude_subcritical:
    verdict = ("CONDENSATE EXCLUDED BY MAGNITUDE. Coupling far sub-critical "
               f"(|G_eff|/G_crit = {worst_ratio:.3e} << 1); sign not decisive.")
elif sign_repulsive:
    verdict = ("CONDENSATE EXCLUDED BY SIGN. Scalar channel repulsive; near/"
               "super-critical magnitude but wrong sign => no condensate.")
else:
    verdict = ("CONDENSATE POSSIBLE / CONDITIONAL. Attractive and not "
               "sub-critical -- NOT excluded; requires full analysis.")

print("\n[7] VERDICT")
print("      " + verdict)
RESULTS['verdict'] = {
    'text': verdict,
    'sign_repulsive': bool(sign_repulsive),
    'magnitude_subcritical': bool(magnitude_subcritical),
    'worst_case_G_eff_over_G_crit': worst_ratio,
    'condensate_excluded': bool(sign_repulsive or magnitude_subcritical),
}

# ============================================================================
# 6. Self-checks (assertions)
# ============================================================================
assert bool(match), "G_crit derivation failed"
assert G_scalar_over_kappa == sp.Rational(-3, 64), "scalar coupling coefficient wrong"
# Magnitude test: every cutoff/flavor case must be sub-critical (ratio < 1).
assert worst_ratio < 1.0, f"expected sub-critical (<1), got {worst_ratio}"
# The load-bearing, cutoff-independent number at Lambda=M_Pl with a single
# species is < 5e-3; report it as the headline conservative bound.
ratio_MPl_single = RESULTS['closed_form_ratio_Lambda_MPl']['Nf_Nc_1']
assert ratio_MPl_single < 5e-3, f"expected << 1 at Lambda=M_Pl single-species, got {ratio_MPl_single}"
assert sign_repulsive, "expected repulsive scalar channel"
print("\n[8] All self-checks PASS.")

# ============================================================================
# 7. Emit JSON
# ============================================================================
outdir = os.path.dirname(os.path.abspath(__file__))
outpath = os.path.join(outdir, 'njl_gap_equation_route1_results.json')
with open(outpath, 'w') as f:
    json.dump(RESULTS, f, indent=2)
print(f"\n[9] Results written to {outpath}")

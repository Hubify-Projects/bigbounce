# A3-2 — Bianchi-I separate-universe cross-check of the matter-contraction f_NL (IN PROGRESS)

**NEXT_SCIENCE_LEDGER #1 / #3 · 2026-09-03 · BigBounce theory-audit lane**

## Plan (written before the computation, committed as a header)

Target: the one computation left open by
`fnl_matter_contraction_adjudication_2026_09_02.md` ("What remains open"):
a second-order *anisotropic* (Bianchi-I) separate-universe computation of the
comoving-gauge squeezed response, including the long mode's shear
sigma^i_j = (khat_i khat_j - delta/3) eps zetadot_L, to test whether it
reproduces the in-in monopole -15/8 and mu^2 coefficient +15/16, i.e. whether
the adjudication's reconciliation mechanism (the delta-N / in-in residual is
carried by the long mode's shear, not by O(k^2) gradients) is correct.

Steps:
1. ADM comoving gauge; derive delta-K and sigma^i_j of the long growing mode
   from psi = -zeta/H + a^2 eps grad^{-2} zetadot; confirm/refute that the
   shear is O(k_L^0) and get its exact coefficient for general eps.
2. Integrate the shear into the local anisotropic scale factors,
   beta_i(eta_B) = int sigma_i dt, on the growing mode; general eps.
3. Local Bianchi-I patch -> short-mode response: isotropic (comoving delta-N)
   piece + anisotropic projection piece; assemble f_NL(mu).
4. Validate the machinery on de Sitter/attractor (must give (5/12)(1-n_s),
   zero quadrupole) and on USR (shear ~ eps -> 0, must give pure monopole).
5. Compare with the in-in f(mu) = -35/16 + (15/16) mu^2.

Integrity: no step is adjusted to land on -35/16. Verdict stated as CONFIRMS /
CONFIRMS-BY-OTHER-MECHANISM / DISAGREES, with the step where any difference
arises, and incomplete steps reported as incomplete.

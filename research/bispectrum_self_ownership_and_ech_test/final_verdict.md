# Final Verdict

## 1. Was Cai's -35/8 numerically reproduced?

**PARTIALLY.** The algebraic verification is complete and exact (all three special cases match). The numerical time-integral implementation runs and gives the correct sign and order of magnitude, but the absolute normalization requires careful treatment of the k-dependent amplitude |A|² = 1/(2k⁴) and the field redefinition (Eq. 28), which we could not reliably parse from the PDF extraction. Full numerical self-ownership requires either (a) reading the original paper properly or (b) implementing the normalization chain end-to-end.

## 2. Do we fully self-own the generic matter-bounce bispectrum?

**ALGEBRAICALLY: YES.** We can evaluate the shape function and extract |B|_NL at any momentum configuration.
**NUMERICALLY: NOT YET.** The time-integral code needs the normalization factors and field redefinition.

## 3. Is the bispectrum currently generic or framework-specific?

**GENERIC.** f_NL = -35/8 is a property of ANY matter-dominated contraction with:
- Standard GR perturbation theory
- Bunch-Davies vacuum
- Single canonical scalar field

It does NOT depend on ECH, LQC, or any specific bounce mechanism. The bounce mechanism only matters for TRANSFERRING the signal from the contracting to expanding phase.

## 4. Is there any credible ECH entry point?

**ONE:** The ECH cubic action might contain additional vertices from the Holst term and contorsion tensor, proportional to 1/γ (Barbero-Immirzi parameter). This would give:

f_NL^{ECH} = -35/8 + δf_NL(γ)

Computing δf_NL requires expanding the ECH action to third order in perturbations — a non-trivial but well-defined calculation.

## 5. Is ECH-specific bispectrum work promising, weak, or likely dead?

**WEAK BUT NOT DEAD.** The only credible path is the cubic-action correction from the Holst term. This is:
- Theoretically well-defined (just expand the action to third order)
- Potentially observable (if 1/γ corrections are O(1))
- A genuine calculation (not speculation)
- But very likely to give δf_NL = 0 (if the Holst term remains topological at third order on FRW backgrounds)

The program lives or dies on whether the Holst term generates nontrivial cubic vertices.

## 6. Exact next calculation

**OPTION A (complete self-ownership):** Obtain a clean PDF of Cai (2009), read Eqs. 14-33 directly, implement the correct normalization chain and field redefinition, and verify -35/8 from the time integral. This is engineering, not physics.

**OPTION B (ECH specificity test):** Expand S_ECH = S_EH + S_Holst to third order in scalar perturbations on the matter-contraction background. Determine whether new cubic vertices appear. If yes: compute δf_NL. If no: ECH-specific bispectrum is dead, and the f_NL = -35/8 remains purely generic.

**RECOMMENDATION:** Option B is higher-value physics. Option A is important for completeness but doesn't change the science. Do B first.

## Overall Status

| Component | Status |
|-----------|--------|
| Generic matter-bounce f_NL = -35/8 | **ALGEBRAICALLY VERIFIED** |
| Old discrepancy (+25/16) | **FULLY EXPLAINED** |
| Numerical infrastructure | **Sound but needs normalization** |
| ECH-specific correction | **Credible path identified (Holst cubic action)** |
| Flagship discriminator | **ALIVE as generic bounce signal** |
| MegaMapper detectability | **YES (8.3σ at -35/8)** |

# P1A R-round — DIRECT vendor — Gemini-2.5-Pro cosmology-physics reviewer

**Model**: `gemini-2.5-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round8
**Wall time**: 62.6s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=36095, completion=895, total=43468

---

## PAPER-GEM-B1
**Classification:** BLOCKER
**Section:** Sec. X (The Perturbation-Transparency Result)
**Issue:** The paper's "central result," the perturbation-transparency theorem, is derived exclusively for canonical scalar matter, where torsion is identically zero. However, the dark-energy mechanisms the paper aims to close are sourced by fermion spin density, a scenario to which the theorem does not apply.
**Fix:** Acknowledge that the theorem is a proof-of-principle for a toy model and cannot be the "central result" for closing the physically relevant fermion-driven ECH channels. Reframe it as an observation about a limiting case.

## PAPER-GEM-B2
**Classification:** BLOCKER
**Section:** Sec. IV.D (Route 4: parity-odd CMB coupling)
**Issue:** The closure of Route 4 is claimed on the basis of an "explanatory deficit," admitting that the model is a "viable parity-odd source" if the coupling `alpha/M` is treated as a free parameter. This is not a closure but a statement of non-predictivity, undermining the paper's headline claim of closing all four minimal routes.
**Fix:** Reclassify Route 4 as "unpredictive" or "unconstrained" rather than "closed." The paper's central claim of closing four routes must be softened to three, with the fourth requiring a re-parameterization that minimal ECH does not provide.

## PAPER-GEM-M1
**Classification:** MAJOR
**Section:** Sec. II.C.1 vs. Sec. XIV.D
**Issue:** The paper presents the "structural tension" (requiring `N_tot ~ 92` for DE vs. `f_NL` erasure) as a key "robustness check." This is misleading, as the paper has already argued in Sec. II.C.1 that the underlying DE mechanism is physically non-viable due to the "reheating thermal-reset," which erases any bounce-era memory.
**Fix:** Demote the "structural tension" argument to a secondary, conditional point. The primary closure argument should be the thermal reset; the tension argument is only relevant if one assumes, contrary to the paper's own physics, that the thermal reset can be evaded.

## PAPER-GEM-m1
**Classification:** minor
**Section:** Sec. XIII (Surviving Mechanism-Independent Tests)
**Issue:** The spectator-ALP birefringence signal (`beta ~ 0.27 deg`) is framed as a key "surviving test." However, the paper's own analysis in the conclusion correctly shows this value is statistically indistinguishable from the current WMAP+Planck measurement, even with future LiteBIRD data.
**Fix:** Reframe this point more accurately in the abstract and main body. The test is for a generic non-zero `beta`, not the specific, non-falsifiable benchmark value of `0.27 deg`.

## PAPER-GEM-n1
**Classification:** nit
**Section:** Sec. IV.B (Route 2)
**Issue:** The dimensionless ratio `Delta-theta_oneloop / Delta-theta_obs` is given with two different expressions that are not equivalent. The first implies `1/M_Pl^2` suppression, the second `1/M_Pl`.
**Fix:** The second expression `(H_0/M_Pl) * M / (M_Pl * alpha * beta_obs)` appears to be the intended one based on the subsequent numerical estimate. Remove the first, incorrect expression to avoid confusion.

## PAPER-GEM-n2
**Classification:** nit
**Section:** Sec. X.E (What Would Break the Transparency)
**Issue:** The list of conditions that would break the transparency theorem is incomplete. The theorem relies on the Holst term being a total derivative, which is true classically, but this term can have physical consequences via non-perturbative effects (instantons) or anomalies when coupled to other sectors.
**Fix:** Add a caveat that the theorem holds at the level of classical variational equations of motion but that non-perturbative or quantum effects sourced by the Pontryagin density are not considered.

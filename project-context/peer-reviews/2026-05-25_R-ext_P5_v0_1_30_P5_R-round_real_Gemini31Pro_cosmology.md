# P5 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P5_v0_1_30
**Wall time**: 37.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=25758, completion=3030, reasoning=2078, total=28788

---

## PAPER-GEM-B1: Overstated mechanism-independent UV bound (BLOCKER)
**Section:** 10.2 (Discussion)
**Issue:** The paper claims the null result establishes an "observational upper bound that any future parity-violating model proposing an environment-dependent chirality signature must respect." This is a massive overstatement of UV-completion independence. The translation of primordial chiral operators (e.g., Chern-Simons $R\tilde{R}$ or axion $F\tilde{F}$) to late-time galactic angular momentum requires a highly mechanism-dependent, non-linear transfer function via Tidal Torque Theory. You cannot bound "any future model" without defining the EFT operators and their specific couplings to the baryonic/dark matter angular momentum acquisition process.
**Fix:** Retract the "any future model" claim. Explicitly state that the cosmological implications are limited by the absence of a theoretical transfer function linking primordial parity-violating EFT operators to non-linear galactic chirality.

## PAPER-GEM-M1: Complete omission of standard parity-violation literature (MAJOR)
**Section:** 1 (Introduction) & 10.2 (Discussion)
**Issue:** The text invokes "early-universe parity-violating physics" and "primordial parity-violating scenarios" but cites absolutely zero standard theoretical literature on the subject. There is no mention of Chern-Simons gravity, axion-like particles (ALPs), or recent foundational work on cosmological parity violation (e.g., Lue, Wang, Kamionkowski 1999; Alexander et al. 2006; or recent LSS 4-point function tests by Philcox, Hou, etc.). 
**Fix:** Cite the standard theoretical reviews and recent LSS parity-violation literature to ground the astrophysical observable in actual high-energy physics frameworks.

## PAPER-GEM-M2: Vacuous model-discrimination claim (MAJOR)
**Section:** 10.2 (Discussion) & 13 (Conclusions)
**Issue:** The paper claims this null result "adds a clean environment-dependent constraint to the bounce-vs.-inflation discrimination program." In the exact same paragraph, it admits that "neither model predicts an environment-dependent CW signature." This is a logical contradiction. A null result on a signal that neither model class predicts does not discriminate between them, nor does it constrain their scope boundaries.
**Fix:** Delete the claim that this result aids bounce-vs-inflation discrimination. Reframe as a purely phenomenological astrophysical constraint.

## PAPER-GEM-M3: Scale-independent RSD anisotropy infects the tidal tensor (MAJOR)
**Section:** 11 (Limitations) & 4.1 (Algorithm)
**Issue:** Section 11 dismisses redshift-space distortions (RSD) because the Finger-of-God displacement ($\sim 5-8$ Mpc/$h$) is smaller than the $R_s = 25$ Mpc/$h$ smoothing scale. This ignores the linear Kaiser effect, which is a *scale-independent* anisotropic modulation of the density field in Fourier space ($\delta_s = \delta_r (1 + f \mu^2)$). Because the V-Web tidal tensor $T_{ij}$ relies on the Hessian of the potential, this line-of-sight anisotropy systematically biases the eigenvalues $\lambda_i$, artificially altering the void/wall/filament/cluster classification boundaries regardless of $R_s$.
**Fix:** Acknowledge that the linear Kaiser effect systematically biases the V-Web eigenvalues along the line of sight. State that a rigorous physical-frame classification requires either real-space reconstruction or an anisotropic $\lambda_{\rm th}$ threshold.

## PAPER-GEM-m1: Neglect of GR projection effects on the large-scale potential (minor)
**Section:** 4.1 (Algorithm, Step 8)
**Issue:** The algorithm solves the Newtonian Poisson equation $\Phi(k) = -\delta_k / k^2$ in observed redshift space. On large scales, the physical-frame density field is modified by GR projection effects (Sachs-Wolfe, lensing magnification, gravitational redshift), which alter the true gravitational potential. While standard in N-body literature, applying a Newtonian tidal tensor to a lightcone without gauge-matching introduces theoretical inconsistencies at horizon-approaching scales.
**Fix:** Add a sentence noting that the Newtonian Poisson equation neglects GR projection effects, meaning the largest-scale V-Web modes are formally gauge-dependent approximations.

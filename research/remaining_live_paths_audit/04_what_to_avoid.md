# What to Avoid: Paths That Look Tempting But Should Be Deprioritized

**Created:** 2026-03-18
**Purpose:** Prevent time-sink research directions that will not advance the science case.

---

## 1. Reopening ECH Perturbation Loops

**Why tempting:** ECH is mathematically clean, we have deep expertise in the framework, and the birefringence prediction (beta = 0.27 deg matching the 3.6 sigma observed signal) keeps it emotionally salient.

**Why avoid:** Perturbation transparency is a STRUCTURAL result. Fourteen barriers close all minimal routes from ECH bounce to distinctive perturbation-level observables. Branches A through W all hit the same wall: ECH perturbations are identical to GR perturbations at linear order and above on FRW backgrounds. The torsion tensor vanishes identically on FRW (T_0 = Q_0 = 0). No new ECH-specific observable can emerge from minimal scalar-matter coupling. This was proven, not merely tested.

**Exception:** Only if someone proposes a fundamentally new coupling type (e.g., fermionic torsion at cosmological densities with spin-density sources comparable to Planck-scale energy densities). Even then, the gravitational democracy barrier likely kills it: spin-density contributions are suppressed by (rho/rho_Pl) at all post-bounce temperatures.

**Estimated time cost if ignored:** 2-4 months for another variant that hits the same wall.

---

## 2. Teleparallel / f(T) / f(Q) / f(R) / Gauss-Bonnet Bounce Builders

**Why tempting:** Active literature with hundreds of papers per year. Looks productive. Many models produce bounces. Conference visibility.

**Why avoid:** These massively expand theory space without converging on sharp discriminators. Most produce "bounce exists" results, not "bounce predicts X uniquely." We would be starting a new program from scratch in a model space with no natural endpoint. Every f(T) bounce paper adds 2-3 free functions. None produce a parameter-free prediction comparable to f_NL = -35/8.

**The trap:** It feels like progress because you can always write another paper. But each paper moves laterally (new model, same class of results) rather than forward (sharper prediction, closer to observation).

**Risk:** 6+ months of model-building with no testable prediction at the end, plus the opportunity cost of not pursuing the LQC f_NL program.

---

## 3. GFT Condensate Cosmology (For Now)

**Why tempting:** Genuinely fundamental. Derives cosmological dynamics from pre-geometric quantum gravity. Conceptually the deepest approach to bounce cosmology.

**Why avoid:** Too far from observational leverage. Current GFT cosmology produces qualitative statements about bounce existence and semiclassical limit recovery, not sharp quantitative predictions. The perturbation theory is still under development. Producing an f_NL prediction from GFT would require:
- Defining perturbations on a GFT condensate (partially done, Gielen et al.)
- Connecting GFT perturbation spectrum to CMB observables (open problem)
- Computing nonlinear corrections (not started)

This is a multi-year investment before reaching perturbation-level predictions.

**When to reconsider:** Only if the LQC-native program completes successfully AND we need a fundamentally different UV completion to address formalism ambiguities (dressed-metric vs hybrid). GFT could eventually adjudicate between LQC formalisms. But that is a second-generation question.

---

## 4. Non-Minimal ECH with Fermions

**Why tempting:** "We haven't tested fermionic matter sourcing torsion at cosmological scales." Torsion couples to spin, fermions have spin, and the Dirac equation in Riemann-Cartan spacetime includes a four-fermion contact interaction. Maybe this does something at high density.

**Why avoid:** This is a different theory class from what our paper covers. The four-fermion interaction from torsion is suppressed by 1/M_Pl^2. At any cosmological temperature T, the spin-density contribution to the energy-momentum tensor scales as (T/M_Pl)^4 relative to the standard radiation contribution. Even at T = 10^16 GeV (GUT scale), this is suppressed by 10^-8. The gravitational democracy barrier applies: ALL gravitational couplings are Planck-suppressed, and fermion spin-density is no exception.

**The deeper issue:** Even if torsion propagates (which it does not in ECH, but does in PGT), the propagating modes couple at gravitational strength. We proved this in Foundation A: g_eff ~ 1/(M_Pl sqrt(|t_3|)). This is generic to gravitational theories.

---

## 5. CMB Anomaly Programs Without Sharp Predictions

**Why tempting:** Anomalies exist at 2-3 sigma (low-ell power deficit, parity asymmetry, hemispherical asymmetry). They seem to favor non-standard initial conditions. Bounce cosmology could explain them.

**Why avoid:** Evidence is not strong enough to anchor a superiority claim. The bounce evidence audit (file 01 of this series) downgraded ALL CMB anomaly claims from MODERATE to WEAK after discovering:
- The Durrer et al. (2023) challenge to the LQC bispectrum prediction
- All fits are qualitative (no Bayesian model comparison)
- Free parameters in the hemispherical asymmetry mechanism
- Alternative explanations exist (Gaztanaga 2025 direct-sum inflation)

Without a specific, quantitative, parameter-free prediction (not just "LQC could explain this qualitatively"), anomaly programs become hand-waving that reads as motivated reasoning.

**Exception:** Only worth pursuing if the LQC perturbation audit (path #1 in the ranked stack) produces a specific scale-dependent signature at ell < 30 that follows from the same Wilson-Ewing model we already study. In that case, it would be a natural extension, not a new program.

---

## 6. Hybrid Dark Energy Splice

**Why tempting:** "Could fix the DE sector while keeping the bounce." DESI data hints at w(z) != -1. Adding w0-wa to our MCMC would improve Delta-AIC by 6-8 points. The fit improvement is REAL.

**Why avoid:** EXHAUSTIVELY explored and rejected across 7+ disguised forms in this repository:
1. Program salvage audit (ranked last)
2. Foundation F (closed: attractor-sensitivity dilemma)
3. Foundation G (closed: bounce has NO CONNECTION to late-time DE)
4. Branch I (confirmed: "ships passing in the night," 122 orders of magnitude separation)
5. Branch U (self-identified failure risks)
6. Paper 1 open question (conceptual, never computed)
7. Foundation A Scenario D (fine-tuning equivalent to CC)

The core result: adding w0-wa to "bounce + LCDM" gives the SAME improvement as adding w0-wa to plain LCDM. The word "bounce" adds zero content to the DE sector. This was the original Paper 1 dream. It is dead. Do not resurrect it.

---

## 7. Running More MCMC Without New Theory

**Why tempting:** MCMC infrastructure works beautifully (236,000+ samples, 64 chains, R-hat < 0.005). Running more chains feels productive. New datasets keep appearing.

**Why avoid:** Current MCMC tests standard LCDM + Delta-N_eff with stock CAMB. Without a custom theory hook implementing bounce-specific modifications to the transfer functions or primordial spectra, more chains just reconfirm Delta-N_eff approximately 0 and H_0 = 67.68. This is not wrong, but it is not informative for the bounce program.

**When it becomes useful again:** When we have a concrete new model that modifies CAMB predictions. Specifically:
- If the f_NL program produces a scale-dependent prediction, implement it as a CAMB modification
- If LQC perturbation corrections modify the matter power spectrum, implement that
- If PBH production from the bounce is viable, the induced GW spectrum needs parameter estimation

Until then, the MCMC infrastructure is an asset in storage, not an active tool.

---

## Summary: The Common Thread

All seven paths share the same failure mode: **they generate activity without advancing the discriminator.** The single discriminator is f_NL = -35/8. Every hour spent on these paths is an hour not spent confirming, strengthening, or extending that prediction. The research program has exactly one live nerve. Protect it.

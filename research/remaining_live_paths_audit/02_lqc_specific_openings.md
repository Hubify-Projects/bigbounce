# LQC-Specific Openings

**Created:** 2026-03-18
**Status:** COMPLETE
**Purpose:** Identify questions that are genuinely LQC-specific -- not answered by generic matter-bounce calculations -- and assess each for novelty and tractability.

---

## Why LQC-Specific Matters

Our flagship prediction f_NL = -35/8 is a GENERIC matter-bounce result. It comes from the contraction phase, not from the bounce itself. The LQC framework adds quantum-geometry corrections that the generic calculation ignores. These corrections could:

1. **Modify f_NL during transfer through the bounce** (enhancement or suppression)
2. **Introduce scale dependence** (f_NL(k) instead of constant f_NL)
3. **Depend on the quantization scheme** (dressed-metric vs hybrid vs deformed algebra)
4. **Depend on the Barbero-Immirzi parameter** (gamma enters LQC but not generic bounce)

Any of these would be a genuinely LQC-specific result that cannot be obtained from the generic matter-bounce literature. This is where the program can produce NEW science rather than repackaging existing results.

---

## Opening 1: Dressed-Metric vs Hybrid Perturbation Formalisms

### What is open
Both the dressed-metric (Agullo-Ashtekar-Nelson 2013, Wilson-Ewing 2013) and hybrid (Fernandez-Mendez-Mena Marugan-Olmedo 2012-2014) approaches are widely used in LQC. They agree at the background level (same modified Friedmann equation, same bounce) but differ at the perturbation level:

- **Dressed-metric:** Perturbations propagate on the quantum-corrected effective background. The effective mass z''/z in the Mukhanov-Sasaki equation receives corrections from quantum geometry. These corrections suppress the tensor-to-scalar ratio (r ~ 10^-4 instead of generic O(1)).
- **Hybrid:** Perturbations are quantized separately from the background. The Mukhanov-Sasaki equation has different correction terms. Agreement with dressed-metric in the deep UV and far IR, but potential differences at intermediate scales.

The 2024 comparison paper (arXiv:2405.12296) documents differences in the power spectrum at intermediate k (near the bounce scale). For the bispectrum, NO comparison exists.

### What would be novel
If the two formalisms give different f_NL for the Wilson-Ewing quasi-dust model, that is a clean, publishable result with direct experimental implications: it changes the MegaMapper detection forecast.

If they agree, that is also publishable as a robustness theorem: the LQC matter-bounce f_NL is formalism-independent, making the prediction more credible.

Either way, this fills a genuine gap in the literature. Nobody has compared bispectrum predictions across LQC formalisms.

### Concrete test
1. Implement the Wilson-Ewing quasi-dust background (w = -0.003, Lambda contribution) in both dressed-metric and hybrid frameworks.
2. Compute the scalar perturbation transfer through the bounce in both formalisms.
3. Compute f_NL at third order (or estimate via Maldacena-consistency-relation arguments if third-order machinery is not available in one formalism).
4. Compare the two values. Report the fractional difference.

### Technical obstacles
- Third-order perturbation theory in LQC is not fully developed in either formalism. The dressed-metric approach has been carried to second order (power spectrum) but not systematically to third order (bispectrum).
- A practical shortcut: use the separate-universe / gradient-expansion approach (which works in the superhorizon limit) with the effective Friedmann equation from each formalism. This avoids the full third-order machinery.

### Status: OPEN. This is the single highest-priority LQC-specific calculation.

---

## Opening 2: Low-k Transfer / Infrared Specificity

### What is open
LQC modifies mode evolution at very large scales (k ~ k_LQC, where k_LQC is the characteristic LQC scale set by the bounce). Modes with k << k_LQC spend the longest time in the quantum-geometry regime and receive the largest corrections. This could produce:

- Scale-dependent power spectrum at ell < 30 (low-ell suppression)
- Scale-dependent non-Gaussianity: f_NL(k) that varies at low k

For the power spectrum, this has been computed (Agullo et al. 2013, 2021). For the bispectrum, it has NOT been computed for any specific model.

### What would be novel
A prediction for the RUNNING of f_NL -- f_NL(k) rather than constant -- at the lowest observable wavenumbers. This would be:

1. LQC-specific (generic matter bounce gives constant f_NL at all k)
2. Potentially observable via multi-tracer LSS techniques or CMB bispectrum tomography
3. A qualitative discriminator: inflation produces nearly constant f_NL, LQC bounce produces scale-dependent f_NL at low k

### Concrete test
1. Compute f_NL(k) for the Wilson-Ewing model in the dressed-metric formalism.
2. Check whether f_NL varies by more than 10% between k = 0.001 Mpc^-1 and k = 0.1 Mpc^-1.
3. If scale-dependent, compute the running alpha_fNL = d(f_NL)/d(ln k) and assess detectability.

### Technical obstacles
- Requires the full k-dependent transfer, not just the squeezed-limit amplitude.
- The LQC corrections are largest at k ~ k_LQC. Observable modes (k ~ 0.001-0.1 Mpc^-1) may be far from k_LQC, making the corrections negligible.
- The scale k_LQC depends on the bounce energy density rho_c and the number of e-folds of contraction. For rho_c ~ 0.41 M_Pl^4, k_LQC is typically far above observable scales unless the contraction phase is very long.

### Honest assessment of detectability
The LQC corrections to f_NL(k) at OBSERVABLE scales are likely small (the modes that reach our detectors exited the horizon deep in the contraction phase, far from the bounce). The corrections grow as k approaches k_LQC, but k_LQC may be 10^50 above observable k. If so, f_NL(k) is effectively constant at all observable scales, and this channel closes.

This needs to be computed, not assumed. But the prior expectation is that the effect is negligible for observable modes.

### Status: PARTIALLY OPEN. Worth computing as part of Path 1 infrastructure, but low prior probability of a detectable signal.

---

## Opening 3: Quantization-Ambiguity Sensitivity

### What is open
LQC has several quantization ambiguities:

1. **Barbero-Immirzi parameter (gamma):** Enters the quantum corrections through the minimum area gap. In ECH, gamma drops out of perturbations. In LQC, gamma enters the effective equations and affects the bounce density rho_c and the perturbation corrections.

2. **Holonomy corrections vs inverse-volume corrections:** Two classes of quantum corrections in LQC. Holonomy corrections (from the polymer quantization of the connection) dominate at high curvature. Inverse-volume corrections (from the discrete area spectrum) dominate at large volume. For the bounce, holonomy corrections are the primary effect. But some authors include both.

3. **Quantization of the Hamiltonian constraint:** Different operator orderings give slightly different effective equations. The standard Ashtekar-Pawlowski-Singh quantization (the "APS" scheme) is the most widely used, but alternatives exist.

### What would be novel
If f_NL depends on gamma or on the choice of quantum corrections:
- It would make the LQC bounce distinguishable from ad hoc bounces (which have no gamma dependence).
- It would provide a route to MEASURING gamma from cosmological data (if f_NL is gamma-sensitive and MegaMapper measures f_NL).
- It would identify which quantization ambiguities are observationally relevant.

If f_NL is INDEPENDENT of these ambiguities:
- It would strengthen the prediction by showing it is robust.
- It would indicate that the bispectrum is controlled by the contraction dynamics, not by the quantum bounce details.

### Concrete test
1. Compute f_NL in the APS quantization for 3 values of gamma (the standard gamma_0 = 0.2375, plus gamma_0/2 and 2*gamma_0).
2. Check whether f_NL varies by more than 1%.
3. If yes, compute df_NL/d(gamma) and assess whether MegaMapper could constrain gamma.

### Technical obstacles
- The standard LQC effective equations depend on gamma through the combination gamma * l_Pl^2 (the minimum area gap). This enters the bounce density rho_c = sqrt(3)/(32 pi^2 gamma^3 l_Pl^4). Changing gamma changes the bounce energy scale.
- However, for modes that are superhorizon at the bounce (k/k_bounce ~ 10^-56 for CMB-relevant modes), the bounce is effectively instantaneous regardless of rho_c. This suggests f_NL is gamma-independent for observable modes.
- The real sensitivity is in the transition: how quickly the universe exits the quantum regime. If the transition duration depends on gamma, the transfer function could be gamma-sensitive for modes near k_LQC.

### Prior expectation
f_NL at OBSERVABLE scales is very likely gamma-INDEPENDENT because the relevant modes exit the horizon deep in the classical contraction phase. The gamma dependence is confined to modes near the bounce scale, which are unobservable. This should be verified, but the prior is that the answer is null.

### Status: BARELY TOUCHED. Worth computing as a check (low effort once Path 1 infrastructure exists), but expected to give a null result for observable modes.

---

## Opening 4: Quasi-Dust Ekpyrotic Two-Field LQC

### What is open
The 2025 paper (arXiv:2509.06148) presents a two-field model in LQC where:
- An ekpyrotic field drives contraction (w >> 1) for BKL resolution
- A quasi-dust field provides the matter component for near-scale-invariant perturbations
- The LQC bounce connects contraction to expansion
- The authors claim viable n_s and r

The paper does NOT compute f_NL. This is the key open question.

### What would be novel
Three possible outcomes:

1. **f_NL is still approximately -35/8.** The two-field model reduces to single-field matter bounce for the bispectrum. This would be interesting but not surprising -- it would confirm that f_NL is controlled by the matter contraction, not by the ekpyrotic pre-phase.

2. **f_NL is significantly different from -35/8.** The ekpyrotic-matter transition produces entropy perturbations that modify the bispectrum. This would be a NEW prediction, potentially more or less testable than -35/8.

3. **f_NL is small (|f_NL| << 1).** The ekpyrotic dynamics suppress non-Gaussianity (as happens in some ekpyrotic models). This would kill the model's testability via f_NL, but might open the tensor channel (ekpyrotic models can have different r predictions).

### Concrete test
1. Implement the two-field background from arXiv:2509.06148.
2. Compute the adiabatic and entropy perturbations through the contraction phase.
3. Track the entropy-to-adiabatic conversion at the bounce.
4. Extract f_NL from the total (adiabatic + converted entropy) bispectrum.

### Technical obstacles
- Two-field perturbation theory is significantly more complex than single-field.
- The entropy-to-adiabatic conversion depends on the details of the bounce trajectory in field space, which is model-dependent.
- The ekpyrotic contraction generically produces large equilateral (not local) non-Gaussianity. Separating the local and equilateral contributions requires careful template analysis.

### Status: NOT TESTED. Worth pursuing if Path 1 confirms that single-field f_NL is robust, AND there is a specific reason to want a second model (e.g., n_s prediction advantage).

---

## Opening 5: Third-Order Perturbation Theory Through LQC Bounce

### What is open
This is the critical gap identified in the fnl_derivation_execution work. The situation is:

- **Pre-bounce f_NL = -35/8** is computed in the matter contraction phase using standard perturbation theory (no LQC corrections needed in the classical regime).
- **The bounce transfer** has been computed at second order (power spectrum: T(k) with LQC corrections giving r ~ 10^-4).
- **Third-order transfer through the bounce** has NOT been computed by anyone. This is the bispectrum transfer.

The assumption in all existing work is that superhorizon modes pass through the LQC bounce without modification to their non-Gaussian correlations. This is physically reasonable for modes with k/k_bounce ~ 10^-56, but it has NOT been verified.

### What would be novel
The first computation of bispectrum transfer through an LQC bounce. Three outcomes:

1. **Transfer is faithful (f_NL preserved):** The pre-bounce f_NL = -35/8 survives the bounce. This is the expected outcome and would strengthen the prediction.

2. **Transfer enhances f_NL:** The LQC corrections at the bounce enhance nonlinear coupling. If the enhancement pushes |f_NL| > 10.3, the model is EXCLUDED by current Planck data. This would be a death sentence for Model B but a novel result.

3. **Transfer suppresses f_NL:** The LQC corrections at the bounce reduce nonlinear coupling. This weakens the detection forecast but the model survives.

### Concrete approaches
Two routes, ordered by increasing rigor:

**Route A (separate-universe approximation):**
Use the gradient expansion / separate-universe approach with the effective LQC Friedmann equation. For superhorizon modes, this should capture the leading transfer effect. The LQC Friedmann equation H^2 = (8piG/3) rho (1 - rho/rho_c) is an algebraic modification. The separate-universe evolution differs from GR only near the bounce, and for modes with k << k_bounce, the difference is infinitesimal in zeta space.

Expected result: faithful transfer (f_NL unchanged), confirming the assumption.

**Route B (full third-order LQC perturbation theory):**
Develop the third-order perturbation equations in the dressed-metric formalism and solve through the bounce numerically. This is a significant technical undertaking, requiring:
- Third-order expansion of the dressed-metric effective equations
- Numerical evolution of bispectrum modes through the bounce
- Extraction of f_NL from the post-bounce bispectrum

This is the definitive calculation but likely requires months of work.

### Recommendation
Start with Route A (separate-universe). If it shows that the transfer is faithful for superhorizon modes (as expected), document this as a robustness result and move on. Only pursue Route B if Route A reveals unexpected behavior near the bounce scale.

### Status: NOT DONE. This is the second-highest priority LQC-specific calculation (after Opening 1), because it directly addresses whether the pre-bounce f_NL survives to become the post-bounce prediction.

---

## Summary: Priority Order for LQC-Specific Calculations

| Priority | Opening | Expected Outcome | Effort | Novelty if Non-Trivial |
|----------|---------|-----------------|--------|----------------------|
| 1 | Dressed-metric vs hybrid for f_NL | Agreement (60%) | MEDIUM | HIGH |
| 2 | Third-order transfer through bounce | Faithful (80%) | MEDIUM (Route A) | VERY HIGH |
| 3 | Quantization-ambiguity sensitivity | Null (80%) | LOW (once #1 exists) | HIGH |
| 4 | Scale-dependent f_NL(k) | Negligible (70%) | MEDIUM | HIGH |
| 5 | Two-field ekpyrotic f_NL | Unknown | HIGH | MEDIUM-HIGH |

### The honest bottom line

The most likely outcome of all five openings is that the LQC-specific corrections are negligible for observable modes. The modes that reach our detectors were superhorizon during the entire quantum-gravity epoch. The LQC corrections are confined to the bounce scale, and the bounce scale is 50+ orders of magnitude above observable k.

However, "most likely negligible" is not the same as "proven negligible." These calculations MUST be done to establish the prediction on firm ground. And if any of them reveal unexpected sensitivity, that would be the most important result in the program -- a genuinely LQC-specific observable signature.

The strategy is: compute them all (in priority order), expect null results, be prepared for surprises.

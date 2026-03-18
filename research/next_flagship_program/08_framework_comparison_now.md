# 08: Framework Comparison — ECH vs LQC vs Generic Matter-Bounce EFT

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Assessment Criteria

For each framework, assess: mathematical control, perturbation calculability, observable specificity, dependence on extra fields, current best flagship observable, major weakness, overall usefulness right now.

---

## ECH (Einstein-Cartan-Holst / Spin-Torsion)

### Mathematical Control: HIGH
- Clean Lagrangian formulation (Palatini + Holst term)
- Exact modified Friedmann equation: H^2 = (rho/3M^2)(1 - rho/rho_c)
- rho_c = 0.21 M_Pl^4 derived from Immirzi parameter gamma = 0.274
- No ambiguities in the background equations

### Perturbation Calculability: LOW
- ECH is perturbation-transparent (Branch Vb result)
- Scalar fields have zero spin current -> torsion = 0 -> perturbation equations are exactly classical Mukhanov-Sasaki
- The bounce modifies the background but NOT the perturbation equations
- No ECH-specific perturbation corrections exist

### Observable Specificity: NONE
- rho_c from gamma = 0.274 is the only ECH-specific parameter
- All perturbation-level predictions are identical to classical GR with a bounce
- No ECH-specific observable signature has been identified
- 14 ECH barriers confirmed this over the entire research program

### Dependence on Extra Fields: NONE
- Standard matter content only
- Torsion is non-propagating (auxiliary field, integrated out exactly)

### Current Best Flagship Observable: NONE
- ECH produces no distinctive perturbation signatures
- f_NL = -35/8 is a matter-bounce prediction, not ECH-specific
- r suppression requires LQC-type corrections that ECH does not provide

### Major Weakness: PERTURBATION TRANSPARENCY
The entire reason ECH cannot drive a positive observable program is that scalar perturbations do not feel the torsion. The bounce is real (non-singular cosmology), but the observable consequences are carried by classical GR perturbation theory, not by ECH corrections.

### Overall Usefulness Right Now: LOW
ECH provides the cleanest derivation of the modified Friedmann equation (one parameter, gamma). It serves as a theoretical "proof of concept" that spin-torsion cosmology produces a bounce. But for the active flagship program, ECH adds nothing beyond what generic matter bounce gives.

---

## LQC (Loop Quantum Cosmology)

### Mathematical Control: MEDIUM-HIGH
- Effective equations derived from full loop quantization (Ashtekar, Pawlowski, Singh)
- Background: H^2 = (rho/3M^2)(1 - rho/rho_c) with rho_c = 0.41 rho_Pl
- Perturbations: dressed-metric approach (Agullo, Ashtekar, Nelson)
- Some ambiguity between dressed-metric and hybrid quantization schemes
- rho_c depends on quantization scheme details (not as cleanly fixed as ECH)

### Perturbation Calculability: MEDIUM-HIGH
- The dressed-metric approach gives explicit modified Mukhanov-Sasaki equations
- Scalar and tensor modes have DIFFERENT effective potentials through the bounce
- This differential treatment is what allows r suppression
- Third-order (bispectrum) perturbation theory has been attempted (Agullo et al. 2015 for inflation) but NOT for the matter bounce

### Observable Specificity: MEDIUM
- r ~ 10^-4 from differential scalar/tensor amplification (specific to LQC dressed-metric)
- f_NL transfer through bounce is calculable in principle (not yet done)
- n_T > 0 (blue tensor tilt, specific to bounce but unmeasurable at r ~ 10^-4)
- alpha_s > 0 (positive running, from Lehners & Wilson-Ewing 2015)

### Dependence on Extra Fields: NONE (for the quasi-dust model)
- Uses dust + Lambda (LCDM matter content)
- No curvaton, no entropy field, no extra scalars

### Current Best Flagship Observable: f_NL = -35/8
- Set by matter contraction dynamics (pre-bounce)
- LQC may modify through bounce transfer (not computed)
- Detection by MegaMapper at 4.4-8.75 sigma (depending on which value is correct)

### Major Weakness: QUANTIZATION AMBIGUITY
The dressed-metric and hybrid approaches give different predictions for perturbation evolution through the bounce. The choice between them is a theoretical commitment, not a derivation from first principles. This introduces model uncertainty.

Also: the third-order perturbation theory needed to compute f_NL through the bounce is not available.

### Overall Usefulness Right Now: HIGH
LQC is the only framework that provides both a clean bounce AND perturbation-level corrections that affect observables. It is the natural home for the flagship f_NL program. The quasi-dust model (Wilson-Ewing) gives the most economical viable scenario.

---

## Generic Matter-Bounce EFT

### Mathematical Control: LOW-MEDIUM
- Background: parametrized by rho_c (free parameter)
- Perturbations: classical Mukhanov-Sasaki (no bounce corrections)
- Bounce mechanism: unspecified (could be NEC violation, higher-derivative gravity, etc.)
- Bounce transfer: model-dependent or assumed transparent

### Perturbation Calculability: LOW
- Without specifying the bounce mechanism, the perturbation transfer through the bounce is undetermined
- The pre-bounce perturbation spectrum is calculable (same as matter contraction)
- The post-bounce spectrum depends on the (unspecified) bounce details

### Observable Specificity: LOW
- f_NL = -35/8 from contracting phase (same as LQC and ECH)
- r is undetermined (depends on bounce transfer)
- No specific r prediction without choosing a bounce mechanism
- BKL stability, ghost/gradient stability — all model-dependent

### Dependence on Extra Fields: DEPENDS
- Minimal model: single scalar field
- Extended models: curvaton, multiple scalars, NEC-violating fields
- The flexibility is both a strength (can accommodate data) and a weakness (low predictivity)

### Current Best Flagship Observable: f_NL = -35/8 (pre-bounce only)
- Same value as LQC, but without the bounce transfer information
- Cannot predict r without specifying the bounce mechanism

### Major Weakness: TOO MUCH FLEXIBILITY
Generic EFT can accommodate almost anything by choosing the bounce mechanism. This makes it unfalsifiable: if one bounce mechanism fails, switch to another. This is the "dressed-up multifield phenomenology" danger identified in the pass-2 analysis.

### Overall Usefulness Right Now: MEDIUM (as a reference framework)
Useful for computing pre-bounce perturbation quantities (which are model-independent). But the post-bounce predictions require committing to a specific framework (LQC, ECH, Horndeski, etc.). Using generic EFT alone risks drifting into generic phenomenology.

---

## Head-to-Head Comparison

| Criterion | ECH | LQC | Generic EFT |
|-----------|-----|-----|-------------|
| Mathematical control | HIGH | MEDIUM-HIGH | LOW-MEDIUM |
| Perturbation calculability | LOW (transparent) | **MEDIUM-HIGH** | LOW |
| Observable specificity | NONE | **MEDIUM** | LOW |
| Dependence on extra fields | None | None | Varies |
| Best flagship observable | None | **f_NL = -35/8** | f_NL (pre-bounce only) |
| r prediction | None (classical) | **~10^-4** | Undetermined |
| Major weakness | Perturbation-transparent | Quantization ambiguity | Too flexible |
| Overall usefulness now | LOW | **HIGH** | MEDIUM (reference only) |

---

## Answers to Key Questions

### Is LQC now the best framework for the active flagship program?

**YES.** LQC is the only framework that:
1. Provides perturbation-level corrections (r suppression)
2. Has a specific quantitative prediction for r (~10^-4)
3. Gives a calculable bounce transfer matrix
4. Supports the quasi-dust model (Wilson-Ewing) which is the most viable

ECH is perturbation-transparent and cannot drive observable predictions. Generic EFT is too flexible and cannot pin down the bounce transfer.

### Is ECH still useful anywhere in the positive program?

**LIMITED.**

ECH is useful as:
- A clean derivation of rho_c from gamma = 0.274 (cross-check on LQC rho_c)
- A proof that spin-torsion cosmology produces a bounce (theoretical existence proof)
- A contrast framework: "ECH gives no perturbation corrections; LQC does. This is a TESTABLE difference between two quantum gravity approaches." This contrast is itself a scientific contribution.

ECH is NOT useful for:
- Driving observable predictions
- Computing perturbation spectra
- The flagship f_NL program

### Should ECH be repositioned mainly as a negative-result / mechanism / contrast framework?

**YES.** ECH's primary scientific value in the positive program is:

1. **Negative result:** "ECH is perturbation-transparent, establishing that not all quantum gravity completions produce observable perturbation corrections"
2. **Mechanism comparison:** "ECH and LQC share the same background but differ at perturbation level, making this a TESTABLE difference between quantum gravity frameworks"
3. **Existence proof:** "Spin-torsion cosmology demonstrates that bouncing cosmology does not require exotic matter or NEC violation — standard geometric corrections suffice"

### Is generic matter-bounce EFT more dangerous because it can become too flexible?

**YES.** Generic EFT is the path toward the failure mode identified in the pass-2 analysis: "GENERIC_MULTIFIELD_MODEL_DISGUISED_AS_BOUNCE." Without committing to a specific UV completion (LQC, ECH, or other), the bounce model can accommodate any observation by tuning the bounce transfer function. This makes it unfalsifiable.

The discipline is: commit to LQC for the perturbation physics, accept the consequences (both positive predictions AND potential falsification), and state clearly which predictions are LQC-specific versus generic.

---

## Framework Strategy Going Forward

1. **LQC** is the primary computational framework for perturbation physics and observable predictions
2. **ECH** is retained as a contrast framework and background cross-check
3. **Generic EFT** is used only for pre-bounce calculations that are demonstrably model-independent (e.g., f_NL = -35/8 from matter contraction, n_s = 1 - 12*epsilon)
4. Every result is tagged with its framework dependence:
   - "GENERIC" = independent of bounce mechanism
   - "LQC-SPECIFIC" = depends on dressed-metric perturbation corrections
   - "ECH-SPECIFIC" = depends on spin-torsion perturbation physics (currently: nothing)

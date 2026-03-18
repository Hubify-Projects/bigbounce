# Final Verdict: f_NL Derivation Program

**Created:** 2026-03-17
**Status:** PROGRAM DESIGN COMPLETE — EXECUTION BEGINS

---

## Question 1: Is the target quantity well-defined?

**YES.**

The target is f_NL^local in the Planck convention, extracted from the squeezed-limit bispectrum via:

$$
f_{\rm NL} = \frac{5}{12} \frac{B_\zeta(k_1, k, k)}{P(k_1) P(k)} \bigg|_{k_1 \to 0}
$$

All conventions are locked (file 02). The quantity is the same f_NL that Planck reports as -0.9 +/- 5.1 and that MegaMapper will constrain to sigma ~ 0.5. There is no ambiguity in what we are computing.

---

## Question 2: What are the two independent derivation paths?

**Path A (Gradient Expansion / Separate Universe):**
- Uses the scalar-field separate-universe approach (NOT the fluid approximation)
- Perturbs the amplitude and phase of the oscillating scalar field
- Tracks the growing mode of zeta through second-order nonlinear evolution
- Extracts f_NL as the coefficient of (zeta^(1))^2 in zeta^(2)
- Physical insight: f_NL arises from nonlinear coupling between growing modes

**Path B (In-In / Cubic Action):**
- Starts from the Maldacena cubic action at epsilon = 3/2, c_s = 1
- Uses exact Bunch-Davies mode functions
- Evaluates the time integrals in the in-in (Schwinger-Keldysh) formalism
- Extracts the bispectrum B_zeta and applies the locked extraction formula
- Computational insight: directly reproduces (or refutes) Cai et al.

**Agreement between both paths validates the result. Disagreement identifies which approximation fails.**

---

## Question 3: What is the biggest single ambiguity?

**The normalization conversion between Cai et al.'s |B|_NL and the Planck f_NL.**

Cai et al. define |B|_NL = (10/3) A_T / (sum k_i^3). This is NOT f_NL^local. The identification |B|_NL = f_NL^local assumes the shape is exactly local. Cai et al. themselves state the shape is only "loosely local."

If the shape deviates from local by O(1) in the equilateral region, the template-projected f_NL^eff could differ from the squeezed-limit f_NL by a cosine factor. This cosine factor has never been computed.

**This ambiguity is resolved by:**
1. Computing B_zeta directly from the cubic action (Path B)
2. Applying our locked extraction formula (not Cai et al.'s |B|_NL)
3. Computing the template projection as a separate step (file 06)

---

## Question 4: Does -35/8 still look plausibly defensible?

**YES, but not guaranteed.**

Arguments FOR -35/8:
- Cai et al. computed directly at c_s = 1 with no small-c_s approximation
- The paper has been cited 200+ times with this value and no published correction
- The Li-Brandenberger discrepancy may be an approximation artifact (their formula uses "~")
- Our convention analysis confirms no additional factor-of-2 from Phi vs zeta

Arguments AGAINST -35/8:
- Li & Brandenberger's independent calculation gives -2.19 at c_s = 1
- The Quintin citation of -35/16 suggests at least one other group found a factor-of-2 difference
- Cai et al.'s |B|_NL normalization is non-standard and the conversion to f_NL^local is non-trivial
- No independent reproduction of -35/8 exists

**Subjective probability: ~35% that -35/8 is exactly right, ~60% that the true value is negative and O(1), ~5% that something unexpected happens (positive, zero, or scale-dependent).**

---

## Question 5: What would kill the flagship lane?

Any of the following:

1. **f_NL is positive.** The sign discrimination against inflation is the core of the flagship claim. Positive f_NL makes the matter bounce indistinguishable from inflation at the non-Gaussianity level.

2. **|f_NL| < 0.5.** MegaMapper sensitivity is sigma ~ 0.5. If |f_NL| < 0.5, detection is impossible and the matter bounce has no testable distinctive prediction.

3. **f_NL is not a pure number.** If f_NL depends on the time of evaluation, the k-ratio, or the bounce model details, it is not a parameter-free prediction. This converts a hard prediction into a soft one, undermining the main advantage over inflation.

4. **The squeezed limit is pathological.** If the bispectrum has an IR divergence or the squeezed limit does not exist (growing-mode singularity), the prediction is ill-defined.

**Most likely failure mode:** |f_NL| turns out to be ~1-2 (between Cai and our expectations), AND the template projection reduces it further by a factor of 0.5-0.7, giving |f_NL^eff| < 1. This is the "death by a thousand cuts" scenario where no single step kills the prediction but the cumulative effect makes it undetectable.

---

## Question 6: What is the exact first derivation step to execute?

**Verify the power spectrum normalization from the exact Bunch-Davies mode function.**

Specifically:

1. Start from v_k(eta) = (e^{-ik eta} / sqrt(2k)) (1 - i/(k eta))
2. Convert to zeta_k = v_k / z with z = a_0 sqrt(3) eta^2
3. Compute P(k) = |zeta_k|^2 on superhorizon scales
4. Verify P_zeta(k) = k^3 P(k) / (2 pi^2) is k-independent (scale invariant)
5. Express P_zeta in terms of a_0 and eta
6. Compare with Cai et al. (2009) power spectrum

**This step is already 90% complete in file 08.** The result is:

$$
P(k, \eta) = \frac{1}{6k^3 a_0^2 \eta^6}, \quad \mathcal{P}_\zeta = \frac{1}{12\pi^2 a_0^2 \eta^6}
$$

**After verification: proceed to the bispectrum calculation via Path B (in-in formalism), which directly compares with Cai et al.**

---

## Program Architecture Summary

```
01_exact_target_statement.md     ← What we're computing (DONE)
02_notation_and_convention_lock.md ← All conventions fixed (DONE)
03_literature_discrepancy_map.md  ← The disagreement decomposed (DONE)
04_derivation_path_A.md          ← Gradient expansion setup (DONE)
05_derivation_path_B.md          ← In-in cubic action setup (DONE)
06_template_projection_problem.md ← Shape projection analysis (DONE)
07_decision_tree_of_outcomes.md  ← All possible results mapped (DONE)
08_first_executable_step.md      ← Power spectrum verification (DONE)
09_manuscript_ready_note.md      ← Internal research justification (DONE)
final_verdict.md                 ← This file (DONE)
```

**All 10 program files are complete. The derivation can now begin.**

---

## The Derivation Execution Order

1. **Power spectrum verification** (file 08) — confirm P(k) normalization
2. **In-in bispectrum** (Path B, file 05) — compute B_zeta from cubic action
3. **f_NL extraction** — apply locked formula to get squeezed-limit f_NL
4. **Cross-check via gradient expansion** (Path A, file 04) — verify with separate-universe approach
5. **Template projection** (file 06) — compute cos(theta) and f_NL^eff
6. **Outcome assessment** (file 07) — determine which branch we're on
7. **MegaMapper forecast update** — revise detection significance

---

## Final Statement

The f_NL derivation program is designed, scoped, and ready to execute. The conventions are locked, the literature discrepancy is mapped, two independent derivation paths are scaffolded, the outcome tree is complete, and the first step is identified.

**The single most important number in this repository — f_NL^local for the matter bounce — will be derived from first principles. Whatever value emerges will determine the future of the entire research program.**

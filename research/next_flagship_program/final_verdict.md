# Final Verdict: Next Flagship Program

**Created:** 2026-03-17
**Status:** COMPLETE

---

## 1. What exactly is the current flagship positive research lane?

**The Wilson-Ewing LCDM Quasi-Dust Matter Bounce in LQC, with the flagship discriminator f_NL^local = -35/8 = -4.375.**

The model:
- Matter contraction with w = -epsilon = -0.003 (from Lambda contribution) -> n_s = 0.964
- LQC quantum bounce at rho_c ~ 0.41 M_Pl^4 -> singularity resolution
- LQC dressed-metric perturbation corrections -> r ~ 10^-4
- Matter contraction nonlinear dynamics -> f_NL = -35/8 (pre-bounce, GENERIC)
- Ekpyrotic pre-phase (w >> 1) for ~10 e-folds -> BKL resolution

**0 extra fields, 1 fitted parameter (epsilon), 1 parameter-free testable prediction (f_NL).**

---

## 2. Does it live primarily in LQC, generic matter bounce, ECH, or combination?

**Primarily LQC, with generic matter-bounce contributions.**

| Component | Framework |
|-----------|-----------|
| n_s = 1 - 12*epsilon | GENERIC (any matter bounce) |
| r ~ 10^-4 | **LQC-SPECIFIC** (dressed-metric) |
| f_NL = -35/8 (pre-bounce) | GENERIC (matter contraction dynamics) |
| f_NL transfer through bounce | **LQC-SPECIFIC** (needs dressed-metric at third order) |
| Singularity resolution | GENERIC (any bounce) |
| BKL resolution | GENERIC (ekpyrotic pre-phase) |

ECH enters only as a contrast framework and background cross-check. It provides no perturbation-level predictions.

---

## 3. What is the repo-wide verdict on the "hybrid splice-in DE" loophole?

**EXHAUSTIVELY EXPLORED AND RIGOROUSLY REJECTED.**

The loophole was investigated in at least 7 disguised forms across the repository:
- Program salvage audit (ranked last, called "routine")
- Foundation F (closed: attractor-sensitivity dilemma)
- Foundation G (closed: "bounce has NO CONNECTION to late-time DE")
- Branch I (confirmed: "ships passing in the night, 122 orders of magnitude separation")
- Branch U (problem statement only, self-identified failure risks)
- Paper 1 open question (conceptual, never computed)
- Foundation A Scenario D (fine-tuning equivalent to CC)

**No w0, wa, or w(z) parameter was ever included in any MCMC run.** All 236,622+ chain samples use fixed w = -1.

The literature confirms our conclusion: nobody anywhere derives w(z) from a bounce mechanism. Every paper that combines bounce + DE either adds DE by hand, reconstructs a Lagrangian from desired cosmology, or invokes a conceptual (not causal) connection.

---

## 4. Would that loophole have saved Paper 1?

**YES, at fit level.** Adding w0wa to our MCMC would have:
- Improved Delta-AIC by ~6-8 points (matching DESI-preferred dynamical DE)
- Placed our model in the (w0 > -1, wa < 0) quadrant
- Allowed a claim like "ECH cosmology with dynamical DE fits DESI better than LCDM"

The fit improvement would have been real. The chi-squared decrease would have been genuine.

---

## 5. Why did we reject it?

**Because the fit improvement comes entirely from the w0wa freedom, not from the bounce.**

This loophole would have saved Paper 1 at fit level, but we rejected it on first-principles grounds because it replaces derivation with phenomenological late-time freedom. Specifically:

1. Adding w0wa to "bounce + LCDM" gives the same improvement as adding w0wa to plain LCDM (Branch I)
2. The bounce contributes nothing to the DE sector (Foundations A-G, all closed)
3. The DE prediction is unfalsifiable (two free parameters absorb any w(z))
4. The IR vacuum program explicitly classified "reducing to CPL" as a failure mode
5. The literature already does this (arXiv:2601.03028), and it carries no theoretical content beyond parameter fitting

**A bounce cosmology paper that fits DESI via w0wa is scientifically equivalent to a LCDM paper that fits DESI via w0wa. The word "bounce" adds zero content to the DE sector.**

---

## 6. What is the single-point-of-failure in the current positive program?

**f_NL = -35/8 being correct, robust, and preserved through the LQC bounce.**

If this value falls, the model has:
- No testable f_NL prediction (or too small to be distinctive)
- An untestable r prediction (~10^-4, below all planned detectors)
- A fitted n_s (comparable to Starobinsky with fewer virtues)
- No fallback discriminator

**THREE SPECIFIC THREATS to the single-point-of-failure:**

1. **The Li & Brandenberger discrepancy:** Their formula gives f_NL ~ -2.2 at c_s = 1, not -4.375. If correct, MegaMapper detection drops from 8.75 sigma to 4.4 sigma. Still interesting but less decisive, and the discrepancy would indicate the Cai et al. calculation has issues.

2. **The Quintin no-go enhancement:** If LQC r suppression also enhances |f_NL| beyond Planck bounds (|f_NL| > 10.3), the model is already observationally excluded.

3. **The "loosely local" shape:** The -35/8 is the squeezed-limit amplitude. The template projection onto the Planck local template may give a different effective f_NL.

---

## 7. What exact next derivation/calculation should be done immediately?

**Gradient-expansion derivation of f_NL in matter contraction, tracking the growing mode of zeta.**

### Specification:
- **Method:** Extended Salopek-Bond gradient expansion to second order in perturbation theory
- **Background:** a(t) = a_0 (-t/t_0)^{2/3}, canonical scalar field with V = m^2 phi^2/2, w = 0
- **Key steps:**
  1. Write perturbed local Friedmann equation to second order
  2. Solve for growing mode: zeta^(1) proportional to (-t)^{-1}
  3. Identify quadratic source for zeta^(2) from the growing mode
  4. Solve for zeta^(2) and extract f_NL = (5/6) zeta^(2)/(zeta^(1))^2
- **Output:** A pure number for f_NL^local in the Planck convention
- **Cross-check:** Compare with -35/8 (Cai et al.) and -2.2 (Li-Brandenberger at c_s = 1)

### Why this dominates alternatives:
- Resolves the foundation crisis (three discrepant values)
- Fastest path to a definitive answer (paper-and-pencil algebra)
- Immediately clarifies the entire program trajectory
- No numerical codes, no LQC machinery, no bounce transfer needed
- Every possible outcome is informative

---

## 8. What should be mentioned explicitly in all future research framing?

### Always state:
1. **Framework:** Whether a result is GENERIC (any matter bounce), LQC-SPECIFIC, or ECH-SPECIFIC
2. **The hybrid DE rejection:** "We explicitly considered and rejected late-time DE freedom. Our claims are restricted to observables the bounce physics genuinely controls."
3. **The single-point-of-failure:** "The distinctive prediction rests on f_NL = -35/8. This has not been independently reproduced and has discrepancies with Li & Brandenberger (2016)."
4. **The ECH contrast:** "ECH and LQC share the same background but differ at perturbation level. ECH is perturbation-transparent. LQC provides perturbation corrections that suppress r and may affect f_NL."
5. **What would kill the model:** "MegaMapper measurement of f_NL = 0.0 +/- 0.5 would exclude the matter bounce prediction at >4.4 sigma (or >8.75 sigma, depending on which pre-bounce value is correct)."

### Never claim:
- That the bounce "explains" or "predicts" dark energy
- That ECH provides perturbation-level predictions
- That f_NL = -35/8 is established beyond doubt
- That the model is "better than inflation" (it is conditionally competitive, contingent on f_NL measurement)

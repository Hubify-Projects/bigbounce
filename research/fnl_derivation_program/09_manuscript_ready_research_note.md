# 09: Manuscript-Ready Research Note

**Created:** 2026-03-17
**Status:** COMPLETE — INTERNAL NOTE, NOT FOR PUBLICATION

---

## Title: Status of the Matter Bounce f_NL Prediction

### Purpose

This note records the scientific reasoning behind three critical decisions:
1. Why hybrid dark energy was rejected
2. Why LQC is the active framework
3. Why the f_NL derivation is the single most important next calculation

This is an internal research note for continuity and clarity. It is NOT paper prose.

---

## 1. Rejection of the Hybrid Dark Energy Loophole

### What the loophole is:

The bounce cosmology model (modified Friedmann equation H^2 = rho/3M^2 * (1 - rho/rho_c)) can be supplemented with a late-time dark energy equation of state w(z) != -1, parametrized as w = w_0 + w_a z/(1+z) (CPL). This adds two free parameters (w_0, w_a) that can improve the fit to current observational data.

### Why it was explored:

The Paper 1 MCMC analysis showed the minimal bounce model (w = -1 exactly) underperforming LCDM at the fit level by Delta-AIC ~ +2 to +6 depending on the dataset combination. Adding w_0, w_a freedom would recover Delta-AIC ~ -6 to -8, making the bounce model statistically competitive.

### Why it was rejected:

1. **The improvement comes from CPL freedom, not from bounce physics.** Any model — LCDM, quintessence, k-essence — gains the same improvement from w_0 != -1 and w_a != 0. The bounce has no role.

2. **No derivation exists.** Nobody in the literature derives w(z) from a bounce Lagrangian. The bounce modifies H^2 at rho ~ rho_c (Planck density). Late-time dark energy lives at rho ~ 10^{-120} rho_Pl. These are separated by 120 orders of magnitude. The connection is phenomenological, not physical.

3. **Explored exhaustively.** The hybrid DE approach was tried in 7+ disguised forms across the repository:
   - Foundation A (PGT coupling)
   - Foundation B (Nieh-Yan non-topological)
   - Foundation C (environmental mass)
   - Foundation D (disformal)
   - Foundation F (initial conditions)
   - Foundation G (vacuum selection)
   - Branches I, U (direct parametric)
   Each closed with a distinct structural barrier. The barriers are not technical limitations — they reflect the physical disconnection between Planck-scale bounce and meV-scale dark energy.

4. **Manuscript-ready rejection statement:** "This loophole would have saved Paper 1, but we rejected it on first-principles grounds because it replaces derivation with phenomenological late-time freedom. The improvement in chi^2 is indistinguishable from adding CPL parameters to LCDM without a bounce."

### Current status: PERMANENTLY CLOSED.

---

## 2. Framework Selection: LQC as Primary

### The three candidate frameworks:

| Framework | Perturbation corrections | r prediction | f_NL modification | Status |
|-----------|------------------------|-------------|-------------------|--------|
| ECH (Einstein-Cartan-Holst) | None (perturbation-transparent) | Unmodified | None | BACKGROUND ONLY |
| LQC (Loop Quantum Cosmology) | Dressed-metric approach | r ~ 10^-4 (suppressed) | Possible enhancement | ACTIVE |
| Generic EFT (model-independent) | Parametric | Free | Free | TOO FLEXIBLE |

### Why LQC:

1. **Perturbation corrections exist.** LQC's dressed-metric approach provides concrete equations for perturbations through the bounce. This is essential for computing how the pre-bounce bispectrum transfers to the post-bounce era.

2. **Tensor suppression.** LQC naturally suppresses the tensor-to-scalar ratio to r ~ 10^-4 through quantum geometry effects. This removes the r/f_NL tension identified by Quintin et al. (2015).

3. **Falsifiable predictions.** LQC gives specific numbers (rho_c = 0.41 rho_Pl, gamma = 0.2375 from black hole entropy) that enter observable predictions. The model is not infinitely flexible.

### Why NOT ECH:

ECH gives the same modified Friedmann equation as LQC (with rho_c = 0.21 M_Pl^4 from gamma = 0.274), but the Branch Vb analysis showed that ECH is **perturbation-transparent**: scalar perturbations pass through the bounce unmodified at linear order. This means:
- ECH cannot suppress r
- ECH cannot modify f_NL at the bounce
- ECH adds nothing beyond the background dynamics

ECH remains as a contrast framework (demonstrating that the modified Friedmann equation alone is insufficient), but it is not the active framework for predictions.

### Why NOT generic EFT:

The EFT approach (parametrize the bounce without committing to LQC or ECH) is too flexible. With enough EFT parameters, any observation can be fitted. This makes the framework unfalsifiable. We use EFT only for pre-bounce, model-independent results where the bounce details don't matter.

---

## 3. Why the f_NL Derivation is the Single Most Important Calculation

### The argument in five steps:

**Step 1: The matter bounce has exactly one distinctive observable.**

After the second-pass viability filter:
- n_s = 0.964 is a one-parameter fit (epsilon = 0.003), not a prediction
- r ~ 10^-4 is below any foreseeable detection threshold
- alpha_s (running) is unmeasurably small
- The only parameter-free, detectable, hard-to-mimic prediction is f_NL^local = -35/8

**Step 2: This observable has a disputed value.**

Three literature values exist: -35/8, -35/16, and -2.19. Two are independent calculations. They disagree by a factor of ~2. No reproduction exists.

**Step 3: The dispute cannot be resolved by reading the literature more carefully.**

The discrepancy may arise from:
- Convention differences (|B|_NL vs f_NL^local)
- Approximation artifacts (c_s -> 1 limit of a c_s << 1 formula)
- Template projection vs squeezed-limit extraction
- An actual computational error in one of the papers

These possibilities cannot be distinguished without an independent calculation.

**Step 4: The model's scientific viability depends on the exact value.**

| Value | MegaMapper sigma | Verdict |
|-------|-----------------|---------|
| -4.375 | 8.75 | Definitive detection |
| -2.19 | 4.4 | Strong evidence (pre-projection) |
| -1.0 | 2.0 | Marginal |
| < 0.5 | < 1.0 | Undetectable |

If |f_NL| < 1, the matter bounce has NO remaining discriminator and the entire program must pivot.

**Step 5: The derivation is computationally tractable.**

The calculation requires:
- Linear mode functions (known, Bessel functions)
- Cubic action for canonical scalar field (known, Maldacena 2003)
- Time integrals in the squeezed limit (analytically tractable)
- Convention conversion (locked in file 02)

This is hard but doable. It does not require new physics, new numerical codes, or access to computing resources beyond paper and pencil (or a CAS).

### Conclusion:

The f_NL derivation has the highest information-per-effort ratio of any calculation available. It either confirms the flagship prediction (enabling the full MegaMapper forecast) or reveals that the prediction is wrong (redirecting the program before further investment).

---

## Summary of Current Program State

| Component | Status | Confidence |
|-----------|--------|------------|
| Background cosmology (modified Friedmann) | ESTABLISHED | HIGH |
| Power spectrum (n_s = 1 - 12 epsilon) | ESTABLISHED | HIGH |
| Tensor spectrum (r ~ 10^-4 in LQC) | ESTABLISHED | MEDIUM (LQC-specific) |
| f_NL^local (matter bounce bispectrum) | DISPUTED | LOW — derivation needed |
| Template projection (f_NL^eff) | NOT COMPUTED | UNKNOWN |
| Bounce transfer at third order | NOT COMPUTED | UNKNOWN |
| MegaMapper forecast | DEPENDS ON f_NL | CONDITIONAL |

**The derivation program (files 01-08) is designed to move "f_NL^local" from DISPUTED/LOW to ESTABLISHED/HIGH.**

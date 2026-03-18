# 06: Shortest Path to an Actual Discriminator

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Situation After Pass 2

The viable model is: **Wilson-Ewing LCDM Quasi-Dust Bounce** (Model B)
- n_s = 1 - 12*epsilon = 0.964 (from w = -epsilon = -0.003)
- r ~ 10^-4 (from LQC dressed-metric)
- f_NL = -35/8 = -4.375 (from matter contraction, parameter-free, CONFIRMED in Planck convention)

The flagship discriminator is: **f_NL^local = -4.375**

---

## What Needs Verification

The f_NL = -35/8 prediction is from Cai et al. (2009), computed for the CONTRACTING phase. Three things could modify the post-bounce observable value:

### 1. Bounce Transfer Effect on f_NL

The LQC bounce modifies the perturbation evolution through the dressed-metric corrections. These corrections suppress r (tensor-to-scalar ratio) by differentially amplifying scalar modes. But scalar amplification at the bounce also affects the NONLINEAR perturbation transfer.

**Question:** Does the LQC bounce transfer matrix preserve, enhance, or wash out f_NL = -35/8?

If the bounce amplifies the scalar power spectrum by a factor A_s^bounce, then naively the bispectrum (three-point function) scales as (A_s^bounce)^(3/2), while the power spectrum scales as A_s^bounce. The ratio B/(P^2) — which determines f_NL — then scales as (A_s^bounce)^(-1/2).

**BUT this is only correct for Gaussian amplification.** If the bounce introduces its own nonlinear corrections (which LQC does, through the rho^2 term), the f_NL transfer could be more complex.

### 2. The EOS Correction to f_NL

The -35/8 is derived for exact dust (w = 0). The viable model has w = -0.003. Does the small EOS correction modify f_NL?

For w = -epsilon with epsilon << 1:
f_NL(w) = -35/8 + O(epsilon)

The leading correction is at most O(epsilon) ~ O(0.003) ~ 0.01. This is negligible compared to the base value of -4.375.

**This does NOT need further calculation.** The correction is negligible.

### 3. The Lambda Contribution

In the LCDM bounce, Lambda provides the effective w < 0. During the contracting phase, Lambda is subdominant to the matter density (which grows as a^-3 during contraction, while Lambda stays constant). The f_NL calculation of Cai et al. applies to the matter-dominated epoch, when Lambda is negligible.

**Lambda does not modify f_NL.** The nonlinear dynamics that set f_NL occur deep in the matter-dominated contraction, where Lambda/rho << 1.

---

## Candidate Next Calculations

### Calculation A: f_NL Transfer Through the LQC Bounce

**What:** Compute the bispectrum (three-point function) of the curvature perturbation zeta through the LQC bounce in the dressed-metric approach.

**Why it matters:** If the bounce preserves f_NL = -35/8, the prediction is solid. If it enhances |f_NL|, the prediction becomes even more distinctive. If it washes out f_NL to ~0, the model loses its discriminator.

**Technical approach:**
1. Use the dressed-metric effective equations for the Mukhanov-Sasaki variable v_k
2. Evolve v_k through the bounce with the LQC-modified z''/z potential
3. Compute the third-order action for the curvature perturbation
4. Evaluate the bispectrum in the squeezed limit

**Difficulty:** HIGH. This is a full perturbation-theory calculation at third order in LQC. Only Agullo & Morris (2015) have attempted anything like this, and their results are limited.

**Literature status:** Agullo, Ashtekar, & Gupt (2015, arXiv:1510.05630) computed the LQC bispectrum for inflation (not the matter bounce). They found that the LQC bounce adds an oscillatory correction to the inflationary bispectrum, but does not fundamentally change f_NL for modes deep in the super-Hubble regime.

**Extrapolation to matter bounce:** For modes with k << k_bounce (which is all observable modes), the bounce corrections to f_NL should scale as (k/k_bounce)^n with n > 0. Since k/k_bounce ~ 10^-56, the corrections are negligibly small. This suggests **f_NL is preserved through the bounce**.

### Calculation B: Explicit LQC Dressed-Metric r Calculation for w = -0.003

**What:** Verify r ~ 10^-4 for the quasi-dust case using the dressed-metric equations.

**Why it matters:** The r ~ 10^-4 estimate is from Wilson-Ewing (2013). It would be valuable to reproduce this with the exact w = -0.003 case.

**Difficulty:** MEDIUM. The calculation requires solving the dressed-metric Mukhanov-Sasaki equation through the LQC bounce for both scalar and tensor modes.

**Value:** LOWER than Calculation A. Even if r changes by a factor of a few, it remains untestable. The exact value of r doesn't matter for the discriminator program.

### Calculation C: f_NL Consistency Check via Independent Method

**What:** Rederive f_NL = -35/8 using the delta-N formalism (correctly, unlike the faulty earlier attempt) or the in-in formalism for the matter bounce.

**Why it matters:** The -35/8 result comes from one paper (Cai et al. 2009). An independent derivation confirms robustness.

**Difficulty:** MEDIUM. The delta-N formalism in the matter bounce requires careful treatment of the growing mode. The key subtlety: in matter contraction, zeta grows on superhorizon scales (unlike inflation where it's constant). The standard delta-N formula N_phi * delta_phi gives the WRONG answer because it assumes constancy of zeta on superhorizon scales.

**The correct approach:** Use the gradient expansion to second order (Salopek-Bond formalism) in the contracting FRW background, keeping track of the growing mode. This should reproduce -35/8.

### Calculation D: Post-Bounce f_NL Including Quintin Enhancement

**What:** Quintin et al. (2015) showed that if the bounce amplifies scalars to suppress r, |f_NL| gets enhanced. Compute the enhancement factor for the LQC dressed-metric bounce.

**Why it matters:** If the enhancement is significant, the prediction shifts from -4.375 to something more negative (e.g., -6 or -10). This would make the model MORE testable but potentially also more constrained by current Planck bounds.

**Difficulty:** HIGH. Requires combining the Quintin scaling relations with the LQC dressed-metric transfer matrix.

**Risk:** If the enhancement pushes |f_NL| > ~10, the model may already be in tension with Planck (f_NL = -0.9 +/- 5.1, so |f_NL| > 10.3 is excluded at 2 sigma).

---

## Selection: THE ONE BEST NEXT CALCULATION

### **Calculation C: Independent derivation of f_NL = -35/8 via gradient expansion**

**Why this one:**

1. **Highest value:** The entire bounce program stands or falls on f_NL = -35/8. Confirming this with an independent method is the single most important verification.

2. **Addresses the root error:** The earlier 5/12 result came from a faulty delta-N calculation. Getting the delta-N or gradient-expansion calculation RIGHT establishes whether the nonlinear superhorizon growth genuinely produces -35/8 or something else.

3. **Achievable:** This is a paper-and-pencil calculation. It does not require numerical LQC codes or new formalism. The gradient expansion in FRW is well-understood.

4. **Clarifies the Quintin enhancement:** By tracking the second-order perturbation through the contracting phase, we can assess whether the -35/8 is the pre-bounce value (which may get enhanced) or the final observable value.

5. **Novel contribution:** If the independent calculation CONFIRMS -35/8 AND explicitly shows why the naive delta-N gives 5/12 (i.e., identifies the error mode), this is a useful technical result that clarifies a point of confusion in the bounce literature.

**Specific steps:**

1. Write the FRW equations for matter contraction: a(tau) proportional to tau^2 (conformal time), H = 2/(3t)
2. Expand the scalar field perturbation to second order: phi = phi_0 + delta_phi + (1/2) delta_phi^(2)
3. Compute zeta to second order using the gradient expansion (Salopek-Bond)
4. Identify the growing mode contribution to zeta^(2) / (zeta^(1))^2 in the superhorizon limit
5. Extract f_NL = (5/6) * zeta^(2) / (zeta^(1))^2 in the local (squeezed) limit
6. Compare to -35/8

**Expected outcome:** Either confirms -35/8 (strengthening the entire program) or reveals a correction (which would need investigation).

---

## What This Calculation Does NOT Do

- It does NOT address the bounce transfer (that's Calculation A, deferred)
- It does NOT verify r (that's Calculation B, lower priority)
- It does NOT compute the Quintin enhancement (that's Calculation D, deferred)

These are left for later because they all depend on the base f_NL value being correct. If the base value turns out to be different from -35/8, all downstream calculations change.

**Verify the foundation first. Then build on it.**

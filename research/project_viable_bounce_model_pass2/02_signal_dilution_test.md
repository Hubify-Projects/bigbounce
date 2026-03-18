# 02: Signal Dilution Test

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Purpose

Test whether the viability fixes applied to bounce models dilute or destroy the key bounce discriminators.

---

## Model B: Wilson-Ewing Quasi-Dust + LQC (The Only Surviving Candidate)

This model achieves viability through:
1. LQC quantum-geometry corrections (suppress r)
2. Slightly negative EOS w = -0.003 (provide red tilt)
3. Lambda contribution to the effective EOS

**Test: What price does each fix extract?**

### Fix 1: LQC Perturbation Corrections

**What it provides:** r ~ 10^-4 (suppressed below observational reach)

**Signal dilution:**
- r becomes untestable — this REMOVES a potential discriminator rather than providing one
- The blue tensor tilt (n_T > 0), which is a generic bounce signature, becomes unmeasurable because the tensor amplitude is too small
- Net effect: r and n_T are lost as discriminators

**Price paid:** The tensor sector is silenced. The inflationary consistency relation (n_T = -r/8) becomes untestable because r itself is untestable.

### Fix 2: Slightly Negative EOS (w = -0.003)

**What it provides:** n_s = 1 - 12*epsilon = 0.964

**Signal dilution:**
- The red tilt is now a one-parameter fit (epsilon determines n_s), comparable to inflation where V'/V determines n_s
- The value epsilon = 0.003 is NOT predicted from first principles — it comes from the ratio of Lambda to matter density at some reference time during contraction
- n_s = 0.964 matches Planck, but so does Starobinsky (n_s = 1 - 2/N = 0.964 for N = 55)

**Price paid:** The spectral tilt becomes a tuned parameter rather than a prediction. The same n_s can be obtained more economically from Starobinsky inflation.

**Does n_s retain any bounce imprint?** Yes — the formula n_s = 1 - 12*epsilon is different from the inflationary formula n_s = 1 - 6*epsilon_V + 2*eta_V. However, BOTH formulas give n_s as a function of one free parameter, and both can match 0.964. The functional form difference is not observationally testable given current precision.

### Fix 3: Lambda (Cosmological Constant)

**What it provides:** Physical motivation for w < 0

**Signal dilution:**
- Lambda is already part of LCDM, so this is not really a new ingredient
- But it ties the bounce model to a specific cosmological history: the contracting phase must include Lambda domination at some point
- This may create tensions with the contraction dynamics (when does Lambda dominate? does it prevent contraction from starting?)

**Price paid:** The model becomes an LCDM-bounce, not a pure matter bounce. The relationship between Lambda and epsilon = 0.003 needs to be derived, not assumed.

---

## The Critical f_NL Question

### If f_NL = -35/8 = -4.375 (Planck-convention, negative)

**Signal dilution test:**
- f_NL is set by the matter contraction dynamics ALONE
- No extra ingredient modifies it (unlike Model A where the curvaton diluted f_NL to -3.7)
- The value is FIXED — it does not depend on epsilon, Lambda, or any other parameter
- This is a genuine parameter-free prediction

**Dilution assessment:** ZERO dilution. The f_NL prediction is untouched by the viability fixes. This is because:
- LQC corrections affect r (tensor-to-scalar amplitude ratio) but NOT f_NL (scalar self-interaction)
- The EOS epsilon affects the tilt but NOT the nonlinear transfer function
- Lambda affects the background but superhorizon nonlinear evolution is determined by the local matter dynamics

**This is the ideal situation: the fixes preserve the discriminator.**

### If f_NL = +5/12 = +0.42 (zeta-convention, positive and small)

**Signal dilution test:**
- f_NL ~ 0.42 is indistinguishable from single-field inflation (f_NL ~ O(n_s - 1) ~ -0.04)
- Even MegaMapper (sigma ~ 0.5) would only see this at 0.8 sigma — not a detection
- The model has NO sharp discriminator left

**Dilution assessment:** The f_NL was never large enough to be a discriminator. The model simply has no smoking gun.

---

## Observable-by-Observable Survival Check

| Observable | Survives fixes? | Still bounce-distinctive? | Testable? |
|-----------|----------------|--------------------------|----------|
| n_s = 0.964 | Yes | No — same as Starobinsky | Yes, but not discriminating |
| r ~ 10^-4 | Yes | Yes (blue n_T would be distinctive) | **No** — too small |
| f_NL = -4.375 | Yes (if this is correct) | **YES** — negative, large, parameter-free | **YES** — MegaMapper 8.75 sigma |
| f_NL = +0.42 | Yes (if this is correct) | No — too small | No |
| alpha_s > 0 | Yes (positive running is bounce-specific) | Moderately — inflation can give either sign | Marginally — CMB-S4 sigma ~ 0.003 |
| Low-k cutoff | Unclear — needs calculation | Yes if present | Marginally — cosmic variance limited |

---

## The Verdict

### If f_NL = -4.375:

"The model survives observationally only by paying the price of **losing the tensor sector as a discriminator** (r too small) and **accepting n_s as a fitted parameter rather than a prediction**. However, the f_NL prediction is PRESERVED intact — parameter-free, large, negative, and testable. The price is acceptable because one sharp discriminator remains."

### If f_NL = +0.42:

"The model survives observationally only by paying the price of **every testable discriminator**. The tensor sector is silenced, n_s is fitted, and f_NL is too small to detect. The model is observationally indistinguishable from inflation with current or next-generation data. The bounce has become pure background."

---

## Additional Test: Does Positive Running (alpha_s > 0) Help?

Lehners & Wilson-Ewing (2015, arXiv:1507.08112) showed the matter bounce predicts POSITIVE running (alpha_s > 0), while standard slow-roll inflation predicts alpha_s < 0 (Starobinsky: alpha_s ~ -2/N^2 ~ -0.0007).

The matter bounce running is:
alpha_s = (n_s - 1)^2 / 12 ~ (0.036)^2 / 12 ~ 10^-4

This is VERY small and positive. Current Planck constraint: alpha_s = -0.005 +/- 0.007. CMB-S4 target: sigma(alpha_s) ~ 0.003.

**At sigma = 0.003, a value of alpha_s = +10^-4 is undetectable (0.03 sigma from zero).**

**Running does not rescue the model.** The predicted alpha_s is too small to measure, and even the sign difference from inflation is unresolvable.

---

## Bottom Line

**Everything depends on the f_NL convention.**

The f_NL = -35/8 calculation from Cai et al. (2009) is the make-or-break result. If it represents the Planck-observable f_NL^local, Model B has a genuine, undiluted, parameter-free discriminator. If it doesn't, the model has nothing left.

**The single most valuable calculation in this entire research program is resolving the f_NL convention issue for the matter bounce.**

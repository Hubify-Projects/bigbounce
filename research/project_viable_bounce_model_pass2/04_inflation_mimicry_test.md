# 04: Inflation Mimicry Test

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Question

Can an inflationary model with comparable complexity reproduce the same observables as Model B (LCDM Quasi-Dust Bounce)?

---

## Model B Predictions (Summary)

| Observable | Bounce Prediction |
|-----------|------------------|
| n_s | 0.964 (from epsilon = 0.003) |
| r | ~10^-4 |
| f_NL^local | -4.375 (if Bardeen convention) OR +0.42 (if zeta convention) |
| alpha_s | ~+10^-4 (positive, very small) |
| n_T | >0 (blue tensor tilt) |
| Low-k cutoff | Possible (depends on bounce scale) |

---

## Observable-by-Observable Mimicry Assessment

### n_s = 0.964

**Inflation can copy this:** TRIVIALLY

Starobinsky R^2 gives n_s = 1 - 2/N = 0.964 for N = 55. Hundreds of other potentials give n_s = 0.964 with appropriate parameter choices. The spectral index is the single most commonly fitted parameter in inflation model-building.

**Mimicry difficulty:** ZERO. Every inflation model worth considering matches n_s = 0.964.

### r ~ 10^-4

**Inflation can copy this:** EASILY

Many small-field inflation models (hilltop, natural inflation with large f, aligned natural inflation) predict r ~ 10^-4 to 10^-3. Even Starobinsky gives r = 0.004, which is small though 40x larger.

Specifically:
- Hilltop quartic inflation: r ~ 10^-4 for appropriate initial conditions
- Kahler moduli inflation: r ~ 10^-10 (even smaller)
- Fiber inflation: r ~ 10^-7

**Mimicry difficulty:** ZERO. Small r is generic in small-field inflation.

### f_NL^local = -4.375 (if correct)

**Inflation can copy this:** VERY DIFFICULT

Single-field slow-roll inflation predicts f_NL = (5/12)(1 - n_s) ~ 0.015. This is 300x smaller than -4.375 and the WRONG SIGN.

Multi-field inflation with curvaton: f_NL = 5/(4r_dec) - 5r_dec/6 - 5/3. For f_NL = -4.375: need r_dec satisfying 5/(4r_dec) - 5r_dec/6 - 5/3 = -4.375. This gives r_dec close to 1, with f_NL ~ -1.25 (minimum). **Cannot reach -4.375 with standard curvaton.**

To get f_NL = -4.375 in inflation requires:
- Self-interacting curvaton with lambda < 0 (unstable potential) — contrived
- A specific non-standard inflationary mechanism — e.g., DBI inflation (but this gives equilateral, not local)
- Multi-field with non-trivial field-space geometry — possible but requires engineering

**Key point:** Negative local f_NL of O(1) magnitude is UNNATURAL in inflation. Standard inflation gives f_NL ~ 0 (single-field) or f_NL > 0 (curvaton with r_dec < 0.9). Getting f_NL = -4.375 requires exotic constructions.

**Mimicry difficulty:** HIGH. This is the bounce's only hard-to-mimic signature.

### f_NL^local = +0.42 (if this is the correct value)

**Inflation can copy this:** TRIVIALLY

Single-field inflation predicts f_NL = O(0.01). The difference between +0.42 and +0.01 is undetectable with any planned experiment (MegaMapper sigma ~ 0.5 would see 0.42 at 0.8 sigma).

**Mimicry difficulty:** ZERO. Completely indistinguishable.

### alpha_s = +10^-4 (positive running)

**Inflation can copy this:** EASILY

While standard slow-roll gives alpha_s < 0, many inflationary models can produce positive running:
- Multi-field inflation with features
- DBI inflation
- String inflation models with moduli

And the predicted |alpha_s| ~ 10^-4 is FAR below the detection threshold (sigma ~ 0.003). So the sign difference is moot.

**Mimicry difficulty:** ZERO (undetectable).

### n_T > 0 (blue tensor tilt)

**Inflation can copy this:** WITH DIFFICULTY

The inflationary consistency relation n_T = -r/8 gives n_T < 0 (red). A blue tensor tilt CANNOT be produced in standard single-field inflation.

However:
- n_T is unmeasurable when r ~ 10^-4 (need to detect tensors first to measure their tilt)
- Some non-standard inflation models (gauge field inflation, axion inflation with gauge field coupling) can produce blue n_T

**Mimicry difficulty:** HIGH in principle, but IRRELEVANT in practice (unmeasurable at r ~ 10^-4).

### Low-k cutoff / large-angle suppression

**Inflation can copy this:** WITH SOME DIFFICULTY

If the bounce produces a low-k cutoff (suppression of power at k < k_bounce for some characteristic scale), this would show up as large-angle suppression in the CMB. Some inflation models can produce this (e.g., fast-roll initial conditions, compact topology), but it's not generic.

However:
- Whether the bounce actually produces a detectable low-k cutoff is model-dependent
- For the LCDM bounce, the bounce scale is near Planck scale — the cutoff would be at k ~ 10^-60 Mpc^-1, far below the observable window
- The existing CMB large-angle anomalies (low quadrupole, etc.) are at ~2-3 sigma and may be statistical flukes

**Mimicry difficulty:** MODERATE in principle, but the bounce may not produce a detectable cutoff either.

---

## Summary: Mimicry Scorecard

| Observable | Inflation mimicry | Notes |
|-----------|------------------|-------|
| n_s = 0.964 | **EASY** | Trivially matched by Starobinsky |
| r ~ 10^-4 | **EASY** | Small-field inflation |
| f_NL = -4.375 | **HARD** | Negative O(1) f_NL is unnatural in inflation |
| f_NL = +0.42 | **EASY** | Indistinguishable from f_NL = 0 |
| alpha_s = +10^-4 | **EASY** | Undetectable |
| n_T > 0 | **HARD** | Violates consistency relation, but unmeasurable |
| Low-k cutoff | **MODERATE** | Model-dependent in both bounce and inflation |

---

## The Hard-to-Mimic Signatures

**There are exactly two:**

1. **f_NL = -4.375** (if this is the correct Planck-convention prediction)
   - Testable: YES (MegaMapper, ~2035)
   - Unnatural in inflation: YES
   - Parameter-free in the bounce: YES (IF correct convention)

2. **Blue tensor tilt (n_T > 0)**
   - Testable: NO (r too small)
   - Unnatural in inflation: YES
   - But ACADEMIC unless tensors are detected

---

## The Honest Assessment

**If f_NL = -4.375 is the correct Planck-observable prediction:**

The bounce model has ONE genuinely hard-to-mimic signature. This is enough to make the model scientifically competitive — a single sharp discriminator is more valuable than many weak ones. The program reduces to: measure f_NL with MegaMapper. If negative at O(1) magnitude, bounce cosmology gains strong support that inflation cannot easily explain.

**If f_NL = +0.42:**

The bounce model has ZERO hard-to-mimic signatures among testable observables. Everything the bounce predicts, inflation can reproduce with equal or less effort. The model becomes observationally superfluous — not wrong, but unnecessary. The theoretical virtues (singularity resolution, no trans-Planckian problem) remain, but they are philosophical, not empirical.

---

## What Inflation CANNOT Copy (Theoretical, Not Observational)

For completeness:
1. Singularity resolution — inflation does not address this
2. Trans-Planckian absence — inflation requires trans-Planckian mode stretching
3. Initial conditions — debatable (both have issues)

These are real theoretical advantages of the bounce, but they are not TESTABLE advantages. Science requires testable predictions. Without f_NL = -4.375, the bounce has no testable advantage over inflation.

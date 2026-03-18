# Final Verdict: Second-Pass Viability Filter

**Created:** 2026-03-17
**Status:** COMPLETE

---

## 1. Did the first-pass viable model remain scientifically distinctive after second-pass filtering?

**YES — but only ONE model survived, and only because of ONE observable.**

Three models entered the second pass:
- **Model A (LQC + Curvaton):** DEAD. Curvaton tilt is blue in matter contraction, cannot fix n_s.
- **Model B (Wilson-Ewing LCDM Quasi-Dust Bounce):** SURVIVED. f_NL = -4.375 is a genuine parameter-free discriminator.
- **Model C (ILS Ekpyrotic):** FAILED DISTINCTIVENESS. The bounce does zero predictive work — all observables set by the two-field ekpyrotic sector and conversion dynamics. This is a multifield contraction model disguised as a bounce.

**The surviving model (B) is distinctive because:**
- All observables are controlled by bounce physics (not by added extra fields)
- The key prediction f_NL = -35/8 = -4.375 is parameter-free
- The only added ingredient beyond the minimal matter bounce is Lambda (already in LCDM)
- n_s = 0.964 comes from w = -0.003, which Lambda provides naturally

---

## 2. Is the bounce still doing predictive work, or only serving as a non-singular regulator?

**The bounce is doing genuine predictive work in Model B.**

Specifically:
- The LQC quantum bounce suppresses r to ~10^-4 (perturbation-level prediction from quantum geometry)
- The matter contraction dynamics produce f_NL = -4.375 (nonlinear superhorizon growth, specific to w = 0 contraction)
- The quasi-dust EOS with Lambda sets n_s = 0.964

The bounce is NOT merely a "non-singular connector" as it is in Model C. The LQC corrections actively shape the observable predictions.

However, there is a nuance: the f_NL is set by the CONTRACTING phase, not by the bounce itself. The bounce's role in f_NL is to faithfully transmit the pre-bounce bispectrum to the post-bounce universe without washing it out. This transmission is expected to be faithful for superhorizon modes (k/k_bounce ~ 10^-56), but has not been explicitly verified at third order in perturbation theory.

---

## 3. What is the biggest source of signal dilution?

**The LQC tensor suppression silences the entire tensor sector.**

By suppressing r to ~10^-4 (below all planned detector thresholds), the LQC bounce eliminates:
- r as a discriminator
- n_T (blue tensor tilt) as a discriminator
- The inflationary consistency relation test

This is the price of viability: the bounce needs LQC corrections to survive the r < 0.036 bound, but those same corrections push r so far down that it becomes unobservable.

**Net effect:** The model loses the tensor sector entirely and must rely exclusively on f_NL.

A secondary dilution: n_s becomes a fitted parameter (from epsilon = 0.003) rather than a prediction. Starobinsky inflation predicts n_s = 0.964 from N without fitting. The bounce model fits n_s from epsilon.

---

## 4. What is the best surviving hard-to-mimic observable?

**f_NL^local = -35/8 = -4.375**

Properties that make it hard to mimic:
1. **Negative sign:** Inflation generically gives f_NL >= 0 for local type (single-field: ~0; curvaton: +0.42 to +inf)
2. **O(1) magnitude:** Not slow-roll suppressed, not enhanced to exclusion — in the sweet spot
3. **Parameter-free:** The value -35/8 follows from w = 0 contraction dynamics alone. No tuning.
4. **Testable:** MegaMapper sigma(f_NL) ~ 0.5 gives 8.75 sigma detection

**No inflationary model naturally produces f_NL^local = -4.375.** To achieve this, inflation would need:
- A curvaton with r_dec > 1 (unphysical) OR
- A self-interacting curvaton with lambda < 0 (unstable potential) OR
- A contrived multi-field construction specifically engineered to produce negative f_NL

The matter bounce produces this value with ZERO additional ingredients. This asymmetry — natural for bounce, unnatural for inflation — is what makes it a genuine discriminator.

---

## 5. Is the program still on a path toward a genuinely competitive bounce cosmology, or drifting into generic multifield phenomenology?

**Model B is NOT drifting into generic multifield phenomenology.**

Model B has:
- 0 extra fields (dust + Lambda, both in LCDM)
- 1 extra parameter beyond minimal cosmology (epsilon = 0.003)
- 1 mechanism beyond standard GR (LQC quantum bounce)

This is SIMPLER than most inflationary models. The only model simpler is Starobinsky R^2, which has 1 parameter and 1 mechanism.

**The program is on a credible path IF f_NL = -4.375 is robust.** The model is:
- Observationally viable (all constraints satisfied)
- Predictively sharp (one parameter-free discriminator)
- Theoretically economical (no extra fields, minimal parameters)
- Testable on a concrete timeline (MegaMapper ~2032-2035)

**The danger:** If the f_NL prediction fails verification (either through a calculation error in Cai et al., or through LQC bounce enhancement pushing |f_NL| > 10 into Planck-excluded territory), the model has NO fallback discriminator. It would become observationally indistinguishable from inflation. This is a single-point-of-failure architecture.

---

## 6. What exact next calculation should be done immediately?

**Independent derivation of f_NL = -35/8 via the gradient expansion method (Salopek-Bond formalism) in matter contraction.**

### Why this specific calculation:

1. The ENTIRE program depends on f_NL = -35/8 being correct
2. The value comes from a single paper (Cai et al. 2009)
3. An earlier attempt in our own analysis (branch_V files) got the WRONG answer (5/12) due to a faulty delta-N approach
4. The correct calculation requires tracking the GROWING mode of zeta on superhorizon scales, which the standard delta-N formalism does not handle (delta-N assumes constant zeta)

### The calculation:

1. Matter contraction background: a(t) = a_0 (-t/t_0)^{2/3}, H = 2/(3t), phi_0(t) = sqrt(2/(3)) M_Pl ln(-t/t_0)

2. First-order perturbation: solve the Mukhanov-Sasaki equation for v_k in the superhorizon limit. Identify the growing mode zeta^(1) proportional to (-t)^{-1} (or equivalently a^{-3/2}).

3. Second-order perturbation: expand the Einstein equations to second order. Source term for zeta^(2) is quadratic in zeta^(1). Solve in the superhorizon limit.

4. Extract f_NL = (5/6) * [zeta^(2) / (zeta^(1))^2] in the squeezed limit (k3 << k1 ~ k2).

5. Compare to -35/8.

### Expected outcome:

- Confirms -35/8 -> program continues with high confidence
- Gets a different value -> recalibrate all predictions and detection forecasts
- Reveals that the growing mode enhancement IS the -35/8 and is robust to small EOS changes -> strongest possible foundation

### What comes after (if confirmed):

1. Estimate the Quintin enhancement through the LQC bounce
2. Verify that |f_NL| remains within Planck bounds post-bounce
3. Compute the exact r in the dressed-metric approach for w = -0.003
4. Write up the complete observable prediction set: {n_s = 0.964, r ~ 10^-4, f_NL = -4.375, alpha_s > 0}

---

## Summary Scorecard

| Question | Answer |
|----------|--------|
| Distinctive after pass 2? | YES (Model B only) |
| Bounce doing predictive work? | YES (LQC corrections + contraction dynamics) |
| Biggest signal dilution? | Tensor sector silenced by LQC (r too small) |
| Best surviving discriminator? | f_NL = -35/8 = -4.375 (parameter-free, negative, testable) |
| Drifting into generic phenomenology? | NO (Model B is minimal — 0 extra fields, 1 parameter) |
| Immediate next calculation? | Independent gradient-expansion derivation of f_NL = -35/8 |
| Risk? | Single-point-of-failure: if f_NL falls, model has no fallback |

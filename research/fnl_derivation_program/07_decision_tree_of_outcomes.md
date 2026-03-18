# 07: Decision Tree of Outcomes

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Derivation Will Produce One of These Outcomes

### Branch 1: f_NL^sq = -35/8 CONFIRMED

**Squeezed-limit amplitude is exactly -35/8 = -4.375 in Planck convention.**

Implications:
- Cai et al. (2009) is correct
- Li & Brandenberger discrepancy explained (approximation artifact at c_s = 1, or template projection vs squeezed limit)
- Quintin -35/16 is citation error (factor of 2 typo)
- Flagship claim: MegaMapper detects at ~8.75 sigma (before template projection)
- Template projection needed next: compute cos(theta) to get effective f_NL

**Next step after confirmation:** Template projection (file 06 method). If cos(theta) > 0.7, the flagship is secure. If cos(theta) < 0.5, the significance drops but detection may still occur.

**Status of paper 2:** GREEN — write the derivation into the paper, state the prediction with template projection caveat.

---

### Branch 2: f_NL^sq = -35/16 or -2.19

**Squeezed-limit amplitude is closer to -2.19 (Li-Brandenberger value).**

Sub-cases:

**2a: f_NL^sq = -35/16 = -2.1875 exactly**
- Cai et al. has a factor-of-2 error (likely in normalization)
- Li & Brandenberger is correct at c_s = 1
- Quintin citation was actually correct all along
- MegaMapper detection: 4.375 sigma (before template projection)
- Still detectable, but marginal after template projection

**2b: f_NL^sq = -2.19 but not exactly -35/16**
- Both Cai et al. AND Li & Brandenberger have approximation issues
- The exact value requires careful numerical evaluation
- MegaMapper detection: ~4.4 sigma (before template projection)

**Next step:** Template projection. If cos(theta) > 0.8, f_NL^eff ~ -1.7 to -1.9, giving MegaMapper ~3.4-3.8 sigma. Still significant. If cos(theta) < 0.5, marginal.

**Status of paper 2:** YELLOW — the prediction exists but is weaker. Must be careful about claiming "conclusive detection" vs "significant evidence."

---

### Branch 3: f_NL^sq is negative but different from both literature values

**Squeezed-limit amplitude is negative but not -35/8 or -2.19.**

Possible values: anything in the range [-10, -0.5].

Sub-cases:

**3a: |f_NL^sq| > 4 (more negative than Cai)**
- Cai et al. had an error that underestimated the amplitude
- This STRENGTHENS the flagship claim
- MegaMapper significance increases

**3b: -4.375 < f_NL^sq < -2.19 (between the two literature values)**
- Both calculations had partial errors
- MegaMapper significance: intermediate

**3c: |f_NL^sq| < 1 (small magnitude)**
- Both literature calculations had significant errors
- MegaMapper detection marginal or impossible
- Flagship claim is damaged but not killed (negative sign still discriminating)

**Next step:** Understand which approximation in the literature produced the error. Compute template projection. Reassess MegaMapper significance.

**Status of paper 2:** DEPENDS on exact value. GREEN if |f_NL| > 3, YELLOW if 1 < |f_NL| < 3, RED if |f_NL| < 1.

---

### Branch 4: f_NL^sq = 0

**The squeezed-limit bispectrum vanishes.**

This would mean:
- The matter bounce produces zero non-Gaussianity at the squeezed limit
- Both Cai et al. and Li & Brandenberger are wrong
- The growing mode does NOT generate a bispectrum (unexpected)

**This is EXTREMELY unlikely** given the physics: growing mode nonlinearity should generically produce O(epsilon) ~ O(1) non-Gaussianity. f_NL = 0 would require an exact cancellation between vertices.

**Next step:** Check for a symmetry or Ward identity that could force cancellation. If found, this is a major theoretical result worth publishing on its own.

**Status of paper 2:** RED — no discriminator survives.

---

### Branch 5: f_NL^sq is POSITIVE

**The squeezed-limit amplitude has the same sign as standard inflation.**

This would mean:
- The matter bounce does NOT produce the opposite-sign f_NL we expected
- The flagship "anti-correlation" discriminator is destroyed
- Standard inflation with f_NL ~ 0 and matter bounce with f_NL > 0 are harder to distinguish

**Consequences:**
- If f_NL > 0 but small (< 1): indistinguishable from inflation. FATAL.
- If f_NL > 0 and large (> 5): still distinguishable from inflation (inflation predicts |f_NL| << 1 for single field), but the sign advantage is lost.

**This is unlikely** given the literature (both calculations give negative values), but a sign error in the literature would be the most consequential finding.

**Next step:** Triple-check the sign. If positive is confirmed, the entire matter bounce f_NL program pivots.

**Status of paper 2:** RED if small positive, ORANGE if large positive.

---

### Branch 6: The calculation reveals that f_NL is NOT a pure number

**The squeezed-limit ratio B/(P*P) depends on k or on eta_f (time of evaluation).**

Sub-cases:

**6a: f_NL depends on eta_f (time dependence)**
- The growing mode introduces genuine time evolution of f_NL
- The prediction depends on WHEN the bounce happens (what value of a_bounce/a_exit)
- f_NL becomes a free parameter, not a prediction
- The "parameter-free" claim is destroyed

**6b: f_NL depends on k_1/k (running)**
- The bispectrum has running non-Gaussianity (n_fNL != 0)
- The squeezed limit is well-defined but the VALUE of f_NL depends on the scale ratio
- This is a new prediction, not a failure — running of f_NL is independently measurable

**6c: f_NL depends on the bounce details**
- The f_NL calculation is valid only PRE-bounce
- The bounce itself modifies f_NL (third-order transfer through the bounce)
- The prediction becomes bounce-model-dependent

**Next step for 6a:** Understand whether the time dependence cancels in the ratio (it should, by scale invariance of the power spectrum). If it doesn't cancel, there is an error in the mode function normalization.

**Next step for 6b:** Compute the running and check if it matches Cai et al.'s shape function.

**Next step for 6c:** This connects to the Quintin no-go (2015) — the bounce amplification of zeta simultaneously enhances f_NL. This may be a feature (larger |f_NL|) or a bug (model dependence).

**Status of paper 2:** YELLOW for 6b (new prediction), RED for 6a or 6c (loss of predictivity).

---

## Probability Assessment (Subjective, Pre-Derivation)

| Branch | Probability | Reasoning |
|--------|------------|-----------|
| 1: -35/8 confirmed | 35% | Cai et al. has been cited 200+ times uncorrected; direct calculation at c_s = 1 |
| 2: -2.19 confirmed | 25% | Li & Brandenberger is independent and more recent |
| 3: Different negative value | 20% | Both calculations may have approximation issues |
| 4: f_NL = 0 | 2% | Would require miraculous cancellation |
| 5: f_NL positive | 3% | Both independent calculations give negative |
| 6: Not a pure number | 15% | Growing mode physics makes this plausible |

---

## The Minimum Actionable Outcome

**Regardless of which branch we land on, the derivation resolves the current uncertainty.**

Currently: f_NL is "probably -35/8 but could be -2.19 or something else."

After derivation: f_NL is one specific value (or proven to be k/time-dependent), with the discrepancy explained.

**Even a negative result (Branch 4, 5, or 6c) is valuable** because it closes the flagship lane cleanly and redirects research toward a more productive avenue.

---

## Decision Rules

### If Branch 1:
- Proceed to template projection
- Write derivation into paper 2
- Compute MegaMapper forecast with template-projected f_NL^eff

### If Branch 2:
- Proceed to template projection
- Adjust MegaMapper forecast
- Investigate whether equilateral f_NL adds independent constraining power

### If Branch 3:
- Identify the error(s) in literature
- Proceed to template projection with corrected value
- Reassess viability based on exact number

### If Branch 4 or 5 (fatal):
- Document the calculation and the failure mode
- Assess whether bounce cosmology has ANY remaining discriminator
- If no discriminator: the entire program pivots to foundational theory

### If Branch 6:
- Determine whether the additional dependence is a prediction or a problem
- If prediction (6b): compute the running, add to paper
- If problem (6a, 6c): determine whether any bounce model avoids it

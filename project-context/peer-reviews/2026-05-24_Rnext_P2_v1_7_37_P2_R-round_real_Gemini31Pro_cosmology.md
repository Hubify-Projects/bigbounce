# P2 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-24_Rnext_P2_v1_7_37
**Wall time**: 101.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=33220, completion=12627, reasoning=11406, total=45847

---

## PAPER-GEM-B1: BLOCKER
**Section:** 9.4 (Discussion / Trispectrum)
**Concrete Issue:** The paper claims the matter bounce predicts the inequality $\tau_{\rm NL} \ge 27.56$ rather than saturation because its bispectrum is "not exactly local." This is theoretically false. The Suyama-Yamaguchi relation $\tau_{\rm NL} \ge (6\fnl/5)^2$ is an equality for *all* single-source models in the squeezed/collapsed limits, regardless of whether the non-Gaussianity shape is exactly local. The matter bounce is a single-field model and therefore strictly saturates the SY bound; conflating bispectrum shape mismatch with multi-source SY violation is a fundamental error.
**Fix:** Correct the text to state that the single-field matter bounce strictly saturates the Suyama-Yamaguchi equality $\tau_{\rm NL} = (36/25)\fnl^2$, and remove the claim that shape non-locality leads to an inequality.

## PAPER-GEM-B2: BLOCKER
**Section:** 9.4 (Discussion / Joint Fisher Forecast)
**Concrete Issue:** The paper quotes a $9.9\sigma$ detection significance based on a joint $(\fnl, n_{\fnl})$ Fisher matrix that yields an unmarginalized $\sigma(\fnl) \approx 0.114$ (admittedly $6\times$ tighter than published SPHEREx forecasts). This matrix is explicitly withheld ("deferred to a companion artifact"). Claiming a $9.9\sigma$ result based on an unvalidated, anomalously tight, and unpublished Fisher matrix violates basic scientific reproducibility and undermines the paper's credible $3-5\sigma$ baseline.
**Fix:** Remove the $9.9\sigma$ claim and the $\sigma(\fnl) \approx 0.114$ / $\sigma_{\rm marg} = 0.44$ numbers entirely until the Fisher matrix is published and validated against the integral constraint and sample variance limits.

## PAPER-GEM-M1: MAJOR
**Section:** 9.5 (Discussion / Cosmic Birefringence)
**Concrete Issue:** The text refers to "the prediction $\beta \approx 0.27^\circ$" from bounce-motivated physics. The matter bounce does not kinematically predict $\beta = 0.27^\circ$; this is the *observed* central value from Minami & Komatsu (2020). Claiming an observational fit of an auxiliary ALP field as a theoretical "prediction" of the bounce is a severe overreach.
**Fix:** Change "the prediction $\beta \approx 0.27^\circ$" to "the observed value $\beta \approx 0.27^\circ$", and clarify that bounce models can *accommodate* this via tuned ALP couplings, not predict it.

## PAPER-GEM-M2: MAJOR
**Section:** 6.3 (Bayesian Comparison / QSFI)
**Concrete Issue:** The paper claims that at the QSFI endpoint $\mu/H = 3/2$, "the bounce-vs-QSFI shape mismatch vanishes and the Bayes factor against the bounce hypothesis collapses to $\mathrm{BF} \to 1$." This is mathematically impossible. At $\mu/H = 3/2$, the QSFI shape becomes exactly local. The bounce shape is only 84% local ($r=0.84$). Therefore, the bounce and QSFI shapes remain distinct, the mismatch does *not* vanish, and the Bayes factor will not collapse to 1.
**Fix:** Correct the text to state that at $\mu/H = 3/2$, QSFI matches the *local* template, leaving a residual 16% shape mismatch against the bounce which preserves a finite Bayes factor.

## PAPER-GEM-m1: minor
**Section:** Abstract & Section 10 (Conclusion)
**Concrete Issue:** The paper contrasts the gauge-frame bounce prediction (-4.375) with the physical-frame inflation prediction ($\to 0$). However, the Conformal Fermi Coordinate (CFC) projection applies to *all* primordial signals. The bounce signal in the physical frame is not exactly -4.375, but $-4.375 + \mathcal{O}(n_s-1)$. Presenting the bounce prediction as immune to the CFC shift while applying it to inflation is theoretically inconsistent.
**Fix:** Add a brief clause acknowledging that the CFC projection also shifts the physical-frame bounce observable by $\mathcal{O}(n_s-1)$, though the contrast $|\fnl^{\rm bounce}| \gg |\fnl^{\rm inf}|$ remains robust.

## PAPER-GEM-m2: minor
**Section:** 7.2 (Systematics / PNG Bias Sensitivity)
**Concrete Issue:** The paper claims the bispectrum is "less sensitive to $b_\phi$ than SDB but not independent of it" because of cross-terms $\fnl b_\phi b_1^2 P(k_1) P(k_2)$. This misses the primary theoretical reason the bispectrum is robust: the primordial matter bispectrum term $B_m \propto \fnl P(k_1)P(k_2)$ does *not* depend on $b_\phi$ at all. The bispectrum has a direct tree-level primordial channel that SDB lacks.
**Fix:** Explicitly state that the bispectrum's robustness stems from the direct primordial matter bispectrum term which is entirely independent of $b_\phi$, diluting the relative impact of the $b_\phi$-dependent bias cross-terms.

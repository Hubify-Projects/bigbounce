# P4 R-round — DIRECT vendor — Grok-4 brutal-honesty reviewer

**Model**: `grok-4` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round4
**Wall time**: 20.9s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=89705, completion=917, total=91186, prompt_details={'text_tokens': 89705, 'audio_tokens': 0, 'image_tokens': 0, 'cached_tokens': 128}, completion_details={'reasoning_tokens': 564, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, num_sources_used=0, cost_in_usd_ticks=1156993500

---

**PAPER-GRO-B1**  
**Section:** Abstract (lines ~40-55) + Sec. 9 (Conclusions)  
**BLOCKER**  
The headline scientific claim is framed as a “-0.12σ subsample-mask ℓ=1 null” while the canonical-mask direct-MC residual is +3.64σ (empirical-rank p_MC=0.030). The paper dismisses the latter as “interpretation (ii) systematic” without a joint nuisance-marginalized model that simultaneously fits a primordial dipole + depth/PSF/morphology templates. This is the load-bearing tension; the null verdict is carried only by the larger-f_sky subsample mask that was chosen after seeing the canonical result.

**Fix:** State explicitly that the canonical-mask +3.64σ residual remains unexplained by the monopole-only leakage channel (which accounts for only ~12 % post-MASTER) and that the no-dipole conclusion is therefore conditional on the subsample-mask geometry.

**PAPER-GRO-B2**  
**Section:** Abstract + Sec. 1 (Introduction) + Sec. 9  
**BLOCKER**  
The paper repeatedly states that the result is “inconsistent in amplitude with Shamir (2020, 2022) by a factor of ~6–12” under the present pipeline, yet immediately adds the carve-out that no matched-footprint Ganalyzer reanalysis was performed. This is not a likelihood-level exclusion and should not be presented as such.

**Fix:** Replace the amplitude-comparison sentence with: “Under the present ViT/TTA pipeline the maximum regional asymmetry is 0.32 %; a matched Ganalyzer reanalysis on the identical footprint and selection is required for a formal exclusion under Shamir’s estimator.”

**PAPER-GRO-M1**  
**Section:** Sec. 9 (Conclusions) + Sec. 5.3 (Monopole+Mask Leakage)  
**MAJOR**  
The “quantifiable monopole-mask leakage channel” is presented as a central new result, yet it is the standard mode-coupling effect of a non-zero monopole through a patchy mask (Hivon et al. 2002). The 99.3 % pre-MASTER reproduction is expected once the global 9.5σ monopole is injected into the canonical geometry; it does not constitute a novel systematic discovery.

**Fix:** Move the leakage calculation to an appendix and state that it is a quantitative illustration of a known effect rather than a new channel.

**PAPER-GRO-M2**  
**Section:** Abstract + Sec. 5.1 (Declared Analysis Hierarchy)  
**MAJOR**  
The declared primary estimators are the real-space dipole (0.43σ) and the subsample-mask MASTER ℓ=1 (-0.12σ). The canonical-mask +3.64σ result is labeled “secondary diagnostic,” yet it is the only estimator that uses the exact footprint on which prior positive claims were made. This hierarchy was fixed after the first catalogue results (v1.0.76), violating the spirit of pre-specification.

**Fix:** Either promote the canonical-mask result to primary status with a full systematics model, or explicitly state that the headline null applies only to the strict-superset subsample mask.

**PAPER-GRO-m1**  
**Section:** Sec. 5.2 (Model Architecture) + Sec. 5.4 (TTA)  
**minor**  
The 21.4 % per-galaxy argmax flip rate under D4-TTA is reported but then declared “not a primary source of uncertainty” because the headline uses soft p_CW-weighted maps. This is correct for the dipole but leaves the HC-spiral injection-recovery floor (Table VII) carrying an unpropagated 21 % label-noise term.

**Fix:** Add a one-sentence propagation: the 0.75 % 50 %-recovery threshold is widened by ~1.21× when the 21.4 % flip rate is folded into the hard-label variance.

**PAPER-GRO-n1**  
**Section:** Abstract (first paragraph)  
**nit**  
The abstract still contains ~470 words of defensive framing (“we emphasize at the outset… prior literature has at times conflated…”) despite the explicit note that it was trimmed from 1839 words. The residual defensive tone is unnecessary for a null result.

**Fix:** Remove the three sentences that explain why the observable is parity-even; retain only the numerical result and scope statement.

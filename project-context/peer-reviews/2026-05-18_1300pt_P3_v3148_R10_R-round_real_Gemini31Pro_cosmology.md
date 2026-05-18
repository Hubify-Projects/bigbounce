# P3_v3148_R10 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1300pt
**Wall time**: 76.5s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=64346, completion=7243, reasoning=6340, total=71589

---

## PAPER-GEM-B1: Unphysical Fisher Bounds Retained in Load-Bearing Text
**Classification:** BLOCKER
**Section:** Abstract & Section 5
**Issue:** The abstract and Section 5 body text still quote the mathematically impossible linear-propagated Fisher bounds: $\sigfnl^{\rm GS} = 2.28 \pm 7.43$ (which implies a negative lower bound of $-5.15$) and the full-sample 95% interval $[3.62, 12.95]$ (which implies adding a distinct tracer degrades the constraint to worse than the single-tracer floor of $8.98$). Caveats (i) and (j) correctly derive the Fisher-positivity-respecting envelopes ($[0.94, 8.98]$ and $[2.4, 8.98]$), but the unphysical numbers were left in the headline text.
**Fix:** Replace the unphysical linear bounds in the abstract and Section 5 with the corrected asymmetric envelopes derived in caveats (i) and (j).

## PAPER-GEM-B2: OOD MSE Normalization Contradiction
**Classification:** BLOCKER
**Section:** 2.2
**Issue:** The text states the $S>5$ anomaly threshold corresponds to an absolute MSE of $\sim 0.143$, notes the 100k OOD sample has a median MSE of $0.178$, and then claims "the 0.87% DESI anomaly rate is preserved on this independent OOD sample." This is a mathematical contradiction: if the threshold (0.143) is below the median (0.178), the anomaly rate on the OOD sample must be $>50\%$, not 0.87%.
**Fix:** Reconcile the arithmetic; either the OOD median is $0.0178$, the threshold is evaluated on a different scale, or the model fails catastrophically on OOD data. Correct the "preserved rate" claim accordingly.

## PAPER-GEM-M1: Incomplete Fix of 5-Fold Jaccard Contradiction
**Classification:** MAJOR
**Section:** 2.2
**Issue:** The abstract was correctly updated to state that the 5-fold cross-validation scores the *full 47,000-spectrum pool* (resolving the deferral (g) mathematical impossibility of 399 intersection objects out of a 470 max union). However, Section 2.2 still states each fold "scores the held-out 20% (9,400 spectra)", leaving the contradiction intact in the main text.
**Fix:** Update Section 2.2 to match the abstract, explicitly stating the top-1% sets are drawn by scoring the full 47,000-spectrum pool.

## PAPER-GEM-m1: Ambiguous Multi-Tracer Bias Marginalization Claim
**Classification:** minor
**Section:** 5
**Issue:** The claim that "the linear-bias amplitude $\delta b$ is absorbed by the multi-tracer cross-correlations" oversimplifies the Fisher matrix behavior. While sample variance cancellation relies on the bias ratio, marginalizing over independent $\delta b_i$ for each tracer with broad priors degrades the $\fnl$ constraint unless a prior on the bias ratio is applied or cross-correlation perfectly breaks the degeneracy.
**Fix:** Specify whether the $4n+1$ Fisher matrix applies a prior to the individual $\delta b_i$ or to their ratio to achieve the reported $\sigfnl$ floor.

## PAPER-GEM-m2: Redundant Stratification Text
**Classification:** minor
**Section:** Abstract
**Issue:** The abstract contains a verbatim redundant repetition of the tier stratification. It states "stratified into two physically distinct tiers: 378,080 point-source... plus 200 Planck..." and immediately follows with "The catalog stratifies into the 378,080 point-source... plus the 200 Planck... summing to the 378,280 headline."
**Fix:** Delete the redundant second sentence.

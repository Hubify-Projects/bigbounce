# P4 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-phase2-verify_P4_v1_0_131
**Wall time**: 27.7s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=90458, completion=2288, reasoning=1374, total=92746

---

**PAPER-GRO-B1**  
**Classification:** BLOCKER  
**Section:** Title + Abstract (L1–3, abstract para 1)  
**Issue:** Title and opening abstract sentence frame the result as “No Evidence for Large-Scale Parity Violation”, yet the paper explicitly states the ℓ=1 dipole is parity-EVEN and “NOT a direct parity-violation test”. This is a direct mismatch between headline claim and stated observable.  
**Fix:** Retitle to “No Evidence for Large-Scale Isotropy Violation in the Projected Galaxy Chirality Dipole” and move the parity-EVEN clarification to the first sentence of the abstract.

**PAPER-GRO-B2**  
**Classification:** MAJOR  
**Section:** §\ref{sec:dipole_symmetry_caveat} + Table I footnote b + §\ref{sec:conclusions} (canonical +3.64σ verdict)  
**Issue:** The +3.64σ canonical-mask residual is attributed to “interpretation (ii) depth/morphology systematic” on the basis of a single-multipole cross-spectrum (ℓ=2, σ=−2.89), a non-monotonic quartile test, and a bootstrap that the paper itself shows is inconclusive for a 1.7 % dipole. Family-wise correction on the cross-spectrum drops it to ~2.3σ; the claim that systematics are “favoured” therefore exceeds the load-bearing evidence.  
**Fix:** Replace “favoured by direct cross-spectrum” with “consistent with a depth-correlated systematic at the present sensitivity; a sub-dominant primordial component is not excluded.”

**PAPER-GRO-B3**  
**Classification:** MAJOR  
**Section:** Abstract + §\ref{sec:shamir} + Table I (Shamir amplitude comparison)  
**Issue:** Despite added disclaimers, the abstract and introduction still quote a factor ~6–12 amplitude tension with Shamir (2020/2022). Because no matched-footprint Ganalyzer reanalysis was performed, this comparison is not a statistical exclusion and functions as narrative inflation.  
**Fix:** Remove the numerical factor and replace with: “Under the present ViT/TTA pipeline the maximum regional asymmetry is 0.32 %, a factor of several smaller than the ~2–4 % amplitudes reported by Shamir; a like-for-like reanalysis is required for a likelihood-level comparison.”

**PAPER-GRO-B4**  
**Classification:** MAJOR  
**Section:** §\ref{sec:prereg} + Table II (data-vector table) + Table I footnote b (MC counts)  
**Issue:** The new 7-row data-vector table is a clear improvement, but row (v) still lists N_MC=500 for the post-MASTER monopole-only null while the text (v1.0.131 update) reports the N=10 000 result. The headline p-value quoted for that null therefore mixes two different MC sizes without a single canonical number.  
**Fix:** Make row (v) and the accompanying footnote report only the N=10 000 values (p_MC=0.0023, 12 % leakage) and delete the legacy N=500 numbers.

**PAPER-GRO-B5**  
**Classification:** minor  
**Section:** §\ref{sec:sensitivity} (Fisher vs empirical floor)  
**Issue:** The text repeatedly cites the statistical Fisher floor (~0.29 % full amplitude) alongside the empirical 50 %-recovery threshold (0.75 %), creating the impression that the pipeline reaches the Fisher limit. The two numbers apply to different samples and different nulls; the gap is not a degradation factor for the same estimator.  
**Fix:** State once, in one paragraph, that the statistical floor is 0.29 % (ideal) while the empirical per-pixel-shuffle threshold on the HC subsample is 0.75 %; do not juxtapose them as a single sensitivity claim.

**PAPER-GRO-B6**  
**Classification:** nit  
**Section:** Throughout (multiple “unprecedented”, “largest”, “first” phrases)  
**Issue:** Phrases such as “the largest survey-scale chirality catalog to date” and “most sensitive chirality measurement ever performed” appear without a quantitative literature survey of comparable audit suites or sample-size normalisations.  
**Fix:** Replace with neutral size statements (“3.2 M equivariant spirals, 1.6× larger than the CE-ResNet spiral sample”) and remove all superlatives.

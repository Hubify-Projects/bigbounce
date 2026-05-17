# P1B_v1B08 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0930pt_P1B_v1B08_R4_R-round_real
**Wall time**: 49.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=13692, completion=5549, reasoning=4692, total=19241

---

## PAPER-GEM-B1: Stale DESI DR2 Chain Status in Section 7.1 (Propagation Failure)
**Classification:** BLOCKER
**Section:** 7.1 (Cross-paper shadow), paragraph (ii)
**Issue:** The DESI DR2 chain status was successfully bumped to 101,979 samples / $\hat{R}-1 = 0.01176$ (as of 2026-05-17) in Table 4 and the Conclusions, but Section 7.1 was missed. It still explicitly quotes the stale v1B.0.7 snapshot: "As of 2026-05-14 22:53 UTC the chain has accumulated 59,832 accepted samples... and reports $\hat R - 1 = 0.01945$".
**Fix:** Update Section 7.1 paragraph (ii) to match the live 101,979 / 0.01176 state to restore internal consistency.

## PAPER-GEM-M1: Versioning Paradox on Deferred Model-Comparison Recompute
**Classification:** MAJOR
**Section:** 5.2 & Appendix B (Table 7)
**Issue:** Section 5.2 states that the model-comparison recomputation "is on-record-deferred to v1B.0.8," and Appendix B lists it as "recompute v1B.0.8". However, the current document *is* v1B.0.8. Deferring an action to the current version number without executing it creates a versioning paradox.
**Fix:** Either execute the recomputation in this draft, or bump the deferral target text to v1B.0.9 in both Section 5.2 and Appendix B.

## PAPER-GEM-M2: Dangling Savage-Dickey Reference in Appendix A
**Classification:** MAJOR
**Section:** Appendix A
**Issue:** Appendix A states, "Bayes factors are estimated via Savage-Dickey from MCMC posteriors... (Sec. 5)". This is a dangling reference to the zombie stats that were successfully purged from Section 5.2 in the v1B.0.7 R3 closure. 
**Fix:** Remove the sentence claiming Bayes factors are estimated via Savage-Dickey from Appendix A, as this estimation is no longer present in the paper.

## PAPER-GEM-m1: Out-of-Sync Key Blocker in Cross-Paper Status Table
**Classification:** minor
**Section:** Table 3
**Issue:** Table 3 lists the P1(b) Key blocker as "Model-comparison recompute (deferred v1B.0.8)". As with PAPER-GEM-M1, this is out of sync with the document's own version number.
**Fix:** Update the deferred version in Table 3 to v1B.0.9, or mark it resolved if the recompute is added.

## PAPER-GEM-m2: Missing Likelihood Definition for ALP MCMC
**Classification:** minor
**Section:** 6 (MCMC parameter estimation)
**Issue:** The text states "Dedicated MCMC sampling of the ALP parameter space (3 configurations, 9,720 total accepted samples) yields..." but never defines the data vector or likelihood being sampled. Without stating what data the MCMC is fitting against, the posterior is a black box.
**Fix:** Add a half-sentence explicitly defining the likelihood (e.g., "using a Gaussian likelihood over the published Planck and ACT $\beta$ measurements").

## PAPER-GEM-n1: Awkward Phrasing in Appendix A
**Classification:** nit
**Section:** Appendix A
**Issue:** The phrase "biased for the correlated $\Delta\Neff$--$H_0$ posterior" uses non-standard prepositional framing.
**Fix:** Change "biased for" to "biased by" or "unreliable for".

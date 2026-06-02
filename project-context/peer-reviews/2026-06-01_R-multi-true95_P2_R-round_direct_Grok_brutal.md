# P2 R-round — DIRECT vendor — Grok-4 brutal-honesty reviewer

**Model**: `grok-4` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-true95
**Wall time**: 19.9s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=30356, completion=716, total=31802, prompt_details={'text_tokens': 30356, 'audio_tokens': 0, 'image_tokens': 0, 'cached_tokens': 128}, completion_details={'reasoning_tokens': 730, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, num_sources_used=0, cost_in_usd_ticks=414256000

---

**BLOCKER-1**  
Abstract + §4 (L79, L288)  
Headline significance 3–5σ (and 5.2–5.5σ optimistic) is computed from Heinrich et al. 2024 local-template Fisher matrix applied to a non-local shape without re-deriving the covariance or estimator bias for the bounce polynomial. The r=0.84 correction is only an amplitude rescaling; projection noise from the 3 % shape mismatch and the c1–c6 null-space scatter are not folded into the published Fisher matrix.  

Fix: Replace all headline σ values with the explicit statement “recovered amplitude significance after local-template projection; full bounce-template Fisher matrix required before claiming detection threshold.”

**BLOCKER-2**  
§5 + Table 2 (L293, L436)  
Bayes-factor grid (BF ∼10–17) rests on an analytic closed-form integral whose numerical values were repeatedly wrong in prior versions (6→4, 8→10, 12→14). The paper now cites scipy.stats.norm post-correction, but still presents the numbers as load-bearing model-selection evidence while the underlying prior widths remain arbitrary and the QSFI endpoint is acknowledged to give BF→1.  

Fix: Downgrade all BF statements to “illustrative sensitivity check under the stated priors; not robust model-selection evidence.”

**MAJOR-1**  
Abstract + §2.3 (L67, L419)  
“First time” quantification of template overlap is asserted after an internal literature search only. No external citation or arXiv scan is supplied, and the 10 000-sample null-space scan is performed in a symmetrized monomial basis chosen by the authors, not the original Cai derivation.  

Fix: Remove “for the first time”; replace with “we compute the overlap factor r under the following weighting schemes and coefficient sampling.”

**MAJOR-2**  
§2.3 + Appendix A (L450, A.1)  
The entire significance chain is convention-dependent: switching from c=2 to c=1 halves every quoted σ. The paper declares the Cai convention “correct” via an operator-algebra argument, yet simultaneously reports the halved numbers “for completeness.” This is an unresolved systematic that moves the result from >3σ to <3σ.  

Fix: State a single convention choice up front and propagate only that choice; move the alternative to a one-line sensitivity note.

**MAJOR-3**  
§3 + §6 (L254, L436)  
The 9.9σ joint (fnl, n_fnl) figure is an idealized Fisher self-consistency check whose six-bin inputs are explicitly “deferred to a companion artifact.” It is therefore not reproducible from the present manuscript and cannot be used to support any claim about scale-dependent bias.  

Fix: Delete the 9.9σ number and the associated paragraph until the companion Fisher inputs are public.

**minor-1**  
§2.1 (L216)  
The underdetermined c1–c6 system is presented as a source of 13 % scatter in r, yet the three benchmark configurations already fix the squeezed-limit amplitude exactly. The scatter therefore affects only intermediate triangles that carry low weight in realistic LSS noise; the quoted ±0.13 range overstates the impact on the headline observable.  

Fix: Report the interquartile range of r under LSS-weighted Fisher only, or drop the null-space scan from the abstract-level uncertainty budget.

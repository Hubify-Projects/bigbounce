# EXTDB2 P2 Grok — chat: https://grok.com/c/d7a34289-69e5-42ef-867f-b55a3e260340?rid=921b1959-9c8c-4ea7-8a55-136df6e4dbd3

Provider: Grok Expert
PDF md5: 1da0518fa79894dfd68bbed7f93efc75
Harvested: 2026-06-28

---

Referee Report: MNRAS / PRD / JCAP
Paper: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
Author: Houston Golden
Date: 27 June 2026

Recommendation: MINOR REVISIONS

BLOCKERS
None. The work is technically sound, contains no ethical or reproducibility red flags, and does not contain outright incorrect claims that would require rejection or major re-analysis. The core technical steps (template overlap, in-in normalization audit, null-space sampling, and closed-form Bayes-factor derivation) are internally consistent and well-documented.

MAJORS

1. Assumption (d) — faithful third-order bispectrum transmission through the bounce (Sec. II C)
This is correctly identified by the author as "the weakest link" and is supported only by a semi-analytic superhorizon scaling estimate giving δfNL~10^{-3}. However, the entire forecasting exercise and the claim that SPHEREx/MegaMapper can test the matter-bounce prediction rest on this assumption remaining valid at the ≲10% level. For a top-journal paper that headlines a concrete detection significance and Bayes-factor discrimination, the current treatment is insufficiently prominent.
Requested revision: Expand the discussion of assumption (d) (either in Sec. II C or a new short "Limitations and robustness" subsection). Explicitly address: (i) which classes of bounce UV completions or transition dynamics could violate faithful cubic transmission at the 5–20% level; (ii) the quantitative threshold at which a violation would invalidate the −35/8 benchmark; and (iii) whether a dedicated numerical check (e.g., LQC-mode-function evolution through the bounce inserted into the full Maldacena cubic integrals) is feasible or planned.

2. Systematics combination methodology and headline forecasting
The paper uses additive quadrature for the dominant systematics while correctly noting that this is a "transparent scoping choice" and that a full joint multi-tracer covariance has been computed only for the SDB channel. The headline realistic range ~2.6–5σ therefore mixes a rigorously validated piece (template mismatch + ε-correction) with a heuristic combination for the remainder.
Requested revision: Either (a) perform a joint Fisher or mock-based propagation of the main nuisances directly into the bispectrum Fisher matrix, or (b) relabel the realistic range more explicitly as "illustrative envelope under quadrature combination; a full joint-covariance forecast would be required for a definitive analysis."

MINORS

1. Headline phrasing — The abstract and early sections lead with the template-corrected optimistic range (5.2–5.5σ) before qualifying with the post-systematics envelope. The primary quoted forecast significance should be the realistic post-budget range, with the optimistic value presented strictly as an upper reference.

2. Scope of "recast" framing vs. original contributions — The paper repeatedly describes itself as a sensitivity recast of Heinrich et al. (2024). However, the actual scientific payload (null-space exploration, multi-scheme template-overlap calculation, symbolic in-in audit, joint running Fisher, and closed-form Bayes-factor grid) is substantially more than a simple rescaling. A short paragraph early in the introduction or Sec. IV clarifying the boundary between "imported baseline" and "original analysis performed here" would prevent misreading.

3. Propagation of template mismatch — degradation implemented via σ_eff = σ(fNL_local)/r. A one-sentence caveat noting that a fully optimal bounce-shaped estimator could recover r→1 (at the cost of losing direct comparability with existing local fNL constraints) would be useful.

4. Minor presentational points: (a) ensure every figure and table is explicitly referenced in the text; (b) a clarifying sentence in Sec. VI about marginalization over theoretical uncertainty in the bounce prediction; (c) promote the continuous hyperprior marginalization over σ_theory to a short paragraph with BF values.

Strengths

1. Template-overlap quantification is state-of-the-art: 10,000-sample null-space scan, five physically motivated Fisher weightings, 200-realization flat-sky injection-recovery test, and ℓ-space Fisher cross-check. r=0.84±0.02 (noise-weighted central value) convincing.

2. Normalization audit and in-in identity verification: explicit symbolic confirmation that the Cai et al. intermediate single-time-ordering result is exactly half the full commutator result via i⟨[ζ3,L]⟩=−2 Im⟨ζ3L⟩ resolves a long-standing factor-of-two discrepancy. High-quality technical work.

3. Transparent and self-critical treatment of theoretical assumptions: six assumptions (a)–(f) stated clearly, Wilson-Ewing quasi-dust model correctly distinguished from more general bounce constructions, assumption (d) flagged as weakest link with honest order-of-magnitude estimate.

4. Joint Fisher validation of the dominant degeneracy: explicit fNL–nfNL running Fisher (and b1–fNL co-marginalization) demonstrates that the running term, not b1–fNL, is the leading direction. Substantive methodological improvement.

5. Bayes-factor analysis with closed-form derivation and prior-sensitivity mapping: analytic expression (Eq. 9), three independent 10^5-realization Monte-Carlo validation ensembles, explicit four-corner grid, and transparent bookkeeping for the r-rebooking. All executed to a high standard.

Overall Assessment: A rigorous, technically deep, and unusually self-aware sensitivity recast. The original contributions are genuine and well-executed. The two major requests are focused and addressable without requiring new data or a complete re-forecast. Recommendation: MINOR REVISIONS.

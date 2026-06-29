# RBEXT P2 ChatGPT — chat: https://chatgpt.com/c/6a42bebb-7368-83e8-98dc-6ffed47fd51c
VERDICT: MAJOR REVISIONS

Provider: ChatGPT (default/Instant tier)
PDF: RBEXT_P2.pdf | md5: 291b9956a032c5a57e12896a128e7f40
Harvested: 2026-06-29

---

1. Recommendation: MAJOR REVISIONS

The paper is ambitious and substantially improved by extensive caveats, but it is not yet acceptable at a top-journal standard because the headline forecast still rests on a recast of an external local-template SPHEREx Fisher result, with several major degradations handled by heuristic quadrature rather than a matched joint covariance.

2. BLOCKERS

None requiring rejection, but one near-blocker: the abstract/headline "2.6–5.5σ" range is too easy to read as a forecasted measurement precision, while the text admits it is a sensitivity envelope, not a joint Fisher forecast. This must be softened everywhere in the abstract/conclusion.

3. MAJORS

- Headline significance is not an independent forecast. The core SPHEREx claim imports Heinrich et al. σ(fNL)=0.7 and applies template/systematic corrections. That is legitimate as a recast, but the title/abstract must consistently say "sensitivity recast," not imply a new SPHEREx forecast.
- Systematics combination is heuristic. GR projection, bϕ, photo-z degradation, template mismatch, and epsilon corrections are combined mostly by additive quadrature. The paper correctly discloses this, but the headline should not present the result as if it came from a joint marginalized bispectrum covariance.
- The bounce transmission assumption remains the weakest theoretical link. Cubic-order transfer through the bounce is assumed, supported only by scaling. Since the observable is a bispectrum, this is a central assumption, not a caveat.
- Template overlap treatment is underdeveloped for an LSS bispectrum estimator. The paper uses CMB-like/shape-space validation and noise-weighted overlap r≈0.84, but does not compute the actual SPHEREx 3D galaxy-bispectrum cross-Fisher against the bounce template. That limits the strength of the quoted degradation.
- Bayes factors are too prominent relative to prior sensitivity. The paper is transparent, but BF≈9–14 depends strongly on competitor prior width, bounce prior width, and bookkeeping. The abstract should call these illustrative prior-dependent diagnostics, not model-selection evidence.

4. MINORS

- Clarify every occurrence of "realistic" to "post-budget scoping envelope."
- Reduce repetition around Cai/Li factor-of-two; the appendix is useful but overlong.
- Keep MegaMapper framed as speculative throughout; avoid placing it visually beside SPHEREx as if equally concrete.
- The anomaly-tracer discussion feels tangential and should be shortened or moved to outlook.
- Make Table IV the canonical source for all significance numbers and remove redundant variants elsewhere.

5. Strengths

- Strong internal honesty: many caveats are explicitly stated rather than hidden.
- The Cai/Li normalization and time-ordering audit is valuable and likely publishable as a technical clarification.
- The template-mismatch issue is real and thoughtfully quantified.
- The paper makes a clear falsifiable connection between matter-bounce phenomenology and near-future PNG measurements.
- The distinction between bispectrum headline and SDB cross-check is mostly well handled.

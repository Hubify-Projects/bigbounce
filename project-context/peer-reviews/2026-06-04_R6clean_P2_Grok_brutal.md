# P2 2026-06-04_R6clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 10.9s

---

**Referee Report**

**Paper tag: P2**  
**Title:** Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook

**Findings**

**P2-E1 (ESSENTIAL)** — Abstract, p. 1  
The abstract states the SPHEREx multi-tracer bispectrum achieves \(\sigma(f_{NL}^{\rm local})\approx 0.7\), “giving template-corrected significance ∼3–5σ after the combined systematic budget … with 5.2–5.5σ as the optimistic case.” The body (Sec. IV, VII, and the explicit convention paragraph on p. 1) shows that adopting the Li–Brandenberger normalization halves every quoted significance (optimistic 2.6–2.75σ, post-systematic 1.5–2.5σ). The abstract therefore presents the higher numbers as the headline result while burying the factor-of-two convention dependence that the authors themselves flag as unresolved. Required fix: either adopt one convention as baseline throughout (with the alternative shown only as a sensitivity check) or rewrite the abstract to state the range under both conventions on equal footing.

**P2-E2 (ESSENTIAL)** — Abstract & Sec. VI, p. 1 and pp. 9–11  
The abstract claims “a detection near \(f_{NL}=-4.375\) favors the bounce over tuned multifield competitors at Bayes factor BF≈10 … up to BF≈17.” The body demonstrates that these numbers are obtained only for a delta-function bounce prior; the recommended physically motivated Gaussian prior \(\sigma_{\rm theory}=1.0\) yields BF≈10 (broad competitor) or BF≈4 (narrow competitor). The abstract therefore reports the theoretical-maximum values as the headline envelope. Required fix: state the recommended-prior result as the primary number and relegate the delta-prior maximum to a parenthetical upper bound.

**P2-E3 (ESSENTIAL)** — Abstract & Sec. IV, p. 1  
The abstract presents the 3–5σ (post-systematic) and 5.2–5.5σ (optimistic) figures as the paper’s headline forecast. Both numbers are derived from the Heinrich et al. (2024) Fisher matrix under the local template; the matter-bounce template mismatch \(r=0.84\pm0.02\) and the full systematic budget are applied afterward. The abstract does not make clear that the quoted significances are a sensitivity recast of an existing forecast rather than an independent calculation. Required fix: rephrase to “we recast the published Heinrich et al. forecast … obtaining … after template and systematic corrections.”

**P2-M1 (MAJOR)** — Overall length  
The manuscript is 22 pages. The scientific content is a template-overlap calculation, a prior-sensitivity scan, and a recast of two published Fisher matrices. No new survey design, no new estimator, and no new data are introduced. A concise Letter or short article of 10–12 pages would suffice; the present length is not justified by the incremental nature of the contribution.

**P2-M2 (MAJOR)** — Sec. V, p. 8–9  
MegaMapper is described as “proposed, not yet approved or funded.” The forecast range 3–7σ is nevertheless presented on equal footing with the SPHEREx numbers. The text must state explicitly that these projections are illustrative only and carry no weight as a near-term test.

**P2-M3 (MAJOR)** — Sec. II C & Appendix A, pp. 4–6 and 18–20  
The paper correctly identifies the factor-of-two discrepancy as partly a convention difference and partly the missing second time-ordering of the in-in commutator. However, it continues to quote both normalizations throughout the results sections. A single primary convention must be chosen; all numerical results must be reported in that convention, with the alternative shown only in one dedicated table or paragraph.

**P2-m1 (MINOR)** — Sec. II A, p. 3  
The claim that the six-coefficient null-space scan quantifies “for the first time” the template mismatch is not accompanied by a literature search demonstrating absence of prior work. Either remove “for the first time” or supply the search that justifies it.

**P2-m2 (MINOR)** — Sec. VI, p. 10  
The three Monte-Carlo ensembles (each \(10^5\) realizations) are presented as independent validation. They are in fact three different samplings of the same analytic Bayes-factor formula. The text should state that the ensembles serve only to confirm numerical stability of the closed-form expression.

**P2-n1 (NIT)** — Multiple sections  
Phrases such as “minimally parameterized,” “UV-completion independence within the scalar-only class,” and “mechanism-independent” appear repeatedly while the six assumptions (a)–(f) are listed only once. A single consolidated caveat paragraph early in the paper would reduce repetition.

**P2-n2 (NIT)** — Fig. 2 caption and surrounding text  
The error bars are described as “optimistic-to-conservative ranges accounting for multi-tracer, photo-z, bias, and GR systematics.” The figure itself does not show the separate contributions; the caption should list which systematics are included in each bar.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript performs a useful but incremental sensitivity analysis of an existing forecast. Its central results are (i) a template-overlap factor \(r\approx0.84\) and (ii) a demonstration that the quoted detection significance is highly sensitive to normalization convention and prior choice. Both points are scientifically sound once the presentation is corrected, but the current abstract and length overstate the robustness and novelty of the work. The required revisions are therefore substantial but not fatal: adopt a single primary convention, report the recommended-prior Bayes factor as the headline number, shorten the manuscript by roughly half, and clearly label the MegaMapper projections as speculative. With those changes the paper would be suitable for Physical Review D.
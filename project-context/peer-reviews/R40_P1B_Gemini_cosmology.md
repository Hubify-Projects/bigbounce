# P1B R40 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 127.6s

---

**Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program (Golden)**

This paper presents three technical verification analyses intended as a companion to a primary theory paper on Einstein-Cartan-Holst (ECH) cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model, serving as a null-consistency test; (2) a Monte Carlo validation of a NaMaster pseudo-Cℓ pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-documented, with a commendable level of transparency regarding methods, data artifacts, and the precise scope of its claims. The inclusion of detailed reproducibility materials and a claims-classification table is exemplary. However, several issues related to the framing of results in the abstract, the statistical robustness of one of the secondary analyses, and overall self-containment must be addressed before the paper can be considered for publication in Physical Review D.

---
### ESSENTIAL REVISIONS

**P1B-E1: Abstract framing of NaMaster pipeline bias is misleading.**
*   **Location:** Abstract, Page 1.
*   **Problem:** The abstract reports the NaMaster pipeline's recovery of an injected signal (`β = 0.27°` recovers `β = 0.238°`) and the resulting bias (`-0.032°`) as a headline result of the validation. However, the main text (p. 9, "Robustness battery and bias attribution" and "Canonical estimator choice") reveals that ~80% of this bias is attributable to the use of an unweighted χ² template fit, which gives undue weight to noise-dominated high-ℓ bins. An inverse-variance weighted fit is shown to recover `β = 0.264°` (bias `-0.006°`), largely removing the issue.
*   **Required Fix:** The abstract must be revised to provide this crucial context. It should state that the reported `-0.032°` bias is a feature of the specific, non-optimal (though canonical) estimator used, and that the bias is significantly reduced with a more standard inverse-variance weighting. Omitting this context misrepresents the source and magnitude of the pipeline's intrinsic bias.

---
### MAJOR REVISIONS

**P1B-M1: Potentially spurious `w₀-wₐ` result is given undue prominence.**
*   **Location:** Section IV (p. 4), Section V.C (p. 10), Table II (p. 20).
*   **Problem:** The paper reports a `+4.3σ` departure from ΛCDM in the `w₀` parameter (Table II), indicating a strong preference for phantom-crossing dark energy. This result is derived from a likelihood that combines two supernova catalogs (DES-SN5YR and Pantheon+) which have ~20% event overlap. As correctly stated in caveat (e) on p. 5, this combination is performed via a simple product of likelihoods without a joint covariance matrix to account for the shared events and their correlated systematics. This is a known-to-be-incorrect statistical procedure that can lead to artificially tightened constraints and biased central values. Presenting a >4σ result based on this flawed analysis, even with caveats, is not appropriate for a high-impact journal.
*   **Required Fix:** This analysis must be significantly de-emphasized. The `w₀-wₐ` results should be clearly labeled as a "demonstration of a potential systematic" or a "caveated diagnostic" throughout the text, not just in the fine print. The `+4.3σ` value should not be highlighted in the main text without an immediate and prominent disclaimer about the invalid statistical combination. The authors should consider either removing this analysis, moving it to an appendix with stronger warnings, or re-running it with a single, non-overlapping SN dataset (e.g., Pantheon+ only) to show how the result changes.

**P1B-M2: Paper lacks sufficient self-containment for a standalone publication.**
*   **Location:** Introduction, Page 2.
*   **Problem:** The paper is a "technical verification companion" to Paper I(a) [1]. While this framing is clear, the paper does not provide enough context for a reader to understand the motivation for the specific analyses without reading the other work. For example, it is not explained *why* ΔNeff is a relevant proxy for ECH spin-torsion effects, or what aspect of the ECH framework motivates the spectator-ALP consistency check.
*   **Required Fix:** The introduction should be expanded to include a concise summary (one to two paragraphs) of the key theoretical claims from Paper I(a) that necessitate the three technical checks performed here. This would make the paper a more valuable and self-contained contribution to the literature.

---
### MINOR REVISIONS

**P1B-m1: Inconsistent sample counts reported for MCMC analysis.**
*   **Location:** Page 3 (footnote 1) and Page 6 (Fig. 1 caption).
*   **Problem:** Footnote 1 on page 3 states the post-burnin count for the full-tension subset is 123,129. The caption for Figure 1 on page 6 reports "119,617 post-burnin samples" for the same dataset. The footnote explains this discrepancy is due to "getdist effective-sample weight-based thinning," but this can cause confusion for the reader.
*   **Required Fix:** To improve clarity, the caption of Figure 1 should be amended to read "119,617 getdist-thinned effective samples" or similar, explicitly distinguishing this number from the raw post-burnin sample count.

**P1B-m2: Justification for primary birefringence constraint is missing.**
*   **Location:** Section IV (p. 6) and Section VI (p. 10).
*   **Problem:** The paper uses the Eskilt & Komatsu [5] joint WMAP+Planck result (`β = 0.342° ± 0.094°`) as the primary observational constraint for the ALP analysis. While other results (Planck NPIPE, ACT DR6) are mentioned, the reason for prioritizing the Eskilt & Komatsu result is not stated.
*   **Required Fix:** Add a brief sentence in Section VI justifying this choice. For example, noting that it represents the most comprehensive joint analysis that accounts for shared systematics between the two experiments.

**P1B-m3: Future date on manuscript.**
*   **Location:** Page 1.
*   **Problem:** The manuscript is dated "June 14, 2026".
*   **Required Fix:** This placeholder should be corrected to the submission date or removed.

**P1B-m4: Uncomputed quantitative claim in abstract.**
*   **Location:** Abstract, Page 1.
*   **Problem:** The abstract states "the scan-prior m ~ H₀ region brackets the published joint WMAP+Planck signal". The word "brackets" implies the signal is contained within the region, which is a quantitative claim.
*   **Required Fix:** While the body supports this, for abstract-level precision, this should be quantified directly or rephrased to be less ambiguous (e.g., "is consistent with the signal"). Given the posterior shifts away from this region, the current phrasing could be seen as over-emphasizing the prior's success. A better phrasing might be: "While the scan-prior includes the m ~ H₀ region consistent with the signal, the posterior...".

---
### NIT-PICKS (Cosmetic)

**P1B-N1: Placeholder citation for companion paper.**
*   **Location:** References, Page 17.
*   **Problem:** Reference [1] is a placeholder for a "companion paper, posted concurrently on arXiv."
*   **Required Fix:** For final publication, this must be updated with the correct arXiv identifier and/or journal reference. This is noted for the record.

**P1B-N2: Minor numerical discrepancy in S₈ tension calculation.**
*   **Location:** Table I caption, Page 19.
*   **Problem:** The caption states the Planck+BAO+SN marginal sits in 2.6σ tension with DES-Y3. My calculation yields (0.827-0.776)/sqrt(0.010²+0.017²) = 2.59σ.
*   **Required Fix:** The value is correct to the quoted precision. No change is required, but this confirms the author's calculation.

---
## Summary recommendation
**MAJOR REVISIONS**

This is a high-quality, rigorous, and transparent technical paper that demonstrates a laudable commitment to reproducibility. The detailed validation work is valuable. However, the issues identified above are significant. The misleading framing of the NaMaster pipeline bias in the abstract must be corrected (P1B-E1). The presentation of a >4σ dark energy result from a statistically flawed combination of datasets is not acceptable in its current form and must be substantially revised (P1B-M1). Finally, the paper should be made more self-contained to maximize its utility to the community (P1B-M2).

I am confident that the author can address these points. Upon successful revision, this paper will be a strong candidate for publication in Physical Review D.
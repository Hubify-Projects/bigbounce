# P5 R36conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.70.pdf` md5=8bf87669 pages=31
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 145.4s

---

Referee Report: P5-R36conf

## General Comments

This manuscript presents a test for the environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1, cross-matched with a galaxy chirality catalog from a companion paper (Paper IV) and environmental classifications from DESIVAST and a V-Web tidal-tensor analysis. The primary result is a null detection: the chirality of spiral galaxies does not show a statistically significant correlation with their large-scale structure environment (void, wall, filament, cluster) at the sensitivity of the current data. The analysis includes a comprehensive suite of robustness checks, systematics tests, and cross-validations against other environmental classifiers.

The core analysis appears to be executed with care, and the detailed reporting of statistical tests and potential systematics is commendable. However, the manuscript in its current form has several critical issues that preclude its publication in Physical Review D. The most significant problems are its heavy reliance on an unpublished and un-peer-reviewed companion paper for foundational inputs (the chirality catalog and the systematic monopole offset), the presence of extensive internal-review and draft-version language, and a structure that obscures the primary result behind a multitude of secondary analyses. The paper requires major revisions to meet the standards of the journal.

## Findings

### ESSENTIAL

**P5-E1: Dependence on Unpublished, Non-Peer-Reviewed Companion Work**
*   **Section:** Throughout, starting with Abstract (p. 1)
*   **Problem:** The entire analysis is predicated on the "chirality catalog of Paper IV [3] (companion work, not yet peer-reviewed)". Key inputs, such as the per-galaxy labels and, critically, the "-0.0026 classifier-monopole offset," are imported from this work. The manuscript treats this monopole as a known systematic to be subtracted, but its origin, magnitude, and uncertainty are not derived or justified within this paper. This makes the current work not self-contained and its conclusions dependent on the validity of a manuscript that has not undergone peer review. A result cannot be considered robust if it is conditioned on an unverified external input.
*   **Required Fix:** The manuscript must be made self-contained.
    1.  The methodology for generating the chirality catalog and, most importantly, the derivation and characterization of the classifier-monopole systematic must be sufficiently summarized in this paper (e.g., in an appendix) for a reader to understand and evaluate it.
    2.  The reference [3] must be updated to a peer-reviewed publication or a public preprint (e.g., on arXiv) that is stable and citable. Publishing a paper that rests on a "not yet peer-reviewed" companion is unacceptable.

**P5-E2: Presence of Internal-Review and Draft-Version Language**
*   **Section:** Throughout
*   **Problem:** The manuscript is littered with phrases and entire sentences that are clearly part of an internal review or drafting process, not a finished scientific paper. This is unprofessional and makes the paper difficult to read. Examples are numerous:
    *   p. 2: "An earlier draft quoted... those values were computed on an unfiltered... and are withdrawn in favor of the declared-parent recompute"
    *   p. 3: "an earlier harmonic-space subsample-mask MASTER-deconvolved l = 1 statistic was withdrawn in Paper IV v1.0.166 after a provenance audit..."
    *   p. 13: "An earlier draft of this table reported... those values are withdrawn in favor of the declared-parent recompute below."
    *   p. 13: "(An earlier draft quoted σ = 11.32 on an n=3,696,152 filament cell; that population belonged to the withdrawn unfiltered nearest-label join...)"
    *   p. 18: "An earlier draft reported n_void = 86,276 / 64,514... those values reproduce exactly only under a zone-indexing defect... The corrected per-cap join values above supersede them"
    *   p. 24: "(An earlier draft compared the Tempel overlap against the V-Web classes of the full matched sample... that comparison, including its headline 0.026 pp filament figure, is withdrawn.)"
    *   p. 27: "An earlier draft of this summary stated the bright/dark split agreed 'within ±0.001'; that statement was stale and is corrected here"
*   **Required Fix:** Remove all such language. The paper should present the final, correct analysis and results. The history of the analysis, including corrected mistakes and withdrawn values, is not appropriate for the final manuscript. This requires a thorough proofread of the entire text.

**P5-E3: Invalid Publication Date**
*   **Section:** Abstract (p. 1)
*   **Problem:** The paper is dated "(Dated: June 2026 — v0.1.70-2026-06-12)". A future date is nonsensical and suggests the use of a placeholder system. This is not a publication-ready document.
*   **Required Fix:** Replace the date with the actual date of submission. Remove the internal versioning string from the visible date line.

### MAJOR

**P5-M1: Paper Length and Structure**
*   **Section:** Entire manuscript
*   **Problem:** At 31 pages, the paper is excessively long for a null-result study. The primary finding (the DESIVAST-anchored null result) is robust and important, but it is buried among a vast number of secondary cross-checks (V-Web, Tempel, ASTRA, T-Web literature, etc.). This structure diffuses the focus and makes it difficult for the reader to identify the main thread of the argument.
*   **Required Fix:** Restructure the paper significantly.
    1.  The main body of the paper should be shortened to focus on: Introduction, Data (chirality and DESI), Methods (for the primary DESIVAST and secondary V-Web tests), Results (presenting the DESIVAST and V-Web results as primary and secondary), Discussion, and Conclusion. This should be achievable in ~10-12 pages.
    2.  The numerous other cross-checks (Tempel, ASTRA, detailed systematics, redshift-shell corrections, etc.) are valuable but should be moved to appendices. This will improve readability while retaining the commendable thoroughness of the analysis.

**P5-M2: Misleading Title and Abstract Framing**
*   **Section:** Title and Abstract (p. 1)
*   **Problem:** The title is "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check...". The body, however, correctly designates the DESIVAST test as primary and the V-Web/T-Web test as secondary. The abstract also leads with the DESIVAST result. The title's emphasis on "T-Web" is therefore somewhat misleading about the paper's primary contribution.
*   **Required Fix:** Revise the title to better reflect the analysis structure. A suggestion: "A Test of the Environmental Dependence of Spiral Galaxy Chirality in DESI DR1 Using Voids and the Cosmic Web". This more accurately frames the DESIVAST void test and the V-Web test as the two main pillars.

**P5-M3: Uncomputed Quantitative Claims**
*   **Section:** p. 28, §XIII. LIMITATIONS
*   **Problem:** The discussion of RSD contamination contains several qualitative statements where quantitative estimates are required. For example: "The implied per-class Δfcw contamination is sub-percent (~ 0.2 pp), the same order of magnitude as the ~0.1 pp filament/cluster class-fraction movement... rather than negligible relative to it." While an order-of-magnitude estimate is provided later on p. 29, this section mixes necessary caveats with uncomputed assertions. The statement "This scalar bound is necessary but not sufficient" is correct but should be followed by a more direct statement of the limitation on the final result.
*   **Required Fix:** The authors state on p. 29 that "we explicitly do not quantify the propagated uncertainty in the present paper". For a paper of this rigor, this is a significant omission. The authors must either perform the required "Zel'dovich-reconstructed re-classification" to quantify this uncertainty, or they must state more clearly and prominently (e.g., in the abstract and conclusions) that the null result is established for redshift-space environments and that its application to real-space environments is subject to an unquantified uncertainty from RSDs. The current framing is insufficient.

### MINOR

**P5-m1: Incomplete Table**
*   **Section:** p. 17, Table VIII
*   **Problem:** The table is malformed in the provided PDF. The `n` column contains extra numbers (e.g., "56,981 28", "621,964 309"). The final row mentioned in the reviewer metadata ("VoidFinder exact, hole-support-footprint-restricted non-void 253,276 126") is also garbled. This appears to be a typesetting or OCR error.
*   **Required Fix:** Correct the formatting of Table VIII to be legible and complete. Ensure all columns contain only the appropriate data.

**P5-m2: Inconsistent Use of "V-Web" and "T-Web"**
*   **Section:** Throughout, e.g., p. 2, footnote `a`
*   **Problem:** The paper uses the Hahn (2007) tidal-tensor (T-Web) formalism but refers to its implementation as "V-Web" for "backward compatibility". While this is explained in a footnote, it creates potential confusion, especially since the Hoffman et al. (2012) velocity-shear V-Web is a distinct method.
*   **Required Fix:** For clarity, the authors should consistently refer to their classifier as "T-Web" or "tidal-tensor web" throughout the main text, as this is the formalism they actually implement. The "V-Web" name can be mentioned once in the methods section with the explanation for the naming choice. The title should also use "T-Web".

**P5-m3: Citation of Preliminary Conference Proceedings**
*   **Section:** p. 15, Ref [13]
*   **Problem:** The reference for DESIVAST is cited as "Rincón et al. 2025, ApJ 982, 38 [13]". The year 2025 is in the future. While this may be an accepted publication with a future issue date, this should be clarified. If it is not yet published, it should be cited as "in press" or with its arXiv identifier.
*   **Required Fix:** Verify the publication status of Ref [13] and format the citation correctly. The same applies to Ref [11] and [12], which are cited as preprints from 2026.

**P5-m4: Effect Size for Homogeneity Test**
*   **Section:** p. 1, Abstract; p. 7, §VI A
*   **Problem:** The abstract and main text report the omnibus homogeneity test result as "χ² = 3.55, 3 d.o.f., p = 0.31". A p-value from a χ² test on a large sample (n > 800,000) can be non-significant even if a small but real effect exists. The authors should report an effect size.
*   **Required Fix:** Report an appropriate measure of effect size, such as Cramér's V, alongside the χ² statistic. (Note: The authors do report Cramér's V for a different test on p. 12, so they are familiar with the method. It should be applied here as well.)

### NIT

**P5-N1: Duplicate Phrase**
*   **Section:** p. 12, §VI D
*   **Problem:** The text reads "...V-Web class × bright/dark, four-by-two on the n_bright+dark = 811,609 bright+dark subset...". The phrase "bright+dark" is repeated.
*   **Required Fix:** Remove the duplicate phrase.

**P5-N2: Awkward Phrasing**
*   **Section:** p. 7, §VI B, Primary analysis path
*   **Problem:** The text says the DESIVAST catalog "ships three independent void-finding algorithms". "Ships" is informal jargon.
*   **Required Fix:** Rephrase to "provides" or "includes".

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a methodologically sound and thorough investigation of a relevant topic in cosmology. The core null result is well-supported by the primary analysis and an extensive set of robustness checks. However, the paper is not ready for publication. The reliance on an unpublished companion work for its central inputs, the inclusion of distracting draft-stage language, and a convoluted structure that obscures the main result are critical flaws.

If the authors can (1) make the paper self-contained by properly incorporating the necessary background from Paper IV, (2) thoroughly remove all internal-review and draft-related text, (3) correct the invalid dating, and (4) significantly restructure the manuscript to distinguish the primary result from the supporting appendices, the paper would be a strong candidate for publication in Physical Review D.
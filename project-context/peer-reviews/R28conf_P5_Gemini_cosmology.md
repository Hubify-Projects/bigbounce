# P5 R28conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.59.pdf` md5=3a80c50b pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 140.0s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals"

This paper presents a detailed investigation into the potential dependence of spiral galaxy chirality on the large-scale cosmic web environment. The authors cross-match a large catalog of spiral galaxies with DESI DR1 data, classify their environments using a tidal-tensor (V-Web) method, and perform a primary cross-check using the DESIVAST void catalog. The analysis is comprehensive, including numerous robustness tests, sensitivity sweeps, and cross-validations against other environment classifiers. The headline result is a null detection: spiral chirality shows no statistically significant dependence on environment beyond a known, catalog-wide monopole offset, which is attributed to a classifier systematic.

The scientific analysis appears to be rigorous and the scope of the cross-checks is impressive. The core conclusion of a null result is well-supported by the data presented. However, the manuscript in its current form has severe presentational issues that make it unsuitable for publication in Physical Review D. The paper reads more like a technical note with a visible development history than a polished scientific article. The required revisions are substantial.

---

### ESSENTIAL Revisions

These issues must be addressed before the manuscript can be considered further.

**P5-E1: Removal of Internal Development History and "Withdrawn" Results**
*   **Location:** Throughout the manuscript (e.g., Page 2, Sec I; Page 10, Sec VI.D.c; Page 11, Sec VII; Page 12, Sec VII; Page 16, Sec VIII.D; Page 17, Sec VIII.F; Page 21, Sec IX.B; Page 24, Sec XI).
*   **Problem:** The paper is replete with references to "earlier drafts," "withdrawn" values, "superseded" results, corrected defects, and "stale" statements. Examples include:
    *   "an earlier harmonic-space... was withdrawn in Paper IV v1.0.166"
    *   "An earlier draft quoted... are withdrawn in favor of the declared-parent recompute"
    *   "those values reproduce exactly only under a zone-indexing defect... The corrected per-cap join values above supersede them"
    *   "that statement was stale and is corrected here"
*   **Required Fix:** Remove all such language. A scientific paper should present the final, correct methodology and results. The history of the analysis, including corrected errors and superseded calculations, is not appropriate for the body of a published article. The manuscript must be rewritten to present only the final, validated analysis path.

**P5-E2: Removal of Local File Paths**
*   **Location:** Throughout the manuscript (e.g., Page 4, Sec IV.A; Page 7, Sec VI.A; Page 8, Sec VI.B; and many others).
*   **Problem:** The text contains numerous explicit file paths to internal analysis artifacts (e.g., `pipelines/p5_desi_chirality/outputs/21_r23conf_meta_closures.json`). This is unacceptable for a formal publication.
*   **Required Fix:** Remove all local file paths. Refer to the data repository (mentioned in Appendix B) for specific numerical results or analysis scripts, but do not embed the file structure in the main text. For example, instead of citing a JSON file, state "as verified in the analysis documented in the data repository [ref]".

**P5-E3: Sign Error in Abstract**
*   **Location:** Page 1, Abstract.
*   **Problem:** The abstract states for the DESIVAST re-projection: `(n=56,981, Δfcw=0.0007)`. However, Table VII (Page 15) and Table VIII (Page 17) show `fcw_void = 0.4964` and `fcw_non-void = 0.4971`. The difference, following the sign convention `fcw_void - fcw_non-void` from Table VIII, is `0.4964 - 0.4971 = -0.0007`.
*   **Required Fix:** Correct the sign of `Δfcw` in the abstract to `-0.0007` to be consistent with the body of the paper.

**P5-E4: Sign Error in Table III Residual Calculation**
*   **Location:** Page 9, Table III.
*   **Problem:** The final column is labeled `σ_obs - σ_pred`. For Quintile 3, `σ_obs = -3.94` and `σ_pred = -2.07`. The residual should be `-3.94 - (-2.07) = -1.87`. The table lists `1.87`. The same sign error appears for Quintile 1. The text on page 8 refers to the residual as `|σ_obs - σ_pred| ≈ 1.87`, which contradicts the table's column header.
*   **Required Fix:** Clarify whether the column is the signed difference or the absolute difference. If it is the signed difference, correct all values in the final column of Table III. If it is the absolute difference, change the column header to `|σ_obs - σ_pred|`. The text and table must be made consistent.

---

### MAJOR Revisions

**P5-M1: Reliance on Unpublished Companion Work**
*   **Location:** Throughout, starting on Page 1, Abstract.
*   **Problem:** The entire analysis is critically dependent on "Paper IV [3]," which is repeatedly described as "not yet peer-reviewed" and "in preparation." Key inputs, such as the galaxy chirality labels and the fundamental `-0.0026` classifier monopole offset, are taken from this work. A paper submitted to PRD must be reasonably self-contained. Basing a null result on a systematic offset derived in an unavailable paper is problematic.
*   **Required Fix:** The authors must either (a) provide a more detailed summary of the methods and results from Paper IV in an appendix to make the present work self-contained, including the derivation and uncertainty of the monopole offset, or (b) ensure that Paper IV is publicly available (e.g., on arXiv) and submitted concurrently. The latter is strongly preferred.

**P5-M2: Non-standard Citation of Forthcoming Work**
*   **Location:** Page 22, Sec IX.C and Page 28, Bibliography ([11], [12]).
*   **Problem:** The paper cites two works, Ullah et al. and Zapata-Zuluaga et al., with publication dates of "2026" and "2026 April." This is not a standard or verifiable citation format.
*   **Required Fix:** These references must be updated to a standard format. If they are available as preprints, cite the arXiv ID. If they are accepted for publication, use "in press" with the journal name. If they are not yet public, they cannot be cited in this manner.

**P5-M3: Manuscript Structure and Readability**
*   **Location:** General structure.
*   **Problem:** The paper is very long (28 pages) for a null result. The primary, most robust result from the DESIVAST-anchored analysis (Section VIII) appears relatively late in the paper, after the less robust V-Web analysis and its extensive sensitivity sweep. The abstract is exceptionally dense and difficult to parse, packed with a long sequence of numbers that obscures the main takeaway.
*   **Required Fix:** Consider restructuring the paper to present the primary DESIVAST result (Section VIII) more prominently, perhaps immediately after the initial V-Web results (Section VI). The V-Web sensitivity analysis (Section VII) could then follow as a robustness check. The abstract should be rewritten to be more accessible, focusing on the main conclusion and the one or two most important supporting numbers (e.g., the final DESIVAST constraint), while moving the detailed ledger of secondary tests to the main text.

---

### MINOR Revisions

**P5-N1: Non-standard Date Format**
*   **Location:** Page 1, under the author's affiliation.
*   **Problem:** The date is given as "(Dated: June 2026)".
*   **Required Fix:** This should be removed. The journal will add the reception date.

**P5-N2: Clarification of P4 vs. P5 Monopole**
*   **Location:** Page 5, Sec V and Page 17, Sec VIII.F.
*   **Problem:** The paper uses `Δfcw` from "Paper IV" (the P4 catalog) for `σ_pred` but then introduces a "P5 matched-sample monopole" for the `σ_vs_monopole` residuals. The distinction and justification are only made clear on page 17.
*   **Required Fix:** Introduce and define the "P4" (full catalog) and "P5" (DESI-matched subsample) monopoles clearly when they are first used in Section V.

**P5-N3: Figure 8 Caption**
*   **Location:** Page 19, Figure 8.
*   **Problem:** The caption states "the Npix_both = 727 pixels". The variable name `Npix_both` is jargon-like.
*   **Required Fix:** Rephrase for clarity, e.g., "...across the 727 pixels containing both voids and a sufficient number of spirals...".

---

### NIT (Cosmetic)

**P5-T1: Awkward Phrasing**
*   **Location:** Page 1, Abstract.
*   **Problem:** "Sample ledger in one breath:" is overly colloquial.
*   **Required Fix:** Rephrase to something more formal, like "Summary of samples and results:".

---

## Summary recommendation

**MAJOR REVISIONS**

The authors have performed an exhaustive and statistically robust analysis of a well-defined physical question. The level of detail in the cross-checks, sensitivity tests, and systematics handling is commendable. The core scientific conclusion—that there is no evidence for environment-dependent spiral chirality at the tested scales and sensitivity—is well-supported and represents a valuable contribution to the literature.

However, the manuscript is not ready for publication. The presentation is severely flawed by the inclusion of extensive "internal chatter" about the paper's own development history, such as withdrawn results and corrected errors. This must be completely excised for the paper to meet professional standards. Furthermore, the critical dependence on an unpublished companion paper and the non-standard citation of other works are major issues that compromise the paper's integrity and verifiability.

While the underlying science is strong, the manuscript requires a thorough rewrite to address these fundamental presentational problems. I recommend that the paper be reconsidered only after these essential and major revisions have been implemented.
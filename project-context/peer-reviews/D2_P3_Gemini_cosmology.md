# P3 D2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=7c935f19 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3455 chars)
**Wall time**: 161.9s

---

**Referee Report on "Spectrally Unusual Sources at Scale..." by Houston Golden**

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of 378,280 unique anomalies. The work uses an autoencoder framework (BIGAE) and introduces a "Path-C" native-retraining protocol to overcome issues with cross-survey model transfer. The paper details the catalog construction, validation, and cross-survey analysis. It then presents two cosmological applications: a multi-tracer forecast for primordial non-Gaussianity (fNL) and a consistency check of the matter-bounce scenario against NANOGrav 15-yr data.

The work is methodologically sophisticated, impressively scaled, and exceptionally transparent about its limitations, validation procedures, and potential pitfalls. The distinction between cross-transfer artifacts and natively-trained results is a crucial lesson for the field. The cosmological applications are relevant and handled with appropriate rigor, particularly the careful treatment of statistical uncertainties and model dependencies. The paper is a substantial contribution. However, its density and complexity require several clarifications and corrections to meet the publication standards of Physical Review D.

---
### ESSENTIAL Revisions

**P3-E1: Abstract-Body Mismatch on LAMOST Status**
*   **Section/Page**: Abstract (p. 1) vs. §IIID, §VIA (p. 10, 19)
*   **Problem**: The abstract states the catalog-grade subset (269,117 entries) "excludes the LAMOST exploratory tier (~113,000 objects retained as a methodological lesson: 98% blue-excess training-bias artifact, injection-recovery gate FAIL)". However, the primary headline count of 378,280 *does* include these objects. The abstract correctly identifies the 269,117 count as the "recommended catalog-grade tier" but the framing could be clearer. The main text (§VIA) correctly frames the LAMOST tier as a "methodological lesson" but its inclusion in the primary headline count (378,280) while being simultaneously flagged as a failed, exploratory artifact creates a contradiction. The headline number should represent the robust, science-ready sample.
*   **Fix**: The abstract and introduction must be revised to state clearly that the primary science-grade catalog contains 269,317 objects, and the full 378,280 catalog is an extended version that includes the exploratory LAMOST tier for methodological completeness. The headline number itself should be the science-grade one. Alternatively, if the author insists on the 378,280 headline, the abstract must state upfront that this number includes a ~113,000-object tier that failed validation and is considered exploratory. The current phrasing is ambiguous.

**P3-E2: Unjustified Use of Future Date**
*   **Section/Page**: Title block (p. 1)
*   **Problem**: The paper is dated "June 19, 2026". This is unconventional for a scientific publication and could cause confusion regarding the timeliness of the data and analysis. While pre-dating for embargo reasons is understood, a date two years in the future is inappropriate for a journal submission.
*   **Fix**: The date must be changed to the date of submission or a reasonably proximate date.

---
### MAJOR Revisions

**P3-M1: Insufficiently Justified fNL Systematics Bounds**
*   **Section/Page**: §V C (p. 18)
*   **Problem**: The paper dismisses several key observational systematics in the fNL forecast with qualitative arguments or internal bounds that lack external validation.
    1.  "General-relativistic projection corrections... contribute |∆σ/σ| < 0.02% at kmax = 0.2h Mpc⁻¹... an internal order-of-magnitude bound from the (H/k)² suppression... not an external-literature value". This is insufficient for PRD. While GR corrections are subdominant for fNL, a simple (H/k)² scaling is not a substitute for a proper calculation using a code like `CLASSgal` or `CAMB_sources`. The claim requires a citation to a work that has computed these effects for a similar survey, or the author must perform the calculation.
    2.  The forecast "assumes zero observational systematics (fiber-assignment, photo-z, foreground)". While the fiber-assignment effect is bounded in a Fisher formalism, the impact of photo-z uncertainties and foreground contamination on the anomaly-selected tracer sample is not quantified at all. These are critical systematics for any multi-tracer analysis.
*   **Fix**:
    1.  For the GR projection effects, either perform a calculation using established codes or cite a specific result from the literature (e.g., from papers by Bonvin, Durrer, Challinor, Yoo) that justifies the <0.02% bound for this specific tracer sample and redshift range.
    2.  The author must add a substantive discussion of the potential impact of photo-z errors and foregrounds on the anomaly tracer sample and the bias measurement. While a full simulation is beyond scope, the paper should at least estimate the potential magnitude of these effects and acknowledge them as a major source of systematic uncertainty for any future analysis.

**P3-M2: Ambiguous Scope of the "Genuine Novelty Fraction"**
*   **Section/Page**: Abstract (p. 1), §IV A (p. 13)
*   **Problem**: The paper reports a "genuine novelty fraction of 178/1,000 ≈ 17.8%". The text correctly clarifies this is a "single-sample point estimate on the DESI top-1,000 score stratum, not a survey-wide rate". However, this crucial caveat is easily missed. The abstract presents this number prominently, and it could be misinterpreted as the novelty rate of the entire 378,280-object catalog.
*   **Fix**: The abstract must be rephrased to state explicitly: "A deep archival cross-match of the *top-1,000 highest-scoring DESI anomalies* yields a candidate genuine novelty fraction of 17.8%; this rate is not extrapolated to the full catalog." The body of the paper (§IV A) should also reinforce that this measurement only applies to the extreme tail of one survey's distribution and cannot be assumed for other surveys or lower-score objects.

**P3-M3: Inconsistent Terminology for eROSITA Tier**
*   **Section/Page**: Abstract (p. 1), §IIIE (p. 11), Table I (p. 7)
*   **Problem**: The eROSITA anomaly set is described in multiple, slightly different ways: "membership-only tier" (§IID), "released as a n = 298 membership list only" (Abstract), "fixed top-298 cap" (Table I caption), "fixed top-298 score-knee cap" (§IIIE). The core issue—that the score axis itself is not reproducible—is handled with excellent transparency in §IIIE, but the terminology should be standardized. The term "score-knee" is particularly confusing as it implies a feature on a score axis that the paper states is irreproducible.
*   **Fix**: Standardize the terminology across the paper. The most accurate and transparent description is "a fixed membership list of 298 objects". Remove the term "score-knee" as it is misleading. The abstract, Table I, and all mentions should use this consistent phrasing.

---
### MINOR Revisions

**P3-m1: Unclear Provenance of Gaia Preprocessing**
*   **Section/Page**: §IIBα (p. 3), §IIG (p. 12)
*   **Problem**: The paper states that the exact 20-feature production script for the Gaia run "was not recovered from any committed backup" and that the specification is "lineage-inferred rather than directly recovered". This is commendably transparent but raises a reproducibility issue.
*   **Fix**: The author should make a final attempt to reconstruct the exact feature list and scaling. If this is impossible, the Gaia portion of the catalog must be flagged as "exploratory and not fully reproducible" in the abstract and throughout the text, similar to how LAMOST is handled, albeit for a different reason. The Data Availability section must also explicitly state that the Gaia preprocessing is best-effort.

**P3-m2: Inconsistent SIMBAD-unmatched Fractions**
*   **Section/Page**: Table I (p. 7) vs. §IV A (p. 13)
*   **Problem**: Table I lists the SIMBAD-unmatched fraction for SDSS DR18 as 90%. The text in §IV A states "SDSS DR18 90% (cool dwarfs outside DESI distribution, present in SDSS photometric but not individually in SIMBAD)". This is consistent. However, Figure 6 (p. 14) shows the SDSS bar also at 90%. The aggregate fraction of 58.8% is calculated from a "pooled run" on the top-100 anomalies of four surveys. The text and captions are clear, but the visual juxtaposition of per-survey total rates and a top-100 aggregate rate could be confusing.
*   **Fix**: Add a sentence to the caption of Figure 6 clarifying that the individual bars represent the unmatched fraction for the *entire* anomaly tier for that survey (as listed in Table I), while the dashed line represents an aggregate over the *top-100* objects from a subset of surveys.

**P3-m3: Potentially Confusing Figure 9**
*   **Section/Page**: §V (p. 19, Fig. 9)
*   **Problem**: Figure 9 shows the per-redshift-bin decomposition of the fNL forecast under a *fixed* bias prior (a=0.15). The caption correctly states that the paper's primary forecast uses the *empirically measured* bias and is consistent with no improvement. However, presenting a figure that shows a 6.1% improvement, even with caveats, could lead to misinterpretation.
*   **Fix**: The title of Figure 9 should be changed to "Reference fNL Forecast for a Fixed Bias Prior (a=0.15); Not the Primary Result". The caption should begin with a bolded sentence: "**This figure illustrates a reference calculation and is not the primary forecast of this work, which finds no significant multi-tracer improvement.**"

**P3-m4: Citation Formatting and Traceability**
*   **Section/Page**: Bibliography (p. 28-29)
*   **Problem**: Several arXiv IDs are for pre-prints of accepted papers. For example, [1] is listed as "Astron. J. (accepted 2025), arXiv:2503.14745". The arXiv ID appears to contain a future date, which is non-standard.
*   **Fix**: Review all citations. Replace pre-print IDs with the final journal reference where available. For accepted but not-yet-published papers, use the correct format and verify the arXiv ID. The "2503" in the arXiv ID for a 2025 paper is highly suspect and should be double-checked.

---
### NITPICKS

**P3-N1: Redundant Phrasing**
*   **Section/Page**: Abstract (p. 1)
*   **Problem**: "the recommended catalog-grade tier contains 269,317 unique entries (269,117 point-source after dropping the 200 Planck map patches; provenance below), drawn from a full Path-C unique catalog of 378,280 anomalies: 378,080 point-source object detections...". The parenthetical breakdown is repeated immediately after.
*   **Fix**: Streamline this sentence. For example: "...the recommended catalog-grade tier contains 269,117 unique point-source entries. This tier is a subset of the full exploratory catalog of 378,280 anomalies (378,080 point sources and 200 Planck CMB map patches)."

**P3-N2: Awkward Footnote Referencing in Table I**
*   **Section/Page**: Table I (p. 7)
*   **Problem**: The footnotes for Table I use a mix of symbols (°, †, #, ||, $, *, ♡, ♣, ♠). This is non-standard and visually cluttered. Standard practice is letters (a, b, c...).
*   **Fix**: Reformat the footnotes to use a standard alphabetical sequence.

**P3-N3: Internal Audit Language**
*   **Section/Page**: §IVA (p. 14)
*   **Problem**: The text refers to an "audit artifact pipelines/p3_anomaly_engine/pathc_dedup/r23conf_dedup_audits.json". While pointing to reproducibility scripts is good, this reads like an internal file path.
*   **Fix**: Rephrase to be more formal. For example: "as documented in the deduplication audit script provided in the companion data repository". This applies to all similar instances.

---
## Summary recommendation

**MAJOR REVISIONS**

This is a very strong, comprehensive, and methodologically important paper. The author has demonstrated an exceptional commitment to transparency and rigorous self-assessment, which is commendable. The scale of the catalog and the care taken in its validation are impressive. The cosmological applications are timely and well-executed.

However, the paper requires major revisions before it can be accepted for publication in Physical Review D. The key issues relate to the clarity of the abstract regarding the status of the LAMOST data, the justification for systematics handling in the fNL forecast, and the precise scope of the headline "novelty fraction". These points must be addressed to ensure that the paper's significant contributions are communicated without ambiguity. Once these revisions are made, the paper will represent a valuable and impactful addition to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a more rigorous, "second pass" review of the paper.

---
### NEW MAJOR Revisions

**P3-M4: Incorrect Power Spectrum Template for NANOGrav Analysis**
*   **Section/Page**: Appendix E, Eq. (E1) (p. 25)
*   **Problem**: The power-law template model used for the NANOGrav MCMC analysis, presented in Eq. (E1), appears to be incorrect. The standard power spectral density for timing residuals from a stochastic background is `P(f) ∝ f^-(γ+3)`. The equation presented has a frequency dependence of `... + (γ-3)log(fyr) - γlog(fi)`. This is equivalent to `P(f) ∝ f_yr^(-3) f^(-γ)`, which is missing the crucial `f^(-3)` dependence. This discrepancy could significantly alter the posterior for γ.
*   **Fix**: The author must verify and correct Eq. (E1) to match the standard template used in pulsar timing analyses (e.g., as in the NANOGrav 15-yr paper [18]). Crucially, the author must also confirm that the MCMC analysis itself was performed with the correct model, and that Eq. (E1) is merely a typographical error in the manuscript. If the analysis was run with the incorrect model as written, the entire NANOGrav section (§V A, Appendix E) must be re-run and its results updated.

---
### NEW MINOR Revisions

**P3-m5: Incorrect Cross-References in Residual Caveats Table**
*   **Section/Page**: Table V (p. 21)
*   **Problem**: The "Resolution" column in Table V, which is intended to guide the reader, contains incorrect cross-references.
    1.  Item (b) "DESI OOD" is pointed to "§II". This is too general. The specific reconciliation and numbers are in §IIC and Table II.
    2.  Item (g) "Jaccard" is pointed to "§III E". This is incorrect; §IIIE is about eROSITA. The DESI Jaccard validation is detailed in §IIC and §VID(i).
*   **Fix**: Correct the section references in the "Resolution" column of Table V to point to the precise locations where these caveats are addressed. For (b), point to §IIC and Table II. For (g), point to §IIC and §VID(i).

**P3-m6: Unsupported "Largest Multi-Archive" Claim**
*   **Section/Page**: Table I caption (p. 7)
*   **Problem**: The caption claims "The total represents the largest multi-archive anomaly search reported to date of which we are aware." While this is likely true given the scale of the work, the paper provides no comparison to other multi-archive searches to substantiate the claim. In a field with rapidly growing data volumes, such claims require explicit justification.
*   **Fix**: Either provide a brief comparison by citing one or two previous large-scale multi-archive efforts and their scale, or soften the claim to "To our knowledge, this is one of the largest..."

---
### NEW NITPICKS

**P3-N4: Irregular Citation Format and Future-Dated arXiv ID**
*   **Section/Page**: Bibliography, citation [1] (p. 28)
*   **Problem**: Citation [1] (the DESI DR1 paper) is listed with an acceptance date of "(accepted 2025)" and an arXiv ID of "arXiv:2503.14745". An arXiv identifier corresponding to March 2025 is not possible at the time of writing. This is either a significant typo or an inside joke, neither of which is appropriate for a formal publication.
*   **Fix**: The author must correct the arXiv identifier and publication year for this reference to reflect its actual status. If it is a typo for `2403` or another valid ID, it should be fixed. If the paper is not yet on arXiv, the reference should be formatted as "in preparation" or "submitted".
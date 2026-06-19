# P3 D1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=62d7b294 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3697 chars)
**Wall time**: 192.8s

---

## Referee Report on "Spectrally Unusual Sources at Scale..."

**Report ID:** P3-D1-R1
**Journal:** Physical Review D

This paper presents a large-scale anomaly detection analysis across seven astronomical surveys (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE), producing a catalog of 378,280 unique anomalous sources. The authors use a custom autoencoder framework (BIGAE) and develop a "Path-C" protocol involving native per-survey retraining to overcome domain-shift issues identified in an initial cross-transfer analysis. The work provides a detailed methodological account, including a frank discussion of failures and limitations, and presents two primary cosmological applications: constraining primordial non-Gaussianity (`fNL`) and testing matter-bounce cosmology against NANOGrav data.

The scale of this work is impressive, and the methodological transparency is commendable. The detailed validation, robustness checks, and careful handling of statistical claims are strengths of the manuscript. However, there are several critical issues, primarily concerning reproducibility and rigor, that must be addressed before this paper can be accepted for publication.

### ESSENTIAL Revisions

**P3-E1: Provenance and Reproducibility of Tabular Feature Preprocessing**
-   **Section/Page:** §II B (p. 3), §III G (p. 13), Acknowledgments (p. 23)
-   **Problem:** The paper repeatedly states that the exact preprocessing scripts for the Gaia and eROSITA catalogs were not recovered from backups. For Gaia, a "lineage-inferred" script from a successor run was used. For eROSITA, the production score axis is described as "unrecoverable as a matter of provenance". These are critical failures of reproducibility for a data-driven paper. While the authors are commended for their transparency, this does not meet the archival standards of PRD. The catalog, as presented, contains components that cannot be programmatically reproduced from source data.
-   **Required Fix:** The authors must either (1) successfully recover the original scripts and re-run the analysis to confirm the results, or (2) re-generate the Gaia and eROSITA anomaly lists from scratch using a fully documented, committed script (e.g., the "successor run" script for Gaia) and report those as the canonical results, updating all downstream numbers. If this is not possible, the Gaia and eROSITA tiers must be moved to a separate appendix for "non-reproducible exploratory results" and removed from all headline counts and primary analyses. The current state of "best-available but not reproducible" is unacceptable for the main body of the paper.

**P3-E2: Abstract-Last Drift Sweep: `σ(fNL)` Headline**
-   **Section/Page:** Abstract (p. 1) vs. §V b (p. 18)
-   **Problem:** The abstract states: "the de-biased point estimate returns the single-tracer baseline σ(fNL)std = 8.98 exactly (no multi-tracer improvement at current S/N)". The body (p. 2) states: "the central 9.4% improvement is a noise-driven forecast pending higher-S/N follow-up, not a detection". While the body correctly resolves this apparent contradiction by explaining the de-biasing procedure, the abstract's use of "exactly" is statistically jarring and potentially misleading. A noisy measurement resulting in a value that is "exactly" the baseline is a zero-probability event; it implies the de-biasing procedure was constructed to produce this outcome.
-   **Required Fix:** Rephrase the abstract to avoid the word "exactly". State the finding more directly, for example: "The de-biased point estimate of the multi-tracer improvement is consistent with zero, returning the single-tracer baseline of σ(fNL)std = 8.98. The analysis finds no statistically significant improvement at current signal-to-noise." This is more accurate and avoids the problematic implication of "exactly".

### MAJOR Revisions

**P3-M1: Boundedness of General Relativistic Systematics**
-   **Section/Page:** §V c (p. 18)
-   **Problem:** The paper bounds the impact of GR projection corrections on the `fNL` forecast with the statement: "|Δσ/σ| < 0.02% at k_max = 0.2 h Mpc⁻¹ ... an internal order-of-magnitude bound from the (H/k)² suppression at the Fisher-weighted scales, not an external-literature value". This is too hand-wavy for PRD. An "internal order-of-magnitude bound" is not a substitute for a calculation. The reader cannot verify this claim.
-   **Required Fix:** The authors must provide a concrete calculation in an appendix, even a schematic one, that justifies this bound. It should show the relevant integrals from the Fisher matrix formalism and how the (H/k)² suppression leads to the quoted <0.02% value for the specific tracer populations and redshift range used in this work. Alternatively, cite a specific equation from a standard reference (e.g., [39, 40, 41]) and show how their parameters plug into it.

**P3-M2: Score Axis for Figure 8**
-   **Section/Page:** §IV C, Figure 8 Caption (p. 17)
-   **Problem:** The caption for Figure 8 states: "the burned-in 'Score' annotations are display values from that script rather than catalog-pipeline outputs". This is confusing. The objects were selected for being anomalous based on their catalog scores. The figure showing these objects should be annotated with the official, canonical catalog scores that led to their selection. Using different, non-catalog "display scores" undermines the connection between the figure and the catalog. For example, panel (d) shows a score of 49.5, which the text identifies as the *cross-transfer* score, while the object's membership in the final catalog depends on its *native re-score*.
-   **Required Fix:** Re-generate the figure annotations to show the canonical, final Path-C native anomaly scores for both the DESI and SDSS detections. The caption should then explicitly state these are the final catalog scores. The cross-transfer score for TIC 37431335 can be mentioned in the text or caption as a diagnostic of the domain shift, but the primary labels on the figure must be the final, physical scores from the released catalog.

**P3-M3: Interpretation of the DESI Science-Class Recount**
-   **Section/Page:** §III A (p. 6)
-   **Problem:** The paper finds that ~98.7% of DESI anomalies are not on primary science targets. The text correctly states this means the catalog is "an anomaly scan of everything DESI pointed a fiber at, dominated by non-science-target spectra". However, the implications for the *nature* of these anomalies are not discussed. Are they instrumental artifacts on sky fibers? Or are they real but faint astrophysical sources that fell into filler or secondary fibers? This distinction is scientifically important.
-   **Required Fix:** Add a paragraph of discussion speculating on the nature of the ~98.7% of anomalies. The authors could, for example, cross-match a small sample of these non-science-target anomalies against deep imaging (e.g., DESI Legacy Imaging) to see if there are faint optical counterparts. While a full analysis is beyond the scope of this paper, some discussion of the possibilities is needed to contextualize this major finding.

### MINOR Revisions

**P3-m1: Clarification of `fNL` Normalization in Figure 11**
-   **Section/Page:** Appendix C, Figure 11 Caption (p. 25)
-   **Problem:** The caption contains a "Normalization note" explaining that the absolute `σ(fNL)` values in the plot are not on the same scale as the main text forecast. While this note is essential, the situation is still confusing for the reader. The plot shows a baseline of `σ(fNL) = 16.85`, whereas the main text uses `σ(fNL)std = 8.98`.
-   **Required Fix:** In addition to the existing note, add a sentence explaining *why* the normalizations are different. E.g., "This Fisher implementation uses a simplified single-volume power-law model, whereas the primary forecast in §V is based on a full redshift-binned analysis, resulting in different absolute sensitivities. Only relative improvements should be compared." This provides the necessary context for the reader.

**P3-m2: Date of Publication**
-   **Section/Page:** Title page (p. 1)
-   **Problem:** The paper is dated "June 18, 2026". This is presumably a typo.
-   **Required Fix:** Correct the date to the current year of submission.

### NITs

**P3-N1: Typo in Figure 10 Caption**
-   **Section/Page:** Figure 10 Caption (p. 22)
-   **Problem:** The caption text reads "...mask cut becl| < 80° of §IIIH...". The symbol for ecliptic latitude is `b_ecl`. The pipe symbols `|` are used for absolute value. The text has `becl|`.
-   **Required Fix:** Change `becl|` to `|b_ecl|`.

## Summary recommendation
**MAJOR REVISIONS**

### Justification
This paper presents a monumental effort in anomaly detection across multiple large-scale astronomical surveys. The scale of the catalog is unprecedented, and the scientific applications, particularly to cosmology, are well-motivated and carefully executed. The authors' commitment to transparency is exemplary; the paper openly discusses methodological failures, provenance issues, and limitations in a way that is both rare and laudable. The detailed validation protocols and robustness checks significantly increase confidence in the primary results.

However, the paper suffers from a critical flaw regarding reproducibility. The admission that key preprocessing scripts for the Gaia and eROSITA catalogs are unrecoverable is a serious issue that is not compatible with the archival standards of a journal like Physical Review D. For a data-driven result, the path from raw data to final product must be fully specified and executable. This ESSENTIAL issue must be fully resolved before the paper can be considered for publication.

Additionally, several MAJOR points regarding the justification of systematic error bounds in the cosmology forecast and the clarity of key figures need to be addressed to bring the paper up to the required standard of rigor.

Assuming the authors can satisfactorily address the critical reproducibility issues, the resulting paper will be a landmark contribution to the field of astronomical data analysis and its application to cosmology. The work is otherwise of high quality and suitable for publication in PRD after the required revisions are made.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a more rigorous, second-pass review of the paper.

### ESSENTIAL Revisions

**P3-E3: Incomplete and Inconsistent Injection-Recovery Figure**
-   **Section/Page:** §IID (p. 5), §VID(ii) (p. 20), Figure 10 (p. 22)
-   **Problem:** Figure 10, the primary visualization for the crucial injection-recovery validation step, is incomplete. The main text (§IID, Step 5) and the figure caption both claim that three surveys PASS the gate (SDSS, Planck, NEOWISE) and three FAIL (LAMOST, Gaia, eROSITA). However, the plot only shows the curves for four surveys (SDSS, LAMOST, Gaia, eROSITA) and completely omits the two 100%-recovery PASS cases (Planck and NEOWISE). A reader looking only at the plot would conclude that only one survey (SDSS) passes the gate. This is a significant misrepresentation of the validation results.
-   **Required Fix:** The figure must be remade to include the injection-recovery results for all six surveys, as described in the text and caption. The curves or data points for Planck and NEOWISE must be added to the plot so that it faithfully represents the full 3-PASS/3-FAIL outcome.

### MAJOR Revisions

**P3-M4: Contradictory Provenance in Figure 3 Legend**
-   **Section/Page:** Figure 3 (p. 8)
-   **Problem:** The figure caption states that the score distributions are for "cross-transfer for SDSS, native for DESI/LAMOST". This is a direct contradiction. The LAMOST anomaly count used for the plot (44,075) is the *cross-transfer* count from Table I, not the native-retrained count (113,342). The plot therefore shows the cross-transfer distribution for LAMOST, which is the basis for the "training-bias artifact" diagnosis, not the final native-retrained distribution. The legend is factually incorrect and misleads the reader about what is being shown.
-   **Required Fix:** Correct the figure caption to accurately describe the provenance of each curve. It should state: "cross-transfer for SDSS and LAMOST, native for DESI".

### MINOR Revisions

**P3-m3: Incorrect Cross-Reference in Abstract**
-   **Section/Page:** Abstract (p. 1)
-   **Problem:** The abstract states, "the SDSS component is the 77,905-object native continuity slice, sized to the cross-transfer count (§II)". The discussion of the SDSS continuity slice is in §III C, not §II.
-   **Required Fix:** Change the cross-reference from `(§II)` to `(§III C)`.

**P3-m4: Incorrect Cross-Reference for Cross-Transfer Baseline**
-   **Section/Page:** §II D (p. 5)
-   **Problem:** The text states, "The initial cross-transfer scan ... is preserved in Table I and §VIA as the verification baseline". Section VIA is "The LAMOST Training-Bias Lesson" and does not serve as the primary location for the cross-transfer baseline results, which are distributed throughout §III.
-   **Required Fix:** Remove the incorrect reference to `§VIA`. A simple reference to Table I and the survey-specific subsections of §III would be more appropriate.

**P3-m5: Incorrect Cross-Reference for Isolation Forest Validation**
-   **Section/Page:** §VI C (p. 20)
-   **Problem:** The text states, "Isolation Forest cross-validation was applied only to the photometric surveys (Gaia 41% stability, eROSITA 81.5%; §VID (ii))". The details of the Isolation Forest validation are not in §VID (ii), which covers injection recovery. The relevant discussions are in §III E (eROSITA) and §III G (Gaia).
-   **Required Fix:** Change the cross-reference from `§VID (ii)` to `(see §III E and §III G)`.

### NITs

**P3-N2: Typo in Abstract Cross-Reference**
-   **Section/Page:** Abstract (p. 1)
-   **Problem:** The cross-reference `§VIE` is a typo.
-   **Required Fix:** Change `§VIE` to `§VI E`.
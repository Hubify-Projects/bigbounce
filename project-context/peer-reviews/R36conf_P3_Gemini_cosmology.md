# P3 R36conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.101.pdf` md5=2cba9f61 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (5104 chars)
**Wall time**: 152.6s

---

**Referee Report for "Spectrally Unusual Sources at Scale..."**

This paper presents a large-scale, multi-survey anomaly detection catalog using an autoencoder framework. The authors apply their method to 37.3 million sources across seven astronomical archives, producing a final catalog of 378,280 unique anomalies. The work includes a detailed methodological discussion, including a "Path-C rebuild" protocol with native per-survey retraining, extensive validation through cross-validation and injection-recovery tests, and an honest appraisal of failure modes. The paper concludes with preliminary cosmological applications, including constraints on primordial non-Gaussianity (fNL) and a consistency check with matter-bounce predictions for the stochastic gravitational-wave background.

The paper is exceptionally thorough, transparent about its limitations, and methodologically rigorous in its self-assessment. The authors' upfront discussion of provenance issues, the distinction between different novelty metrics, and the careful framing of negative or tentative results (e.g., the fNL constraint) are commendable. The contribution is significant, providing a valuable resource to the community and important methodological lessons for future large-scale anomaly searches.

However, several points require significant clarification and revision before the paper can be considered for publication in Physical Review D. The primary issues relate to the clarity of key quantitative claims and the communication of the catalog's complex, heterogeneous nature.

## Findings

### ESSENTIAL

*   **P3-E1: Abstract-Body Inconsistency on fNL Constraint.**
    *   **Section/Page:** Abstract (p. 1) vs. §V B (p. 16).
    *   **Problem:** The abstract states: "inserting the noisy â into the Fisher-positivity-respecting form... gives a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98]... the central 9.4% improvement is a noise-driven forecast pending higher-S/N follow-up, not a detection." The body (§V B) correctly states that the de-biased estimate shows *no improvement*: "The de-biased amplitude max(0, â² – σ_a²) = 0 returns the single-tracer baseline σ(fNL) = 8.98 exactly (no improvement)". The abstract highlights the biased central value (8.14) and the "9.4% improvement" first, only qualifying it afterward. This is misleading. The primary, robust result is *no detection of improvement*.
    *   **Fix:** The abstract must be rewritten to lead with the primary, de-biased result: that the analysis returns the single-tracer baseline exactly and provides no evidence for multi-tracer improvement at the current signal-to-noise. The biased central forecast (8.14) and the concept of a "noise-driven forecast" should be presented as a secondary, methodological point about the statistics of noisy estimators, not as a headline result. The "9.4% improvement" claim should be removed from the abstract or explicitly framed as a statistical artifact.

### MAJOR

*   **P3-M1: Confusing Presentation of LAMOST Anomaly Counts.**
    *   **Section/Page:** Abstract (p. 1), Table I (p. 7), §III D (p. 10).
    *   **Problem:** The paper presents conflicting narratives about the effect of the LAMOST native retrain. The abstract and body highlight a "21.5x LAMOST S > 5 anomaly-rate reduction after native retraining (44,075 -> 2,054)". However, the final released LAMOST catalog contains 113,342 objects, an *increase* from the 44,075 cross-transfer count. Table I footnote || states the difference in the total catalog size "reflects the LAMOST native retrain (44,075 -> 113,342)", which is arithmetically an increase. This is confusing. The "reduction" is a diagnostic at a fixed threshold, while the "increase" is the result of adopting a different (top-1%) threshold for the final catalog.
    *   **Fix:** The authors must clarify this everywhere it is mentioned.
        1.  In the abstract, explicitly state that the 21.5x reduction is a *diagnostic* of the model's domain adaptation at a fixed S>5 threshold, but that the released LAMOST exploratory tier uses a top-1% cut, resulting in a catalog of 113,342 objects.
        2.  Rewrite Table I footnote || to be unambiguous. For example: "The LAMOST contribution to the Path-C total changes from the cross-transfer count of 44,075 to the native-retrained top-1% slice of 113,342. A like-for-like diagnostic at a fixed S>5 threshold shows a 21.5x rate reduction (to 2,054 anomalies), confirming the cross-transfer was contaminated by a training-bias artifact."

*   **P3-M2: Unquantified Robustness Claims.**
    *   **Section/Page:** §III B (p. 3), §VI C (p. 19).
    *   **Problem:** The paper makes several qualitative claims of robustness where a quantitative bound is required. For example, in §III B, regarding the data leakage from fitting scalers on the full sample, the paper states: "We assume it does not materially reorder the within-survey anomaly ranking". While a follow-up check provides a Jaccard score (0.76), the initial assumption is left ungrounded. Similarly, in the Limitations (§VI C), the paper lists "Unweighted reconstruction error" as a limitation, noting that low-S/N regions contribute noise. It then states "The injection-recovery gates of §VID (ii) bound the practical impact". This connection is not obvious and needs to be quantified.
    *   **Fix:** Replace qualitative assertions with quantitative statements. For the scaler issue, the text should lead with the quantitative check, not the assumption. For the unweighted MSE, the authors should provide a brief, quantitative argument for how a 64% recovery rate on continuum-dips (for SDSS) bounds the impact of noise from low-S/N regions. If this cannot be done, the claim that the gate "bounds the practical impact" should be removed. This applies to all instances of "robust to", "consistent with", "negligible", etc. — provide the number or remove the claim.

*   **P3-M3: Prominence of Provenance and Reproducibility Issues.**
    *   **Section/Page:** Throughout (e.g., §III B, §III E, §III G).
    *   **Problem:** The paper commendably documents several significant provenance and reproducibility issues: data leakage in feature scaling (§III B), an unrecoverable score axis for eROSITA (§III E), and an unrecoverable preprocessing script for Gaia (§III G). While these are noted in the respective sections, their collective impact on the catalog's utility and the methodological lessons learned should be synthesized and given more prominence.
    *   **Fix:** Add a dedicated subsection in the Discussion (§VI) titled "Provenance and Reproducibility Challenges in Large-Scale Analyses". This section should summarize the specific issues encountered (scaler leakage, lost scripts, non-reproducible axes) and articulate the broader lesson: that for a result to be truly reproducible, the entire software toolchain, not just the model weights, must be version-controlled and archived with the same rigor as the data. The current transparent-but-scattered approach should be centralized to drive home this crucial methodological point.

### MINOR

*   **P3-m1: Inconsistent Score Reporting in Figure 8.**
    *   **Section/Page:** Figure 8 caption (p. 17).
    *   **Problem:** The caption states: "the burned-in 'Score' annotations are display values from that script rather than catalog-pipeline outputs; in particular, the panel (a, b) annotations (3.2, 2.8) are not the catalog selection scores and should not be compared against the S > 5 DESI threshold." This implies a degree of sloppiness in the figure generation pipeline. While the documentation is appreciated, for a journal like PRD, figures should reflect the canonical, published data.
    *   **Fix:** Regenerate the figure using the official catalog scores. If this is not possible for some reason, the caption must explain *why* the display scores differ from the catalog scores and provide the actual catalog scores for these three objects directly in the caption text for comparison.

*   **P3-m2: Ambiguous Language in Earlier Draft Reference.**
    *   **Section/Page:** §IV B (p. 14).
    *   **Problem:** The text contains a reference to a previous state of the analysis: "(An earlier draft quoted 38,330 pixels with χ²/dof = 3.76; that artifact's pixel-selection and variance model could not be recovered from the committed analysis tree, and the figure is withdrawn in favor of the reproducible recompute above.)"
    *   **Fix:** This is internal version history and does not belong in a published paper. Remove this parenthetical sentence entirely. The paper should present the final, validated result without reference to prior, flawed versions.

### NIT

*   **P3-N1: Dated Reference.**
    *   **Section/Page:** Abstract (p. 1).
    *   **Problem:** The paper is dated "(Dated: June 2026)".
    *   **Fix:** Update the date to the current submission date.

## Summary recommendation

**MAJOR REVISIONS**

This is a strong, comprehensive, and valuable paper. The scale of the analysis is impressive, and the authors' commitment to transparency regarding the catalog's many complexities and limitations is a model for the field. The paper makes a clear contribution both as a data product and as a methodological case study.

However, the identified issues, particularly the misleading presentation of the fNL constraint in the abstract and the confusing narrative surrounding the LAMOST anomaly counts, must be resolved. The paper must be revised to ensure that all claims are presented with maximum clarity and that the primary, robust conclusions are not obscured by secondary, artifact-driven, or model-dependent details. Once these revisions are made, the paper will be an excellent candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a second, more rigorous review of the paper.

### NEW FINDINGS

### MAJOR

*   **P3-M4: Inconsistent Normalization and Presentation of fNL Forecasts.**
    *   **Section/Page:** §V B (p. 16) vs. Appendix C / Figure 11 (p. 24).
    *   **Problem:** The paper presents two different single-tracer baseline forecasts for primordial non-Gaussianity that are numerically inconsistent, creating a significant potential for reader confusion. The primary forecast in the main text (§V B) uses a baseline of σ(fNL)std = 8.98. However, the shot-noise sensitivity analysis in Appendix C and Figure 11 uses a single-tracer baseline of σ(fNL) = 16.85. While a "Normalization note" in the Figure 11 caption attempts to explain this as a difference between a "redshift-binned Fisher" and a "simplified analytic" implementation, this is insufficient. Presenting two different numbers for the same core physical quantity (the baseline constraining power of DESI QSOs) is confusing and undermines confidence in the forecast. The burden should not be on the reader to reconcile two different internal calculations via a caption footnote.
    *   **Fix:** The authors must reconcile these forecasts.
        1.  The preferred solution is to re-run the simplified analysis in Appendix C so that its baseline matches the canonical 8.98 value from the main text. All numbers in Figure 11 and the accompanying text should be updated accordingly.
        2.  If this is not possible, the main text (§V B) must explicitly address the discrepancy. It should state that a simplified forecast is used for the shot-noise analysis, that its baseline is σ(fNL) = 16.85, and explain *why* this differs by nearly a factor of two from the main forecast's baseline of 8.98, and why only relative improvements from that analysis are considered trustworthy. The current approach of hiding this major numerical discrepancy in an appendix figure caption is not acceptable.

*   **P3-M5: Misleading Visualization of Non-Comparable Anomaly Scores.**
    *   **Section/Page:** Figure 3 (p. 9).
    *   **Problem:** The left panel of Figure 3 plots the anomaly score `S` distributions for DESI DR1 and LAMOST DR10 on the same x-axis. The paper is otherwise commendably clear that the score `S` is standardized per-survey and that "absolute S values are not comparable across independently trained surveys" (§II B). The figure's visualization directly contradicts this crucial methodological principle. By placing them on a shared axis, the figure implicitly and strongly invites a direct comparison of scores (e.g., "a LAMOST anomaly with S=15 is more/less significant than a DESI anomaly with S=15"), which the authors' own methodology forbids.
    *   **Fix:** The figure must be remade to avoid this misleading comparison. The two distributions should be plotted in separate, adjacent panels (e.g., a top and bottom panel) with their own x-axes, even if the axis ranges are identical. The caption should then be updated to reinforce that the scores are on survey-native scales and are not directly comparable.

### MINOR

*   **P3-m3: Incorrect Internal Cross-References.**
    *   **Section/Page:** Abstract (p. 1), §III A (p. 6).
    *   **Problem:** The paper contains several incorrect internal cross-references that point to the wrong sections, hindering navigation and verification of claims.
        1.  The abstract states the "size benchmark is anchored to... [11]; §VI". However, §VI (Discussion) does not contain the benchmark comparison; this comparison is made in the abstract itself and in §VII (Conclusions).
        2.  §III A states "see §VID for the implications of this scope choice". However, §VID is about residual caveats of the rebuild protocol; the implications of the scope choice (i.e., that 98.7% of anomalies are on non-science spectra) are discussed in §III A itself.
    *   **Fix:** The authors must perform a careful pass over all internal references (`\ref`) and ensure they point to the correct section, table, or figure that substantiates the claim being made. The specific incorrect references identified here must be corrected.

*   **P3-m4: Unsupported "Largest Multi-Archive" Claim.**
    *   **Section/Page:** Table I Caption (p. 7).
    *   **Problem:** The caption claims, "The total represents the largest multi-archive anomaly search reported to date." This is a strong claim of novelty. However, the paper's primary benchmark for scale is Liang et al. [11], which is a *single-survey* search. To substantiate the claim of being the largest *multi-archive* search, the authors should compare their work (in terms of number of archives, sources, or both) to the next-largest published multi-archive anomaly search. Without this comparison, the claim is asserted but not demonstrated.
    *   **Fix:** The authors should either add a citation and comparison to the next-largest multi-archive anomaly search to substantiate their claim, or soften the language to something demonstrably true, such as "a large-scale anomaly search across seven astronomical archives."
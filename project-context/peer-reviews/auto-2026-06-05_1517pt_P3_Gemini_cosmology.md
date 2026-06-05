# P3 auto-2026-06-05_1517pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11173 chars)
**Wall time**: 168.9s

---

Here is a referee report for the submitted manuscript.

## Referee Report: "Spectrally Unusual Sources at Scale..."

**Manuscript ID:** P3
**Journal:** Physical Review D

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of 378,280 unique anomalies. The authors apply an autoencoder framework (BIGAE), develop a robust "Path-C" validation protocol based on native per-survey retraining, and explore applications of the resulting catalog, including constraints on primordial non-Gaussianity (`f_NL`) and consistency with matter-bounce cosmology predictions for the nanohertz gravitational-wave background.

The work is impressive in its scale, methodological rigor, and transparency. The authors' detailed treatment of cross-survey transfer artifacts, the development of a native-retraining protocol, and the frank discussion of failures (e.g., the LAMOST training-bias artifact) are commendable and set a high standard for future work in this area. The resulting catalog is a significant contribution.

However, several revisions are required to meet the publication standards of Physical Review D. These range from an essential correction of a key numerical result in the cosmology section to major revisions for clarity in the main summary table.

---

### Detailed Findings

#### ESSENTIAL

*   **P3-E1 | Section V (p. 10) & Abstract (p. 1) | Incorrect `f_NL` improvement calculation.**
    *   **Problem:** The paper states that the empirical bias measurement yields a central forecast `σ(f_NL) = 8.14` compared to a single-tracer baseline of `σ(f_NL)_std = 8.98`, and calls this a "7.9% improvement". A direct calculation of the fractional improvement in the constraint `σ` is `(1 - 8.14 / 8.98) * 100% = 9.35%`. The improvement in Fisher Information (`I ∝ 1/σ²`) is `( (8.98² / 8.14²) - 1 ) * 100% = 21.7%`. The quoted 7.9% figure is not reproducible from the provided `σ` values and appears to be incorrect. This error affects a headline cosmological result in both the abstract and the main text.
    *   **Required Fix:** Recompute the percentage improvement and correct the value in the abstract and Section V.b. Clarify whether the improvement is being quoted for `σ(f_NL)` or for the Fisher information `I(f_NL)`.

#### MAJOR

*   **P3-M1 | Table I (p. 7) | Confusing presentation of canonical vs. diagnostic results.**
    *   **Problem:** The main body of Table I, specifically the `N_anom` column, presents the initial "cross-transfer" anomaly counts. A footnote (`*`) explains that these are superseded by the final "Path-C native-retrained" counts, which are the paper's primary scientific result. The final counts are only summarized in a separate row at the bottom. This structure is confusing and prone to misinterpretation, as a reader might mistakenly take the diagnostic cross-transfer numbers as the final results.
    *   **Required Fix:** Restructure Table I to make the final, canonical Path-C native-retrained counts the primary entries for each survey in the main table body. The initial cross-transfer counts, which serve as a "before/after" diagnostic, should be moved to a separate column labeled "Cross-transfer (diagnostic)" or into the footnotes to avoid confusion.

#### MINOR

*   **P3-m1 | Table I, footnote || (p. 7) | Inappropriate version-history language.**
    *   **Problem:** The footnote contains the phrase: "The earlier 'strict subset' framing is replaced with this exact 284/298 = 95.3% overlap." This reads like an internal comment or a response to a previous review cycle and is not appropriate for the final published text.
    *   **Required Fix:** Rephrase the footnote to remove the version-history language. For example: "The two anomaly detectors show a 95.3% (284/298) overlap on the canonical eROSITA sample, an enrichment of 95.3x over random chance."

*   **P3-m2 | Section III.E (p. 6) & Abstract (p. 1) | Ambiguous description of eROSITA gate status.**
    *   **Problem:** The text describes the eROSITA result as "gate FAIL at 5σ subspace injection, but highest XV-stability of any Path-C survey". The abstract similarly lists it under "FAIL-with-diagnostic". While the additional context is useful, the primary result is that it failed the pre-defined injection-recovery gate. The current phrasing could be misinterpreted as excusing the failure.
    *   **Required Fix:** Clarify the language. State clearly that the survey failed the injection-recovery gate criterion. The high cross-validation stability can then be presented as an important diagnostic result that may suggest the injection test was not optimally suited for this particular dataset, but it does not override the gate result.

*   **P3-m3 | Section IV.A (p. 9) | Novelty fraction requires clearer qualification.**
    *   **Problem:** The abstract states the genuine novelty fraction is "~17.8% (single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested)". This is a very precise statement. The main text in Section IV.A correctly derives this from the DESI top-1,000 sample. However, given that this is a key "novelty" claim for the entire 378,280-source catalog, the fact that it is an extrapolation from a specific, high-score subset of one survey should be emphasized more strongly.
    *   **Required Fix:** In the abstract and conclusions, slightly rephrase to make it explicitly clear that the 17.8% figure is derived from the *top-1,000 DESI anomalies* and serves as the best current estimate of the genuine novelty rate, which may differ for other surveys or at lower anomaly scores.

#### NIT (Nitpicks)

*   **P3-N1 | Abstract (p. 1) | Abstract is very dense.**
    *   **Problem:** The abstract is packed with a large number of quantitative results. While comprehensive, its density makes it difficult to parse quickly.
    *   **Required Fix:** Consider minor streamlining for readability. This is a suggestion, not a requirement. For example, some of the detailed gate pass/fail percentages could be moved to the main text.

*   **P3-N2 | Table III (p. 8) | Inconsistent score scales.**
    *   **Problem:** Table III reports two scores for eROSITA sources, `S_BigAE` and `S_IF,raw`, which have vastly different scales (`~1` vs. `~10^4`). The caption explains this, but it is visually jarring and makes comparison difficult.
    *   **Required Fix:** Consider reporting a standardized (e.g., z-scored or percentile-ranked) version of the `S_IF` score to place it on a more comparable footing with `S_BigAE`.

---

## Summary recommendation

**MAJOR REVISIONS**

This is a potentially groundbreaking paper that presents a valuable, large-scale anomaly catalog and demonstrates rigorous validation and quality control. The methodological lessons, particularly regarding the pitfalls of transfer learning without native retraining, are a significant contribution in their own right. The cosmological applications are timely and interesting.

However, the manuscript requires major revisions before it can be accepted. The essential correction of the `f_NL` improvement calculation is non-negotiable for a journal with PRD's standards of numerical precision. Furthermore, the main summary table (Table I) must be reorganized for clarity to ensure the paper's primary results are presented unambiguously. Once these and the other minor points are addressed, the paper will represent a superb and impactful contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating findings from the second, more detailed review.

================================================================
Here is a referee report for the submitted manuscript.

## Referee Report: "Spectrally Unusual Sources at Scale..."

**Manuscript ID:** P3
**Journal:** Physical Review D

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of 378,280 unique anomalies. The authors apply an autoencoder framework (BIGAE), develop a robust "Path-C" validation protocol based on native per-survey retraining, and explore applications of the resulting catalog, including constraints on primordial non-Gaussianity (`f_NL`) and consistency with matter-bounce cosmology predictions for the nanohertz gravitational-wave background.

The work is impressive in its scale, methodological rigor, and transparency. The authors' detailed treatment of cross-survey transfer artifacts, the development of a native-retraining protocol, and the frank discussion of failures (e.g., the LAMOST training-bias artifact) are commendable and set a high standard for future work in this area. The resulting catalog is a significant contribution.

However, several revisions are required to meet the publication standards of Physical Review D. These range from essential corrections of key numerical results to major revisions for clarity and consistency.

---

### Detailed Findings

#### ESSENTIAL

*   **P3-E1 | Section V (p. 10) & Abstract (p. 1) | Incorrect `f_NL` improvement calculation.**
    *   **Problem:** The paper states that the empirical bias measurement yields a central forecast `σ(f_NL) = 8.14` compared to a single-tracer baseline of `σ(f_NL)_std = 8.98`, and calls this a "7.9% improvement". A direct calculation of the fractional improvement in the constraint `σ` is `(1 - 8.14 / 8.98) * 100% = 9.35%`. The improvement in Fisher Information (`I ∝ 1/σ²`) is `( (8.98² / 8.14²) - 1 ) * 100% = 21.7%`. The quoted 7.9% figure is not reproducible from the provided `σ` values and appears to be incorrect. This error affects a headline cosmological result in both the abstract and the main text.
    *   **Required Fix:** Recompute the percentage improvement and correct the value in the abstract and Section V.b. Clarify whether the improvement is being quoted for `σ(f_NL)` or for the Fisher information `I(f_NL)`.

*   **P3-E2 | Section IV.A (p. 9) & Table I (p. 7) | Inconsistent aggregate SIMBAD-unmatched fraction.**
    *   **Problem:** The paper claims an aggregate SIMBAD-unmatched fraction of 58.8% for the cross-transfer sample (in Table I and Section IV.A). However, a weighted average of the per-survey unmatched percentages and counts provided in Table I yields a much higher value of ~89.8%. The origin of the 58.8% figure is not documented and appears inconsistent with the provided data.
    *   **Required Fix:** Recompute and correct the aggregate SIMBAD-unmatched fraction. If the calculation is non-trivial (e.g., uses a different sample than implied), the methodology must be explicitly described.

#### MAJOR

*   **P3-M1 | Table I (p. 7) | Confusing presentation of canonical vs. diagnostic results.**
    *   **Problem:** The main body of Table I, specifically the `N_anom` column, presents the initial "cross-transfer" anomaly counts. A footnote (`*`) explains that these are superseded by the final "Path-C native-retrained" counts, which are the paper's primary scientific result. The final counts are only summarized in a separate row at the bottom. This structure is confusing and prone to misinterpretation, as a reader might mistakenly take the diagnostic cross-transfer numbers as the final results.
    *   **Required Fix:** Restructure Table I to make the final, canonical Path-C native-retrained counts the primary entries for each survey in the main table body. The initial cross-transfer counts, which serve as a "before/after" diagnostic, should be moved to a separate column labeled "Cross-transfer (diagnostic)" or into the footnotes to avoid confusion.

*   **P3-M2 | Conclusion 6 (p. 14) | Stale number for OOD Jaccard stability.**
    *   **Problem:** Conclusion 6 states: "OOD control-vs-control 0.874 (PASS)". However, the main text in Section VI.D.i (p. 12) gives a different value: "An independent 103,000-spectrum OOD holdout ... confirms production-vs-5-seed-control Jaccard J_prod×ctrl = 0.732 (≥ 0.50, PASS)". These numbers are inconsistent.
    *   **Required Fix:** Correct the value in the conclusion to match the one derived and discussed in the main body of the paper (0.732).

#### MINOR

*   **P3-m1 | Table I, footnote || (p. 7) | Inappropriate version-history language.**
    *   **Problem:** The footnote contains the phrase: "The earlier 'strict subset' framing is replaced with this exact 284/298 = 95.3% overlap." This reads like an internal comment or a response to a previous review cycle and is not appropriate for the final published text.
    *   **Required Fix:** Rephrase the footnote to remove the version-history language. For example: "The two anomaly detectors show a 95.3% (284/298) overlap on the canonical eROSITA sample, an enrichment of 95.3x over random chance."

*   **P3-m2 | Section III.E (p. 6) & Abstract (p. 1) | Ambiguous description of eROSITA gate status.**
    *   **Problem:** The text describes the eROSITA result as "gate FAIL at 5σ subspace injection, but highest XV-stability of any Path-C survey". The abstract similarly lists it under "FAIL-with-diagnostic". While the additional context is useful, the primary result is that it failed the pre-defined injection-recovery gate. The current phrasing could be misinterpreted as excusing the failure.
    *   **Required Fix:** Clarify the language. State clearly that the survey failed the injection-recovery gate criterion. The high cross-validation stability can then be presented as an important diagnostic result that may suggest the injection test was not optimally suited for this particular dataset, but it does not override the gate result.

*   **P3-m3 | Section IV.A (p. 9) | Novelty fraction requires clearer qualification.**
    *   **Problem:** The abstract states the genuine novelty fraction is "~17.8% (single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested)". This is a very precise statement. The main text in Section IV.A correctly derives this from the DESI top-1,000 sample. However, given that this is a key "novelty" claim for the entire 378,280-source catalog, the fact that it is an extrapolation from a specific, high-score subset of one survey should be emphasized more strongly.
    *   **Required Fix:** In the abstract and conclusions, slightly rephrase to make it explicitly clear that the 17.8% figure is derived from the *top-1,000 DESI anomalies* and serves as the best current estimate of the genuine novelty rate, which may differ for other surveys or at lower anomaly scores.

*   **P3-m4 | Figure 8 (p. 16) | Undocumented single-tracer baseline value.**
    *   **Problem:** The caption of Figure 8, which illustrates the shot-noise sensitivity of the multi-tracer `f_NL` forecast, refers to a "single-tracer baseline (σ(f_NL) = 16.85)". This value is not mentioned or derived anywhere else in the paper. The main text consistently uses a different single-tracer baseline of `σ(f_NL)_std = 8.98` (from DESI QSOs). This creates confusion about which baseline is being used for comparison.
    *   **Required Fix:** Clarify the origin of the `σ(f_NL) = 16.85` value. If it corresponds to a different experimental setup (e.g., a SPHEREx-like forecast without multi-tracer), this should be explicitly stated in the caption or the relevant appendix.

*   **P3-m5 | Section V.A (p. 11) | Ambiguous Bayes factor interpretation.**
    *   **Problem:** The paper calculates `B_MB/SMBHB = 7.14x10³` and correctly states this is "decisive" on the Jeffreys' scale. However, this is a model comparison between two specific alternatives (Matter Bounce vs. SMBHB). It does not rule out other models (e.g., cosmic strings) or the null hypothesis (no GWB). The strong language could be misinterpreted as a definitive preference for the matter-bounce model over all other possibilities.
    *   **Required Fix:** Add a clarifying sentence to state that this Bayes factor represents a strong preference for the matter-bounce GWB template *over the SMBHB template*, but does not constitute a detection of the bounce model itself or rule out other potential GWB sources.

#### NIT (Nitpicks)

*   **P3-N1 | Abstract (p. 1) | Abstract is very dense.**
    *   **Problem:** The abstract is packed with a large number of quantitative results. While comprehensive, its density makes it difficult to parse quickly.
    *   **Required Fix:** Consider minor streamlining for readability. This is a suggestion, not a requirement. For example, some of the detailed gate pass/fail percentages could be moved to the main text.

*   **P3-N2 | Table III (p. 8) | Inconsistent score scales.**
    *   **Problem:** Table III reports two scores for eROSITA sources, `S_BigAE` and `S_IF,raw`, which have vastly different scales (`~1` vs. `~10^4`). The caption explains this, but it is visually jarring and makes comparison difficult.
    *   **Required Fix:** Consider reporting a standardized (e.g., z-scored or percentile-ranked) version of the `S_IF` score to place it on a more comparable footing with `S_BigAE`.

*   **P3-N3 | General | Overuse of acronyms and jargon.**
    *   **Problem:** The paper uses a large number of acronyms (BIGAE, OOD, XV, MSE, etc.) and internal jargon ("Path-C", "gate PASS/FAIL"). While many are standard, the density can make the paper difficult for non-specialists to follow. The term "gate" is particularly opaque without reading the methods section carefully.
    *   **Required Fix:** Consider defining key terms more prominently or adding a small glossary. For example, briefly define "gate" in the abstract, e.g., "pre-defined injection-recovery quality gates". This is a suggestion for improving readability.

---

## Summary recommendation

**MAJOR REVISIONS**

This is a potentially groundbreaking paper that presents a valuable, large-scale anomaly catalog and demonstrates rigorous validation and quality control. The methodological lessons, particularly regarding the pitfalls of transfer learning without native retraining, are a significant contribution in their own right. The cosmological applications are timely and interesting.

However, the manuscript requires major revisions before it can be accepted. The essential corrections of the `f_NL` improvement calculation and the aggregate SIMBAD-unmatched fraction are non-negotiable for a journal with PRD's standards of numerical precision. Furthermore, the main summary table (Table I) must be reorganized for clarity, and a stale number in the conclusions must be corrected. Once these and the other minor points are addressed, the paper will represent a superb and impactful contribution to the literature.
================================================================
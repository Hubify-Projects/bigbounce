# P3 R54 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R54_P3/paper3_draft.pdf` md5=84563f72 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (18704 chars)
**Wall time**: 149.1s

---

Here is the complete referee report.

## Referee Report for "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalies. The authors apply a consistent autoencoder framework (BIGAE), develop a "Path-C" native-retraining protocol to address cross-survey domain shift issues, and perform initial cross-survey validation and cosmological application studies. The scale of the catalog is impressive, and the methodological lessons, particularly regarding training-set bias (LAMOST) and domain-shift artifacts (SDSS), are valuable for the field.

However, the paper requires significant revisions to meet the standards of Physical Review D. The abstract overstates several key results, particularly the cosmological constraints, which are shown in the body to be null detections or noise-dominated forecasts. The presentation mixes verification-level results with primary science results, requiring careful disentanglement. Several sections lack the quantitative rigor and self-contained explanations necessary for a PRD publication. The following detailed findings must be addressed.

---
### Detailed Findings

#### ESSENTIAL

**P3-E1: Abstract vs. Body Mismatch on Cosmological Results**
-   **Location:** Abstract, p. 1
-   **Problem:** The abstract presents the `f_NL` and NANOGrav results as significant findings, which is misleading.
    1.  **`f_NL`:** The abstract states a "central forecast (fNL) = 8.14 with 1σ envelope [3.92, 8.98]" and a "9.4% improvement". However, the body (§V A, p. 18) correctly explains that this is a "noise-driven forecast" and that the de-biased estimate "returns the single-tracer baseline σ(fNL)std = 8.98 exactly (no multi-tracer improvement at current S/N)". The abstract presents the optimistic, biased forecast as the primary result.
    2.  **NANOGrav:** The abstract reports a "decisive" Bayes factor of 7.14×10³ against the SMBHB model. The body (§V A, p. 19 and §F, p. 21) correctly adds the critical caveat that "environmentally modified SMBHB models can produce γ ~ 2.5–3", which would be consistent with their measurement and invalidate the "decisive" claim against the entire physical class of SMBHB models. The abstract omits this essential context.
-   **Required Fix:** The abstract must be rewritten to accurately reflect the null results from the body.
    1.  For `f_NL`, state clearly that the analysis is consistent with no multi-tracer improvement and that the current constraint is the single-tracer baseline. The "improvement" is a statistical artifact and should not be in the abstract.
    2.  For NANOGrav, the Bayes factor must be qualified as being against an "idealized circular-orbit" SMBHB reference model, and the abstract must mention that environmentally modified models are not ruled out. The word "decisive" should be qualified or removed.

**P3-E2: Unjustified "Catalog-Grade" vs. "Exploratory" Distinction**
-   **Location:** Abstract, p. 1; §IID, p. 5; §VII, p. 23
-   **Problem:** The paper introduces a "recommended catalog-grade tier" (269,317 entries) by excluding the LAMOST tier, which is labeled "exploratory". However, it also states that Gaia and eROSITA "remain exploratory components" and carry "per-object exploratory validity flags". This creates a contradiction. If Gaia and eROSITA are exploratory, they should also be excluded from the "catalog-grade" count, or the definition of "catalog-grade" is meaningless.
-   **Required Fix:** The authors must define "catalog-grade" rigorously and apply it consistently.
    -   Option A: Define "catalog-grade" as passing all validation gates (Jaccard, injection-recovery). In this case, only DESI, SDSS, Planck, and NEOWISE qualify. The "catalog-grade" count would be much smaller. Gaia, eROSITA, and LAMOST would all be "exploratory".
    -   Option B: Abandon the "catalog-grade" terminology. Present the full catalog of 378,280 anomalies and clearly state in the abstract and body which survey components are considered robustly validated versus exploratory, based on the gate results. This seems more honest. The current headline count of 269,317 is an arbitrary intermediate step.

**P3-E3: Inconsistent Anomaly Score Definitions and Cross-Survey Comparability**
-   **Location:** §II B b, p. 4; Figure 3 Caption, p. 10
-   **Problem:** The paper states multiple times that absolute `S` values are not comparable across surveys because they are standardized on per-survey validation pools. However, the initial SDSS and LAMOST analyses are performed using the DESI-trained model and DESI's (μ_val, σ_val), placing them on the DESI score scale. Figure 3 (left panel) then plots DESI and LAMOST scores on the same axis, inviting a direct comparison that the text forbids. The caption's warning is insufficient. Furthermore, the paper uses at least four different thresholding schemes (absolute S>5, fixed-size continuity slice, top-percentile, fixed-count cap), making rate comparisons highly problematic.
-   **Required Fix:**
    1.  The text must be more forceful about the non-comparability of scores. The phrase "should be read per-survey, not on a shared scale" is too weak.
    2.  Figure 3 (left panel) must be changed. Either split it into two separate plots or use a different visualization (e.g., rank-order plots) that does not imply a shared scale.
    3.  The abstract and introduction must state upfront that due to different training and thresholding, the reported anomaly "rates" are survey-specific bookkeeping figures, not measurements of a universal astrophysical anomaly frequency. The 1.01% rate for the "Path-C unique" total in Table I is particularly meaningless as it aggregates these disparate definitions.

#### MAJOR

**P3-M1: Insufficient Detail on `f_NL` Fisher Forecast**
-   **Location:** §V A, p. 18; Appendix C, p. 23
-   **Problem:** The `f_NL` forecast is a major cosmological application claim, but its derivation is opaque. The paper cites a "5-σ refit of §VID caveat (i)" and provides `F_0` and `c` values without showing the underlying Fisher matrix, tracer properties (bias, dn/dz), or survey specifications (area, k_max) used. A reader cannot reproduce the calculation or verify its assumptions. The jump from the empirical `a_jk` to the forecast `σ(f_NL)` is not self-contained. The statement "The conditional SPHEREx multi-tracer forecast yields 2.6–5σ detection significance" is an uncomputed claim imported from another paper's methodology, not a result of this work's data.
-   **Required Fix:**
    1.  Provide the full Fisher matrix formalism used, either in the main text or an appendix.
    2.  Tabulate the assumed tracer properties (b(z), n(z)) for both the standard DESI QSOs and the anomaly sample.
    3.  Clearly state all cosmological and survey parameters assumed (e.g., fiducial cosmology, survey area, k_min, k_max).
    4.  The SPHEREx forecast must be rephrased to make it clear this is not a result derived from the catalog presented in this paper, but an illustration of potential future use.

**P3-M2: Overstated Novelty and Confusing SIMBAD vs. Archival Cross-Match**
-   **Location:** §IV A, p. 13; Figure 6, p. 14
-   **Problem:** The paper correctly distinguishes between the "SIMBAD-unmatched fraction" (a database coverage metric) and the "genuine novelty fraction" (17.8%). However, this crucial distinction is not made in the abstract. The abstract reports the 17.8% figure but the body and figures (e.g., Fig 6) are dominated by the much larger, less meaningful SIMBAD-unmatched fractions. This will cause readers to misinterpret the catalog's novelty. The 58.8% "aggregate" SIMBAD-unmatched fraction is a confusingly constructed average that should be removed.
-   **Required Fix:**
    1.  The abstract must explicitly state that the "genuine novelty fraction" is ~17.8% *for the DESI top-1000 stratum* and that this is a deep archival cross-match result, contrasting it with the much higher but less meaningful SIMBAD-unmatched fractions.
    2.  De-emphasize the SIMBAD-unmatched fractions throughout the text. They are a secondary diagnostic, not a primary result.
    3.  Remove the 58.8% aggregate from Figure 6 and the text. It is not a well-defined or useful statistic. The per-survey bars are sufficient to make the point about heterogeneous database coverage.

**P3-M3: Unresolved eROSITA Score Axis Provenance**
-   **Location:** Abstract, p. 1; §IIIE, p. 11; Table IV, p. 12
-   **Problem:** The paper states the eROSITA tier is a "membership list only" because the per-object score axis is "non-reproducible". It documents a thorough but failed attempt to recover the score axis. This is a major methodological failure for that survey component. Releasing a ranked list without a reproducible ranking criterion is problematic. The abstract mentions this only in passing.
-   **Required Fix:** This limitation needs to be stated more prominently. The abstract must clearly state that the eROSITA component is a fixed, non-re-rankable membership list. The "exploratory" flag is insufficient to convey the severity of this issue. The authors should consider whether a non-reproducible ranked list meets the bar for inclusion in a scientific catalog at all, even an exploratory one. At minimum, the primary catalog files must carry a very prominent warning flag for all eROSITA sources.

**P3-M4: Effect Size Missing for Key Statistical Test**
-   **Location:** §III A, p. 8 (DESI anomaly rates by SPECTYPE)
-   **Problem:** The paper states that "galaxies are flagged as anomalous at ~20 times the rate of QSOs (0.75% vs. 0.037%)". A Wilson 95% binomial CI is provided, establishing statistical significance. However, no effect size is given. Is this rate difference driven by a small number of objects, or is it a population-wide effect? This is a key astrophysical finding derived from the catalog and requires more rigorous support.
-   **Required Fix:** Calculate and report an effect size for this rate comparison (e.g., a risk ratio or odds ratio with confidence intervals) to quantify the practical significance of the 20x rate difference.

#### MINOR

**P3-m1: Ambiguous Dating**
-   **Location:** Title block, p. 1
-   **Problem:** The paper is dated "June 19, 2026". This is presumably a typo.
-   **Required Fix:** Correct the date to the actual submission date.

**P3-m2: Inconsistent Use of "Quarantined"**
-   **Location:** Abstract, p. 1; §IID, p. 5; Appendix F, p. 26
-   **Problem:** The abstract states ACT DR6 is "quarantined as a cross-transfer artifact". The body refers to it as "formally quarantined". This terminology is non-standard. It seems to mean "excluded from the final analysis due to failing validation checks".
-   **Required Fix:** Replace "quarantined" with a more standard and explicit phrase like "excluded" or "failed validation and was excluded". Use this phrasing consistently.

**P3-m3: Unclear Provenance of Gaia Preprocessing**
-   **Location:** §II B α, p. 3; §G, p. 12
-   **Problem:** The paper states "the exact 20-feature production script for the published 50K-source run was not recovered" and that the specification is "lineage-inferred". This lack of direct provenance is a weakness.
-   **Required Fix:** While the script may be lost, the authors should, if possible, list the 20 features used in an appendix to provide maximum possible transparency. The current description is too vague. The statement in the Data Availability section (§VII, p. 23) that the "exact column list is enumerated in the manifest" is good, but this information should also be in the paper itself for self-containment.

**P3-m4: Confusing Footnotes in Table I**
-   **Location:** Table I, p. 7
-   **Problem:** The footnotes in Table I are extremely dense and contain critical information about threshold definitions that should be in the main text or the table caption. For example, the details of the SDSS "fixed-size continuity slice" vs. the "top-1% proper" are essential for understanding the results and are buried in footnote ♡.
-   **Required Fix:** Move the essential methodological details from the footnotes into the main text (§II B b) and the table caption. Footnotes should be reserved for minor clarifications, not core definitions.

**P3-m5: Unnecessary Acronym**
-   **Location:** Throughout
-   **Problem:** The paper uses "BIGAE (BigBounce Integrated Galaxy Autoencoder)". The "BigBounce" part seems to be branding without a clear connection to the autoencoder's function, which is general-purpose. The name is distracting.
-   **Required Fix:** Recommend renaming the framework to something more descriptive and neutral, or simply referring to it as "the autoencoder framework" throughout. If the name is kept, the motivation for "BigBounce" should be explained.

**P3-m6: Citation Formatting**
-   **Location:** Bibliography, pp. 28-29
-   **Problem:** Several citations are incomplete or use inconsistent formatting. For example, [1] and [12] are listed as "accepted" or have future dates ("2025", "2026"), which is not appropriate for a final submission. They should be listed as arXiv preprints if they are not yet published.
-   **Required Fix:** Update all citations to their final published form or, if unpublished, use a consistent arXiv format with the submission version. Remove future publication dates.

#### NIT

**P3-N1: Awkward Phrasing**
-   **Location:** Abstract, p. 1
-   **Problem:** "the size benchmark is anchored to the largest published single-survey anomaly catalog" is awkward.
-   **Required Fix:** Rephrase to something like: "processing more sources than the largest previously published single-survey anomaly catalog [11]".

**P3-N2: Redundant Figure Label**
-   **Location:** Figure 1, p. 3
-   **Problem:** The figure title burned into the plot ("DESI DR1 Latent Space...") is redundant with the figure caption.
-   **Required Fix:** Remove the title from the plot image itself.

**P3-N3: Typo in Figure 10 Caption**
-   **Location:** Figure 10 Caption, p. 22
-   **Problem:** "becl| > {85°, 82°, 80.5°}" and "becl < 80°". The use of `|becl|` (absolute latitude) seems inconsistent with the single inequality.
-   **Required Fix:** Clarify the mask definition. Is it `|becl| < 80°` or `becl < 80°`? The text in §IIIH says `|becl| < 80°`. The caption for the injection test seems to imply sources are planted *outside* this region and the test is whether they are correctly excluded. Please clarify the exact procedure. The current text is confusing.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper presents a substantial and valuable dataset, and the methodological explorations are a solid contribution to the field of astronomical data mining. The scale of the work is commendable. However, the manuscript in its current form is not acceptable for publication in Physical Review D. The abstract significantly misrepresents the main cosmological results, which are the most relevant part for the PRD audience. The distinction between robust and exploratory parts of the catalog is inconsistent, and the presentation of key metrics (anomaly scores, novelty fractions) is confusing. The paper must be substantially rewritten to present the results with the rigor, clarity, and conservative framing expected of a high-impact physics journal. Once the essential and major issues listed above are thoroughly addressed, the paper will likely be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the complete, updated referee report, incorporating findings from the "fresh eyes" review.

================================================================
Here is the complete referee report.

## Referee Report for "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalies. The authors apply a consistent autoencoder framework (BIGAE), develop a "Path-C" native-retraining protocol to address cross-survey domain shift issues, and perform initial cross-survey validation and cosmological application studies. The scale of the catalog is impressive, and the methodological lessons, particularly regarding training-set bias (LAMOST) and domain-shift artifacts (SDSS), are valuable for the field.

However, the paper requires significant revisions to meet the standards of Physical Review D. The abstract overstates several key results, particularly the cosmological constraints, which are shown in the body to be null detections or noise-dominated forecasts. The presentation mixes verification-level results with primary science results, requiring careful disentanglement. Several sections lack the quantitative rigor and self-contained explanations necessary for a PRD publication. The following detailed findings must be addressed.

---
### Detailed Findings

#### ESSENTIAL

**P3-E1: Abstract vs. Body Mismatch on Cosmological Results**
-   **Location:** Abstract, p. 1
-   **Problem:** The abstract presents the `f_NL` and NANOGrav results as significant findings, which is misleading.
    1.  **`f_NL`:** The abstract states a "central forecast (fNL) = 8.14 with 1σ envelope [3.92, 8.98]" and a "9.4% improvement". However, the body (§V A, p. 18) correctly explains that this is a "noise-driven forecast" and that the de-biased estimate "returns the single-tracer baseline σ(fNL)std = 8.98 exactly (no multi-tracer improvement at current S/N)". The abstract presents the optimistic, biased forecast as the primary result.
    2.  **NANOGrav:** The abstract reports a "decisive" Bayes factor of 7.14×10³ against the SMBHB model. The body (§V A, p. 19 and §F, p. 21) correctly adds the critical caveat that "environmentally modified SMBHB models can produce γ ~ 2.5–3", which would be consistent with their measurement and invalidate the "decisive" claim against the entire physical class of SMBHB models. The abstract omits this essential context.
-   **Required Fix:** The abstract must be rewritten to accurately reflect the null results from the body.
    1.  For `f_NL`, state clearly that the analysis is consistent with no multi-tracer improvement and that the current constraint is the single-tracer baseline. The "improvement" is a statistical artifact and should not be in the abstract.
    2.  For NANOGrav, the Bayes factor must be qualified as being against an "idealized circular-orbit" SMBHB reference model, and the abstract must mention that environmentally modified models are not ruled out. The word "decisive" should be qualified or removed.

**P3-E2: Unjustified "Catalog-Grade" vs. "Exploratory" Distinction**
-   **Location:** Abstract, p. 1; §IID, p. 5; §VII, p. 23
-   **Problem:** The paper introduces a "recommended catalog-grade tier" (269,317 entries) by excluding the LAMOST tier, which is labeled "exploratory". However, it also states that Gaia and eROSITA "remain exploratory components" and carry "per-object exploratory validity flags". This creates a contradiction. If Gaia and eROSITA are exploratory, they should also be excluded from the "catalog-grade" count, or the definition of "catalog-grade" is meaningless.
-   **Required Fix:** The authors must define "catalog-grade" rigorously and apply it consistently.
    -   Option A: Define "catalog-grade" as passing all validation gates (Jaccard, injection-recovery). In this case, only DESI, SDSS, Planck, and NEOWISE qualify. The "catalog-grade" count would be much smaller. Gaia, eROSITA, and LAMOST would all be "exploratory".
    -   Option B: Abandon the "catalog-grade" terminology. Present the full catalog of 378,280 anomalies and clearly state in the abstract and body which survey components are considered robustly validated versus exploratory, based on the gate results. This seems more honest. The current headline count of 269,317 is an arbitrary intermediate step.

**P3-E3: Inconsistent Anomaly Score Definitions and Cross-Survey Comparability**
-   **Location:** §II B b, p. 4; Figure 3 Caption, p. 10
-   **Problem:** The paper states multiple times that absolute `S` values are not comparable across surveys because they are standardized on per-survey validation pools. However, the initial SDSS and LAMOST analyses are performed using the DESI-trained model and DESI's (μ_val, σ_val), placing them on the DESI score scale. Figure 3 (left panel) then plots DESI and LAMOST scores on the same axis, inviting a direct comparison that the text forbids. The caption's warning is insufficient. Furthermore, the paper uses at least four different thresholding schemes (absolute S>5, fixed-size continuity slice, top-percentile, fixed-count cap), making rate comparisons highly problematic.
-   **Required Fix:**
    1.  The text must be more forceful about the non-comparability of scores. The phrase "should be read per-survey, not on a shared scale" is too weak.
    2.  Figure 3 (left panel) must be changed. Either split it into two separate plots or use a different visualization (e.g., rank-order plots) that does not imply a shared scale.
    3.  The abstract and introduction must state upfront that due to different training and thresholding, the reported anomaly "rates" are survey-specific bookkeeping figures, not measurements of a universal astrophysical anomaly frequency. The 1.01% rate for the "Path-C unique" total in Table I is particularly meaningless as it aggregates these disparate definitions.

#### MAJOR

**P3-M1: Insufficient Detail on `f_NL` Fisher Forecast**
-   **Location:** §V A, p. 18; Appendix C, p. 23
-   **Problem:** The `f_NL` forecast is a major cosmological application claim, but its derivation is opaque. The paper cites a "5-σ refit of §VID caveat (i)" and provides `F_0` and `c` values without showing the underlying Fisher matrix, tracer properties (bias, dn/dz), or survey specifications (area, k_max) used. A reader cannot reproduce the calculation or verify its assumptions. The jump from the empirical `a_jk` to the forecast `σ(f_NL)` is not self-contained. The statement "The conditional SPHEREx multi-tracer forecast yields 2.6–5σ detection significance" is an uncomputed claim imported from another paper's methodology, not a result of this work's data.
-   **Required Fix:**
    1.  Provide the full Fisher matrix formalism used, either in the main text or an appendix.
    2.  Tabulate the assumed tracer properties (b(z), n(z)) for both the standard DESI QSOs and the anomaly sample.
    3.  Clearly state all cosmological and survey parameters assumed (e.g., fiducial cosmology, survey area, k_min, k_max).
    4.  The SPHEREx forecast must be rephrased to make it clear this is not a result derived from the catalog presented in this paper, but an illustration of potential future use.

**P3-M2: Overstated Novelty and Confusing SIMBAD vs. Archival Cross-Match**
-   **Location:** §IV A, p. 13; Figure 6, p. 14
-   **Problem:** The paper correctly distinguishes between the "SIMBAD-unmatched fraction" (a database coverage metric) and the "genuine novelty fraction" (17.8%). However, this crucial distinction is not made in the abstract. The abstract reports the 17.8% figure but the body and figures (e.g., Fig 6) are dominated by the much larger, less meaningful SIMBAD-unmatched fractions. This will cause readers to misinterpret the catalog's novelty. The 58.8% "aggregate" SIMBAD-unmatched fraction is a confusingly constructed average that should be removed.
-   **Required Fix:**
    1.  The abstract must explicitly state that the "genuine novelty fraction" is ~17.8% *for the DESI top-1000 stratum* and that this is a deep archival cross-match result, contrasting it with the much higher but less meaningful SIMBAD-unmatched fractions.
    2.  De-emphasize the SIMBAD-unmatched fractions throughout the text. They are a secondary diagnostic, not a primary result.
    3.  Remove the 58.8% aggregate from Figure 6 and the text. It is not a well-defined or useful statistic. The per-survey bars are sufficient to make the point about heterogeneous database coverage.

**P3-M3: Unresolved eROSITA Score Axis Provenance**
-   **Location:** Abstract, p. 1; §IIIE, p. 11; Table IV, p. 12
-   **Problem:** The paper states the eROSITA tier is a "membership list only" because the per-object score axis is "non-reproducible". It documents a thorough but failed attempt to recover the score axis. This is a major methodological failure for that survey component. Releasing a ranked list without a reproducible ranking criterion is problematic. The abstract mentions this only in passing.
-   **Required Fix:** This limitation needs to be stated more prominently. The abstract must clearly state that the eROSITA component is a fixed, non-re-rankable membership list. The "exploratory" flag is insufficient to convey the severity of this issue. The authors should consider whether a non-reproducible ranked list meets the bar for inclusion in a scientific catalog at all, even an exploratory one. At minimum, the primary catalog files must carry a very prominent warning flag for all eROSITA sources.

**P3-M4: Effect Size Missing for Key Statistical Test**
-   **Location:** §III A, p. 8 (DESI anomaly rates by SPECTYPE)
-   **Problem:** The paper states that "galaxies are flagged as anomalous at ~20 times the rate of QSOs (0.75% vs. 0.037%)". A Wilson 95% binomial CI is provided, establishing statistical significance. However, no effect size is given. Is this rate difference driven by a small number of objects, or is it a population-wide effect? This is a key astrophysical finding derived from the catalog and requires more rigorous support.
-   **Required Fix:** Calculate and report an effect size for this rate comparison (e.g., a risk ratio or odds ratio with confidence intervals) to quantify the practical significance of the 20x rate difference.

**P3-M5: Arbitrary SDSS Threshold Definition**
-   **Location:** §II B b, p. 4; Table I, p. 7
-   **Problem:** The headline SDSS anomaly count (77,905) is based on a "fixed-size continuity slice". The size of this slice is justified as being chosen "to equal the cross-transfer count". This is not a principled, data-driven, or physically motivated threshold. It is an arbitrary choice designed to preserve a number from a preliminary, flawed analysis. This undermines the scientific interpretation of the SDSS anomaly tier, as its size and composition are not based on any intrinsic property of the data.
-   **Required Fix:** The authors must either provide a strong scientific justification for using this "continuity" threshold or, preferably, replace it with a standard, interpretable threshold for the headline result (e.g., the top-1% cut of 19,253 objects, which is already computed and mentioned in footnotes). Using an arbitrary threshold for a primary catalog component is not acceptable.

**P3-M6: Paper Not Self-Contained**
-   **Location:** §II B α, p. 3
-   **Problem:** The paper describes a "bounded robustness check" for the eROSITA feature scaler, which is a critical validation step. However, the methodology and full results are not described in the paper. Instead, the text points to an external JSON file in a code repository ("artifact pipelines/.../erosita_scaler_refit.json"). A published paper must be self-contained; essential validation procedures cannot be offloaded to external, un-refereed code repositories.
-   **Required Fix:** The methodology, setup, and full results of this robustness check must be described in sufficient detail within the paper (likely in an appendix) for a reader to understand and assess its validity without accessing external files.

#### MINOR

**P3-m1: Ambiguous Dating**
-   **Location:** Title block, p. 1
-   **Problem:** The paper is dated "June 19, 2026". This is presumably a typo.
-   **Required Fix:** Correct the date to the actual submission date.

**P3-m2: Inconsistent Use of "Quarantined"**
-   **Location:** Abstract, p. 1; §IID, p. 5; Appendix F, p. 26
-   **Problem:** The abstract states ACT DR6 is "quarantined as a cross-transfer artifact". The body refers to it as "formally quarantined". This terminology is non-standard. It seems to mean "excluded from the final analysis due to failing validation checks".
-   **Required Fix:** Replace "quarantined" with a more standard and explicit phrase like "excluded" or "failed validation and was excluded". Use this phrasing consistently.

**P3-m3: Unclear Provenance of Gaia Preprocessing**
-   **Location:** §II B α, p. 3; §G, p. 12
-   **Problem:** The paper states "the exact 20-feature production script for the published 50K-source run was not recovered" and that the specification is "lineage-inferred". This lack of direct provenance is a weakness.
-   **Required Fix:** While the script may be lost, the authors should, if possible, list the 20 features used in an appendix to provide maximum possible transparency. The current description is too vague. The statement in the Data Availability section (§VII, p. 23) that the "exact column list is enumerated in the manifest" is good, but this information should also be in the paper itself for self-containment.

**P3-m4: Confusing Footnotes in Table I**
-   **Location:** Table I, p. 7
-   **Problem:** The footnotes in Table I are extremely dense and contain critical information about threshold definitions that should be in the main text or the table caption. For example, the details of the SDSS "fixed-size continuity slice" vs. the "top-1% proper" are essential for understanding the results and are buried in footnote ♡.
-   **Required Fix:** Move the essential methodological details from the footnotes into the main text (§II B b) and the table caption. Footnotes should be reserved for minor clarifications, not core definitions.

**P3-m5: Unnecessary Acronym**
-   **Location:** Throughout
-   **Problem:** The paper uses "BIGAE (BigBounce Integrated Galaxy Autoencoder)". The "BigBounce" part seems to be branding without a clear connection to the autoencoder's function, which is general-purpose. The name is distracting.
-   **Required Fix:** Recommend renaming the framework to something more descriptive and neutral, or simply referring to it as "the autoencoder framework" throughout. If the name is kept, the motivation for "BigBounce" should be explained.

**P3-m6: Citation Formatting**
-   **Location:** Bibliography, pp. 28-29
-   **Problem:** Several citations are incomplete or use inconsistent formatting. For example, [1] and [12] are listed as "accepted" or have future dates ("2025", "2026"), which is not appropriate for a final submission. They should be listed as arXiv preprints if they are not yet published.
-   **Required Fix:** Update all citations to their final published form or, if unpublished, use a consistent arXiv format with the submission version. Remove future publication dates.

**P3-m7: Misleading Title Wording**
-   **Location:** Title
-   **Problem:** The title includes "a Native-Trained Novelty Fraction". This phrasing suggests a single, global novelty fraction was derived for the entire catalog. In reality, the paper computes a point estimate for a specific, high-score stratum of one survey (the DESI top-1000).
-   **Required Fix:** The title should be revised to be more precise and avoid overgeneralization. For example: "...and a Novelty Fraction Estimate for High-Score DESI Sources".

**P3-m8: Juxtaposition of Incomparable Sigmas**
-   **Location:** Abstract, p. 1
-   **Problem:** The abstract juxtaposes `σ(fNL)` (a forecast 1σ uncertainty on a parameter) with `+1.13σ` and `+4.61σ` from the NANOGrav analysis (parameter-shift significances relative to a Bayesian posterior uncertainty). These are statistically different concepts of "sigma". Presenting them side-by-side without context is confusing and implies they are comparable measures of significance.
-   **Required Fix:** Add a clarifying note in the abstract or rephrase to avoid the direct juxtaposition of these different statistical quantities.

#### NIT

**P3-N1: Awkward Phrasing**
-   **Location:** Abstract, p. 1
-   **Problem:** "the size benchmark is anchored to the largest published single-survey anomaly catalog" is awkward.
-   **Required Fix:** Rephrase to something like: "processing more sources than the largest previously published single-survey anomaly catalog [11]".

**P3-N2: Redundant Figure Label**
-   **Location:** Figure 1, p. 3
-   **Problem:** The figure title burned into the plot ("DESI DR1 Latent Space...") is redundant with the figure caption.
-   **Required Fix:** Remove the title from the plot image itself.

**P3-N3: Typo in Figure 10 Caption**
-   **Location:** Figure 10 Caption, p. 22
-   **Problem:** "becl| > {85°, 82°, 80.5°}" and "becl < 80°". The use of `|becl|` (absolute latitude) seems inconsistent with the single inequality.
-   **Required Fix:** Clarify the mask definition. Is it `|becl| < 80°` or `becl < 80°`? The text in §IIIH says `|becl| < 80°`. The caption for the injection test seems to imply sources are planted *outside* this region and the test is whether they are correctly excluded. Please clarify the exact procedure. The current text is confusing.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper presents a substantial and valuable dataset, and the methodological explorations are a solid contribution to the field of astronomical data mining. The scale of the work is commendable. However, the manuscript in its current form is not acceptable for publication in Physical Review D. The abstract significantly misrepresents the main cosmological results, which are the most relevant part for the PRD audience. The distinction between robust and exploratory parts of the catalog is inconsistent, and the presentation of key metrics (anomaly scores, novelty fractions) is confusing. The paper must be substantially rewritten to present the results with the rigor, clarity, and conservative framing expected of a high-impact physics journal. Once the essential and major issues listed above are thoroughly addressed, the paper will likely be a strong candidate for publication.
================================================================
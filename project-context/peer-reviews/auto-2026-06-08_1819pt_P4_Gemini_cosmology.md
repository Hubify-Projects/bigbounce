# P4 auto-2026-06-08_1819pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 184.1s

---

This is a referee report for the manuscript "Survey-Scale Galaxy Chirality with Equivariant TTA..." by Houston Golden.

The manuscript presents a detailed analysis of galaxy chirality using a large dataset of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole in the chirality distribution, constrained at a high level of precision. The authors employ a modern machine learning pipeline with a Vision Transformer (ViT) and introduce a rigorous set of bias mitigation techniques and systematic checks, most notably Test-Time Equivariant Averaging (TTA). A key part of the analysis is the identification and quantification of a "monopole-mask leakage channel," which the authors demonstrate can create a spurious dipole signal. They convincingly argue that a +3.64σ residual signal found on a specific "canonical mask" is a systematic artifact, not a cosmological detection.

The paper is well-structured, the analysis is exceptionally thorough, and the commitment to reproducibility through public data and code release is commendable. The declared analysis hierarchy and the extensive battery of null tests and systematic checks in the appendices set a high standard for this type of work. The distinction between parity-even (dipole) and parity-odd (monopole, even-l) observables is correctly and clearly maintained.

While the overall quality of the work is very high and suitable for publication in Physical Review D, there are several essential and major issues that must be addressed before the manuscript can be accepted.

## Findings

### ESSENTIAL

**P4-E1 | Page 8, Figure 4**
*   **Problem:** The caption for Figure 4 is completely inconsistent with the figure's content.
    *   The caption describes a "Top: l=1 dipole power. Bottom: l=2 quadrupole" plot with "Black: data; orange band: 500-MC monopole-only generative null".
    *   The figure is a single bar chart for l=1 to l=5 with blue bars labeled "Measured" and gray error bars for "Null expectation".
    *   The caption text is a summary of a result, not a description of the figure elements.
*   **Required Fix:** Rewrite the caption to accurately describe the content of Figure 4. The figure itself may need to be revised to be consistent with the results presented in the tables (e.g., Table III), or the text needs to be updated to refer to this specific single-l power plot, which is not otherwise presented.

**P4-E2 | Page 1, Page 11**
*   **Problem:** The manuscript uses future dates. The date on the title page is "June 2026" and the data release tag in the Data Availability section is "v2026.04". This is inappropriate for a scientific publication.
*   **Required Fix:** Change all dates to reflect the actual date of submission or acceptance.

**P4-E3 | Page 5, Figure 1**
*   **Problem:** The caption for Figure 1 states "Test-time D4 equivariant averaging (TTA). For each input image x, the classifier is evaluated on the eight D4 transforms (four rotations × two reflections)." However, the main text (Sec. III C, page 3) explicitly states, "We restrict to 2-fold TTA (original + horizontal flip) rather than the full D4 group because mirrors flip chirality by definition...". This is a direct contradiction on a key methodological point.
*   **Required Fix:** Correct the caption of Figure 1 to be consistent with the methodology described in the main text (i.e., 2-fold or Z2 TTA, not D4).

### MAJOR

**P4-M1 | Page 1, Page 8**
*   **Problem:** There is an unexplained and significant discrepancy between two different metrics used to describe the significance of the canonical-mask residual. The abstract and main text quote "+3.64σ" based on a moment-ratio (`z = Δ/σ_null`), but also give an "empirical rank p_mc = 0.030", which is noted to be "≈1.9σ Gaussian-equivalent". For a non-Gaussian null distribution, the empirical rank is often a more robust measure of significance. The paper proceeds using the much higher 3.64σ value without justifying why the moment-based estimator is more reliable than the empirical rank in this case.
*   **Required Fix:** The authors must provide a clear explanation for this discrepancy. They should justify their choice to use the 3.64σ value as the headline significance for this residual and discuss the implications of the lower, 1.9σ significance derived from the empirical rank.

**P4-M2 | Page 3, Sec. III B**
*   **Problem:** The classifier's training set is heavily dependent on the predictions of a previous model (CE-ResNet), with 67.6% of training labels derived from it. While the authors acknowledge this, the potential for inheriting and amplifying biases from the parent model is a significant concern. This represents a major limitation of the classifier's claim to independent ground truth.
*   **Required Fix:** This limitation should be more prominently discussed in the main body of the paper (e.g., in the Discussion section), not just noted in the Methods. The authors should elaborate on how their bias-hardening suite specifically mitigates risks associated with this training strategy.

**P4-M3 | Page 4, Table I**
*   **Problem:** The "σ" column in Table I is used inconsistently. For estimators (i), (ii), (iii), and (v), it reports a significance in standard deviations. For estimator (iv), it reports a p-value (`PLEE ≤10^-4`) in the text description while the column is blank. For estimator (vi), it reports a sensitivity threshold, and the column is blank.
*   **Required Fix:** Rename the column to "Significance" or a similar, more general term. Fill in the appropriate values for all rows. For the p-value, this would be the equivalent sigma (`>3.7σ`). For the sensitivity floor, the cell should indicate that it is a limit, not a measurement (e.g., "N/A" or "Sensitivity").

### MINOR

**P4-m1 | Page 4, Table II**
*   **Problem:** The calculated values for "Dev. (σ)" in Table II do not exactly match a direct calculation from the other numbers provided (`Dev = (f_cw - 0.5) / σ`, with `σ = sqrt(p(1-p)/N)`). For example, for Tier C, the calculation yields -9.31σ, while the table reports 9.5σ. The differences are small but suggest a minor inconsistency in the reported numbers or the value of N_spiral used.
*   **Required Fix:** Please verify the numbers in Table II and ensure they are internally consistent, or add a note explaining the source of the small discrepancy.

**P4-m2 | Page 2, Sec. I**
*   **Problem:** The text states "the post-MASTER dipole significance is -0.122σ (subsample mask, headline) / +0.43σ (real-space cross-check)." The use of a forward slash "/" to separate two distinct results is confusing and could be misinterpreted as a ratio.
*   **Required Fix:** Rephrase this sentence to clearly separate the two results, for example: "...the post-MASTER dipole significance is -0.122σ on the subsample mask (our headline result), and +0.43σ in a real-space cross-check."

**P4-m3 | Page 2, Sec. I**
*   **Problem:** The paper claims its result is "inconsistent in amplitude with Shamir's claimed ~3% signal by a factor of ~ 6-12". The paper's 50% recovery threshold is A_50 ~ 0.75%. This implies a tension factor of 3% / 0.75% = 4. The origin of the larger factor of 6-12 is not immediately clear from the text.
*   **Required Fix:** Please clarify the calculation that leads to the factor of 6-12. It may be based on the measured amplitude (which is near zero) rather than the sensitivity threshold, but this should be stated explicitly.

**P4-m4 | Page 5, Footnote 1**
*   **Problem:** Footnote 1 contains internal-tracking language not suitable for publication, such as "The previous wording...", "A parallel rerun on N(p)all-trial draws is in queue...", and "...will be reported empirically when the N(p)all rerun completes."
*   **Required Fix:** Finalize the analysis and remove this internal-project-management language. The footnote should present the final, definitive methodology.

**P4-m5 | Page 6, Table IV**
*   **Problem:** The z-scores in Table IV are slightly inconsistent with a direct calculation from the provided data and null values. For the pre-MASTER pseudo-C_l, the calculation gives z=1.57, while the table reports +1.68. For the hemisphere max|A|, the calculation gives z=4.36, while the table reports +4.42.
*   **Required Fix:** Please double-check these calculations and correct the numbers if necessary, or clarify if the discrepancy is due to rounding of the displayed values.

**P4-m6 | Page 1, Abstract**
*   **Problem:** Typo in the abstract: "apodized-mask test (+3.57σ on C² 2º apodization)". The "C² 2º" is unclear.
*   **Required Fix:** Correct the typo. It likely refers to a C^2-class apodization over a 2-degree scale.

**P4-m7 | Page 3, Sec. II A**
*   **Problem:** Typo in the description of the DESI imaging campaigns: "DECALS (d<+32°)". The "d" should likely be a delta symbol (δ).
*   **Required Fix:** Correct the typo.

**P4-m8 | Page 3, Sec. III C**
*   **Problem:** Typo in the text describing the D4-TTA hold-out: "|∆(pcw>|<0.0016".
*   **Required Fix:** Correct the typo to something like "|Δ⟨P_cw⟩| < 0.0016".

### NIT

**P4-N1 | Page 1, Abstract**
*   **Problem:** The abstract states "...on the strict-superset subsample mask (n=5,547,858, fsky = 0.659)...". This number `n` is later clarified in Table I to be `N_map_weighted`, which is not a direct galaxy count. This could be confusing to a reader of the abstract alone.
*   **Required Fix:** Consider briefly clarifying what `n` represents in the abstract, e.g., "(n=5.5M weighted sources...)" to avoid misinterpretation.

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, rigorous, and important contribution to the field. The analysis is comprehensive and the conclusions are well-supported by the evidence presented. However, the manuscript in its current form contains several critical errors, most notably the complete mismatch between Figure 4 and its caption, the contradiction regarding the TTA methodology, and the use of future dates. These essential fixes, along with the major revisions required to clarify the significance metrics and discuss the limitations of the training data, are necessary before the paper can be accepted for publication. I am confident that the authors can address these points and I look forward to reviewing a revised version of this excellent work.
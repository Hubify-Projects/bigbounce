# P4 auto-2026-06-08_1737pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 152.2s

---

## Referee Report: [Paper P4]

**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)

**Recommendation:** MAJOR REVISIONS

---

### General Comments

This paper presents a comprehensive analysis of galaxy chirality using a large dataset of 8.47 million galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole (l=1) in the chirality distribution, a finding of significant interest to the community. The authors employ a modern machine learning pipeline, including a Vision Transformer (ViT) classifier and a Test-Time Equivariant Averaging (TTA) technique to mitigate systematic biases.

The strength of the paper lies in its rigorous and multi-pronged approach to systematics. The authors clearly distinguish between different estimators and null hypotheses, provide a "Declared Analysis Hierarchy," and perform an extensive set of diagnostic tests detailed in the appendices. The identification and quantification of a "monopole-mask leakage channel" as a significant systematic is a valuable contribution. The distinction between the parity-even axial-vector dipole and a true parity-odd signal is correctly maintained.

However, the manuscript in its current form is not acceptable for publication in Physical Review D. It suffers from several critical errors, internal inconsistencies, and a lack of polish that undermine the credibility of the otherwise strong analysis. These include a fundamental contradiction in the reported statistical significance of a key residual, calculation errors in figures and tables, inconsistent data reporting, and the presence of internal-review language. The authors must address these issues thoroughly before the paper can be reconsidered.

---

### Findings

#### ESSENTIAL

**P4-E1: Contradictory Statistical Significance of the Canonical-Mask Residual**
*   **Location:** Abstract (p. 1), Sec. III.A (p. 3), Sec. IV.D (p. 4), Sec. VII.b (p. 8), and elsewhere.
*   **Problem:** The paper repeatedly reports the post-MASTER canonical-mask residual as "+3.64σ" while simultaneously quoting an "empirical rank p_mc = 0.030". A p-value of 0.030 from 500 Monte Carlo simulations (rank 15/500) corresponds to a one-sided significance of approximately +1.88σ, not +3.64σ. A +3.64σ result would correspond to a p-value of ~1.4e-4. This is a severe contradiction of more than an order of magnitude in p-value. The text suggests these two numbers come from the same null ("500-MC binomial per-pixel-shuffle null" in the abstract), which is impossible if they are derived from the same set of simulations.
*   **Required Fix:** The authors must clarify the origin of these two numbers. If they come from different null hypotheses or different statistical estimators (e.g., moment-based vs. rank-ordered), this must be stated explicitly and justified at every mention. The current presentation is deeply confusing and invalidates the statistical claims surrounding this residual. This must be corrected throughout the manuscript, including the abstract, main body, and conclusions.

**P4-E2: Erroneous Calculation in Figure 1 (Equivariant Averaging)**
*   **Location:** Figure 1 (p. 5).
*   **Problem:** The "Equivariant Predictions" shown in the rightmost column of Figure 1 do not correspond to the procedure described by Equation (2). For the second galaxy (218924_639), the calculation should be `Peq_CW = 0.5 * (Porig_CW + Pflip_CCW) = 0.5 * (0.999 + 0.955) = 0.977`. The figure, however, shows a value of 0.955. It appears the "Flipped Predictions" were incorrectly copied into the "Equivariant Predictions" column.
*   **Required Fix:** This figure is intended to illustrate the paper's core bias-mitigation method (TTA). It must be corrected to show the actual results of the equivariant averaging as defined in Equation (2).

**P4-E3: Inconsistent Galaxy Counts in Figure 2**
*   **Location:** Figure 2 (p. 6) and Sec. IV.A (p. 3).
*   **Problem:** The caption of Figure 2 states it shows the "Catalog C composition". However, the counts for CW, CCW, and Not-Spiral classes in the figure (CW=1,687,069, CCW=1,634,726, NS=5,152,736) directly contradict the counts given for Catalog C in the main text in Sec. IV.A (CW=1,592,107, CCW=1,609,053, NS=5,273,371).
*   **Required Fix:** The figure and text must be made consistent. If the figure depicts a different catalog (e.g., Catalog A or B), the figure and its caption must be updated accordingly.

**P4-E4: Presence of Internal-Review and Placeholder Language**
*   **Location:** Footnote 1 (p. 4), text below Figure 1 (p. 5), Abstract (p. 1), Data Availability (p. 11).
*   **Problem:** The manuscript contains language that is inappropriate for a peer-reviewed publication.
    1.  Footnote 1 (p. 4): "The previous wording... was ambiguous... A parallel rerun... is in queue".
    2.  Text below Fig 1 (p. 5): "...will be reported empirically when the N(p)all rerun completes."
    3.  Date (p. 1): The paper is dated "June 2026".
    4.  Data Availability (p. 11): The release tag is "v2026.04".
*   **Required Fix:** All such internal notes, comments on previous versions, mentions of pending computations, and future dates must be removed. The paper must be presented as a finished piece of work.

#### MAJOR

**P4-M1: Discrepancy in Training Set Size**
*   **Location:** Sec. II.B (p. 2).
*   **Problem:** The text states the training labels come from three sources: GZ1 (6,637), CE-ResNet (17,153), and Synthetic (2,000). The sum is 25,790. However, the text claims the "combined training set contains 26,636 images". This discrepancy of 846 images is unexplained. Furthermore, the claim that 67.6% of labels derive from CE-ResNet (p. 3) is not reproducible with either number.
*   **Required Fix:** Clarify the source of all training images and ensure the numbers are consistent.

**P4-M2: Errors in Table II (Global CW Fraction)**
*   **Location:** Table II (p. 4) and Sec. IV.B (p. 4).
*   **Problem:** The "Dev. (σ)" column in Table II contains errors. For Tier C, the CW fraction is 0.4974, which is less than 0.5. The deviation should be negative, but the table reports "9.5". The correct value is (0.4974 - 0.5) / 0.000279 ≈ -9.32σ. The text in Sec. IV.B repeats this error. The other deviation values in the table are also slightly inaccurate.
*   **Required Fix:** Recompute all values in the "Dev. (σ)" column and correct the corresponding text. Ensure the sign is correct.

**P4-M3: Overstated Claim Regarding Previous Work**
*   **Location:** Sec. V.A (p. 6).
*   **Problem:** The paper claims that "the monopole-mask leakage channel... can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples." The authors have demonstrated this leakage channel within their own DESI/ViT pipeline. Claiming it reproduces a signal from a different survey (SDSS) analyzed with a different pipeline (Ganalyzer) is an extrapolation.
*   **Required Fix:** Soften this claim. The authors can state that their finding provides a plausible *candidate mechanism* for previously reported signals, but they cannot claim to have reproduced those specific results without a matched-footprint reanalysis using the original pipeline's selection criteria.

**P4-M4: Figure 4 Caption-Figure Mismatch**
*   **Location:** Figure 4 (p. 8).
*   **Problem:** The caption describes a two-part figure: "Top: l=1 dipole power. Bottom: l=2 quadrupole." The figure itself is a single panel showing the power spectrum from l=1 to l=5.
*   **Required Fix:** Rewrite the caption to accurately describe the content of the figure.

**P4-M5: Unexplained Increase in Significance after Monopole Subtraction**
*   **Location:** Appendix A (p. 9).
*   **Problem:** The text states that monopole subtraction "increases σ from +1.85 to +3.64 (the canonical-mask number)." This is a surprising result. Subtracting a mode from a field would typically be expected to reduce power, not increase the significance of another mode by a factor of two.
*   **Required Fix:** Provide a clear, physical explanation for this effect. For example, does the subtraction process significantly reduce the variance of the null-hypothesis simulations more than it reduces the measured power in the data? A sentence or two of clarification is needed.

#### MINOR

**P4-m1: Ambiguous Phrasing on Amplitude Disfavorment**
*   **Location:** Sec. VII.B (p. 8).
*   **Problem:** The text states the null result "disfavors... the Shamir ~3% amplitude class by a factor of ~6-12." The paper's 3σ sensitivity is A ≈ 0.75%. A 3% signal is a factor of 4 larger in amplitude (3 / 0.75 = 4). The factor of 6-12 is unclear; it may refer to significance (a 3% signal would be ~12σ), but the text says "amplitude class".
*   **Required Fix:** Clarify the statement. It is better to state that a 3% amplitude signal is ruled out at >10σ significance under their pipeline and that their result constrains any dipole amplitude to be less than 0.75% (at 3σ).

**P4-m2: Calculation Error in Table IV**
*   **Location:** Table IV (p. 6).
*   **Problem:** For the "Pre-MASTER pseudo-C(l=1)" statistic, the z-score is calculated as z = (1.696 - 1.685) / 0.007 = 1.57. The table reports z = +1.68.
*   **Required Fix:** Correct the z-score in the table.

#### NIT

**P4-N1: Typo in Appendix C**
*   **Location:** Appendix C.c (p. 10).
*   **Problem:** The text states the post-LEE significance reduces to `< 10`. This appears to be a typo for `< 1σ`.
*   **Required Fix:** Correct the typo.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a methodologically strong and scientifically important null result on the galaxy chirality dipole. The authors' focus on identifying and mitigating systematics is commendable and sets a high standard for future work in this area. However, the manuscript is marred by a significant number of errors, ranging from a critical contradiction in its statistical reporting to incorrect figures, inconsistent numbers, and unprofessional placeholder text. These issues are too numerous and severe for the paper to be published in its current form. I recommend that the paper undergo major revisions to address all the points listed above. If the authors can correct these errors and inconsistencies, the revised manuscript will represent a solid and valuable contribution to the literature.
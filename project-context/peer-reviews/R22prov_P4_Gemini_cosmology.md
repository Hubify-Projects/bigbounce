# P4 R22prov — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 163.5s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

**Report ID:** P4-R22prov

This paper presents a comprehensive analysis of galaxy chirality using a large dataset of 8.47 million galaxies from the DESI Legacy Surveys. The authors employ a Vision Transformer (ViT) classifier and a crucial Test-Time Equivariant Averaging (TTA) method to mitigate systematic biases. The main scientific results are a null detection of a real-space chirality dipole and the exclusion of a specific 1.7% amplitude cosmological dipole model. The paper also provides a detailed investigation of systematics, identifying a "monopole-mask leakage" channel and attributing a residual signal in the angular power spectrum to coherent, low-multipole systematics rather than a cosmological signal.

The work is notable for its methodological rigor, particularly the use of TTA, the extensive suite of null tests, and the transparent handling of a withdrawn result from a previous version of the manuscript. The systematic analysis is thorough and largely convincing. However, several points require clarification and revision before the paper can be considered for publication in Physical Review D.

---

### ESSENTIAL Revisions

**P4-E1: Placeholder Date**
*   **Section/Page:** Title page (p. 1), Appendix A (p. 11)
*   **Problem:** The paper is dated "(Dated: June 2026)". Appendix A refers to a "June 2026 provenance audit". This future date is highly irregular and appears to be a placeholder. Scientific papers must be dated corresponding to their submission or revision date.
*   **Required Fix:** Replace all instances of "June 2026" with the actual date of submission/revision.

**P4-E2: Conflicting Significance Metrics for Canonical-Mask Residual**
*   **Section/Page:** Abstract (p. 1), Section VII.b (p. 10)
*   **Problem:** The significance of the post-MASTER canonical-mask residual is presented in a confusing manner. The abstract states: "+3.64σ (z = Δ/σ_null moment-ratio; empirical rank p_mc = 0.030, i.e. ≈1.9σ Gaussian-equivalent)". This presents two different significance values, +3.64σ and ≈1.9σ, for the same result without adequate explanation. While a z-score (moment-ratio) and an empirical p-value can differ, especially for non-Gaussian null distributions, the large discrepancy (a factor of ~2 in sigma) is jarring and undermines the clarity of the finding. The reader is left unsure which metric is more reliable or appropriate.
*   **Required Fix:** The authors must clarify this point.
    1.  Explicitly state in the text why two different metrics are used and why they differ.
    2.  Justify which metric should be considered primary.
    3.  If the null distribution is significantly non-Gaussian, the empirical rank is often more robust. The authors should consider foregrounding the ≈1.9σ value and explaining that the +3.64σ value assumes a Gaussian-like interpretation of the moments which may not be fully applicable. This clarification is essential for the correct interpretation of this key systematic signal.

### MAJOR Revisions

**P4-M1: Scope and Interpretation of the Withdrawn Result**
*   **Section/Page:** Abstract (p. 1), Appendix A (p. 11)
*   **Problem:** The paper commendably withdraws a previous null result. The new result on the same analysis channel (apodized-footprint MASTER l=1) is a highly significant +7.28σ excess, which is now attributed to systematics. The abstract states the old result was on a "putative 'strict-superset subsample mask'" and was "computed on a synthetic-footprint catalog". The link between a synthetic footprint and a null result, versus a real footprint and a +7.28σ systematic, is not fully elucidated. Was the synthetic footprint unrealistically uniform, thereby suppressing the mask-coupling systematic that is now detected?
*   **Required Fix:** In Appendix A, add a sentence or two explicitly hypothesizing why the synthetic-footprint calculation produced a null result while the real-footprint calculation did not. A plausible explanation, such as the synthetic mask lacking the specific geometric features of the real mask that couple the monopole to the dipole, would make the provenance audit and the new interpretation much more compelling and self-contained.

### MINOR Revisions

**P4-m1: Clarification of σ-value Comparability in Table I**
*   **Section/Page:** Table I (p. 4)
*   **Problem:** The abstract and main text correctly warn that σ values from different null procedures are not directly comparable. However, Table I, which is the central summary of all key results, presents multiple σ values side-by-side without this warning in its caption.
*   **Required Fix:** Add a sentence to the caption of Table I, such as: "Note: Significance (σ) values are defined relative to their respective nulls (listed in the 'Null' column) and are not directly comparable to each other."

**P4-m2: Ambiguity in Table II Deviation Column**
*   **Section/Page:** Table II (p. 5)
*   **Problem:** The column "Dev. (σ)" in Table II appears to list the absolute value of the deviation from 0.5000 in units of σ, but this is not stated. For Catalog C, the excess is negative (-0.26%), but the deviation is listed as a positive 9.5σ.
*   **Required Fix:** Clarify the column header, for example, to "|fcw - 0.5|/σ", or add a footnote explaining that the absolute deviation is reported.

**P4-m3: Consistency of High-Confidence Sample Size**
*   **Section/Page:** Abstract (p. 1), Table I (p. 4)
*   **Problem:** The abstract states "471,049 high-confidence per-spiral after p_eq > 0.9". However, the "injection floor" estimator in Table I, which is the only result that appears to use this high-confidence (HC) sample, lists the sample size as "471,049 HC". It is not immediately clear what "per-spiral" means in the abstract, and the table entry is terse.
*   **Required Fix:** For clarity, either remove "per-spiral" from the abstract or briefly define it. Ensure the sample definition is consistent and clear between the abstract and Table I.

**P4-m4: Footnote 2 Clarity**
*   **Section/Page:** Appendix E (p. 13)
*   **Problem:** Footnote 2 is critical for understanding the robustness checks on high-confidence subsamples. It explains a subtle but important point about the "monopole-preserving" estimator. While the content is correct, its density makes it difficult to parse.
*   **Required Fix:** Consider slightly rephrasing the footnote for improved readability. For instance, breaking down the logic into bullet points or sequential statements could help the reader follow the argument that the collapse of the signal on HC cuts is evidence for a label-noise systematic.

### NIT-PICKS (Cosmetic)

**P4-N1: Awkward Phrasing in Falsification Criterion**
*   **Section/Page:** Abstract (p. 1)
*   **Problem:** The sentence "a future 5σ detection at A ~ 0.75% would be entirely consistent with the present non-detection (only 50% of injected A = 0.75% signals are recovered at 3σ under our null; a detection in the unrecovered half is not in tension with non-detection in the recovered half)" is convoluted.
*   **Required Fix:** Rephrase for clarity. For example: "A future 5σ detection at an amplitude A ≈ 0.75% would not be in tension with this null, as our injection-recovery tests show only a 50% probability of detecting such a signal at >3σ. A detection would simply imply the true signal fell in the 50% of realizations our analysis was not sensitive to."

**P4-N2: Redundant Word in Abstract**
*   **Section/Page:** Abstract (p. 1)
*   **Problem:** The phrase "The MASTER-deconvolved pseudo-C_l channel on the patchy survey footprint is presented as a systematics diagnostic, not an independent cosmological null." is slightly redundant.
*   **Required Fix:** Suggest simplifying to "The MASTER-deconvolved pseudo-C_l channel on the patchy survey footprint serves as a systematics diagnostic, not an independent cosmological null."

---

## Summary recommendation

**MAJOR REVISIONS**

The paper represents a substantial and high-quality analysis. The authors' commitment to rigorous systematics testing and transparency is exemplary. The core scientific results—the null real-space dipole and the template-fit exclusion—appear robust and are well-supported by the evidence presented.

However, the issues identified, particularly the use of a future placeholder date (P4-E1) and the confusing presentation of the significance for the canonical-mask residual (P4-E2), are critical barriers to publication. These must be addressed thoroughly. The other points, while less critical, will significantly improve the paper's clarity and impact. Once these revisions are made, the paper will likely be suitable for publication in Physical Review D.
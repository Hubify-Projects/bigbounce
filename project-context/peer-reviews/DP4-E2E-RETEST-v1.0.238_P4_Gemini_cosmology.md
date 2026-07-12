# P4 DP4-E2E-RETEST-v1.0.238 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/chirality_catalog_paper.pdf` md5=03f03e2a pages=35
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2067 chars)
**Wall time**: 207.4s

---

# Referee Report

**Paper ID:** P4
**Title:** A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning

This paper presents a measurement of the large-scale chirality dipole of spiral galaxies using a new catalog of 8.5 million galaxies from the DESI Legacy Surveys. The authors employ a Vision Transformer with a test-time equivariant averaging (TTA) procedure to classify galaxies, resulting in what they claim is the largest and most bias-hardened chirality-labeled catalog to date. The primary result is a null detection of the dipole. The analysis is comprehensive, including a detailed treatment of potential systematics, a clear hierarchy of statistical estimators, and a robust calibration of the measurement's sensitivity.

The work is of high quality, methodologically innovative, and directly addresses a topic of cosmological interest that has seen conflicting claims in the literature. The analysis is exceptionally thorough, with a rigorous approach to systematics that sets a new standard for this type of measurement. The paper is well-written, clearly structured, and provides extensive details and data products to ensure reproducibility. It is suitable for publication in Physical Review D after addressing the following points.

---
## Findings

### ESSENTIAL

**P4-E1** | Section: III.B (p. 4), Table I (p. 5) | **Clarity of the primary exclusion claim.** | The paper's two primary cosmological claims are (i) the consistency of the real-space dipole with null and (ii) the disfavoring of a specific 1.7% dipole template. However, the nature of the second claim needs to be stated more precisely in the main text to avoid misinterpretation by readers. The abstract and main text state that a 1.7% dipole is "disfavored at z ≈ -7.6". Appendix D and the caption of Fig. 10 clarify that this is a "template-model-disfavor statistic under the spatial error model, not a calibrated detection significance" or a frequentist exclusion. While this is technically correct, the distinction is subtle. The primary analysis hierarchy in Sec. III.B and the decision tree in Table I should more explicitly state that the WLS template fit is a *model-dependent disfavoring* of a clean dipole template, and not a general-purpose frequentist exclusion limit on any dipole-like signal. This is crucial because the block-bootstrap error model is specific to the spatial correlations of the *measured* field, and its application to testing an external template carries assumptions about the nature of the noise and systematics. | **Required Fix:** In the "Declared Analysis Hierarchy" (Sec. III.B, p. 4) and the "Estimator decision tree" (Table I, p. 5), modify the description of the WLS template fit to explicitly state that it is a "template-model disfavor statistic" and not a frequentist exclusion limit. For example, change "A clean cosmological 1.7% dipole is disfavored" to "A clean 1.7% dipole template is disfavored by a WLS fit (z ≈ -7.6)". This clarification should also be propagated to the abstract and conclusions to ensure the scope of the claim is unambiguous.

### MAJOR

**P4-M1** | Section: II.B (p. 2), Appendix B (p. 26) | **Unclear description of training set augmentation.** | The description of the training set construction is confusing. Page 2 states: "after flip augmentation of the training split the combined pool is 26,616 images". Page 3 gives `ntrain = 21,293 post-augmentation`, `nval = 5,323`, and an `826-image difference` attributed to the augmentation. This is not transparent. Standard flip augmentation would double the training set size. The text implies that only 826 new images were created/added. This needs to be explained clearly. If only a subset of images were augmented, the rationale should be provided. The current description is insufficient for another researcher to reproduce the training set exactly from the source components. | **Required Fix:** Rewrite the paragraph in Sec. II.B and the corresponding details in Appendix B to provide a step-by-step, unambiguous description of the training set construction. Specify the exact number of images in the training and validation splits *before* augmentation, and then describe precisely how the augmentation was applied (e.g., "Each of the 20,467 images in the training split was horizontally flipped to create an augmented partner, resulting in a post-augmentation training set of 40,934 images," or "A random subset of 826 images from the training split was selected for flip augmentation..."). The current numbers do not seem to add up under standard procedures.

### MINOR

**P4-m1** | Section: Abstract (p. 1), IV.C (p. 10) | **Typo in asymmetry definition.** | The abstract contains a typo in the definition of the asymmetry parameter `Ap`. It states: `which maps to our Ap = 2(fcw - 1) without rescaling`. The correct definition, as given in the note on page 10, is `Ap = 2(fcw - 0.5)`. An asymmetry of `fcw - 1` would be nonsensical. | **Required Fix:** Correct the formula in the abstract to `Ap = 2(fcw - 0.5)`.

**P4-m2** | Section: VI.A (p. 17) | **Clarity of GZ1-human-only test sample.** | The text describing the GZ1-human-only test states: "the 48,414 confident... GZ1 spirals cross-match... to N = 46,017 DESI-footprint galaxies". It is not immediately clear why the number of galaxies drops from 48,414 to 46,017. Is this due to footprint effects, masking, or some other quality cut? | **Required Fix:** Briefly explain the reason for the drop in galaxy numbers from the GZ1 confident sample to the final analysis sample used in the test (e.g., "...cross-match to N = 46,017 DESI-footprint galaxies after applying the analysis mask.").

**P4-m3** | Section: VII (p. 22), Table IX | **Inconsistency in reported significance.** | The conclusion (Sec. VII.a) states that an injected 1.7% dipole yields a median recovered significance of `z ≈ 68–218`, versus an observed `+7.28σ`. Table IX, which this text references, reports the same injected `z` range but lists the observed significance as `+7.28a`, with footnote 'a' reading "Observed harmonic channel; systematics-attributed (Appendix D)." The value `+7.28σ` comes from the apodized footprint analysis (Table V), while the canonical-mask direct value is `+3.64σ` (or `+7.93σ` with more nulls). While the paper is generally excellent at keeping these separate, the conclusion should be precise about which observed value is being compared. | **Required Fix:** In Sec. VII.a, clarify which observed significance is being used for the comparison. E.g., "...versus the observed +7.28σ on the apodized footprint." Or, if the comparison is meant to be more general, cite both the canonical and apodized observed values to avoid ambiguity.

### NIT

**P4-N1** | Section: IV.D (p. 12) | **Minor phrasing ambiguity.** | The text states: "The prior literature's pre-MASTER dipole-detection claims are therefore attributed at the pre-MASTER level to this leakage channel under our DESI/ViT-Small pipeline; a matched Ganalyzer reanalysis remains required for a likelihood-level exclusion of their specific estimator and cuts." The phrasing "under our... pipeline" could be misread as applying their pipeline to the prior literature's data, which is not what was done. The point is that this mechanism, present in the current analysis, is a plausible explanation for prior results. | **Required Fix:** Rephrase for clarity. Suggestion: "This leakage channel, demonstrated within our DESI/ViT-Small pipeline, provides a plausible mechanism to explain the pre-MASTER dipole-detection claims in prior literature; however, a matched Ganalyzer reanalysis..."

**P4-N2** | Section: Appendix D (p. 31), Table XV | **Clarity on rank-deficiency.** | The caption of Table XV correctly identifies that the design matrix is rank-deficient because the three imaging-leg templates sum to zero and are collinear with the constant term. The text in the caption mentions this, but it could be stated more directly at the beginning of the caption for immediate clarity. | **Required Fix:** Add a sentence at the beginning of the Table XV caption, such as: "Note: The design matrix is rank-deficient because the three imaging-leg fraction templates are collinear with the constant term. As a result, the individual z-scores for the leg and constant templates are not meaningful, though the dipole recovery is unaffected."

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an outstanding paper that represents a significant step forward in the search for a cosmic chirality signal. The methodology is robust and innovative, the analysis of systematics is exemplary, and the conclusions are well-supported and carefully stated. The authors have successfully navigated a complex analysis with many potential pitfalls, and the result is a convincing null measurement with a well-calibrated sensitivity. The paper's structure, with its clear analysis hierarchy and decision-tree logic, is a model of clarity for complex observational analyses. The commitment to reproducibility is also commendable. The required revisions are minor and are intended to further improve the clarity and precision of the claims. The paper is a substantial contribution to the field and is highly recommended for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a rigorous re-examination of the paper.

---
### ADDITIONAL FINDINGS

**P4-m4** | Section: IV.B (p. 8), Table IV | **Minor arithmetic inconsistency in table.** | In Table IV, the row for "B (calibrated)" lists a CW fraction of `0.50400(27)` and a deviation of `+14.6σ`. The deviation is calculated as `(fcw - 0.5) / σ`. A deviation of +14.6 with an excess of +0.004 implies an uncertainty `σ = 0.004 / 14.6 ≈ 0.000274`. The parenthetical uncertainty `(27)` implies `σ = 0.00027`. This is a minor discrepancy (14.6σ vs 14.8σ) and does not affect any conclusions, but it appears to be a small typo in the parenthetical uncertainty, which should likely read `(274)` if the number of spirals is similar to the other tiers. | **Required Fix:** Please check the uncertainty calculation for the "B (calibrated)" tier in Table IV and correct the parenthetical value if necessary.

**P4-m5** | Section: III (p. 3) | **Imprecise cross-reference.** | On page 3, the text refers to propagating the GZ1 accuracy "to all downstream isotropy bounds via the sub-percent systematic floor in Sec. IV C". While Section IV.C (Dipole Analysis) does discuss systematics revealed by the confidence-cut sweep, the primary discussion of the sensitivity floor, which is calibrated by injection-recovery tests, is in Section V.B. | **Required Fix:** For maximum clarity, consider refining the cross-reference to point to Section V.B, or to both IV.C and V.B, to more accurately direct the reader to the relevant discussion of the sensitivity floor.

**P4-m6** | Section: IV.C (p. 11) | **Incorrect cross-reference.** | On page 11, the text discussing the confidence threshold contains the phrase "(see the calibration caveat in Sec. II)". The primary discussion of why the `peq` confidence scores are uncalibrated ranking outputs, not frequentist probabilities, occurs on page 7, which is part of Section IV.A. The reference to Section II is incorrect. | **Required Fix:** Correct the cross-reference to point to the appropriate discussion in Section IV.A.
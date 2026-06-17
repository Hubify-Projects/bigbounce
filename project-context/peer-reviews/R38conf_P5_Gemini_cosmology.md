# P5 R38conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.73.pdf` md5=4109fb18 pages=31
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 168.1s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample"

This paper presents a comprehensive and statistically rigorous test for the environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1. The authors cross-match a large chirality catalog with DESI redshifts and perform two main analyses: a primary test anchored on the public DESIVAST void catalog, and a secondary test using a V-Web tidal-tensor classifier. The headline result is a null detection: after accounting for a previously identified catalog-wide systematic monopole and statistical noise, there is no evidence that spiral handedness depends on cosmic-web environment (void, wall, filament, or cluster). The analysis is exceptionally thorough, including numerous robustness checks, sensitivity sweeps over classifier parameters, and cross-validations against independent environmental classifiers.

The work is of high quality and the statistical methods are sound. However, there are several issues, one of which is essential, that must be addressed before the paper can be considered for publication in Physical Review D.

### ESSENTIAL Revisions

**P5-E1: Dependence on a Non-Peer-Reviewed Companion Paper**
*   **Section:** Throughout, starting on Page 1 (Abstract)
*   **Problem:** The entire analysis framework, particularly the interpretation of all results, is critically dependent on "Paper IV [3] (companion work, not yet peer-reviewed)". Specifically, the value of the classifier-monopole systematic (`Afcw = -0.0026`) is taken as a direct input from this unreviewed manuscript. This monopole is used to calculate the predicted deviation (`opred`) against which all observed deviations are compared. An analysis in PRD cannot be fundamentally dependent on results from a paper that has not undergone peer review. The current manuscript is not self-contained.
*   **Required Fix:** The manuscript must be made self-contained. The authors must either:
    1.  Incorporate a summary of the monopole derivation from Paper IV into an appendix of the present manuscript. This appendix should be sufficient for a reader to understand how the monopole was established, its statistical significance, and the evidence for its interpretation as a classifier systematic rather than a physical signal.
    2.  Alternatively, publication of this manuscript should be delayed until Paper IV has been accepted for publication in a peer-reviewed journal.
    Given the centrality of the monopole to every interpretation in this work, this is an essential requirement for publication.

### MAJOR Revisions

**P5-M1: Interpretation of the Bright vs. Dark Target Class Residual**
*   **Section:** II (p. 2), VI.D (p. 12), XI (p. 27)
*   **Problem:** The most significant residual signal found in the paper is the difference in `fcw` between the "bright" (BGS-dominated) and "dark" (LRG/ELG/QSO) target classes. On the full sample (Table XV), this is a 0.81 pp difference, corresponding to a `|z| = 1.95` tension. In the filament class (p. 12), this becomes a `|z| ≈ 2.1` tension with an opposite sign (`σ = -2.98` for bright vs. `σ = +1.61` for dark). The authors interpret this as a residual BGS-selection-function systematic. While plausible, this is not definitively proven. The paper's headline claim of "no environment dependence" is weakened by this unresolved ~2σ residual, which is clearly correlated with both environment (filament/cluster) and target selection.
*   **Required Fix:** The authors should either provide stronger evidence for the selection-function interpretation or, more appropriately, soften their conclusions. The abstract and discussion should more explicitly flag the bright/dark dichotomy as the most significant remaining challenge to a pure null interpretation and state that it cannot be fully disentangled with the current data. The current explanation is plausible but presented with more certainty than is warranted.

**P5-M2: Paper Length and Structure**
*   **Section:** Entire manuscript
*   **Problem:** At 31 pages, the paper is excessively long for what is ultimately a (very robust) null result. The main narrative thread is diluted by the inclusion of numerous secondary and tertiary cross-checks in the main body of the text. The core argument is strong but could be presented much more concisely.
*   **Required Fix:** The paper should be restructured to improve clarity and reduce length. I recommend a target length of ~20-22 pages for the main text.
    *   The primary analysis (V-Web headline result in Sec. VI and the DESIVAST cross-validation in Sec. VIII) should form the core of the paper.
    *   The extensive Phase 2 sensitivity sweep (Sec. VII) could be summarized in a paragraph in the main text, with the detailed tables and discussion moved to an appendix.
    *   The additional cross-checks against Tempel+2014 (Sec. IX.B), concurrent literature (Sec. IX.C), and ASTRA (Sec. X) are valuable for robustness but are secondary. These should be condensed and moved to an appendix. This would significantly improve the readability and impact of the main result.

### MINOR Revisions

**P5-m1: Unquantified Uncertainty from Redshift-Space Distortions (RSDs)**
*   **Section:** XIII (Limitations, p. 28)
*   **Problem:** The V-Web classification is performed on observed redshift-space positions. The "Limitations" section correctly notes that RSDs affect the tidal tensor eigenvalues and that a quantitative bound requires a reconstruction. While the authors provide a plausible order-of-magnitude argument that the effect is sub-dominant for their 25 Mpc/h smoothing scale, this remains an unquantified systematic uncertainty on the V-Web results. The RSD-robustness test for DESIVAST in Sec. VIII is a membership test against a *fixed* void geometry and does not address the impact of RSDs on the *derivation* of that geometry.
*   **Required Fix:** The abstract's summary of the V-Web result should include a caveat about the use of redshift-space positions. The discussion in Sec. XIII should be slightly strengthened to make it clear that the RSD impact on the V-Web classifier is a key unquantified systematic, even if it is expected to be small.

**P5-m2: Unsubstantiated Quantitative Robustness Claim**
*   **Section:** II (Robustness, p. 2)
*   **Problem:** The text states: "...the any-hole/maximal-sphere comparison at n_void = 57,081 gives Afcw continuity within ±0.6 pp". This quantitative claim of "±0.6 pp" is not derived or referenced anywhere else in the paper. An explicit calculation based on the numbers in Sec. VIII.E gives a shift of 0.6 pp (from +0.06 pp to -0.54 pp), but this is a single value, not a continuity bound.
*   **Required Fix:** Rephrase this sentence to state the observed shift directly and remove the un-derived "continuity within ±X" language. For example: "swapping from the any-hole to the maximal-sphere criterion shifts the resulting Afcw by 0.6 percentage points".

**P5-m3: Confusing Unit Conversion Footnote**
*   **Section:** IV.A (p. 4, footnote 1)
*   **Problem:** Footnote 1, which describes the conversion from Mpc to h⁻¹ Mpc, is written in a confusing manner: "numerical value D/(h⁻¹ Mpc) = h D/(1Mpc) = h · D[Mpc]".
*   **Required Fix:** Rewrite the footnote for clarity. Suggestion: "To convert a distance D given in Mpc to units of h⁻¹ Mpc, we multiply by h. Using Planck 2018 cosmology (h ≈ 0.6766), a distance of D = 843 Mpc corresponds to D ≈ 843 × 0.6766 h⁻¹ Mpc ≈ 570 h⁻¹ Mpc."

### NIT-PICKING (Cosmetic)

**P5-N1: General Comments**
*   The paper is exceptionally well-written and free of typographical errors. The transparency regarding post-hoc analysis choices and withdrawn prior results is commendable. The use of an "analysis tree" (Table II) is excellent practice.
*   The re-computation of key statistics (χ², σ values) from the provided tables confirms the authors' calculations. The contingency tables in Appendix B are a welcome addition for reproducibility.

## Summary recommendation
**MAJOR REVISIONS**

This is a methodologically sound and impressively thorough paper that provides strong evidence for the independence of spiral chirality from large-scale structure environment in DESI DR1. The null result is robustly tested against a wide array of potential systematics and analysis choices. However, the paper in its current form cannot be accepted due to its critical reliance on an unpublished, non-peer-reviewed companion paper (Paper IV) for its central systematic correction. This issue must be resolved by making the present work self-contained. Additionally, the paper would benefit significantly from restructuring to improve conciseness and from a more cautious interpretation of the unresolved residual signal related to target type. Once these issues are addressed, the paper will represent a significant contribution to the field.
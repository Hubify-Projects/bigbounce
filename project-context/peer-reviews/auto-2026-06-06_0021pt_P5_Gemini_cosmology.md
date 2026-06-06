# P5 auto-2026-06-06_0021pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 171.4s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"

This manuscript presents an analysis of the chirality of spiral galaxies as a function of their large-scale structure environment, using a cross-match between a new galaxy chirality catalog and the DESI Data Release 1. The primary conclusion is a null result: after accounting for a catalog-wide systematic offset, the fraction of clockwise (CW) vs. counter-clockwise (CCW) spiral galaxies is found to be independent of environment (void, wall, filament, or cluster). The analysis is comprehensive, employing multiple cosmic-web classification algorithms (V-Web, DESIVAST, Tempel, ASTRA) and a wide range of robustness checks.

While the statistical analysis is thorough and the robustness checks are impressive, the manuscript suffers from several critical flaws that preclude its publication in Physical Review D in its current form. The most severe issue is its complete reliance on an unpublished, non-peer-reviewed companion paper for its primary input data and systematic corrections.

### ESSENTIAL Revisions

**P5-E1: Foundational Reliance on Unpublished Work**
*   **Section:** Throughout, e.g., Abstract (p. 1), Section II (p. 2), Section III A (p. 2)
*   **Problem:** The entire analysis is predicated on the galaxy chirality catalog and the "catalog-monopole offset" described in "Paper IV [3]", which is cited as a "companion work, not yet peer-reviewed" and "in preparation". A published paper cannot be fundamentally dependent on data and core systematic corrections from a non-existent or non-peer-reviewed source. The validity of every conclusion in this manuscript hinges entirely on the correctness of Paper IV, which cannot be assessed by the reader or referee.
*   **Required Fix:** The manuscript cannot be published until Paper IV is, at a minimum, publicly available on a preprint server (e.g., arXiv) and submitted for publication. Preferably, Paper IV should be accepted for publication. Alternatively, the present manuscript must be made self-contained by adding a substantial appendix that details the creation of the chirality catalog, the training of the classifier, the validation tests performed, and the derivation of the systematic monopole offset. This appendix must be sufficiently detailed for the results to be independently scrutinized.

**P5-E2: Incorrect Dismissal of a Statistically Significant Result**
*   **Section:** VI D (p. 6)
*   **Problem:** The redshift-stratified cross-check of the cluster class finds a deviation of σ = -3.14 for the third redshift quartile (Z3). The text then states, "All four z-quartile deviations sit in the -1.7 to -3.2σ band, none individually crossing the Bonferroni-4 |σ| = 3.02 threshold at α = 0.01." This statement is factually incorrect, as |-3.14| > 3.02. This is a 3.14σ deviation that survives a proper look-elsewhere correction. It cannot be dismissed.
*   **Required Fix:** The authors must acknowledge that this bin crosses the significance threshold. They must remove the incorrect statement and provide a proper discussion of this result. While it may be a statistical fluctuation, it is the most significant finding in the paper and must be treated as such. This could, for example, point to a redshift-dependent systematic or a hint of a real effect in a specific regime.

**P5-E3: Manuscript and Reference Dating**
*   **Section:** Title page (p. 1), Bibliography (p. 20)
*   **Problem:** The manuscript is dated "June 4, 2026". This is unprofessional and causes significant confusion when interpreting the publication dates of references (e.g., [11], [12], [13]), which are cited with 2025 and 2026 dates.
*   **Required Fix:** The date must be corrected to the actual date of submission. All reference dates should be checked for accuracy at the time of submission.

**P5-E4: Gross Typo in Abstract**
*   **Section:** Abstract (p. 1)
*   **Problem:** The abstract states "DESI Data Release 1 redshift catalog (16.4 × 10⁹ ZWARN=0 input rows)". This is 16.4 billion, which is three orders of magnitude too large. The correct number for DESI DR1 is ~16.4 million. This is a significant error in a key number in the abstract.
*   **Required Fix:** Correct 10⁹ to 10⁶. The value 16,361,731 from Table I should be used for consistency.

### MAJOR Revisions

**P5-M1: Ambiguity in Abstract**
*   **Section:** Abstract (p. 1)
*   **Problem:** The abstract is extremely dense and reads more like an executive summary. The sentence "the CW fraction shows no environment dependence above the sensitivity floor set by the Paper IV catalog-monopole offset of ~0.2pp (systematic-dominated...) and by counting statistics of ~5pp (statistical-dominated...)" is confusing. It juxtaposes two "floors" (0.2pp and 5pp) that differ by a factor of 25 without a clear explanation of their respective domains of applicability.
*   **Required Fix:** Rewrite the abstract to be more concise and clear. The key results should be presented without overwhelming the reader with a dozen different sigma values. The concept of the sensitivity floor should be explained more simply, for instance by stating that the search is sensitive to environmental variations of X%, and no such variation is found.

**P5-M2: Potential 3.4σ Tension Under-reported**
*   **Section:** Abstract (p. 2), Section VII C (p. 7)
*   **Problem:** The analysis of tracer programs reveals a sign-flip in the chirality deviation between bright and dark samples in filaments, leading to a |z| ≈ 3.4σ tension (mentioned on p. 2). The authors flag this as a "real diagnostic" but anchor their headline result on the DESIVAST analysis, which is less sensitive to this effect. While this is a reasonable analysis strategy, this 3.4σ tension is one of the most significant signals discussed and should be mentioned in the abstract as a key finding, even if it is interpreted as a systematic.
*   **Required Fix:** Add a sentence to the abstract summarizing the 3.4σ tension found in the tracer-program analysis and the interpretation that it likely stems from selection-function systematics.

### MINOR Revisions

**P5-m1: Inconsistent Calculation of Predicted Sigma**
*   **Section:** VI A (p. 5)
*   **Problem:** The predicted sigma for the filament class due to the monopole is given as σ_pred(filament) ≈ -3.16. However, a direct calculation using the provided formula and numbers (σ_pred = 2 * Δf_cw * √N = 2 * (-0.0026) * sqrt(408187)) yields -3.32. The value for the cluster class (-3.28) calculates correctly.
*   **Required Fix:** Please verify the calculation for the filament class and correct the value in the text.

**P5-m2: Incorrect Bonferroni Threshold Calculation**
*   **Section:** V B (p. 5)
*   **Problem:** The text states: "Treating the five DESIVAST estimators as a Bonferroni-5 family at α = 0.05, the per-test threshold is σ_Bonf,α=0.05,K=5 ≈ 2.81". For α=0.05 and K=5, the per-test significance is α_eff = 0.05/5 = 0.01. The corresponding two-sided z-score is ~2.58, not 2.81. A z-score of 2.81 corresponds to α_eff ≈ 0.005.
*   **Required Fix:** Correct the calculation. Either state the threshold is 2.58 for α=0.05, or state that the threshold 2.81 corresponds to α=0.025.

**P5-m3: Typo in Abstract**
*   **Section:** Abstract (p. 1)
*   **Problem:** The text reads: "none reach 30 after look-elsewhere correction". The "0" is a typo.
*   **Required Fix:** Change "30" to "3σ".

**P5-m4: Non-standard Poisson Equation Convention**
*   **Section:** IV A (p. 3)
*   **Problem:** The Poisson equation in k-space is given as Φ(k) = -δ_k/k², while the tidal tensor is T_ij(k) = k_i k_j Φ(k). The standard cosmological convention is ∇²Φ ∝ +δ, leading to T_ij(k) = -k_i k_j Φ(k). While the author's convention is internally consistent (the two sign flips cancel), it is non-standard and could cause confusion.
*   **Required Fix:** Add a brief note acknowledging that the sign convention for the potential Φ is chosen to simplify the expression for the tidal tensor.

### NITs (Nitpicks)

**P5-N1: Awkward Phrasing**
*   **Section:** III B (p. 3)
*   **Problem:** The sentence "These row counts are derived in this work by applying our cuts to the DR1 zall catalog (not published DR1 constants); the fetch + filter driver is derived in this work" is awkward.
*   **Required Fix:** Rephrase for clarity, e.g., "The sample was selected by applying the following cuts to the DESI DR1 zall catalog...".

**P5-N2: Typo in σ Symbol**
*   **Section:** II (p. 2)
*   **Problem:** The text reads "consistent with parity at ~ 1σ".
*   **Required Fix:** Add the missing sigma symbol: "~1σ".

## Summary recommendation
**REJECT**

The manuscript is rejected in its current form. The scientific analysis is detailed and appears to be executed with care, featuring an excellent set of robustness tests that strengthen its null conclusion. However, the work is critically undermined by its foundational reliance on an unpublished and non-peer-reviewed companion paper (Paper IV) for its primary data and systematic corrections. This is a fatal flaw that makes the entire analysis unverifiable. Furthermore, the manuscript incorrectly dismisses a statistically significant (3.14σ) finding and contains several errors, including a major typo in the abstract and an unprofessional future date.

The paper shows significant promise and could be a valuable contribution to the literature. I would be willing to review a substantially revised version that addresses all the ESSENTIAL points listed above. Specifically, the work must be made self-contained or wait until its foundational companion paper is publicly available and has undergone peer review.
# P2 2026-06-04_1814pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 52.2s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: Forecasts for SPHEREx and MegaMapper"**

**Paper ID:** P2
**Round:** 2026-06-04_1814pt

This paper presents forecasts for testing the matter bounce scenario using primordial non-Gaussianity (PNG) measurements from the SPHEREx and MegaMapper surveys. The main contributions are: (1) a clarification of a factor-of-two discrepancy in the literature regarding the predicted value of `fNL = -35/8`, (2) the first quantification of the template mismatch between the matter-bounce bispectrum and the standard local template, and (3) a detailed Bayesian model comparison to assess the discriminating power of these future surveys.

The paper is well-motivated and timely. The calculation of the template mismatch factor `r` is a novel and important contribution for interpreting future data. The systematic analysis, particularly the emphasis on the robustness of the bispectrum channel compared to the scale-dependent bias, is valuable. However, the manuscript contains several significant issues that must be addressed before it can be considered for publication.

---

### ESSENTIAL Revisions

**P2-E1: Irrelevant Parity-Odd Observable Analysis**
- **Section/Page:** Sec. 9.4, p. 11
- **Problem:** The third paragraph of this section is dedicated to an analysis of cosmic birefringence (`β`), a parity-odd observable. This is entirely unrelated to the subject of the paper, which is the bispectrum and scale-dependent bias from `fNL`, a parity-even observable. The paragraph presents a new analysis of Planck data for `β`, which appears to be material from the cited "companion paper." Its inclusion here is confusing, breaks the flow of the paper, and is inappropriate.
- **Fix:** Remove the entire third paragraph of Section 9.4, beginning with "An independent observable—cosmic birefringence..."

**P2-E2: Unscientific Subjective Confidence Statement**
- **Section/Page:** Sec. 2.3, p. 4
- **Problem:** At the end of the discussion resolving the literature discrepancy on the value of `fNL`, the paper states: "We assign 92% confidence to this normalization." This is not a statistically derived confidence level but a subjective statement of belief in the argument's correctness. Such language is inappropriate for a scientific paper. The strength of the argument should stand on its own.
- **Fix:** Replace this sentence with a qualitative summary of the argument's strength. For example: "Based on this analysis of the commutator factor and convention differences, we conclude that `fNL = -35/8` is the correct value in the Planck/Komatsu-Spergel convention."

**P2-E3: Clarity on Null Result Significance**
- **Section/Page:** Abstract, p. 1
- **Problem:** The abstract claims, "A null result from SPHEREx would disfavor the quasi-dust matter bounce benchmark under assumptions (a)–(e) at > 4σ significance." While the optimistic forecast supports this, Section 4 (p. 5) notes that the significance can drop to `3.0σ` in a conservative scenario with GR marginalization. A null result in that case would be `|0 - (-4.375)| / (0.7/0.876 * (5.5/3.0)) ≈ 3σ` from the bounce prediction. The abstract should reflect this dependence on systematics modeling.
- **Fix:** Modify the abstract to acknowledge the range of possible significance for a null result. For example: "...at 3–5σ significance, depending on the successful mitigation of large-scale systematics."

---

### MAJOR Revisions

**P2-M1: Speculative Nature of the Consistency Relation**
- **Section/Page:** Sec. 8.2, p. 10
- **Problem:** This section introduces an `fNL-ns` consistency relation, which is a potentially powerful result. However, the derivation of the key coefficient `c` is not provided. The text states that its value is bounded (`c ∈ [-0.7, -10]`) and that "Narrowing this range requires evaluating all four cubic-action integrals simultaneously," which has not been done in this work. As presented, this section is more of a prospectus for future work than a solid result of this paper.
- **Fix:** The section must be rewritten to clearly state the preliminary nature of this relation. The authors should either provide a more detailed derivation of the bounds on `c` (perhaps in an appendix) or explicitly frame the entire section as a suggestion for a future consistency test, highlighting what calculations are needed to make it concrete.

**P2-M2: Incorrect SPHEREx Timeline**
- **Section/Page:** Sec. 9.1, p. 10
- **Problem:** The paper states: "SPHEREx (launched March 2025; first all-sky survey completed December 2025; science data release expected ~2028)". A survey completion in December 2025 is impossible for a March 2025 launch. The nominal SPHEREx mission plan involves four all-sky surveys over two years.
- **Fix:** Correct the timeline. A more accurate statement would be: "SPHEREx (scheduled for launch no earlier than 2025) will perform an all-sky survey over a nominal two-year mission. The first science data release is expected circa 2028."

---

### MINOR Revisions

**P2-m1: Removal of Internal Notes and Versioning Artifacts**
- **Section/Page:** Title page (p. 1) and Sec. 6.3 (p. 7)
- **Problem:** The manuscript contains artifacts from the writing process.
    1. The title page includes a date and version number: "March 24, 2026 — v1.6.0".
    2. The end of Section 6.3 contains an internal note to the author: "The abstract quotes ~ 8–17, which uses the broadened bounce prior and the baseline GR scenario."
- **Fix:** Remove these artifacts from the manuscript.

**P2-m2: Abstract Clarity on Bayes Factor**
- **Section/Page:** Abstract, p. 1
- **Problem:** The abstract states that a detection would favor the bounce "at Bayes factor ~ 8–17". The main text reveals this value is highly sensitive to prior choices, with the value for a delta-function prior being much larger (Table 2). The abstract should be more precise.
- **Fix:** Clarify the assumptions behind the quoted Bayes factor in the abstract. For example: "...at a Bayes factor of ~8–17, assuming a moderately broadened prior on the theoretical prediction to account for model uncertainties."

**P2-m3: Inconsistent Code Versioning**
- **Section/Page:** Data and Code Availability, p. 12
- **Problem:** The paper is labeled v1.6.0 on the title page, but the GitHub link provided is pinned to a release tag `v2.1.0`.
- **Fix:** Ensure the version of the paper is consistent with the version of the code repository it describes.

**P2-m4: Citation Placeholder**
- **Section/Page:** Throughout
- **Problem:** All citations appear as `[?]`.
- **Fix:** Populate the bibliography and replace the placeholders with proper citations.

---

### NIT (Typos/Suggestions)

**P2-N1: Redundant Figure Axis Labels**
- **Section/Page:** Figure 5, p. 9
- **Problem:** The y-axis labels `σ(fNL)` (left) and `Detection significance (σ)` (right) are slightly different but represent related quantities. The right panel is a simple scaling of the left panel.
- **Fix:** Consider using a consistent label (e.g., `σ(fNL)`) for both, or simply presenting the more fundamental left panel and explaining its implication for significance in the caption.

---

## Summary recommendation
**MAJOR REVISIONS**

This paper makes a tangible and useful contribution to the cosmology literature by quantifying the observability of the matter bounce `fNL` prediction. The calculation of the template mismatch and the detailed systematic-aware forecast are valuable for the community, especially with SPHEREx's first data release on the horizon. However, the manuscript is currently marred by several significant issues, most notably the inclusion of an entire section on an unrelated observable (cosmic birefringence) and the use of unscientific language to express confidence in a theoretical argument. Once these essential and major issues are thoroughly addressed, the paper will be a strong candidate for publication in Physical Review D.
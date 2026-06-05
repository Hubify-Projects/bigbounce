# P5 2026-06-04_R2pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 85.0s

---

**Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"**

This manuscript presents a detailed investigation into the potential correlation between spiral galaxy chirality and large-scale structure environment, using data from the DESI Data Release 1. The author performs a primary analysis by cross-matching a large chirality catalog with the DESIVAST void catalog, and supports this with numerous secondary analyses and robustness tests. The main conclusion is a null result: spiral galaxy handedness is found to be statistically independent of cosmic environment at the sensitivity of this study.

The analysis is thorough, and the author demonstrates a sophisticated understanding of the statistical methods and potential systematic effects involved. The transparent discussion of the "garden-of-forking-paths" and the clear designation of primary vs. secondary analysis paths is commendable. The robustness of the null result across different void-finding algorithms, cosmic-web classifiers, and galaxy samples is a significant strength.

However, the paper requires major revisions to address several critical issues related to its foundational data dependency, structure, and the interpretation of key findings.

### ESSENTIAL Revisions

**P5-E1: Dependency on non-peer-reviewed work.**
- **Section:** Abstract, II, throughout.
- **Problem:** The entire analysis is predicated on the galaxy chirality labels and the classifier monopole offset from "Paper IV [3]", which is cited as a "companion work, not yet peer-reviewed". The validity of every result in this manuscript is conditional on the correctness of Paper IV. While the author correctly treats the inputs from Paper IV (labels and monopole) as fixed and propagates their effects, the lack of peer review for the foundational dataset is a critical issue for publication.
- **Fix:** The paper can only be published after Paper IV has been accepted for publication in a peer-reviewed journal. The manuscript must be updated to reflect the final published status and citation of Paper IV. In the interim, the conditional nature of the results must be stated more forcefully in the abstract and introduction.

**P5-E2: Presentation of code paths in main text.**
- **Section:** Throughout (e.g., p.3, p.4, p.5, etc.).
- **Problem:** The text contains numerous explicit file paths to the analysis pipeline (e.g., `pipelines/p5_desi_chirality/scripts/02_fetch_desi_dr1.py`). While this is excellent for reproducibility, it is not appropriate for the body of a published article. This information belongs in a dedicated code/data availability statement or appendix, linked to a public repository.
- **Fix:** Remove all explicit file paths from the main prose. Consolidate this information into a "Data and Code Availability" section or an appendix, providing a single link to a public code repository (e.g., on GitHub or Zenodo) where the full pipeline structure is documented.

### MAJOR Revisions

**P5-M1: Paper Structure and Length.**
- **Section:** Overall.
- **Problem:** The paper is 21 pages long, which is excessive for a single null result, however robust. The narrative structure is suboptimal. The "primary analysis path" (the DESIVAST-anchored result), which is the strongest and cleanest evidence, is not presented until Section VIII on page 10. The preceding sections are dedicated to the "secondary" V-Web analysis, which is shown to be weaker and more affected by systematics. This buries the lede and makes the paper's core argument difficult to follow.
- **Fix:** Restructure the paper to present the strongest, primary result first. A suggested structure:
    1. Introduction
    2. Data (Chirality Catalog, DESI DR1, DESIVAST)
    3. The Primary Null Result: Chirality in DESIVAST Voids (current Sec. VIII). This section should include the core result (Table VII) and the three-algorithm robustness check.
    4. Supporting Analyses and Cross-Checks (this would contain the V-Web analysis, Tempel, ASTRA, etc., presented more concisely). The V-Web analysis should be framed from the outset as a consistency check that reveals important systematics (like the bright-vs-dark split), which the primary analysis avoids.
    5. Discussion & Limitations
    6. Conclusion
    Many of the detailed cross-validations (e.g., the full ASTRA and Tempel sections) could be summarized in the main text and moved to an appendix to improve readability and reduce the main text length to a target of ~15 pages.

**P5-M2: Handling of the Bright-vs-Dark Dichotomy.**
- **Section:** VI D b (p. 7), Abstract.
- **Problem:** The paper finds a `|z| ≈ 3.4σ` difference in the chirality of filament galaxies between the "bright" (BGS) and "dark" (LRG/ELG/QSO) target samples. This is a statistically significant detection. The paper correctly states that the data do not allow a clean separation between a selection-systematic origin and a genuine astrophysical effect. However, the headline claim of "no environment dependence" needs to be more carefully qualified in light of this finding. While the primary DESIVAST analysis (restricted to low-z BGS) is insensitive to this specific issue, it remains the most significant non-null result in the paper's exploratory phase.
- **Fix:** The abstract and conclusion must more clearly state that while the primary, controlled test on the DESIVAST BGS sample yields a null result, a significant `(3.4σ)` difference in chirality is detected in filaments when comparing different galaxy tracers (BGS vs LRG/ELG/QSO). This finding, while likely systematic in origin, represents a key area for future investigation and is a non-trivial result of this work. The current phrasing ("real residual structure") is good, but its prominence should be elevated.

**P5-M3: Redshift-Space Distortion (RSD) Treatment.**
- **Section:** XIII (p. 18), X (p. 10).
- **Problem:** The paper argues its primary DESIVAST analysis is "essentially RSD-immune" but acknowledges that the secondary V-Web analysis is performed in redshift space and is subject to RSDs. The discussion of the RSD impact on V-Web in Sec. XIII is good, but the estimate of the effect is qualitative ("sub-dominant at the current ~10^-3 precision").
- **Fix:** The "Order-of-magnitude boundary-crossing estimate" on p. 19 needs to be more quantitative. The author estimates 3-5% of galaxies are in boundary cells. A simple calculation should be added to show the maximum possible effect on `∆f_CW`. For example: assume 4% of filament galaxies (`f_CW ≈ 0.498`) flip into the wall class (`f_CW ≈ 0.503`). The change in the average `f_CW` would be `0.04 * (0.503 - 0.498) = 0.0002`. Performing this simple bounding calculation for the main class pairs would substantiate the claim that the effect is sub-dominant to the statistical precision and strengthen the paper's argument.

### MINOR Revisions

**P5-m1: Comparison of Observed vs. Predicted Monopole Deviation.**
- **Section:** VI A (p. 5).
- **Problem:** The paper compares the observed `σ` in the filament and cluster classes to the `σ_pred` from the Paper IV monopole. For the cluster class, `σ_obs = -4.66` while `σ_pred ≈ -3.28`. The text describes this as being "within order-unity of observation". This is vague. The difference is 1.38 standard deviations of the measurement itself.
- **Fix:** State the comparison more precisely. For example: "The observed deviation in the cluster class is -4.66σ, which is 1.38σ larger than the -3.28σ deviation predicted from the classifier monopole. While this is a modest discrepancy, the sign and magnitude are broadly consistent with the monopole being the dominant source of the deviation." This is more transparent than "order-unity".

**P5-m2: Appendix A (Toy EFT Mapping).**
- **Section:** Appendix A (p. 19).
- **Problem:** The toy model operator `L_parity ⊃ g_ϕ (∇_i ϕ) (∇_i ρ/ρ_bg) (L̂ · ẑ)` is presented. The author correctly lists several major theoretical caveats, including the breaking of rotational invariance and the lack of gauge invariance. Given these significant limitations, the utility of the appendix is debatable.
- **Fix:** The appendix is acceptable as a "guide for future model-building" as stated, given the extensive disclaimers. However, the author should consider adding a sentence explicitly stating that constructing a fully covariant and gauge-invariant operator that reproduces this phenomenology on large scales is a non-trivial theoretical challenge left for future work. This would further clarify the schematic nature of the appendix.

### NITs (Typos/Formatting)

**P5-n1: Version number in dateline.**
- **Section:** Title block (p. 1).
- **Problem:** The dateline includes an internal version number: "(Dated: June 4, 2026 — v0.1.45-2026-06-04)".
- **Fix:** Remove the version number (`v0.1.45-2026-06-04`) for the final publication.

**P5-n2: Author contact information.**
- **Section:** Footnote (p. 2).
- **Problem:** The author's email is given as `houston@hubify.com`. This appears to be a non-institutional, potentially commercial, email address.
- **Fix:** The author should consider providing a more permanent academic contact identifier, such as an ORCID link, in addition to or instead of the current email address.

## Summary recommendation
**MAJOR REVISIONS**

This paper presents a comprehensive and statistically rigorous search for an environmental dependence of spiral galaxy chirality using the latest DESI data. The primary result, anchored on the peer-reviewed DESIVAST void catalog, is a convincing null detection. The strength of the paper lies in its extensive suite of robustness checks, cross-validations against multiple independent methods, and transparent handling of potential systematics, particularly the classifier bias inherited from its input catalog. However, the paper requires major revisions before it can be considered for publication. The most critical issue is its reliance on a non-peer-reviewed companion paper (Paper IV) for its primary data; publication must wait until Paper IV is accepted. Furthermore, the paper's structure should be significantly revised to present the strongest, primary result first, which would improve clarity and impact. The handling of a significant (3.4σ) discrepancy found between different galaxy tracers also needs to be sharpened, as it constitutes an important, albeit likely systematic, finding in its own right. Once these structural and contextual issues are addressed, this will be a valuable contribution to the literature, providing a stringent observational constraint for models of cosmic parity violation.
# P5 2026-06-04_1814pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 70.7s

---

# Referee Report on "Environmental Dependence of Spiral Chirality..."

## General Comments

This paper presents a detailed investigation into the environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1 and a large, pre-existing chirality catalog. The primary result is a null detection: the fraction of clockwise (CW) vs. counter-clockwise (CCW) spirals does not show a statistically significant dependence on the cosmic-web environment (void, wall, filament, cluster) at the sensitivity of the current data.

The analysis is, in large part, exceptionally thorough. The author performs an extensive series of robustness tests, cross-validations against multiple independent environment classifiers (V-Web, DESIVAST, Tempel+ FoF, ASTRA), and internal consistency checks. The careful treatment of a known systematic (a catalog-wide "monopole" offset from the input chirality catalog) by subtracting its predicted effect is a major strength of the analysis. The designation of the DESIVAST-anchored analysis as the "primary" path is well-justified and provides the paper's most robust constraint.

However, the paper has several significant issues that must be addressed before it can be considered for publication. The most critical is the heavy reliance on an unpublished companion work ("Paper IV") for the fundamental data (chirality labels) and the main systematic correction (the monopole offset). Furthermore, the paper contains numerous internal version-control artifacts that are inappropriate for a submitted manuscript. The theoretical discussion in the appendix is weak, and the treatment of redshift-space distortions (RSDs) in the secondary V-Web analysis needs to be presented more transparently. Finally, the paper's structure and length could be significantly improved to better highlight the primary scientific contribution.

The following detailed report outlines the required revisions.

---
## Detailed Findings

### ESSENTIAL

**P5-E1: Reliance on Unpublished Companion Work**
-   **Location:** Throughout the paper, e.g., Abstract (p. 1), Section II (p. 2), Section VI (p. 5).
-   **Problem:** The entire analysis is predicated on the chirality catalog and the catalog-wide monopole offset (∆fCW = −0.0026) derived in "Paper IV [3]", which is described as "not yet peer-reviewed". This makes it impossible for a referee or reader to independently assess the validity of the input data and the core systematic correction. The conclusions of the present paper are not verifiable without access to the methods and validation of Paper IV.
-   **Fix:** The paper must be made more self-contained. At a minimum, a new section or appendix must be added that summarizes the essential details from Paper IV. This should include: (1) A brief description of the classifier architecture and training. (2) The method used for Z2 test-time augmentation to ensure equivariance. (3) A summary of the validation tests performed on the classifier. (4) A clear derivation of the catalog-wide monopole offset and the evidence supporting its interpretation as a classifier bias rather than a cosmological signal. Ideally, Paper IV should be submitted concurrently and reviewed as a companion paper.

**P5-E2: Internal Versioning and Review Artifacts**
-   **Location:** Throughout the paper.
-   **Problem:** The manuscript is littered with internal version-control tags, audit logs, and notes to the author. This is unprofessional and unacceptable for a peer-reviewed publication.
-   **Examples:**
    -   p. 1, Dated line: `(R-upgraded-round9 close: 7 do-now fixes — title retitle, “strongest” softening, RSD anisotropy reframe, DESI`
    -   p. 1, Abstract: `(v0.1.44 PER-M1 clarification)`
    -   p. 1, Abstract: `per R-ext-GRO-M2`
    -   p. 8, Sec. VII.d: `(GEM-M1 closure)`
    -   p. 10, Sec. VIII: `(v0.1.40, GEM-M2 closure addressing R-multi-round2 pattern-008)`
    -   p. 18, Sec. XIII: `(v0.1.44 GEM-M1 + GPT-M3 + GRO-M1 3-way reframing)`
    -   p. 19, Conclusions: `(v0.1.44 GEM-m1 scope-locality caveat; R-ext-GRO-min1 reframing...)`
-   **Fix:** The author must perform a thorough search and remove *all* such artifacts from the manuscript before resubmission.

**P5-E3: Flawed Theoretical Model in Appendix**
-   **Location:** Appendix A (p. 20).
-   **Problem:** The toy EFT mapping is theoretically unsound as presented. The operator `L_parity ⊃ g_ϕ (∇i ϕ) (∇i ρ/ρ_bg) (L̂ · ẑ)` explicitly breaks rotational invariance with the `(L̂ · ẑ)` term. The author acknowledges this and other issues (gauge invariance of ρ and L̂) but the caveats do not fix the fact that the presented operator is ill-defined. Presenting a flawed operator, even as a "toy model", is misleading and detracts from the paper's empirical strengths.
-   **Fix:** Appendix A should be removed. If the author wishes to connect the results to theory, this should be done in a more schematic and pedagogical way in the main discussion, without writing down specific, incorrect Lagrangians. For example, the text could simply state that any parity-violating coupling between a pseudoscalar field and the density gradient would be constrained by this work, and then provide the order-of-magnitude estimate without the problematic operator formalism.

### MAJOR

**P5-M1: Paper Structure and Length**
-   **Location:** Overall structure.
-   **Problem:** The paper is 21 pages long, and its structure does not effectively communicate the main result. The primary, most robust analysis (the DESIVAST-anchored test) is buried in Section VIII, while the secondary, weaker, and more systematic-prone V-Web analysis is presented first (Section VI). The main text is also diluted by numerous secondary cross-checks (Sections IX, X) that, while valuable, distract from the core argument.
-   **Fix:** The paper should be restructured to improve clarity and focus.
    1.  Present the primary DESIVAST analysis (current Section VIII) first, immediately after the Data and Methods sections. This is the strongest and cleanest result and should be the focus.
    2.  Present the V-Web analysis (current Sections VI, VII) second, clearly framed as a supporting analysis with larger systematic uncertainties (RSDs, survey edge effects).
    3.  Move the additional cross-checks against external classifiers (Tempel+, T-Web, ASTRA; current Sections IX, X) to an appendix. These are important for robustness but are not central to the main DESI-based result.
    4.  This restructuring should allow the main text to be condensed to a more standard length of ~12-15 pages, making the paper more accessible and impactful.

**P5-M2: Redshift-Space Distortions (RSDs) in V-Web Analysis**
-   **Location:** Primarily Section XIII (p. 18), but relevant to Section IV (p. 3).
-   **Problem:** The V-Web analysis uses a tidal tensor classifier run on redshift-space positions. As the author correctly notes in the Limitations section, RSDs introduce an "anisotropic eigenvalue deformation" which is the dominant systematic for this method. However, this crucial caveat is buried on page 18. For the V-Web analysis to be interpreted correctly, this limitation must be made clear from the outset.
-   **Fix:**
    1.  In Section IV.A, where the V-Web algorithm is described, add a paragraph explicitly stating that the classification is performed in redshift space and briefly explaining how RSDs are expected to affect the tidal tensor eigenvalues and subsequent classification.
    2.  The abstract should also qualify the V-Web result by mentioning it is based on a redshift-space classification. The current text does not.

### MINOR

**P5-m1: Overly Specific Title**
-   **Location:** Title (p. 1).
-   **Problem:** The title is extremely long and reads more like a sentence from an abstract. It includes specific galaxy counts for subsets of the analysis, which is unnecessary detail for a title.
-   **Fix:** Shorten the title to be more concise while capturing the essence of the work. For example: "A Test of the Environmental Dependence of Spiral Galaxy Chirality in DESI Data Release 1".

**P5-m2: Inconsistent Use of Significance Metrics**
-   **Location:** p. 2, Robustness paragraph.
-   **Problem:** The text states: "The joint two-sample z-test on the bright-vs-dark fCW difference is |z| ≈ 3.4σ on the filament class...". This phrasing conflates the z-statistic from a two-sample test with a "sigma" deviation from a single-proportion null hypothesis, which are not directly comparable without qualification. While likely just a shorthand, it can be misleading.
-   **Fix:** Rephrase to be more precise. For example, "...is |z| ≈ 3.4, corresponding to a p-value of X" or "...is a 3.4σ-equivalent deviation". Alternatively, simply state the z-score and p-value.

**P5-m3: Abstract Clarity**
-   **Location:** Abstract (p. 1).
-   **Problem:** The abstract is very dense, packed with numerical results, σ-values, and internal jargon (e.g., "post-TTA equivariant"). It is difficult to parse for a non-expert.
-   **Fix:** Rewrite the abstract to focus more on the high-level findings and their implications. State the main result (no environmental dependence found), the key piece of evidence (the DESIVAST null result on ~57k void spirals), and the conclusion that observed deviations are consistent with a known instrumental systematic. The specific σ-values for each cosmic-web class can be left to the main text.

### NIT

**P5-N1: Email Address Format**
-   **Location:** p. 2, footnote.
-   **Problem:** The email address is given as `houston@hubify.com`. For an academic paper, an institutional or persistent email address (e.g., via ORCID) is preferred. If the author is independent, a professional address (e.g., via a personal domain or a standard provider) would be more conventional than a company-specific one, unless Hubify is a research-sponsoring entity.
-   **Fix:** Consider updating the contact email address to a more standard academic or professional format.

---
## Summary recommendation

**MAJOR REVISIONS**

The analytical work in this paper is of high quality, demonstrating a rigorous and comprehensive approach to testing a subtle astrophysical hypothesis. The author's diligence in performing and documenting a vast array of robustness checks is commendable. However, the paper in its current form is not acceptable for publication. The absolute reliance on an unpublished companion paper for its core inputs is a critical flaw that undermines the verifiability of the results. Additionally, the manuscript is marred by numerous unprofessional artifacts from the author's internal review process, and the paper's structure obscures its most significant findings. A significant restructuring, the removal of all internal tags, and the inclusion of essential methodological details from the companion work are required before the paper can be reconsidered.
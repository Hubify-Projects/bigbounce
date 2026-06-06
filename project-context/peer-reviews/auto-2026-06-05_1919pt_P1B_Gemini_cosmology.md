# P1B auto-2026-06-05_1919pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (8719 chars)
**Wall time**: 1336.9s

---

## Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Journal:** Physical Review D

This paper presents three technical analyses intended as a companion to a separate work (Paper I(a)) on Einstein-Cartan-Holst (ECH) cosmology. The analyses are: (1) a Markov Chain Monte Carlo (MCMC) analysis of the ΛCDM+ΔNeff model as a proxy for new radiation, (2) a validation of a NaMaster-based pseudo-Cℓ pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The technical work within each of the three sections appears to be sound. The MCMC analyses are well-converged, the pipeline validation is properly scoped, and the ALP consistency check is presented with appropriate and important caveats regarding fine-tuning and model-dependence. The author is commendably transparent about the limitations of each analysis, for instance by clearly stating that the ΔNeff and ALP analyses are not direct or unique tests of the ECH framework.

However, the paper suffers from significant structural problems and a lack of narrative cohesion that hinder its readability and impact. The three documented analyses are largely disconnected from one another and their collective relevance to the E-C-H program is not strongly established. The manuscript reads more like a collection of three separate technical notes than a single, unified companion paper. Substantial revisions are required before it can be considered for publication in Physical Review D.

---

### ESSENTIAL Revisions

**P1B-E1: Major Structural Reorganization Required (Sections III & V, Pages 3, 4, 6)**
*   **Problem:** The paper presents results from two distinct MCMC analyses: a ΛCDM+ΔNeff run (Table I) and a w₀wₐ run (Table II). The discussion of these two separate analyses is confusingly interwoven. Section III, which is titled "Stock-CAMB ΛCDM+ΔNeff MCMC", begins discussing the results of the w₀wₐ run ("Physics interpretation (Table II)...", p. 3) before that analysis has been properly introduced. Section V ("Cosmological Fits and Model Comparison"), which appears to be the intended home for the w₀wₐ analysis, then confusingly re-states the main results of the ΔNeff run. This structure makes the paper extremely difficult to follow.
*   **Required Fix:** The paper must be restructured to cleanly separate the two MCMC analyses. I recommend the following structure:
    1.  Section III: Focus exclusively on the ΛCDM+ΔNeff analysis. Present the motivation, methods, Table I, Figure 1, and all associated discussion and conclusions for this run.
    2.  Section IV: Introduce and discuss the w₀wₐ analysis. Present the motivation for this separate test (e.g., testing the quintom-B scenario), the methods, Table II, and all associated discussion.
    3.  Subsequent sections (NaMaster validation, ALP check) can then follow. This reorganization is essential for the clarity and logical flow of the manuscript.

### MAJOR Revisions

**P1B-M1: Justification for a Unified Companion Paper (Overall)**
*   **Problem:** The paper presents three disparate analyses. The author is explicit that the ΔNeff run is a generic proxy and that the ALP birefringence mechanism is not a distinctive ECH prediction. The NaMaster validation is a purely technical exercise. As such, the link between these analyses and the main ECH program described in "Paper I(a)" feels tenuous. The paper does not sufficiently justify why these three specific, largely independent analyses belong together in a single companion paper.
*   **Required Fix:** The introduction should be revised to provide a much stronger, more explicit justification for the selection and grouping of these three analyses. It must clearly articulate how each piece of work, despite its stated limitations, provides a necessary and complementary verification for the specific claims made in Paper I(a). Without a compelling narrative thread connecting the parts, the paper lacks the cohesion expected of a single publication.

**P1B-M2: Misleading Comparison to Other Torsion Models (Section III, Page 5)**
*   **Problem:** The "Independent cross-validation" subsection on page 5 compares the H₀ and σ₈ results from the paper's generic ΔNeff proxy run to those from Liu et al. [11], who analyze a specific Einstein-Cartan torsion model. The text notes that the parameters agree at the <1σ level. This comparison is potentially misleading. The underlying physical models are completely different; one adds a free-streaming radiation component (ΔNeff), while the other modifies gravity. Agreement on cosmological parameters between two different, poorly constrained models does not constitute a meaningful cross-validation.
*   **Required Fix:** This subsection should be removed or substantially rephrased. If the author wishes to keep it, it must be framed with extreme care, emphasizing that the models are physically distinct and that the parameter agreement is merely a coincidental observation, not a validation of either model.

### MINOR Revisions

**P1B-m1: Figure Caption Clarity (Figure 1, Page 5)**
*   **Problem:** The caption for Figure 1 states it contains "119,617 post-burnin samples, getdist-thinned from 176,240 raw". However, a simple calculation based on footnote 1 (p. 2) gives a post-burnin count of 176,240 * 0.7 = 123,368. The explanation for this discrepancy ("reflects additional getdist effective-sample weight-based thinning") is buried in the main text on page 3.
*   **Required Fix:** Move the explanation for the sample count directly into the caption of Figure 1 for clarity and to avoid reader confusion.

**P1B-m2: Inconsistent "Fiducial" ALP Parameters (Section VI, Page 7)**
*   **Problem:** On page 7, Eq. (3) calculates β ≈ 0.29° for a set of parameters including `m ≈ 2H₀` and `Δφ/fₐ ≈ 1.07`. Immediately after, the text states "The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H₀, Δφ/fₐ ≈ 1.0." It is unclear which set of parameters is truly "fiducial" and why two different examples are used back-to-back.
*   **Required Fix:** Clarify the fiducial parameter choice. Use one consistent set of parameters for the main illustrative example in the text.

**P1B-m3: Incomplete Bibliography Entry (Reference [20], Page 10)**
*   **Problem:** The citation for the Cobaya paper [20] is formatted incorrectly and is missing the publication year. It reads "Journal of Cosmology and Astroparticle Physics 05 (057), 057".
*   **Required Fix:** Correct the citation. The correct format should be similar to "J. Cosmol. Astropart. Phys. 05 (2021) 057".

### NIT-PICKS (Cosmetic)

**P1B-N1: Redundant Language in Abstract (Page 1)**
*   **Problem:** The abstract contains the phrase "...both in kms¯¹ Mpc-1)". The unit is written with a superscript -1 and then a text -1.
*   **Required Fix:** Correct to "...both in km s⁻¹ Mpc⁻¹)".

---

## Summary recommendation

**MAJOR REVISIONS**

The paper contains sound technical work and demonstrates a high level of scientific integrity, particularly in its careful scoping and disclosure of limitations. However, its current structure is deeply flawed, making the central arguments difficult to follow. The essential task for the author is to completely reorganize the manuscript to present the different MCMC analyses in a clear, sequential manner. Furthermore, a stronger justification for why these three specific analyses constitute a single, cohesive companion paper is needed. Once these significant structural and narrative issues are addressed, the paper could be a valuable technical contribution.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the revised review, incorporating the new findings from the second pass.

================================================================
## Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Journal:** Physical Review D

### General Comments

This paper presents three technical analyses intended as a companion to a separate work (Paper I(a)) on Einstein-Cartan-Holst (ECH) cosmology. The analyses are: (1) a Markov Chain Monte Carlo (MCMC) analysis of the ΛCDM+ΔNeff model as a proxy for new radiation, (2) a validation of a NaMaster-based pseudo-Cℓ pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The technical work within each of the three sections appears to be sound. The MCMC analyses are well-converged, the pipeline validation is properly scoped, and the ALP consistency check is presented with appropriate and important caveats regarding fine-tuning and model-dependence. The author is commendably transparent about the limitations of each analysis, for instance by clearly stating that the ΔNeff and ALP analyses are not direct or unique tests of the ECH framework. The arithmetic and internal consistency of the reported values are excellent.

However, the paper suffers from significant structural problems and a lack of narrative cohesion that hinder its readability and impact. The three documented analyses are largely disconnected from one another and their collective relevance to the E-C-H program is not strongly established. The manuscript reads more like a collection of three separate technical notes than a single, unified companion paper. Substantial revisions are required before it can be considered for publication in Physical Review D.

---

### ESSENTIAL Revisions

**P1B-E1: Major Structural Reorganization Required (Sections III & V, Pages 3, 4, 6)**
*   **Problem:** The paper presents results from two distinct MCMC analyses: a ΛCDM+ΔNeff run (Table I) and a w₀wₐ run (Table II). The discussion of these two separate analyses is confusingly interwoven. Section III, which is titled "Stock-CAMB ΛCDM+ΔNeff MCMC", begins discussing the results of the w₀wₐ run ("Physics interpretation (Table II)...", p. 3) before that analysis has been properly introduced. Section V ("Cosmological Fits and Model Comparison"), which appears to be the intended home for the w₀wₐ analysis, then confusingly re-states the main results of the ΔNeff run. This structure makes the paper extremely difficult to follow.
*   **Required Fix:** The paper must be restructured to cleanly separate the two MCMC analyses. I recommend the following structure:
    1.  Section III: Focus exclusively on the ΛCDM+ΔNeff analysis. Present the motivation, methods, Table I, Figure 1, and all associated discussion and conclusions for this run.
    2.  Section IV: Introduce and discuss the w₀wₐ analysis. Present the motivation for this separate test (e.g., testing the quintom-B scenario), the methods, Table II, and all associated discussion.
    3.  Subsequent sections (NaMaster validation, ALP check) can then follow. This reorganization is essential for the clarity and logical flow of the manuscript.

### MAJOR Revisions

**P1B-M1: Justification for a Unified Companion Paper (Overall)**
*   **Problem:** The paper presents three disparate analyses. The author is explicit that the ΔNeff run is a generic proxy and that the ALP birefringence mechanism is not a distinctive ECH prediction. The NaMaster validation is a purely technical exercise. As such, the link between these analyses and the main ECH program described in "Paper I(a)" feels tenuous. The paper does not sufficiently justify why these three specific, largely independent analyses belong together in a single companion paper.
*   **Required Fix:** The introduction should be revised to provide a much stronger, more explicit justification for the selection and grouping of these three analyses. It must clearly articulate how each piece of work, despite its stated limitations, provides a necessary and complementary verification for the specific claims made in Paper I(a). Without a compelling narrative thread connecting the parts, the paper lacks the cohesion expected of a single publication.

**P1B-M2: Misleading Comparison to Other Torsion Models (Section III, Page 5)**
*   **Problem:** The "Independent cross-validation" subsection on page 5 compares the H₀ and σ₈ results from the paper's generic ΔNeff proxy run to those from Liu et al. [11], who analyze a specific Einstein-Cartan torsion model. The text notes that the parameters agree at the <1σ level. This comparison is potentially misleading. The underlying physical models are completely different; one adds a free-streaming radiation component (ΔNeff), while the other modifies gravity. Agreement on cosmological parameters between two different, poorly constrained models does not constitute a meaningful cross-validation.
*   **Required Fix:** This subsection should be removed or substantially rephrased. If the author wishes to keep it, it must be framed with extreme care, emphasizing that the models are physically distinct and that the parameter agreement is merely a coincidental observation, not a validation of either model.

### MINOR Revisions

**P1B-m1: Figure Caption Clarity (Figure 1, Page 5)**
*   **Problem:** The caption for Figure 1 states it contains "119,617 post-burnin samples, getdist-thinned from 176,240 raw". However, a simple calculation based on footnote 1 (p. 2) gives a post-burnin count of 176,240 * 0.7 = 123,368. The explanation for this discrepancy ("reflects additional getdist effective-sample weight-based thinning") is buried in the main text on page 3.
*   **Required Fix:** Move the explanation for the sample count directly into the caption of Figure 1 for clarity and to avoid reader confusion.

**P1B-m2: Inconsistent "Fiducial" ALP Parameters (Section VI, Page 7)**
*   **Problem:** On page 7, Eq. (3) calculates β ≈ 0.29° for a set of parameters including `m ≈ 2H₀` and `Δφ/fₐ ≈ 1.07`. Immediately after, the text states "The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H₀, Δφ/fₐ ≈ 1.0." It is unclear which set of parameters is truly "fiducial" and why two different examples are used back-to-back.
*   **Required Fix:** Clarify the fiducial parameter choice. Use one consistent set of parameters for the main illustrative example in the text.

**P1B-m3: Incomplete Bibliography Entry (Reference [20], Page 10)**
*   **Problem:** The citation for the Cobaya paper [20] is formatted incorrectly and is missing the publication year. It reads "Journal of Cosmology and Astroparticle Physics 05 (057), 057".
*   **Required Fix:** Correct the citation. The correct format should be similar to "J. Cosmol. Astropart. Phys. 05 (2021) 057".

**P1B-m4: Incorrect Section Reference (Page 8)**
*   **Problem:** In the "NaMaster pipeline validation" summary paragraph on page 8, the text "(see §VI body text)" refers to the discussion of the pipeline bias.
*   **Required Fix:** This discussion actually occurs in Section IV (page 5). The reference should be corrected to "§IV".

**P1B-m5: Unquantified Claim about Pipeline Bias (Page 5)**
*   **Problem:** On page 5, the text states the recovered pipeline bias of 0.032° is "consistent with the apodized-mask bias expected from a 2° apodization scale".
*   **Required Fix:** This claim is unquantified. The paper should either provide a simple calculation or a citation for the *expected* bias from such a mask, or rephrase the statement to be qualitative.

### NIT-PICKS (Cosmetic)

**P1B-N1: Redundant Language in Abstract (Page 1)**
*   **Problem:** The abstract contains the phrase "...both in kms¯¹ Mpc-1)". The unit is written with a superscript -1 and then a text -1.
*   **Required Fix:** Correct to "...both in km s⁻¹ Mpc⁻¹)".

---

## Summary recommendation

**MAJOR REVISIONS**

The paper contains sound technical work and demonstrates a high level of scientific integrity, particularly in its careful scoping and disclosure of limitations. However, its current structure is deeply flawed, making the central arguments difficult to follow. The essential task for the author is to completely reorganize the manuscript to present the different MCMC analyses in a clear, sequential manner. Furthermore, a stronger justification for why these three specific analyses constitute a single, cohesive companion paper is needed. Once these significant structural and narrative issues are addressed, the paper could be a valuable technical contribution.
# P1B D2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=b166f4c0 pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 174.8s

---

## Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program...

This paper presents a technical companion documenting three verification analyses related to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model, serving as a null test for an extra radiation-like degree of freedom; (2) a Monte Carlo validation of a NaMaster pseudo-Cℓ pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-written, methodologically rigorous, and transparent. The authors take great care to clearly define the scope of each analysis, explicitly stating what is and is not being claimed. Caveats and potential systematics are not only disclosed but are often highlighted prominently, which is a model of good scientific practice. The level of detail provided, particularly regarding the MCMC configurations, pipeline validation, and reproducibility materials, is commendable and meets the highest standards for a technical paper. The distinction between different statistical quantities (e.g., pipeline recovery bias vs. sky detection significance) is handled with a clarity that is unfortunately rare.

While the overall quality is excellent, there is one major structural issue that hinders the readability and logical flow of the paper. Addressing this, along with a few minor points, would significantly improve the manuscript.

---
### Findings

#### ESSENTIAL
(None)

#### MAJOR

**P1B-M1: Misplaced discussion of `w0-wa` analysis**
*   **Section + page number:** Section III, page 4.
*   **Specific problem:** Section III is titled "STOCK-CAMB ACDM+ΔNeff MCMC: GENERIC RADIATION-PROXY TEST". Its scope is clearly defined as a null test of the ΔNeff parameter using the chains summarized in Table I. However, a large portion of page 4, starting with the paragraph "Physics interpretation (Table II)", is dedicated to a detailed discussion of a completely different analysis: a `w0-wa` dark energy model fit using the `iter2` chain, whose results are in Table II. This discussion, including the subsequent "Caveats" subsection, is entirely out of place in Section III. It conflates two separate analyses with different models, datasets, and systematics (most notably the SN-overlap issue unique to the `w0-wa` chain). This severely disrupts the logical flow and makes the paper difficult to follow.
*   **Required fix:** Move the entire block of text from "Physics interpretation (Table II)..." to the end of the "Caveats" subsection on page 4 out of Section III. This content should be consolidated and placed within Section V.C, which is correctly titled "wowa cross-check with stated SN-overlap systematic". This restructuring will ensure that Section III remains focused on the clean, self-contained ΔNeff analysis, and the more complex, heavily-caveated `w0-wa` diagnostic is discussed in the appropriate model comparison section.

#### MINOR

**P1B-m1: Ambiguous cross-reference in Appendix C**
*   **Section + page number:** Appendix C, page 19, Configuration (ii).
*   **Specific problem:** The text states, "The [4,60] continuous-prior rerun (below) is the primary coupling-inference result...". The use of "(below)" is ambiguous. While the continuous-prior configuration is indeed described later in the appendix, it is not immediately following, and it is part of a different paragraph block.
*   **Required fix:** For clarity, replace the ambiguous "(below)" with a more specific reference. For example: "(the `c5_continuous` chain detailed in the 'Sampled parameters and priors' paragraph below)".

#### NIT (Cosmetic)

**P1B-N1: Figure 3 caption detail**
*   **Section + page number:** Section IV, page 8, Figure 3 caption.
*   **Specific problem:** The caption notes that an error bar for the `fsky = 0.32` point was missing from the original run and had to be computed in a dedicated rerun.
*   **Required fix:** This level of internal process documentation is not necessary for the final publication. The authors should simply update the plot to include the computed error bar and remove the sentence explaining its provenance from the caption. The current text is acceptable if the plot cannot be changed, but a fully updated plot would be cleaner.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper represents a high-quality contribution, characterized by its rigor, transparency, and thoroughness. The analyses are well-executed, and the results are presented with appropriate context and caveats. The reproducibility package is exemplary. The paper is almost ready for publication in Physical Review D.

However, the structural issue identified in **P1B-M1** is significant enough to warrant a major revision. The misplacement of the `w0-wa` analysis disrupts the paper's logical structure and clarity. Fortunately, this should be a straightforward issue to fix by reorganizing the content as recommended. Once this structural problem is addressed, the paper will be a model for how to write a technical verification companion and will be an excellent candidate for publication.
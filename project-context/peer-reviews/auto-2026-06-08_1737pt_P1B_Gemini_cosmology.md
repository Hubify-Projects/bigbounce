# P1B auto-2026-06-08_1737pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 123.7s

---

## Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program..."

**Manuscript ID:** [Assigned by editor]
**Author:** Houston Golden
**Journal:** Physical Review D

This paper presents technical verification material for a separate work (Paper I(a)) on Einstein-Cartan-Holst (ECH) cosmology. It documents three distinct analyses: (1) a `ΛCDM+ΔNeff` MCMC analysis as a null test, (2) a `NaMaster` pipeline validation for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is generally well-executed in terms of the individual analyses. The author is commendably transparent about the scope and limitations of each test, providing clear "scope statements" and caveats. The level of detail, particularly in the MCMC sample counting, parameter degeneracy checks, and the ALP fine-tuning disclosure, is excellent and supports the goal of reproducibility. The provision of a public code repository is a significant strength.

However, the manuscript suffers from a major structural flaw in its presentation of a fourth, unannounced analysis concerning a `w0-wa` cosmological model. This, along with several other points of clarification, must be addressed before the paper can be considered for publication.

---

### ESSENTIAL Revisions

*   **P1B-E1: Major Structural Issue with the `w0-wa` Analysis**
    *   **Location:** Abstract (p. 1), Introduction (p. 2), Section III (p. 3), Table II (p. 4), Conclusions (p. 8).
    *   **Problem:** The abstract and introduction explicitly state that three analyses are documented. However, the paper presents a fourth, highly significant analysis of a `w0-wa` model, which finds a >4σ departure from ΛCDM (Table II, `wo` departs by +4.3σ). This result is introduced abruptly in the middle of the paper (p. 3) without any framing, given a detailed summary in Table II, and then confusingly mentioned again in the "Forward" section of the conclusion as if it were a future result. A result of this significance cannot be buried in a companion paper without being a central part of its narrative.
    *   **Required Fix:** The author must fundamentally restructure the paper. There are two options:
        1.  **Elevate the `w0-wa` result:** If this result is robust and central to the author's program, it must be announced in the title and abstract, properly introduced, and the paper's narrative must be rewritten to accommodate it as a primary finding.
        2.  **Remove the `w0-wa` result:** If the result is preliminary or intended for a separate publication, it must be removed entirely from this manuscript (including Table II and all associated discussion). A companion paper focused on verification is not the appropriate venue to introduce a standalone >4σ tension.

---

### MAJOR Revisions

*   **P1B-M1: Confusing Sample Count in Figure 1 Caption**
    *   **Location:** Figure 1 Caption (p. 5).
    *   **Problem:** The caption states "119,617 post-burnin samples, getdist-thinned from 176,240 raw". This is confusing because footnote 1 (p. 3) establishes the post-burnin count for this chain as ≈123,368. While the text explains the "getdist effective-sample weight-based thinning," the primary number in a figure caption should be the total number of samples used to generate the posteriors (the post-burnin count).
    *   **Required Fix:** Modify the caption to be unambiguous. For example: "Full-tension MCMC corner plot. The posteriors are generated from 123,368 post-burnin samples (derived from 176,240 raw samples). The 119,617 count shown reflects additional getdist-based thinning for plotting."

*   **P1B-M2: Unclear Symbolic Form of Birefringence Equation**
    *   **Location:** Section VI, Equation (3) (p. 7).
    *   **Problem:** Equation (3) is presented as `β ≈ (α_EM * 8 / 4π) * 1.07 ≈ 0.29°`. This form improperly mixes the general symbolic expression with specific numerical values (`C_αγ=8`, `Δφ/fa=1.07`). This makes the underlying physics formula difficult to parse.
    *   **Required Fix:** First, state the general symbolic equation clearly, e.g., `β = (α_EM / 4π) * C_αγ * (Δφ/fa)`. Then, show the numerical evaluation for the specific parameter choices as a separate step.

---

### MINOR Revisions

*   **P1B-m1: Inappropriate Internal History Language**
    *   **Location:** Section III, "Physics interpretation (Table II)" (p. 3).
    *   **Problem:** The text states, "An earlier count erroneously quoted '98.6% quintom-B' weight". Language referring to previous (presumably unpublished) errors is not suitable for a formal publication.
    *   **Required Fix:** Remove this sentence and simply state the correct finding from the converged chain directly.

*   **P1B-m2: Disorganized Narrative Flow**
    *   **Location:** Pages 3-4.
    *   **Problem:** The text discussing the MCMC results jumps from the `ΔNeff` analysis (Table I) to the `w0-wa` analysis (Table II), and then back to a detailed check of the `H0` tension in the `ΔNeff` run. This makes the logic difficult to follow.
    *   **Required Fix:** Restructure the text to discuss each analysis in a self-contained manner. Complete the discussion of the `ΔNeff` run (including the `H0` tension check) before introducing the `w0-wa` analysis (if it is to be kept).

*   **P1B-m3: Potentially Inaccurate Scaling Relation for ALP Displacement**
    *   **Location:** Section VII (p. 8).
    *   **Problem:** The text claims that "at fixed β = 0.342°, Δφ/fa ∝ 1/θi along the underdamped trajectory". The total displacement `Δφ` from recombination to today is a non-trivial integral of the equation of motion, and its dependence on the initial condition `θi` is more complex than simple proportionality.
    *   **Required Fix:** Justify this scaling relation or rephrase it as a qualitative statement or an approximation. For example: "...a reduction in `θi` requires a corresponding increase in `C_αγ` to hold the product `C_αγ Δφ/fa` constant."

---

### NIT (Cosmetic)

*   **P1B-N1: Future Date on Manuscript**
    *   **Location:** Page 1.
    *   **Problem:** The date is listed as "(Dated: 2026-06-08 PDT)".
    *   **Required Fix:** Correct this to the actual date of submission.

---

## Summary recommendation

**MAJOR REVISIONS**

This manuscript provides a valuable and transparent technical record of several cosmological analyses. The author's commitment to reproducibility and careful scoping of claims is commendable. However, the paper is critically undermined by the inclusion of a major, unannounced result concerning a >4σ tension with ΛCDM in a `w0-wa` model. This structural problem makes the paper's narrative incoherent and buries a potentially significant finding in an inappropriate context.

The paper can be reconsidered for publication in Physical Review D only after the author has fundamentally restructured the manuscript to either properly feature the `w0-wa` analysis as a central result or remove it entirely. The other required revisions concerning clarity and presentation must also be addressed.
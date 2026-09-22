# P2 R-CONFIRM-2026-09-22 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-3.1-pro-preview`
**Input PDF**: `research/focused_paper_source_integration/02_full_draft.pdf` sha256=d3afe79fe70ce13cee5ec8149e84c4b42c78224ca6a90569058ec501222f5c2f pages=12
**Review packet(s)**: `4560f267b77390cf094814d5d4c14497ddcfbe7c6f4c43c4ba797e7143fb3166`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 193.9s

---

This is a referee report for the manuscript "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping" submitted to Physical Review D. 

The author presents a rigorous re-evaluation of the local non-Gaussianity amplitude $f_{\rm NL}^{\rm local}$ generated during a matter-dominated contracting phase in bounce cosmology. By exactly re-summing the four cubic vertices of the Maldacena action, the author derives $f_{\rm NL}^{\rm local} = -35/16$, resolving a historical factor-of-two discrepancy in the literature (which previously quoted $-35/8$). The paper then maps this exact shape to the SPHEREx multi-tracer bispectrum sensitivity, carefully separating the exact algebraic results from the conditional observational forecasts and nuisance marginalizations.

The algebraic derivation is exceptionally well-documented, and my manual verification of the polynomial coefficients, the squeezed limit, the equilateral limit, and the folded limit confirms the author's exact-fraction results perfectly. The paper's strict demarcation between the exact theoretical benchmark and the completion-dependent observational mapping is highly commendable and meets the rigorous standards of this journal. 

However, there are a few missing citations for quantitative comparisons, a leaked internal script name in the text, and a version mismatch in the reproducibility artifacts that must be corrected before publication.

### Findings

**ESSENTIAL (Must be fixed for acceptance)**
*   **ID: P2-E1**
    *   **Location:** DATA AND CODE AVAILABILITY, page 7
    *   **Problem:** Provenance surface version mismatch. The text explicitly states: "That deposit archives the reviewed v1.7.125 release PDF and source (the exact bytes reviewed at that release); the present manuscript is v1.7.130, 5 patch releases ahead, and will be added to the same Zenodo record as a new version on the next re-stage." This violates the requirement that the provided DOI must resolve to the exact bytes of the manuscript currently under review. 
    *   **Required Fix:** Update the Zenodo deposit to freeze and archive the exact v1.7.130 artifacts, and update the DOI in the text to point to this current release.

**MAJOR (Significant revision required)**
*   **ID: P2-M1**
    *   **Location:** Section II.C, page 3
    *   **Problem:** Uncomputed quantitative claim without citation. The text states: "Existing scaling arguments suggest percent-level changes, but their coefficient requires evaluating the four cubic integrals..." No citation is provided for the "existing scaling arguments."
    *   **Required Fix:** Provide the appropriate literature citation(s) for these scaling arguments.
*   **ID: P2-M2**
    *   **Location:** Section IV, page 5
    *   **Problem:** Uncomputed quantitative claim without citation. The text states: "The approximately 34.7% bias-marginalized gain over the real-space calculation... is materially larger than the roughly 18% gain quoted for an already-redshift-space monopole-to-multipole comparison..." There is no citation indicating where this 18% gain is quoted (presumably Heinrich et al. or a similar SPHEREx forecast).
    *   **Required Fix:** Add the specific citation for the 18% gain figure.
*   **ID: P2-M3**
    *   **Location:** Section VII, page 6
    *   **Problem:** Undefined jargon / leaked script name. The text states: "Omitting fingers-of-God damping makes the absolute C14 information gain optimistic." The term "C14" is used as a standalone noun without definition in the main text; it appears to be a leak of the script filename `c14_rsd_multipole_fisher.py` mentioned in the Data Availability section.
    *   **Required Fix:** Replace "C14" with descriptive physics text (e.g., "redshift-space multipole").

**NIT (Cosmetic)**
*   **ID: P2-N1**
    *   **Location:** Figure 1, page 2
    *   **Problem:** Plotting limits error. The equilateral marker (orange triangle) is evaluated at $B_{NL} = -255/128 \approx -1.992$, but the y-axis top limit is $-2.000$. Consequently, the marker is plotted outside the upper bounding box of the axis.
    *   **Required Fix:** Expand the y-axis limits (e.g., up to $-1.950$) so the equilateral marker sits cleanly inside the plot area.

## Summary recommendation
MINOR REVISIONS

The core physics, algebraic derivations, and statistical mappings in this paper are outstanding and mathematically flawless. The resolution of the historical $f_{\rm NL}$ discrepancy is a valuable contribution to the literature, and the exact-fraction bookkeeping is highly rigorous. The required revisions are purely administrative and textual: updating the Zenodo DOI to match the current manuscript version, adding two missing citations for external quantitative comparisons, fixing a leaked script name in the prose, and adjusting a figure axis. Once these minor corrections are made, the paper will be ready for acceptance.
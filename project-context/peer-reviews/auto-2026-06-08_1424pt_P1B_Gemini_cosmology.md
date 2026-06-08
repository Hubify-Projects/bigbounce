# P1B auto-2026-06-08_1424pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 135.0s

---

## Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."

**Manuscript ID:** [Assigned by journal]
**Authors:** Houston Golden
**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

### Summary of the Paper
This manuscript serves as a technical companion to a separate work (Paper I(a)) on Einstein-Cartan-Holst (ECH) spin-torsion cosmology. It documents three distinct verification analyses:
1.  An MCMC analysis of the `ACDM+ΔNeff` model using stock CAMB, presented as a null-consistency test for an extra radiation-like component.
2.  A Monte Carlo validation of a `NaMaster`-based pseudo-C_ell pipeline for measuring cosmic birefringence, demonstrating unbiased recovery of an injected signal.
3.  A consistency check showing that a standard spectator axion-like particle (ALP) model can accommodate the currently observed birefringence signal, while carefully noting the required fine-tuning and model-building challenges.

The paper also includes a fourth, less well-integrated analysis of a `w0wa` dark energy model. The author is commendably transparent about the scope and limitations of each analysis, consistently distinguishing between pipeline validation and sky detection, and between generic model tests and specific ECH predictions.

### General Assessment
The manuscript presents a set of detailed and rigorous technical verifications. The quality of the analyses, the careful statistical treatment, and the high level of transparency regarding scope, limitations, and potential model-building issues (e.g., ALP fine-tuning) are commendable. The provision of a public repository with code and configuration files is excellent practice.

However, the manuscript suffers from a significant structural and narrative problem that currently makes it unsuitable for publication in Physical Review D. The presentation is disjointed, particularly with the introduction of an undocumented `w0wa` analysis and the confusing separation of the `ΔNeff` MCMC setup and results.

With a major structural revision, the paper could constitute a valuable contribution, showcasing the detailed verification work necessary to support theoretical cosmology programs. The recommendation is therefore for **MAJOR REVISIONS**.

---
### Detailed Findings

#### ESSENTIAL Revisions

**P1B-E1: Manuscript Date**
- **Location:** Page 1, under the author's name.
- **Problem:** The paper is dated "2026-06-08 PDT". This future date is inappropriate for a manuscript under review and suggests it is a preliminary draft.
- **Required Fix:** Replace the date with the current submission date.

**P1B-E2: Major Structural and Narrative Reorganization**
- **Location:** Primarily Sections III, V, and the discussion of Table II.
- **Problem:** The paper's narrative is disjointed and difficult to follow.
    1.  The abstract and introduction frame the paper around three specific analyses. However, a fourth analysis of a `w0wa` model (Table II) is introduced abruptly on page 3 and presented on page 4 without any prior motivation or framing. This makes it seem like an unrelated and out-of-place result.
    2.  The discussion of the primary `ACDM+ΔNeff` MCMC analysis is split confusingly across Section III ("Stock-CAMB ACDM+Neff MCMC...") and Section V ("Cosmological Fits and Model Comparison"). Section III introduces the run, while Section V presents the results, leading to unnecessary fragmentation.
- **Required Fix:** The paper must be restructured to present a clear, linear narrative. I recommend the following structure:
    1.  Create a new, unified section, for example, "MCMC Analysis of Extended Cosmological Models".
    2.  This section should contain two distinct subsections:
        - **Subsection A: `ACDM+ΔNeff`: A Generic Radiation-Proxy Test.** This subsection should contain all material related to the `ΔNeff` analysis, including the setup from the current Sec. III and the results from the current Sec. V, along with Table I and Figure 1.
        - **Subsection B: `w0wa`: A Test of the Dark Energy Dynamics.** This subsection must begin with a proper introduction motivating the analysis (e.g., as a test for quintom behavior relevant to the bounce scenarios discussed in the main Paper I(a)). It should then present the results from Table II and the associated discussion.
    3.  The abstract and introduction must be updated to reflect this four-part structure, properly introducing the `w0wa` analysis as a planned component of the verification work. This will transform the paper from a confusing collection of notes into a coherent technical report.

---
#### MINOR Revisions

**P1B-M1: Figure Caption Clarity**
- **Location:** Page 5, Figure 1 Caption.
- **Problem:** The caption states the plot contains "119,617 post-burnin samples, getdist-thinned from 176,240 raw". However, footnote 1 on page 2 calculates the post-burnin sample count as ~123,368. The text on page 3 explains this discrepancy as "additional getdist effective-sample weight-based thinning". This explanation should be in the caption itself for clarity.
- **Required Fix:** Modify the caption to be self-contained. For example: "Full-tension MCMC corner plot. The plot shows 119,617 samples, which result from applying getdist's effective-sample weight-based thinning to the 123,368 post-burn-in samples (derived from 176,240 raw samples)."

**P1B-M2: Confusing Cross-Paper Citation**
- **Location:** Page 2, Introduction, "Cross-paper citations" paragraph.
- **Problem:** The text states: "When this companion reports MCMC values (H₀, σ₈, etc.) that are referenced in the main paper, those values come from Secs. III and V here." This is confusing because it's not clear why two separate sections would be the source.
- **Required Fix:** This issue will likely be resolved by implementing the essential structural revision (P1B-E2). The sentence should be updated to point to the new, single, well-defined section containing all MCMC results.

---
#### NIT (Cosmetic)

**P1B-N1: Precision in Table I**
- **Location:** Page 3, Table I.
- **Problem:** The "Worst R-1" value for the "Full-tension" column is listed as "0.001". Footnote `a` gives the more precise value of `9.74 x 10⁻⁴`.
- **Required Fix:** For consistency, consider reporting the value in the table as "0.0010" or "<0.001" to better reflect the precision mentioned in the footnote, or simply leave as is, as it's a minor point.

---
## Summary recommendation
**MAJOR REVISIONS**

This manuscript contains high-quality, rigorous, and transparently reported technical work that is valuable for the cosmology community. The author's careful attention to scoping, limitations, and reproducibility is exemplary. However, the paper's current structure significantly obscures the content and narrative flow, preventing it from meeting the publication standards of Physical Review D. The abrupt inclusion of the `w0wa` analysis and the fragmented discussion of the `ΔNeff` MCMC must be addressed. If the authors undertake the essential structural reorganization outlined above, the resulting manuscript would be a strong candidate for publication.
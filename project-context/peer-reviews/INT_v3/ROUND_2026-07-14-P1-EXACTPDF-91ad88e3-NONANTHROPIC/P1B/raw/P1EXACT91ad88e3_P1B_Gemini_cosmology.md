# P1B P1EXACT91ad88e3 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1B/frozen/arxiv/paper1b_mcmc_companion.pdf` md5=246b407b pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 142.5s

---

## Referee Report on "Reproducible Cosmological Proxy and Pipeline Checks: Stock-CAMB ΛCDM+ΔNeff MCMC, Synthetic NaMaster Recovery, and a Generic Spectator-ALP Birefringence Fit"

This paper presents three self-contained computational studies focused on reproducibility and consistency checks within modern cosmology. The studies are: (1) a Markov Chain Monte Carlo (MCMC) analysis of the ΛCDM+ΔNeff model using stock CAMB and public data, (2) a synthetic pipeline validation for cosmic birefringence measurements using NaMaster, and (3) a consistency check of a generic spectator axion-like-particle (ALP) model against published birefringence data.

The authors are commendably clear and upfront about the limited scope of their work. They repeatedly emphasize that these are proxy, pipeline, and consistency checks, not new detections or evidence for specific beyond-Standard-Model theories like Einstein-Cartan-Holst gravity. This framing is maintained consistently throughout the manuscript. The level of detail provided for reproducibility, including explicit sample counts, bug-fix disclosures, and links to code/data repositories, is exemplary and sets a high standard. The numerical calculations that were checked appear to be correct, and the conclusions drawn are appropriately cautious and well-supported by the analyses presented.

While the paper is of high quality, there are a few essential and major points that must be addressed before it can be considered for publication in Physical Review D.

---

### ESSENTIAL Revisions

**P1B-E1: Placeholder Reference for Companion Paper**
*   **Section:** I. Introduction (p. 1), VII. Conclusions (p. 15), References (p. 20)
*   **Problem:** The paper repeatedly cites a companion paper, "Paper I(a)", using a placeholder arXiv identifier: `[arXiv:XXXX.XXXXX]`. This appears as reference [1]. A submitted manuscript cannot rely on placeholder references for context, even if the authors claim the present work is "logically separate." The context provided by the companion paper (e.g., the origin of the minimal-contact operator) is part of the scientific motivation.
*   **Required Fix:** Replace the placeholder with a valid, citable reference (e.g., a submitted manuscript's arXiv ID). If the companion paper is not yet available on a public server, all context-setting material must be integrated into this manuscript to make it fully self-contained, or the references must be removed.

**P1B-E2: Stale Git Commit Hash in Reproducibility Section**
*   **Section:** Data and Code Availability (p. 16)
*   **Problem:** The paper states: "current snapshot commit: b22f8cc9". However, the reviewer metadata indicates that the version under review corresponds to a later commit (`91ad88e3`). This discrepancy undermines the otherwise excellent reproducibility framework. The version of the paper and the version of the code repository it documents must be perfectly synchronized at the time of publication.
*   **Required Fix:** Update the git commit hash in the manuscript to the exact hash corresponding to the version of the code and results presented in the final, submitted draft.

---

### MAJOR Revisions

**P1B-M1: Ambiguity in NaMaster Estimator Normalization**
*   **Section:** IV. Data Methods: CMB E-B Analysis (p. 7)
*   **Problem:** Equation (4) defines the χ² estimator used to recover the birefringence angle β. The signal template is given as `(1/4) sin(4β) CEE,tmpl`. The canonical expression for the rotation-induced EB power spectrum is `CEB = (1/2) sin(4β) (CEE - CBB)`. In the `CBB -> 0` limit, this becomes `(1/2) sin(4β) CEE`. The paper's expression differs by a factor of 2. The text asserts that "the explicit factor of 1/4 is the standard cosmic-rotation EB normalization... and is not omitted." This claim is not standard and requires explicit justification. Is there a non-standard definition of the power spectrum or the χ² being used? Or is the template being fit to something other than the decoupled `CEB`? Without a clear derivation or reference for this normalization, the results of the NaMaster analysis, particularly the ~12% multiplicative bias, are difficult to interpret and reproduce.
*   **Required Fix:** Provide a clear, step-by-step derivation of the `(1/4) sin(4β)` factor in the estimator, starting from the transformation of the Stokes parameters and the definition of the power spectra. Alternatively, if this is a typo, correct the equation to use the standard `(1/2) sin(4β)` prefactor and verify that this does not change the numerical results or conclusions of Section IV. If the code indeed uses `1/4`, the text must explain precisely why this choice was made and how it relates to the canonical formalism.

---

### MINOR Revisions

None.

---

### NITs (Cosmetic)

None.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper represents a valuable contribution to the practice of computational cosmology, emphasizing rigor, transparency, and reproducibility. The analyses are thorough, and the conclusions are stated with appropriate scientific caution. The quality of the documentation is exceptionally high. However, the manuscript in its current form is not publishable due to the use of a placeholder reference and a stale code repository hash, which are essential for the paper's integrity. Furthermore, a key equation in the pipeline validation analysis contains a non-standard normalization that must be clarified or corrected. Once these issues are satisfactorily addressed, the paper should be suitable for publication in Physical Review D.
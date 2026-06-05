# P4 2026-06-04_R5clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 77.1s

---

# Referee Report on Paper P4

## General Comments

This paper presents a detailed and rigorous analysis of galaxy chirality on a survey-scale dataset from the DESI Legacy Imaging Surveys. The primary result is a null detection of an ℓ=1 angular dipole in the galaxy chirality field, which constrains isotropy-breaking signatures in the late universe. The authors perform an exceptionally thorough investigation of potential systematic effects, which is a major strength of the work. The identification and quantification of a "monopole-mask leakage channel"—whereby a small global classifier bias couples with the survey geometry to create a spurious dipole signal—is a particularly important methodological contribution to this field. The theoretical scoping, especially the careful distinction between parity-even (isotropy-breaking) and parity-odd (parity-violating) observables, is handled with commendable precision.

However, while the scientific content is of high quality, the manuscript in its current form is not suitable for publication in Physical Review D. The primary issues are its excessive length and dense, convoluted structure, which render the main arguments nearly impenetrable. The paper reads more like an internal technical note or a software documentation manual than a scientific journal article. A major restructuring and significant shortening are required to make the work accessible to the journal's readership.

My recommendation is for **MAJOR REVISIONS**. The underlying analysis is excellent and, if presented appropriately, will be a significant contribution.

---
## Findings

### ESSENTIAL

**P4-E1: Paper Length and Structure**
*   **Section:** Entire manuscript
*   **Problem:** At 56 pages, the paper is far too long for a PRD publication, where even detailed methods/catalog papers are typically half this length. The core scientific narrative is buried under an overwhelming amount of procedural detail, descriptions of intermediate pipeline steps, and exhaustive reporting of every diagnostic check. This level of detail obscures the main findings and makes the paper exceptionally difficult to follow.
*   **Fix:** The paper must be substantially restructured and shortened. I recommend the following structure:
    1.  **Main Paper (target length: 20-25 pages):** This should contain a clear, linear narrative.
        *   Introduction: Motivation and context.
        *   Data & Core Methodology: Describe the dataset, the classifier, and the key principles of the systematic control (e.g., Equivariant TTA, MASTER deconvolution).
        *   Results: Present the main results in a logical sequence: (1) the raw, uncorrected signal; (2) the identification of the monopole-mask leakage channel; (3) the primary null result for the ℓ=1 dipole on the subsample-mask after full correction; (4) the existence and diagnosis of the +3.64σ residual on the canonical-mask, with a summary of the evidence pointing to its systematic origin.
        *   Discussion & Conclusions: Discuss the implications, the theoretical context (parity-even vs. odd), and the final null conclusion.
    2.  **Appendices:** Move the vast majority of the detailed diagnostic descriptions into appendices. This includes:
        *   The full Bias Hardening Suite (Sec. III F).
        *   Detailed breakdown of the "multi-null battery" and joint nuisance fit (Sec. V.D, p. 21-25).
        *   The NaMaster configuration (Sec. VIII).
        *   Detailed results of the signal-hunt diagnostics (confidence/sky/leg stratifications, Sec. IV E).
        *   Extended discussions on TTA variants (D4 vs Z2), mask robustness sweeps, etc.

**P4-E2: Removal of Internal/Review Artifacts**
*   **Section:** Throughout (e.g., Abstract, p. 6, p. 11, p. 18, p. 35, p. 47)
*   **Problem:** The manuscript contains numerous phrases and asides that refer to the paper's own version history, previous (now-retracted) results, or the review process. This is unprofessional and inappropriate for a final scientific publication.
*   **Examples:**
    *   p. 6: "...the hierarchy below was fixed at v1.0.76 of this manuscript..."
    *   p. 11: "We therefore retract the original ∆ = −1.35% argmax-CW-fraction claim as sample-noise..."
    *   p. 18: "...the older snapshot value 2.75σ predates the canonical Nspiral = 3,201,160 recount..."
    *   p. 35: "Earlier drafts also cited a ∆ = −1.35% argmax CW-fraction shift... This manuscript retracts this..."
*   **Fix:** All such language must be systematically removed. The paper should be presented as a finished work, reporting the final methodology and results without reference to its own development history or past errors.

### MAJOR

**P4-M1: Clarity and Readability**
*   **Section:** Entire manuscript
*   **Problem:** The paper's narrative is highly fragmented and difficult to follow. The main line of argument is constantly interrupted by asides, forward/backward references, and, most disruptively, references to specific "companion artifact" JSON files in an external repository. This practice is not standard for a journal article and makes the text unreadable as a self-contained document. The proliferation of newly-defined jargon (e.g., "canonical-mask," "subsample-mask," "canonical-N direct-MC") further complicates the reading experience.
*   **Fix:**
    1.  As part of the restructuring in P4-E1, the main text must be rewritten to present a clear, linear argument. The logical flow should be straightforward, with complex diagnostics summarized and their detailed execution relegated to appendices.
    2.  All references to specific filenames (e.g., `p4_multinull_battery.json`) must be removed from the main text. It is sufficient to state that the data and analysis scripts are publicly available and to describe the results of the analysis in the paper itself.
    3.  The key analysis configurations (e.g., the different masks and nulls) should be clearly defined in a single place, perhaps a table in the Methods section, to help the reader keep track of them.

### MINOR

**P4-N1: Duplicate Phrases**
*   **Section:** p. 42, Sec. VI F
*   **Problem:** There are instances of duplicated words or phrases.
*   **Example:** "this closes the mask-definition mask-definition robustness question"
*   **Fix:** The manuscript should be carefully proofread to correct these and any other typographical errors.

**P4-N2: Theoretical Scoping in Discussion**
*   **Section:** p. 43, Sec. VI G
*   **Problem:** The section "Relation to possible parity-violating sectors" is excellent in its careful distinction between isotropy tests (parity-even) and parity tests (parity-odd). However, the authors state they "retain the language 'parity-violating chirality dipole' for continuity with the Shamir literature". While the clarification is provided, this retention of imprecise language can still cause confusion.
*   **Fix:** The authors should consider consistently using the more precise term "isotropy-breaking chirality dipole" or "axial-vector dipole" throughout the manuscript, while noting in the introduction that this is the observable previously discussed under other names in the literature. This would improve the long-term clarity of the field.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper presents a scientifically rigorous and methodologically significant analysis that results in a new, strong null constraint on cosmic-scale galaxy chirality. The authors' treatment of systematics is exemplary. However, the manuscript is not in a state suitable for publication. Its excessive length, convoluted structure, and inclusion of internal development artifacts make it largely inaccessible. The authors must undertake a major revision to restructure the paper into a concise main article with supporting appendices, focusing the main text on a clear, linear narrative of their core findings. If this restructuring is done effectively, the paper will be an outstanding contribution to the field.
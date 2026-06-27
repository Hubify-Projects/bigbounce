# P1B R55 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R55_P1B/paper1b_mcmc_companion.pdf` md5=2d80d814 pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 167.6s

---

Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program

## General Comments

This manuscript presents a technical companion paper documenting three verification analyses related to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program. The analyses are: (1) a stock-CAMB MCMC analysis of the ACDM+ΔNeff model as a proxy for extra radiation, (2) a Monte Carlo validation of a NaMaster-based pipeline for measuring cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-executed and presented. The authors demonstrate a high level of rigor in their analyses, with extensive self-criticism, clear scoping of claims, and thorough documentation of methods, limitations, and robustness checks. The distinction between pipeline validation and sky detection, and between model consistency and model evidence, is maintained with admirable discipline throughout the manuscript. The transparency regarding potential systematics (e.g., supernova catalog overlap, Planck release-pairing) and data-processing artifacts is a model of good scientific practice. The work is of high quality and suitable for publication in Physical Review D after minor revisions.

## Findings

### ESSENTIAL

*   **P1B-E1:** **Section: End of document (p. 21)**
    *   **Problem:** The document contains internal reviewer metadata at the very end of the text: `[REVIEWER METADATA — NOT PART OF THE PAPER — DO NOT FLAG AS ARTIFACTS] Paper tag: P1B | Round: R55 | Pages: 21 Round context (not in paper): R55 convergence-confirmation [END REVIEWER METADATA]`. This block is not part of the scientific paper and must be removed before publication.
    *   **Fix:** Remove the entire `[REVIEWER METADATA ...]` block.

### MINOR

*   **P1B-M1:** **Section: III (p. 4) and V.C (p. 12)**
    *   **Problem:** The paper presents a detailed analysis of a `w0-wa` model extension, which occupies a significant fraction of Section III and is revisited in Section V.C and Table II. While this analysis is interesting, it feels like a detour from the three core verification tasks outlined in the abstract and introduction (ΔNeff, NaMaster, ALP). Its connection to the main ECH program is less direct than the other three analyses. The paper's length is substantial (21 pages), and this section contributes to it.
    *   **Fix:** Consider restructuring to better integrate or de-emphasize the `w0-wa` analysis. One option is to briefly summarize the result in the main text and move the detailed discussion (including Table II and its extensive footnotes) to an appendix. This would improve the narrative focus of the main paper on the three primary verification tasks.

*   **P1B-M2:** **Section: IV (p. 10, Footnote 4)**
    *   **Problem:** Footnote 4 provides an excellent, detailed explanation of the "pipeline-recovery SNR". However, the distinction between this template-fit SNR and the significance of the recovered angle (`β/σ_β`) is a crucial point that is easy for readers to miss. The main text mentions the SNR figures (20.32, 25.71) but relies on the footnote for the full context.
    *   **Fix:** Elevate the core distinction from the footnote into the main body text. Briefly state in the main text that the quoted SNR refers to the significance of the *injected template* against single-realization noise, and is distinct from the statistical significance of the recovered angle `β` itself, which is `β/σ_β`. This clarification is important enough to warrant placement in the main text.

### NIT (Nitpicks / Typos)

*   **P1B-N1:** **Section: Abstract (p. 1)**
    *   **Problem:** The abstract states: "the worst-case bias across injections, -0.040° at βinj = 0.342°, is carried forward as the observed pipeline bias floor — both are MC pipeline-recovery figures, not sky-measurement systematics, and are not directly comparable to each other's published sky significances)." The phrase "each other's" is slightly ambiguous.
    *   **Fix:** Suggest rephrasing for clarity, for example: "...and are not directly comparable to published sky-detection significances."

*   **P1B-N2:** **Section: IV (p. 8)**
    *   **Problem:** The text describes the noise model for Q and U maps: "...and draws independent Gaussian realizations with the same σ_pix for Q and U (no √2 factor; ...)." While the implementation is explicitly stated and justified, this is a non-standard choice that might momentarily confuse readers accustomed to noise being specified for Stokes I. A brief clarifying phrase could be helpful.
    *   **Fix:** Consider adding a short parenthetical clarification, e.g., "(i.e., the noise is specified per Stokes parameter, not for total intensity)."

*   **P1B-N3:** **Section: VI (p. 13)**
    *   **Problem:** The text states: "The simplified inverse-variance combination below (3.9σ) is retained as an auxiliary cross-check only and is explicitly not used as the headline number anywhere in this paper." The calculated value is 3.95σ.
    *   **Fix:** For consistency with the high precision used elsewhere, report the value as 3.95σ or state that 3.9σ is a rounded figure.

## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent and meticulously prepared manuscript. It serves as a model for a technical verification paper, with clear scoping, transparent methodology, and thorough robustness testing. The authors are their own sharpest critics, which inspires confidence in the results. The single essential correction is the removal of internal metadata. The minor suggestions are intended to further improve the paper's structure and clarity. The paper is a strong contribution and will be a valuable resource for researchers in the field.
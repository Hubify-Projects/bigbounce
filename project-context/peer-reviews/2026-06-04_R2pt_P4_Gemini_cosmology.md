# P4 2026-06-04_R2pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 75.0s

---

## Referee Report for Paper HUBIFY-2026-004

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.12σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Journal:** Physical Review D
**Round:** 2026-06-04_R2pt

### General Comments

This paper presents an exceptionally thorough and rigorous analysis of the large-scale angular distribution of spiral galaxy chirality using a catalog of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of an ℓ=1 dipole, which is the key observable for an isotropy-breaking axial-vector mode. The authors correctly and importantly distinguish this parity-EVEN isotropy test from a direct test of parity violation.

The analysis employs modern machine learning techniques (a Vision Transformer with Test-Time Augmentation) and sophisticated statistical methods (NaMaster for power spectrum estimation) to control for systematics. The paper's main strengths are:
1.  The careful and explicit separation of different estimators and null hypotheses, which avoids confusion.
2.  The identification and quantification of a monopole-to-dipole leakage channel due to mask geometry, which provides a plausible explanation for previous claims of detection in the literature.
3.  A comprehensive suite of systematic checks that add significant weight to the final null conclusion.
4.  A clear and correct theoretical framing, particularly regarding the symmetry properties of the observables (parity-even vs. parity-odd) and the scope of the constraints (late-universe vs. primordial).

However, the paper's presentation is a significant weakness. At 56 pages, it is excessively long for a journal article. The structure is often difficult to follow, reading more like a technical report that documents every step of the research process, including dead ends and corrections from previous internal versions. This obscures the main, high-impact scientific results. The manuscript is also replete with internal artifacts such as file paths and version history notes that are inappropriate for a final publication.

The scientific work is of high quality and warrants publication in Physical Review D, but only after a fundamental restructuring and revision of the manuscript to improve clarity, conciseness, and professionalism.

### Findings

#### ESSENTIAL

1.  **P4-E1: Excessive Length and Structure.** The manuscript's length (56 pages) is prohibitive and not justified for the core scientific contribution. The paper must be substantially restructured into a main article (suggested max. 20 pages) and one or more appendices or a supplementary document. The main article should focus on the key results: the introduction, a summary of the methods, the primary null result, the interpretation of the key systematic (the canonical-mask residual), a discussion of the implications, and conclusions. The exhaustive details of every systematic check (e.g., the blow-by-blow account of the multi-null battery on pp. 21-26, the full bias-hardening suite, detailed NaMaster configurations) should be moved to the appendix/supplement.
    *   **Required Fix:** Restructure the paper as described above. The goal should be a main text that is readable and focused on the principal scientific claims, with the extensive supporting details available for the dedicated reader in an appendix.

2.  **P4-E2: Internal Artifacts and File Paths.** The manuscript is littered with internal file paths (e.g., `pipelines/p2_chirality/...`), variable names from code (e.g., `class_flip_rate.any_class_z2_to_d4_pct`), and labels like "Reproducibility artifact:". This is unprofessional and makes the text difficult to read.
    *   **Location:** Throughout the paper, e.g., p. 5 (footnote 3), p. 9 (footnotes b, c), p. 10, p. 13, p. 19, p. 21, etc.
    *   **Required Fix:** Remove all such artifacts. Data and code should be referenced via the Data Availability section and proper citations, not by printing internal paths in the main text or captions.

3.  **P4-E3: Version History in Prose.** The text contains numerous references to the manuscript's own evolution, such as corrections, retractions of prior internal results, and justifications for changes. This "sausage-making" is inappropriate for a final scientific paper.
    *   **Location:** e.g., p. 6 ("fixed at v1.0.76"), p. 7 ("the earlier ~0.79% value... is corrected here"), p. 15 ("the pre-recount figure... is superseded"), p. 35 ("Earlier drafts also cited... This manuscript retracts this...").
    *   **Required Fix:** Remove all references to the paper's own version history. The manuscript should present the final, definitive analysis and narrative.

#### MAJOR

1.  **P4-M1: Narrative Structure of Results.** The Results section, particularly from Sec. IV.D onwards (pp. 21-26), presents a long, linear sequence of diagnostic tests. This makes the central argument difficult to follow. The section reads like a log of analyses performed rather than a structured scientific argument.
    *   **Required Fix:** Rewrite this section to be hierarchical and argument-driven. Clearly state the finding (the +3.64σ residual), pose the alternative interpretations (e.g., cosmological signal vs. systematic artifact), and then systematically present the evidence from the various tests to adjudicate between them. This will greatly improve clarity and impact.

2.  **P4-M2: Repetition.** The core results are summarized in a very dense, similar fashion in the Abstract, Introduction, Discussion, and Conclusions. While some repetition is expected, the current level makes the paper feel bloated and reduces the impact of each section.
    *   **Required Fix:** Streamline these sections. The introduction should motivate the work, the discussion should place the results in a broader context, and the conclusions should provide a concise summary. Avoid repeating the same block of text with minor variations.

#### MINOR

1.  **P4-m1: Informal/Defensive Tone.** In several places, the tone is overly defensive or informal for a scientific publication.
    *   **Location:** e.g., p. 3 ("we refrain from claiming the audit suite is 'the most extensive' without a literature survey"), p. 9 ("see §III E for the full closure narrative").
    *   **Required Fix:** Revise the language to be more formal, direct, and objective. State what was done and why, without the additional meta-commentary.

2.  **P4-m2: Clarity on Primary vs. Secondary Results.** The paper analyzes several estimators for the dipole, with the main results being a null (`-0.12σ` and `+0.43σ`) and a key systematic being significant (`+3.64σ`). While the "Declared Analysis Hierarchy" is an excellent feature, the prose sometimes refers to "the result" ambiguously.
    *   **Location:** e.g., p. 39, "The catalog's reported result — Catalog C post-TTA dipole at σ=0.43, p=0.30 — is a non-detection". This is one of two primary nulls, but the headline is the `-0.12σ` MASTER result.
    *   **Required Fix:** Ensure the prose is always precise about which estimator is being discussed, especially in summary statements, to prevent any potential confusion.

#### NIT

1.  **P4-N1: Proofreading.** A final, thorough proofread is needed to catch minor typos, grammatical errors, and awkward phrasing (e.g., "σfrom null" in Table XVIII caption).

## Summary recommendation

**MAJOR REVISIONS**

The scientific analysis presented in this paper is of the highest quality and represents a significant contribution to the field. The work is thorough, the conclusions are robustly supported, and the theoretical framing is sound. If the results hold, this paper will likely become a key reference for galaxy chirality studies.

However, the manuscript in its current form is not acceptable for publication. The excessive length, convoluted narrative structure, and inclusion of numerous internal notes and file paths make it extremely difficult to read and digest. The paper must undergo a major restructuring to separate the core scientific argument from the exhaustive supporting details, and it must be professionally edited to remove all non-publication-ready artifacts. Once these significant presentational issues are addressed, the paper will be a strong candidate for publication in Physical Review D.
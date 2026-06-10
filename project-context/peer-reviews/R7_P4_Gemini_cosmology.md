# P4 R7 — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 91.7s

---

# Referee Report

**Paper ID:** P4
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.12σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Journal:** Physical Review D

This paper presents a large-scale search for a galaxy chirality dipole using 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of the ℓ=1 dipole, which constrains the isotropy of the universe in the late-time morphology channel. The work is notable for its scale and for its exceptionally thorough treatment of potential systematic effects. The authors develop and apply an "equivariant test-time augmentation" (TTA) pipeline to mitigate classifier bias and perform an exhaustive series of diagnostic tests to characterize residual systematics. A key contribution is the quantitative demonstration of a "monopole-mask leakage channel," whereby a global monopole (a uniform asymmetry in the classification of clockwise vs. counter-clockwise spirals) can leak into dipole and higher-multipole modes due to the complex geometry of the survey mask.

The scientific analysis is of high quality. The methodology is sound, the results are well-supported by a vast array of consistency checks, and the theoretical interpretation is careful and correctly scoped. The authors clearly distinguish between the parity-even dipole observable they constrain and direct tests of parity violation. The paper's main weakness is its presentation: at 54 pages, it is excessively long and its structure obscures the primary results, making it very difficult for a reader to follow the main logical thread. The work requires significant restructuring before it can be considered for publication.

## Findings

### ESSENTIAL

**P4-E1: Paper Length and Structure**
*   **Section/Page:** Entire manuscript.
*   **Problem:** The paper, at 54 pages, is far too long for a standard research article in Physical Review D. The core scientific results—the null dipole measurement and the characterization of the monopole-mask leakage channel—are buried under an overwhelming number of secondary diagnostics, robustness checks, and detailed procedural descriptions. This structure makes the paper's central narrative difficult to follow and diminishes the impact of its important conclusions. The current format is more appropriate for a technical data release document than a focused scientific paper.
*   **Fix:** The paper must be substantially restructured. I recommend a main article of no more than 15 pages that focuses on:
    1.  A concise motivation and summary of previous work.
    2.  The core methodology (the ViT classifier and equivariant TTA).
    3.  The primary results: the headline null dipole measurement (−0.12σ and +0.43σ) and the detection of the +3.64σ canonical-mask residual.
    4.  A focused section demonstrating that the +3.64σ residual is a systematic effect, presenting only the most compelling evidence (e.g., the ℓ=2 > ℓ=1 power, the cross-spectrum with density, and the joint model fit).
    5.  A concise discussion and conclusion.
    The vast majority of the other diagnostic tests (e.g., detailed confidence/leg stratifications, two-point function analysis, hemisphere scans, pixel-count threshold sweeps, detailed D4-TTA validation) and detailed descriptions of null-test implementations should be moved to one or more appendices or to a separate supplemental material document.

### MAJOR

**P4-M1: Clarity of Narrative**
*   **Section/Page:** Primarily Sections IV, V, and VI.
*   **Problem:** The paper's central narrative is the contrast between a null result on a clean, wide-area analysis and a significant-looking residual on a smaller, patchier "canonical mask," followed by a demonstration that this residual is a systematic. This is a powerful story, but it is currently told in a fragmented way across dozens of subsections. The evidence proving the systematic nature of the +3.64σ residual is scattered across pages 21-25 and is difficult to synthesize.
*   **Fix:** As part of the restructuring required in P4-E1, the main text should present this narrative in a more linear and focused manner. A dedicated section titled, for example, "The +3.64σ Canonical-Mask Residual and its Systematic Origin" should be created. This section would consolidate the key evidence from the multi-null battery, the direct cross-spectrum with pixel density, and the conclusive joint nuisance-marginalized model fit, providing a clear and decisive argument for the reader.

**P4-M2: Redundancy**
*   **Section/Page:** Entire manuscript.
*   **Problem:** There is considerable repetition of key results and interpretations across the Abstract, Introduction, Results (Section IV), Discussion (Section VI), and Conclusions (Section VII). For example, the multi-null battery results for the canonical-mask residual are described in detail in the abstract, again in the introduction (p. 3-4), again in the results (p. 18, 21-23), and summarized again in the discussion.
*   **Fix:** The restructuring of the paper should be used as an opportunity to eliminate this redundancy. The Discussion section, in particular, should be dramatically shortened. Instead of restating results, it should focus on their interpretation and implications, referring back to the relevant tables, figures, and sections where the results were originally presented.

### MINOR

**P4-m1: Table and Figure Placement**
*   **Section/Page:** e.g., Page 7.
*   **Problem:** Some tables are referenced several pages before they appear. For instance, on page 7, the text references Table I and Table II, but these tables are located on pages 8 and 9, respectively. This disrupts the flow of reading.
*   **Fix:** In the revised manuscript, please ensure that all tables and figures are placed as close as possible to their first mention in the text.

**P4-m2: Internal Jargon and Artifacts**
*   **Section/Page:** Various.
*   **Problem:** The text contains a few instances of what appears to be internal project jargon or versioning information that is not meaningful to an external reader.
    1.  Page 21, Table VII caption: "The N=500 simulation supersedes the smoke result at N=25". The term "smoke result" is undefined and appears to be internal slang for a preliminary test.
    2.  Page 45, Section VIIb: "...seed 42 matching the Wave 12 hemisphere convention)". "Wave 12" is not defined and seems to be an internal project name.
*   **Fix:** Please rephrase these sentences to remove the internal jargon. For (1), "This N=500 simulation provides a more precise calibration than earlier, smaller-N tests" or similar would suffice. For (2), the reference to "Wave 12" can likely be removed without loss of meaning.

**P4-m3: Typographical Error**
*   **Section/Page:** Page 23, left column.
*   **Problem:** A duplicate word appears in the text: "...per the the bootstrap injection-recovery diagnostic) but the COMBINATION of..."
*   **Fix:** Remove the repeated "the".

### NIT

**P4-N1: Title Length**
*   **Section/Page:** Page 1.
*   **Problem:** The title is exceptionally long and detailed. While it accurately describes the paper's contents, it is unwieldy.
*   **Fix:** The author might consider a shorter, more impactful title, moving the specific numerical results and technical terms to the abstract. For example: "A Null Search for a Cosmological Chirality Dipole on 3.2 Million DESI Legacy Spirals". This is a suggestion at the author's discretion.

**P4-N2: Author Email**
*   **Section/Page:** Page 2, footnote.
*   **Problem:** The author's email address, `houston@hubify.com`, appears to be associated with a commercial entity rather than a research institution, which is unconventional for a physics publication.
*   **Fix:** The author may wish to use a more standard academic or professional email address. This is a minor point left to the author's discretion.

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a high-quality, comprehensive, and important null result in the search for cosmological-scale chirality. The methodological rigor, particularly in the treatment of systematics, is a significant strength and serves as a valuable contribution to the field. The scientific conclusions are well-supported by the exhaustive analysis. However, the paper in its current form is not suitable for publication due to its excessive length and convoluted structure. The core message is obscured by the sheer volume of supporting detail, making the paper inaccessible. The work must be significantly restructured into a concise main paper with the bulk of the diagnostic material moved to appendices, as detailed in finding P4-E1. Once this major structural revision is complete, the paper will represent a definitive statement on the galaxy chirality dipole and will be a strong candidate for publication in Physical Review D.
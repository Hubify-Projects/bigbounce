# EXT10 Harvest — P5 — ChatGPT
- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc684-5918-83e8-b53e-28fde5fca69a
- PDF md5: 43619245
- Harvested: 2026-06-13 15:16 PDT

---

## Referee report — MNRAS-style

**Manuscript reviewed:** Paper 5 v0.1.74, "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample."

---

**Recommendation: MINOR REVISIONS**

The paper is scientifically close to publishable. The primary null result is well supported by the DESIVAST analysis, and the extensive secondary checks mostly reinforce rather than complicate the conclusion. I do not see a missing load-bearing control that would require substantial reanalysis. The remaining must-fix items are mainly nomenclature, reproducibility/provenance, and presentation hygiene before publication.

---

**1. BLOCKERS — must fix before publication**

**B1. Correct the V-Web/T-Web nomenclature everywhere it appears as a method label**
Location: Title/abstract, p. 1; §I p. 3; §IV heading and opening, p. 4; Fig. 2 caption p. 6; many later captions and section references.
Issue: The paper repeatedly calls the implementation "V-Web" while explicitly stating that the computation is the Hahn 2007 tidal-tensor/T-Web recipe and that the Hoffman et al. velocity-shear V-Web would require a velocity reconstruction not used here. In the cosmic-web literature, V-Web and T-Web denote different fields. The current text acknowledges the distinction but then keeps the inaccurate label "for backward compatibility."
Proposed fix: Rename the method throughout the paper as T-Web tidal-tensor classification. Reserve "V-Web" only for historical/internal artifact names, e.g. "the pipeline path retains vweb in filenames." This is a mandatory publication fix but does not require new calculations.

**B2. Make the chirality input and reproducibility bundle stable and referee-accessible**
Location: §II–III, pp. 3–4; Appendix C, p. 31.
Issue: The analysis relies on Paper IV for the per-galaxy CW/CCW labels and the manuscript states that Paper IV is in preparation / not yet peer reviewed. The publication version must contain the actual DOI, immutable tag/commit, and dataset revisions.
Proposed fix: Before acceptance, provide a stable arXiv/DOI citation for Paper IV or include the minimal classifier-validation material needed to referee this paper independently. Add the exact Git commit, Zenodo/archival DOI, HuggingFace dataset revision/hash, and the artifact filenames used for Tables VIII–XIV.

---

**2. MAJORS — should fix**

**M1. Promote the footprint-restricted / exact DESIVAST control into the primary DESIVAST result table**
Location: §VIII B, p. 17; §VIII E, pp. 19–20; Tables VIII–X.
Issue: The paper later notes that the unrestricted non-void control includes objects not required to lie within the DESIVAST usable footprint. The paper does supply a footprint-restricted control that is also null.
Proposed fix: Make the primary DESIVAST table explicitly side-by-side: k=20 hole union, exact hole union, maximal-sphere interior, and footprint-restricted non-void. Then quote one designated primary contrast in the abstract and conclusion.

**M2. Use the unique-TARGETID parent as the default for the secondary T-Web contingency statistics**
Location: §VI A, pp. 7–9; §VIII F, pp. 20–21; Appendix B p. 31.
Issue: The paper reports the main secondary T-Web table on 812,793 environment-labeled rows, while acknowledging that these carry 28,973 duplicate rows over 783,820 unique env-matched spirals and that duplicates technically violate independence in the row-level contingency test.
Proposed fix: Present unique-TARGETID values first in the main text and move row-level coadd-row values to an appendix/closure table.

**M3. Make the post-hoc primary/secondary hierarchy visible in the abstract and conclusion**
Location: §V B, pp. 7–8; abstract p. 1; conclusions p. 29.
Issue: The manuscript is transparent that DESIVAST was designated primary post hoc. However, the abstract still gives a very large amount of secondary T-Web detail and uses "headline" language around the secondary T-Web table.
Proposed fix: In the abstract and conclusion, make the first quantitative result the DESIVAST void-vs-non-void contrast and describe the full-DR1 T-Web run as a secondary consistency check.

**M4. Temper the ASTRA-DESI validation claim and add a compact agreement metric**
Location: §X, pp. 26–27; Table XIV.
Issue: The ASTRA overlap reports poor per-object agreement: ASTRA distributes the 25,186 overlap spirals across all four classes, whereas the T-Web run puts essentially all of them into filament/cluster with only three objects in void+wall.
Proposed fix: Add a small confusion matrix or normalized mutual information for ASTRA argmax vs T-Web on the 25,186 objects. Replace wording like "headline null does not depend on which independent classifier is applied" with "the EDR-overlap chirality statistic is null under both classifiers despite poor per-object environment agreement."

**M5. Sharpen the fixed-redshift-space / survey-selection scope of the secondary T-Web result**
Location: §IX A, pp. 21–24; §XIII, pp. 28–29.
Issue: The paper acknowledges redshift-space and selection-function limitations, including that no full-DR1 published cosmic-web VAC is available.
Proposed fix: Add one sentence to the abstract and conclusions: "The T-Web classifications should be read as fixed redshift-space, survey-selection-conditioned labels; the DESIVAST void result is the primary environmental null."

---

**3. MINORS — polish**

- Abstract length and density (p. 1–2): The abstract is effectively a compressed methods paper. Shorten to: DESIVAST primary result, T-Web secondary null, ASTRA/Tempel as one sentence, and the main caveat.
- PDF/source/title consistency: Make the manuscript title, PDF metadata title, arXiv title, and repository title identical.
- Figure 8 rendering problem (p. 22): The top colorbar label and the lower-panel title overlap visibly in the rendered PDF. Regenerate the figure with more vertical spacing.
- Use "void spirals," not "voids," for the 56,981 count (p. 1, §VIII).
- Units notation: Alternate between Mpc/h and h^{-1} Mpc; choose one notation (preferably h^{-1} Mpc for distances).
- Avoid referee-like prose inside the manuscript (§IX B p. 25 has a paragraph beginning "Verdict."). Replace with "Summary."
- SPECTYPE clarity (Table I p. 4): Add a footnote giving SPECTYPE composition for the chirality-relevant and env-labeled subsets.
- "Largest to date" phrasing (§VIII B p. 17): Qualify very narrowly or add a citation.
- Appendix A toy EFT (pp. 29–30): Consider shortening or moving to a companion theory paper.
- Table/figure captions: Move repetitive caveats to a "statistical conventions" paragraph.

---

**4. Strengths**

- The DESIVAST primary analysis is strong and appropriately powered: 56,981 VoidFinder void spirals from the 678,945-object low-z DESIVAST parent, with a null void-vs-non-void contrast, and robustness across VoidFinder, V2-REVOLVER, V2-VIDE, and catalog-native GALZONE definitions.

- The paper is unusually transparent about analysis hierarchy and multiplicity, including the post-hoc primary/secondary declaration and Bonferroni-5 treatment of the DESIVAST family.

- The dual-parent sample ledger is now mostly clear: 678,945 low-z DESIVAST parent, 783,820 unique env-matched T-Web spirals, and 812,793 coadd-row env-labeled rows are distinguished and reconciled.

- The conditional permutation framing is statistically appropriate: the label-shuffle null conditions on the observed global CW fraction, while the monopole uncertainty is treated analytically.

- The manuscript includes multiple independent diagnostics — DESIVAST, ASTRA, Tempel FoF, redshift/density/sky scans, program splits, grid resolution, shell corrections — and the null conclusion does not rest on a single fragile statistic.

- The limitations section is unusually candid about RSD, survey selection, lack of a full-DR1 environmental VAC, and the diagnostic rather than load-bearing status of secondary classifiers.

---

**5. Specific requested scrutiny**

**DESIVAST void cross-classifier:** This is the best part of the paper and should remain the primary claim. The VoidFinder result is null, the three-algorithm DESIVAST robustness is null, and the V2 catalog-native GALZONE rows are also null. My only substantive request is to promote the footprint-restricted and exact-rerun controls into the primary DESIVAST table.

**T-Web tidal-tensor classification over 14.6M DESI DR1 galaxies:** The computation is a T-Web tidal-tensor classification, not a V-Web velocity-shear classification. The full-DR1 secondary result is acceptable as a consistency check, especially because the DESIVAST result is primary, but the nomenclature must be fixed.

**ASTRA-DESI per-object cross-validation (25,186 spirals):** The ASTRA overlap is useful but should remain clearly diagnostic. Both ASTRA argmax and entropy-weighted statistics are null, but the per-object agreement is poor (T-Web overlap has only three objects in void+wall). This validates that the chirality statistic is null under a different environmental assignment on the EDR overlap, not that the T-Web labels themselves are validated.

**Dual-parent ledger (678,945 vs 783,820 unique TARGETID counts):** The ledger is acceptable and largely clear. The manuscript should nevertheless put object-level T-Web tables first and use row-level tables only as reproducibility closures.

**Conditional-permutation framing correction:** The corrected framing is sound. Conditioning permutations on the observed global CW count tests environment association rather than exact parity, which is the right null for this paper. I do not see a statistical blocker here.

---

**Overall verdict**

After the two publication blockers are addressed — especially the T-Web/V-Web terminology and stable reproducibility/citation bundle — I would recommend publication. The paper does not need substantial scientific rework; it needs a cleaner, journal-facing presentation of a robust DESIVAST-anchored null result.

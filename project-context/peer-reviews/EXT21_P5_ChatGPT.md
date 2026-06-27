# EXT21 P5 ChatGPT — chat: https://chatgpt.com/c/6a3e4f24-a68c-83e8-a6ec-db2d7354b613

Referee report — Paper P5, "DESI chirality"

1. Recommendation: ACCEPT

I recommend ACCEPT. The manuscript now presents a scientifically controlled null result: no detectable dependence of spiral chirality on large-scale-structure environment in DESI DR1, with the headline result properly anchored on the DESIVAST void/non-void analysis rather than on the noisier T-Web void bin. The load-bearing claims are supported by multiple independent checks: DESIVAST VoidFinder, V2-REVOLVER, V2-VIDE, catalog-native GALZONE definitions, T-Web sensitivity sweeps, redshift/density/sky nulls, selection-corrected rebuilds, grid-resolution checks, and explicit treatment of target-program residuals.

I do not find a blocker or a major issue requiring substantial scientific rework. Remaining points are clarity, presentation, and reader-navigation issues.

2. BLOCKERS
None.

3. MAJORS
None.

4. MINORS

Abstract / pp. 1–2 — Abstract is too dense and effectively functions as a mini-paper.
Proposed fix: compress the abstract around the primary DESIVAST result, the secondary T-Web consistency result, and the main limitations. Move most robustness-detail enumeration to the introduction or a "Results summary" paragraph.

Section V B / pp. 7–8 — Primary/secondary analysis declaration is excellent but could be made visually clearer.
Proposed fix: add one short boxed statement or italicized paragraph: "The primary estimand is DESIVAST void vs non-void ΔfCW; all T-Web and auxiliary classifiers are secondary diagnostics." This will prevent readers from over-weighting the T-Web four-class table.

Section VI A / pp. 8–9 — The T-Web void bin n = 428 may still attract undue attention.
Proposed fix: in Table III caption, explicitly say "not used as the primary void constraint" and point to Section VIII / Table X. The body text already explains this, but the table should be self-contained.

Section VIII B / pp. 17–18 and Table VIII — k=20 vs exact DESIVAST membership presentation is slightly confusing.
Proposed fix: either add the exact nvoid = 57,081 row directly to Table VIII or clarify in the caption that the main DESIVAST void row uses the retained k=20 artifact count while the footprint-restricted control uses the exact-membership retabulation.

Section VIII E / pp. 19–20 — "0 maximal voids per pixel" proxy language is careful but could be further simplified.
Proposed fix: add one plain-language sentence: "This bin should be interpreted primarily as a DESIVAST-coverage/mask diagnostic, not as a physical zero-void environmental class."

Section IX A / pp. 22–24 — Selection-corrected T-Web rebuild is important but very long.
Proposed fix: summarize the key numbers first, then move some implementation details to an appendix or table note. The core point is strong: the selection correction drastically changes class assignments but leaves fCW null.

Section X / pp. 26–27 — ASTRA cross-validation is appropriately caveated, but the role of this test should be demoted in wording wherever necessary.
Proposed fix: consistently call it an "EDR-overlap diagnostic" rather than "cross-validation" when making headline-level claims, since the paper itself notes strong per-galaxy label disagreement and limited overlap.

Section XI / p. 27 and Table XV — Systematics table reports raw σfrom half but the text interprets post-monopole residuals.
Proposed fix: add one additional column or footnote giving the monopole-subtracted residual scale for the rows with raw |σ| > 3, especially the confidence-threshold and bright-program rows.

Figure 8 / p. 22 — Bottom-panel title/labeling appears visually crowded/overlapping in the rendered PDF.
Proposed fix: adjust vertical spacing or reduce title length.

Appendix C / p. 31 — Reproducibility statement is strong but should include archive finalization details.
Proposed fix: once available, insert the DOI-minted archive identifier, exact manuscript tag, and any required data-access command or README path.

Throughout — Some artifact paths and implementation notes interrupt the narrative.
Proposed fix: retain the reproducibility information but consider moving the densest artifact-path lists to Appendix C or table footnotes.

Appendix A / pp. 30–31 — Toy EFT mapping is carefully caveated, but its non-load-bearing status should be emphasized in the section title.
Proposed fix: rename to "Non-load-bearing toy EFT mapping" or add "not used in the empirical inference" in the first sentence.

5. Strengths

- Correct primary-result anchoring. The manuscript appropriately treats the DESIVAST void/non-void contrast as the primary result and demotes the small T-Web void bin to a secondary diagnostic.

- Strong robustness across independent void definitions. The DESIVAST VoidFinder, V2-REVOLVER, V2-VIDE, and catalog-native GALZONE checks all return null contrasts below the declared Bonferroni-5 threshold.

- Transparent treatment of classifier monopole systematics. The paper repeatedly distinguishes raw σ-from-half from monopole-referenced residuals and shows that large raw deviations in populated bins are expected projections of the catalog-wide chirality monopole.

- Good multiplicity discipline. The primary/secondary analysis-tree declaration, Bonferroni thresholds, empirical max-statistic nulls, and explicit post-hoc caveat substantially reduce garden-of-forking-paths concerns.

- Detailed selection-function and survey-mask diagnostics. The redshift-shell correction, randoms-weighted low-z stress test, footprint-restricted DESIVAST control, HEALPix scans, and target-program splits directly address the dominant survey-systematics channels.

- Reproducibility orientation is unusually strong. The paper includes concrete artifact paths, committed-output references, deterministic seeds, contingency tables, and a data/code availability appendix.

- Limitations are stated honestly. The redshift-space nature of the result, RSD caveats, ASTRA overlap limitations, T-Web classifier limitations, and companion-paper dependencies are presented transparently rather than hidden.

Final assessment

The paper's scientific claim is appropriately scoped: it is a redshift-space, DESI-DR1, environment-conditioned chirality null result, with DESIVAST as the primary void constraint and T-Web as a secondary full-sample diagnostic. I find no missing load-bearing control and no unsupported claim that requires substantial reanalysis. The remaining revisions are presentation and clarity improvements. The manuscript is suitable for acceptance.

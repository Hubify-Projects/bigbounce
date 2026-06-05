# P3 2026-06-04_R3clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 14.7s

---

**Referee Report: P3 (2026-06-04_R3clean)**

**Paper length**: 50 pages. PRD methods/catalog papers are typically 15–30 pages. The contribution (a catalog release plus ancillary Fisher forecasts) does not justify the length. The manuscript contains extensive repetition of tier definitions, deferred caveats, and artifact references that should be removed or condensed. Recommended maximum: 22 pages (core methods + catalog description + one focused validation section).

**ESSENTIAL findings**

P3-E1. Abstract (unnumbered opening block, pp. 1–3). The opening text repeatedly states “the largest-scale application … to date” while immediately qualifying that LAMOST is exploratory only, ACT is quarantined, the 378 280 headline mixes physically distinct tiers, and the 17.8 % novelty figure is a single-sample point estimate at the top-1 000 stratum with no full-catalog measurement. The abstract therefore does not accurately summarize what the body proves. Required fix: rewrite the abstract to state only the quantities that survive all stated caveats (e.g., “we release a catalog of 378 080 point-source anomalies … after native retraining; cross-survey novelty is measured at 17.8 % in the top-1 000 DESI stratum”).

P3-E2. Section I (p. 3) and repeated tier language (pp. 1–2). The text contains verbatim or near-verbatim duplication of the 378 080 / 200 / 378 280 stratification and the “point-source tier” versus “Planck CMB-patch tier” definitions at least four times in the first three pages. Required fix: define each tier once in a single paragraph and refer to it thereafter; delete all duplicates.

P3-E3. Section V (pp. 21–23) and §VI D caveat (i). Multiple σ(fNL) values are presented (linear-extrapolation 8.27 ± 2.37, positivity-respecting 8.14 with envelope [3.92, 8.98], GS-subset 1.95 with envelope [0.94, 8.98]) without explicit statement that they rest on different functional forms and different data subsets. The linear form is shown to violate Fisher positivity outside a narrow anchor region, yet is still quoted. This is an ESSENTIAL violation of the instruction on σ values from different null procedures. Required fix: present only one canonical estimator with its exact functional form and data subset; move all variants to a single, clearly labeled supplementary table.

P3-E4. Throughout (e.g., pp. 1, 6, 8, 12, 26, 28). The manuscript contains numerous internal audit tags and review-log artifacts: “companion artifact pipelines/p3 …”, “queued as a methods-paper companion task”, “deferred to a companion artifact”, “multi-round convergent finding”, “R5 Gemini-M3”, “earlier draft”, “retracted here per R5”. Required fix: remove every such phrase; replace with standard citations or delete.

P3-E5. Section II D and §VI D (multiple locations). The Path-C “gate” criteria, injection-recovery numbers, and cross-validation diagnostics are presented as decisive validation, yet the text simultaneously states that three of six surveys fail the formal ≥ 50 % gate and that LAMOST remains below threshold even after the continuum-dip variant. The conclusion that the catalog is “validated” is therefore unsupported. Required fix: state explicitly which surveys pass which quantitative gate and which do not; do not claim overall validation.

**MAJOR findings**

P3-M1. Section IV A (p. 19). The 58.8 % SIMBAD-unmatched aggregate is presented as a headline figure while the text immediately states that extended NED+VizieR matching reduces the genuine novelty fraction to 17.8 % at the top-1 000 stratum only. The abstract and title language (“Anomalies”) exploit the higher number. Required fix: report only the 17.8 % figure as the primary novelty metric; move the SIMBAD percentages to a diagnostic table.

P3-M2. Section V (p. 22). The multi-tracer forecast assumes zero observational systematics (fiber assignment, photo-z, PSF, foregrounds, completeness). The text acknowledges that any non-zero budget “could degrade” the result but still presents σ(fNL) = 8.14 as the central forecast. Required fix: either marginalize the systematics or state that the quoted number is an upper bound on improvement under idealized conditions.

P3-M3. Section VI C (p. 26). The manuscript lists six major limitations yet concludes that the catalog “has utility beyond source discovery.” The limitations (single architecture, incomplete injection tests, training-sample overlap, B-dominant calibration concern, redshift coverage, GR projection effects) collectively undermine the cosmological claims. Required fix: either remove the cosmological-application section or demonstrate that the limitations do not affect the quoted σ(fNL) numbers.

**MINOR findings**

P3-m1. Table I caption and footnotes (p. 14). Three different threshold policies are used across surveys but are described in a single dense footnote. Required fix: add a one-sentence summary row stating the exact threshold applied to each survey.

P3-m2. Figure 11 caption (p. 31). The caption states “3 PASS / 3 FAIL-with-diagnostic” while the plotted curves include additional morphology variants that do not match this count. Required fix: align caption with plotted data or remove the summary sentence.

**NIT findings**

P3-n1. Multiple locations. Phrases such as “the paper is organized as follows” and “we emphasize that” are used repeatedly; they are not erroneous but add unnecessary length.

P3-n2. Section III F (p. 17). The narrow dynamic range of the Planck native scores (0.063) is noted but not quantified relative to the spectroscopic surveys. A one-sentence comparison would suffice.

**Summary recommendation**

**REJECT**

The manuscript is 50 pages long, contains extensive internal review artifacts and duplicated text, presents multiple inconsistent σ(fNL) estimators without clear qualification, and qualifies its central claims so heavily that the abstract no longer accurately represents what has been proved. These are not cosmetic issues; they violate PRD standards for clarity, length, and honest reporting of results. A substantially shortened and cleaned resubmission that reports only quantities surviving all stated caveats could be reconsidered, but the present version cannot.
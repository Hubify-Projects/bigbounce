# EXT21 P4 ChatGPT — chat: https://chatgpt.com/c/6a3e4eee-d48c-83e8-b4e3-b2a879c3a7dc

Referee Report — Paper P4, "Galaxy chirality catalog"

1. Recommendation: ACCEPT

The paper is scientifically publishable in its present form. I find no blocker and no major issue requiring substantial scientific rework. The manuscript is unusually transparent about estimator hierarchy, label dependence, null conventions, systematic channels, and reproducibility artifacts. The primary conclusion — a null high-confidence real-space chirality dipole, with harmonic-channel residuals treated as systematics diagnostics rather than cosmological detections — is appropriately supported.

The remaining items below are editorial, reproducibility-polish, or figure-clarity fixes.

2. BLOCKERS
None.

3. MAJORS
None.

4. MINORS

Fig. 7, page 10 — raw vs equivariant map visual comparability.
The raw Catalog A panel appears much more sparsely populated than the Catalog C panel, although the caption describes both as NSIDE=64 sky maps with a shared footprint-style comparison. Because the caption calls this visual diagnostic the "methodology cornerstone," the authors should either replot the raw panel on the same pixel grid/footprint convention as the equivariant panel, or explicitly explain why the raw panel is visually sparse. This does not affect the quantitative null result, but it should be clarified.

Data Availability, pages 21–22 — archival DOI still future-tense.
The paper promises a Zenodo archival snapshot at journal submission. Before publication, replace the future-tense language with the DOI, release tag, and checksum/manifest location for the exact PDF/source/artifact bundle.

Sections III A, IV C–D, Tables I/III/IV — significance terminology.
The manuscript correctly states that the various "σ" values are not comparable across null procedures, but the number of conventions is dense. Consider renaming table columns such as "Reported statistic" or "z" to "moment-z vs stated null" where applicable, and add one compact reader-facing summary before the Results: "Only the HC real-space dipole and WLS template exclusion are primary; MASTER σ values are diagnostic."

Sections III B, IV C, VI A — high-confidence threshold provenance.
The peq > 0.6 threshold is well motivated by the confidence-cut sweep, but the phrase "the generator script has used throughout" is not quite as clean as a formal analysis declaration. Add one sentence stating whether peq > 0.6 was fixed before the final systematic audit, and identify the exact committed config/artifact that fixes the threshold.

Sections I, V, VI B, VII — wording of comparison with Shamir.
The manuscript is careful in most places to say that a matched Ganalyzer reanalysis is required for a likelihood-level exclusion. A few amplitude-comparison phrases such as "excluded by a factor" should be uniformly softened to "not reproduced under the present pipeline" or "inconsistent in amplitude under the present pipeline," unless accompanied immediately by the matched-analysis caveat.

Appendix B, Table VIII — scope of bias-hardening tests.
T1 is a protocol implementation check by construction, and T5 is explicitly not counted as an independent directional-coupling validation. The text should slightly revise "All 8 tests pass" to "All 8 operational checks meet their thresholds, with T1/T5 carrying the scope caveats described above." This avoids overstating the independence of the bias suite.

Appendix E — edge-on contamination anchor.
The edge-on contamination statement is important: 65.7% of b/a < 0.3 objects receive CW/CCW labels. Add the matched sample size and source of the b/a selection in the same paragraph, so readers can assess whether this is a small diagnostic subset or a large morphology audit.

Minor typography/formatting.
Some artifact paths are long and visually interrupt the text. For the journal version, consider moving repeated artifact paths into a compact artifact-manifest table or appendix note, leaving only short artifact IDs in the main text.

5. Strengths

- Scale and public utility. The 8.47M-object catalog, including 3.2M spiral classifications, is a substantial community resource and a clear advance over prior chirality catalog scale.

- Appropriate estimator hierarchy. The paper clearly separates primary cosmological estimators from diagnostic harmonic-channel measurements, avoiding the common mistake of treating all significant low-ℓ power as cosmological evidence.

- Strong bias-hardening methodology. The flip-equivariant TTA procedure, raw/calibrated/equivariant catalog tiers, confidence cuts, and extensive null tests make the central null result much more credible than a simple binary classifier analysis.

- Transparent handling of systematics. The monopole-mask leakage channel is quantified rather than waved away, and the post-MASTER residual is treated conservatively as a systematics-attributed diagnostic.

- Reproducibility culture. The paper repeatedly identifies scripts, artifacts, seeds, masks, sample sizes, null sizes, and release locations. This is well above the norm for a survey-scale machine-learning catalog paper.

- Careful statistical language. The manuscript repeatedly warns that σ values from different null procedures are not directly comparable. This prevents a misleading "detection" reading of the harmonic residuals.

- Useful falsification criterion. The A50/A95 injection-recovery framing gives future work a concrete amplitude scale for comparing new detections against this null result.

Overall assessment

This is a publishable survey-scale catalog and null-result paper. The scientific core is sound: the high-confidence real-space dipole is null, the clean-dipole template is strongly disfavored under the adopted block-bootstrap model, and the remaining harmonic residuals are conservatively assigned to footprint/depth/morphology systematics. I recommend acceptance, with only minor production and clarity edits.

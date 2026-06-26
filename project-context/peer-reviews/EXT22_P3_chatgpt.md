# EXT22 P3 chatgpt — chat: https://chatgpt.com/c/6a3e6833-c07c-83e8-919b-c8da52314429

Referee Report — Paper P3 (revised), "Multi-survey anomaly catalog"

1. Recommendation: MINOR REVISIONS
The revised manuscript is substantially publishable. It is unusually transparent about failure modes, score-axis limitations, exploratory tiers, native-retrain controls, and cosmology-forecast non-detections. I do not find a blocker requiring new analysis before publication. The remaining changes are primarily scope/terminology clarifications needed to prevent readers from over-quoting the headline catalog counts as uniformly validated astrophysical-object discoveries.

2. BLOCKERS
None.
No issue I found rises to the level of a publication blocker or requires substantial scientific rework. The manuscript already discloses the central caveats: DESI full-stream versus science-target counts, LAMOST as exploratory/training-bias dominated, eROSITA membership-only status, Gaia preprocessing limitations, ACT quarantine, and the non-detection status of the fNL and NANOGrav applications.

3. MAJORS
None requiring major revision.
The following are important clarity fixes, but they can be handled as minor revisions because the underlying analyses and caveats are already present in the paper.

4. MINORS

Title / Abstract / §VII — clarify "source/object" versus "spectrum/patch anomaly" terminology.
Location: Abstract p. 1; §III A pp. 6–8; §VII pp. 22–23.
Issue: The manuscript sometimes describes the full 378,080 point-source tier as "object detections" or "sources," while §III A makes clear that the DESI headline is dominated by non-primary-science spectra, sky/filler/calibration rows, or non-validated target types. This is transparently discussed, but the title/abstract phrasing can still be misquoted.
Fix: Use "spectral/source-or-patch anomaly detections" for the full headline, and reserve "astrophysical object catalog" language for the science-target or coordinate-associated subsets. In the abstract, add one sentence that the DESI full-stream count is not a science-target-only object catalog and that the like-for-like science-class recount is 2,468.

Abstract / Table I / §VII — "catalog-grade" is still ambiguous because some included components carry exploratory flags.
Location: Abstract p. 1; Table I footnotes pp. 7–8; §VII p. 23.
Issue: The text says the "recommended catalog-grade tier" contains 269,317 unique entries, but later emphasizes that Gaia and eROSITA carry exploratory validity flags, while LAMOST is explicitly exploratory and excluded from that tier. The distinction is understandable after careful reading, but the phrase "catalog-grade" risks implying uniform validation.
Fix: Define three explicit tiers early and use the names consistently: "validated core," "released flagged tier," and "exploratory methodological tier." If 269,317 includes flagged Gaia/eROSITA entries, call it a "recommended released tier with per-object validity flags," not simply "catalog-grade."

Table I is scientifically useful but too overloaded for first-pass comprehension.
Location: Table I, pp. 7–8.
Issue: The table footnotes contain core methodological information, threshold exceptions, score-axis caveats, dedup accounting, and tier-status definitions.
Fix: Split the material into two tables: one compact survey-count table and one "threshold/provenance/validity flag" table.

eROSITA score-axis caveat should be made visually unavoidable wherever the tier is counted.
Location: Abstract p. 1; §III E pp. 10–12; Table I pp. 7–8; Data availability p. 23.
Fix: Wherever the 298-source tier appears in a count table or abstract summary, label it "membership-only; no reproducible per-object production score axis."

DESI B-dominant component should be kept clearly separate from the validated multi-band population.
Location: §III A p. 8; §VI C p. 20; Table VII p. 24.
Fix: Add a column or short sentence flagging B-dominant objects as "calibration-systematics candidate pending color/photometric validation," while keeping multi-band anomalies as the stronger astrophysical subset.

Figures with historical or display-only score axes need stronger in-figure labeling.
Location: Fig. 2 p. 6; Fig. 3 p. 10; Fig. 8 p. 17; Fig. 9 p. 19; Fig. 11 p. 25.
Fix: Add small in-panel labels such as "cross-transfer baseline, not headline catalog," "display score, not catalog S," or "internal normalization only" directly on the figures.

Two fNL normalizations should be separated more cleanly.
Location: §V pp. 18–19; Appendix C and Fig. 11 p. 25.
Fix: Rename Appendix C/Fig. 11 as a "relative shot-noise sensitivity diagnostic" and avoid foregrounding its absolute σ(fNL) values except in the caption.

Clean minor rendered/text artifacts before submission.
Location: Table IX / Appendix E p. 27.
Fix: Clean the LaTeX table footnotes and re-render.

Final data-release placeholders should be resolved at production.
Location: Data availability p. 23.
Fix: Insert the Zenodo DOI and verify the manifest hashes in the released archive.

5. Strengths

The manuscript is exceptionally transparent about failure modes. ACT is quarantined, LAMOST is retained as a methodological lesson, eROSITA is downgraded to membership-only where appropriate, and Gaia's preprocessing provenance is explicitly limited.

The Path-C rebuild is a strong methodological improvement over the initial cross-transfer scan. Native retrains, Jaccard gates, injection-recovery diagnostics, dedup sensitivity sweeps, and explicit tier flags make the catalog much more credible than a simple large-scale autoencoder scan.

The DESI science-class recount is a valuable and honest correction. It prevents the headline 195,829 DESI anomalies from being overinterpreted as a like-for-like increase over prior DESI science-target anomaly catalogs.

The novelty analysis is responsibly calibrated. The paper distinguishes SIMBAD-unmatched fractions from genuine novelty and provides a deeper 18-catalog cross-match estimate for the DESI top-1,000 stratum.

The cosmological applications are framed with appropriate restraint. The fNL analysis correctly emphasizes that the de-biased estimate gives no current multi-tracer improvement, and the NANOGrav Bayes factor is caveated against environmentally modified SMBHB models.

The paper provides unusually good reproducibility breadcrumbs: artifact paths, validation statistics, retrain provenance, threshold disclosures, score-axis exceptions, and planned public release details are all present.

Overall assessment
This is a strong revised catalog paper. It is not merely a large anomaly list; it is also a useful methodological case study in why native retraining, score-axis provenance, and tier-specific validity flags matter for astronomical anomaly detection at survey scale. I recommend minor revisions focused on terminology, tier labeling, and figure/table clarity. No new analysis is required for publication.

# EXT22 P3 grok — chat: https://grok.com/c/58510df7-11fa-4add-972d-8b6fd3648ba3

Referee Report: MNRAS / PRD / JCAP format
Paper: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches (Houston Golden, June 19, 2026 revision; HUBIFY-2026 P3 series)

Recommendation: MINOR REVISIONS

The manuscript presents the largest multi-survey autoencoder anomaly detection campaign to date (37.3 M sources + patches across DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck, Gaia DR3, NEOWISE). It delivers a rigorously validated catalog (Path-C native-retrain protocol with explicit per-survey Jaccard / injection-recovery / OOD gates), a transparent stratification into catalog-grade (269k) vs. exploratory tiers, a genuine novelty fraction via deep 18-catalog cross-match (17.8% at DESI top-1k stratum), highlighted cross-survey coincidences (including an uncataloged BAL QSO), high-z QSO candidates, and conservative secondary cosmological applications (multi-tracer fNL forecast and NANOGrav γ consistency check).
The work is ambitious in scope yet exemplary in methodological transparency, provenance documentation, and conservative scoping of claims. No load-bearing scientific claim lacks critical controls or reproducibility support. All major limitations (single-architecture dependence, injection-recovery gaps for three surveys, training-bias diagnosis for LAMOST, eROSITA score-axis irreproducibility, novelty-fraction stratum specificity, unweighted MSE) are explicitly enumerated and handled. The paper meets MNRAS/PRD standards for large-scale astronomical catalog papers once minor clarifications and polish items are addressed.

1. BLOCKERS
None.

2. MAJORS
None. (No unsupported load-bearing claims, missing critical controls, or non-reproducibility issues that would require substantial scientific rework. The eROSITA membership-list framing and Gaia exploratory flag are already handled with appropriate caution; the 17.8% novelty figure is correctly caveated as a top-1k point estimate; cosmological applications are secondary and conservative.)

3. MINORS (recommended fixes; all are polish / clarification / submission-day items)

Abstract & §I (catalog-grade definition). The headline "recommended catalog-grade tier contains 269,317 unique entries" is correct but could be misread on first pass. Add one explicit sentence in the abstract (and reinforce in §I or Table I caption) stating: "The catalog-grade point-source subset (269,117 objects) excludes the LAMOST exploratory tier; downstream analyses requiring validated detections should use the per-object validity-flag column provided in the release."

§III E (eROSITA). The provenance discussion of the irreproducible S_BigAE axis is already excellent and transparent. Add one sentence at the end of the subsection: "Downstream users should treat the released n = 298 membership list as the canonical, reproducible selection and should not use the published per-object S_BigAE values for any quantitative ranking, stacking, or meta-analysis."

§V (fNL forecast). The envelope treatment [3.92, 8.98] and de-biasing to the single-tracer baseline are statistically correct and sophisticated. For readers who skim the Fisher section, add one short parenthetical or footnote reminder: "Because the mapping 1/σ²(fNL) = F0 + c α² is convex, the propagated 1σ envelope (rather than the central value) is the appropriate summary statistic when α is itself uncertain."

§III B (high-z QSO candidates). The existing caveat ("Redrock template-fit redshifts … at low continuum S/N … independent confirmation by visual inspection or re-observation is still required") is appropriate. Consider adding a brief clause noting that template-fitting pipelines at z ≳ 6 with low S/N have documented failure modes in the DESI literature; this would preempt reviewer questions without changing any conclusion.

§VI C (Limitations) & Table V. Two very minor tightenings: (i) in limitation (7) on unweighted MSE, explicitly note that the injection-recovery gates already bound the practical impact for the validated tiers; (ii) in Table V item (f) (BigAE vs. IF overlap), add "(not an independent cross-method confirmation)" for absolute clarity.

Minor textual / footnote polish (non-blocking). A few table footnotes (especially Table I ♡/♠/§ and the eROSITA rate disclosure) are already dense but self-contained; a final consistency pass to ensure every symbol used in a footnote is defined within it would eliminate any risk of reader confusion. Figure 9 caption and §V text correctly distinguish the fixed-α reference from the primary empirical-α result; a single cross-reference sentence would help.

Data-release manifest. The planned HuggingFace + GitHub + Zenodo release with SHA-256 manifest, per-survey schema flags, and explicit "membership-list only" tagging for eROSITA is exemplary. No action required beyond the standard "confirm DOI inserted at submission" placeholder.

All of the above are readily addressable in a revised manuscript and do not require new analysis, re-runs, or architectural changes.

4. Strengths (≥3)

Unprecedented scale with rigorous per-survey validation. The Path-C native-retrain + multi-gate protocol (5-fold Jaccard ≥0.70, OOD Jaccard ≥0.50, injection-recovery at 5σ, systematics masks, 7-way 5″ deduplication) is a methodological advance over prior single-survey anomaly searches. The explicit PASS/FAIL-with-diagnostic classification and retention of LAMOST only as a methodological lesson demonstrate scientific integrity.

Exemplary transparency and provenance. Training-bias diagnosis for LAMOST (98% blue-excess → 21.5× rate compression on native retrain), irreproducible eROSITA score axis with membership-list canonical selection, lineage-inferred Gaia preprocessing, full pod-provision JSON, committed scripts, and the quarantined ACT appendix are all handled at a level rarely seen in catalog papers. Table V (residual caveats) and the explicit "exploratory validity flag" column in the release are models of good practice.

Genuine novelty metric and cross-survey science. The 17.8% (Wilson ±1.2%) genuine novelty fraction from the 18-catalog CDS X-Match on the DESI top-1k stratum is the correct primary discovery-rate figure (far superior to the 58.8% SIMBAD-unmatched aggregate). The three highlighted DESI×SDSS coincidences (known QSO, time-variable TIC 374313355, uncataloged BAL QSO at z ≈ 0.86) and the null Planck×ACT cross-correlation are cleanly presented.

Conservative cosmological scoping. The multi-tracer fNL forecast correctly uses the propagated envelope rather than the noisy central value, reports the de-biased null improvement, and includes the full environmental caveat on the NANOGrav SMBHB interpretation. Neither application is overstated as a detection. The SPHEREx 2.6–5σ forecast is properly conditioned on future survey execution and tracer calibration.

Reproducibility and community utility. The planned public release (catalog tables, model weights, training/inference scripts, MCMC chains, taxonomy galleries, manifest with hashes) plus the explicit "use catalog-grade tier with validity flags" guidance makes this work immediately usable by the wider community.

Overall Assessment
This is a high-quality, carefully executed large-scale data-mining paper that advances both methodology (native-retrain + explicit gate protocol) and discovery potential (multi-survey anomalies + high-z QSO candidates). The scientific claims are well-supported, the limitations are honestly enumerated rather than minimized, and the cosmological applications are appropriately scoped as illustrative secondary science. With the minor clarifications listed above, the manuscript will be ready for acceptance. I recommend MINOR REVISIONS.
The referee is happy to review a revised version.

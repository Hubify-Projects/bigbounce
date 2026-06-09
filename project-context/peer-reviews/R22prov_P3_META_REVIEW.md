# P3 R22prov — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 522.7s

---

Meta-review for “Spectrally Unusual Sources at Scale: …”

I read the rendered PDF and the five prior reports. Below are issues that, to the best of my check, none of the five reviewers flagged. I focus on deep-chain arithmetic, cross-reference consistency, hidden conditioning, post‑hoc selection, and unit/sensitivity pitfalls.

P3-META-E1
- Severity: ESSENTIAL
- Section + page: §II.B (Method: Training and Scoring), Eq. (1), p. 3; §III (survey results) passim
- Why others missed: Most scrutiny was on thresholds and scores, not on the loss functional form itself.
- Specific problem: The anomaly score is built from an unweighted per-element MSE across spectra and catalog vectors: “minimizing per-element mean-squared error (MSE); … S(x) ≡ (MSE(x) − μval)/σval.” For spectra, this ignores per-pixel inverse-variance (noise) weighting and arm-dependent throughput/variance; for photometric vectors it implicitly treats heterogeneous features (e.g., counts vs colors vs errors) as commensurate.
- Required fix: Recompute scores (or at least rerun a validation slice) with an inverse-variance-weighted MSE for spectroscopic data and a feature-scaled (e.g., z‑normalized or Mahalanobis) residual for catalog features; quantify how rankings and rates change. At minimum, add a sensitivity test showing that the top‑N anomalies and key headline fractions are robust to noise-weighted residuals.

P3-META-M1
- Severity: MAJOR
- Section + page: §III.C (SDSS) p. 5; §III.D (LAMOST) p. 6; Table I footnotes ♡ and ♠ p. 8
- Why others missed: Reviewers focused on the “top‑1% misuse (77,905)” but not on the percentile-to-S mapping.
- Specific problem: The paper repeatedly reports “top‑1%” selections whose survey-specific S thresholds are S ≥ 0.1060 (SDSS) and S ≥ 0.4613 (LAMOST). Given S is a “z‑scored” residual on the validation scale, a 99th percentile at S ~ 0.1–0.46 implies the scored distribution is far narrower than the validation distribution, but no evidence is shown. As written, the z‑score semantics and the use of “percentiles” on a different normalization are opaque.
- Required fix: Provide, per survey, histograms of MSE and S for the training/validation pool and for the scored catalog, with the indicated percentile cut marked, to demonstrate how a top‑1% in the scored data can sit at S ≪ 1 on the validation-normalized axis. Explicitly state that percentiles are computed on the scored sample’s S, not on a standard normal.

P3-META-M2
- Severity: MAJOR
- Section + page: §III.A (DESI DR1) p. 4; §IV.A.b “Expected false-match rates” p. 10
- Why others missed: Earlier reviews flagged contradictory cross‑match wording, but not the quantitative implication.
- Specific problem: For the DESI top‑10,000 anomalies, the paper reports “only 0.2% in SIMBAD.” With the authors’ own density estimate nSIMBAD ≈ 3×10^−5 arcsec^−2 and r = 5″, the random-match expectation is Pfalse ≈ πr^2 n ≈ 0.00236 (0.236%). Thus, the observed 0.2% SIMBAD matches are consistent with pure chance. The manuscript presents the low SIMBAD incidence as indicative of novelty without noting this null consistency.
- Required fix: Add the computation and explicitly state that the SIMBAD hit rate for the DESI top‑10k is indistinguishable from random-coincidence expectations; this reinforces the text’s broader point that “SIMBAD-unmatched” is not a novelty rate.

P3-META-M3
- Severity: MAJOR
- Section + page: §IV.D (Planck × ACT cross-correlation) p. 11; §III.F (Planck) p. 6; Appendix F (ACT) p. 20
- Why others missed: Prior reviews asked for a statistic; none noted the de facto disjoint footprints.
- Specific problem: The Planck native retrain uses a |b| ≥ 20° mask; the ACT cross-transfer anomalies “concentrate along the Galactic plane.” The resulting near-disjoint sky regions make a null cross-correlation nearly guaranteed “by construction,” independent of any deeper conclusion about survey-specific systematics.
- Required fix: State explicitly that the two anomaly sets have largely disjoint footprints due to the |b| cuts, quantify the fractional sky overlap of the two anomaly masks, and qualify the “null” as trivial given this geometry unless a masked, overlap‑only cross‑correlation is performed.

P3-META-M4
- Severity: MAJOR
- Section + page: §V.a (Empirical bias measurement) p. 12
- Why others missed: Attention went to Fisher normalization and percent improvements; the randoms construction was not probed.
- Specific problem: The Landy–Szalay measurement uses “26,920 anomaly-window-matched randoms” with a 30‑region jackknife, but the exact survey mask, angular completeness, and depth variations for the anomaly tracer sample are not specified. Given the anomalies are drawn from heterogeneous surveys and selection cuts, the definition of the random catalog is load‑bearing.
- Required fix: Precisely define the angular mask for the QSO-candidate subset and how the randoms are generated to match the on‑sky selection (tile coverage, veto masks, redshift selection if used). Provide a plot of data vs randoms per HEALPix pixel or per angular bin to document adequacy. Otherwise, move the α measurement to an illustrative appendix.

P3-META-M5
- Severity: MAJOR
- Section + page: §III.E (eROSITA) p. 6–7; Table I footnote § p. 8; Table III p. 9
- Why others missed: Others praised the 95.3% “enrichment” but didn’t examine the null model.
- Specific problem: The 95.3× “enrichment over random-independence” between the BigAE S-selection and the IsolationForest set uses a null of independent selections. But the IF is trained on the BigAE latent space (16‑d encoder features), making the detectors highly dependent. “Random independence” is not an appropriate baseline; the 95.3× factor is not meaningful evidence of cross‑method agreement.
- Required fix: Replace the independence null with an appropriate dependent baseline (e.g., compare overlap to an IF trained on raw eROSITA features or to a VAE/OCSVM trained independently). Report Cohen’s κ or another agreement metric that accounts for shared features, and avoid the “× enrichment” phrasing which assumes independence.

P3-META-M6
- Severity: MAJOR
- Section + page: §II.A (Architecture) p. 2; §VI.D(ii) (injection–recovery) p. 15
- Why others missed: They noted poor emission‑line recovery but not the likely architectural cause.
- Specific problem: Spectra are “downsampled by a factor of 16” to 496 bins and scored with an unweighted MSE. This architecture is intrinsically biased toward broad continuum departures and against narrow features; it likely explains the systematically poor emission‑line injection recovery. The manuscript acknowledges “known limits” but does not quantify the impact of the downsampling itself.
- Required fix: Run a small control with higher spectral resolution (e.g., 2× or 4× more bins) and/or a noise‑weighted loss to show how emission‑line sensitivity changes. If infeasible, quantify expected line‑sensitivity degradation from the downsampling kernel (lines vs bin width) and state that narrow-line anomaly discovery is outside the validated capability.

P3-META-M7
- Severity: MAJOR
- Section + page: §II.D (Path‑C gates) p. 3–4
- Why others missed: They critiqued PASS/FAIL heterogeneity but not gate calibration.
- Specific problem: The numerical gate thresholds (e.g., Jaccard ≥ 0.70; injection–recovery ≥ 50% at 5σ) appear ad hoc and not pre‑registered or justified against simulations or prior art. This risks post‑hoc thresholding tuned to “PASS” some surveys and “FAIL” others.
- Required fix: Justify each gate (with references or simulations) or, at minimum, report sensitivity of conclusions to reasonable threshold variations (e.g., what flips if the Jaccard gate were 0.75/0.65, or 5σ recovery gate 40%/60%). Clearly separate hard acceptance criteria from diagnostic checks.

P3-META-m1
- Severity: MINOR
- Section + page: §IV.C (dedup) p. 10–11
- Why others missed: Dedup radius was discussed; epoch propagation was not.
- Specific problem: The text acknowledges not propagating Gaia proper motions to survey epochs, yet draws conclusions from a 5″ fixed-radius dedup across surveys with multi‑year epoch differences. High–proper-motion stars could be systematically under‑matched, suppressing multi‑survey coincidences.
- Required fix: Estimate the fraction of the anomaly sample in the high‑PM tail (e.g., via Gaia PM distribution) for which 5″ over epoch baselines would cause missed matches; either propagate to epochs for these cases or provide a quantitative bound on the missed‑match rate.

P3-META-m2
- Severity: MINOR
- Section + page: §IV.A.b (Expected false-match rates) p. 10; §III.A top‑10k SIMBAD result p. 4
- Why others missed: They caught contradictory wording, not this compositional point.
- Specific problem: The “none of the top 100 appear in any database” statement sits next to an extended 20‑catalog match result for the top‑1,000 (82.2% archival IDs). The top‑100 subset result is not reconciled with the per‑source false‑match expectation nor with the broader 20‑catalog outcome.
- Required fix: Reword to avoid “any database” unless strictly limited to named spectroscopic databases. Provide exact per-database counts for top‑100 and harmonize with the 20‑catalog top‑1,000 result.

P3-META-m3
- Severity: MINOR
- Section + page: §IV.B (Spatial analysis) p. 10
- Why others missed: They questioned χ^2 usage; not the sample composition.
- Specific problem: It is unclear whether the combined-catalog latitude/dust correlations include the 200 Planck patches (sky regions) along with point sources. Counting map patches and point sources together in per‑pixel counts can bias the interpretation.
- Required fix: State explicitly whether Planck patches were excluded from the “point-source” spatial tests. If included, repeat the correlations for point sources only and report both.

P3-META-m4
- Severity: MINOR
- Section + page: §IV.C (random-coincidence budget) p. 11
- Why others missed: Focus was on radius sensitivity, not the chance‑coincidence estimate itself.
- Specific problem: “Expected random coincidence contribution is ≲ 10 across all survey pairs” is asserted without showing the calculation despite highly non‑uniform survey densities and footprints.
- Required fix: Provide the computation (pairwise areal densities, sky area overlap, πr^2 factor) or move this to an appendix with numbers per major pair; otherwise soften to a qualitative “negligible.”

P3-META-m5
- Severity: MINOR
- Section + page: §III.A (DESI DR1) p. 4; §II.B p. 3
- Why others missed: The numeric equality slid by because μval=val_loss can happen; here the conflation matters.
- Specific problem: The same quantity 0.0287 is used as both “validation MSE μval” in the S definition context and as the “val loss at convergence.” These are the same only if the reported loss is the mean MSE over the validation set at the exact same preprocessing/normalization. If val_loss includes regularization or different scaling, μval≠val_loss.
- Required fix: Clarify precisely that μval is the mean MSE over the held‑out pool at convergence with the exact same preprocessing used for scoring, and that it equals the reported validation loss. If not, report μval explicitly.

P3-META-m6
- Severity: MINOR
- Section + page: §III.B (High‑z QSO candidates) p. 5; Fig. 12 caption p. 19
- Why others missed: They flagged AE value scale in Fig. 12 elsewhere; the selection’s false‑positive control wasn’t queried.
- Specific problem: The z ≈ 6 candidates are defined by three signatures (GP trough, rZ dominance, ≥1 emission line), but there is no estimate of the false‑positive rate under the model’s reconstruction and downsampled spectral resolution.
- Required fix: Provide a back‑of‑the‑envelope false‑positive estimate (e.g., apply the same cuts to random non‑anomaly DESI spectra to estimate contamination) or clearly label these as unvetted candidates pending follow‑up.

P3-META-N1
- Severity: NIT
- Section + page: §III.H (NEOWISE), Fig. 5 caption p. 9
- Why others missed: Focus was on score definition and polar-cap fraction; not on unit consistency in the image.
- Specific problem: The DESI Legacy DR9 cutout is labeled “256 × 256 pixels (108″ × 108″)”; Legacy Survey DR9 imaging typically has ~0.262″/pix, so 256 px ≈ 67″, not 108″. If binned or resampled, this needs stating.
- Required fix: Confirm pixel scale and either correct the angular size or note any binning/resampling used to arrive at 108″ per 256‑px stamp.

Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential and major blockers: dimensional/normalization issues in the Fisher summary, inconsistent/unclear database cross-matching claims, implausible or unlabeled training times, ambiguous ACT totals and cross-correlation claims, missing injection–recovery and dedup sensitivity specifics, and, additionally from this meta‑review, the noise‑weighting omission in the loss, the trivial geometry behind the Planck×ACT “null,” an invalid independence baseline for the eROSITA cross‑validation, un‑justified acceptance gates, and percentile/z‑score mapping opacity. My estimate is 10–15 substantive fixes across analysis, figures/tables, and text. Confidence that the paper would survive external (non‑BigBounce) peer review is moderate if the authors address these systematically; the data product is valuable, but the methodological and presentation corrections are necessary for PRD standards.
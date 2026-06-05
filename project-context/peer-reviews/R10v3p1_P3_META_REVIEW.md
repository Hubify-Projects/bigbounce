# P3 R10v3p1 — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 348.2s

---

Meta-review: Blind spots not caught by the 5 prior referees

P3-META-E1
Severity: ESSENTIAL
Section + page: §II D, Step 6, p. 3–4 (“7-way positional dedup at 5′′”); §IV C, p. 10 (multi-survey coincidences)
Why others missed it: Reviewers questioned false-match arithmetic but did not examine astrometric systematics and epoch/proper-motion effects of a fixed 5″ radius across heterogeneous surveys.
Specific problem: The paper applies a uniform 5″ positional deduplication radius across DESI/SDSS/LAMOST (sub-arcsec astrometry), Gaia (sub-0.1″ with non-negligible proper motions), and NEOWISE (∼6″ PSF) without (i) epoch propagation of Gaia proper motions, (ii) survey-dependent error ellipses/beam sizes, or (iii) crowding-aware logic in dense regions (e.g., LMC, Galactic plane tails). This can over-merge unrelated neighbors and wrongly collapse moving objects, while simultaneously under-merging NEOWISE counterparts where 5″ is smaller than the effective beam-convolved matching kernel.
Required fix: Replace the single 5″ rule with a survey-pair–specific probabilistic cross-match (e.g., Budavári–Szalay) that ingests positional uncertainties, epochs, proper motions (for Gaia), and PSF/beam models (for NEOWISE). Recompute the 10,213 collapsed detections and the 637 multi-survey coincidences with this robust matcher, and propagate the change to the 378,280 headline. Report a per-pair false/over-merge rate with Monte Carlo under the real masks.

P3-META-E2
Severity: ESSENTIAL
Section + page: §III F (Planck), p. 6; Table V, p. 15
Why others missed it: Reviewers noted gate logic but not the internal inconsistency in training/scan set sizes for Planck.
Specific problem: The text says “trained on 2×10^5 galactic-plane-masked … SMICA patches,” but the Planck “Input” for anomaly selection is “20,000 … patches” and the Table V training time is “10.6” (seconds) for a 1.1M-parameter ConvAE. This is inconsistent on three fronts: (i) where did the additional 180,000 training patches come from if only 20,000 are “Input”? (ii) 10.6 seconds is implausible for training on 2×10^5 64×64 images; (iii) the validation set and scoring set are not clearly partitioned, risking leakage.
Required fix: Clarify the Planck data universe: total number of available patches, training/validation/test splits, and which distinct set was scanned to produce the 200 anomalies. Correct the training time units (likely minutes or hours), provide hardware/epochs/batch size, and certify there is no overlap between training/validation and the 20,000 scored patches.

P3-META-E3
Severity: ESSENTIAL
Section + page: Table V (Computational details), p. 15
Why others missed it: Others critiqued methodology; none audited the physical plausibility of the training-time units.
Specific problem: Planck ConvAE “Train time (s) = 10.6” for 2×10^5 patches and 1.1M parameters is not credible on an A100, even with aggressive mixed precision; eROSITA/Gaia/NEOWISE times are also reported as seconds without dataset sizes for the training split. These figures are non-reproducible as stated.
Required fix: Report training durations with correct units and context (epochs, optimizer, batch size, mixed precision yes/no, data loader throughput) and give uncertainty or variance across reruns. If the Planck training size was smaller (e.g., 20k patches), correct the earlier “2×10^5” statement and align all numbers.

P3-META-E4
Severity: MAJOR
Section + page: §II A, p. 2; §III D, p. 6
Why others missed it: LAMOST issues were discussed, but not the band-definition mismatch.
Specific problem: The paper defines per-band residuals rB, rR, rZ over fixed DESI-like ranges (3600–6200 Å, 6200–8200 Å, 8200–9800 Å) “for spectroscopic surveys (DESI, SDSS, LAMOST)”. LAMOST does not have a DESI-like Z arm and nominally covers ≲9100 Å. Using a DESI-derived Z window (8200–9800 Å) on LAMOST forces a partially out-of-coverage band, biasing rZ and any band-dominance taxonomy.
Required fix: Redefine per-band windows per survey according to instrument coverage, or compute residuals on a common overlap wavelength grid after masking absent channels. Recompute per-band dominance statistics and any taxonomy or candidate selections that used rB/rR/rZ on LAMOST (and, if used, SDSS’s exact coverage).

P3-META-E5
Severity: MAJOR
Section + page: §IV A, p. 9 (“20 curated all-sky catalogs via CDS X-Match”)
Why others missed it: Reviewers disputed extrapolation but not the “all-sky” designation itself.
Specific problem: The list includes DES DR2, SDSS DR12/DR16, Pan-STARRS1, VLASS—none of which are all-sky. Labeling the union as “all-sky catalogs” is incorrect and biases the interpretation of the 82.2% archival-ID and the residual 17.8% novelty fraction because footprint incompleteness is not modeled.
Required fix: Restrict the novelty audit to truly all-sky catalogs (e.g., Gaia, 2MASS, AllWISE/CatWISE, unWISE, NVSS where applicable) or apply per-object footprint masks so a “non-match” is counted only where the catalog covers that position. Recompute the 82.2% and 17.8% with proper coverage conditioning and quote uncertainties.

P3-META-E6
Severity: MAJOR
Section + page: §II B, p. 2
Why others missed it: Others focused on threshold comparability; no one flagged the calibration wording.
Specific problem (quote): “For DESI DR1, μval ≈ 0.0287 … and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143 …” In a z-score S = (MSE − μval)/σval, σval should be measured on the validation set, not “set such that” a chosen threshold maps to an MSE value. This reads as post-hoc calibration of σval to a preferred MSE cutoff.
Required fix: Replace with the actual σval measured on the validation split and report the implied MSE at S=5 with uncertainty. If a different re-scaling was intentionally applied, define it explicitly (e.g., S̃ = (MSE − μval)/σ̃) and justify why this alternate σ̃ was used.

P3-META-E7
Severity: MAJOR
Section + page: §III C, p. 6; Table I, p. 7
Why others missed it: One review noted SDSS percentile inconsistency; none flagged the Ntotal mismatch across sections.
Specific problem: SDSS “Input: 2,304,830 spectra” (Table I) versus “native re-score complete across 1,925,279 DR18 spectra” (§III C). The published native SDSS anomaly count (77,905 at S ≥ 0.1060) is 4.05% of 1.925M, not 3.38% of 2.305M. The Table’s Ntotal and the text’s processed-N disagree, confounding rate comparisons and dedup accounting.
Required fix: Unify the SDSS Ntotal across the manuscript. If the native run used a quality-selected subset (1.925M), list that value in Table I and recompute the reported percentage and any aggregate statistics that used 2.305M.

P3-META-M1
Severity: MAJOR
Section + page: §V c and §VI D (e), p. 10–12
Why others missed it: Reviewers questioned the Fisher form, not the GR correction magnitude claim.
Specific problem (quote): “General-relativistic projection corrections (O(H^2/k^2)) contribute |Δσ/σ| < 0.02% at kmax = 0.2 h Mpc−1 (plane-parallel monopole …).” fNL sensitivity is driven by the largest scales (small k), where relativistic number-count terms are not negligible. A blanket 0.02% claim without derivation, survey window, or redshift distribution is not credible.
Required fix: Provide a calculation (e.g., CLASSgal or equivalent) showing the additive GR terms’ impact on the large-scale clustering and on the forecasted Fisher information with the actual redshift/area/tracer weights used. If not performed, remove the 0.02% statement and replace with a conservative bound or a citation-supported range.

P3-META-M2
Severity: MAJOR
Section + page: §III H, p. 8; Fig. 4 caption; §II D step 4, p. 3
Why others missed it: Others accepted the 2.6× excess at face value; none checked the null model.
Specific problem: The NEOWISE polar-cap excess (3.9% vs 1.52% uniform-sphere expectation) is used to “confirm scan-pattern contamination,” but the null tested is uniform-on-sphere, not the known highly non-uniform NEOWISE scanning-law exposure. This test cannot diagnose contamination relative to the correct null.
Required fix: Build the NEOWISE exposure-based null (e.g., from depth/coverage maps) and quantify the polar-cap enrichment relative to that, with uncertainties. If unavailable, downgrade the claim to a qualitative note and remove the quantitative “2.6×” language.

P3-META-M3
Severity: MAJOR
Section + page: §IV C (cross-survey matches), p. 10–11; Fig. 6
Why others missed it: Reviewers criticized using ACT for cross-correlation; none noted cross-survey matches mixing cross-transfer and native SDSS scores.
Specific problem: In the DESI×SDSS examples, the SDSS anomaly score shown for TIC 374313355 is 49.5, a value characteristic of the cross-transfer run (Fig. 2 right), not the native SDSS scoring used elsewhere. Presenting a cross-transfer score in a headline cross-survey match conflicts with the paper’s own statement that cross-transfer outputs are diagnostic-only.
Required fix: Replace the SDSS scores in Fig. 6 with the native SDSS scores, or explicitly label them as cross-transfer artifacts and exclude them from any quantitative claims. Verify that all three cross-survey match examples use the same, final anomaly definition.

P3-META-M4
Severity: MAJOR
Section + page: §II A, p. 2 (photometric/census inputs); Eq. (1), p. 2
Why others missed it: One review flagged variance weighting for spectra; none addressed feature scaling for tabular surveys.
Specific problem: For photometric/catalog surveys (eROSITA 47, Gaia 20, NEOWISE 15 features), no per-feature standardization is reported prior to computing MSE in Eq. (1). Raw-feature MSE will be dominated by the largest-scale or most heteroscedastic columns (e.g., fluxes vs flags), making the anomaly score depend on units/scale rather than physical outlierness.
Required fix: Standardize each feature (mean 0, unit variance) or whiten using the training covariance before training/scoring. Recompute photometric anomaly scores, thresholds, and overlaps (eROSITA IF cross-validation numbers will likely change).

P3-META-M5
Severity: MINOR
Section + page: §III F (Planck), p. 6
Why others missed it: Reviewers focused on gate logic; none on score-scale definition.
Specific problem: Planck “Top-200 native anomaly patches (score range [0.558, 0.621])” are reported without defining whether this “score” is the canonical S = (MSE−μval)/σval or a raw MSE from the ConvAE. The range (∼0.6) is inconsistent with the “S>5” convention used elsewhere.
Required fix: Define the Planck score axis explicitly (z-scored MSE vs raw loss), give μval/σval for the ConvAE if S is used, and state the selection threshold in that metric.

P3-META-m1
Severity: MINOR
Section + page: §II B, p. 2; Appendix D, p. 16
Why others missed it: Prior reviews focused on SDSS taxonomy breadth; none on method disclosure.
Specific problem: The manuscript claims SDSS cross-transfer anomalies are “ultra-cool dwarfs (M7–T2)” and Table II lists 10 spectral categories, but no method is given for mapping latent clusters to astrophysical types beyond SIMBAD name presence/absence. This risks circular labeling (database class ≠ spectral class).
Required fix: Provide an explicit taxonomy method (e.g., template fitting, color–spectral-type mapping, or a supervised classifier on a labeled subset) and a confusion matrix against external types. Otherwise, phrase the labels as “likely” and avoid hard class names (M7–T2, BAL QSO) without spectroscopic confirmation.

P3-META-m2
Severity: MINOR
Section + page: §V b, p. 10
Why others missed it: Reviewers critiqued the Fisher form; none flagged the 2D–3D mismatch context.
Specific problem: The α measurement is from an angular 2-point Landy–Szalay (θ ∈ [0.04°, 0.25°]), yet the forecast discussion immediately references kmax = 0.2 h Mpc−1 and 3D Fisher blocks without describing the mapping between the 2D mask/selection and the 3D Fisher configuration. The link between the measured α and the (3D) Fisher setup is missing.
Required fix: Add the projection formalism (Limber or full non-Limber) that maps the angular α measurement into the 3D Fisher pipeline, or perform the α measurement in 3D (with photo-z or spectroscopic z) to match the forecast model. State the redshift distributions used.

P3-META-N1
Severity: NIT
Section + page: §III E, p. 6–8; politicized wording
Why others missed it: Focus was on methods; this is editorial tone.
Specific problem: “eROSITA DR1 … eastern half under Rosatom proprietary control” is not an appropriate or precise data-rights description for a PRD manuscript and can age poorly; the correct phrasing is about SRG consortium data policies.
Required fix: Replace with a neutral, factual statement about data availability (e.g., “DR1 includes the western Galactic hemisphere; eastern hemisphere data are not publicly released by the SRG consortium at this time.”)

Meta-review recommendation
REJECT

Given the union of all six reviews, there are now multiple independent essential blockers: training/scan inconsistencies and implausible timings (E2–E3), improper cross-match/dedup methodology (E1), mis-specified novelty audit (E5), ambiguous score calibration (E6), and SDSS Ntotal inconsistency (E7), on top of previously raised broken references, unresolved “Fig. ??” placeholders, gate violations, and ad hoc Fisher modeling. My confidence that the paper would survive external peer review in its present form is very low. Even after major revision, the project likely needs to be split (validated catalog/data paper vs. a separate, defensible cosmology analysis) and to correct methodological foundations (cross-match, feature scaling, GR/systematics modeling) before PRD-level acceptance is realistic.
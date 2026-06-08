# P3 auto-2026-06-08_1354pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 496.1s

---

Meta-review for “Spectrally Unusual Sources at Scale: …”

Below are issues that, to the best of my check, were not flagged by any of the five prior referees. I focused on end‑to‑end arithmetic consistency, hidden assumptions in scoring/normalization, deduplication geometry, and workload accounting.

P3-META-E1
- Severity: ESSENTIAL
- Section + page: II.C GPU Inference Pipeline (p. 3)
- Why others missed it: Most attention went to catalog thresholds and cosmology; few audited the wall‑clock accounting against the stated throughputs.
- Specific problem (quote): “The total processing time … was approximately 42 hours (wall‑clock), dominated by the DESI DR1 scan (19,705 s …) and the LAMOST DR10 scan (11.4M). The CMB and photometric surveys each required < 10 seconds of GPU time.”
- Required fix: Reconcile the 42 h total with per‑survey runtimes implied by the reported throughputs (e.g., DESI ≈5.5 h at 1,142 spectra/s for 22.5 M; LAMOST ≈3.3 h at 950 spectra/s for 11.4 M; SDSS ≈0.6 h; Planck/Gaia/NEOWISE/eROSITA are seconds). Either correct the total, or document additional wall‑clock components (I/O, CPU preprocessing, retries, queueing) with an itemized breakdown.

P3-META-E2
- Severity: ESSENTIAL
- Section + page: III.A DESI DR1 (p. 4–5)
- Why others missed it: It’s a narrative inconsistency rather than a number mismatch; easy to gloss over.
- Specific problem (quote): “We processed all 22,504,897 coadded spectra from the Main Survey across the five primary target classes: BGS, LRG, ELG, QSO, and MWS.” Versus later in same subsection: “Across the 6.5 million spectra in DESI DR1 that carry a validated TARGETTYPE classification … the remaining ∼16 million spectra are unclassified filler targets, sky fibers, or calibration exposures…”
- Required fix: Clarify precisely which spectra are included in the 22.5 M production scan vs which belong to the “five primary target classes.” If ∼16 M are not in those classes, do not describe the full 22.5 M as “across the five primary target classes.” Provide exact class fractions and how non‑science fibers were treated in training/scoring and the per‑class rate statements.

P3-META-M1
- Severity: MAJOR
- Section + page: II.A Architecture + II.B Training and Scoring (pp. 2–3), III.A (p. 4)
- Why others missed it: Most critiques focused on thresholds/domains, not the loss definition vs instrument noise.
- Specific problem: The anomaly score is raw per‑element MSE (Eq. 1) without any statement of inverse‑variance weighting or per‑wavelength noise standardization; yet DESI’s three arms have markedly different noise and throughput. A raw MSE makes the anomaly metric depend on absolute flux scale and arm‑dependent noise, not just spectral morphology.
- Required fix: State whether inputs were variance‑whitened or continuum‑normalized per spectrum/arm. If not, quantify how S changes under inverse‑variance weighting and/or per‑arm normalization, and provide a sensitivity test (e.g., re‑score a held‑out subset with noise‑weighted MSE). If such normalization was used, document it explicitly (scaling, units).

P3-META-M2
- Severity: MAJOR
- Section + page: III.E eROSITA DR1, III.G Gaia DR3 (pp. 6, 8), II.A (p. 2)
- Why others missed it: The photometric tiers attracted fewer technical critiques than the spectroscopy/CMB tiers.
- Specific problem: For catalog/photometric surveys you state “input dimension matches the number of catalog features …” but there is no statement that heterogeneous features (mixed units/scales) were standardized before training. Using raw MSE on unstandardized features yields a distance dominated by whichever column has the largest dynamic range or unit choice.
- Required fix: Document per‑feature preprocessing (mean/variance standardization, clipping, transforms) used for eROSITA, Gaia, NEOWISE. If none, re‑run a feature‑standardized variant on a held‑out subset and report the effect on anomaly ranking, particularly for the eROSITA top‑298.

P3-META-M3
- Severity: MAJOR
- Section + page: II.D Step 6 + IV.C Cross-survey analysis (pp. 3, 10)
- Why others missed it: Prior reviews focused on 5″ radius choice; not on graph‑theory artifacts.
- Specific problem: Deduplication uses a friends‑of‑friends union‑find at a uniform 5″ linking length across seven surveys with disparate PSFs/epochs and no cap on cluster diameter. FOF can percolate via chains (A within 5″ of B, B within 5″ of C, etc.), producing associations whose endpoints are separated by >>5″ and potentially mismatched across epochs/PSFs.
- Required fix: Report the distribution of cluster sizes and maximum intra‑cluster separations; enforce a hard cap (e.g., all pairwise separations ≤5″) or adopt a probabilistic cross‑match (Budavári–Szalay) with per‑survey astrometric errors/proper‑motion propagation. Provide a sensitivity test showing the unique‑object count under a non‑percolating matcher.

P3-META-M4
- Severity: MAJOR
- Section + page: II.B Training and Scoring (p. 2), III.A (p. 4), Fig. 6 (p. 11)
- Why others missed it: Assumed standard in spectroscopy, but it is never stated here.
- Specific problem: The manuscript never specifies flux normalization before AE input (e.g., median/continuum normalization, per‑arm scaling, log‑flux). Figures show “Norm. flux” for display, but it is unclear if the AE is trained on normalized flux or raw coadded flux. Without consistent normalization, S can be driven by overall flux level differences (weather/exposure depth) rather than morphology.
- Required fix: Explicitly state the spectral preprocessing applied prior to training/inference (e.g., per‑spectrum continuum normalization, sigma‑clipping, arm‑by‑arm scaling). If no normalization was used, quantify the dependence of S on overall flux scale and demonstrate stability across exposure depth bins.

P3-META-M5
- Severity: MAJOR
- Section + page: IV.C Cross-Survey Matches (p. 10)
- Why others missed it: The 5″ choice was discussed, but not epoch/proper‑motion effects.
- Specific problem: Matching ignores epoch differences and proper motions, yet Gaia DR3 anomalies are variable stars where μ can be large; NEOWISE/SDSS/DESI epochs differ by many years. This risks false non‑matches (missing real associations) and, conversely, spurious matches where a high‑μ source moved into a 5″ radius by chance at a later epoch.
- Required fix: For Gaia‑involving pairs, re‑compute a test match with Gaia positions propagated to the other survey’s epoch (or inflate Gaia error accordingly) and report how many additional matches appear/disappear. At minimum, state the epoch spans for each survey and quantify the expected loss rate for μ > 100 mas/yr under a 5″ radius.

P3-META-M6
- Severity: MAJOR
- Section + page: II.B (p. 2–3), III.C (p. 5), Table I footnote (p. 7)
- Why others missed it: Many flagged percentile inconsistencies, but not the root definitional clash.
- Specific problem: The paper promises “S refers without exception to the per‑survey standardized (z‑scored) residual w.r.t. that survey’s validation split,” yet the SDSS/LAMOST cross‑transfer baselines and the SDSS “top‑77,905 at S ≥ 0.1060” continuity slice explicitly use the DESI‑trained scale. Thus “S” does not, in fact, have a single definition across the paper; it is a survey‑native z‑score in some places and a DESI‑anchored cross‑survey score in others.
- Required fix: Separate the symbols: use, e.g., S_native for true per‑survey z‑scored residuals and S_DESI→X for DESI‑anchored cross‑transfer scores. Retitle every threshold and figure axis accordingly, and provide a one‑paragraph mapping between them where you compare or union the selections.

P3-META-m1
- Severity: MINOR
- Section + page: III.A DESI DR1 (p. 4)
- Why others missed it: It looks like an innocuous sanity check.
- Specific problem: “Spearman rank correlation between anomaly score and SNR is ρ = −0.03 (p = 0.12 on a stratified subsample of 2,670 spectra, log‑uniform in SNR)…” There is no definition of the SNR used (per pixel? per arm? median? pipeline metric?), nor the estimator details (robustness to outliers), so its interpretability is limited.
- Required fix: Define the SNR metric (e.g., median per‑pixel S/N in the R arm over rest‑frame 6200–8200 Å) and how it was computed for DESI coadds. Provide the same Spearman test for each arm (B,R,Z) to check for arm‑driven calibration bias.

P3-META-m2
- Severity: MINOR
- Section + page: III.H NEOWISE (p. 8)
- Why others missed it: The pole‑mask arithmetic was accepted at face value.
- Specific problem: The ecliptic‑cap excess is stated as “2.6× the uniform‑null expectation (1.52%).” That expectation depends on how |b_ecl| was computed (ICRS→ecliptic transform, epoch), the mask’s edge definition, and whether the candidate pool was already latitude‑biased. None of this is specified here.
- Required fix: Explicitly state the coordinate system/epoch and show the area fraction calculation for |b_ecl| ≥ 80° (or cite a short derivation) and whether the base sample prior to selection is uniform in ecliptic latitude. Add a one‑line uncertainty (binomial 95% CI) for the 3.9% observed fraction.

P3-META-m3
- Severity: MINOR
- Section + page: Table V (p. 16)
- Why others missed it: Attention was on the Planck CAE line; not on consistency across rows.
- Specific problem: “Train time (s)” is reported to single‑digit seconds for eROSITA/Gaia/NEOWISE, but the main text states training runs “up to 200 epochs with early stopping” and “typically at 100–150 epochs.” Without the number of epochs and training‑set sizes per survey, these times are not reproducible.
- Required fix: Add the actual number of epochs run for each native retrain, the training‑set size used, and the hardware used for training in Table V (or a footnote). If these are warm‑starts or shallow‑epoch runs, state that.

P3-META-N1
- Severity: NIT
- Section + page: II (p. 2): “Sections II–II D describe the method…”
- Why others missed it: Simple editorial glitch overshadowed by larger issues.
- Specific problem: “Sections II–II D” is odd phrasing; likely intended “Sections II–II.D” or “Section II and II.D”.
- Required fix: Correct the cross‑reference phrasing.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential/major blockers: inconsistent thresholding and catalog composition, arithmetic inconsistencies in the fNL forecast, broken cross‑references, the inclusion of gate‑FAIL tiers in the headline, and (from this meta‑review) a hard inconsistency in the 42 h wall‑clock accounting, unresolved normalization/whitening for the AE loss across heterogeneous noise/features, and FOF dedup percolation risks without diagnostics. My estimate is ≥12 independent blockers that must be fixed for PRD standards. Confidence that the paper would survive external peer review without these changes is low; with a thorough rewrite that (i) standardizes scoring/threshold definitions, (ii) removes or demotes gate‑FAIL tiers from the headline, (iii) corrects all arithmetic and cross‑references, (iv) documents preprocessing/weighting, and (v) reconciles runtime accounting and dedup geometry, the manuscript could become publishable.
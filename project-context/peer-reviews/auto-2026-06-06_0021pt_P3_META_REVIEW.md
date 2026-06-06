# P3 auto-2026-06-06_0021pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 376.5s

---

META-REFEREE REPORT — PRD submission “Spectrally Unusual Sources at Scale: …”

Scope
I read the rendered PDF (20 pages plus figures/tables/appendices) and all five prior reports. Below are issues that, to the best of my audit, none of the five reviewers identified. I bias toward hard-to-catch classes (end-to-end arithmetic chains, cross-reference inconsistencies, hidden conditioning, fairness of comparisons, unit/dimensional pitfalls).

New findings

P3-META-E1
- Severity: ESSENTIAL
- Section/page: IV.B Spatial Analysis, p. 9–10
- Why others missed it: They critiqued the test qualitatively but did not check the HEALPix bookkeeping.
- Problem (quote): “A spatial uniformity test across 38,330 HEALPix pixels (Nside = 64) … χ2 = 143,936, dof = 38,329.”
- Issue: For Nside = 64, the full-sky pixel count is 12 Nside^2 = 49,152, not 38,330. If a mask was applied, it is not described; if “occupied pixels” were used, the degrees of freedom are not the appropriate count for a uniformity test on a masked sky. The χ2 and ν (and hence χ2/ν) are uninterpretable without a precisely specified sky mask and the corresponding expectation per pixel under that mask.
- Required fix: Specify the exact sky mask used (and why 38,330 pixels remain), how the expected per-pixel counts are computed under that mask, and recompute χ2 and dof accordingly. If no explicit completeness model is available, drop the χ2 result and replace it with a masked-sky Monte Carlo with correct dof accounting.

P3-META-E2
- Severity: ESSENTIAL
- Section/page: II.D (Path-C rebuild gates), Fig. 7 (p. 13), and throughout
- Why others missed it: They discussed gate outcomes but did not notice the anchor survey is absent from the injection gate summary.
- Problem (quote): Step 5 lists six surveys; Fig. 7 reports SDSS, LAMOST, eROSITA, Gaia, Planck, NEOWISE. DESI is not shown and no DESI injection–recovery number is reported anywhere.
- Issue: The anchor survey (DESI) is not subjected to the stated injection–recovery gate, yet its catalog drives many claims. This is an asymmetric validation gap relative to the other surveys.
- Required fix: Run and report DESI injection–recovery (for both continuum and emission-line plants, matched to the DESI noise properties) at the same amplitude grid and quote the 5σ recovery. If infeasible, explicitly downgrade DESI’s validation status and rephrase claims that rely on DESI’s completeness/sensitivity.

P3-META-E3
- Severity: ESSENTIAL
- Section/page: II.D Step 6 (p. 3), IV.C (p. 10–11), Table I footnotes (p. 7)
- Why others missed it: They discussed false-match arithmetic but not the dedup radius validity across bands.
- Problem (quote): “7-way positional dedup at 5″.” Applied uniformly to all surveys; also 5″ SIMBAD cone used for novelty and the multi-catalog CDS X-Match.
- Issue: A fixed 5″ matching radius is not appropriate across surveys with very different astrometric precisions and beam sizes (e.g., eROSITA typical 68–90% positional uncertainties often >5″; NVSS/VLASS radio positions; Planck patches are not point sources). This likely under-merges true cross-survey duplicates and biases “unique object” and “multi-survey coincidences” downward, while simultaneously biasing novelty upward for X-ray/radio matches.
- Required fix: Use survey-pair-specific matching radii (or probabilistic cross-matching using positional uncertainties), and rerun the 7-way dedup and novelty accounting. At minimum, add a sensitivity study showing how the unique-object count and 637 multi-survey clusters change for eROSITA- and radio-inclusive pairs under 5″/10″/15″.

P3-META-E4
- Severity: MAJOR
- Section/page: III.F Planck CMB (p. 6)
- Why others missed it: They focused on gate criteria and cross-correlation but not on train/test leakage risk.
- Problem (quote): “Native convolutional autoencoder trained on 2×105 masked patches … Input: 20,000 SMICA patches … Top-200 native anomaly patches form the catalog’s Planck tier.”
- Issue: It is not stated that the 20,000 scanned patches are disjoint from the 200,000 training patches; the paper elsewhere acknowledges training–test overlap for DESI but does not address it for Planck. If overlap exists, it will deflate reconstruction error and contaminate the anomaly selection.
- Required fix: State and enforce a strict disjointness between training, validation, and scan sets for Planck. If any overlap existed, rerun the scan on a held-out set and update counts/patches.

P3-META-E5
- Severity: MAJOR
- Section/page: II.A–B (pp. 2–3), III.E–H (pp. 6–8)
- Why others missed it: Score-scale inconsistencies were noted, but not the root cause in feature scaling.
- Problem (quote): “input dimension matches the number of catalog features (47, 20, 15, respectively) … minimizing per-element MSE.” No description of feature scaling/standardization per feature for photometric/catalog inputs.
- Issue: Without per-feature normalization (e.g., z-scoring each input feature on the training set), unweighted MSE is dominated by features with the largest numeric scales or variances. This compromises anomaly scoring comparability within each photometric survey and across surveys, independent of the S rescaling.
- Required fix: Document the per-feature preprocessing (e.g., mean/variance normalization) for eROSITA, Gaia, NEOWISE (and any catalog-like inputs). If not performed, do so and recompute anomaly scores and thresholds; otherwise, quantify the impact via ablation (with/without scaling).

P3-META-M6
- Severity: MAJOR
- Section/page: IV.A (“Archival cross-match and genuine novelty fraction,” p. 9)
- Why others missed it: They flagged the lack of error bars; not the cross-match geometry.
- Problem (quote): “cross-matched against 20 curated all-sky catalogs via CDS X-Match (… NVSS, VLASS, 4XMM, Chandra, …) using a 5-arcsec cone; archival-ID rate 82.2%.”
- Issue: A uniform 5″ cone is too small for some radio/X-ray catalogs (NVSS beam ~45″; X-ray positional errors often >5″), so the “no counterpart” bin is inflated for those domains. This structurally biases the 17.8% “genuine novelty” upward.
- Required fix: Redo the 20-catalog cross-match with catalog-appropriate radii (or an uncertainty-aware match), and provide the adjusted archival-ID fraction with a bootstrap uncertainty. Report the sensitivity of the 17.8% to radius choices by catalog family.

P3-META-M7
- Severity: MAJOR
- Section/page: V.A (“Empirical bias measurement,” p. 10)
- Why others missed it: They critiqued σ(fNL) formulas and GR terms; not the random catalog adequacy.
- Problem (quote): “5,384 QSO-candidate sample … 26,920 anomaly-window-matched randoms … Landy–Szalay … jackknife 30 regions, θ ∈ [0.04°, 0.25°].”
- Issue: The random catalog is only 5× the data catalog. For small scales and irregular selection, this is typically marginal; standard practice uses ≳10× (often 20–50×) to suppress DR and RR shot noise. With 30 jackknife regions, the random insufficiency inflates variance and can bias the α estimate.
- Required fix: Regenerate the random catalog at ≥20× the data size, recompute w(θ) and α with the same jackknife, and report any change. If keeping 5×, justify with variance diagnostics (e.g., RR error vs. signal).

P3-META-M8
- Severity: MAJOR
- Section/page: III.H NEOWISE (p. 8), IV.A novelty and cross-match (p. 9)
- Why others missed it: They discussed polar caps and thresholds, not astrometry epochs.
- Problem (quote): NEOWISE top anomaly matched to a DESI Legacy Survey grz cutout; “no SIMBAD entry within 5″.”
- Issue: No proper-motion correction is applied when cross-identifying NEOWISE (multi-epoch mid-IR, 2014–2024) to optical imaging epochs (DESI-LS, Gaia). High-proper-motion stars can move >5″ over a decade, leading to false “no counterpart” and inflating novelty and anomaly rates in the polar regions (where scanning cadence differences also matter).
- Required fix: Apply a proper-motion-aware cross-match for NEOWISE↔optical/Gaia (propagate to a common epoch), and re-evaluate novelty/non-matches for bright/saturated optical counterparts.

P3-META-m9
- Severity: MINOR
- Section/page: II.B Training & scoring (p. 2), III.A–D (pp. 4–6)
- Why others missed it: They focused on σval wording; not on noise weighting.
- Problem (quote): “minimizing per-element MSE” and “SNR independence ρ = −0.03.”
- Issue: For spectra, per-pixel MSE is unweighted by the per-pixel variance, despite very non-uniform flux uncertainties across arms and wavelength. The reported global Spearman ρ (−0.03) on a small subsample does not substitute for an explicit inverse-variance weighting or per-arm noise equalization during training/scoring.
- Required fix: Either retrain/score with inverse-variance weighting (if per-pixel σ is available) or justify with a more robust SNR–S audit across the full DESI sample (stratified by arm and SNR) and provide per-arm weighted vs. unweighted comparisons.

P3-META-m10
- Severity: MINOR
- Section/page: III.B Confirmed high-z QSO candidates (p. 5)
- Why others missed it: They asked for redshifts/lines for examples, but not this internal consistency.
- Problem (quote): “Applying these three cuts … yields 12 candidates with z = 6.0–6.23.” Table VI lists only 19 Z‑dominant anomalies overall, which implies the selection is extraordinarily restrictive but the exact query and sample definition are not provided.
- Issue: The three-cut filter is undefined operationally (e.g., how “at least one detected line” was algorithmically enforced and over what windows). Reproducibility is not possible from the text alone.
- Required fix: Provide a precise, reproducible definition of the three filters (algorithm, line windows, S/N thresholds), and release the 12-object list with coordinates and measured z for verification.

P3-META-N11
- Severity: NIT
- Section/page: II.C GPU inference (p. 3)
- Why others missed it: They focused on training times; this is a small clarity point.
- Problem (quote): “The CMB and photometric surveys each required < 10 seconds of GPU time.” It reads like end‑to‑end time but is plausibly inference‑only; training is elsewhere.
- Required fix: Label this explicitly as “inference wall-clock,” and add corresponding training-wall clocks for the same domains (or say “training not applicable/not performed” for cross-transfer placeholders).

Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, I count at least 8–10 true blockers: incorrect Fisher baseline in the main text; unresolved/missing figures; SDSS “top-1%” arithmetic/labeling; implausible training-time reporting; inconsistent σ(fNL) baselines; score-scale inconsistencies; the new HEALPix dof problem; missing DESI injection–recovery; cross-match/dedup radii inappropriate across bands; Planck train/test leakage risk; inadequate random catalog for α; and absent proper-motion handling for NEOWISE cross-identifications. My confidence that the paper can ultimately pass external peer review is moderate: the data product is valuable and many issues are fixable, but the cosmology claims must be made rigorously consistent, the validation needs to be symmetric across surveys (especially DESI), and the cross-match/dedup methodology must be brought up to field standards before PRD publication.
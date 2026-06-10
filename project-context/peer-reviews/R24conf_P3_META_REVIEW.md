# P3 R24conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 405.7s

---

META-REFEREE REPORT (focus: blind‑spots none of the 5 referees caught)

P3-META-E1 — eROSITA “S > 0.259 (top 0.03%)” is numerically incompatible with the paper’s own S-definition
- Severity: ESSENTIAL
- Where: Sec. III.E (p. 8–9), Table I caption/row (p. 8), Table III (p. 9)
- Why others missed it: Prior reviews noted ambiguity/non‑independence of the eROSITA detector, but none checked that a z‑scored S threshold of 0.259 cannot correspond to a top 0.03% tail.
- Problem: The paper defines S as a standardized residual S = (MSE − μval)/σval. In that parameterization, the 99.97th percentile of a light‑tailed distribution would require S ≳ 3.4, not S > 0.259. Table III then lists the top 5 eROSITA anomalies with SBigAE between 0.439 and 1.084 — again far from an extreme tail. The text currently states: “Anomaly count: 298 at S > 0.259 (top 0.03%; data‑driven score‑knee threshold)”.
- Required fix: Clarify what axis the “0.259” actually refers to. If the production cut is on a raw IsolationForest score or on a re‑scaled, non‑z‑scored detector output, say so explicitly and do not denote it by S. If it is S in the sense of Eq. (2), provide the empirical S‑percentile for the scored sample and reconcile the 0.259 value with the “top 0.03%” statement (most likely the “0.03%” is wrong or the symbol S is misused). Update Table I, Table III labels, and all eROSITA threshold prose accordingly.

P3-META-M1 — HEALPix bookkeeping error in the sky-uniformity test; Nside=64 implies 49,152 pixels, not 38,330
- Severity: MAJOR
- Where: Sec. IV.B (p. 11)
- Why others missed it: Reviewers focused on the selection‑function caveat, not the hard pixel arithmetic.
- Problem: The text says: “A spatial uniformity test across 38,330 HEALPix pixels (Nside = 64) … χ2 = 143,936, dof = 38,329”. At Nside=64 the full‑sky Npix must be 12×Nside^2 = 49,152. Using 38,330 indicates an implicit mask/footprint selection, but this is never defined; yet the χ2 and dof are presented as if for an unambiguous pixel set.
- Required fix: State precisely how the 38,330 pixels were selected (union mask? populated pixels only? latitude cuts?), report the corresponding sky fraction, and make clear that the dof is for the masked subset. If the intention was full‑sky, redo the test on all 49,152 pixels (with mask weights) or remove the χ2 claim.

P3-META-M2 — “Mask injection-recovery” for NEOWISE is not a detection gate; it’s a tautology
- Severity: MAJOR
- Where: Sec. III.H (p. 9–10), Fig. 10 caption and Sec. VI.D(ii) (p. 16)
- Why others missed it: Others flagged gate PASS/FAIL in general; no one questioned the logical status of a mask “recovery.”
- Problem: The manuscript counts “NEOWISE ecliptic-pole mask: 1000/1000 = 100% (gate PASS)” as if it were an injection‑recovery of an anomaly detector. In fact, the “injection” consists of placing sources at |βecl| > {85°, 82°, 80.5°} and then “recovering” them by applying a fixed catalog mask |βecl| < 80°. Passing this test is guaranteed by construction and has no bearing on detector sensitivity or catalog reliability.
- Required fix: Reclassify the NEOWISE mask exercise as a sanity check of the masking geometry, not an injection‑recovery gate. Remove it from the “3 PASS” headline count in Fig. 10 and Sec. II.D(5), and present it separately as a QA check. The only valid detection‑gate results are those testing an anomaly detector’s response to planted signals under the catalog’s scoring rule.

P3-META-M3 — CMB patch pre-processing is underspecified; MSE scoring is not interpretable without it
- Severity: MAJOR
- Where: Sec. II.A (p. 2), Sec. III.F (p. 7), Table V footnote (p. 19)
- Why others missed it: Focus was on Planck denominators and rates, not on the signal processing chain.
- Problem: The Planck tier is ranked by “per‑patch reconstruction‑MSE” with scores in [0.558, 0.621], but there is no statement of patch preprocessing (e.g., units [K_CMB], map normalization, beam matching, DC offset/gradient removal, apodization). Without these, the MSE has no clear physical scale and is vulnerable to trivial offsets/gradients dominating the anomaly score.
- Required fix: Document the exact preprocessing steps applied to each 64×64 SMICA patch before training/scoring (unit conversion, mean/variance normalization, whether the patch mean was removed, any filtering/apodization). If no normalization was applied, justify why, and add a robustness test showing that the top‑ranked patches are not dominated by DC or large‑scale gradient differences.

P3-META-M4 — Geometric-mean bias estimator for Landy–Szalay is undocumented and potentially inappropriate
- Severity: MAJOR
- Where: Sec. V.a (p. 14)
- Why others missed it: They checked the propagated σ(fNL), not the estimator choice.
- Problem: The paper states: “Two estimators: central‑value geomean bgeo = 1.27 (αgeo = 0.27); jackknife geomean bjk = 1.19 ± 0.65 (αjk = 0.19 ± 0.65).” A geometric mean of bias ratios across θ‑bins (or regions) is non‑standard; no definition of the bins, weights, or rationale for using a geometric mean instead of an arithmetic/weighted fit is provided.
- Required fix: Define precisely how bgeo and bjk are computed (bins, weights, whether logs are averaged and why), and report the corresponding arithmetic‑mean (or fit‑based) estimator as a cross‑check. If the geometric mean was chosen to down‑weight outliers, say so and show that conclusions are unchanged with a conventional estimator.

P3-META-M5 — RA-only shifts for the DESI×SDSS random-overlap control are not geometry preserving
- Severity: MAJOR
- Where: Sec. IV.A (p. 10–11)
- Why others missed it: They focused on the lack of significance, not on the control construction.
- Problem: The “empirical RA‑shifted‑control expectation of 2.75 (mean of ±0.5°, ±1.0° shifts)” uses RA‑only offsets at fixed Dec. This does not preserve sky density or footprint geometry uniformly (e.g., near the poles and for surveys with complex tiling), and can bias the expected coincidence rate.
- Required fix: Recompute the control using 2D shifts/rotations (e.g., small great‑circle displacements with random position angles) or a spherical scramble that preserves the joint footprint, and report the sensitivity of the expected matches to the control construction. Alternatively, drop the numeric 2.75 and keep only the qualitative “positional coincidence alone carries no significance.”

P3-META-m1 — Conflict between “S refers without exception to standardized residual” and photometric score reporting (beyond Planck)
- Severity: MINOR
- Where: Sec. II.B (p. 3), Sec. III.E and Table III (p. 8–9)
- Why others missed it: They flagged Planck’s exception, but not the photometric side.
- Problem: The manuscript promises “S refers without exception to the per‑survey standardized residual,” yet in the photometric sections the reported thresholds/values (e.g., eROSITA “S > 0.259”, Table III’s SBigAE values ≈0.4–1.1 for top anomalies) are inconsistent with an extreme‑tail z‑score usage and appear to be on an ad‑hoc or mis‑scaled axis.
- Required fix: Either (i) actually standardize and report S for all catalogs (photometric and CMB) or (ii) amend the global statement and introduce distinct symbols (e.g., SBigAE, Sraw) plus a small table mapping each survey’s “anomaly axis” to its definition and typical percentiles.

P3-META-m2 — χ2 uniformity test implicitly treats pixel counts as independent with equal variance; neither assumption is stated
- Severity: MINOR
- Where: Sec. IV.B (p. 11)
- Why others missed it: They accepted the high‑level caveat but not the test mechanics.
- Problem: A χ2 test on counts per HEALPix pixel assumes (approximately) independent, Poisson‑like variates with known expectations. The text does not state what variance model was used, nor how covariance induced by the surveys’ tiling/selection was handled (beyond a general caveat).
- Required fix: Add one sentence: “We model counts as independent Poisson deviates with expectation proportional to the joint selection function; in this illustrative test we approximate that by a uniform expectation over the masked pixel set.” If that is not the case, describe what was done or remove the χ2 statistic in favor of the already‑present qualitative caveat.

P3-META-n1 — Minor reproducibility nit: PTA ESS figure is internally inconsistent with the quoted τ unless clarified
- Severity: NIT
- Where: Appendix E (p. 19)
- Why others missed it: They focused on prior sensitivity, not sampler diagnostics.
- Problem: With 32 walkers × 10,000 production steps and τ ≈ 58, a naive ESS estimate would be ≈ (32×10,000)/(2×58) ≈ 2,760. The text reports ESS ≈ 5,500 without stating whether τ is per‑parameter, post‑thinning, or aggregated differently.
- Required fix: State how ESS was computed (per‑parameter median τ, chain‑concatenation convention, or the library’s exact definition) so the 5,500 figure can be reconciled with τ ≈ 58.

## Meta-review recommendation
MAJOR REVISIONS

The new issues above include (i) a hard numerical inconsistency in eROSITA’s S/percentile mapping, (ii) an Nside/pixel‑count mismatch in the sky‑uniformity test (and missing variance assumptions), (iii) a misframed “mask injection‑recovery” presented as a gate PASS, (iv) missing CMB patch preprocessing needed to interpret MSE‑based rankings, (v) an undocumented/non‑standard bias estimator used in the Landy–Szalay analysis, and (vi) a non‑geometry‑preserving random‑overlap control. All are fixable with clarifications and modest recomputations but are material to PRD‑level methodological clarity.

Given the union of all six reviews, the paper now has multiple ESSENTIAL items (incorrect Fisher F0, de‑bias arithmetic, mixed matching radii, Planck denominator/rate, eROSITA S/percentile, data/code availability) and more than a dozen MAJOR clarifications/corrections. My assessment is that these are addressable in one revision cycle if the author prioritizes (a) correcting the few hard math/denominator errors, (b) cleaning up symbol/axis consistency, (c) tightening the cosmology presentation to avoid overstated central values, and (d) scrubbing internal‑audit residue. Confidence the paper would survive external (non–bigbounce) PRD review after these fixes: moderate to high, provided the eROSITA and Planck clarifications and the Fisher mapping corrections are implemented cleanly and the abstract is de‑promoted to reflect the de‑biased null on σ(fNL).
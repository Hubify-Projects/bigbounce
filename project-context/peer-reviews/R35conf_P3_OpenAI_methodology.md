# P3 R35conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.99.pdf` md5=1e97ec59 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6593 chars)
**Wall time**: 356.1s

---

Referee report (Physical Review D, Methods-focused)

I read the full manuscript carefully, including all figures, tables, equations, appendices, and captions. Below I itemize issues by severity. Each item lists an ID, page/section, the specific problem (with quotes when possible), and the required fix.

ESSENTIAL

P3-E1 — Abstract (p.1) and throughout: internal revision/provenance language and “earlier draft” text in body
- Problem: Multiple instances of version-history and internal-bookkeeping prose appear in the main text, e.g. “an earlier draft quoted 264,938/264,738...” (p.1), “an earlier draft quoted 38,330 pixels with χ2
ν = 3.76...” (p.14), “an earlier draft listed 10.6 s, which is inconsistent... and has been withdrawn” (Table VI footnote, p.23).
- Required fix: Remove all earlier-draft/version-history/provenance narrative from the main text. Replace with the current, final numbers only, and if needed explain methodology changes succinctly without referring to prior drafts. PRD does not allow internal revision log text in the published article.

P3-E2 — Data availability (p.22): placeholder DOI text
- Problem: “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
- Required fix: Replace with the actual DOI(s). Provide finalized, immutable repository links and checksums for the released datasets, code, and MCMC chains. PRD requires stable archival identifiers upon publication.

P3-E3 — eROSITA score axis irreproducibility vs. usage consistency (pp.10–11, Table I caption, §III E, Table IV)
- Problem: The text states the eROSITA SBigAE score axis is irreproducible and the tier is released as a membership list only; yet elsewhere the paper uses values/thresholds (e.g., “production-run score-knee threshold 0.259”) that cannot be reproduced from committed artifacts.
- Required fix: Purge all uses of the irreproducible score axis from the main paper (threshold values, labels, or implications). State explicitly and uniformly that the released eROSITA component is a membership list only ranked by the committed raw-score artifact; provide the exact, reproducible ranking variable and its definition in the Methods. Ensure every place that references “SBigAE” for eROSITA is removed or clearly labeled as non-reproducible and not used for any quantitative result. Confirm no analysis in the manuscript (counts, overlaps, rates) depends on the irreproducible axis.

P3-E4 — Threshold heterogeneity and estimator declaration (pp.4–7, Table I)
- Problem: The manuscript uses different anomaly-selection thresholds across surveys (absolute S>5 for DESI; percentile cuts for Gaia/NEOWISE/Planck; a fixed-size continuity slice for SDSS; an unrecoverable score-knee for eROSITA). While some caveats are stated, the primary estimator and decision rules are not pre-declared in a uniform, survey-agnostic way.
- Required fix: Explicitly declare the primary anomaly estimator and survey-specific selection rule in a single, consolidated Methods subsection, listing for each survey the exact, reproducible rule (including the definition of S with µval, σval; the exact percentile or fixed-count; and any mask). State clearly which surveys contribute data-driven rates vs predetermined counts. Ensure the Abstract and Conclusions only quote rates grounded in data-driven thresholds and avoid mixing fixed-count tiers with measured frequencies without an explicit qualifier.

P3-E5 — Catalog “unique objects” deduplication and cross-survey association at fixed 5″ (pp.13–16)
- Problem: A uniform 5″ radius is used across surveys with heterogeneous astrometry/PSFs (Gaia <<1″; NEOWISE ~6″). The manuscript acknowledges this and shows a {3″,5″,7″} sensitivity sweep; however, the main “unique objects” headline still relies on a one-size 5″ rule.
- Required fix: Either (a) implement and report a probabilistic cross-match (e.g., Budavári–Szalay) using per-survey positional uncertainties (and for Gaia, proper-motion epoch propagation) as the primary deduplication, or (b) clearly re-label the “unique objects” count as “5″-deduplicated associations” and move the “unique objects” phrasing to the supplement, while committing to a probabilistic cross-match in a subsequent revision. If (a) is impractical for this submission, adopt survey-pair-dependent radii reflecting PSF/astrometric errors and provide a sensitivity study; update the headline count accordingly.

P3-E6 — Use of training/validation leakage in tabular scalers (pp.3–4, §II.B.a, Gaia/eROSITA/NEOWISE)
- Problem: The normalization constants for eROSITA and NEOWISE are fit on the full sample (not training split), introducing validation/tail information into the scaler. The paper quantifies an effect for eROSITA but states NEOWISE and Gaia checks are “queued.”
- Required fix: For every tabular survey used in any headline statistic (counts, overlaps, map-level summaries), re-run the scaler fit on the training split only, retrain, and report top-1% Jaccard overlaps and tail churn analogously to the eROSITA audit. If this cannot be completed now, label the affected tiers as exploratory and remove them from any headline totals or claims (including the 378,280 headline) until the train-only scaler audit is done.

P3-E7 — Abstract claims vs. body backing (pattern-045 drift sweep)
- Problem: The Abstract carries several strong, high-level quantitative claims (e.g., 378,280 unique anomalies; 269,317 catalog-grade subset; 17.8% novelty; 21.5×/6500× reductions; σ(fNL) envelope) that are justified in the body but require exact cross-references and consistent wording.
- Required fix: For each abstract sentence containing a number, add an in-text parenthetical or ensure an unambiguous pointer in the body text (section/table/figure). Verify the “catalog-grade subset” number is consistently defined (with/without Planck patches) in the Abstract and Conclusions (269,317 including Planck; 269,117 without); use the same phrasing and numbers in both locations.

P3-E8 — Sigma/null-procedure comparability (mixing σ from different constructs)
- Problem: σ(fNL) forecast (Fisher-based, parameter-uncertainty) and NANOGrav γ posterior shifts are presented near each other in the Conclusions. While caveats are stated in their sections, the Conclusions list both without explicit “not directly comparable” language.
- Required fix: Where σ(fNL) Fisher forecasts and PTA spectral-index sigma-shifts appear in the same paragraph, explicitly state that these σ’s arise from different statistical quantities and are not directly comparable.

P3-E9 — Planck autoencoder training-time footnote referencing inconsistent prior number (Table VI, p.23)
- Problem: “... the total training wall-clock for this run was not preserved ... an earlier draft listed 10.6 s, which is inconsistent ... and has been withdrawn.”
- Required fix: Remove the earlier-draft reference; simply state that the wall-clock time was not recorded and is not essential to any inference. If training time is relevant, rerun and report it.

MAJOR

P3-M1 — Reliance on fixed-count tiers in headline totals (Table I, pp.7–8)
- Problem: Planck, Gaia, and NEOWISE entries represent predetermined 1% selections; eROSITA is a fixed top-298. These are mixed into overall headline “unique anomalies” and “rate” statements, despite not being data-driven frequencies.
- Required fix: In all places where totals or “rates” are reported, add explicit qualifiers that these totals include fixed-count tiers and do not represent measured anomaly frequencies. Consider presenting (i) a “data-driven-rate-only” subtotal (DESI, SDSS-native thresholds that are data-driven), and (ii) a “fixed-count-tier subtotal,” before giving the combined “catalog-size” total.

P3-M2 — Gaia tier stability and inclusion in headline counts (Table I footnote ⋆, §VI.D.ii)
- Problem: The Gaia DR3 tier has 41% cross-validation stability and fails the 5σ injection-recovery gate; however, it contributes to the aggregate headline unique-object total.
- Required fix: Either exclude Gaia from any headline totals and present it as an exploratory tier (clearly outside catalog-grade) or complete additional validation (train-only scaler audit, robust XV-stability on multiple random seeds) to justify inclusion.

P3-M3 — eROSITA injection-recovery FAIL (1.2% at 5σ) yet used in headline counts
- Problem: eROSITA fails the sensitivity gate (even with strong XV-stability). It is still part of the headline 378,280 total.
- Required fix: As with Gaia, either (a) remove it from the “catalog-grade” headline and keep it as an exploratory membership list (with a separate subtotal), or (b) provide a compensating validation (e.g., an independent detector not sharing BigAE latent, such as an IF or VAE trained on raw features, with held-out performance) to justify inclusion.

P3-M4 — “Largest” and “∼141×” claims (Abstract, p.1; Conclusions, p.21)
- Problem: The “largest-scale” and “∼141× the largest prior single-survey anomaly catalog” claims are anchored to Liang et al. (single-survey DESI EDR, 2,685 anomalies) while this work aggregates seven archives. The paper contains caveats elsewhere; the Abstract is more absolute.
- Required fix: In Abstract and Conclusions, add “to our knowledge” and qualify explicitly that the comparison is to a single-survey catalog (Liang et al.), while the present work aggregates multiple surveys and includes fixed-count tiers. Avoid implying a like-for-like comparison.

P3-M5 — Landy–Szalay bias-ratio method reporting (Section V)
- Problem: The bias-ratio estimator αjk is reported with 30-region jackknife and randoms (26,920). However, details enabling reproduction are sparse (bin edges, mask, footprint weights, exact random generation procedure, angular selection_mask).
- Required fix: Provide in Methods: angular binning details, random generation procedure (matching sky selection function and footprints), mask definition, estimator normalization, and the exact catalog used (number per redshift bin, cuts). Include a figure or a table with w(θ) measurements and errors for both samples.

P3-M6 — Spatial χ2 test (p.14)
- Problem: A χ2
ν = 15.7 uniformity test is reported against a model that assumes “uniform per-occupied-pixel mean with Poisson variance.” This is not a meaningful null for a combined footprint without selection-function modeling, and the significant χ2 is then caveated.
- Required fix: Either remove the χ2 statistic from the main text or move it to an appendix labeled as a toy statistic, emphasizing it is not interpretable without per-survey completeness maps. Retain only the (more interpretable) latitude/dust correlation nulls in the main body.

P3-M7 — NEOWISE injection-recovery gate (pp.12, 21)
- Problem: The NEOWISE “mask geometry” injection-recovery passes by construction, yet is counted among the PASS gates in some summaries.
- Required fix: In every summary that tallies “gates PASS,” segregate geometry-QA passes from sensitivity tests or annotate explicitly “NEOWISE: geometry-QA only, not a detector sensitivity gate.”

P3-M8 — Footnote symbols and manuscript style (Table I and elsewhere)
- Problem: Nonstandard footnote symbols (♡, ♠, ♢, ⋆, #, ¶, ∥) are used extensively in a dense table caption; PRD style typically uses numeric or alphabetic markers and shorter captions.
- Required fix: Convert to standard footnote markers and condense the caption. Move long methodological notes to Methods or an appendix.

P3-M9 — ACT DR6 quarantined block retained in multiple places (Appendix F; mentions in Table I caption and §IV.D)
- Problem: The ACT cross-transfer block is not a science result and fails both gates. Yet, multiple references in the main text revisit it.
- Required fix: Retain a single, short pointer to Appendix F explaining quarantine; remove repeated references in the main text, to avoid reader confusion.

MINOR

P3-m1 — Abstract: novelty fraction phrasing (p.1)
- Problem: “yields a genuine novelty fraction of 178/1,000 ≈ 17.8% ... (a single-sample point estimate on the DESI top-1,000 score stratum...)”
- Required fix: Add “This estimate is specific to the DESI top-1,000 anomaly stratum; no survey-wide or catalog-wide novelty rate is claimed.”

P3-m2 — False-match rates (p.13)
- Problem: The SIMBAD false-match estimate assumes global uniform density.
- Required fix: Provide a brief appendix figure/table showing the HEALPix map of local SIMBAD densities and the corresponding expected false-match probability as a function of sky position for completeness (or label the value as a global-mean back-of-envelope).

P3-m3 — Equation (E1) units/normalization (Appendix E)
- Problem: The derived form is dimensionally consistent but the normalization choice (e.g., log10(12π^2)) is presented without a short derivation or reference for readers less familiar with the ceffyl free-spectrum normalization.
- Required fix: Add one sentence with a reference to the exact free-spectrum normalization convention used (e.g., to NANOGrav methods supplement) so readers can cross-check factors of Tobs and fyr.

P3-m4 — Figure axis labels and units
- Problem: Several figures use generic “Probability density” without axis units; Fig. 5 uses degrees but not explicitly labeled units; Fig. 7 scatter (score vs. Galactic distance) does not state that distance is absolute latitude |b| in degrees.
- Required fix: Add units to all axes (e.g., “Probability density (normalized)”, “Angular distance from Galactic plane |b| (deg)”, “Wavelength (Å)”). Verify every axis has units where applicable.

P3-m5 — Consistent use of primes and arcsecond symbols
- Problem: Mixed notation (′, ″, arcsec); in some places “5′′” appears with inconsistent kerning.
- Required fix: Normalize to ″ for arcseconds throughout.

P3-m6 — Minor typos/grammar
- Problem: A few hyphenation and spacing issues (e.g., “over -represents” in §III F; “per-occupied-pixel” extra hyphen).
- Required fix: Proofread and correct minor typography.

NIT

P3-N1 — Long captions in Table I and Table VI
- Problem: Captions are essay-length and hinder readability.
- Required fix: Move explanatory material to text or appendix; keep captions concise.

P3-N2 — Overuse of in-text file-path “artifact” pointers
- Problem: Numerous internal repository paths interrupt the narrative.
- Required fix: Consolidate pointers into a Reproducibility appendix listing artifacts and checksums; reference that appendix from the text instead of embedding paths inline.

P3-N3 — “to which we are aware” phrasing
- Problem: “of which we are aware” appears; standard phrasing is “to our knowledge.”
- Required fix: Adopt standard phrasing.

Arithmetic and internal consistency spot-checks (selected)

- Headline sums: 195,829 (DESI) + 77,905 (SDSS native continuity slice) + 113,342 (LAMOST native top-1%) + 298 (eROSITA) + 200 (Planck native) + 500 (Gaia) + 419 (NEOWISE) = 388,493; dedup 10,213 → 378,280 unique. Compression 10,213/388,493 ≈ 2.629%. Consistent.
- “Catalog-grade subset” counts: 269,317 including Planck patches; subtract 200 Planck → 269,117 point-source. Consistent across text; ensure both Abstract and Conclusions use exactly the same numbers/phrasing.
- DESI science-class like-for-like: 2,468 / 2,685 ≈ 0.919 → “≈0.9×” correct. Rate vs 20,299,155 ≈ 0.0122% matches Table II.
- SDSS cross-transfer vs native S>5: 77,905 / 12 ≈ 6,492 → “~6500×” correct.
- LAMOST cross-transfer vs native S>5: 44,075 / 2,054 ≈ 21.46 → “21.5×” correct.
- Novelty fraction: 178/1000 = 17.8%. Binomial SE ≈ 1.21% → “Wilson 68% ±1.2%” consistent.
- NEOWISE pole contamination: 17/436 ≈ 3.90%; quoted uniform sphere benchmark 1.52%; ratio ≈ 2.57 → “2.6×” consistent.
- Fisher σ(fNL): Using F0 = 1/8.98^2 and c=0.0747, α=0.19 gives σ ≈ 8.14; envelope [3.92, 8.98] consistent.
- NANOGrav γ: ΔγMB = (3.0 − 2.567)/0.382 = 1.13σ; ΔγSMBHB = (4.33 − 2.567)/0.382 = 4.61σ. Consistent.

Length and scope

The paper is very long (28 pages) for the core methodological contribution. Many details (file-path artifacts, version history, long captions) can move to a Reproducibility appendix or the data repository/Supplemental Material. A streamlined main text of ~20–22 pages would be appropriate while preserving essential technical detail.

## Summary recommendation
MAJOR REVISIONS

The manuscript is ambitious and contains a large amount of careful self-audit. However, it does not yet meet PRD standards for methodological rigor and presentation. Essential fixes are needed: remove revision-history text in the body, supply final DOIs, present a clean and uniform declaration of estimators/thresholds, resolve the eROSITA irreproducibility (or confine it strictly to a membership list not used in headline counts), address fixed-count tiers’ inclusion in totals, and either adopt a probabilistic cross-match for “unique objects” or clearly downgrade that label. Additional major issues include stability of Gaia/eROSITA tiers, better reporting for the bias-ratio estimator, and clarifying sigma comparability in the Conclusions. With these revisions and some condensation of nonessential narrative, the paper could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second pass)

ESSENTIAL

P3-E10 — Incorrect de-biasing arithmetic in σ(fNL) discussion (Section V; “de-biased amplitude” line)
- Problem: The text states “max(0, α̂^2 − σ^2_α) = max(0, 0.192 − 0.652) = 0.” This plugs α̂ = 0.19 and σα = 0.65 directly instead of their squares. Correct values are α̂^2 = 0.0361 and σ^2_α = 0.4225. The qualitative conclusion (zero after max) holds, but the numbers shown are wrong.
- Required fix: Replace “0.192 − 0.652” with “0.036 − 0.423” (or exact values). State explicitly that the max is zero because α̂^2 < σ^2_α.

P3-E11 — S-definition confusion for SDSS/LAMOST in Table I caption vs native rescoring (§III C, §III D, Table I caption)
- Problem: The caption says SDSS and LAMOST “share the DESI-trained BigAE score scale,” while the body treats SDSS/LAMOST native rescoring with their own µval, σval and native thresholds (e.g., S ≥ 0.1060; S ≥ 0.4613). This is ambiguous about which validation pool defines S at each occurrence.
- Required fix: Clarify per occurrence whether S is computed from (i) the DESI-trained cross-transfer checkpoint with DESI’s µval, σval applied to another survey, or (ii) a survey-native retrain with that survey’s own µval, σval. Provide µval and σval for every native retrain used anywhere S is quoted.

P3-E12 — Canonical-S reproducibility parameters missing (global; §II.B.b, Data release)
- Problem: Recomputing S requires µval and σval for each survey’s native retrain (and seed/checkpoint identifiers). Only DESI’s µval is shown; others are absent.
- Required fix: Publish µval and σval (and random seeds/checkpoint IDs) for all native retrains in the data release/Methods so third parties can reproduce canonical-S.

P3-E13 — Gaia preprocessing provenance gap (Section II.B.a; Data release)
- Problem: The exact 20-feature Gaia production preprocessing script was “not recovered,” and the paper uses a lineage-inferred recipe. This prevents exact reproduction.
- Required fix: Recover and archive the exact production preprocessing code or explicitly mark the Gaia tier irreproducible, remove it from headline totals, and confine it to exploratory status pending a reproducible rerun.

MAJOR

P3-M10 — Heuristic, modality-misaligned gate thresholds (Section II.D Steps 1 and 5; §VI.D(ii))
- Problem: The single val-loss gate “≤ 0.30” is applied across disparate modalities/scales (spectra vs CMB patches pre-standardized per patch), and injection gates are heuristic. This mixes incommensurate MSE scales and ad hoc thresholds.
- Required fix: Either (a) define modality-normalized gates (e.g., use S on validation or percentile ranks) with a brief power/sensitivity rationale, or (b) clearly label current gates as heuristic QA checks and avoid PASS/FAIL language in headlines; move formal performance claims to metrics that are comparable across modalities.

P3-M11 — Planck top-200 not held-out; single split only (Section III.F; Table VI footnote)
- Problem: The released Planck top-200 is scored on a bank that includes training patches; only one deterministic 85/15 split is examined (152/48 train/val in the top-200).
- Required fix: Report stability of the top-200 under multiple independent train/validation splits and/or publish a held-out top-200 selection (scored from a model that did not train on those patches). Provide a top-N overlap curve across ≥5 random splits.

P3-M12 — Coordinate-frame claim without quantification (Section IV.D; §III.F)
- Problem: The text says Planck anomalies “concentrate at the south ecliptic pole” while selection/training is in Galactic coordinates (|b| ≥ 20°). The ecliptic pattern is asserted but not shown/quantified.
- Required fix: Add a small figure or table showing the ecliptic-latitude distribution of Planck anomalies (and a uniform-sky baseline), or soften the claim to a qualitative observation with an explicit “not quantified” qualifier.

P3-M13 — DESI science-class recount reproducibility details missing (Section III.A; Table II)
- Problem: The 20,299,155-row “main-survey primary-bit” denominator and the 2,468/1″ match depend on exact targeting bitmasks/logic.
- Required fix: Specify the exact bit names/values and logic used to define “primary science-class” rows (code snippet or table), so others can reproduce the 2,468 matches and the 0.012% rate.

P3-M14 — Non-portability of S > 5 across domains presented without a formal analysis (§II.B.c)
- Problem: “Applying S > 5 to a random uncurated SPARCL sweep flags >50% of spectra” is reported but not analyzed; it underscores that S is dataset-anchored.
- Required fix: Either provide a short analysis of S-transport across catalog curation (e.g., show how µval, σval shift on uncurated vs curated sets and the implied threshold migration), or remove the “>50%” statement and confine the warning to a qualitative caution about domain dependence.

MINOR

P3-m7 — Fig. 5 cutout size arithmetic mismatch (Section III.H; Fig. 5 caption)
- Problem: Caption says “256 × 256 pixels (108″ × 108″).” At 0.262″/px (LS DR9), 256 px corresponds to ~67.1″, not 108″.
- Required fix: Correct the angular size or the pixel dimensions; ensure all gallery captions use consistent pixel scales.

P3-m8 — Inconsistent numeric precision for σ(fNL) baseline (Section V; Appendix C/Figure 11 caption)
- Problem: The baseline appears as 8.98 in some places and 8.982 in others (used inside F0 = 1/8.982). The tiny difference is harmless numerically but distracts.
- Required fix: Adopt a single baseline value/precision (e.g., 8.98) throughout, and recompute F0 accordingly for consistency.

P3-m9 — SDSS/LAMOST S ranges not tied to their native µval, σval in text (Sections III.C, III.D)
- Problem: Native S thresholds (0.1060, 0.4613) are reported without the corresponding µval, σval for context.
- Required fix: Add the native (µval, σval) for SDSS and LAMOST (as done for DESI) in Methods or a small table.

P3-m10 — Caption/body duplication of Planck “concentration” language without units/frame tags (Sections III.F, IV.D; Fig. 2)
- Problem: The map/caption use equatorial coordinates while the text describes ecliptic-plane features; frames are mixed without explicit labels.
- Required fix: State the frame in each sentence/caption and, where referring to ecliptic features, present or reference an ecliptic-frame map.

NO repeats of previously listed issues. These are additional to the first review and focus on hard arithmetic, caption-to-body coherence, reproducibility parameters for S, gating comparability across modalities, and small but consequential inconsistencies (e.g., Fig. 5 size).
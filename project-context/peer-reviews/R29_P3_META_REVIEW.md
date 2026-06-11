# P3 R29 — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 704.0s

---

Meta-referee report (PRD) — blind-spot audit

I read the rendered PDF and all five prior referee reports. Below I list issues that, to the best of my check, none of the five reviewers flagged. Each item includes the location, why it may have been missed, the specific problem (with quotes), and the required fix.

P3-META-E1 — “Genuine novelty” measurement is vulnerable to multiple-testing false matches and sky-coverage heterogeneity
- Severity: ESSENTIAL
- Section + page: §IV.A “Archival cross-match and genuine novelty fraction,” p. 11–12; Abstract p. 1; Conclusions item 2 p. 19
- Why missed: All reviewers focused on SIMBAD-vs-archival distinctions and the Wilson CI, but not on the family-wise error rate and coverage bias when matching against many heterogeneous catalogs at once.
- Problem: The 82.2% “archival-ID rate” (hence 17.8% “genuine novelty”) is computed by querying “20 curated all-sky catalogs via CDS X-Match (Gaia DR3, SDSS, DESI Legacy Imaging, DES DR2, Pan-STARRS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, …)”. Many of these are not actually all-sky (e.g., Pan-STARRS1, SDSS, DES, GALEX, NVSS, VLASS, Chandra, 4XMM). The analysis counts “≥1 match in any” as an identification but does not control the family-wise false-match rate across K catalogs or restrict to the common footprint. With K≈20 independent (and often dense) layers, the probability of at least one spurious association can be orders of magnitude larger than the single-catalog per-source rate; heterogenous sky coverage further biases the absence/presence mixture.
- Required fix: (a) Restrict the novelty estimate to catalogs with near-uniform full-sky coverage (e.g., Gaia, WISE/AllWISE/CatWISE, 2MASS, Legacy Imaging) or compute it within the intersection of footprints; (b) report the matching radius used for the CDS X-Match and per-catalog source densities; (c) provide a family-wise false-match bound (e.g., Šidák/Bonferroni using local densities or a Monte Carlo scrambled control); (d) recompute the 82.2%/17.8% with these controls, or clearly relabel the current figure as an upper bound on the archival-ID rate (hence a lower bound on novelty), not a point estimate.

P3-META-M2 — No tri-survey coincidences is implausible; the dedup analysis likely undercounts multi-survey clusters
- Severity: MAJOR
- Section + page: §IV.C “Cross-Survey Matches,” p. 13
- Why missed: Reviewers checked dedup arithmetic but not the plausibility of “none spans three or more surveys.”
- Problem: The manuscript states “exactly 637 of the 9,553 clusters span two surveys (none spans three or more).” Given seven inputs (DESI, SDSS, LAMOST, eROSITA, Gaia, NEOWISE, Planck) and known high-density, all-sky catalogs (Gaia, NEOWISE), it is surprising that no cluster has members from ≥3 surveys (e.g., a DESI×Gaia×NEOWISE or SDSS×Gaia×NEOWISE coincidence within 5″). This suggests either an overly strict per-survey filtering before dedup, a bug in how survey tags are aggregated within union-find components, or an under-match for the wide-PSF NEOWISE tier.
- Required fix: Provide a reproducible audit listing all clusters with ≥3 distinct survey tags, or else document why zero tri-survey clusters are expected after your per-tier cuts. As a robustness check, rerun dedup at 7″ with NEOWISE included and report the count of ≥3-survey clusters. If still zero, supply a code snippet and component membership examples to demonstrate correct survey-tag aggregation.

P3-META-M3 — High‑z QSO selection uses an arm‑dominance criterion without per‑arm normalization, risking systematic bias
- Severity: MAJOR
- Section + page: §III.B “High‑z QSO Candidates,” p. 6; §II.B per‑arm residuals, p. 4
- Why missed: Prior reviews addressed the “Candidates” rewording and confirmation status but not the statistical validity of the rZ > rB and rZ > rR test itself.
- Problem: Candidates are selected by “Z-arm dominated anomaly scores, meaning rZ > rB and rZ > rR.” The paper explicitly says “the per-arm sub-scores are computed on the common normalized input scale and are not independently z‑scored per arm,” i.e., arm-to-arm σ differences are not normalized out. DESI’s arms have different throughput/SNR and potentially different residual scales after the global normalization. Using raw mean-absolute residuals per arm (even averaged over NX) without per-arm variance normalization can misclassify arm dominance for reasons unrelated to astrophysics (instrumental noise and calibration differences between B/R/Z).
- Required fix: Re-define arm-dominance using per-arm standardized residuals (subtract per-arm mean and divide by per-arm std computed on the native survey’s validation pool), or show that the rZ/rB and rZ/rR ratios are robust across SNR strata. At minimum, recompute the 12 high‑z “rZ‑dominant” candidates under a per-arm normalized test and report any changes.

P3-META-M4 — Injection–recovery for Planck is not tied to the published threshold; 100% at 5σ is not an operating‑point sensitivity
- Severity: MAJOR
- Section + page: §III.F “Planck CMB,” p. 9–10; Fig. 10 caption p. 20
- Why missed: Others flagged the NEOWISE geometry “PASS,” but not that the Planck 100% result is disconnected from the catalog’s selection operating point.
- Problem: The Planck tier is published as the top‑200 ranked patches; the injection–recovery test reports “500/500 = 100% at 5σ Gaussian‑bump amplitude.” Because patches are standardized (mean 0, std 1) before inference and no post‑plant re‑standardization is done, a 5σ bump is extremely strong but its relation to the catalog threshold (the per-patch MSE defining the top‑200) is not quantified. As stated, 100% at 5σ does not tell the reader what the detection efficiency is near the actual decision boundary (e.g., 50% recovery at threshold).
- Required fix: Report the detection efficiency curve as a function of amplitude with the recovery criterion set to “enters the published top‑200” (or top‑1% if you switch to a fixed percentile). Quote the amplitude at which 50% (and 90%) of injected patches cross the threshold. Without anchoring to the catalog’s operating point, 100% at 5σ is not a meaningful sensitivity claim.

P3-META-M5 — B‑dominant DESI anomalies are flagged as calibration‑suspect but are still included in headline counts and maps
- Severity: MAJOR
- Section + page: §III.A DESI DR1 (B‑dominant anomalies), p. 5; §VI.C Limitations (item 3), p. 17; Fig. 7 map p. 14
- Why missed: Reviewers noted limitations generally but not the inconsistency between the caution and continued use in global summaries.
- Problem: ~44,000 DESI B‑dominant anomalies (22.7%) are explicitly “flagged as calibration‑suspect; confirmation via photometric color selection is needed.” Yet these objects remain in the 195,829 DESI count and in the sky maps and cross‑survey dedup underlying headline totals. If a large (and spatially structured) calibration-suspect subset is included, spatial tests and overlap statistics may be biased.
- Required fix: Publish two DESI (and combined) catalog variants: (a) full, and (b) “DESI-clean” with B‑dominant anomalies removed or down‑weighted. Recompute the DESI sky map, the spatial χ^2 diagnostic, and the 7‑way dedup compression on the DESI‑clean set; report the differences. For fairness, use the “clean” tier for any downstream quantitative statements about distribution and cross‑survey coincidences.

P3-META-m6 — The “20 curated all‑sky catalogs” phrasing is inaccurate
- Severity: MINOR
- Section + page: §IV.A (list of catalogs), p. 11–12
- Why missed: Most attention was on reproducibility; this is a wording/accuracy point.
- Problem: The paper calls the 20‐catalog set “curated all‑sky catalogs.” Several named surveys are not all‑sky (e.g., Pan‑STARRS1, SDSS, DES, GALEX, NVSS, VLASS, Chandra, 4XMM).
- Required fix: Change to “curated set of major sky surveys” and, if retained in the methods, add a one‑line note that footprint heterogeneity was accounted for as per P3‑META‑E1 (or explicitly state it was not, and that this biases the point estimate).

P3-META-m7 — The CDS X‑Match radius used for the 20‑catalog novelty estimate is not specified
- Severity: MINOR
- Section + page: §IV.A “Archival cross‑match,” p. 11–12
- Why missed: Others checked SIMBAD 5″ and pooled 3″ but not the CDS multi‑catalog runs.
- Problem: The SIMBAD runs are explicit (5″; pooled 3″ case noted). The CDS 20‑catalog run omits the matching radius. CDS defaults and per‑catalog optimals differ; the novelty estimate cannot be reproduced without this.
- Required fix: Specify the CDS X‑Match cone radius used (and whether it was uniform across catalogs); if different radii were used per catalog, list them succinctly.

P3-META-m8 — Per‑arm residual definition may conflate arm length differences if downsampled NX are unequal
- Severity: MINOR
- Section + page: §II.B per‑arm residuals, p. 4
- Why missed: Reviewers focused on normalization, not NX.
- Problem: rX is defined as mean absolute residual over arm X, rX = (1/NX) Σ|xi − x̂i|. If NX differs across B/R/Z after downsampling, then “mean” compensates for length, but noise/error aggregation scales with √NX; depending on the continuum normalization, comparability might still be imperfect.
- Required fix: State the actual NX per arm after downsampling and confirm they are identical; if not, add a short justification that “mean absolute residual” remains appropriate (or use an arm‑level z‑normalization before comparing rZ vs rB,rR).

P3-META-m9 — Landy–Szalay bias measurement lacks an explicit mask/footprint treatment
- Severity: MINOR
- Section + page: §V “Empirical bias measurement,” p. 15
- Why missed: Reviewers queried selection definition but not mask handling.
- Problem: The Landy–Szalay analysis uses 26,920 randoms and 30 jackknife regions but does not describe how the DESI mask/footprint and any vetoes were applied to randoms. Without this, αjk may be biased by selection inhomogeneity.
- Required fix: Add a sentence describing the footprint/mask used for randoms and the jackknife tiling. If a simple RA/Dec box was used, state it and caution that αjk is a first‑pass estimate subject to mask refinement.

P3-META-N10 — “Canonical‑S top‑298” phrasing for eROSITA conflicts with the earlier admission that SBigAE is irreproducible
- Severity: NIT
- Section + page: Table I footnote §, p. 9–10 (“Empirical intersection … 284 of 298 canonical‑S top‑298 are also in the IsolationForest top‑9,303”)
- Why missed: Reviewers hit the broader eROSITA axis problem but not this stray wording.
- Problem: Calling the 298 “canonical‑S top‑298” contradicts §III.E where SBigAE is declared irreproducible and “not a science data product.”
- Required fix: Replace “canonical‑S top‑298” with “published 298‑member membership list” throughout; ensure no other stray “canonical‑S” phrasing remains for eROSITA.

Meta-review recommendation
MAJOR REVISIONS

Considering all six reviews together, there are multiple essential/major blockers: (i) reproducibility and dimensional errors (others), (ii) Planck denominator inconsistency (others), (iii) irreproducible eROSITA axis (others), plus (iv) the novelty‑fraction methodology issues (this report), (v) the absence of any ≥3‑survey matches plausibility gap (this report), (vi) the arm‑dominance normalization flaw in high‑z selection (this report), and (vii) injection‑recovery not anchored to the Planck operating threshold (this report). I count at least 10 essential/major items across the union of reports that must be addressed. My confidence that, after a thorough rewrite addressing these points (including a cleaned novelty estimate and dedup audit), the paper would survive an external PRD review is moderate: the core catalog contribution is strong, but publication will require tightened methodology, consistent accounting, and removal or repair of all non‑reproducible axes.
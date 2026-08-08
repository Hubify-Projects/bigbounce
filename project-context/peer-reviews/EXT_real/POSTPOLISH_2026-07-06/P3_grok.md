# EXT POSTPOLISH 2026-07-06 — P3 — Grok

- **Provider:** Grok, BigBounce - Papers project
- **Model/effort:** Expert
- **Chat URL:** https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=506941ea-10ac-488c-b5f8-14ef2b802ab5
- **PDF:** P3_v3.1.140.pdf (md5 55459a5f46ec48754a74db448f1e7657)
- **Harvested:** 2026-07-07
- **Thought for:** 1m
- **Parsed verdict (from response):** MAJOR REVISIONS

## Raw verbatim response

VERDICT: MAJOR REVISIONS
ISSUES:

[MAJOR] Abstract, §I, and §III E: The eROSITA DR1 tier (n=298 membership list at production threshold 0.259) and its per-object S_BigAE scores cannot be reproduced from any committed artifact; 16 monotone rescalings of the raw reconstruction score plus IsolationForest retrains all fail to recover the threshold or preserve monotonicity (Spearman ρ ≈ −0.10 on top ranks), indicating an undocumented post-hoc rescaling step. Although a raw-score top-298 recipe is now supplied, the published scores and original selection axis lack provenance, violating reproducibility standards for a catalog data product; the tier also fails the 5σ injection-recovery gate (1.2 % recovery) and is retained only as an exploratory addendum.

[MAJOR] Abstract, §I, §III A, and Table II: The primary deliverable is presented as a "validated catalog-grade subset of 268,519 unique anomalies" whose "validation establishes that the 268,519 subset is real," yet 98.7 % of the dominant DESI component (≈190 k deduplicated clusters) lie on sky-fiber/filler/calibration spectra with no primary science TARGETTYPE; the science-target-matched yield is only 2,468 clusters (≈0.92× the Liang et al. EDR benchmark of 2,685 on comparable target selection). The large multipliers (∼141×, ∼73×) are explicitly labeled process-volume figures, not like-for-like increases in confirmed astrophysical anomalies; the title and headline framing therefore overstate the scale and nature of validated new sources relative to the evidence presented.

[MINOR] §II B and §III E: Feature scalers for the eROSITA (47-feature) and NEOWISE (15-feature) tabular surveys were fit on the full sample rather than the training split alone, allowing validation-set tail information to enter the normalization constants used for MSE scoring. The supplied eROSITA robustness check shows ∼15–17 % extreme-tail churn (comparable to retrain floor), but absolute S values and any downstream score-dependent statistics remain affected; the paper should adopt train-split-only normalization as standard and quantify the effect on all affected tiers.

[MINOR] §III F and §VI D (i): The Planck top-200 tier is selected in-sample on the full 2×10^5-patch native bank; while the post-hoc held-out enrichment test (48/200 observed vs. ∼30 expected, binomial p ≈ 5.5×10^{-4}) argues against memorization inflation, the selection itself is not held-out. Combined with the stated sensitivity floor for narrow single-pixel lines (recover only at ≥15σ on the 496-bin mean-reconstruction scorer), this requires a more prominent, quantitative caveat in the abstract and primary validation claims when asserting that the 268,519 subset is detector-validated for the reported anomaly class.

[MINOR] §IV A and cross-match methodology: The 17.8 % genuine-novelty fraction (178/1,000) for the DESI top-1,000 is correctly measured against an 18-catalog CDS X-Match baseline and properly distinguished from the much higher SIMBAD-unmatched fractions; however, the paper must explicitly state that this fraction applies only to the ranked top-1,000 stratum and does not extend to the full 268,519 validated set or to the exploratory tiers, to prevent readers from generalizing the discovery rate.

The central claim of a validated 268,519-source multi-survey anomaly catalog is only partially supported by the evidence: per-survey stability (5-fold J̄CV = 0.862, OOD J̄ = 0.732) and injection-recovery gates pass for the core broad/continuum class in DESI, SDSS (64 %), Planck (100 %), and NEOWISE geometry QA, but are undermined by the irreproducible eROSITA tier, the 98.7 % non-science-target dominance in the DESI contribution, the explicitly process-volume (not confirmed-detection) character of the headline count, and the narrow-line sensitivity floor.

# EXTDB2 P3 Grok — chat: https://grok.com/c/3a2cbba3-7b6a-4d31-a352-490dacd06c32?rid=7966e7ac-af4a-4ad1-a8ac-d699dddfd47c

Provider: Grok Expert
PDF md5: d3d662cb8d0c737032580465397911f2
Harvested: 2026-06-28

---

Referee Report: MNRAS / PRD / JCAP
Paper: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 269,317 Recommended-Tier (378,280 Total) Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches
Author: Houston Golden
Date of report: 28 June 2026

1. Recommendation
MAJOR REVISIONS

The work represents a substantial technical effort in large-scale unsupervised anomaly detection across heterogeneous archives. The Path-C native-retrain protocol, multi-gate validation framework, and extended archival novelty assessment are methodologically thoughtful and represent a genuine advance over prior single-survey efforts. However, the manuscript in its current form does not meet the acceptance threshold for a top-tier journal. The headline claims and catalog framing significantly overstate the delivered scientific yield relative to the documented limitations, one key component has irreproducible scores, and the cosmological application section rests on a null empirical result that is presented too optimistically.

2. BLOCKERS (must be resolved for acceptance)

B1. Irreproducible eROSITA scores and undocumented production axis (Section III E; Table IV; pipelines/p3_anomaly_engine/r24conf_erosita_axis_sweep.json). The production SBigAE threshold (0.259) and per-object scores cannot be recovered from any of 16 tested monotone rescalings of the committed raw reconstruction scores, nor from retrained IsolationForest axes. The top-5 scores are non-monotone in the raw artifact (Spearman ρ = −0.10). The manuscript states that the membership list itself (n=298) is the canonical, reproducible product. While this is transparent, releasing a catalog component whose primary ranking/selection axis is irreproducible from committed artifacts is unacceptable for a data-release paper. Either (a) recompute the tier with fully committed, reproducible code, or (b) explicitly demote eROSITA to a purely exploratory membership list with no scores and stronger caveats.

B2. Headline framing vs. documented scope for DESI DR1 (Abstract; Section III A; Table II). The abstract and title lead with 195,829 DESI anomalies (0.87% of 22.5 M spectra) and the overall 269k/378k figures. Only later is it revealed that ~98.7% of the deduplicated DESI anomaly clusters fall on spectra with no primary science-class TARGETTYPE bit (86% have TARGET=0 — sky fibers, secondary/ToO programs, fillers). The science-target-matched subset is only 2,468 clusters (~1.3% of the DESI tier; ≈0.9× the Liang et al. EDR benchmark on a like-for-like science-target basis). The abstract and introduction must be rewritten to lead with the validated/catalog-grade numbers and to state explicitly, up front, the science-target fraction.

3. MAJORS (substantive but potentially fixable)

M1. Cosmological application section overstates current constraining power (Section V; abstract). The empirical Landy–Szalay bias ratio α_jk = 0.19 ± 0.65 is statistically consistent with zero (0.29σ) and with the fiducial α=0.15. The de-biased point estimate returns exactly the single-tracer baseline σ(fNL)=8.98; the central forecast of 8.14 is noise-driven. The 12 high-z QSO-candidate objects are explicitly unconfirmed. Recommend: (a) move the fNL forecast to an explicit "forecast for future work" subsection or appendix, (b) clearly state that the current anomaly-selected sample yields no improvement over single-tracer.

M2. Validation scope and sensitivity characterization. DESI relies on 5-fold Jaccard (¯J_CV=0.862) and OOD Jaccard rather than injection-recovery. The injection-recovery tests that were performed are continuum-dip only. Many reported anomalies (high-z, emission-line, Z-dominant) are not well-probed. For a catalog claiming robustness, either execute a broader injection suite or provide a stronger quantitative argument why stability metrics alone suffice.

M3. Inclusion of failed-gate components in headline "Path-C unique catalog." Gaia (5.2% injection-recovery, 41% XV-stability) and eROSITA (1.2% recovery) fail the detector-sensitivity gates yet contribute to the 378,280 total. LAMOST retained as "methodological lesson" after 21.5× rate compression. Either (a) make the recommended tier the primary released catalog with exploratory components clearly separated, or (b) provide a tiered release with explicit guidance on downstream use.

M4. Limited demonstrated astrophysical yield beyond the novelty fraction. The extended CDS X-Match yields a genuine novelty fraction of 17.8% (178/1,000) — a strong result. However, the paper provides almost no characterization of what these genuinely novel objects are. For a catalog paper, readers expect at least a preliminary taxonomy or example science cases for the novel subset.

4. MINORS

1. Abstract and title precision — lead with conservative, validated numbers; demote totals to secondary position.
2. DESI high-z candidate status — tighten language; clearly flag as unconfirmed.
3. Figure and table captions — make cross-transfer vs. native-retrain distinction unambiguous in every caption.
4. Companion data release plan — explicit, citable release plan required (per-object tables with validity flags, model weights, training scripts).
5. Minor notation/axis clarity — anomaly score S is per-survey standardized; repeat cross-survey incomparability reminder in every multi-survey figure.
6. Spatial uniformity test caveat — strengthen the caveat or remove numeric χ²=15.7 from main text.

5. Strengths

1. Methodological rigor and transparency of the Path-C protocol — per-survey native retraining, explicit multi-gate validation, documented failure modes (LAMOST, SDSS, ACT), validity flags per object. Sets a high standard for large-scale anomaly catalog construction.

2. Genuine novelty assessment — shift from SIMBAD-unmatched fractions to extended 18-catalog CDS X-Match yielding 17.8% genuine novelty is the right methodology. Substantive improvement over prior anomaly papers.

3. Scale + reproducibility infrastructure — processing 37.3 M sources with documented per-survey training, deterministic pipelines, and committed artifacts/scripts. Technical achievement.

4. Careful treatment of systematics in cosmological forecast — explicit de-biasing step, convex-mapping envelope for σ(fNL), acknowledgment that central improvement is noise-driven, Savage-Dickey Bayes factor caveats on NANOGrav comparison. Statistical maturity.

Summary: Ambitious, technically serious work with real methodological contributions. Blockers and majors are primarily issues of framing, scope calibration, and reproducibility of one component — precisely the areas where top-journal standards are non-negotiable for a data-release paper. Optimistic that a revised manuscript would be suitable for publication. Recommendation: MAJOR REVISIONS.

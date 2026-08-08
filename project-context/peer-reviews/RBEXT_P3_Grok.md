# RBEXT P3 Grok — chat: https://grok.com/c/729def66-51da-4fd6-8c93-f4e4d0aafc3e
VERDICT: MAJOR REVISIONS

Provider: Grok (Expert tier)
PDF: RBEXT_P3.pdf | md5: f6b8d9a5e16fc5f4f3301433c9c556dc
Harvested: 2026-06-29

---

Referee Report: MNRAS / PRD / JCAP
Paper: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 269,317 Recommended-Tier (378,280 Total) Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches
Author: Houston Golden
Date: 29 June 2026

1. Recommendation: MAJOR REVISIONS

2. BLOCKERS

None. There is no evidence of data fabrication, plagiarism, ethical violation, or irreproducible core pipeline. The eROSITA score-axis provenance failure is serious but not a blocker because the membership list itself is reproducible from committed raw artifacts.

3. MAJORS

Headline framing and science-yield vs. process-scale mismatch (§I, §III A, Table I, Table II, §VI E)

The paper leads with "≥268,519 unique validated anomalies" and cites process-scale multipliers (∼141× point-source tier, ∼73× DESI S > 5 subset) relative to Liang et al. However, §III A shows only 2,468 (∼1.3%) of DESI anomalies fall on validated science-target spectra; the like-for-like science-target comparison is ≈0.9× the Liang et al. benchmark (2,468 vs. 2,685), not the quoted multipliers. This is a clear case of headlining the more-favorable of two numbers.

Required action: Make the science-target subset the unambiguous headline deliverable. Relegate full-stream numbers to a clearly labeled "supplementary full-archive scan" section. Revise all multiplier language to distinguish process-scale from science-target-scale.

eROSITA DR1 tier — irreproducible score axis (§III E, Table IV, §VI D(ii))

The production threshold (0.259) and per-object SBigAE values cannot be recovered on any of 16 monotone rescalings of committed raw reconstruction scores, nor on retrained IsolationForest axes. The top-5 values are non-monotone (Spearman ρ = −0.10). The 5σ injection-recovery rate is only 1.2% (gate FAIL). Per-object scores are unusable for meta-analysis, score-weighted stacking, or threshold re-derivation.

Required action: Either (a) re-derive a reproducible score axis from committed raw artifacts, or (b) reclassify entire eROSITA contribution as exploratory/supplementary and remove it from headline validated counts.

Cosmological application — optimistic central-value presentation despite statistical null result (§V)

The Landy–Szalay measurement on 5,384 QSO-candidate sample yields α_jk = 0.19 ± 0.65 (0.29σ from null). The 1σ envelope is [3.92, 8.98] — fully consistent with zero improvement. The de-biased amplitude returns exactly the single-tracer baseline. The NANOGrav result is only marginally consistent (+1.13σ) and the Bayes factor is prior-sensitive.

Required action: Re-frame §V as a preliminary methodological exercise. Move numerical forecast discussion to appendix. Remove implications that the current catalog tightens fNL constraints competitively.

Tier nomenclature and reader-misinterpretation risk (Table I, §III D/E/G)

LAMOST (training-bias artifact: 98% blue-excess, 5.8% injection recovery, gate FAIL), Gaia (5.2% recovery, 41% XV-stability), and eROSITA appear in recommended/validated language before being relabeled exploratory in fine print.

Required action: Define a single "validated core catalog" (DESI + SDSS native + Planck + NEOWISE). Move all exploratory/failed tiers to clearly labeled supplementary data products with prominent health warnings.

Limited scientific impact beyond catalog production

Beyond three cross-survey cross-matches and 12 high-z QSO candidates, there is no strong population study or quantitative science result leveraging the multi-survey aspect. The 17.8% novelty fraction is measured only on the DESI top-1,000.

Required action: Add a dedicated science-results subsection or re-frame as a methods + data-release contribution.

[Note: response was truncated by cookie dialog before MINORS and STRENGTHS sections]

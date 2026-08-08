# P3 RB-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=b5565d8e pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6990 chars)
**Wall time**: 454.9s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog …”

Overall scope and remit
I reviewed the entire 30-page manuscript, including all figures, tables, equations, captions, and the abstract. I recomputed the quoted percentages/ratios where possible, checked dimensional consistency, and audited the statistical procedures and claims of significance. The submission is ambitious and contains many internal audits and caveats, which I appreciated. However, several methodological and reproducibility issues must be fixed for Physical Review D standards.

Findings and required actions

ESSENTIAL

P3-E1 — Abstract; also §II D, §III E, §VII; multiple pages
Problem: The “validated catalog-grade subset” headline number is reported as “≥268,519 unique anomalies (≥268,319 point-source)” with the explicit admission that “the exact validated-only 5′′ re-dedup … is not recomputable from the committed aggregate artifacts.” Publishing a non-recomputable core headline undermines reproducibility.
Required fix: Provide an exact, recomputable validated-only dedup manifest (7-way 5′′ union-find run restricted to the validated components) and update the headline to the exact value with a frozen file hash/DOI. If this is impossible, remove the “validated catalog-grade” count from the abstract and throughout; instead, clearly label any such number as non-reproducible and move it to an appendix as an illustrative estimate.

P3-E2 — Abstract; §II D Step 1; §VI D(ii); Table I notes; Fig. 10
Problem: Heterogeneous and partly ad hoc gating/threshold rules across surveys (DESI absolute S>5; SDSS “continuity slice” S≥0.1060 sized to match a transfer-learning count; LAMOST native top-1%; eROSITA fixed top-298 on an irreproducible score axis; Planck/NEOWISE fixed 1%) are not pre-registered, and for SDSS the continuity slice is not the native top-1% nor the canonical S>5. This risks selection-tuning and hampers cross-survey comparability.
Required fix: Pre-declare a single primary selection rule per survey family (e.g., “native-trained model; selection by top-q% on standard S,” with q fixed) and re-issue the primary catalog on those rules. Keep continuity/membership-only tiers as explicit secondary products. Alternatively, justify—with power/robustness studies—why non-uniform thresholds are necessary and that they do not change the main conclusions.

P3-E3 — Abstract; §Data Availability (p. 24)
Problem: Data/code availability is in future tense (“will be made public with the arXiv posting”; “DOI inserted at submission”), and critical artifacts are referenced via internal paths (“pipelines/…/*.json”), not immutable DOIs.
Required fix: Deposit all load-bearing artifacts (native-rescore tables, 7-way dedup manifests, injection-recovery plants/results, Planck native model and top-200 patch indices, SDSS/LAMOST native checkpoint metrics, MCMC chains) in a public archive with stable DOIs (Zenodo or equivalent). Replace all internal path references with working DOIs and include file hashes. The paper cannot proceed without this.

P3-E4 — §III E (pp. 11–12); Table IV caption; Abstract
Problem: The eROSITA per-object SBigAE score axis is irreproducible; yet eROSITA contributes to the “recommended tier” in the abstract/main text (even if flagged exploratory).
Required fix: Either (a) remove eROSITA entirely from any “recommended” count/tier and keep it as a membership-only exploratory appendix, or (b) re-derive a reproducible score axis and selection (e.g., canonical S, or an independently refit detector), and deposit the exact derivation. Align all abstract counts with the final decision.

P3-E5 — §IV B (p. 15)
Problem: Cramér’s V is written as “Cramér’s V = √(χ2/(N·(k−1)) = 376,713/(378,280 × 24,048) ≈ 0.0064)”. The numeric step drops the square root in the expression even though the result equals the square-rooted value. This is a methodological expression error in a statistical headline.
Required fix: Correct the expression to show the square root on the numeric ratio, i.e., V = sqrt[376,713/(378,280×24,048)] ≈ 0.0064, and briefly define k (number of occupied HEALPix pixels) and N (total objects) to prevent ambiguity.

P3-E6 — Abstract-last drift; multiple statements
Problem: The abstract mixes validated and exploratory components in the “recommended tier,” and interleaves “PASS”/“FAIL” injection-recovery results with a global novelty statement, risking reader confusion about what is catalog-grade.
Required fix: Rewrite the abstract so that (i) only validated components contribute to headline “catalog-grade” counts; (ii) exploratory components are enumerated separately; and (iii) each “PASS/FAIL” refers to a single, clearly defined gate (detector-sensitivity vs. geometry-QA). Ensure the ordering and strength of the abstract statements exactly match the corresponding strongest caveats in the body.

MAJOR

P3-M1 — §II D (p. 5); Table I notes; §VI D(ii), Fig. 10
Problem: Gate thresholds (val-loss ≤ 0.30 within ≤100 epochs; injection-recovery ≥50% at 5σ; Jaccard ≥0.70/≥0.50) are heuristic, not supported by a power analysis or sensitivity study. Only one borderline gate (SDSS 64% vs 50%) could flip under stricter criteria.
Required fix: Provide a sensitivity analysis varying gate thresholds (e.g., 0.2–0.4 val-loss; 40–70% injection recovery; Jaccard ±0.1), showing that survey PASS/FAIL calls remain stable except where explicitly acknowledged. Report how headline counts would change.

P3-M2 — §III C (pp. 10–11); Table I footnote ♡; §IV C (p. 17)
Problem: The SDSS “continuity slice” (77,905) is not the native top-1% (19,253) nor S>5 (12). It is used in overlap/dedup geometry and in several narrative points. This selection is arbitrary and could bias cross-survey overlap structure.
Required fix: Re-run the 7-way 5′′ dedup (and all overlap-sensitive metrics) with the SDSS native top-1% set. Report differences alongside the continuity-slice version. For the main text, use the native top-1% as the primary SDSS catalog; move the 77,905 slice to SI as a secondary comparison.

P3-M3 — §IV A (pp. 13–14)
Problem: SIMBAD-unmatched percentages are shown (Fig. 6, Table I) and later corrected by an 18-catalog cross-match leading to 17.8% genuine novelty (DESI top-1,000). However, the abstract and some text still foreground large SIMBAD percentages which readers may misinterpret.
Required fix: Every occurrence of SIMBAD-unmatched fractions in the main text must be paired with the explicit qualifier that these are database-coverage statistics and not novelty. Where space is tight (figure captions), add a one-sentence warning and cross-reference §IV A. Keep the 17.8% novelty as the only discovery-rate statistic.

P3-M4 — §V (pp. 17–19); Appendix C/D
Problem: The Fisher-forecast mapping 1/σ^2 = F0 + c α^2 and its calibration (F0,c) are not fully documented (derivation given only as “5-α refit” without enough explicit numbers to be reproduced).
Required fix: Provide the five calibration points (the exact α grid and resulting σ or 1/σ^2 values) and the fitting procedure to obtain c (with uncertainty). Deposit the Fisher code and inputs via DOI. Ensure the “positivity-respecting” formulation is cross-validated against a direct Fisher matrix with α→0 and α→α±σα.

P3-M5 — §III F (“Train/score disjointness”, p. 12–13)
Problem: The Planck top-200 anomaly set is drawn from a scored set that includes training patches; the top-200 are not held-out, although an enrichment toward validation patches is noted (binomial p≈4×10−4).
Required fix: Provide a clean held-out top-200 list by re-scoring an independent sky bank not used in training/validation and show the top-k overlap and score distribution stability. If infeasible, quantify the possible inflation of anomaly scores by in-sample training and add a prominent caveat in §III F and the abstract.

P3-M6 — §II B (pp. 3–4) and §III G (p. 13)
Problem: For Gaia (20-feature run), the exact production preprocessing script was not recovered; for eROSITA, scalers were fit on the full sample, not train-only (with some bounded checks). This undermines reproducibility and comparability.
Required fix: For Gaia, either (a) recover and deposit the exact preprocessing script via DOI, or (b) rerun with a fully specified pipeline and replace the published Gaia anomalies accordingly. For all tabular surveys, rerun with train-only scalers (or fully document why using full-sample scalers does not change ranks materially), and deposit before/after overlaps and rank correlations.

MINOR

P3-m1 — §IV C (pp. 16–17)
Problem: Dedup-radius sensitivity is reported (3′′/5′′/7′′) with small unique-count differences. However, no uncertainty band is assigned to the headline unique count from this choice, though the sensitivity is small.
Required fix: Add a sentence in §IV C quantifying the maximum possible headline-count variation (≤0.086%) due to the radius choice and clarifying that it is negligible relative to other uncertainties.

P3-m2 — §III A (p. 6); Table II
Problem: The “like-for-like ≈0.9×” comparison vs. Liang et al. (2,468/2,685≈0.92) is rounded down; the denominator definition differences are intricate (TARGETTYPE vs bitmask).
Required fix: Quote the exact ratio (0.92×) and keep the definitions transparent by adding a one-sentence reminder that the benchmark used the EDR science-target selection while your recount uses DR1 under the science-bit mask.

P3-m3 — §IV A (p. 14)
Problem: Expected false-match count for DESI×SDSS (3′′ shift control ≈2.3) is compared with 3 observed true matches from an earlier cross-transfer exercise; later a different run yields 4 vs 2.75. The controls (RA-only shifts) are geometry-imperfect.
Required fix: Label both as heuristic and add one sentence committing to a great-circle random rotation test in the data release; remove any implied statistical inference from these numbers in the main text.

P3-m4 — §III H (p. 13)
Problem: The NEOWISE ecliptic mask “injection-recovery” is a geometry-QA and not a detector-sensitivity test; the paper largely makes this clear.
Required fix: In Fig. 10 caption, bold “geometry-QA” once and add “not a sensitivity PASS” to prevent casual misreading.

P3-m5 — §V A; Appendix E (pp. 19–21,26–28)
Problem: Bayes-factor robustness is carefully addressed, but the decisive Jeffreys label risks being over-read relative to the astrophysical-environment caveat.
Required fix: In §V A, add one sentence up front (not only in the final paragraph) that the “decisive” Bayes factor applies only to the idealized circular SMBHB prior and does not exclude environmentally modified SMBHBs.

P3-m6 — §II C (p. 5)
Problem: Throughput and wall-clock numbers are useful but belong in SI.
Required fix: Move detailed pod provisioning JSON paths and retry/resume events to SI; retain only the key throughput numbers in the main text.

NIT

P3-n1 — Throughout
Problem: Numerous internal file paths and run-log filenames (e.g., pipelines/p3_anomaly_engine/…, log.json, *_R54.json) clutter the main text.
Required fix: Collect these into a single “Reproducibility Artifacts” table in SI, with DOIs/hashes. In the main text, keep only human-readable identifiers and DOI links.

P3-n2 — Fig. 2 caption (p. 7)
Problem: “Color-coded by survey (see legend)” without a legend color-key on the printed page margin is slightly awkward but decipherable.
Required fix: Ensure the color legend is explicit and readable in print.

P3-n3 — Typos/wording
- §III F: “re-removal” can be simplified to “removal (reapplied)”.
- §IV B: add units “deg” once in “angular distance from the Galactic plane” axis label in Fig. 7 bottom-right panel.

Length and focus
At 30 pages, with many operational details, the manuscript is long for PRD. I recommend compressing to 24–26 pages by moving implementation logs, pod/throughput minutiae, and extended footnotes to SI. Keep all core derivations, gates, injection-recovery curves, and the Fisher/NANOGrav analyses in the main text.

Abstract-last drift sweep
I verified the main abstract scalars against the body. Most are consistent (e.g., 378,280 unique = 388,493 − 10,213; DESI-only 195,829 ≈ 0.87% of 22.5M; SDSS 64% injection-recovery; Planck 100%; LAMOST 5.8%; Gaia 5.2%; eROSITA 1.2%; novelty 17.8% ±1.2%; αjk = 0.19 ± 0.65; σ(fNL) envelope [3.92, 8.98]; NANOGrav γ = 2.567 ± 0.382; +1.13σ relative to 3.0 and +4.61σ relative to 4.33; Bayes factor 7.14×10^3). However, the abstract currently (i) mixes validated and exploratory components in the “recommended” tier; and (ii) presents a non-recomputable “validated subset ≥268,519.” Both require the ESSENTIAL fixes above.

Bibliography
Spot checks (DESI DR1 2025 AJ accepted; eROSITA 2024 A&A; NANOGrav 2023 ApJL; UMAP/HDBSCAN arXiv/software) are reasonable. Please ensure that all quoted external statistics (e.g., Liang et al. 2,685 anomalies) match the cited source’s abstract or tables.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript contains substantial new work at scale and is careful in many statistical caveats, but it does not yet meet PRD standards for methodological rigor and reproducibility. The most serious issues are (i) the non-recomputable “validated” headline, (ii) non-uniform, partly ad hoc selection thresholds lacking a pre-declared primary estimator/tier (notably for SDSS and eROSITA), and (iii) incomplete data/code availability (no stable DOIs). These are fixable. Once corrected—and with the abstract revised to align precisely with the validated results—the submission could be suitable for PRD, provided the requested sensitivity analyses and reproducibility artifacts are supplied.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes audit)

ESSENTIAL

P3-E7 — Abstract; §V; Fig. 9; selection for Fisher inputs
Problem: The Fisher forecast uses “AI-selected anomaly-tracer counts per redshift bin; the seven bins total 40,192 tracers,” but the paper never specifies the redshift-quality and targeting-quality cuts used to build this 40,192-object tracer set (e.g., ZWARNING=0, reliable template class, S/N cuts, primary row choices, sky/filler exclusion). Earlier, you emphasize that 98.7% of DESI anomalies are on non-primary science targets and note possible calibration/systematics in B-dominant spectra. Using anomalies without an explicit, reproducible quality mask risks contaminating the Fisher inputs with unreliable redshifts and non-cosmological spectra.
Required fix: Define and document the exact quality and targeting cuts for the 40,192 Fisher tracers (ZWARN, SPECTYPE, SN thresholds, TARGETTYPE/bitmasks, PRIMARY row logic), deposit the resulting list via DOI, and show how σ(fNL) changes if you tighten/loosen these cuts (e.g., ZWARN=0 vs ≤4; exclude filler/sky fibers). If this provenance cannot be nailed down, move the 40,192-based forecast to SI and keep only the bias-measurement result.

MAJOR

P3-M7 — §V vs Appendix C; forecast configuration consistency
Problem: The main Fisher forecast (σ(fNL) std = 8.98, “positivity-respecting” 1/σ2 = F0 + c α2) is calibrated using a 5–α grid but the Appendix C/shot-noise figure discusses a “canonical 5-tracer DESI QSO/LRG/BGS + gold/silver-anomaly” configuration on an internal normalization (single-tracer 16.85; dense-limit 11.71), while the main text elsewhere treats a DESI-QSO single-tracer 8.98 baseline and an anomaly add-on. The number of tracers and normalizations differ between main text and appendix, risking reader confusion about what configuration underlies F0 and c.
Required fix: State explicitly, in §V, the exact tracer set and normalization used to determine F0 and c, and reconcile it with the 5-tracer configuration in Appendix C (or move the 5-tracer figure to SI as illustrative only). Provide a small table mapping “config → (σstd, F0, c)” so readers can see which numbers belong together.

P3-M8 — “Largest”/“at scale” claims; §I, Abstract, §VII
Problem: The paper claims “largest application of autoencoder anomaly detection … of which we are aware,” and several “×” multipliers versus prior work. There is no structured comparison (sample sizes, object counts, per-survey thresholds) against recent multi-archive or very-large single-archive anomaly searches (including non-autoencoder approaches).
Required fix: Add a comparison table listing prior published anomaly catalogs (method class, archives, N processed, N anomalies, selection rule) and show, with citations, where 37.3M and 378,280 stand. If comparable-scale efforts exist (even non-AE), adjust the claim; otherwise, anchor the “largest” assertion to that table.

P3-M9 — §III F Planck CMB anomalies: missing simulation-based null
Problem: The native Planck top-200 patches concentrate near the south ecliptic pole and you attribute this to scan-pattern noise. Without a simulation-based null (e.g., Planck FFP or noise-only realizations run through the same pipeline), the anomaly list is likely dominated by survey noise inhomogeneity rather than astrophysics.
Required fix: Run at least one Planck noise-only or FFP realization through the identical CAE+ranking to (i) quantify the expected spurious anomaly rate and (ii) show the sky distribution under the null. If infeasible for this round, explicitly reframe the Planck tier as a “noise/systematics map-diagnostics product” and remove it from any “catalog-grade validated” wording in the abstract and conclusions.

P3-M10 — §III A SNR–score correlation claim
Problem: The claimed negligible SNR correlation (ρ = −0.03, p = 0.12) is computed on a stratified, non-representative subsample chosen to be log-uniform in SNR. You note this caveat but still use the numerical p-value in the main text.
Required fix: Provide the same correlation on a true random DESI subsample (with N and p-value), and/or show a partial correlation controlling for ZWARN or S/N. If not available before publication, remove the p-value and state only that the stratified effect size is small.

P3-M11 — §II B; §III A; training-pool representativeness
Problem: The DESI BigAE is trained on 47,000 spectra, but no stratification is given (per TARGETTYPE/SPECTYPE, S/N, z). Given the clear training-bias lesson from LAMOST, it is important to show that the 47k pool spans the DESI science classes and S/N/redshift ranges used later.
Required fix: Provide a training-pool summary (class/z/SNR histograms vs. the full DR1 curated set) and an overlap Jaccard by class between each of the 5 CV folds’ top-1% and the production top-1%. Deposit the training-ID list via DOI.

MINOR

P3-m7 — §III E; Table I; novelty figures on unstable tiers
Problem: eROSITA’s membership has documented ∼15–17% extreme-tail churn across reruns/hardware; Gaia’s XV-stability is 41%. Yet you report counts like “203 SIMBAD-unmatched eROSITA membership-list sources” without an uncertainty.
Required fix: Quote uncertainty bands for such integrals on unstable tiers (e.g., ±(membership churn) on counts), or move them to SI with a stability disclaimer.

P3-m8 — §IV C; overlap structure transparency
Problem: You report 637 cross-survey clusters and “none spans three or more surveys,” but no pairwise overlap matrix is shown.
Required fix: Add a 7×7 pairwise overlap matrix (counts of 5′′ coincidences) in SI to document which pairs dominate the 637 multi-survey clusters.

P3-m9 — Fig. 9 and §V wording
Problem: Fig. 9’s per-bin tracer histogram (40,192 anomalies) is described as an illustration of the fixed-α reference, while §V’s primary forecast uses an empirical α from a different 5,384-object QSO-candidate set.
Required fix: Add a one-sentence caption note: “Counts shown are from the DESI anomaly subsample used in the fixed-α reference; the empirical-α forecast uses a different, 5,384-object QSO-candidate set.”

NIT

P3-n4 — Appendix E Eq. (E1) clarity
Problem: Eq. (E1) omits units/comments for ρi and fi; logs are base-10 but this is not reiterated in the line below.
Required fix: Add “log10 throughout,” define ρi units or normalization (e.g., PSD per frequency bin), and state fi = (i+1)/Tobs in yr−1 explicitly in the equation context.

Explanation
The initial review focused on reproducibility, mixed tiers, threshold heterogeneity, and data/DOI issues. The fresh-eyes pass highlighted additional comparability and provenance gaps affecting the cosmology forecast inputs (P3-E7), consistency between main-text and appendix forecast configurations (P3-M7), support for “largest” claims (P3-M8), the need for a null-simulation control for the Planck tier (P3-M9), and representativeness/SNR-correlation evidentiary gaps (P3-M10, P3-M11). These additions target PRD’s rigor expectations without repeating earlier points.
# P3 auto-2026-06-08_1424pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8019 chars)
**Wall time**: 505.8s

---

Referee report on: “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches”

Scope of review
- Focus: methodology rigor, statistical validity, internal consistency, arithmetic checks, clarity of estimators and thresholds, error propagation, significance claims.
- I have read the full 20-page manuscript including figures, tables, equations, captions, and appendices.

Overall assessment
This paper assembles a very large multi-archive “anomalies” catalog using autoencoders and offers several methodology claims and cosmological projections. However, there are multiple methodology inconsistencies, a dimensionally incorrect key equation parameter used in the fNL forecast, threshold-policy contradictions, and runtime/accounting inconsistencies. Several claims in the abstract conflate distinct “sigma” concepts without an explicit “not directly comparable” caveat, and the data/code availability statement is not compliant with PRD expectations. The paper can potentially be brought to PRD standards, but only after substantial revisions.

Findings
ESSENTIAL

P3-E1 (Section V b; page 11 and Table IV (i); page 13)
- Problem: Dimensionally incorrect baseline Fisher term. The text states “Under the Fisher-positivity-respecting asymptotic form 1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747.” Likewise Table IV (i) lists “F0 = 1/8.98^2” inconsistently (“1/8.982” in body; table uses “1/8.982” text but context suggests squared). For 1/σ^2 to have units of inverse-variance, F0 must be 1/σstd^2 = 1/(8.982)^2 ≈ 0.0124, not 1/8.982 ≈ 0.1113. Your central value σ(fNL) = 8.14 is numerically consistent with F0 = 1/(8.982)^2, so the written formula is wrong.
- Required fix: Correct all occurrences to F0 = 1/(8.982)^2 and audit the propagation of this correction across the manuscript (Section V, Table IV (i), Appendix C). State numerical values explicitly once (F0 ≈ 0.01240, c = 0.0747) and verify all derived σ values.

P3-E2 (Abstract; page 1; Section V b; page 11)
- Problem: Inconsistent “% improvement” versus quoted σ values. With σstd = 8.98 and σcentral = 8.14, the fractional improvement is (8.98 − 8.14)/8.98 = 9.35%, not “7.9%” (or “7.93%”). The 7.9% figure appears to come from a linearized α-scaling, but the positivity-respecting form used for the central σ implies the 9.35% figure.
- Required fix: Make the improvement percentage numerically consistent with the reported σ values throughout the paper (abstract, Section V, conclusions, Table IV). If you prefer to quote a linearized “forecast scaling,” present it separately and label it clearly as a different approximation. Do not mix numbers from different approximations.

P3-E3 (Section II B; page 2; Table I footnotes and Section III C; pages 7–8)
- Problem: Threshold-policy contradictions for SDSS (and, by spillover, LAMOST). Section II B states “DESI DR1 and SDSS DR18 use an absolute canonical-S cut at S > 5.0,” whereas Table I footnotes and Section III C state the SDSS headline count is a top-1% continuity slice (S ≥ 0.1060), with only 12 objects at S > 5 under the DESI scale and a native-rescore context. This is inconsistent and confusing for reproducibility and for interpreting rates.
- Required fix: Unify and clearly document, per survey, the definitive threshold/selection actually used for each headline count (both in the table and the main text). Remove contradictions. If multiple threshold definitions are used for different purposes (domain-shift diagnostic vs catalog continuity slice), separate them cleanly and label them unambiguously where first introduced. Include a compact per-survey threshold table in the main text with one authoritative line per survey.

P3-E4 (Abstract; page 1; throughout)
- Problem: Mixing different “sigma” concepts without an explicit “not directly comparable” caveat. The abstract juxtaposes “5σ” injection amplitudes (a detector test measured in multiples of noise σ) with “+4.61σ” significance for the NANOGrav γ posterior Gaussian distance. These σ’s quantify different nulls and are not comparable. The abstract lacks an explicit statement to that effect.
- Required fix: Add an explicit sentence in the abstract and again at first juxtaposition in the main text stating that the “σ” used in injection-recovery (amplitude units relative to local noise) is not comparable to the “σ” used as posterior standard deviations in parameter inference. Wherever two distinct σ-quantities appear side-by-side, add “not directly comparable.”

P3-E5 (Section V b; page 11)
- Problem: Ambiguous “1σ envelope [3.92, 8.98]” for σ(fNL). This range is produced by mapping α ± 1σ into σ(fNL) via 1/σ^2 = F0 + c α^2; it is not a 1σ uncertainty on σ(fNL) under any standard sampling distribution for σ. Labeling it a “1σ envelope” without a construction explanation is misleading.
- Required fix: Define precisely how that interval is constructed (e.g., extremizing σ(fNL)(α) over α ∈ [α̂ − σα, α̂ + σα]) and replace “1σ envelope” with “range induced by α ± 1σ propagated through the Fisher formula; not a Gaussian 1σ on σ(fNL).” Add: “not directly comparable to a conventional 1σ parameter uncertainty.”

P3-E6 (Section II C; page 3; Table V; page 16)
- Problem: Inference runtime accounting is inconsistent. You state “total processing time … approximately 42 hours,” “dominated by DESI (19,705 s) and LAMOST,” with others “<10 seconds.” From provided throughputs, DESI ~5.47 h and LAMOST (11.4M/950 s−1) ~3.33 h; adding all others and the listed training times (~2.5 h) totals ~11–12 h, not ~42 h. The discrepancy of ~30 h is unexplained.
- Required fix: Recompute and report consistent wall-clock times, stating clearly what is included (I/O, preprocessing, training, inference, checkpointing, retries). If 42 h is correct, provide a breakdown that reconciles it with the quoted throughputs.

P3-E7 (Data availability; page 14, end of Conclusions)
- Problem: Data/code statement is not PRD-compliant. You state the catalog is “private pending arXiv acceptance; public upon acceptance.” PRD requires data and code supporting the results to be available to referees and, upon publication, to readers. Conditioning release on arXiv acceptance is inappropriate.
- Required fix: Provide a stable, accessible repository (with DOI where possible) available to referees now, and commit to making it public upon journal acceptance. Remove references to “pending arXiv acceptance.”

MAJOR

P3-M1 (Section V a–b; page 11; Appendix C; page 16)
- Problem: Primary estimator choice for α is not pre-declared and selection is post-hoc. Two estimators appear (geometric-mean Landy–Szalay and jackknife geomean), with αjk adopted. Criteria for choosing between them are not pre-registered and details (e.g., mask, randoms, binning, systematics mitigation) are insufficient to reproduce αjk = 0.19 ± 0.65.
- Required fix: Pre-declare the primary α estimator and justify its choice; provide sufficient details for exact reproduction (footprint, mask, pixelization, randoms generation size, edge corrections, bin definitions, estimator normalization, covariance estimation, and jackknife region construction). Provide robustness checks (vary bins, masks). If a different estimator was trialed, report it in a transparent model-selection narrative.

P3-M2 (Section IV A; page 9; Fig. 5)
- Problem: The aggregate “58.8% SIMBAD-unmatched” fraction lacks a clear aggregation definition (simple mean, weighted by anomalies per survey, or pooled match fraction). Without counts per survey per matched/unmatched, this number cannot be reproduced.
- Required fix: Specify exactly how the aggregate was computed (pooled fraction = total unmatched anomalies / total anomalies across surveys with SIMBAD-matchable coordinates). Provide the per-survey numerator and denominator in a supplementary table.

P3-M3 (Section III F; pages 6–7)
- Problem: CMB anomaly score definition and calibration. For Planck, the “score range [0.558, 0.621]” differs qualitatively from the canonical-S z-score scale used elsewhere. It is unclear whether those scores are raw MSE, normalized MSE, or some other quantity.
- Required fix: Clearly define the CMB anomaly score, including normalization, its relation to S in Eq. (2), and the thresholding policy used. Provide the validation distribution’s mean and variance (if S-like) or explicitly state that the selection is top-1% by raw loss.

P3-M4 (Section III C; pages 5–6; Fig. 2 right)
- Problem: Extremely large SDSS transfer-learning scores S ~ 10^10–10^11 on a z-scored axis indicate either numerical instability or a mismatch in the definition of S when transferring across domains. While you note “cross-transfer artifact,” the numerical stability and floating range are not discussed.
- Required fix: Document the numerical range and precision safeguards (data scaling, clipping, dtype) that ensure S remains meaningful under domain shift. Consider plotting in terms of percentile ranks for the cross-transfer presentation, or provide a rationale for interpreting 10^11-standard-deviation values.

P3-M5 (Section IV C; page 10)
- Problem: Chance-coincidence expectation “≲ 10 across all survey pairs” for the 7-way, 5″ dedup is stated without the parameters used in the calculation (surface densities, overlapping sky area).
- Required fix: Provide the calculation details: effective overlapping sky area per pair, surface densities used, and the formulae so that the ≲ 10 estimate is reproducible.

P3-M6 (Appendix E; page 16)
- Problem: Equation (E1) lacks dimensional clarity and definitions (ρi, fyr, fi, Tobs) and the mapping from the KDE product to the likelihood used. The Bayes factors rely on this exact likelihood specification.
- Required fix: Define all symbols in (E1), specify the likelihood form from the KDE product and precisely how it is used, and cite the corresponding term in the released product (including units/scales). Include the prior normalization for γ used in Savage–Dickey and show how the BF values are computed.

MINOR

P3-m1 (Section III A; pages 4–5)
- Problem: Repetition. The “Across the 6.5 million spectra … galaxies are flagged …” paragraph appears twice with near-duplicate content.
- Required fix: Remove the duplicated paragraph and consolidate the information once.

P3-m2 (Section II B; page 2)
- Problem: Notation clarification for S and z (astrophysical redshift) is helpful; however, later parts of the paper occasionally refer to “score” without reiterating that S is standardized MSE. This is minor but can confuse readers in sections where S is not used.
- Required fix: Add a short reminder at the start of each survey subsection that continues to use S that “S denotes the per-survey standardized reconstruction loss as defined in Eq. (2).”

P3-m3 (Table I; page 7)
- Problem: The “Rate (%)” for the “Path-C unique (primary)” row is shown as 1.01%. The table label could be misread as an independent “measured rate” rather than an aggregate catalog composition fraction with mixed survey thresholds.
- Required fix: Add a footnote clarifying that the total “rate” aggregates across heterogeneous thresholds and should not be interpreted as a single-survey anomaly frequency.

P3-m4 (Figures 2, 6)
- Problem: Axes are generally labeled but units are implicit (e.g., “Normalized flux” equals arbitrary units after normalization). This is standard, but a brief note in the caption would help.
- Required fix: Add “Normalized to unit continuum; arbitrary units” to the spectral figure captions.

P3-m5 (References)
- Problem: A few references are missing arXiv IDs or exact journal volume/pages are inconsistently provided across entries (e.g., [11], [12] include arXiv vs in-press notes inconsistently).
- Required fix: Regularize references to include consistent bibliographic info (journal, volume, page, year, arXiv where applicable).

NITS

P3-n1 (Typos; pages 12, 16)
- Problem: “Ceffyl” appears as “Ceffyl KDE chain” and “Ceffyl”/“ceffyl”; maintain capitalization consistency.
- Required fix: Standardize to “ceffyl” if that is the package name; otherwise capitalize consistently.

P3-n2 (Style; pages 6–7, Appendix F)
- Problem: Internal project jargon appears (“Path-C”, “quarantined”, “artifact”), which is fine within the narrative but occasionally reads like an internal log.
- Required fix: Consider replacing with more neutral methodological language (“native retrain protocol”, “excluded due to validation failure”) where appropriate for PRD style.

P3-n3 (Conclusions; page 14)
- Problem: The concluding bullet 7 contains a long sentence with multiple clauses.
- Required fix: Split into two sentences for readability.

Length
The manuscript is long (20 pages main text plus appendices and extensive footnotes) relative to the core PRD-appropriate methodological contributions (Fisher formalism, bias measurement, and cosmological implications). I recommend consolidating survey-by-survey operational details and cross-transfer diagnostics into a shorter appendix and focusing the main text on:
- Formal definition of the anomaly score and thresholds,
- Validation gates and injection–recovery methodology,
- The α estimator construction and Fisher forecast methodology and results,
- Cosmological interpretation and limitations.
A main text of ~12–14 pages would be appropriate.

Additional arithmetic checks (spot-audited)
- 378,280 unique = 388,493 survey-level − 10,213 dedup = 378,280 (correct).
- 378,080 point sources + 200 Planck map patches = 378,280 (correct).
- DESI anomaly rate: 195,829/22,504,897 = 0.870% (correct).
- SDSS cross-transfer fraction: 77,905/2,304,830 = 3.381% (correct).
- LAMOST rate-compression: 44,075/2,054 ≈ 21.46× (correct).
- SDSS rate-compression: 77,905/12 ≈ 6,492× (≈6500× claimed; correct).
- NEOWISE polar caps: expected fraction 1 − sin 80° = 1.519%; observed 17/436 = 3.899% ⇒ 2.57× (rounded 2.6×; correct).
- eROSITA enrichment: E[random overlap] = 298×9303/930,203 ≈ 2.98; observed 284 ⇒ 95.3× enrichment (correct).
- NANOGrav distances: |4.33 − 2.567|/0.382 = 4.61σ; |3.0 − 2.567|/0.382 = 1.13σ (both correct).

## Summary recommendation
MAJOR REVISIONS

The paper contains a dimensionally incorrect Fisher-baseline term used in the fNL forecast, inconsistent threshold policies across sections, a mismatch between reported run-time totals and per-survey throughputs, ambiguous presentation of a “1σ envelope” for σ(fNL), and a non-compliant data/code availability statement. These are critical issues for a PRD methodology paper. If the authors correct the Fisher-term error and all propagated quantities, unify and document thresholds, reconcile run-time accounting, clarify uncertainty propagation and σ-notion mixing, and provide compliant data/code access with full reproducibility for the α measurement and Planck scoring, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P3-E8 (Section III C; Table I footnote ♡; Fig. 2 right)
- Problem: “Top-1%” for SDSS is arithmetically inconsistent. The manuscript repeatedly labels the 77,905-object SDSS slice as “top-1%,” but:
  - 2,304,830 total → 1% = 23,048 (not 77,905).
  - 1,925,279 “native re-score” total → 1% = 19,253 (you also quote 19,253 elsewhere).
  - 77,905 corresponds to 3.38% of 2,304,830 or 4.05% of 1,925,279, not 1%.
- Required fix: Remove every “top-1%” label attached to the 77,905 figure. State explicitly which denominator and percentile each slice uses (e.g., “3.38% of 2.3048M cross-transfer” and “1.00% = 19,253 of 1.9253M native”). Align Table I footnote ♡, Section III C, and figure captions.

P3-E9 (Appendix C Fig. 8 vs Section V)
- Problem: Forecast baselines are inconsistent and not cross-referenced. Section V adopts a single-tracer DESI baseline σstd = 8.98 for the α→σ(fNL) mapping. Appendix C Fig. 8 uses a “baseline multi-tracer = 12.72” and “dense limit = 11.71” for a “canonical 5-tracer configuration of §V,” but §V does not define this 5-tracer baseline. Readers cannot map the 8.98-based Fisher used in the main text to the 12.72-based curves in Fig. 8.
- Required fix: Explicitly define the 5-tracer baseline in §V (tracer set, binning, n(z), b(z), Veff, kmax, systematics) and state that Appendix C analyzes that configuration. Add a sentence in §V explaining that the α→σ mapping in the main text uses the DESI single-tracer baseline (8.98), while Appendix C examines a separate SPHEREx-like 5-tracer baseline (12.72). Provide a bridging table listing both baselines with inputs.

P3-E10 (Table V; Section II B; Section II C)
- Problem: Training-time numbers are implausible given the stated training regimen. Section II B says up to 200 epochs with typical convergence at 100–150 epochs. Table V lists photometric/CMB “train time” of 1.2–10.6 seconds (Gaia 1.2 s, NEOWISE 1.6 s, eROSITA 7.6 s, Planck 10.6 s), which is incompatible with even a handful of epochs on 10^4–10^5 examples at batch size 512. Either the reported times are not end-to-end training times, or the epoch/early-stopping description is inaccurate.
- Required fix: Reconcile training regimens with wall-clock “train time.” Report: dataset size used for training, epochs actually run to convergence per survey, hardware, dtype, and what is included (data loading, augmentation, validation scoring). If numbers are per-epoch, say so; if they are inference-only, relabel. Provide realistic end-to-end training times.

P3-E11 (Section IV C)
- Problem: Over-strong bound on uniqueness sensitivity to match radius. The text claims that using alternate radii “cannot change the unique-object count by more than the 10,213 total compression observed at 5″.” That is only true when decreasing the radius (approaching no merges). Increasing the radius can increase the number of merges beyond 10,213, reducing the unique-object count by more than this amount.
- Required fix: Replace the absolute “cannot change by more than 10,213” with a correct one-sided statement: decreasing the radius cannot decrease the unique-object count by more than 10,213 relative to 5″; increasing the radius could reduce it further. Provide a brief sensitivity table for {3″,5″,7″} to quantify the effect.

MAJOR

P3-M7 (Section II B vs Section II D Step 1)
- Problem: Inconsistent training-set sizes. Section II B cites “47,000 spectra for DESI, proportionally sampled subsets for other surveys.” Section II D Step 1 states “a fresh BigAE is trained on a 2–5×10^5-spectrum subset of each survey’s own data.” DESI (47k) and SDSS/LAMOST (200k–500k) statements conflict; it is unclear which was used for each survey’s native retrain.
- Required fix: Provide a per-survey training-set-size table (Ntrain, Nval, Nfeatures), and ensure the narrative matches.

P3-M8 (Section III C)
- Problem: SDSS DR18 native re-score denominator mismatch is unexplained. You state DR18 provides 2,304,830 spectra, but the native re-score uses 1,925,279 spectra. The basis for excluding ~379,551 spectra is not described.
- Required fix: List the quality/flag cuts that reduce 2.3048M to 1.9253M (e.g., SNR thresholds, pipeline flags), with counts per criterion so the denominator is reproducible.

P3-M9 (Section III C vs Table II vs Fig. 3)
- Problem: Category/cluster mapping ambiguity. The text says the dominant SDSS UMAP/HDBSCAN cluster (∼84%) contains ultra-cool dwarfs. Table II’s top classes are “Uncategorized” (52.7%) and “NIR excess/high-z” (33.0%), which do not transparently map to “M7–T2 dwarfs.” The linkage between clusters and the emission-line taxonomy is not specified.
- Required fix: Provide a confusion/mapping table between HDBSCAN clusters and the emission-line taxonomy (counts, fractions), and document the rule used to label clusters as “cool dwarfs.”

P3-M10 (Cross-references: §VI D (v) vs Table IV)
- Problem: Cross-reference style is inconsistent. The text cites “§VI D (v)” while Table IV enumerates caveats by letters (a–j), not roman numerals.
- Required fix: Use a single, consistent indexing scheme for caveats across text, figures, and tables (e.g., Table IV (f) for the eROSITA IF overlap).

P3-M11 (Image scale; Figs. 4, 9 captions; Section III B)
- Problem: Cutout angular scales are asserted (e.g., “128×128 ≈ 54″ per side,” “256×256 = 108″×108″”) without stating the pixel scale or resampling used. DESI Legacy Survey images have native pixel scales different from 0.42″/pixel implied by these numbers; readers cannot reconcile the shown sizes with standard LS pixel scale.
- Required fix: State the image pixel scale (native or resampled) used for all cutouts and verify the quoted on-sky sizes. If resampled, provide the procedure.

MINOR

P3-m6 (Table I footnote ♠ vs abstract/body)
- Problem: “Catalog-grade tier” composition is ambiguous. Footnote ♠ lists Planck among catalog-grade contributors to the 264,938 unique objects, but elsewhere you recommend the 378,080 point-source tier for object-level analyses (excluding Planck patches).
- Required fix: Clearly separate “catalog-grade point-source tier” from “CMB patch tier,” and state whether the 264,938 excludes or includes the 200 Planck patches.

P3-m7 (Section heading just above Table I)
- Problem: “Two threshold families are in use…” is inaccurate; three families are used (absolute S>5, fixed top-1%, and eROSITA score-knee).
- Required fix: Change to “three threshold families” and list them once, with a compact per-survey table.

P3-m8 (Section IV A b; DESI×SDSS pair)
- Problem: For the DESI×SDSS 3″ cross-match, the expected random-coincidence “∼2.3” lacks the surface-density/area inputs and overlap footprint used.
- Required fix: Provide the pair’s overlap area, source densities, and the formula used to compute 2.3, similar to the request already made for the 7-way estimate.

P3-m9 (Fig. 2 right caption)
- Problem: “Spanning twelve orders of magnitude from the threshold (S = 5) to S = 1.9×10^11.” The ratio is 3.8×10^10 (~10.6 orders), not 12.
- Required fix: Either correct the phrasing (“~11 orders of magnitude”) or drop the numeric count and keep the log–log axis remark.

STYLE/NITS

P3-n4 (Wording; §III E)
- Problem: “(eastern half under Rosatom proprietary control)” reads like internal commentary rather than neutral scientific prose.
- Required fix: Use neutral phrasing (e.g., “eROSITA DR1 covers the western Galactic hemisphere; the eastern hemisphere is not publicly available in DR1”).

Explanation
The fresh pass focused on reproducibility arithmetic, baseline consistency, and appendix/main-text coherence. The most consequential new issues are the SDSS “top-1%” mislabeling (P3-E8), the baseline mismatch between Section V and Appendix C (P3-E9), implausible seconds-scale training times versus stated epoch schedules (P3-E10), and an over-strong uniqueness bound for alternate match radii (P3-E11). These impact interpretability and reproducibility and should be corrected for PRD-level rigor.
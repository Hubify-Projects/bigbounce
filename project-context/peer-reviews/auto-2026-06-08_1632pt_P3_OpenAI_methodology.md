# P3 auto-2026-06-08_1632pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7733 chars)
**Wall time**: 401.4s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches”

Scope of review
- Role: PRD methodology referee
- Focus: statistical and methodological rigor, internal consistency, dimensional analysis, arithmetic checks, significance claims, estimator declarations, reproducibility

Overall assessment
The paper presents a very large multi-archive anomaly-detection effort and includes an ancillary cosmology application. While much of the arithmetic checks out, several load-bearing issues require correction before the work can meet PRD standards:
- A dimensional/numerical mistake in the Fisher forecast formula (F0 term) that propagates through the fNL results.
- Inconsistent and, at points, incorrect use of “top-1%” for the SDSS thresholds and rates.
- Internal inconsistency about what constitutes the “catalog-grade” subset (Planck CMB patches included in one place, excluded in another).
- Ad-hoc gating and pass/fail criteria not pre-justified or sensitivity-tested.
- Data/code availability statements are contradictory (claimed as public, but listed as private pending arXiv acceptance).
- Several additional methodological and clarity problems (e.g., SDSS category definitions vs SIMBAD-match fractions, robustness of absolute S>5 threshold across domains, claims based on quarantined ACT anomalies).

Findings
ESSENTIAL items (must fix for PRD)

P3-E1
- Section V, page 11 (“b. Fisher forecast”): “Under the Fisher-positivity-respecting asymptotic form 1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747 … inserting αjk = 0.19 gives σ(fNL) = 8.14…”
- Problem: F0 is dimensionally wrong and numerically inconsistent. If σstd = 8.98 is the single-tracer baseline standard deviation, then F0 must be 1/σstd^2 = 1/(8.98^2) ≈ 0.0124, not 1/8.982 ≈ 0.111. The reported σ(fNL) = 8.14 is only recovered if F0 = 1/8.98^2 and c ≈ 0.0747.
- Required fix: Correct all occurrences of F0 to 1/σstd^2. Recompute and restate the forecast equation, central value, and envelope with explicit numbers from the corrected F0. State the numerical values used for F0 and c, and show one explicit calculation recovering σ = 8.14 to avoid further ambiguity.

P3-E2
- Table IV (page 13), row (i): “Fisher positivity: 1/σ(fNL)^2 = F0 + cα^2 with F0 = 1/8.982, c = 0.0747…”
- Problem: Same dimensional/numerical mistake as P3-E1 repeated in the table.
- Required fix: As in P3-E1, replace F0 by 1/8.982^2 ≈ 0.0124 everywhere.

P3-E3
- Table I footnote ♡ (page 7) and Section III C (page 6): “SDSS DR18 three-threshold disclosure… headline cross-transfer count of 77,905 at S ≥ 0.1060 is the top-1% continuity slice… the same 1,925,279-spectrum DR18 sample yields 19,253 anomalies at the harder top-1% score-knee cut S ≥ 0.2051…”
- Problem: 77,905/1,925,279 ≈ 4.05%, not 1%. Labeling 77,905 as a “top-1%” slice is incorrect and inconsistent with the stated 19,253-object “top-1%” count.
- Required fix: Remove all “top-1%” labels from the 77,905-object SDSS slice; clearly define each threshold and the corresponding fraction. Provide a single, consistent summary of SDSS thresholds, counts, and rates:
  - Cross-transfer S>5: 77,905/2,304,830 = 3.38% (already in Table I)
  - Native re-score S ≥ 0.1060: 77,905/1,925,279 ≈ 4.05%
  - Native re-score top-1%: 19,253/1,925,279 = 1.00%
  - Native re-score S>5: 12/1,925,279 ≈ 0.00062%
  Ensure every “top-1%” mention refers only to the 19,253-object set.

P3-E4
- Abstract (page 1) vs Table I footnote ♠ (page 7) vs Section IV C footnote block (page 7): The abstract says the recommended catalog-grade subset is “∼265,000 unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE)” i.e., point sources only, excluding LAMOST and Planck. Table I footnote ♠ states “catalog-grade tier (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE) is 264,938…”
- Problem: Internal inconsistency: The abstract excludes Planck patches from the catalog-grade subset, but Table I footnote includes Planck in the 264,938 figure. Also, the conclusions/usage note insist downstream “object-level analyses” should use the 378,080 point-source tier.
- Required fix: Choose one consistent definition of “catalog-grade subset” and use it everywhere. If “catalog-grade” is intended to be point sources only, provide the exact integer for that subset and remove Planck from that count. If Planck is to be included, then explicitly relabel the tier as “catalog-grade objects + Planck patches” and keep the point-source-only number adjacent. The abstract, Table I footnote ♠, and Conclusions must agree.

P3-E5
- Abstract (page 1): “The catalog, model weights, and reproducibility scripts are publicly released.”
- Data availability (page 14): “deposited on HuggingFace … private pending arXiv acceptance; public upon acceptance.”
- Problem: Contradiction between “publicly released” and “private pending acceptance.” PRD requires verifiable availability at review.
- Required fix: Make all artifacts stated as “publicly released” actually public at time of review or revise the text to reflect the current public availability accurately, including persistent DOIs, commit hashes, and version tags sufficient for full reproducibility.

P3-E6
- Section II D (pages 3–4) and throughout: Gating thresholds are introduced (e.g., val loss ≤ 0.30 or injection-recovery ≥ 50% at 5σ; DESI k-fold Jaccard ≥ 0.70; OOD Jaccard ≥ 0.50) without prior justification, power analysis, or sensitivity checks.
- Problem: Ad-hoc gates and pass/fail declarations are not justified a priori; this opens the door to post-hoc threshold selection. PRD methodology standards require that primary estimators and decision thresholds be pre-declared or justified with sensitivity analysis.
- Required fix: Either pre-register the gate thresholds (demonstrate they were specified before looking at the results) or provide a sensitivity study showing conclusions are robust to reasonable variations of these thresholds. For each gate, report how the PASS/FAIL status would change for ±20% variations in the threshold and discuss the impact on headline conclusions.

P3-E7
- Abstract (page 1) and Section III C (page 6): “∼6500× SDSS rate compression after native retraining” and Fig. 2 caption/right panel.
- Problem: The claimed “∼6500× rate compression” as written conflates counts and rates across different denominators and thresholds:
  - 77,905 (cross-transfer anomalies over 2,304,830; 3.38%) vs 12 (native S>5 over 1,925,279; 0.00062%) produce a count ratio of 6492×, but the rates are not directly comparable (different denominators, and S>5 vs S≥0.1060 are not like-for-like).
- Required fix: Replace “rate compression” with the precise, denominator-matched quantity you intend:
  - If you mean count reduction from 77,905 to 12, say “count reduction 6492×” and explicitly state both denominators and thresholds for each.
  - If you intend a rate ratio, compute it with a consistent denominator, threshold, and sample (e.g., apply both thresholds to the same 1,925,279 native-scored set and report the two fractions). Remove any ambiguous “rate” wording where denominators or score scales differ.

MAJOR items (significant revisions required)

P3-M1
- Section II B (page 3): “applying [S>5] to a random uncurated SPARCL sweep flags > 50% of spectra … a catalog-curation effect, not a threshold artifact; see §VI D (b) for full OOD reconciliation.”
- Problem: If the absolute S>5 threshold inflates to >50% flagged in a reasonable OOD sample, then the “absolute” threshold is not transportable across catalog calibrations. This undermines the interpretability of “S>5” as an absolute anomaly cut and suggests severe domain shift.
- Required fix: Provide a quantitative domain-calibration procedure for S (e.g., recalibrating µval and σval per-domain, or a robust quantile-based mapping) and demonstrate that anomaly rates stabilize across curated vs OOD samples when the calibration is applied. Alternatively, restrict all claims tied to “absolute S>5” to the curated DESI DR1 domain and explicitly prohibit transport.

P3-M2
- Section IV D (page 10): “This null result demonstrates that CMB patch anomalies from autoencoder analysis are dominated by survey-specific systematics rather than primordial cosmological signals…”
- Problem: The ACT anomalies used here are from a quarantined, undertrained, cross-transfer checkpoint that fails both gates (Appendix F). A domain-mismatched, undertrained model cannot support this strong a conclusion.
- Required fix: Soften the claim to a methodological note tied to the specific, quarantined ACT block; e.g., “Using a cross-transfer, undertrained checkpoint for ACT that fails our training gates, we find a null Planck×ACT cross-correlation consistent with instrument/systematics differences; no cosmological inference can be drawn.” Make the same clarification in the Conclusions where relevant.

P3-M3
- Table I footnote ⋆ and §III G (pages 7–8): Gaia DR3 IsolationForest XV-stability = 41.0% on an expanded 500,000-source sample; text says “treat as exploratory.”
- Problem: In several summary places (e.g., Abstract “recommended catalog-grade subset…”; Conclusions point 1), Gaia appears to be treated in the “catalog-grade” tier without the strong caveat that it is training-sample-conditioned.
- Required fix: Either (a) demote Gaia to the exploratory tier in all headline/tier summaries, or (b) add explicit “exploratory” caveats next to Gaia everywhere you list catalog-grade components, including the Abstract and Conclusions.

P3-M4
- Section IV A b (page 9): “For the 7-way 5″ deduplication, the expected random coincidence contribution is ≲ 10 across all survey pairs against 637 observed multi-survey clusters (<2% contamination).”
- Problem: No calculation details (surface densities, sky areas, pair enumerations) are provided. This estimate is load-bearing for contamination claims.
- Required fix: Provide the explicit calculation (per-survey source densities on the overlapping footprints, the matching radius used per pair, and the exact combinatorics) or move the derivation to an appendix and cite it. Report uncertainties.

P3-M5
- Section III C/Table II (pages 6–8): “The 52.7% ‘Uncategorized’ fraction reflects objects that match a SIMBAD entry but lack a specific astrophysical type classification in the database,” but earlier SDSS SIMBAD-unmatched fraction is stated as 90%.
- Problem: If 52.7% of 77,905 are “SIMBAD entries but untyped,” this implies far more matched objects than the 10% SIMBAD-matched fraction previously reported. As written, this is contradictory.
- Required fix: Define precisely what your “Uncategorized” label means operationally, and reconcile it with the 90% SIMBAD-unmatched statement. If “Uncategorized” is a classifier-internal bucket not tied to SIMBAD matching, rewrite the sentence accordingly and add the actual SIMBAD-match fraction within each class to avoid confusion.

P3-M6
- Section IV A (pages 8–9): The genuine novelty fraction for DESI top-1000 is given as 17.8% but without uncertainty.
- Problem: As a discovery-rate figure, a binomial confidence interval is needed to quantify precision.
- Required fix: Report the binomial 68% and 95% confidence intervals for the 178/1000 estimate, and make clear it applies only to the top-1000 stratum and is not an estimate for the full catalog.

P3-M7
- Figures/thresholds (multiple pages): The paper frequently uses “top-1%” selections for surveys like Gaia and NEOWISE as “predetermined-count selections.”
- Problem: Predetermined top-1% counts are not measurements of intrinsic anomaly frequency. While the authors do say this in Table I footnote, the main text occasionally treats these as anomaly rates.
- Required fix: Everywhere a “top-1%” count is presented, add an adjacent note “predetermined count; not an intrinsic rate,” or move all such counts into a single table clearly labeled as predetermined.

MINOR items (address but paper can proceed)

P3-m1
- Section II D final paragraph (page 4): “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”
- Problem: Duplicate phrase.
- Required fix: Remove the duplicate parenthetical.

P3-m2
- Figure 2 right panel/caption (page 5): “S up to 1.9×10^11.”
- Problem: Extremely large standardized score values invite questions about numerical stability and scaling under cross-transfer. You flag this as an artifact, which is good; however, the magnitude suggests the need to note numeric precision handling (e.g., float64, any clipping/robust scaling).
- Required fix: Add one sentence describing numeric precision used and any safeguards against overflow/underflow.

P3-m3
- Section III C (page 6): “UMAP/HDBSCAN clustering of the top-50,000 cross-transfer anomalies …”
- Problem: Why top-50,000 and not all 77,905? Is the selection random or score-ranked? Potential selection bias in the embedding.
- Required fix: State selection criteria (random vs score-ranked) and justify the subsample size.

P3-m4
- Section III C (page 6): State the SDSS-native re-score rates explicitly for the thresholds you use (S ≥ 0.1060 and S ≥ 0.2051) to make rates traceable without back-calculation.

P3-m5
- Section IV A (pages 8–9): The “100% archival-ID rate” on 20-object samples is a very small-N claim. It is acceptable as an illustration but should be labeled as such.
- Required fix: Add an explicit “small-N illustration” caveat with an exact binomial CI for 20/20.

P3-m6
- Section IV C (page 10): 5″ matching radius justification is reasonable but would benefit from one table listing per-survey positional precision and PSF sizes to substantiate the chosen compromise.

P3-m7
- Data/code citations: Provide exact commit hashes/tags for the GitHub repository and exact dataset version identifiers/DOIs for the HuggingFace artifacts.

P3-m8
- Conclusions (page 14): Where you present the total 378,280, immediately reiterate the point-source vs map-patch stratification to avoid downstream misuse.

NITs (cosmetic)

P3-n1
- Title block (page 1): “(Dated: June 2026)” PRD typically does not require a dated line; check journal style.

P3-n2
- Hyphenation and en-dashes are inconsistent (e.g., “cross-transfer,” “cross-transfer”). Apply consistent hyphen/dash style.

P3-n3
- References: Note [33] contains a parenthetical explaining the bibkey; ensure final bibliography conforms to PRD style without internal notes.

P3-n4
- Remove repeated uses of “headline” and “headline finding” where unnecessary; they distract from the core results.

Arithmetic and internal consistency spot-checks (selected)
- DESI anomaly rate: 195,829/22,504,897 = 0.870% (as stated).
- Multi-band breakdown summation (Table VI): 151,244 + 44,436 + 34 + 19 + 96 = 195,829 (consistent).
- LAMOST cross-transfer vs native S>5 compression: 44,075/2,054 ≈ 21.46× (as stated “21.5×”).
- SDSS cross-transfer anomaly fraction: 77,905/2,304,830 = 3.38% (Table I).
- NEOWISE ecliptic mask: 419/436 = 96.1%; rejected 17/436 = 3.90%; two-cap area at 10° is 1 − cos(10°) = 1.52%; 3.90/1.52 ≈ 2.57× (as stated “2.6×”).
- Dedup compression: 10,213/388,493 = 2.63% (as stated).
- Genuine novelty fraction: 178/1000 = 17.8% (needs CI; see P3-M6).
- Bias result: αjk = 0.19 ± 0.65 ⇒ 0.29σ from 0 (consistent with the text).
- Correct Fisher with F0 = 1/8.98^2 and c = 0.0747 yields σ = 8.14 for α = 0.19 and the advertised envelope [3.92, 8.98].
- NANOGrav γ: (3.0 − 2.567)/0.382 = 1.13σ; (4.33 − 2.567)/0.382 = 4.61σ (as stated).
- SIMBAD false-match expectation at 5″: n = 3.0×10^-5 arcsec^-2, area = π(5″)^2 ≈ 78.54 arcsec^2 ⇒ Pfalse ≈ 2.36×10^-3; expected ≈ 195,829 × 2.36×10^-3 ≈ 462 (as stated).

Length
At 20 pages, the paper is long but defensible given the multi-survey scope. If the authors can consolidate threshold disclosures and move lengthy footnotes into an appendix, the main text could likely be reduced by 2–3 pages without loss.

## Summary recommendation
MAJOR REVISIONS

The work is ambitious and many computations are consistent, but there are several critical methodological and internal-consistency issues that must be corrected for PRD. Chief among them are the dimensional/numerical error in the Fisher forecast (F0), the inconsistent and incorrect “top-1%” SDSS threshold labeling, the conflicting definition of the “catalog-grade” subset, the ad-hoc gating thresholds without prior justification or sensitivity analysis, and contradictory data-availability statements. Addressing the ESSENTIAL and MAJOR items above will substantially improve methodological rigor and clarity to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL (must fix)

P3-E8
- Inconsistency between main-text Fisher “positivity” form and Appendix C linear scaling.
- Main text adopts 1/σ(fNL)^2 = F0 + c α^2 (positivity-respecting). Appendix C then states σ(fNL) “varies linearly with α” and Table VII is derived by “linear scaling” from α = 0.15.
- Numerical conflict: with F0 = 1/8.98^2 ≈ 0.0124 and c = 0.0747, α = 0.30 gives σ = 7.24 (quadratic) versus Table VII’s 7.88 (linear). For α = 0.05 the quadratic gives σ ≈ 8.91 (≈0.8% improvement), Table VII says 8.80 (2.0%).
- Required fix: Use one consistent (α^2) form everywhere, recompute Table VII and any text that quotes the linear scaling.

P3-E9
- Notation collision for S on the eROSITA axis.
- Table I footnote (eROSITA) says “equivalent to S > 0.259 on the eROSITA-native IsolationForest raw-score axis,” reusing S for an IF raw score. Elsewhere S is explicitly the BigAE z-scored reconstruction residual.
- Required fix: Reserve S for the canonical BigAE z-score only; use a distinct symbol for the IF raw isolation score. If the eROSITA published 298-source cut is on IF raw, say so unambiguously and remove S from that clause. If it is on SBigAE, provide the correct SBigAE threshold. As written, dimensions/units are conflated.

MAJOR (significant revisions)

P3-M8
- Contradictory archival cross-match claims for DESI top anomalies.
- Section III A: “Cross-matching the top 10,000 [DESI] anomalies against six databases… none of the top 100 appear in any database.” Section IV A: a 20-catalog CDS X-Match for the DESI top-1,000 yields 82.2% archival IDs. Given that the “six databases” listed include SDSS and AllWISE, “none of the top 100” having any catalog entry is implausible and conflicts with the 82.2% result at larger N.
- Required fix: Define the six-database match exactly (catalog list, radius, required fields) and the criterion for a “hit.” Recompute the top-100 statement; if it was “no SIMBAD entries” (or “no spectroscopic classifications”), say that explicitly and remove “none… in any database.” Provide the per-catalog hit rates for the top-100 to reconcile with the top-1,000 multi-catalog result.

P3-M9
- Planck CMB “score range [0.558, 0.621]” uses units inconsistent with the canonical S definition.
- Earlier, “S” is the per-survey standardized residual; top anomalies elsewhere have S ≥ 5 (DESI) or percentile equivalents. The Planck entry quotes a “score range [0.558, 0.621]” for the top-1%, which is not on the S scale and appears to be a raw MSE (or different detector output).
- Required fix: State explicitly which axis is used for Planck scoring (e.g., raw MSE) and do not label it S. If the top-1% Planck selection is defined on raw MSE, provide the mapping or z-scaling used for comparability, or clearly mark it non-comparable.

P3-M10
- Spatial correlation tests reported without controlling for heterogeneous angular selection functions.
- Section IV B reports combined-sample tests (e.g., Spearman r with Galactic latitude and Pearson r with Planck dust) and quotes p-values. With seven surveys’ strongly inhomogeneous and partially disjoint footprints, these p-values are not interpretable without modeling the joint selection function or restricting to common footprints.
- Required fix: Either (a) restrict the test to a well-defined common sky region with known completeness, or (b) emulate the survey footprints/selection in the null via random catalogs per survey and report significance against that null. Otherwise, qualify the current p-values as non-comparable and remove any inference based on them.

P3-M11
- Post-hoc count matching in SDSS “native re-score top-77,905 at S ≥ 0.1060.”
- Section III C says the native SDSS re-score “top-77,905… supersedes the cross-transfer count,” i.e., uses the same count as the cross-transfer anomalies, but at a completely different threshold and on a different scoring axis/domain. This looks like a posteriori count-matching.
- Required fix: Justify why 77,905 was chosen for the native slice beyond matching a previous count. Provide a sensitivity analysis showing that conclusions (class distributions, SIMBAD fractions, etc.) are robust to ±50% in the chosen count, or choose a principled threshold (e.g., top-1% or score-knee only) and stick to it.

MINOR (address but paper can proceed)

P3-m9
- Clarify DESI σval disclosure. Section II B: “σval is set such that the S > 5 threshold corresponds to MSE ≈ 0.143” reads as if σval were chosen to produce that mapping. It should be implied by the measured (µval, σval). Provide the actual σval numerical value used for DESI and reword to “implies MSE ≈ 0.143.”

P3-m10
- Unreferenced Jaccard number in Conclusions.
- Conclusions point 6 cites “OOD control-vs-control 0.874 (PASS)”; this value is not defined or derived earlier (Section II B reports production-vs-control Jaccard 0.732). Add the definition, dataset, seeds, and where that 0.874 comes from.

P3-m11
- Training-time units in Table V are not credible for Planck.
- Planck native convolutional AE “Train time (s) = 10.6” for 2×10^5 patches and a 1.1M-param CNN on A100 appears unrealistic by orders of magnitude. Clarify units (seconds vs minutes/hours), batch size, and number of epochs; if this is wall-clock for one epoch, say so.

P3-m12
- Figure 7 legend clarity.
- The use of “FAIL*” markers in the legend without a direct per-curve labeling of which gate is being assessed is confusing. Add a simple key indicating which specific gate each curve addresses (e.g., “cont.-dip gate,” “em.-line gate,” “mask gate”).

P3-m13
- Planck injection test definition.
- “500/500 = 100% injection-recovery at 5σ Gaussian-bump amplitude” does not define how σ is measured on a map patch. Specify σ (per-patch RMS after mask? global RMS?), bump width, and placement. This matters because your gate criterion (b) hinges on that definition.

P3-m14
- “AE” vs “rZ” label confusion in Figure 9 and Section III B.
- You note that panel labels show rZ but printed as “AE” for legacy compatibility. This is easy to misread as the global anomaly score S. Add an in-figure note or a one-line caption clarifier: “AE label denotes rZ, not S.”

COMPARABILITY/NULL PROCEDURE WARNINGS

P3-E10
- Mixed fNL baselines without clear comparability statements.
- Section V uses σstd = 8.98 (DESI single-tracer) as the reference; Appendix C Figure 8 shows a “single-tracer baseline = 16.85” and “baseline multi-tracer = 12.72” for the canonical 5-tracer configuration. These are different null procedures/data models, yet baseline labels are similar and can be misread as directly comparable.
- Required fix: Add explicit statements next to each σ baseline describing the tracer set, redshift binning, V(k) and kmax assumptions; avoid reusing “baseline” without qualifier. Where two σ values are juxtaposed, say “not directly comparable.”

FIGURE-CAPTION VS BODY CHECKS

P3-m15
- Figure 2 right panel caption states that the SDSS native re-score compresses extreme S values to < 14. The body text never presents the native S distribution to substantiate that cap. Add a reference figure or a table statistic (e.g., max S under native re-score) to back the caption.

ARITHMETIC/CROSS-REFERENCE SPOT CHECKS (new)

- No new arithmetic mismatches beyond those already flagged above; most sums and simple ratios remain consistent on this second pass. However, the DESI “top-100 have no database entries” (P3-M8) is numerically implausible given the later 82.2% archival-ID for the top-1,000 and must be reconciled as noted.

If the authors correct these additional issues (on top of those in the initial report), the paper’s methodological clarity and internal consistency will be substantially improved.
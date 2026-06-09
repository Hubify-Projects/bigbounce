# P3 R22prov — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7299 chars)
**Wall time**: 362.1s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog …” (22 pages)

Scope of review
I evaluated the statistical methodology, derivations, numerical consistency, and internal coherence across text, tables, and figures. I recomputed quoted ratios, percentages, and key σ values appearing in the abstract, body, figures, and tables. Page numbers below refer to the rendered PDF page numbers supplied with this submission.

Findings

ESSENTIAL

P3-E1 (Section V, p. 12; Table IV caveat (i), p. 15): Dimensional inconsistency in Fisher summary constant F0
- Problem: The text defines the “positivity-respecting” Fisher form as 1/σ(fNL)^2 = F0 + c α^2 and then states F0 = 1/8.982. This is dimensionally inconsistent. F0 must equal 1/σstd^2 = 1/(8.982)^2 ≈ 0.01239, not 1/8.982 ≈ 0.1113. The reported central result σ(fNL) = 8.14 happens to match the squared form (F0 = 1/8.982^2), but the printed definition is wrong in two places (main text and Table IV).
- Required fix: Correct F0 everywhere to F0 = 1/σstd^2 = 1/(8.982)^2. Re-audit all places where F0 is used or quoted (main text, caveats table, captions) and explicitly show the one-line computation yielding 8.14 from F0 = 0.01239, c = 0.0747, and α = 0.19. State clearly that the [3.92, 8.98] envelope comes from α ∈ [max(0, μ − σ), μ + σ] with the positivity floor at α = 0.

P3-E2 (Section III.H, p. 7; §II.D Step 4 p. 3; Fig. 5 caption p. 9): Factor-of-two error in NEOWISE polar-cap “uniform-null” comparison
- Problem: You remove 17/436 = 3.9% of NEOWISE anomalies inside the |becl| ≥ 80° ecliptic polar caps and claim “2.6× the uniform-null expectation (1.52%).” A 10°-radius spherical cap has fractional area (1 − cos 10°) ≈ 0.0152 per cap, but there are two caps; the combined area is ≈ 3.04%. Thus, the observed 3.9% is ≈ 1.28×, not 2.6×, the two-cap null.
- Required fix: Compare against the two-cap baseline (3.04%), update the enrichment factor to ≈ 1.28×, and adjust any related text (including §II.D step 4 and §III.H). If you intend a per-cap analysis, make that explicit and do not compare a two-cap fraction to a one-cap baseline.

P3-E3 (Table V, p. 17): Implausible training times (units likely incorrect) for Planck CMB convolutional autoencoder (and ACT cross-transfer row)
- Problem: Table V lists a 1.1M-parameter Planck CAE trained on 2×10^5 patches with a training time of 10.6 s. This is off by orders of magnitude (even a single epoch over 2×10^5 64×64 patches on an A100 cannot complete in ~10 seconds). The ACT cross-transfer row also shows a 7.0 s training time. These numbers render the pipeline timing audit non-credible.
- Required fix: Recompute and report realistic wall-clock training times with units, epoch counts, and dataset sizes (number of batches, epochs, batch size). If the numbers were meant to be minutes, hours, or per-epoch, label them correctly. If they are placeholders, remove them and replace with measured timings.

P3-E4 (Section III.A, p. 4): Contradictory database cross-match statement for DESI top anomalies
- Problem: “Cross-matching the top 10,000 anomalies against six databases (SIMBAD, NED, AllWISE, Milliquas, Gaia DR3, SDSS) finds only 0.2% in SIMBAD and 12.7% in NED; none of the top 100 appear in any database.” Given the listed six databases include dense photometric catalogs (Gaia, AllWISE) and SDSS, “none of the top 100 in any database” is highly implausible and contradicts the later Section IV.A extended cross-match result (82.2% archival identifications on the DESI top-1,000).
- Required fix: Precisely define “appear in any database” (named objects only? spectroscopic catalogs only? what matching radius?) and provide the per-database counts for the top-100 and top-10,000 subsets. If the intent was “none in SIMBAD or NED,” say so unambiguously and do not list Gaia/AllWISE/SDSS in that sentence. Ensure consistency with the Section IV.A 82.2% archival-ID result.

P3-E5 (Data availability statement, p. 16): Data not publicly accessible at submission
- Problem: “HuggingFace … private pending arXiv acceptance; public upon acceptance.” PRD requires that data and code necessary to validate the results be accessible at submission or that a clear plan with a DOI be provided.
- Required fix: Make the catalog and code public with a stable DOI (Zenodo, institutional repository) at submission, or provide a compelling justification acceptable to PRD along with an access mechanism for referees and readers. Replace “pending acceptance” language with a permanent, citable URL/DOI.

P3-E6 (Table I, p. 8): Mixing ACT-included “Total (cross-transfer)” with ACT-excluded per-survey block is confusing and risks misinterpretation
- Problem: The table’s per-survey block excludes ACT, but the “Total (cross-transfer, ACT-incl.)” row includes ACT (+200). This requires reading long footnotes to reconcile the 200-object discrepancy and can easily mislead readers into double-counting or misunderstanding what is in-scope.
- Required fix: Split the totals cleanly: (i) a cross-transfer total excluding ACT (319,243), (ii) a line explicitly labeled “+ ACT DR6 cross-transfer patches (quarantined): +200,” and (iii) a grand-total-with-ACT line if you must retain it as a diagnostic. Better yet, move all ACT numbers to Appendix F only, and keep the main table self-consistent (ACT-free).

MAJOR

P3-M1 (Section IV.A, p. 8–10; Fig. 6 caption p. 10): “Aggregate 58.8% SIMBAD-unmatched” lacks weighting method and denominator clarity
- Problem: It is unclear whether 58.8% is (a) a simple average of per-survey unmatched fractions, (b) weighted by anomaly counts, or (c) weighted by sky coverage. The sample used (e.g., SDSS “continuity slice” vs. “S > 5” strict set) also affects this figure.
- Required fix: State precisely how 58.8% is computed, list the per-survey numerators/denominators used, and provide the weighted/unweighted value(s). If multiple SDSS/LAMOST thresholds exist, state which pool was used for this aggregate.

P3-M2 (Section IV.D, p. 11): Planck × ACT “null result” lacks statistic, uncertainties, and quantitative significance
- Problem: The text asserts a null cross-correlation without specifying the estimator (e.g., Landy–Szalay between patch-centers, HEALPix cross-power), the random catalog construction, or the uncertainty estimate. No p-value or σ-equivalent is given for the observed null.
- Required fix: Specify the cross-correlation estimator, the binning, the random-trial methodology, and report the uncertainty band (jackknife or bootstrap). Quote a quantitative consistency-with-null measure (e.g., χ^2/dof with p-value). Otherwise, move this to a qualitative remark.

P3-M3 (Section V, p. 12; Fig. 9 caption p. 13; Appendix C, p. 17–18): Keep fixed-α and empirical-α forecasts strictly segregated at every juxtaposition
- Problem: You correctly caution that Fig. 9 is the fixed-α reference and that the main result uses empirical αjk, but both appear in Section V and the caption without an explicit “not directly comparable” tag where the numbers (8.43 vs. 8.14) are shown.
- Required fix: Add an explicit sentence wherever both appear side-by-side: “The fixed-α and empirical-α forecasts are not directly comparable; they use different α assumptions and covariance structures.” Retain the warning in the caption and in the main text at first juxtaposition.

P3-M4 (Section II.D, p. 3–4; Figure 10 p. 15): Injection–recovery details insufficient for reproducibility
- Problem: The paper reports 3 PASS / 3 FAIL-at-5σ, but the exact plant morphology for each survey, noise model, S/N computation, and detection criterion are not fully specified in the text (e.g., continuum-dip profile, line widths/amplitudes for spectroscopic surveys, variability-axis injection for Gaia).
- Required fix: Provide a concise per-survey paragraph (or a compact table in the appendix) enumerating: plant function, amplitude definition, noise model, per-survey detection threshold, and recovery counting rule. Cite the exact files/scripts in the repository and include one illustrative example per survey in the paper.

P3-M5 (Sections II.B and III.A, p. 3–5): Training-sample leakage and in-sample scoring
- Problem: DESI scores are computed on a catalog that includes the 47k training spectra. While you provide a 5-fold Jaccard PASS and an OOD holdout PASS, the main rate (0.87%) still pools in-sample and out-of-sample.
- Required fix: Add a line reporting the anomaly rate on the DESI pool with the 47k training objects removed (or on the OOD-only pool), and show that the rate and tail statistics do not materially change. If they do, quantify the impact.

P3-M6 (Section IV.C, p. 10–11): 5″ fixed-radius deduplication across heterogeneous astrometry
- Problem: The text acknowledges the heterogeneity and states the 5″ choice is a “conservative compromise.” However, no sensitivity sweep is shown.
- Required fix: Provide a small sensitivity analysis in the appendix (e.g., counts at 3″, 5″, 7″; change in multi-survey cluster count and total compression). Even a paragraph with the numbers suffices.

P3-M7 (Section III.H, Fig. 5 p. 9): NEOWISE anomaly score definition
- Problem: The NEOWISE selection is “top-1%,” yet Fig. 5 quotes a “Score = 11.5” and the text calls it “canonical-S.” It’s unclear whether S is used only for ranking or also for mask evaluation.
- Required fix: State explicitly that NEOWISE uses the same canonical-S score (Eq. 2) for ranking but a top-1% cut for selection; clarify that the reported S = 11.5 is the canonical score.

MINOR

P3-m1 (Section II.D, p. 4): Duplicated phrase
- Problem: “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”
- Required fix: Remove duplication; keep a single, precise statement.

P3-m2 (Section III.A, p. 4): Claimed “0% artifact rate in top 200” lacks a method
- Problem: “Spectral inspection of the top 200 confirms a 0% artifact rate.” What is the artifact definition and who inspected (single reviewer vs. blinded multi-rater)?
- Required fix: Add one sentence specifying the inspection protocol (criteria, number of raters) or soften the claim (e.g., “no artifacts found on visual inspection”).

P3-m3 (Fig. 3, p. 6): Extremely large S range in SDSS cross-transfer panel
- Problem: S spans to ~10^11. While this is discussed as an artifact of cross-transfer, the axis could mislead.
- Required fix: Add a brief note in the caption that the dynamic range is a cross-transfer artifact due to the DESI-trained scale applied to out-of-distribution SDSS spectra, and that the native re-score compresses S < 14.

P3-m4 (Fig. 6, p. 10): Clarify that SIMBAD-unmatched is not a novelty fraction
- Problem: Although the text emphasizes this, add the key sentence in the caption as well.
- Required fix: Append: “This is a database-coverage diagnostic; it is not a catalog novelty fraction.”

P3-m5 (Section III.E, p. 6–7): “Novel” label in Table III needs explicit definition here
- Problem: Table III marks SIMBAD status “Novel,” which readers may misinterpret as “novel across all archives.”
- Required fix: Include a note under the table: “Novel here means no SIMBAD counterpart within 5″; it is not an all-archives novelty claim.”

P3-m6 (Section IV.B, p. 10): χ^2 uniformity comment
- Problem: You correctly say the χ^2 is dominated by footprint inhomogeneity. Strengthen the caution.
- Required fix: Add: “We do not interpret χ^2_ν > 1 as evidence for astrophysical clustering; selection-function modeling would be required.”

P3-m7 (Appendix E, p. 18): Posterior summary notation
- Problem: You present both “mean ± sample std-dev” and central 68% credible interval numbers; make clear which error bar is used for the σ-shift calculation.
- Required fix: Add “The ±0.382 is the sample standard deviation of γ used to compute σ-shifts; the asymmetric 68% CI is reported for completeness.”

P3-m8 (Bibliography): Reference [33] label notes “publication-year 2024; bibkey retained as Heinrich2023”
- Problem: This is internal bookkeeping; it belongs in BibTeX comments, not in the bibliography text.
- Required fix: Remove bracketed note from the references section.

NIT

P3-n1: Hyphenation artifacts (e.g., con- / –) are visible in several places. Clean final typesetting.
P3-n2: Capitalization of “Path-C” protocol varies slightly; standardize.
P3-n3: “quasi-matter bounce” vs. “matter-bounce” usage; choose one consistent term where appropriate for the class considered (w = 0).

Length
The manuscript is long (22 pages) but methods-heavy. With the fixes above, the length is acceptable for PRD. If a reduction is required, I suggest moving the descriptive taxonomy galleries and some table footnotes into appendices.

Audit of abstract and conclusion scalars
- 37.3M processed, 378,280 unique (378,080 point-source + 200 Planck) — consistent with Table I and §II.D dedup math.
- DESI anomalies 195,829/22.5049M = 0.87% — consistent.
- “∼141×” vs Liang et al. (2,685): 378,080 / 2,685 ≈ 141 — consistent.
- “∼73× like-for-like” for DESI-only: 195,829 / 2,685 ≈ 72.9 — consistent.
- LAMOST 21.5× compression (44,075 → 2,054 S>5) — consistent.
- SDSS ~6500× compression (77,905 cross-transfer vs. 12 at S>5 native) — consistent.
- DESI 5-fold Jaccard 0.862 — consistent with §II.B.
- Injection-recovery PASS/FAILs and percentages — consistent with Fig. 10 and text.
- Landy–Szalay αjk = 0.19 ± 0.65 and Fisher result σ(fNL) = 8.14 with [3.92, 8.98] — numerically consistent only if F0 = 1/8.982^2; fix required per P3-E1.
- NANOGrav γ = 2.567 ± 0.382; Δγ/σ = (3.0 − 2.567)/0.382 = 1.13; (4.33 − 2.567)/0.382 = 4.61 — consistent. Bayes factor ratio 3.23 / 4.52e−4 ≈ 7.14×10^3 — consistent.

## Summary recommendation
MAJOR REVISIONS

The paper contains substantial and promising methodology, but there are critical issues that must be corrected before it can meet PRD standards: a dimensional error in the Fisher constant F0 (though numerically used correctly), a factor-of-two statistical mistake in the NEOWISE polar-cap enrichment, implausible training-time reporting (undermining reproducibility), contradictory database cross-match language that affects novelty claims, and a confusing presentation of ACT-inclusive totals in the main table. Additional clarifications are needed on the aggregate SIMBAD fraction, Planck×ACT null quantification, injection–recovery specifications, and data availability. Addressing the ESSENTIAL and MAJOR items above will materially improve rigor and clarity.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

ESSENTIAL

P3-E7 (Fig. 12, p. 19 vs. text §III.B): Implausible “AE” values plotted for DESI anomalies
- Problem: Fig. 12 labels for DESI DR1 objects show AE values up to 83,518 and 17,663, but the paper states DESI canonical S spans 5–25.2 and that the panel’s “AE” tag stands for a per-arm sub-score (rZ) with mean ≈ 3.9 for the high‑z set (§III.B). Values O(10^4–10^5) cannot be DESI S or rZ.
- Required fix: Correct the figure labels to the stated quantity (rZ or S) on the DESI-native scale, or relabel explicitly as “cross-transfer S (DESI-trained scale on SDSS)” if that is what was plotted. As-is the figure contradicts the stated DESI score ranges and misleads readers.

P3-E8 (SDSS “top-1%” misuse; §III.C p. 5; Table I footnote ♡ p. 8): 77,905 is not 1%
- Problem: Multiple places call the 77,905-object SDSS slice “top-1%.” 1% of 1,925,279 is 19,253; of 2,304,830 it is 23,048. 77,905 corresponds to ≈4.0% of 1.93M (or 3.38% of 2.30M).
- Required fix: Remove every “top-1%” label tied to 77,905; define it as a “continuity slice equal in size to the cross-transfer set.” Keep the true top‑1% native value (19,253) separate and consistently named.

P3-E9 (§IV.C, p. 11): Unsupported “≤ 0.1%” robustness claim for dedup radius
- Problem: You state the 378,280 unique-object count is robust to radius refinements at ≲0.1%. The only bound demonstrated is the hard ceiling from current compression: 10,213/388,493 ≈ 2.63%. No evidence is shown for ≤0.1%.
- Required fix: Either provide the requested 3″/5″/7″ sensitivity numbers (already requested in P3-M6) and demonstrate the ≤0.1% change, or soften to “few‑percent” and remove the 0.1% figure.

P3-E10 (§II.D Step 1 vs. §II.B/§III.A): Inconsistent training-pool size claim
- Problem: Step 1 states native retrains use 2–5×10^5 spectra per survey. DESI’s native model is trained on 47,000 spectra—well below that range.
- Required fix: Amend Step 1 to reflect the actual per-survey choices (e.g., “O(5×10^4) for DESI; 2–5×10^5 for others”), or report the true DESI pool that satisfies the stated range.

P3-E11 (Table I footnote ∥, p. 8): Ambiguity/misleading wording about ACT subtraction
- Problem: The footnote says “excluding ACT subtracts exactly 200 from both the input sum and the unique-object count.” For Ntotal (processed items), excluding ACT subtracts 20,000, not 200. “Input sum” is undefined and invites confusion with Ntotal.
- Required fix: Rewrite precisely: “Excluding ACT removes 20,000 patches from Ntotal processed and 200 anomalies from the pre-dedup sum; ACT contributes 0 to the unique-object count due to 0 overlaps.”

MAJOR

P3-M8 (Cross-method comparability of “PASS/FAIL” gates; §II.D p. 3–4; Fig. 10 p. 15): Heterogeneous null procedures pooled into one scoreboard
- Problem: The six PASS/FAIL claims mix fundamentally different tests: spectral Gaussian-bump vs. continuum-dip vs. emission-line plants, a variability-axis injection for Gaia, and a geometry-based “mask injection” for NEOWISE. Pooling them in a single PASS/FAIL chart implies comparability that is not established.
- Required fix: Add a paragraph explicitly stating these gates are method-specific and not directly comparable; provide per-survey rationale for why each test probes sensitivity to the catalog’s target anomalies. Consider renaming “PASS/FAIL” to “criterion met/not met for this test.”

P3-M9 (Fig. 4 vs. §III.C p. 7): 3 populations vs. 14 HDBSCAN clusters mismatch
- Problem: The text says UMAP/HDBSCAN “yields 3 latent-space populations,” while Fig. 4 shows 14 HDBSCAN clusters (and “59.4% clustered”). Readers cannot reconcile “3 populations” with “14 clusters.”
- Required fix: Clarify that 14 HDBSCAN clusters were grouped into 3 physical categories (cool dwarfs, high‑z candidates, blue‑excess QSOs), and show the mapping or a confusion matrix.

P3-M10 (§III.C p. 5): Unexplained drop from 2,304,830 to 1,925,279 spectra in SDSS native re-score
- Problem: The native re-score uses 1,925,279 DR18 spectra versus 2,304,830 available. The exclusion criteria are not stated.
- Required fix: State and justify the quality cuts (e.g., S/N, flagged plates/fibers), and give numerators/denominators so the reader can reproduce the 1.925M pool.

P3-M11 (Fig. 8 p. 12 vs. §III.C): Ambiguous SDSS score axis in the DESI×SDSS spectral pair
- Problem: Panel (d) shows SDSS “Score = 49.5,” but §III.C asserts the SDSS native re-score compresses cross-transfer extremes to S < 14. The panel must therefore be a cross-transfer (DESI-trained) score, not native.
- Required fix: Label explicitly whether panel (d) uses the DESI-trained cross-transfer S or the SDSS-native S. If cross-transfer, add the clarifying sentence to the caption/body.

P3-M12 (Catalog-grade tier composition; Abstract p. 1 vs. Table I footnote ♠ p. 8): Whether Planck patches are included is inconsistent
- Problem: The abstract’s “catalog-grade subset” lists only point-source surveys (DESI + SDSS + eROSITA + Gaia + NEOWISE; excludes LAMOST), implying exclusion of Planck. Footnote ♠ counts “Planck native” within the catalog-grade tier of 264,938.
- Required fix: State unambiguously whether Planck CMB patches are in or out of the “catalog-grade subset” used for object-level analyses; keep that definition consistent across abstract, body, and footnotes.

MINOR

P3-m9 (Table V, p. 17): Training-time units and definitions missing for all rows
- Problem: Beyond the implausible CAE times (already flagged), all training-time entries lack units and whether they represent wall-clock per epoch or total.
- Required fix: Add explicit units, batch sizes, epochs, and dataset sizes for each row.

P3-m10 (Appendix D, p. 17): Incomplete UMAP stability specification
- Problem: “Trustworthiness 0.9797 ± 5×10−5” is reported without the neighborhood parameter k.
- Required fix: Report k used for trustworthiness, plus the UMAP hyperparameters here (currently only in prose earlier).

P3-m11 (§III.F, p. 6): Planck anomaly “score range [0.558, 0.621]” needs axis definition
- Problem: It is not stated whether this is canonical S, a CAE reconstruction MSE, or another normalized score.
- Required fix: Name the score explicitly and how it relates to Eq. (2) (or note that the CMB CAE uses a different normalization).

P3-m12 (§II.D Step 6, p. 4; §IV.D, p. 11): “Zero overlaps with ACT” claim should cite the actual 8-way run
- Problem: You assert zero overlaps for ACT vs. others while ACT is excluded from the canonical 7-way dedup. Readers cannot verify without the 8-way numbers.
- Required fix: Add a sentence with the 8-way-with-ACT dedup counts (pre/post) and confirm 0 overlaps numerically.

NIT

P3-n4 (§II.B, p. 3): Wording “on the rescaled scale” is awkward; suggest “on this score’s scale.”
P3-n5 (§III.E, p. 6): “eastern half under Rosatom proprietary control” is informal; use neutral phrasing about data-rights period for the Russian consortium.
P3-n6 (Appendix E, p. 18): “Ceffyl” capitalization varies; standardize to “ceffyl.”

Explanation
This second pass focused on arithmetic consistency, caption–body alignment, equation dimensionality, cross-references, and comparability of null procedures. The items above are new relative to the first review and materially improve clarity and reproducibility if addressed.
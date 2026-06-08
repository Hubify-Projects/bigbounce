# P3 auto-2026-06-08_1520pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8669 chars)
**Wall time**: 393.8s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies ...” (20 pages)

Scope of review
I evaluated the paper for methodological rigor with focus on statistical validity, derivation chains, dimensional consistency, internal arithmetic, uncertainty propagation, significance claims, and consistency between abstract/conclusions and body. I audited all load-bearing numbers that can be recomputed from the text, figures, and tables.

Findings

ESSENTIAL

P3-E1 (Section V, pp. 10–11; also Table IV caveat (i), p. 13; Abstract, p. 1)
Problem: Dimensional inconsistency and misdefinition of F0 in the Fisher “positivity-respecting” relation. The paper adopts 1/σ(fNL)^2 = F0 + c α^2 but then sets F0 = 1/8.982 (text on p. 11 and p. 13), while σstd = 8.98 is the single-tracer baseline. To make σ(α=0) = σstd, one must have F0 = 1/σstd^2 = 1/8.982^2 ≈ 0.01239, not 1/8.982 ≈ 0.1113. The reported central forecast σ(fNL) = 8.14 and the “1σ envelope” [3.92, 8.98] do numerically match the corrected F0 = 1/8.982^2, but the text and table explicitly state F0 = 1/8.982, which is dimensionally wrong and would give σ ≈ 2.96 for α = 0.19.
Required fix: Correct F0 everywhere to F0 = 1/σstd^2 = 1/8.982^2. Recompute and restate all dependent quantities, including the central “% improvement” and any confidence envelopes. Ensure the abstract, body text (Sec. V), Table IV (item (i)), and Appendix C are consistent.

P3-E2 (Table I caption and footnote ♡, p. 7; Section III C, p. 5)
Problem: SDSS “top-1%” inconsistency and count mismatch. The paper repeatedly refers to a “top-1%” SDSS DR18 anomaly slice of 77,905 objects (e.g., Table I caption: “S ≥ 0.1060 for SDSS top-1%”). However, the SDSS native re-score sample is 1,925,279 spectra (Sec. III C), and 1% of this is 19,253, not 77,905. Indeed, the same footnote ♡ admits “the same 1,925,279-spectrum DR18 sample yields 19,253 anomalies at the harder top-1% score-knee cut S ≥ 0.2051,” directly contradicting the “top-1%” label for 77,905. 77,905/1,925,279 = 4.05% (not 1%). The text in Sec. III C also states “the top-77,905 native slice at S ≥ 0.1060 supersedes the cross-transfer count,” which preserves the count rather than adhering to any top-1% criterion.
Required fix: Remove all incorrect “top-1%” language for the 77,905 SDSS count. Either (a) use the correct top-1% count (19,253) throughout and recompute all roll-ups, dedup statistics, and totals; or (b) if you intentionally preserve a larger “continuity slice,” label it accurately with its quantile (≈ top-4.05%) and clearly separate it from any true 1% slice. All downstream totals (e.g., the 388,493 survey-level sum, the 378,280 unique count after dedup) must be recomputed or explicitly justified as independent of this correction. As written, this is a major internal inconsistency.

P3-E3 (Abstract p. 1; Section IV D, p. 10; Appendix F, pp. 18–19)
Problem: Using a quarantined, gate-failing ACT DR6 cross-transfer set to support a substantive cross-correlation conclusion in the main text. Sec. IV D states as a “null result” that “Planck and ACT anomalies do not cluster at the same sky positions,” and interprets this as evidence that “CMB patch anomalies … are dominated by survey-specific systematics.” However, Appendix F explicitly explains that the ACT cross-transfer model fails both validation gates (val MSE ~ 2.2×10^4 and <1% injection-recovery at 5σ) and no native retrain was executed; ACT is “not a science result.” Yet the main text still draws a scientific conclusion from Planck×ACT using this invalid set.
Required fix: Remove the Planck×ACT cross-correlation result from the main text, or move it to Appendix F with an explicit statement that no scientific inference should be drawn from it. Do not claim any methodological or physical conclusion in the main body based on quarantined data.

P3-E4 (Data availability statement, p. 14)
Problem: Data/code availability does not meet PRD transparency standards. The catalog is “deposited on HuggingFace … private pending arXiv acceptance; public upon acceptance.” This is not sufficient for peer review or eventual replication. PRD requires durable, public availability upon publication (and access for referees during review).
Required fix: Provide a public, citable, versioned DOI (e.g., Zenodo) for the datasets and code at submission or, at minimum, for the revised resubmission. Remove “private pending …” language and replace with persistent DOIs and commit hashes. Ensure all results in the paper are reproducible from the posted artifacts.

P3-E5 (Abstract p. 1 and Section headers II, III, V, XII multiple locations)
Problem: Multiple “σ” conventions are juxtaposed without explicit “not directly comparable” caveats at the point of juxtaposition. The abstract alone lists: “5σ” injection amplitudes (noise-level units), “<1σ from null” for a jackknife bias estimator, and “+1.13σ” parameter shifts in a posterior for NANOGrav—all adjacent with no explicit statement that these sigmas are not comparable. The body provides some local clarifications (e.g., non-Gaussian posterior widths in Sec. V A), but there is no global warning and not every juxtaposition is qualified.
Required fix: Add an explicit, early “Sigma conventions” paragraph (e.g., end of Sec. I or start of Sec. II) stating that the paper uses several distinct σ definitions (injection amplitude in noise units; frequentist estimator dispersion; posterior standard deviation or credible widths), which are not commensurate, and that any comparison across them is invalid. In the abstract and at every place where differing σ notions appear together, insert a brief “not directly comparable” qualifier.

P3-E6 (Abstract p. 1; Sec. V, p. 11; Appendix C, p. 15)
Problem: Inconsistent “% improvement” for σ(fNL). With corrected F0, αjk = 0.19 gives σ = 8.14. Relative to σstd = 8.98, the improvement is (8.98 − 8.14)/8.98 = 9.36%, not 7.9% as stated in the abstract and Sec. V. It appears 7.9% was obtained from a linearized scaling around α = 0 (6.1% at α = 0.15 extrapolated to 0.19), which contradicts using the positivity-respecting form to compute σ = 8.14.
Required fix: Recompute and report a single consistent improvement percentage from the same chosen formula (preferably the corrected positivity-respecting formula with F0 = 1/σstd^2). Update the abstract and Sec. V text accordingly.

MAJOR

P3-M1 (Section III H and Fig. 7 caption; pp. 8 and 13)
Problem: Treating a geometrical mask “injection-recovery” at 100% as a gate PASS on par with signal-detection gates. The NEOWISE “ecliptic-pole mask” test is a diagnostic of scan-pattern contamination removal, not a recovery of planted signals. Reporting “1000/1000 = 100% (gate PASS)” next to true detection-recovery curves is potentially misleading.
Required fix: Separate the NEOWISE mask diagnostic from signal injection-recovery tests. Do not count it toward the “3 PASS” tally unless a true signal-plant recovery is performed. Clarify in text and in Fig. 7 caption.

P3-M2 (Section IV A, pp. 8–9; Fig. 5)
Problem: The aggregate SIMBAD-unmatched fraction of 58.8% is reported without a transparent weighting scheme. It is unclear whether the fraction is anomaly-count-weighted across surveys, and whether surveys with predetermined 1% anomaly quotas (Gaia, NEOWISE, Planck) are included appropriately. The statement “aggregate 58.8%” cannot be independently recomputed from the paper as-is.
Required fix: Specify the exact computation: per-survey numerator/denominator, weighting (by anomaly counts), and which surveys are included (exclude Planck sky patches; include only coordinate-matchable anomalies). Provide the per-survey counts used to construct Fig. 5 and the aggregate.

P3-M3 (Section IV C, pp. 9–10)
Problem: “Expected random coincidence” estimates for 7-way 5″ dedup (≲ 10) are stated without derivation. Given heterogeneous astrometry and PSFs (Gaia to NEOWISE), the calculation depends on surface densities per catalog and matching radii.
Required fix: Provide the calculation (or a table) showing survey surface densities, effective matching radii per pair (or justify uniform 5″), and the resulting expected random overlaps. Alternatively, move the claim to an appendix with the derivation.

P3-M4 (Section V, p. 11 and Appendix C, p. 15)
Problem: Presentation of the “Gold+Silver” restricted result yields a central σ(fNL) = 1.95 with a huge ± envelope under caveat (j). This headline-worthy central value is not robust and is immediately walked back, but it risks overemphasis.
Required fix: Move the Gold+Silver αGS and σ(fNL)GS result to an appendix, or present it only with a prominent cautionary box stating explicitly that it is not a validated forecast and should not be used in any summary. Remove it from the main flow.

P3-M5 (Section V A, p. 12; Appendix E, pp. 15–16)
Problem: NANOGrav spectral-index analysis lacks a clear prior specification for the Bayes factors and does not report numerical uncertainty on BMB/SMBHB. While the parameter-shift σ computations are fine, the Savage–Dickey Bayes factors need explicit priors and numerical integration tolerances; only the prior range (γ ∈ [0, 7]) is stated.
Required fix: State the exact priors used for the point nulls (γ = 3.0 and γ = 4.33) in the Savage–Dickey ratio, the kernel bandwidths in the KDE posterior density at the point null, and provide an uncertainty estimate (e.g., via bootstrap over the chain or KDE bandwidth variation). Cite or deposit the code used for the Bayes-factor computation.

MINOR

P3-n1 (Section II D, p. 4)
Problem: Duplicate phrasing. “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”
Required fix: Remove the duplicated parenthetical clause.

P3-n2 (Section III A, p. 4)
Problem: The “galaxies flagged at ∼20× the QSO rate (0.75% vs. 0.037%)” appears twice in similar form in the same subsection.
Required fix: Consolidate to a single, clearly stated comparison once.

P3-n3 (Table I caption, p. 7)
Problem: Overloaded footnote symbols (‡, §, ⋆, ♡, ♠) with very long prose make this table difficult to audit. Some of the prose contradicts main-text phrasing (see ESSENTIAL P3-E2).
Required fix: Condense and align the footnotes with the corrected main text. Move detailed methodological caveats to an appendix and keep the table footnotes concise.

P3-n4 (Section I, Abstract phrasing, p. 1)
Problem: “The catalog, model weights, and reproducibility scripts are publicly released.” Conflicts with “private pending arXiv acceptance” later (p. 14).
Required fix: Harmonize the statements per P3-E4.

P3-n5 (Figure 2 right, p. 5)
Problem: Axis label for “Probability density” on a log–log plot of S that spans 1e2–1e11 is shown but it’s unclear whether the y-axis is a PDF estimate or a normalized histogram density. 
Required fix: Specify in the caption whether the curves are kernel density estimates, normalized histograms, or something else, and note any bandwidth/normalization used.

NIT

P3-N1 (Stylistic, multiple pages)
Problem: Frequent use of internal process terms (“Path-C rebuild,” “quarantined,” “checksum 1812395110,” “seed 20,260,501,” “private pending arXiv acceptance”) reads like an internal engineering log rather than a PRD article.
Required fix: Retain only what is necessary for reproducibility (e.g., random seeds are fine), but remove process language that does not serve the scientific narrative.

P3-N2 (Bibliography, p. 19)
Problem: Ref. [33] has “publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity” inside the citation text.
Required fix: Clean to standard PRD citation format without process commentary.

P3-N3 (Units and symbols, multiple)
Problem: Mixed arcsecond formatting (5′′) and ASCII quotes; occasional typographical dashes.
Required fix: Standardize arcsecond/arcminute notation and dashes to PRD style.

Audit of key scalars in abstract and conclusions

- “37.3 million sources” vs Table: cross-transfer total 37,292,042 and Path-C 37,272,042. 37.3M is consistent.
- “378,280 unique anomalies; 378,080 point-source + 200 Planck.” Consistent with Table I summary and Sec. IV C.
- “Recommended catalog-grade subset ~265,000” equals 378,280 − 113,342 ≈ 264,938 (per ♠ footnote). Consistent.
- “141× prior single-survey [11]” with 378,080/2,685 ≈ 141.0. Consistent.
- “DESI-only 195,829 is ~73× increase” with 195,829/2,685 ≈ 72.9. Consistent.
- “Genuine novelty fraction ~17.8%” with 822/1,000 matches ⇒ 17.8% novel. Consistent.
- “LAMOST rate compression 21.5×” with 44,075/2,054 ≈ 21.46. Consistent.
- “SDSS ~6500× rate compression” from 77,905 vs 12 ⇒ 6,492. ≈ 6.5×10^3. Numerically consistent, but the “rate” wording is confusing since 77,905 is not “top-1%” (see P3-E2).
- “DESI 5-fold Jaccard J̄ = 0.862” matches Sec. II B. Consistent.
- “3 PASS, 3 FAIL” for injection-recovery matches Fig. 7 narratives, except the NEOWISE mask (see P3-M1).
- “αjk = 0.19 ± 0.65” and σ(fNL) central 8.14 with envelope [3.92, 8.98]. Consistent if F0 = 1/8.982^2 and α uncertainty is mapped via α^2 to extremal σ values. However, the reported 7.9% improvement is inconsistent (see P3-E6).
- “NANOGrav γ = 2.567 ± 0.382; γ = 3.0 at +1.13σ; γ = 4.33 at +4.61σ; BMB/SMBHB = 7.1×10^3.” The σ-shifts check out, Bayes factor numerically matches log10 B ≈ 3.85, but see P3-M5 for missing uncertainty on B.

Other arithmetic spot-checks

- χ^2/dof = 143,936/38,329 = 3.756 (reported 3.76). OK.
- NEOWISE polar-cap excess: 17/436 = 3.90%; uniform sphere for two 10° caps: 1 − cos 10° = 1.519%. Ratio 2.57× (reported 2.6×). OK.
- Dedup compression: 388,493 − 10,213 = 378,280; 10,213/388,493 = 2.629%. OK.
- False SIMBAD match rate: n ≈ 3.0×10^-5 arcsec^-2, r = 5″ ⇒ πr^2 n ≈ 2.36×10^-3 per source ⇒ ≈ 462 among 195,829 DESI anomalies (reported “~460”). OK.

Length
At 20 pages plus long table footnotes, the paper is dense. Given the scope (multi-survey methodology plus two cosmology applications), this is acceptable for PRD Methods provided the core inconsistencies are corrected. If the authors retain extensive engineering/process prose, I recommend moving it to appendices to keep the main text crisp.

## Summary recommendation
MAJOR REVISIONS

The submission contains serious internal inconsistencies that must be corrected before it reaches PRD standards, most notably the misdefined Fisher F0 (dimensionally wrong in text/tables), the inconsistent SDSS “top-1%” count (77,905 vs the correct 19,253), the use of a quarantined ACT dataset to draw a main-text conclusion, and inconsistent %‑improvement reporting. Data/code availability also needs to meet PRD transparency norms. Once these essential issues are fixed, and the major clarity items addressed, the paper could be suitable for PRD as a methods/data-driven contribution.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P3-E7 (Sec. IV C, Fig. 6; internal contradiction of “flagged by both surveys”)
Problem: The first DESI×SDSS cross-survey match shown in Fig. 6a–b has anomaly scores 3.2 (DESI) and 2.8 (SDSS), both below the paper’s anomaly thresholds (S > 5 for the canonical DESI/SDSS axis). Yet the body text states “Known QSO at z ≈ 1.55: independently flagged by both surveys, validating the cross-survey approach.” It was not flagged by either anomaly detector per the stated thresholds.
Required fix: Correct the description: either remove this pair from the “independently flagged” examples or state explicitly that this is a non-anomalous control match used for validation, not part of the anomaly catalogs. If you intend to show a control, label it as such in the caption and main text.

P3-E8 (Global “S” definition vs per-survey usage; Sec. II B, III E–F, Table I and Table III)
Problem: “S” is defined once (Eq. 2) as a z-scored reconstruction residual (mean-subtracted, variance-normalized on the validation split). However:
- eROSITA: the headline cut is given as S > 0.259 for the “top 0.03%.” For a z-scored variable, 0.259 is a very mild offset (≈40% upper-tail under Gaussian), not ≈0.03%. That threshold is incompatible with a true z-score scale unless the reported “S” is not actually standard-normalized or the “0.03%” quantile is not computed on S.
- Planck: the native top-1% anomalies have “score range [0.558, 0.621].” On a z-score scale, top-1% corresponds to ≳2.3; 0.56–0.62 cannot be a top-1% tail in z-units. This suggests those are raw losses or some other metric, not the canonical S.
- Table III labels SBigAE as “canonical-S z-scored,” yet the top-298 threshold S > 0.259 conflicts with z-score tail expectations.
Required fix: Unify and disambiguate scoring notation across surveys. If some surveys use non-z-scored “scores” (raw MSE, IF raw scores, or other), rename them (e.g., L, IFraw) and don’t call them S. If eROSITA/Planck selections are based on a different score axis, say so and report consistent, comparable z-units (if available) alongside. Update all thresholds/captions to avoid implying top-1% or top-0.03% on a z-scale when not true.

P3-E9 (Sec. II B, DESI thresholding prose)
Problem: The definition of S uses σval “the standard deviation of MSE on the held-out validation split,” but the text then says for DESI “σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143.” σval should be measured, not “set to make” a threshold land at a particular MSE; this reads like a post-hoc normalization, contradicting Eq. (2).
Required fix: Clarify that σval is empirically measured on the validation split, report its value, and then show that this measured σval implies the stated MSE threshold (MSE = μval + 5 σval ≈ 0.143). Remove any wording that implies manual tuning of σval.

P3-E10 (Cross-reference labeling inconsistencies; Sec. II B, III E, Table I footnotes vs Sec. VI D)
Problem: Multiple cross-references point to “§VI D (b), (f), (v), (j)” while Sec. VI D itself uses roman numerals (i), (ii), etc., and Table IV uses Latin letters (a)–(j). Example: Sec. II B references “§VI D (b)” for OOD reconciliation, but Sec. VI D contains (i), (ii) (and Table IV has (a)–(j)); likewise Table I footnotes cite “§VI D (f)” and “(v)”.
Required fix: Standardize the caveat labels and ensure all cross-references point to existing, uniquely labeled items. If Table IV (a–j) is the authoritative index, refer to those; if Sec. VI D (i–x) is, then use that consistently.

P3-E11 (Sec. II C vs Table V; total wall-clock time inconsistency)
Problem: The paper states “total processing time … ≈ 42 hours (wall-clock), dominated by the DESI DR1 scan (19,705 s) and the LAMOST DR10 scan.” Using the provided throughputs and counts yields a much smaller total:
- DESI: 22.5M / 1142 s−1 ≈ 19,705 s = 5.47 h (given)
- LAMOST: 11.42M / 950 s−1 ≈ 12,019 s ≈ 3.34 h
- SDSS: 2.30M / 1100 s−1 ≈ 2,095 s ≈ 0.58 h
- Planck: 20k / 8,000 s−1 ≈ 2.5 s; Gaia ≈ 1.25 s; NEOWISE ≈ 1.6 s; eROSITA ≈ 7.6 s; ACT ≈ 6.9 s
Sum inference ≈ 9.4 h. Adding all training times from Table V gives ≈ 2.3 h, total ≈ 11.7 h — still far from 42 h.
Required fix: Reconcile the 42 h figure with the quoted throughputs. If 42 h includes repeated scans, I/O bottlenecks, or idle/wait time, say so and provide a breakdown. Otherwise correct the wall-clock claim.

MAJOR

P3-M6 (Fig. 2 right caption numerical overstatement)
Problem: The caption claims “spanning twelve orders of magnitude from the threshold (S = 5) to S = 1.9 × 10^11.” The range in S is 1.9×10^11 / 5 = 3.8×10^10, i.e., ≈10.58 orders of magnitude, not twelve.
Required fix: Correct the stated dynamic range (≈11 orders of magnitude), or rephrase to refer to the y-axis if that is what spans twelve orders.

P3-M7 (Appendix C vs Sec. V: inconsistent σ(fNL)(α) scaling)
Problem: Appendix C Table VII explicitly uses linear scaling from the α = 0.15 baseline to tabulate σ(fNL) vs α (e.g., σ = 7.88 at α = 0.30), whereas Sec. V adopts the “positivity-respecting” formula 1/σ^2 = F0 + c α^2 (after correcting F0 per your previous review). The two produce different σ(α) curves; e.g., at α = 0.30 the quadratic form gives σ ≈ 7.24 (with F0 = 1/8.982^2, c = 0.0747), not 7.88.
Required fix: Use a single, consistent σ(α) model throughout (preferably the quadratic/positivity form) and recompute Appendix C accordingly. Make Table VII and the text consistent with Sec. V.

P3-M8 (Sec. III B: “Confirmed High-z QSO Candidates” heading vs content)
Problem: The section title says “Confirmed High-z QSO Candidates,” which is contradictory: “confirmed” vs “candidates.” The text indicates selection by three criteria including “at least one detected emission line,” which supports candidate status, not necessarily formal confirmation (no redshift-fit quality metrics or follow-up spectroscopy are reported).
Required fix: Rename to “High-z QSO candidates” and include quantitative line-detection S/N and redshift-fit uncertainties, or provide explicit confirmation criteria if “confirmed” is retained.

MINOR

P3-n6 (Sec. IV A, footnote language)
Problem: The phrase “hypergeometric two-sided p ≈ 0” for the 284/298 overlap is not informative; p-values cannot be “≈ 0.”
Required fix: Quote a numeric upper bound (e.g., p < 10^−X) from an exact hypergeometric test and state the assumptions.

P3-n7 (Fig. 4 pixel scale inconsistency)
Observation: The DESI Legacy Survey DR9 cutout is labeled “256×256 pixels (108″×108″),” implying 0.42″/pix, while DESI-LS images are typically 0.262″/pix. This could be a resample/crop, but the caption doesn’t say.
Suggested fix: Note if the cutouts were rebinned or downsampled, and state the native pixel scale to avoid confusion.

P3-n8 (Sec. III C narrative blending native vs cross-transfer)
Problem: The SDSS section alternates between cross-transfer (DESI-trained on SDSS) and native re-score statements in one paragraph, which can confuse what count/sample each statistic refers to.
Required fix: Split into two clearly labeled subsections or paragraphs: (i) cross-transfer diagnostic; (ii) native re-score results. Ensure counts and percentages are not intermingled.

P3-n9 (Abstract/Conclusions: selective omission of DESI OOD Jaccard)
Observation: Conclusions list OOD “control-vs-control” Jaccard 0.874 (PASS), but omit the “production-vs-5-seed-control Jaccard = 0.732” that appears in Sec. II B and Sec. VI D (i), potentially overemphasizing the stronger number.
Suggested fix: Report both OOD Jaccards side-by-side for completeness, or make clear which is the headline validation.

NIT

P3-N4 (Terminology: “score” vs “S”)
Problem: The manuscript often says “score” without specifying whether it is the canonical S, a raw MSE, or an IsolationForest score (e.g., Planck “score range,” NEOWISE “score = 11.5”).
Required fix: Replace ambiguous “score” with S, L (loss), or SIF,raw consistently, and define each upon first use in each survey subsection.

P3-N5 (Overuse of “≈” with integers)
Problem: Several exactly known counts are prefixed with “∼” (e.g., “∼ 20× the QSO rate,” “∼ 6500×”), which is stylistically acceptable, but where exact ratios are straightforward, a precise value ± uncertainty reads more rigorously.
Suggested fix: Where possible, report exact ratios and add “≈” only when rounding is intentional.

NO DUPLICATES
None of the issues above duplicate items in your initial report; they address new arithmetic inconsistencies, figure/text mismatches, cross-reference errors, scoring-definition drift across surveys, a wall-clock time inconsistency, and an overclaim in a section heading.
# P3 auto-2026-06-05_1817pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8658 chars)
**Wall time**: 519.7s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches” (20 pages)

Scope of review
- Focus: methodology rigor, statistical validity, internal arithmetic and logical consistency, derivation chains, significance claims, figure/table audits.
- I have read the full manuscript, checked equations, recomputed every quoted scalar that is computable from the text, and audited tables and figure captions vs. body claims.

Findings

ESSENTIAL

P3-E1 (Sec. V.b, p. 10; Abstract p. 1; Table IV caveat (i), p. 13)
Problem: Fisher expression and baseline F0 are dimensionally/numerically inconsistent. You state “1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747,” yielding σ(fNL) = 8.14 for α = 0.19. If F ≡ 1/σ^2, the DESI single-tracer baseline σstd = 8.98 implies F0 = 1/σstd^2 = 1/(8.982)^2 = 0.012396…, not 1/8.982 = 0.1113…. Your numerical result σ = 8.14 is consistent with F0 = 1/(8.982)^2 and c ≈ 0.0747 (since 1/8.14^2 − 1/8.98^2 ≈ 0.002695 = c α^2). The text and Table IV currently state F0 = 1/8.982, which is wrong by a factor ≈ 8.98.
Required fix: Correct all occurrences of F0 to F0 = 1/(8.982)^2. Explicitly show the computation to σ = 8.14 for α = 0.19 to avoid ambiguity. Ensure every place this formula appears (Abstract, Sec. V, Table IV) is made consistent.

P3-E2 (Abstract p. 1; Sec. V.b p. 10; Conclusions p. 14)
Problem: Quoted “7.9% improvement” inconsistent with the stated baseline and central σ. From σstd = 8.98 and σ = 8.14, the fractional improvement is (8.98 − 8.14)/8.98 = 0.0946 = 9.46%, not 7.9%.
Required fix: Replace “7.9% improvement” by the correct 9.4–9.5% (or recompute if σ is changed by E1 corrections). Ensure the Conclusions repeat the corrected value.

P3-E3 (Multiple places: Sec. II.A p. 2; Sec. II.B p. 2–3; Sec. III.B p. 5)
Problem: Unresolved cross-references “Fig. ??” remaining in the body text (e.g., “architecture shown schematically in Fig. ??”; “per-band contributions … Fig. ??”; “Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts…”). PRD cannot accept manuscripts with unresolved figure references.
Required fix: Resolve all “Fig. ??” placeholders to concrete numbers and ensure the referenced figures exist and match the described content.

P3-E4 (Sec. III.C p. 5–6; Table I footnotes ♡ p. 7)
Problem: Incoherent and self-contradictory thresholding for SDSS DR18 native scores.
- You repeatedly call the 77,905-object SDSS slice “top-1% continuity slice,” but 77,905/1,925,279 = 4.05%, not 1%.
- You also say “the same sample yields 19,253 anomalies at the harder top-1% score-knee cut,” where 19,253 is in fact 1% of 1,925,279. The narrative conflates a 4% sample (77,905) with a 1% sample.
- Further, you report “S ≥ 0.1060” (for 77,905) and “S ≥ 0.2051” (for 19,253). If S is defined as a per-survey “z-scored” residual (Eq. 2), a top-1% one-sided tail at z ≈ 2.33 is expected for an approximately standard distribution; thresholds near 0.1–0.2 are inconsistent with your S definition unless you show a drastically rescaled or strongly non-standardized distribution.
Required fix: 
- Correct the percentiles and labels: specify clearly which cuts correspond to 4% vs 1%, and stop calling 77,905 a “top-1%” slice.
- Explain and document the S scaling for SDSS native scores: report μval, σval, and show the empirical CDF or at least give the actual S value at the 99th percentile under your per-survey S-normalization. If S is not a z-score for SDSS native, state that explicitly and rename the variable to avoid confusion.
- Reconcile all places where SDSS thresholds are quoted (text, Table I footnotes, and any supplementary) so the counts/percentiles/thresholds are consistent.

P3-E5 (Sec. III.D p. 6; Table I footnotes ♠ p. 7)
Problem: Analogous inconsistency for LAMOST native thresholds. You call 113,342 “top-1%,” which is arithmetically plausible given N ≈ 1.13×10^7, but you report S ≥ 0.4613 for this cut while S is presented as a z-scored residual. Like SDSS, a top-1% threshold near S ≈ 0.46 contradicts the definition in Eq. (2) unless you demonstrate a different S normalization.
Required fix: As in E4, report μval, σval for LAMOST native training, provide the empirical S CDF or the 99th percentile S, and either (i) show why S≈0.46 truly corresponds to the 99th percentile under your normalization, or (ii) rename and redefine the score axis you are using for the percentile cut so it is not conflated with the canonical “S” z-score.

P3-E6 (Sec. V.a p. 10)
Problem: α is used in a load-bearing Fisher formula without a precise definition in the main text. You later imply α ≡ bQSO-cand/bfull-anomaly − 1 (since bjk = 1.19 ± 0.65, αjk = 0.19 ± 0.65), but this mapping is never explicitly stated at first use.
Required fix: Define α unambiguously at its first appearance (e.g., “α ≡ bAI/bstd − 1”). State the estimator of b (Landy–Szalay normalization/weights, angular binning, mask, and how you combine bins to a geomean), and how jackknife errors are propagated from b to α.

P3-E7 (Sec. II.B p. 3)
Problem: “For DESI DR1, μval ≈ 0.0287 … and σval is set such that the S > 5 catalog threshold corresponds to MSE≈0.143.” σval must be computed from the validation set, not “set to force” a threshold. As written, this invites circularity.
Required fix: Rephrase to “σval ≈ [value], which implies the S > 5 cut corresponds to MSE ≈ 0.143,” and give the actual σval number.

MAJOR

P3-M1 (Sec. IV.B p. 9–10)
Problem: Spatial uniformity test uses Nside = 64 but quotes “38,330 HEALPix pixels (Nside = 64)” and dof = 38,329. Full sky at Nside = 64 has 49,152 pixels; the text does not define the mask/footprint selection that reduces to 38,330 pixels. Without an explicit sky mask and exposure/footprint union definition, χ^2 and dof are not reproducible, and the “non-uniform” statement is not interpretable.
Required fix: Specify the exact sky mask/union of survey footprints used, the criterion for including a pixel (e.g., any catalog coverage vs. observed-area weighting), and report the resulting sky fraction fsky. Provide enough detail for a reader to reproduce dof = 38,329.

P3-M2 (Sec. III.F p. 6; Table V p. 15)
Problem: Planck CMB native autoencoder training time listed as 10.6 s for 2×10^5 masked patches and a 1.1M-parameter CNN is not credible on an A100; inference throughputs are plausible, but training time is too small by orders of magnitude. The same table mixes training and inference metrics without clear units/checks. This undermines the computational reproducibility.
Required fix: Audit and correct the Planck training time units and values (likely minutes or hours), and clearly distinguish training vs. inference columns. Provide wall-clock times with hardware details (GPU model, batch size, number of epochs).

P3-M3 (Sec. IV.A p. 8–9; Abstract p. 1; Conclusions p. 14)
Problem: The 17.8% “genuine novelty” fraction is reported as a single-sample point estimate with “no upper/lower-bound status.” PRD requires quantified uncertainty for central empirical fractions. A simple binomial 68% CI is trivial here.
Required fix: Report the binomial 68% and 95% confidence intervals for 178/1000 (e.g., 17.8% ± 1.2% at 68% CL, ±2.5% at 95% CL; compute precisely), and state that it pertains to the top-1,000 DESI anomalies only.

P3-M4 (Sec. V.a p. 10; Appendix C p. 15)
Problem: Methodological clarity on the bias measurement is insufficient for reproduction. The LS estimator variant, weights, bin centers/edges, mask, and random catalog generation are only partially specified, and combining across bins by “geomean” is unusual and unmotivated.
Required fix: 
- Specify the Landy–Szalay estimator version used, angular bin edges and number of bins, weighting scheme (FKP or uniform), and the depth/footprint mask.
- Describe the construction of the “26,920 anomaly-window-matched randoms,” including how the window/selection function was built.
- Justify the geomean aggregation or replace with a standard χ^2 fit for b across bins.

P3-M5 (Table I and related text, p. 7; throughout)
Problem: The paper mixes cross-transfer and native-retrained counts in a manner that remains confusing despite caveats. In particular, keeping a 77,905-object SDSS “continuity slice” (actually ≈ 4%) for some analyses while emphasizing S > 5 yields 12 native anomalies promotes apples-to-oranges comparisons.
Required fix: Present a clean, primary, native-only catalog definition in the main table, and demote all cross-transfer or continuity slices to a clearly labeled appendix table, with explicit warnings that they are not comparable for rate statistics. The main table should list only the native, per-survey, final thresholds and counts.

P3-M6 (General style/footnotes; Table I p. 7)
Problem: Use of decorative footnote symbols (♡, ♠) and very long narrative footnotes in a table is not PRD style and obscures the quantitative content.
Required fix: Move explanatory footnote prose to the main text or an appendix; use standard numeric or alphabetic footnotes; keep table footnotes concise.

MINOR

P3-m1 (Sec. II.C p. 3; Table V p. 15)
Problem: Text says “CMB and photometric surveys each required < 10 seconds of GPU time” without stating this is inference time, while Table V’s “Train time (s)” column presents training times. Could be misread as training.
Required fix: Clarify in Sec. II.C that the < 10 s refers to inference. Ensure Table V captions/headers clearly distinguish training vs inference.

P3-m2 (Sec. IV.A.b p. 9)
Problem: Expected-false-match calculation uses nSIMBAD ≈ 3.0×10−5 arcsec−2. The source for this density is not cited or derived.
Required fix: Provide a citation or an explicit calculation for the adopted SIMBAD surface density.

P3-m3 (Sec. III.A p. 4)
Problem: “σval is set such that …” wording (see E7) appears again implicitly; additionally, DESI per-arm sub-scores rB, rR, rZ are mentioned but not formally defined.
Required fix: Provide explicit formulae for rB, rR, rZ or remove the per-arm decomposition unless used in a quantitative result.

P3-m4 (Sec. VII bullet 6 p. 14 vs Sec. II.B p. 3)
Problem: Two different OOD/Jaccard numbers appear: “production-vs-5-seed-control Jaccard J̄prod×ctrl = 0.732” (Sec. II.B) and “OOD control-vs-control 0.874” (Conclusions). The latter is not introduced earlier.
Required fix: Define “control-vs-control” Jaccard, explain the difference from “prod×ctrl,” and report both consistently in the methods where readers expect to find them.

P3-m5 (Data availability p. 14)
Problem: Data are “private pending arXiv acceptance; public upon acceptance.” For PRD review, the data/code should be accessible to referees.
Required fix: Make an anonymized or tokenized private link available to referees during review or deposit to a journal-approved repository with reviewer access.

P3-m6 (Appendix E, Eq. E1 p. 16)
Problem: Notation ρi not defined; dimensionality/log-convention unclear.
Required fix: Define ρi explicitly (e.g., log10 of strain power spectral density or energy density proxy), and reference the standard relation used.

NITS

P3-n1 (Sec. II.D p. 3)
Problem: Redundant phrasing “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”
Required fix: Remove repetition.

P3-n2 (Throughout)
Problem: Occasional informal phrases (“single most important methodological lesson,” “this is not a science result”). PRD style prefers neutral, precise phrasing.
Required fix: Tidy wording to neutral declarative statements.

P3-n3 (Typographic)
Problem: Mixed use of primes and ASCII quotes for arcseconds (5′′).
Required fix: Ensure arcsec symbol is consistent.

P3-n4 (Length)
Problem: The main text is lengthy relative to the focused methods results, with multiple digressions (ACT appendix, taxonomy galleries reference) that could be trimmed.
Recommendation: Aim for ≤16 pages main text by moving extended narrative/diagnostics to appendices or supplementary.

Audit of abstract and conclusions numerics
- 378,280 unique anomalies; 378,080 point-source + 200 Planck patches: Consistent with Table I Path-C row and 7-way dedup (388,493 − 10,213 = 378,280).
- DESI-only 195,829/22,504,897 = 0.87%: correct.
- “∼141×” vs [11] (378,080/2,685): 141.0: correct.
- “∼73×” DESI-only vs [11] (195,829/2,685): 73.0: correct.
- Novelty fraction 17.8% from top-1,000 cross-match: 178/1,000: correct, but CI missing (see M3).
- LAMOST 21.5× and SDSS ∼6500× rate compressions: consistent with numbers given (2,054 at S>5 vs 44,075 cross-transfer; and 12 at S>5 native vs 77,905 cross-transfer).
- DESI k-fold Jaccard 0.862: text consistent.
- Injection-recovery: SDSS 64%, Planck 100%, NEOWISE 100%; LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2% at 5σ: matches body.
- Fisher forecast σ(fNL) = 8.14 central with envelope [3.92, 8.98]: consistent with the positivity form once F0 fixed (E1), but improvement % misreported (E2).
- NANOGrav γ = 2.567 ± 0.382; distances to γ = 3.0 and 4.33 as 1.13σ and 4.61σ; BMB/SMBHB ≈ 7.14×10^3: consistent.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript has multiple core methodological inconsistencies that must be corrected before it can be considered at PRD standards. Chief among them are (i) a dimensionally incorrect Fisher baseline (F0) that is used in key claims (and a misreported percent improvement), (ii) unresolved figure references, and (iii) serious incoherence in the definition and use of the anomaly score S and associated percentiles for SDSS and LAMOST native analyses (percentiles and thresholds do not add up as described). Additional substantial clarifications are required for the spatial analysis mask and the bias-measurement methodology. Once these essential and major issues are resolved and the presentation is tightened, the paper may be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P3 — ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P3-E8 (Fig. 6 vs. text; Sec. IV.C p. 10–11)
Problem: Cross-survey match “Match 1” is claimed to be “independently flagged by both surveys,” but the figure shows anomaly scores below the stated thresholds in both surveys: DESI score = 3.2 and SDSS score = 2.8. Under the paper’s own thresholds (DESI S > 5 native; SDSS native S > 5 or the authors’ other stated SDSS native cuts), these spectra would not be in either survey’s anomaly set.
Required fix: Reconcile the claim and the figure. Either (i) correct the statement to reflect that only one survey flagged this source (and specify which), or (ii) explain why a sub-threshold score appears (e.g., a different score axis, alternative cut used for this particular figure), and provide the actual anomaly-qualifying scores used for catalog inclusion.

P3-E9 (Global S definition; Sec. II.B p. 2–3 vs. multiple sections/figures)
Problem: In Sec. II.B you state “Throughout this paper, ‘S’ refers without exception to the per-survey standardized (‘z-scored’) reconstruction residual,” but later practice contradicts this:
- SDSS is sometimes scored on the DESI-trained cross-transfer scale (Fig. 2 caption).
- Planck native tier reports “score range [0.558, 0.621]” for a top-1% selection (Sec. III.F), which is inconsistent with a z-score one-sided 1% tail (~2.33) unless you demonstrate a very nonstandard S distribution.
- NEOWISE highlights a “Score = 11.5” top object (Fig. 4) while also using a fixed top-1% selection; again this is not obviously a z-score from a native standardization.
Required fix: Remove the “without exception” statement and precisely define, for each survey and for each usage (native vs. cross-transfer), the score axis used, its normalization (μval, σval), and the thresholding scheme. If different surveys use different, non-z-standardized axes, rename those axes in text and figures so they are not conflated with “S” as defined by Eq. (2).

P3-E10 (SIMBAD category inconsistency; Sec. III.C p. 5–6; Table II p. 8)
Problem: Table II says the 52.7% “Uncategorized” class “reflects objects that match a SIMBAD entry but lack a specific astrophysical type classification.” This cannot be reconciled with the earlier statement in Sec. III.C that the SDSS DR18 cross-transfer anomalies are 90% SIMBAD-unmatched. If 52.7% of 77,905 matched SIMBAD, the unmatched rate would be ≤ 47.3%, not 90%.
Required fix: Clarify what “Uncategorized” means (likely your internal emission-line/continuum taxonomy, not SIMBAD-matched status) and correct the explanatory sentence. Report SIMBAD-match fractions and taxonomy fractions as separate, non-conflicting quantities.

P3-E11 (Total wall-clock time inconsistency; Sec. II.C p. 3; Table V p. 15)
Problem: You state the total inference “processing time” across surveys was ≈ 42 hours, “dominated by the DESI DR1 scan (19,705 s).” Using your own throughputs from Table V:
- DESI: 22.5M/1,142 ≈ 19,703 s = 5.47 h
- LAMOST: 11.4M/950 ≈ 12,000 s = 3.33 h
- SDSS: 2.30M/1,100 ≈ 2,095 s = 0.58 h
- Others are ≲10 s each by text and Table V
The sum is ≈ 9.4 hours, not 42 hours. There is a factor ~4–5 discrepancy.
Required fix: Audit and correct the reported wall-clock total. If training times, data I/O, preprocessing, or reruns are included, state that explicitly and break down training vs. inference vs. I/O components with hardware and concurrency details.

P3-E12 (Threshold-family contradiction; Sec. II.B p. 2–3 vs. Table I footnotes/text)
Problem: Sec. II.B states “DESI DR1 and SDSS DR18 use an absolute canonical-S cut at S > 5.0.” Elsewhere, the SDSS native analysis retains a “top-77,905 native slice at S ≥ 0.1060” and also quotes 12 objects at S > 5 (Table I footnotes and Sec. III.C). These are mutually inconsistent descriptions of the SDSS primary cut.
Required fix: State unambiguously which single SDSS definition is used for the primary, native, science-grade catalog and move any alternative “continuity slice” to a separately labeled, clearly non-primary table/appendix. Ensure Sec. II.B reflects the true per-survey thresholds actually used for the primary catalog.

MAJOR

P3-M7 (SDSS N mismatch and selection; Sec. III.C p. 5–6; Table I p. 7)
Problem: Table I lists SDSS DR18 Ntotal = 2,304,830, but the text for the SDSS native re-score says “complete across 1,925,279 spectra” (≈17% fewer). The quality/selection cuts producing the 1.93M sample are not specified.
Required fix: Provide the filtering criteria (e.g., S/N, pipeline flags, bad pixels, redshift completeness) that reduce 2.30M to 1.93M, and update Table I or add a “used N” column so rate comparisons are reproducible.

P3-M8 (Planck×ACT “null” result lacks a statistic; Sec. IV.D p. 10)
Problem: The cross-correlation is described as “null... do not cluster above random,” but no quantitative metric (e.g., cross-correlation coefficient, p-value under a randomization test, or a jackknife covariance) is provided.
Required fix: Report a well-defined test statistic, its uncertainty, and a p-value (or upper limit) relative to a stated null model, including the footprint masks for both surveys.

P3-M9 (Expected-random dedup overlaps; Sec. IV.A.b p. 9)
Problem: You state the expected random-coincidence contribution to the 7-way, 5″ dedup “is ≲ 10” across all survey pairs but provide no calculation or surface-density inputs for each catalog pair.
Required fix: Show the calculation (surface densities, sky area, matching radius, mask overlap per pair) or provide a Monte Carlo estimate with uncertainties so the “< 2% contamination” claim for the 637 multi-survey clusters is auditable.

MINOR

P3-m7 (Abstract/Conclusions language)
Problem: Claim “the largest multi-archive anomaly search to date” is not accompanied by a specific comparison to prior multi-archive works (only a single-survey comparison to [11] is given).
Required fix: Add a citation-backed comparison to the most comparable multi-archive searches (if any), or soften the claim to “to our knowledge” with a brief literature scan.

P3-m8 (Fig. 3 labeling vs. text; p. 6)
Problem: The figure overlay text mentions “14 clusters, 99.4% clustered,” while the caption and body text discuss “three latent-space populations.” This is potentially confusing.
Required fix: Clarify in the caption that HDBSCAN found 14 clusters which you group into 3 physical-population super-clusters, and provide the mapping or object counts per group.

P3-m9 (Fig. 9 panel labels “AE=…”)
Problem: The “AE=” numeric labels are not defined in the caption and appear orders of magnitude larger than any per-arm residuals (e.g., “AE=83,518”), conflicting with earlier statements that “AE” refers to the Z-arm sub-score rZ. If these are not rZ, the label is misleading; if they are, the scale contradicts earlier ranges for rB/rR/rZ.
Required fix: Define “AE” precisely for Fig. 9 (units, range, how computed). If it is a legacy quantity unrelated to rZ, rename it to avoid confusion and ensure consistency with Sec. III.B’s description.

P3-m10 (Missing citation for SPARCL; Sec. II.B p. 3)
Problem: The NOIRLab SPARCL service used for OOD validation is not cited.
Required fix: Add a formal citation/URL/DOI for SPARCL and specify the query parameters used (date, sky region, random-seed provenance).

P3-m11 (Ambiguous database statement; Sec. III.A p. 4)
Problem: “None of the top 100 [DESI] appear in any database” conflicts with the prior sentence that the top-10,000 have 12.7% in NED and also seems unlikely given inclusion of SDSS/AllWISE/Gaia catalogs. It is unclear whether “any database” refers only to SIMBAD/NED or to the broader 20-catalog CDS X-Match set.
Required fix: Specify exactly which databases were checked for the “top 100” result and report the matched/unmatched counts per database (or explicitly state that it refers to SIMBAD-only).

NITS

P3-n5 (Figure/text consistency for units and symbols)
Problem: Mixed and undefined units/symbols persist in several captions (e.g., degrees vs. RA/Dec notation; “AE” units; “score” vs. “S”).
Required fix: Standardize units in figure axes/captions and ensure every nonstandard symbol is defined locally in the caption.

Explanation
These are new findings not included in the initial review. The most critical are (i) the sub-threshold scores shown in Fig. 6 for a purported dual-survey anomaly, (ii) the global misuse/inconsistency of “S” relative to its formal definition, (iii) the SDSS SIMBAD contradiction in Table II, and (iv) the 42-hour wall-clock inconsistency with your own throughputs. Addressing these, together with the previously reported issues, is necessary to reach PRD standards.
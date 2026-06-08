# P3 auto-2026-06-08_1354pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9251 chars)
**Wall time**: 499.7s

---

Referee report (methodology/statistics) for “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog …”

I read the full 20-page manuscript, all figures, tables, equations, and the abstract/conclusions. Below I itemize all methodological, statistical, and arithmetic issues found, with severity tags and concrete required fixes. Page numbers refer to the rendered PDF pagination shown in the document (1–20).

ESSENTIAL

P3-E1 (Sec. V.b, p. 11; Table IV caveat (i), p. 13)
Problem: Dimensional/arithmetical error in Fisher “positivity-respecting” formula constants. Text states “1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747.” F0 must be 1/σ_std^2, i.e., F0 = 1/(8.98)^2 ≈ 0.01240, not 1/8.98 ≈ 0.111. Despite this misprint, the reported σ(fNL)=8.14 at α=0.19 only agrees if F0=1/(8.98)^2 is used.
Required fix: Correct F0 everywhere to F0 = 1/(8.98)^2. Audit all downstream uses (Sec. V.b, Table IV (i), Appendix C) to ensure numerical self-consistency, and restate the derivation/fit of c with correct units.

P3-E2 (Sec. V.b, p. 11)
Problem: Miscomputed “improvement” percentage. With σ_std = 8.98 and σ = 8.14, the fractional improvement is (8.98−8.14)/8.98 = 9.3%, not 7.9% as stated.
Required fix: Recompute and correct the improvement percentage and associated prose. If a different baseline was intended, state it explicitly and show the calculation.

P3-E3 (Table I footnote ♡ and Sec. III.C, pp. 7 and 5)
Problem: Contradictory “top-1%” thresholds for SDSS. You claim both “top-77,905 at S ≥ 0.1060” and “19,253 anomalies at the harder top-1% score-knee cut S ≥ 0.2051” are “top-1%.” For the stated native-scored sample of 1,925,279 spectra, 1% is 19,253. 77,905 corresponds to 4.05%.
Required fix: Remove the “top-1%” label from the 77,905 slice or correct the counts/denominator. Present a single, unambiguous definition of each threshold, with the correct corresponding counts and percentages. Ensure consistency between Table I, Sec. III.C, and figure captions.

P3-E4 (Abstract p. 1; Table I footnote ♠ p. 7; Sec. IV.C p. 10)
Problem: Catalog-grade subset count inconsistent. Abstract recommends “∼265,000 unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE),” excluding LAMOST and also stating that Planck patches are not objects. Table I footnote then states “catalog-grade tier (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE) is 264,938,” which includes Planck patches and numerically equals 275,151 − 10,213 (subtracting the full 7-way compression, which improperly includes LAMOST and intra-survey duplicates).
Required fix: Provide the exact deduplicated unique-object count for the catalog-grade subset that you actually recommend for object-level analyses: explicitly exclude LAMOST and Planck. Report the precise dedup result for that 5-survey set (DESI+SDSS+eROSITA+Gaia+NEOWISE), with the corresponding compression due solely to those five. Correct the abstract and footnote accordingly.

P3-E5 (Sec. V.b p. 11 vs. Table IV (i) p. 13)
Problem: Conflicting confidence-level labeling for the σ(fNL) “envelope.” On p. 11 you write “1σ envelope [3.92, 8.98],” while Table IV (i) calls the same numbers the “95% envelope.”
Required fix: State a single, correct confidence level for the [3.92, 8.98] bounds, and transparently explain how they are obtained from α_jk = 0.19 ± 0.65. If derived from ±1σ in α (and the α^2 dependence), keep the “1σ envelope” language and remove the “95%” claim.

P3-E6 (Sec. IV.A and Fig. 5, p. 9)
Problem: Aggregate SIMBAD-unmatched fraction “58.8%” is not reproducible from the reported per-survey fractions and counts. Using either the cross-transfer or Path-C per-survey anomaly counts and the stated unmatched percentages yields ≳80–90%, not 58.8%. The figure also mixes different sample definitions (e.g., “DESI DR1 (top 10K) 99%”) without a common denominator.
Required fix: Precisely define the denominator(s) for the aggregate. Report the computation (weighted by anomaly counts per survey at a clearly specified selection) and give its value with uncertainty. If using different sample sizes per survey (e.g., DESI “top-10K”), state that and avoid aggregating across incomparable denominators; otherwise recompute on a harmonized basis.

P3-E7 (Sec. III.B p. 5; Appendix D/Fig. 9 p. 17)
Problem: Inconsistent use/units of the “AE” label on images. On p. 5 you say panel labels report r_Z (“printed as ‘AE’”), with mean ⟨r_Z⟩ ≈ 3.9 for high-z candidates. In Fig. 9, AE values are O(10^3–10^5), inconsistent with r_Z and with S. This mislabeling prevents replication and interpretation.
Required fix: Unambiguously define what “AE” is in every figure (S? arm sub-score? raw MSE?), include units/scales, and ensure consistency with the earlier text. If Fig. 9 uses a different metric, rename the label accordingly and correct the captions/prose where needed.

P3-E8 (Abstract p. 1; Table I footnote regarding fixed top-1% selections, p. 7)
Problem: In the abstract you present “378,280 unique anomalies” and an overall “1.01%” rate without caveat, yet several surveys (Planck, Gaia, NEOWISE) use a fixed top-1% selection by construction. Table I footnote provides the caveat, but the abstract does not.
Required fix: Add an explicit abstract-level caveat that several surveys’ contributions are predetermined top-1% selections and that the overall “1.01%” is not an unbiased measurement of intrinsic anomaly frequencies across all archives.

MAJOR

P3-M1 (Sec. III.A p. 4)
Problem: “None of the top 100 [DESI anomalies] appear in any database” appears to contradict the later archival cross-match of the top-1,000 yielding 82.2% identifications across 20 catalogs.
Required fix: Clarify that the “six databases” in Sec. III.A (SIMBAD, NED, AllWISE, Milliquas, Gaia DR3, SDSS) differ from the 20-catalog CDS X-Match set used later, and indicate whether any of the DESI top-100 are among the 822/1000 matches in the extended set. Provide exact counts for the top-100 under the 20-catalog match to remove ambiguity.

P3-M2 (Sec. IV.C p. 10)
Problem: Unsupported robustness claim: “present 378,280 unique-object count is robust to [matching-radius/probabilistic cross-match] refinements at the ≲ 0.1% level.” The only hard bound shown is the observed 2.63% compression at 5″.
Required fix: Either provide an actual sensitivity test (e.g., recompute unique-object count at 3″ and 7″ and show changes) or soften the claim to the demonstrated bound (≤2.63%). If keeping the <0.1% claim, include the quantitative test in the paper.

P3-M3 (Sec. II.D p. 3 and Table I footnotes p. 7)
Problem: Threshold taxonomy is confusing and sometimes internally inconsistent: absolute S>5.0 (DESI), a “top-1% continuity slice” that is numerically 4.05% for SDSS native, a “score-knee cut” also labeled top-1% for SDSS, LAMOST top-1% at S≥0.4613 while S is defined as a per-survey z-score (making 0.46 a 32% tail under a Gaussian), etc.
Required fix: Provide a clean, survey-by-survey table of the final, authoritative thresholds with: selection type (absolute S cut vs percentile), the exact value, the denominator (N_total actually scored), the resulting N_anom, and the true anomaly percentage. Remove contradictory “top-1%” descriptors.

P3-M4 (Sec. V.a p. 11)
Problem: Insufficient specification of the Landy–Szalay bias-ratio measurement. No mask description, random catalog construction, sky coverage, completeness, or justification of 30-region jackknife region size are provided; no stability checks vs. region count.
Required fix: Detail the mask(s), random catalog generation, angular binning, number densities, and completeness corrections. Provide a stability test (e.g., results vs. 20/40 jackknife regions) to demonstrate robustness of α_jk and its uncertainty.

P3-M5 (Sec. III.F p. 6; Fig. 7 p. 13)
Problem: Injection–recovery for Planck CMB uses “5σ Gaussian-bump amplitude” but the noise reference (“σ”) is not defined (per-pixel RMS? per-patch? filtered?).
Required fix: Define σ precisely for the CMB patches, including filtering and map units, and state the bump width/profile. Provide a reference plot showing the injected template relative to the patch noise power.

P3-M6 (Sec. III.E p. 6; Table I footnote § p. 7)
Problem: “Hypergeometric two-sided p ≈ 0” phrasing for the 284/298 overlap is not quantitative.
Required fix: Report an explicit p-value or an upper bound (e.g., p < 10^{-x}) with the exact hypergeometric parameters used.

P3-M7 (Appendix D and Fig. 9, p. 17)
Problem: The taxonomy/UMAP/HDBSCAN clustering is reported as “trustworthiness 0.9797 ± 5×10^-5 (PASS), kNN-preservation and cross-seed Spearman FAIL … Trustworthiness is the primary stability claim.” This is too cursory for a stability assessment of a 10-family taxonomy used in scientific interpretation.
Required fix: Provide quantitative cross-seed clustering stability metrics (e.g., adjusted Rand index across seeds) and a confusion matrix across seeds for the 10 clusters. Alternatively, explicitly demote the taxonomy to a purely illustrative appendix with no load-bearing claims.

P3-M8 (Sec. III.H p. 8)
Problem: NEOWISE “score = 11.5” but no distribution or scale is shown for that survey’s S, and selection is a fixed top-1% by design.
Required fix: Add a NEOWISE score distribution figure or table (analogous to Fig. 2 for spectroscopic surveys), with the selection threshold marked and the top anomaly position indicated.

MINOR

P3-m1 (Sec. II.D p. 3)
Problem: Repetition/typo: “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”
Required fix: Remove the duplicate phrase.

P3-m2 (Sec. III.A p. 4)
Problem: “0.2% in SIMBAD and 12.7% in NED” for the DESI top-10,000: the actual matched counts (e.g., 20/10,000 and 1,270/10,000) should be stated explicitly for clarity.
Required fix: Report the absolute numbers.

P3-m3 (Sec. III.D p. 6; Fig. 7 caption p. 13)
Problem: “9.7× improvement” is quoted without context; likely 5.8% vs 0.6% for LAMOST emission-line vs continuum-dip.
Required fix: Show the two numbers being compared and how the factor is computed.

P3-m4 (Sec. V.A p. 12)
Problem: Bayes factor interpretation (“decisive on Jeffreys’ scale”) is prior-dependent. You specify a γ-uniform prior but do not state the bounds in that specific sentence.
Required fix: Remind the reader at point-of-use that the Savage–Dickey value refers to γ ∈ [0,7], log10 A ∈ [−18, −11], and add a brief prior-sensitivity sentence.

P3-m5 (Data availability, p. 14)
Problem: “private pending arXiv acceptance; public upon acceptance” is not aligned with PRD data availability expectations.
Required fix: Provide an accession that is public upon publication acceptance, or state an embargo policy consistent with PRD guidelines.

NITS

P3-n1 (Throughout)
Problem: Inconsistent capitalization and hyphenation of technical terms (e.g., “Gaussian-bump,” “gate-PASS,” mixed use of symbols/spaces).
Required fix: Copy-edit for consistency.

P3-n2 (Fig. 1 caption, p. 4)
Problem: “ACT DR6 is quarantined and excluded” while ACT appears in the legend could be misread.
Required fix: Add “excluded from the canonical Path-C counts; included here only as part of the cross-transfer baseline figure.”

P3-n3 (Appendix E, eq. E1, p. 16)
Problem: Missing a brief statement of map/units for ρ_i and f_i, and whether log10 is base-10 throughout (implied, but restate).
Required fix: Add one clarifying sentence.

Additional length/fit-to-contribution comment
The paper attempts two substantial, somewhat orthogonal contributions: a multi-archive anomaly catalog methodology/dataset, and cosmological applications (fNL forecast; PTA spectral-index model comparison). While both are interesting, the cosmology sections (Sec. V–V.A, Appendices C/E) are currently under-specified methodologically (see ESSENTIAL/MAJOR items above) and read as preliminary add-ons. For PRD standards, either (a) substantially strengthen the methodological derivations and validation in Sec. V with full transparency and corrections noted above, or (b) move the cosmology material to a companion paper and focus this submission on the catalog methodology and validation. If retained, the overall manuscript length is acceptable (~20 pages), but the cosmology parts require more detail per P3-M4, P3-E1/E2/E5.

Audit of abstract and conclusions scalars vs. body
- 37.3 million processed: matches Table I totals (37,292,042 cross-transfer; 37,272,042 Path-C excluding ACT).
- 378,280 unique anomalies: matches Sec. IV.C and Table I footnote after dedup (388,493 − 10,213).
- 378,080 point-source + 200 Planck: matches Table I footnote stratification.
- “∼141×” prior largest (2,685): 378,080/2,685 ≈ 141.0 OK.
- “DESI-only ∼73×”: 195,829/2,685 ≈ 72.9 OK.
- “17.8% genuine novelty”: 178/1000 OK and sourced in Sec. IV.A.
- “21.5× LAMOST compression”: 44,075/2,054 ≈ 21.5 OK.
- “∼6500× SDSS rate compression”: 77,905/12 ≈ 6,492 OK.
- “DESI 5-fold Jaccard 0.862”: matches Sec. II.B/Caveat (i).
- Injection–recovery gates: numbers match Fig. 7.
- Cross-matches: three objects shown in Fig. 6 OK.
- α_jk = 0.19 ± 0.65: matches Sec. V.a.
- σ(fNL) = 8.14: numerically correct only if F0 = 1/(8.98)^2 (P3-E1).
- “7.9% improvement”: inconsistent (P3-E2).
- PTA γ result and σ-shifts: internally consistent with reported numbers; Bayes factors consistent; ensure clarity per P3-m4.

## Summary recommendation
MAJOR REVISIONS

The submission contains multiple essential methodological and arithmetic inconsistencies that must be corrected before the paper can meet PRD standards. Chief among these are the dimensional error in the Fisher forecasting formula and the miscomputed improvement percentage, contradictory “top-1%” definitions for SDSS, an inconsistent catalog-grade subset count, a non-reproducible aggregate SIMBAD-unmatched fraction, and ambiguous figure labeling (“AE”). The cosmology section requires clearer estimator specification and robustness tests. With these issues rectified and the statistical methodology clarified and internally consistent, the manuscript could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh review pass)

ESSENTIAL

P3-E9 (Appendix C vs. Sec. V; Fig. 8, p. 15 vs. Sec. V.b, p. 11)
Problem: Inconsistent σ(fNL) baselines and forecasting frames. Appendix C/Fig. 8 states a single-tracer baseline σ(fNL)=16.85 and a dense multi-tracer limit σ(fNL)=11.71 (baseline-multi 12.72), whereas Sec. V.b uses σstd=8.98 for the single-tracer baseline and forecasts centered around 8.14–8.98. These frameworks are not reconciled, yet conclusions and “percent improvement” language are intercompared across them.
Required fix: Unify the forecasting setup across the paper. Either (a) bring Appendix C to the same Fisher configuration and data vector as Sec. V (same kmax, tracer set, survey volumes, priors), or (b) clearly label Appendix C as a different scenario and remove all cross-references that compare its numbers to the σstd=8.98 baseline. Provide a side-by-side table showing which figures/sections use which baseline and prevent mixing them in prose or percentages.

P3-E10 (Sec. III.F, p. 6)
Problem: Violation of the “single S definition” rule for the CMB tier. The paper states “Throughout this paper, S refers without exception to the per-survey standardized (‘z-scored’) reconstruction residual” (Sec. II.B). However, Planck CMB anomalies are reported with “score range [0.558, 0.621]” after a convolutional AE retrain, with no z-scoring to a validation distribution and no units/axis name given. This is not the canonical S used elsewhere (z-scored MSE).
Required fix: Either (a) z-score the Planck CAE residuals exactly as defined for S, report SPlanck for the 200 patches, and mark the top-1% cut on that S scale; or (b) explicitly rename this axis (e.g., “raw CAE residual”) everywhere it appears and add a hard disclaimer that it is not comparable to S from the other surveys. Update Table I and Sec. III.F accordingly.

P3-E11 (Sec. IV.B, p. 10)
Problem: HEALPix and χ2 test setup inconsistent/incomplete. You write “A spatial uniformity test across 38,330 HEALPix pixels (Nside=64) reveals … χ2=143,936, dof=38,329.” Nside=64 has 49,152 pixels; using 38,330 implies a substantial mask that is nowhere specified. Expected counts per pixel under the null and the area/footprint weights are also not specified, so χ2ν=3.76 is not reproducible or interpretable.
Required fix: Define the exact sky mask and pixel selection used, give the number of retained pixels and sky fraction, state how expected counts per pixel were computed under the null, and provide the per-survey footprint weighting or completeness map used. If the test only covers “occupied pixels,” rename it accordingly and justify degrees of freedom. Without this, remove or demote the χ2 claim.

P3-E12 (Sec. III.C, III.E; Table I, pp. 5–7)
Problem: Threshold percentiles vs. reported S thresholds are internally incoherent for z-scored S. Examples: “SDSS native top-77,905 at S≥0.1060” corresponds to 4.05% of 1,925,279 spectra (not 1%), yet S=0.106 would be near the median of a z-score, not a 96th percentile. eROSITA’s “S>0.259 (top 0.03%)” is also inconsistent with any z-scored interpretation unless the full-sample S distribution is wildly compressed relative to the validation set. These claims cannot be reconciled with the stated S definition.
Required fix: For each survey using an S threshold, publish the empirical CDF of S on the actually-scored full sample and report the percentile corresponding to the quoted S threshold (with a figure or table). If S is not genuinely z-scored to unit variance on the validation set or the production set has a shifted distribution, state this explicitly and stop using “z-scored” language. Correct Table I footnotes and Sec. III.C/III.E text to reflect the true percentiles.

MAJOR

P3-M9 (Sec. V.a, p. 11)
Problem: α is used in the Fisher formula and in the Landy–Szalay result (αjk=0.19±0.65) but is never explicitly defined in the main text when introduced. The reader must infer α≡b−1 from “bgeo=1.27 (αgeo=0.27).”
Required fix: Add an explicit definition of α the first time it is used: α ≡ bQSOcand/bfull−1, with b measured from the Landy–Szalay estimator on the specified mask and angular bins.

P3-M10 (Sec. IV.D, p. 10; Appendix F)
Problem: The Planck×ACT “null cross-correlation” conclusion relies on an ACT anomaly set that explicitly fails both training gates and is quarantined (Appendix F). Using that set to infer a scientific conclusion about lack of correlation risks biasing the conclusion by construction.
Required fix: Soften the language to “no evidence for correlation using our quarantined ACT cross-transfer set; we refrain from astrophysical interpretation.” Alternatively, provide a minimal robustness check (e.g., repeat using randomized Planck anomalies matched to the ACT latitude distribution) to show the null is not purely driven by ACT’s known systematics.

P3-M11 (Sec. III.C figure text vs. body, p. 6; Fig. 3)
Problem: The figure panel text for Fig. 3 (left) includes “77,905 anomalies (score ≥ 5.0), 14 clusters …” while the body text for SDSS native scoring describes a 77,905-object continuity slice at S≥0.1060 (and a separate 12-object S>5 native slice). The co-occurrence of “77,905” with “score ≥ 5.0” can be misread as referring to the native re-score.
Required fix: Amend the Fig. 3 caption/panel text to explicitly say “SDSS DR18 cross-transfer (DESI-trained) anomalies with S>5.0: N=77,905.” Ensure the body text nearby repeats that this refers only to cross-transfer, not native scoring.

P3-M12 (Sec. II.D and Fig. 7, pp. 3 and 13)
Problem: Mixed “gate” null procedures are presented as comparable. For example, NEOWISE “mask injection-recovery: 1000/1000=100%” is a geometric masking sensitivity test, not a signal-injection recovery on an AE residual. Planck uses a Gaussian-bump injection; SDSS/LAMOST use continuum-dip or emission-line plants; eROSITA/Gaia quote XV-stabilities. These are different nulls with different σ definitions.
Required fix: Add a comparability caveat above Fig. 7: gates refer to different validation procedures and are not directly comparable across surveys. Provide per-survey definitions of σ and “recovery” in one table, and avoid mixing “PASS/FAIL at 5σ” across heterogenous tests.

P3-M13 (Sec. III.C figure-caption claim, p. 5)
Problem: “spanning twelve orders of magnitude from the threshold (S=5) to S=1.9×10^11” is numerically overstated. The ratio 1.9×10^11 / 5 ≈ 3.8×10^10 spans ≈10.6 orders of magnitude, not twelve.
Required fix: Correct the statement to “≈10–11 orders of magnitude” or provide the exact dynamic range relative to a properly defined baseline.

MINOR

P3-m6 (Sec. IV.A, p. 9; Table I, footnote §, p. 7)
Problem: The false-match estimate for SIMBAD uses nSIMBAD≈3.0×10^-5 arcsec^-2 but the source/catalog version is not cited, and the value may vary by sky region and magnitude cut.
Required fix: Cite the source and epoch/magnitude dependence of this surface density, or add a brief sensitivity statement (e.g., doubling n changes Pfalse from 0.24% to 0.48% for DESI).

P3-m7 (Sec. III.F, p. 6; Table V, p. 16)
Problem: Training/inference timing for the Planck CAE (10.6 s training; ~8,000 patches/s) is unusually short for 1.1M parameters and 2×10^5 patches unless only a few epochs were run. The number of epochs is not stated here (only “converged at val loss=0.4437”).
Required fix: State the number of epochs actually trained and the stopping criterion used for the Planck CAE in Sec. III.F or Table V to make the timing reproducible.

P3-m8 (Sec. V.a, p. 11)
Problem: The mapping from the bias-ratio estimate to the Fisher coefficient c is not fully specified. You note “verified positive via 5-α refit,” but do not list the α grid or the χ2/likelihood used for the fit.
Required fix: Add the α grid values used to fit c and the goodness-of-fit metric (or place them in the repository and cite the file).

NITS

P3-n4 (Sec. IV.B, p. 10)
Problem: “We note that the absence of Galactic latitude correlation is a necessary but not sufficient condition…” Good caveat, but “Spearman r=0.0005, p=0.92” is given without an explicit N (number of pixels). Given the pixel-count ambiguity (P3-E11), this should be included.
Required fix: Add the number of pixels used for these correlation tests and confirm that they employ the same mask as the χ2 test.

P3-n5 (Sec. III.F, p. 6)
Problem: “Top-200 native anomaly patches (score range [0.558, 0.621]) form the catalog’s Planck CMB tier” — add units/axis name in-line or parenthetically (see P3-E10).

Explanation
This fresh pass focused on arithmetic consistency, figure-caption alignment, dimensional definitions, cross-reference integrity, null-procedure comparability, and abstract fidelity. The most significant new issues are (i) contradictory σ(fNL) baselines and forecasting frames between Appendix C and Sec. V, (ii) the CMB tier’s non-canonical “score” that violates the paper’s single S definition and undermines cross-survey comparability, (iii) an incompletely specified HEALPix/χ2 setup whose degrees of freedom do not match Nside without a stated mask, and (iv) incoherent percentile claims for small S thresholds given the stated z-scoring. Addressing these will materially improve reproducibility and internal consistency.
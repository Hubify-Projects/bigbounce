# P3 R23conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.80.pdf` md5=03f05e26 pages=23
**Input format**: TEXT + web search + pass-2 self-critique (12676 chars)
**Wall time**: 103.0s

---

P3-E1 (ESSENTIAL)  
Section: Abstract, p.1  
Problem: The abstract states “The point-source tier is ∼ 141× the size of the largest prior single-survey anomaly catalog ; the DESI-only subset (195,829 anomalies) is a ∼ 73× like-for-like increase.” There is no quantitative comparison in  in the paper text to verify these exact factors; they are derived from combining the present work’s numbers with Liang et al.’s reported 2,685 anomalies over DESI EDR spectra. This is an inference, not a quoted statistic from  itself, and it is not explicitly documented in the body with a transparent calculation.  
Required fix: In Section I or III.A, explicitly derive these factors from the numbers in  and this paper (e.g., “Liang et al.  report 2,685 anomalies; our 378,080-point-source catalog is 378,080 / 2,685 ≈ 141× larger; DESI-only 195,829 / 2,685 ≈ 73×.”). Clarify in the abstract and body that these are *derived ratios based on their quoted counts*, not statistics taken directly from ’s tables. If any assumption about “like-for-like” selection deviates from ’s selection, state it explicitly or weaken “like-for-like”.

P3-E2 (ESSENTIAL)  
Section: Abstract & Throughout, p.1 and later cosmology sections  
Problem: Multiple sigma significances from different procedures are juxtaposed without always making their non-comparability explicit at each juxtaposition. Examples include:  
- Abstract: “σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at < 1σ; σ(fNL)std = 8.98 single-tracer baseline). A NANOGrav 15-yr KDE free-spectrum MCMC yields γ = 2.567 ± 0.382; the matter-bounce prediction γ = 3.0 sits at +1.13σ and SMBHB γ = 4.33 at +4.61σ.”  
These σ’s refer to different parameters (fNL forecast error, γ posterior width) and different statistical objects (forecast Fisher errors vs posterior parameter shifts), yet they are presented in a single compressed narrative without an explicit “not directly comparable” caveat right there.  
Required fix: Wherever sigma-based significances from different null procedures or parameters are placed side by side (e.g., Abstract, §V, §V A), add explicit language stating that these σ values are *not directly comparable*, because they arise from different quantities and statistical frameworks (forecast Fisher error vs posterior parameter shift from PTA). Examples: “…this 7.9% change in σ(fNL)std is a *forecast* and not directly comparable to the σ significances quoted for the PTA spectral index,” or split into separate sentences clearly demarcating the contexts.

P3-E3 (ESSENTIAL)  
Section: Abstract, p.1; Section V, p.12–13  
Problem: The fNL forecast claims “An empirical Landy–Szalay bias measurement…inserting this into the Fisher-positivity-respecting form 1/σ(fNL )2 = F0 + c α2 gives a central forecast σ(fNL ) = 8.14 with 1σ envelope [3.92, 8.98]…” with “7.9% improvement consistent with no improvement at < 1σ.” The derivation of this “Fisher-positivity-respecting” form is not fully transparent in the main text, and the mapping from αjk to the bracketed interval [3.92, 8.98] is only sketchily justified by a brief remark in §VI D (i). There is potential for confusion: 3.92 is far smaller than 8.14 and 8.98, and the phrase “1σ envelope” suggests a symmetric interpretation, yet this is not a standard 1σ error and readers are left unclear on its construction.  
Required fix: Provide an explicit, fully worked derivation of the mapping from α to σ(fNL), including how F0 and c are obtained, how the “1σ envelope” [3.92, 8.98] is computed from αjk = 0.19 ± 0.65, and why this envelope is highly asymmetric. Clearly distinguish: (a) the central *forecast* (σ(fNL) = 8.14) from (b) the range over α-jk’s 1σ interval producing σ(fNL) ∈ [3.92, 8.98]. Rephrase “1σ envelope” to something like “range of forecasts corresponding to αjk ± 1σ” and state explicitly that this is not the posterior 1σ error on fNL, but a propagated uncertainty in the forecast due to α. The abstract must be updated so that this subtlety is not compressed into a misleading shorthand.

P3-E4 (ESSENTIAL)  
Section: Abstract, p.1  
Problem: The abstract states “The NANOGrav 15-yr KDE free-spectrum MCMC yields γ = 2.567 ± 0.382; the matter-bounce prediction γ = 3.0 sits at +1.13σ (marginally consistent) and SMBHB γ = 4.33 at +4.61σ (Savage-Dickey BMB/SMBHB = 7.1×103).” While  is correctly cited as the NANOGrav 15-year gravitational wave background detection, it does *not* provide these bounce-specific Bayes factors or γ-values for this particular KDE-powered free-spectrum template analysis; these are new results. Yet the text gives them in a way that could be misread as “quoted from .”  
Required fix: In §V A and the abstract, explicitly label these as *new analyses performed in this paper using the public NANOGrav KDE free-spectrum likelihood*, not as numbers from . E.g., “Using the public NANOGrav 15-year HD-correlated KDE free-spectrum product , *we perform a new 2-parameter MCMC fit* and obtain γ =…; the corresponding Bayes factor is …” Make the distinction from NANOGrav’s own published parameter fits explicit, including that your priors differ and that the reported Bayes factor is your computation, not theirs.

P3-E5 (ESSENTIAL)  
Section: §II.B, Eq. (2), p.2–3  
Problem: Definition of S(x): “S(x) ≡ (MSE(x) − µval)/σval” with the claim “For DESI DR1, µval ≈ 0.0287 (validation MSE) and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143…” implies σval ≈ (0.143 − 0.0287)/5 ≈ 0.0229. However, earlier they implicitly treat σval as the empirical standard deviation of MSE on the validation set. There is potential internal inconsistency: either σval is *defined* as the sample standard deviation of the validation MSE, or it is tuned ad hoc to locate S = 5 at a particular MSE. Both cannot simultaneously be true without further clarification.  
Required fix: Clarify the definition: explicitly state whether σval is the empirical std-dev of the validation MSE distribution or an adjusted scale chosen so that S = 5 corresponds to a particular MSE. If it is empirical, remove or appropriately qualify the “is set such that…” sentence; if it is tuned, do not call it the standard deviation. PRD requires unambiguous definitions.

P3-E6 (ESSENTIAL)  
Section: §III.A, DESI DR1 anomaly rates and per-class percentages, p.3–4  
Problem: The anomaly rate is given as 195,829 / 22,504,897 = 0.87%; galaxies flagged at “∼ 20× the rate of QSOs (0.75% vs. 0.037%).” These ratios should be recomputed from the provided numbers. The galaxy and QSO counts underlying these rates are not shown, and thus a reader cannot verify the ratios from the text. When percentages are central to results, they should be tied to explicit counts.  
Required fix: Provide the actual galaxy and QSO anomaly and total counts (e.g. “Ngal,anom / Ngal,total, NQSO,anom / NQSO,total”) so that the 0.75% and 0.037% rates and the factor ~20 can be verified. Ensure rounding is consistent; if exact factor is, say, 20.3, note “~20”.

P3-E7 (ESSENTIAL)  
Section: §III.C, SDSS DR18, p.5–6; Table I, p.8–9  
Problem: There is a complex use of thresholds and slices for SDSS (canonical S > 5 on DESI-scale gives 12 objects; but the SDSS headline of 77,905 uses a “fixed-size continuity slice at S ≥ 0.1060 (4.05%)”). The top-1% SDSS proper is 19,253 objects at S ≥ 0.2051. However, in Table I Nanom for SDSS is 77,905 with Rate 3.38% but footnote ♡ explains this is a cross-transfer count superseded by native retrains, while the Path-C native counts appear only in text. As written, Table I is confusing and conflates cross-transfer and native counts; a casual reader will likely misunderstand which numbers are final.  
Required fix: Redesign Table I to include two explicitly separated blocks or columns: “Cross-transfer (historical)” and “Path-C native (canonical)” for each survey, with clear labels and no reuse of the same Nanom header. For SDSS, list: Ntotal (native rescored 1,925,279); Nanom (S > 5: 12); Nanom (top-1%: 19,253); Nanom (4.05%-slice: 77,905). Use a separate column for the “headline continuity slice used in deduplication” and clearly mark this as methodological, not the survey’s intrinsic anomaly rate. The abstract’s 77,905 number must be labeled consistently as continuity-slice rather than “anomaly count” tied to a physical threshold.

P3-E8 (ESSENTIAL)  
Section: §III.D, LAMOST DR10/Path-C description; Table I & text, p.6–7, p.8–9  
Problem: The LAMOST description mixes cross-transfer and native-retrain counts in a way that is hard to follow: cross-transfer Nanom = 44,075 (0.39%) is in Table I; text later says Path-C native rescoring gives 2,054 anomalies at S > 5 and defines a “top-113,342 native slice at S ≥ 0.4613”, called “genuine top-1% cut (113,342 of 1.13 × 10^7)”. However, these numbers are not in the main Table I, and the phrasing “genuine top-1% cut” can be misread as the canonical anomaly rate, although the paper later dismisses most of the LAMOST tier as training-bias artifacts.  
Required fix: As for SDSS, explicitly structure the LAMOST entry with separate rows or clearly delimited bullets: (i) cross-transfer Nanom and rate (historical); (ii) native S > 5 Nanom and rate; (iii) top-1% Nanom used as exploratory tier. Flag in the table that the 113,342 top-1% tier *is not recommended* for science, and that the canonical catalog-grade set excludes this tier. Also, the abstract must be consistent: if “point-source tier” 378,080 excludes the LAMOST exploratory tier, provide the exact point-source count without LAMOST and with it, and ensure all numbers match when recomputed.

P3-E9 (ESSENTIAL)  
Section: §IV.A, SIMBAD cross-match; Fig. 6, p.10–11  
Problem: The “∼ 17.8% genuine novelty fraction” is based on 178/1,000 objects at the DESI top-1,000 score stratum, cross-matched against 20 catalogs. This is correctly described as a single-sample point estimate. However, in the abstract and multiple places it is written as if this number characterizes the catalog more broadly, without *explicitly* restating at each use that it only applies to the top-1,000 DESI anomalies and not to the full 378k catalog.  
Required fix: In the abstract and any headline statements, always qualify 17.8% as “for the DESI top-1,000 anomalies at the highest-score stratum; no statement is made about the full catalog.” Consider rephrasing the abstract sentence to: “Extended archival cross-matching of the top-1,000 DESI anomalies… yields a genuine novelty fraction of ∼17.8% *in this highest-score subsample*; we do not attempt to generalize this rate to the full catalog.” This is necessary to avoid overgeneralization.

P3-E10 (ESSENTIAL)  
Section: §V.A & Appendix E, PTA analysis, p.13–14, p.18–19  
Problem: The PTA analysis uses NANOGrav’s public KDE free-spectrum likelihood but does not explicitly specify the form of the likelihood function used, any approximations relative to the original PTA analysis (e.g., whether off-diagonal covariances and HD correlations are fully retained in the KDE interpolation), or how the Savage-Dickey ratio is computed in detail (kernel bandwidths, evaluation grid). PRD typically requires enough methodological detail for an independent researcher to reproduce the statistical computation from the likelihood description alone; merely stating “we use emcee with these priors” is insufficient.  
Required fix: Expand Appendix E to specify: (1) the exact form of the likelihood L(γ, A | KDE product), including whether it is taken directly from the provided KDE interpolant or re-constructed; (2) the precise formula used for the Savage–Dickey density ratio and how the densities at γ = 3.0 and γ = 4.33 are evaluated from the chain (e.g., kernel-density estimator with specified bandwidth). Add a note comparing qualitatively with the main NANOGrav analysis to confirm that your inference is consistent in the overlapping parameterization. This will make the Bayes factor reproducible.

P3-M1 (MAJOR)  
Section: Bibliography entries [1]–, , , –, pp.22–23  
Problem: Citation metadata needs tightening to meet PRD standards. For instance:  
- [1] “The DESI Data Release 1,” 2025, “DESI DR1 documentation.” This is missing journal information; DR1 is normally documented in an ApJS or arXiv paper with a full author list (DESI Collaboration), arXiv ID, and journal reference. Similarly, [4] “The SRG/eROSITA All-Sky Survey: The first X-ray all-sky survey in the 21st century,” Astron. Astrophys. 682, A34 (2024) appears plausible but should be cross-checked against ADS for volume/page correctness; the exact volume and page (682, A34) must match the official reference.  Nicolaou et al. is dated “arXiv:2506.17376 (2026)”—this is a *future-dated* arXiv ID relative to submission date if the ID syntax is incorrect or not yet live; the “2506” yymm pattern corresponds to June 2025, not 2026. The metadata “(2026)” is suspicious and likely erroneous.  
Required fix: For every reference:  
- Provide full and correct citation: exact title, journal, volume, page, year, and arXiv identifier where applicable, verified against arXiv.org and NASA ADS.  
- Remove future year mismatches: ensure  “arXiv:2506.17376 (2026)” uses the correct year consistent with the arXiv timestamp (probably 2025). If the arXiv ID does not exist, this is an invalid citation and must be corrected or removed.  
- For survey documents (DESI DR1, LAMOST DR10, Gaia DR3, NEOWISE Year Ten, Planck 2018 results, ACT DR6), cite their official survey papers with DOIs, not generic “documentation” statements.  

P3-M2 (MAJOR)  
Section: Abstract & §III, p.1, p.3–7  
Problem: Length vs contribution. The paper runs 23 pages and devotes substantial space to operational details, gate narratives, and internal auditing (Path-C, Jaccard, injection tests, etc.). While methodological rigor is commendable, the main scientific contributions—actual astrophysical anomalies, any new classifications, and cosmological implications—occupy a relatively small fraction of the text. The cosmological applications are by the author’s own admission “illustrative” and not detections. PRD expects the narrative to focus on physics rather than internal QA logs.  
Required fix: Consider condensing the Path-C audit and computational pipeline into a more concise Methods + one dedicated validation section, moving most of the “Path-C residual caveats” and extended gate-result narratives to a supplementary document. The main text could reasonably be reduced to ~15–17 pages by trimming redundant re-descriptions of thresholds and gates, while retaining the essentials of the anomaly catalog, key astrophysical examples, and the cosmology forecasts.

P3-M3 (MAJOR)  
Section: Figures 3, 6, 9, 10, 11, 12 and related text, various pages  
Problem: Some figures are borderline “filler” or at least not optimally used. For example, Fig. 6 (SIMBAD-unmatched fractions) largely restates numbers that are already in text and uses a horizontal bar plot with a dashed line whose quantitative value is less central than the explanation text. Fig. 11 (shot-noise sensitivity) uses σ(fNL) values in a different normalization from the main forecast, which risks confusion. Fig. 12 (taxonomy gallery) is visually appealing but shows only one object per family and is more appropriate for a data-release note than a PRD article unless the taxonomy is central to a physics argument—which it is not.  
Required fix: Either (a) justify each figure explicitly as supporting a physics point (e.g., show how anomaly classes map into specific bias regimes for the fNL forecast), or (b) move less essential figures (especially taxonomy gallery and duplicate stylistic plots of σ vs. α or n̄) to an online supplement. Ensure the remaining figures all have clear physics conclusions that are not already obvious from tables/text.

P3-M4 (MAJOR)  
Section: §II.C, GPU inference pipeline, p.3  
Problem: The detailed wall-clock times, batch sizes, pod restarts, and I/O anecdotes (e.g., “single ∼11 h pod-restart-with-resume after a network blip during the SDSS pass”) are not necessary for PRD-level documentation and obscure the core methodological content.  
Required fix: Compress this section to the key reproducible parameters—GPU type, batch size, approximate throughput per survey—and remove narrative elements about network glitches. If resource usage is relevant (e.g., to argue feasibility), tabulate only essential metrics in Table V and drop anecdotal timing text.

P3-M5 (MAJOR)  
Section: §VI.C Limitations, point (7), p.15–16  
Problem: The unweighted MSE score is acknowledged as suboptimal (no inverse variance weighting), yet the paper stops at pointing to the injection gate as addressing this. For PRD, where the robustness of anomaly metrics can influence cosmological inferences, this is thin; especially for DESI spectra where per-pixel variance is known and standard.  
Required fix: At minimum, include a quantitative test on a subset (e.g., 10^5 DESI spectra) comparing rankings obtained with unweighted MSE vs inverse-variance weighted χ^2, including a correlation coefficient and a discussion of any systematic shifts in high-scoring anomalies. If that is impractical for the current submission, explicitly limit any cosmological claims to a qualitative, exploratory status and state that robust cosmological exploitation will require re-analysis with variance-weighted scores.

P3-N1 (MINOR)  
Section: Abstract & §I, “largest-scale” and “largest multi-archive anomaly search”, p.1, p.16–17  
Problem: Claims of “largest-scale application”, “largest multi-archive anomaly search reported to date” and “∼ 141× the largest prior single-survey anomaly catalog” require careful support. There may be other large-scale ML anomaly searches in the literature or in survey collaboration internal work that are not cited.  
Required fix: Qualify these claims as “to our knowledge” and ensure that [10–12] indeed represent the largest previously published anomaly catalogs in peer-reviewed literature. Otherwise, narrow the statement to “largest for DESI-like spectroscopic surveys” or similar.

P3-N2 (MINOR)  
Section: Throughout, referencing SDSS DR18 vs DR16 & cross-matches, e.g., §IV.A, p.10–11  
Problem: The cross-match uses “SDSS DR12/DR16” while the main spectroscopic survey is DR18 [3]. It is not entirely clear why these particular DRs were selected for cross-matching and whether including DR18 itself changes the archival ID rate.  
Required fix: Briefly justify the choice of SDSS DR12/DR16 in the 20-catalog X-match list and state whether including DR18 spectra/photometry would change the 82.2% archival-identification rate.

P3-N3 (MINOR)  
Section: Appendix A, Planck row of Table V, p.18  
Problem: The footnote notes that “an earlier draft listed 10.6 s, which is inconsistent… and has been withdrawn.” This is internal version-history language about drafts, which PRD generally discourages in the final text.  
Required fix: Remove reference to “earlier draft” and simply state the current best estimate; if the precise training wall-clock is not available, say “training wall-clock was not recorded” without referencing draft history.

P3-N4 (MINOR)  
Section: §II.D Step 6 and §IV.C, deduplication radius sweep, p.4, p.11  
Problem: The dedup-radius sweep (3″, 5″, 7″) is well-documented; however, the text claims “maximum unique-count variation of 0.086% relative to the canonical 5″ result” without showing the intermediate values in a concise table. While numbers are present in prose (378,604 / 378,280 / 378,145), this is harder to parse.  
Required fix: Add a short one-line table with Rmatch and Nunique, and explicitly compute the percentage differences in that table, so readers can immediately verify the 0.086% number.

P3-N5 (MINOR)  
Section: §III.E, eROSITA DR1, p.6–7  
Problem: The statement “IsolationForest cross-validation: 284/298 = 95.3% of the canonical-S top-298 are in the IF top-9,303 — a descriptive internal-consistency overlap, not independent confirmation, since the IF is trained on the 16-d BigAE latent…” is careful but could still be misread as endorsing IF as validation.  
Required fix: Add one clarifying sentence: “Because the IF is trained on the same latent representation, this overlap does *not* validate the BigAE anomalies independently; it only checks internal consistency of the joint detector pipeline.”  

P3-N6 (MINOR)  
Section: §V, “SPHEREx 3–5σ detection” wording, p.12–13  
Problem: “The matter-bounce prediction … is testable at 3–5σ with SPHEREx” could be interpreted as a robust forecast, yet the specific configuration and systematics leading to 3 vs 5σ are not fully detailed.  
Required fix: Add a qualifier such as “under optimistic assumptions about systematics similar to those in Heinrich et al. ” and, if possible, give a simple approximate Fisher computation or reference that directly supports the 3–5σ range.

P3-N7 (MINOR)  
Section: Acknowledgments and Data Availability, p.17–18  
Problem: The HuggingFace and GitHub URLs are included in plaintext. PRD sometimes prefers URLs in footnotes or in supplementary materials, and these repositories should be fully stable and citable (e.g., with DOIs via Zenodo).  
Required fix: Ensure that all data and code repositories are archived with DOIs and update references to include those DOIs, possibly moving the raw URLs to a footnote or supplemental material.

P3-N8 (MINOR)  
Section: §III.B, high-z QSO candidates, p.5  
Problem: Redshift range “z = 6.0–6.23” and sub-score values rZ ≈ 3.9 are given, but there is no explicit mention of whether these redshifts are pipeline values or re-fits, and no uncertainty is quoted.  
Required fix: Clarify that redshifts are from the DESI Redrock pipeline (or from custom fits) and, if possible, quote typical uncertainties or at least state that they are approximate. This matters given the high-z claim.

P3-N9 (MINOR)  
Section: §IV.B, χ^2 uniformity test, p.10–11  
Problem: The spatial χ^2 test uses 38,330 HEALPix pixels, giving χ^2ν = 3.76, but the binning includes many low-count cells where asymptotic χ^2 approximations are poor. This is not acknowledged.  
Required fix: Add a caveat that the χ^2 test is approximate due to low counts per pixel in many bins, and emphasize that it is not used to claim statistically rigorous clustering, only to illustrate non-uniformity dominated by survey footprints.

P3-N10 (MINOR)  
Section: §III.G, Gaia DR3, p.7  
Problem: The variance in terminology around “variable-axis injection” and “variability IF” could confuse readers; it is not immediately clear which Gaia-derived variables are used and whether any period/amp parameters are included.  
Required fix: Briefly list the Gaia DR3 features used (e.g., mean G, BP–RP, variability amplitude, etc.) and specify which feature(s) the injection is performed along.

P3-N11 (MINOR)  
Section: §III.H, NEOWISE, p.7; Fig. 5  
Problem: The NEOWISE top anomaly has “Score = 11.5” but the caption does not specify whether this score is canonical-S or some alternate metric.  
Required fix: State explicitly “canonical-S anomaly score S = 11.5” in the caption so it is clear that this is the same scoring definition used throughout.

P3-N12 (MINOR)  
Section: §III.B & §Appendix B, taxonomy vs arm dominance, p.5, p.18  
Problem: There is some mild redundancy between DESI “high-z QSO candidates” and later the taxonomy plus arm-dominance classification; the reader must cross-reference multiple sections to understand how many of the 12 high-z candidates fall into which family and dominance category.  
Required fix: Include a short statement in §III.B summarizing how these 12 objects are categorized in the later taxonomy (e.g., all in the “High-z QSO” family, all Z-dominant, etc.), or add a small table listing their family and S scores.

P3-N13 (MINOR)  
Section: §II.D, Step 5, injection-recovery description, p.3–4  
Problem: “500 planted signals per survey at six amplitude levels (0.5–20×σ)” is concise, but there is no explicit statement of how these plants are distributed in wavelength/frequency space for spectra (random positions? restricted to line-free regions?).  
Required fix: Add one sentence specifying how injection locations are chosen and whether overlapping with strong emission lines is allowed. This affects interpretation of the recovery rates.

P3-N14 (NIT)  
Section: Throughout  
Problem: A few minor typographical issues:  
- “foregound” appears once as “foreground” (check carefully).  
- Traces like “Landy–Szalay” vs “Landy– Szalay” are inconsistent.  
Required fix: Run a careful spellcheck and ensure consistent hyphenation and accent usage for names and technical terms.

P3-N15 (NIT)  
Section: §III.C, caption of Fig. 4, p.7  
Problem: “score > 5.0” in the burned-in panel title is said to refer to a DESI-trained cross-transfer score axis while the paper has switched to native SDSS scores for Path-C; this can confuse readers who see the figure out of context.  
Required fix: Add a note in the caption: “The ‘score > 5.0’ label refers to the DESI-trained cross-transfer score used in the initial baseline; the native SDSS Path-C scores are lower and not shown here.”

P3-N16 (NIT)  
Section: §V.A, “decisive on Jeffreys’ scale”, p.13–14  
Problem: The Jeffreys terminology is correct, but some readers find “decisive” too qualitative.  
Required fix: Consider adding the corresponding ln B or σ-equivalent for context, or simply say “log10 B = 3.85, which Jeffreys classifies as ‘decisive’.”

P3-N17 (NIT)  
Section: §VI.F, “Implications for Bounce Cosmology”, p.16  
Problem: The sentence “The NANOGrav spectral index γ = 2.567 ± 0.382 is marginally consistent with the bounce prediction γ = 3.0 (+1.13σ) while strongly disfavoring SMBHB (+4.61σ). Neither constitutes a detection.” is correct but slightly rhetorically strong.  
Required fix: Consider softening to “These values are consistent with the bounce prediction within 1.2σ and disfavor the simple SMBHB index at ≈4.6σ. We emphasize that this is a 2-parameter template analysis on a processed likelihood and does not constitute a full PTA model comparison.”

## Summary recommendation  
MAJOR REVISIONS  

The paper is ambitious and thorough in internal auditing and offers a large, well-documented anomaly catalog with interesting cosmological applications. However, for PRD standards, the treatment of some key statistics (fNL forecast envelope, novelty fraction, PTA Bayes factors) needs clearer derivations and more precise language to avoid overinterpretation. The mixture of cross-transfer vs native thresholds and counts must be reorganized to prevent confusion, and the bibliography contains at least one problematic arXiv/year combination and several incomplete survey references. With these essential and major issues addressed, the work could become a strong methodological contribution, but in its current form it requires substantial revision before it is suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P3-E11 (ESSENTIAL)  
Section: §III.A & §IV.A, DESI DR1 anomaly counts vs SIMBAD cross-match, p.3–4, p.10  

**Problem (arithmetic / consistency):** The paper repeatedly quotes a **“DESI DR1 ∼99% SIMBAD-unmatched”** rate, but the only explicit DESI SIMBAD cross-match actually described is for the **top-10,000 anomalies**, where **0.2%** (∼20/10,000) have SIMBAD entries.[p.3–4][p.10] That indeed implies 99.8% unmatched in that top-10k subset, but nowhere is a SIMBAD cross-match reported for the full 195,829-object DESI anomaly catalog. The abstract and Fig. 6 bar (“DESI DR1 (top 10K)”) are easy to misread as characterizing DESI as a whole, not a restricted subset.[p.1][p.10]  

**Required fix:**  
- Explicitly state **in every place the DESI SIMBAD fraction is quoted** that this ∼99–99.8% unmatched rate refers **only to the top-10,000 anomalies**, not to the full DESI anomaly catalog.  
- Either (a) remove any implication that the full 195,829-object DESI list has been cross-matched to SIMBAD, or (b) actually perform that cross-match and report the global fraction.  
- In Fig. 6 and accompanying text, make the “(top 10K)” qualifier visually / textually prominent and repeat in the caption that **no statement is made about SIMBAD coverage for all DESI anomalies**.  

---

P3-E12 (ESSENTIAL)  
Section: §II.B (“σval is set such that…”) vs §III.C, Fig. 3 right panel, p.2–3, p.6  

**Problem (arithmetic / definition mismatch):** Equation (2) defines **S(x) = (MSE(x) − µval)/σval**, with **µval, σval** the validation-set mean and standard deviation.[p.2] For DESI DR1 they specify **µval ≈ 0.0287** and then say **“σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143”**.[p.3] This implies σval ≈ (0.143 − 0.0287)/5 ≈ 0.0229, which is not necessarily the empirical standard deviation of the validation MSE. Later, the SDSS cross-transfer anomalies are described as reaching **S ≈ 1.9 × 10¹¹**.[p.6] If S is truly standardized by an empirical σval of order 10⁻², values of 10¹¹ correspond to catastrophically enormous MSEs and numerically unstable scaling; if σval was instead manually tuned or renormalized, then for SDSS S is no longer a pure “z-score” in the statistical sense. The text never reconciles these two uses (empirical std-dev vs hand-chosen scale), leaving S ill-defined for non‑DESI surveys.  

**Required fix:**  
- In §II.B explicitly separate the **DESI** definition of σval (empirical std-dev of the DESI validation MSE distribution) from the **cross-transfer SDSS/LAMOST** score scale. If the SDSS and LAMOST S values were obtained with a different (e.g. rescaled or numerically stabilized) σval, specify that and give the numeric σval used.  
- Clarify that **the extreme SDSS S values up to 10¹¹ are artifacts of the DESI‑trained cross-transfer scale**, not interpretable as literal “z-scores.” Either re-label that axis (e.g. “rescaled MSE proxy S̃”) in Fig. 3 right panel, or explicitly note that these values are **off the calibrated z-scale**.  
- Ensure that all uses of “z-scored” and “standardized” are accurate: if σval is not the empirical standard deviation, do not refer to S as a z-score in the strict statistical sense for those surveys.  

---

P3-E13 (ESSENTIAL)  
Section: §V, §V A vs Appendix C & Appendix E, σ(fNL) and γ error normalizations, p.12–14, p.17–19  

**Problem (null-procedure comparability + normalization):** The paper uses **two different σ(fNL)** normalization schemes:  
- Main-text Fisher forecast in §V with **σ(fNL)std = 8.98** and multi-tracer σ(fNL) ≈ 8.14.[p.12]  
- Shot-noise figure (Fig. 11) and Appendix C with a different internal baseline **σ(fNL)std = 16.85** and dense-limit multi-tracer σ(fNL) = 11.71.[p.19]  

Although Fig. 11’s caption notes that these are “internal to the shot-noise Fisher implementation” and “not on the same absolute normalization,” the body of §V does not clearly restate this caveat when referencing the shot-noise sensitivity, so a reader could incorrectly compare percentages or absolute σ values across the two frameworks.[p.12–13][p.17–19]  

Similarly, in §V A the γ posterior is summarized both as **γ = 2.567 ± 0.382 (Gaussian)** and as **γ = 2.591\(_{-0.287}^{+0.291}\)** (68% CI), and the ±0.382 is then used as the denominator for the “+1.13σ” and “+4.61σ” shifts, even though this is not the same uncertainty as the half-width of the quoted credible interval.[p.13–14] The paper acknowledges the non-Gaussianity in passing but does not explicitly state that the “σ” used for shifts is **not** the CI half-width.  

**Required fix:**  
- In §V when discussing Fig. 11 and Appendix C, explicitly insert language such as: “**These σ(fNL) values use a separate, simplified Fisher normalization and are not directly comparable in absolute terms to the σ(fNL)std = 8.98 baseline used in the main DESI forecast; only the *relative* percentage changes are comparable.**”  
- In §V A, immediately after giving both γ summaries, add a sentence clarifying: “**The +1.13σ and +4.61σ shifts are computed using the posterior standard deviation 0.382, not the half-width of the 68% credible interval, and therefore are not exactly equivalent to rescaling the quoted [2.304, 2.882] interval.**”  
- When γ and σ(fNL) significances appear in the same paragraph (abstract and §V A), reiterate that their “σ” units arise from different underlying distributions (Fisher forecast vs MCMC posterior) and should not be mixed quantitatively.  

---

P3-M6 (MAJOR)  
Section: §III.A & §IV.B, χ² spatial uniformity test and HEALPix counts, p.10–11  

**Problem (arithmetic / interpretation):** The spatial-uniformity test uses **38,330 HEALPix pixels (Nside = 64)** and reports **χ² = 143,936** with **dof = 38,329**, giving **χ²ν = 3.76**.[p.10–11] For Nside = 64 the total number of HEALPix pixels on the sky is **12 × 64² = 49,152**; the use of 38,330 pixels implies masking, but neither the sky fraction nor the exact mask is stated. Without specifying which pixels are included, what expected counts per pixel were used, or how the mask interacts with the per-survey footprints, χ²ν = 3.76 is only weakly interpretable. The text then briefly notes this is “dominated by inhomogeneous footprints,” but the test is still presented as a global spatial-uniformity check in a way that could be misread as evidence of astrophysical clustering.[p.10–11]  

**Required fix:**  
- Explicitly state how the **38,330 pixels** are selected from the 49,152 Nside = 64 pixels (e.g. “pixels with survey coverage above a threshold f\_sky”).  
- Briefly specify the **expected-count model** used in the χ² test (uniform over the retained pixels, or weighted by survey exposure/footprint?).  
- Strengthen the caveat: add a sentence noting that **because the χ² test does not incorporate the detailed angular selection functions of each survey, χ²ν = 3.76 should not be used to infer intrinsic clustering**, and that the main robust results are the null correlations with latitude and dust.  

---

P3-M7 (MAJOR)  
Section: §III.B, high‑z QSO candidates and per-arm scores, p.5  

**Problem (internal consistency / clarity):** High‑z QSO candidates are selected requiring **r\_Z > r\_B, r\_Z > r\_R** and total **S > 5**, with 12 such objects reported.[p.5] Example per-arm sub-scores for two objects are given (r\_Z = 5.30, 5.18) and a mean ⟨r\_Z⟩ ≈ 3.9, but **no total S values are shown** for those objects. Because Eq. (2) defines S from the full-spectrum MSE, and sub-scores r\_B, r\_R, r\_Z are “per-band contributions” with no explicit formula linking them back to S (additive? weighted? normalized independently?), a reader cannot verify that these candidates in fact satisfy **S > 5** or how much of S is driven by the Z-arm. The incomplete definition risks confusion about whether r\_Z is on the same standardized scale as S, or uses a separate normalization.  

**Required fix:**  
- Explicitly define how **r\_B, r\_R, r\_Z** are computed (e.g. “band-restricted MSE normalized by the same µval, σval” or another scheme) and state whether they share the same units as S.  
- Provide at least one explicit **worked example** giving both (r\_B, r\_R, r\_Z) and S for a high‑z candidate.  
- Clarify whether the **Z-arm dominance** criterion is applied in raw band MSE, in standardized band scores, or in some other metric. This will make the selection reproducible and resolve ambiguity about the relationship between S and the per-band sub-scores.  

---

P3-N6 (MINOR)  
Section: §III.C & Table II vs Fig. 3, SDSS emission-line categories and “ultra-cool dwarfs,” p.6–7, p.8–9  

**Problem (figure–text coherence):** SDSS DR18 cross-transfer anomalies are described as being dominated (∼84%) by **ultra-cool dwarfs M7–T2**.[p.6][Fig. 4 caption] Table II then gives an emission-line taxonomy in which the largest categories are **“Uncategorized” (52.7%)** and **“NIR excess / high‑z” (33.0%)**, with no explicit “ultra-cool dwarf” bin.[p.8] While the text explains that “uncategorized” is an internal residual-pattern label, a casual reader may struggle to see how the 84% M7–T2 figure maps onto these taxonomy categories, especially since Fig. 3’s SDSS panel is primarily about score distribution.  

**Required fix:**  
- Add a brief clarifying sentence in §III C or under Table II explicitly linking the **M7–T2 fraction** to specific taxonomy classes, e.g., “Most of the ultra-cool dwarfs fall into the ‘Uncategorized’ and ‘NIR excess / high-z’ residual categories; the 84% cool-dwarf fraction is derived from a separate spectral-type classifier, not from the emission-line taxonomy alone.”  
- Optionally, note in Fig. 4’s caption that the physical-class labels derive from a different classifier than the Table II residual classes, to prevent the impression that the two sets of labels are inconsistent.  

---

P3-N7 (MINOR)  
Section: §II.D Step 6 vs Appendix F, deduplication “8-way-with-ACT” variant, p.4, p.8–9, p.19–21  

**Problem (internal cross-reference):** Step 6 in §II.D mentions that “The 8-way-with-ACT variant (+200 objects, zero positional overlaps) is preserved as a sensitivity-check artifact,” but does not give an explicit number for the **8-way unique-object count**.[p.4] Table I footnote ∥ briefly mentions “388,693 → 388,493” and “378,480 → 378,280,” but without clearly tying these to “with ACT” vs “without ACT” in the main text.[p.8–9] Appendix F later states that including ACT would produce **378,480** unique objects (+200), but a reader must piece together these values from disparate locations.  

**Required fix:**  
- In §II.D Step 6, after mentioning the 8-way-with-ACT variant, explicitly state: “**The corresponding 8-way deduplicated unique-object count would be 378,480 (i.e., +200 relative to the 7-way 378,280 headline).**”  
- Ensure that Table I footnote ∥ explicitly labels these as “8-way (with ACT)” vs “7-way (without ACT)” and that this labeling is echoed once in the body text, so readers do not have to infer which number belongs to which configuration.  

---

NO ADDITIONAL HIGH-SEVERITY FINDINGS in categories B, D, F, G, H, I, J beyond those already captured in P3‑E2, P3‑E3, P3‑E4, P3‑E9, P3‑E10, P3‑M3, and P3‑M5.  

- **B (figure–caption vs body):** For the figures explicitly inspected (Figs. 3, 6, 7, 8, 9, 10, 11, 12), the captions and body descriptions are numerically and conceptually consistent; mismatches are primarily about emphasis/utility (already noted in P3‑M3), not incorrect numbers.  
- **D (internal cross-references):** Checked key \S, table, and appendix references tied to headline claims (Path‑C steps, Jaccard stability, injection tests, Fisher form, PTA likelihood). All point to the intended material; problems are interpretive rather than mispointed.  
- **F (abstract faithfulness):** Every concrete number or claim in the abstract has a corresponding derivation or discussion in the body; the main issues are wording/interpretation (e.g. sigma comparability, novelty scope, “largest” claims) already flagged in P3‑E2, P3‑E3, P3‑E4, P3‑E9, P3‑N1.  
- **G & H (novelty and hedges):** Novelty claims are now mostly qualified (“to our knowledge,” “single-sample point estimate,” etc.); remaining issues are nuance-level and subdominant to those already raised.  
- **I & J (appendix vs main-text; stale numbers):** Checked σ(fNL) baselines, GS sample corrections, and PTA-chain settings between main text and appendices; where different normalizations are used, they are at least qualitatively acknowledged. The new P3‑E13 above addresses the only place where this may still be confusing; no clear evidence of outright stale or contradictory numeric updates was found.
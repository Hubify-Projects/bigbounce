# P3 auto-2026-06-05_1617pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11208 chars)
**Wall time**: 477.1s

---

# Referee Report — Paper P3
**"Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies..."**

## Overall assessment

This is a 20-page manuscript that conflates four distinct projects (a multi-archive anomaly catalog, a multi-tracer $f_{\rm NL}$ forecast, a NANOGrav spectral-index re-fit, and a methodological lessons-learned record) into a single submission. The catalog work is potentially of value as a community data product (analogous to a VAC release), but the load-bearing scientific claims that justify a PRD submission — the cosmological forecast and the bounce/NANOGrav connection — are either consistent with no signal at <1σ or in apparent tension with the original collaboration result. The manuscript also contains broken figure references in three places, a headline arithmetic inconsistency in the abstract, and unredacted internal jargon throughout. This is not a first-pass acceptable submission to PRD.

---

## ESSENTIAL findings (must fix before any further review)

**P3-E1 — Broken figure references in the body (multiple pages).**
Page 2: *"architecture shown schematically in Fig. ??"*; *"(Fig. ??)"* in §II B.
Page 5: *"Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts..."*
These are unresolved LaTeX references in the rendered PDF. The schematic of the BigAE architecture and the high-z QSO candidate gallery are claimed in the body but absent from the figure list. Either supply the figures or remove the claim. PRD does not accept submissions with broken `\ref{}` calls.

**P3-E2 — Arithmetic inconsistency in the headline $\sigma(f_{\rm NL})$ improvement (Abstract, §V, Conclusions).**
Abstract: *"central forecast $\sigma(f_{\rm NL}) = 8.14$ with $1\sigma$ envelope $[3.92, 8.98]$ (7.9% improvement... $\sigma(f_{\rm NL})^{\rm std} = 8.98$ single-tracer baseline)."*
Recompute: $(8.98 - 8.14)/8.98 = 9.35\%$, not $7.9\%$. The 7.9% number would correspond to $\sigma = 8.27$, not 8.14. Either the central value or the percentage is wrong; both appear in the abstract, body, and conclusions. This is a load-bearing headline number that fails internal audit.

**P3-E3 — Bibliography contains internal-bookkeeping prose.**
Reference [33] reads: *"...arXiv:2311.13082 [astro-ph.CO] [publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]"*. This is an internal note that must not appear in the published reference list.

**P3-E4 — NANOGrav posterior is inconsistent with the published NANOGrav 15-yr result and this is not addressed.**
Page 11: $\gamma = 2.567 \pm 0.382$ from the authors' MCMC of the public KDE free-spectrum likelihood. The NANOGrav collaboration's own analysis [18] reports a broader posterior peaked near $\gamma \approx 3.2$. The authors' tight, lower-central-value posterior implies either (a) the model is misspecified (a pure power law on the binned KDE without the HD-correlation kernel, intrinsic-pulsar-noise marginalization, or the correlated-vs-uncorrelated power split that NANOGrav used), or (b) a different likelihood object is being fit. Without explicit reproduction of NANOGrav's own fit on the same product, the +1.13σ "bounce consistency" and +4.61σ "SMBHB disfavor" claims cannot be trusted. The Savage-Dickey $B = 7.1\times10^3$ inherits this same defect and is also a two-model comparison that ignores the full model space NANOGrav considers.

**P3-E5 — Title overclaims scope.**
*"Spectrally Unusual Sources at Scale"* is misleading: 4 of 7 retained surveys (eROSITA, Planck, Gaia, NEOWISE) are not spectroscopic. The eROSITA, Gaia, and NEOWISE catalogs use $\sim$15–47 tabular features, and Planck operates on map patches. The title should reflect the multi-wavelength / multi-data-type scope.

**P3-E6 — "Path-C" is unredacted internal project jargon.**
The term "Path-C" appears in the title, abstract, §II D, §III, §IV, §V, §VI, §VII, and Appendix F. It carries no astrophysical meaning and is undefined except as "the rebuild" with no relation to anything in the literature. PRD readers will have no idea what "Path-C" means. Replace throughout with a descriptive name (e.g., "native-retrain protocol" or "NRP-v1") and remove from the title.

**P3-E7 — Headline "141× the largest prior single-survey anomaly catalog" comparison is contaminated by a tier the authors themselves recommend excluding.**
Abstract: *"point-source tier is $\sim$141× the size of the largest prior single-survey anomaly catalog."* That 378,080 point-source figure includes ~113,000 LAMOST objects which (per the authors' own §III D, §VI A, and Table IV) (a) fail the injection-recovery gate at 5σ, (b) are 98% blue-excess training-bias artifacts, and (c) are explicitly excluded from the recommended catalog-grade subset of ~265,000. The honest comparison is $265{,}000 / 2{,}685 \approx 99\times$, not 141×. The 141× figure must be removed or qualified at every appearance.

**P3-E8 — "Central forecast $\sigma(f_{\rm NL}) = 8.14$" is statistically misleading.**
The measured $\alpha_{\rm jk} = 0.19 \pm 0.65$ is $0.29\sigma$ from zero with 95% CI $[-1.08, +1.46]$. Under a Fisher-positivity form $1/\sigma^2 = F_0 + c\alpha^2$ the data is fully consistent with $\alpha = 0$ (no improvement at all). Calling 8.14 a "central forecast" while the 1σ envelope upper bound equals the baseline 8.98 is a presentational sleight: the more honest summary is "no statistically significant improvement detected at the available S/N; $\sigma(f_{\rm NL}) \in [3.92, 8.98]$ at 1σ." The "7.9% improvement" framing should be removed from the abstract or replaced with "consistent with zero improvement at < 1σ" as the headline, not as a parenthetical.

---

## MAJOR findings

**P3-M1 — Threshold inconsistency across surveys breaks any uniform interpretation of the catalog.**
Table I uses S > 5.0 for DESI (anchored to validation MSE), top-1% for SDSS/LAMOST/Planck/Gaia/NEOWISE (data-driven percentile), and a different score-knee for eROSITA. The text concedes that applying S > 5 to SDSS yields only 12 objects (vs. headline 77,905) and to LAMOST only 2,054 (vs. headline 113,342). The catalog therefore mixes objects selected by criteria that differ by factors of $10^3$–$10^4$ in stringency, and the "1.01%" aggregate rate in Table I is a meaningless average. Either pick one threshold philosophy and re-run everything, or replace the aggregate rate with per-survey rates only.

**P3-M2 — 200 Planck CMB sky-region patches are summed with 378,080 point-source detections in the headline.**
The repeated "378,080 + 200 = 378,280" stratification is acknowledged in the paper, but the headline 378,280 is then quoted in the title, abstract, and conclusions as if it were a single number. Map patches are not objects; they should be reported as a separate quantity and not added to the point-source count. This is the same defect ACT was quarantined for, only with Planck retained.

**P3-M3 — The single-tracer baseline $\sigma(f_{\rm NL})^{\rm std} = 8.98$ is not justified.**
Published DESI QSO single-tracer constraints (e.g. the kSZ tomography and BAO/RSD literature) are much weaker than 8.98 for the data volume covered here. Where does 8.98 come from? No covariance, no $k_{\max}$, no survey volume, no $\bar n$ used to derive $F_0 = 1/8.98^2$ are quoted in the body. Without this, the entire forecast is unverifiable.

**P3-M4 — Fig. 7 caption claims PASS for Planck and NEOWISE but neither appears in the figure legend.**
The legend lists six curves (SDSS continuum-dip, SDSS emission-line, LAMOST continuum-dip, LAMOST emission-line, eROSITA latent IF, Gaia variab. IF). The caption then states *"Three surveys PASS the gate at 5σ: SDSS DR18 continuum-dip..., Planck CMB native..., and NEOWISE ecliptic-pole mask..."* — yet Planck and NEOWISE injection-recovery curves are not plotted. Caption and figure must agree.

**P3-M5 — The 22.7% B-dominant DESI anomalies are flagged as "calibration-suspect" but counted in every headline.**
§VI C (3) lists "B-dominant contamination" of 44,436 DESI anomalies as needing confirmation. These are still included in the 195,829 DESI total quoted throughout. Either purge them or report a corrected headline.

**P3-M6 — Spatial χ² result is acknowledged as dominated by footprint heterogeneity, then reported anyway.**
§IV B: *"the significant $\chi^2_\nu = 3.76$ is dominated by the inhomogeneous footprints... rather than intrinsic astrophysical clustering."* Remove the number from the body. A statistic that the authors themselves admit cannot be interpreted should not be presented as a result.

**P3-M7 — The 17.8% genuine novelty fraction is reported without uncertainty.**
$178/1000$ has a binomial 95% Wilson CI of $[15.4\%, 20.5\%]$ at fixed top-1000. The paper acknowledges the top-1000 sample is a single stratum and the full-catalog rate is "empirically untested," yet 17.8% is the headline novelty figure in the abstract and conclusions. At minimum, quote with binomial CI; ideally re-do at additional score strata to bound the score-dependence.

**P3-M8 — Savage–Dickey Bayes factor 7.1×10³ is a two-model comparison that omits the actual NANOGrav model space.**
Reporting $B_{\rm MB/SMBHB}$ in isolation is misleading because NANOGrav fits a much larger set of new-physics templates (cosmic strings, inflationary GW, scalar-induced GW, first-order phase transitions, etc., per Afzal et al. [28]). The matter-bounce template is one of many; a pairwise $B$ vs SMBHB ignores all alternatives that may be favored over both. This should either be replaced with a posterior over the full new-physics model space or removed.

**P3-M9 — In-sample training-pool overlap in DESI is acknowledged but not corrected.**
The 195,829 DESI headline rate is computed on a 22.5M catalog that includes the 47,000 training spectra. The 5-fold Jaccard 0.862 is computed on the 47K training pool only — i.e., on objects that all five folds have seen. The OOD Jaccard 0.732 on 100k unseen spectra is the more relevant number and should be the headline stability figure.

**P3-M10 — Planck native CMB autoencoder fails criterion (a) and is retained on a Gaussian-bump injection test.**
Val_loss = 0.4437 vs. criterion (a) cutoff 0.30 — a 48% miss. Criterion (b) PASS via 500/500 = 100% Gaussian-bump recovery is a near-trivial test for a convolutional autoencoder on smooth CMB. This is not a meaningful validation; a realistic test would use point-source insertions, $\Lambda$CDM-realization swaps, or beam-mismatched plants.

**P3-M11 — The 12 $z\sim6$ QSO candidate claim is poorly traceable.**
§III B describes a selection on Z-arm dominance + Lyα/N V/Si IV emission. But §III A reports only 19 Z-dominant objects total (with score range 5.1–25.2). It is unclear how 12 of those 19 land in the $z=6.0$–$6.23$ Lyα-trough class. Tabulate the 12 candidates explicitly (TARGETID, RA, Dec, $z$, $r_Z$) in the main text; the current "Full coordinates... in the companion data repository" is insufficient for a discovery claim in PRD.

**P3-M12 — 5-fold Jaccard mean of 0.862 reported with three different control numbers without cross-walk.**
The paper reports $\bar J = 0.862$ (5-fold internal), $\bar J_{\rm prod\times ctrl} = 0.732$ (OOD), and "OOD control-vs-control 0.874" (Conclusions). These three Jaccards are computed on different samples and against different references; presenting them in a single paragraph without explicit cross-walk is confusing.

**P3-M13 — TIC 374313355 score = 49.5 is the SDSS cross-transfer score, not the native score.**
The cross-transfer score scale is the same one §III C demonstrates inflates SDSS scores by ~6500×. Quoting "score = 49.5" for a cross-survey match candidate in the body and in Fig. 6 caption without the corresponding native re-score is mixing apples and oranges and is misleading.

**P3-M14 — The 4n+1-nuisance Fisher block, GR projection result, and shot-noise penalty are all stated as $< 0.02\%$ or $< 0.01\%$ corrections with no derivation.**
Page 10 and Appendix C: bold claims like *"$|\Delta\sigma/\sigma| < 0.02\%$ at $k_{\max} = 0.2~h~{\rm Mpc}^{-1}$"* are presented in single sentences. For a PRD-level cosmology forecast paper, the Fisher matrix entries, prior choices, and degeneracy directions need to be in an appendix.

**P3-M15 — "Genuine novelty" definition rests on a 20-catalog CDS X-match that is opaque.**
The list of 20 catalogs given in §IV A actually contains only 17 named entries. The match radius (5″), positional uncertainties of source catalogs, and per-catalog completeness are not characterized. A "novelty" claim against catalogs with heterogeneous depth at fixed angular radius is poorly defined.

**P3-M16 — Footnote § in Table I cites the eROSITA 81.5% XV-stability as "the highest of any Path-C survey" but Gaia is the only other survey measured, at 41%.**
With $n=2$ surveys measured, "highest" is a trivial statement. Remove the framing.

---

## MINOR findings

**P3-Mi1** — §III A: $\rho = -0.03$, $p = 0.12$ from $N = 2{,}670$ is "no practically significant" — but a Pearson/Spearman $p = 0.12$ at $\rho = -0.03$ and $N \sim 2700$ is what one expects under the null; the conclusion is fine but the phrasing implies a meaningful test result.

**P3-Mi2** — §III E: the "novel" SIMBAD status of the eROSITA top-5 is reported, but they sit near the LMC where SIMBAD coverage is incomplete due to source confusion. The 68% SIMBAD-unmatched rate should be qualified.

**P3-Mi3** — §III F: "criterion (a) FAIL, but criterion (b) PASS" should be reported in Table I, not buried.

**P3-Mi4** — §IV C: "different surveys flag fundamentally distinct populations with minimal redundancy" is presented as a finding but is trivial given the very different wavelength regimes and selection functions.

**P3-Mi5** — Fig. 2 right panel title "SDSS DR18 (transfer learning)" mixes the cross-transfer scan into a panel that also presents native-retrain content elsewhere. Label which model produced the scores.

**P3-Mi6** — Table II "Uncategorized" category at 52.7% reduces the informativeness of the table. The caption acknowledges this, but the table itself should be flagged or the category split into "SIMBAD-matched-but-untyped" vs. "completely unmatched."

**P3-Mi7** — Appendix F is unusual: a "quarantined methodological artifact" retained as a full appendix. Either fold it into a methodology footnote or remove from the main paper. PRD does not normally accept negative-result appendices of this length.

**P3-Mi8** — Author affiliation "Independent Researcher" on a paper claiming cosmological forecasts and a Bayes factor of $7\times10^3$ in a contested area is unusual; not a basis for rejection but worth noting that no institutional review or co-author cross-check is documented.

**P3-Mi9** — Reference list — citation [12] "Mon. Not. Roy. Astron. Soc. (2026, in press)" needs DOI or arXiv ID; reference [1] "DESI DR1 documentation" is not a citable bibliography entry; should point to Adame et al. 2024/2025.

**P3-Mi10** — Repeated phrases: "cross-transfer artifact" appears 8+ times, often with identical surrounding clauses; "before/after diagnostic" appears 5+ times in identical phrasing. Tighten.

**P3-Mi11** — Abstract length (~50 lines as rendered) is well above PRD norms for abstracts (~250 words ≈ 20 lines). Cut.

---

## NITS

**P3-N1** — Page 8 Table III caption: "Note: two scores are reported per source" — content reads more as methodological prose than table footnote.

**P3-N2** — Table IV (Path-C residual caveats) crams long-form derivation pointers into the table cells. This belongs in a numbered list, not a table.

**P3-N3** — Page 9, paragraph "b. Expected false-match rates" — the 460 expected false matches figure is computed but not compared to anything; clarify what it implies for the 17.8% novelty.

**P3-N4** — "Decisive on Jeffreys' scale" (page 11) is a strong characterization riding on the questionable Bayes factor of P3-M8/P3-E4.

**P3-N5** — Figure 8 axes and Figure 9 image-gallery format are non-standard and could be improved.

---

## Length and scope

For the actual demonstrated science content — a multi-survey anomaly detection catalog with caveats and a null-result multi-tracer forecast — 20 pages is too long. Recommended maximum after revisions: **10–12 pages** with the bounce/NANOGrav content either moved to a separate dedicated paper or compressed into a single paragraph in §V that does not make detection-style claims.

---

## Summary recommendation

**REJECT**

The paper is not yet at PRD's bar. Three unresolved figure references in the rendered PDF, an arithmetic inconsistency in the headline $f_{\rm NL}$ improvement (7.9% vs. recomputed 9.35%), an unredacted internal bibkey note in the reference list, undefined internal jargon ("Path-C") in the title, and an apparent disagreement with the NANOGrav 15-yr collaboration result that is not addressed make this a first-pass reject independent of the science. The science itself — a $0.29\sigma$ bias measurement framed as a "central forecast improvement," a $7\times10^3$ Bayes factor that excludes the model space the NANOGrav collaboration actually compares against, a 141× catalog-size claim contaminated by a tier the authors themselves recommend excluding, and threshold heterogeneity across surveys that breaks any uniform interpretation — does not, in its current form, justify a PRD publication. The catalog data product itself is potentially useful and could be released through a different venue; the cosmological forecast and bounce claim should be pursued in a separate, dedicated, properly-validated paper.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Referee Findings — Fresh-Eyes Pass

After re-examining the paper systematically against the audit categories, I found multiple additional issues my initial review missed. The most consequential involve internal inconsistency between the main text and the appendix's Fisher forecast, a stale Jaccard number in the conclusions, and a caveat-numbering scheme that makes cross-references ambiguous throughout.

---

## NEW ESSENTIAL findings

**P3-E9 — Three different "single-tracer baselines" for σ(f_NL) appear in the same forecast.**
- §V (main text): "single-tracer DESI QSO baseline is σ(f_NL)^std = 8.98"
- Appendix C, Fig. 8 caption: "the dotted dark-red line marks the single-tracer baseline (σ(f_NL) = 16.85)"
- Same caption: "Ideal (dense limit) σ = 11.71"; "Baseline multi-tracer σ = 12.72"

The headline forecast inherits F₀ = 1/8.98² and reports a 7.9%/9.4% improvement; the appendix figure asserts the single-tracer baseline is 16.85 (nearly 2× larger) and uses 12.72 as the multi-tracer baseline. The "+7.93% ideal-multi figure" cited at the end of Appendix C.1 cannot be reconciled with any of (8.98, 16.85, 12.72, 11.71) at face value. The Fisher analysis is internally inconsistent across main text and appendix.

**P3-E10 — Conclusions point 6 quotes a Jaccard number that does not appear elsewhere in the paper.**
Conclusions point 6: *"DESI 5-fold Jaccard stability J̄ = 0.862 (PASS); OOD control-vs-control 0.874 (PASS)."*
But §II B and §VI D (i) both report the OOD/production-vs-5-seed-control number as J̄_prod×ctrl = **0.732**, not 0.874. The 0.874 figure appears nowhere else in the body and "control-vs-control" is not defined. This is a stale or invented number in the headline summary of the paper's main reproducibility claim.

**P3-E11 — Appendix C Table VII is mathematically inconsistent with the main-text Fisher form.**
§V adopts the Fisher-positivity form 1/σ² = F₀ + cα² with F₀ = 1/8.98², c = 0.0747. Under that form, at α = 0.50: 1/σ² = 0.01240 + 0.0747×0.25 = 0.03108 ⇒ **σ = 5.67**.
Appendix C Table VII reports σ = **7.15** at α = 0.50 and explicitly states this is "linear scaling of the fiducial 7-bin Fisher result at α = 0.15." The two forms agree only at the fitted α = 0.15 anchor and diverge at every other α value tabulated. The appendix sensitivity table therefore does not represent the methodology adopted in the main text. Either the appendix must be rebuilt under the Fisher-positivity form (and the linear table withdrawn), or the main text must explain why two incompatible scalings coexist.

**P3-E12 — Fig. 6 Match 1 reports DESI score = 3.2, below the catalog threshold S > 5.**
The DESI anomaly catalog is defined by S > 5.0 (§II B, §III A, Table I footnotes). Fig. 6 panel (a) labels Match 1 with "Score = 3.2" on the DESI side and "Score = 2.8" on the SDSS side. Match 1 therefore cannot be in the DESI anomaly set, yet §IV C presents it as one of the three highlighted DESI×SDSS cross-survey matches. Either the figure score is mislabeled, the threshold has been silently relaxed for cross-matching, or Match 1 is not in fact a cross-survey anomaly match.

**P3-E13 — Caveat numbering scheme is inconsistent and renders most §VI D cross-references ambiguous.**
The body uses two parallel naming conventions for Path-C caveats:
- Roman numerals **(i), (ii), (v)** for §VI D body items (DESI in-sample; injection synthesis; IsolationForest XV in Table I footnote §)
- Letters **(a)–(j)** for Table IV residual-caveat rows

Both are referenced as "§VI D caveat (X)". Specifically: "§VI D caveat (i)" on page 10 (Fisher positivity) refers to Table IV item (i) — a letter — while "§VI D (i)" on page 3 refers to the Roman-numeral DESI in-sample item. References to "§VI D (e)", "(f)", "(j)" on pages 10–11 are Table IV letter entries with no §VI D body text, while references to "§VI D (ii)", "(v)" are Roman-numeral body items. A PRD reader cannot disambiguate these calls.

**P3-E14 — §VI D body text is truncated/missing relative to references made to it.**
§VI D as printed contains only caveats **(i)** and **(ii)** as discursive paragraphs before the section transitions out. Yet body and table footnotes invoke §VI D caveats **(iii), (iv), (v), (e), (f), (i), (j)** as if they had been written. Items (iii)–(v) are entirely absent. The closure status of these caveats is asserted in Table IV but never argued in the body — yet Table IV's caption claims "All ten items are closed (resolved in paper)." If the resolutions are only in the companion repository, the paper has not closed them at PRD-publication standard.

---

## NEW MAJOR findings

**P3-M17 — Table I LAMOST row (44,075) is the cross-transfer count; the headline 378,280 sums a different LAMOST number (113,342).**
Per Table I footnote ¶: "Per-survey N_anom values shown in this column are the initial cross-transfer scan counts." Per Table I footnote ‡: LAMOST native re-score = 113,342. The Path-C unique-object headline at the bottom of Table I sums to 378,280, which requires the LAMOST contribution to be 113,342, not the displayed 44,075. A reader summing the displayed column does not obtain 378,280; the discrepancy of ~69,000 anomalies is buried in footnotes. The same applies (more weakly) to SDSS, but the cross-transfer and native top-1% counts happen to coincide at 77,905 by construction. Table I should display the values actually summed by the headline row.

**P3-M18 — Aggregate "58.8% SIMBAD-unmatched" in Table I cannot be reproduced from per-survey rates.**
Per-survey unmatched fractions in Fig. 5: 99% (DESI), 90% (SDSS), 68% (eROSITA), 50% (LAMOST), 45% (NEOWISE), 27% (Gaia). Weighted by N_anom this gives ~90%; unweighted average gives ~63%. Neither reproduces 58.8%. The 58.8% number is presented as the cross-archive aggregate in Table I and again in Fig. 5 ("Aggregate 58.8%"), but its derivation is not stated and cannot be back-computed from the displayed inputs.

**P3-M19 — Fig. 6 TIC 374313355 SDSS score = 49.5 is on an unidentified scale.**
The SDSS cross-transfer score range extends to 10¹¹ (Fig. 2 right panel); the SDSS native-retrain top-77,905 threshold is S ≥ 0.106. A score of 49.5 is plausibly cross-transfer; on the native scale it would be extreme. The figure does not specify which scale the score reflects, and the headline catalog uses the native scale. Match 2's score of 49.5 is therefore not directly interpretable.

**P3-M20 — Equation (E1) PTA likelihood: NANOGrav-convention dependence is not stated.**
The 12π² normalization, f_yr reference, and bin-width 1/T_obs convention are written in (E1) with no statement of which NANOGrav data product convention is matched. Different PTA pipelines use different conventions for whether the residual or characteristic-strain spectrum is fit, and the inferred γ can shift by 0.1–0.3 depending on choice (within the reported 0.382 uncertainty). Given that the headline +1.13σ "bounce consistency" and +4.61σ "SMBHB disfavor" depend on the central value of γ, the convention identification matters and should be stated.

---

## NEW MINOR findings

**P3-Mi12 — Verbatim paragraph repetition on page 4–5.**
The block beginning "Galaxies are flagged at ∼ 20× the QSO rate (0.75% vs. 0.037%); anomalies peak at z ∼ 0.75 vs. z ∼ 0.93 for normal spectra. The three highest-scored anomalies (S = 25.2, 24.6, 24.5)..." appears twice in consecutive paragraphs of §III A, the second time rephrased but with identical numerical content. Tighten.

**P3-Mi13 — Catalog count in §IV A list is 18, not 20.**
The parenthetical "20 curated all-sky catalogs" enumerates Gaia DR3, SDSS DR12, SDSS DR16, DESI Legacy DR9, DES DR2, Pan-STARRS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, USNO-B, UCAC5, APASS — that is 18 entries. (Correction to my P3-M15, which undercounted as 17.) The denominator of the 17.8% novelty fraction depends on which catalogs were actually queried.

**P3-Mi14 — Reference [25] (Hellings & Downs 1983) appears unused.**
I cannot locate a body citation to [25]. NANOGrav HD-correlation context cites [18] and [28]. Either add a citation or remove the reference.

**P3-Mi15 — Fig. 1 caption count (319,443) versus body description.**
Fig. 1 plots "all 319,443 anomalies across 8 archives" including ACT, but ACT is quarantined and contributes zero to every body claim. The figure exists as a "cross-transfer baseline" diagnostic per its caption, but its placement (a full-width Mollweide on page 4) gives it visual prominence equal to a science-result map. Either move to appendix or relabel.

**P3-Mi16 — Abstract "~265,000 unique objects" recommended subset arithmetic.**
DESI 195,829 + SDSS 77,905 + eROSITA 298 + Gaia 500 + NEOWISE 419 = **274,951** before dedup. The ~265,000 figure presumably subtracts ~10,000 duplicates, but the 10,213 reported dedup count is the total across all 7 surveys, not just these 5; the appropriate subtraction (excluding LAMOST and Planck) is not derived. The ~265,000 should be made traceable.

**P3-Mi17 — eROSITA top-1% reference set is stated as 9,303 sources in Table I footnote §; 1% of 930,203 is 9,302.03.**
Rounding choice OK; flagged for completeness because it propagates to the 81.5% XV-stability denominator (7582/9303).

---

## NEW NITS

**P3-N6 — Table IV (e) refers to "k_max = 0.2 h Mpc⁻¹" using "h" without explicit definition.** Standard but should be glossed once.

**P3-N7 — "f_yr" in Equation (E1) is undefined.** Implicit as 1/(1 year) but should be stated.

**P3-N8 — Multiple references to "BigAE" capitalization vary ("BigAE", "BIGAE", "Big AE" in text rendering).** Pick one form.

**P3-N9 — Fig. 6 panel (c) labels "TIC 374313355 — DESI epoch" with score 8.1, but panel (d) reports SDSS score 49.5 with caption text "consistent with a stellar flare or accretion event."** The factor-6 score asymmetry between DESI and SDSS epochs is presented as physical variability evidence; it is equally consistent with the cross-transfer-vs-native score-scale inconsistency flagged in P3-M19. The flare interpretation needs photometric corroboration before the figure can claim "stellar flare or accretion event."

---

## Updated summary recommendation

The new findings do not change the bottom-line **REJECT** recommendation but reinforce it on additional independent grounds. In particular: (i) the appendix's σ(f_NL) sensitivity table uses a different (linear) functional form than the main text's Fisher-positivity form (P3-E11); (ii) three mutually incompatible single-tracer Fisher baselines appear across §V and Appendix C (P3-E9); (iii) a stale Jaccard number (0.874) appears in the headline conclusions while the body reports 0.732 (P3-E10); (iv) the caveat-numbering scheme uses both Roman numerals and letters interchangeably and §VI D body text is truncated relative to its referents (P3-E13, P3-E14); and (v) Fig. 6 Match 1 is below the catalog threshold on the DESI side, undermining the cross-survey discovery claim (P3-E12).

These are precisely the class of internal-consistency failures that a PRD reader can identify in one careful read-through. The paper requires a full audit pass and re-verification of every numerical entry before resubmission to any journal.
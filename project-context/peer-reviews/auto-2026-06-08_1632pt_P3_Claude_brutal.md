# P3 auto-2026-06-08_1632pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (17585 chars)
**Wall time**: 423.5s

---

# Referee Report: P3 — "Spectrally Unusual Sources at Scale"

## Overall Assessment

This is a methods/catalog paper that tries to be three papers at once: (1) a multi-survey anomaly catalog, (2) a cosmological forecast for fNL via multi-tracer techniques, and (3) a pulsar timing array analysis of matter-bounce GWB. None of the three components meets PRD standards individually, and their juxtaposition creates a paper that is neither a clean catalog release (which belongs in a survey journal) nor a focused cosmology result. The catalog itself is heavily compromised by acknowledged systematic failures (3 of 6 injection-recovery gates FAIL at 5σ, the LAMOST 98% blue-excess artifact is explicitly "exploratory," ACT is quarantined, the SIMBAD novelty claim collapses from 58.8% to 17.8% under proper cross-matching, and the fNL improvement is "consistent with no improvement at <1σ"). The author repeatedly hedges headline claims into meaninglessness while still presenting them as headlines.

---

## ESSENTIAL findings

**P3-E1 (Abstract, p.1): Headline fNL "improvement" is null but presented as a result.**
The abstract states "σ(fNL) = 8.14 ... 7.9% improvement consistent with no improvement at <1σ." This is a null result being marketed as a numerical forecast. A central value with a 1σ envelope of [3.92, 8.98] that contains the baseline (8.98) at its upper edge means the data are consistent with zero improvement. PRD does not publish forecasts whose central value is statistically indistinguishable from the no-information baseline. Either reframe explicitly as an upper limit / null, or remove from abstract.

**P3-E2 (Abstract & §V A, pp.1, 12): Inconsistent σ definitions juxtaposed without warning.**
The abstract reports γ = 2.567 ± 0.382 and the matter-bounce γ=3.0 at "+1.13σ." Recomputing: (3.0 − 2.567)/0.382 = 1.133. OK. But the body simultaneously reports γ = 2.591⁺⁰·²⁹¹₋₀.₂₈₇ as the quantile summary. Using ±0.29, the same shift would be +1.41σ for the +1.13σ claim. Reviewer instruction #7 applies: the paper acknowledges these are different uncertainty types but uses one for the headline sigma without justifying the choice that minimizes the tension. SMBHB γ=4.33 at "+4.61σ" — recomputing: (4.33 − 2.567)/0.382 = 4.615, OK with the std-dev. With the quantile width ±0.29 it would be 6.0σ. The author must justify why ±0.382 (which gives the *smaller* SMBHB tension and the *less* significant bounce consistency) is the appropriate scale, since they are inconsistent choices: smaller σ for SMBHB rejection would *strengthen* the Bayesian narrative, larger σ would *weaken* the bounce consistency. The arbitrary choice is suspicious.

**P3-E3 (Abstract, p.1): "Spatial distribution of all 319,443 anomalies" but headline is 378,280.**
Figure 1 caption: "Spatial distribution of all 319,443 anomalies across 8 archives." The headline number is 378,280. This is the cross-transfer baseline (which the paper itself says is "not a science result"). The principal map of the paper visualizes the discarded baseline, not the canonical catalog. Replace with a map of the 378,280 Path-C catalog or explicitly relabel and demote.

**P3-E4 (Table I & §III, pp.7–8): Table I displays cross-transfer counts as headline per-survey numbers.**
The "Nanom" column shows 77,905 for SDSS and 44,075 for LAMOST — these are cross-transfer counts that the paper says are not science. The Path-C native rate for SDSS at S>5 is 12 sources; for LAMOST the native top-1% slice gives 113,342. The footnote attempts to disclose this, but the column itself is misleading. A reader scanning Table I sees the wrong numbers as the per-survey detection counts. Recompute: 195,829 + 77,905 + 44,075 + 298 + 200 + 500 + 436 = 319,243, not the stated 319,443 in the Table I total row (off by 200). The "319,443" likely includes ACT's 200 patches but the table excludes ACT — the arithmetic is broken.

**P3-E5 (Table I, p.7): Path-C unique 378,280 arithmetic does not close.**
Footnote ∥ states: "DESI 195,829 + SDSS 77,905 + LAMOST 113,342 + eROSITA 298 + Planck 200 + Gaia 500 + NEOWISE 419 = 388,493" → after 10,213 dedup → 378,280. Recomputing the sum: 195,829 + 77,905 = 273,734; +113,342 = 387,076; +298 = 387,374; +200 = 387,574; +500 = 388,074; +419 = 388,493. ✓ The sum is correct. But the SDSS entry of 77,905 here is the cross-transfer count, contradicting the previous text saying SDSS native gives only 12 sources at S>5 OR 77,905 at top-1%. So the 77,905 in the unique-object math refers to the top-1% native slice (S≥0.1060), NOT the cross-transfer 77,905 — these happen to be the same number by construction (top-1%). This is intentionally confusing; the author should use distinct symbols or rename one of these.

**P3-E6 (Abstract & §VI A, pp.1, 12): LAMOST inclusion in headline despite explicit gate FAIL.**
The 378,280 headline includes 113,342 LAMOST objects retained despite (a) 98% blue-excess training-bias artifact, (b) injection-recovery FAIL at 5.8% (gate is 50%), and (c) the author's own statement "exploratory tier only." Including a known-contaminated tier in the headline count, then disclosing the contamination in footnotes, inflates the catalog size by ~30%. The "recommended catalog-grade subset is ~265,000" should be the headline number. The 378,280 framing is dishonest.

**P3-E7 (Table III, p.8): Mismatch between SBigAE and IF score columns.**
Table III shows S_BigAE = 1.084, 0.815, 0.591, 0.498, 0.439 for the top-5 eROSITA. The text in §III E says "top anomaly ... S = 1.084". But footnote § in Table I says the eROSITA threshold is "S > 0.259 ... roughly the top-0.03%". Five objects with S in [0.439, 1.084] are all well above 0.259. That's consistent. But the IF raw scores (34,182, 16,270, ...) have no axis definition for the reader — the table says they're on a "~0–3.5×10⁴ scale" without justification. Two parallel detector axes with no explicit calibration map invites cherry-picking.

**P3-E8 (Fig. 2, p.5): "Threshold S = 5" in left panel but right panel shows SDSS reaching S = 1.9 × 10¹¹.**
The same axis label "anomaly score S" is used for both panels, but the right panel's S values are cross-transfer artifacts spanning 12 orders of magnitude. The caption acknowledges this but the figure is still misleading because the y-axis "Prob. density" reaches 10⁻¹⁴, indicating a single object at extreme values is being plotted as a "density." A pre-canonical artifact shown on the same axis as the canonical scores violates basic figure hygiene.

**P3-E9 (§V, p.10): The α empirical measurement contradicts itself.**
"αgeo = 0.27; αjk = 0.19 ± 0.65 ... consistent with zero at 0.29σ and with the prior fiducial α = 0.15 at 0.06σ (95% CI: α ∈ [−1.08, +1.46])." The 95% CI for α from ±0.65 is [−1.08, +1.46] — recomputing: 0.19 ± 1.96×0.65 = [−1.08, +1.46]. ✓ But this α has zero diagnostic power: it spans more than ±1 around 0, which means the multi-tracer bias enhancement is completely unconstrained by this measurement. Inserting an unconstrained α into a Fisher forecast and reporting "central forecast σ(fNL) = 8.14" is meaningless. The Gold+Silver subset gives αGS,jk = +1.83 ± 2.03 — even worse. These should be reported as upper limits or removed; they do not support the abstract's σ(fNL) claim.

**P3-E10 (§V, p.10): Fisher positivity ad-hoc.**
"1/σ(fNL)² = F₀ + cα²" — this functional form is asserted without derivation. Why α²? A bias enhancement α enters Fisher information linearly through the cross-power and bias-difference terms; α² is one particular regime. The "5-α refit c > 0" justification is not a derivation. Without an explicit calculation showing the Fisher decomposition that yields this exact form (with the claimed c = 0.0747), this is a fitting parameter masquerading as a forecast.

**P3-E11 (Abstract & §V A, pp.1, 12): Savage-Dickey Bayes factor lacks prior justification.**
"BMB/SMBHB = 7.14×10³ (log10 B = +3.85, decisive)" depends entirely on the γ-uniform prior on [0,7]. Savage-Dickey is well-defined only for nested models with a delta-function comparison; here both γ=3.0 (matter-bounce) and γ=4.33 (SMBHB) are point predictions evaluated against a free-γ posterior. The "decisive" language follows Jeffreys' scale which is famously prior-dependent. PRD requires (a) explicit prior justification, (b) sensitivity to prior choice, (c) acknowledgment that this is not a model-comparison Bayes factor in the standard sense. Reporting "decisive" with no priors-sensitivity analysis is unacceptable.

**P3-E12 (§III A, p.4): "0% artifact rate" claim is unverifiable.**
"Spectral inspection of the top 200 confirms a 0% artifact rate." Visual inspection by whom? With what criteria? Inter-rater reliability? With ~44,000 B-dominant anomalies flagged elsewhere as "calibration-suspect" (§VI C), the claim that the top-200 have zero artifacts contradicts the broader catalog quality assessment.

**P3-E13 (§V, p.10): Multi-tracer projection to "3–5σ detection of fNL = −35/8 with SPHEREx."**
This range is asserted without a Fisher calculation in the paper. The companion data repository is invoked but the load-bearing cosmological claim of the paper (testability at 3–5σ) appears nowhere in the body with derivation. PRD does not accept "trust me, see the repo" for the main scientific motivation.

**P3-E14 (§II B, p.2): Internal audit tags in body text.**
"§VI D caveat (i)", "§VI D (b)", "§VI D (f)", "§VI D (v)" — these are bookkeeping tags pointing to a 10-item caveats table. While the table itself (Table IV) is fine, the inline citation of letter codes ("caveat (b)", "caveat (v)", "caveat (i)") reads as internal review-cycle bookkeeping. Convert to descriptive references ("the eROSITA cross-validation caveat") or eliminate.

**P3-E15 (§III F, p.6): Planck native CMB autoencoder gate logic is contradictory.**
"val_loss = 0.4437 (criterion (a) FAIL, but criterion (b) PASS: 500/500 = 100% injection-recovery)." Criterion (a) is val_loss ≤ 0.30. A val_loss of 0.4437 is 1.5× the threshold, which the paper calls "FAIL." Then claims criterion (b) passes via 100% injection-recovery on Gaussian-bump signals. But the Gaussian-bump injection is by construction designed to be detectable by an autoencoder trained on smooth backgrounds; it does not test whether the autoencoder distinguishes physical signal from CMB realization variance. This is a circular validation. The 200 Planck patches should not be in the headline catalog.

**P3-E16 (Page count): 20-page paper for a result that is largely null.**
Given that (a) the catalog has 3 of 6 surveys gate-FAIL, (b) the fNL improvement is null, (c) the NANOGrav consistency is +1.13σ (not a detection), (d) ACT is quarantined, (e) LAMOST is explicitly exploratory — the actual scientific content is roughly a 4-page catalog paper. PRD page limits should be ≤ 8 pages for the surviving content.

---

## MAJOR findings

**P3-M1 (Abstract, p.1): "~141× the size of the largest prior single-survey anomaly catalog" claim.**
Comparing 378,080 point sources to Liang et al. 2,685 = 141×. But the recommended catalog-grade subset is ~265,000, giving 99×. And the 17.8% genuine novelty rate applied to 378,080 = ~67,000 actual novel objects, giving 25× the Liang count. The "141×" figure measures detection events, not discoveries. Reframe.

**P3-M2 (§II B, p.2): Inconsistent threshold families undermine cross-survey comparison.**
"DESI DR1 and SDSS DR18 use an absolute canonical-S cut at S > 5.0; LAMOST DR10 and Gaia DR3 use the 99th-percentile; eROSITA uses a data-driven IsolationForest score-knee threshold; Planck and NEOWISE use a fixed top-1%." Five different threshold families across seven surveys means the per-survey anomaly rates are not commensurable, but the paper repeatedly aggregates them (319,443 total, 378,280 unique).

**P3-M3 (§III B, p.4): TARGETTYPE sample size hand-wave.**
"Across the 6.5 million spectra in DESI DR1 that carry a validated TARGETTYPE classification ... the remaining ~16 million spectra are unclassified filler targets, sky fibers, or calibration exposures excluded from this per-class breakdown." But the headline anomaly count of 195,829 is computed over all 22.5M. So the per-class breakdown is conditional on 30% of the catalog. The galaxy-to-QSO 20× ratio cannot be cited as a property of the DESI anomaly population.

**P3-M4 (§III B, p.4): The "12 z≈6 QSO candidates" identification has confused score reporting.**
"rZ = 5.30 ... rZ = 5.18 ... Panel labels report the per-arm Z-arm sub-score rZ (printed as 'AE' for legacy compatibility), not the total anomaly score S; all twelve pass the S > 5 catalog cut at the total-score level (mean ⟨rZ⟩ ≈ 3.9)." If mean rZ is 3.9 and individual rZ values are 5.18, 5.30, then the highest rZ values are above the threshold but the average is below. Mixing two score axes in image labels and text is error-prone.

**P3-M5 (Figure 9, p.17): "AE" scores in the gallery range 3,768 to 83,518.**
"AE=83518" — these are cross-transfer or pre-canonical scores. The current paper canonicalizes S in z-units. Showing AE values up to 83,518 in a representative gallery, with no scale conversion or annotation, suggests this figure was generated before the canonicalization in §II B was applied. Either regenerate with canonical S or label as legacy.

**P3-M6 (§IV A, p.9): SIMBAD 58.8% → 17.8% collapse contradicts abstract framing.**
The abstract leads with the 17.8% genuine novelty fraction. The body shows this was measured on a single sample (top-1000 DESI) and the full-catalog rate is "empirically untested." Yet a separate 100% archival recovery rate is reported for "randomized 20-object samples" from eROSITA, NEOWISE, Gaia. If those samples have 100% archival ID, the catalog-wide novelty rate is much lower than 17.8%. The headline 17.8% applies only to DESI top-1000 and is unrepresentative of the catalog as a whole.

**P3-M7 (§IV B, p.10): χ² test of spatial uniformity is dismissed by the author.**
"The significant χ²ν = 3.76 is dominated by the inhomogeneous footprints of the seven retained archives rather than intrinsic astrophysical clustering." If this is acknowledged, why report the χ² result at all? Remove it.

**P3-M8 (Fig. 3, p.6): UMAP figure shows percentages but caption is loose.**
"Dominant cluster (green, ~84% of objects)" but the panel shows percentages in legend like "(4119)" — what fraction of 77,905? Recompute: cluster 0 = 84%, then ~65,440. The legend numbers do not appear to sum to 77,905. Axis labels UMAP-1, UMAP-2 give no scale interpretation (acceptable for UMAP), but the cluster ID legend extends to 13 — only 14 clusters claimed, top one dominates, structure of the remaining 12 is uninterpreted.

**P3-M9 (§III E, p.6): "284/298 = 95.3% overlap, 95.3× enrichment" coincidence.**
Two different quantities both happen to be "95.3" — overlap fraction and enrichment factor. Either coincidence or arithmetic error. Recomputing: 298/930,203 × 9,303 ≈ 2.98 expected, observed 284, ratio = 284/2.98 = 95.3. ✓ Coincidence confirmed but worth flagging in text.

**P3-M10 (§V A, p.12): NANOGrav posterior reuse.**
The author fits a power-law to the published Ceffyl KDE free-spectrum likelihood. This is not a re-analysis of NANOGrav data; it is post-processing of NANOGrav's reduced product. PRD readers will assume "MCMC fit to NANOGrav data" means raw timing residuals. State clearly that no new PTA information is added beyond a power-law fit to an already-published spectrum.

**P3-M11 (Table II, p.8): Category percentages don't aggregate cleanly.**
Sum: 52.7+33.0+7.8+1.6+1.5+1.0+0.7+0.7+0.5+0.5 = 100.0%. ✓ But "Uncategorized" = 52.7% being the dominant class means the classification pipeline is effectively a coin flip for half the catalog. This undermines the §VII conclusion that "SDSS anomalies cluster into 3 UMAP/HDBSCAN populations (84% cool dwarfs)" — those are two different classifications (10-class lexical vs. 3-cluster UMAP), and the paper doesn't reconcile them.

**P3-M12 (§V, p.10): Single-tracer baseline σ(fNL)^std = 8.98.**
This value is asserted with no citation. Standard DESI QSO single-tracer forecasts in the literature give σ(fNL) ~5–15 depending on systematics; an 8.98 baseline needs a source. Without it, the "improvement" cannot be benchmarked.

**P3-M13 (§VI E, p.13): Liang et al. comparison is misleading.**
"Our DESI anomaly rate of 0.87% is consistent with the 1.07% rate reported by Liang et al." But Liang et al. used a normalizing-flow VAE on EDR; this paper uses a deterministic FC autoencoder on DR1. Two different architectures on different data releases producing similar rates is interesting but does not "suggest spectroscopic anomaly rate is a stable property" — it could be a coincidence between two arbitrary thresholding choices.

**P3-M14 (Fig. 4 caption, p.8): "Score = 11.5" with no context.**
What is a score of 11.5 on the NEOWISE detector? The Table I footnote says NEOWISE uses "fixed top-1%" — so 11.5 is just a raw MSE z-score with no defined ceiling. Cross-referencing the figure to the abstract or score-distribution discussion is needed.

**P3-M15 (§VII, p.14): "Conclusions" section repeats content verbatim from earlier.**
"NANOGrav KDE-likelihood MCMC yields γ = 2.567 ± 0.382; matter-bounce γ = 3.0 at +1.13σ" — verbatim from abstract. Conclusion sections should synthesize, not repeat.

**P3-M16 (Bibliography, p.19): Reference [33] Heinrich et al.**
"[33] C. Heinrich, O. Doré, and E. Krause, ... J. Cosmol. Astropart. Phys. 2024, 074 (2024), arXiv:2311.13082 [astro-ph.CO] [publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]." Internal bibkey commentary is in the bibliography itself. Remove the bracketed editorial note.

---

## MINOR findings

**P3-Mi1 (§II A, p.2): "BigAE" naming.**
The architecture is a standard FC autoencoder with ~120K-660K parameters. Calling it "BigAE" is marketing; modern deep-learning "big" models are ≥10⁹ parameters. Either rename or justify.

**P3-Mi2 (§II B, p.2): The footnote-style "(note: 'z-scored' here is the statistics term...)" is awkward.**
Move this disambiguation to a dedicated nomenclature paragraph.

**P3-Mi3 (Table V, p.16): Training time for DESI native = 3,600 s, but §II B says "training is run for up to 200 epochs ... convergence typically occurs at 100–150 epochs."**
With batch size 512 and 47,000 spectra, 100 epochs = ~9,200 batches. 3,600 s for this is ~0.39 s/batch on H200 — extremely slow for a 660K-parameter model. Suggests bottleneck elsewhere or table value is wrong.

**P3-Mi4 (§III A, p.4): "ρ = −0.03 (p = 0.12 on a stratified subsample of 2,670 spectra)."**
A correlation of −0.03 with p = 0.12 is "not significant," but for n = 2,670 the p-value for r = 0.03 should be ~0.12. ✓ Consistent but uninformative — the SNR-score correlation could still bias the top-of-the-tail anomaly rankings.

**P3-Mi5 (Fig. 5, p.9): Bar labels read "99%, 90%, 68%, 50%, 45%, 27%" with aggregate "58.8%".**
Recompute aggregate as a weighted average: depends on per-survey weights. Without disclosing weights, "58.8%" cannot be checked.

**P3-Mi6 (§V, p.10): "(95% CI: α ∈ [−1.08, +1.46])."**
The notation α ∈ [−1.08, +1.46] for a "bias enhancement" allowing negative values needs interpretation. A negative α would imply the anomaly tracers have *lower* bias than the parent — physically possible but not addressed.

**P3-Mi7 (§VI A, p.12): "Any anomaly is unusual relative to the training set, not 'unusual in the universe'."**
This methodological observation is correct but undermines the entire framing of the paper. If acknowledged, the title's "spectrally unusual" is misleading.

**P3-Mi8 (Appendix C, p.15): Linear scaling of Fisher information with α.**
"Fractional improvement scales as ∆σ/σ_std ≈ (6.1%/0.15) α" but §V uses the α² Fisher-positivity form. The Appendix C and §V Fisher formulas are inconsistent (linear in α vs. quadratic in α²). Reconcile.

**P3-Mi9 (Fig. 6, p.11): TIC 374313355 DESI score = 8.1, SDSS score = 49.5.**
Score difference of 6× between epochs for the same object. The paper attributes this to time-variability but offers no spectroscopic comparison metric (continuum flux ratio, line equivalent widths). A score difference is not evidence of variability without flux calibration.

**P3-Mi10 (§VI D Table IV, p.13): "Headline result" column conflates problem and resolution.**
"DESI OOD: training-pool cut flags 52.8% of OOD (61× headline)" — the 52.8% rate when the threshold is applied to raw uncurated SPARCL data is not "reconciled" by saying it's a curation effect; it suggests the catalog threshold has no meaning outside the curated training distribution.

**P3-Mi11 (Footnote ¶ on Table I, p.7): Recursive footnote.**
"Per-survey Nanom values shown in this column are the initial cross-transfer scan counts. The Path-C native-retrained counts, which supersede these values, are reported in §II D and summarized in the 'Path-C unique (primary)' row below." But the Path-C row in Table I shows only the total 378,280, not per-survey native counts. Reader cannot reconstruct per-survey native numbers from Table I alone.

**P3-Mi12 (Appendix E, p.16): Hellings-Downs is cited [25] but the analysis fits power-law only, not the HD correlation.**
The author fits γ to the published HD-correlated likelihood, but does not test HD correlation independently.

**P3-Mi13 (References, p.19): [11] Liang et al. publication year MNRAS 525.**
arXiv:2307.07664 — MNRAS publication is correct. OK.

**P3-Mi14 (References, p.19): [12] Nicolaou "MNRAS (2026, in press)."**
"In press" for 2026 should specify acceptance status. If unpublished, mark as "in preparation."

**P3-Mi15 (§III H, p.8): NEOWISE polar-cap fraction calculation.**
"17/436 = 3.9% polar-cap fraction represents a 2.6× excess over the uniform-sphere null expectation (1.52%)." Recompute null: solid angle of |b_ecl|>80° polar caps = 2 × 2π(1−cos 10°) / 4π = (1 − cos 10°) ≈ 0.0152 = 1.52%. ✓ Ratio 3.9/1.52 = 2.57. ✓

**P3-Mi16 (§V, p.10): "5,384 QSO-candidate sample."**
This number appears suddenly — what is its relationship to the 195,829 DESI anomalies or the 12 z≈6 QSO candidates? Cross-reference needed.

---

## NIT findings

**P3-N1 (Title, p.1): "Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches."**
Awkward phrasing. "Source and map-patch" or split into two clauses.

**P3-N2 (Abstract, p.1): "(Dated: June 2026)."**
Future date in a current-submission abstract.

**P3-N3 (§II A, p.2): "BigAE is a deterministic autoencoder (not variational), prioritizing reconstruction fidelity and anomaly-score interpretability."**
"Interpretability" of MSE scores is asserted without justification.

**P3-N4 (Fig. 1, p.4): Mollweide projection axis labels "0°, 30°, 60°..." for RA written in two different formats.**
RA at top in degrees with negative values; standard astronomy uses hours (0h–24h) or 0°–360°.

**P3-N5 (Table I, p.7): "♡" and "♠" symbols used as footnote markers.**
Non-standard; use letters or daggers.

**P3-N6 (§II D, p.3): "Path-C" naming.**
"Path-C" suggests Paths A and B existed earlier. Internal versioning leakage. Rename or explain.

**P3-N7 (§III D, p.6): "21.5×" compression appears in abstract and §III D; the factor 44,075/2,054 = 21.46. ✓ But the abstract also says "the recommended catalog-grade subset is ~265,000" and the LAMOST exclusion contributes 113,342 to the 378,080 point-source tier. 378,080 − 113,342 = 264,738 ≈ 265,000. ✓**

**P3-N8 (§VI D Table IV, p.13): "All ten items are closed (C = resolved in paper)."**
"C =" notation appears nowhere else; orphaned legend.

**P3-N9 (Appendix F, p.18): "What this appendix is not."**
Defensive heading, suggests author anticipates misuse. Better to embed cautions inline.

**P3-N10 (References, p.19): URL for [1] "DESI DR1 documentation" is not a citable reference.**
Should cite DESI Collaboration et al. 2024 paper formally.

**P3-N11 (§II B, p.2): Equation (1) uses 1/N normalization but Eq. (2) uses µ_val, σ_val from MSE distribution — verify the normalization convention.**

**P3-N12 (Fig. 2 caption, p.5): "twelve orders of magnitude from the threshold (S = 5) to S = 1.9×10¹¹."**
log₁₀(1.9×10¹¹/5) ≈ 10.6 orders. Not 12. Recompute.

**P3-N13 (§III A, p.4): "Spearman r = 0.0005" for spatial uniformity.**
A correlation of 0.0005 is functionally zero; useful as a null test but reporting four significant figures is misleading.

**P3-N14 (§IV C, p.10): "The 7-way positional deduplication at 5'' identifies 637 multi-survey coincidences across 388,493 survey-level detections."**
388,493 vs. 378,280: difference is 10,213. ✓ Dedup math closes.

---

## Summary recommendation

**REJECT**

This paper combines a methodologically compromised catalog (3 of 6 surveys gate-FAIL at 5σ, LAMOST tier explicitly described as "exploratory" yet retained in headline counts, ACT quarantined), a null fNL forecast presented as a numerical improvement (αjk = 0.19 ± 0.65, fully consistent with zero, 95% CI spanning [−1.08, +1.46]), and a PTA "consistency check" that is a power-law fit to a published reduced product rather than new PTA analysis. The abstract leads with three quantitative claims (378,280 anomalies, 17.8% novelty, σ(fNL) = 8.14) that each have substantial caveats undermining their headline status: the 378,280 figure includes a contaminated tier the author themselves recommend excluding, the 17.8% applies to a 1,000-object subsample of a 378,000-object catalog and is "empirically untested" at the full-catalog scale, and the σ(fNL) "improvement" is consistent with no improvement at <1σ. Internal bookkeeping ("Path-C", caveat-letter cross-references, "bibkey retained as Heinrich2023"), arithmetic inconsistencies (319,443 vs. 319,243 in Table I total), inconsistent σ definitions in the NANOGrav analysis, and confused score-axis presentations (Fig. 9's AE scores up to 83,518 in a paper that canonicalizes S in z-units) compound the substantive problems. The paper should be split into (a) a focused catalog release describing the ~265,000 catalog-grade subset with honest novelty fractions, submitted to a survey journal, and (b) a separate cosmology paper if and when the multi-tracer measurement achieves >2σ signal. In its current form, neither component meets PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Second Pass: Fresh-Eyes Findings on P3

After a focused re-examination targeting the categories listed (arithmetic, figure-vs-body, equations, cross-references, null comparability, abstract faithfulness, novelty claims, hedges, appendix-vs-text, stale numbers), substantial new issues emerged that the first pass missed. Most damaging: the abstract's headline "7.9% improvement" arithmetic does not match the inputs in the body, and Appendix C uses a different single-tracer baseline than §V — two incompatible fNL forecasts coexist in the same paper.

---

## NEW ESSENTIAL findings

**P3-E17 (Abstract, p.1 vs §V, p.10): The "7.9% improvement" number does not match the inputs.**
The abstract reports "σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement)". The improvement implied by these numbers is (8.98 − 8.14)/8.98 = **9.36%**, not 7.9%. The actual "7.9%" figure appears to be imported from Appendix C / Fig. 8, where the canonical 5-tracer Fisher forecast gives baseline-multi 12.72 → ideal-multi 11.71, i.e., (12.72 − 11.71)/12.72 = **7.94%**. That is a *different calculation entirely* (a dense-limit forecast over a 5-tracer Fisher with its own baseline 12.72), not the αjk = 0.19 → σ(fNL) = 8.14 path. The abstract conflates two unrelated forecasts.

Alternatively (and more damning), Appendix C says "fractional improvement scales as ∆σ/σ_std ≈ (6.1%/0.15) α", giving for α = 0.19: (6.1/0.15) × 0.19 = **7.73%** ≈ "7.9%". If this *linear* scaling is what produced the abstract number, then the abstract contradicts §V's own "Fisher-positivity-respecting" α² form (which gives 9.4%). Either way, the abstract's central forecast does not reproduce from §V's inputs.

**P3-E18 (Appendix C Fig. 8, p.15 vs §V, p.10): Two incompatible single-tracer baselines.**
§V asserts σ(fNL)^std = 8.98 (single-tracer DESI QSO baseline). Fig. 8 in Appendix C displays "Baseline multi-tracer = 12.72" and (per the caption) "single-tracer baseline σ(fNL) = 16.85". These three numbers (8.98, 12.72, 16.85) cannot all describe the same configuration. The reader has no way to identify which Fisher setup is canonical, and the headline forecast σ(fNL) = 8.14 is referenced to one of them without ever being benchmarked against the others.

**P3-E19 (Table IV vs body §II–§VI): Caveat-numbering scheme is broken.**
Table IV lists caveats (a) through (j) — ten lettered rows. The body cites "§VI D caveat (i)" (multiple times in §II B, §V), "§VI D (b)", "§VI D (f)", and "§VI D (v)". Of these, (v) does not exist in Table IV at all. Further, (i) is ambiguous: §VI D's prose opens with paragraphs labeled "(i) DESI in-sample training–test overlap. (ii) Injection-recovery synthesis." — using *Roman* numerals — while Table IV uses the *letter* (i) for "Fisher positivity". The body's "caveat (i)" sometimes refers to the Roman-numeral prose item (in-sample overlap) and sometimes to the table letter (Fisher positivity). These are different claims being referenced under the same label.

**P3-E20 (Table I, p.7): "Total (cross-transfer, ACT-incl.) = 319,443" does not equal the sum of the visible per-survey rows.**
Summing the displayed Nanom column: 195,829 + 77,905 + 44,075 + 298 + 200 + 500 + 436 = **319,243**, not 319,443. The 200-object discrepancy is the quarantined ACT cross-transfer block, which the footnote *explicitly removes* from the per-survey rows ("not listed in the main per-survey block below") but then silently includes in the table total via the "ACT-incl." qualifier. A "total" row whose value disagrees with the sum of the rows it totals violates table consistency. Either show the ACT row or recompute the total to 319,243.

**P3-E21 (§IV A & Table I, p.9): The 58.8% aggregate SIMBAD-unmatched figure does not reconcile.**
Per-survey rates: DESI 99% (top-10K), SDSS 90%, LAMOST 50%, eROSITA 68%, NEOWISE 45%, Gaia 27%. 
- Simple mean: (99+90+50+68+45+27)/6 = 379/6 = **63.2%**.
- Weighted by Nanom (195,829, 77,905, 44,075, 298, 436, 500): weighted average = ~**89.5%** (dominated by DESI ×99%).
- Headline 58.8%.

No standard reweighting reproduces 58.8%. If DESI is downweighted because its 99% applies only to top-10K (not 195,829), the appropriate proxy is unclear — but the body never discloses the aggregation rule. This number is unverifiable.

**P3-E22 (§II D Step 5 vs §III H, pp.3, 8): Plant count inconsistency.**
§II D Step 5: "500 planted signals per survey at six amplitude levels". §III H NEOWISE: "Mask injection-recovery: 1000/1000 = 100%". Fig. 7 caption: "NEOWISE ecliptic-pole mask (PASS, 1000/1000 = 100%)". The protocol says 500; the survey-specific report says 1000. Doubling the plant count silently changes the statistical power of the gate and should be either disclosed as a per-survey deviation or harmonized.

---

## NEW MAJOR findings

**P3-M17 (Fig. 2, p.5): LAMOST count shown is the discarded cross-transfer number.**
Fig. 2 left panel legend: "LAMOST DR10 (44,075)". This is the cross-transfer count that §III D and Table I footnote ‡ explicitly supersede with the Path-C native count 113,342. The headline-tier catalog has 113,342 LAMOST objects; the figure displays the pre-rebuild number. Stale figure.

**P3-M18 (Abstract, p.1 vs §IV C, p.10): Abstract names two of three DESI×SDSS matches and omits the known QSO.**
Abstract: "Three DESI×SDSS cross-matches include a time-variable source (TIC 374313355) and an uncataloged BAL QSO at z ≈ 0.86." §IV C lists three: (1) known QSO at z ≈ 1.55, (2) TIC 374313355, (3) BAL QSO at z ≈ 0.86. The abstract drops match (1). For a paper whose validation rests on cross-survey concordance, the known-QSO match is the validation anchor — its omission inflates the apparent discovery count.

**P3-M19 (§II B vs §II D Step 1, pp.2, 3): Training-pool size inconsistency for DESI.**
§II B: "a representative subset of the data (47,000 spectra for DESI ...)". §II D Step 1: "A fresh BigAE is trained on a 2–5×10⁵-spectrum quality-selected subset of each survey's own data." The DESI native model is described as trained on 47K, but the Path-C protocol asserts 200K–500K. Either DESI does not satisfy Step 1, or the Step 1 protocol description is inconsistent with the DESI implementation.

**P3-M20 (§V, p.10): The "5,384 QSO-candidate sample" appears without derivation.**
"A Landy–Szalay angular two-point analysis on the full 5,384 QSO-candidate sample (26,920 anomaly-window-matched randoms, 30-region jackknife, signal bins θ ∈ [0.04°, 0.25°])". Where do 5,384 candidates come from? §III B says 12 z ≈ 6 QSO candidates. §III A says ∼ 8,300 objects are anomalous QSO/star spectra (0.037% × 22.5M, but classified subset is 6.5M giving ∼2,400). The 5,384 number is the entire empirical basis for the αjk measurement and is never tied to upstream catalog cuts.

**P3-M21 (§V, p.10 vs Appendix C Fig. 8): Gold/Silver subsample definitions inconsistent.**
§V Gold+Silver: "1,122-object Gold+Silver subset". Fig. 8: "anomaly_gold ñ = 8.5e-06" and "anomaly_silver ñ = 4.5e-05" in (Mpc/h)⁻³. The 1,122-object subset has no number-density derivation; the Fig. 8 ñ values have no count derivation. The two "Gold+Silver" definitions in the paper share a name but not a definition.

**P3-M22 (§V A vs Abstract, p.12): Sigma-choice for NANOGrav cherry-picks the more-favorable interpretation.**
The paper presents both γ = 2.567 ± 0.382 (Gaussian-approx) and γ = 2.591⁺⁰·²⁹¹₋₀.₂₈₇ (asymmetric 68% CI). For the matter-bounce test:
- Using ±0.382 (mean shift): (3.0 − 2.567)/0.382 = **+1.13σ** (marginally consistent).
- Using ±0.291 (asymmetric mode/median): (3.0 − 2.591)/0.291 = **+1.41σ** (~10% probability mass beyond).

For the SMBHB test:
- Using ±0.382: (4.33 − 2.567)/0.382 = **+4.62σ** (strongly disfavored).
- Using ±0.291: (4.33 − 2.591)/0.291 = **+5.97σ** (still strongly disfavored).

The author chose ±0.382 throughout. This choice *minimizes* the bounce tension (1.13σ favorable) while keeping the SMBHB rejection (4.62σ still decisive). Picking the σ that maximizes both the bounce-favorable narrative *and* still produces a "decisive" SMBHB rejection looks like an a-posteriori choice. The author justifies it ("the appropriate mean-shift uncertainty for the +1.13σ parameter-shift test") but the same logic would apply to the ±0.291 quantile width for a quantile-based test, and the choice is never benchmarked against either.

**P3-M23 (§II D Step 1 / "criterion (b)"): The Planck native gate-PASS is a fallback ladder.**
"Retained if (a) validation loss ≤ 0.30 after ≤ 100 epochs, or (b) injection-recovery ≥ 50% at 5σ." Planck has val_loss = 0.4437 — explicit FAIL on (a), saved by 100% on (b). This OR-gate means a model can fail the in-distribution reconstruction quality check and still be admitted if it detects injected signals. For an autoencoder, those are correlated: a model that can recover Gaussian bumps need not be good at flagging genuine CMB anomalies. The OR-gate is methodologically permissive and should be acknowledged as such.

**P3-M24 (§IV B, p.10): Spatial uniformity correlations computed at pixel level, not anomaly level.**
"Spearman r = 0.0005, p = 0.92" and "Pearson r = 0.006, p = 0.21". For 378,280 anomalies, even r = 0.005 would give p < 10⁻³. The reported p-values match approximately n = 38,330 (the HEALPix pixel count), so the correlation was computed across pixel-level anomaly densities, not at the object level. This is not stated. Anomaly-level analysis would likely show stronger latitude dependence.

**P3-M25 (Acknowledgments / Data Availability, p.14): Catalog is "private pending arXiv acceptance".**
The principal product of the paper is the catalog. Conditioning its release on arXiv acceptance is unusual; PRD requires public data availability at submission, not at acceptance. Either the catalog is released now (so reviewers can verify the 378,280 number, the 17.8% novelty fraction, the 637 multi-survey matches) or the paper cannot be reviewed on its principal claim.

**P3-M26 (Reference [33] entry, p.19): Submission-year vs publication-year disclosure should not be in the bibliography.**
"[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]" — this is a draft-management note that should not appear in published references. (Already partially flagged as P3-M16 in the first pass for being "internal commentary"; this second-pass note adds that it directly affects citation indexing.)

---

## NEW MINOR findings

**P3-m1 (§I, p.1): "This is the largest-scale application of autoencoder anomaly detection across seven astronomical archives."**
"Largest-scale" needs benchmark. The comparison cited (Liang et al. ~250K spectra) is single-survey. No other multi-archive autoencoder anomaly campaign is cited for comparison. The claim is plausible but unbenchmarked.

**P3-m2 (§III A, p.4): "The three highest-scored anomalies are Z-dominant with scores of 25.2, 24.6, and 24.5, consistent with high-redshift sources whose rest-frame optical emission lines have been redshifted into the DESI Z arm."**
This paragraph appears twice on page 4 (once at top, once after the SNR-correlation discussion). Verbatim or near-verbatim duplication.

**P3-m3 (Table V, p.16): Throughput numbers inconsistent with training scale.**
DESI: "∼3,600 s" training, batch size 512, 47K spectra → ~92 batches/epoch × (say) 100 epochs = 9,200 batches in 3,600 s = 0.39 s/batch. On H200 for a 660K-parameter MLP, that is ~100× slower than expected. Either the training was CPU-bottlenecked (and the "GPU pipeline" claim is misleading) or the time is wrong.

**P3-m4 (§II D Step 4, p.3): "the rejected 3.9% polar-cap fraction is 2.6× the uniform-null expectation".**
The uniform expectation for the |becl| > 80° cap is (1 − cos 80°)/2 + (1 − cos 80°)/2 per pole = (1 − cos 80°) = 0.826 × 2 → too large. Actually, fraction of sphere at |becl| > 80° = 2 × (1 − sin 80°) = 2 × (1 − 0.9848) = 0.0303 = **3.0%**. Footnote says "(1.52%)". That value 1.52% would correspond to a single polar cap of |becl| > 80° = (1 − sin 80°) = 0.0152 ✓ — *one* cap only. But the rejected fraction 17/436 = 3.9% is for *both* caps. So either the null expectation should be 3.0% (two caps), giving 1.3× not 2.6×, or the rejected count should be one cap (8-9 objects), giving consistent ratio. The 2.6× excess claim is off by ~2× depending on interpretation.

**P3-m5 (§II B, p.2): "For DESI DR1, µval ≈ 0.0287 (validation MSE) and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143 on the rescaled scale."**
Then σval = (0.143 − 0.0287)/5 = 0.02286. This σval is implicit, not stated. A reader trying to reproduce the threshold must back it out from the prose.

**P3-m6 (§III F, p.6): "Top-200 native anomaly patches (score range [0.558, 0.621])".**
The score range [0.558, 0.621] (width 0.063, mean ~0.59) is very narrow for the top 1% of a "natively retrained" detector. Either the score distribution is pathologically compressed or the 200 patches are at the long tail of a distribution where ranking is dominated by noise. No score-distribution figure is shown for the Planck native model.

**P3-m7 (§V, p.10): "The single-tracer DESI QSO baseline is σ(fNL)^std = 8.98".**
Adopted without citation. Standard DESI QSO single-tracer Fisher forecasts in the literature (e.g., Mueller et al., Sailer et al.) span 5–20 depending on kmax, fsky, photo-z systematics. 8.98 is plausible but unsourced.

**P3-m8 (Conclusion §VII point 6, p.14): "OOD control-vs-control 0.874 (PASS)".**
0.874 doesn't appear anywhere in §II B's OOD discussion, which gives J̄_prod×ctrl = 0.732. Where does 0.874 come from? Either a different OOD test not described in the body, or a stale number.

**P3-m9 (Abstract, p.1): "(σ(fNL)^std = 8.98 single-tracer baseline)".**
The σ symbol overloading is acknowledged in §II B (z-score S vs redshift z), but σ(fNL) is now used for both the Fisher uncertainty and the validation-set standard deviation σval. With the additional posterior-summary σ for NANOGrav (±0.382), the paper has three "σ" notations active simultaneously, never disambiguated.

**P3-m10 (Table I footnote, p.7): "Empirical intersection (§VI D (f)): 284 of 298 ... overlap 95.3%. The two anomaly detectors agree on the dominant population to a precision well beyond what either single detector achieves against random; the earlier 'strict subset' framing is replaced with this exact 284/298 = 95.3% overlap."**
"Earlier strict subset framing" — what earlier framing? Within this paper, or a prior revision? Reads as a tracked change leaked into the manuscript.

**P3-m11 (§VI E, p.13): "and a ~90× increase in sample size".**
22.5M / 250K = 90×. ✓ But the rate is normalized; "increase in sample size" with similar rate is a robustness claim, not a discovery claim. The framing in P3-M1 (first pass) applies: 90× more spectra at similar rate ≠ 141× more discoveries.

**P3-m12 (§V A, p.12): "Companion multi-PTA datasets (EPTA DR2 [26], PPTA DR3 [27]) independently report HD-correlated signals consistent with NANOGrav".**
"Consistent with" is unquantified. EPTA and PPTA report slightly different γ central values; this is a known mild tension. The "consistent with" hedge papers over it.

**P3-m13 (Bibliography [11], p.19): Liang et al. citation.**
"Mon. Not. Roy. Astron. Soc. 525, 1078 (2023), arXiv:2307.07664." This is the Liang+ paper, but the main text says they searched "~250,000 DESI EDR spectra, finding 2,685 anomalies (1.07%)". The arXiv version typically reports the search on the BGS sample; cross-check the comparison sample sizes to ensure the "141×" and "73×" claims use matched baselines (BGS-only vs. full Main Survey).

**P3-m14 (§I, p.1): "When combined with multi-wavelength catalogs from eROSITA [4], Gaia [5], NEOWISE [6], and microwave sky surveys from Planck [7] and ACT [9], the total data volume accessible to a single research group now exceeds tens of millions of sources across the electromagnetic spectrum."**
This sentence motivates the paper but does not cite ACT's full DR6 [9] correctly in context — ACT is then quarantined, so its inclusion in the motivation is performative.

**P3-m15 (§II A, p.2): Architecture description lacks complete specification.**
"The encoder consists of four linear layers with batch normalization and ReLU activations, with dropout (p = 0.15, 0.10) after the first two layers". Four layers but dropout on only two — which two? Width sequence not specified (the full architecture is deferred to the companion data repository). Reproducibility requires the layer widths in the paper.

---

## Summary of new findings

| Class | Count | Most damaging |
|-|-|-|
| New ESSENTIAL | 6 | P3-E17 (7.9% number doesn't reproduce), P3-E18 (incompatible baselines) |
| New MAJOR | 10 | P3-M22 (σ-choice cherry-picked), P3-M25 (catalog withheld) |
| New MINOR | 15 | P3-m4 (polar-cap null), P3-m11 (90× vs 141× framing) |

The most consequential new findings are **P3-E17 and P3-E18**: the abstract's headline cosmological forecast number ("7.9% improvement, σ(fNL) = 8.14") does not arithmetically reproduce from the inputs in §V, and Appendix C uses a single-tracer baseline (16.85) that is a factor ~1.9× larger than §V's baseline (8.98). These are not subtle issues; they indicate the cosmology calculations in §V and Appendix C were performed by different paths with different assumptions and never reconciled. Combined with **P3-E19** (the broken caveat-numbering scheme) and **P3-E20** (Table I total off by 200), the paper shows multiple signs of having been assembled from drafts with mismatched bookkeeping conventions.
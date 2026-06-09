# P3 auto-2026-06-08_2353pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (12069 chars)
**Wall time**: 529.9s

---

# Referee Report — Manuscript "Spectrally Unusual Sources at Scale…"

## Overall assessment

This is a 20-page submission whose abstract advertises (i) the "largest-scale" multi-survey anomaly catalog (378,280 sources), (ii) a cosmological forecast σ(f_NL)=8.14, and (iii) a NANOGrav matter-bounce versus SMBHB Bayes factor of 7.1×10³. On careful audit, every one of the three load-bearing claims either folds into a null result, depends on data the authors themselves classify as contaminated, or disagrees with the cited primary literature. The Path-C self-validation protocol is published *with three of its six gates explicitly failed* and the failing surveys retained in the catalog regardless. The manuscript also carries multiple internal-bookkeeping artifacts in the camera-ready text, an internally inconsistent score definition, a figure caption whose baseline σ(f_NL) disagrees with the body by a factor ~2, and duplicate body text. This does not meet the PRD bar.

---

## ESSENTIAL findings

**P3-E1 — Inconsistent definition of the canonical anomaly score S (p. 2, §II B).**
Eq. (2) states "μ_val and σ_val are the mean and standard deviation of MSE on the held-out 20% validation split." The very next paragraph states "σ_val is set such that the S > 5 catalog threshold corresponds to MSE≈0.143 on the rescaled scale." These are mutually exclusive: σ_val is either the empirical validation std *or* it is chosen to hit a target threshold. The entire paper's "5σ" anomaly language hangs off this definition. **Required:** pick one definition, derive σ_val numerically, and propagate.

**P3-E2 — Headline σ(f_NL) "improvement" is statistically a null result presented as a forecast (Abstract, p. 1; §V, p. 11).**
The empirical α_jk = 0.19 ± 0.65 is 0.29σ from zero with 95% CI [−1.08, +1.46]. The "7.9% improvement" σ(f_NL)=8.14 vs baseline 8.98 has 1σ envelope [3.92, **8.98**] — i.e. the upper bound is *exactly* the no-improvement baseline. This is not a forecast of an improvement; it is consistent with no improvement at <1σ. The abstract must not present this as a positive result. The accompanying "consistent with no improvement at <1σ" hedge is contradicted by repeating "7.9% improvement" as a headline number.

**P3-E3 — Fig. 8 caption (p. 15) disagrees with §V baseline by ~2×.**
Fig. 8 caption: "single-tracer baseline (σ(f_NL)=16.85)" and "dense-tracer limit σ(f_NL)=11.71"; the legend marks "Baseline multi-tracer = 12.72." The body (§V, p. 11; Appendix C Table VII) uses σ(f_NL)^std = 8.98 throughout. These cannot both be correct. One of (a) the body's headline 7.9% improvement claim or (b) the Fig. 8 sensitivity plot is using the wrong Fisher matrix. This must be resolved before any f_NL number can be quoted.

**P3-E4 — Appendix C Table VII (p. 16) references "fiducial 7-bin Fisher" while §V/§VI use a 5-tracer Fisher.** Number of bins/tracers driving the Fisher information is the most basic input to a forecast and the document carries two incompatible labels for it.

**P3-E5 — Internal bookkeeping in references (p. 19, ref. [33]).**
Reference [33] carries an in-bibliography note: "publication-year 2024; bibkey label retained as `Heinrich2023` for arXiv-submission-year continuity". This is a private build artifact and must be stripped from a published reference list.

**P3-E6 — Version-history language in Table I § footnote (p. 6).**
"...the earlier 'strict subset' framing is replaced with this exact 284/298 = 95.3% overlap." This is review-log prose, not a published-paper sentence. The reader was never shown the earlier framing.

**P3-E7 — Version-history language in Table IV row (j) (p. 14).**
"GS corrected: σ(f_NL)^GS ∈ [0.94, 8.98] central 1.95; prior ±7.43 dropped". A "prior" value that has been "dropped" should not appear in the final table. The reader cannot evaluate "Fisher-pos. α²-form; caveat (i)" without context that has been removed.

**P3-E8 — Three of six methodological gates FAIL, yet the failing surveys are published in the headline catalog.**
LAMOST (5.8% at 5σ), Gaia (5.2%), eROSITA (1.2%) all FAIL the ≥50% injection-recovery gate stated in §II D Step 1. The paper retains their anomalies in the 378,280 headline anyway, with text such as "FAIL-with-diagnostic" and "exploratory tier." A gate that does not gate is not a gate. Either (a) raise the bar and exclude the failing surveys from headline counts, or (b) remove the "Path-C six-step validation protocol" framing. The current presentation gives the impression of validated work that has, in fact, failed its own published criteria for half its surveys.

**P3-E9 — Cross-transfer ACT block used to manufacture a science claim while admitted to be undertrained (§IV D, p. 10; Appendix F, p. 18).**
§IV D states "Planck and ACT anomalies do not cluster... This null result demonstrates that CMB patch anomalies from autoencoder analysis are dominated by survey-specific systematics rather than primordial cosmological signals." Appendix F simultaneously states that ACT cross-transfer has validation MSE ≈ 2.2×10⁴ (gate fail by factor 7×10⁴) and <1% injection-recovery at 5σ. A null cross-correlation between a working detector and a non-functional one is meaningless. The "important negative result" claim must be withdrawn.

**P3-E10 — γ value from NANOGrav re-fit disagrees with NANOGrav's own published HD-correlated power-law result (§V A, p. 12).**
NANOGrav 15-yr (Agazie et al. 2023, ref. [18]) reports γ ≈ 3.2 ± 0.6 from the HD-correlated power-law fit. The author's re-fit to the public KDE free-spectrum product gives γ = 2.567 ± 0.382 — a >1σ shift in the central value and an apparent factor-1.5 reduction in uncertainty. This needs (i) explicit head-to-head reproduction of the NANOGrav-published value as a self-consistency check; (ii) explanation of why the central value moves; (iii) honest acknowledgment that the Bayes factor B_{MB/SMBHB}=7.1×10³ depends on a γ posterior the original NANOGrav analysis did not endorse. As presented, the "decisive on Jeffreys' scale" claim is unsupported.

**P3-E11 — Duplicate body text (§III A, p. 4).**
The block beginning "Galaxies are flagged at ∼20× the QSO rate (0.75% vs. 0.037%); anomalies peak at z ∼ 0.75 vs. z ∼ 0.93 for normal spectra. The three highest-scored anomalies (S=25.2, 24.6, 24.5) are Z-dominant, consistent with high-z Gunn–Peterson absorption." is repeated essentially verbatim immediately afterwards starting "Across the 6.5 million spectra in DESI DR1 that carry a validated TARGETTYPE..."

**P3-E12 — Title and abstract jargon "Path-C" is never expanded.**
"Path-C" appears in the title and abstract and ~30 times in the body, but the manuscript never defines what "Path" or "C" stand for. It reads as an internal milestone tag.

**P3-E13 — Headline 378,280 mixes incompatible strata.**
378,280 = 378,080 point sources + 200 Planck CMB *map patches*. These are not the same kind of object (the Planck entries are sky regions). The footnote acknowledges this and asks downstream analysis to use 378,080. Adding incompatible objects to inflate the headline is dishonest. Quote only 378,080 in the title and abstract.

**P3-E14 — The "141× the largest prior single-survey catalog" claim is misleading.**
378,080 includes 113,342 LAMOST objects that the same paper labels "98% blue-excess training-bias artifact, injection-recovery gate FAIL." The honest comparable number for a like-for-like single-survey win is DESI 195,829 → 73×, which the paper does also quote — but the abstract leads with the 141× figure built on data the author has already disowned.

**P3-E15 — Conclusion §VII point 6 cites an OOD Jaccard "0.874 (PASS)" (p. 14) that does not match any number stated earlier in the body.**
§II B reports J̄_prod×ctrl = 0.732; §VI D (i) repeats 0.732. The number 0.874 appears nowhere else and is not derived. Either correct the conclusion or define the quantity.

---

## MAJOR findings

**P3-M1 — Spectroscopic input scopes are not justified.** Gaia DR3 input = 50,000 variables (out of >10 million in vari catalogue); NEOWISE input = 43,518 sources (out of >10⁹). The paper presents these as full-survey scans. The 1% top-percentile threshold produces predetermined counts (500, 436); footnote in Table I admits "their 1.00% anomaly rates should not be interpreted as independent measurements." Then the rates *are* reported as if they were, including in the unique-object headline.

**P3-M2 — 5,384 QSO-candidate sample (§V, p. 11) lacks provenance.** The sample is the input to the empirical bias measurement that drives the headline f_NL forecast. Its construction (selection function, redshift distribution, n̄, host galaxy match radius) is not described. PRD requires this for a Fisher forecast claim.

**P3-M3 — Fig. 1 (p. 4) shows the *quarantined* state of the catalog.** Figure caption: "Mollweide projection of the initial cross-transfer anomaly baseline (319,443 detections shown; canonical Path-C unique count is 378,280...)". The headline figure of the paper depicts a superseded baseline including ACT DR6 which is excluded from results. Replace with a figure of the canonical Path-C 378,080-object catalog.

**P3-M4 — Fig. 2 (p. 5) right panel shows scores up to S ≈ 10¹¹, an admitted cross-transfer artifact.** Caption acknowledges "the extreme dynamic range of SDSS is a cross-transfer artifact." Then why dedicate half of Fig. 2 to it? Use the native-retrain SDSS score distribution.

**P3-M5 — Fig. 7 (p. 13) legend lists 6 curves (SDSS×2, LAMOST×2, eROSITA, Gaia), but the caption claims "three additional non-spectral retrains (Planck CMB native convolutional autoencoder, NEOWISE ecliptic-pole mask) brought into the same axis."** Planck and NEOWISE traces are not visible in the legend; presumably hidden by the 100% PASS line. Caption is misleading about what is plotted.

**P3-M6 — Table III (p. 7) double-axis presentation.** Two anomaly scores per source (S_BigAE, S_IF,raw) on incomparable scales (one is 0–3.5×10⁴, the other 0–~1). The reader cannot judge which one corresponds to the 298-source headline cut without footnote text. State explicitly that S>0.259 refers to S_BigAE only.

**P3-M7 — "Bayes factor decisive" framing (§V A) abuses the Savage–Dickey statistic.**
B_{MB/SMBHB} = (B_{MB/free}) / (B_{SMBHB/free}) only equals the MB-vs-SMBHB Bayes factor if MB and SMBHB are both nested in the same free-γ prior. The matter-bounce γ=3 and SMBHB γ=4.33 are *point predictions* within different cosmologies; the Savage–Dickey ratio compares posterior density to prior density at those single points and is highly sensitive to the prior width [0,7]. A 50% wider γ prior changes the Bayes factor proportionally. State the prior sensitivity; the "decisive on Jeffreys' scale" claim does not survive a prior-width sensitivity test.

**P3-M8 — "Genuine novelty fraction ~17.8%" (Abstract).** This is one CDS X-Match cone-search at the top-1,000 stratum. No null/control test (e.g., random positions on the same footprint, expected coincidence rate, false-negative rate of CDS X-Match for catalog non-detections) is presented. PRD novelty claims require a quantitative false-positive estimate.

**P3-M9 — SPHEREx forecast (§V, p. 12).** "The projected SPHEREx multi-tracer forecast yields 3–5σ detection significance for the matter-bounce f_NL = −35/8 prediction (uncertainty range reflects systematic degradation budget)." No equation, no derivation, no inputs. Heinrich et al. forecast σ(f_NL)≈0.7 for the bispectrum-only SPHEREx; the leap to "3–5σ" with the AI-anomaly tracer subset is not shown.

**P3-M10 — Page count vs. actual content.** Three of seven retained surveys fail validation; one (ACT) is fully quarantined; the f_NL forecast is null; the NANOGrav fit is in tension with the original NANOGrav publication. The remaining defensible content (DESI native catalog of 195,829 anomalies + ~3 individually interesting cross-survey objects) does not require 20 pages. Recommended maximum: 10–12 pages if the cosmology sections are removed; 15 pages if they are retained as clearly-labeled appendices.

**P3-M11 — α_jk uncertainty propagation.**
Eq. for σ(f_NL)² inverse uses αjk = 0.19 with σ_α = 0.65, but the "1σ envelope [3.92, 8.98]" is computed by inserting α±σ_α. This is not a 1σ envelope of σ(f_NL); a proper propagation requires the asymptotic-form Jacobian under non-Gaussian α posterior support across zero. Show derivation.

**P3-M12 — Gate criteria are OR-combined (§II D Step 1), so the Planck CMB native autoencoder passes gate (b) despite gate (a) val_loss 0.4437 being ~50× the threshold 0.30.** A 50× val-loss failure of criterion (a) is not "PASS" — the OR combination defeats the purpose of having criterion (a) at all. Justify.

**P3-M13 — Table I "Path-C unique (primary)" row anomaly rate 1.01% is computed against the *cross-transfer* N_total (37,272,042) but the catalog uses *native-retrained* counts. The rate denominator and numerator come from different scoring runs.**

**P3-M14 — γ_GW = 2.567 ± 0.382 is reported with two different uncertainty conventions on p. 12 ("±0.382" mean-shift, "+0.291/−0.287" credible-interval). The text explains this but uses both interchangeably without distinguishing in subsequent +1.13σ and +4.61σ tests.** Specifically: which σ enters the +4.61σ SMBHB exclusion? If it's the credible-interval width 0.29, the exclusion grows to +6.1σ. Internal arithmetic inconsistency.

**P3-M15 — Table II (p. 7) sums to 77,905 with 52.7% "Uncategorized" — over half the SDSS anomaly classification is "Uncategorized," yet the inferred-categories chart in Fig. 3 (right) and the body claim "84% cool dwarfs." 52.7% + 33% NIR-excess ≠ 84% cool dwarfs without explicit reconciliation.**

---

## MINOR findings

**P3-m1** — DESI fiber-collision selection effects (§III A, p. 4) "not modeled in the current analysis." For a catalog whose spatial uniformity is used to argue for astrophysical origin, this is a non-trivial omission.

**P3-m2** — Spearman correlation ρ=−0.03 with p=0.12 on N=2,670 (§III A) is noted as "no practically significant" — the p-value is not significant, but ρ at that sample size with p=0.12 is consistent with a weak true correlation. Tone down.

**P3-m3** — Page 4 Fig. 1 legend shows 8 surveys including ACT DR6 despite ACT being quarantined throughout the paper.

**P3-m4** — Acknowledgment thanks "RunPod" for compute — informal. Acceptable but unusual.

**P3-m5** — Table I caption is 23 lines long and contains substantive results ("Empirical intersection: 284 of 298 canonical-S top-298 sources..." with hypergeometric p≈0). Captions should not carry results.

**P3-m6** — §VI D Table IV refers to "C = resolved in paper" but the table column is unlabeled.

**P3-m7** — The Bayes factor BMB/SMBHB is quoted as 7.1×10³ in abstract, 7.14×10³ in §V A, and 7.14×10³ in conclusions. Pick one precision.

**P3-m8** — Acknowledgments are buried before the bibliography but Data Availability ("private pending arXiv acceptance") contradicts the abstract claim "The catalog... is publicly released."

**P3-m9** — References [33] and abstract list "Heinrich et al." bispectrum-only forecast σ(f_NL) ≈ 0.7. This number should be traced explicitly to a table or equation in Heinrich+24 for verification.

**P3-m10** — "spectroscopic redshift is always written z with astrophysical context; the anomaly score S is never called 'z'" (p. 2) is meta-prose; remove.

**P3-m11** — Page 12 §VI C: "Six limitations govern interpretation of these results" — actually seven items follow if we count the unnumbered "Novelty fractions." Recount.

**P3-m12** — Table V (p. 16) lists ACT DR6 row even though ACT is quarantined. Caption admits this but the row should be in Appendix F only.

**P3-m13** — Fig. 9 (p. 17) panel labels say "AE=…" for the score column; main text calls this S. Use one symbol consistently.

**P3-m14** — Bibliography reference [12] "Nicolaou et al." marked "in press" — confirm at proof stage.

---

## NIT findings

**P3-n1** — "Mollweide projection" — Fig. 1 axes are labeled in degrees but no grid spacing label.

**P3-n2** — Inconsistent dash style: "log_loss" vs "val loss" vs "val_loss."

**P3-n3** — Page 1 abstract has a manual hyphenation glitch ("Native-Trained").

**P3-n4** — "≲" and "<" mixed; pick one.

**P3-n5** — Equation (E1) lacks numbering parenthesis closure consistency.

---

## Summary recommendation

**REJECT**

The paper packages a methodologically interesting but scientifically modest anomaly catalog inside an inflated narrative whose three flagship claims do not survive audit. The σ(f_NL) "forecast" is consistent with no improvement at <1σ yet is sold as a 7.9% improvement in the abstract; the NANOGrav Bayes factor depends on a γ posterior that disagrees with NANOGrav's own published value and on a prior-width-sensitive Savage–Dickey ratio; the headline 378,280-object catalog mixes incompatible strata, includes a survey the authors themselves classify as a training-bias artifact, and is built around a validation protocol whose own gates fail for half the input surveys. The body carries an internally inconsistent score definition (Eq. 2), a Fig. 8 baseline that disagrees with the §V baseline by a factor ~2, in-bibliography version-history annotations (ref. [33]), version-history prose in two tables, duplicate body text, and a quarantined survey still presented in the headline figure. PRD's bar is novel, validated, and tightly-claimed physics. With the cosmology overclaims withdrawn this manuscript could become a useful methods paper for an astronomy journal, but in present form it is not acceptable to PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

# Fresh-Eyes Pass — Additional Findings

I re-audited the paper against the ten checklist categories. The arithmetic check found three genuinely new contradictions, including one that affects the headline f_NL number. Several internal-reference and stale-number issues escaped the first pass.

---

## ADDITIONAL ESSENTIAL findings

**P3-E16 — The σ(f_NL)=8.14 value and the "7.9% improvement" headline are arithmetically inconsistent (Abstract, p. 1; §V, p. 11).**
The Fisher-positivity form 1/σ² = F₀ + cα² with F₀ = 1/8.98² and c = 0.0747 (§VI D caveat (i)) gives, at α_jk = 0.19:
1/σ² = 0.012402 + 0.0747 × 0.0361 = 0.015099, hence σ = **8.138** ≈ 8.14 ✓.
But (8.98 − 8.14)/8.98 = **9.35%**, not 7.9%.
The 7.9% figure matches *linear scaling* of the Table VII fiducial (6.1% at α=0.15) up to α=0.19: 6.1% × 0.19/0.15 = 7.73% ≈ 7.7–7.9%. The body simultaneously quotes the **nonlinear-Fisher σ** and the **linear-scaling improvement**. These come from two different forecast formalisms (the very issue Appendix C is supposed to clarify) and cannot both be the headline. Either (i) σ=8.14 with 9.35% improvement, or (ii) σ=8.29 (linear) with 7.9% improvement. The abstract publishes the inconsistent pair.

**P3-E17 — Stale Jaccard value in Conclusions §VII point 6 (p. 14).**
The text reads "DESI 5-fold Jaccard stability J̄ = 0.862 (PASS); OOD control-vs-control **0.874** (PASS)." Both §II B and §VI D (i) state that the production-vs-5-seed-control Jaccard is **0.732**, not 0.874. The value 0.874 appears nowhere else in the paper. This looks like a number from an earlier version that survived editing. The two numbers (0.732 and 0.874) are >18% apart and cannot both be the same quantity.

**P3-E18 — Table I caption references undefined footnote symbols ♡ and ♠ (p. 6).**
The caption text reads "see footnotes ♡ and ♠ for the per-survey three-threshold disclosure" and the table column attaches ♡ to SDSS DR18 and ♠ to LAMOST DR10. The actual table footer carries footnotes ¶, †, ‡, ║, § — there is no ♡ or ♠ footnote anywhere on the page. The reader cannot find the disclosed thresholds the caption advertises.

---

## ADDITIONAL MAJOR findings

**P3-M16 — Dangling cross-reference §VI D (v) (Table I §-footnote, p. 6; Fig. 7 caption, p. 13; Table V footnote).**
The §-footnote of Table I states "IsolationForest cross-validation-stability footnote (§VI D caveat (v))…" Fig. 7 caption likewise points the reader to "§VI D (v)" for the ecliptic-pole mask injection. The body of §VI D contains only items (i) "DESI in-sample training–test overlap" and (ii) "Injection-recovery synthesis." There is no (iii), (iv), or (v). Three high-visibility references point to non-existent text.

**P3-M17 — Inconsistent caveat-labeling system between §VI D body and Table IV.**
§VI D body labels caveats with **Roman numerals** (i), (ii). Table IV labels them with **lowercase letters** (a)–(j). Cross-references in the body freely mix the two ("§VI D (e)" in §V; "§VI D (f)" in Table I; "§VI D (i)" in §V; "§VI D (j)" in §V). A reader following these cross-references cannot tell which labeling is canonical or which item is meant. The Roman-numeral list in §VI D includes only two entries; the Table IV alphabetic list has ten; they overlap partially.

**P3-M18 — Fig. 2 caption mislabels LAMOST count provenance (p. 5).**
Caption: "cross-transfer for SDSS, **native for DESI/LAMOST**." But the LAMOST curve in the figure shows **44,075** anomalies — which is the **cross-transfer** count per Table I footnote ‡. The native LAMOST count is **113,342**. Fig. 2 is showing the cross-transfer LAMOST distribution while claiming to show the native one. This is the same kind of "before/after" confusion that the abstract sets up Path-C to resolve, and the headline figure of the spectroscopic distributions still mixes them.

**P3-M19 — "Local-linear propagation σ ≈ 8.98 − 3.66α" is mathematically incompatible with the stated stationary-point structure (§VI D caveat (i)).**
The Fisher-positivity form has 1/σ² = F₀ + cα², so dσ/dα|_{α=0} = 0 by construction (α=0 is a stationary point of σ, as the caveat correctly notes). A linear expansion of σ around α=0 therefore has slope **0**, not −3.66. The −3.66 must be a chord secant between (α=0, σ=8.98) and (α=0.15, σ=8.43), not a derivative — but the prose calls it "local-linear propagation." Either the slope is misidentified or the stationary-point claim is wrong. The caveat is logically self-contradictory as written.

**P3-M20 — SDSS native top-77,905 cut: number is matched to the cross-transfer count rather than to a principled threshold (Table I footnote ‡; §III C).**
The native re-score is on 1,925,279 SDSS spectra; the published native count is **77,905** at S ≥ 0.1060. This is 4.05% of the re-score pool, not the "top 1%" cut applied to all other percentile-selected surveys, and not the absolute S > 5.0 cut applied to DESI (which would yield 12 sources). The 77,905 number is identical to the cross-transfer count, which suggests the threshold was *chosen* to make the cross-transfer and native catalogs the same size — defeating the purpose of an independent native re-score for comparing scales. No principle is offered for selecting S ≥ 0.1060.

**P3-M21 — Multiple bibliography entries appear to be uncited.**
On a body-text search I find no citations of refs [25] Hellings & Downs 1983, [29] Phinney 2001, [34] Münchmeyer et al. (kSZ tomography), [36] Lentati et al. 2013, or refs [38]–[41] (Bonvin & Durrer, Challinor & Lewis, Di Dio et al.) The GR-projection corrections discussion in §V mentions the topic but does not cite [38]–[41]. The "Verde 2013" ref [24] also appears uncited. PRD style discourages padded bibliographies.

**P3-M22 — §III A switches denominators between the headline 0.87% and the per-class breakdown without flagging the change (p. 4).**
"195,829 anomalies above the S > 5.0 threshold, an anomaly rate of 0.87%" uses N = 22.5M as the denominator. The next paragraph "galaxies are flagged at ∼20× the QSO rate (0.75% vs. 0.037%); anomalies peak at z ∼ 0.75" uses N ≈ 6.5M (validated-TARGETTYPE subset only). The two rates are not directly comparable; the 0.75% galaxy rate, applied across the full 22.5M catalog, would already exceed the headline 0.87%. The reader is given conflicting frames within the same paragraph.

**P3-M23 — NEOWISE polar-cap "2.6× excess" significance not quantified.**
17/436 = 3.9% polar-cap fraction vs uniform-null 1.52% (1−cos 10°). Expected count = 6.6, observed = 17, Poisson significance ≈ (17−6.6)/√6.6 = +4.05σ. The paper quotes only the ratio "2.6×" and reads it as decisive ("quantitatively confirming scan-pattern contamination"); it does not state the Poisson significance, and the small absolute count (17) makes the significance the right quantity to quote.

**P3-M24 — Table VII (Appendix C) uses "fiducial 7-bin Fisher" with baseline σ(f_NL)^std = 8.98, while the Shot-noise subsection of the same Appendix C uses a "canonical 5-tracer configuration" with baseline σ(f_NL)^std = 16.85 and dense-limit 11.71.**
These are different Fisher matrices yielding different baselines (8.98 vs 16.85 — almost a factor of 2). They are presented in the same appendix and the reader is given no rule for which one supersedes the other. Fig. 8 implicitly takes the 5-tracer side; the body §V exclusively uses the 7-bin side. The forecast is therefore under-specified at the level of "what is the single-tracer baseline."

---

## ADDITIONAL MINOR findings

**P3-m15** — Pearson r=0.006, p=0.21 for dust-emission correlation (§IV B): sample size N is not stated; reader cannot re-derive the p-value.

**P3-m16** — eROSITA cut: paper says "top-0.03%" but 298/930,203 = 0.0320%. Within rounding tolerance but the displayed threshold "S > 0.259 (top-0.03%)" actually corresponds to 0.032%.

**P3-m17** — §V quotes χ²_ν = 3.76 from χ² = 143,936 / 38,329; 143936/38329 = 3.756. Within rounding but quoted to one too few significant figures given the leading 3.

**P3-m18** — Two distinct uncertainty reports for γ_NANOGrav (±0.382 mean-shift vs +0.291/−0.287 quantile) are explained, but the +1.13σ and +4.61σ shift statistics both use ±0.382 without re-stating that choice; the abstract does the same. Already partly covered by P3-M14; the new specific issue is that the body never tells the reader **which** σ to use for the displayed +Nσ shifts.

**P3-m19** — Table V (p. 16) gives ACT DR6 training time 7.0 s and throughput 2,900 patches/s. With 20,000 ACT patches, inference takes ~6.9 s. The footnote ‡ in the table acknowledges the cross-transfer ACT checkpoint is "undertrained" — a 7-second training run on a 4,096-input autoencoder is below the threshold of any meaningful comparison and should not be reported as a row in the timing table.

**P3-m20** — "5,384 QSO-candidate sample" in §V appears with no construction recipe; the matched 26,920 randoms (= 5 × 5,384) are stated; the cross-reference to which anomalies form this sample (DESI? DESI+SDSS? gold+silver+bronze tiers?) is implicit and must be inferred from §VI D (j)'s "1,122-object Gold+Silver subset" being a sub-set. Already noted in P3-M2; the new sub-issue is that the four tiers (Gold, Silver, Bronze, and the 5,384 sample) are never numerically reconciled.

---

## ADDITIONAL NIT findings

**P3-n6** — Fig. 2 left-panel score axis labels three points (24.5, 24.6, 25.2) but only two are visually separated.

**P3-n7** — Numbers ESS≈5,500, τ≈58, walkers=32 are consistent (10,000/58 × 32 ≈ 5,517) but expressed as "(> 50τ per walker, convergence satisfied)"; the inequality is 10,000 > 50 × 58 = 2,900 (per-walker chain length), not "ESS > 50τ per walker." Slightly mislabeled criterion.

**P3-n8** — "σ_val is set such that the S > 5 catalog threshold corresponds to MSE≈0.143 on the rescaled scale" (p. 2): "rescaled scale" is undefined.

**P3-n9** — §III A "Spearman rank correlation between anomaly score and SNR is ρ = −0.03 (p = 0.12 on a stratified subsample of 2,670 spectra, log-uniform in SNR)". For ρ = −0.03 and N = 2,670, Z = −1.55 → p = 0.12 (two-tailed). Arithmetic OK; but for N=2,670 the rejection threshold for the null of ρ=0 at 5σ is |ρ| > 0.097, so |ρ|=0.03 is consistent with anything in [−0.067, +0.007] at 1σ — the null is not strongly demonstrated, only not excluded.

**P3-n10** — Fig. 1 caption gives the unique-object count parenthetically as "(319,443 detections shown; canonical Path-C unique count is 378,280…)". The figure title overlays "319,443 anomalies across 8 archives" — 8 archives includes ACT, contradicting §II D's quarantine of ACT.

---

## Summary of the second pass

The fresh-eyes audit found **one additional arithmetic contradiction at headline level** (σ=8.14 ↔ 7.9% improvement, P3-E16), **one stale Jaccard value in the conclusions** (P3-E17), **one table referring to non-existent footnotes** (P3-E18), **one mislabeled headline figure** (P3-M18 LAMOST count is cross-transfer, not native), and **two dangling cross-reference systems** (P3-M16 §VI D (v) does not exist; P3-M17 Roman ↔ alphabetic mismatch). The internal forecast machinery (P3-M19 stationary-point inconsistency; P3-M24 two incompatible Fisher matrices within Appendix C) further degrades the headline σ(f_NL) claim that was already flagged in the first pass.

Taken together with the first review, the manuscript carries:
- Two contradictory definitions of σ_val (E1) and two contradictory definitions of σ(f_NL)^std (M24, 8.98 vs 16.85).
- Three contradictory Jaccard reports (J=0.862 5-fold, J=0.732 prod-vs-control in §II B, J=0.874 in conclusions).
- Mixed Roman/alphabetic caveat labels with three dangling cross-references.
- One headline σ(f_NL) value (8.14) that does not match its own headline improvement (7.9%).

These are not interpretive disagreements; they are bookkeeping failures in a paper whose principal claim is a quantitative forecast. The PRD recommendation stands at **REJECT**, and the additional findings strengthen the case that a substantial rewrite (not just response-to-referee revisions) is required before resubmission.
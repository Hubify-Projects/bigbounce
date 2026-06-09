# P3 auto-2026-06-08_1737pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (15095 chars)
**Wall time**: 566.9s

---

# PRD Referee Report — Paper P3

**Title:** *Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies…*
**Submission:** Physical Review D
**Author:** single (Independent Researcher)
**Recommendation:** **REJECT**

This report does not soften findings. I will not enumerate strengths because the manuscript does not meet the threshold at which strengths become relevant.

---

## A. Scope / venue mismatch

**P3-E1 (ESSENTIAL) — PRD is not the appropriate venue.**
The paper is dominantly an astronomical anomaly catalog (Sections III, IV, Appendix D) with two thin, late-paper cosmology subsections (§V, §V A). The catalog content (UMAP/HDBSCAN families, SIMBAD/NED cross-matches, taxonomy galleries, photometric color excesses, BAL QSO discovery) belongs in ApJS / MNRAS. The two PRD-relevant pieces (αjk → σ(fNL); NANOGrav γ fit) are (i) consistent with null and (ii) already in the literature in stronger form. The body cannot be reorganized within PRD's scope without removing ~70% of its content.

**P3-E2 (ESSENTIAL) — abstract overclaim of cosmology content.**
Both PRD-relevant numbers in the abstract are explicitly null results in the body:
- αjk = 0.19 ± 0.65 — author admits "< 1σ from null" (p. 1, p. 11).
- σ(fNL) "7.9% improvement consistent with no improvement at < 1σ" (p. 1).
- γ = 2.567 ± 0.382 — matter-bounce γ = 3 is "+1.13σ marginally consistent" — not evidence for anything.

A PRD abstract cannot sell two null results as headline findings. Either prove something or remove from the abstract.

---

## B. Internal-bookkeeping / draft-process language in the body

**P3-E3 (ESSENTIAL) — pervasive internal audit language.**
The body is saturated with internal review/version tags. Selected examples (non-exhaustive):
- "Path-C rebuild protocol" / "Path-C native retrain" / "Path-C unique" — used in abstract, Table I, throughout. This is internal version naming, not a methodological label that means anything to an external reader.
- "Cross-transfer baseline preserved as the before/after diagnostic" (e.g. p. 3, p. 6 Table I notes ‡ and ∥, p. 8 Fig. 3 caption "the figure is preserved as a before/after diagnostic of the cross-transfer domain-shift").
- "FAIL-with-diagnostic" (p. 1, p. 13 Fig. 7) — invented jargon for "fails the test but we want to keep it."
- "Two-part gate" / "Step 1 / Step 5 of §II D" — workflow language.
- "Quarantined" (ACT DR6) — quarantine is an internal process state, not a publishable status.
- "Sensitivity-check artifact in the companion data repository," "before/after baseline," etc.
- "(§VI D caveat (j))," "(§VI D caveat (v))," "(§VI D caveat (i))" — these are referenced as if they were a checklist, not a discussion.
- Table IV header: "Path-C residual caveats. All ten items are closed (C = resolved in paper…)" — this is a punch-list from an internal review, not a journal table.

PRD does not publish internal QA logs. **Every such instance must be removed and the content rewritten in normal scientific prose, or excised.**

**P3-M1 (MAJOR) — undisclosed pre-publication identifiers.**
Phrasing such as "the LAMOST exploratory tier (∼113,000 objects retained as a methodological lesson…)" and the explicit "FAIL-with-diagnostic" decomposition in Fig. 7 indicate this manuscript is mid-iteration. The bookkeeping must not be visible in the published version.

---

## C. Arithmetic and internal consistency

**P3-E4 (ESSENTIAL) — "7.9% improvement" cannot be reproduced.**
Abstract and §V: σ(fNL) = 8.14, baseline 8.98 ⇒ (8.98 − 8.14)/8.98 = **9.35%**, not 7.9%. The "7.93%" figure appears in Appendix C in a *different* (5-tracer ideal-multi-vs-baseline-multi) configuration with σ values 11.71 and 12.72; the author appears to have copy-pasted that percentage onto the αjk = 0.19 forecast where it does not apply. Either the central value (8.14), the baseline (8.98), or the quoted percentage (7.9%) is wrong; the three are not mutually consistent.

**P3-E5 (ESSENTIAL) — abstract "~265,000 catalog-grade subset" does not match the body sums.**
DESI + SDSS + eROSITA + Gaia + NEOWISE native-retrained counts:
195,829 + 77,905 + 298 + 500 + 419 = **274,951**. After 2.63% global compression this is ≈ 267,000; even with a generous deduplication margin, the abstract's "∼265,000" is off and is not derived in the body.

**P3-E6 (ESSENTIAL) — aggregate SIMBAD-unmatched 58.8% cannot be reproduced.**
Using the body's per-survey rates and counts (DESI 99% × 195,829, or 99% × 10,000 top-cut as the body alternately uses; SDSS 90% × 77,905; LAMOST 50% × 44,075; eROSITA 68% × 298; NEOWISE 45% × 436; Gaia 27% × 500), neither weighting yields 58.8%:
- Full-catalog weighting → ≈ 89.8%
- Top-10K-weighting for DESI → ≈ 77%

Either the underlying per-survey fractions or the aggregate are inconsistent.

**P3-M2 (MAJOR) — "95.3× enrichment" is mislabeled.**
§VI D (f) and Table I footnote: 284 observed vs. 2.98 expected ⇒ 284/2.98 = 95.3 is an **observed-to-expected ratio**, which is the enrichment factor expressed as a multiplier of expectation. That is fine. But the phrase "95.3× enrichment over random-independence" appears twice on p. 7 and again on p. 14 alongside "95.3% overlap" — the visual collision (95.3% and 95.3×) is coincidental and confusing; clarify.

**P3-M3 (MAJOR) — DESI 73× / catalog 141× scale claims are not like-for-like.**
The comparator (Liang et al. 2023) ran on ~250 k spectra and reported 2,685 anomalies (1.07%). This paper ran on 22.5 M spectra and reports 195,829 (0.87%). The "73×" and "141×" multiplicative claims are **scale-of-input** comparisons dressed as **catalog-size advances**. The honest comparison is the anomaly rate, which is nearly identical (and the author actually says so on p. 13). Remove "73×" and "141×" from the abstract or qualify as input-volume ratios.

**P3-M4 (MAJOR) — per-survey thresholds preclude a meaningful "rate" comparison.**
Table I mixes (i) absolute S > 5.0 (DESI), (ii) 99th-percentile (SDSS, LAMOST), (iii) score-knee (eROSITA), (iv) fixed top-1% (Planck, Gaia, NEOWISE). The "anomaly rate" column is therefore not a measured quantity for surveys (iv); the author explicitly notes this but still tabulates "Rate (%)" alongside the others. The §II B claim that S is "per-survey z-scored" is also internally inconsistent with the body — if S were truly z-scored, S > 5 would not produce a 0.87% tail for DESI while producing 6 × 10⁻⁶ for SDSS native (12/1.93 M). Either S is not standardized, or the standardization is not what is claimed.

**P3-M5 (MAJOR) — abstract "3 PASS, 3 FAIL" injection-recovery is sold as a feature.**
Half the surveys fail the methodology's own pre-registered gate (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2% vs. ≥ 50% required at 5σ). Including the failing surveys in the headline 378,280 count, then defending them as "FAIL-with-diagnostic," is methodologically unacceptable. Headline numbers should be restricted to surveys that pass the gate.

---

## D. Statistical / forecasting issues

**P3-E7 (ESSENTIAL) — using a null measurement as a positive Fisher input is improper.**
αjk = 0.19 ± 0.65 has 1σ envelope crossing zero. The author then propagates the central value into 1/σ(fNL)² = F₀ + cα², gets σ(fNL) = 8.14, and labels this "central forecast." This is forecasting on noise. The defensible statement is σ(fNL) = 8.98⁺⁰·⁰⁰₋_₅.₀₆ (i.e., upper bound = baseline, lower bound from 1σ tail) — i.e., no improvement is established. The "1σ envelope [3.92, 8.98]" hides this asymmetry by reporting the upper as the baseline.

**P3-E8 (ESSENTIAL) — Savage-Dickey Bayes factor over-interpreted.**
§V A computes BMB/free = 3.23 and BSMBHB/free = 4.52 × 10⁻⁴ from γ-marginal posteriors and reports BMB/SMBHB = 7.14 × 10³ as "decisive on Jeffreys' scale." But this is a *parameter-shift* statement under a fixed amplitude prior; it is not a model comparison between bounce and SMBHB physics (which differ in amplitude prior, possibly in spectral shape away from a single-γ power law, in spatial correlations, etc.). NANOGrav's own analysis [28] reports B-factors that are far from "decisive" for any single new-physics model. The "decisive" framing is unsupported.

**P3-M6 (MAJOR) — γ posterior summary inconsistency.**
§V A: γ = 2.567 ± 0.382 (Gaussian mean ± std) and equivalently γ = 2.591⁺⁰·²⁹¹₋₀·₂₈₇. The author acknowledges the two widths differ because the posterior is non-Gaussian and "uses the appropriate width for each test." This is post-hoc selection of summary statistic — for the 1.13σ and 4.61σ shift tests, the appropriate uncertainty is the *one-sided distance* in the posterior, not either summary. Quote actual posterior tail probabilities (P(γ > 3), P(γ > 4.33)) instead.

**P3-M7 (MAJOR) — SPHEREx 3–5σ detection projection.**
§V states a "projected SPHEREx multi-tracer forecast yields 3–5σ detection significance for the matter-bounce fNL = −35/8 prediction." This number is not derived in this paper; it requires σ(fNL) ~ 1, but the paper's own central forecast is σ(fNL) = 8.14, an order of magnitude too large. The 3–5σ figure is inherited from Heinrich et al. and has nothing to do with the anomaly catalog. Remove or attribute clearly to the reference forecast and disconnect from this catalog's contribution.

**P3-M8 (MAJOR) — Planck CMB native CAE fails one gate criterion.**
§III F: val_loss = 0.4437 (criterion (a) ≤ 0.30 FAIL). It is admitted into the catalog via criterion (b). But the published 200 Planck patches then enter the headline 378,280 count. A model that fails the validation-loss criterion should not contribute to a unique-object headline; this is a category error and inflates the headline.

**P3-M9 (MAJOR) — 17.8% genuine novelty fraction is one point with no uncertainty.**
Author admits "single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested." Putting this fraction in the abstract as "the discovery-rate figure" while saying readers should ignore the 58.8% SIMBAD figure is contradictory. Either compute a real uncertainty (bootstrap) and stratum-vs-full extrapolation, or remove from the abstract.

---

## E. Figure / table issues

**P3-M10 (MAJOR) — Fig. 1 caption refers to a non-headline number.**
"Mollweide projection of the initial cross-transfer anomaly baseline (319,443 detections shown; canonical Path-C unique count is 378,280…)." The figure shows the wrong number for the headline catalog. The reader cannot recover the 378,280 quantity from any figure in the paper.

**P3-M11 (MAJOR) — Fig. 9 / Appendix B "AE" panel labels.**
"Panel labels report the per-arm Z-arm sub-score rZ (printed as 'AE' for legacy compatibility)." This is the author telling the reader the figure is mislabeled and to mentally substitute. Re-render the figure with correct labels.

**P3-M12 (MAJOR) — Table I "Rate (%)" column is meaningless across rows.**
Mixed thresholds (absolute S, percentile, top-N) produce values that are not directly comparable; the column gives the false impression of measured anomaly rates. Either split into separate tables per threshold family or eliminate the column.

**P3-N1 (NIT) — Table I footnotes use ♡, ♠, ‡, §, ¶, †, ∥, ⋆ in dense combination. Several are visually hard to distinguish on rendered output (♡ on SDSS row, ♠ on LAMOST). Use plain Latin-letter footnote markers.**

**P3-N2 (NIT) — Figure 2 right panel: x-axis "Anomaly score S" spans 10⁻² to 10¹⁰; caption says this is a cross-transfer artifact and the same objects re-score to S < 14 natively. Why is the figure retained?**

**P3-N3 (NIT) — Figure 6 panel (d) caption: SDSS reconstruction (red dashed) is essentially flat against a ~3× elevated black continuum. The "anomaly score 49.5" panel does not show what the caption claims (the reconstruction does not track the spectrum because the model has no continuum support there); the figure would benefit from per-band residuals.**

---

## F. Novelty / literature framing

**P3-M13 (MAJOR) — "Largest-scale application" claim.**
Largest by *input volume*, yes. But (i) the cross-transfer scan that produced the original 319,443 number is admitted to be a methodological artifact, and (ii) the surviving native-retrained per-survey counts include three failing-injection-recovery surveys (LAMOST 113,342, Gaia 500, eROSITA 298). The author cannot simultaneously claim "largest catalog" and disavow ~30% of it as exploratory/training-bias artifact. Either prune the catalog or downgrade the claim.

**P3-M14 (MAJOR) — Author affiliation / data access.**
Single-author independent researcher producing a 22.5 M-spectrum DESI DR1 anomaly catalog plus eROSITA, Gaia, NEOWISE, Planck, SDSS, LAMOST analyses, plus a NANOGrav MCMC. The paper does not document data-access agreements (DESI DR1 was public at submission), survey collaboration courtesy reviews, or independent code review. PRD policy requires data sources be clearly traceable; the "HuggingFace dataset (private pending arXiv acceptance)" structure is not adequate.

**P3-M15 (MAJOR) — fNL = −35/8 framing.**
Planck 2018 already constrains fNL = −0.9 ± 5.1 (local), which is consistent with −4.375 at < 1σ but also consistent with zero. The paper's own forecast σ(fNL) = 8.14 is worse than Planck. Framing the matter-bounce prediction as a near-future SPHEREx target is fine but should not appear in the abstract of *this* paper, since this paper contributes nothing to that constraint at the claimed precision.

---

## G. Other issues

**P3-M16 (MAJOR) — definition of "anomaly" is survey-dependent.**
The deduplication unifies "anomaly" objects across surveys that used different scoring functions (BigAE, IsolationForest, score-knee, top-1%) and different definitions of the input (point sources for six surveys, sky-region patches for Planck). The footnote in Table I admits this and creates a 378,080-point-source + 200-patch stratification. The headline 378,280 mixes these and should not. Use 378,080 as the headline and discuss the 200 separately, since the author themselves recommends this on p. 1 ("Downstream object-level analyses … should use the 378,080 point-source tier").

**P3-M17 (MAJOR) — duplicate / redundant material.**
The "BAL QSO at z ≈ 0.86" feature is repeated nearly verbatim at least three times (abstract, §IV C, §VII). The "98% LAMOST blue-excess training-bias artifact" is stated five+ times. The "Path-C rebuild" methodology is described in §II D, then re-summarized in §III, §VI A, §VI D, and §VII. Compress to a single description.

**P3-M18 (MAJOR) — single-architecture limitation.**
§VI C admits no ensemble; IsolationForest is run only on two photometric surveys for "cross-validation," but obtains Jaccard 41% on Gaia, which the paper itself reads as a stability failure. The catalog rests on a single deterministic AE with no architecture-independence test for the dominant surveys (DESI, SDSS, LAMOST). PRD-acceptable methodology would require a second independent detector on each headline survey.

**P3-N4 (NIT) — "z-scored" vs "redshift z" disambiguation paragraph (p. 2) is unnecessary if the score is consistently called S. Remove.**

**P3-N5 (NIT) — Several long inline parentheticals (p. 3, p. 6) make the prose unreadable. PRD style favors concise sentences.**

**P3-N6 (NIT) — Equation (E1) numbering: the 1/2 prefactor multiplies the full bracket; verify this matches the standard ρ_i = A² /(12π² Tobs) (f_yr/f_i)^γ f_yr⁻³ definition used by NANOGrav. The factor structure is unusual.**

**P3-N7 (NIT) — Page count.** 20 pages for content that, after removing the catalog (→ ApJS), the failed-injection surveys, and the duplicate Path-C summaries, would compress to ≈ 6 PRD pages on the αjk and NANOGrav pieces. Recommended max for a focused PRD version: **8 pages**.

---

## Summary recommendation

**REJECT**

The manuscript is a multi-survey anomaly catalog with two thin cosmology appendages, both of which are admitted in-text to be null at < 1σ; it fails PRD's scope by being predominantly observational catalog work; it contains pervasive internal QA / draft language ("Path-C," "gate FAIL-with-diagnostic," "before/after diagnostic," "quarantined," "caveat (i)…(j)") that does not belong in a published paper; it has at least three independent arithmetic inconsistencies in headline numbers (7.9% improvement, ~265,000 subset, 58.8% SIMBAD-unmatched); it includes in its headline catalog three surveys that fail its own pre-registered injection-recovery gate and one CMB model that fails one of its two-part gate criteria; it sells null statistical results (αjk consistent with 0; γ matter-bounce at +1.13σ) as forecast/discovery achievements; and it claims "largest" and "73×/141×" advances that are input-volume ratios rather than methodological progress over Liang et al. The appropriate path is resubmission of the catalog to ApJS/MNRAS after substantial cleanup, and a *separate*, focused, ≤ 8-page PRD paper if and only if the αjk or γ analysis can be brought to a defensible non-null result on independent data.

---

## PASS 2 — self-critique findings (what initial review missed)

# PRD Referee Report — Paper P3 (Second Pass, Fresh-Eyes Findings)

I re-examined the paper systematically against the ten classes of issue. The first review caught the high-level architectural problems; this pass surfaces additional arithmetic, equation, figure–body, and cross-reference failures that strengthen the rejection.

---

## A. Arithmetic — newly recomputed values

**P3-E9 (ESSENTIAL) — The "7.9% improvement" is provably copied from a different Fisher configuration.**
I now have the exact source of the inconsistency I flagged in P3-E4. From the Appendix C Fig. 8 caption: σ(fNL)_ideal-multi = 11.71, σ(fNL)_baseline-multi = 12.72. Compute (12.72 − 11.71)/12.72 = **7.94% ≈ 7.9%**. This is the "ideal-multi vs baseline-multi" improvement in a *canonical 5-tracer Heinrich-style configuration*. The headline σ(fNL) = 8.14 vs. baseline 8.98 gives (8.98 − 8.14)/8.98 = **9.35%**. The 7.9% in the abstract, §V, and §VII (conclusions bullet 5) has been transplanted from the wrong calculation; the empirical-α result it is attached to has a different baseline (8.98), a different functional form (Fisher-positivity quadratic, not linear), and gives a different number (9.35%, not 7.9%).

**P3-E10 (ESSENTIAL) — Two mutually inconsistent "single-tracer baselines."**
§V: "the single-tracer DESI QSO baseline is σ(fNL)^std = 8.98."
Fig. 8 and its caption (Appendix C): "Ideal (dense limit) σ = 11.71. Baseline multi-tracer σ = 12.72. Single-tracer baseline σ = 16.85."

The paper has *two* different single-tracer baselines (8.98 in §V; 16.85 in Appendix C) used in adjacent calculations. Neither is derived in the body; no reconciliation appears. The reader cannot determine which is correct or which the SPHEREx 3–5σ forecast (§V) is anchored to.

**P3-M19 (MAJOR) — Appendix C uses linear scaling; §V uses Fisher-positivity quadratic; the two diverge except at α = 0.15.**
Table VII derives σ(fNL) by *linear scaling* of the fiducial result anchored at α = 0.15 (σ = 8.43). §V uses 1/σ² = F₀ + cα² with c = 0.0747 (Fisher-positivity quadratic). Both reproduce σ = 8.43 at α = 0.15 *by construction* (c is fit to that anchor), but they disagree everywhere else.

For example, at α = 0.05:
- Table VII (linear scaling): σ = 8.80 ("2.0% improvement").
- §V Fisher-positivity: 1/σ² = 0.01240 + 0.0747(0.0025) = 0.01259 → σ = 8.91 (**0.78%** improvement).

For the headline α_jk = 0.19, Table VII would give σ ≈ 8.29 (~7.7%); §V gives σ = 8.14 (9.35%). The two appendices are using *different functional forms* of the same forecast. Pick one and apply it consistently.

**P3-M27 (MAJOR) — "Consistent with the 1.07% rate reported by Liang et al." is statistically false.**
§VI E claims the DESI anomaly rate of 0.87% is "consistent with the 1.07% rate reported by Liang et al." Poisson uncertainty on 195,829/22,504,897 = 0.87% is √195,829/22,504,897 = 0.002%. The difference 1.07% − 0.87% = 0.20% absolute is ≳100σ in Poisson terms. The author hand-waves a statistically incompatible rate as "consistent." If a systematic-uncertainty floor is invoked, it must be quoted.

**P3-N10 (NIT) — eROSITA "9,303-object" reference set.**
Footnote §: "top-1% IF cross-validation pool" of 930,203 → 9,302.03, rounded should be 9,302, not 9,303. Off by 1.

**P3-N11 (NIT) — Pearson r = 0.006, p = 0.21 (§IV B).**
For r = 0.006 at N = 38,330, t = r√(N−2)/√(1−r²) ≈ 1.176, giving two-sided p ≈ 0.24, not 0.21. Minor but the recomputed value does not match.

---

## B. Figure–caption vs. body-claim

**P3-E12 (ESSENTIAL) — Fig. 7 contradicts its own caption.**
Caption: "Three surveys PASS the gate at 5σ: SDSS DR18 continuum-dip, Planck CMB native (500/500 = 100% at 5σ), and NEOWISE ecliptic-pole mask (1000/1000 = 100%)." Solid curves shown on the figure: six lines, labelled SDSS DR18 (continuum-dip), SDSS DR18 (emission-line), LAMOST DR10 (continuum-dip), LAMOST DR10 (emission-line), eROSITA DR1 (latent IF), Gaia DR3 (variab. IF). **Neither Planck nor NEOWISE curves appear on the plot.** Two of the three claimed PASSes are not on the figure that allegedly demonstrates them.

**P3-M25 (MAJOR) — Fig. 9 panel labels are inconsistent with the score system defined in §III A.**
Appendix D Fig. 9 panel labels include "AE=83518" (multi-band representative) and "AE=17663" (BAL QSO). §III A defines canonical S with maximum 25.2 across the entire 22.5M DESI scan. There is no score axis in the paper that produces values of order 10⁴–10⁵ for DESI native anomalies. Either the figure was generated from a previous (cross-transfer) checkpoint that the rest of the paper supersedes, or "AE" denotes raw MSE (in which case it should be labeled MSE and the scale explained). Currently the figure cannot be interpreted.

**P3-M22 (MAJOR) — Total S vs per-arm rB, rR, rZ relationship is never defined.**
§III A introduces per-band sub-scores rB, rR, rZ "computed over the blue/red/NIR subsets." §III B states 12 high-z QSO candidates have "mean Z-arm sub-score ⟨rZ⟩ = 3.9" but "all objects have total score S > 5 by construction." The reader cannot reproduce or check this without knowing whether S is the sum, mean, max, or L2 norm of the per-band scores. Fig. 9 panels label objects with single-number "AE" values whose meaning depends on this undefined combination rule.

---

## C. Equation dimensional / functional consistency

**P3-E11 (ESSENTIAL) — Equation (E1) has a spurious 1/2 prefactor.**
The standard NANOGrav free-spectrum power-law template is
ρ_i = (A²/12π²) (f_i/f_yr)^{−γ} f_yr^{−3} / T_obs,
i.e. log₁₀ ρ_i = 2 log₁₀ A − log₁₀(12π²) + (γ−3) log₁₀ f_yr − γ log₁₀ f_i − log₁₀ T_obs **without** a 1/2 prefactor. Equation (E1) writes:

log₁₀ ρ_i = **(1/2)** [2 log₁₀ A − log₁₀(12π²) + (γ−3) log₁₀ f_yr − γ log₁₀ f_i − log₁₀ T_obs]

If ρ is power, the 1/2 is wrong. If ρ is amplitude (= √power), the convention should be stated and the units of A correspondingly halved in dimension. Neither is done. This is the single equation in the paper that delivers the headline NANOGrav γ posterior; it cannot be left ambiguous. P3-N6 in my initial review flagged this as a check; the recomputation now confirms an error.

---

## D. Internal cross-references and consistency

**P3-M24 (MAJOR) — Table I footnote ¶ is factually wrong.**
Footnote ¶: "Per-survey N_anom values shown in this column are the initial cross-transfer scan counts. The Path-C native-retrained counts, which supersede these values, are reported in §II D and summarized in the 'Path-C unique (primary)' row below."

But the values 298 (eROSITA), 200 (Planck), 500 (Gaia), 419 / 436 (NEOWISE), and arguably 195,829 (DESI) are **not** cross-transfer counts. eROSITA, Gaia, and NEOWISE were never cross-transferred from DESI — they were trained natively from the start. Planck was native-retrained and 200 is the post-retrain headline. DESI is the native model itself. The footnote treats all entries as if they were superseded by a later Path-C value, but for five of seven rows the entries *are* the Path-C value. The "cross-transfer" framing of the column is incorrect for most of it.

**P3-N8 (NIT) — Appendix archival cross-match catalog count.**
§IV A says "DESI DR1 top-1,000 anomalies … against **20 curated all-sky catalogs** via CDS X-Match (Gaia DR3, SDSS DR12/DR16, DESI Legacy Imaging DR9, DES DR2, Pan-STARRS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, USNO-B, UCAC5, APASS)." I count **18** catalogs in the parenthetical (counting SDSS DR12 and DR16 separately). Either the number is wrong or two catalogs are missing from the list. The 82.2% archival-ID rate quoted depends on this list.

---

## E. Null-procedure non-comparability

**P3-M20 (MAJOR) — Paper's NANOGrav γ disagrees with NANOGrav's own published constraint on the same dataset.**
The NANOGrav 15-yr official analysis [18] reports HD-correlated γ ≈ 3.2 ± 0.6. This paper, using the *same Zenodo KDE product*, fits γ = 2.567 ± 0.382. The two are ~1σ apart (mean offset 0.63 vs joint σ ≈ 0.71). For γ values to differ between (a) the official NANOGrav posterior on full timing residuals and (b) the present paper's posterior on the released KDE free-spectrum product is not automatically inconsistent — they are different likelihoods — but the offset is large, in the direction that *helps* the matter-bounce claim (γ = 3 is much closer to 2.57 than to 3.2), and the paper makes no comparison. A reader cannot tell whether the 1.13σ "marginal consistency" of matter-bounce in this paper would survive against the NANOGrav-internal γ posterior (which gives γ = 3 at ~0.3σ vs. ~1.4σ depending on which posterior).

**P3-M21 (MAJOR) — Score–SNR correlation test is biased by stratification.**
§III A: "Spearman rank correlation between anomaly score and SNR is ρ = −0.03 (p = 0.12 on a stratified subsample of 2,670 spectra, log-uniform in SNR)." Stratifying log-uniformly in SNR *deliberately removes* the natural SNR distribution, which is precisely the distribution along which any score-vs-SNR systematic would manifest. The proper test is on the full sample with its natural SNR distribution. The stratification-uniform construction artificially deflates the correlation by removing the high-leverage endpoints. The claim of "no practically significant SNR dependence" is not supported.

---

## F. Abstract faithfulness

**P3-M23 (MAJOR) — "Galaxies flagged at ~20× the QSO rate" has no statistical test.**
§III A: "Galaxies are flagged at ∼20× the QSO rate (0.75% vs. 0.037%); anomalies peak at z ∼ 0.75 vs. z ∼ 0.93 for normal spectra." A 20× class-dependent rate ratio in an "anomaly detector" is a textbook signature of class-conditional calibration bias (the model reconstructs QSOs better than galaxies → galaxies look anomalous). No KS test on the z distributions, no examination of whether galaxy-vs-QSO calibration bias drives the catalog. This finding, if true, undermines the cross-class interpretability of S, but the body presents it as routine.

---

## G. Unsupported novelty claims

**P3-E13 (ESSENTIAL) — UMAP trustworthiness "0.9797 ± 5×10⁻⁵" is implausibly precise.**
Appendix D: "UMAP stability: trustworthiness 0.9797 ± 5×10⁻⁵ ... across 20 independent seeds." A standard deviation of 5×10⁻⁵ for a trustworthiness score across 20 different random seeds of UMAP (a stochastic algorithm with k-NN sampling) is *six orders of magnitude tighter* than typical UMAP-seed variability on a 195,829-point dataset (~10⁻³–10⁻² is normal). Either the number is wrong or the "20 seeds" are not actually independent (e.g. same seed reused, or random_state set deterministically). This deserves an explanation; as stated it is not credible.

---

## H. Unquantified hedges

**P3-M28 (MAJOR) — "No correlation with Planck dust intensity" understates a near-significant trend.**
§IV B: Pearson r = 0.006 at N = 38,330 gives t ≈ 1.18, p ≈ 0.24. The paper reports p = 0.21 (small discrepancy, P3-N11) but frames this as "no correlation with Planck dust intensity, establishing that the anomaly signal is not driven by Galactic foreground contamination." For a dust-foreground systematic on this size of sample, the relevant null-hypothesis cost is much smaller than α = 0.05; p ≈ 0.21–0.24 is **not** strong evidence against foreground contamination, particularly given that the survey selection functions preferentially avoid the Galactic plane (which the author themselves acknowledges suppresses any latitude-dependent signal). The "establishing" verb is unwarranted.

---

## I. Appendix vs main-text mismatch

**P3-M29 (MAJOR) — Appendix C / §V forecasts use different functional forms (already covered in P3-M19 above); §V cosmological "δb is broken by multi-tracer" is hand-waved.**
§V: "δs (magnification bias) as the dominant systematic axis; δb is broken by the multi-tracer technique." Seljak's multi-tracer technique cancels cosmic variance on the bias *ratio* if the ratio is known; it does not "break" individual bias uncertainties unless the second tracer's bias is known *a priori*. The α-measurement of §V is precisely a measurement of the bias ratio, with σ = 0.65 (P3-E7 in initial review). The "broken by multi-tracer" wording is not supported by the empirical α-precision.

---

## J. Stale numbers

**No additional stale numbers detected** beyond those in the initial review (the "265,000," "58.8%," "7.9%" trio in P3-E4/E5/E6). The "PEP-Liang rate consistency" issue (P3-M27) is structurally similar to a stale-number issue: a phrase that may have been written when the rates were less precise and never updated.

---

## Summary of new findings

Twelve new substantive items (4 ESSENTIAL, 8 MAJOR, 3 NITS), all consistent with the recommendation to **REJECT**:

- **P3-E9 / E10** trace the abstract's "7.9% improvement" to a copy-paste from a different Fisher configuration (Fig. 8 5-tracer ideal-vs-baseline-multi) and expose two unreconciled "single-tracer baselines" (8.98 in §V; 16.85 in Appendix C).
- **P3-E11** identifies a likely algebraic error in equation (E1), the only equation that defines the NANOGrav fit.
- **P3-E12** documents that the figure (Fig. 7) supporting the "3 PASS, 3 FAIL" headline does not include two of the three claimed PASS curves.
- **P3-E13** flags an implausibly precise UMAP trustworthiness uncertainty.
- **P3-M19** shows two appendices use inconsistent forecasting functional forms (linear vs. Fisher-positivity quadratic) that agree only at the anchor α = 0.15.
- **P3-M20** identifies an undisclosed disagreement with NANOGrav's own published γ posterior on the same dataset.
- **P3-M21** shows the score–SNR null test is constructed in a way that suppresses the signal it claims to bound.
- **P3-M22 / M25** show that the per-arm score system underlying the high-z QSO selection and the Appendix D taxonomy figure is never algebraically defined, and that the figure labels use a numerical scale (AE = 10⁴–10⁵) inconsistent with the body's score axis.
- **P3-M24** establishes that Table I footnote ¶ is factually wrong about which entries are cross-transfer counts.
- **P3-M27** identifies that the "consistent with Liang et al." claim is statistically incompatible at very high σ given the sample sizes involved.
- **P3-M28** shows the foreground-null claim rests on p ≈ 0.21–0.24, which is not strong evidence.
- **P3-N8 / N10 / N11** are arithmetic/counting discrepancies (catalog enumeration, top-1% rounding, p-value recomputation).

The initial review was correct in its overall judgment but underestimated the depth of internal arithmetic and figure-vs-body inconsistency. The new findings strengthen, rather than modify, the **REJECT** recommendation: the manuscript's two PRD-relevant numerical results (σ(fNL) forecast, NANOGrav γ) rest on a computation whose percentage-improvement headline cannot be reproduced from its own inputs, whose single-tracer baseline appears at two different values in different sections, whose forecasting function differs between appendices, whose NANOGrav fit equation contains a likely error, and whose NANOGrav posterior disagrees with the published collaboration result on the same data without comment.
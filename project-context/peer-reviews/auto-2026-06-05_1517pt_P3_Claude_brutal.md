# P3 auto-2026-06-05_1517pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (10279 chars)
**Wall time**: 492.8s

---

# Referee Report — Paper P3
## "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies..."

I have read the paper in full, audited the figures, tables, equations, arithmetic, and the abstract→body→figure consistency chain. This is fundamentally a **catalog/methods paper with weak, null-result cosmological add-ons**, submitted to a journal (PRD) whose acceptance bar requires a clear, well-supported physics result. Most of the headline numbers are either inflated by definitional sleight-of-hand or qualified into meaninglessness in the body. I recommend **REJECT** for PRD; the catalog work would be more appropriate at MNRAS or ApJS, and the cosmology pieces (Sec. V) are too weak to anchor a PRD submission.

---

## ESSENTIAL findings (paper cannot be accepted without these)

### P3-E1 — Broken cross-references in body (Fig. ??)
**Sections II A and II B, page 2; page 5.** The body contains live LaTeX cross-reference failures: "*architecture shown schematically in Fig. ??*" (Sec. II A), "*per-band contributions rB, rR, rZ … (Fig. ??)*" (Sec. II B), and "*Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts*" (Sec. III B). These are unrendered references in a manuscript being formally submitted. **Fix:** repair all `\ref{}` calls; if the referenced figure does not exist, either add it or remove the in-text claim.

### P3-E2 — Abstract headline "378,280 unique anomalies" is incoherent across survey definitions
**Abstract; Table I, page 7.** The 378,280 total mixes three fundamentally different selection rules: (a) absolute reconstruction-MSE thresholds (DESI S>5), (b) per-survey top-1% slices that are *by construction* a fixed-count selection (Planck, Gaia, NEOWISE), and (c) "top-77,905" / "top-113,342" *native* re-slices for SDSS and LAMOST that retain the *cross-transfer count* even though the native-retrain gate produces dramatically smaller catalogs (12 SDSS sources at S>5; 2,054 LAMOST sources at S>5 — disclosed in the footnotes). The headline therefore is not a count of detections above a common physical threshold — it is a sum of fixed-count quotas designed to preserve the cross-transfer-era headline. **Fix:** Either (a) report a single headline at a common per-survey definition (e.g. each survey's native gate threshold), in which case the catalog is *vastly* smaller (≲ 200k, much of it Path-C-failing), or (b) replace the headline with two separate numbers and stop calling the total "anomalies."

### P3-E3 — Three of six injection-recovery gates FAIL, including the LAMOST tier that contributes ~30% of the catalog
**Sec. II D, III D, III E, Fig. 7.** LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2% recovery at 5σ — all far below the 50% gate. The paper labels these "FAIL-with-diagnostic" and *still includes them in the headline catalog*. The 113,342 LAMOST objects are explicitly retained "as an exploratory tier" with FAIL gate status and 98% blue-excess training-bias artifact. This is not consistent with PRD-grade catalog construction. **Fix:** Headline must report the catalog excluding all FAIL-gate surveys — the abstract acknowledges this only obliquely ("recommended catalog-grade subset is ∼265,000"). The actual lead number should be 265k, not 378k.

### P3-E4 — Cosmological "result" in Sec. V is a null, presented as a positive forecast
**Abstract; Sec. V.** αjk = 0.19 ± 0.65 is *consistent with zero at 0.29σ*. The "central forecast σ(fNL) = 8.14 (7.9% improvement)" is meaningless given the 1σ envelope [3.92, 8.98] that *includes the no-improvement baseline*. The paper itself admits this is "consistent with no improvement at <1σ" and "not a positive multi-tracer detection claim." For PRD, a null forecast wrapped in a "central value" framing is not a physics contribution. **Fix:** Either drop the fNL section entirely, or report it honestly as a null with no headline σ improvement.

### P3-E5 — NANOGrav "result" is also a null dressed as discriminating evidence
**Abstract; Sec. V A.** γ = 2.567 ± 0.382. Matter-bounce γ = 3.0 is at +1.13σ; SMBHB γ = 4.33 is at +4.61σ. The Savage–Dickey Bayes factor BMB/SMBHB = 7.1×10³ is real *given the model space considered*, but the paper explicitly states "Neither constitutes a detection." The matter-bounce prediction is also >1σ from the posterior mean — the data do not prefer it, they merely disfavor SMBHB more strongly. Presenting this in the abstract as the second pillar of a PRD paper is misleading. **Fix:** Either (a) demote to a brief consistency check or (b) anchor the paper on a real result (none in current draft).

### P3-E6 — Figure 9 score values are inconsistent with the body's canonical S definition
**Appendix D, Fig. 9, page 17.** The image gallery labels read "AE=9240", "AE=17663", "AE=83518", "AE=4058", etc., while the body claims S ∈ [5.0, 25.2] for DESI DR1 (Sec. III A). A score of 83,518 in a panel labeled as a representative DESI anomaly is incompatible with the stated DESI score range. This is either (a) a different score axis used in the figure without disclosure or (b) a remnant of pre-Path-C cross-transfer scoring that should have been removed. **Fix:** Reconcile axis or remove figure. As-shown, the figure contradicts the canonical-S definition that Sec. II B insists on.

### P3-E7 — Use of "Path-C" throughout body as internal version label
**Title, abstract, Sec. II D, throughout.** "Path-C" appears 30+ times in the body and even in the **title**. This is internal project-bookkeeping language (the [REVIEWER METADATA] confirms "v3.1.75" naming). A published PRD title cannot read "Catalog of 378,280 Path-C Unique Anomalies" — Path-C is meaningless to any external reader and is plainly an internal revision tag. **Fix:** Strip all "Path-C" labels from title, abstract, and section headings; describe the methodology by name (e.g., "native-retrain protocol").

### P3-E8 — Bibliography contains internal bookkeeping
**Reference [33].** Reads literally: *"[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]"* — this is an editorial note left inside the published bibliography. **Fix:** Remove.

### P3-E9 — Table I row-sum and Path-C reconciliation hidden by overloaded footnotes
**Table I, page 7.** The table's `N_anom` column shows cross-transfer counts (77,905 SDSS, 44,075 LAMOST) but the Path-C unique-total row uses *different* native-retrain counts (77,905 SDSS, 113,342 LAMOST). Recomputing the input sum: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493, minus 10,213 dedup = 378,280 ✓. But the SDSS native count happens to equal the cross-transfer count (77,905) — i.e., the "top-77,905 native slice" is a back-fitted quota chosen to match the cross-transfer headline rather than a principled threshold. **Fix:** Either use a defined threshold (gate value, e.g. 12 SDSS objects at S>5) or disclose openly in the table cell that the native count is back-matched to the cross-transfer quota.

### P3-E10 — Scope mismatch with PRD
The paper is 20 pages dominated by catalog construction, SIMBAD cross-matching, image galleries, and survey processing tables. The Sec. V cosmology contains zero detections, two nulls, and a Fisher forecast that does not improve over the baseline at >1σ. This is a methods/catalog paper for MNRAS or ApJS, not a Physical Review D physics result. **Recommended max length if reframed:** 8 pages plus an appendix. As-submitted: too long for the contribution.

---

## MAJOR findings

### P3-M1 — "Largest" / "141×" comparison is unfair
**Abstract.** The 141× figure compares the *total* 378,080 multi-survey catalog (with 3 fixed-quota top-1% selections) to the Liang+2023 *single-survey* count above a different threshold on different data (EDR vs DR1). The like-for-like 73× DESI-only comparison is more honest but still inflated by threshold differences and the ~90× input sample-size increase. Replace "141×" with "DESI DR1 scaled relative to Liang+2023 EDR by N_input × N_anomaly = …" or drop the multiplier framing.

### P3-M2 — B-dominant contamination 22.7% not closed
**Sec. III A; Sec. VI C.** ~44,000 DESI B-dominant anomalies are "flagged as calibration-suspect" with confirmation "needed." This is 22.7% of the headline DESI catalog. A PRD-grade catalog cannot ship with a quarter of the entries in unresolved calibration-suspect status.

### P3-M3 — Single-architecture admission and lack of independent cross-validation on spectroscopic surveys
**Sec. VI C, (1).** Authors admit no IsolationForest / VAE cross-check was applied to DESI, SDSS, or LAMOST. Given the LAMOST training-bias artifact (Sec. III D, §VI A) was only detected by a *secondary* cross-transfer comparison, the lack of an independent detector on the main DESI catalog is a critical methodological gap.

### P3-M4 — Spatial χ² result is meaningless by author's own admission
**Sec. IV B, page 10.** χ²_ν = 3.76 is "dominated by the inhomogeneous footprints," so the test is uninformative. Why is it reported as a numerical result?

### P3-M5 — NEOWISE/Gaia/Planck rates of "1.00%" are by construction
**Table I.** Footnote acknowledges that for three surveys the "anomaly rate" is the top-1% quota, not an intrinsic frequency. These should not appear in a "rate" column at all — they are quotas, and presenting them as 1.00% measurements is misleading. Replace cells with "(top-1% quota)" or remove the rate column.

### P3-M6 — Genuine novelty fraction 17.8% is one number from one stratum
**Sec. IV A.** The flagship novelty headline (17.8%) is a *single-sample point estimate at the top-1,000 DESI score stratum*, with the full-catalog rate "empirically untested." This is too thin to be the abstract's discovery-rate figure. Either bootstrap a confidence interval or downgrade the claim in the abstract.

### P3-M7 — Fisher forecast 1σ envelope [3.92, 8.98] is a forced-positivity artifact
**Sec. V, §VI D (i).** Because α=0 is a stationary point of 1/σ² = F₀ + cα², the envelope is asymmetric and *constructed* to include the baseline. Quoting σ(fNL)=8.14 "central" with this envelope is forecast-statistics theater. PRD would not accept this packaging.

### P3-M8 — Reference 12 cited as "in press"; reference 1 is "DESI DR1 documentation"
**Bibliography.** Citing software documentation as a primary DESI DR1 reference and an "in press" Nicolaou et al. without arXiv number is below PRD's referencing standard.

### P3-M9 — Heinrich et al. forecast σ(fNL) ≈ 0.7 quoted in abstract is bispectrum-only and not what the paper improves
**Introduction.** The abstract invokes Heinrich+2023 σ(fNL)≈0.7 as the target sensitivity, but the paper's own forecast operates at the σ(fNL) ~ 8–13 single-tracer scale and shows <1σ improvement. The juxtaposition implies a connection that does not exist. Clarify or remove.

### P3-M10 — Figure 1 caption / title inconsistency
**Fig. 1, page 4.** Figure title says "Spatial distribution of all 319,443 anomalies across **8** archives" but caption says "319,443 detections shown … **ACT DR6 is quarantined and excluded**." Title and caption disagree on whether ACT is in the plot. Fix the figure or the caption.

### P3-M11 — Table I footnote symbols (♡, ♠, etc.) appear unattached
**Table I, page 7.** The header lists "SDSS DR18♡" and "LAMOST DR10♠" with the footnote keys disclosed in the caption text, but they are mixed with ¶, †, ‡, §, ∥, ⋆ in a confusing soup. Standardize.

### P3-M12 — "TIC 374313355" framed as "time-variable" with no time-domain analysis
**Sec. IV C, Fig. 6.** The DESI and SDSS spectra differ in continuum level, but no light curve, epoch comparison, or significance test is presented. Calling it a "time-variable source" in the abstract is overreach.

### P3-M13 — eROSITA Table III IF raw scores 8,234 / 16,270 / 34,182 alongside S_BigAE < 1.1 are confusing
**Table III, page 8.** Two score axes shown side-by-side without normalization. Caption admits IF raw is "not a parallel catalog axis." Why include it then? Remove or normalize.

### P3-M14 — Figure 7 plots LAMOST cont./em. emission-line variants but the discussion conflates morphologies
**Fig. 7, Sec. VI D (ii).** The "3-PASS / 3-FAIL" headline is per *survey* but the curves are per *injection morphology*; SDSS continuum-dip PASS is paired with SDSS emission-line at 7.2% (would FAIL). Disclose that the gate decision is morphology-dependent.

### P3-M15 — NANOGrav fit uses published KDE product, not raw timing residuals
**Sec. V A; §VI C (5).** Acknowledged limitation, but the headline Bayes factor 7.14×10³ is reported as if it were a primary analysis. The KDE pipeline incurs information-loss approximations not propagated into the BF.

### P3-M16 — "Quasi-matter bounce model predicts fNL = −35/8 = −4.375"
**Introduction.** The cited value is from Cai+2009; the cosmological literature for matter-bounce non-Gaussianity has been refined since, with model-dependent prefactors. The single-value framing of a 15-year-old prediction as testable to 3–5σ requires more careful citation and discussion of model dependence.

---

## MINOR findings

### P3-Mi1 — Spearman ρ = −0.03 p = 0.12 on "stratified subsample of 2,670 spectra"
**Sec. III A.** Cannot compute p-value from rank correlation without df disclosure and tail orientation; on 2,670 points |ρ|=0.03 gives p ~ 0.12 only under specific assumptions; show formula or test.

### P3-Mi2 — Equation (E1) factor-of-12π² placement
**Appendix E.** Standard pulsar timing power-law convention should be displayed with explicit units of ρ. Confirm units (s²) and the Tobs prefactor convention; some readers will read this differently.

### P3-Mi3 — UMAP trustworthiness 0.9797 ± 5×10⁻⁵ over 20 seeds
**Appendix D.** Standard error this tight (5×10⁻⁵) on a 0.98 statistic over only 20 seeds requires CI methodology disclosure.

### P3-Mi4 — Abstract reads "Native-Trained Novelty Fractions" but the novelty figure is a single 17.8% point estimate
Section title is plural; reality is singular.

### P3-Mi5 — Page 6, Fig. 3 caption uses cross-transfer baseline that the body declares "before/after diagnostic, not a science result"
Why is a figure devoted to a non-science-result diagnostic occupying half a page? Move to appendix.

### P3-Mi6 — Sec. III F mentions "Linear(4096,128)" with PyTorch-style notation inside body text
Use mathematical notation; e.g. "fully-connected layer ℝ⁴⁰⁹⁶ → ℝ¹²⁸."

### P3-Mi7 — Equation (1) and (2) — N is overloaded
N is "input dimensionality" in (1) but also "input dimension matches the number of catalog features" earlier; reuse symbols collide.

### P3-Mi8 — "BigAE" is asserted as a framework but never defined as an acronym
Spell out at first use.

### P3-Mi9 — "TIC 374313355" appears in two different contexts (score 49.5 in SDSS, 8.1 in DESI) — is this the same object?
Fig. 6 caption clarifies but the body in Sec. IV C does not state which score is reported.

### P3-Mi10 — Caveat (j) in Table IV references "GS corrected" but the body uses "Gold+Silver"
Inconsistent abbreviation.

### P3-Mi11 — Appendix F retains a "quarantined" ACT block as a sub-paper
This whole appendix is internal-process documentation; trim or remove.

### P3-Mi12 — Figure 9 "border color indicates taxonomy class" but border colors are not legible at print resolution
Add a legend.

### P3-Mi13 — "Independent Researcher" affiliation acceptable but the paper's computational claims (H200, 42 hours) deserve a code/data DOI for reproducibility, not just a HuggingFace + GitHub link
HuggingFace dataset is "private pending arXiv acceptance"; for PRD review, the dataset must be accessible to referees now.

### P3-Mi14 — Table III: dec column labeled "Dec" — units (degrees) not stated.

### P3-Mi15 — Table V: ACT row retained in the computational details with disclaimer; either remove or move to Appendix F.

---

## NITs

### P3-N1 — Repeated phrase "before/after diagnostic" appears 6+ times verbatim.

### P3-N2 — "cross-transfer" hyphenation inconsistent ("cross-transfer" vs "cross transfer" vs "crosstransfer" — page 12).

### P3-N3 — "validation MSE" / "val_loss" mixed throughout.

### P3-N4 — Date "(Dated: June 2026)" — future-dated submission.

### P3-N5 — Section headers in title-case inconsistent ("Path-C Rebuild Methodology: Native Retrains as Core Protocol" vs others).

### P3-N6 — "∼ 6500×" SDSS rate-compression — give exact ratio (77,905 / 12 = 6492×).

---

## Summary recommendation
**REJECT**

This is a catalog construction paper with substantial methodological self-criticism (LAMOST blue-excess artifact, ACT quarantine, three FAIL-gate surveys retained as "exploratory") and two null cosmological add-ons, packaged with a 378,280-headline that is internally acknowledged to overstate the science-grade catalog by ~30%. The internal version label "Path-C" appears in the title, broken figure references (Fig. ??) appear in the body, the bibliography contains an editorial note, and the score scale on Figure 9 contradicts the score scale defined in Sec. II B. Neither the fNL forecast (αjk consistent with zero) nor the NANOGrav fit (γ = 2.567 with both physical predictions ruled out at >1σ) constitutes a PRD-grade physics result, as the authors themselves explicitly state. The catalog work is potentially publishable at MNRAS/ApJS after the LAMOST tier is removed, all FAIL-gate surveys are excluded from the headline, the "Path-C" branding is stripped, and the cosmology sections are demoted to consistency-checks rather than headlines. As currently framed for PRD, it should not be advanced to a revise-and-resubmit cycle.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report (Second Pass) — Additional Findings on P3

After a fresh pass focused on arithmetic auditing, equation consistency, figure-vs-body cross-checks, and appendix-vs-main-text reconciliation, I identified several additional issues that the first pass missed. The most significant are two **essential**-tier arithmetic/methodology inconsistencies.

---

## ESSENTIAL findings (new)

### P3-E11 — Appendix C Fisher forecast uses a method §VI D explicitly says "fails"
**Sec. V, Appendix C (Table VII), Sec. VI D (i).** The paper presents **two incompatible Fisher forecasts** for σ(fNL):
- **§V (primary)** uses the Fisher-positivity-respecting quadratic form 1/σ² = F₀ + cα² with F₀ = 1/8.98², c = 0.0747.
- **Appendix C / Table VII** uses linear scaling: Δσ/σ_std ≈ (6.1%/0.15)·α.

These give substantively different σ at α ≠ 0.15. Recomputing:
| α | Table VII (linear) | §V form (quadratic) | Discrepancy |
|---|---|---|---|
| 0.20 | 8.25 | 8.06 | 2.3% |
| 0.30 | 7.88 | 7.23 | 9.0% |
| 0.50 | 7.15 | **5.67** | **26%** |

Worse, §VI D(i) explicitly states: *"local-linear propagation σ(fNL) ≈ 8.98 − 3.66α **fails** inside the 1σ interval α ∈ [−0.46, +0.84] that crosses zero."* Yet Table VII tabulates the linear forecast across α ∈ [0.05, 0.50] — entirely within the regime the paper itself flags as broken. The α=0 stationary-point argument (slope is zero by construction in the quadratic form) means the linear method is qualitatively wrong near α=0, where most of Table VII lives.

**Fix:** Either (a) recompute Table VII using the quadratic form, in which case the headline 6.1% improvement at α=0.15 changes, or (b) delete Appendix C / Table VII and state that the prior linear forecast is superseded. Cannot retain both.

### P3-E12 — Table I "Aggregate 58.8%" SIMBAD-unmatched not reproducible from per-survey rates
**Table I, Fig. 5, Sec. IV A.** I tried every reasonable aggregation of the disclosed per-survey rates (DESI 99% / SDSS 90% / LAMOST 50% / eROSITA 68% / NEOWISE 45% / Gaia 27%) against the cross-transfer anomaly counts. None reproduce 58.8%:

| Aggregation | Result |
|---|---|
| Count-weighted, DESI=99% on full catalog | **89.8%** |
| Count-weighted, DESI = top-10K only (10K @ 99%) | 77.0% |
| Count-weighted, ex-DESI | 75.2% |
| Unweighted mean of six surveys | 63.2% |
| Median | 49% |
| Stated headline | **58.8%** |

The 58.8% can only be reached if DESI's *full-catalog* SIMBAD-unmatched rate is ≈49% (much lower than the top-10K's 99%), e.g., back-solving: 0.588×319,043 = 187,716 implies DESI's full-catalog unmatched count ≈ 95,031, i.e. rate ≈ 48.5%. But this "true" DESI full-catalog rate is **never disclosed** anywhere in the paper; instead Table I shows DESI at 99% with a "(top 10K)" Fig. 5 disambiguation that is not propagated.

**Fix:** Either (a) disclose the full-DESI-catalog SIMBAD-unmatched rate used in the aggregation, (b) show the derivation, or (c) remove the unaudit-able 58.8% headline.

---

## MAJOR findings (new)

### P3-M17 — Figure 6 SDSS score axis is undefined between cross-transfer and native pipelines
**Fig. 6, Sec. IV C, Sec. III C.** The SDSS scores reported in Fig. 6 panels (2.8, 49.5, 12.3) cannot be interpreted without specifying which scoring axis they live on. Fig. 2 (right) shows the SDSS *cross-transfer* axis spans S ∈ [10⁻¹, 10¹¹]; the SDSS *native* axis (per Sec. III C) uses a cut at S ≥ 0.1060 for the top-77,905. A score of 49.5 is a top-1%-equivalent outlier on cross-transfer but a near-threshold value if read as a native score. The "highest of any cross-matched object" claim in the Fig. 6 caption is meaningless without axis disclosure.

### P3-M18 — Table V Planck CMB training time of 10.6 seconds is implausible
**Table V, page 15.** The native Planck convolutional AE (1.1M parameters, 200,000 patches, "up to 100 epochs" per Sec. II B) is reported with training time **10.6 s**. Even at very aggressive batch sizes on A100, training a 1.1M-parameter conv-AE on 200K samples for 100 epochs should be in the minutes-to-hours range. By comparison, the DESI fully connected AE (660K params, 47K samples) takes 3,600 s in the same table. The 10.6 s figure is either a typo (likely minutes or 10⁶ s), inference time mislabeled as training, or actual training was vastly shorter than the 200-epoch envelope claimed in Sec. II B. **Fix:** Audit and correct.

### P3-M19 — Equation (2) leaves cross-transfer μ_val and σ_val undefined
**Eq. (2), Sec. II B.** The paper defines S = (MSE − μ_val)/σ_val with "μ_val and σ_val ... on the held-out 20% validation split of *that survey's* training pool." But for cross-transfer scoring (DESI-trained AE applied to SDSS/LAMOST), there is no native training pool for the *target* survey. Which (μ_val, σ_val) is used? If DESI's, then the cross-transfer SDSS scores reaching ~10¹¹ in Fig. 2 are scaled by DESI's σ_val ≈ 0.023, implying SDSS reconstruction MSEs of order 10⁹ — physically meaningless and not annotated. The body never resolves this normalization ambiguity.

### P3-M20 — Sec. III A admits DESI fiber-assignment systematic, then Sec. V ignores it
**Sec. III A vs Sec. V.** Sec. III A: *"DESI fiber assignment incompleteness ... introduces a spatial selection function that could correlate with anomaly rate ... this systematic is not modeled in the current analysis."* But Sec. V's σ(fNL) forecast uses exactly this anomaly-tracer sample with a Landy–Szalay angular correlation that is acutely sensitive to fiber-collision-induced angular incompleteness on the ~0.04°–0.25° scales used (the DESI fiber patrol radius is ~62", and fiber collisions modulate pair counts strongly on <0.1° scales). The forecast cannot claim "zero observational systematics" while the body acknowledges the dominant DESI angular systematic is unmodeled.

### P3-M21 — Sec. III C native gate "PASS" is reported without showing the criterion is *meaningfully* satisfied
**Sec. III C; Sec. II D Step 1.** The Path-C gate criterion (a) is "validation loss ≤ 0.30." SDSS native val_loss = 0.0311 — i.e., **10× better than the gate threshold**. LAMOST native = 0.0329, similarly. A gate set 10× looser than the achieved values is not a discriminating gate. Combined with the LAMOST gate-(b) FAIL at 5.8% injection-recovery, this indicates the two-part gate of §II D Step 1 is configured to almost always pass on criterion (a) and almost always fail on criterion (b) — i.e., the two criteria do not jointly constrain the catalog. The "PASS" determinations are therefore informationally thin.

---

## MINOR findings (new)

### P3-mi16 — Eq. (E1) lacks units
**Appendix E.** The displayed pulsar-timing power-law residual log₁₀ρ_i has implicit units of seconds with f_yr in yr⁻¹ and T_obs in yr; no unit declaration appears. A reader trying to reproduce the MCMC fit must guess conventions.

### P3-mi17 — Sec. III B per-band relation between S and (r_B, r_R, r_Z) is undefined
**Sec. II B and III B.** Eq. (2) defines only S (the global standardized MSE). The per-band r_B, r_R, r_Z are stated as "computed over the blue/red/NIR subsets" but the functional relationship between S and the per-band values is never given. The Sec. III B high-z candidate selection claims ⟨r_Z⟩ ≈ 3.9 with all twelve passing S > 5 — but this cannot be checked without the per-band normalization.

### P3-mi18 — Sec. III A 0% artifact rate in top-200 from "spectral inspection"
**Sec. III A.** No description of the inspection protocol, inspector identity, or blinding. A subjective 0% artifact rate is not an auditable quantity.

### P3-mi19 — Sec. IV B Pearson p-value
**Sec. IV B.** Reported r=0.006, p=0.21 for the dust-intensity correlation. Recomputing on 38,330 pixels gives t = 0.006·√38,328 = 1.18, two-sided p ≈ 0.24. Close to 0.21 but not exact; likely reflects a slightly different N. Cite the exact N and test.

### P3-mi20 — Aggregate "0.86%" rate in Table I
**Table I.** Total cross-transfer row: 319,443/37,292,042 = 0.857% → 0.86% ✓. But the same row's 58.8% is unauditable (per P3-E12). The numerical density of the table conceals which entries are derived consistently and which are not.

### P3-mi21 — Sec. V A ESS calculation
**Sec. V A.** "ESS ≈ 5,500 (> 50τ per walker)". With 32 walkers × 10,000 production / τ=58 = 5,517 ✓ on a total-chain basis, but the "> 50τ per walker" criterion would require each walker to have >50×58 = 2,900 effective samples, vs the 10,000/58 ≈ 172 raw samples per walker. The convergence claim is not standard.

### P3-mi22 — Sec. V A "matter-bounce γ = 3.0 at +1.13σ" is fragile to the prior bound
**Sec. V A.** Posterior γ = 2.567 ± 0.382 from a flat prior γ ∈ [0, 7]. The Savage–Dickey factor 7.1×10³ is computed against the same prior; widening or narrowing the prior changes the Bayes factor multiplicatively. Standard practice requires reporting BF sensitivity to prior range; not done.

---

## NITs (new)

### P3-N7 — Title line break "37.3 Million Sources and Map Patches" — number-word formatting inconsistent with "Sources" elsewhere lowercased.

### P3-N8 — Sec. VI D Table IV row (c) reads "δfiber" inline with Greek-letter subscripts; renders ambiguously.

### P3-N9 — Sec. V A "EPTA DR2, PPTA DR3" referenced but not used in the headline γ fit; the parenthetical wastes space.

### P3-N10 — "Mpc/h" vs "h Mpc⁻¹" mixed across Sec. V and Appendix C.

---

## Summary of second-pass impact

The two **new essential** findings substantively undermine the cosmology section:

- **P3-E11** means the σ(fNL) headline numbers differ by ~10–25% depending on which Fisher method the reader applies, and the paper presents both without quantifying the discrepancy.
- **P3-E12** means the second headline figure of the paper (58.8% SIMBAD-unmatched, the basis for the discovery-rate narrative in the abstract) is not reproducible from the disclosed per-survey rates.

Combined with the original review's findings (broken Fig. ?? references, "Path-C" branding in the title, internal bibliography note, FAIL-gate surveys in the headline catalog, two null cosmology results presented as primary contributions), the recommendation **stands at REJECT** for PRD. The catalog would require a substantial rewrite before consideration at MNRAS/ApJS, and the cosmology sections should be removed or demoted to consistency checks.
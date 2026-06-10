# P3 auto-2026-06-09_0025pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-sonnet-4-6` [FALLBACK from claude-opus-4-7]
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 NO_NEW
**Wall time**: 35683.2s

---

# Referee Report: "Spectrally Unusual Sources at Scale…" (P3)

---

## Preamble

This paper presents a multi-survey autoencoder anomaly catalog, fNL multi-tracer forecasting, and a NANOGrav spectral-index analysis. The anomaly detection methodology has genuine merit, and the scale of the sweep is impressive. However, the paper contains several arithmetic errors, incompatible internal configurations, a headline count inflated by acknowledged contamination, and seriously overclaimed cosmological conclusions. I cannot recommend acceptance in the current form.

---

## ESSENTIAL FINDINGS — Paper cannot be accepted without fix

---

### P3-E1 | §V (p. 11) and Abstract (p. 1) | Arithmetic error: "7.9% improvement" contradicts σ(fNL) = 8.14

**Problem.** The abstract and §V simultaneously state "σ(fNL) = 8.14" and "7.9% improvement" against the "σ(fNL)^std = 8.98 single-tracer baseline."

Recomputing: (8.98 − 8.14)/8.98 × 100% = 0.84/8.98 × 100% = **9.35%**, not 7.9%.

The "7.9%" derives from the linear scaling formula in Appendix C/Table VII: ∆σ/σ_std ≈ (6.1%/0.15) × α_jk = 40.67% × 0.19 = 7.73% ≈ 7.9%, which would give σ ≈ 8.28, not 8.14.

The paper computes σ = 8.14 from the quadratic Fisher form (1/σ² = F₀ + c α²) but quotes the improvement from an incompatible linear approximation. These two formulas cannot be applied to the same α = 0.19 and quoted together. Every instance of "7.9% improvement" paired with "σ = 8.14" is arithmetically inconsistent.

**Required fix.** Adopt one formula throughout and recompute all quoted improvements. If the quadratic form is primary, the improvement at α_jk = 0.19 is 9.35%, not 7.9%. Update the abstract, §V, Table VII, and every downstream sentence.

---

### P3-E2 | Appendix C / Figure 8 (p. 15) vs. §V (p. 11) | Two wholly incompatible Fisher configurations with no reconciliation

**Problem.** Figure 8 and Appendix C §1 display σ(fNL) values of **11.71** (ideal multi-tracer limit), **12.72** (baseline multi-tracer), and **16.85** (single-tracer baseline) for what is called the "canonical 5-tracer configuration." Section V uses **8.14** (multi-tracer central), **8.43** (α = 0.15 fiducial), and **8.98** (single-tracer baseline) — a factor of ~1.5–1.9× smaller throughout.

The caption of Fig. 8 states that the "headline +6.1% DESI-only improvement is consistent with the shot-noise-degraded value across the full 15–30% Heinrich-et al. penalty range." This would place the DESI-only improvement as a marginal add-on inside a multi-tracer configuration with σ_baseline ≈ 12.72, not as an improvement from the 8.98 single-tracer baseline quoted in §V.

These two configurations are **mutually exclusive headlines**. The abstract quotes σ(fNL) = 8.14 (from the §V configuration), while Figure 8 shows the same tracer catalog producing forecasts in the 11–17 range. No explanation is given for the discrepancy.

**Required fix.** Identify which configuration is the primary result, define it in one place, and make all figures and supplemental material consistent. If Figure 8 and §V describe different cosmological setups (e.g., different k-ranges, survey footprints, or tracer combinations), say so explicitly in both places and present only one as the headline σ(fNL).

---

### P3-E3 | Abstract (p. 1), Table I (p. 6), §III.D (p. 7) | Headline count "378,280" includes ~113,000 known-contaminated LAMOST objects

**Problem.** The abstract states the "recommended catalog-grade subset is ~265,000 unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE), which excludes the LAMOST exploratory tier (~113,000 objects retained as a methodological lesson: 98% blue-excess training-bias artifact, injection-recovery gate FAIL)."

Despite this explicit acknowledgment that ~113,000 objects are a "training-bias artifact" retained only as a "methodological lesson," all 378,280 are presented as the headline in the title, abstract, and §VII. The 378,280 figure is not qualified as "including ~30% contamination" in the title or at first mention. The description "Path-C Unique Anomalies" implies these are validated anomalies.

**Required fix.** The headline must either (a) be changed to 265,000 with the LAMOST tier demoted entirely to an appendix, or (b) the title must explicitly flag that the count includes 113,000 known-contaminated objects. Every first-pass claim of "378,280 unique anomalies" must carry the caveat that ~30% are acknowledged artifacts.

---

### P3-E4 | §V.A (pp. 12–13) | NANOGrav "decisive" Bayes factor BMB/SMBHB = 7.1×10³ is unsupportable as stated

**Problem.** The paper claims log₁₀B = +3.85 ("decisive" on Jeffreys' scale) that matter-bounce is preferred over SMBHB, based on fitting a power-law template to the published NANOGrav 15-yr KDE free-spectrum summary statistic. Three compounding issues make this claim unpublishable:

(i) The analysis uses a derived summary product (the KDE of per-bin free-spectrum posteriors), not the raw timing residuals. Fitting to a summary statistic does not properly propagate covariances between frequency bins and systematically understates uncertainty. The NANOGrav collaboration explicitly warns against treating the free-spectrum KDE as a full likelihood replacement.

(ii) The published NANOGrav 15-yr analysis (Agazie et al. 2023, Afzal et al. 2023 [28]) uses their own full-pipeline analysis including environmental effects, spectral turnover, and eccentricity models, and does not report SMBHB disfavored at multi-sigma. A single-paper independent analysis reporting SMBHB disfavored at 4.61σ directly contradicts the collaboration's own published conclusions and demands an explicit reconciliation.

(iii) The Savage-Dickey ratio compares point predictions at γ = 3.0 and γ = 4.33 against a broad uniform prior over γ ∈ [0, 7]. This ratio is prior-dominated and varies by orders of magnitude under any reasonable alternative prior choice. Calling the result "decisive" without a prior-sensitivity analysis is inappropriate.

**Required fix.** Either remove the NANOGrav section, or: (a) quantify the error introduced by using the KDE summary product vs. the full likelihood; (b) reconcile the γ = 2.567 ± 0.382 result with the NANOGrav collaboration's published spectral constraints; (c) perform a prior-sensitivity analysis for the Savage-Dickey ratio; (d) remove the word "decisive" and all language implying detection.

---

### P3-E5 | Abstract (p. 1), Title, §II.D (p. 3), throughout | "Path-C" is internal versioning language in the title and body

**Problem.** The paper title and abstract both feature "Path-C" as a descriptor. The body uses "Path-C rebuild," "Path-C native-retrain," "Path-C unique-object headline" throughout. This naming pattern (Path-A, Path-B, Path-C suggests internal iteration labels) is internal project-management bookkeeping that has propagated into the manuscript. A reader has no way to decode this label from the title alone. The method should be given a descriptive name (e.g., "native-retrain multi-survey protocol").

**Required fix.** Replace "Path-C" with a descriptive term throughout, including the title.

---

### P3-E6 | §V (p. 10–11) | QSO-candidate sample (5,384 objects) driving the fNL bias measurement has no documented selection criteria

**Problem.** Section V states: "A Landy–Szalay angular two-point analysis on the full 5,384 QSO-candidate sample." No selection criteria for these 5,384 objects are stated anywhere in the text. The reader cannot determine how they were identified from the 195,829 DESI anomalies. This sample is the entire basis for the empirical bias measurement α_jk = 0.19 ± 0.65 and the downstream σ(fNL) forecast. A central scientific measurement based on an undocumented sample is unpublishable.

**Required fix.** Provide explicit selection criteria for the 5,384 QSO candidates: score threshold, redshift range, spectral class assignments, TARGETTYPE cuts, etc. Reproduce these criteria in the data release.

---

### P3-E7 | §VI.C (p. 12), Abstract (p. 1), Table I (p. 6) | Surveys failing injection-recovery gate are included in "recommended catalog-grade subset"

**Problem.** The abstract defines the "recommended catalog-grade subset" as DESI + SDSS + eROSITA + Gaia + NEOWISE (~265,000 objects). Of these, **Gaia DR3** has injection-recovery 5.2% (gate FAIL) and XV-stability 41.0%, and **eROSITA DR1** has injection-recovery 1.2% (gate FAIL), with the paper explicitly noting "catalog completeness for LAMOST, Gaia, and eROSITA is formally unquantified" (§VI.C). Including eROSITA and Gaia in the "recommended catalog-grade subset" while simultaneously declaring them gate FAIL is internally contradictory. Users following the paper's guidance will use a subset that the paper's own validation protocol has not cleared.

**Required fix.** Redefine the recommended subset to include only surveys that pass all gates (DESI, SDSS, Planck, NEOWISE), or explicitly quantify the completeness penalty incurred by including gate-FAIL surveys and state the conditions under which those surveys can be used.

---

## MAJOR FINDINGS — Significant revision required

---

### P3-M1 | Table VII (p. 16), §V (p. 11) | Linear and quadratic Fisher formulas applied to the same α without acknowledgment

**Problem.** Table VII explicitly states it uses "linear scaling from the fiducial full 7-bin Fisher result at α = 0.15." Section V uses the quadratic form 1/σ² = F₀ + cα². At α = 0.20, the linear formula gives σ = 8.25 (8.1% improvement) while the quadratic gives σ = 8.057 (10.1% improvement). The two differ by 0.19 in σ, ~2% in improvement. Table VII and Section V are not consistent, but the paper presents them as part of a unified analysis.

**Required fix.** Adopt one formula throughout. If the quadratic form is correct for Section V (it is, by the Fisher positivity argument in §VI.D(i)), then Table VII must be recomputed using the same quadratic form.

---

### P3-M2 | §IV.A (pp. 8–9) | "~17.8% genuine novelty fraction" is a single-stratum point estimate, not a catalog-level metric

**Problem.** The abstract, §IV.A, §VII, and Figure 5 caption all present "~17.8%" as the primary novelty metric for the catalog. The paper itself states this is a "single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested." The top-1,000 represents 0.5% of DESI anomalies (1,000/195,829) and 0.26% of the full catalog (1,000/378,280). Since novelty fraction decreases monotonically with decreasing anomaly score (the highest-scored objects are by definition the most unusual), the 17.8% figure is an upper bound on the full-catalog novelty rate. Presenting it as the "discovery-rate figure" and instructing readers to "quote 17.8% (not 58.8%) when summarizing the catalog's discovery rate" is misleading.

**Required fix.** Reframe 17.8% as "novelty fraction at the top-1,000 score stratum (upper bound on full-catalog rate)." Remove instructions to use it as the catalog discovery rate.

---

### P3-M3 | §III.F (p. 7) | Planck CMB autoencoder fails gate criterion (a); anomaly patches are not characterized

**Problem.** The Planck native convolutional autoencoder has val loss = 0.4437, which exceeds criterion (a) (≤ 0.30) by 48%. It passes only on criterion (b) (100% injection-recovery). The 200 anomaly patches have scores in the range [0.558, 0.621] — a remarkably narrow range suggesting these patches may be distinguished by a single systematic feature rather than diverse anomalies. No example reconstructions, angular power spectra, or physical characterization of the 200 patches is provided.

**Required fix.** Show example reconstructions for the 200 Planck patches. Characterize what property triggers high anomaly scores. Address whether the narrow score range indicates a single systematic effect (e.g., point-source contamination, map artifacts). Acknowledge that the val loss criterion failure is a relevant caveat.

---

### P3-M4 | §V.A (pp. 12–13) | The anomaly catalog plays no role in the NANOGrav analysis

**Problem.** The NANOGrav spectral-index MCMC analysis (§V.A, Appendix E) fits a power-law template to the NANOGrav KDE free-spectrum. The anomaly catalog is not used anywhere in this analysis. The claim in §VII point 5 that this constitutes a "cosmological application" of the anomaly catalog is false: it is an independent PTA analysis that could have been performed without any of the surveyed data. The paper bundles this analysis to strengthen the cosmological motivation, but the connection is absent.

**Required fix.** Either remove the NANOGrav section and move it to a dedicated companion paper, or establish a concrete, quantitative connection between the anomaly catalog (or its tracer properties) and the PTA analysis. Merely stating both involve "bounce cosmology" is not a scientific connection.

---

### P3-M5 | §III.G, §III.H (p. 8) | Gaia and NEOWISE parent samples have no documented selection criteria

**Problem.** Gaia DR3 input is 50,000 variable stars; NEOWISE input is 43,518 infrared sources. Gaia DR3 contains ~1.8 billion sources; the NEOWISE catalog has hundreds of millions. Neither section explains how the input parent sample was selected. Anomaly rates (1.0% for both) are meaningless without knowing the selection function of the parent catalog. If these 50,000/43,518 were selected on known variability or extreme infrared color, the anomaly detection is circular.

**Required fix.** Document the exact queries used to extract the Gaia and NEOWISE input samples. State the number density on sky, magnitude range, and any quality cuts. Without this, these survey tiers cannot be evaluated.

---

### P3-M6 | §III.B (p. 5) | 12 z≈6 QSO candidates presented without coordinates or independent confirmation

**Problem.** The "confirmed high-z QSO candidates" section uses the word "confirmed" (section title) despite providing no spectroscopic confirmation beyond the autoencoder selection + three selection criteria applied to the same DESI spectra. Providing TARGETIDs without right ascension/declination or equivalent coordinates in the main paper makes independent verification impossible. No previous spectroscopic or photometric identification for any of the 12 objects is provided.

**Required fix.** Replace "confirmed" with "candidate" throughout. Provide RA/Dec for all 12 objects. State SIMBAD and NED status for each. Change the section title.

---

### P3-M7 | §II.A (p. 2) | BigAE convolutional Planck architecture is not BigAE; nomenclature is inconsistent

**Problem.** The paper defines BigAE as "a symmetric fully connected autoencoder" but §III.F and §II.D use a completely different architecture for Planck CMB (3 convolutional layers + FC bottleneck, 1.1×10⁶ parameters). This architecture is called "Path-C native CMB convolutional autoencoder" but is also described under the BigAE framework. This confusion is compounded in Table V, which lists Planck as having latent dim 128† and 1.1M parameters with a dagger footnote explaining it's a convolutional architecture.

**Required fix.** Clearly separate BigAE from the Planck convolutional autoencoder in §II.A. The Planck model should be described in its own subsection, not as a variant of BigAE.

---

### P3-M8 | §II.B (p. 2–3) | DESI scoring includes filler-tile, sky-fiber, and calibration spectra

**Problem.** The 0.87% anomaly rate applies to all 22,504,897 DESI spectra including ~16 million "filler-tile, sky-fiber, or calibration-exposure spectra without a validated TARGETTYPE." Sky fibers and calibration exposures are instrumentally defined and will have spectra far outside the training distribution by design. The fraction of the 195,829 anomalies drawn from this unclassified ~16M tier is never stated. If a substantial fraction are sky/calibration artifacts, the catalog is significantly contaminated.

**Required fix.** Report what fraction of the 195,829 DESI anomalies come from the ~16M unclassified tier. Flag these as calibration suspects distinct from the astrophysically meaningful subset.

---

## MINOR FINDINGS — Address before acceptance

---

### P3-m1 | §II.D (p. 3) | Exact duplicate phrase
> "reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)"

The parenthetical is a verbatim repetition of the preceding clause. **Delete one.**

---

### P3-m2 | Figure 1 (p. 4) | Spatial map shows cross-transfer baseline (319,443), not the canonical catalog (378,280)

Figure 1 shows the "initial cross-transfer anomaly baseline" with 319,443 detections. The headline result is 378,280 after native retraining. The primary figure in the paper should show the primary result. The cross-transfer baseline map belongs in the appendix as a "before" diagnostic. **Add a Path-C spatial distribution figure as Figure 1.**

---

### P3-m3 | Table I (p. 6) | Column header "N^¶_anom" footnote says cross-transfer counts; body says "canonical results"

The ¶ footnote explicitly states: "Per-survey Nanom values shown in this column are the initial cross-transfer scan counts." But the table header and text describe these as canonical results. This creates a direct contradiction between the table header and the footnote. **Separate cross-transfer and Path-C counts into distinct columns.**

---

### P3-m4 | §V (p. 11) and Appendix C | "7-bin Fisher" is never defined

The phrase "7-bin Fisher result at α = 0.15 (Section V)" appears in §VI.D caveat (i) and Appendix C. No Fisher matrix with "7 bins" is defined or described in §V. The number of bins in the angular power spectrum analysis is never stated. **Define this explicitly.**

---

### P3-m5 | Figure 9 (p. 17) | "AE" label notation inconsistent with canonical score S

Panel labels use "AE=5.30" etc. The text explains: "Panel labels report the per-arm Z-arm sub-score r_Z (printed as 'AE' for legacy compatibility), not the total anomaly score S." A figure for public release should not use internal legacy labels. **Replace "AE" with "r_Z" in figure panel labels.**

---

### P3-m6 | §IV.A (p. 9) | SIMBAD-unmatched fractions given without binomial confidence intervals

For eROSITA (203/298 = 68%), a ±5% binomial interval applies. For the smaller subsets, this uncertainty is non-negligible. **Report binomial 68% CI for each unmatched fraction.**

---

### P3-m7 | §II.B (p. 2) | 0.70 gate threshold for Jaccard stability is not justified

The paper specifies "gate ≥ 0.70" for Jaccard stability without citation or derivation. **Justify this threshold with reference to prior work or a calibration study.**

---

### P3-m8 | §III.D (p. 7) | Injection-recovery "9.7× improvement over emission-line variant" is ambiguous

The 5.8% (continuum-dip) vs. 0.6% (emission-line) comparison uses a ratio 5.8/0.6 = 9.67×. But this is the ratio of the two plant-morphology variants for the same survey, not an improvement over a previous version. The phrase "9.7× improvement" suggests temporal improvement (before/after native retrain), which is not what is meant. **Rephrase as "9.7× higher recovery rate for continuum-dip vs. emission-line injection morphology."**

---

### P3-m9 | Throughout | Heterogeneous injection-recovery morphologies prevent cross-survey comparison

The paper reports injection-recovery rates for: continuum-dip (SDSS, LAMOST), subspace injection (eROSITA), variability-axis injection (Gaia), and ecliptic-pole mask (NEOWISE). Figure 7 presents all six on the same axis as if they are commensurable. The Planck 100% result uses Gaussian-bump amplitude injections; NEOWISE 100% uses spatial masking, not amplitude injection. Combining these as "3 PASS / 3 FAIL" is statistically invalid. **Present each survey's injection-recovery test separately with explicit plant descriptions, and remove the unified Figure 7 presentation or clearly label each curve's plant type.**

---

### P3-m10 | §IV.B (p. 9) | χ²_ν = 3.76 spatial uniformity statistic is confounded by footprint geometry

The text itself acknowledges: "the significant χ²_ν = 3.76 is dominated by the inhomogeneous footprints of the seven retained archives rather than intrinsic astrophysical clustering." This statistic is uninformative about astrophysical signal. **Remove it from the abstract and results or replace with per-survey angular autocorrelation computed within each survey's footprint.**

---

### P3-m11 | §V (p. 11) | 1σ envelope [3.92, 8.98] asymmetry not adequately explained in main text

The lower bound 3.92 corresponds to α = 0.84 (α_jk + 1σ = 0.84), the upper bound 8.98 corresponds to α → 0 under the physical constraint α ≥ 0. This is explained in §VI.D(i) but not in §V. Main text readers will not understand why the "1σ" envelope is asymmetric or why the upper bound is exactly the single-tracer baseline. **Add a one-sentence explanation in §V.**

---

### P3-m12 | §V (p. 11) | "7.9% improvement consistent with no improvement at <1σ" is misleading

The 1σ lower bound is σ(fNL) = 3.92, which represents a 56% improvement. Saying the result is "consistent with no improvement at <1σ" only because the error bar includes α = 0 and the upper envelope equals the baseline — while the lower envelope shows a 56% improvement — creates a falsely pessimistic impression. **Restate: "the central forecast corresponds to a 9.35% improvement; the 1σ interval spans [−100% improvement, 0%] on the upper end due to α_jk crossing zero, making no improvement consistent at the 0.29σ level."**

---

## NITS — Cosmetic

---

**P3-N1** | Abstract (p. 1): "BMB/SMBHB = 7.1×10³" vs. body "7.14×10³" — round consistently.

**P3-N2** | §II.B (p. 2): The parenthetical disambiguating 'z-scored' from spectroscopic redshift is necessary but overly verbose; consider a single footnote instead.

**P3-N3** | Table V (p. 16): ACT DR6 row (quarantined) appears in the main computational table; belongs in Appendix F only.

**P3-N4** | §VII conclusion point 6 (p. 14): "OOD control-vs-control 0.874 (PASS)" — this metric is not defined or introduced in the main text; appears only in the conclusions.

---

## Arithmetic Audit Summary

| Claim | Recomputed | Paper states | Status |
|---|---|---|---|
| LAMOST compression | 44,075/2,054 = 21.46× | 21.5× | ✓ |
| SDSS compression | 77,905/12 = 6,492× | ~6500× | ✓ |
| 141× vs. ref [11] | 378,280/2,685 = 140.9× | ~141× | ✓ |
| 73× DESI-only | 195,829/2,685 = 72.9× | ~73× | ✓ |
| DESI rate | 195,829/22,504,897 = 0.870% | 0.87% | ✓ |
| Arm count sum | 151,244+44,436+34+19+96 = 195,829 | 195,829 | ✓ |
| Dedup compression | 10,213/388,493 = 2.629% | 2.629% | ✓ |
| 637+9,576 = 10,213 | ✓ | 10,213 | ✓ |
| Path-C sum to 388,493 | 195,829+77,905+113,342+298+200+500+419 = 388,493 | 388,493 | ✓ |
| σ(fNL) at α=0.19 (quadratic) | 1/σ²=1/8.98²+0.0747×0.19²=0.01511; σ=8.137 | 8.14 | ✓ |
| **Improvement at σ=8.14** | **(8.98−8.14)/8.98 = 9.35%** | **"7.9%"** | **✗ FAIL** |
| MB σ-deviation | (3.0−2.567)/0.382 = 1.133σ | +1.13σ | ✓ |
| SMBHB σ-deviation | (4.33−2.567)/0.382 = 4.615σ | +4.61σ | ✓ |
| Envelope lower bound (α=0.84) | σ = 3.919 | 3.92 | ✓ |
| eROSITA unmatched | 298×0.68 = 202.6 | 203 | ✓ |
| NEOWISE polar fraction | 17/436 = 3.90% | 3.9% | ✓ |

One confirmed arithmetic error (7.9% improvement), compounded by the incompatible Fisher configurations of P3-E1 and P3-E2.

---

## Page count and
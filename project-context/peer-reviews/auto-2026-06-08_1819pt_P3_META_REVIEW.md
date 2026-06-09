# P3 auto-2026-06-08_1819pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `claude-opus-4-7` [FALLBACK to Claude]
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 277.2s

---

# Meta-Review of P3 (auto-2026-06-08_1819pt)

I have read the rendered PDF and the five prior reports. The prior reviews caught the principal Fisher-forecast arithmetic error (7.9% vs 9.4%), the artificially-capped 1σ envelope [3.92, 8.98] vs the correct [3.92, 5.95], the audit-language saturation, the failed-gate inclusions, the Fig 1 "8 archives" title contradiction, the Fig 5 axis mislabel, the future-dated reference [12], the SDSS coverage gap (1.93M vs 2.30M), the table-restructuring need, and the NANOGrav-vs-catalog disconnect. Below are issues none of the five reviewers caught.

---

## NEW ESSENTIAL findings

### P3-META-E1 — Inconsistent OOD Jaccard value: 0.874 vs 0.732 (Conclusions item 6, p.14 vs §II B p.2 and §VI D (i) p.13)

**Why missed:** All five reviewers focused on the Fisher arithmetic chain; none cross-checked the OOD validation number across all three locations it appears.

**Quote:** Conclusions item 6: *"DESI 5-fold Jaccard stability J̄ = 0.862 (PASS); OOD control-vs-control 0.874 (PASS)."*
§II B: *"the production-vs-5-seed-control is J̄prod×ctrl = 0.732 (gate ≥ 0.50, PASS)."*
§VI D (i): *"OOD holdout (seed 20,260,501) confirms production-vs-5-seed-control Jaccard J̄prod×ctrl = 0.732 (≥ 0.50, PASS)."*

The same metric is reported as 0.732 in two places in the body and as 0.874 in the Conclusions. The 0.874 value appears nowhere else in the paper and has no derivation.

**Required fix:** Reconcile. State which is correct, and if 0.874 is a different metric, label it as such.

### P3-META-E2 — Two incompatible single-tracer σ(f_NL) baselines without reconciliation (Fig 8 p.15 vs §V p.11)

**Why missed:** Reviewers checked the Fisher arithmetic but did not compare the Appendix C figure baselines to the §V baseline. R3 caught the Table VII inconsistency but not the more flagrant Fig 8 mismatch.

**Quote:** Fig 8 caption: *"Multi-tracer Fisher σ(fNL) vs. tracer number density n̄ for the canonical 5-tracer configuration of §V. The dashed gray line marks the dense-tracer limit (σ(fNL) = 11.71); the dotted dark-red line marks the single-tracer baseline (σ(fNL) = 16.85)."*
§V: *"σ(fNL)std = 8.98 single-tracer baseline."*

The same paper uses σ_single-tracer = 16.85 in Appendix C/Fig 8 and σ_single-tracer = 8.98 in §V, with no reconciliation. This is a 1.9× difference in the headline forecast denominator. The "+7.93% ideal-multi figure (canonical 5-tracer) is therefore the dense-tracer limit, and the headline +6.1% DESI-only improvement is consistent with the shot-noise-degraded value" sentence in Appendix C splices percentages from two completely different baseline configurations.

**Required fix:** Identify which baseline corresponds to which forecast, and state the relationship. If 8.98 is the DESI-DR1-only QSO baseline and 16.85 is some other configuration's single-tracer reference, label them.

### P3-META-E3 — IsolationForest cross-validation for Gaia uses a different (10×-expanded) dataset than the published catalog (Table I footnote §, p.6)

**Why missed:** R1 mentioned the 41% IF stability as evidence against the catalog but did not catch that the 41% number characterizes a *different* underlying sample than the published Gaia anomaly set.

**Quote:** Table I footnote §: *"41.0% (2048/5000) for Gaia DR3 (using a 10×-expanded 500,000-source sample; see caveat (v) for details)."*
§III G: *"Input: 50,000 variable stars... Anomaly count: 500 (top 1%)."*

The published Gaia catalog is 500 anomalies drawn from 50,000 sources. The IF cross-validation that yields 41% stability is run on a 500,000-source pool that is *not* the published catalog's input. The 41.0% metric therefore validates a counterfactual catalog, not the one released. (For eROSITA the analogous 81.5% figure is on 9,303 from 930,203, which *is* the published-catalog input — so the methodological mismatch is Gaia-specific.)

**Required fix:** Either re-run IF cross-validation on the actual 50,000-source Gaia input (matching the published catalog), or explicitly relabel the 41% as "stability on an extended 10× pool, not on the released catalog."

### P3-META-E4 — DESI 5-fold Jaccard J̄ = 0.862 is computed on the 47k training pool, not the 22.5M published catalog (§II B p.2)

**Why missed:** R1 noted training/test overlap but did not flag that the Jaccard stability gate—the paper's primary catalog-robustness claim—does not test the catalog that is published.

**Quote:** §II B: *"each fold trains a fresh BigAE on 80% and scores the full 47,000 spectra... Mean pairwise Jaccard overlap of each fold's top-1% anomaly set is J̄ = 0.862."*

The published catalog is 195,829 anomalies from 22.5M spectra. The Jaccard stability gate computes overlap on top-1% of the 47k *training pool*, which is the in-sample overlap of 470 objects per fold across five seeds. The stability of the 195,829-object published catalog is unmeasured. The S>5 cut applied to the 22.5M-spectrum production scan and the top-1% applied to the 47k cross-validation pool are also different thresholds, so the metric does not even self-consistently characterize the same selection function as the catalog.

**Required fix:** Score the five fold-trained models on the full 22.5M spectra, apply the S>5 cut, and report inter-fold Jaccard on the resulting >100k-object sets.

---

## NEW MAJOR findings

### P3-META-M1 — α is transferred from DESI to a SPHEREx forecast with no justification (Abstract, §V p.11)

**Why missed:** All five reviewers focused on the arithmetic of α propagation; none questioned whether α is even transferable across surveys.

The empirical α_jk = 0.19 ± 0.65 is measured on 5,384 DESI QSO candidates. The forecast σ(f_NL) is then computed for SPHEREx (a future low-resolution, all-sky NIR survey with different selection function, redshift coverage, depth, and bias). α encodes an anomaly-selection-vs-standard-sample bias ratio that is specific to DESI's spectroscopic anomaly identification; it is not a survey-invariant quantity. The forecast as written assumes the SPHEREx anomaly-selected tracer would inherit the DESI-measured α.

**Required fix:** Either restrict the forecast to DESI itself (σ(f_NL)^DESI for the actual DESI survey), or derive a bridging argument for why α generalizes to SPHEREx.

### P3-META-M2 — The "7.9% improvement" comes from the Table VII linear formula, not the Fisher form (§V p.11)

**Why missed:** R1 (E1) flagged the 7.9% vs 9.35% discrepancy as a free-floating arithmetic error but did not identify its origin.

The linear extrapolation in Table VII gives improvement(α=0.15) = 6.1%, scaling linearly: 6.1% × (0.19/0.15) = 7.73%, ≈ 7.9% when rounded. The paper claims to use the Fisher form 1/σ² = F_0 + cα², which yields σ = 8.14 and improvement (8.98−8.14)/8.98 = 9.35%. The two numbers come from two different methods. The author quoted the σ value from the Fisher form (8.14) but the improvement percentage from the linear-scaling form (7.9%), producing an internally inconsistent claim that is *not* a simple arithmetic error.

**Required fix:** State which method is canonical and use it consistently. If Fisher form, the improvement is 9.4%, not 7.9%.

### P3-META-M3 — Gold+Silver subset (1,122 objects) selection criteria undocumented (§V p.11)

**Why missed:** R1 (M8) caught that the BAL QSO has no coordinates, but no reviewer flagged the unspecified Gold+Silver cut, which produces α_GS = +1.83 ± 2.03 — a substantially more favorable central value than the full sample.

The 1,122 high-confidence subset of the 5,384-object QSO candidate sample is described as "Gold+Silver" with sample densities n̄_gold = 8.5×10⁻⁶ and n̄_silver = 4.5×10⁻⁵ (h/Mpc)⁻³ stated only in Fig 8 caption, but the underlying selection criteria (anomaly score cut? redshift cut? confidence flag?) are not specified anywhere in the body. The Gold+Silver α = +1.83 vs full-sample α = +0.19 is a 1× shift in the same direction as the desired f_NL improvement; post-hoc subsample selection that strengthens a result requires explicit pre-registration disclosure.

**Required fix:** Specify the exact selection criteria for Gold and Silver tiers, and whether these criteria were defined before or after the α measurement.

### P3-META-M4 — Landy–Szalay random density 5× the data is below standard practice (§V p.11)

**Why missed:** No reviewer audited the LS estimator's random oversampling factor.

The paper uses 26,920 randoms for 5,384 QSO candidates, i.e., N_rand/N_data = 5. Standard LS practice uses N_rand/N_data ≥ 20–50 to drive shot noise in the random catalog below the cosmological signal. At 5× oversampling, the random-density shot noise contributes ~9% additional variance to ξ(θ) compared to the dense-random limit, inflating the bias-measurement error bar. The reported σ_α = 0.65 may itself be underestimated.

**Required fix:** Re-run LS with ≥ 50× random oversampling; report whether α_jk changes.

### P3-META-M5 — Savage-Dickey factor inconsistent with stated posterior (§V A p.12, Table IV p.14)

**Why missed:** Reviewers checked the +1.13σ and +4.61σ parameter shifts but did not independently recompute the Bayes factor from the stated posterior.

Under the stated Gaussian-approximation posterior γ = 2.567 ± 0.382 with uniform prior γ ∈ [0,7]:
- p(γ = 3 | D) ≈ exp(−(3−2.567)²/(2×0.382²)) / (0.382√(2π)) = 0.549
- p(γ = 3 | prior) = 1/7 = 0.143
- B_MB/free (Savage-Dickey) = 0.549 / 0.143 = **3.84**

The paper reports B_MB/free = 3.23. Similarly for SMBHB:
- p(γ = 4.33 | D) ≈ exp(−10.65) / 0.958 = 2.47×10⁻⁵
- B_SMBHB/free = 2.47×10⁻⁵ / 0.143 = **1.73×10⁻⁴**

The paper reports 4.52×10⁻⁴ (factor of 2.6 too large). If the actual posterior is non-Gaussian, the Bayes factor calculation may be correct, but then the Gaussian-approx σ = 0.382 used for the +4.61σ SMBHB parameter shift is *not* applicable. Either:
- (a) the posterior is Gaussian → recompute Bayes factors to ≈ 3.84 and ≈ 1.7×10⁻⁴ (ratio still ~ 2×10⁴);
- (b) the posterior is non-Gaussian → withdraw the Gaussian-approximation σ from the +4.61σ SMBHB and +1.13σ MB tests.

Cannot have both ways.

**Required fix:** State whether the Bayes factors are computed from kernel-density estimation of the actual posterior (in which case the +1.13σ/+4.61σ Gaussian-σ test is invalid) or from a Gaussian approximation (in which case the numerical Bayes factors are wrong).

### P3-META-M6 — Fig 8 baseline (16.85) implies σ(f_NL) numbers in §V are non-SPHEREx (§V vs Appendix C)

**Why missed:** Tied to META-E2 but distinct: if the SPHEREx single-tracer baseline is 16.85 (per Fig 8, which is labeled "for the canonical 5-tracer configuration of §V"), then the 8.98 used in §V is not the SPHEREx baseline but presumably a DESI-only or different forecast. The paper conflates a measurement on DESI tracers with a forecast for SPHEREx, but the baseline numbers come from yet a third configuration.

**Required fix:** Provide a single table mapping baseline (single-tracer σ) → improved (multi-tracer σ) → α-dependence for each of {DESI-only, SPHEREx canonical, SPHEREx with anomaly tracers}.

---

## NEW MINOR findings

### P3-META-m1 — Fig 9 panel "AE" values span 3.768 to 83,518 with inconsistent semantics (Fig 9 p.17)

**Why missed:** R1 m3 noted AE inconsistency but did not catalog the magnitudes.

Panel labels read "z=6.20 | AE=5.30" (a per-arm subscore, range 0–25) and "AE=83518" (a raw MSE proxy, range 10³–10⁵). These are different quantities under the same label. A reader cannot interpret the gallery without unit ambiguity.

**Required fix:** Use one consistent score (the canonical S of Eq 2) in panel labels, or label units per panel.

### P3-META-m2 — Eq (E1) does not specify units of T_obs (Appendix E, p.17)

**Why missed:** R1 M10 flagged dimensional ambiguity in Eq E1 but did not isolate the T_obs unit ambiguity.

The factor log₁₀(T_obs) appears in Eq E1. Standard PTA conventions use seconds (so T_obs ≈ 5.06×10⁸ s for 16.03 yr), but the text says "T_obs = 16.03 yr." If T_obs is in years in the log term, the inferred amplitude log₁₀ A is shifted by log₁₀(3.15×10⁷)/2 ≈ 3.7 dex relative to the conventional seconds convention.

**Required fix:** State T_obs units explicitly, and verify the inferred log₁₀ A = −14.025 against published NANOGrav 15-yr re-fits.

### P3-META-m3 — The 9,576 intra-survey duplicates imply per-survey catalogs contain unmerged repeats (§IV C, Table I footnote ‖)

**Why missed:** Focus was on the 637 cross-survey clusters; the 9,576 intra-survey number passed unaudited.

The 7-way 5″ dedup collapses 10,213 detections total: 637 multi-survey + 9,576 intra-survey. Each survey's anomaly catalog therefore contains, on average, ~1,370 internal positional duplicates. For DESI's 195,829 anomalies this implies ≥0.5% are repeat-fiber-of-same-target spectra; for the smaller surveys it implies a higher fractional contamination. The paper does not break down which surveys contribute the 9,576.

**Required fix:** Tabulate intra-survey duplicate counts by survey.

### P3-META-m4 — Uniform prior γ ∈ [0,7] is used for Savage-Dickey on a physical parameter with informative priors (§V A p.12)

**Why missed:** Reviewers did not audit prior choice for the Bayes factor.

A uniform prior on γ ∈ [0,7] places equal weight on γ = 0 (white noise) and γ = 7 (steep red). Standard GW-physics priors are informed: SMBHB models predict γ = 13/3 ≈ 4.33 with O(0.5) systematic; matter-bounce models predict γ ≈ 3 ± O(0.5). The Bayes factor B_MB/SMBHB = 7.1×10³ depends linearly on prior width via the Savage-Dickey ratio's normalization (or model-evidence integral for nested models). A physics-motivated prior would reduce the factor by ~3-fold.

**Required fix:** Report Bayes factor sensitivity to prior width, or use a physics-motivated prior.

### P3-META-N1 — Fig 8 vertical lines for "anomaly_gold" and "anomaly_silver" use a configuration nowhere defined in §V (Fig 8 caption p.15)

The Gold/Silver tiers, their density derivations, and their connection to the 1,122-object subset are not provided in the body before being plotted.

---

## Meta-review recommendation

**REJECT**

Given the union of all six reviews, the actual blocker count is approximately **9 essential issues** (R1's E1–E9 list incompletely overlaps with R3 and R4; meta-review adds E1–E4): the Fisher arithmetic chain has two distinct errors (R1-E1 and R1-E9, confirmed by R3); the σ(f_NL) envelope cap is mathematically wrong (R1-E9, R3-E1); three of six surveys fail injection-recovery gates and remain in the headline (R1-E3, R4-M1); the OOD Jaccard, IF cross-validation, and Fisher baselines are internally inconsistent (META-E1–E4); the Bayes factor is inconsistent with its stated posterior (META-M5); and the catalog is built atop bookkeeping language that signals an unfinished manuscript (R1-E5, R4-N2). My confidence that this paper would survive external (non-bigbounce) peer review at PRD is **very low** (≲5%). The catalog itself may be a useful community data product after substantial restructuring and an honest withdrawal of the σ(f_NL) and NANOGrav claims, but as currently written the paper conflates an unfinished engineering catalog with three unrelated cosmological forecasts that do not derive from the catalog and contain demonstrable numerical errors. Even a sympathetic editor would request that the cosmology be removed entirely and the catalog be resubmitted to a data-release venue (ApJS, MNRAS, or PASP) rather than PRD.
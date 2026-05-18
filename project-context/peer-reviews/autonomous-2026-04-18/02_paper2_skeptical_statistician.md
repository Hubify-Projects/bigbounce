# Paper 2 — Skeptical Statistician Peer Review (autonomous-2026-04-18)

**Reviewer persona:** Bayesian hygiene fanatic. Fisher-forecast skeptic. Monte Carlo first, analytic derivatives never.
**Manuscript:** `research/focused_paper_source_integration/02_full_draft.tex` (revtex4-2, 372 lines, compiled 2026-04-17)
**SSOT reference:** `project-context/SSOT/paper-2/status.md` v1.6.0 headline 97 %
**Fisher code audited:** `h200_scripts/experiments/fisher_forecast_spherex.py`
**Fisher result JSON audited:** `pipelines/h200_results/overnight_batch5/fisher-forecast-spherex/fisher_forecast_summary.json`
**Bias-validation JSON audited:** `pipelines/p1_highz_tracers/outputs/step4_bias_validation/bias_validation.json`

---

## Headline

**The paper is substantially honest about adopted external forecasts (σ(fNL)=0.7 from Heinrich+2023 for SPHEREx, σ(fNL)=0.5 from Schlegel+2022 for MegaMapper). But the "internal" Fisher pipeline this lab built — the one referenced in the parent directive as σ = 16.85 / 12.72 / 11.71 with +7.93 % anomaly improvement — is BROKEN. The committed `fisher_forecast_summary.json` returns σ(fNL) = 0.0, Fisher values of order 10^13, and a "matter bounce detection significance" of 13,295,528 σ. Every `improvement_pct` is `NaN` from divide-by-zero. The paper itself does not cite these broken numbers (which is good), but the directive's numerology appears to be confabulated from an unverified mental model, not derived from the code on disk. The bias-validation chain also does not support the claimed 2.28 × extreme-anomaly bias that the directive asserts is cross-walked into the Fisher.**

The paper as a literary object is in better shape than the computational infrastructure that was supposed to support a bespoke forecast. Its survival strategy is to externalize: it adopts published σ(fNL) from Heinrich+2023 and Schlegel+2022 and applies a template-correction factor `r`. That `r` computation is the paper's real novel contribution and is defensible. The Bayesian model-comparison section is prior-dependent in the usual bad ways and the authors mostly admit this, but the reporting is still slanted.

**Verdict: MAJOR REVISION before submission — but the revisions are (a) add a brutal Fisher-condition-number paragraph to §3 or §7, (b) kill the directive's numbers if they ever enter the paper, (c) stop claiming a 600 k-MC Bayesian analysis without committing the code, (d) disclose the broken internal Fisher as a known limitation rather than letting it sit in the repo as an attractive nuisance.**

---

## Major

### M1. The committed Fisher forecast (`fisher_forecast_spherex.py`) is numerically broken. All committed σ(fNL) values are ≈ 0 and `detection_sigma = 10^7`.

Reading `fisher_forecast_summary.json`:
- `single_SPHEREx_only`: `fisher_total = 9.24e12`, `sigma_fnl = 0.0`, `detection_sigma_matter_bounce = 13,295,528.47`.
- `single_SPHEREx_DESI_plus_anomaly`: `fisher_total = 2.13e13`, `sigma_fnl = 0.0`, `detection_sigma = 20,200,634.72`.
- Every `anomaly_improvements.*.improvement_pct = NaN` (0.0/0.0).
- Every `multi_tracer_improvements.*.improvement_pct = NaN`.
- `best_sigma_fnl = 0.0`, `matter_bounce_detection_sigma = Infinity`.

Diagnosis: the code in `matter_power_spectrum` uses an Eisenstein–Hu zero-baryon transfer function, then normalizes to σ8 via a CDM-only σ8 integral, but the k-integration range for the σ8 normalization (`k = 1e-4 … 1e1`) and the Fisher k-range (same range in k_centres) are mis-matched against the per-tracer shot noise (`1/nbar` with `nbar ~ 1e-4` to `1e-7` (h/Mpc)^3), so P_obs is vastly dominated by the sample-variance term and `(dP/dfnl / P_obs)^2 ~ (Delta_c / alpha)^2` integrated over 50 log-spaced k-bins with Veff ~ few × (Gpc/h)^3 drives the Fisher to 10^13 per config. In short: the absolute amplitude of P(k) and the volume-weighting of modes are both off by many orders of magnitude, and the `round(sigma, 4)` then collapses sub-millionth-of-unity σ to 0.0. The fact that this was allowed to ship as a pipeline result with no sanity-check against "is σ > 0.01 ever attained by any real survey?" is a serious quality-control failure.

**Impact on paper:** The paper itself does not cite the broken numbers — it cites σ = 0.7 and σ = 0.5 from published work, which is fine. But the SSOT claims "SPHEREx Fisher code 100 %" (§10), which is false. The paper's `\url{…/v2.1.0/research/}` data-availability statement points a reader to code that, if run, produces σ = 0.0. That is a reproducibility lie.

**Required fix:** Either (a) fix the normalization and rerun so that the bespoke Fisher returns σ(fNL) in the 1–10 range matching external expectations, or (b) remove the Fisher-forecast code from the data-availability statement and explicitly note in §4 that the paper's SPHEREx constraint is adopted from Heinrich+2023 with a template-correction factor applied, with no independent Fisher computation by this work.

### M2. Directive-level numbers (σ = 16.85 / 12.72 / 11.71, +7.93 %, σ=0.36 Fisher-ideal / 0.93 Munchmeyer) are not in the paper and not derivable from the committed code. If they're planned to enter the paper, they must be computed fresh.

The parent review prompt cites specific Fisher values:
- baseline σ(fNL) = 16.85
- standard multi-tracer σ(fNL) = 12.72
- 5-tracer anomaly-optimized σ(fNL) = 11.71
- +7.93 % improvement over standard
- SPHEREx σ = 0.36 (Fisher ideal) / 0.93 (Munchmeyer+2019 conservative)
- Detection 4.7–12 σ of fNL = -4.375 by 2027

None of these numbers appear in `02_full_draft.tex`. They do not appear in the committed `fisher_forecast_summary.json`. There is no file under `pipelines/p1_highz_tracers/`, `pipelines/p3_anomaly_engine/`, or `pipelines/h200_results/` that produces them. (The closest hit is `bias_validation.json` which reports improvement_pct = 0.04 %, 0.03 %, 0.0009 % — three orders of magnitude below the 7.93 % claim.)

If these numbers are targets for a future forecast run, they must be generated by fixed, reproducible code and pass a sanity check before entering the manuscript or the status pages. They should not appear in any downstream surface (CLAUDE.md, index.html, SSOT, wiki) until they do.

**Specific sanity checks before any such forecast lands:**
1. σ(fNL) on a DESI-like survey with bispectrum + SDB should be ≈ 3–5 (matches Heinrich+2023, Mueller+2021). Getting 12 or 16 would be a factor of ≈ 3 off and needs justification.
2. Compute the Fisher condition number κ(F). Typical multi-tracer Fishers at this scale have κ ~ 10^4–10^6; if κ > 10^10 the matrix is effectively rank-deficient and the σ you read off a single element is an artefact of near-zero eigenvalues in the inverse.
3. Check Fisher-vs-MCMC on a synthetic data realisation. If they disagree by more than a factor of 2 the Fisher is wrong.

### M3. The 2.28 × extreme-anomaly clustering-bias claim (which the directive says is "cross-walked into the Fisher via a concrete b_anomaly × δb variance") is not in `bias_validation.json`.

The committed bias-validation JSON has five samples (`qso_all`, `gold_silver`, `gold_only`, `baseline_all`, `ir_non_qso`). The reported `relative_bias_vs_baseline` values are:

| Sample | relative_bias | n_objects | Notes |
|---|---:|---:|---|
| qso_all | 0.964 | 5000 | **below** baseline |
| gold_silver | 1.582 | 1122 | the 1.58 × |
| gold_only | 0.966 | 116 | **below** baseline |
| baseline_all | 1.000 | 5000 | — |
| ir_non_qso | 1.038 | 5000 | flat |

There is no 2.28 × entry. Gold-only's bias is actually slightly below baseline (0.966) — the opposite of what you would naively expect for the hardest-selected tier, and an immediate red flag of small-N noise. `dd_total = 61` for gold-only means ≈ 61 pair counts across 12 angular bins — five pairs per bin average. This is not a measurement; it is a fluctuation.

Worse, the "mean_w_large_scale" used to derive the relative bias is computed over only the largest 2–3 θ bins, where:
- Several samples show **negative** w(θ) (baseline_all: −0.085, −0.408; qso_all: −0.161, −0.490; gold_only: −0.345; gold_silver: +0.750, +0.574).
- Averaging over a 2-bin window that includes negative values near zero produces a ratio that is arbitrarily sensitive to which bin is included.

The metadata says `"note": "Preliminary — uses uniform randoms, not DESI survey window function"`. That single sentence is doing a lot of work: without the DESI footprint mask, the randoms don't reproduce the survey geometry and w(θ) on scales comparable to the survey's angular scale is biased by boundary effects. A clustering measurement that doesn't mask to the actual survey footprint is not publishable as a bias measurement.

**Required fix:** Either (a) recompute w(θ) against a DESI footprint random catalog with ≥ 5× the data number of randoms and propagate the LS covariance; (b) demonstrate via jackknife that the 1.58 × result is stable against removal of any one angular bin; or (c) downgrade the claim from "1.58 × enhanced clustering" to "preliminary indication, not used in the Fisher." The paper's §7 already acknowledges this by NOT numerically folding the 1.58 × into the σ(fNL) quote — but downstream materials (wiki, SSOT, directive) promote it to a headline result. That's a tension and it needs to resolve toward honesty.

### M4. The "600,000 Monte Carlo realizations" Bayesian claim has no committed code or posterior samples.

The paper's §6.3 and abstract both claim "over 600,000 Monte Carlo realisations across multiple frameworks." The SSOT §3 says "exact 600K MC Bayesian breakdown (script framework exists; individual posterior samples on pod, not committed)."

This is a problem. A published Bayes factor requires at minimum:
1. The likelihood form — it's written analytically in Eq. (6) of the paper (Gaussian likelihood + uniform competitor prior + delta bounce prior). OK.
2. The realised `fNL_obs` samples or the RNG seed. Not committed.
3. The priors on nuisance parameters (σ(fNL) ∈ [0.5,1.5], multi-tracer efficiency ∈ [0.5,1.0], b_φ Gaussian 20 % scatter, σ_GR ∈ [0,1.0]). Stated in prose. No code.
4. The aggregated Bayes factors per scenario. Only the headlines are in Table II, Table III.

Table II reports BF ranges 10–23 and P(BF>3) of 87–96 %. Table III (GR-aware) reports BF vs tuned competitor = 7.9–10.9 across four scenarios. These are not reproducible from anything in the repo.

**Required fix:** Commit a `bayes_mc.py` with fixed RNG seed, the prior spec, and the aggregated output CSV/JSON. Without it, the reader cannot verify the 8–17 Bayes factor in the abstract. The paper's "Data and Code Availability" section links a v2.1.0 tag, but I don't see the MC script inventory in the SSOT file inventory (§8). Either link it or delete the claim.

### M5. Bayes-factor prior sensitivity is reported honestly but still under-reported.

The paper does say (§6.3, final paragraph): "Varying the multifield competitor prior width gives Bayes factors from 7 (narrow [−5,+5]) to 57 (broad [−15,+15])." It also says the delta bounce prior maximally favors the bounce and Gaussian-broadening to σ_theory = 1.0 drops the median BF from ~17 to ~8.

This is good practice — it just needs one more step. When the competitor prior width goes from [−5,+5] to [−15,+15] the BF changes by **8×**. That means the claimed headline result ("bounce favored at 8–17") is fundamentally a statement about prior choice, not data. A reader should see a **prior-sensitivity table** with the matrix of (bounce prior width) × (competitor prior width) → BF, so the prior-dependence is obvious. A single abstract sentence can be skimmed past; a table cannot.

**Required fix:** Add a 3×3 or 4×4 prior-sensitivity table in §6.3 or Appendix. Without it, the Bayes factor numerology reads as "here's a lucky prior choice."

### M6. The "template-correction factor r" derivation is the paper's strongest original contribution but it has an unquantified CMB-Fisher convergence concern.

The paper says (§3.2): "validated by ℓ-space Fisher overlap … (r = 0.878 ± 0.012, stable across ℓ_ref = 50–950)."

This is good. But the CMB Fisher for f_NL is known to be dominated by low-ℓ modes where cosmic variance limits things, and the SDB channel for LSS is dominated by the **smallest** k (largest scale) where f_sky and integral constraints bite. These two channels don't share the same effective weighting. Quoting a single r value of 0.85–0.90 across both needs more than the sentence that's there. Specifically:

- What's the range of r if you weight by the SPHEREx bispectrum triangle distribution rather than a generic "LSS/SDB" spectrum?
- Does r depend on the k_min the survey can reach? Fig. 3 (k_min cliff) suggests MegaMapper σ(fNL) moves from 0.5 to 2.2 across the realistic k_min range. Does r move proportionally? If yes, the "r ≈ 0.85–0.90" abstract sentence is too stable.
- The Monte Carlo "200 realizations" injection recovery — what's the variance? The paper gives `r_meas = 0.90 ± 0.01`. With 200 samples that's a standard error of ~0.14/sqrt(200) = 0.01, which matches. But is the scatter 0.14 really symmetric around 0.90? If the template-estimator is biased at the folded configuration where |B_NL| is small, a pile-up at r ≈ 0.5 could be happening and the mean ± SD hides it.

**Required fix:** Provide a histogram figure or at least a 5-95 % percentile quote on r from the MC injection. And provide r separately for SPHEREx-bispectrum weighting vs MegaMapper-SDB weighting — the paper folds these together but the two channels have very different overlap integrals.

### M7. The σ(fNL) = 0.7 value adopted from Heinrich+2023 is taken as a given with no sensitivity quote on the underlying forecast assumptions.

Heinrich+2023 (2311.13082) is itself a Fisher forecast with its own choices (fiducial cosmology, tracer number density, multi-tracer efficiency, nonlinear bias model). When this paper "adopts σ(fNL) = 0.7" it imports all of Heinrich+2023's assumptions wholesale.

Does this paper's σ_GR uncertainty, which is added on top, overlap or double-count with GR projections already included in Heinrich+2023? Table III shows that GR marginalization at σ_GR = 1.0 drops BF vs SSFSR from 3.3e6 to 329 — a factor of 10^4. If Heinrich+2023 already includes a GR-marginalized term, applying this paper's GR layer on top is double-discounting. If Heinrich+2023 does not include GR, the "adopted" σ(fNL) = 0.7 is an ideal limit and the paper's headline 5–5.5 σ detection is overstated by whatever the GR contamination is worth.

**Required fix:** A one-sentence footnote distinguishing "Heinrich+2023's σ = 0.7 is GR-free" vs "Heinrich+2023's σ = 0.7 is GR-marginalized." I cannot tell from the present text which one the authors believe.

### M8. SPHEREx 2027 detection timeline is aggressive.

The paper says (§8.1) "SPHEREx (launched March 2025; first all-sky survey completed December 2025; science data release expected ∼2028)." The parent directive then promotes this to "4.7–12 σ detection of f_NL = -4.375 by 2027."

2028 is the published DR1 target. 2027 would require DR0.5, which is not publicly announced. A bispectrum analysis at σ(fNL) = 0.7 requires completed photo-z calibration, full-sky mask validation, nonlinear-bias modelling, and relativistic projection modelling on the actual survey data. That pipeline is not 18 months of work from a mission that just finished its first all-sky in Dec 2025.

**Required fix:** State "by 2028 DR1 (first multi-tracer bispectrum target)" not "by 2027." If a DR0.5 intermediate is plausible, cite it.

### M9. f_NL triple-role claim: "galaxy bispectrum + PBH abundance regulator + induced GW spectral shape" — are these three really independent tests or one test with three projections?

This claim comes from CLAUDE.md rather than the paper itself, but it's worth flagging for the Paper 2 + Paper 3 cross-file consistency: if a single parameter (fNL = -4.375) controls all three observables through the same physics (superhorizon primordial curvature statistics), then a detection in one is not "independent confirmation" by the other two — they're correlated draws from the same underlying prior.

The three channels have different systematic-error sources (galaxy bias for bispectrum, PBH threshold physics for abundance, second-order perturbation theory for induced GW). Systematic independence is genuine. Statistical independence is not — if fNL is really fNL, the three channels share a fully correlated central value. The paper should be careful not to multiply 5 σ × 3 σ × 2 σ as if they were independent detections.

**Required fix:** If the triple-role claim appears in Paper 2, add a sentence: "The three channels share a common parameter but have independent dominant systematics; their joint significance is not the sum-in-quadrature of individual sigmas but a joint likelihood on a single parameter."

### M10. Fisher condition-number diagnostic is never quoted.

Every multi-tracer Fisher paper I've ever reviewed should report κ(F). The paper does not. The committed code does `np.linalg.inv(C)` inside the multi-tracer branch with only `try/except LinAlgError` — i.e. it catches outright singularity but does nothing about near-singularity. At z ≈ 2.9 where DESI tracers drop out and only one SPHEREx tracer is active, the Fisher has effectively one measurement constraining several degenerate bias+fNL directions; the condition number should blow up there. The per-z Fisher numbers in the JSON do show the expected drop at high z (0 at z = 2.5+ for DESI configs) — but there's no accompanying statement like "we drop z > X from the forecast because κ > 10^8."

**Required fix:** Compute and report the Fisher condition number per configuration. Drop redshift bins where κ exceeds a documented threshold (e.g. 10^8).

---

## Minor

### m1. Cross-paper citations: Paper 1 cite is present, Paper 3 cite is absent but arguably needed.
The paper cites `\cite{Golden:2026framework}` (Paper 1, the ECH-transparency companion) correctly. The SSOT §6 argues Paper 3 is NOT implicitly cited because the multi-tracer language is about SPHEREx/MegaMapper-as-designed — that's true of §§4–5. However §7.4 mentions "photometric redshift outliers" and §6.3 mentions "multi-tracer efficiency" without explicit cross-ref to the BigBounce anomaly-tracer program. If the directive's 5-tracer anomaly-optimised forecast ever makes it into the paper, Paper 3 cross-ref becomes mandatory. As-is the paper stands alone.

### m2. `\date{\today}` on line 23.
Once the arXiv posting date is fixed, replace with the literal date string. Auto-updating date means every local rebuild changes the date, which confuses archival hashes.

### m3. Abstract math renders fine but the "4–6 σ significance" in §9 conflicts with the abstract's "~5–5.5 σ template-corrected."
Pick one range and use it consistently. Currently §6 says BF = 8–17 over tuned, §3 says detection 5.5 σ (bispectrum only) to 3.0 σ (σ_GR = 1), §9 says "4–6 σ." Not contradictory but the casual reader will catch the shifting endpoints.

### m4. "600,000 Monte Carlo realizations across analytic, mock-based, and GR-aware frameworks."
If 600 k is the sum across three frameworks (e.g. 200 k + 200 k + 200 k), say that. If it's three independent 600 k runs, say that. As currently written it's ambiguous and sounds bigger than it might be.

### m5. Table III floating-point inconsistency.
BF vs SSFSR = 3.3 × 10^6 appears twice (Ideal and Corrected scenarios). If the "Corrected (10 % residual)" scenario has a residual GR contamination, its BF should differ from Ideal. If by construction they're the same, state it.

### m6. The Appendix convention computation (Cai vs Li-Brandenberger) is good but should reference the audit that pinned it at 92 % confidence.
§2.3 says "We assign 92 % confidence to this normalization." 92 % is a Bayesian weight over what prior? One sentence of methodology would close this.

### m7. Acknowledgments disclose AI assistance. Good. Make sure arXiv metadata (Comments field) repeats this.

### m8. Fig. 3 caption says MegaMapper "orange" and SPHEREx SDB-only "blue."
Confirm figure color-blind-safety. The lab usually uses viridis-style palettes; this one sounds like a standard dichromat-unsafe pair.

### m9. Table II `P(BF>3)` quoted as "87–96%" and "97%" — whence the uncertainty on a probability?
Should be a credible interval with stated quantiles, not an unlabeled range.

### m10. Eq. (6) Bayes-factor formula uses `L(fNL_obs | fNL = -35/8)` but the paper also uses an implicit Gaussian likelihood with fNL_obs drawn from `N(-35/8, σ)`. Specify the likelihood form explicitly in the equation environment.

---

## Nitpicks

- Line 26 abstract: "${\sim}\,5$--$5.5\sigma$" — the `{\sim}\,` before the range is unnecessary; use `\sim 5$--$5.5\sigma`.
- Line 66: "commutator factor" appears without forward-reference. One sentence earlier pointing to Appendix A would help.
- Line 96: the paragraph on the Wilson-Ewing w = -0.003 correction is a single 400-word paragraph with multiple nested claims. Break into three paragraphs.
- Line 129: "(i)~ℓ-space Fisher overlap ... (ii)~Monte Carlo injection recovery ... (iii)~a literature search confirming no prior quantification of this overlap exists." (iii) is not a validation step; it's a novelty claim. Move to the introduction or a footnote.
- Line 143: "(a) the bispectrum channel avoids ultra-large-scale mode dependence, (b) lower redshift (z ≈ 1.5) reduces GR projection contamination, (c) multi-tracer across redshift bins provides effective cosmic variance cancellation" — sentence is fine but (c) is the Seljak 2009 effect and should cite Seljak.
- Line 166: "Non-canonical single-field models (DBI, etc.) produce equilateral-shape f_NL, not local." — cite Chen+Huang+Kachru+Shiu 2007 or similar.
- Line 188: "we note that the delta-function prior for the bounce model maximally favors a parameter-free prediction." Good. Can you state the shrinkage of BF under a σ_theory = 0.5 Gaussian prior too, not just σ_theory = 1.0? Readers should see the sensitivity function.
- Line 228: bphi figure caption says "20 % prior ... ~4σ ... 50 % ... ~2σ. The bispectrum channel remains at ~6σ regardless." The 6σ bispectrum-channel number conflicts with the abstract's 5–5.5σ. Is this with or without template-correction r?
- Line 270: "These effects are expected to degrade the forecast significance by O(10–30%)" — "expected" is a soft word. Cite a reference or a calculation.
- Line 288: "the consistency relation ... c ∈ [-0.7, -10]" — a 14× range in the slope is not a "consistency relation," it's an un-constrained parameter. Soften the claim or tighten the range.
- Line 310: "A detection of fNL ≈ -4 by SPHEREx, if confirmed by any of these independent probes, would constitute overwhelming evidence." "Overwhelming" is not a quantitative word; reserve for 5σ+ joint significance.
- Line 330: NaMaster birefringence discussion belongs in Paper 1 or a separate ALP note, not Paper 2. It reads as out-of-scope for an fNL-forecast paper.
- `focused_paper_refs.bib` entry `Namikawa:2025` has `eprint = {2501.00000}` — placeholder eprint. Replace or drop.

---

## Proposed new tasks

| # | Task ID | Severity | Description | Owner |
|---|---|---|---|---|
| 1 | P2-FISHER-REBUILD | **BLOCKER** | Fix `fisher_forecast_spherex.py` normalization so σ(fNL) is in the [0.1, 20] range and `improvement_pct` is finite. Add a unit test that fails if σ < 0.01 on a canonical DESI-like config. | agent + pod |
| 2 | P2-FISHER-CONDNUM | **MAJOR** | Compute and log Fisher condition number per config; drop bins where κ > 10^8. | agent |
| 3 | P2-DIRECTIVE-NUMEROLOGY-KILL | **MAJOR** | If σ = 16.85/12.72/11.71 or +7.93 % are planned for any user-facing surface, first produce them from fixed code with a sanity check. Otherwise scrub them from CLAUDE.md, directives, and any downstream file. | agent |
| 4 | P2-BIAS-VAL-RERUN | **MAJOR** | Redo `step4_bias_validation` with (a) DESI footprint random catalog, (b) 5× randoms, (c) jackknife SEM, (d) no reliance on bins where `w_theta < 0`. Report jackknifed 1.58 × with error bar. | pod |
| 5 | P2-BAYES-MC-COMMIT | **MAJOR** | Commit the 600 k-realisation Bayesian MC driver + output CSV + RNG seed. Until committed, downgrade the abstract claim from "over 600,000 realisations" to "analytic Bayes factor with MC marginalisation over nuisance priors." | agent |
| 6 | P2-BAYES-PRIOR-TABLE | **MAJOR** | Add 3×3 prior-sensitivity table (bounce prior width × competitor prior width → BF) in §6.3. | agent |
| 7 | P2-R-FACTOR-HIST | MINOR | Add a histogram or 5-95 % percentile quote for the r-factor MC injection recovery. | agent |
| 8 | P2-GR-DOUBLE-COUNT-CHECK | MINOR | Footnote clarifying whether Heinrich+2023's σ = 0.7 is GR-free or GR-marginalized and whether Table III's σ_GR adds on top. | agent |
| 9 | P2-SPHEREX-TIMELINE-FIX | MINOR | Change "by 2027" → "by 2028 DR1" in any user-facing surface. | agent |
| 10 | P2-FNL-TRIPLE-ROLE-DEP | MINOR | If triple-role claim enters Paper 2, add a line on shared-parameter correlation across channels. | agent |
| 11 | P2-BIB-PLACEHOLDER-PURGE | NIT | `focused_paper_refs.bib` `Namikawa:2025` has placeholder eprint `2501.00000`. Replace or drop the reference. | agent |
| 12 | P2-DATE-PIN | NIT | Replace `\date{\today}` with the fixed submission date pre-arXiv-upload. | agent |

---

## Verdict

**Status: MAJOR REVISION.**

The paper's literary and analytic content — the template-correction factor r, the Wilson-Ewing consistency relation, the appendix on the Cai vs Li-Brandenberger convention — are defensible and are the paper's real contribution. The Fisher forecast it reports is imported from Heinrich+2023 and Schlegel+2022, which is fine as long as the import is stated honestly.

What is NOT fine:
1. The repo ships a broken Fisher code that returns σ = 0 and is linked from the paper's data-availability statement.
2. The SSOT and directive promote anomaly-forecast numbers (σ = 16.85 → 11.71, 7.93 % improvement, 2.28 × bias) that are not in the paper, not in the committed code, and partially contradicted by the bias-validation JSON (which reports 0.04 % improvement, not 7.93 %).
3. The 600 k Bayesian MC is claimed but the driver and output samples are uncommitted.
4. The Bayes-factor sensitivity to prior choice is a factor of 8× and is reported but under-emphasized.

**Before arXiv submission, items 1–4 above must be closed OR the corresponding claims removed from the paper and all downstream surfaces. In priority order: (P2-DIRECTIVE-NUMEROLOGY-KILL + P2-FISHER-REBUILD) > P2-BAYES-MC-COMMIT > P2-BIAS-VAL-RERUN > P2-BAYES-PRIOR-TABLE.**

The paper-level science is good. The infrastructure backing the paper-level science is worse than the paper itself suggests. Close the gap by improving the infrastructure, not by quoting the infrastructure's current broken output.

— skeptical-statistician-2026-04-18

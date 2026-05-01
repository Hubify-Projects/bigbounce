---
title: R42 cross-model peer review — synthesis & verdict (Gemini complete, OpenAI pending)
date: 2026-05-01 06:05 UTC
reviewer: Houston Method v2 / take-critiques-seriously protocol
gemini_model: gemini-3.1-pro-preview (gemini-2.0-pro-exp + gemini-1.5-pro both 404'd; introspected list_models and fell through to strongest available Pro tier)
openai_model: gpt-5 (still running adef16d827353816d at synthesis time)
basis: project-context/peer-reviews/r42-cross-model-2026-05-01/{gemini_p1,gemini_p2,gemini_p3,gemini_p4}_review.md
purpose: classify every Gemini finding into verified-valid / needs-domain-check / pushback (per `feedback_take_critiques_seriously.md`: full hard fix is default; pushback only with file/code/data citation)
---

## Headline verdicts (Gemini)

| Paper | Verdict | BLOCKERs | MAJOR | MINOR |
|---|---|---|---|---|
| P1 spin-torsion | REJECT | 3 | 2 | 2 |
| P2 f_NL forecast | REJECT | 3 | 2 | 2 |
| P3 anomaly catalog | MAJOR REVISION | 4 | 3 | 2 |
| P4 chirality catalog | MAJOR REVISION | 2 | 2 | 2 |

None of the four sailed through. Gemini broke the within-Anthropic echo chamber as
intended (see `feedback_cross_model_peer_review.md`). The pattern Gemini calls
out across all four: **tighter-than-official error bars and undocumented stats
in 3/4 papers**, plus claim-vs-derivation gaps where structural caveats undercut
headline claims.

## Verification grid

Status legend: VERIFIED-VALID = I confirmed against source; PUSHBACK = Gemini
misread context, citation provided; DOMAIN-CHECK = methodologically substantive,
defer to domain expert / next reviewer wave to confirm or refute; STRUCTURAL = a
framing or organizational fix, not contested.

### P1 — Spin-Torsion Cosmology

| ID | Gemini finding | My status | Citation / note |
|---|---|---|---|
| P1-CM-B1 | MCMC bait-and-switch — chains test ΛCDM+ΔNeff, not ECH | VERIFIED-VALID | `CLAUDE.md` §"key results": "MCMC verification: ΔNeff ≈ 0 in all datasets; H₀ = 67.68 (standard ΛCDM)". Paper's Bayes-factor headline rests on a proxy, not on torsion. Fix: reframe MCMC as ΛCDM-with-extra-radiation consistency check, not as ECH evidence; remove "evidence for ECH" framing from abstract / Table III. |
| P1-CM-B2 | Synthetic PTA Bayes factor B≈302 from synthetic NANOGrav data | VERIFIED-VALID | Methodologically circular: fitting your model to a realization drawn from a competitor's best-fit template gives no Bayesian information. Fix: delete §XV.C synthetic-data Bayes factor; if PTA evidence is wanted, use Agazie et al. 2023 free-spectrum posteriors. |
| P1-CM-B3 | "Disconnected predictions" — ALP & f_NL admittedly mechanism-independent, yet labeled as ECH "predictions" | STRUCTURAL | Already disclosed inside the paper. Fix: retitle/reframe as a structural-closure no-go theorem with separate phenomenological appendices; remove "unified" framing from abstract. Aligns with our existing R31 reframe direction (per `1dd2735` cross-paper decoupling commit). |
| P1-CM-M1 | Dimensional scaling ansatz for ECH→Λ is parametric guess, not a derivation | STRUCTURAL | Disclosed in §II.C; promote disclosure into abstract. |
| P1-CM-M2 | NaMaster pipeline-recovery (SNR 20.32) co-listed with real Planck/ACT detections in Table I | VERIFIED-VALID | Pipeline-validation result and observational result should not be in the same evidence row. Move NaMaster recovery to methodology appendix. |
| P1-CM-m1 | Savage-Dickey known-biased estimator still quoted as headline | VERIFIED-VALID | Paper itself flags r=−0.89 correlation breaks Savage-Dickey. Fix: switch to nested sampling or AIC/BIC headline; relegate biased estimator to comparison footnote. |

### P2 — f_NL Forecast (matter bounce)

| ID | Gemini finding | My status | Citation / note |
|---|---|---|---|
| P2-CM-B1 | "PDF hallucination" — Gold+Silver QSO pipeline (5,384 candidates, Landy-Szalay 1.58×) absent from PDF | **PUSHBACK** | Paper title (`02_full_draft.tex` L19): "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook". Abstract (L29) explicitly scopes to forecasts, template overlap, and Bayes-factor model comparison — NOT to a QSO clustering pipeline. The Gold+Silver result lives in `pipelines/p1_highz_tracers/` and is referenced from P3 §VI.C limitation `(iv)` (`paper3_draft.tex` L568) as a calibration check on α=0.15, not as a P2 result. Gemini conflated CLAUDE.md program-context (which spans all 4 papers + pipelines) with this paper's scope. The PDF is internally consistent as a forecast paper. **However**, this exposes a real risk: future cross-model reviewers will keep making the same mistake unless the program-context block we hand to reviewers is paper-scoped, not program-scoped. Fix: add a "Scope of this manuscript" sentence to the cross-model prompt template, not to the PDF. |
| P2-CM-B2 | Multiplicative r-factor projection invalid against full multi-tracer covariance | DOMAIN-CHECK | Methodologically dense. The argument is that the bispectrum covariance includes b_2, b_{s²}, RSDs, tracer-specific shot noise — these don't commute with the simple primordial r overlap. Worth taking seriously: this is a real concern. Fix path: either compute the full Fisher matrix with the exact bounce shape inside the multi-tracer covariance, or add a clear caveat that "noise-weighted r" is a fast approximation, not a covariance-correct projection. |
| P2-CM-B3 | "Convention" vs "physics error" framing for Cai vs Li-Brandenberger | VERIFIED-VALID | Appendix A.1 itself shows the missing time-ordering in Li-Brandenberger. A missing in-in time-ordering changes the expectation by a factor of 2 — that is a calculation error, not a normalization choice. Fix: remove "dual-norm" framing from abstract / §II / Appendix A; state plainly that Li-Brandenberger is incomplete; keep Table IV only as an explicit error-vs-correct comparison. |
| P2-CM-M1 | Delta-function prior on bounce f_NL inflates Bayes factor vs broad-uniform inflation prior | VERIFIED-VALID | Paper §II.C admits 1–8% ε-correction uncertainty; a delta prior is therefore physically unjustified. Fix: present σ_theory = 0.5, 1.0, 2.0 prior sweep as PRIMARY in abstract & Table II; relegate delta-prior column as theoretical-upper-bound comparison only. |
| P2-CM-M2 | "Bispectrum nearly independent of b_phi" claim is false | DOMAIN-CHECK | f_NL enters tree-level galaxy bispectrum via Δb(k) ∝ f_NL b_phi cross-terms. Likely correct critique. Fix: cite Heinrich et al. 2023 b_phi treatment explicitly (likely fix-by-universality) and add caveat that relaxing b_phi degrades the 5.25σ headline. |

### P3 — Anomaly Catalog

| ID | Gemini finding | My status | Citation / note |
|---|---|---|---|
| P3-CM-B1 | Title says "319,443 Anomalies" but Table I primary row is Path-C unique 378,280 | VERIFIED-VALID | `paper3_draft.tex` L44 title: "319{,}443 Anomalies and Native-Trained Novelty Rates"; L200 Table I cross-transfer baseline 319,443; L201 Path-C unique 378,280 bolded as "primary". Title carries the deprecated cross-transfer total while paper itself says Path-C is primary. Fix: retitle to use 378,280 OR use a phrasing that covers both ("...from 37.3 million spectra, 378,280 unique anomalous sources after seven-survey deduplication"). Update abstract simultaneously. |
| P3-CM-B2 | Redshift validity for anomaly-selected tracers — Redrock fails on OOD spectra | DOMAIN-CHECK | Real concern: the very property that makes a spectrum anomalous (unusual continuum / shifted lines) is the property that breaks template-fit redshift pipelines. Fix path: visual inspection of a representative S>5 subsample, OR cross-match against known high-z spec catalogs, OR remove the f_NL forecast from this paper and move it to P2. |
| P3-CM-B3 | PTA γ = 3.20 ± 0.42 tighter than Agazie et al. 2023 official 3.2 ± 0.6, with zero MCMC documentation | VERIFIED-VALID | `paper3_draft.tex` L542: "γ = 3.20 ± 0.42 (GPU MCMC, combined PTA)" — no likelihood spec, no priors, no RN/DM models, no R-hat, no posterior figure. Paper §VI calls it "preliminary". Fix: either full MCMC documentation appendix (likelihood, priors, RN model, R-hat, ESS, posterior plot) OR remove §V.A entirely and revert to citing Agazie 2023's official value. |
| P3-CM-B4 | BigAE-vs-IsolationForest validation mismatch for eROSITA & Gaia | VERIFIED-VALID | `paper3_draft.tex` L583 (caveat (v)): explicitly says "we refit fresh IsolationForests" for the injection-recovery, while §III.E and §III.H state the eROSITA & Gaia anomaly catalogs were generated by 16-d BigAE latent. The IF refit is a diagnostic on the same feature space, but it is NOT validating the BigAE rankings used to build the catalog. Fix: re-run injection-recovery on the actual BigAE checkpoints used to score the eROSITA & Gaia catalogs; OR explicitly relabel the IF result as a methodology-cross-check rather than a validation of the released catalogs. |
| P3-CM-M1 | f_NL Fisher forecast missing systematics marginalization | DOMAIN-CHECK | Real concern: airmass / seeing / focal-plane systematics produce 1/k² scale-dependent clustering that mimics f_NL. LAMOST 98% blue-excess is exactly this class of contamination. Fix: add quantitative marginalization over imaging/spectroscopic systematics templates, OR explicitly state forecast is conditional on zero systematic contamination. |
| P3-CM-M2 | α=0.15 fiducial enhancement uncalibrated; 6.1% headline depends on it | VERIFIED-VALID | Paper §VI.D itself admits α=0.15 is "broadly consistent" but sample (1,122) "too small to be definitive". Fix: present σ(f_NL) improvement as a function of α (already in App C per §VI.D) in main text; demote 6.1% from headline to "α=0.15 reference value"; add primary-limitation flag to abstract. |
| P3-CM-M3 | ACT DR6 quarantined but still in Table I and §III.G | STRUCTURAL | Easy cut. Drop ACT row from Table I, move §III.G content to a "lessons learned" appendix or omit entirely. Keep only as Path-C before/after artifact reference. |
| P3-CM-m1 | SIMBAD-unmatched 58.8% headline misleading vs 17.8% genuine novelty | STRUCTURAL | Already partially addressed in §VI.D ("Anomalous Sources" not "Uncataloged Objects" in title). Push 17.8% as primary metric in abstract; demote 58.8% to a methodology footnote. |

### P4 — Chirality Catalog

| ID | Gemini finding | My status | Citation / note |
|---|---|---|---|
| P4-CM-B1 | NaMaster deconvolution math impossible if MC nulls are masked; Footnote 5 admits wrong N (N_total vs N_spiral) in shot-noise subtraction | DOMAIN-CHECK | If Footnote 5 really admits N_total vs N_spiral mix-up, then Gemini's logic is correct: a linear deconvolution matrix cannot turn a 2.75σ outlier into −0.12σ unless the variance is dominated by off-diagonal coupling, which it isn't for white shot noise. Fix: recompute pseudo-C_ℓ and deconvolved C_ℓ with N_spiral consistent across data and 1,000 MC nulls; report empirical p-value from MC ensemble; remove "mode coupling inflates the signal" narrative if the bug is the actual cause. **HIGH PRIORITY** — this is the load-bearing null-result claim of the paper. |
| P4-CM-B2 | Z₂ TTA does not enforce rotational equivariance; spatially varying PSF ellipticity could project monopole into spurious dipole | DOMAIN-CHECK | Plausible mechanism. Fix: cross-correlate Catalog C CW-fraction map directly against DESI Legacy PSF ellipticity and position-angle maps; show CW fraction is independent of local survey orientation to <0.1%. |
| P4-CM-M1 | Catalog B circular calibration against CE-ResNet | STRUCTURAL | Calibrate Catalog B against independent Galaxy Zoo 1 labels (already cross-matched per §II.B), or deprecate Catalog B for cosmological parity tests. |
| P4-CM-M2 | Edge-on TTA assumes rotational invariance | DOMAIN-CHECK | Fix: evaluate equivariant CW fraction for the b/a < 0.3 subsample directly; if it deviates from 0.5000, TTA is failing on rotated edge-ons and leakage must be quantified. |
| P4-CM-m1 | 0.2% sensitivity floor below 0.26% systematic monopole | VERIFIED-VALID | Logically inconsistent unless systematic is proven dipole-orthogonal. Fix: reword sensitivity claim as Poisson-statistical limit only; explicitly state systematic-inclusive limit is ≥0.26%. |
| P4-CM-m2 | Bonferroni on 650 correlated hemispheres over-conservative | DOMAIN-CHECK | Use empirical MC threshold for max-over-directions, or Euler characteristic for Gaussian random fields on a sphere. Real but minor. |

## What's missing from the OpenAI half

- adef16d827353816d still running at synthesis time
- openai_p1_review.md exists with header but empty body — possibly truncated mid-write or output capture failure; will revisit when agent reports completion
- openai_p2_review.md is partial (BLOCKERs only, no MAJOR/MINOR section yet)
- p3 / p4 reviews not yet written

OpenAI partial findings already on disk that need to be folded in:
- P2-OA-B1: scale-dependent bias formula in Eq. 3 missing 1/k² (matches dimensional analysis critique against text)
- P2-OA-B2: Bayes factor inconsistencies across abstract / §VI.C / Table II / Table III
- P2-OA-B3: r > 1 reported despite Eq. 4 claiming r ≤ 1 (super-squeezed coefficient set leaked into scan)
- P2-OA-B4: code release pinned at v1.7.0 while manuscript is v1.7.5

The P2-OA findings are mostly orthogonal to Gemini's P2 findings and add real value; the v1.7.0 vs v1.7.5 reproducibility gap is fixable in 5 minutes (`git tag v1.7.5 && git push --tags`).

## Pattern across all 4 papers

Three load-bearing classes of cross-model finding:

1. **Tighter-than-official error bars / undocumented MCMC** — P1 (Savage-Dickey on bias-flagged correlation), P3 (PTA black-box). Pattern: we report precision the underlying chains/priors don't actually support.
2. **Claim vs derivation gap** — P1 (ECH "predicts" things admittedly mechanism-independent), P2 (delta prior + r-factor projection inflate Bayes factor and σ), P3 (forecast assumes systematics-free + uncalibrated α), P4 (sensitivity floor below systematic floor). Pattern: structural caveats inside the paper undercut the headline number.
3. **Validation-vs-product mismatch** — P3 (BigAE catalogs validated by IF refit), P4 (NaMaster N_spiral bug + Z₂-TTA-only equivariance). Pattern: the artifact tested is not the artifact released.

This is exactly the class of finding `feedback_cross_model_peer_review.md` warned would be invisible inside an Anthropic-only review pipeline. Default disposition per `feedback_take_critiques_seriously.md` is FULL HARD FIX; pushback only with citation, and the only PUSHBACK I'm willing to issue is **P2-CM-B1** (paper-scope mismatch with program-context) which has a clean file/abstract citation.

## Next-action queue (Houston Method v2: each new finding becomes a queue row, not a future-work bullet)

R42-cross-model-Wave-10 candidate rows for `SSOT/queue.md`:

```
| P1 | CM-B1 | reframe MCMC §III.D / VII.B / Table III as ΛCDM+ΔNeff consistency, NOT ECH evidence; abstract drop "evidence for ECH" |
| P1 | CM-B2 | delete §XV.C synthetic-PTA Bayes factor; if needed, replace with citation to Agazie 2023 official value |
| P1 | CM-B3 | reframe paper as structural-closure no-go theorem; demote ALP & f_NL to phenomenological appendices |
| P1 | CM-M1 | promote ECH→Λ dimensional-ansatz disclosure into abstract |
| P1 | CM-M2 | move NaMaster pipeline-validation (SNR 20.32) from Table I evidence row to methodology appendix |
| P1 | CM-m1 | switch headline Bayes factor to nested-sampling or AIC/BIC; demote Savage-Dickey to footnote |
| P2 | CM-B2 | full Fisher matrix with exact bounce shape inside multi-tracer galaxy bispectrum covariance, OR add explicit "noise-weighted r is approximation" caveat |
| P2 | CM-B3 | reframe Cai vs Li-Brandenberger as algebra error not convention; remove "dual-norm" framing |
| P2 | CM-M1 | promote σ_theory={0.5,1.0,2.0} prior sweep as PRIMARY Bayes factor; demote delta-prior to upper-bound comparison |
| P2 | CM-M2 | drop "bispectrum independent of b_phi" claim; cite Heinrich 2023 b_phi treatment explicitly |
| P2 | OA-B1 | fix Eq. 3 scale-dependent bias formula to include 1/k² (M(k,z) = 2 k² T(k) D(z) / (3 Ω_m H₀²)) |
| P2 | OA-B2 | reconcile Bayes factor numbers across abstract / §VI.C text / Table II / Table III; single self-consistent table |
| P2 | OA-B3 | enforce r ≤ 1 physical constraint; either restrict null-space scan to physical coefficients or fix overlap implementation |
| P2 | OA-B4 | tag repo at v1.7.5 with all scripts/configs for current manuscript; OR roll manuscript claims back to v1.7.0 outputs |
| P3 | CM-B1 | retitle paper to use Path-C unique 378,280 OR dual phrasing; sync abstract and headline metrics |
| P3 | CM-B2 | redshift validation for S>5 anomaly subsample (visual inspection + high-z catalog cross-match) OR move f_NL forecast to P2 |
| P3 | CM-B3 | full MCMC appendix (likelihood, priors, RN/DM noise model, R-hat, ESS, posterior plot) OR delete §V.A and revert to Agazie 2023 |
| P3 | CM-B4 | re-run injection-recovery on actual BigAE checkpoints for eROSITA & Gaia OR explicitly relabel IF refit as methodology cross-check |
| P3 | CM-M1 | add quantitative systematics marginalization to f_NL Fisher OR explicit zero-systematic caveat with abstract flag |
| P3 | CM-M2 | demote 6.1% headline; present σ(f_NL) as function of α; flag uncalibrated α as primary limitation in abstract |
| P3 | CM-M3 | drop ACT DR6 from Table I and §III.G; preserve only as Path-C before/after reference |
| P3 | CM-m1 | promote 17.8% genuine-novelty fraction as primary; demote 58.8% SIMBAD-unmatched to methodology footnote |
| P4 | CM-B1 | recompute pseudo-C_ℓ and deconvolved C_ℓ with N_spiral consistent across data + 1000 MC nulls; report empirical p-value; remove mode-coupling-inflates-signal narrative if the N_spiral bug is the actual cause |
| P4 | CM-B2 | cross-correlate Catalog C CW-fraction map vs DESI Legacy PSF ellipticity + PA maps; prove CW independence to <0.1% |
| P4 | CM-M1 | recalibrate Catalog B against independent Galaxy Zoo 1 labels OR deprecate Catalog B for cosmological parity tests |
| P4 | CM-M2 | evaluate equivariant CW fraction for b/a<0.3 subsample directly; quantify TTA-on-rotated-edge-on leakage |
| P4 | CM-m1 | reword 0.2% sensitivity floor as Poisson-statistical limit only; state systematic-inclusive limit ≥0.26% |
| P4 | CM-m2 | replace Bonferroni-650 with empirical MC max-over-directions threshold OR Euler-characteristic Gaussian-random-fields-on-sphere |
```

(P2-CM-B1 is the single PUSHBACK, not queued. Cross-model prompt template gets a "Scope of this manuscript" sentence so future reviewers don't repeat the conflation.)

## Recommendation for Houston

**Highest-leverage trio** (closes the most adversarial review surface area for the least effort):
1. P1-CM-B1 + P1-CM-B3 + P1-CM-M2 — reframe P1 as structural closure + ΛCDM+Neff consistency, not ECH evidence. Touches abstract, §III.D, §VII.B, Table I, Table III. Mostly text edits; no new compute. **The "unified framework" framing is the most attackable surface across all four cross-model reviewers.**
2. P3-CM-B1 + P3-CM-M3 — retitle to Path-C 378,280, drop ACT row. Single restamp, no new compute. Closes the most reviewer-visible inconsistency on P3.
3. P4-CM-B1 — N_spiral bug fix in NaMaster shot-noise subtraction. If Footnote 5 really admits this, the recompute is a few hours of GPU time and could turn the central P4 statistical claim from "fragile null" to "rigorously bounded null".

**Compute-heavy items** (queue but don't block on Wave 10 first text round):
- P3-CM-B3 full MCMC docs (or pivot to citation)
- P3-CM-B4 BigAE-on-eROSITA+Gaia injection-recovery
- P4-CM-B1 N_spiral recompute (fast on H200)
- P4-CM-B2 PSF cross-correlation (depends on DESI Legacy PSF map availability)

**Wait for OpenAI to land** before final Wave-10 close — they will likely add 4-6 more findings, especially on P3 and P4.

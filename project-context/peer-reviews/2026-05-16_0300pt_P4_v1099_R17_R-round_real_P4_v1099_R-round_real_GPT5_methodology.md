# P4_v1099 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0300pt_P4_v1099_R17_R-round_real
**Wall time**: 126.3s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=83353, completion=6463, reasoning=4660, total=89816

---

## PAPER-GPT-B1 — BLOCKER — MASTER headline is not a same-estimator leakage closure

| Audit item | Evidence | Verdict |
|---|---|---|
| Same-map/same-mask closure? | Pre-MASTER leakage uses un-monopole-subtracted CW-fraction map on canonical mask; headline post-MASTER uses monopole-subtracted CW-deficit map on larger subsample mask. | Not a valid “MASTER removes leakage” closure. |
| Monopole subtraction defined correctly? | NaMaster appendix says headline field is `f_CW - 0.5`; with global `f_CW=0.4974`, this leaves a nonzero masked monopole. | Methodologically wrong/inconsistent. |
| Same-mask result null? | Canonical-mask direct MC gives `+1.85σ`, `p=15/500=0.030`, not the headline `-0.12σ`. | Headline is mask-choice dependent. |

**Location:** Abstract; Secs. `Dipole Analysis`, `Monopole+Mask Leakage Generative Null`, `Conclusions`, `NaMaster MASTER configuration`.

**Issue:** The claimed pre/post-MASTER collapse is not demonstrated on identical inputs; the map, mask, monopole treatment, and null all change. Also, subtracting `0.5` is not sample-mean monopole removal, and omitting `ℓ=0` from the coupling matrix while a residual monopole remains invalidates the leakage accounting.

**Fix:** Rerun a single declared data vector on the same mask pre/post MASTER: subtract the weighted mask mean or include `ℓ=0` in the coupling model. Make the canonical-mask direct-MC result the main same-footprint result unless a preregistered, quantitative mask-selection justification is added.

## PAPER-GPT-B2 — BLOCKER — Same full-catalog dipole is reported as both null and `4.31σ`

| Audit item | Evidence | Verdict |
|---|---|---|
| Headline real-space dipole | Sec. `Dipole Analysis`: `0.43σ`, `p=0.30`. | Null. |
| Alternative full Catalog C real-space-like estimator | Table `face_on`: Catalog C full `+4.31σ (p=0.001)` under monopole-preserving null. | Detection-level discrepancy. |
| Reconciliation supplied? | Text says estimator definition/null-sample variance. | Not quantitatively credible. |

**Location:** Sec. `Dipole Analysis`; Table `High-confidence-spiral robustness rerun`; Sec. `Edge-On Galaxy Contamination`.

**Issue:** A factor-10 significance discrepancy on the same Catalog C full sample cannot be dismissed as “estimator definition” without showing both estimators’ null distributions, weights, covariance, and response to injected dipoles. This directly undermines the headline non-detection.

**Fix:** Define both dipole estimators algebraically, run them on the same MC ensembles and injected skies, and show calibration/consistency. Until then, do not use the `0.43σ` estimator as load-bearing.

## PAPER-GPT-M1 — MAJOR — Injection-recovery sensitivity is overclaimed as systematic-inclusive/full-catalog

| Audit item | Evidence | Verdict |
|---|---|---|
| Empirical sweep sample | `N=471,049` HC-spiral subsample. | Not full `3.2M` catalog. |
| Injection mechanism | Synthetic relabeling with `p_CW=1/2(1+A n·n_inj)`. | Bypasses image classifier/systematics. |
| Claimed use | Abstract/conclusions call `A≈0.75%` empirical/systematic-inclusive sensitivity for catalog-scale result. | Overclaim. |

**Location:** Abstract; Sec. `Sensitivity Floor`; Table `mc_injection`; Conclusions item 1.

**Issue:** The `0.75%` threshold is an algorithmic recovery threshold on a high-confidence subsample under synthetic relabeling. It does not propagate classifier confusion, rotational TTA uncertainty, morphology-dependent label bias, depth/PSF label correlations, or the full Catalog C mask/noise.

**Fix:** Reframe as “HC-subsample injection threshold.” Either run the injection sweep on full Catalog C with probability/label-noise/systematics preserved, or remove “systematic-inclusive” and full-catalog sensitivity language.

## PAPER-GPT-M2 — MAJOR — Hemisphere look-elsewhere calibration is internally inconsistent

| Audit item | Evidence | Verdict |
|---|---|---|
| Analytic LEE | Bonferroni/BH across ~650 directions gives `<1σ`. | Null. |
| Direct MC LEE | 0/10,000 exceedances reported as `p_LEE≤1e-4`, `>3.7σ`. | Rejection. |
| MC interpretation | Text says true p “may be arbitrarily smaller” and bounded by MC size. | Misstates MC uncertainty. |

**Location:** Sec. `Hemisphere Asymmetry`; Fig. `hemisphere`; Sec. `hemisphere_disc`.

**Issue:** Zero exceedances in 10,000 null draws does not establish a true tail probability `≤1e-4`; it gives a finite-resolution/rank estimate with uncertainty. The paper mixes different hemisphere statistics/amplitude conventions and incompatible nulls, then alternates between “consistent with null” and “rejects random-label null.”

**Fix:** Declare one hemisphere statistic and one primary null. Report `(k+1)/(N+1)` with a confidence interval or run more MC; separate random-label rejection from a systematics-preserving null and stop quoting the analytic Bonferroni result as a comparable correction.

## PAPER-GPT-M3 — MAJOR — Low-ℓ power-spectrum significances lack a valid covariance treatment

| Audit item | Evidence | Verdict |
|---|---|---|
| Per-bin z-scores | Table reports `+6.097σ`, `+2–3σ` bandpowers; null means hidden. | Underreported calibration. |
| Joint statistic | `χ²/dof=161.2/38` quoted. | No covariance shown. |
| MC tail support | `+6σ` claims from 1000 MC; empirical p=0 possible. | Tail not calibrated. |

**Location:** Table `Angular power spectrum`; Sec. `Dipole Analysis`; NaMaster appendix.

**Issue:** MASTER bandpowers on a cut sky are correlated; a diagonal per-bin `z` and diagonal `χ²/dof` are not valid without the full null covariance. Negative decoupled “power” entries and hidden null means further obscure what is being tested.

**Fix:** Publish null means and the full covariance matrix, compute multivariate χ²/rank p-values with that covariance, and avoid `6σ` tail language unless supported by enough MC or a validated parametric tail model.

## PAPER-GPT-m1 — minor — v1.0.99 propagation-tail regressions remain on public surface

| Audit item | Evidence | Verdict |
|---|---|---|
| Stale release tag | Footnote `fn:repro_artifacts` and Data Availability cite `paper4-v1.0.98`. | Stale tag remains. |
| `f_sky` drift | Tables/captions still show `0.494`, `0.491`, `0.4928` for canonical contexts despite `0.49005` target. | Not globally closed. |
| Parity wording | Body still says “primordial parity-violating signal” / “cosmological parity violation” for the dipole channel. | Some stale framing remains. |
| HC rename | `HC-broad-0.6` mostly appears correct. | No obvious stale HC-spiral-0.6 blocker. |

**Location:** `fn:repro_artifacts`; Data Availability; Tables `headline_summary`, `monopole_mask_null`, `l1_estimators`; Secs. `wtheta`, `Motloch`, Conclusions.

**Issue:** The public-surface cleanup is incomplete: stale version tags and canonical `f_sky` values remain, and some body prose still describes the dipole as parity-violating rather than isotropy-breaking axial-vector.

**Fix:** Global grep/replace before external review: update release tags to `paper4-v1.0.99` or current successor, normalize canonical `f_sky` to `0.49005` where applicable, and replace residual dipole-channel parity language with “isotropy-breaking axial-vector chirality dipole.”

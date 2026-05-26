# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-phase2-verify_P4_v1_0_131
**Wall time**: 147.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=100382, completion=7852, reasoning=6551, total=108234

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Abstract; Secs. `Declared Analysis Hierarchy`, `Dipole Analysis`, `Monopole+Mask Leakage`, `Conclusions`; Tables `data_vectors`, `headline_summary`, `l1_estimators`.

**Issue:** The headline `-0.12σ` subsample-mask null and the canonical-mask `+3.64` residual are not the same data vector: mask, `f_sky`, monopole subtraction, weighting, null model, and even map definition differ. The manuscript still states/implies that MASTER “removes” the leakage and that the canonical residual is resolved, but the v1.0.131 10k post-MASTER monopole-only null says pure monopole leakage explains only ~12% of canonical `C1`; the remaining ~88% is unresolved without the pending systematics-preserving null / joint nuisance model.

**Fix:** Either perform the joint nuisance-marginalized/systematics-preserving canonical-mask analysis, or demote the conclusion to “null for one declared subsample-mask estimator; canonical low-ell residual unresolved/systematics-suspected.” Do not compare the canonical pre/post values to the subsample result as a like-for-like MASTER collapse.

## PAPER-GPT-B2 — MAJOR

**Section:** Table `data_vectors`; Table `headline_summary`; footnote `fn:mc_count`; Table `mc_injection`; Sec. `Sensitivity`.

**Issue:** The new data-vector table did not land cleanly. Examples: real-space dipole row says `N_MC=500` while the text says `10,000`; injection row says `500 + 100/A` while the sensitivity paragraph says `N_MC,null=1000`; Table `mc_injection` caption says `N_MC,null=500`; row (v) says “10000 in v1.0.130 ext” although the 10k run is v1.0.131; canonical mask `f_sky/N_pix` values vary between `0.49005/24087`, `0.494/24269`, and `0.491`.

**Fix:** Make one authoritative table with, for every statistic, exact map, mask, `f_sky`, `N_pix`, `N_gal`, null class, `N_MC`, rank convention, and artifact. Then propagate those values consistently through captions, abstract, and conclusions.

## PAPER-GPT-B3 — MAJOR

**Section:** Abstract; Table `headline_summary` footnote b; Secs. `Dipole Analysis`, `Conclusions`, `Signal-Hunt Diagnostics`.

**Issue:** Statistical significance is over-quoted via moment-z. The canonical direct-MC residual is repeatedly called `+3.64σ`, but its stated empirical-rank value is `p_MC=15/500=0.030`, i.e. not a Gaussian `3.64σ` detection. Similarly, the `-2.89σ` cross-spectrum is described as “directly confirmed” despite being a single-multipole diagnostic with trials correction only at ~2.3σ.

**Fix:** Use empirical p-values as the primary significances whenever the MC null is non-Gaussian/heavy-tailed; label moment-z explicitly as diagnostic only. Replace “confirmed” / “directly confirmed” with “suggestive” unless a systematics-preserving, trial-corrected likelihood test is supplied.

## PAPER-GPT-B4 — MAJOR

**Section:** Table `headline_summary` footnote c; Table `data_vectors` row vi; Sec. `TTA`.

**Issue:** The 21.4% hard-label flip uncertainty propagation is arithmetically wrong. “Doubling the per-bin Poisson σ” cannot produce a `1.21×` widening, and an independent flip probability `q=0.214` implies either signal attenuation `D=1-2q=0.572` with corrected-amplitude σ inflation `1/D≈1.75`, or a different uncorrected-label variance model that must be derived/MC-calibrated.

**Fix:** Recompute every hard-label diagnostic uncertainty by either explicit D4 stochastic resampling or a stated analytic flip model. Remove the `1.21×` claim unless it is derived from the actual estimator covariance.

## PAPER-GPT-B5 — MAJOR

**Section:** Sec. `Sensitivity`; Table `mc_injection`; Conclusions item 1 and falsification criterion.

**Issue:** The `0.75%` “empirical sensitivity/falsification” threshold is from a strict-HC hard-label subsample (`N≈471k`) with a per-pixel-shuffle null that destroys depth/PSF/morphology covariance. It is then used as a catalog-level/full-pipeline sensitivity and sometimes called “systematic-inclusive,” despite the primary cosmology estimator being a soft `A_p` map on the 3.2M catalog and despite full-catalog injection-recovery being listed as pending.

**Fix:** State the `0.75%` number only as “strict-HC hard-label per-pixel-shuffle 50%-recovery threshold.” Do not use it as full-catalog/systematics-inclusive sensitivity or falsification criterion until the full-catalog soft-map injection with a systematics-preserving null is run.

## PAPER-GPT-B6 — MAJOR

**Section:** Introduction; Sec. `Comparison with Previous Work`; Conclusions item 2.

**Issue:** The Shamir closure failed. The paper alternates between Shamir 2022 being `~1.3M` input galaxies, `~2e5` post-Ganalyzer spirals, and “nearly `1.3M` spiral galaxies”; it also says `3.2M` is `~2.5×` larger than `~200k`, which is wrong by a factor of ~6.4 (`3.2M/0.2M≈16`). The “factor `~6–12` smaller” amplitude framing also remains despite the stated scope narrowing.

**Fix:** Pick one verified comparator per Shamir paper and use correct arithmetic. If no matched Ganalyzer reanalysis is performed, restrict the text to qualitative amplitude disagreement under the present pipeline and remove exclusion-style ratio rhetoric.

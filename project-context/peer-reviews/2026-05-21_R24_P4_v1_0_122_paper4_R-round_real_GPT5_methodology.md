# paper4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P4_v1_0_122
**Wall time**: 98.3s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=94833, completion=4947, reasoning=3896, total=99780

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Sec. IX.H “Edge-On Galaxy Contamination”, Table `face_on`, reconciliation paragraph  
**Issue:** Catalog C full gives a weighted-LSQ dipole of `+4.31σ (p=0.001)` on the same nominal data for which the headline real-space dipole is `+0.43σ (p=0.30)`. The stated explanation (“estimator definition” / “null-sample variance”) is not a reconciliation of a factor-10 significance discrepancy; it makes the primary null estimator look cherry-picked.  
**Fix:** Run both estimators on identical map, mask, monopole treatment, weights, and MC null; identify the bug or systematic causing `+4.31σ`. Until resolved, remove or qualify the headline “real-space dipole null.”

## PAPER-GPT-M1 — MAJOR

**Section:** Abstract; Sec. IV “Dipole Analysis”; Sec. IV.B “Monopole+Mask Leakage”; Conclusions  
**Issue:** The paper repeatedly says MASTER “removes” monopole-mask leakage via `+6.48σ → -0.122σ`, but this comparison changes field definition, monopole subtraction, and mask (`f_sky≈0.49` canonical vs `0.659` subsample). The like-for-like canonical post-MASTER result remains `+3.64σ`, and the post-MASTER monopole-only null explains only `12%` of that residual.  
**Fix:** Stop presenting this as MASTER-alone removal. Provide a same-field/same-mask ablation separating monopole subtraction, mask change, and MASTER inversion; state the load-bearing result only as a subsample-mask null.

## PAPER-GPT-M2 — MAJOR

**Section:** Abstract; Table III caption; Conclusions “Canonical-N MASTER”  
**Issue:** The canonical-mask `+3.64σ` is a moment-z under a non-Gaussian 500-MC null, while the empirical-rank calibration is `p_MC=15/500=0.030`; treating `+3.64σ` as a Gaussian-tail significance overstates the evidence. The manuscript alternates between calibrated p-value language and detection-like sigma language.  
**Fix:** Report this everywhere as `moment-z=+3.64, empirical p=0.030`, not as a Gaussian `3.64σ` detection/residual significance. If a sigma-equivalent is needed, derive it from the empirical p-value or validate Gaussian tails with much larger MC.

## PAPER-GPT-M3 — MAJOR

**Section:** Abstract; Sec. IV.B multi-null battery; Sec. IV.C signal-hunt summary  
**Issue:** Interpretation (ii) is described as “directly confirmed” by the cross-spectrum, but the evidence is only suggestive: `ℓ=1` cross-spectrum is `-1.53σ`, `ℓ=2` is `-2.89σ` before trials and only ~`2.3σ` after the stated 5-multipole correction. No nuisance-marginalized model comparison separates primordial dipole from depth/PSF/morphology templates.  
**Fix:** Replace “confirmed/directly confirmed” with “favored/suggestive.” Add an explicit statement that no likelihood-level primordial-dipole + systematics model has been fit or marginalized.

## PAPER-GPT-M4 — MAJOR

**Section:** Sec. IX.J “Sensitivity Floor”; Conclusions item 1 and “Falsification criterion”  
**Issue:** The empirical `0.75%` threshold is called “systematic-inclusive,” but the text also admits the per-pixel-shuffle null destroys depth/PSF/morphology covariance and is not fully systematics-preserving. The paper further reports pipeline-choice thresholds spanning `0.75%–1.5%`, yet uses `0.75%` as a hard falsification floor.  
**Fix:** Call `0.75%` a present-pipeline per-pixel-shuffle operational threshold, not systematic-inclusive. Either use the conservative `1.5%` stress-test value in falsification language or quote the full `[0.75%,1.5%]` range pending a systematics-preserving injection suite.

## PAPER-GPT-M5 — MAJOR

**Section:** Conclusions, first paragraph; Table I footnote b; Sec. IV.B v1.0.121 closure  
**Issue:** The Conclusions still state “post-MASTER monopole-only realizations were not computed,” directly contradicting Table I footnote b and Sec. IV.B, which report the v1.0.121 `N=500` MASTER-decoupled monopole-only null (`12%` of data, empirical `p=0.006`). This is a stale load-bearing statement.  
**Fix:** Delete the stale sentence and replace it with the computed post-MASTER monopole-only result, including the `12%` contribution and the conclusion that additional systematics beyond pure monopole leakage are required.

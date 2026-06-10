# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-20_1010pt_P4_v1_0_121_R22
**Wall time**: 106.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=93369, completion=5942, reasoning=4834, total=99311

---

## PAPER-GPT-B1 — BLOCKER

- **Section:** Abstract; §III.A; §IX.J Sensitivity; Table `tab:mc_injection`; Conclusions falsification criterion.
- **Issue:** The manuscript repeatedly states the strict HC-spiral injection floor as **50%-recovery at 3σ = 0.75%**, but the round closure says the **strict-HC=0.9 sweep closes at 1.5%**. This contaminates the abstract sensitivity claim, the falsification criterion, and all “systematic-inclusive 0.75%” language.
- **Fix:** Align the artifact/predicate: if the quoted sample is strict-HC=0.9 / `N=471,049`, update the threshold to **1.5%** everywhere; if 0.75% belongs to another cut, rename the cut and stop using it as the strict-HC falsification floor.

## PAPER-GPT-B2 — BLOCKER

- **Section:** Table `tab:headline_summary` footnote b; Conclusions “Headline finding”; §IV.C v1.0.121 closure paragraph.
- **Issue:** The paper says the post-MASTER monopole-only null was “not computed,” while §IV.C later reports the v1.0.121 computed result: data `C1=6.55e-6`, null mean `8.0e-7`, std `1.19e-6`, `z=+4.84`, empirical `p=0.006`, i.e. monopole-only explains only 12%. The closure is not propagated paper-wide, so the three interpretation anchors are not coherently presented.
- **Fix:** Update Table I/footnotes and Conclusions to include the post-MASTER monopole-only null and remove all “not computed” statements; explicitly state the 12% explained / 88% unexplained result in the summary table.

## PAPER-GPT-M1 — MAJOR

- **Section:** Conclusions “Canonical-N MASTER ℓ=1 direct compute”; §IV.C; Table `tab:l1_estimators`.
- **Issue:** The canonical-mask residual is reported as `+3.64σ` but also `p_MC=15/500=0.030`; these are not the same significance scale, and the text even says `+3.64σ` is “below this paper’s 3σ detection threshold.” This is internally inconsistent and statistically misleading.
- **Fix:** Call `+3.64` a **moment-z** only, make the empirical-rank `p_MC=0.030` the calibrated significance, and stop comparing the moment-z to Gaussian σ thresholds unless the null tail is Gaussian-validated.

## PAPER-GPT-M2 — MAJOR

- **Section:** §IX.J Sensitivity; Abstract; Conclusions item 1/falsification.
- **Issue:** The injection-recovery floor is called “systematic-inclusive,” but the per-pixel-shuffle null destroys depth/PSF/morphology/label covariance, while the paper documents 21% D4 hard-label flips, morphology-bin non-flatness, and PSF correlations. The systematic error budget is not propagated into the claimed sensitivity/falsification threshold.
- **Fix:** Rename the threshold as a per-pixel-shuffle/mask-depth-count empirical threshold, or build a covariance-preserving null/template-regressed injection sweep and include D4/morphology/PSF uncertainty in `N_eff` and amplitude errors.

## PAPER-GPT-M3 — MAJOR

- **Section:** Abstract; §IV.C multi-null battery; Fig. `fig_multipoles`; §IX.L.
- **Issue:** Interpretation (ii) is overclaimed as “directly confirmed” / “smoking gun” / “rigorously rules out” a real dipole. The anchors are only suggestive: ℓ=2 cross-spectrum is `z=-2.89` before full family correction, the 25% leg-proxy is explicitly not a lower bound, and the MASTER monopole-only null merely shows 88% is not pure monopole leakage, not that it is depth/PSF/morphology.
- **Fix:** Downgrade to “favored/suggestive,” apply trials correction to the cross-spectrum/template searches, and frame real-dipole vs systematic as a joint model comparison or nuisance-marginalized fit, not a ruled-out interpretation.

## PAPER-GPT-M4 — MAJOR

- **Section:** Table `tab:headline_summary`; Table `tab:multipole`; NaMaster configuration appendix.
- **Issue:** The primary subsample MASTER row uses `N_map_weighted=5,547,858` from “TTA duplication,” exceeding the physical `3,201,160` spirals, while shot-noise text alternates between `N_spiral`, `N_map_weighted`, `f_sky=0.491`, and `f_sky=0.659`. Duplicated TTA passes are not independent galaxies, so the noise normalization / effective sample size is dimensionally ambiguous.
- **Fix:** Define the exact map weights and compute a Kish/per-pixel `N_eff`; use that consistently in MASTER noise/null generation, or use the physical galaxy count with probability weights and remove “TTA duplication” as an independent-count denominator.

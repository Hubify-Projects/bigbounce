# P4_v1_0_104_R_INTERNAL R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1545pt
**Wall time**: 140.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=86317, completion=8318, reasoning=7250, total=94635

---

## PAPER-GPT5-B1 — BLOCKER — Abstract; §III.A; §IX.J; Table `mc_injection`; Table `headline_summary`

**Issue:** The injection-recovery sample is still internally contradictory. The text calls the load-bearing 0.75% threshold an `N=471,049` `P>0.9` HC-spiral result, while the new closure says the released JSON was run on `p_eq>0.6`, `N=2,107,494`; other in-paper `p_eq>0.6` counts are `~949k`. This invalidates the quoted Fisher comparisons and operational sensitivity floor.

**Fix:** Pick the artifact as canonical. If `injection_recovery_extended.json` is `N=2,107,494`, update every table/text/Fisher floor to that sample; if the paper wants `N=471,049`, rerun the sweep and cite a matching JSON.

## PAPER-GPT5-B2 — BLOCKER — §IV “Dipole Analysis”; §IX.F Table `face_on`

**Issue:** The same Catalog C full sample is reported as a null real-space dipole (`+0.43σ`, `p=0.30`) and as a strong detection in the HC-robustness table (`+4.31σ`, `p=0.001`, monopole-preserving null). “Different estimator definition and null-sample variance” is not an adequate reconciliation for a factor-10 significance flip on the same sky data.

**Fix:** Put both estimators on the same map, mask, weighting, and null ensemble; either explain and invalidate the LSQ estimator or treat the discrepancy as unresolved. Do not claim a closed real-space no-dipole result until this is fixed.

## PAPER-GPT5-B3 — BLOCKER — NaMaster appendix; §IV.B; §VII conclusions

**Issue:** The MASTER “monopole-subtracted” field is defined as `f_CW(p)-0.5`, but the observed catalog mean is `f_CW=0.49735`; subtracting 0.5 leaves a nonzero mask-weighted monopole (`-0.00265` in `f_CW`, `-0.0053` in asymmetry units). The claim that the `ℓ=0` mode is removed from the input is therefore false unless the mask-weighted sample mean is subtracted or explicitly projected out.

**Fix:** Define the actual data vector unambiguously: subtract `⟨f_CW⟩_mask`, include/marginalize `ℓ=0`, or stop calling the map monopole-subtracted. Recompute/report the `ℓ=1` MASTER result under that declared convention.

## PAPER-GPT5-M1 — MAJOR — §IX.A “Raw Catalog A Dipole Was Dominated by Observational Systematics”

**Issue:** The text says TTA makes the soft chirality score `p_CW^eq - p_CCW^eq` “average to zero per galaxy.” Eq. (2) does not do that; it only enforces flip-equivariance of the output protocol. This contradicts the earlier correct caveat that TTA does not force `p_CW^eq=p_CCW^eq` per galaxy or globally.

**Fix:** Replace the false per-galaxy cancellation claim with the correct flip-swap relation. Attribute depth-coupling suppression only to the measured before/after dipole collapse, not to a nonexistent algebraic cancellation.

## PAPER-GPT5-M2 — MAJOR — Abstract; §IV.G “Hemisphere Asymmetry”; Fig. `hemisphere`; §IX.F

**Issue:** The hemisphere LEE discussion conflates distinct observables/nulls. A local `3.05σ` excursion cannot become `p_LEE≤10^{-4}` after a max-over-directions correction for the same statistic; elsewhere the text alternates between “<1σ consistent with null” and “>3.7σ rejection,” and §IX.F even uses `p_LEE<10^{-4}` as if it excluded directionality.

**Fix:** Split the hemisphere analysis into separately named statistics with separate amplitudes, local z, max-stat p, grid, and null model. Remove any combined verdict; state plainly which null is rejected and which multiplicity calculation is only a conservative parametric cross-check.

## PAPER-GPT5-m1 — minor — §IV.D Table `leg_conf_cross` LEE paragraph

**Issue:** The 15-cell Bonferroni numbers are arithmetically fine only if one preselected z per cell is tested. Table `leg_conf_cross` reports two z columns (`σ_iso`, `σ_mono`); if either was searched or used for claims, the family is 30 tests, not 15.

**Fix:** Declare the monopole-preserving null as the sole preselected family, or apply a 30-test/max-stat correction. Keep the DECaLS `[0.8,1.0)` cell as supporting only, since its significance depends on which null column is treated as primary.

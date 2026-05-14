# P4_v1056 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_1700pt
**Wall time**: 69.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=55868, completion=2843, total=58711

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Abstract; Secs. `hemisphere`, `hemisphere_disc`; Fig. `hemisphere` caption.  
**Issue:** Hemisphere look-elsewhere result is mathematically inverted/contradictory: Bonferroni for local `3.05σ` over ~650 trials gives non-significance, but the direct MC says `0/10000` nulls exceed data, i.e. `p_LEE ≤ 1e-4`, which is highly significant, not “consistent with null.” You cannot use an upper bound on a small tail probability as a null verdict.  
**Fix:** Recompute/inspect the hemisphere MC statistic and tail direction. If `0/10000` exceedances is correct, report it as a significant post-LEE anomaly and explain tension with Bonferroni; if not, correct the MC exceedance count/p-value everywhere.

## PAPER-GPT-B2 — BLOCKER

**Section:** Sec. `sensitivity`; Conclusions item 1; Fig. `multipoles` caption; Motloch comparison.  
**Issue:** The factor-of-2 amplitude convention is still not propagated. The paper acknowledges the full-amplitude Fisher floor should be ~`0.29%`, but still derives and quotes `0.14–0.20%` / “statistical-only Poisson floor is `0.2%`” in multiple downstream places.  
**Fix:** Replace all full-dipole-amplitude sensitivity claims using `0.2%` with the corrected `~0.29%` Fisher floor, or explicitly relabel `0.2%` as the CW-fraction half-modulation, not `A` in `p_CW=1/2(1+A cosθ)`.

## PAPER-GPT-B3 — BLOCKER

**Section:** Abstract; Table `multipole`; Sec. `dipole`; Conclusions “Canonical-N MASTER projection”.  
**Issue:** The load-bearing post-MASTER `ℓ=1` result is not directly computed on the canonical Catalog C spiral sample; it is a subsample-mask result plus an analytic projection, while the direct canonical single-mode NaMaster run is deferred “post-arXiv.” The cited subsample count `n=5,547,858` is also not the canonical spiral count and is not cleanly defined for the chirality map.  
**Fix:** Run the canonical `ℓ=1` MASTER/NaMaster analysis on `N_spiral=3,201,160`, `f_sky≈0.491` with MC nulls and replace the projection. Until then, demote the MASTER `ℓ=1` headline to provisional and use only the directly computed real-space dipole as primary.

## PAPER-GPT-M1 — MAJOR

**Section:** Table `multipole`; Sec. `dipole`; Conclusions.  
**Issue:** The paper says higher multipoles are “consistent with null,” but Table III reports `+6.097σ` at `ℓ_eff=4` and joint `χ²/dof=161.2/38=4.24`. Calling this “mask-coupled monopole leakage” without explicitly marginalizing/subtracting the monopole or using a covariance that includes it invalidates the null-consistency claim.  
**Fix:** Recompute pseudo-`C_ℓ`/MASTER after removing or jointly fitting the monopole, and quote significances from the full covariance including mask leakage. Otherwise remove “all higher multipoles are null” claims.

## PAPER-GPT-M2 — MAJOR

**Section:** Secs. `labels`, `sensitivity`, `comparison`, Conclusions.  
**Issue:** The independent CW/CCW agreement is only `69.91%` (`κ=0.40`), but the dipole sensitivity is computed on catalog labels as if they were true chirality labels. A symmetric binary classifier with accuracy `a≈0.70` attenuates true asymmetries by roughly `2a−1≈0.40`, so true-sky amplitude limits could be degraded by ~`2.5×`, before uncertainty in the confusion matrix.  
**Fix:** Propagate a CW/CCW confusion matrix into the dipole response/injection tests, or state that the `0.5%` floor is for detected catalog-label asymmetry, not true galaxy chirality amplitude.

## PAPER-GPT-M3 — MAJOR

**Section:** Secs. `tta`, `systematic_dipole`, `cw_frac`.  
**Issue:** The paper overclaims what flip-TTA guarantees: probability-level equivariance does not imply unbiased hard-label CW fractions, zero classifier bias, or cancellation “to machine precision.” The surviving `9.5σ` monopole directly disproves the stronger wording.  
**Fix:** Replace “eliminates bias by construction” with “enforces horizontal-flip covariance of soft outputs.” Quantify residual hard-label bias empirically and avoid using equivariance as proof of unbiasedness.

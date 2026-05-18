# P4_v1_0_109_R_INTERNAL R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1715pt
**Wall time**: 109.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=89181, completion=5304, reasoning=4334, total=94485

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Abstract; Sec. `prereg`; Table `headline_summary`; Sec. `sensitivity`; Table `mc_injection`; Conclusions.  
**Issue:** Injection-recovery sample identity is still contradictory: abstract says the released JSON used `p_eq>0.6` with **2,107,494** rows, while the methods/table/sensitivity/conclusions repeatedly state **471,049** HC spirals. This changes the Fisher floor from ≈0.36% to ≈0.76% and flips the systematic-degradation interpretation.  
**Fix:** Pick the actual injection sample from the artifact and update every N, Fisher floor, threshold comparison, and conclusion. If both sweeps exist, split into two explicitly labeled tables.

## PAPER-GPT-B2 — BLOCKER

**Section:** Sec. `monopole_mask_null`; Conclusions “Canonical-N MASTER”; Appendix `namaster_config`.  
**Issue:** Canonical-mask MASTER result is internally inconsistent and stale: v1.0.107 text reports corrected binomial-null **+3.64σ**, abstract uses that multi-null framing, but conclusions still foreground **+1.85σ** as the canonical residual; appendix claims proper monopole subtraction leaves ≈**+1.77σ**. These cannot all be the same final estimator.  
**Fix:** Define one final canonical data vector/null after proper monopole subtraction and propagate it everywhere. Move +1.85/+1.77 to historical/provenance only or label them as distinct obsolete nulls.

## PAPER-GPT-B3 — MAJOR

**Section:** Sec. `monopole_mask_null`, v1.0.108 multi-null battery; Abstract.  
**Issue:** Bootstrap-null language is still overclaimed. Independent pixel/gala​xy resampling can capture marginal overdispersion/non-binomial variance, but it destroys off-diagonal spatial covariance; text still says it “captures spatial-correlation variance” and uses the -0.22σ result as if it nulls the low-ℓ residual.  
**Fix:** State strictly: bootstrap captures marginal pixel overdispersion, not spatial correlations. Add a spatial block bootstrap or depth/PSF/morphology-conditioned null before using it to adjudicate low-ℓ systematics.

## PAPER-GPT-B4 — MAJOR

**Section:** Sec. `monopole_mask_null` verdict; Abstract cross-spectrum paragraph.  
**Issue:** Interpretation (i) is not rigorously “ruled out.” ℓ=2>ℓ=1, bootstrap variance inflation, p_eq quartiles, and a single rℓ=2=-0.65 / -2.89σ density cross-spectrum disfavor a clean dipole, but they do not exclude a mixed model containing both a real ℓ=1 dipole and depth-correlated low-ℓ systematics.  
**Fix:** Rephrase to “disfavored; interpretation (ii) is preferred.” To close it, fit a joint model with dipole amplitude plus density/PSF/morphology templates and report marginalized constraints/likelihood ratios.

## PAPER-GPT-B5 — MAJOR

**Section:** Abstract; Sec. `monopole_mask_null`, “Direct cross-spectrum smoking gun.”  
**Issue:** Cross-spectrum methodology is underspecified for a load-bearing claim: no equation for \(r_\ell\), no statement whether \(n_{\rm total}\) is raw density or overdensity, no mean-subtraction/mask/MASTER/noise-debias details, no MC count, no look-elsewhere correction over ℓ/templates. Calling -2.89σ a “smoking gun” overstates the statistical weight.  
**Fix:** Add the estimator definition, map preprocessing, null construction, covariance, and trials accounting. Downgrade wording unless the result survives template/multipole LEE and is propagated into the C1 systematic budget.

## PAPER-GPT-B6 — MAJOR

**Section:** Abstract; Sec. `dipole`; Sec. `systematic_dipole`; Conclusions.  
**Issue:** The paper still says MASTER “fully removes/collapses” the +6.48σ pseudo-\(C_\ell\) excess to -0.122σ, but those numbers use different map definitions, monopole treatments, masks, and even multipole/binning contexts. That is not a valid isolated MASTER before/after comparison.  
**Fix:** Either run a matched pre/post-MASTER comparison on the identical map/mask/multipole or consistently state that the reduction is due to the full chain: map choice + monopole subtraction + mask change + MASTER.

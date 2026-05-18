# P4_v1_0_111_R_INTERNAL R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1745pt
**Wall time**: 66.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=89882, completion=4088, reasoning=3106, total=93970

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Abstract; §III/§IX.J Sensitivity; Table `mc_injection`; Conclusions item 1  
**Issue:** The injection-recovery sample is internally inconsistent. The abstract says the released `injection_recovery_extended.json` was run on `p_eq>0.6` with `N=2,107,494`, but the methods/table/conclusions repeatedly treat the same sweep as `p_eq>0.9`, `N=471,049`; the Fisher comparison and claimed `0.75%` operational threshold therefore are not anchored to a single data vector.  
**Fix:** Pick the actual injection sample and rewrite every threshold/Fisher comparison using that exact `N`, or rerun the sweep on the stated `P>0.9` sample. Remove “proxy” Fisher comparisons from the abstract.

## PAPER-GPT-B2 — BLOCKER

**Section:** §IV.D Monopole+Mask Leakage; Conclusions “Canonical-N MASTER”; NaMaster appendix  
**Issue:** The `+1.85σ` vs `+3.64σ` canonical-mask reconciliation is not coherent. The paper alternately says `+3.64σ` comes from proper monopole subtraction, while the appendix says explicit subtraction changes `+1.85σ` only to `~+1.77σ`; the data/null values also differ (`C1=2.298e-5` vs `1.51e-5`, null std `8.10e-6` vs `3.31e-6`) without a single side-by-side methodology table.  
**Fix:** Add a table with exact map, mask, monopole subtraction in data and null, null generator, MC count, `C1`, null mean/std, and σ for both runs. Until reconciled, do not use either canonical σ in verdict logic.

## PAPER-GPT-B3 — MAJOR

**Section:** Abstract; Introduction; Fig. `multipoles` caption; §IV.D operational conclusion; §IX.B  
**Issue:** Bootstrap was not dropped consistently. The text still says the bootstrap null gives `-0.22σ`, is “consistent with null,” is the “canonical honest framing,” and even recommends treating the canonical-mask result as null under bootstrap, despite later admitting the bootstrap is tautological for cosmological-dipole testing.  
**Fix:** Remove bootstrap from the abstract, conclusions, and any verdict language. Mention it only once as a sampling-variance diagnostic that cannot discriminate real dipole vs position-correlated systematic.

## PAPER-GPT-B4 — MAJOR

**Section:** §IV.D “Honest scientific verdict across the three interpretations”  
**Issue:** The three-discriminator closure overclaims. `ℓ=2>ℓ=1`, quartile washout, and `A×n` cross-spectrum are suggestive of systematics, but the paper treats them as ruling out a real dipole without a joint likelihood, look-elsewhere correction, or injected-dipole distribution for the same diagnostics. Quartile splitting also reduces SNR by about `√4`, so “all |σ|<1” is not by itself decisive for a full-sample `3.6σ` feature.  
**Fix:** Recast as “systematics-favored, not a detection.” Quantify `P(ℓ2≥obs, ℓ1≈obs, quartile pattern, cross-spectrum)` under injected-dipole and depth-systematic simulations before saying “ruled out” or “confirmed.”

## PAPER-GPT-B5 — MAJOR

**Section:** Abstract; §III preregistered hierarchy; §IX.J Sensitivity; Conclusions  
**Issue:** The per-pixel/random-label null is repeatedly called “systematic-inclusive” or said to preserve depth/mask-edge correlations, but the global label shuffle destroys label–depth/PSF/morphology covariance. It preserves positions/counts, not the systematic coupling needed to calibrate false dipoles.  
**Fix:** Rename it “position/count-preserving, label-covariance-destroying null.” A systematic-inclusive threshold requires nulls or injections conditioned on measured depth, PSF, morphology, and imaging-leg covariance.

## PAPER-GPT-B6 — minor

**Section:** Abstract  
**Issue:** The abstract is still a defensive internal log, not an abstract. It contains reviewer-round notes, artifact-debug prose, contradictory methodological caveats, and bootstrap language that should have been removed.  
**Fix:** Replace with a short final-state abstract: sample, classifier, primary estimators, leakage demonstration, final dipole result, empirical sensitivity, and matched-pipeline caveat. No internal audit labels or version-history prose.

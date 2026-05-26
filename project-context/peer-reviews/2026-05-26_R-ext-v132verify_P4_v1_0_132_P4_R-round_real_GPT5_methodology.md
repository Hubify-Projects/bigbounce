# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v132verify_P4_v1_0_132
**Wall time**: 85.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=100721, completion=4912, reasoning=3624, total=105633

---

## PAPER-GPT-B1 — BLOCKER

**Section/Table:** Table `data_vectors`; Sec. `Dipole Analysis`; Sec. `NaMaster MASTER configuration`  
**Issue:** The load-bearing data vector is still not uniquely defined. Table says the MASTER rows use a soft \(p_{\rm CW}\)-weighted \(A_p\) with galaxy-weighted monopole subtraction; Sec. `Dipole Analysis` defines \(A_p=(N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})\) from hard labels; the NaMaster appendix again describes hard-count \(A_p\), while the nulls alternate between label-shuffle, per-pixel-shuffle, and binomial realizations. The quoted \(-0.12\sigma\), \(+3.64\sigma\), and MC p-values are not reproducible from a single declared field.  
**Fix:** Give one mathematical definition per estimator: field, weights, denominator, monopole subtraction, mask, and null. Regenerate all MASTER/MC numbers from those exact vectors or explicitly relabel them as different estimators.

## PAPER-GPT-B2 — BLOCKER

**Section/Table:** Sec. `NaMaster MASTER configuration`; Sec. `Dipole Analysis`; Table `l1_estimators`  
**Issue:** Monopole treatment and mask choice remain internally inconsistent. The text says the headline subsample-mask map is monopole-subtracted by the galaxy-weighted mask mean, but the appendix says \(f_{\rm CW}-0.5\), which leaves the observed \(0.49735\) monopole; the canonical correction changes \(C_1\) and \(\sigma\) substantially, proving this is not negligible. The \(f_{\rm sky}=0.659\) “subsample” mask is also not sufficiently defined and is used to bypass the \(+3.64\sigma\) canonical residual without a matched systematics-preserving null.  
**Fix:** Apply the same explicit galaxy-weighted monopole subtraction to all masks, define the \(f_{\rm sky}=0.659\) mask algorithmically, and rerun canonical/subsample MASTER with identical nulls. Do not make the \(-0.12\sigma\) headline claim until this reconciliation is shown.

## PAPER-GPT-M1 — MAJOR

**Section/Table:** Declared Analysis Hierarchy item (v); Table `data_vectors` row (v); Table `headline_summary` footnote b  
**Issue:** The v1.0.132 MC-count closure did not land cleanly. The hierarchy still says the monopole-only generative null is \(N=500\), Table `data_vectors` row (v) says “500 (10000 in v1.0.130 ext)”, and footnote b calls \(N=500\) the headline result before appending the \(N=10{,}000\) rerun. This fails the claimed 500→10,000 canonical fix.  
**Fix:** Make the canonical row unambiguously \(N_{\rm MC}=10{,}000\), move the \(N=500\) result to a historical cross-check, and quote only the \(N=10{,}000\) mean/std/z/rank-p in headline tables.

## PAPER-GPT-M2 — MAJOR

**Section:** Abstract; Sec. `Sensitivity Floor`; Conclusions/falsification criterion  
**Issue:** The amplitude convention remains inconsistent. The paper alternates among \(0.2\%\), \(0.29\%\), \(0.4\%\), \(0.75\%\), and \(1.5\%\) thresholds, sometimes for half-modulation \(A/2\), sometimes full amplitude \(A\), and sometimes HC subsample versus full catalog. The LSST projections also conflict: \(0.08\%\), \(0.04\%\), and \(0.44\%\) appear in different places.  
**Fix:** Use one convention \(p_{\rm CW}=\frac12(1+A\cos\theta)\). Quote the full-amplitude empirical threshold only for the exact sample tested; separate ideal Fisher, HC empirical, full-catalog empirical, and LSST projections in one table.

## PAPER-GPT-M3 — MAJOR

**Section:** Abstract; Sec. `Monopole+Mask Leakage Generative Null`; Sec. `Relation to possible parity-violating sectors`  
**Issue:** The systematic-attribution language is overclaimed. A single \(r_{\ell=2}=-0.65\), \(-2.89\sigma\) cross-spectrum result is only \(\sim2.3\sigma\) after the paper’s own trials correction, yet the abstract says the depth-correlated systematic is “directly confirmed” and uses it to exclude a clean dipole-only interpretation. No joint nuisance-marginalized dipole+systematics model has been run.  
**Fix:** Replace “confirmed/exclude” with “suggestive/favoured”. Perform the pending joint fit with dipole plus depth/PSF/morphology templates and report marginalized evidence or likelihood-ratio results before making exclusion claims.

## PAPER-GPT-M4 — MAJOR

**Section/Figure:** Sec. `Hemisphere Asymmetry`; Fig. `hemisphere`; Sec. `hemisphere_disc`  
**Issue:** The look-elsewhere treatment is statistically incoherent. The same hemisphere channel is reported as \(<1\sigma\) post-Bonferroni and as \(p_{\rm LEE}\le10^{-4}\) from direct MC, but these are different statistics/grids/normalizations and cannot both be used as interpretive support. Also, zero exceedances in \(10^4\) MC gives a resolution-limited estimate/upper confidence bound, not a deterministic \(p\le1/(N+1)\) measurement.  
**Fix:** Define one hemisphere statistic and one trials correction. For zero exceedances quote a confidence interval, e.g. \(p<3/(N+1)\) at 95%, and stop mixing it with the analytic Bonferroni result.

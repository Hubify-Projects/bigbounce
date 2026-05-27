# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P4_v1_0_138
**Wall time**: 95.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=106584, completion=5205, reasoning=4142, total=111789

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Table `data_vectors`; §Dipole Analysis; §NaMaster MASTER configuration  
**Issue:** The load-bearing $\ell=1$ data vector is inconsistent: Table rows (ii–v) call it a soft $p_{\rm CW}$-weighted $A_p$, while §Dipole and §NaMaster define $A_p=(N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})$ from hard labels. This invalidates the claim that the 21.4% argmax-flip uncertainty is irrelevant to the headline.  
**Fix:** Define one primary map algebraically, state whether it is soft or hard, and recompute all MASTER/noise/null results for that exact map. If hard-label counts are used, propagate the $D_4$ argmax uncertainty into the headline.

## PAPER-GPT-B2 — BLOCKER

**Section:** §Monopole+Mask Leakage Generative Null, “Joint nuisance-marginalized model fit” / “Extended joint fit”  
**Issue:** The “formal exclusion” of a 1.7% dipole at $z=-250$ is not a valid marginalized likelihood result. It uses a weighted linear regression with diagonal count weights despite demonstrated spatial covariance/systematics, treats $A=\sqrt{a_x^2+a_y^2+a_z^2}$ as Gaussian, and compares a parameter shift to an underestimated posterior width.  
**Fix:** Use a full covariance calibrated from systematics-preserving simulations, profile/marginalize over dipole direction and nuisance templates in the three Cartesian components, and quote $\Delta\chi^2$/profile likelihood or posterior credible limits. Remove all “250σ” and “formally excluded” language until then.

## PAPER-GPT-M1 — MAJOR

**Section:** Abstract; Table `headline_summary`; §Conclusions “Canonical-$N$ MASTER”  
**Issue:** The canonical-mask residual is repeatedly reported as “$+3.64\sigma$,” but the same text gives empirical rank $p_{\rm MC}=15/500=0.030$. A 500-realization null with rank $p=0.03$ does not support a 3.64σ tail claim; the moment-$z$ is not calibrated significance.  
**Fix:** Report this as “moment-$z=3.64$, empirical $p=0.030$” and, if a sigma equivalent is needed, convert the empirical $p$ under a stated one-/two-sided convention or run enough MC to calibrate the tail.

## PAPER-GPT-M2 — MAJOR

**Section:** §Test-Time Equivariant Averaging, “Hard-label variance widening”; Table `headline_summary` footnote c  
**Issue:** The flip-noise variance derivation is wrong. For $x_{\rm obs}=x_{\rm true}\oplus f$, $P(x_{\rm obs}=1)=e+(1-2e)p$ and $\mathrm{Var}(x_{\rm obs})=q(1-q)$; at $p\simeq0.5$ symmetric flips do not add $e(1-e)$ to binomial variance. If estimating the true labels after de-dilution, the variance inflates by roughly $1/(1-2e)^2$ in variance, not by 1.21× in $\sigma$.  
**Fix:** Re-derive with an explicit misclassification matrix and state whether diagnostics estimate observed hard labels or de-biased true labels. Recompute hard-label error bars and injection-recovery thresholds accordingly.

## PAPER-GPT-M3 — MAJOR

**Section:** §Sensitivity Floor; §Monopole+Mask Leakage, “Full-catalog injection-recovery sensitivity”  
**Issue:** The sensitivity numbers are internally inconsistent. The full-catalog injection claim says $A=0.5\%$ gives median $\sigma=12.62$, while the paper’s own full-catalog Fisher floor says a 0.5% full-amplitude dipole should be only $\sim5\sigma$ ideal, and the HC sweep treats 0.5% as a non-detection.  
**Fix:** Put all injection sweeps on the same amplitude convention, estimator, mask, null, and $\sigma$ calibration. Do not claim a full-catalog $\le0.50\%$ threshold unless it is reconciled with Fisher scaling.

## PAPER-GPT-M4 — MAJOR

**Section:** §Declared Analysis Hierarchy; §Dipole Analysis; §Conclusions  
**Issue:** The paper says “either” primary estimator being null suffices, while another closely related canonical-mask $\ell=1$ estimator is non-null under its own moment statistic. This is not a valid multi-estimator decision rule, especially with a declared hierarchy fixed after initial results rather than pre-registered.  
**Fix:** Define a single primary test statistic before interpretation, or combine the estimators in a joint model with explicit covariance and mask dependence. Treat mask changes as robustness tests, not as independent null-sufficiency.

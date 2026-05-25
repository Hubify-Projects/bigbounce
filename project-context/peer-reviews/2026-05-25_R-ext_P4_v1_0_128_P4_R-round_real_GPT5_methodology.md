# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P4_v1_0_128
**Wall time**: 85.3s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=97224, completion=4190, reasoning=3106, total=101414

---

## PAPER-GPT-B1 — BLOCKER

**Section:** §§Methods “Pre-Registered Analysis Hierarchy”, Dipole Analysis, Conclusions  
**Issue:** The headline null is mask/estimator-dependent: $\ell=1$ is $-0.12\sigma$ on the “subsample” mask but $+3.64$ moment-$z$ on the canonical mask, and the canonical residual stays large under pixel-threshold sweeps. Declaring the favorable mask “load-bearing” while assigning the other to systematics is not a valid null result without an a priori mask/data-vector definition and nuisance-marginalized model.  
**Fix:** Predefine one primary mask/data vector before unblinding, or present a joint likelihood including primordial dipole plus depth/PSF/morphology templates with nuisance marginalization. If the result remains mask-dependent, headline it as inconclusive/mask-sensitive, not a null.

## PAPER-GPT-B2 — BLOCKER

**Section:** Tables I, mask-robustness table, Conclusions “Canonical-$N$ MASTER”  
**Issue:** Moment-$z$ values are repeatedly reported as “$\sigma$” significances despite empirical MC calibration contradicting them: canonical $+3.64$ has $p_{\rm MC}=15/500=0.030$ ($\sim2.2\sigma$ two-sided), not $3.64\sigma$; mask-robustness “$+6$–$+8\sigma$” from $N=200$ MC cannot support tail claims beyond the rank resolution. The paper itself notes heavy-tailed nulls elsewhere, so Gaussian tail conversion is unjustified.  
**Fix:** Quote empirical-rank $p$ values with finite-MC uncertainty, or run enough MC / validate a parametric tail model. Reserve “$\sigma$” for calibrated Gaussian-equivalent significances.

## PAPER-GPT-M1 — MAJOR

**Section:** §Sensitivity Floor and Minimum Detectable Signal  
**Issue:** The Fisher sensitivity derivation still mixes full-amplitude $A$ and half-modulation $A/2$. For $p_{\rm CW}=\frac12(1+A\cos\theta)$, the full-amplitude 1-$\sigma$ Fisher error is $\sqrt{3/N_{\rm eff}}$, so the full-amplitude 3-$\sigma$ floor is $\sim0.29\%$ for $N=3.20$M before mask inflation, not the repeatedly cited $0.14$–$0.2\%$ except as a half-modulation quantity.  
**Fix:** Rewrite the subsection using one convention throughout. State full-amplitude floors only: $\sim0.29\%$ ideal full catalog, $\sim0.4\%$ with mask inflation, $\sim0.76\%$ for the 471k HC subsample.

## PAPER-GPT-M2 — MAJOR

**Section:** §Sensitivity, Conclusions, Data Availability  
**Issue:** The empirical $0.75\%$ threshold is called “systematic-inclusive” in several places, but the null is per-pixel/label shuffle and explicitly destroys depth/PSF/morphology covariance. That is not a systematic-inclusive sensitivity budget; it is a statistical/null-model-specific injection recovery on selected HC cuts, with other variants giving up to $1.5\%$.  
**Fix:** Rename it “per-pixel-shuffle empirical threshold for the stated HC pipeline.” Do not use it as a systematic-inclusive limit or falsification floor until injections are run through a covariance-preserving depth/PSF/morphology null.

## PAPER-GPT-M3 — MAJOR

**Section:** §Signal-Hunt Diagnostics, §Dipole “multi-null battery”  
**Issue:** The depth-systematic interpretation is overclaimed. The main cross-spectrum evidence is $r_{\ell=2}=-0.65$ at $-2.89\sigma$ before full trials/nuisance correction, and the DECaLS-stratum cross-spectrum is only $-1.6$–$-1.7\sigma$; these are suggestive diagnostics, not confirmation or a basis for excluding a primordial component.  
**Fix:** Replace “confirmed/directly ties” language with “suggestive.” Perform a joint model comparison with dipole and depth/PSF/morphology templates marginalized, or leave the canonical residual unresolved.

## PAPER-GPT-M4 — MAJOR

**Section:** Table III / §Dipole Analysis / NaMaster appendix  
**Issue:** The multipole table is not auditable: it mixes single-$\ell$ and bandpower estimators, subsample and canonical masks, pre-/post-MASTER language, and omits null means needed to reproduce the displayed $z$ values. Several rows show negative $C_\ell$ values and positive significances, which may be possible after subtraction but cannot be checked from the table.  
**Fix:** Split into separate tables for subsample single-$\ell$, canonical MASTER, and raw pseudo-$C_\ell$. Include measured $C_\ell$, null mean, null std, empirical $p$, mask, monopole-subtraction status, and MC count for every row.

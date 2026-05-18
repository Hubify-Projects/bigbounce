# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1640pt_P4_v1_0_115_R20
**Wall time**: 89.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=87949, completion=4667, reasoning=3624, total=92616

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Abstract; §§3.1, 4.2–4.3, Conclusions, NaMaster appendix  
**Issue:** The headline “MASTER removes leakage” is not demonstrated on a like-for-like data vector. The paper compares un-monopole-subtracted canonical-mask pseudo-$C_\ell$, monopole-subtracted subsample-mask MASTER, and canonical-mask direct-MC with different masks, fields, nulls, and monopole treatments, then treats the $-0.12\sigma$ subsample result as dispositive despite the same catalog giving $+3.64\sigma$ on the canonical mask.  
**Fix:** Run the full MASTER + null pipeline on the same map definition, monopole subtraction, weighting, and mask for data and all nulls; present the canonical and subsample results as separate estimators unless a validated transfer/leakage model connects them.

## PAPER-GPT-B2 — BLOCKER

**Section:** Conclusions, “Canonical-$N$ MASTER $\ell=1$ direct compute”  
**Issue:** The canonical result is reported as $+3.64\sigma$ but also as empirical-rank $p_{\rm MC}=15/500=0.030$; those are incompatible tail statements ($p=0.03$ is $\sim1.9\sigma$ one-sided, not $3.64\sigma$). The text also calls $+3.64\sigma$ “below this paper’s $3\sigma$ detection threshold,” which is arithmetically false.  
**Fix:** Quote either the empirical-rank p-value or a Gaussianized z-score calibrated from a sufficiently large/null-smoothed tail; do not call $+3.64\sigma$ sub-$3\sigma$.

## PAPER-GPT-M1 — MAJOR

**Section:** Abstract; §4.3 Monopole+Mask Leakage; §4.4 Signal-hunt diagnostics  
**Issue:** The “real cosmological dipole ruled out” verdict is overclaimed. $\ell=2>\ell=1$, non-monotonic confidence quartiles, and a single $r_{\ell=2}=-0.65$ cross-spectrum at $-2.89\sigma$ do not exclude a real dipole plus systematics without a joint model, look-elsewhere correction, and marginalization over depth/PSF/morphology templates.  
**Fix:** Rephrase as “disfavored under these diagnostics,” or fit a joint likelihood with dipole amplitude and systematics templates marginalized; report likelihood ratios/Bayes factors only after that marginalization.

## PAPER-GPT-M2 — MAJOR

**Section:** §4.2 Dipole Analysis; NaMaster appendix  
**Issue:** The shot-noise/error propagation for the asymmetry field is not rigorous. A per-pixel ratio field $A_p=(N_{\rm CW}-N_{\rm CCW})/N_{\rm spiral}$ with highly nonuniform $n_p$ is treated with a global tracer shot-noise term $4\pi f_{\rm sky}/N_{\rm spiral}$, while the paper itself admits per-pixel weighting is required.  
**Fix:** Propagate binomial per-pixel variances through the exact mask/MASTER operator, or use inverse-variance weighted maps and MC nulls that reproduce the observed $n_p$ distribution; remove analytic significances that depend on the homogeneous-noise approximation.

## PAPER-GPT-M3 — MAJOR

**Section:** §9.J Sensitivity; Conclusions item 1 and falsification criterion  
**Issue:** The empirical $0.75\%$ “systematic-inclusive” threshold comes from the $471{,}049$ high-confidence subsample and a relabeling injection that does not preserve classifier confusion, depth/PSF/morphology correlations, or the full 3.2M-catalog systematics. It is then used as a paper-wide operational floor and falsification scale.  
**Fix:** Label it explicitly as an HC-subsample per-pixel-shuffle sensitivity only; run a full-catalog injection with observed labels/systematics preserved or stop using $0.75\%$ as the survey-wide systematic-inclusive bound.

## PAPER-GPT-M4 — MAJOR

**Section:** §3.5 TTA; Conclusions “$D_4$-TTA rotational-equivariance validation”  
**Issue:** The $D_4$ validation does not close the rotation-systematics budget: the holdout has only 1,558 galaxies, a quoted $\pm1.3\%$ floor, a $1.35\%$ argmax CW-fraction shift, and a 21.4% argmax flip rate, yet sub-percent catalog-level claims proceed without propagating this uncertainty into the dipole/systematic budget.  
**Fix:** Either perform full-catalog or statistically powered $D_4$ inference, or include the observed rotation-induced uncertainty as a systematic term and weaken sub-percent sensitivity claims accordingly.

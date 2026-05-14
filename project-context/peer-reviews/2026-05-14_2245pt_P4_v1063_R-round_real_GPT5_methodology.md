# P4_v1063 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_2245pt
**Wall time**: 56.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=60010, completion=3331, total=63341

---

No BLOCKER-grade findings.

## PAPER-GPT-M1 — MAJOR

**Section:** Abstract; §IX canonical-$N$ MASTER direct compute, item (iii)  
**Issue:** The per-pixel random-label null is described inconsistently: the abstract says it *does not preserve* depth/GZ1-label spatial structure, while §IX says it preserves marginal depth/mask/edge coupling and therefore does not average leakage away. These are opposite statistical claims and the +1.85σ “leakage-floor” interpretation depends on which is true.  
**Fix:** Define the permutation null exactly and state what spatial structures it preserves/destroys. If depth-correlated chirality is destroyed, do not use that null to calibrate leakage; construct a depth-/mask-/label-systematics-preserving null or weaken the interpretation.

## PAPER-GPT-M2 — MAJOR

**Section:** Table III; §IX estimator table  
**Issue:** The expanded estimator tables are still not statistically self-contained: significances require a null mean, but only measured \(C_\ell\) and \(\sigma_{\rm null}\) are shown. Several bandpowers are negative, so the table must specify whether values are noise-subtracted/deconvolved bandpowers, not raw powers.  
**Fix:** Add columns for \(\langle C_\ell^{\rm null}\rangle\), noise-subtraction status, estimator type, and MC count for every row. Ensure each listed significance is directly reproducible from table entries.

## PAPER-GPT-M3 — MAJOR

**Section:** Abstract; Table III caption; §IX estimator table footnote  
**Issue:** The subsample-mask MASTER row is ambiguous: the text quotes \(n=5{,}547{,}858\), \(f_{\rm sky}=0.659\), while the §IX table lists \(N_{\rm spiral}=3{,}201{,}160\) with a footnote calling 5,547,858 a “pixel-weighted galaxy count / TTA duplication.” A count larger than the catalog spiral count cannot be treated as interchangeable without defining weights and \(N_{\rm eff}\).  
**Fix:** Give the exact map construction for the \(f_{\rm sky}=0.659\) estimator: object count, duplicated/weighted count, pixel weights, shot-noise denominator, and effective \(N\). Do not label both as the same \(N_{\rm spiral}\) without a derivation.

## PAPER-GPT-M4 — MAJOR

**Section:** §Sensitivity; Abstract; §Conclusions item 1  
**Issue:** The empirical injection-recovery “publication-grade” floor is inferred from the HC-spiral subsample \(N=471{,}049\), but is repeatedly reported as the canonical/full-catalog \(3.2\)M sensitivity. Also, the tested criterion is \(P(\sigma>2)\), not \(P(\sigma>3)\), and 50% recovery is not reached at \(A=0.5\%\).  
**Fix:** Either rerun injection-recovery on the full Catalog C sample with a \(P(\sigma>3)\ge 0.5\) criterion and amplitudes above 0.5%, or state strictly that the current result is only \(A_{\rm floor}>0.5\%\) for the HC-spiral/per-pixel-shuffle setup, not a demonstrated 3σ full-catalog threshold.

## PAPER-GPT-M5 — MAJOR

**Section:** §Confidence Stratification; Abstract; Introduction; Conclusions  
**Issue:** §Confidence declares the high-confidence \(0.3\sigma\) dipole as the “primary” result and claims the abstract/introduction/conclusions quote it, but those sections instead quote the unstratified \(0.43\sigma\), MASTER \(-0.122\sigma\), and canonical \(+1.85\sigma\) values. This is an internal contradiction in the headline estimator chain.  
**Fix:** Choose one primary estimator hierarchy. Either remove the high-confidence-primary claim, or propagate the \(0.3\sigma\) value consistently and explain how it relates to the full-sample real-space and MASTER estimators.

## PAPER-GPT-M6 — MAJOR

**Section:** Abstract; §Hemisphere Asymmetry; Fig. hemisphere caption  
**Issue:** The conversion from hemisphere half-difference \(0.17\%\) to full dipole amplitude \(A=0.853\%\) is not derived and appears inconsistent with the simple full-sky relation for \(p_{\rm CW}=\frac12(1+A\cos\theta)\), where hemisphere half-difference would scale as \(A/4\). This matters because \(0.853\%\) exceeds the quoted empirical \(>0.5\%\) sensitivity floor, yet is dismissed as non-detection.  
**Fix:** Derive the hemisphere-statistic-to-\(A\) conversion for the actual mask/axis weighting, or remove the full-\(A\) number. Do not compare the hemisphere max-statistic amplitude to the injection-recovery dipole floor unless both use the same estimator and mask.

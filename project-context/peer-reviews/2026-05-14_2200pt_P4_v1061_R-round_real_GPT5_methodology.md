# P4_v1061 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_2200pt
**Wall time**: 66.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=57888, completion=3395, total=61283

---

No BLOCKER-grade findings.

## PAPER-GPT-M1 — MAJOR — Sec. “Sensitivity Floor” / Abstract / Conclusions

Concrete issue: The empirical “publication-grade” floor \( |A_{\rm dipole}|>0.5\% \) is derived from the HC-spiral subset (\(N=471{,}049\)), not the canonical \(3{,}201{,}160\)-spiral Catalog C sample, and the injection grid only reports \(P(\sigma>2)=0.18\) at \(A=0.5\%\), not 50% recovery at \(3\sigma\). This does not support wording that implies a demonstrated \(3\sigma\), full-catalog detection threshold.

Fix: Rerun injection recovery on the full canonical Catalog C sample with amplitudes above 0.5% until \(P(\sigma>3)>0.5\), or explicitly label the current result as a conservative HC-subsample bound with no demonstrated \(3\sigma\) recovery threshold.

## PAPER-GPT-M2 — MAJOR — Sec. “Sensitivity Floor”, Fig. 7 caption, Conclusions item 1

Concrete issue: The Fisher-floor amplitude-convention closure is not clean: several remaining statements still call \(\sim0.2\%\) the “minimum detectable dipole” / “statistical-only Fisher floor,” despite the corrected full-amplitude floor being \(\sim0.29\%\) ideal or \(\sim0.4\%\) conservative under \(p_{\rm CW}=\frac12(1+A\cos\theta)\). This reintroduces the half-modulation/full-amplitude ambiguity the revision claims to close.

Fix: Replace all user-facing “dipole floor \(\sim0.2\%\)” statements with “half-modulation \(A/2\) floor \(\sim0.2\%\)” or “full-amplitude \(A\) floor \(\sim0.29\%\) ideal / \(\sim0.4\%\) conservative.”

## PAPER-GPT-M3 — MAJOR — Sec. “Angular power spectrum” / Table III

Concrete issue: The paper simultaneously claims MASTER-deconvolved multipoles are null and reports large residual bandpower anomalies: \(\ell_{\rm eff}=4\) at \(+6.097\sigma\), joint \(\chi^2/{\rm dof}=161.2/38=4.24\). Calling “all higher multipoles consistent with null” is false as written, even if the excess is attributed to monopole leakage rather than parity violation.

Fix: State explicitly that only the single-mode \(\ell=1\) statistic is null; remove “all higher multipoles null” language, and either monopole-subtract/marginalize before MASTER bandpowers or present the \(\ell\ge2\) table as a failed broadband-null/systematics diagnostic.

## PAPER-GPT-m1 — minor — Sec. “Hemisphere Asymmetry” / Fig. 8 / Sec. “The 3.05σ Hemisphere Signal”

Concrete issue: The LEE discussion is internally confused: the text first says the \(3.05\sigma\) hemisphere peak does not survive Bonferroni/BH and is \(<1\sigma\), then says direct max-stat MC gives \(p_{\rm LEE}\le10^{-4}\) and rejects the random-label null. These are not interchangeable conclusions; the direct max-stat MC should supersede the analytic grid penalty.

Fix: Delete the “does not survive LEE” conclusion or confine it to the obsolete analytic approximation. Present the direct MC max-stat result as the operative random-label-null result, then separately explain why that null is not systematic-inclusive.

## PAPER-GPT-m2 — minor — Table IV / Sec. “Sky Region Balance”

Concrete issue: The regional uniformity table uses a superseded snapshot total \(3{,}321{,}795\) while the canonical analysis uses \(3{,}201{,}160\); the per-region canonical recount is deferred. Regional uniformity is used as evidence that the \(9.5\sigma\) monopole is spatially uniform, so relying on stale regional counts weakens that claim.

Fix: Recompute the seven regional CW fractions from the canonical `class_eq` catalog and replace the snapshot rows. If retained for provenance, move snapshot counts to an appendix, not the load-bearing table.

## PAPER-GPT-m3 — minor — Sec. “Catalog Tiers”, Platt recalibration paragraph

Concrete issue: The claim that GZ1 Platt recalibration “converged at the starting point” and therefore provides no recalibration leverage is statistically under-specified. Chance accuracy does not imply a flat NLL surface or zero gradient in \((A,B)\); the optimizer could also be stuck due to saturation, weighting, label encoding, or tolerance.

Fix: Report the final gradient norm, Hessian/uncertainties, tolerance, and NLL change from \((A_0,B_0)\), or remove the inference that the starting-point convergence is meaningful calibration evidence.

# P4_v1100 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0330pt_P4_v1100_R18_R-round_real
**Wall time**: 122.8s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=83557, completion=6979, reasoning=5526, total=90536

---

No BLOCKER-grade findings. Known deferred residuals are not re-litigated as blockers; items below are new arithmetic/statistical issues or propagation-tail polish.

## PAPER-GPT-M1 — MAJOR — Sensitivity amplitude convention still self-contradicts

**Section:** §IX.J “Sensitivity Floor,” Conclusions item 1  
**Issue:** The text alternates between half-modulation \(A/2\) and full amplitude \(A\): it correctly derives \(\sigma(A/2)=0.048\%\) and full-amplitude \(3\sigma\) Fisher floor \(\sim0.29\%\), but then calls \(3\times0.048\%=0.14\%\rightarrow0.2\%\) a “minimum detectable amplitude” and later mixes this with full-amplitude thresholds.  
**Fix:** Use full \(A\) everywhere in headline prose/tables; relegate \(A/2\) to one derivation paragraph. State: ideal full-catalog Fisher \(3\sigma\) floor \(\approx0.29\%\); conservative masked full-amplitude floor \(\approx0.4\%\); operational HC empirical threshold \(0.75\%\).

| Truth audit | Verdict |
|---|---|
| Type | New/statistical-consistency issue |
| Severity driver | User-facing sensitivity claim |
| Deferred residual? | Related to known 0.75% threshold, but this is a fixable prose/arithmetic inconsistency |
| Diminishing-returns? | No |

## PAPER-GPT-M2 — MAJOR — GZ1-dilution arithmetic is wrong

**Section:** §III.A “Pre-Registered Analysis Hierarchy,” sensitivity-floor bullet  
**Issue:** The symmetric-error model gives \(\epsilon\simeq0.185\) and dilution \(D=1-2\epsilon\simeq0.63\). Therefore an observed \(0.75\%\) threshold corresponds to a true amplitude \(0.75/0.63\simeq1.19\%\), not \(\sim0.79\%\).  
**Fix:** Replace the claimed \(\sim0.79\%\) “true underlying” bound with the model-dependent value actually implied by the stated model, or remove the conversion entirely and keep \(0.75\%\) as an observed-catalog threshold.

| Truth audit | Verdict |
|---|---|
| Type | New arithmetic/systematic-budget error |
| Severity driver | Mis-propagates classifier-error dilution into amplitude bound |
| Deferred residual? | No |
| Diminishing-returns? | No |

## PAPER-GPT-M3 — MAJOR — \(\ell=1\) post-MASTER null is not “1-dof chi-squared”

**Section:** §IV.B “Dipole Analysis,” post-MASTER \(C_1\) paragraph  
**Issue:** The paper says the \(\ell=1\) post-MASTER null is “a 1-dof chi-squared.” A full-sky scalar \(C_1\) estimator has \(2\ell+1=3\) modes; on a cut sky after MASTER it is a generalized/MC-calibrated distribution, not a 1-dof \(\chi^2\).  
**Fix:** Delete the 1-dof claim. Make the empirical 500-MC rank \(p\) the only primary \(p\)-value; if an analytic comparison is kept, estimate \(\nu_{\rm eff}\) from the MC distribution.

| Truth audit | Verdict |
|---|---|
| Type | New statistical-framing error |
| Severity driver | Wrong null-distribution statement |
| Deferred residual? | No |
| Diminishing-returns? | No |

## PAPER-GPT-M4 — MAJOR — Residual “parity-violation observable is the dipole” language remains

**Section:** Abstract; §VIII “Symmetry classification”; scattered “dipole-parity” captions/prose  
**Issue:** The abstract still says “the parity-violation observable is the dipole, not the monopole,” directly contradicting the paper’s own derivation that the \(\ell=1\) chirality dipole is parity-even and tests isotropy/axial-vector anisotropy, not parity violation. Similar “dipole-parity observable/statistic” wording persists.  
**Fix:** Replace direct dipole-channel language with “isotropy-breaking axial-vector dipole observable.” Keep “parity-violating” only for cited prior claims, EFT/4PCF contexts, or explicitly parity-odd monopole/even-\(\ell\) diagnostics.

| Truth audit | Verdict |
|---|---|
| Type | R18 propagation-tail closure failure |
| Severity driver | Scientific symmetry misstatement on public surface |
| Deferred residual? | No; fix is text-only |
| Diminishing-returns? | No |

## PAPER-GPT-m5 — minor — Stale canonical-mask \(f_{\rm sky}=0.494\) survives

**Section:** Table I/headline summary row (iv); Conclusions Table “Three \(\ell=1\) estimators” canonical direct-MC row  
**Issue:** Canonical-mask contexts still show \(f_{\rm sky}=0.494\), while the closure target and nearby text use \(0.49005\). This is exactly the stale-value propagation tail R18 asked to audit.  
**Fix:** Change canonical-mask entries to \(0.49005\) or explicitly label any noncanonical hemisphere-grid value as a distinct estimator, not the canonical mask.

| Truth audit | Verdict |
|---|---|
| Type | Diminishing-returns propagation polish |
| Severity driver | Table consistency, not result-changing |
| Deferred residual? | No |
| Diminishing-returns? | Yes |

## PAPER-GPT-m6 — minor — Low-\(\ell\) joint \(\chi^2/{\rm dof}\) is still over-formal without covariance

**Section:** Table III multipoles; §IV.B angular-power discussion  
**Issue:** The table quotes joint \(\chi^2/{\rm dof}=161.2/38\) for low-\(\ell\) bandpowers, but MASTER bandpowers on a cut sky are correlated and no covariance matrix is used/displayed. As written, the number looks like a formal goodness-of-fit statistic.  
**Fix:** Label it “diagonal diagnostic only; no formal \(p\)-value,” or provide the MC covariance and recompute \(\chi^2=C^T\Sigma^{-1}C\).

| Truth audit | Verdict |
|---|---|
| Type | Persistent-residual deferred item |
| Severity driver | Statistical-method rigor, but already scoped as diagnostic |
| Deferred residual? | Yes: low-\(\ell\) covariance treatment |
| Diminishing-returns? | Mostly yes unless a formal \(p\)-value is claimed |

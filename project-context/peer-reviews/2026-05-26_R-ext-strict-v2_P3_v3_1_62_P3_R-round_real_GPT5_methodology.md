# P3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v2_P3_v3_1_62
**Wall time**: 155.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=68104, completion=8097, reasoning=7037, total=76201

---

No BLOCKER-grade findings.

## PAPER-GPT-M1 — MAJOR

**Section:** §2.2 “In-sample scoring and held-out validation” vs §6.4(i)  
**Issue:** §2.2 still says each fold “scores the held-out 20% (9,400 spectra)” while reporting union/all-five statistics only possible when all folds score the same 47,000-object pool. The current wording falsely presents the Jaccard statistic as held-out-only validation.  
**Fix:** Rewrite §2.2 to match §6.4(i): full-pool scoring for rank-stability, with a separate held-out-only validation if available. Otherwise recompute the Jaccard statistics on disjoint held-out folds.

## PAPER-GPT-M2 — MAJOR

**Section:** §2.2 threshold policy; Table I caption/footnotes; §3.2–§3.3  
**Issue:** Threshold definitions are internally inconsistent. §2.2 says DESI and SDSS use absolute \(S>5\), but the SDSS headline/native count is \(77{,}905\) at \(S\ge0.1060\) while only 12 sources pass \(S>5\); LAMOST similarly uses top-1% \(113{,}342\) while \(S>5\) gives 2,054.  
**Fix:** Define one primary threshold per survey in Methods and use it everywhere. Put strict-\(S>5\), top-percentile continuity slices, and exploratory tiers in separate rows/tables, then recompute dedup/headline totals for the declared primary catalog.

## PAPER-GPT-M3 — MAJOR

**Section:** Table I; §3.4 Planck CMB; §7 Conclusions  
**Issue:** Planck Path-C arithmetic is inconsistent: Table I lists \(N_{\rm total}=20{,}000\), \(N_{\rm anom}=200\), rate \(1\%\), but §3.4 says the native Path-C model rescored \(2\times10^5\) patches and selected the top 200, which is \(0.1\%\), not \(1\%\). The 37.3M denominator also mixes full catalog sizes with partially rescored SDSS/LAMOST and the old Planck 20k count.  
**Fix:** Use actual Path-C processed denominators consistently. Either call Planck a fixed top-200/top-0.1% cap or select 2,000 patches for top-1%; update total processed counts and rates accordingly.

## PAPER-GPT-M4 — MAJOR

**Section:** Abstract; §5; §6.3 Limitations; §7 Conclusions; Appendix C  
**Issue:** The paper says the canonical Fisher-positive mapping is \(1/\sigma^2=F_0+c\alpha^2\), giving \(\sigma(f_{\rm NL})=8.14\) with \(1\sigma\) envelope \([3.92,8.98]\), but summaries still report the invalid local-linear \(8.27\pm2.37\) and GS \(2.28\pm7.43\) as if they are forecasts. Appendix C also keeps the linear \(\alpha\)-sensitivity table despite the positivity correction.  
**Fix:** Replace all headline/summary forecast numbers with the positivity-respecting envelopes. Move linear values to a clearly labeled legacy/reference paragraph only, or recompute the full sensitivity table from Fisher runs / the \(\alpha^2\) form.

## PAPER-GPT-M5 — MAJOR

**Section:** Appendix C, “Shot-noise sensitivity for sparse anomaly tracers”  
**Issue:** The shot-noise appendix uses \(\sigma(f_{\rm NL})\) baselines \(16.85,12.72,11.71\), inconsistent with the main-text \(8.98/8.43/8.14\) scale. It also describes Fisher-information penalties as degradations while quoting a 15% penalty value \(12.56<12.72\), i.e. an apparent improvement.  
**Fix:** Recompute the shot-noise curves in the same Fisher normalization as §5. State whether the penalty is applied to Fisher information or to \(\sigma\), and ensure degradation increases \(\sigma\); otherwise remove this appendix.

## PAPER-GPT-m1 — minor

**Section:** §5.2 NANOGrav; Appendix D  
**Issue:** The deferred “Savage-Dickey on the existing chain” framing is not generally valid for comparing bounce vs SMBHB if they are non-nested fixed-\(\gamma\) models with different amplitude priors. The existing chain also uses independent per-bin KDE factors, not a joint PTA likelihood.  
**Fix:** Replace “Savage-Dickey” with direct model evidence integrals \(Z_M=\int L(\gamma_M,\log A)\pi_M(\log A)\,d\log A\), or explicitly state the nesting/common-prior assumptions required for Savage-Dickey.

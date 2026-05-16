# P4_v1086_R6 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_1935pt
**Wall time**: 109.3s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=76785, completion=6940, reasoning=5681, total=83725

---

## PAPER-GPT-B1 — BLOCKER — Secs. \ref{sec:sensitivity}, \ref{sec:conclusions}; Table \ref{tab:mc_injection}

**Issue:** Injection-recovery claims are still internally inconsistent: Table reports $A=0.5\%$ with median $+1.73\sigma$, $P(\sigma>3)=0.15$, and $A=0.75\%$ with $P(\sigma>3)=0.55$, but Conclusions still says $P(\sigma>3)=0.03$ at $0.5\%$ and also says the sweep “does not cross $P(\sigma>3)$ at any tested amplitude.” Text also alternates five vs nine amplitudes and $N_{\rm MC,null}=500$ vs 1000.

**Fix:** Replace every stale injection-recovery statement from the canonical `injection_recovery_extended.json`: nine amplitudes, $N_{\rm MC,null}=1000$, $A=0.5\%:P_3=0.15$, $A=0.75\%:P_3=0.55$ / interpolated 50%-recovery threshold near $0.75\%$. Define the exact HC selection once.

## PAPER-GPT-B2 — BLOCKER — Abstract, Secs. \ref{sec:dipole}, \ref{sec:systematic_dipole}, \ref{sec:conclusions}, \ref{sec:namaster_config}

**Issue:** The “same data / MASTER collapse” overclaim persists. Conclusions says the raw pseudo-$C_\ell$ collapses to $-0.12\sigma$ “once MASTER … is applied on the same data,” but the compared quantities differ in mask, monopole subtraction, and input field; the appendix also ambiguously says both the mask and field are $n_{\rm spiral}$-weighted, implying possible double weighting in NaMaster.

**Fix:** Rewrite all remaining “MASTER removes/collapses” language as a three-step chain: monopole subtraction + mask change + MASTER. Add one definitive table giving, for each quoted $C_1$, the exact map, mask, weighting, apodization, monopole treatment, binning, and null.

## PAPER-GPT-M1 — MAJOR — Sec. \ref{sec:signal_hunt}; Table \ref{tab:leg_conf_cross}

**Issue:** The DECaLS non-monotonicity argument overclaims: the sequence $+1.15,+4.53,+0.90,-0.34,+4.06\sigma$ does not “rule out” a primordial dipole by behavior alone. SNR under confidence cuts need not be monotonic when $N$, footprint, morphology mix, dilution, and estimator variance change; the high-confidence DECaLS bin is itself a $+4\sigma$ excursion.

**Fix:** Downgrade to “evidence for footprint/systematics.” If claiming exclusion, fit a common-axis signal+dilution model across bins/legs and report a formal trend or likelihood-ratio test with trials over leg$\times$confidence bins.

## PAPER-GPT-M2 — MAJOR — Secs. \ref{sec:hemisphere}, \ref{sec:hemisphere_disc}, \ref{sec:wtheta}

**Issue:** LEE accounting is incoherent for the hemisphere statistic: Bonferroni/BH gives “$<1\sigma$ consistent with null,” while the direct max-statistic MC gives $p_{\rm LEE}\le10^{-4}$, which already includes the look-elsewhere scan and rejects the random-label null. For the brick-interior $w(\theta)$ test, the arithmetic is fine, but $P(|z|>2.32)\times10\simeq0.20$ is a post-LEE Bonferroni probability, not “pre-LEE.”

**Fix:** Define separate hemisphere observables if they are truly different; otherwise use the direct max-stat MC as the primary LEE result and state the random-label null is rejected, with systematics attribution requiring a systematics-preserving null. Correct the brick pre/post-LEE wording.

## PAPER-GPT-M3 — MAJOR — Secs. \ref{sec:intro}, \ref{sec:comparison}, Conclusions; bibliography Shamir:2022DESI

**Issue:** The Shamir DESI comparator is numerically inconsistent. The paper alternates between “nearly $1.3\times10^6$ spirals” and “$\sim200{,}000$ spirals out of $\sim1.3$M total,” while still quoting a $3.2{\rm M}/1.3{\rm M}\simeq2.5\times$ ratio; if the spiral count is 200k, the ratio is $\sim16\times$.

**Fix:** Decide whether the comparator is Shamir’s total catalog or Ganalyzer spiral subset, cite the exact published number, and recompute all size ratios. Do not use the ratio as sensitivity evidence without matched footprint/selection.

## PAPER-GPT-M4 — MAJOR — Secs. \ref{sec:gz1_joint}, \ref{sec:data_availability}

**Issue:** Reproducibility/versioning and validation denominators are not journal-grade. Manuscript version is v1.0.86, but Data Availability pins code/artifacts to `paper4-v1.0.84` plus vague “successor patch tags,” while HF uses `v2026.04`; the GZ1 section says the 6,637 training objects are excluded and metrics are on 234,282 external matches, but then reports $141{,}438/240{,}919$.

**Fix:** Pin exact Git commit/tag, HF revision SHA, artifact hashes, and row counts for v1.0.86. Recompute or relabel GZ1 metrics consistently as training-excluded or inclusive, with denominators matching every quoted accuracy and $\kappa$.

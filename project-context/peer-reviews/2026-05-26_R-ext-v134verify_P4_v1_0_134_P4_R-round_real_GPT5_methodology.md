# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v134verify_P4_v1_0_134
**Wall time**: 104.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=102519, completion=5628, reasoning=4659, total=108147

---

## PAPER-GPT-B1 — BLOCKER — Conclusions, “Canonical-$N$ MASTER $\ell=1$ direct compute”

Concrete issue: Arithmetic contradicts the claimed canonical-mask $+3.64\sigma$. The listed values $C_1=2.298\times10^{-5}$, null mean $8.004\times10^{-6}$, null std $8.097\times10^{-6}$ give
\[
(2.298e{-5}-8.004e{-6})/8.097e{-6}=1.85,
\]
not $3.64$. Elsewhere the corrected $+3.64$ uses $C_1=1.51\times10^{-5}$, mean $3.12\times10^{-6}$, std $3.31\times10^{-6}$.

Fix: Replace the conclusion/table numeric triplet with the corrected demonopole-subtracted values, or label the current triplet explicitly as the legacy $+1.85\sigma$ baseline. Use one data vector/null consistently.

## PAPER-GPT-M1 — MAJOR — Table I footnote c / Sec. III.E TTA flip propagation

Concrete issue: The hard-label flip variance derivation is wrong. For $p_{\rm flip}=0.214$, $1+4p(1-p)=1.673$ in variance, i.e. $\sqrt{1.673}=1.29\times$ in $1\sigma$, not $1.21\times$; if treated as signal dilution, the correction is $1/(1-2p)\simeq1.75$.

Fix: State whether the flip channel is modeled as added variance or signal dilution, recompute the factor, and update all hard-label diagnostic uncertainties using the corrected propagation.

## PAPER-GPT-M2 — MAJOR — Sec. Sensitivity / Table `mc_injection` / Conclusions

Concrete issue: The injection-recovery MC count is internally inconsistent: text says $N_{\rm MC,null}=1000$ for the canonical extended sweep, while Table IX caption says $N_{\rm MC,null}=500$ for the same `wave_14_nn` table. The same section also calls the $0.75\%$ threshold “systematic-inclusive” despite admitting the per-pixel-shuffle null destroys depth/PSF/morphology covariance.

Fix: Use one MC count per artifact/table. Demote $0.75\%$ to a present-pipeline HC per-pixel-shuffle recovery threshold unless a systematics-preserving injection/null with depth/PSF/morphology covariance is actually run.

## PAPER-GPT-M3 — MAJOR — Sec. Hemisphere Asymmetry / Sec. Hemisphere Discussion

Concrete issue: The hemisphere look-elsewhere treatment is incoherent. The direct max-stat MC gives $p_{\rm LEE}\le10^{-4}$ after scanning directions, while the text also uses an analytic Bonferroni/BH result to call the hemisphere signal “consistent with null after look-elsewhere”; these are different nulls/statistics and cannot both be the operative LEE verdict.

Fix: Pre-specify one hemisphere statistic and one null. If the direct MC max-stat is primary, report random-label-null rejection and reserve cosmological interpretation for a systematics-preserving null.

## PAPER-GPT-M4 — MAJOR — Sec. Monopole+Mask Leakage, boundary-distance variance check

Concrete issue: The new boundary-distance claim says $\langle A_p^2\rangle=\{8.22,7.84,8.62,8.66,8.37\}\times10^{-3}$ is “statistically uniform” and comparable to Poisson scatter, but no shell uncertainties or effective weighted sample sizes are given. Naively, variance-mean SEs for $N_{\rm pix}=\{1940,\dots,16826\}$ are only percent-level, so the $\sim10\%$ range is not automatically negligible.

Fix: Add bootstrap/jackknife/MC error bars and a constant-variance $\chi^2$ or $p$-value. If not consistent, soften to “no strong edge enhancement” rather than “statistically uniform.”

## PAPER-GPT-m1 — minor — Body-text scrub

Concrete issue: Reviewer/tool prose remains visible in the manuscript, e.g. “question raised in ChatGPT M3” in Sec. Mask robustness and “cross-confirmed by Gemini 3.1-Pro and GPT-5” in the dipole footnote.

Fix: Replace with objective scientific wording or move provenance to LaTeX comments/artifact metadata only.

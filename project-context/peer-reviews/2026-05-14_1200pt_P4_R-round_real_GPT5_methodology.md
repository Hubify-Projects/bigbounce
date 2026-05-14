# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_1200pt
**Wall time**: 69.3s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=52236, completion=3529, total=55765

---

## PAPER-GPT-B1 — BLOCKER — Abstract; Sec. “Hemisphere Asymmetry”; Sec. “The 3.05σ Hemisphere Signal”

Concrete issue: The paper says the 3.05σ hemisphere asymmetry “does not survive” look-elsewhere correction, but the direct MC footnote says zero of 10,000 nulls exceed the data, i.e. \(p_{\rm LEE}\le 10^{-4}\), which means it *does* survive at the MC resolution. The amplitude is also inconsistent: text says 0.17%, footnote reports \(\max |A|=8.531\times10^{-3}\) = 0.853%.

Fix: Recompute the hemisphere statistic with one definition of amplitude/significance and one direction grid. If \(p_{\rm LEE}\le10^{-4}\) remains, stop calling it a fluctuation and either identify the systematic or weaken the null claim.

## PAPER-GPT-B2 — BLOCKER — Sec. “Dipole Analysis”, Table 2 / MASTER discussion

Concrete issue: The load-bearing post-MASTER \(\ell=1\) result is not canonical: Table 2 says the “single-mode” row uses an analysis subsample \(n=5{,}547{,}858\), \(f_{\rm sky}=0.659\), while the claimed canonical catalog has \(N_{\rm spiral}=3{,}201{,}160\), \(f_{\rm sky}=0.491\), and the paper admits the canonical-\(N\) \(\ell=1\) recompute is still TODO. The same table reports a \(+6.097\sigma\) low-\(\ell\) bandpower and \(\chi^2/{\rm dof}=161.2/38\), contradicting “all higher multipoles are consistent with null.”

Fix: Run one final MASTER analysis on the exact canonical Catalog C spiral sample, mask, weights, and binning. Report measured \(C_\ell\), null mean, null \(\sigma\), rank \(p\), and do not mix earlier masks/subsamples with the headline statistic.

## PAPER-GPT-B3 — BLOCKER — Sec. “Sensitivity Floor and Minimum Detectable Signal”

Concrete issue: The analytic dipole sensitivity misses a factor of 2. With \(p_{\rm CW}(\hat n)=\tfrac12(1+A\cos\theta)\), the fitted coefficient in CW fraction is \(A/2\), so Eq. (2)’s \(\sigma(A_{\rm dip})=0.048\%\) is the uncertainty on the CW-fraction modulation, not on \(A\); the ideal \(3\sigma\) amplitude floor is \(\sim0.29\%\), not 0.14–0.2%, before mask/\(N_{\rm eff}\) inflation. The empirical injection table also does not support a 0.5% “3σ 50%-recovery threshold”: at \(A=0.5\%\), median significance is only 0.68 and \(P(\sigma>2)=0.18\), with no \(P(\sigma>3)\) threshold reached.

Fix: Define amplitude convention unambiguously and redo the Fisher calculation with the correct factor, active mask, and weights. State the empirical threshold as “\(>0.5\%\)” unless larger injections demonstrate 50% recovery at the claimed sigma threshold.

## PAPER-GPT-M1 — MAJOR — Sec. “The Raw Catalog A Dipole Was Entirely Systematic”

Concrete issue: The paper claims TTA “forces each galaxy to contribute equally to \(N_{\rm CW}\) and \(N_{\rm CCW}\)” and hence \(N_{\rm CW}-N_{\rm CCW}=0\) per galaxy. Eq. (TTA) only symmetrizes probabilities between original/flip evaluations; the catalog uses hard argmax labels, and the observed \(9.5\sigma\) monopole proves nonzero hard-label imbalance remains.

Fix: Remove the per-galaxy cancellation claim. Analyze either soft signed weights \(p_{\rm CW}^{\rm eq}-p_{\rm CCW}^{\rm eq}\) or hard-label counts consistently, and empirically measure residual depth/mask coupling after TTA.

## PAPER-GPT-M2 — MAJOR — Sec. “Sky Region Balance”, Table 3

Concrete issue: The sky-balance table uses a stale snapshot total \(3{,}321{,}795\), not the canonical \(3{,}201{,}160\), while regional uniformity is used as a load-bearing defense of the monopole and dipole null. The claim that affected objects “redistribute uniformly” is asserted, not shown; the canonical per-region recompute is deferred.

Fix: Replace Table 3 with the canonical per-region counts and CW fractions from the exact production catalog. Do not use snapshot regional maxima for Shamir comparisons or systematic-uniformity claims.

## PAPER-GPT-M3 — MAJOR — Abstract; Sec. “Comparison with Shamir”; Conclusions

Concrete issue: The “excluded at \(>5\sigma\)” / “\(\sim20\sigma\) regionally” framing is overclaimed. It compares Shamir’s reported amplitudes to this pipeline’s regional Poisson error while ignoring the paper’s own systematic floor, non-independent classifier/selection differences, stale regional table, and the fact that the empirical dipole recovery threshold is not a Gaussian \(\sigma\).

Fix: Rephrase as an amplitude-level disagreement under the present pipeline unless a common likelihood with matched footprint, selection, classifier systematics, and Shamir’s model is constructed. Use “disfavored by a factor \(\sim6\)–12 in amplitude,” not “excluded at \(20\sigma\).”

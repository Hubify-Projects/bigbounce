# P4_v1057 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_1800pt
**Wall time**: 70.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=56574, completion=3898, total=60472

---

## PAPER-GPT-B1 — BLOCKER — Conclusions enum item 1 / §VIII.B

Concrete issue: The required LEE reframe is still not consistently applied. Conclusions still says “No scale or sky region shows a signal exceeding \(3\sigma\) after look-elsewhere correction,” and §VIII.B concludes “statistical fluctuation,” both contradicting the direct \(10^4\)-MC result: zero nulls reach data, \(p_{\rm LEE}\le 10^{-4}\), post-LEE \(\gtrsim3.7\sigma\) rejection of the random-label null.

Fix: Replace those statements with: the hemisphere max statistic rejects the random-label/permutation null, but is attributed to depth-/label-coupled systematics because independent \(\ell=1\) dipole estimators are null. Do not call it “consistent with null” or a “statistical fluctuation” under that null.

## PAPER-GPT-M1 — MAJOR — §IX.J Sensitivity / Conclusions item 1 / Abstract

Concrete issue: The factor-of-2 amplitude correction is not propagated. Abstract says Fisher floor \(0.29\%\), but §IX.J still derives \(0.14\%\to0.2\%\), and Conclusions still says “statistical-only Poisson floor is \(0.2\%\)” / “\(\lesssim0.2\%\).”

Fix: Under \(p_{\rm CW}(\hat n)=\tfrac12(1+A\cos\theta)\), the fitted CW-fraction half-modulation uncertainty must be doubled for \(A\): \(3\times 2\times0.048\%\simeq0.29\%\). Replace all \(0.2\%\) full-amplitude claims or explicitly relabel them as half-modulation.

## PAPER-GPT-M2 — MAJOR — Abstract / Fig. hemisphere caption / §V.C

Concrete issue: Hemisphere amplitude conventions are arithmetically inconsistent. A CW-fraction half-difference of \(0.17\%\) is not “equivalent” to full dipole amplitude \(A=0.853\%\) by a factor-of-2 convention; \(0.853/0.17\simeq5.0\).

Fix: Define separately the scanned hemisphere statistic, full hemisphere difference, and cosine-dipole amplitude \(A\). Give the actual mask-weighted conversion formula, or remove the claimed equivalence.

## PAPER-GPT-M3 — MAJOR — §V.B Table III / MASTER discussion / Conclusions v1.0.55 paragraph

Concrete issue: The load-bearing MASTER \(\ell=1\) result is still not directly computed on the canonical Catalog C spiral sample. The paper relies on an analytic projection from a different mask/subsample, while Table III/text mix a single \(\ell=1\) mode with \(\ell_{\rm eff}=4\,[2,6]\) bandpowers and even calls \([2,6]\) a dipole estimator despite excluding \(\ell=1\).

Fix: Run the canonical single-mode NaMaster \(\ell=1\) MC on \(N_{\rm spiral}=3{,}201{,}160\), \(f_{\rm sky}=0.491\), or demote MASTER to a non-load-bearing cross-check. Separate single-mode \(\ell=1\) from bandpowers and include null means in the table.

## PAPER-GPT-m1 — minor — Fig. class pie caption / §IV.B

Concrete issue: The caption says the Catalog C CW/CCW fractions are “consistent with exact parity,” but \(0.4974\pm0.000279\) is a \(9.5\sigma\) monopole deviation from \(50/50\).

Fix: Say “near-balanced in amplitude but formally inconsistent with a 50/50 monopole; the dipole estimator is null.”

## PAPER-GPT-m2 — minor — §VIII.A systematic-dipole discussion

Concrete issue: The text says equivariant averaging “eliminates the real-space systematic by construction” and residual bias “cancels to machine precision,” but the downstream hard-label catalog retains a \(9.5\sigma\) monopole and only empirically suppresses the dipole.

Fix: Restrict the construction claim to soft flip-symmetrized probabilities under horizontal reflection. State that hard-label dipole suppression is empirical: \(2.31\sigma\to0.43\sigma\), not machine-precision cancellation.

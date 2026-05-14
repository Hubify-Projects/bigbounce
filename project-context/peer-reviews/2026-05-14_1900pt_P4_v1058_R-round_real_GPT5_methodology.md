# P4_v1058 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_1900pt
**Wall time**: 43.3s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=56970, completion=2552, total=59522

---

## PAPER-GPT-B1 — BLOCKER — §IX / §VIII.B / Abstract / Conclusions: sensitivity floor is still internally inconsistent

Issue: The paper acknowledges the factor-of-2 amplitude convention problem, but the old $0.2\%$ Fisher floor remains in §VIII.B derivation, Conclusions item 1, Motloch comparison, Future Directions, and falsification language. Under $p_{\rm CW}=\tfrac12(1+A\cos\theta)$, the derived $\sigma=0.048\%$ is for the CW-fraction half-modulation, so the full-amplitude $3\sigma$ Fisher floor is $\sim0.29\%$, not $0.14$–$0.2\%$.

Fix: Re-derive §VIII.B with the factor of 2 explicit and replace all remaining “$0.2\%$ statistical floor” claims by “$\sim0.29\%$ Fisher full-amplitude floor”; keep empirical “$>0.5\%$” as the operational floor.

## PAPER-GPT-B2 — BLOCKER — §VIII.B injection-recovery: “systematic-inclusive” sensitivity is overclaimed

Issue: The injection test relabels final Catalog-C galaxies with an artificial dipole, then measures recovery. That tests the map/dipole estimator and per-pixel null, not the end-to-end classifier response to a true image-level chirality dipole; it bypasses classifier confusion, NS routing, confidence-dependent misclassification, morphology coupling, and training-label bias.

Fix: Reframe the injection-recovery result as “catalog-label/estimator-level empirical floor,” not “systematic-inclusive pipeline floor,” unless an end-to-end image/probability-level injection or a confusion-matrix-corrected forward model is added.

## PAPER-GPT-M1 — MAJOR — §IV.B / Table III: MASTER $\ell=1$ methodology is not cleanly specified

Issue: The text alternates between a single-mode $\ell=1$ MASTER result, an $\ell_{\rm eff}=4$ bandpower spanning $\ell=2$–6, and an analytic projection from a different mask/sample. A bandpower excluding $\ell=1$ cannot be described as a dipole estimator, and the canonical $N_{\rm spiral}$ single-mode run is explicitly deferred.

Fix: Separate three quantities: raw pseudo-$C_1$, subsample-mask single-mode MASTER $C_1$, and canonical projected estimate. Delete language calling the $\ell=2$–6 bandpower a dipole estimator; make the direct canonical run a verification item, not part of the primary result.

## PAPER-GPT-M2 — MAJOR — §IV.C / Fig. 7: hemisphere amplitude arithmetic/conventions are inconsistent

Issue: The hemisphere scan quotes a CW-fraction half-difference of $0.17\%$ and “equivalent full dipole amplitude” $A=0.853\%$. For $p_{\rm CW}=\tfrac12(1+A\cos\theta)$ on uniform hemispheres, hemisphere difference is $A/2$ and half-difference is $A/4$, implying $A\approx0.68\%$, not $0.853\%$ unless mask weighting changes the conversion. The conversion is not shown.

Fix: State the exact estimator used to convert hemisphere contrast to $A$, including mask weights; otherwise remove the “equivalent full dipole amplitude” or correct it.

## PAPER-GPT-M3 — MAJOR — §IV.E / Table IV: sky-balance table uses superseded counts for a headline comparator

Issue: The regional balance table uses a snapshot total $3{,}321{,}795$, while the canonical catalog has $3{,}201{,}160$ spirals. The paper uses the maximum regional asymmetry $0.32\%$ as a headline Shamir-comparator, but the canonical per-region recompute is deferred.

Fix: Recompute Table IV from the canonical Catalog-C labels/counts before submission, or demote the $0.32\%$ regional maximum to a non-canonical diagnostic.

## PAPER-GPT-m1 — minor — §VIII.A: overstrong “by construction” cancellation language

Issue: The text says equivariant averaging cancels residual bias “to machine precision” / “eliminates the systematic by construction,” but hard-label Catalog C still has a $9.5\sigma$ monopole and morphology-dependent CW-fraction variation. The later caveat partly fixes this, but the stronger claim remains misleading.

Fix: Say TTA enforces flip-symmetry of soft outputs under the two-pass protocol and empirically suppresses the dipole; do not claim hard-label count balance or complete systematic elimination by construction.

# paper4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P4_v1_0_122
**Wall time**: 83.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=94833, completion=4009, reasoning=3106, total=98842

---

## PAPER-GPT-B1 — BLOCKER — §IX.K / Table X vs §IV.B headline real-space dipole

Concrete issue: The same Catalog C full sample has a headline real-space dipole of `+0.43σ, p=0.30` in §IV.B, but Table X reports “Catalog C full” as `+4.31σ (p=0.001)` under another real-space cosθ estimator. Calling this “estimator definition” is not an adequate reconciliation; it invalidates the claim that the full-catalog real-space dipole is robustly null.

Fix: Recompute both estimators on the identical map/mask/weights/null and show the algebraic relation, or demote the `+0.43σ` headline until the `+4.31σ` full-sample result is explained or removed as a faulty diagnostic.

## PAPER-GPT-M1 — MAJOR — Abstract / §IV.D / §XIII, trials-correction framing

Concrete issue: The paper still says the depth-correlated systematic is “directly confirmed” by the ℓ=2 cross-spectrum, while §IV.D admits the corrected evidence is only suggestive: ℓ=2 cross-spectrum Bonferroni-corrected is only ~2.3σ and the monopole-only post-MASTER empirical rank is ~2.5σ. This overclaims statistical significance and contradicts the R22 softening.

Fix: Replace “confirmed/directly confirmed” everywhere with “favored/suggested”; state that a nuisance-marginalized joint fit is required before excluding a primordial component.

## PAPER-GPT-M2 — MAJOR — §XIII Conclusions, Shamir 2022 1.3M comparator regression

Concrete issue: Conclusion item 2 says Shamir 2022 had “nearly `1.3×10^6` spirals,” contradicting the Introduction and bib note that `1.3×10^6` is the input pool, with only ~200k Ganalyzer-retained spirals. This is exactly the Perplexity R22 M-4 closure and has regressed.

Fix: Change to “`~1.3×10^6` DESI input galaxies, `~2×10^5` retained spirals,” and keep the `~2.5×` ratio tied to the retained-spiral comparator only.

## PAPER-GPT-M3 — MAJOR — §XIII Headline finding vs Table I footnote b / §IV.D

Concrete issue: The Conclusions still state “post-MASTER monopole-only realizations were not computed,” but Table I footnote b and §IV.D say they were computed in v1.0.121 (`master_decoupled_monopole_null.json`). This stale statement breaks the post-MASTER leakage interpretation.

Fix: Delete the stale parenthetical and summarize the computed result: monopole-only post-MASTER explains ~12% of canonical `C1`, leaving ~88% for other systematics.

## PAPER-GPT-M4 — MAJOR — §IX.J / Table IX injection sweep metadata and sensitivity claim

Concrete issue: The injection-recovery sweep is internally inconsistent: prose says `N_MC,null=1000`, Table IX caption says `N_MC,null=500`, and the paper adopts `0.75%` while also disclosing a strict-HC no-pixel-filter sweep giving `1.5%`. The falsification/sensitivity threshold is therefore pipeline-choice dependent but is presented as canonical.

Fix: Split the three sweeps into separate rows with exact sample predicate, pixel cut, `N_MC`, artifact, and threshold; quote the operational sensitivity as a range `[0.75%, 1.5%]` unless a single predeclared production predicate is justified.

## PAPER-GPT-m1 — minor — §XIII / §IV terminology, “systematic-inclusive” injection floor

Concrete issue: Several places call the per-pixel-shuffle injection threshold “systematic-inclusive,” then immediately admit the null destroys depth/PSF/morphology covariance. That is not systematic-inclusive; it is an empirical statistical/null-pipeline threshold.

Fix: Replace “systematic-inclusive” with “per-pixel-shuffle empirical” throughout, and reserve “systematics-inclusive” for a null preserving depth/PSF/morphology covariance.

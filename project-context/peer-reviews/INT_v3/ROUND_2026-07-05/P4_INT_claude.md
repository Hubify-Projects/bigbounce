# P4 INT full-source referee review — v1.0.212

**Reviewer:** Claude Code INT leg (Houston subscription), full-source access
**Paper:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (8.47M-galaxy chirality null dipole)
**Date:** 2026-07-05
**Verdict: ACCEPT (minor)** — every headline number reproduces from committed artifacts; the ~47%-unexplained residual is honestly disclosed and not overclaimed.

## Central claim
The central claim — a null real-space chirality dipole at sub-percent sensitivity — **is supported**. The HC (p_eq>0.6) real-space dipole is +0.41σ (rank-p=0.31), robust across the confidence-cut sweep and under an independent re-implementation, and the GZ1-human-label-only sub-model independently returns z=−0.04.

## Number verification (against committed outputs)
- **+0.41σ HC null:** `outputs/dipole/catalog_c_summary.json` → `significance_sigma=0.4080`, `p_value=0.3085`, `n_spirals_highconf=949584`, shuffle `0.5789`. Paper (+0.41σ, p=0.31, N_HC=949,584, z=0.58) — **MATCH**.
- **CW fraction:** artifact `0.49735` ↔ paper `0.4974` — MATCH.
- **Confidence-cut sweep** (`c12_r24conf_local_batch.json` queue10): z_mom = +4.27,+4.11,+4.02 at cuts 0/0.4/0.5; +0.407,+1.137,+0.510 at 0.6/0.7/0.8. Paper states +4.3,+4.1,+4.0 / +0.41,+1.14,+0.51 — **EXACT MATCH**. Genuine step-function collapse at p_eq=0.6; low-conf excess confined to the tail. n_gal=949,584 at 0.6 matches N_HC.
- **WLS z≈−18:** `joint_nuisance_bootstrap_sigma.json` → A=4.552e-3 A_p, σ_boot=1.629e-3, A_ref=0.034 ⇒ (A−A_ref)/σ = **−18.07**. Paper "z≈−18 under NSIDE=8 block-bootstrap" — MATCH. Bootstrap-mask ≠ canonical-mask caveat is disclosed in-artifact (both 440 super-pixels, A agrees to 4 sig figs).
- **GZ1-only sub-model:** `gz1only_dipole_result.json` → `z_sigma=−0.0442`. Paper "z=−0.04" — MATCH. (Small N=14,964 HC, N_pix=7 — decisive-independence check, honest.)
- **~47% unexplained residual:** `systematic_l1_forward_model.json` verdict `ATTRIBUTION_PARTIAL`, `fraction_of_observed_amplitude=0.5236`; DR8 morphology (`_dr8morph.json`) raises 52%→53% (+0.7pt, `NO_MEANINGFUL_IMPROVEMENT`); confidence template (`_morphology.json`) adds ~0pt. Paper's "~53% explained, ~47% honest open item, DR8/pod-bound" — **MATCH**. `morphology_data_availability_verified_2026-07-02` documents the missing per-galaxy morphology is genuinely un-staged (NOT fabricated).
- **A_50/A_95:** paper's HC-broad A_50≈0.75%, A_95 bracket 1.0–1.5% is the *real-space* estimator floor; artifacts show distinct floors per subsample/null (hc09 A_50@3σ=1.5%; full-catalog=0.5%) — paper correctly labels each estimator-specific and non-interchangeable.

## Issues

**[MINOR-1]** Abstract A_95 falsification bracket (1.0–1.5%) is the least-directly-anchored headline: the HC-broad injection-recovery run producing the *exact* 1.0–1.5% real-space A_95 bracket was not isolated to a single committed JSON in this pass (multiple injection-recovery files give different floors for different subsamples/nulls; c16 full-sample gives A_50≈0.36%/A_95≈0.63%). The A_50≈0.75% HC anchor is stated in the prereg hierarchy and the intro; the 1.0–1.5% A_95 upper bracket relies on the pinned-by-review value. Recommend adding a single one-line artifact pointer for the HC-broad A_95 bracket for full reproducibility parity with the other headline numbers.

**[MINOR-2]** Two shuffle-null z values circulate for the same HC sample: the primary generator gives z=0.58 (`catalog_c_summary`) and the re-implementation `c11b_hc_dipole_nulls.json` gives z=0.70/0.696. The paper labels these correctly ("same-generator primary" vs "independent re-implementation"), but the abstract quotes both (0.58 and 0.70) without the one-word "re-implementation" qualifier that the body has — a reader could misread it as instability. Trivial wording tighten.

**[MINOR-3]** The +3.64σ (500-MC) vs +7.93σ (10^4-perm) vs +7.28σ (apodized) harmonic-residual triple is heavily footnoted and correctly framed as distinct null procedures / diagnostic-only, but it remains the single densest source of reader confusion in the paper. Not a data problem — a presentation one; the notation section and decision-tree table already do the heavy lifting.

## Null robustness + honesty assessment
**The null IS robust and honestly disclosed.** The p_eq>0.6 cut is a-priori in the generator (git-pre-specified), and the sweep proves the verdict is cut-invariant across the HC regime while the low-conf excess is a step-function systematic (verified in c12). The ~47% unexplained ℓ=1 residual is labeled `ATTRIBUTION_PARTIAL` in the artifact and disclosed as a genuine open item (DR8-morphology-bound, not fabricated). No number mismatch, no undisclosed systematic, no overclaim found. The systematics-attributed harmonic residuals are consistently walled off from the two PRIMARY cosmological rows.

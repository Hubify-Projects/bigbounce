# INT Claude-subscription Review — P4 v1.0.239 — claude-opus-4-8
paper: P4  version: v1.0.239  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-13T07:43:07Z
context-note: M18

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've completed a full read and verified every headline number against the committed artifacts (recomputed, not just read). All primary numbers reproduce: primary dipole `+0.41σ, p=0.31` (`catalog_c_summary.json`); WLS `z≈−7.6`, best-fit `0.455%`, `σ_boot=1.63e-3` (`joint_nuisance_bootstrap_sigma.json`, with the old `z≈−18` correctly retired as a factor-of-2 error); `A₅₀≈0.75%`, `A₉₅∈(1.0,1.5]%` (`c16_r24conf_pod_batch.json`); GZ1-human-only null `z=−0.54` (`gz1only_fullN_dipole_result.json`); monopole leakage `99.32%`, residual `+1.69σ` (`monopole_mask_null_results.json`); harmonic `+7.31/+7.93σ` (`c9a_10k_nulls.json`); and the newly-folded e2e transfer function `T_raw=0.2303`, `T_eq=0.9997` (`e2e_transfer_function_full.json`). No fabrication detected.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MINOR]** Abstract, `chirality_catalog_paper.tex:659` (and Sec. notation `:738`): the WLS statistic `z≈−7.6` is placed prominently in the abstract, but it is explicitly *not* a calibrated frequentist significance (it is a block-bootstrap template-disfavor moment-ratio). A reader skimming the abstract will misread it as a `7.6σ` exclusion. Demote the numeral or attach the "template-disfavor, not a frequentist exclusion" qualifier inline at first mention in the abstract, as is done later at `:676`/`:738`.

2. **[MINOR, borderline MAJOR]** Pseudo-label independence, `:1101–1104`: 66.5% of training labels are CE-ResNet pseudo-labels, so the shuffle/permutation nulls randomize the model's own outputs. The only fully model-free cross-check (GZ1 human votes, `N=46,017`) is ~4.5× coarser (`A₅₀≈3.4%`) than the headline HC sample, so the *sub-percent* null is not independently validated at sub-percent scale by any model-independent estimator. This is honestly disclosed and bounded a-fortiori by the template-agnostic block-bootstrap + injection floor, which is a valid argument — but it is the paper's load-bearing residual limitation and should remain unmissable in the abstract, not only in Sec. VII.

3. **[MINOR]** WLS reproducibility, `:959` and Appendix D: the paper states the block-bootstrap WLS operates "on the full canonical-mask `A_p` field," but the committed `σ_boot` artifact (`joint_nuisance_bootstrap_sigma.json`) uses a `|b_gal|>15°` galactic-latitude mask, not the canonical `N_spiral≥10` mask. The artifact self-documents consistency to 4 significant figures (both give 440 super-pixels, `A_dip=4.55e-3`), but the paper text does not carry that mask-equivalence note — a referee reproducing the `z≈−7.6` from the stated mask would hit a definitional mismatch. Add the equivalence statement to the paper.

4. **[MINOR]** e2e transfer function, `:1183–1187`: the text says the probability antisymmetry `T_eq=0.9997` is "verified numerically image-by-image on all `8.47×10⁶` galaxies," but the artifact shows the `T_eq` flip-recovery statistic is computed over the `3,201,201` equivariant CW/CCW spiral pairs (`n_pairs_eq`), while only the probability-vector antisymmetry check spans all 8.47M. The wording conflates the two sample sizes; separate them.

5. **[MINOR]** Presentation density, pervasive (e.g. abstract `:659`, notation `:734–738`, decision-tree `:752–776`, Reader's note `:1012`, conclusions `:1277`): the caveats "not directly comparable as detection significances / systematics-attributed / a matched-footprint Ganalyzer reanalysis is required" are restated well over a dozen times across abstract, notation, three table captions, two "Reader's notes," and the conclusions. Even at the mandated ≤25 pp the manuscript reads as internally self-justifying. Consolidate to a single canonical statement (Sec. notation) with cross-references, per the paper's own stated intent.

6. **[MINOR]** Title (`:649`) vs. scope: "8.5 Million DESI Galaxies" is the classified-catalog size, whereas the primary null rests on `N≈9.5×10⁵` HC spirals (or 3.2M full-catalog spirals). The abstract clarifies this, but the title mildly overstates the sample entering the headline measurement.

**(3)** Yes — the central claim (the large-scale morphological chirality dipole is consistent with null at sub-percent sensitivity, with a genuine Shamir-scale dipole excluded by injection-recovery) is supported: every primary number reproduces against the committed artifacts, the WLS factor-of-2 error has been correctly fixed, and the classifier's modest accuracy and pseudo-label dependence both bias the estimator *toward* null, making the non-detection conservative rather than optimistic.

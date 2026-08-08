# INT Claude-subscription Review — P4 v1.0.235 — claude-opus-4-8
paper: P4  version: v1.0.235  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T02:31:03Z
context-note: Wave-1 stability re-test at current version; no changes since last review

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've read the full paper, cross-checked the disposition ledger for the correct paper (P4), and verified the load-bearing numbers against the committed artifacts (`catalog_c_summary.json`: σ=0.4080→+0.41, p=0.3085→0.31, shuffle z=0.5789→0.58, 10⁴ realizations; counts arithmetic and binomial σ=0.000279 reproduce; Shamir A_ref=0.017 / z≈−7.6 and naive-WLS z=−112 reproduce from the disclosed inputs). Here is my referee report.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES**

1. **[MINOR]** *Unmodelled ~47% harmonic residual — physical origin unresolved* (`chirality_catalog_paper.tex:628`, `:1025`). The imaging+morphology forward model accounts for only ≈52–54% of the post-MASTER ℓ=1 residual amplitude (`systematic_l1_forward_model_dr8morph.json`, 53.0%, cosθ=+0.84), leaving ~47% as an explicit open item whose systematic-vs-signal origin the paper cannot close in-repo. The *a-fortiori* bound (entire residual A_p=0.695% < A₅₀=0.75% < A₉₅∈(1.0,1.5]%) is valid and correctly insulates the primary null, so this is not fatal — but a PRD referee will want the depth-conditioned per-pixel classifier-purity map the paper itself names as the closing computation, or a sharper statement that it is deferred. Disclosed but genuinely open (DP4-17).

2. **[MINOR]** *Spatially-resolved confusion matrix absent* (`:845`, `:1078`). The dipole-bias argument relies on the CW↔CCW error asymmetry being null in every GZ1 stratum (Appendix B, ≲1.4 pp) plus the model-free GZ1-human null. That is a strong mitigation, but there is still no confusion matrix as a joint function of position/depth/PSF/confidence, so a spatially-varying *asymmetric* misclassification cannot be excluded at the map level, only bounded globally. Honestly disclosed (DP4-15); a referee would ask this be foregrounded as a stated limitation on the central claim rather than only in §sensitivity.

3. **[MINOR]** *Presentation density / length* (`:623`–`:631`, whole document, 37 pp). The abstract is a ~200-word block dense with parenthetical caveats and unit-mapping asides; the main text carries heavy `\artifact{}` code-path density inline. The science is correct, but the load-bearing single message (null real-space dipole; harmonic channel is a diagnostic) is harder to extract than it should be. PRD would request tightening (relegate unit-derivation asides and artifact paths to appendices/Data Availability).

4. **[MINOR]** *p_eq>0.6 primary-sample cut* (`:713`–`:715`). The high-confidence cut is the "first threshold at which the low-confidence excess disappears," i.e. outcome-adjacent. The paper adequately defends it (pre-specified in §prereg, stable across p_eq∈{0.6,0.7,0.8}, and — decisively — the calibration-free GZ1-human-only null returns the same result), so this is disclosed-and-answered (DP4-07); noting for completeness, no action strictly required.

No MAJOR issues: I found zero genuinely-new correctness defects. Every number I recomputed matches the committed artifacts, the Shamir factor-of-2 is correctly handled (A_p = 2(f_CW−½) with Shamir's asymmetry mapped 1:1, no double-count), and the σ-incommensurability caveats are stated consistently and repeatedly. The ChatGPT-style "z≈−7.6 is really ~1.4σ under g-dilution" and "62% not 47%" reframes are definitional, not defects (the paper labels z a template-disfavor statistic, not a detection significance, and bounds the *entire* residual below A₉₅).

**(3)** Yes — the central claim (a null chirality dipole at sub-percent sensitivity) is supported: it rests on the primary real-space HC estimator (+0.41σ, p=0.31, verified against artifact) and the fully model-free GZ1-human-only cross-check (z=−0.54σ), both of which bypass the systematics-dominated harmonic channel, so the unresolved residual and missing spatial confusion map are honestly-disclosed limitations rather than threats to the conclusion.

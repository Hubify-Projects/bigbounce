# INT Claude-subscription Review — P5 v0.1.118-2026-07-10 — claude-opus-4-8
paper: P5  version: v0.1.118-2026-07-10  tex: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T03:44:50Z
context-note: W2 confirm wave on v0.1.118; no changes since last review

======================================================================
RAW RESPONSE (verbatim):
======================================================================

All arithmetic confirmed (0.9/0.3982=2.26; 2×0.6991−1=0.3982; class range 1.98 pp). I have verified the load-bearing numbers directly against the committed artifacts. Here is my referee report.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES**

1. **[MINOR] Abstract contradicts the body and the committed artifact on the environment-stratified confusion matrix.** `p5_desi_chirality.tex:786` — the abstract states the physical-chirality de-attenuation "carries additional uncertainty from environment-dependent relabeling (**no environment-stratified confusion matrix is available**; §limitations/App A)." This is now false. The body it cites (§Limitations, `:4559`–`:4568`, and Discussion `:4448`–`:4459`) says the void/non-void stratum "**is now measured directly**" and reports it (void N=933, err-asym −0.023; non-void N=5,778, −0.005; diff −0.018, z=−0.89, p=0.37; nulls across all three void definitions p=0.25/0.66/0.19). I verified every one of those numbers against the committed artifact `pipelines/p2_chirality/outputs/gz1_stratified_confusion.json` (`stratified_by_environment_void_P5: {"status": "COMPUTED"}`, dated 2026-07-11) — they match exactly. The abstract's parenthetical is a stale disclosure that both contradicts the section it points to and *undersells* the paper's own now-computed, null-corroborating evidence. Fix: change the abstract to reflect that the void-axis stratum is now directly measured and consistent with symmetric error, or (weaker) qualify it to the remaining un-stratified residual. This is the only substantive item; it is presentation-level, not a result error.

2. **[MINOR] Residual stale changelog framing in the source header.** `p5_desi_chirality.tex:70` — the v0.1.116 changelog comment still asserts "The void/non-void environment stratum remains HONESTLY not-yet-computed," which is superseded by the now-computed matrix integrated into the body. Comments don't render, but this is the same drift that produced issue #1; the source-of-truth note should be reconciled so a future editor doesn't re-propagate the "unavailable" wording.

**Numbers I recomputed against committed artifacts and confirmed correct (no action):** primary footprint-restricted contrast Δf_CW=+0.0018, z=+0.78, p=0.43, n_void=57,081, n_non-void=253,276 (`29_ext3…json`); k=20 secondary Δf=+0.0007 with n_non-void=678,945−56,981=621,964; GALZONE V2-REVOLVER Δ=−0.0037/|z|=1.25/p=0.21/n=104,912 vs 40,877 and V2-VIDE Δ=+0.0019/z=0.72/p=0.47 (`30_ext4…json`); GZ1 error-asymmetries by imaging-leg (+0.0042 / −0.0020) and confidence (−0.0019 / +0.0065) with CIs; accuracy 0.91→0.96 at conf>0.6; de-attenuation 0.9/0.3982=2.26 pp; 2a−1=0.3982; per-class range 1.98 pp; χ²=3.55 homogeneity. All consistent.

**(3)** Yes — the central claim (no void/non-void environmental dependence of classifier-labelled spiral chirality, |Δf_CW|≤0.004 across all five DESIVAST definitions, bounded to ≈0.9 pp / ≈2.26 pp de-attenuated) is fully supported by the committed artifacts; the only fix needed is a stale abstract sentence that now contradicts the paper's own strengthened evidence.

Best Next Steps
- Edit `p5_desi_chirality.tex:786` to state the void-stratum confusion matrix is now directly measured and null (bump to v0.1.119, directive-G PDF hygiene: recompile, re-mirror, Convex `paperVersions:bump`).
- Reconcile the `:70` changelog note in the same bundle so the "not-yet-computed" framing doesn't re-propagate.
- Re-test P5 for the clean-wave count after the edit (directive K).

Say `continue` and I will take the next best scoped step.

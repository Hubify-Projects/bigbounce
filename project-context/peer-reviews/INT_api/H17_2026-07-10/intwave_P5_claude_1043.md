# INT Claude-subscription Review — P5 v0.1.125-2026-07-12 — claude-opus-4-8
paper: P5  version: v0.1.125-2026-07-12  tex: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T17:43:00Z
context-note: rebuild wave on v0.1.125: overhaul-introduced pre-declared/post-hoc contradiction fixed (DP5-24, git-proven origin); no other changes

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've verified the manuscript's key numbers against the committed artifacts and confirmed the v0.1.125 fix. Verification results:

- **Primary result** `Δf_CW=+0.0018, z_Δ=+0.78, p_Δ=0.43, n_void=57,081` → matches `outputs/29_ext3_desivast_footprint_retabulation.json` exactly (nonvoid−void = 0.498279−0.49647 = 0.001809; z=0.781; p=0.4349; n_void_exact=57081). ✓
- **RSD reconstruction** `−0.069pp→−0.045pp, |shift|=0.024pp, MC +0.026±0.049, |z| 0.32→0.18` → matches `outputs/27_rsd_void_recon_bound.json`. ✓
- **Systematic quadrature** `√(0.44²+0.37²+0.60²+0.37²+0.11²+0.24²+0.02²+0.02²)=√0.898=0.94≈0.9pp` → recomputed, correct. ✓
- **De-attenuation** `0.9/0.3982≈2.26pp` with `2a−1=0.3982` from `a=0.6991` → correct. ✓
- **DP5-24 fix** (sole v0.1.125 change): abstract L787 now reads "designated-primary (exploratory, not pre-registered)", consistent with §V.B L1402-1404, §V.B L1518-1520, and Conclusions L4454-4456. No residual "pre-declared"/asserted-pre-registration contradiction anywhere in the body. ✓

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MINOR]** Abstract, `p5_desi_chirality.tex:785` and title-macro `:24` — the companion Paper IV is cited via the unresolved placeholder `\paperIVarxiv = arXiv:XXXX.XXXXX`. The headline is correctly argued to be monopole-invariant and to depend only on the public `class_eq` labels (verified in §II/App A), so this is a citation-timing issue, not a scientific dependency — but a live arXiv identifier must replace the placeholder before publication.

2. **[MINOR]** Abstract, `:789-791` — the estimand is described as the "void-vs-non-void CW-fraction contrast Δf_CW = +0.0018", but the committed artifact stores this as `delta_f_cw_nonvoid_minus_void = +0.001809` (non-void minus void). The magnitude, z, p, and null verdict are unaffected, but the sign label ("void-vs-non-void" with a `+` sign) is the reverse of the artifact's stated ordering; state the subtraction convention explicitly to avoid ambiguity.

3. **[MINOR]** RSD scope wording, `:2572-2576` vs artifact verdict string — the paper correctly labels the reconstructed contrast as the *unrestricted* void contrast (n=678,987, n_void=57,058, no footprint mask), but `outputs/27_rsd_void_recon_bound.json`'s own `verdict` field calls it "the footprint-restricted primary Δf_CW". The paper text is the honest/correct one; the artifact's internal label should be reconciled so the reproducibility trail is unambiguous.

4. **[MINOR]** De-attenuated physical bound, abstract `:807` (≈2.26 pp) — this converts the classifier-labelled bound via a single scalar attenuation factor `2a−1≈0.40` tied to the 69.91%/κ=0.40 GZ1 floor. This is disclosed as a proxy, but the linear-attenuation model assumes label errors are parity-symmetric; the paper supports that with the GZ1-overlap stratified confusion matrix (err-asymmetry consistent with zero), so the assumption is defended — worth a one-line forward-pointer to that support at the abstract site.

**(3)** Yes — the central claim (no environment-conditional spiral-chirality signal, bounded at ≈0.9 pp on the classifier-labelled fraction / ≈2.26 pp de-attenuated, with the family-wise Bonferroni-5 DESIVAST null and the RSD-reconstruction bound both verified against the committed artifacts) is supported and honestly scoped; the residual items are structural/disclosure-level (unresolved companion arXiv ID, sign-label clarity), not defects in the result.

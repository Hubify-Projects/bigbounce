# P4 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v3_P4_v1_0_138
**Wall time**: 17.2s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=96303, completion=2100, reasoning=1356, total=98403

---

**PAPER-GRO-B1**  
**BLOCKER** — Abstract + title (lines ~80-120)  
Title and abstract headline "No Evidence for Large-Scale Parity Violation" while the observable is explicitly parity-EVEN axial-vector dipole (ℓ=1). The paper itself notes prior literature conflates the channels. This framing is false confidence and risks misleading readers.  
Fix: Retitle to "No Evidence for Large-Scale Isotropy Violation in Projected Galaxy Chirality Dipole" and qualify the abstract's first paragraph with the parity-EVEN scope in the lead sentence.

**PAPER-GRO-B2**  
**MAJOR** — §VI.D + v1.0.137 joint-fit paragraph (around line 1400+)  
The joint nuisance-marginalized fit claims "FORMALLY EXCLUDED at 99% confidence" for interpretation (i) at 1.7%. The 9-template design matrix has explicit collinearity (leg fractions + constant offset) and the 15-cell leg×conf extension shows large residuals (|z| up to 26). The 0.23% residual dipole is still detected at z=+40.9.  
Fix: Change to "disfavored at >99% under the 9-template nuisance model; a full morphology/PSF/depth template regression is required for formal exclusion."

**PAPER-GRO-B3**  
**MAJOR** — Abstract + §IX (sensitivity claims)  
Abstract and falsification criterion cite the empirical 0.75% 50%-recovery-at-3σ threshold as the operational floor while the Fisher asymptote is 0.29% full-amplitude. The GZ1 agreement (69.91%, κ=0.40) implies ~0.63 dilution but is not folded into the headline sensitivity or falsification criterion.  
Fix: Report both numbers side-by-side in the abstract and state the empirical threshold already includes classification noise; remove the 0.29% figure from the falsification sentence.

**PAPER-GRO-B4**  
**MAJOR** — §4.4 + canonical-mask +3.64σ verdict (multiple sections)  
The +3.64σ canonical residual is attributed to depth/morphology systematics on the basis of cross-spectrum, leg proxy, and density-stratified null. All three anchors are suggestive (family-wise ~2.4σ, leg-proxy not a lower bound, density-stratified still leaves +3.80σ). No full template regression is performed.  
Fix: State "favored interpretation (ii) at ~2.4σ family-wise significance; a joint model comparison with full morphology templates is required to confirm."

**PAPER-GRO-B5**  
**minor** — Introduction + §shamir (Shamir comparison)  
The paper states the result is inconsistent with Shamir 2020/2022 by factor ~6-12 "under the present ViT/TTA pipeline and selection" but repeatedly disclaims a likelihood-level exclusion. The amplitude difference is load-bearing for the narrative yet the disclaimer is buried.  
Fix: Move the "no likelihood-level exclusion" sentence into the abstract and lead comparison paragraph.

**PAPER-GRO-B6**  
**nit** — Entire document (LaTeX comments)  
~200 lines of version-history and "R-ext-vXXX 5/5-clean" closure prose in comments. This is invisible in the PDF but reveals the manuscript was iteratively rewritten to satisfy prior AI reviewer packages rather than written from first principles.  
Fix: Strip all review-closure prose from the source before final arXiv upload; retain only scientific changelog.

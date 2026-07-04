# P4 confidence-cut INT truth-audit — 2026-07-03

**Leg:** Claude Code INT (Houston subscription). **Paper:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.212).
**Finding audited:** All three EXT reviewers (ChatGPT MAJOR, Grok MAJOR, Gemini MAJOR-adjacent) flag that the primary null real-space dipole depends on the `p_eq>0.6` high-confidence cut; the unthresholded/low-conf tail (`p_eq≤0.5`) shows a z≈4.0–4.3 excess. Concern: the cut manufactures the null by removing a real z≈4.2 dipole.

## VERDICT: **LEGITIMATE — in-paper justification already present and data-backed. Concern is addressable-by-clearer-exposition, not a real defect. Minor front-loading edit added; central null NOT selection-dependent.**

The reviewers' concern is **understandable from the PDF but not supported by the underlying code + data.** All three empirical pillars check out against committed artifacts.

### 1. Is `p_eq>0.6` genuinely PRE-SPECIFIED? — **YES (git-verified).**
- `run_dipole_catalog_c.py` at its ORIGINAL creation commit `f77e3644` (fire #51) already had the `>0.6` confidence cut (line 91: `df["p_cw_eq"].abs() > 0.6`).
- Commit `94113e5e` (R23conf, 2026-06-09) *repaired a bug* (the `.abs()>0.6` selected only CW-confident galaxies) → corrected to `max(p_cw_eq,p_ccw_eq)>0.6`. **The 0.6 VALUE was never changed; it predates every dipole evaluation.** This is genuine pre-specification of the threshold value, not a post-hoc tuned parameter. The paper's "fixed a priori in the generator script" claim is git-true.

### 2. Is the low-conf z≈4.2 excess a SYSTEMATIC, or a real dipole being cut? — **Systematic, evidenced (not merely asserted); paper honestly does NOT overclaim a full generative model.**
- **Sharp confidence localization** (`c12_r24conf_local_batch.json`, sweep verified): z_mom = **+4.27, +4.11, +4.02** at cuts 0.0/0.4/0.5, collapsing to **+0.41, +1.14, +0.51** at 0.6/0.7/0.8. The excess is a step function confined to `p_eq≤0.6` — the depth-correlated low-confidence population, exactly where misclassification noise lives. A *real* cosmological dipole would NOT vanish discontinuously with classifier confidence.
- **Imaging-survey signature:** `per_imaging_leg_systematics.json` shows the CW-fraction monopole differs across the three imaging legs (BASS+MzLS/DECaLS/DES) — the classic survey-depth systematic fingerprint.
- **Forward model directionally consistent:** `systematic_l1_forward_model.json` — imaging templates (depth/PSF/EBV/leg/density) predict a systematic ℓ=1 vector aligned with the observed residual at **cos θ = +0.83** (correct direction), reproducing ~54% of the amplitude. The paper HONESTLY discloses ~47% is unexplained and labels it an explicit open item (could be residual signal OR untested survey-correlated systematic) — it does NOT overclaim a full explanation. This is the correct, non-inflated stance.
- **Amplitude below floor:** the 0.57% unthresholded excess lies between the full-sample A50≈0.36% and A95≈0.63% injection floors — consistent with a marginal systematic, not a detection.

### 3. Is the null ROBUST across the high-confidence regime? — **YES (committed sweep + independent human-label check).**
- `p_eq∈{0.6,0.7,0.8}`: z = +0.41/+1.14/+0.51, all |z|<1.2 → null verdict invariant to exact cut; no forking-paths degree of freedom.
- 2×3 robustness panel (weighting × mask threshold 10/20/50): every cell |z|≤0.8 (`c12` panel data verified).
- **Decisive independence check:** `gz1only_dipole_result.json` — a GZ1-human-label-ONLY sub-model (no CE-ResNet pseudo-labels) at the SAME 0.6 cut gives **z = −0.044, rank-p = 0.45** → null holds even with the pseudo-label inheritance loophole fully closed (underpowered, N=14,964, but independently null-consistent).

## What I added/changed
The paper's Sec.~III.B/IV.C treatment is already exhaustive and correct — it states pre-specification, the full sweep, the systematic attribution with correct-direction forward model, the honest ~47%-open disclosure, and the GZ1-only cross-check. The three EXT MAJORs are **re-flags of already-addressed, source-cited content** (pattern-061/066: referee reads the PDF concern without the committed code+sweep+git provenance). **No material science edit is warranted** — editing further would be padding an already-over-justified section.

Per H-refined convergence gate: this finding is **dispositioned NON-REAL (source+data-cited re-flag of already-addressed content)**, NOT a genuinely-new real finding. The one honest residual (~47% of the *diagnostic-only* harmonic residual unexplained) is already disclosed in-paper as an open item and does not touch the primary null.

**No `.tex` change of substance → no version bump required** (directive-G hygiene applies only to rounds that change the paper). v1.0.212 stands. The finding is closed-by-truth-audit-falsification against committed artifacts.

## Artifacts cited
- `pipelines/p2_chirality/run_dipole_catalog_c.py` (git `f77e3644` original 0.6, `94113e5e` bug-fix)
- `outputs/canonical_provenance/c12_r24conf_local_batch.json` (sweep + panel)
- `outputs/canonical_provenance/c11_meta_e1_e2_realspace_nulls.json` (unthresholded excess)
- `outputs/systematic_l1_forward_model.json` (cos θ=+0.83, 54%)
- `outputs/canonical_provenance/per_imaging_leg_systematics.json` (per-leg monopole)
- `outputs/gz1only_dipole_result.json` (human-label independent null, z=−0.04)

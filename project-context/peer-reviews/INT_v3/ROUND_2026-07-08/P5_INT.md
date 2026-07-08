# P5 INT — full-source regression check (v0.1.107)

**Reviewer:** Claude Code INT (subscription subagent, full-source read — CLAUDE.md I1)
**Scope:** closure-wave regression check only (scoped headline + post-hoc caveat + RSD bound consistency). No new-finding hunt.
**File:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`

## Verdict: CLOSURE WAVE CLEAN — no regressions

### Scoped headline — consistent
- Title (L648): "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Void Null Test on 56,981 DESI DR1 Spirals."
- Abstract headline (L657, sharpened in v0.1.107): "spiral galaxy chirality shows no **void/non-void** [difference]" (was "no environment [difference]" — narrowed to the actual estimand). Δf_CW = +0.0007 (z_Δ=+0.31, p_Δ=0.76). Framed as a **bounded null** (L665, `\emph{bounded null}`).
- Family-wise conclusion (Bonferroni-5 uniform null across all 5 DESIVAST void definitions, |z_Δ|≤1.25) promoted as the robustly-quotable headline; the DESIVAST-anchored primary path is explicitly the post-hoc one. Consistent between abstract and §primary_path.

### Post-hoc caveat — consistent and repeated
- Abstract L659: "(primary path, DESIVAST-anchored, **post-hoc designated**)"; L672 "the **post-hoc** primary … disclosed."
- L696–718: "Independence from Paper IV internals"; "**post-hoc** in the strict sense that no timestamped plan predates [the data]"; robustly-quotable statement handed to the family-wise Bonferroni-5 null, not the single post-hoc primary. No claim of blind/pre-registered analysis anywhere. Consistent throughout.

### RSD bound — consistent everywhere
- Abstract L674: "All T-Web findings are **redshift-space statements**."
- L938–941: "all null tests inherit redshift-space distortion (RSD) effects, and the headline environment-independence statement is therefore a **redshift-space statement**" → §limitations anisotropic-tidal-tensor / scalar-σ_v RSD decomposition.
- v0.1.107 closure ADDED: fixed-void-geometry RSD stress test (void memberships under maximum plausible RSD displacement), with the explicit disclaimer "We do not claim full RSD immunity," and labels the diagnostic path "(diagnostic, redshift-space only, not load-bearing)." Reinforces the bound; introduces no over-claim.

### v0.1.107 closure edits (commit 428d132e)
Version bump + additive scope-hardening prose only: headline narrowed to void/non-void, post-hoc designation made explicit, family-wise Bonferroni-5 null promoted, RSD stress-test + non-immunity disclaimer added, `\paperVersion` tag references. **Zero science numbers changed** (Δf_CW, z-values, N=56,981/46,017, ±4.8pp, χ²=3.55 all intact).

Regressions: **none**.

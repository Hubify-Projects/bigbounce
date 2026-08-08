# INT API Review — P2 v1.7.120 — gemini (gemini-3.1-pro-preview)
paper: P2  version: v1.7.120  model: gemini-3.1-pro-preview
provenance: commit=worktree  pdf=research/focused_paper_source_integration/02_full_draft.pdf  sha256=2111e62f6eb2423dc1880fad5fa90c8da1feac75ff4b44891573f6d90762cc06
modality: native-PDF (inline_data base64)
UTC: 2026-07-14T18:39:52.560307Z  |  latency: 20.2s  |  attempt: 1
usage: {"promptTokenCount": 5294, "candidatesTokenCount": 367, "totalTokenCount": 7172, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 5200}, {"modality": "TEXT", "tokenCount": 94}], "thoughtsTokenCount": 1511, "serviceTier": "standard"}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MINOR REVISIONS

ISSUES:
1. [MINOR] Section VI.C (Prior-Volume Illustration) provides a one-dimensional Gaussian summary likelihood exercise but explicitly disclaims it as a model-selection claim or forecast. Since the author states these are "retained as reproducibility artifacts rather than promoted as paper evidence," this section dilutes the primary theoretical and recast results and should be significantly condensed or removed.
2. [MINOR] In Section IV, the redshift-space extension omits Fingers-of-God (FoG) damping and non-Gaussian covariance, which the author properly acknowledges makes the absolute significance optimistic. The manuscript would benefit from a brief quantitative estimate (even if a rough literature-based percentage) of how much FoG and nonlinear damping typically degrades this specific multi-tracer bispectrum signal to bound the optimism.
3. [MINOR] In Appendix A, the author effectively uses the $c_s = 1$ limit of Li et al.'s general-$c_s$ formula ($-165/16 + 65/(8c_s^2)$) to cross-check the $-35/16$ result. While the citation is clear, briefly expanding on how the quasi-dust corrections or $c_s \neq 1$ deviations map onto the specific vertices in the main text (Sec II.C) would make the connection between the exact kinematic limit and the model-dependent quasi-dust corrections more self-contained.

The central claim that the exact kinematic matter-bounce local amplitude is $f_{NL} = -35/16$ is rigorously supported by a careful re-summation of the cubic vertices, explicit demonstration of the previous permutation bookkeeping error, and independent cross-checks.
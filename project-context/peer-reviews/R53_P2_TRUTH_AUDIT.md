# R53 P2 — Truth Audit (verdict-first vs source)

**Paper:** P2 — "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx
Sensitivity Recast with a MegaMapper Outlook"
**Source:** `research/focused_paper_source_integration/02_full_draft.tex`
**PDF audited:** `/tmp/R53_P2/02_full_draft.pdf` md5=7a1425ed, 28 pp, 0 undef refs
**Date:** 2026-06-26
**Prior state:** R52+EXT21+EXT22 polish-tier convergence (0 BLOCKER / 0 genuine MAJOR);
phase3_bispectrum_shape_overlap.json artifact fixed in R52.

## Legs

| Leg | Status | Verdict |
|-----|--------|---------|
| Claude (Opus full read) | OK | polish-tier; 3 minor internal-consistency defects |
| OpenAI gpt-5 (native PDF, high effort, pass-2) | OK | MAJOR REVISIONS (~40 items) |
| Gemini 2.5 Pro (native PDF) | OK | MAJOR REVISIONS (glowing summary) |
| Grok 4.3 (rasterized PDF) | OK | MAJOR REVISIONS |
| Perplexity (citations) | FAIL | 401 insufficient_quota |

## Verdict summary

The three external vendors all returned "MAJOR REVISIONS," but verdict-first audit
against source shows the overwhelming majority of findings are **FALSIFIED**
(mischaracterize the source or are mathematically wrong), **OPINION** (editorial
placement the paper already substantively addresses), or **submission-gated** (Zenodo
DOI). Examples of FALSIFIED/OPINION (not acted):

- Grok E1/E2 (optimistic-vs-realistic not labeled; BF prior width not stated): both
  ranges are explicitly labeled "optimistic/realistic-after-budget"; abstract already
  states broad [-15,+15] → BF 9-14 AND narrow [-5,+5] → BF 4-7. FALSIFIED.
- Grok M1 (null-space rank not basis-invariant): rank is invariant under invertible
  linear maps; basis-dependence of ±0.13 already explicitly conceded; falls back to
  basis-independent r_cos. FALSIFIED.
- Grok/OpenAI M2/M3 (5.2-5.5σ from unvalidated flat-sky; recast not labeled): headline
  is a recast of published Heinrich σ=0.7, NOT the flat-sky injection cross-check;
  "sensitivity recast not independent forecast" stated pervasively. FALSIFIED.
- OpenAI M5 (√11 vs 15-30% shot-noise inconsistent): explicitly two different
  quantities (naive Poisson amplitude vs bispectrum-estimator effective). FALSIFIED.
- OpenAI M10 (Planck 0.75σ arithmetic): already shown inline at body; OpenAI's own
  audit confirms 4.275/5.71=0.75. FALSIFIED.
- DOI/commit-SHA, κ_ε derivation, joint-covariance check, MegaMapper-out-of-abstract,
  more Fisher detail: submission-gated or OPINION (paper honestly hedges each).

## VERIFIED DO-NOW closures (3; all polish-tier, no headline change)

**R53-1 — Percentile mislabel (OpenAI E11; ground-truthed against artifact).**
The null-space conservative-floor value "16th percentile r=0.75 → 4.7σ" is wrong:
`c9h_nullspace_significance_propagation.json` gives r_16=0.702, r_25=0.746(≈0.75),
r_84=0.989, significance_16=4.39σ, significance_84=6.18σ. So 0.75 is the **25th**
percentile (interquartile lower), and the true 16th = 0.70 → 4.4σ. The per-sample
16-84 band (4.4-6.2σ) was already correct; the mislabel made the prose internally
contradictory. Corrected 16th-pctile r 0.75→0.70 and floor 4.7σ→4.4σ at all 3 sites;
[0.75,0.94] retained as the correctly-labeled interquartile range.
- abstract: `r_{16th}=0.75`→`0.70`
- §II body (asymmetric-tail sentence): `0.75/4.7σ`→`0.70/4.4σ`, `84th 0.94/5.9σ`→
  `0.99/6.2σ`, interquartile-endpoint note added
- Table IV (tab:systematics) null-space row: `0.75 / floor 4.7σ`→`0.70 / floor 4.4σ`

**R53-2 — r_LSS<r_CMB causal prose (Gemini M1 + OpenAI M12).**
§III.B had a self-contradictory causal chain ("LSS upweights modes where templates
coincide, thereby increasing weight of configs where mismatch is largest"). Rewritten
to the correct relative-weighting direction (LSS shifts weight onto folded/intermediate
relative to CMB-Fisher) and grounded in the numerical Fisher integration
(null_space_analysis.py). Numbers 0.829/0.876 unchanged.

**R53-3 — Bayes-factor prior-width arithmetic (OpenAI E15).**
"widening [-15,+15]→[-20,+20] adds ΔBF ≲ 1" contradicts the paper's own BF ∝ W
(Eq. bf_approx): W:30→40 scales BF by 4/3 (9.8→13.1). Corrected. Headline BF≈9
unchanged.

## Recompile + overflow

Recompiled ×3 + bibtex: 0 undef refs, 28 pp. Overflow audit: only 2 pre-existing
sub-3pt overfull hboxes (Table I degenerate-boundary row; commutator equation), both
in math regions untouched by R53 edits. No new overflow. All 11 referenced artifacts
verified present on disk.

## Convergence statement

P2 remains at **polish-tier convergence**: 0 BLOCKER, 0 genuine MAJOR. R53 closed 3
source-verified MINOR internal-consistency defects (one ground-truthed against the
released artifact). No headline number (5.2-5.5σ optimistic, 2.6-5σ realistic,
BF≈9-14) changed. All external "MAJOR" verdicts resolve to FALSIFIED/OPINION/
submission-gated on verdict-first audit. Recommend re-confirm at R54.

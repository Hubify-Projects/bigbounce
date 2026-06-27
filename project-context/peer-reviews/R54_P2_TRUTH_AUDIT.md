# R54 P2 — Truth Audit (convergence-confirmation round)

**Date:** 2026-06-26
**Paper:** P2 — `research/focused_paper_source_integration/02_full_draft.tex`
**Round context:** R54 convergence test after R52+R53 + EXT21/22 (0 BLOCKER / 0 genuine MAJOR).
**Compile:** pdflatex ×2 → bibtex (BIBINPUTS=src) → pdflatex ×2 → **0 undefined refs**. 28 pp, md5 e87fdb7c (review PDF).
**Vendor legs:** OpenAI `gpt-5` OK (258.9s), Gemini `2.5-pro` OK (150.7s), Grok `4.3` OK (295.6s). **Perplexity FAILED** (401 insufficient_quota). No Anthropic leg in this tool build (3/4 reviewers OK).

## Net verdict: CONVERGED

OpenAI's independent arithmetic audit reproduced every load-bearing number
(5.18–5.47σ template-corrected; 3.01σ GR floor; 2.73σ all-combined; 2.63σ Li
stress-test; 0.75σ Planck recast; τ_NL 27.6; σ_marg 3.10/7.03). My own Opus
re-derivation agrees: κ_ε·|Δε|≈0.36, f_NL∈[−4.35,−4.02] (0.6–8%), convention
map (5/3)³(3/5)⁴·2 = 6/5, BF σ_eff=0.7/0.84=0.833→9.2. R53 closures verified
landed and consistent across all sites (16th-pctile r=0.70/4.4σ matches
c9h JSON r_16=0.702; r→1 BF 9.8→13.1 prior-width; LSS<CMB causal prose).
Missing-json (c9h_nullspace_significance_propagation.json) present, values match.

## NEW verified closures (2, both NIT-tier, no science/headline change)

| ID | Tier | Source | File:line | Old → New |
|----|------|--------|-----------|-----------|
| R54-1 | NIT | Gemini P2-m4 | 02_full_draft.tex:979–980 | Table IV b_φ-30%/50% Acts-on cell `denom.\ ($\oplus$)` → `denom.\ (repl.)` — ⊕ (caption-defined = quadrature) contradicted "baseline replacement" combination rule for these rows |
| R54-2 | NIT | OpenAI P2-M9/B1 | 02_full_draft.tex:1041 | Fig 4 caption `MegaMapper conservative ($\sigma=1.5$)` → added "(illustrative: between σ≈0.5 ideal and b_φ-50% σ≈2.2 … not an independently calibrated forecast)" — value was unanchored in body |

## Triaged — no edit (verdict, evidence)

- **Gemini P2-E1** (reviewer-metadata block "after page 28"): FALSIFIED — harness-injected `[REVIEWER METADATA …]`; `grep` = 0 occurrences in .tex source.
- **Gemini P2-m1** (Eq 2 sign "+35/8"): FALSIFIED — L636 source is `\to -\frac{35}{8}` (negative); PDF misread; Table benchmarks −4.375.
- **Gemini/Grok P2-M1** (28 pp → 15–22 pp): OPINION — length/style; mandate excludes flagging the recast for being a recast.
- **OpenAI P2-E2 / Grok P2-E1/M3** (additive-quadrature "realistic" headline / "not directly comparable" qualifier): STALE — abstract+§IV+§VII+Table IV caption already label it a scoping choice "a full joint Fisher would need to confirm" (EXT1 F4/C3, EXT2).
- **OpenAI P2-E3/E5** (Zenodo DOI placeholder, artifact names): DEFERRED — submission DOI, excluded by scope.
- **OpenAI P2-E4** (Gaussian-prior BF closed form): STALE — eq:bf_exact (CDF) + eq:bf_approx + worked example L864 reproduce BF≈9.2 (HD DO-NOW closed v1.7.63).
- **OpenAI P2-E6** (anomaly-tracer 10–20%): not load-bearing — L750/L752 label it "upper bound pending shot-noise-corrected Fisher"; "headline 2.6–5σ does not rely on anomaly-selected tracers."
- **OpenAI P2-M1** (injection-recovery "toy" rename): OPINION — L657/L659 already caveat "isotropic Gaussian noise … 2D flat-sky CMB-style estimator … not the 3D galaxy-bispectrum estimator … not a full simulation pipeline."
- **OpenAI P2-M5/M6** (δf_NL~10⁻³, photo-z 5%, shot-noise 15–30%): STALE — L755/L953 derivations + citations present (OAI-M8 R36conf closed).
- **OpenAI P2-M7 / Grok P2-M2** (explicit Wick vertex worked example): OPINION — App A.1 gives the −2Im operator-algebra identity + Eq Bfull with symmetry factors; paper explicitly states it does not re-derive the four conformal-time integrals (only Cai/Li have).
- **OpenAI P2-M8** (BF vs SSFSR over-emphasis): STALE — abstract labels BFs "illustrative … not definitive model-selection evidence."
- **OpenAI P2-M10 / N11** (r=0.84 vs noise list 0.829/0.830/0.835): NOT-RE-OPENED — deliberate R36conf OAI-M9 standardization to 0.84; ±0.02 band covers the cluster; floor robust to r=0.829 (2.97σ≈3.0σ, shown L750).
- **OpenAI P2-N1/N2/N3/N4/N5/N6/N7/N8/N9/N10/N12/N13, P2-C1, P2-F1**: editorial polish / pdftotext glitches (e.g. N12 "k∑1" — source is `k_1 \ll k`, L638) / already-present caveats. OPINION.
- **Grok P2-N1** (date June 19 vs 2028 release): cosmetic — compile date.
- **Grok P2-NIT1** (naive-uncorrected row printed): deliberate (EXT3 C1 / EXT7) "not used in headline" reference row.

## Recompile (post-edits): ×2 + bibtex + ×2 → 0 undefined. Overflow: 2 pre-existing sub-3pt hboxes (2.95pt tab:benchmarks, 1.23pt eq line); both edits in already-multi-line cells, no new overflow.

## CONVERGENCE STATEMENT

P2 is **CONVERGED** at R54. Three independent native-PDF vendors return zero
BLOCKER and zero genuine new MAJOR; OpenAI's arithmetic audit corroborates every
headline number. The only actionable output is 2 NIT-tier internal-consistency /
honesty-label fixes (Table IV ⊕→repl., Fig 4 σ=1.5 illustrative-label), neither
of which touches any scientific claim, number, or headline. All remaining vendor
items are STALE (already caveated in prior rounds), FALSIFIED (PDF-extraction
artifacts / misreads), submission-scope (DOI), or OPINION (length/polish). No
re-opening of the R52/R53-closed 16th-pctile mislabel or missing-json (both
verified intact).

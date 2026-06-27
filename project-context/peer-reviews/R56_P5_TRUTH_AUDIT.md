# R56 P5 — Truth Audit (HARDENED / de-biased re-review)

**Paper:** P5 — Environmental Dependence of Spiral Chirality (DESIVAST three-algorithm + T-Web)
**Source:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.85)
**PDF:** `/tmp/R56_P5/p5_desi_chirality.pdf` md5=c3295c1f, 33 pp, 0 undef, 0 overfull
**Reviewers:** Gemini 2.5 Pro (native PDF), Grok 4.3 (rasterized), GPT-5 high (native + pass-2), Perplexity (FAILED — quota 401). Plus own Opus full read.
**Standard:** Hardened PRD/MNRAS bar. Self-favoring / unstated-assumption / internal-inconsistency = real finding (MINOR min). Patterns 061–064 + calibration filter applied to genuine false-positives only.

Net consensus: **MAJOR REVISIONS** from all three vendors — but every vendor's headline ESSENTIALs are either (a) FALSIFIED on disk, (b) already-disclosed/structural (Paper IV unpublished), or (c) explicitly out-of-scope per task (DOI). Verified NEW correctness items are MINOR-tier.

---

## Verdict-first table

| ID | Vendor | Claim | Verdict | Action |
|----|--------|-------|---------|--------|
| Gem-E2 | Gemini | "Sign errors in Table X (Δf_CW)" | **FALSIFIED** | Header l.2295 = `f_non-void − f_void`; tabulated +0.0007/−0.0019/−0.0001 match exactly. Reviewer transcribed convention backwards. Genuine false-positive. |
| Gem-E3 / Grok-E4 | Gemini/Grok | "Future placeholder date June 26 2026" | **FALSIFIED** | Today IS 2026-06-26 (env date). Vendor knowledge-cutoff artifact. |
| OAI-M7 | GPT-5 | "filament σ = −2.55 not −2.61" | **FALSIFIED** | Exact integers (203,261/408,187) → σ = −2.606 → −2.61. Reviewer used rounded f=0.4980. Caption already states σ from integers. |
| Gem-E1 / Grok-E1 / OAI-standalone | all | "Depends on unpublished Paper IV" | **OUT-OF-SCOPE / TRULY-BLOCKED** | Real publication-gate, but P5 re-estimates monopole internally (f_CW^P5=0.49719, Table VII) and is constructed to not depend on Paper IV load-bearing numbers. Cannot close without making Paper IV public — outside P5. Already disclosed throughout. |
| OAI-E6 | GPT-5 | "Missing DOI string" | **SKIP (DOI)** | Per task: skip DOI. Real pre-submission item, deferred-genuine. |
| Grok-E2 | Grok | "Abstract stronger than body on void bin" | **FALSIFIED (already-present)** | Abstract l.516–524 already states void bin "sample-size limited at n=428" + "no evidence beyond catalog-monopole offset." Requested rewrite already in text. |
| Grok-E3 | Grok | "non-comparability qualifier missing at every table" | **STALE/already-present** | Qualifier present in cw_vs_env, within_class_density, tempel, program_split, healpix captions. NIT at most. |
| Grok-M2 / -M4 / OAI-E5 | Grok/GPT | n=6 power; Phase-2 FPR; ASTRA variance | **FALSIFIED (already-addressed)** | n=6 caveated as "indicative, not statistically established" + 39% CP bound; Phase-2 has empirical max-stat p_LEE + global p=0.36/0.27 + Bonf-9; ASTRA variance validated vs 10⁴-draw MC to 1.2%/<0.02σ, labeled non-load-bearing. |
| OAI-E3 | GPT-5 | "Move all [A#]/version prose out of body" | **OPINION** | [A#] inline IDs are a deliberate D-round design (Appendix C map). Style preference, not a defect. |
| OAI-E7 | GPT-5 | "Recast primary path as pre-registered" | **OPINION (integrity-correct as-is)** | Paper is HONEST that designation is post-hoc (sec:primary_path). Recasting as pre-specified would FALSIFY. Current transparent treatment is correct. |
| OAI-E4 | GPT-5 | "Mixed monopole reference" | **FALSIFIED (already-reconciled)** | l.2535–2551 + l.994–1022 explicitly define which monopole used where + 8% reconciliation. |
| Grok-M1 / OAI-M6 | Grok/GPT | "33pp too long" | **OPINION** | Editorial, not correctness. |
| OAI-M9/M10/M11/M3 | GPT-5 | CIC deconv check; independent RNG seeds; catalog-native complement; effect sizes | **AUGMENT / already-partly-addressed** | Grid-convergence 128³–384³ + distinct-stream re-draws + GALZONE complement disclosed (l.2363). Remaining = pod-compute augment, not text DO-NOW. |
| **OAI-E1** | GPT-5 | "Paper IV dipole +0.41σ(p=0.31)/+0.43σ(p=0.30) σ→p inconsistent" | **VERIFIED MINOR** | 0.41σ ↛ p≈0.31 on any tail convention; two quotes also disagree. **CLOSED** — dropped non-load-bearing p-values, kept σ (no fabrication). |
| **OAI-E2** | GPT-5 | "Redshift p=0.372 vs 0.80/0.81 contradictory" | **VERIFIED MINOR** | Two distinct statistics (max-abs-dev vs quintile LEE) presented without distinction. **CLOSED** — labeled both explicitly at l.1313 + l.1325. |
| **OAI-E8** | GPT-5 | "100% covariate-complete vs edge-on on 152,455 subset" | **VERIFIED MINOR** | Real ambiguity. **CLOSED** — clarified edge-on enters only featured sub-model; full model uses 4 full-coverage covariates. |
| **Gem-M1** | Gemini | "cluster σ=−4.66 vs σ_pred=−3.28 'within order-unity'" | **VERIFIED MINOR (self-favoring)** | Imprecise wording downplays 1.38σ residual. **CLOSED** — replaced with explicit residuals (+0.71/−1.38) bounded by monopole-reference uncertainty + σ_vs_monopole<1.15. |

## Self-favoring item under hardened bar?
**Yes — one:** Gem-M1 "within order-unity of observation" downplayed a −1.38σ cluster residual. Closed as real MINOR with explicit residual values.

## Integrity fixes verified intact (R52/R55 + prior)
- Bonferroni-1054 |σ|=4.07 (l.1051) ✓
- Bonferroni-5 |σ|=2.58 / Cramér's V=0.078 / log₁₀p≈−1069 / χ²=4933 ✓
- Table V (within_class_density) log₁₀ density covariate (l.1461–1464) ✓
- Paper IV harmonic-channel reframe / MASTER ℓ=1 withdrawn (l.704–712) ✓
- χ-unit multiply-by-h (AUTO-FALSIFY note l.26–34; footnote l.849–862) ✓
- \mbox{-} usages (16) all math-mode compound subscripts (non\mbox{-}void, T\mbox{-}Web) — render as proper hyphens, NOT artifacts ✓

## NEW VERIFIED closed: 4 MINOR (OAI-E1, OAI-E2, OAI-E8, Gem-M1). No BLOCKER/MAJOR survived hardened audit.

## Convergence statement
R56 is a near-converged round. Three independent native-PDF vendors agree the numerical core is correct and the headline null is supported; their MAJOR-REVISION verdicts rest entirely on (a) the structural Paper-IV-unpublished gate (out of P5's control), (b) editorial length/style, and (c) DOI minting — none of which are in-scope closures. The only NEW correctness items were four MINOR internal-consistency/precision wording fixes, all closed. Zero verified BLOCKER or MAJOR. Recommend R57 as the convergence-confirmation round; no science change pending.

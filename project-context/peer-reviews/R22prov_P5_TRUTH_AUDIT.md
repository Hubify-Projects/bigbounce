# P5 R22prov — Truth audit (v0.1.50, 21pp, native-PDF round)

**Inputs**: R22prov_P5_SYNTHESIS.md (77 findings / 10 consensus groups), R22prov_P5_META_REVIEW.md,
5 vendor files, p5_desi_chirality.tex v0.1.50, artifacts
`outputs/16_cosmic_web_zshell_corrected.{json,md}` + `scripts/16_cosmic_web_zshell_corrected.py`
+ `results/analysis_cosmic_web/desivast_*.json` + `env_finder/01_compute_vweb.py`.
**Auditor recomputations**: per-class σ from exact Table II counts, σ_pred at all quoted N,
class-count sums, program-split sums, 4×2 omnibus χ² (new), h-unit code audit, 3 web citation checks.

**Headline counts**: Claude_brutal returned ZERO findings. Verdicts:
**24 VERIFIED · 6 VERIFIED-LIKELY · 20 PARTIAL · 12 FALSIFIED · 13 OPINION/NIT-batch · 2 HOUSTON-DECISION**
(77 total). Round verdict: **NOT CLEAN** → v0.1.51 wave (text + small compute).

---

## 1. Consensus-group verdict table

| Group | Reviewers | Verdict | Evidence |
|---|---|---|---|
| `table_ii` META-E1 — Table II/Fig 3/abstract say "n = 791,635" but per-class counts (428+6,673+408,187+397,505) sum to **812,793** | META | **VERIFIED** (load-bearing) | Sum recomputed = 812,793. Artifact JSON `canonical_recomputed` shows ALL = 812,793 with identical per-class n/n_CW → headline table IS the env-labeled superset. §VIII.F (tex 1352–1363) documents the 21,158-row excess but the headline surfaces (tex 573, 606, 116, 1986) mislabel the parent. Fix: relabel to 812,793 (monopoles agree to 4 decimals, conclusion invariant). |
| `table_ii` Grok-E2 / Perpl-E3 — σ-flavor juxtapositions lack non-comparability qualifier | Grok, Perpl | **PARTIAL** | Real but "at every juxtaposition" is over-broad. Portfolio disposition = P2-R22prov2 V8: add local notes at abstract + §V + Tables II/V/X. |
| `table_ii` Grok-M2 — void bin n=428 "cannot carry the headline; anchor on DESIVAST" | Grok | **FALSIFIED** | Already implemented: §V.B (tex 522–537) declares DESIVAST n=56,981 the PRIMARY path; V-Web is secondary. Reviewer demands the existing design. |
| `table_ii` OAI-E3 — Tempel filament concordance computed on disjoint samples | OAI | **VERIFIED** | tex 1613–1614: V-Web f=0.4980 (n=408,187 full sample) vs Tempel f=0.4982 (n=14,317 of the 110,586 overlap). Must restrict V-Web side to the same overlap. Supporting-only check (paper already labels it "not load-bearing") but the comparison as computed is invalid. Compute: small. |
| `table_ii` OAI-M3 — ×40 tightening mixes 791,635/812,793 parents | OAI | **FALSIFIED** | Artifact JSON: canonical range 1.98pp AND corrected 0.05pp both computed on the same 812,793 joined-spiral parent (`spiral_counts` canonical=corrected=812,793). Apples-to-apples. The apparent mismatch is purely META-E1's mislabel of Table II. |
| `table_ii` OAI-m10 — filament σ should be −2.56 not −2.61 | OAI | **FALSIFIED** | Recomputed from exact counts (n_CW=203,261, N=408,187): σ = −2.6061 → −2.61 correct. Reviewer back-derived from the 4-decimal-rounded f=0.4980 (gives −2.556). Rounding-recompute confab. |
| `table_ii` OAI-n3 — 24 Mpc/h max hole radius uncited | OAI | **VERIFIED (minor)** | tex 1169; state "computed from the parsed VoidFinder hole catalog" or cite DESIVAST §. |
| `companion` Gemini-E1 / Perpl-E2 — load-bearing dependence on unpublished Paper IV | Gemini, Perpl | **HOUSTON-DECISION** + 1 VERIFIED sub-item | P5 consumes only P4's labels + monopole Δf=−0.0026 (uncertainty propagated, tex 222–227). Publication ordering (arXiv P4 before/with P5) is Houston's call; PRD permits companion citations. **VERIFIED sub-item found by this audit**: tex 274–276 still cites P4's "−0.12σ subsample-mask MASTER-deconvolved ℓ=1" — **withdrawn in P4 v1.0.166 (SEV-1 retraction 2026-06-09, synthetic-footprint provenance)**. Must update §II to P4's re-anchored headline (real-space +0.43σ, p=0.30 + template-fit exclusion). P5's environment null does not depend on the dipole result — only the stale sentence needs fixing. |
| `companion` Perpl-m3 — no DOI/version for "companion data repository" | Perpl | **VERIFIED** | App. B (tex 2080–2094) names no repository/commit/DOI. Reinforced: the DESIVAST point-in-sphere driver is NOT in `scripts/` (only its JSON outputs in `results/analysis_cosmic_web/`). Commit driver + cite via `\artifact{}` + version tag. |
| `shamir_citation` META-M7 — Shamir comparison apples-to-oranges | META | **PARTIAL** | tex 1876–77 already scopes to "environment-dependent chirality of the Shamir 2022 amplitude". Add one sentence: this null does not adjudicate Shamir's *global* anisotropy claim (P4's dipole bound does that, separately). |
| `shamir_citation` Perpl-E1 — "cannot verify any citations (no access)" | Perpl | **FALSIFIED** | Reviewer-capability disclaimer, not a paper defect. All 12 bib entries spot-checked; 3 web-verified this audit (links in §4). Zero confabulated references. |
| `sigma_mixing` Perpl-E3/M1/M2 | Perpl | E3 **PARTIAL** (above) · M1 **FALSIFIED** (Table II gives exact n_CW; σ recomputes exactly: filament −2.606, cluster −4.658) · M2 **PARTIAL** (σ_pred basis documented at §VIII.F tex 1367–1376, −0.0026 vs −0.0028 reconciled; add one clarifying sentence on which monopole feeds which table) |
| `sigma_mixing,table_ii` OAI-E6 — filament bright 416,701 exceeds class total | OAI | **VERIFIED (ESSENTIAL)** | Internal contradiction confirmed three ways: (a) catalog program split sums to 791,635 (775,760+14,782+875+218 ✓, tex 806–810) but filament bright+dark = 437,904 > filament total 408,187 on *either* parent; (b) filament-dark 21,203 > catalog-dark 14,782 — impossible on the same parent; (c) χ² line uses n_bright+dark = 811,609 (≈ superset). The bright/dark per-class numbers (also quoted in abstract, tex 191–194) come from an undeclared third basis or are wrong. Recompute on one declared parent and report all N, f per subgroup (closes OAI-m17 too). |
| `companion,length` Grok-M1 21pp / `length` Perpl-M5 | Grok, Perpl | **OPINION** | Portfolio C18 disposition (consistent with P2/P4 rounds). Note: the abstract is ~1,300 words — genuinely outsized for PRD; trimming it is the one length item worth doing. |
| `future_date` Gemini-M3 — "futuristic" 2025/2026 citations | Gemini | **FALSIFIED** (auto-class b) | It IS June 2026. All three "future" papers exist (links §4). Reviewer training-cutoff artifact, same as P4-D17 / P2 rounds. |
| `table_iv` OAI-m14 — ρ̄ undefined | OAI | **VERIFIED (minor)** | tab:within_class_density uses ρ̄ with no units/normalization; define (smoothed log-density per §IV step 12). |

## 2. Single-vendor ESSENTIAL / MAJOR table

| ID | Finding | Verdict | Evidence / disposition |
|---|---|---|---|
| Grok-E1 | "No abstract in manuscript" | **FALSIFIED** (auto-class c) | `\begin{abstract}` tex 78–213. revtex PDF text-layer artifact. |
| Grok-E3 | Title misstates 56,981 vs n=428 | **FALSIFIED/STALE** | Title restructured v0.1.44 (GRO-B1) to lead with DESIVAST primary; abstract separates n=428 V-Web vs n=56,981 DESIVAST explicitly (tex 145–150). |
| Grok-M3 | No grid-resolution convergence test (256³ only) | **VERIFIED-LIKELY** | Phase 2 sweeps R_s, λ_th but never N_grid. Cheap compute (z-shell rebuild ran in 102 s; a 128³/384³ canonical recheck is ~minutes–hours). Wave compute C7. |
| Grok-N1 | "conservative" 1″ wording inconsistent | **FALSIFIED/STALE** | v0.1.49 E3 close added the Tractor shared-astrometry explanation (tex 322–331); "conservative for this catalog pair" is now justified in place. |
| Grok-N2(+NIT1) | Mollweide convention missing; caption dup | **PARTIAL** | fig:healpix_skymap states "equatorial" (tex 919); fig:voids_vs_chirality (tex 1454) does not → add. Caption dedupe = NIT batch. |
| META-E2 | Void counts 1,461/420/295 vs 1,992/1,478 "contradictory" | **PARTIAL** | Not contradictory: 1,461/420/295 are **interior** voids at the z≤0.24 statement (tex 1082–83); 1,992/1,478 are **catalog totals** of "effective voids" (tex 1218–20). Distinct object types, both labeled, but terse — add one linkage sentence or a per-algorithm count mini-table (entries used per analysis). |
| META-E3 | h⁻¹ Mpc unit slip risk; conversion undocumented | **PARTIAL** (slip scenario contradicted where auditable) | Code audit: `env_finder/01_compute_vweb.py:103–107` and `scripts/16_…py:104–106` both do `comoving_distance(z).value * (H0/100)` — explicit Mpc→h⁻¹Mpc. DESIVAST membership driver not in repo (can't audit) → commit it (with Perpl-m3) + add the one-sentence unit-documentation + χ(z=0.2) sanity value to §VIII.A. |
| META-M1 | "within ~1σ of σ_pred" not a formal test | **PARTIAL** | Fair critique of tex 467–471 phrasing; the formal version already exists (Table X: one-sample residual vs f^P5, all |σ|<1.15). Replace the loose language; add the omnibus χ² (next row). |
| META-M6 | No omnibus homogeneity test on canonical run | **VERIFIED — and already computed in this audit** | 4×2 χ² from artifact counts: **canonical χ²=3.547, 3 dof, p=0.315; z-shell-corrected χ²=0.112, p=0.990**. Both null → drop-in sentence + strengthens the paper. Subsumes META-m4. |
| META-M2 | Unstratified label-shuffle nulls anticonservative | **VERIFIED-LIKELY** | Legit given the paper's own per-leg residual claims. Compute C3: re-run permutations stratified by imaging leg + program (pipeline + data exist; seed-driven). |
| META-M3 | k=5 NN density proxy endogenous (spirals-only) | **VERIFIED-LIKELY** | Compute C4: recompute proxy on all matched primaries (2.23M) and re-run quintiles. |
| META-M4 | Occupied-cells-only shell means biased vs randoms | **VERIFIED-LIKELY** | Applies to the new v0.1.50 z-shell estimator. Compute C6: HEALPix-weighted / random-based shell-mean cross-check. |
| META-M5 | No covariate control (mass/size/inclination) | **VERIFIED-LIKELY** | Compute C5: logistic regression of CW on env + {z, size, axis ratio, mag} — confirm P4 catalog carries the covariates; else nearest match on z+mag. |
| OAI-E1 | Sweep "n=3,696,152" exceeds any chirality parent | **VERIFIED** | tex 981–983. Max chirality-labeled parent = 2,232,212 (791,635 relevant). The quoted n (and the σ_pred −10 computed from it) must be the 14.6M-galaxy class population, on which σ_from_half is undefined. Clarify basis or recompute the cell on the spiral subsample. |
| OAI-E2 | §XI "BGS within ±0.001 of dark" contradicts 0.4970 vs 0.5051 | **VERIFIED** | tex 1831–33 vs 806–808 (Δ=0.0081) and the abstract's own 3.4σ sign-flip. Stale sentence; rewrite the systematics summary line (with M4 mini-table). |
| OAI-E4 | "p<10⁻¹⁰⁰⁰" | **VERIFIED (trivial)** | tex 200, 861. Replace with p≪10⁻³⁰⁰ or χ²-bound phrasing. |
| OAI-E5 (+m6, Perpl-m1) | T-Web/V-Web naming drift (§IX.A says "T-Web classifier of §IV A") | **VERIFIED (text)** | tex 1477 vs §IV heading "V-Web cosmic-web classification" (tex 379). v0.1.50 title footnote started the T-Web migration; body is mid-migration. One harmonization pass: V-Web = our implementation alias, T-Web (Hahn 2007) = the recipe, single reminder sentence. |
| OAI-M1 (+Gemini-m1) | σ_pred(filament) −3.16 wrong | **VERIFIED** | 2·(−0.0026)·√408,187 = **−3.32**. Paper self-inconsistent: tex 621 says −3.16, tex 1023 says 3.32. Fix tex 621 + discussion. |
| OAI-M2 | Monopole "~0.2 pp" understates −0.26 pp | **VERIFIED** | Abstract tex 112. Change to "≈0.26 pp". |
| OAI-M4 | Systematics list lacks Ns/values | **PARTIAL** | One-line summary §XI; add per-split f_CW/N mini-table (rides with E2 fix). |
| OAI-M5 | NSIDE 16 (297 px) vs Fig 8 NSIDE 32 (885 px) "incompatible" | **FALSIFIED** | Two different analyses, both described: NSIDE=16 maximal-void stratification (tex 1293–95, Table) vs NSIDE=32 Pearson correlation (tex 1424–33, Fig). 297@16 vs 885@32 is self-consistent (×4 pixel count). Optional caption cross-pointer only. |
| OAI-M6 | σ_vs_monopole parent mixing | **PARTIAL** | tex 1358–60: superset and headline monopoles agree to 4 decimals, documented. META-E1 relabel closes the residual ambiguity. |
| OAI-M7 | KDTree fixed k=20 not guaranteed-complete | **VERIFIED-LIKELY** | Legit edge-case; data in `data/desivast/` → compute C8: assert max #holes within 24 Mpc/h of any spiral ≤ 20 (or rerun with `query_ball_point`); one guard sentence. |
| Perpl-E4 (+Gemini-E2) | Post-hoc primary path / forking paths | **OPINION** | §V.B openly declares post-hoc status + Bonferroni-5 multiplicity bookkeeping (tex 505–559) — the accepted mitigation short of preregistration, which cannot be retrofitted. No further action. |
| Perpl-E5 | Toy EFT operator not in cited literature | **FALSIFIED** | App. A states this itself, verbatim ("not contained in either…", tex 2021–2029) plus rotational/gauge-invariance caveats. Reviewer demands the existing text. Removal = style OPINION. |
| Perpl-E6 | "Statistically independent" too strong given RSD | **PARTIAL** | Conclusions already scope "within DESI DR1 at V-Web resolution"; RSD is the longest limitations item (tex 1908–1967). Soften 2–3 sites to "no detectable environment dependence at current sensitivity". |
| Perpl-M3 (+Gemini-M1) | Bright/dark 3.4σ under-prominent | **PARTIAL** | Abstract devotes a full paragraph (tex 188–212) and names it "the strongest single residual structure" (tex 877). Disentanglement is genuinely DR2/Rubin-data-bound (dark sample 5× larger). No further action this round beyond the E6 numeric repair. |
| Perpl-M4 | RSD reconstruction not performed | **PARTIAL / no-action** | Explicitly carried as the dominant caveat with order-of-magnitude boundary-crossing estimate (tex 1946–1967). Zel'dovich re-classification = follow-up-scale compute; deferral is explicit in-paper and was accepted in prior rounds. |
| Gemini-M2 | Structure: DESIVAST should come earlier | **OPINION** | §V.B already front-declares the primary path; full reordering = editorial preference. |

## 3. Batched MINOR/NIT sweep (one v0.1.51 text pass)

| ID | Item | Verdict → action |
|---|---|---|
| META-m1 | `scripts/16 cosmic web zshell corrected.py` cited as raw local path (tex 1492, also 1524) | VERIFIED → `\artifact{}` + commit hash (also a /latex-audit raw-`\texttt`-path violation) |
| META-m2 | Jeffreys intervals called "exact binomial credible" (tex 445, 250) | VERIFIED → rename "Jeffreys 95% credible intervals" |
| META-m3 | Logistic regression coefficient without SE/p/scaling (tex 641–44) | VERIFIED → report SE, z, p, per-unit-z scaling |
| META-m5 | DESI-side dedup rule unstated (tex 312–13) | VERIFIED → one sentence: unique TARGETID in zall-pix-iron, no many-to-one after join |
| OAI-m9 | σ_pred = **−**2Δf√N sign error in two captions (tex 681, 709) vs Eq. (1) | VERIFIED → drop the minus |
| OAI-m11 | "1,821 valid pixels" cuts unstated (tex 1410) vs 1,496 in Fig 8 | VERIFIED → state z-range + spiral-count threshold beside 1,821 |
| OAI-m12 | "~5 pp" ambiguity (abstract tex 114) | VERIFIED → "±4.8 pp (2σ half-width) for the void bin" |
| OAI-n1 | "N_grid=256 ×" should be 256³ (tex 933) | VERIFIED → fix |
| OAI-n4 | "HEALPix-NSIDE-=32" stray hyphen (tex 1408) | VERIFIED → fix |
| OAI-m7 | 0.026 pp vs displayed 0.02 pp | PARTIAL → re-report after OAI-E3 overlap recompute, 2 sig figs |
| OAI-m13 | "largest…to date" superlative | PARTIAL → "to our knowledge" (hedge half-present at tex 1203–07) |
| OAI-m15 | "§XIII" cross-ref for V-Web secondary path (tex 1108) | PARTIAL → point to §IV/§VII + §XIII |
| OAI-m16 | counting-floor phrasing (tex 1013–18) | PARTIAL → name which class floors the 0.22 pp sits below/above |
| OAI-m5/n5/m8, Perpl-m2, Grok-NIT1 | pp-vs-fraction units, Mpc/h convention, inline Eq-1 parens, symbol-definition order, caption dup | NIT batch → single consistency pass |
| OAI-n2, Perpl-n1 | hyphenation, sentence length | OPINION → skip |

## 4. FALSIFIED list with evidence (12)

1. **Gemini-M3 "future preprints"** — auto-class (b): it IS June 2026. All three contested papers exist:
   - DESIVAST: Rincón et al., ApJ 982, 38 (2025) — https://arxiv.org/abs/2411.00148 (posted 2024-11-01, published 2025; ID/DOI/volume all match bib)
   - Ullah et al. 2026, "Cosmic-web quenching with DESI DR1: T-Web environments…" — https://arxiv.org/abs/2604.02463 (posted 2026-04-02; title matches bib exactly)
   - Zapata-Zuluaga et al. 2026, "The Cosmic Web in the DESI EDR: A Probabilistic Environment Catalog" — https://arxiv.org/abs/2604.01456 (posted 2026-04-01; authors Zapata-Zuluaga, Guevara-Montoya, Torres-Gomez, Hernandez, Forero-Romero match bib exactly)
2. **Gemini-N1** Rincón "2025 journal year vs Nov-2024 arXiv inconsistent" — normal posting→publication lag; both correct (links above).
3. **Grok-E1** "no abstract" — abstract environment at tex 78–213; PDF text-layer artifact (auto-class c).
4. **Grok-E3** title misstates — title leads with DESIVAST 56,981 since v0.1.44; V-Web 428 separated in abstract.
5. **Grok-M2** "void bin carries headline" — DESIVAST primary-path declaration §V.B already anchors the headline exactly as demanded.
6. **Grok-N1** "conservative" wording — v0.1.49 Tractor shared-astrometry explanation (tex 322–331) justifies it in place.
7. **OAI-M3** ×40 mixes parents — artifact JSON proves both ranges on the identical 812,793 parent.
8. **OAI-M5** NSIDE mismatch — two distinct, separately-described analyses; counts mutually consistent.
9. **OAI-m10** filament σ −2.56 — exact-count recompute gives −2.606 (paper correct); reviewer used rounded f.
10. **Perpl-E1** "cannot verify citations" — capability disclaimer; 12/12 bib entries verified (Hahn MNRAS 375,489; Hoffman MNRAS 425,2049; Cautun MNRAS 441,2923; Planck A&A 641,A6; Shamir MNRAS 516,2281/2208.13866; Lue PRL 83,1506; Alexander Phys.Rep. 480,1; Tempel A&A 566,A1; + 3 web links above; 2 companions correctly labeled in-prep).
11. **Perpl-E5** EFT operator "not grounded" — App. A states and caveats exactly this, verbatim.
12. **Perpl-M1** abstract numbers unrecomputable — Table II carries exact n_CW; all σ recompute exactly.

Perplexity ESSENTIAL falsification rate this round: 3/6 (E1, E5 false; E2 Houston-call; E3/E6 partial; E4 opinion) — feed to pattern-001 stats with the P2 5/5 result.

## 5. Disposition

**Round verdict: NOT CLEAN.** 5 VERIFIED ESSENTIALs on current text + 1 audit-discovered stale companion citation.

### v0.1.51 wave — text (same bundle, /pdf-restamp-bundle)
- T1 **META-E1**: relabel Table II / Fig 3 caption / abstract / conclusions parent set → 812,793 env-labeled superset (keep §VIII.F reconciliation; conclusion invariant).
- T2 **OAI-E6 + E2 + m17**: recompute bright/dark per-class split on one declared parent; publish N,f per subgroup; rewrite §XI "±0.001" line (+ M4 mini-table).
- T3 **OAI-M1**: σ_pred(filament) −3.16 → −3.32 (tex 621).
- T4 **OAI-E1**: fix/clarify sweep cell n=3,696,152 basis.
- T5 **OAI-E4** p≪10⁻³⁰⁰ · **OAI-M2** 0.26 pp · **OAI-m9** caption sign · **stale P4 −0.12σ** §II update to v1.0.166 re-anchored headline.
- T6 **OAI-E5/m6/Perpl-m1**: T-Web/V-Web harmonization pass.
- T7 **Grok-E2/Perpl-E3** σ non-comparability notes; **META-M7** Shamir scoping sentence; **Perpl-E6** soften 2–3 "independent" sites; **META-E2** void-count linkage sentence; **META-E3** unit-documentation sentence.
- T8 Batched sweep table §3 + META-m1/Perpl-m3 artifact-citation fixes (commit DESIVAST driver).

### v0.1.51 wave — compute (all local-feasible)
- C1 **META-M6/M1/m4** omnibus χ²: DONE in this audit — canonical χ²=3.547 (3 dof, p=0.315); z-shell χ²=0.112 (p=0.990). Drop into §VI.A + §IX.A.
- C2 **OAI-E3** Tempel concordance on the 110,586 overlap (small parquet job).
- C8 **OAI-M7** KDTree k-sufficiency guard check (data/desivast present; minutes).
- C3 **META-M2** stratified label-shuffles · C4 **META-M3** parent-tracer density proxy · C5 **META-M5** covariate regression · C6 **META-M4** random-based shell means · C7 **Grok-M3** 128³/384³ grid-convergence — hours-scale jobs, run before round closure per do-now rule.

### No-action
All 12 FALSIFIED; OPINION items (length ×3, structure, forking-paths ×2, EFT-removal, style ×2); Perpl-M4 RSD (explicit in-paper deferral, DR2-bound); OAI-M5/M6, Grok-M2/N1/E3 (already implemented).

### Houston decision
- Companion-paper ordering (Gemini-E1/Perpl-E2): arXiv P4 before/with P5 submission so [3] resolves to a public preprint.

*Audited 2026-06-09. No paper edits made in this task.*

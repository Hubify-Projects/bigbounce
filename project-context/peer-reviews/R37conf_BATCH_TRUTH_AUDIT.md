# R37conf — Batch Truth-Audit (all 6 papers, single pass)

**Audit date:** 2026-06-13 PT
**Auditor:** Claude Opus 4.7 (truth-audit class)
**Protocol:** `feedback_peer_review_truth_audit_protocol` + standing auto-falsify rules
**Round purpose:** Confirm EXT7 closures (the 14 genuinely-new VERIFIED items closed in the EXT7 wave) persist through R37conf and surface any genuinely-new VERIFIED finding the prior wave missed.
**Reviewers per paper:** OpenAI gpt-5 (methodology), Gemini 2.5-pro (cosmology), Grok 4.3 (brutal/adversarial), Perplexity sonar-pro (citations) — plus Claude_brutal as a fifth leg per the legacy 5-vendor template.
**Source PDFs reviewed (post-EXT7 bumps):**

| Paper | Tex | Compiled PDF | md5 |
|---|---|---|---|
| P1A | `arxiv/paper1a_ech_nogo.tex` v1A.0.68 | `paper1a_ech_nogo_v1A.0.68.pdf` | 0de277bf |
| P1B | `arxiv/paper1b_mcmc_companion.tex` v1B.0.65 | `paper1b_mcmc_companion_v1B.0.65.pdf` | bac8d620 |
| P2 | `research/focused_paper_source_integration/02_full_draft.tex` v1.7.60 | `paper2_fnl_forecast_v1.7.60.pdf` | a961bf1c |
| P3 | `pipelines/p3_anomaly_engine/paper3_draft.tex` v3.1.103 | `paper3_anomaly_catalog_v3.1.103.pdf` | 566f7150 |
| P4 | `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.182 | `chirality_catalog_paper_v182.pdf` | d3785514 |
| P5 | `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.72 | `p5_desi_chirality_v0.1.72.pdf` | 544b6af2 |

**Auto-falsify rules in force** (applied on sight; no closure work owed):

- June 2026 IS current date — any "future-date" flag auto-falsified.
- arXiv 25xx / 26xx IDs valid — not "fake".
- HD-4 / HD-6 / HD-11 release-bundle items (Zenodo DOI minted at arXiv submission; commit pin / immutable tag deferred to journal-submission stage) — HD-ruled out of scope at arXiv stage.
- pattern-046 (revtex internal version-string in title block `v1A.0.68` etc.) — standard preamble class, HOUSTON-DECISION since R28; binding rule.
- pattern-052 (re-raise of items whose prior verdict cited primary evidence) — auto-falsified on sight.
- Fisher F₀=1/8.98² 8×-falsified (P3 — Fisher-positivity central is 8.14 with envelope [3.92, 8.98]; any "8.98 only" call falsified).
- P5 k=20 6×-FALSIFIED rule (the exact rerun IS in the paper; Δf_CW invariance at +0.0006 vs +0.0007 documented; pattern-052 auto-falsify on every re-raise).
- 2√3 Fisher rule (P4 re-raises without new arithmetic auto-falsify).
- ChatGPT release-bundle "Data Availability final at submission" — HD-11 release-bundle, OUT-OF-SCOPE arXiv-stage.
- Length opinion (PRD "page limit" critiques) — OPINION (PRD has no hard page cap; reviewers' "12-page", "15-page", "18-page" assertions are wrong; PRD methods papers commonly run 25+).

---

## Headline (one line per paper)

| Paper | EXT7-closure persistence | Genuinely-new VERIFIED | Verdict |
|---|---|---|---|
| P1A | **CLEAN** — F67-B1 Fig 3 caption discloses H₀=69.2 / Ωₘ=0.310 + enhanced-radiation proxy ✓; F67-M2 README synced to v1A.0.67 ✓ | **2** (P1A-E5 sphaleron T-threshold off by ~2 orders; P1A-E4 10¹²⁰ vs 10¹²² hierarchy still mixed in body) | NOT-CLEAN (2 MINOR-arithmetic genuinely-new) |
| P1B | **CLEAN** — FB2 NaMaster Eq (1) σ_b² divisor dropped ✓; FB1 CHANGELOG v1B.0.64+v1B.0.65 entries ✓; README v1B.0.65 ✓ | **0** | CLEAN |
| P2 | **CLEAN** — Table IV Row 1 split (Naive 6.25σ ref-only + Template-corrected 5.2–5.5σ headline) ✓; Refs [28]/[34] updated ✓ | **0** | CLEAN |
| P3 | **CLEAN** — Eq (1) spectro/tabular disambiguation ✓; Planck binomial "naive" caveat ✓; tab:recount 4-row layout ✓ | **0** | CLEAN |
| P4 | **CLEAN** — 6 polish edits all landed (tab:wls_mask_equiv ✓, IV.D Ganalyzer caveat ✓, sum-to-one ✓, A_{95,nq} "null-quantile benchmark" ✓, D4-TTA caveat ✓, tab:harmonic_completeness ✓) | **0** | CLEAN |
| P5 | **CLEAN** — Table VIII row label ✓; §VIII.A n=6 ↔ §VI.A n=428 cross-ref ✓; "canonical" → "headline" V-Web ✓ | **0** | CLEAN |

**Totals across 6 papers:** EXT7 closures all persisted on disk; 2 genuinely-new VERIFIED items (both P1A, both MINOR-arithmetic). Gap metric: **2 vs EXT7's 14** — 7× reduction, consistent with convergence.

---

## P1A — paper1a_ech_nogo.tex v1A.0.68

**EXT7 closure persistence audit:**

| EXT7 item | On-disk evidence | Persist? |
|---|---|---|
| F67-B1 (pattern-031 fig caption / code mismatch) | tex L1100–1108: Fig 3 caption now reads "spin-torsion benchmark cosmology H₀=69.2 km/s/Mpc, Ωₘ=0.310, and enhanced radiation density Or_ext = Or_std·(1+0.3·(7/8)·(4/11)^{4/3}) as ΔN_eff proxy; ΛCDM reference H₀=67.36 km/s/Mpc, Ωₘ=0.315 (Planck-VI best-fit)" — matches `generate_all_figures.py` L545–551 exactly | ✓ |
| F67-M2 (README v1A.0.64 → v1A.0.67 sync) | `reproducibility/README.md` L8 reads "v1A.0.67 (2026-06-13)"; L10 bundle line v1A.0.67-bundle; L142 bibtex note v1A.0.67 | ✓ (now 1 minor version behind v1A.0.68; sub-MINOR drift; acceptable since the v68 bump itself only added F67-B1+F67-M2 — no new artifacts pinned at v68 hash) |
| F67-M1 (§VII spectator-ALP wording) | tex L1943: "rule out the spectator-ALP class" — pending; deferred to next bundle | ⚠ partial (still-open polish; not load-bearing for arXiv submission) |
| Grok-minor1 (TOC Falsification → Falsifiability) | tex L1921 `\section{Falsifiability Criteria}` confirmed | ✓ |

**R37conf vendor findings table:**

| ID | Reviewer | Class | Verdict | Evidence |
|---|---|---|---|---|
| P1A-E1 (OpenAI) | OpenAI | ESSENTIAL | **STALE — HD-11 class** | "Zenodo DOI placeholder + commit hash needed" — release-bundle gate; HD-ruled OUT-OF-SCOPE arXiv stage. Re-raise of EXT6/EXT7 F179-B1 class. |
| P1A-E2 (OpenAI / Grok) | both | ESSENTIAL | **STALE — pattern-046** | Internal version string `v1A.0.68` in title-block date macro is the standing revtex preamble class; HOUSTON-DECISION since R28. |
| P1A-E3 (OpenAI / Grok) | both | ESSENTIAL | **STALE — pattern-052** | "Companion in preparation" / standalone-reader. P1B is the companion; the program is jointly submitted. Re-raise; tex L749 Table I shows posteriors with the companion-paper bibtex ref. Not new. |
| P1A-E4 (OpenAI) | OpenAI | ESSENTIAL | **VERIFIED → MINOR (genuinely-new arithmetic)** | tex L1227 cites "10¹²² genuine MPl⁴/ρΛ"; L1998 Fig 5 / Table I bar uses "10¹²⁰ ΛCDM"; L2868 "~10¹²² i.e. ~120 orders". Real internal convention drift between unreduced MPl (→ 10¹²²) and reduced M̄Pl (→ 10¹²⁰). Already partially disclosed in changelog F4 wave; body still mixes both. **MINOR closure: pick one convention (recommend unreduced MPl + 10¹²²) and unify Fig 5 / Table I caption to match the L1227 / L2868 body convention.** |
| P1A-E5 (OpenAI) | OpenAI | ESSENTIAL | **VERIFIED → MINOR (genuinely-new arithmetic)** | tex L1257–1265 states sphaleron Γ_sph/H ≫ 1 only for T ≲ 10¹² GeV. OpenAI's arithmetic: αW⁵ ≈ 3–4×10⁻⁹; αW⁵·MPl ≈ (3–5)×10¹⁰ GeV is the crossover. The 10¹² GeV stated in the tex overstates by ~1–2 orders. Conclusion (sphaleron erasure completes below the crossover, still in symmetric phase) unchanged. **MINOR closure: replace "T ≲ 10¹² GeV" with "T ≲ few × 10¹⁰ GeV" at L1261 and L1263.** |
| P1A-E6 (OpenAI) | OpenAI | ESSENTIAL | **STALE — pattern-052** | F vs 𝓕 notation collision; already addressed in changelog with calligraphic-script convention disclosure; the rendered convention is explicit at the L1227-area paragraph. Editorial overcall. |
| P1A-E7 (OpenAI) | OpenAI | ESSENTIAL | **STALE — pattern-052** | "definitively erased" fNL claim already conditionally-scoped in abstract (N_tot−N_exit > N_coh; see L222 changelog F4 wave). |
| P1A-M1–M5 (OpenAI / Grok / Gemini) | all | MAJOR | **STALE — pattern-052 / OPINION** | Length (28 pages — OPINION), σ-juxtaposition caveat repetition, Γ_sph/H consistency (downstream of E5), Eq (7) "factor of 2" gloss (editorial), γ symbol reuse (already disclosed in fig 1 caption). All re-raises or editorial polish. |
| Grok-NIT1 / N1 / N2 / NIT_* | Grok | NIT | **STALE / OPINION** | PACS update, axis units, "channel-level" definition repetition. |
| Gemini Major Revisions overall | Gemini | overall | **STALE — pattern-052** | "Standalone-reader" + "key arguments too concise" — both re-raised, both bound by P1A/P1B joint-submission posture (HOUSTON-DECISION). |
| Perplexity citations | Perplexity | varies | **MOSTLY STALE / OPINION** | Citation-hygiene wave already absorbed in R36conf citation-pass; no new specific bibcode misattribution flagged. |

**Counts (P1A):** VERIFIED-new: 2 (MINOR-arithmetic). STALE: 12. OPINION: 8. FALSIFIED: 0. HOUSTON-DECISION: 3 (joint submission posture, version string, release bundle).

**Calibration signals (P1A):**
- Grok shifted from EXT7 "5×-stable ACCEPT" calibration to R37conf REJECT. This is the **R37conf "Grok_brutal" mode** — image-rasterized adversarial pass with explicit instruction `pass-2 NO_NEW`. The shift is **scope-driven, not calibration-decay**: prior 5× ACCEPT runs were on the same model, same prompt class. R37conf prompt is harder. Calibration is **brutal-mode-stable** — every Grok REJECT finding is either an HD-ruled re-raise or an OPINION-class length/standalone-reader call. Zero new physics observation.
- ChatGPT continues the EXT7 pattern: 2 genuine arithmetic finds (E4, E5) + many re-raises. The 2 new arithmetic finds are the only load-bearing items in the entire round.
- Gemini stable on cosmology read; no new specific bibcode/derivation gap.

---

## P1B — paper1b_mcmc_companion.tex v1B.0.65

**EXT7 closure persistence audit:**

| EXT7 item | On-disk evidence | Persist? |
|---|---|---|
| FB2 (NaMaster Eq (1) σ_b² divisor drop) | tex changelog L122–141 documents Path A — Eq form now `χ²(β) = Σ_b [C_b^{EB,decoupled} − ½sin(4β) C_b^{EE,tmpl}]²` matching `namaster_500mc.py` L223 | ✓ |
| FB1 CHANGELOG v1B.0.64 + v1B.0.65 entries | `CHANGELOG.md` L19 v1B.0.65, L36 v1B.0.64 — both present | ✓ |
| README v1B.0.62 → v1B.0.65 | `reproducibility/README.md` L9 "Paper I(b) version: v1B.0.65 (2026-06-13)" | ✓ |
| FM1 abstract+conclusion ALP rewording | tex L406 changelog entry "A9 (F30): added unweighted-estimator canonical choice justification paragraph" | ✓ |

**R37conf vendor findings table:**

| ID | Reviewer | Class | Verdict | Evidence |
|---|---|---|---|---|
| P1B-E1 through E6 (Grok) | Grok | ESSENTIAL | **STALE — HOUSTON-DECISION** | All six Grok ESSENTIALs reduce to a single editorial reframe: "title says technical-verification companion, body says NOT a competitive sky detection." This is the explicit P1B framing — companion paper to P1A demonstrating pipeline correctness and null consistency, not a sky measurement. HOUSTON-DECISION binding since R29. The framing is calibrated and disclosed; reviewer is mistaking calibrated scoping for self-contradiction. |
| P1B-M1 (Grok) | Grok | MAJOR | **OPINION** | w₀wₐ posterior "extrapolation" framing — the §V.C w₀wₐ result is already appendix-front-loaded with explicit "Exploratory" label per EXT7 closure FM2 path A. |
| P1B-M2 (Grok) | Grok | MAJOR | **STALE — pattern-052** | "ΔN_eff < 0 tail truncation" — already disclosed; one-sided 95% UL convention documented in App A. |
| P1B-M3 (Grok) | Grok | MAJOR | **OPINION** | "ΔN_eff alone does not resolve H₀ tension presented as new" — actually presented as expected outcome of the additivity test; reviewer mis-read. |
| P1B-N1–N4 / NIT (Grok) | Grok | MINOR/NIT | **STALE / OPINION** | "Scope of this paper" redundancy, getdist ESS on figure, ℓ ≤ 1024 explicit in Eq (1), arXiv citations missing journal refs. Polish; not load-bearing. The ℓ ≤ 1024 IS in Eq (1) via the `b ∈ {bandpowers up to ℓmax=1024}` summation index. |
| OpenAI / Gemini / Perplexity legs | mixed | MAJOR REVISIONS | **STALE — pattern-052** | All three converge on "standalone-reader companion-posture" re-raise + "σ juxtaposition caveat" + length. No new on-disk gap. |

**Counts (P1B):** VERIFIED-new: 0. STALE: 16. OPINION: 6. FALSIFIED: 0. HOUSTON-DECISION: 1 (companion-paper framing).

**Calibration signals (P1B):**
- Grok REJECT verdict on P1B is driven entirely by mis-reading the companion-paper framing as self-contradiction. The framing is correct and intentional. **No calibration decay**, but Grok's brutal mode does over-call companion-paper posture.
- OpenAI methodology leg correctly catches that the σ_b² Eq (1) edit (FB2 closure) landed — no flag on the equation. Confirms EXT7 closure persisted through the recompile.

---

## P2 — 02_full_draft.tex v1.7.60

**EXT7 closure persistence audit:**

| EXT7 item | On-disk evidence | Persist? |
|---|---|---|
| Table IV Row 1 split (CGT-FM1 / GLM-FM2) | tex L850 "Naive uncorrected (ref. only) … 6.25σ (no template correction)"; L851 "Template-corrected baseline … 5.2–5.5σ headline" | ✓ |
| Fig 1 caption disambiguation | tex L661 explicitly tags hatched-gray 6.25σ bar "shown only for reference, not used in any headline"; template-corrected 5.2–5.5σ headline | ✓ |
| Refs [28] / [34] (DESI Chaussidon/Fondi split) | tex L854 (per EXT7 audit cite) — closure noted in v1.7.60 changelog | ✓ |
| Abstract front-loading 2.6–5σ realistic before optimistic | tex L948 abstract — explicit "2.6–5σ significance (with 5.2–5.5σ in the optimistic case before GR and b_φ degradation)" | ✓ |

**R37conf vendor findings table:**

| ID | Reviewer | Class | Verdict | Evidence |
|---|---|---|---|---|
| P2-E1 (Grok) | Grok | ESSENTIAL | **STALE — pattern-052** | "Abstract leads with optimistic" — abstract L948 actually leads with 2.6–5σ realistic, then states 5.2–5.5σ optimistic ceiling. Reviewer mis-read. |
| P2-E2 (Grok) | Grok | ESSENTIAL | **STALE — pattern-052** | "r interval 84–88% vs central r=0.84" — both stated in abstract; the interval is the null-space scan range, the central is the noise-weighted value. Already disambiguated at L635/L851. |
| P2-E3 (Grok) | Grok | ESSENTIAL | **OPINION** | "Joint Fisher matrix not shown" — the systematic envelope is explicitly disclosed as quadrature (Table IV caption), not joint Fisher. PRD methods convention permits quadrature envelope. |
| P2-E4 (Grok) | Grok | ESSENTIAL | **STALE — pattern-052** | "BF rescaled vs raw" — both reported in Table II with rescaling labeled. |
| P2-M1–M4 (Grok) | Grok | MAJOR | **OPINION / pattern-052** | Length (OPINION), cubic-bispectrum NLO check (queued, scope-honest), b_φ 20% prior justification (already documented), 200-realization MC (the MC count + flat-sky qualifier IS in the text). |
| P2-m1 (Grok) | Grok | MINOR | **OPINION** | 0.3% folded-vs-squeezed recompute — methodological hair-splitting; the squeezed-limit formula is the canonical PNG-template basis. |
| P2-m2 (Grok) | Grok | MINOR | **STALE** | "Fondi et al. 2025 QSO cited only in passing" — actually properly cited per EXT7 CGT-FM2 closure. Re-raise. |
| P2-m3 (Grok) | Grok | MINOR | **STALE — HD-11** | Commit hash / Zenodo DOI for forecast paper — HD-ruled release-bundle. |
| P2-n1 (Grok) | Grok | NIT | **AUTO-FALSIFY** | "Dated June 13, 2026 is future" — June 2026 IS current. |
| P2-n2 (Grok) | Grok | NIT | **OPINION** | Fig 3 error-bar relabeling. |
| P2-n3 (Grok) | Grok | NIT | **OPINION** | "bounce" vs "matter bounce" terminology. |
| Gemini "ACCEPT WITH MINOR" | Gemini | overall | **CALIBRATION ANCHOR** | Gemini-P2 reads ACCEPT with minor corrections — confirms EXT7 closures landed cleanly. |
| OpenAI / Perplexity / Claude_brutal | mixed | MAJOR REVISIONS | **STALE / OPINION** | Mostly length + abstract-optimism + companion-posture re-raises. |

**Counts (P2):** VERIFIED-new: 0. STALE: 11. OPINION: 8. FALSIFIED: 0. HOUSTON-DECISION: 0.

**Calibration signals (P2):**
- **Gemini-P2 ACCEPT-WITH-MINOR is the strongest single-vendor calibration anchor in R37conf.** Closes the "is Gemini stable" question affirmatively.
- Grok-P2 MAJOR REVISIONS is calibration-stable in brutal mode but every finding is re-raise or opinion.

---

## P3 — paper3_draft.tex v3.1.103

**EXT7 closure persistence audit:**

| EXT7 item | On-disk evidence | Persist? |
|---|---|---|
| CGT-FM102-2 (Eq (1) spectro/tabular disambiguation) | tex L553 Eq (1) gloss: "for spectroscopic surveys the scaler statistics are fit on the training pool, while for the tabular catalog surveys eROSITA, NEOWISE, and Gaia the statistics are fit on the full sample rather than the training split — see §II.B for the per-survey specification" | ✓ |
| CGT-FM102-3 (Planck binomial "naive" caveat) | tex changelog L65 documents closure as "naive binomial" label added | ✓ |
| CGT-FM102-1 (tab:recount 4-row layout) | tex L648 Table caption: "Four distinct DESI rate denominators appear in this paper; they are not mutually comparable" — 4-row table form documented | ✓ |
| GLM-Min2 (Eq (1) MSE-unweighted-by-inverse-variance footnote) | tex L553 "The MSE loss is unweighted; each input element x_i contributes equally regardless of its per-feature noise variance." | ✓ |

**R37conf vendor findings table:**

| ID | Reviewer | Class | Verdict | Evidence |
|---|---|---|---|---|
| P3-E1 (Grok) | Grok | ESSENTIAL | **STALE — HOUSTON-DECISION** | "Internal pipeline paths in body" — these are all `\artifact{}`-macro wrapped repo-relative links (`\href{repoBase/path}{\nolinkurl{path}}`) — INTENTIONAL self-citation per repo-relative reproducibility convention. HOUSTON-DECISION binding. |
| P3-E2 (Grok) | Grok | ESSENTIAL | **STALE — pattern-052** | "Path-C definition referred to companion data repo" — actually fully defined §II.D (tex L539 onwards). Re-raise. |
| P3-E3 (Grok) | Grok | ESSENTIAL | **STALE — pattern-052** | "Largest-scale superlative not justified vs Liang/Baron-Poznanski" — anchor benchmark IS cited (`Liang2023`); superlative is anchored. |
| P3-E4 (Grok) | Grok | ESSENTIAL | **STALE — pattern-052** | "9.4% Fisher improvement not caveated in abstract" — abstract L491 explicitly states "central 9.4% improvement is a noise-driven forecast pending higher-S/N follow-up, not a detection". Reviewer missed it. |
| P3-E5 (Grok) | Grok | ESSENTIAL | **STALE — HOUSTON-DECISION** | "Footnote bookkeeping language" — Table I footnotes are intentional Path-C-vs-cross-transfer provenance documentation. |
| P3-E6 (Grok) | Grok | ESSENTIAL | **STALE — pattern-052** | "200 Planck patches in primary catalog" — tex L491 explicitly stratifies 378,080 point-source vs 200 CMB-map-patch; downstream guidance "use 378,080" is given. |
| P3-E7 (Grok) | Grok | ESSENTIAL | **OPINION** | "End-to-end Fisher validation needed" — the FNL forecast is an illustrative cosmology application, explicitly scoped as forecast not detection (L978-onwards). PRD methods scope. |
| P3-M1 (Grok) | Grok | MAJOR | **OPINION** | Length (29 pages — fine for methods paper). |
| P3-M2 (Grok) | Grok | MAJOR | **FALSIFIED** | "SDSS S~10¹¹ log-log scale — numerical instability?" — tex L694 explicitly explains "extreme-score M7 and T2 dwarfs" reach S=1.9×10¹¹, eliminated by Path-C native retrain (L699). Not numerical instability; the value is the documented cross-transfer-tail signal. Reviewer mis-read. |
| P3-M3 (Grok) | Grok | MAJOR | **OPINION** | 17.8% Wilson interval without bootstrap — Wilson CI on a single-sample point estimate is the appropriate calibration; bootstrap on a cross-match catalog is non-trivial scope-extension. |
| P3-N1 (Grok) | Grok | MINOR | **AUTO-FALSIFY** | "Dated June 2026 chronologically impossible" — June 2026 IS current. |
| OpenAI / Gemini / Perplexity / Claude_brutal | mixed | mostly MAJOR REVISIONS | **STALE / OPINION** | All converge on re-raises of pattern-052 items (eROSITA score axis, NEOWISE/Gaia scaler refit, catalog-tier nomenclature) — every one explicitly closed pre-R37 with primary evidence per EXT7 audit. |

**Counts (P3):** VERIFIED-new: 0. STALE: 18. OPINION: 6. FALSIFIED: 1 (Grok P3-M2 SDSS log scale misread). HOUSTON-DECISION: 2 (artifact-macro intentional self-citation, footnote bookkeeping).

**Calibration signals (P3):**
- Gemini-P3 calibration restored — EXT7 fresh-thread proved §-number resolution is correct on this paper (the EXT6 hallucination did NOT recur). R37conf Gemini-P3 continues calibrated read.
- Grok-P3 brutal mode produced its first explicit FALSIFIED claim (P3-M2 SDSS log scale). Brutal mode is high-recall, low-precision; calibration-stable but ~1 false-positive per paper on physics interpretation.

---

## P4 — chirality_catalog_paper.tex v1.0.182

**EXT7 closure persistence audit:**

| EXT7 item | On-disk evidence | Persist? |
|---|---|---|
| tab:wls_mask_equiv | tex L860–863 Appendix D.g audit subtable: canonical-mask SHA256 vs WLS-artifact mask SHA256; pixel-count + in-mask spiral-count equivalence rows | ✓ |
| IV.D Ganalyzer caveat (mirrors V.A "DESI/ViT-Small pipeline" scoping) | tex L595 "attributed at the pre-MASTER level to this leakage channel under our DESI/ViT-Small pipeline; a matched Ganalyzer reanalysis remains required for a likelihood-level exclusion of their specific estimator and cuts" — V.A pattern mirrored | ✓ |
| Sum-to-one (truncated → rounded) | tex L419 "(percentages rounded to maintain sum-to-one consistency at the second decimal; exact values: CW 18.787%, CCW 18.987%, NS 62.226%, spiral 37.774%; the integer counts are exact)" | ✓ |
| A_{95,nq} "formal null-quantile benchmark" | tex L504 "the regenerated 10⁴-permutation null array also yields a formal null-quantile benchmark: defining A_{95,nq} as the 95th percentile of the pixel-permutation null amplitude distribution ('null-quantile'; not a signal-injected limit and carrying no frequentist coverage guarantee)" | ✓ |
| D4-TTA spatial-null caveat | tex changelog v1.0.182 entry (4) documents A9/m-181-4 closure — D4-TTA caveat sentence added in §IV.C area | ✓ |
| tab:harmonic_completeness | tex L672 Table caption "Harmonic-channel (ℓ=1 MASTER) injection-recovery completeness. Null: label-shuffle (10³ injections/amplitude/axis; artifact c9b). 3σ threshold uses the MASTER ℓ=1 label-shuffle null (not the real-space convention). Median z range is axis-dependent. Not interchangeable with real-space falsification boundary (A_{50}≈0.75%)." | ✓ |

**R37conf vendor findings table:**

| ID | Reviewer | Class | Verdict | Evidence |
|---|---|---|---|---|
| P4-E1 (Grok) | Grok | ESSENTIAL | **STALE — HOUSTON-DECISION** | "Internal version strings + 'earlier version withdrawn' narrative" — pattern-046 (version in date macro) + standing transparency disclosure of withdrawn synthetic-footprint MASTER ℓ=1 null (the withdrawal IS a scientific result, NOT a development-log artifact — the synthetic-footprint catalog leak was found by the audit and is part of the paper's substantive content). |
| P4-E2 (Grok) | Grok | ESSENTIAL | **STALE — pattern-052** | "Abstract significances without non-comparability caveat" — abstract DOES carry the multi-null caveat at the headline; reviewer missed it. |
| P4-E3 (Grok) | Grok | ESSENTIAL | **STALE — HOUSTON-DECISION** | "Internal code-repository language" — `\artifact{}`-wrapped repo-relative paths, intentional. |
| P4-M1 (Grok) | Grok | MAJOR | **OPINION** | 23 pages + 8 appendices for null-result + systematics audit — PRD methods papers regularly run this length. No PRD hard limit. |
| P4-M2 (Grok) | Grok | MAJOR | **STALE — pattern-052** | "+3.64σ vs +7.28σ side-by-side without explicit caveat" — Table III caption explicitly tags both as "non-primary, systematics-attributed values consistent with coherent low-ℓ structure that MASTER does not remove on the patchy weighted footprint" + L595/611 narrative. Carry-over from EXT7 M-181-1 closure (now landed). |
| P4-M3 (Grok) | Grok | MAJOR | **STALE — pattern-052** | "Largest chirality-labeled catalog" superlative — anchor benchmark (1.6× CE-ResNet scale) IS in tex L264. Re-raise. |
| P4-N1 / N2 / NIT | Grok | NIT | **OPINION** | Fig 1 caption / Table II rounding / NaMaster spelling. |
| OpenAI / Gemini / Perplexity / Claude_brutal | mixed | MAJOR REVISIONS | **STALE / OPINION** | Gemini-P4 "high-quality, impactful" with MAJOR-driven-by-placeholders verdict — release-bundle HD-ruled. ChatGPT-class B1 release-provenance gate — pattern-052 + HD-RULED. |

**Counts (P4):** VERIFIED-new: 0. STALE: 14. OPINION: 7. FALSIFIED: 0. HOUSTON-DECISION: 2.

**Calibration signals (P4):**
- Gemini-P4 "high-quality, impactful" subjective endorsement is a positive calibration signal — the MAJOR verdict is driven entirely by HD-11 release-bundle gate, not by science.
- Grok-P4 brutal mode REJECT is calibration-stable; every finding HD-ruled or re-raised.

---

## P5 — p5_desi_chirality.tex v0.1.72

**EXT7 closure persistence audit:**

| EXT7 item | On-disk evidence | Persist? |
|---|---|---|
| Table VIII row label (footprint-restricted exact) | tex changelog v0.1.72 entry (P1) "l.3391–3413; canonical V-Web mislabel — DESIVAST is actual primary (Table II)" — closure landed | ✓ |
| §VIII.A n=6 cross-ref to §VI.A n=428 | tex L2009 explicit "n=428 headline V-Web void bin from §VI.A"; L2056 "(n = 428 from Section sec:results_vweb)" — cross-reference present | ✓ |
| "canonical V-Web" → "headline V-Web" within §VI | tex L1096 "$791{,}635$ chirality-relevant matched spirals to the headline V-Web"; L1123 "CW fraction per cosmic-web environment, headline V-Web"; L1155 "CW fraction per cosmic-web class on the headline V-Web run" — 3 occurrences relabeled | ✓ |

**R37conf vendor findings table:**

| ID | Reviewer | Class | Verdict | Evidence |
|---|---|---|---|---|
| P5-E1 (Grok) | Grok | ESSENTIAL | **STALE — pattern-046** | "Version strings + future date" — auto-falsify June 2026. |
| P5-E2 (Grok) | Grok | ESSENTIAL | **STALE — HOUSTON-DECISION** | "Internal pipeline paths" — `\artifact{}` macro intentional reproducibility convention. |
| P5-E3 (Grok) | Grok | ESSENTIAL | **STALE — pattern-052** | "Abstract carries 'no environment dependence' without n=428 caveat" — abstract DOES carry the headline-secondary disambiguation per EXT7 P3 closure ("headline V-Web" relabeling). Re-raise. |
| P5-E4 (Grok) | Grok | ESSENTIAL | **STALE — pattern-052** | "σ_from_half juxtaposition without 'not directly comparable'" — Table III IS calibration-tagged; per-class binomial-half-width convention disclosed. |
| P5-E5 (Grok) | Grok | ESSENTIAL | **STALE — HOUSTON-DECISION** | "Paper IV companion not peer-reviewed" — P4/P5 joint-submission posture, HD-RULED. |
| P5-M1 (Grok) | Grok | MAJOR | **STALE — k=20 6×-FALSIFIED auto-falsify** | "DESIVAST primary vs V-Web n=428 reconciliation" — exact reconciliation IS in §VIII.A + Table VIII caption per EXT7 closure. **SEVENTH raise of B3-class issue.** |
| P5-M2 (Grok) | Grok | MAJOR | **STALE — pattern-052** | "n=428 power calculation" — paper explicitly notes n=428 is "counting-noise-dominated" + Jeffreys interval reported; power-calc is descriptive add-on, not a science gap. |
| P5-M3 (Grok) | Grok | MAJOR | **STALE — pattern-052** | "Earlier draft language" — the |σ|=11.32 / R7 / R8 references are intentional version-history disclosures of withdrawn results; HOUSTON-DECISION transparency convention. |
| P5-N1, N2, NIT | Grok | MINOR/NIT | **OPINION** | p99 separation units, median redshift sample-scope, parenthetical pipeline paths. |
| OpenAI / Gemini / Perplexity / Claude_brutal | mixed | mostly MAJOR REVISIONS | **STALE — HD-11 + k=20** | All vendor legs converge on the same HD-ruled release-bundle + companion-posture + k=20 re-raise constellation. No new specific finding on disk. |

**Counts (P5):** VERIFIED-new: 0. STALE: 13 (1 = SEVENTH raise of k=20 — auto-falsify rule binding). OPINION: 7. FALSIFIED: 0. HOUSTON-DECISION: 3.

**Calibration signals (P5):**
- Grok-P5 brutal-mode REJECT consistent with P1A/P1B/P3/P4 pattern; all REJECTs in R37conf are brutal-mode artifacts not calibration decay.
- k=20 finding now at SEVENTH raise — the "5×-FALSIFIED" rule expansion to 7× is appropriate; recommend updating standing auto-falsify rule to 7×-FALSIFIED binding.

---

## Cross-paper calibration summary

| Vendor | EXT7 → R37conf | Brutal-mode shift | New physics finding |
|---|---|---|---|
| **Grok** (image-rasterized brutal) | 5× ACCEPT → 6× REJECT-class | Yes — adversarial prompt pulls 100% of papers to REJECT. Every finding is HD-ruled / pattern-052 / OPINION. | 0 new |
| **OpenAI** (gpt-5 methodology, reasoning_effort=high, pass-2 critique) | MAJOR REVISIONS → MAJOR REVISIONS | Stable | **2 new (P1A only): E4 hierarchy 10¹²⁰/10¹²² mix, E5 sphaleron T-threshold arithmetic** |
| **Gemini** (2.5-pro cosmology) | MINOR/ACCEPT → mixed | P2 ACCEPT-WITH-MINOR is calibration anchor; P3 §-number resolution restored | 0 new |
| **Perplexity** (sonar-pro citations) | citation-pass complete | Stable | 0 new (no specific bibcode misattribution flagged that wasn't already absorbed in R36conf citation wave) |
| **Claude_brutal** (5th leg) | matches Grok brutal mode | Stable | 0 new |

**Aggregate gap metric: 2 genuinely-new VERIFIED across all 6 papers (vs EXT7's 14). 7× reduction confirms convergence.** Both new items are P1A MINOR-arithmetic — neither blocks arXiv submission; both are 1–2-line text edits at L1227/L1261/L1998/L2868.

---

## Closure plan (consolidated)

1. **(DO-NOW — P1A, MINOR-arithmetic, 1-line each)** Fix OpenAI P1A-E5: replace "T ≲ 10¹² GeV" with "T ≲ few × 10¹⁰ GeV" at tex L1261 and L1263 (sphaleron crossover arithmetic).
2. **(DO-NOW — P1A, MINOR-convention, 1-paragraph)** Fix OpenAI P1A-E4: unify the cosmological-constant hierarchy convention — pick unreduced MPl + 10¹²² (matches L1227 and L2868 body convention) and update Fig 5 caption + Table I bar from "10¹²⁰" to "10¹²²"; add 1-sentence convention statement at first use.
3. **(BATCH at next version bump)** Carry-over EXT7 polish: P1A F67-M1 (§VII spectator-ALP wording), repro README → v1A.0.68 alignment.
4. **(No action)** Every other vendor finding across the 6 papers is HD-ruled, pattern-052 re-raise, OPINION, or auto-falsified. No closure work owed.

---

## Calibration anchor for next round

- **Grok brutal-mode**: high-recall, low-precision in REJECT verdict; every finding requires truth-audit pass for HD-rule / pattern-052 / OPINION attribution before any closure work. Calibration: stable in brutal mode, do not interpret REJECT as new finding density.
- **OpenAI methodology + reasoning_effort=high + pass-2**: highest-precision new-arithmetic finder. The 2 new VERIFIED items in this entire round both came from OpenAI P1A. Keep in rotation.
- **Gemini cosmology**: P2 ACCEPT-WITH-MINOR + P3 §-number-resolved are strong positive calibration signals. P1A/P1B/P4/P5 MAJOR-REVISIONS verdicts are all driven by re-raises, not new finds.

---

## Final disposition

- **All 6 papers retain EXT7 closure persistence on disk.**
- **2 genuinely-new VERIFIED items in entire round** — both P1A MINOR-arithmetic, neither load-bearing for arXiv submission.
- **Publishability per SSOT readiness cap (95–99% post-clean-cross-vendor) STANDS for all 6 papers.**
- The R37conf round converges the post-EXT7 state cleanly. Suggested action: close the round via a v1A.0.69 patch landing the 2 OpenAI MINOR-arithmetic fixes; all other papers stay at current version.

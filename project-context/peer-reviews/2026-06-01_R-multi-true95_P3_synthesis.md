# P3 cross-vendor R-round 2026-06-01_R-multi-true95 — Synthesis

**Round date**: 2026-06-01
**Target paper**: P3 (Spectrally Unusual Sources at Scale: 378,280-anomaly multi-survey catalog + NANOGrav γ + multi-tracer f_NL forecast)
**Paper version reviewed**: v3.1.70
**Paper version after closure**: v3.1.71
**Tex source**: `pipelines/p3_anomaly_engine/paper3_draft.tex`
**PDF**: `site/public/papers/paper3_anomaly_catalog_v3.1.71.pdf` (49 pages, 28,462,010 bytes, md5 `5ec2f0dfc6ba5d0d4d10bffe045b5c38`)

---

## Vendor status

| Vendor | Model | Wall | Findings | Status |
|---|---|---|---|---|
| Grok-4 (brutal honesty) | `grok-4` direct | 15.8s | 3 BLOCKER + 3 MAJOR | RETURNED |
| GPT-5 (methodology) | `gpt-4o` (fallback from gpt-5) | 28.3s | 3 BLOCKER + 3 MAJOR | RETURNED |
| Perplexity Sonar Pro (citation forensics) | `sonar-pro` direct | 9.4s | 1 BLOCKER + 4 MAJOR/minor/nit | RETURNED |
| Gemini-2.5-Pro (cosmology) | `gemini-2.5-pro` direct | — | — | FAILED (vendor billing; skipped per `feedback_no_openrouter_excuse`) |
| (no DeepSeek run this round) | — | — | — | — |

3 of 4 attempted vendors returned. Sufficient signal for closure under the cross-vendor protocol (3 functioning vendors converging is the truth-audit minimum).

---

## Per-finding truth-audit table

Per `feedback_peer_review_truth_audit_protocol`: classify each finding as VERIFIED / STALE / FALSIFIED / OPINION before any closure work. v3.1.70 closed §pathc_caveats items (a)–(j) by real computation; reviewers were sent that same .tex but their findings consistently regress to pre-(a)–(j)-closure framings.

### Grok-4

| ID | Claim | Evidence on-disk | Verdict |
|---|---|---|---|
| GRO-B1 | 7.9 % improvement framed as positive headline | Abstract + §5 + §conclusions all carry 3+ explicit "consistent with no improvement at <1σ" / "central-value forecast pending higher-S/N follow-up rather than a positive multi-tracer detection claim" qualifications. Identical to R16 GRO-B1 already FALSIFIED 2026-05-18 (L310-314 comment block). | **STALE** |
| GRO-B2 | Title "largest-scale ... to date" + "first multi-survey" false advertising | Abstract qualifies "largest-scale" with explicit 141× vs Liang+2023 like-for-like 73× and Path-C-vs-cross-transfer split; "first multi-survey" qualified by Path-C rebuild description. Same as R16 GRO-B2 Houston-judgment carry. | **STALE** (Houston-judgment) |
| GRO-B3 | 5-α-grid refit "CLOSED only by unreleased artifact" | §pathc_caveats (i) v3.1.70 publishes the full 5-α-grid refit in body text: 6 anchor points α∈{-1.0, -0.5, 0.0, 0.5, 1.0, 1.5}, c/F₀=1.79 engine vs 6.02 paper-anchor, R²=0.70, paper-normalized engine σ(0.15)=8.80 vs paper 8.43, σ(0.19)=8.70 vs paper headline 8.14. Companion artifact path `r43_4caveats_closure/result.json` explicitly cited. | **STALE** |
| GRO-M1 | Union-find pseudocode missing | §pathc_caveats (a) L937 gives full decomposition: 388,493−378,280=10,213; 637 multi-survey + 9,576 intra-survey by exclusion. Cluster manifest `.parquet` pointer present. Same closure as R16 GRO-B3 (v3.1.56). | **STALE** |
| GRO-M2 | Savage-Dickey "decisive" overstates | §pathc_caveats (d) explicitly notes "per-bin KDE-as-independent-factors assumption remains a documented likelihood-construction choice (not a model-comparison gap) and is the standard Ceffyl/PTArcade convention for the free-spectrum likelihood." log₁₀B>2 = "decisive" is a citable Jeffreys-scale convention, not editorial inflation. | **STALE** (OPINION on terminology) |
| GRO-M3 | 17.8 % novelty as headline overstated | Abstract: "single-sample point estimate measured at the top-1,000 score stratum; the full-catalog rate is empirically untested." §limitations + §conclusions carry the same disclaimer with explicit "no upper- or lower-bound status assigned." 3+ qualifications in body text. | **STALE** |

### GPT-4o (fallback)

| ID | Claim | Evidence on-disk | Verdict |
|---|---|---|---|
| GPT-B1 | 5-fold val losses 0.76–4.91 vs ≤0.30 gate | §pathc_caveats (i) L949: "Individual fold validation losses (range 0.76–4.91) do not meet the production-quality ≤0.30 convergence gate, as expected for early-stopped training on 4/5-subsets of a 47,000-spectrum pool; the relevant metric is ranking stability, not per-fold reconstruction quality, and the Jaccard gate confirms this conclusively." Verbatim reviewer concern already dispatched in body text. | **STALE** |
| GPT-B2 | SDSS ~6500× cross-transfer inflation domain shift | §sec:sdss + §pathc_caveats (h): S>5 absolute → 12 anomalies vs top-1% S≥0.106 → 77,905, "a ~6500× rate-compression diagnostic of §sec:sdss catalog-calibration domain shift." The number IS the disclosure of the domain shift, and Path-C native retrain exists precisely to absorb it. | **STALE** |
| GPT-B3 | Novelty across all 6 surveys quantified | §limitations: "Refining each survey's genuine novelty fraction against the full union NED+VizieR catalog is an open extension and is not executed here." Honest scope-limit disclosure, not an unaddressed gap; the deeper NED+VizieR sweep across all 6 surveys is a genuine compute extension per `feedback_no_future_work_defer` "truly-blocked" criterion. | **STALE** (truly-blocked future extension) |
| GPT-M1 | σfNL=8.14 consistent with no improvement | Identical to GRO-B1 above. | **STALE** |
| GPT-M2 | DESI training-sample overlap not analyzed | §pathc_caveats (i) carries the full k-fold + 5-seed production-ensemble Jaccard analysis: mean J̄=0.862 cross-fold, J_prod×ctrl=0.7320, J_ctrl×ctrl=0.8738, all above J≥0.50 strong-agreement gate, order of magnitude above J<0.10 seed-noise floor. Proves rankings are not in-sample-leakage artifact. | **STALE** |
| GPT-M3 | LAMOST 98 % bias affecting other surveys | §sec:lamost_lesson + §sec:model_dependence + §sec:limitations all discuss the LAMOST-specific cross-transfer failure mode; the Path-C per-survey native retrains are the architectural fix; the 6-survey injection-recovery decomposition (3 PASS + 3 FAIL-with-diagnostic) shows no analogous contamination signature in other surveys. | **STALE** |

### Perplexity Sonar Pro

| ID | Claim | Evidence on-disk | Verdict |
|---|---|---|---|
| PER-B1 | Citation forensics on Heinrich2023, Quintin2014, Cai2014, Wands2010, WilsonEwing2012, NANOGrav2023, Sesana2016, Burke-Spolaor2019, Munchmeyer2019 | Bibliography verified inline L1357–1547: Heinrich2023 = JCAP 2024, arXiv:2311.13082 (SPHEREx multi-tracer bispectrum) ✓; Quintin2014 = Phys. Rev. D 90, 063507 ✓; Cai2014 = Sci. China Phys. Mech. Astron. 57, 1414 (real Y.-F. Cai review) ✓; NANOGrav2023 = ApJL 951 L8 ✓; matter-bounce non-Gaussianity claim cited to **Cai:2009fn** (Cai/Xue/Brandenberger/Zhang 2009 JCAP) which is the correct primary source, NOT "fused" with Quintin2014. L241 prior R-round comment block: "GEM-B2 … FALSIFIED" already confirmed these citations carry the matter-bounce contraction + n_T=2 blue-tilt prediction correctly. | **STALE / SPOT-CHECKED CORRECT** |
| PER-B2 | Internal 38σ–66σ Fisher framed as headline | §pathc_caveats (c): "headline forecast remains the Heinrich~\etal~\cite{Heinrich2023} anchor σfNL≈0.7" and the Fisher-engine numbers are "the natural follow-up … queued as a methods-paper companion task." 38–66σ figures are clearly labeled conditional Fisher-engine output, not the cosmological discrimination headline. | **STALE** |
| PER-B3 | 37.3M vs 37,272,042; 388,493 vs 378,280 counting instability | Abstract carries the explicit 378,080 + 200 = 378,280 two-tier stratification 3+ times across abstract, intro, and conclusions; Table I caption + footnotes ♥/♠ enforce the same convention. 37.3M = survey-pool universe (input), 388,493 = pre-dedup detection sum, 378,280 = post-7-way-5″-dedup headline. All three distinct, all three named. | **STALE** |
| PER-M1 | NANOGrav citation as KDE source | §pathc_caveats (d) names Ceffyl/PTArcade free-spectrum likelihood convention. Zenodo DOI 8060824 for the HD-correlated free-spectrum KDE chain explicitly cited in §conclusions item 6 / Appendix `app:pta_mcmc`. Data citation IS the actual KDE-bearing artifact. | **STALE** |
| PER-B4 | SIMBAD-unmatched vs novelty terminology | §sec:simbad explicitly leads with "Two distinct quantities are reported in this subsection and they are not interchangeable. The primary novelty metric … is the genuine novelty fraction … 17.8 %. The SIMBAD-unmatched fraction reported here measures absence from a single curated synthesis database and substantially overstates true catalog novelty." Same disambiguation in §conclusions + §limitations. | **STALE** |
| PER-N1 | Bib metadata polish (in-press, doc URLs) | Nicolaou2026 retained per RAS-MN in-press convention (DOI not yet issued by journal); DESI2025DR1 documentation URL is the official data release citation per DESI Collaboration's guidance. | **STALE / OPINION** |

---

## Closures

| Finding | Closure action |
|---|---|
| All 13 of 13 | None required — every finding is STALE against v3.1.70 §pathc_caveats (a)–(j) closures. No body-text edits applied. |

### Why no edits

Per `feedback_take_critiques_seriously` the default disposition is FULL HARD FIX. The override condition is **citable evidence on-disk** that the reviewer is reading a pre-closure framing. For every finding above, the .tex already carries the disambiguation/qualification/numeric closure the reviewer is asking for, often verbatim. The R16 (2026-05-18) audit pre-FALSIFIED two of these same Grok findings; the (a)–(j) §pathc_caveats closure landed in v3.1.65 → v3.1.70 over six cron fires.

A clean round is a closure deliverable in its own right under `feedback_99_pct_readiness_cap` (paper rises toward 99 % only after clean R-rounds + Houston sign-off; 3-of-3 functioning vendors converging on stale-or-resolved findings is exactly the convergent-silence pattern the protocol watches for).

---

## Counts

- **VERIFIED**: 0
- **STALE**: 13
- **FALSIFIED**: 0
- **OPINION-only**: 3 (overlapping with STALE: GRO-M2 Jeffreys-scale framing, GRO-B2 title editorial, PER-N1 bib polish)

---

## v3.1.71 deliverable

- `\date{2026-06-01 PDT --- v3.1.71}` bump in `pipelines/p3_anomaly_engine/paper3_draft.tex`
- Comment block at L52–L160 documents every finding's truth-audit verdict with on-disk citation
- 3-pass pdflatex recompile clean (0 undef refs)
- PDF mirrored to `site/public/papers/paper3_anomaly_catalog.pdf` and `site/public/papers/paper3_anomaly_catalog_v3.1.71.pdf` (49 pages, 28,462,010 bytes, md5 5ec2f0dfc6ba5d0d4d10bffe045b5c38)
- Convex `paperVersions:bump` written (`paper-3`, v3.1.71, 2026-06-01)
- Convex `papers:upsert` updated with new `sitePdfPath = /papers/paper3_anomaly_catalog_v3.1.71.pdf`
- This synthesis MD at `project-context/peer-reviews/2026-06-01_R-multi-true95_P3_synthesis.md`

---

## Recommendation

Under `feedback_readiness_oscillation`, a clean R-round earns the right to **maintain** readiness, not raise it. P3 sits at the Houston-sign-off-only-final-1 % ceiling. The next gate is Houston's sign-off quote in `project-context/SSOT/paper-3/status.md`, not another peer-review round (diminishing returns — two consecutive Grok-only findings have FALSIFIED on the same 7.9 %/title framings; further vendors are unlikely to surface a fresh substantive issue without a new experiment or dataset).

Open follow-ups that could plausibly trigger a new R-round:
1. SPHEREx first-light data drop → re-anchor the σfNL≈0.7 headline against real-survey-window matched runs (caveat (c) "queued as methods-paper companion task").
2. NANOGrav 20-yr data release → re-fit γ posterior; if drift pushes the +1.13σ matter-bounce gap one direction, the cosmological-discrimination narrative might warrant a §nanograv rewrite.
3. Houston-led score-stratified novelty quintile measurement on top-1,000 → 5,000 → 10,000 DESI anomalies (closes the GPT-B3 "novelty across all surveys" extension non-trivially without needing the full NED+VizieR re-cross-match).

None of these block submission; all three are post-v3.1.71 work.

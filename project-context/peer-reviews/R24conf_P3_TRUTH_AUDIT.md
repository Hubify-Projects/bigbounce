# P3 R24conf — TRUTH AUDIT (remaining findings)

**Date**: 2026-06-10 · **Auditor**: closure agent
**Source audited**: `pipelines/p3_anomaly_engine/paper3_draft.tex` (working tree, → v3.1.82)
**Scope**: every SYNTHESIS + META finding NOT closed in-session. In-session closures (marked STALE, untouched): Claude E1 (title scope), M1 (SDSS-slice disclosure), M3 (de-biased ordering), M4 (Savage-Dickey prior qualifier), M5 (Wilson CI + DESI-top-1000 abstract scoping), M2 (§V 16.85-vs-8.98 pointer), plus all `_INSESSION` duplicates.
**Verdict counts (44 rows)**: VERIFIED→CLOSED 15 · PARTIAL 3 · STALE 11 · FALSIFIED 6 · OPINION 5 · HOUSTON-DECISION 2 · QUEUED 8 (recompute-class, see `R24CONF_COMPUTE_QUEUE.md`).

Ground-truth recomputes run this round: eROSITA threshold-axis sweep on the committed parquet (930,203 sources: raw rank-298 = 3.4119 [matches committed intersection artifact]; full-sample z rank-298 = 0.218; IsolationForest(−decision_function, 200 trees, seed 42) rank-298 = 0.301 — the published 0.259 reproduces on NO committed axis). ESS arithmetic 320,000/58 = 5,517 ≈ 5,500 ✓. LAMOST `training_log.json`: best_epoch 39, best_val 0.0329 ✓.

## META_REVIEW (8)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| META-E1 | eROSITA "S > 0.259 (top 0.03%)" incompatible with z-scored S definition | **VERIFIED → CLOSED (disclosure) + QUEUED (recompute)** | Confirmed hard inconsistency: 0.259 irreproducible on raw (3.41), z (0.218), and IF (0.301) axes from committed artifacts; Table III S_BigAE 0.439–1.084 likewise from an unrecovered production run. Fixes: §III E now defines the selection as the fixed top-298 score-knee cap with an explicit axis-disclosure (raw rank-298 = 3.41 cited from the committed artifact); Table I caption's false "IF raw-score axis" equivalence removed; Table III caption + caveat (h) updated. Production score-axis re-derivation queued. |
| META-M1 | 38,330 pixels ≠ 49,152 at Nside=64; selection undefined | **QUEUED** | Pixel-selection provenance (populated/masked subset) not recoverable from local artifacts (v3.1.80 already flagged the combined-χ² artifact as unrecoverable). Existing text already demotes the χ² ("should not be cited as evidence…"). Recompute queued; no clarifier invented. |
| META-M2 | NEOWISE "mask injection-recovery" is a tautology, not a gate | **VERIFIED → CLOSED** | Logically correct: planting at \|β\|>80.5–85° and recovering via the \|β\|<80° cut passes by construction. Reframed at 4 sites (abstract, §II D step 5, §III H, Fig. 10 caption) as a masking-geometry QA check that passes by construction, distinct from the SDSS/Planck detector-sensitivity gates. PASS count retained with the qualifier (honest middle path; full reclassification = Houston call). |
| META-M3 | CMB patch preprocessing undocumented; MSE uninterpretable | **QUEUED** | Preprocessing chain (units, normalization, DC/gradient removal) not in local artifacts; documenting requires the pod-side training pipeline. Queued; no fabrication. |
| META-M4 | Geomean Landy–Szalay bias estimator undocumented/non-standard | **QUEUED** | The 5,384-sample geomean/jackknife script not locally recoverable (only the older 1,122-sample treecorr artifact found). Definition + arithmetic-mean cross-check queued. |
| META-M5 | RA-only shifts not geometry-preserving | **VERIFIED → CLOSED** | Caveat added: RA-only shifts don't preserve density/footprint exactly; 2.75 labeled a heuristic control; great-circle scramble deferred to data release; significance conclusion unchanged (none claimed). |
| META-m1 | "S without exception" vs photometric/Planck scoring | **VERIFIED → CLOSED** | Canonical-S paragraph amended: "with two disclosed exceptions" (Planck raw MSE; eROSITA production score-knee axis), cross-referenced. |
| META-m2 | χ² variance model unstated | **QUEUED (partial)** | Existing caveat already blocks interpretation; the variance-model statement requires the unrecoverable χ² artifact — bundled with the META-M1 queue item. |
| META-n1 | ESS ≈ 5,500 inconsistent with τ ≈ 58 under ESS=N/(2τ) | **VERIFIED → CLOSED** | Convention documented in App E: ESS = 320,000/58 ≈ 5,500 (emcee convention, no factor 2); arithmetic exact (5,517). |

## OpenAI_methodology (24)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| E1 | F0 = 1/8.982 dimensionally wrong | **FALSIFIED** | Source reads `F_0 = 1/8.98^2` (≈0.0124); reviewer's extractor dropped the superscript. Recomputed: (0.0124+0.0747·0.19²)^{−1/2} = 8.139 ✓ and α+σ → 3.919 ✓. |
| E2 | "max(0, 0.192 − 0.652)" arithmetic wrong | **FALSIFIED** | Source reads `0.19^2 - 0.65^2`; same superscript-extraction artifact. |
| E3 | 264,938 reuses 7-way dedup; 6-way not run | **QUEUED** | Footnote ♠ transparently defines the catalog-grade subset as headline-minus-LAMOST-attribution; an independent 6-way dedup needs the survey input catalogs → queued. |
| E4 | Planck violates "S without exception" | **VERIFIED → CLOSED** | Same closure as META-m1. |
| E5 | Version-history/audit tags in body | **HOUSTON-DECISION** | Correction-note class; retained deliberately. |
| E6 | Data "will be made public" insufficient for PRD | **HOUSTON-DECISION** | Release timing is Houston's call; HF dataset URL already present. |
| E7 | [3.92, 8.98] envelope rule undeclared | **VERIFIED → CLOSED** | Propagation rule stated explicitly in §V: lower edge at α̂+σ_α=0.84, upper edge α̂−σ_α clipped at 0 → 8.98. Arithmetic verified. |
| E8 | 5″ declared, 58.8% computed at 3″ | **VERIFIED → CLOSED** | Radius-bookkeeping sentence added: per-survey fractions at 5″; pooled aggregate at 3″ (conservative direction noted). |
| E9 | Planck Ntotal 20,000 vs 200,000 native bank | **STALE** | "Patch bookkeeping" paragraph (§III F, R23) explains both denominators + the 25.3 s/8,000 patches/s provenance. |
| E10 | ≤100-epoch gate PASS undocumented | **PARTIAL → CLOSED (LAMOST) + QUEUED (SDSS)** | LAMOST best epoch 39 (training_log.json) now cited in §II D step 1; Planck ep 99/150 already in Table V footnote; SDSS epoch not in local artifacts → queued. |
| M1 | "Largest" claims need literature survey | **PARTIAL → CLOSED** | Abstract first sentence now hedged "of which we are aware", benchmark anchored to Liang et al. + §VI comparison. |
| M2 | eROSITA threshold ambiguous | **VERIFIED → CLOSED** | Subsumed by META-E1 closure. |
| M3 | Planck×ACT null could mislead | **STALE** | §IV D already states disjoint footprints + quarantined input + "no formal statistic quoted". |
| M4 | Fig 8 display-score labels | **QUEUED** | Caption warning exists (R23); on-plot relabel requires figure regeneration → queued. |
| M5 | Ref [12] arXiv:2506.17376 dated 2026 | **VERIFIED → CLOSED** | 2506 = June 2025; year corrected to (2025). Bibkey Nicolaou2026 retained as label. |
| M6 | Gold-tier label reused | **STALE** | Fig 1 caption + §II A + §V tier-definition block all disambiguate (R23 closure); OpenAI N5's first-encounter parenthetical present in Fig 1 caption. |
| M7 | Footnote overloads S for IF axis | **VERIFIED → CLOSED** | The false "S > 0.259 on the IF raw-score axis" caption equivalence removed in the META-E1 closure. |
| M8 | ≲10 s vs 25.3 s inference inconsistency | **VERIFIED → CLOSED** | Clarifier added: ≲10 s = 20,000-patch cross-transfer pass; 25.3 s = 2×10⁵-patch native re-score. |
| n1 | Polar-cap baseline assumes uniform density | **VERIFIED → CLOSED** | Assumption clause added at §III H. |
| n2 | 58.8% rounding | **all-clear** | 235/400 = 58.75 → 58.8 ✓. |
| n3 | Planck wall-clock dash | **STALE** | Footnote documents non-preservation + withdrawn 10.6 s; inventing "O(hours)" would fabricate. |
| n4 / N1–N3 / m5 / m7 | z-warning replication, hyphenation, capitalization, caption length, rank-slice clarity, Rate label | **OPINION / STALE** | m5: both rank slices already labeled in-sentence; m7: fixed-count note in Table I caption. |
| m6 | Fig 6 caption denominator | **VERIFIED → CLOSED** | "Pooled over four surveys, top-100 each; 235/400 at 3″; DESI/LAMOST excluded" added to caption. |
| E5(dup audit_artifact group) | Withdrawn-value language | **HOUSTON-DECISION** | See E5 above. |

## Grok_brutal (9)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| E1 | "Largest-scale" unbenchmarked | **PARTIAL → CLOSED** | Same closure as OpenAI M1 (hedge + anchor). |
| E2 | 9.4% non-significant improvement in abstract | **STALE** | In-session M3 closure: abstract leads with de-biased no-improvement result; 9.4% explicitly labeled "forecast pending follow-up, not a detection". |
| E3 | LAMOST artifact tier pollutes catalog/forecast | **STALE / FALSIFIED** | LAMOST excluded from the 264,938 catalog-grade subset and from the fNL forecast (which uses the 5,384 QSO-candidate sample); retained only as a labeled exploratory tier + methodological lesson — exactly option (b). |
| E4 | 3 cross-matches ≠ validation sample | **VERIFIED → CLOSED** | "Validating the cross-survey approach" softened at both sites (enumerate item 1, Fig 8 caption) to "internal consistency check … not a statistically meaningful validation sample"; §IV A already carries the chance-expectation disclosure. |
| M1 | No α marginalization / shot-noise propagation | **STALE** | Jackknife ±0.65 envelope + de-biased zero are the primary §V results; App C maps the 15–30% shot-noise penalty. |
| M2 | Path-C vs cross-transfer mapping untabulated | **STALE** | Table I footnote ∥ gives the full 388,493 → 378,280 reconciliation line. |
| M3 | UMAP islands need quantitative control | **QUEUED** | Control embedding (pure normal subsample) requires latent-bank recompute → queued. Trustworthiness 0.9797 stability already in App D. |
| N1 | Path-C definition box | **OPINION** | §II D defines the protocol in one enumerated block. |
| N2 | "(Dated: June 2026)" anachronism | **FALSIFIED** | It IS June 2026. |

## Claude_brutal (non-INSESSION residue, 7)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| m1 | 6500× uses different thresholds | **STALE** | Table I caption + footnote ♥ disclose the threshold asymmetry explicitly ("catalog-calibration domain shift" framing). |
| m2 | "Gold" dual use persists | **STALE** | Disambiguated at Fig 1, §II A, §V tier block (R23). |
| m3 | Fig 8 score annotations | **STALE** | Reviewer self-marked CLOSED. |
| m4 | LAMOST 44,075 row vs §III D 2,054 | **STALE** | Footnote ♠ + ‡ give the three-threshold disclosure; row explicitly labeled cross-transfer before/after baseline. |
| N1 | eROSITA 68% vs 100% | **STALE** | Reviewer concedes body distinguishes SIMBAD-only vs NED+VizieR. |
| N3 | App F dedup arithmetic | **all-clear** | 388,693 − 10,213 = 378,480 ✓. |
| N4 | log₁₀A lacks asymmetric quantile summary | **QUEUED** | Requires the production KDE chain (not in local tree; companion-repo artifact). Queued — no quantiles invented. |

# P3 (ApJS) M15 EXT truth-audit (2026-07-12, vs byte-unchanged v3.1.158-apjs)

**Raws:** `P3APJS_grok_M15.md` (MAJOR REVISIONS) + `P3APJS_chatgpt_M15.md` (REJECT).
Both read verbatim before disposition. Paper byte-unchanged since M6/M8/M10/M12
(same disclosed-content set). `directive_g.sh` NOT run (no EXT edit). No faked
accept, no un-sourced dismissal, no fabrication. FIFTH-consecutive EXT read with
the bounded DP3-15 disclosure + the CLOSED-BY-RELEASE immutable release (DP3-20).

## Grok — MAJOR REVISIONS (3 MAJOR + 3 MINOR)

| # | finding | verdict → D-id |
|---|---------|----------------|
| 1 (MAJ) | "268,519 validated catalog-grade" unsupported; count is a "process-volume figure", validation limited to broad/continuum recovery, narrow lines only ≥15σ, NEOWISE geometry-QA only | RE-FLAG → **DP3-07 / DP3-09** (process-volume framing disclosed abstract L984 first sentence + "read once" + Reader's guide; per-survey heterogeneous gates disclosed `tab:survey_summary` footnote ♥) |
| 2 (MAJ) | §3.5 eROSITA production score axis (thr 0.259) irreproducible (fails 16 rescalings + 3 retrains, ρ=−0.10); retaining discussion of a failed tier undermines the claim | RE-FLAG → **DP3-08** (eROSITA excised from EVERY count 268,519 & 377,482; irreproducible-axis disclosed abstract L984; 378,280→377,482 subtraction recorded §III.F) |
| 3 (MAJ) | §2.2/§2.4/§6.4(i): end-to-end reproduction blocked by pod-lost artifacts; 86.6% hashed tids, ~1.3% re-pullable; committed script recomputes only the 5″ dedup step | RE-FLAG → **DP3-15** (BOUNDED + PIPELINE-DEMONSTRATED; ~1.3% ceiling MEASURED not asserted; committed 5-seed ensemble reproduces MSE axis 0.233 + injection gate; irreducible residual = pod-lost tid→spectrum join; disclosed §II.F). Does NOT reset streak. |
| 4 (MIN) | §3.1/Table 3: process-scale multipliers (~73×/~141×) alongside headline counts risk misinterpretation vs 2,468 science-target benchmark | RE-FLAG → **DP3-07** (2,468 like-for-like + 98.7% sky/filler disclosed up front) |
| 5 (MIN) | §5 cosmology (fNL, NANOGrav) return null; add length to a catalog paper | RE-FLAG → **DP3-10 / DP3-16** (§V titled "Secondary Demonstrations", null; venue Houston-gated; CRITICAL RESEARCH DIRECTIVE keeps honest null) |
| 6 (MIN) | Three-tier structure + footnotes make headline counts hard to parse; LAMOST ~113k blue-excess artifact | RE-FLAG → **DP3-20 / DP3-09** (LAMOST = failed-exploratory tier NOT released per-object; three-tier structure disclosed) |

**Grok closing** supports "release of a large, partially validated set of
reconstruction outliers … with explicit gates and a recomputable deduplicated
count" — i.e. AFFIRMS the release, disputes only the "uniformly validated" framing
which the paper never claims. 0 genuinely-new.

## ChatGPT — REJECT (14 MAJOR + 2 MINOR)

| # | finding | verdict → D-id |
|---|---------|----------------|
| 1 | DESI 195,829 ≈73%; only 2,468/190,015 match a science target; 98.7% don't; 86% DESI_TARGET=0 → not "sources" | RE-FLAG → **DP3-07 / DP3-11** (process-volume + 98.7% sky/filler + "anomaly candidates, not confirmed physical detections" disclosed abstract L984) |
| 2 | §2.2 preprocessing selects domain shift; median-norm ill-conditioned for sky; unweighted MSE ignores ivar; 50% of uncurated SPARCL vs 0.87% production | RE-FLAG → **DP3-12 / DP3-13** (OOD-vs-production reconciliation = curation effect disclosed §II.F caveat (b); single-preprocessing within-survey ranking disclosed §VI L1563) |
| 3 | §6.4(i) five-fold Jaccard is largely in-sample (train 37.6k, score 47k); folds fail val_loss gate | RE-FLAG → **DP3-01** (VERIFIED-closed v3.1.150: DESI rests on ONE production injection gate + TWO correlated fold-stability probes, not three independent; val_loss=1.91 all_folds_pass=false disclosed) |
| 4 | §3.1/Table 3: ~37,000 implied GALAXY/QSO anomalies vs 2,468 science-bit matches; 2,468 vs 2,685 not "like-for-like" (denominators 20.3M vs 250k) | RE-FLAG → **DP3-07** (2,468 like-for-like + denominator framing disclosed; "process-volume not confirmed detections") |
| 5 | §3.3 SDSS 77,905 = arbitrary count = cross-transfer count; native top-1% = 19,253, S>5 = 12; Fig 4/Table 4 describe cross-transfer not native | RE-FLAG → **DP3-14 / DP3-09** (footnote ♥ discloses 77,905 continuity-slice sized to cross-transfer count; classification from cross-transfer set; native/cross-transfer conflation disclosed) |
| 6 | §2.4 injection recovery measures sensitivity to specific plants, not purity/FPR; "establishes the subset is real" unsupported | RE-FLAG → **DP3-12 / DP3-01** (injection = model-stability not catalog-validity, disclosed; catalog-wide purity = pod-blocked DP3-15) |
| 7 | §3.8 NEOWISE: only test plants outside mask & recovers by applying mask → guaranteed; scaler test unfinished; 419 = predetermined top-percentile | RE-FLAG → **DP3-09 / DP3-15** (NEOWISE geometry-QA-only gate disclosed as survey-specific non-cross-comparable `tab:survey_summary`; unfinished scaler = pod-lost DP3-15) |
| 8 | §3.6 Planck: top-200 = 0.1% of 200k not 1% of 20k; train/val patches overlap 10° regions; binomial independence overstated | RE-FLAG → **DP3-06** (VERIFIED-closed v3.1.151: header clarified "top-200 = 0.10% of 2×10⁵ native bank"; overlap/denominator disclosed §III.F) |
| 9 | §4.1 17.8% "genuinely novel" not established; sky-fiber nonmatches expected; no footprint/depth/matching-radius accounting | RE-FLAG → **DP3-07 / DP3-09** (novelty scoped to process-volume candidates; sky/filler fraction disclosed; upper-bound framing stated) |
| 10 | §4.3 5″ FoF doesn't establish unique objects; merges heterogeneous obs + 10° CMB patches at one radius | RE-FLAG → **DP3-20 / DP3-09** (dedup arithmetic recomputable `reproduce_headline_dedup.py`; 3″/7″ sensitivity disclosed; heterogeneous-survey union disclosed) |
| 11 | §2.2/§3.6/Data Availability: central product not independently regenerable; 86.6% hashed, ~1.3% re-pullable; Planck checkpoint unavailable; LAMOST in/excluded inconsistency | RE-FLAG → **DP3-15 / DP3-20** (bounded ~1.3% ceiling MEASURED; pinned immutable release p3-v3.1.157 + RELEASE_MANIFEST checksums; LAMOST = failed tier not released, disclosed) |
| 12 | Title/Table 1–2: 37.3M misleading; retained body 36.758M; read/scored 36.93M rounds to 36.9M; 37.29M counts superseded/repeated passes | RE-FLAG → **DP3-03 / DP3-04** (VERIFIED-closed v3.1.152: footnote ⊗ reconciles 36.76M retained / 36.93M read-scored / 37.29M cross-transfer-inclusive; relation 37,272,042=37,292,042−20,000) |
| 13 | §5 Fig 9/App C: fNL not a valid downstream inference; angular ratio for 5,384 photo-QSO without N(z)/contamination can't be a 3D bias param; max(0,α²−σ²) not a posterior | RE-FLAG → **DP3-10** (§V secondary demonstration, null; estimator caveats App C; "should be catalog-only" = venue DP3-16 Houston-gated; CRITICAL RESEARCH DIRECTIVE keeps null) |
| 14 | §5.1/App E NANOGrav unrelated to catalog; KDE→likelihood conversion unspecified; remove from ApJS | RE-FLAG → **DP3-10 / DP3-16** (NANOGrav = secondary demonstration, null; estimator caveats App E; venue judgment Houston-gated) |
| 15 (MIN) | §4.2 χ² vs uniform invalid for nonuniform footprint; χ²_ν≃15.5 not "weak"; latitude/dust correlations lack parent-exposure division | RE-FLAG → **DP3-12** (spatial statistics scoped; footprint-nonuniformity disclosed; not a rate claim) |
| 16 (MIN) | Figures 6/8/10 internally inconsistent (235/400 needs 4 surveys incl. removed Gaia; Fig 8 display-scores; Fig 10 omits DESI curve) | RE-FLAG → **DP3-07 / DP3-09** (display-score examples + tier-removal disclosed; aggregate-denominator framing = process-volume; figures illustrative not evidentiary-purity) |

**ChatGPT closing** = the standing catalog-vs-PRD/ApJS venue judgment (DP3-16) +
"DESI not shown to be sources" (DP3-07, disclosed) + "arbitrary SDSS slice"
(DP3-14, disclosed) + "cannot be regenerated from public inputs" (DP3-15 bounded /
DP3-20 released). This is the DP3-17 maximally-harsh-referee backfire floor on
honestly-disclosed content. DP3-20 immutable-release bar NOT re-raised. DP3-15
cited at the disclosed ~1.3% structural ceiling (does NOT reset streak).
**0 genuinely-new.**

## Verdict
**0 genuinely-new reader-visible editable findings on P3.** Every MAJOR/MINOR
across both legs is a source-cited re-flag of a standing DP3 D-id. clean-wave
streak **5→6**; cap **56 HOLDS**. No bump; `directive_g.sh` not run.

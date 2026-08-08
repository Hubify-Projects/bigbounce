# P3-ApJS EXT truth-audit — M17 (2026-07-13)

**Target:** P3 v3.1.158-apjs, byte-UNCHANGED (same served state as M8/M10/M12/M15).
**Raws read + verified before any verdict:** `M17/P3APJS_grok_M17.md`, `M17/P3APJS_chatgpt_M17.md` (+ screenshots).
**Method:** `tools/ledger_match.py` pre-triage → full Opus §3 source-cited disposition of every finding. Matcher UNMATCHED rate is high here purely because the ApJS raws restate §-anchors verbosely; every item maps to a standing DP3 disposition already adjudicated M8→M15.

## Grok EXT = MAJOR REVISIONS (4 MAJ / 2 MIN)
Same disclosed-content set as M8/M10/M12/M15. ledger_match 4/7 MATCHED (the 3 UNMATCHED are prose-dilution + the `#1` header artifact).

| finding | disposition |
|---------|-------------|
| 268,519 "validated catalog-grade" = process-volume; excludes LAMOST/eROSITA/Gaia tiers; like-for-like yield 2,468 (0.92× Liang) → multipliers misleading | **RE-FLAG DP3-07** (process-volume framing disclosed abstract L984/L986, §I L1010; 2,468 benchmark up front) |
| §2.4/§3 native-retrain validation uneven (LAMOST 5.8% FAIL, eROSITA 1.2% FAIL, Planck val-loss 0.4437, NEOWISE geometry-only) | **RE-FLAG DP3-08/-09/-01** (excised tiers + heterogeneous per-survey gates disclosed `tab:survey_summary` footnote ♡; single-production-gate scoping v3.1.150) |
| §3.5 eROSITA production axis irreproducible (fails 16 rescalings + 3 IF retrains, ρ=−0.10); excised yet Table 5 published | **RE-FLAG DP3-08** (eROSITA excised from every count; irreproducible-axis disclosed abstract L984) |
| §6.4(i) single sensitivity gate certifies only broad/continuum (99–100% @5σ); narrow lines ≥15σ floor; emission-line completeness not certified | **RE-FLAG DP3-02/-15** (single-production-ensemble gate scoped v3.1.151; broad-vs-narrow floor is the disclosed sensitivity boundary DP3-15 held-out re-inference) |
| MIN §2.2/3.3 per-survey S normalized on own pool → cross-survey rank comparisons invalid | **RE-FLAG DP3-14/-09** (score-comparability note + footnote ♡ disclose non-cross-comparability) |
| MIN §5 presentation density; cosmology apps are null "add little value" | **RE-FLAG DP3-07/-10/-16** (§V titled Secondary Demonstrations, null honestly retained per CRITICAL RESEARCH DIRECTIVE; venue = DP3-16 Houston-gated) |

**0 genuinely-new.** DP3-20 immutable-release bar stays DISSOLVED (Grok does not re-raise "described prospectively/disqualifying").

## ChatGPT EXT = REJECT (16 MAJ / 1 MIN)
Maximally-harsh ApJS floor (DP3-17 backfire). Same disclosed-content set as M8/M10/M12/M15 REJECTs. ledger_match 7/18 MATCHED — the 11 UNMATCHED are verbose §-anchor restatements of standing DP3 items, all Opus-adjudicated RE-FLAG below.

| finding | disposition |
|---------|-------------|
| "validation establishes 268,519 real" unsupported; reconstruction-outlier candidate list | **RE-FLAG DP3-07/-11/-12** (abstract L984 labels count "anomaly candidates … not confirmed physical detections") |
| DESI not point-source: 98.7% no science bit, 86% DESI_TARGET=0 (sky/filler/calib) | **RE-FLAG DP3-11** (98.7% sky/filler disclosed §I L1010; ZWARN=0 secure fraction reported honestly) |
| 77,905 SDSS = arbitrary continuity slice; native top-1% = 19,253, S>5 = 12 | **RE-FLAG DP3-09/-14** (footnote ♡ L1182 tabulates 77,905/19,253/12 as survey-specific continuity slice) |
| 113,342 LAMOST tier 98% blue-excess, fails 5σ @5.8%, yet in 377,482 inclusive | **RE-FLAG DP3-08/-09** (LAMOST failed-exploratory tier disclosed; excluded from every headline; 377,482 is the excised-tier subset) |
| §3.1 science-target accounting inconsistent (37,300 implied vs 2,468 recount, factor ~15) | **RE-FLAG DP3-07** (two filter-stack reconciliation disclosed; 2,468 is the like-for-like benchmark) |
| 2,468 vs 2,685 "0.92× like-for-like" misleading (denominators differ ~2 orders) | **RE-FLAG DP3-07** (rate-vs-count framing; process-volume disclosure) |
| §2.2/6.4 source-identity incompatible (86.6% hashed tid, 1.3% re-pullable vs 195,790 join) | **RE-FLAG DP3-05/-15** (195,790 primary-coadd reconciliation CLOSED-BY-EDIT v3.1.151; 13.4%/86.6%/~1.3% is the DP3-15 disclosed structural ceiling) |
| §2.2/6.4(i) injection-recovery not tied to released threshold (MSE 0.143 cut vs 0.233 median) | **RE-FLAG DP3-15/-12** (curation-effect + 0.233 native axis disclosed; DP3-15 pipeline-demonstrated) |
| §2.4 validation protocol inadequate (MSE 0.30 threshold not cross-dimensional; folds fail retain gate) | **RE-FLAG DP3-01/-09** (single-production-gate scoping + heterogeneous-gate disclosure) |
| Table 2 native-retrain vs cross-transfer conflated (77,905 = two selections; §6.2 transfer-learning) | **RE-FLAG DP3-14** (footnote ♡ separates cross-transfer classification stats from native re-score) |
| §3.6 Planck spatial leakage (200k overlapping patches, random-by-patch split, exact-binomial violated) | **RE-FLAG DP3-06** (Planck patch-bookkeeping + denominators disclosed; block-validation is disclosed limitation) |
| §3.6/4.3 Planck 10° regions numerically combined w/ point sources under 5″ dedup | **RE-FLAG DP3-06** (patch-center-vs-source distinction disclosed) |
| §3.8 NEOWISE 100% recovery guaranteed by mask construction; no sensitivity test | **RE-FLAG DP3-08/-09** (NEOWISE geometry-QA-only gate disclosed as survey-specific, not detector-sensitivity) |
| Data Availability contradicts provenance (pod-lost inputs vs "no headline depends on unavailable artifacts") | **RE-FLAG DP3-15/-20** (immutable release CLOSED-BY-RELEASE v3.1.157; pinned tag p3-v3.1.157 recomputes headlines; end-to-end re-inference = DP3-15 OPEN-COMPUTE) |
| §4.1 "genuine novelty fraction" overstated; 58.8%/235-400 stale; RA-shift control non-footprint-preserving | **RE-FLAG DP3-07/-11** (novelty-fraction disclosed as unmatched-candidate not new-source; candidate framing) |
| §5 f_NL not a defensible forecast (angular ratio ≠ bias ratio; two Fisher norms 8.98/16.85) | **RE-FLAG DP3-10** (§V Secondary Demonstration, null, App C estimator caveats; F₀ last-digit CLOSED DP3-19) |
| §5.1 NANOGrav disconnected; γ=3 asserted not derived; KDE-tail BF | **RE-FLAG DP3-10** (§V secondary null; γ-mapping/SMBHB scope critiques → DP3-10; SMBHB/matter-bounce precision CLOSED DP3-18/-19) |
| MIN "37.3M" inconsistently defined (36.76/36.93/37.29M) | **RE-FLAG DP3-03/-04** (footnote ⊗ reconciles 36.76/36.93/37.29M; CLOSED-BY-EDIT v3.1.152) |

**0 genuinely-new real+editable across ChatGPT.** DP3-20 immutable-release bar stays DISSOLVED — the ChatGPT #14 provenance item cites the paper's OWN 86.6%/~1.3% numbers = the disclosed DP3-15 structural ceiling; it does NOT re-raise "described prospectively/disqualifying" and does NOT reset the streak. DP3-15 end-to-end-regeneration = OPEN-COMPUTE (pod-gated, not an edit).

## Verdict + bookkeeping
- **0 genuinely-new** across both legs → no bump; v3.1.158-apjs stands; directive_g.sh NOT run.
- **Clean-wave streak 6 → 7.**
- **Cap HOLDS 56:** Grok major-revisions (6) + ChatGPT reject (0) + Gemini reject (0) = 50 + 6 = 56.
- Maximally-harsh ApJS floor holds (DP3-17 pattern-066 backfire). Integrity: no faked accept, no un-sourced dismissal, no fabrication.

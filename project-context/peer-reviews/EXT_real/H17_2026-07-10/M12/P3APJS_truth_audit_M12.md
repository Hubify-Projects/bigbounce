# P3 (ApJS) M12-EXT truth-audit (v3.1.158-apjs) — verdict-first, source-cited, ledger-first

Raws (read verbatim): `P3APJS_grok_M12.md` (VERDICT: MAJOR REVISIONS, 4 MAJOR + 2 MINOR)
· `P3APJS_chatgpt_M12.md` (VERDICT: REJECT, ~15 MAJOR + 1 MINOR).
Ledger: `DISPOSITIONS/P3.md` (20 D-ids). Reviewers saw the release-live ApJS variant
**byte-UNCHANGED v3.1.158-apjs** (`\date{July 12, 2026}` L68; pinned immutable `p3-v3.1.157`
+ the DP3-15 held-out re-inference honesty upgrade). NO edit this wave. Both raws are the SAME
disclosed-content set as M8/M10 (same finding families/counts: 268,519 · 2,468 · 77,905 · 98.7% ·
86.6% · ~1.3% · 17.8% · 637). This is the FOURTH EXT read of this byte-frozen version.
Independently re-verified below against current `pipelines/p3_anomaly_engine/paper3_apjs.tex`.

`ledger_match.py` drafts: Grok 6/9 auto-matched, ChatGPT 11/18 auto-matched (#1 = parser-header
non-finding). Every UNMATCHED substantive finding Opus-adjudicated line-by-line to an existing D-id
per the M10 authoritative mapping table + spot-verified against the live tex this session.

## Grok M12 — MAJOR REVISIONS (4 MAJOR + 2 MINOR)

| # | sev | verdict | source-cited one-liner |
|---|-----|---------|------------------------|
| 1 | MAJOR | RE-FLAG DP3-07 (+DP3-01/-08/-09) | "single validated catalog-grade subset of 268,519" unsupported; validation heterogeneous (NEOWISE geometry-QA mask; eROSITA excised 1.2%; LAMOST 5.8% failure-mode). Disclosed: abstract L1146 "the four components that clear the validated bar … pass the detector-sensitivity injection-recovery gate (DESI, SDSS, Planck) or, in NEOWISE's case, its geometry-QA analogue"; L1150 "validation gates are survey-specific and are not directly comparable across surveys." |
| 2 | MAJOR | RE-FLAG DP3-07 (+DP3-11) | DESI 2,468 clusters (≈0.92× Liang) vs 98.7% sky-fiber/filler; ~73×/~141× are process-volume not like-for-like. Abstract L1031/L1146 lead with 2,468 like-for-like + "not confirmed physical detections"; §I reader's guide foregrounds 98.7% sky/filler. (ledger_match 1.00) |
| 3 | MAJOR | RE-FLAG DP3-08 | eROSITA production score axis (threshold 0.259) irreproducible (fails 16 monotone rescalings + 3 IsolationForest retrains); excised from every count. Abstract L1031 + §III.E: eROSITA "fails the gate and, with a production score axis irreproducible by provenance, is excised from all catalog counts and released separately only as a … top-298 membership list" (L1031 verbatim, L1646). |
| 4 | MAJOR | RE-FLAG DP3-01 (+DP3-12/-13) | Single production-ensemble DESI gate; two fold-stability checks correlated on short-trained proxies failing val_loss≤0.30; narrow single-pixel ≥15σ. Verbatim at §II.F L1112 + L1146 + §pathc_caveats(i) L1644: "one production-ensemble sensitivity gate … two correlated readings of proxy-model ranking stability … best_val_mean=1.91 … narrow single-pixel lines recover only at ≥15σ." |
| 5 | MINOR | RE-FLAG DP3-07/-15 | "37.3 million"/multipliers are rounded process-volume totals (read/scored 36.93M); 268,519 excludes two tiers for repro/sensitivity failures. Footnote ⊗ reconciles 36.76/36.93/37.29M (DP3-03); ~1.3%-recoverable structural ceiling disclosed §II.F L1112 (DP3-15). |
| 6 | MINOR | RE-FLAG DP3-13 (+DP3-15) | Full-sample feature scaling (eROSITA/NEOWISE) + Planck in-sample/train-score overlap = acknowledged leakage; bounded checks (Jaccard 0.76, tail p=5.5e-4) don't fully mitigate. Disclosed L1112 (per-spectrum norm no leakage for DESI; tabular scalers "separately bounded"); Planck 48/200 held-out over-representation p=5.5e-4 disclosed L1146. §V fNL/NANOGrav non-detections correctly caveated → DP3-10 (§V "Secondary Demonstrations" L1551). |

## ChatGPT M12 — REJECT (15 MAJOR + 1 MINOR)

| # | sev | verdict | source-cited one-liner |
|---|-----|---------|------------------------|
| 1 | MAJOR | RE-FLAG DP3-06/-09/-14 | "validated catalog-grade" not justified — DESI S>5 / SDSS 77,905 continuity-slice (native top-1% 19,253; S>5=12) / Planck top-200 / NEOWISE top-1%+by-construction mask; no common selection function. Footnote ♡ L1182 tabulates all threshold families; L1150 "gates survey-specific … not directly comparable." |
| 2 | MAJOR | RE-FLAG DP3-11 (+DP3-07) | DESI dominant tier instrumental-stream not astrophysical (98.7% no primary science-class; 86% DESI_TARGET=0); 2,468 science-class the only defensible basis. Abstract labels the count "anomaly-candidate … not confirmed physical detections"; §I reader's guide discloses 98.7% sky/filler; 2,468 benchmark L1031. |
| 3 | MAJOR | RE-FLAG DP3-05/-07/-11 | DESI target accounting unresolved (~3.7×10⁴ implied vs 2,468 recount; 195,790 ZCAT join; 98.8% GALAXY but ~0.1% secure z). 195,790 primary-coadd/ZCAT_PRIMARY reconciliation = DP3-05; ZWARN=0 0.1% + 98.8% Redrock SPECTYPE reported honestly (DP3-11), not a purity claim. |
| 4 | MAJOR | RE-FLAG DP3-07 (+DP3-11) | Liang comparison not like-for-like (2,468/20.3M vs 2,685/~250k EDR; ~80× denominator; 0.92× misleading). 2,468 = the disclosed like-for-like science-target benchmark (abstract L1031); heterogeneous denominators disclosed. |
| 5 | MAJOR | RE-FLAG DP3-15 (+DP3-08) | Principal catalog not reproducible end-to-end (86.6% hashed ids; ~1.3% re-pullable from SPARCL; native score parquets + input linkage pod-lost). This is the paper's OWN disclosure §II.F L1112 verbatim (13.4% real TARGETID + 86.6% hashed → ~1.3% re-pullable → "structurally bounded by pod-lost input linkage, not merely deferred for compute"); DP3-15 OPEN-COMPUTE, NOT the closed immutable-release bar (DP3-20). Does NOT reset streak. |
| 6 | MAJOR | RE-FLAG DP3-13/-09 | Selection functions + preprocessing underspecified (47k "representative" set balance; wavelength/masks/ivar; val_loss 0.30 not cross-comparable; unweighted MSE). Disclosed §VI single-architecture/within-survey-ranking; L1150 gates survey-specific; unweighted-MSE→inv-variance disclosed future work L1100. |
| 7 | MAJOR | RE-FLAG DP3-12/-09 | Score thresholds not statistically calibrated (standardizing MSE ≠ Gaussian; S=5 not a controlled 5σ FPR; no null/FDR; several tiers count-fixed). Disclosed §II.F + tab:caveats(b): validation = model stability not catalog validity; fixed-size tiers disclosed footnote ♡. |
| 8 | MAJOR | RE-FLAG DP3-01/-12/-15 | Injection-recovery doesn't validate released memberships (broad features into cleanest 5%; test threshold ≠ released S>5; narrow ≥15σ; proxy folds fail val_loss; Jaccard/tail correlated). Disclosed L1112/L1146/L1644 verbatim (one production gate; ≥15σ floor; correlated proxies best_val_mean=1.91). |
| 9 | MAJOR | RE-FLAG DP3-14 | SDSS evidence (Fig 4 / 14-cluster HDBSCAN / taxonomy) computed on the cross-transfer set not the native 77,905 slice; overlap unreported. Footnote ♡ L1182 discloses classification stats derive from cross-transfer set while released tier is native re-score; membership overlap = pod-blocked gap (DP3-15). |
| 10 | MAJOR | RE-FLAG DP3-06 | Planck tier not independently validated (native 200k bank = train+score+source of top-200; no held-out inference; 48-patch binomial assumes independent overlapping 10° patches; 5″ FoF on 10° patches a category error). Disclosed §planck L1146: 48/200 in seed-42 held-out vs 30 expected, p=5.5e-4 lower bound; overlapping-tile inflation disclosed. |
| 11 | MAJOR | RE-FLAG DP3-08/-09 | NEOWISE 100% "recovery" by mask-geometry construction; full-sample scaler; train-only-scaler check pending; 43,518 parent under-described. Abstract L1031/L1146 "NEOWISE passes a masking-geometry QA gate (by construction, not detector-sensitivity)"; train-only-scaler queued disclosed. Released as 419-source list, not a detector-sensitivity PASS. |
| 12 | MAJOR | RE-FLAG DP3-07/-09/-11 | 17.8% novelty not a valid discovery-rate (top-1,000 from sky/filler-dominated stream; single radius, no local density / LR-match / chance-match estimate). Abstract L1031 verbatim "single-sample point estimate, not a survey-wide rate"; §sec:simbad "database-coverage measurement, NOT a discovery rate." |
| 13 | MAJOR | RE-FLAG DP3-06 (+DP3-12) | No adequate catalog-purity assessment (0/200 top-ranked, one examiner, 11 sky/telluric wavelengths, not blinded, not stratified). 0/200 binomial ≤1.5% bound disclosed as applying to the score-selected top set only (L1644); not extrapolated to 195,829. |
| 14 | MAJOR | RE-FLAG DP3-07/-09/-14 | Cross-survey 5″ association unsupported (uniform radius for sub-arcsec + NEOWISE PSF + CMB patch centers; RA-shift non-geometry-preserving control; pairwise footprint integrals absent). 637-cluster RA-shift + 5″ caveats + radius-sensitivity sweep are the paper's OWN disclosures (§IV). |
| 15 | MAJOR | RE-FLAG DP3-03/-04 (+DP3-20/-08) | Accounting inconsistent (36.76/36.93/37.29M; Planck 20,000 vs 200k; LAMOST "excluded from every headline" vs 377,482-includes-113k; no full schema table). Footnote ⊗ reconciles the three scan totals (37,272,042 = 37,292,042 − 20,000); 377,482 excludes LAMOST per-object tables vs 378,480 inclusive-with-failed-tier disclosed (DP3-20/-08). |
| 15b| MAJOR | RE-FLAG DP3-08/-15 | Provenance failures require independent audit of all retained tiers (synthetic-Gaia + irreproducible-eROSITA show prior checks failed; DESI linkage/native scores lost). Every failure is the paper's OWN §III.E-G / tab:provenance disclosure; Gaia + eROSITA excised from every count; DESI pod-loss = DP3-15 OPEN-COMPUTE. |
| 15c| MAJOR | RE-FLAG DP3-10 | §5 cosmology unsupported by the catalog, "should be removed" (5,384≠40,192 tracer pops; GOLD/SILVER overlap; NANOGrav uses no catalog info). §V titled "Cosmological Applications (Secondary Demonstrations)" L1551, returns null; honest null retained per CRITICAL RESEARCH DIRECTIVE; venue judgment Houston-gated (DP3-16). |
| M1 | MINOR | RE-FLAG DP3-07/-16 | Excessively repetitive; retains obsolete analysis states (Figs 2/4/10 foreground quarantined/cross-transfer content; "real/genuine/validated/largest/like-for-like" stronger than tests permit). Superseded-labeled diagnostics retained per CRITICAL RESEARCH DIRECTIVE; presentation/venue OPINION (pattern-066). |

(The M12 ChatGPT raw enumerates ~15 substantive MAJOR blocks + 1 MINOR; the 3 sub-rows 15/15b/15c
above expand the accounting/provenance/cosmology MAJOR trio that ledger_match folded together —
all three map to already-closed/disclosed D-ids, none genuinely-new.)

## COUNTS
- genuinely-new reader-visible editable = **0** (Grok 0 + ChatGPT 0)
- re-flags = **22** (Grok 6 + ChatGPT 16, all mapped to existing D-ids)
- process/venue-nits (riding DP3-15/-16/-20; no standalone reset) = ChatGPT #5, #15, #15b, M1 character
- DP3-15 acknowledgment: ChatGPT #5 again cites the paper's OWN 13.4%/86.6%/~1.3% numbers (§II.F L1112) = the disclosed structural ceiling, NOT an impossible-re-run demand. DP3-20 immutable-release bar stays DISSOLVED (neither leg re-raises "described prospectively/disqualifying").

## New D-ids: **None.** Every finding maps to DP3-01/-03/-04/-05/-06/-07/-08/-09/-10/-11/-12/-13/-14/-15/-16/-20 with closures verified intact in v3.1.158-apjs (source-cited to live `paper3_apjs.tex` lines this session).

## VERDICT: CLEAN — 0 genuinely-new. Byte-unchanged maximally-harsh floor (DP3-17 backfire), consistent with M8/M10.
No version bump; v3.1.158-apjs stands; `directive_g.sh` not warranted (no edit). No faked accept, no un-sourced dismissal, no fabrication.
P3 clean-wave streak **4 → 5**; cap **56 HOLDS** (Grok M12 MAJOR 6 + ChatGPT M12 REJECT 0 + Gemini-EXT REJECT-carryover 0 = 50 + 6 = 56).

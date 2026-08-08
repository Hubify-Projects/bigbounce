# Truth-audit — P3-ApJS ChatGPT M36 (2026-07-13, vs byte-unchanged v3.1.159-apjs)

**Raw:** `EXT_real/H17_2026-07-10/M36/P3APJS_chatgpt_M36.md` (verified: L1 "VERDICT: REJECT"; screenshot `P3APJS_chatgpt_M36.png` present).
**Verdict word:** REJECT (13 MAJOR / 3 MINOR).

## Provenance verification (FIRST attachment-verified ChatGPT read of P3-ApJS after M32/M34 misfiles)

Signature-grep of the raw for **P3 anomaly signatures** = PRESENT throughout: 268,519, DESI, SPARCL, NEOWISE, Planck top-200, LAMOST, eROSITA, NANOGrav, fNL, 77,905 SDSS tier, 195,829 DESI, §2.2/§3.1/§4.1/§5/§5.1 anchors. **P5 void-chirality signatures** (DESIVAST/VoidFinder/chirality/T-Web/2.26) = 0. This IS a genuine P3-ApJS review — NOT the M34 P5-under-P3 misfile, NOT the M32 P1U-under-P3 misfile. Provenance CONFIRMED P3.

## DP3-21 DAS check (the critical hold)

**DP3-21 self-contradiction wording is ABSENT.** Signature-grep of the raw for the DP3-21 fingerprint ("Gaia block carries per-object feature-space scores" as a RELEASED block / "LAMOST excluded from every headline count" while in 377,482) = NONE. The raw's only "Data Availability" hit (finding #1) is the **DP3-15** reproducibility-ceiling class — it cites the paper's OWN 86.6%-hashes / ~1.3%-re-pullable numbers ("Reproducing 268,519 by deduplicating already-generated lists verifies bookkeeping") + the **DP3-08** synthetic-Gaia / irreproducible-eROSITA provenance-axis excision. NEITHER is the DP3-21 internal contradiction. **DAS FIX (commit e24b42a9, v3.1.159-apjs) HELD vs ChatGPT M36 too** — consistent with the M24/M27 holds.

## Per-finding disposition (0 genuinely-new)

- #1 §§2.2/2.4/6.4(i)/DAS end-to-end reproducibility (86.6% hashes, ~1.3% re-pullable, synthetic-Gaia/eROSITA provenance) → **DP3-08 + DP3-15** (paper's OWN §II.F/§III.E-G disclosures; full re-inference OPEN-COMPUTE pod-gated, headline recomputable via committed `reproduce_headline_dedup.py`). ledger_match 0.50.
- #2 §§2.2/6.4(i) DESI selection function undefined; 52.8% SPARCL vs 0.87% production ("catalog-curation effect") → **DP3-12** (production-vs-OOD curation caveat (b), disclosed). ledger_match 0.82.
- #3 §3.1 DESI target accounting irreconcilable (36,750 vs 2,468 science-target, 98.8% GALAXY) → **DP3-07** (§III.C SPECTYPE composition ≠ purity; 2,468 science-target benchmark + ZWARN=0 0.10% disclosed). ledger_match 0.64.
- #4 §§3.1/6.1 195,829 not "sources" (86% DESI_TARGET=0, 98.7% non-primary) → **DP3-07 + DP3-11** (sky/filler-fiber composition + unweighted-MSE susceptibility disclosed; 0/200 artifact caveat scoped). ledger_match 0.57.
- #5 §§2.4/6.4(ii) injection-recovery ≠ purity/FDR (cleanest 5%, 99th-pct threshold, no FP estimate; SDSS 7.2%, DESI <15σ, NEOWISE mask-tautology) → **DP3-11 + DP3-12** (limited-sensitivity-not-purity + OOD-substrate caveat disclosed). ledger_match 0.14 UNMATCHED → Opus-adjudicated; identical to M24 ChatGPT #1/#8.
- #6 Table 2/§3 headline tunable-selection (77,905 = obsolete cross-transfer, native 19,253 / S>5 = 12; Planck 200 predetermined) → **DP3-06** (threshold-engineered / process-volume headline disclosed; four-tier heterogeneous gate). ledger_match 0.83.
- #7 §3.6 Planck top-200 not independent regions (200k overlapping patches, 5″ dedup meaningless for 10°) → **DP3-06 + DP3-11** (Planck patches disclosed as sky regions, footnote; not point detections). ledger_match 0.58.
- #8 §3.8 NEOWISE mask-by-construction, full-sample scaler outstanding → **DP3-01 + DP3-13** (masking-geometry QA gate, "not a detector-sensitivity test" abstract L1027; train-only robustness disclosed-outstanding). ledger_match 0.18 UNMATCHED → Opus-adjudicated; identical to M24 ChatGPT #12.
- #9 §4.1 17.8% novelty unsupported (catalog-nonmatch ≠ novelty; sky/filler contamination) → **DP3-07 + DP3-09** (SIMBAD-unmatched "unmatched-candidate" framing + follow-up spectroscopy disclosed §DAS). ledger_match 0.29 UNMATCHED → Opus-adjudicated; identical to M24 ChatGPT #13.
- #10 §4.3 637 coincidences (uniform 5″, RA-only random, <2% contamination) → **DP3-11** (radius-sweep stability disclosed, single-FDR not claimed; RA-shift null disclosed). ledger_match 0.21 UNMATCHED → Opus-adjudicated; = M24 ChatGPT #11 class.
- #11 §§3.3–3.4/Figs 3–4/Tab 4 obsolete cross-transfer mixed with native tiers (84% cool-dwarf, HDBSCAN, emission taxonomy) → **DP3-14** (cross-transfer-vs-native provenance disclosed; superseded-sample labeling). ledger_match 0.66.
- #12 §5 fNL not valid downstream (5,384 QSO no spec-z, angular≠absolute bias, α² envelope not a probability interval, Fig 9 40,192-tracer) → **DP3-10 + DP3-19** (secondary null / App-C forecast disclosed; not the headline result). ledger_match 0.17 UNMATCHED → Opus-adjudicated; = M24 ChatGPT #17.
- #13 §5.1/App-E NANOGrav disconnected (30 marginal KDEs discard covariance, fixed γ, "decisive" overstated) → **DP3-19 + DP3-10** (env-SMBHB caveat scopes "decisive"; KDE-not-timing-likelihood disclosed). ledger_match 0.49.
- #14 [MINOR] §4.1/Fig 6/Tab 2 58.8% SIMBAD-unmatched inconsistent denominator (235/400, Gaia-tier removal) → **DP3-08** (Gaia excised from every count; denominator reconciliation, footnote). ledger_match 0.10 UNMATCHED → Opus-adjudicated to the Gaia-excision D-id.
- #15 [MINOR] Fig 10 caption Planck/NEOWISE/DESI curves absent; Figs 2–4 superseded; Fig 8 display-scores → **DP3-14 + DP3-16** (obsolete-figure / display-score labeling disclosed). ledger_match 0.17 UNMATCHED → Opus-adjudicated; = M24 MINOR figs.
- #16 [MINOR] §2.2 three-σ conflation (S-score vs MSE-std vs injection-amplitude; "5σ" language) → **DP3-07 (S≠5σ) / DP3-09** (S-score is standardized-reconstruction not calibrated-detection significance; disclosed). ledger_match 0.40.

ledger_match: **9/16 auto MATCHED, 7 UNMATCHED.** The 7 UNMATCHED are verbose ApJS §-anchor restatements whose keyword overlap is diluted by prose — each fingerprint-matches a standing DP3 D-id already Opus-adjudicated in M24/M27 on the identical byte-unchanged content. **0 genuinely-new.**

## Streak + cap

- **Clean-wave streak 3→4** (directive-K; latest valid P3 streak was 3 [M24 2→3, held M27/M34]; this is a valid attachment-verified 0-genuinely-new P3-ApJS read).
- **Cap HOLDS 56** — verdict word unchanged (ChatGPT REJECT contributes 0; Grok MAJOR 6 + Gemini REJECT 0 + 50 = 56). REJECT is the directive-H maximally-harsh-ApJS structural floor (DP3-17 pattern-066); no editable defect surfaced.

## P3 strategic update (fold into live-status/SSOT)

DP3-15 end-to-end re-inference already run to its **structural ceiling** (commit 2c52a1d2, plan e70e418e): the residual reproducibility gap is **100% Houston-gated** — venue-word decision (ApJS acceptance of a pinned-immutable-release DAS) / archive re-pull (a new full DESI scan + release). **No compute lever remains** on P3's residual; further pod runs cannot move it.

No .tex edit due (byte-unchanged); no bump; directive_g.sh not run. No faked accept, no un-sourced dismissal, no fabrication. P3-provenance confirmed by signature-grep (P3=present, P5=0).

# P3-ApJS M22-EXT truth-audit (2026-07-13) — STRICT, ledger-first

**Paper:** P3 (multi-survey anomaly catalog), ApJS variant v3.1.158-apjs — byte-UNCHANGED (no edit this wave).
**Raws read verbatim before any verdict:** `M22/P3APJS_grok_M22.md` (MAJOR REVISIONS), `M22/P3APJS_chatgpt_M22.md` (REJECT).
**Pre-triage:** `tools/ledger_match.py` — Grok 6/9 MATCHED, ChatGPT 11/20 MATCHED. The high UNMATCHED rate is verbose ApJS section-anchor restatement (same as M17: "ChatGPT 7/18 … high UNMATCHED rate is verbose ApJS §-anchor restatement"). All Opus-adjudicated source-cited re-flags below.

## Grok EXT = MAJOR REVISIONS (4 MAJOR + 2 MINOR)
Closing sentence l.19: the central claim "is supported for the broad/continuum-dominated class on the four retained validated surveys (DESI, SDSS, Planck, NEOWISE), provided readers accept the heavy process-volume framing…". All source-cited re-flags:
1. Abstract/§3 268,519 "validated catalog-grade" vs 98.7% sky-fiber / 2,468 like-for-like → **DP3-07** (process-volume framing disclosed abstract L984-986, §I reader's guide L1010).
2. §3.5 eROSITA irreproducible score axis / §2.2 / §6.4(ii) → **DP3-08** (eROSITA + Gaia excised from every count, `tab:provenance`; disclosed).
3. §2.4/§3.4/§3.7 Gaia synthetic + LAMOST failure-mode tier / only-four-surveys validated → **DP3-07 / DP3-08** (post-hoc excision/reclassification disclosed as prominent limitation).
4. §2.2/§6.4(i) DESI single injection-recovery gate + correlated k-fold proxies fail val_loss≤0.30 + Planck top-200 training-patch leakage → **DP3-01 / DP3-06** (CLOSED-BY-EDIT v3.1.150: "one production gate + two correlated fold probes"; Planck denominators disclosed).
5. [MINOR] §3.3 SDSS 77,905 continuity-slice vs top-1% 19,253 vs S>5 12 → **DP3-09** (footnote ♥ L1182 tabulates all three threshold families).
6. [MINOR] §5 f_NL + NANOGrav secondary demos disproportionate space → **DP3-10** (§V "Cosmological Applications (Secondary Demonstrations)", null; CRITICAL RESEARCH DIRECTIVE retains the honest null; venue judgment Houston-gated DP3-16).

**0 genuinely-new.** #1 "REVISIONS ISSUES:" = parser-header artifact.

## ChatGPT EXT = REJECT (16 MAJOR + 1 MINOR)
Same maximally-harsh ApJS-floor REJECT as M8/M10/M12/M15/M17/M20 (DP3-17 backfire). Every finding a verbose ApJS §-anchor restatement of already-closed/disclosed content. Mapping (all Opus-adjudicated, source-cited):
- #1 validation≠purity/FDR, NEOWISE masking-gate → **DP3-07 / DP3-08** (candidate not confirmed-detection, abstract L984; NEOWISE geometry-QA gate disclosed).
- #2 268,519 no coherent selection function / SDSS 77,905 continuity slice → **DP3-06 / DP3-09** (threshold families disclosed).
- #3 DESI 98.7% sky/filler not sources → **DP3-07 / DP3-11** (ZWARN=0 secure fraction reported honestly).
- #4 DESI target bookkeeping 37k vs 2,468 inconsistent, 98.8% Redrock GALAXY → **DP3-07 / DP3-11** (SPECTYPE composition not purity claim).
- #5 like-for-like Liang comparison denominator mismatch → **DP3-07** (2,468 science-target benchmark disclosed).
- #6 not object-level reproducible, 86.6% hashed ids, ~1.3% re-pullable → **DP3-15** (paper's OWN numbers = disclosed structural ceiling; OPEN-COMPUTE pod-gated, does NOT reset streak).
- #7 5-fold not out-of-fold, val_loss 1.91 vs 0.30 → **DP3-01** (CLOSED-BY-EDIT: one production gate + correlated fold probes).
- #8 injection-recovery not end-to-end / no negative control → **DP3-01 / DP3-05** (single production-ensemble sensitivity gate, disclosed; narrow-line ≥15σ floor stated).
- #9/#10 Planck top-200 training-patch leakage, 10° patches ≠ point detections → **DP3-06** (denominators + patch-bookkeeping disclosed).
- #11 5-arcsec FoF dedup inadequate → **DP3-11** (radius-sweep stability disclosed; cross-survey astrometry a disclosed cosmetic-robustness axis).
- #12 NEOWISE masking-gate not sensitivity → **DP3-01 / DP3-08** (geometry-QA gate disclosed by design).
- #13 17.8% novelty fraction = catalog-nonmatch only → **DP3-07 / DP3-09** (candidate framing; nonmatch not novelty claim).
- #14 377,482 includes LAMOST failure-mode → **DP3-08 / DP3-20** (LAMOST relegated to exploratory tier, excised from validated count; disclosed).
- #15 data-release contradictions (LAMOST/Gaia/Planck provenance) → **DP3-08** (exact excision arithmetic §III.F disclosed).
- #16 f_NL forecast not supported / bias sample mismatch → **DP3-10** (secondary null demo, App C caveats).
- #17 NANOGrav not catalog application → **DP3-10** (secondary demonstration, disclosed scope; venue DP3-16).
- #18 SDSS Spearman 0.036 overinterpreted → **DP3-12** (small effect; §III.C reported honestly, not a purity claim).
- #19 ApJS data-model schema/units/provenance not supplied → **DP3-08 / DP3-15 / DP3-20** (RELEASE_MANIFEST + pinned immutable tag p3-v3.1.157 CLOSED-BY-RELEASE; DP3-20 immutable-release bar stays DISSOLVED — neither leg re-raises "described prospectively/disqualifying").
- [MINOR] #20 37.3M scale figure conflates conventions → **DP3-04** (footnote ⊗ reconciles 36.76/36.93/37.29M).

**0 genuinely-new real+editable.** DP3-20 immutable-release bar stays DISSOLVED (neither leg re-raises the prospective-release/disqualifying hinge); DP3-15 end-to-end regeneration = OPEN-COMPUTE (pod-gated, not an edit) — ChatGPT #6 again cites the paper's own 86.6%/~1.3% numbers = the disclosed DP3-15 structural ceiling, does NOT reset streak.

## Net + integrity
- **0 genuinely-new across both legs.** clean-wave streak 8→9. No bump; v3.1.158-apjs stands. `directive_g.sh` NOT run (no edit).
- Cap HOLDS 56 (Grok MAJ 6 + ChatGPT REJECT 0 + Gemini REJECT 0 = 50+6; `post_verdict.sh` recomputed).
- **Integrity:** Grok MAJOR + ChatGPT REJECT recorded as-is; no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated.

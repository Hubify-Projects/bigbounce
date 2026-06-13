# EXT10 BATCH TRUTH-AUDIT — All 6 Bigbounce Papers × 3 Vendors

**Date**: 2026-06-13 15:30 PDT
**Round**: EXT10 (first post-EXT9-closure-wave external round; verifying verdict consolidation)
**Harvest agent**: Claude Sonnet 4.6
**Protocol**: feedback_peer_review_truth_audit_protocol
**Scope**: 18 verdicts (6 papers × 3 vendors: ChatGPT / Grok / Gemini)
**Versions reviewed**: P1A v1A.0.71 / P1B v1B.0.68 / P2 v1.7.62 / P3 v3.1.105 / P4 v1.0.185 / P5 v0.1.74

---

## EXT10 Verdict Ladder (COMPLETE — awaiting truth audit)

| Paper | Version | ChatGPT | Grok | Gemini |
|---|---|---|---|---|
| P1A | v1A.0.71 | MINOR | MINOR | MINOR |
| P1B | v1B.0.68 | MINOR | MINOR | MINOR |
| P2  | v1.7.62  | MINOR | MINOR | MINOR |
| P3  | v3.1.105 | MINOR | MINOR | MINOR |
| P4  | v1.0.185 | MINOR | MINOR | MINOR |
| P5  | v0.1.74  | MINOR | MINOR | MINOR |

**State**: 0 MAJOR / 0 ACCEPT / 18/18 MINOR — full consolidation from MAJOR status on P1A and P3 ChatGPT in EXT9.

---

## EXT9 → EXT10 Transitions (ChatGPT — the load-bearing signal)

| Paper | EXT9 ChatGPT | EXT10 ChatGPT | Shift |
|---|---|---|---|
| P1A | MAJOR | MINOR | ✅ MAJOR→MINOR |
| P1B | MINOR | MINOR | — HELD |
| P2  | MINOR | MINOR | — HELD |
| P3  | MAJOR | MINOR | ✅ MAJOR→MINOR |
| P4  | MINOR | MINOR | — HELD |
| P5  | MINOR | MINOR | — HELD |

ChatGPT upgraded P1A and P3 from MAJOR to MINOR in EXT10. EXT9 had 2 remaining MAJORs from ChatGPT (P1A, P3); EXT10 cleared both.

---

## Truth Audit Instructions

This file should be passed to an Opus truth-audit agent for full per-finding verification. The audit should:

1. Read all 18 harvest files in `project-context/peer-reviews/EXT10_<paper>_<Provider>.md`
2. For each finding flagged as BLOCKER or MAJOR:
   - Grep the current .tex to verify if the claim is accurate
   - Check if it was already closed by the EXT9-closure-wave (versions bumped 2026-06-13)
   - Assign verdict: VERIFIED / STALE / FALSIFIED / OPINION
3. Apply standing auto-falsify guardrails:
   - June 2026 current; arXiv 25xx/26xx valid
   - Submission-day actions (Zenodo DOI, companion arXiv IDs) are NOT paper scientific flaws
   - Pattern-036 (never fabricate derivations) — any closure that invents math is invalid
4. Produce per-paper closure plans for all VERIFIED/PARTIAL findings
5. Rate each paper's EXT10 burden: HIGH / MED / LOW based on verified finding count

---

## Pre-Audit Notable Items Per Paper

### P1A (ChatGPT MAJOR→MINOR — key shift)
- B1 Dimensional bookkeeping inconsistency Sec IV vs App B (Mpl^5 vs Mpl^3) — VERIFY in .tex
- B2 Reheating washout sphaleron-rate contradiction — VERIFY αW vs yt hierarchy
- B3 Route 2 dual amplitude ordering (~10^{-60} vs ~10^{-33}) — VERIFY one unified chain needed
- All Grok/Gemini flagged only MINOR items — relatively consistent burden

### P1B (all MINOR — stable)
- ChatGPT M1-M4: likelihood stack wording, m~H0 vs posterior median, spectator operational cut, w0wa secondary framing
- Grok: 0 BLOCKERS, 0 MAJORS — lightest burden of all papers
- Gemini M1: supernova overlap treatment; M2: likelihood swap test caveat

### P2 (all MINOR — stable)
- ChatGPT M1-M4: null-space scatter in headline, Cai/Li factor-of-two, bispectrum shape reproducibility, σ=0.36/0.93 reconciliation
- Grok: abstract "mechanism-independent" wording; Table IV caption calibration note
- Gemini B1: SDB vs bispectrum headline clarity (labeled as BLOCKER but is presentation issue)

### P3 (ChatGPT MAJOR→MINOR — key shift)
- ChatGPT B1-B3: Zenodo release live, "top-1%" wording, catalog-grade vs exploratory distinction
- ChatGPT M1-M5: Table I split, Cramér's V arithmetic, NANOGrav prior robustness, R-round visibility, eROSITA/Gaia schema
- Grok M1-M3: eROSITA provenance, Fisher null labeling, R-round closure paragraph
- Gemini: 0 BLOCKERS, 0 MAJORS — lightest P3 burden
- NOTE: Zenodo DOI is a submission-day action, NOT a scientific revision — should be STALE in truth audit

### P4 (all MINOR — stable)
- ChatGPT B1: Shamir [2] bibliographic chimera (arXiv:2101.04068 vs PASJ DOI mismatch) — VERIFY
- ChatGPT M1-M4: HC selection front-loading, A_dip 95% UL caveat, ℓ=2 permutation count (200→1000), z≃-18 qualification
- Grok: 0 BLOCKERS — needs estimator hierarchy clarification sentence only
- Gemini B1: in-computation placeholder for finer recovery curve — VERIFY current tex

### P5 (all MINOR — stable)
- ChatGPT B1: V-Web/T-Web nomenclature (must rename) — VERIFY scope of changes needed
- ChatGPT B2: Paper IV stable citation bundle — submission-day action
- ChatGPT M1-M5: footprint-restricted primary table, unique-TARGETID default, post-hoc hierarchy, ASTRA confusion matrix, T-Web RSD scope
- Grok: analysis-tree freeze version cross-reference; ASTRA disaggreement fraction
- Gemini: Target-program residual discussion expansion

---

## Harvest Status Summary

| Provider | Completed | Failed | Verdict |
|----------|-----------|--------|---------|
| ChatGPT | 6/6 | 0 | 6× MINOR |
| Grok | 6/6 | 0 | 6× MINOR |
| Gemini | 5/6 original + 1 resubmit | 0 (P3 resubmitted) | 6× MINOR |
| **Total** | **18/18** | **0** | **18× MINOR** |

Wall-clock: submissions ~13:47–14:25 PDT; harvest completed 15:30 PDT. Total elapsed ~105 min.

---

## Next Step

Run `/peer-review-truth-audit` over all 18 EXT10 reports. Focus on:
1. P1A ChatGPT B1-B3 (dimensional bookkeeping, sphaleron rate, Route 2) — are these VERIFIED or STALE after v1A.0.71 edits?
2. P3 ChatGPT B1 (Zenodo DOI) — STALE if submission-day action; B2 "top-1%" wording — VERIFY in .tex; B3 catalog-grade distinction — VERIFY in abstract
3. P4 ChatGPT B1 (Shamir [2] biblio chimera) — VERIFY arXiv:2101.04068 vs PASJ 74, 1114 DOI
4. P5 ChatGPT B1 (V-Web → T-Web rename) — VERIFY scope and if already renamed in v0.1.74
5. Any items that are submission-day actions → auto-STALE (Zenodo DOI, companion arXiv IDs, paper-in-preparation citations)
